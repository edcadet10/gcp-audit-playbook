"""Title: Run a scoped Google Cloud audit evidence procedure.
Description: Prepare tooling, authenticate, verify scope, execute fixed reads and create hashed workpapers.
References: https://docs.cloud.google.com/sdk/docs/authenticate
https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-ancestors
https://docs.cloud.google.com/asset-inventory/docs/asset-types
"""
import argparse, csv, datetime as dt, hashlib, json, pathlib, re, subprocess, sys, uuid
from bootstrap import ensure_sdk, environment, launcher
from operations import OPERATIONS, READ_VERBS, READ_EXCEPTIONS

ROOT=pathlib.Path(__file__).resolve().parents[1]
UTC=dt.timezone.utc
def now(): return dt.datetime.now(UTC).isoformat()
def save(path,value):
    path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def validate_id(value,pattern,label):
    if not isinstance(value,str) or not re.fullmatch(pattern,value):
        raise ValueError(f'Invalid {label}')
    return value
def validate_scope(scope):
    allowed={'organization','account','projects','organization_reads','billing_accounts','regions','locations','constraints','start','end','log_limit','scc_locations'}
    if set(scope)-allowed: raise ValueError('Unknown scope fields; commands, endpoints and flags cannot be supplied in scope')
    validate_id(scope.get('organization'),r'[1-9][0-9]{2,24}','organization')
    validate_id(scope.get('account'),r'[A-Za-z0-9_.+@-]{3,254}','account')
    projects=scope.get('projects')
    if not isinstance(projects,list) or not projects or len(set(projects))!=len(projects): raise ValueError('Provide unique approved project IDs')
    for p in projects: validate_id(p,r'[a-z][a-z0-9-]{4,28}[a-z0-9]','project ID')
    if type(scope.get('organization_reads',False)) is not bool: raise ValueError('organization_reads must be boolean')
    for field,pattern in [('billing_accounts',r'[A-Fa-f0-9]{6}-[A-Fa-f0-9]{6}-[A-Fa-f0-9]{6}'),('regions',r'[a-z][a-z0-9-]{1,50}'),('locations',r'[a-z][a-z0-9-]{1,50}'),('scc_locations',r'[a-z][a-z0-9-]{1,50}'),('constraints',r'[a-zA-Z][a-zA-Z0-9_.]{1,180}')]:
        values=scope.get(field,[])
        if not isinstance(values,list) or len(values)!=len(set(values)): raise ValueError(f'{field} must be a unique list')
        for v in values: validate_id(v,pattern,field)
    for field in ['start','end']:
        validate_id(scope.get(field),r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ',field)
    start,end=[dt.datetime.fromisoformat(scope[k].replace('Z','+00:00')) for k in ['start','end']]
    if start>=end or end>dt.datetime.now(UTC): raise ValueError('Use an ordered historical UTC window')
    limit=scope.get('log_limit',1000)
    if type(limit) is not int or not 1<=limit<=10000: raise ValueError('log_limit must be between 1 and 10000')
    return scope

class ReadError(Exception): pass
class ScopeError(Exception): pass

class CLI:
    def __init__(self,account):
        self.account=account
        self.root=ensure_sdk()
        self.launch=launcher(self.root)
        self.env=environment(account)
    def call(self,args,interactive=False):
        flags=[] if interactive else ['--format=json','--verbosity=warning','--quiet']
        call_env=dict(self.env)
        if interactive:
            # Authentication may need a verification-code prompt; cloud reads stay noninteractive.
            call_env['CLOUDSDK_CORE_DISABLE_PROMPTS']='0'
        try:
            proc=subprocess.run(self.launch+list(args)+flags,env=call_env,shell=False,
                capture_output=not interactive,text=True,encoding='utf-8',errors='replace',timeout=900)
        except subprocess.TimeoutExpired as exc: raise ReadError('CLI command timed out; completeness is unknown') from exc
        if proc.returncode: raise ReadError((proc.stderr or 'Interactive authentication failed')[:6000])
        if interactive: return {}
        try: data=json.loads(proc.stdout)
        except (ValueError,TypeError) as exc: raise ReadError('CLI returned invalid JSON; output is not complete evidence') from exc
        return {'data':data,'warning':(proc.stderr or '').strip()[:6000]}
    def prepare(self):
        # Inspect the dedicated config before any cloud command or interactive login.
        cfg=self.call(['config','list','--all'])['data']
        auth=cfg.get('auth',{})
        if any(auth.get(k) for k in ['impersonate_service_account','access_token_file','credential_file_override']) or auth.get('disable_credentials') in [True,'True','true']:
            raise ScopeError('Credential override or impersonation found in dedicated CLI configuration')
        if any(v for v in cfg.get('api_endpoint_overrides',{}).values()):
            raise ScopeError('Custom API endpoints are outside this collector scope')
        identities=self.call(['auth','list'])['data']
        if self.account not in [i.get('account') for i in identities]:
            self.call(['auth','login',self.account,'--no-launch-browser'],interactive=True)
            identities=self.call(['auth','list'])['data']
        if self.account not in [i.get('account') for i in identities]: raise ScopeError('Expected account was not authenticated')
        return self.call(['version'])['data']
    def read(self,args):
        return self.call([*args,'--account='+self.account])

class Collector:
    def __init__(self,scope,cli,out):
        self.scope=validate_scope(scope)
        self.cli=cli
        self.out=pathlib.Path(out)
        self.records=[]
        self.cache={}
        self.folders=set()
        self.numbers={}
        self.candidates=[]
    def record(self,op,target,status,data=None,error=None,command=None):
        row=dict(sequence=len(self.records)+1,operation=op,target=target,status=status,collected=now(),command=command,error=error)
        if data is not None:
            filename=f'{row["sequence"]:04}-{op}.json'
            save(self.out/filename,data)
            row.update(file=filename,sha256=hashlib.sha256((self.out/filename).read_bytes()).hexdigest(),count=len(data) if isinstance(data,list) else 1)
        self.records.append(row)
        return row
    def verify_projects(self):
        # All projects are checked before any workload read; a mismatch aborts the entire run.
        for project in self.scope['projects']:
            result=self.cli.read(['projects','get-ancestors',project])
            ancestors=result['data']
            if result.get('warning') or not isinstance(ancestors,list): raise ScopeError('Unreliable project ancestry response')
            orgs=[str(x.get('id')) for x in ancestors if x.get('type')=='organization']
            if orgs != [self.scope['organization']]: raise ScopeError('Project ancestry does not match approved organization')
            folders=[str(x.get('id')) for x in ancestors if x.get('type')=='folder']
            for folder in folders: validate_id(folder,r'[1-9][0-9]{0,24}','ancestor folder')
            self.folders.update(folders)
            identity=self.cli.read(['projects','describe',project])
            if identity.get('warning') or identity['data'].get('projectId')!=project: raise ScopeError('Project identity mismatch')
            self.numbers[project]=validate_id(str(identity['data']['projectNumber']),r'[1-9][0-9]{0,24}','project number')
            self.record('preflight_ancestry',project,'Collected',ancestors,command=['projects','get-ancestors',project])
            self.record('preflight_project',project,'Collected',identity['data'],command=['projects','describe',project])
    def execute(self,key,context,args):
        op=OPERATIONS[key]
        path=tuple(op['command'])
        if path[-1] not in READ_VERBS and path not in READ_EXCEPTIONS: raise ScopeError('Non-read operation rejected')
        if args[:len(path)]!=list(path): raise ScopeError('Command prefix mismatch')
        # Generated arguments only; no user-supplied flags-file, destinations, tokens or URLs.
        if any(a.startswith(('--flags-file','--impersonate','--access-token','--destination','--log-http')) for a in args): raise ScopeError('Forbidden flag')
        target=json.dumps(context,sort_keys=True)
        try:
            response=self.cli.read(args)
            data=response['data']
            if not isinstance(data,(dict,list)): raise ReadError('Unexpected JSON result shape')
            cap=self.scope.get('log_limit',1000) if key=='audit_logs' else 100 if key=='builds' else None
            status='Truncated' if cap and isinstance(data,list) and len(data)>=cap else 'Sampled' if cap else 'NeedsReview' if response.get('warning') else 'Collected'
            self.record(key,context,status,data,response.get('warning'),args)
            if key=='asset_iam': self.find_candidates(data,context)
            return data
        except ReadError as exc:
            self.record(key,context,'Incomplete',error=str(exc),command=args)
            return None
    def project_read(self,key,project):
        ck=(key,project)
        if ck not in self.cache:
            op=OPERATIONS[key]
            args=[*op['command'],*op['flags']]
            if key in ['project','project_iam','billing_link']: args.append(project)
            if key=='asset_iam': args.append('--scope=projects/'+project)
            args.append('--project='+project)
            self.cache[ck]=self.execute(key,{'project':project},args)
        return self.cache[ck]
    def run_operation(self,key):
        if key not in OPERATIONS: raise ScopeError('Unregistered operation')
        op=OPERATIONS[key]
        kind=op['scope']
        base=[*op['command'],*op['flags']]
        s=self.scope
        if kind in ['organization','folder','access_policy','scc'] and not s.get('organization_reads',False):
            self.record(key,'organization','NotAuthorized',error='organization_reads is false'); return
        if kind=='organization':
            args=base+([s['organization']] if key=='org_iam' else ['--organization='+s['organization']])
            self.execute(key,{'organization':s['organization']},args); return
        if kind=='folder':
            if not self.folders: self.record(key,'ancestor folders','NoTargets',error='Verified projects have no folder ancestors')
            for folder in sorted(self.folders): self.execute(key,{'folder':folder},base+[folder])
            return
        if kind=='billing':
            accounts=s.get('billing_accounts',[])
            if not accounts: self.record(key,'billing accounts','MissingInput',error='No independently approved billing account IDs')
            for account in accounts: self.execute(key,{'billing_account':account},base+['--billing-account='+account])
            return
        if kind=='scc':
            locations=s.get('scc_locations',[])
            if not locations: self.record(key,'SCC location','MissingInput',error='Supply all approved SCC locations')
            for location in locations: self.execute(key,{'organization':s['organization'],'location':location},base+['--organization='+s['organization'],'--location='+location])
            return
        if kind=='access_policy':
            policies=self.execute('access_policies',{'organization':s['organization']},OPERATIONS['access_policies']['command']+['--organization='+s['organization']])
            if not policies:
                self.record(key,'access policies','NoTargets' if policies==[] else 'DependencyFailed',error='Reconcile access-policy population'); return
            for policy in policies:
                name=validate_id(policy.get('name'),r'accessPolicies/[1-9][0-9]{0,24}','access policy')
                if policy.get('parent')!='organizations/'+s['organization']: raise ScopeError('Access policy parent mismatch')
                self.execute(key,{'policy':name},base+['--policy='+name.split('/')[-1]])
            return
        for project in s['projects']:
            args=base+['--project='+project]
            if kind=='project': self.project_read(key,project)
            elif kind in ['region','location','constraint']:
                field={'region':'regions','location':'locations','constraint':'constraints'}[kind]
                values=s.get(field,[])
                if not values: self.record(key,project,'MissingInput',error=f'No approved {field}; regional absence is not service absence')
                for value in values:
                    extra=[value] if kind=='constraint' else ['--'+kind+'='+value]
                    self.execute(key,{'project':project,kind:value},args+extra)
            elif kind=='logs':
                query=f'logName:"cloudaudit.googleapis.com" AND timestamp>="{s["start"]}" AND timestamp<"{s["end"]}"'
                self.execute(key,{'project':project,'start':s['start'],'end':s['end']},args+[query,'--limit='+str(s.get('log_limit',1000)),'--order=asc'])
            elif kind in ['service_account','pool','secret','sql_instance']:
                dependency={'service_account':'service_accounts','pool':'wif_pools','secret':'secrets','sql_instance':'sql'}[kind]
                rows=self.project_read(dependency,project)
                if not rows:
                    self.record(key,project,'NoTargets' if rows==[] else 'DependencyFailed',error=f'Reconcile {dependency} population'); continue
                if not isinstance(rows,list): raise ScopeError('Unexpected parent enumeration')
                for row in rows:
                    name=row.get('name','')
                    if kind=='service_account':
                        validate_id(name,r'projects/[^/]+/serviceAccounts/[^/]+','service account resource')
                        if name.split('/')[1] not in [project,self.numbers[project]]: raise ScopeError('Service account parent mismatch')
                        value=validate_id(row.get('email'),r'[A-Za-z0-9_.+@-]{3,254}','service account email')
                        extra=['--iam-account='+value]
                    elif kind=='pool':
                        pattern=r'projects/'+self.numbers[project]+r'/locations/global/workloadIdentityPools/([a-zA-Z0-9_-]+)'
                        match=re.fullmatch(pattern,name)
                        if not match: raise ScopeError('Workload pool parent mismatch')
                        extra=['--workload-identity-pool='+match.group(1)]
                    elif kind=='secret':
                        match=re.fullmatch(r'projects/('+re.escape(project)+'|'+self.numbers[project]+r')/secrets/([a-zA-Z0-9_-]+)',name)
                        if not match: raise ScopeError('Secret parent mismatch')
                        extra=[match.group(2)]
                    else:
                        if row.get('project')!=project: raise ScopeError('SQL instance parent mismatch')
                        extra=['--instance='+validate_id(name,r'[a-z][a-z0-9-]{0,97}','SQL instance')]
                    self.execute(key,{'project':project,'resource':name},args+extra)
            elif kind=='keyring':
                locations=s.get('locations',[])
                if not locations: self.record(key,project,'MissingInput',error='No approved KMS locations')
                for location in locations:
                    rings=self.execute('keyrings',{'project':project,'location':location},OPERATIONS['keyrings']['command']+['--project='+project,'--location='+location])
                    if not rings:
                        self.record(key,{'project':project,'location':location},'NoTargets' if rings==[] else 'DependencyFailed',error='Reconcile key ring population'); continue
                    for ring in rings:
                        name=ring.get('name','')
                        match=re.fullmatch(r'projects/('+re.escape(project)+'|'+self.numbers[project]+')/locations/'+re.escape(location)+r'/keyRings/([A-Za-z0-9_-]+)',name)
                        if not match: raise ScopeError('Key ring parent mismatch')
                        self.execute(key,{'project':project,'keyring':name},args+['--location='+location,'--keyring='+match.group(2)])
            else: raise ScopeError('Unsupported operation scope')
    def find_candidates(self,data,context):
        # Deliberately narrow: candidates require human effective-access analysis.
        for entry in data if isinstance(data,list) else []:
            for binding in entry.get('policy',{}).get('bindings',[]):
                members=binding.get('members',[])
                if binding.get('role') in ['roles/owner','roles/editor'] or any(x in ['allUsers','allAuthenticatedUsers'] for x in members):
                    self.candidates.append(dict(type='IAM review candidate',scope=context,resource=entry.get('resource'),binding=binding,
                        rationale='Review broad/basic or public grant with inheritance, conditions, deny, boundaries and service-specific controls; no automatic finding.'))

def recipes(): return json.loads((ROOT/'scripts/recipes.json').read_text(encoding='utf-8'))
def main(default_id=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--procedure',default=default_id)
    parser.add_argument('--plan',action='store_true',help='Show reads and required evidence without installing, authenticating or connecting')
    parser.add_argument('--scope',type=pathlib.Path)
    parser.add_argument('--output',type=pathlib.Path,help='Private local evidence parent directory outside this repository')
    args=parser.parse_args()
    items=recipes()
    if args.procedure not in items: parser.error('Choose a procedure ID from scripts/recipes.json')
    recipe=items[args.procedure]
    if args.plan:
        print(json.dumps(dict(procedure=recipe,operations=[OPERATIONS[x] for x in recipe['operations']]),indent=2)); return 0
    if not args.scope or not args.output: parser.error('--scope and --output are required for collection')
    scope=validate_scope(json.loads(args.scope.read_text(encoding='utf-8')))
    parent=args.output.resolve()
    if parent==ROOT or parent.is_relative_to(ROOT): raise ValueError('Evidence must be stored outside the public repository')
    parent.mkdir(parents=True,exist_ok=True)
    out=parent/(dt.datetime.now(UTC).strftime('%Y%m%dT%H%M%SZ')+'-'+args.procedure+'-'+uuid.uuid4().hex[:8])
    out.mkdir()
    save(out/'scope.json',scope)
    save(out/'procedure.json',recipe)
    manifest=dict(procedure=args.procedure,started=now(),assessment='Not assessed',state='Incomplete',records=[])
    collector=None
    try:
        cli=CLI(scope['account'])
        manifest['sdk']=cli.prepare()
        collector=Collector(scope,cli,out)
        collector.verify_projects()
        for key in recipe['operations']: collector.run_operation(key)
        manifest['state']='NeedsReview'
    except (ReadError,ScopeError,ValueError,RuntimeError,OSError,KeyError) as exc:
        manifest['error']=str(exc)
    finally:
        manifest['finished']=now()
        if collector:
            manifest['records']=collector.records
            save(out/'review-candidates.json',collector.candidates)
            if any(r['status'] in ['Incomplete','DependencyFailed','MissingInput','NotAuthorized','Truncated'] for r in collector.records): manifest['state']='Incomplete'
        save(out/'manifest.json',manifest)
        with (out/'evidence-requests.csv').open('w',newline='',encoding='utf-8') as f:
            writer=csv.writer(f); writer.writerow(['procedure','required_evidence','owner','evidence_reference','status','review_notes'])
            for request in recipe['required_evidence']: writer.writerow([args.procedure,request,'','','Missing',''])
        (out/'assessment.md').write_text('# '+recipe['title']+'\n\nStatus: **Not assessed**\n\n'+recipe['procedure']+'\n\n## Required evidence\n\n'+ '\n'.join('- '+x for x in recipe['required_evidence'])+'\n\n## Review\n\nCriterion: '+recipe['criterion']+'\n\nChallenge: '+recipe['falsification']+'\n\nRecord evidence references, sample population, observed facts, contrary explanations, owner response and reviewer conclusion. Missing documents remain evidence gaps.\n',encoding='utf-8')
        hashes=[dict(file=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in sorted(out.iterdir()) if p.is_file()]
        save(out/'SHA256SUMS.json',hashes)
    print(json.dumps({'output':str(out),'collection_state':manifest['state'],'assessment':'Not assessed'},indent=2))
    return 2 if manifest['state']=='Incomplete' else 0

if __name__=='__main__':
    try: sys.exit(main())
    except (ValueError,OSError) as exc:
        print(str(exc),file=sys.stderr); sys.exit(2)
