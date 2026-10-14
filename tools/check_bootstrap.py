"""Title: Verify pinned SDK download references.
Description: Inspect official archive URLs with HEAD and compare pinned hashes with Google's published download table.
Reference: https://docs.cloud.google.com/sdk/docs/downloads-versioned-archives
Does not download, install or run an SDK.
"""
import concurrent.futures, datetime, json, pathlib, sys, urllib.request
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from bootstrap import ARCHIVES, VERSION
def check(item):
    platform,(filename,digest)=item
    url='https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/'+filename
    with urllib.request.urlopen(urllib.request.Request(url,method='HEAD'),timeout=30) as response:
        return dict(platform=list(platform),version=VERSION,url=url,status=response.status,bytes=response.headers.get('Content-Length'),sha256=digest)
source_rows=json.loads((ROOT/'research/source-checks.json').read_text(encoding='utf-8'))
table=next(r for r in source_rows if r['url'].endswith('/downloads-versioned-archives'))
table_text=(ROOT/'research/source-cache'/table['cache']).read_text(encoding='utf-8')
for _,digest in ARCHIVES.values():
    if digest not in table_text: raise ValueError('Pinned hash missing from the reviewed official download table')
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:results=list(pool.map(check,ARCHIVES.items()))
(ROOT/'research/bootstrap-checks.json').write_text(json.dumps({'checked':datetime.datetime.now(datetime.timezone.utc).isoformat(),'archives':results,'limitation':'Availability and recorded hashes only; installation not exercised on these platforms.'},indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
