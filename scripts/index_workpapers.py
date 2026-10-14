"""Title: Index existing local audit workpapers.
Description: Hash explicitly supplied files, reconcile required evidence labels and leave audit judgments unassessed.
References: https://csrc.nist.gov/pubs/sp/800/53/a/r5/final
https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide
This local-only step neither requires cloud authentication nor invokes a cloud command.
"""
import argparse, csv, hashlib, json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
def index(procedure,manifest,base):
    recipes=json.loads((ROOT/'scripts/recipes.json').read_text(encoding='utf-8'))
    if procedure not in recipes: raise ValueError('Unknown procedure')
    base=pathlib.Path(base).resolve()
    rows=[]
    with pathlib.Path(manifest).open(newline='',encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            if row.get('procedure')!=procedure: continue
            file=(base/row.get('relative_path','')).resolve()
            if not file.is_relative_to(base) or not file.is_file(): raise ValueError('Workpaper path escapes the approved directory or is not a file')
            if not row.get('owner') or not row.get('evidence_type'): raise ValueError('Owner and evidence_type are required')
            with file.open('rb') as stream: digest=hashlib.file_digest(stream,'sha256').hexdigest()
            rows.append(dict(row,sha256=digest,size_bytes=file.stat().st_size,status='Present; content and relevance require review'))
    supplied={r['evidence_type'] for r in rows}
    return dict(procedure=procedure,assessment='Not assessed',workpapers=rows,
        missing=[e for e in recipes[procedure]['required_evidence'] if e not in supplied],
        limitation='A matching evidence label and file hash do not demonstrate authenticity, sufficiency or operating effectiveness.')
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--procedure',required=True); p.add_argument('--manifest',required=True,type=pathlib.Path)
    p.add_argument('--base',required=True,type=pathlib.Path); p.add_argument('--output',required=True,type=pathlib.Path)
    a=p.parse_args()
    if a.output.resolve().is_relative_to(ROOT): raise ValueError('Keep workpaper indexes outside the public repository')
    result=index(a.procedure,a.manifest,a.base)
    with a.output.open('x',encoding='utf-8') as f: json.dump(result,f,indent=2)
    print(json.dumps({'indexed':len(result['workpapers']),'missing':result['missing'],'assessment':'Not assessed'}))
if __name__=='__main__': main()
