"""Title: Review incident lessons and closure
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: incident sample; postmortems; closure evidence
Documentation:
https://docs.cloud.google.com/architecture/framework/operational-excellence/learn-from-failures
https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("SEC-05"))
