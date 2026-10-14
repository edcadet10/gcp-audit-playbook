"""Title: Review Secret Manager access and replication
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: secret ownership; consumer mapping; access review
Documentation:
https://docs.cloud.google.com/secret-manager/docs/best-practices
https://docs.cloud.google.com/secret-manager/docs/access-control
https://docs.cloud.google.com/sdk/gcloud/reference/secrets/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("KEY-01"))
