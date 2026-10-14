"""Title: Assess secret rotation and version lifecycle
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: rotation execution records; version-to-deployment mapping
Documentation:
https://docs.cloud.google.com/secret-manager/docs/rotation-recommendations
https://docs.cloud.google.com/secret-manager/docs/view-secret-version
https://docs.cloud.google.com/sdk/gcloud/reference/secrets/list
https://docs.cloud.google.com/sdk/gcloud/reference/secrets/versions/list
https://docs.cloud.google.com/sdk/gcloud/reference/run/services/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("KEY-02"))
