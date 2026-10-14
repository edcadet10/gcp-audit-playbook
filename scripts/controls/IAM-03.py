"""Title: Review joiner mover leaver controls
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: HR sample; directory membership; removal tickets
Documentation:
https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys
https://docs.cloud.google.com/iam/docs/groups-in-cloud-console
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
https://docs.cloud.google.com/sdk/gcloud/reference/organizations/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/folders/get-iam-policy
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("IAM-03"))
