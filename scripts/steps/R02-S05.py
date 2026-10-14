"""Title: Inspect service account escalation paths
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: privilege graph; deployment approvals
Documentation:
https://docs.cloud.google.com/iam/docs/service-account-permissions
https://docs.cloud.google.com/iam/docs/best-practices-service-accounts
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/list
https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R02-S05"))
