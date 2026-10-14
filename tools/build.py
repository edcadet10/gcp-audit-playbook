"""Title: Build the reusable audit work program.
Description: Generate control docs, script wrappers and workpaper templates from the authored catalog.
Reference: https://docs.cloud.google.com/architecture/framework/security
"""
import csv, json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from catalog_data import CONTROLS, DOMAINS, PHASES, RUNBOOKS
from operations import OPERATIONS
def write(path,text):
    file=ROOT/path; file.parent.mkdir(parents=True,exist_ok=True); file.write_text(text,encoding='utf-8')
def dump(path,value): write(path,json.dumps(value,indent=2,ensure_ascii=False)+'\n')
def csvfile(path,headers,rows=()):
    p=ROOT/path; p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f,lineterminator='\n'); w.writerow(headers); w.writerows(rows)
sources=json.loads((ROOT/'references/sources.json').read_text(encoding='utf-8')) if (ROOT/'references/sources.json').exists() else []
source_map={s['url']:s for s in sources}
def links(urls):
    return ' · '.join('['+source_map.get(u,{}).get('title',u.split('docs.cloud.google.com/')[-1]).split('|')[0].strip()+']('+u+')' for u in dict.fromkeys(urls))
recipes={c['id']:dict(c) for c in CONTROLS}
by_id={c['id']:c for c in CONTROLS}
def merge(key,title,ids,evidence=None):
    controls=[by_id[x] for x in ids.split()]
    return dict(id=key,title=title,controls=ids.split(),
        procedure=' '.join(c['id']+': '+c['procedure'] for c in controls),
        criterion=' '.join(c['id']+': '+c['criterion'] for c in controls),
        falsification=' '.join(c['id']+': '+c['falsification'] for c in controls),
        required_evidence=list(dict.fromkeys((evidence.split(';') if evidence else [])+[e for c in controls for e in c['required_evidence']])),
        operations=list(dict.fromkeys(x for c in controls for x in c['operations'])),
        sources=list(dict.fromkeys(u for c in controls for u in c['sources'])))
for key,title,ids,evidence in PHASES: recipes[key]=merge(key,title,ids,evidence)
runbook_docs=['# Fieldwork runbooks\n\nEight five-step investigations. Each step has an executable read-only evidence procedure. Run from the repository root; plan mode is offline. Human review and requested workpapers are necessary to complete the step. See [collection instructions](../scripts/README.md) and [assessment rules](../PLAYBOOK.md#assessment-rules).\n']
for key,title,ids in RUNBOOKS:
    runbook_docs.append(f'## {key} — {title}\n')
    for i,cid in enumerate(ids.split(),1):
        step=f'{key}-S{i:02}'
        c=by_id[cid]; recipes[step]=merge(step,c['title'],cid)
        runbook_docs.append(f'### Step {i}: {c["title"]}\n\n**Procedure:** {c["procedure"]}\n\n**Acceptable evidence:** '+ '; '.join(c['required_evidence'])+f'.\n\n**Challenge:** {c["falsification"]}\n\n**Decision criterion:** {c["criterion"]}\n\n**Script:** [{step}.py](../scripts/steps/{step}.py). Description: collect the mapped configuration, record acquisition gaps, and create this step\'s evidence requests and assessment workpaper.\n\n```sh\n# Title: Preview {c["title"]}\n# Description: Display the documented evidence plan without connecting.\npython scripts/steps/{step}.py --plan\n```\n\n**Google references:** {links(c["sources"])}\n')
