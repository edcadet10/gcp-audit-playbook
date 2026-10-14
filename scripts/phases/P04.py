"""Title: Establish the baseline and sample
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: adopted baseline; sampling rationale; exception register; policy baseline; review minutes; constraint baseline; effective-policy comparison
Documentation:
https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview
https://docs.cloud.google.com/architecture/framework/security
https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy
https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list
https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/describe
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("P04"))
