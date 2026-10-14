"""Title: Inspect private access and egress
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: egress policy; flow-log analysis; network diagrams
Documentation:
https://docs.cloud.google.com/vpc/docs/private-google-access
https://docs.cloud.google.com/vpc/docs/private-service-connect
https://docs.cloud.google.com/nat/docs/overview
https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/list
https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("NET-03"))
