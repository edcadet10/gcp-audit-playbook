"""Title: Review messaging access and data lifecycle
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: messaging data flow; subscriber ownership; retention approval
Documentation:
https://docs.cloud.google.com/pubsub/docs/subscription-properties
https://docs.cloud.google.com/pubsub/docs/authentication
https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/list
https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("RUN-04"))
