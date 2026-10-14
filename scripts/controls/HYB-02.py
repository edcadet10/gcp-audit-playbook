"""Title: Assess VPN redundancy and authentication
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: VPN topology; key custody record; prior failover results
Documentation:
https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview
https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/best-practices
https://docs.cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("HYB-02"))
