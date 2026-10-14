"""Title: Assess classification and data discovery
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: classification register; discovery profile export; coverage reconciliation
Documentation:
https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R05-S01"))