write('docs/FIELDWORK-RUNBOOKS.md','\n'.join(runbook_docs))
dump('controls/catalog.json',CONTROLS); dump('scripts/recipes.json',recipes); dump('scripts/operations.json',OPERATIONS)
catalog=['# Control catalog\n\n100 consultant-authored controls across 20 domains. Google references support product behavior; the auditor and organization adopt the criteria, sample design, severity and operating requirements. Each script collects metadata and creates a workpaper; it does not make an audit opinion.\n\n[Main playbook](../PLAYBOOK.md) · [Run scripts](../scripts/README.md) · [CSV](control-catalog.csv)\n']
for code,d in DOMAINS.items():
    catalog.append(f'## {code} — {d["name"]}\n\nSuggested accountable owner: **{d["owner"]}**.\n')
    for c in [x for x in CONTROLS if x['domain']==code]:
        cid=c['id']
        catalog.append(f'### {cid} — {c["title"]}\n\n**Objective and applicability:** {c["objective"]}. {c["applicability"]}\n\n**Read-only evidence procedure:** {c["procedure"]}\n\n**Required workpapers:** '+ '; '.join(c['required_evidence'])+f'.\n\n**Consultant assessment criterion:** {c["criterion"]}\n\n**Try to disprove the conclusion:** {c["falsification"]}\n\n**Script title:** {c["title"]}. **Description:** collect '+', '.join(OPERATIONS[o]['title'].lower() for o in c['operations'])+f'; create evidence requests and an unassessed review workpaper. [Open {cid}.py](../scripts/controls/{cid}.py).\n\n**Operations:** '+', '.join('`'+o+'`' for o in c['operations'])+f' — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).\n\n**Google documentation:** {links(c["sources"])}\n\n**Response if the criterion fails:** {c["remediation"]}\n\n**Reassessment:** {c["cadence"]}\n')
write('controls/CONTROL-CATALOG.md','\n'.join(catalog))
csvfile('controls/control-catalog.csv',['id','domain','title','owner','procedure','criterion','falsification','required_evidence','operations','sources'],[[c[k] if not isinstance(c[k],list) else '; '.join(c[k]) for k in ['id','domain','title','owner','procedure','criterion','falsification','required_evidence','operations','sources']] for c in CONTROLS])
coverage=['# Script coverage\n\nEvery control, fieldwork step and engagement phase has one executable entry point. All share the same setup, authentication, scope verification and read dispatcher. **A mapped script does not replace interviews, directory evidence, data-plane ACL exports, prior exercises or an auditor\'s conclusion.**\n\n| Procedure | Title and purpose | Script | Evidence operations |\n|---|---|---|---|']
for key,recipe in recipes.items():
    group='controls' if key in by_id else 'phases' if key.startswith('P') else 'steps'
    urls=list(dict.fromkeys(recipe['sources']+[OPERATIONS[o]['source'] for o in recipe['operations']]))
    header='Title: '+recipe['title']+'\nDescription: Collect fixed read-only metadata, record gaps, and create the review workpaper.\n'
    wrapper='"""'+header+'Required evidence: '+ '; '.join(recipe['required_evidence'])+'\nDocumentation:\n'+'\n'.join(urls)+'\n"""\nimport pathlib, sys\nsys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))\nfrom audit import main\nif __name__ == "__main__":\n    sys.exit(main("'+key+'"))\n'
    write(f'scripts/{group}/{key}.py',wrapper)
    coverage.append(f'| {key} | {recipe["title"]} | [{key}.py](../scripts/{group}/{key}.py) | '+', '.join(recipe['operations'])+' |')
write('docs/SCRIPT-COVERAGE.md','\n'.join(coverage)+'\n')
operations=['# Documented read operations\n\nThe code register is [operations.py](../scripts/operations.py). Each entry is a fixed command path; scope values cannot supply command strings. Permissions below are the focal read permissions, not a guarantee that they alone satisfy all ancestor, service usage or supporting calls. Confirm least privilege during the pilot using [Google\'s IAM role reference](https://docs.cloud.google.com/iam/docs/understanding-roles) and [Cloud Asset Inventory permissions](https://docs.cloud.google.com/asset-inventory/docs/roles-permissions). Never grant Owner or Editor to make a collector work.\n\nNo output file flags, cloud exports to buckets, data queries, secret payload reads, API enablement, role changes or remediations are dispatched. Binary Authorization `policy export` is a documented semantic read to stdout. gcloud handles server pagination for uncapped list operations; inventory consistency and visibility still require reconciliation.\n']
for key,o in OPERATIONS.items():
    operations.append(f'## {key} — {o["title"]}\n\n{o["description"]}\n\n- **Command:** `gcloud '+ ' '.join(o['command']+o['flags'])+f'`\n- **Scope expansion:** `{o["scope"]}`; see [scope and fan-out rules](COLLECTION-GUIDE.md).\n- **Focal permissions:** `{o["permission"]}`.\n- **Documentation:** {links([o["source"]])}\n')
