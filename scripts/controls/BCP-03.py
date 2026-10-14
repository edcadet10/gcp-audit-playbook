"""Title: Assess restore evidence
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: dated restore reports; integrity checks; business sign-off
Documentation:
https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide
https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restoring
https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/list
https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("BCP-03"))
