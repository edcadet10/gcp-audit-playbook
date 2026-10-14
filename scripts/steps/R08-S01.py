"""Title: Assess Security Command Center coverage
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: SCC configuration export; coverage matrix; detector status
Documentation:
https://docs.cloud.google.com/security-command-center/docs/service-tiers
https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview
https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R08-S01"))
