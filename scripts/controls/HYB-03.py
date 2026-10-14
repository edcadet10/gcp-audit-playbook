"""Title: Assess Interconnect dependencies
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: provider circuit records; monitoring export; topology
Documentation:
https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview
https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/redundancy
https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("HYB-03"))
