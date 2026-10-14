"""Title: Assess allocation and cost reporting
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: billing-export settings; allocation report; finance reconciliation
Documentation:
https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery
https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe
https://docs.cloud.google.com/sdk/gcloud/reference/billing/projects/describe
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("FIN-03"))
