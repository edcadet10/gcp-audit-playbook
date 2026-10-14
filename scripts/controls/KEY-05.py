"""Title: Assess CMEK and external key dependencies
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: CMEK coverage matrix; external-key contract; recovery evidence
Documentation:
https://docs.cloud.google.com/kms/docs/cmek
https://docs.cloud.google.com/kms/docs/ekm
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("KEY-05"))
