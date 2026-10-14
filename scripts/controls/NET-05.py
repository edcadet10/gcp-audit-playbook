"""Title: Review DNS and network telemetry
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: DNS settings export; flow evidence; network monitoring use cases
Documentation:
https://docs.cloud.google.com/dns/docs/dnssec
https://docs.cloud.google.com/vpc/docs/flow-logs
https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/list
https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("NET-05"))
