"""Title: Review BigQuery access and fine-grained controls
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: dataset ACL export; row and column policy metadata; sharing register
Documentation:
https://docs.cloud.google.com/bigquery/docs/row-level-security-intro
https://docs.cloud.google.com/bigquery/docs/column-level-security-intro
https://docs.cloud.google.com/bigquery/docs/authorized-views
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R03-S05"))
