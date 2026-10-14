"""Title: Assess agent tools and retrieval boundaries
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: agent tool inventory; retrieval ACL evidence; prior adversarial evaluations
Documentation:
https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview
https://docs.cloud.google.com/model-armor/overview
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R07-S04"))
