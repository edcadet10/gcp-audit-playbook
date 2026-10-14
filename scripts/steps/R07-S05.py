"""Title: Review AI evaluation and operational oversight
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: evaluation reports; model approvals; AI incident records
Documentation:
https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview
https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-filters
https://docs.cloud.google.com/sdk/gcloud/reference/ai/models/list
https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R07-S05"))
