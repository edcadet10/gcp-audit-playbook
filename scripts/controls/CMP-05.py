"""Title: Inspect disks and deletion protection
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: disk classification; backup mapping; deletion policy
Documentation:
https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption
https://docs.cloud.google.com/compute/docs/instances/preventing-accidental-vm-deletion
https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("CMP-05"))
