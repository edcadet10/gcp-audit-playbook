"""Title: Resolve effective firewall exposure
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: effective-firewall export; network exposure register
Documentation:
https://docs.cloud.google.com/firewall/docs/firewall-policies-overview
https://docs.cloud.google.com/firewall/docs/firewalls
https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("NET-01"))
