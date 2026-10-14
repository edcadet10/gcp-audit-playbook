"""Title: Assess host login controls
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: guest account inventory; login policy; access review
Documentation:
https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin
https://docs.cloud.google.com/compute/docs/oslogin
https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/describe
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("CMP-02"))
