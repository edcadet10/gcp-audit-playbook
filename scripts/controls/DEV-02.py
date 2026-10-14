"""Title: Assess build identity and secrets
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: build configuration export; secret mapping; identity review
Documentation:
https://docs.cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account
https://docs.cloud.google.com/build/docs/securing-builds/use-secrets
https://docs.cloud.google.com/sdk/gcloud/reference/builds/list
https://docs.cloud.google.com/sdk/gcloud/reference/builds/triggers/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("DEV-02"))
