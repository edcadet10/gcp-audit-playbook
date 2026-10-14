"""Title: Prioritize and agree actions
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: finding register; management responses; triage queue; mute rules; ticket samples; quality review; closure evidence
Documentation:
https://docs.cloud.google.com/security-command-center/docs/review-manage-findings
https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings
https://docs.cloud.google.com/architecture/framework/security
https://csrc.nist.gov/pubs/sp/800/53/a/r5/final
https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("P08"))
