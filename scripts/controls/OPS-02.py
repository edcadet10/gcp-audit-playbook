"""Title: Review quotas and capacity risk
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: quota register; utilization evidence; capacity plan
Documentation:
https://docs.cloud.google.com/docs/quotas/overview
https://docs.cloud.google.com/compute/docs/regions-zones
https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/describe
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("OPS-02"))
