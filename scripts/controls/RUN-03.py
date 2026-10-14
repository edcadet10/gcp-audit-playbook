"""Title: Inspect scheduled and batch execution
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: job ownership; failure records; target authorization
Documentation:
https://docs.cloud.google.com/run/docs/create-jobs
https://docs.cloud.google.com/scheduler/docs/http-target-auth
https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/list
https://docs.cloud.google.com/sdk/gcloud/reference/scheduler/jobs/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("RUN-03"))
