"""Title: Review backup coverage and immutability
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: backup coverage matrix; vault settings export; administrator review
Documentation:
https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault
https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots
https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/list
https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("BCP-02"))
