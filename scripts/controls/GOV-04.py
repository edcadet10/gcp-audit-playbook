"""Title: Review exceptions and policy ownership
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: exception register; policy baseline; review minutes
Documentation:
https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview
https://docs.cloud.google.com/architecture/framework/security
https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list
https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("GOV-04"))
