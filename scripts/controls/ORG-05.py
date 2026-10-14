"""Title: Review custom constraints and drift
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: policy-as-code repository export; change records
Documentation:
https://docs.cloud.google.com/resource-manager/docs/custom-constraints
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("ORG-05"))
