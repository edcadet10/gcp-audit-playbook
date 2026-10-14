"""Title: Review Cloud Run exposure and identity
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: service architecture; invoker review; region inventory
Documentation:
https://docs.cloud.google.com/run/docs/securing/ingress
https://docs.cloud.google.com/run/docs/authenticating/overview
https://docs.cloud.google.com/sdk/gcloud/reference/run/services/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("RUN-01"))
