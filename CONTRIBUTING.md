# Contributing

For technical changes, update the authored catalog in `tools/catalog_data.py` or fixed operation register in `scripts/operations.py`, cite current Google documentation, and identify the observation that could falsify your interpretation. Do not add cloud writes, secret payload reads or arbitrary command/URL inputs to the evidence runner.

Run `python tools/build.py`, `python tests/test_audit.py` and `python tools/validate.py`. For a command change, check local SDK help with `python tools/check_cli.py --sdk-root PATH_TO_GOOGLE_CLOUD_SDK`. Run `python tools/check_sources.py` when references change and review the relevant document contents; HTTP success is not semantic verification.

Document supported scope, focal permissions, pagination, limits, sensitive fields and unsupported evidence. Add meaningful adversarial tests when changing collection behavior. Keep company scope files, credentials and completed workpapers outside this public repository.

Sources: [Google CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference), [asset consistency](https://docs.cloud.google.com/asset-inventory/docs/asset-types), [IAM read permissions](https://docs.cloud.google.com/iam/docs/understanding-roles).
