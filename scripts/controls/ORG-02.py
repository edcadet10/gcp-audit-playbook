"""Title: Assess domain and external sharing restrictions
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: external-party register; sharing exceptions
Documentation:
https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains
https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/describe
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("ORG-02"))
