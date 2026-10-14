"""Title: Review regional and zonal failure readiness
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: failover design; capacity evidence; prior exercise
Documentation:
https://docs.cloud.google.com/architecture/framework/reliability/design-scale-high-availability
https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list
https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/list
https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/describe
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("BCP-04"))
