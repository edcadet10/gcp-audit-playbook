"""Title: Review routing sinks and exclusions
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: sink destination IAM; delivery metrics; filter review
Documentation:
https://docs.cloud.google.com/logging/docs/routing/overview
https://docs.cloud.google.com/logging/docs/export/aggregated_sinks
https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("LOG-02"))
