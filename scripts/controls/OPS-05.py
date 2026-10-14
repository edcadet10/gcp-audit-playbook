"""Title: Assess service ownership and incident learning
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: service catalog; on-call roster; postmortem actions
Documentation:
https://docs.cloud.google.com/architecture/framework/operational-excellence/learn-from-failures
https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels
https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("OPS-05"))
