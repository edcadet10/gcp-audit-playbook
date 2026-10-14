"""Title: Review emergency and time-bound privilege
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: emergency runbook; exercise record; privilege approvals
Documentation:
https://docs.cloud.google.com/iam/docs/pam-overview
https://docs.cloud.google.com/docs/security/best-practices-continuous-access-to-google-cloud
https://docs.cloud.google.com/sdk/gcloud/reference/organizations/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("IAM-04"))
