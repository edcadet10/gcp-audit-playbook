"""Title: Assess MFA and identity federation
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: IdP policy and membership exports; authentication review
Documentation:
https://docs.cloud.google.com/iam/docs/workforce-identity-federation
https://support.google.com/a/answer/9176657
https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/organizations/get-iam-policy
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("IAM-02"))
