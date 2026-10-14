"""Title: Inventory AI services and accountable uses
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: AI use-case register; provider inventory; application data flow
Documentation:
https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform
https://docs.cloud.google.com/vertex-ai/generative-ai/docs/overview
https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/list
https://docs.cloud.google.com/sdk/gcloud/reference/ai/models/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/services/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("AI-01"))
