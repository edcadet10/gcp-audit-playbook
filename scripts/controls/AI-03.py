"""Title: Review AI endpoint and runtime access
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: AI access review; endpoint architecture; runtime identity mapping
Documentation:
https://docs.cloud.google.com/vertex-ai/docs/general/access-control
https://docs.cloud.google.com/vertex-ai/docs/general/vpc-service-controls
https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("AI-03"))
