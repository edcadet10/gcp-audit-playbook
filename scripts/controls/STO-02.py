"""Title: Review uniform access and granular permissions
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: bucket permission review; managed-folder inventory; legacy ACL export
Documentation:
https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access
https://docs.cloud.google.com/storage/docs/managed-folders
https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("STO-02"))
