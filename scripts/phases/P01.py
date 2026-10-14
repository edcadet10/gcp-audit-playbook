"""Title: Authorize and scope
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: signed charter; scope and authorization; responsibility matrix; independent project register; population reconciliation; service-owner approvals; obligation register; scope decisions; control crosswalk
Documentation:
https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy
https://docs.cloud.google.com/asset-inventory/docs/asset-types
https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate
https://docs.cloud.google.com/security/compliance/overview
https://docs.cloud.google.com/architecture/framework/security
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe
https://docs.cloud.google.com/sdk/gcloud/reference/billing/projects/describe
https://docs.cloud.google.com/sdk/gcloud/reference/services/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("P01"))
