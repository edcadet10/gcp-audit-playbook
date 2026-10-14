"""Title: Verify effective organization policies
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: constraint baseline; effective-policy comparison
Documentation:
https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy
https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview
https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list
https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/describe
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("ORG-01"))
