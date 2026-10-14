"""Title: Assess maintenance and support lifecycle
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: support matrix; upgrade plan; provider notices
Documentation:
https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule
https://docs.cloud.google.com/functions/docs/runtime-support
https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/list
https://docs.cloud.google.com/sdk/gcloud/reference/functions/list
https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("OPS-03"))
