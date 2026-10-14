"""Title: Validate detection use cases
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: detection catalog; prior exercise results; alert routing export
Documentation:
https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview
https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
https://docs.cloud.google.com/sdk/gcloud/reference/logging/metrics/list
https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R08-S02"))
