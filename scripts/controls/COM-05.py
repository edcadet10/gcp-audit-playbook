"""Title: Review audit evidence and assurance closure
Description: Collect fixed read-only metadata, record gaps, and create the review workpaper.
Required evidence: finding register; quality review; management responses; closure evidence
Documentation:
https://docs.cloud.google.com/architecture/framework/security
https://csrc.nist.gov/pubs/sp/800/53/a/r5/final
https://docs.cloud.google.com/sdk/gcloud/reference/asset/list
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from audit import main
if __name__ == "__main__":
    sys.exit(main("COM-05"))
