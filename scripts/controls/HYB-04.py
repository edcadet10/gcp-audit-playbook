"""Title: Review peering and transit trust
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: peering approvals; transit routing analysis
Documentation:
https://docs.cloud.google.com/vpc/docs/vpc-peering
https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview
https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("HYB-04"))
