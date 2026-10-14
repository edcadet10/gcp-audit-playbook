"""Title: Challenge findings
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: contrary evidence; technical review; group membership export; effective-access workpaper; access approvals; sharing register; ACL metadata when applicable; signed URL governance; finding register; quality review; management responses; closure evidence
Documentation:
https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control
https://docs.cloud.google.com/iam/docs/policy-types
https://docs.cloud.google.com/iam/docs/conditions-overview
https://docs.cloud.google.com/storage/docs/public-access-prevention
https://docs.cloud.google.com/storage/docs/access-control/signed-urls
https://docs.cloud.google.com/architecture/framework/security
https://csrc.nist.gov/pubs/sp/800/53/a/r5/final
https://docs.cloud.google.com/sdk/gcloud/reference/organizations/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/folders/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/list
https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/list
https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/describe
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("P07"))
