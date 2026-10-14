"""Title: Assess SQL availability and recovery
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: recovery objectives; backup history; restore results
Documentation:
https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups
https://docs.cloud.google.com/sql/docs/postgres/high-availability
https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/list
https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("DAT-02"))
