"""Title: Assess patching and vulnerability operations
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: patch compliance export; asset reconciliation; exception records
Documentation:
https://docs.cloud.google.com/compute/vm-manager/docs/overview
https://docs.cloud.google.com/compute/vm-manager/docs/patch
https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("CMP-04"))
