"""Title: Assess deployment approvals and admission
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: release sample; attestation metadata; admission results
Documentation:
https://docs.cloud.google.com/binary-authorization/docs/overview
https://docs.cloud.google.com/deploy/docs/promote-release
https://docs.cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/list
https://docs.cloud.google.com/sdk/gcloud/reference/container/binauthz/policy/export
https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/list
https://docs.cloud.google.com/sdk/gcloud/reference/run/services/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R07-S03"))
