"""Title: Resolve inherited privileged access
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: group membership export; effective-access workpaper; access approvals
Documentation:
https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control
https://docs.cloud.google.com/iam/docs/policy-types
https://docs.cloud.google.com/iam/docs/conditions-overview
https://docs.cloud.google.com/sdk/gcloud/reference/organizations/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/folders/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R02-S01"))
