"""Title: Allocate shared responsibility
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: responsibility matrix; service-owner approvals
Documentation:
https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate
https://docs.cloud.google.com/sdk/gcloud/reference/services/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("GOV-02"))
