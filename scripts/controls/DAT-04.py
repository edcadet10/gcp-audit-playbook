"""Title: Assess BigQuery lifecycle and query governance
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: job-history metadata; transfer schedules; data retention matrix
Documentation:
https://docs.cloud.google.com/bigquery/docs/managing-datasets
https://docs.cloud.google.com/bigquery/docs/reference/auditlogs
https://docs.cloud.google.com/bigquery/docs/exporting-data
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("DAT-04"))
