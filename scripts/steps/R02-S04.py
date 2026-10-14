"""Title: Validate federation trust boundaries
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: federation design; provider export; subject-to-role mapping
Documentation:
https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines
https://docs.cloud.google.com/iam/docs/workload-identity-federation
https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/list
https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R02-S04"))
