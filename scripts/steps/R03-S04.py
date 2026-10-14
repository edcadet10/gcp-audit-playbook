"""Title: Assess public and external bucket access
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: sharing register; ACL metadata when applicable; signed URL governance
Documentation:
https://docs.cloud.google.com/storage/docs/public-access-prevention
https://docs.cloud.google.com/storage/docs/access-control/signed-urls
https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/describe
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R03-S04"))
