"""Title: Assess cost anomalies and abuse readiness
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: anomaly history; cost response procedure; incident sample
Documentation:
https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies
https://docs.cloud.google.com/sdk/gcloud/reference/billing/budgets/list
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("FIN-05"))
