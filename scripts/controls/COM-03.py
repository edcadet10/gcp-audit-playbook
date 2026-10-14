"""Title: Review privacy lifecycle and deletion evidence
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: data-flow map; deletion request samples; processor register
Documentation:
https://docs.cloud.google.com/security/compliance/gdpr
https://docs.cloud.google.com/storage/docs/lifecycle
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/list
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("COM-03"))
