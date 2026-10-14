"""Title: Assess recovery operations and ownership
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: runbook review; access checklist; exercise action log
Documentation:
https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R06-S05"))
