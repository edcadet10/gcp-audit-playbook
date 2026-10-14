"""Title: Assess integrity and evidence visibility
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: evidence-access matrix; error register; log administrator review
Documentation:
https://docs.cloud.google.com/logging/docs/access-control
https://docs.cloud.google.com/logging/docs/audit/best-practices
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R04-S05"))
