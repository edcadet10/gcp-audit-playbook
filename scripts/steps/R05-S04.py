"""Title: Assess KMS purpose and separation of duties
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: key inventory; custody matrix; access review
Documentation:
https://docs.cloud.google.com/kms/docs/separation-of-duties
https://docs.cloud.google.com/kms/docs/iam
https://docs.cloud.google.com/sdk/gcloud/reference/kms/keyrings/list
https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R05-S04"))
