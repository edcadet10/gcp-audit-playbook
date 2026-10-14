"""Title: Assess workload isolation and recovery
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: network-policy export; volume inventory; restore report
Documentation:
https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy
https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke
https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("GKE-05"))
