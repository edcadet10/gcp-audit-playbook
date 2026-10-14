"""Title: Assess observability against service objectives
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: SLO register; monitoring policy export; incident sample
Documentation:
https://docs.cloud.google.com/architecture/framework/reliability
https://docs.cloud.google.com/monitoring/slo-monitoring
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/logging/metrics/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("OPS-01"))
