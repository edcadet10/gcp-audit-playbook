"""Title: Offline CLI syntax probe. Description: Read help, never cloud resources.
Reference: https://docs.cloud.google.com/sdk/gcloud/reference/help
"""
import argparse, concurrent.futures, hashlib, json, os, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from operations import OPERATIONS
p = argparse.ArgumentParser()
p.add_argument('--sdk-root', required=True)
a = p.parse_args()
env = dict(os.environ, CLOUDSDK_PAGER='', PAGER='', CLOUDSDK_CORE_DISABLE_PROMPTS='1', CLOUDSDK_COMPONENT_MANAGER_DISABLE_UPDATE_CHECK='1')
def probe(op):
    proc = subprocess.run([sys.executable, str(pathlib.Path(a.sdk_root)/'lib/gcloud.py'), *op['command'], '--help'], capture_output=True, text=True, encoding='utf-8', errors='replace', env=env, timeout=90)
    body = proc.stdout + proc.stderr
    required = [flag.split('=')[0] for flag in op['flags']]
    return dict(id=op['id'], command=op['command'], exit_code=proc.returncode,
        missing_flags=[f for f in required if f not in body],
        documented_flags=sorted(set(__import__('re').findall(r'--[a-z][a-z0-9-]+',body))),
        help_sha256=hashlib.sha256(body.encode()).hexdigest(),
        synopsis=body[body.find('SYNOPSIS'):body.find('DESCRIPTION')].strip()[:1800],
        error=body[:800] if proc.returncode else None)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    result = list(pool.map(probe, OPERATIONS.values()))
(ROOT/'research/cli-help-checks.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
for row in result:
    if row['exit_code'] or row['missing_flags']:
        print(json.dumps({k:v for k,v in row.items() if k!='help'}))
print(f'Probed {len(result)} fixed command paths against local SDK help; no authentication or resource reads.')
