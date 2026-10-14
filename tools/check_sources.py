"""Title: Verify reference availability. Description: Fetch cited primary pages and record titles,
redirects and small factual excerpts for human review; HTTP success is not semantic validation.
Reference: https://docs.cloud.google.com
"""
import concurrent.futures, datetime, html, json, pathlib, re, sys, time, urllib.request
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
sys.path.insert(0,str(ROOT/'scripts'))
from catalog_data import CONTROLS
from operations import OPERATIONS
EXTRA = [
 'https://docs.cloud.google.com/sdk/docs/install-sdk',
 'https://docs.cloud.google.com/sdk/docs/downloads-versioned-archives',
 'https://docs.cloud.google.com/sdk/docs/authenticate',
 'https://docs.cloud.google.com/sdk/gcloud/reference/topic/startup',
 'https://docs.cloud.google.com/sdk/gcloud/reference/auth/login',
 'https://docs.cloud.google.com/sdk/gcloud/reference/auth/list',
 'https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-ancestors',
 'https://docs.cloud.google.com/asset-inventory/docs/roles-permissions',
 'https://docs.cloud.google.com/iam/docs/understanding-roles',
 'https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/getIamPolicy',
 'https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list',
 'https://www.cisecurity.org/benchmark/google_cloud_computing_platform',
 'https://csrc.nist.gov/pubs/sp/800/61/r3/final',
 'https://cloudsecurityalliance.org/research/cloud-controls-matrix',
 'https://sre.google/sre-book/table-of-contents/',
 'https://owasp.org/www-project-top-10-for-large-language-model-applications/'
]
urls = sorted(set(EXTRA + [u for c in CONTROLS for u in c['sources']] + [o['source'] for o in OPERATIONS.values()]))
cache = ROOT/'research/source-cache'
cache.mkdir(exist_ok=True)
def check(url):
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'GCP-Audit-Playbook-Reference-Review/1.0'})
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req,timeout=35) as response:
                    body=response.read().decode('utf-8',errors='replace')
                    final=response.url
                break
            except Exception:
                if attempt==2: raise
                time.sleep(1+attempt)
        title=re.search(r'<title[^>]*>(.*?)</title>',body,re.S)
        main=re.search(r'<main\b.*?</main>',body,re.S)
        cleaned=re.sub(r'<(script|style)\b[^>]*>.*?</\1>','',main.group(0) if main else body,flags=re.S)
        cleaned=html.unescape(re.sub('<[^>]+>',' ',cleaned))
        cleaned=re.sub(r'\s+',' ',cleaned).strip()
        digest=__import__('hashlib').sha256(url.encode()).hexdigest()[:16]
        (cache/(digest+'.txt')).write_text(cleaned,encoding='utf-8')
        return dict(url=url,final_url=final,status=200,title=html.unescape(title.group(1)).strip() if title else '',
                    text_chars=len(cleaned),cache=digest+'.txt',retrieved=datetime.datetime.now(datetime.timezone.utc).isoformat())
    except Exception as exc:
        return dict(url=url,status='error',error=str(exc))
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
    result=list(pool.map(check,urls))
(ROOT/'research/source-checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
(ROOT/'references').mkdir(exist_ok=True)
(ROOT/'references/sources.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'total':len(result),'errors':[r for r in result if r['status']!=200]},indent=2))
