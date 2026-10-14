"""Title: Review budgets and spend control behavior
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: budget approvals; notification delivery; response records
Documentation:
https://docs.cloud.google.com/billing/docs/how-to/budgets
https://docs.cloud.google.com/sdk/gcloud/reference/billing/budgets/list
https://docs.cloud.google.com/sdk/gcloud/reference/billing/projects/describe
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R08-S04"))
