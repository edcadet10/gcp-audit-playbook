"""Title: Review operational change and access
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: change samples; emergency approvals; supplier access review
Documentation:
https://docs.cloud.google.com/architecture/framework/operational-excellence/manage-change
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
https://docs.cloud.google.com/sdk/gcloud/reference/builds/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("OPS-04"))
