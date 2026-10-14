"""Title: Review user-managed service account keys
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: key exception register; rotation records; usage review
Documentation:
https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys
https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys
https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/list
https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("WID-02"))
