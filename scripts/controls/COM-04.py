"""Title: Assess regulated workload controls
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: control-package export; contracts; access approval records
Documentation:
https://docs.cloud.google.com/assured-workloads/docs/overview
https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview
https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/describe
https://docs.cloud.google.com/sdk/gcloud/reference/logging/read
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("COM-04"))
