"""Title: Assess landing-zone design
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: architecture diagrams; design decisions; exception register
Documentation:
https://docs.cloud.google.com/architecture/blueprints/security-foundations
https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/organizations/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/folders/get-iam-policy
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("GOV-03"))
