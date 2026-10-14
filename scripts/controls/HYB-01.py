"""Title: Review Shared VPC administration
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: Shared VPC relationship export; responsibility matrix
Documentation:
https://docs.cloud.google.com/vpc/docs/shared-vpc
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("HYB-01"))
