"""Title: Assess deny and principal access boundaries
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: deny and boundary policy export; principal-set membership; access analysis
Documentation:
https://docs.cloud.google.com/iam/docs/deny-overview
https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("R02-S02"))
