"""Title: Verify Data Access audit coverage
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: service logging matrix; effective auditConfig analysis
Documentation:
https://docs.cloud.google.com/logging/docs/audit
https://docs.cloud.google.com/logging/docs/audit/configure-data-access
https://docs.cloud.google.com/sdk/gcloud/reference/organizations/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/folders/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/services/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R04-S01"))
