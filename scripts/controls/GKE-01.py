"""Title: Assess cluster control-plane access
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: cluster architecture; administrator review
Documentation:
https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster
https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation
https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("GKE-01"))
