"""Title: Review optimization decisions and commitments
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: utilization report; recommendation export; commitment register
Documentation:
https://docs.cloud.google.com/recommender/docs/overview
https://docs.cloud.google.com/billing/docs/how-to/cud-analysis
https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/describe
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("FIN-04"))
