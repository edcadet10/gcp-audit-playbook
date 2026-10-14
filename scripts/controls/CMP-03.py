"""Title: Review boot integrity and images
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: image approval; integrity monitoring; vulnerability export
Documentation:
https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm
https://docs.cloud.google.com/compute/docs/images/image-management-best-practices
https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list
https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/list
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("CMP-03"))
