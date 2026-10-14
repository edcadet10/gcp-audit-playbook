"""Title: Review finding triage and suppression
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: triage queue; mute rules; ticket samples
Documentation:
https://docs.cloud.google.com/security-command-center/docs/review-manage-findings
https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings
https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("SEC-02"))
