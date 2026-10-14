"""Title: Assess functions and event triggers
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: function inventory; trigger policy; runtime review
Documentation:
https://docs.cloud.google.com/functions/docs/securing/managing-access-iam
https://docs.cloud.google.com/functions/docs/runtime-support
https://docs.cloud.google.com/sdk/gcloud/reference/functions/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("RUN-02"))
