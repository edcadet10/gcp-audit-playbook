"""Title: Assess service account key guardrails
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: key policy; exception approval; legacy key inventory
Documentation:
https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts
https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/describe
https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list
https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("ORG-03"))
