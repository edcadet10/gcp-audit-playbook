"""Title: Establish organizational ownership and scope
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: signed charter; independent project register; population reconciliation
Documentation:
https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy
https://docs.cloud.google.com/asset-inventory/docs/asset-types
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe
https://docs.cloud.google.com/sdk/gcloud/reference/billing/projects/describe
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R01-S01"))
