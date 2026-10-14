"""Title: Assess AI data use and retention
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: feature and retention matrix; contracts; data approvals
Documentation:
https://docs.cloud.google.com/vertex-ai/generative-ai/docs/data-governance
https://docs.cloud.google.com/vertex-ai/generative-ai/docs/vertex-ai-zero-data-retention
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("AI-02"))
