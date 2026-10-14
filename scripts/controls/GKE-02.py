"""Title: Review Kubernetes RBAC and admission
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: Kubernetes RBAC export; admission policy and results; namespace ownership
Documentation:
https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control
https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission
https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("GKE-02"))
