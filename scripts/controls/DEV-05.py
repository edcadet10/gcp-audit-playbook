"""Title: Review infrastructure drift and change evidence
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: IaC export; drift report; change sample
Documentation:
https://docs.cloud.google.com/architecture/blueprints/security-foundations
https://docs.cloud.google.com/docs/terraform/best-practices/general-style-structure
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/describe
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("DEV-05"))
