"""Title: Map obligations to system scope
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: obligation register; scope decisions; control crosswalk
Documentation:
https://docs.cloud.google.com/security/compliance/overview
https://docs.cloud.google.com/architecture/framework/security
https://docs.cloud.google.com/sdk/gcloud/reference/services/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("COM-01"))