write('docs/SCRIPT-OPERATIONS.md','\n'.join(operations))
register=['# Source register\n\nReviewed 14 October 2026. Provider references explain product semantics; independent references inform the assessment method. Link checks are recorded separately from human interpretation. Redirects and retrieval times are preserved in [sources.json](sources.json). Recheck mutable documentation before each engagement. This is an independent work program, not a Google, CIS, NIST or CSA certification.\n\n| Source | Publisher | Reference |\n|---|---|---|']
for i,s in enumerate(sources,1):
    publisher='Google' if any(x in s['url'].split('/')[2] for x in ['google.com','google']) else 'Independent framework owner'
    register.append(f'| REF-{i:03} | {publisher} | {links([s["url"]])} |')
write('references/SOURCES.md','\n'.join(register)+'\n')
template_specs={
 'scope-register':['organization','folder','project_id','project_number','business_owner','environment','criticality','regions','billing_account','in_scope','exclusion_rationale'],
 'access-request':['identity','scope','operation','permission','proposed_read_role','approver','expiry','pilot_result'],
 'coverage-matrix':['service','project','region','expected_population','observed_population','native_reconciliation','permission_gap','unsupported_type','decision'],
 'sampling-plan':['control','population','period','risk_strata','selection_method','sample_size','rationale','selected_items','limitations'],
 'evidence-register':['evidence_id','control','source','scope','collected_utc','period','file_reference','sha256','custodian','sensitivity','completeness','retention'],
 'control-assessment':['control','title','applicability','design_result','operating_result','evidence_ids','status','reviewer','review_date','limitations'],
 'finding-register':['finding_id','control','condition','criterion','cause','impact','likelihood','severity','confidence','affected_population','evidence_ids','owner','response','due_date','status'],
 'exceptions':['exception_id','control','scope','rationale','compensating_control','evidence','approver','expiry','review_date'],
 'remediation-plan':['finding_id','action','owner','dependencies','target_date','change_record','rollback','validation','residual_risk','closure_approver'],
 'retention-matrix':['data_class','system','primary_retention','backup_retention','log_retention','location','legal_hold','deletion_evidence','owner'],
 'identity-review':['principal','type','source_scope','role','group_expansion','condition','deny_boundary_review','business_justification','owner','decision'],
 'recovery-matrix':['business_service','data_store','RPO','RTO','backup_mechanism','key_dependency','last_restore','integrity_evidence','actual_RPO','actual_RTO','gap'],
 'framework-crosswalk':['adopted_framework','version','requirement','applicability','control_ids','evidence','mapping_owner','mapping_confidence'],
 'decision-log':['decision_id','date','question','evidence_for','evidence_against','decision','owner','revisit_trigger'],
 'test-record':['control','claim','kill_criterion','sample','procedure','expected','actual','evidence','conclusion','reviewer']
}
for name,headers in template_specs.items():
    rows=[[c['id'],c['title'],'Undetermined','','','','Not assessed','','',''] for c in CONTROLS] if name=='control-assessment' else []
    csvfile('templates/'+name+'.csv',headers,rows)
write('templates/README.md','# Engagement workpapers\n\nCopy these into the private engagement evidence location. Do not commit completed customer workpapers to this public repository. Templates are consultant work products; adopt requirements with the organization.\n\n'+ '\n'.join('- ['+name+']('+name+'.csv)' for name in template_specs)+'\n\n- [Engagement charter](engagement-charter.md)\n- [Finding narrative](finding.md)\n- [Executive report](executive-report.md)\n\nBasis: '+links(['https://docs.cloud.google.com/architecture/framework/security','https://csrc.nist.gov/pubs/sp/800/53/a/r5/final'])+'\n')
print(json.dumps({'controls':len(CONTROLS),'domains':len(DOMAINS),'procedures':len(recipes),'operations':len(OPERATIONS),'sources':len(sources),'templates':len(template_specs)+3}))
