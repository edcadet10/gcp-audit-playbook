"""Title: Review source and build trigger trust
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: repository protection export; pipeline design; trigger approvals
Documentation:
https://docs.cloud.google.com/build/docs/securing-builds/gate-builds-on-approval
https://docs.cloud.google.com/sdk/gcloud/reference/builds/triggers/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R07-S01"))
