"""Title: Assess VPC Service Controls
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: perimeter design; access-level export; dry-run review
Documentation:
https://docs.cloud.google.com/vpc-service-controls/docs/overview
https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules
https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/list
https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/list
https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("NET-04"))
