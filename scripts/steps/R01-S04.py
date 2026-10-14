"""Title: Review resource locations and sovereignty
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: data-location register; contract requirements; service exceptions
Documentation:
https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations
https://docs.cloud.google.com/assured-workloads/docs/overview
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/describe
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R01-S04"))
