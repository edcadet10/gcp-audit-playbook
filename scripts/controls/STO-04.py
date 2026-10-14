"""Title: Inspect bucket encryption and location
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: encryption coverage export; location requirements; key dependency map
Documentation:
https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys
https://docs.cloud.google.com/storage/docs/locations
https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("STO-04"))
