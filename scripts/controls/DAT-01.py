"""Title: Review Cloud SQL access and exposure
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: database user and grant export; connectivity design; engine baseline
Documentation:
https://docs.cloud.google.com/sql/docs/postgres/iam-authentication
https://docs.cloud.google.com/sql/docs/postgres/authorize-networks
https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance
https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("DAT-01"))
