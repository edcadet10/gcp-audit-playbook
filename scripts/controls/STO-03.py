"""Title: Assess retention lifecycle and deletion recovery
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: retention schedule; legal holds; recovery examples
Documentation:
https://docs.cloud.google.com/storage/docs/bucket-lock
https://docs.cloud.google.com/storage/docs/soft-delete
https://docs.cloud.google.com/storage/docs/lifecycle
https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("STO-03"))
