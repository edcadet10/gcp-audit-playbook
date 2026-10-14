"""Title: Assess runtime secrets and network dependencies
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: deployment history; secret mapping; dependency diagram
Documentation:
https://docs.cloud.google.com/run/docs/configuring/services/secrets
https://docs.cloud.google.com/run/docs/configuring/connecting-vpc
https://docs.cloud.google.com/sdk/gcloud/reference/run/services/list
https://docs.cloud.google.com/sdk/gcloud/reference/functions/list
https://docs.cloud.google.com/sdk/gcloud/reference/secrets/list
https://docs.cloud.google.com/sdk/gcloud/reference/secrets/versions/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("RUN-05"))
