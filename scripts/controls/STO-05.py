"""Title: Review storage logging and transfer paths
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: transfer-job export; access review; logging coverage
Documentation:
https://docs.cloud.google.com/storage/docs/audit-logging
https://docs.cloud.google.com/storage-transfer/docs/overview
https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("STO-05"))
