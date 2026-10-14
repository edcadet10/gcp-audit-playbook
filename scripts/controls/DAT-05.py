"""Title: Assess other managed data platforms
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: service-specific configuration exports; native grants; restore evidence
Documentation:
https://docs.cloud.google.com/spanner/docs/security-privacy-compliance
https://docs.cloud.google.com/firestore/docs/security/overview
https://docs.cloud.google.com/bigtable/docs/access-control
https://docs.cloud.google.com/alloydb/docs/overview
https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instances/list
https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("DAT-05"))
