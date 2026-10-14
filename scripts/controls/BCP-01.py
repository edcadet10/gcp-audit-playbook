"""Title: Map recovery objectives to dependencies
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: business impact analysis; dependency map; approved RPO/RTO
Documentation:
https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide
https://docs.cloud.google.com/architecture/framework/reliability
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
https://docs.cloud.google.com/sdk/gcloud/reference/billing/projects/describe
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("BCP-01"))
