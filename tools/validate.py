"""Title: Validate playbook integrity.
Description: Check authored/generated mappings, local links and anchors, script syntax, and required source coverage.
Reference: https://docs.cloud.google.com/sdk/gcloud/reference
"""
import ast, json, pathlib, re, sys, urllib.parse
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from operations import OPERATIONS
from catalog_data import CONTROLS, PHASES, RUNBOOKS, DOMAINS
errors=[]
def require(ok,message):
    if not ok: errors.append(message)
def slug(text):
    text=re.sub('<[^>]+>','',text).strip().lower().replace('`','')
    text=re.sub(r'[^\w\- ]','',text)
    return text.replace(' ','-')
recipes=json.loads((ROOT/'scripts/recipes.json').read_text(encoding='utf-8'))
require(len(CONTROLS)==100 and len(DOMAINS)==20,'Unexpected control/domain count')
require(len(recipes)==150,'Every control, runbook step and phase must have a recipe')
require(len({c['id'] for c in CONTROLS})==100,'Duplicate control IDs')
require(json.loads((ROOT/'controls/catalog.json').read_text(encoding='utf-8'))==CONTROLS,'Generated catalog drift')
require(json.loads((ROOT/'scripts/operations.json').read_text(encoding='utf-8'))==OPERATIONS,'Generated operation drift')
for key,recipe in recipes.items():
    group='controls' if key in {c['id'] for c in CONTROLS} else 'phases' if key.startswith('P') else 'steps'
    path=ROOT/'scripts'/group/(key+'.py')
    require(path.is_file(),f'Missing entry script {key}')
    if path.is_file():
        text=path.read_text(encoding='utf-8')
        require('Title:' in text and 'Description:' in text and 'Documentation:' in text,f'Missing script metadata {key}')
    require(bool(recipe['required_evidence']),f'No required evidence: {key}')
    require(bool(recipe['criterion']) and bool(recipe['falsification']),f'No criterion/challenge: {key}')
    require(any('google.com/' in s for s in recipe['sources']),f'No Google source: {key}')
    for op in recipe['operations']: require(op in OPERATIONS,f'Unknown operation {key}:{op}')
for file in ROOT.rglob('*.py'):
    if '.git' not in file.parts:
        try: ast.parse(file.read_text(encoding='utf-8'))
        except SyntaxError as exc:errors.append(str(file.relative_to(ROOT))+': '+str(exc))
checked_links=0
for file in ROOT.rglob('*.md'):
    if '.git' in file.parts: continue
    body=file.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',body):
        if re.match(r'^(https?://|mailto:)',target):continue
        target=target.strip('<>')
        path,_,anchor=target.partition('#')
        resolved=(file.parent/urllib.parse.unquote(path)).resolve() if path else file
        checked_links+=1
        require(resolved.exists(),f'Broken local link: {file.relative_to(ROOT)} -> {target}')
        if anchor and resolved.is_file() and resolved.suffix=='.md':
            headings=re.findall(r'^#{1,6}\s+(.+)$',resolved.read_text(encoding='utf-8'),re.M)
            require(urllib.parse.unquote(anchor) in {slug(x) for x in headings},f'Broken anchor: {file.relative_to(ROOT)} -> {target}')
sources=json.loads((ROOT/'references/sources.json').read_text(encoding='utf-8'))
source_urls={s['url'] for s in sources}
for c in CONTROLS:
    for u in c['sources']:require(u in source_urls,f'Unregistered source: {c["id"]} {u}')
for o in OPERATIONS.values():require(o['source'] in source_urls,f'Unregistered command source: {o["id"]}')
for s in sources:require(s['status']==200,f'Unavailable source: {s["url"]}')
report=dict(controls=len(CONTROLS),domains=len(DOMAINS),procedures=len(recipes),operations=len(OPERATIONS),sources=len(sources),local_links_checked=checked_links,errors=errors,passed=not errors)
(ROOT/'research/validation-results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
sys.exit(bool(errors))
