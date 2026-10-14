"""Title: Assess external application protection
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: load-balancer architecture; TLS policy export; exception register
Documentation:
https://docs.cloud.google.com/armor/docs/security-policy-overview
https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts
https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("NET-02"))
