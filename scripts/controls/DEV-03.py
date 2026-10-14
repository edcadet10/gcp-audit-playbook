"""Title: Review artifact access and vulnerability governance
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: deployed digest register; scan export; SBOM; exceptions
Documentation:
https://docs.cloud.google.com/artifact-registry/docs/access-control
https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview
https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/list
https://docs.cloud.google.com/sdk/gcloud/reference/run/services/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("DEV-03"))
