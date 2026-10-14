"""Title: Review workload identity activity
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: activity review; log coverage matrix; automation schedules
Documentation:
https://docs.cloud.google.com/iam/docs/audit-logging
https://docs.cloud.google.com/iam/docs/service-account-creds
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/list
https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("WID-05"))
