"""Title: Review key lifecycle and availability
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: key-version metadata export; destruction approvals; dependency mapping
Documentation:
https://docs.cloud.google.com/kms/docs/key-rotation
https://docs.cloud.google.com/kms/docs/key-states
https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("KEY-04"))
