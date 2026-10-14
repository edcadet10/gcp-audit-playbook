"""Title: Assess retention location and protected access
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: retention matrix; SIEM settings; bucket access review
Documentation:
https://docs.cloud.google.com/logging/docs/buckets
https://docs.cloud.google.com/logging/docs/storage
https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("LOG-03"))
