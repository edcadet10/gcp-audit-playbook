"""Title: Reconcile the population
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: inventory reconciliation; coverage gaps; signed charter; independent project register; population reconciliation; creation and retirement tickets; retention approvals; finance project register; billing account approvals; cost allocation
Documentation:
https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy
https://docs.cloud.google.com/asset-inventory/docs/asset-types
https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects
https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels
https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account
https://docs.cloud.google.com/billing/docs/how-to/view-linked
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe
https://docs.cloud.google.com/sdk/gcloud/reference/billing/projects/describe
https://docs.cloud.google.com/sdk/gcloud/reference/services/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("P03"))
