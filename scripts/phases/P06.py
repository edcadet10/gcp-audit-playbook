"""Title: Review operating effectiveness
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: known-event test; historical operation samples; known-event record; source and destination evidence; timing comparison; detection catalog; prior exercise results; alert routing export; dated restore reports; integrity checks; business sign-off
Documentation:
https://docs.cloud.google.com/logging/docs/view/logging-query-language
https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs
https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview
https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts
https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide
https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restoring
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/list
https://docs.cloud.google.com/sdk/gcloud/reference/logging/metrics/list
https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/list
https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("P06"))
