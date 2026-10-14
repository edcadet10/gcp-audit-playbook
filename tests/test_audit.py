"""Title: Disconfirm the read-only collector's safety and evidence claims.
Description: Deterministic offline tests; no authentication, SDK installation or cloud calls.
References: https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-ancestors
https://docs.cloud.google.com/logging/docs/audit
"""
import copy, datetime, importlib, io, json, os, pathlib, subprocess, sys, tempfile, unittest, zipfile
from unittest.mock import patch
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import audit, bootstrap, index_workpapers
from operations import OPERATIONS

SCOPE=dict(organization='123456789012',account='audit@example.com',projects=['example-prod-123'],organization_reads=True,
    billing_accounts=[],regions=['us-central1'],locations=['global'],scc_locations=['global'],constraints=['storage.publicAccessPrevention'],
    start='2026-01-01T00:00:00Z',end='2026-02-01T00:00:00Z',log_limit=2)

class FakeCLI:
    def __init__(self,overrides=None): self.calls=[]; self.overrides=overrides or {}
    def read(self,args):
        self.calls.append(args)
        for prefix,result in self.overrides.items():
            if args[:len(prefix)]==list(prefix):
                if isinstance(result,Exception): raise result
                return {'data':copy.deepcopy(result),'warning':''}
        if args[:2]==['projects','get-ancestors']:
            return dict(data=[{'type':'project','id':'333333333333'},{'type':'folder','id':'222222222222'},{'type':'organization','id':'123456789012'}],warning='')
        if args[:2]==['projects','describe']:
            return dict(data={'projectId':args[2],'projectNumber':'333333333333'},warning='')
        return {'data':[],'warning':''}

class AuditTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.out=pathlib.Path(self.temp.name); self.scope=copy.deepcopy(SCOPE)
    def tearDown(self): self.temp.cleanup()
    def collector(self,overrides=None): return audit.Collector(self.scope,FakeCLI(overrides),self.out)
    def test_scope_rejects_command_injection(self):
        self.scope['projects']=['example-prod-123;whoami']
        with self.assertRaises(ValueError): audit.validate_scope(self.scope)
    def test_scope_rejects_account_metacharacters(self):
        self.scope['account']='audit@example.com&whoami'
        with self.assertRaises(ValueError): audit.validate_scope(self.scope)
    def test_scope_rejects_arbitrary_flags_and_endpoints(self):
        self.scope['flags']=['--flags-file=x']
        with self.assertRaises(ValueError): audit.validate_scope(self.scope)
    def test_scope_rejects_future_or_reversed_window(self):
        self.scope['end']='2025-01-01T00:00:00Z'
        with self.assertRaises(ValueError): audit.validate_scope(self.scope)
    def test_scope_rejects_invalid_calendar_date(self):
        self.scope['start']='2026-02-31T00:00:00Z'
        with self.assertRaises(ValueError): audit.validate_scope(self.scope)
    def test_wrong_organization_stops_before_workload_reads(self):
        c=self.collector({('projects','get-ancestors'):[{'type':'organization','id':'999999999999'}]})
        with self.assertRaises(audit.ScopeError): c.verify_projects()
        self.assertEqual(len(c.cli.calls),1)
    def test_project_identity_mismatch_stops(self):
        c=self.collector({('projects','describe'):{'projectId':'other-project','projectNumber':'444'}})
        with self.assertRaises(audit.ScopeError): c.verify_projects()
    def test_verified_ancestors_drive_folder_scope(self):
        c=self.collector(); c.verify_projects(); c.run_operation('folder_iam')
        self.assertEqual(c.cli.calls[-1],['resource-manager','folders','get-iam-policy','222222222222'])
    def test_write_verb_rejected_before_dispatch(self):
        c=self.collector()
        with patch.dict(OPERATIONS,{'evil':dict(OPERATIONS['instances'],command=['compute','instances','delete'])}):
            with self.assertRaises(audit.ScopeError): c.execute('evil',{},['compute','instances','delete'])
        self.assertEqual(c.cli.calls,[])
    def test_command_prefix_mismatch_rejected(self):
        c=self.collector()
        with self.assertRaises(audit.ScopeError): c.execute('instances',{},['projects','delete','example-prod-123'])
        self.assertEqual(c.cli.calls,[])
    def test_forbidden_flag_rejected(self):
        c=self.collector()
        with self.assertRaises(audit.ScopeError): c.execute('instances',{},['compute','instances','list','--flags-file=evil'])
    def test_org_reads_require_explicit_scope(self):
        self.scope['organization_reads']=False; c=self.collector(); c.run_operation('org_assets')
        self.assertEqual(c.records[-1]['status'],'NotAuthorized'); self.assertEqual(c.cli.calls,[])
    def test_billing_requires_independent_scope(self):
        c=self.collector(); c.run_operation('budgets')
        self.assertEqual(c.records[-1]['status'],'MissingInput'); self.assertEqual(c.cli.calls,[])
    def test_missing_regions_not_empty_service_population(self):
        self.scope['regions']=[]; c=self.collector(); c.run_operation('run_services')
        self.assertEqual(c.records[-1]['status'],'MissingInput')
    def test_permission_denied_not_empty_success(self):
        c=self.collector({('compute','instances','list'):audit.ReadError('PERMISSION_DENIED')}); c.run_operation('instances')
        self.assertEqual(c.records[-1]['status'],'Incomplete'); self.assertNotIn('file',c.records[-1])
    def test_empty_success_is_not_control_pass(self):
        c=self.collector(); c.run_operation('instances')
        self.assertEqual(c.records[-1]['status'],'Collected'); self.assertEqual(c.records[-1]['count'],0)
        self.assertNotIn('assessment',c.records[-1])
    def test_log_cap_is_truncated(self):
        c=self.collector({('logging','read'):[{'id':'a'},{'id':'b'}]}); c.run_operation('audit_logs')
        self.assertEqual(c.records[-1]['status'],'Truncated')
        self.assertTrue(any('timestamp>=' in a and 'timestamp<' in a for a in c.cli.calls[-1]))
    def test_below_cap_remains_sampled(self):
        c=self.collector({('logging','read'):[{'id':'a'}]}); c.run_operation('audit_logs')
        self.assertEqual(c.records[-1]['status'],'Sampled')
    def test_failed_parent_never_becomes_no_targets(self):
        c=self.collector({('iam','service-accounts','list'):audit.ReadError('disabled API')}); c.run_operation('sa_keys')
        self.assertEqual(c.records[-1]['status'],'DependencyFailed')
        self.assertEqual(len(c.cli.calls),1)
    def test_child_parent_mismatch_stops(self):
        c=self.collector({('iam','service-accounts','list'):[{'name':'projects/other-project/serviceAccounts/x','email':'sa@example.com'}]})
        c.numbers={'example-prod-123':'333333333333'}
        with self.assertRaises(audit.ScopeError): c.run_operation('sa_keys')
        self.assertEqual(len(c.cli.calls),1)
    def test_candidates_never_assert_exposure(self):
        c=self.collector(); c.find_candidates([{'resource':'x','policy':{'bindings':[{'role':'roles/viewer','members':['allUsers']}]}}],{})
        self.assertEqual(len(c.candidates),1); self.assertNotIn('severity',c.candidates[0]); self.assertIn('no automatic finding',c.candidates[0]['rationale'])
    def test_every_operation_has_read_semantics_and_google_reference(self):
        for op in OPERATIONS.values():
            self.assertTrue(op['command'][-1] in audit.READ_VERBS or tuple(op['command']) in audit.READ_EXCEPTIONS,op['id'])
            self.assertTrue(op['source'].startswith('https://docs.cloud.google.com/sdk/gcloud/reference/'))
    def test_malformed_json_is_read_error(self):
        cli=audit.CLI.__new__(audit.CLI); cli.launch=['mock']; cli.env={}
        with patch('subprocess.run',return_value=subprocess.CompletedProcess([],0,'not json','')):
            with self.assertRaises(audit.ReadError): cli.call(['compute','instances','list'])
    def test_nonzero_exit_is_read_error(self):
        cli=audit.CLI.__new__(audit.CLI); cli.launch=['mock']; cli.env={}
        with patch('subprocess.run',return_value=subprocess.CompletedProcess([],1,'[]','Denied')):
            with self.assertRaises(audit.ReadError): cli.call(['compute','instances','list'])
    def test_timeout_is_incomplete(self):
        cli=audit.CLI.__new__(audit.CLI); cli.launch=['mock']; cli.env={}
        with patch('subprocess.run',side_effect=subprocess.TimeoutExpired('mock',900)):
            with self.assertRaises(audit.ReadError): cli.call(['compute','instances','list'])
    def test_config_override_rejected_before_authentication(self):
        cli=audit.CLI.__new__(audit.CLI); cli.account='audit@example.com'; calls=[]
        def call(args,interactive=False): calls.append(args); return {'data':{'auth':{'impersonate_service_account':'bad@example.com'}}}
        cli.call=call
        with self.assertRaises(audit.ScopeError): cli.prepare()
        self.assertEqual(calls,[['config','list','--all']])
    def test_authentication_must_produce_expected_account(self):
        cli=audit.CLI.__new__(audit.CLI); cli.account='audit@example.com'; calls=[]
        def call(args,interactive=False):
            calls.append(args)
            return {'data':{} if args[0]=='config' else [{'account':'wrong@example.com'}]}
        cli.call=call
        with self.assertRaises(audit.ScopeError): cli.prepare()
        self.assertEqual(calls[2],['auth','login','audit@example.com','--no-launch-browser'])
        self.assertFalse(any(c[0]=='projects' for c in calls))
    def test_setup_precedes_authentication(self):
        order=[]
        with patch.object(audit,'ensure_sdk',side_effect=lambda:order.append('install-check') or self.out), patch.object(audit,'environment',return_value={}),patch.object(audit,'launcher',return_value=['fake']):
            cli=audit.CLI('audit@example.com')
        self.assertEqual(order,['install-check'])
        self.assertEqual(cli.launch,['fake'])
    def test_interactive_login_can_prompt_but_cannot_enable_apis(self):
        cli=audit.CLI.__new__(audit.CLI); cli.launch=['mock']; cli.env={'CLOUDSDK_CORE_DISABLE_PROMPTS':'1','CLOUDSDK_CORE_SHOULD_PROMPT_TO_ENABLE_API':'false'}
        with patch('subprocess.run',return_value=subprocess.CompletedProcess([],0,None,None)) as run:
            cli.call(['auth','login','audit@example.com','--no-launch-browser'],interactive=True)
        actual=run.call_args.kwargs['env']
        self.assertEqual(actual['CLOUDSDK_CORE_DISABLE_PROMPTS'],'0')
        self.assertEqual(actual['CLOUDSDK_CORE_SHOULD_PROMPT_TO_ENABLE_API'],'false')
    def test_environment_blocks_inherited_overrides_and_api_enablement(self):
        with patch.object(bootstrap,'LOCAL',self.out), patch.dict(os.environ,{'CLOUDSDK_API_ENDPOINT_OVERRIDES_COMPUTE':'https://bad.invalid','CLOUDSDK_AUTH_IMPERSONATE_SERVICE_ACCOUNT':'bad@example.com'}):
            env=bootstrap.environment('audit@example.com')
        self.assertNotIn('CLOUDSDK_API_ENDPOINT_OVERRIDES_COMPUTE',env)
        self.assertNotIn('CLOUDSDK_AUTH_IMPERSONATE_SERVICE_ACCOUNT',env)
        self.assertEqual(env['CLOUDSDK_CORE_SHOULD_PROMPT_TO_ENABLE_API'],'false')
    def test_archive_path_traversal_rejected(self):
        archive=self.out/'bad.zip'
        with zipfile.ZipFile(archive,'w') as z:z.writestr('../escape.txt','bad')
        with self.assertRaises(ValueError):bootstrap.extract_archive(archive,self.out/'unpacked')
    def test_plan_does_not_install_authenticate_or_read(self):
        with patch.object(sys,'argv',['audit.py','--procedure','IAM-01','--plan']),patch.object(audit,'CLI',side_effect=AssertionError('cloud connection attempted')),patch('sys.stdout',new_callable=io.StringIO):
            self.assertEqual(audit.main(),0)
    def test_output_inside_public_repo_rejected_before_setup(self):
        scopefile=self.out/'scope.json'; scopefile.write_text(json.dumps(self.scope))
        with patch.object(sys,'argv',['audit.py','--procedure','IAM-01','--scope',str(scopefile),'--output',str(ROOT/'evidence')]),patch.object(audit,'CLI',side_effect=AssertionError('setup attempted')):
            with self.assertRaises(ValueError): audit.main()
    def test_workpaper_hash_is_not_effectiveness_opinion(self):
        (self.out/'report.txt').write_text('synthetic evidence')
        (self.out/'index.csv').write_text('procedure,evidence_type,relative_path,owner\nBCP-03,dated restore reports,report.txt,Owner\n')
        result=index_workpapers.index('BCP-03',self.out/'index.csv',self.out)
        self.assertEqual(result['assessment'],'Not assessed'); self.assertEqual(len(result['missing']),2)
        self.assertEqual(len(result['workpapers'][0]['sha256']),64)
    def test_workpaper_path_escape_rejected(self):
        (self.out/'index.csv').write_text('procedure,evidence_type,relative_path,owner\nBCP-03,dated restore reports,../private.txt,Owner\n')
        with self.assertRaises(ValueError): index_workpapers.index('BCP-03',self.out/'index.csv',self.out)
    def test_all_scope_expansions_match_documented_cli_flags(self):
        self.scope['billing_accounts']=['ABCDEF-123456-ABCDEF']
        overrides={
            ('iam','service-accounts','list'):[{'name':'projects/example-prod-123/serviceAccounts/sa@example-prod-123.iam.gserviceaccount.com','email':'sa@example-prod-123.iam.gserviceaccount.com'}],
            ('iam','workload-identity-pools','list'):[{'name':'projects/333333333333/locations/global/workloadIdentityPools/example-pool'}],
            ('secrets','list'):[{'name':'projects/333333333333/secrets/example-secret'}],
            ('sql','instances','list'):[{'name':'example-db','project':'example-prod-123'}],
            ('kms','keyrings','list'):[{'name':'projects/example-prod-123/locations/global/keyRings/example-ring'}],
            ('access-context-manager','policies','list'):[{'name':'accessPolicies/555555555555','parent':'organizations/123456789012'}]
        }
        c=self.collector(overrides); c.verify_projects()
        for key in OPERATIONS:c.run_operation(key)
        self.assertFalse([r for r in c.records if r['status'] in ['Incomplete','DependencyFailed','MissingInput','NotAuthorized']])
        documented={r['id']:r['documented_flags'] for r in json.loads((ROOT/'research/cli-help-checks.json').read_text())}
        for row in c.records:
            if row['operation'].startswith('preflight_'):continue
            for arg in row['command']:
                if arg.startswith('--'):self.assertIn(arg.split('=')[0],documented[row['operation']],str(row))

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(AuditTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    report={'tests_run':result.testsRun,'failures':[(str(t),e) for t,e in result.failures],'errors':[(str(t),e) for t,e in result.errors],
        'passed':result.wasSuccessful(),'mode':'Offline fake CLI; no cloud collection','recorded':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    (ROOT/'research/test-results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    sys.exit(0 if result.wasSuccessful() else 1)
