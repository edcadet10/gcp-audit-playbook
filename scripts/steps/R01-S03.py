"""Title: Reconcile billing and project accountability
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: finance project register; billing account approvals; cost allocation
Documentation:
https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account
https://docs.cloud.google.com/billing/docs/how-to/view-linked
https://docs.cloud.google.com/sdk/gcloud/reference/billing/projects/describe
https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R01-S03"))
