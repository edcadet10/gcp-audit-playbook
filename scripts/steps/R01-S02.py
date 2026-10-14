"""Title: Review project lifecycle and shutdown
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: creation and retirement tickets; retention approvals
Documentation:
https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects
https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels
https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe
https://docs.cloud.google.com/sdk/gcloud/reference/services/list
https://docs.cloud.google.com/sdk/gcloud/reference/billing/projects/describe
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R01-S02"))
