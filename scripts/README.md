# Run the audit evidence scripts

Every control, numbered runbook step and engagement phase has a Python entry script with a title, description and Google documentation. The common runner performs **tool check → missing SDK installation → authentication → scope verification → read operations → evidence workpaper**. No Python packages or PowerShell modules need to be installed separately. [Google installation reference](https://docs.cloud.google.com/sdk/docs/install-sdk) · [Authentication reference](https://docs.cloud.google.com/sdk/docs/authenticate).

## Preview a control without connecting

**Title: Preview the inherited-access procedure.** **Description:** display the read operations, required evidence, assessment criterion and Google references; no installation, authentication or cloud query occurs. [IAM inheritance documentation](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control).

```sh
# Title: Preview inherited-access evidence
# Description: Print the offline plan for IAM-01.
# Reference: https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control
python scripts/controls/IAM-01.py --plan
```

On Windows, the PowerShell bootstrap can show the plan even when Python is unavailable:

```powershell
# Title: Preview a control from PowerShell
# Description: Read the local procedure metadata without preparing tools or signing in.
# Reference: https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control
./scripts/Bootstrap.ps1 -Procedure IAM-01 -Plan
```

## Prepare the approved scope

Copy [scope.example.json](scope.example.json) to an engagement directory outside this repository. Replace every example with approved values. The example is illustrative, not a discovery result or recommended location policy. Use the [charter](../templates/engagement-charter.md) and [scope register](../templates/scope-register.csv).

| Field | Meaning |
|---|---|
| `organization` | Exact organization number; all projects must have this ancestor |
| `account` | Exact authorized Google CLI account; this release supports email-style identities |
| `projects` | Explicit approved project IDs; use separate scope files for different organizations |
| `organization_reads` | Explicit authorization for organization-wide and ancestor-folder reads; default false |
| `billing_accounts` | Independently approved account IDs; an empty list produces a gap for budget collection |
| `regions` | All approved service regions for regional collectors; reconcile against asset and service-owner records |
| `locations` | All approved locations for logging, KMS, Scheduler and Artifact Registry; include `global` only where applicable |
| `scc_locations` | Actual SCC finding locations; an incorrect location can hide expected findings |
| `constraints` | Adopted constraint names without `constraints/`; the example list is not a comprehensive policy baseline |
| `start`, `end` | Historical UTC interval, start inclusive and end exclusive, in `YYYY-MM-DDTHH:MM:SSZ` form |
| `log_limit` | Bounded log sample size, 1–10000; reaching the limit marks Truncated |

Product basis: [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), [asset list scope](https://docs.cloud.google.com/sdk/gcloud/reference/asset/list), [effective organization policy](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/describe), [SCC finding locations](https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list), [log read filters](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read).

## Collect a control's evidence

**Title: Collect inherited-access evidence.** **Description:** verify tools and credentials, check organization ancestry, read the mapped policies and create local evidence and review workpapers. The collector cannot expand directory groups or determine final effective access by itself. [Google policy types](https://docs.cloud.google.com/iam/docs/policy-types).

```sh
# Title: Collect inherited-access evidence
# Description: Run the scoped read procedure and preserve its results outside the repository.
# Reference: https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control
python scripts/controls/IAM-01.py --scope /private/acme/scope.json --output /private/acme/evidence
```

Windows example:

```powershell
# Title: Prepare prerequisites and collect inherited-access evidence
# Description: Bootstrap a supported runtime if needed, then authenticate and collect scoped reads.
# Reference: https://docs.cloud.google.com/sdk/docs/downloads-versioned-archives
./scripts/Bootstrap.ps1 -Procedure IAM-01 -Scope 'C:\Audit\Company\scope.json' -Output 'C:\Audit\Company\evidence'
```

For a numbered fieldwork step use `scripts/steps/R02-S01.py`; for an engagement phase use `scripts/phases/P03.py`. The `P05` phase executes the union of all catalog operations and can produce substantial metadata. Start with the approved pilot and select applicable controls before a full run. Every procedure supports `--plan`; [coverage index](../docs/SCRIPT-COVERAGE.md).

## Prerequisite and authentication sequence

The Python runner requires Python **3.12–3.15**; Google currently supports a broader range, but this toolkit relies on safe archive extraction available in Python 3.12. Windows Bootstrap.ps1 finds a compatible runtime or downloads Google's Windows x64 SDK with bundled Python. On Linux and macOS, use an existing approved Python runtime, such as the one in your administrative environment. The Python collector then locates an existing Google SDK or downloads the pinned 589.0.0 portable archive for Windows x64, Linux x64/Arm64 or macOS x64/Arm64. It verifies Google's recorded SHA-256 before extraction. Unsupported platforms and checksum mismatches stop. An existing SDK is not silently upgraded. [Official installation requirements](https://docs.cloud.google.com/sdk/docs/install-sdk) · [Versioned archives](https://docs.cloud.google.com/sdk/docs/downloads-versioned-archives).

The SDK is invoked through its Python launcher using an argument array with `shell=False`; shell strings are not accepted from the scope file. The portable SDK is kept under `~/.gcp-audit/sdk/`; no system PATH or shell profile is changed. A dedicated account configuration lives under `~/.gcp-audit/accounts/`. Protect this credential directory as you would any administrative sign-in state. [SDK startup behavior](https://docs.cloud.google.com/sdk/gcloud/reference/topic/startup).

The runner inspects the dedicated configuration for credential or API endpoint overrides, checks the expected account and initiates `gcloud auth login ACCOUNT --no-launch-browser` if it is absent. Follow Google's interactive sign-in instructions, then the runner rechecks the account. Each read explicitly supplies `--account`; each project read explicitly supplies `--project`. CLI authentication is distinct from ADC. Existing ambient service-account impersonation and endpoint overrides are deliberately excluded. This release does not bootstrap service-account keys, workforce federation files or delegated impersonation. [CLI authentication](https://docs.cloud.google.com/sdk/docs/authenticate) · [auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login).

All approved project ancestries are checked before workload reads. A mismatch aborts. Folder fan-out comes only from verified project ancestors. Child service-account, pool, secret, SQL and KMS reads use validated parent enumerations. APIs remain disabled if the caller finds them disabled; enabling an API, granting permissions or configuring a quota project belongs to the customer's separately approved preparation process. [Ancestry reference](https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-ancestors) · [asset quota and billing flags](https://docs.cloud.google.com/sdk/gcloud/reference/asset/list).

## Add existing operating workpapers

Cloud metadata cannot prove a restore succeeded, an employee left, an MFA policy covered an external user, or an agent respected retrieval ACLs. Each procedure writes `evidence-requests.csv` with the specific missing evidence. Obtain approved exports/reports and complete the review. A separate local-only script can hash the supplied workpapers against their exact evidence labels. [NIST assessment methods](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) · [Google recovery guidance](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide).

**Title: Index prior restore evidence.** **Description:** read an explicitly prepared CSV manifest, hash files under the approved directory, and report missing required labels. It does not open a cloud connection or determine whether the report proves recovery. Copy [workpapers.example.csv](workpapers.example.csv) and adapt it.

```sh
# Title: Index existing restore workpapers
# Description: Hash approved local reports and record missing evidence types.
# Reference: https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide
python scripts/index_workpapers.py --procedure BCP-03 --manifest /private/acme/workpapers.csv --base /private/acme/documents --output /private/acme/restore-index.json
```

## Read the result

Each run creates a uniquely named directory containing raw JSON, scope, procedure metadata, collection manifest, evidence requests, review candidates, an **unassessed** workpaper and `SHA256SUMS.json`. Review state and stderr warnings before reviewing content. An Incomplete run exits with code 2; a completed acquisition exits 0 and still needs assessment. Files may contain sensitive configuration and log values. Do not commit them to a public repository. [Collection states and limitations](../docs/COLLECTION-GUIDE.md).

No customer organization was queried while developing this toolkit. The [verification record](../research/DISCONFIRMATION.md) separates offline behavior tests, local CLI syntax checks, source review and unperformed live checks. Pilot against your organization's permissions and services before relying on collection coverage.
