"""Title: Review cluster maintenance and supply chain
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: version inventory; upgrade history; image provenance
Documentation:
https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels
https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions
https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/list
https://docs.cloud.google.com/sdk/gcloud/reference/container/binauthz/policy/export
https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("GKE-04"))
