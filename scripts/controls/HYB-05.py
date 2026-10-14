"""Title: Assess hybrid administration access
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: administration design; IAP access policy export; access sample
Documentation:
https://docs.cloud.google.com/iap/docs/using-tcp-forwarding
https://docs.cloud.google.com/compute/docs/oslogin
https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("HYB-05"))
