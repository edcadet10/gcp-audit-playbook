"""Title: Prove an existing event's end-to-end trace
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: known-event record; source and destination evidence; timing comparison
Documentation:
https://docs.cloud.google.com/logging/docs/view/logging-query-language
https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/list
https://docs.cloud.google.com/sdk/gcloud/reference/logging/metrics/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R04-S04"))
