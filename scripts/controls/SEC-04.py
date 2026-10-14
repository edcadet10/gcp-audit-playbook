"""Title: Assess incident readiness and containment authority
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: incident plan; contact roster; tabletop report
Documentation:
https://docs.cloud.google.com/architecture/blueprints/security-foundations/operation-best-practices
https://docs.cloud.google.com/docs/security/overview/whitepaper
https://docs.cloud.google.com/sdk/gcloud/reference/organizations/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("SEC-04"))
