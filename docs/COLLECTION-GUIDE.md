# Collection mechanics and assurance limits

The collector implements the read procedures in the [operation register](SCRIPT-OPERATIONS.md). Google defines the command behavior; this document describes the repository's evidence convention and implementation boundaries.

## Scope and fan-out rules

| Operation scope | Expansion | Completeness consideration |
|---|---|---|
| project | Every explicitly approved project, checked against organization ancestry first | Does not discover unauthorized projects |
| organization | Explicit organization number, only when `organization_reads` is true | Can include projects outside the selected workload list; charter must authorize organization-wide metadata |
| folder | Ancestor folders returned for the approved projects | Requires the separate organization-read authorization |
| region / location | Cross-product of approved projects and supplied locations | Missing locations remain an engagement coverage gap |
| constraint | Every approved project and explicitly selected constraint | The selected list must cover the adopted baseline |
| service_account / pool / secret / sql_instance | Validated children from the relevant native project list | Failed parent enumeration becomes DependencyFailed; empty becomes NoTargets |
| keyring | Project and approved location, then validated key rings | No implicit global-to-regional expansion |
| access_policy | Policies enumerated under the approved organization; parent checked | Service perimeter analysis still needs access-level and membership evidence |
| billing | Explicitly approved billing account IDs | Project ancestry does not authorize the billing account |
| SCC | Approved organization and explicitly selected SCC locations | Tier, activation and detector coverage are separately reviewed |
| logs | Approved project, explicit UTC start/end and bounded sample | Reaching the limit is Truncated; all log results remain samples |

References: [project ancestry](https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-ancestors), [asset scopes](https://docs.cloud.google.com/sdk/gcloud/reference/asset/list), [effective constraints](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/describe), [SCC list](https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list), [audit log reads](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read).

## Collection states

| State | What it means | Auditor action |
|---|---|---|
| Collected | Command returned parseable metadata without reported warning or configured sample cap | Reconcile coverage and evaluate content |
| Sampled | An intentionally bounded operation returned fewer than the cap | Limit conclusions to the sample; assess sampling bias |
| Truncated | The configured sample cap was reached | Narrow the period or obtain an approved fuller export; do not claim completeness |
| NeedsReview | A warning or completed run still needs review | Inspect warning, workpapers and required evidence |
| Incomplete | CLI error, malformed output, timeout or incomplete overall run | Preserve error, identify missing evidence and arrange authorized follow-up |
| MissingInput | Required location, constraint, SCC or billing scope absent | Complete approved scope; never guess a customer's target |
| NotAuthorized | Organization-wide read not authorized in scope | Obtain appropriate authorized evidence or qualify the conclusion |
| DependencyFailed | Child read cannot proceed because its parent list failed | Resolve the parent evidence gap |
| NoTargets | A successful parent enumeration returned no children | Reconcile absence independently; this is not a control pass |

Collection state never changes the audit assessment from **Not assessed**. `--plan` reads local metadata only. Supporting templates and workpaper hashes are local operations and do not require installing a cloud SDK or authenticating.

## Read-only boundary

The dispatcher accepts registered operations and generated argument arrays. The scope schema rejects arbitrary flags, command text and endpoints. Mutating cloud verbs are absent, with one explicit semantic exception: `container binauthz policy export` returns the current policy to stdout. No export destination is supplied. Conversely, read APIs may use HTTP POST, including [organizations.getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/getIamPolicy) and [entries.list](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list). Read-only must be assessed from API semantics rather than HTTP method alone.

The SDK environment clears inherited CLOUDSDK overrides, disables API-enablement prompting and uses a dedicated account configuration. The installed SDK's API-enablement code path was inspected during development; this is implementation evidence for the reviewed version, not a permanent API contract. A least-privileged collector without cloud write permissions remains necessary. The bootstrap installs local tools and saves sign-in state, while providers may generate audit records for reads. [Google authentication guidance](https://docs.cloud.google.com/sdk/docs/authenticate) · [IAM role reference](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Evidence handling

Create the evidence parent directory with the organization's approved access controls and storage encryption before collection. The runner refuses output under the public repository, but does not provision enterprise retention, encryption, ACLs or a chain-of-custody system. Metadata can include identities, IP addresses, environment variables, pipeline substitutions and request contents. Do not treat JSON exports as sanitized merely because the operation is read-only. [Audit-log content](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs) · [BigQuery log content](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs).

The runner writes files locally and hashes the initial package. Preserve that package, then create separately versioned analyst workpapers. Rehash or independently record subsequent changes. The final hash manifest cannot authenticate itself; record its hash or signed custody receipt in the engagement's independent evidence register. `index_workpapers.py` indexes only explicitly supplied files and does not assess document authenticity or control effectiveness.

## Coverage that requires additional evidence

| Area | Collected here | Additional evidence needed |
|---|---|---|
| Human identity | GCP allow policies and principal references | Cloud Identity/Workspace/IdP MFA, sessions, group expansion, HR lifecycle |
| Effective access | Ancestor policies, resource allow policies, supported resource metadata | Deny/boundary completeness, custom-role permission details, conditions, data-plane ACLs and evaluated paths |
| Kubernetes | Cluster configuration | Live RBAC/admission/network-policy metadata and prior enforcement evidence; no Secret payloads |
| Storage | Bucket metadata and searchable IAM | Object ACL metadata where applicable, signed-access issuance and transfer evidence |
| BigQuery and other data stores | Supported assets and IAM | Native dataset/database grants, row/column policies, job histories, recovery reports |
| Monitoring | Log metrics and supported assets | Full alerting, SLO, notification and incident records |
| Recovery | Existing snapshots, schedules and SQL backup records | Restore execution, integrity checks, RPO/RTO evidence and business sign-off |
| Delivery | Triggers, build samples, repositories, pipelines and admission policy | Repository branch protections, provenance, exact deployed digests and approval records |
| AI and agents | Endpoints, models, supported datasets, service identities | Application tool permissions, retrieval ACLs, data handling and adversarial evaluation results |
| Compliance | Resource configuration and adopted control mapping | Contracts, applicability decisions, regulatory interpretation and assurance reports |

Each corresponding [control](../controls/CONTROL-CATALOG.md) provides Google product references and an explicit evidence request. Supported assets can omit fields or lag recent changes; use native evidence when the field needed for a decision is absent. [Asset support and consistency](https://docs.cloud.google.com/asset-inventory/docs/asset-types).

## Troubleshooting decisions

If a read is denied, retain the error and review the operation's documented permissions with the granting team. If an API is disabled, record MissingCapability in the analyst's gap register; the raw operation state remains Incomplete. If a region or tier is wrong, correct the approved scope and preserve the earlier run. If an existing SDK lacks a command, review an approved SDK update separately; the collector does not replace an existing installation. If a sample reaches its cap, narrow the interval and reconcile the union, including boundary timestamps and duplicate event identifiers. If a project changes parent during the engagement, stop affected conclusions and repeat scope verification. [CLI install](https://docs.cloud.google.com/sdk/docs/install-sdk) · [logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).
