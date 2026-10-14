# Google Cloud Audit Playbook

**Independent consultant work program · Version 1.0 · Research reviewed 14 October 2026**

Use this guide to plan, perform, challenge and report a Google Cloud security, governance, compliance-readiness, resilience and operational audit. It contains [100 controls](controls/CONTROL-CATALOG.md), [eight fieldwork runbooks](docs/FIELDWORK-RUNBOOKS.md), [150 executable procedures](docs/SCRIPT-COVERAGE.md), [69 read operations](docs/SCRIPT-OPERATIONS.md) and [18 engagement templates](templates/README.md). The breadth is intended to support tailoring; it does not establish coverage of every Google product, every data-plane permission or every regulatory requirement.

Google documentation is linked beside the relevant procedure and technical interpretation. **The objectives, sampling method, acceptance criteria, severity model and reporting practices are consultant-authored.** The organization must adopt its own requirements. Provider compliance certifications, benchmark scores and successful script runs are inputs to an assessment, rather than an audit opinion. Basis: [Google security, privacy and compliance framework](https://docs.cloud.google.com/architecture/framework/security), [shared responsibility](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate), [NIST assessment procedures](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final).

## Navigate the engagement

| Work product | Where to work |
|---|---|
| Detailed tests, evidence and contrary explanations | [Control catalog](controls/CONTROL-CATALOG.md) |
| Investigations spanning multiple services | [Fieldwork runbooks](docs/FIELDWORK-RUNBOOKS.md) |
| Installation, sign-in and execution | [Script instructions](scripts/README.md) |
| Scope expansion, evidence states and limitations | [Collection guide](docs/COLLECTION-GUIDE.md) |
| Exact command and focal read permissions | [Operation register](docs/SCRIPT-OPERATIONS.md) |
| Technical foundations and independent frameworks | [Source register](references/SOURCES.md) |
| Charter, assessment, findings and report | [Templates](templates/README.md) |
| Tests that challenged this toolkit | [Disconfirmation record](research/DISCONFIRMATION.md) |

## Engagement boundaries

The supported collector targets an explicitly named organization and an approved list of projects. It verifies every project's organization ancestry before service collection. Organization-wide IAM, asset inventory, firewall, SCC and access-policy reads additionally require `organization_reads: true` in the engagement scope. Billing accounts are independently approved scopes. Regional lists cover only the supplied regions or locations; global does not mean every region. Standalone projects, multiple organizations, sovereign/universe endpoints, workforce principal identifiers that do not fit the provided account validation, impersonated collectors and private connectivity requirements need a separately reviewed extension or separate engagement runs. Basis: [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), [project ancestry command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-ancestors), [billing associations](https://docs.cloud.google.com/billing/docs/how-to/view-linked).

This is a read-only audit. It takes concrete action by acquiring configuration, reconciling populations, recording errors, producing review candidates and creating workpapers. It does not enable APIs, grant access, alter policies, run SQL jobs, read secret payloads, download storage objects, launch scans, restore systems, invoke agents, send test alerts or remediate findings. Existing exercise records and authorized metadata exports provide operating evidence. New active tests require a separate agreed test plan outside this collector. The distinction follows the difference between inspectable configuration and exercised behavior in [Google disaster recovery guidance](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide) and [NIST assessment methods](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final).

Local effects are expected: the bootstrap may download the official SDK, authentication stores local credentials, and evidence files are created. Reads can generate provider audit records, consume quotas and incur service-dependent costs. Review logging sensitivity before collection because metadata and log payloads can include identities, request values or SQL text. Read-only describes cloud configuration, not an absence of every side effect. Basis: [CLI authentication](https://docs.cloud.google.com/sdk/docs/authenticate), [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit), [BigQuery audit records](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs).

## P01 — Authorize and scope

**Script title:** Authorize and scope. **Description:** [P01.py](scripts/phases/P01.py) gathers project ownership and responsibility evidence and creates the authorization workpaper. Use plan mode before access is approved. Map this phase to GOV-01, GOV-02 and COM-01.

Record the legal entity, organization numbers, folders, project IDs and numbers, billing accounts, environments, geographic requirements, material services and review period in the [charter](templates/engagement-charter.md). Identify the sponsor, audit lead, evidence custodian, cloud platform lead, identity owner, SOC, data owners, SRE, finance and compliance representatives. Agree the deliverables, escalation path, distribution list, evidence retention and acceptance process.

Tailor all 100 controls. Mark a control Not applicable only with an evidenced reason and reviewer approval. For an unused service, reconcile service inventory, asset inventory and owner confirmation. A disabled API or permission-denied response is not evidence that the service is absent. Include inherited controls in host projects, security projects, key projects, shared networks, external directories and source repositories even if the application resides elsewhere. Basis: [enterprise foundations](https://docs.cloud.google.com/architecture/blueprints/security-foundations), [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), [Cloud Asset Inventory supported types](https://docs.cloud.google.com/asset-inventory/docs/asset-types).

Agree whether the assignment assesses point-in-time design, operating effectiveness over a period, or both. A retrospective audit must not present today's state as evidence of the entire period. Request historical changes, approvals and operating samples early. Basis: [asset history and consistency](https://docs.cloud.google.com/asset-inventory/docs/asset-types), [NIST assessment planning](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final).

## P02 — Prepare tooling and access

**Script title:** Prepare tooling and access. **Description:** [P02.py](scripts/phases/P02.py) executes the common prerequisite sequence and collects scope and access evidence. Review its offline plan first.

Use a dedicated audit workstation or approved administrative environment with Python 3.12–3.15. Windows users can start with [Bootstrap.ps1](scripts/Bootstrap.ps1), which can obtain Google's bundled Python if necessary. Each collection entry point verifies SDK availability, installs a checksum-verified portable SDK when absent, checks the dedicated CLI configuration, authenticates the exact account, then verifies project ancestry. No pip modules are required. CLI credentials and Application Default Credentials are distinct; this toolkit uses CLI authentication. Basis: [official SDK installation](https://docs.cloud.google.com/sdk/docs/install-sdk), [versioned archives](https://docs.cloud.google.com/sdk/docs/downloads-versioned-archives), [CLI authentication](https://docs.cloud.google.com/sdk/docs/authenticate).

Build a least-privilege [access request](templates/access-request.csv) from the selected operations. Relevant read-role families include Cloud Asset Viewer, Browser, Security Reviewer, Organization Policy Viewer, Logs Viewer, Private Logs Viewer and service-specific viewers; these are candidates to evaluate, not a universal bundle to grant. Some general viewers expose customer data or more metadata than intended. The granting team must inspect current role contents and approve scopes and expiry. Do not give the collector Owner, Editor, API enablement, IAM modification or secret payload permissions to resolve an error. Basis: [IAM role definitions](https://docs.cloud.google.com/iam/docs/understanding-roles), [asset permissions](https://docs.cloud.google.com/asset-inventory/docs/roles-permissions), [logging access control](https://docs.cloud.google.com/logging/docs/access-control).

Pilot on one approved representative project. Record SDK version, all denied reads, missing APIs, quota-project requirements and network limitations. Missing APIs remain gaps for the owner to address under a separate change; the runner suppresses API-enablement prompting. Expand only after the scope and evidence behavior are understood. Installation and API compatibility have not been tested against a customer organization during creation of this repository.

## P03 — Reconcile the population

**Script title:** Reconcile the population. **Description:** [P03.py](scripts/phases/P03.py) gathers organization inventory when authorized, project metadata and billing associations for comparison with independent records.

Create a [coverage matrix](templates/coverage-matrix.csv) by project, service, resource type and region. Join Cloud Asset Inventory to billing/finance records, the CMDB, application ownership and service-native lists. Explain every difference: scope exclusion, deletion timing, indexing delay, insufficient permissions, unsupported resource type or missing native evidence. Keep expected counts and observed counts separate.

Cloud Asset Inventory has supported-type and method limitations and eventual consistency; historical data is best-effort. A successful empty list describes the response to that particular request. It does not prove the organization's total population is empty. Region lists are an explicit input and must be reconciled to asset locations and application records before service absence is concluded. Basis: [supported asset types and consistency](https://docs.cloud.google.com/asset-inventory/docs/asset-types), [asset listing semantics](https://docs.cloud.google.com/sdk/gcloud/reference/asset/list).

Use [R01](docs/FIELDWORK-RUNBOOKS.md#r01--population-and-evidence-completeness) to investigate coverage. Document unsupported products in the extension backlog with a named owner, native read interface and evidence contract. Relevant examples include database-native permissions, Kubernetes RBAC, object ACLs, directory memberships, monitoring policies and AI application tool definitions.

## P04 — Establish the baseline and sample

**Script title:** Establish the baseline and sample. **Description:** [P04.py](scripts/phases/P04.py) collects organization-policy evidence and creates baseline and sampling requests.

Record the adopted requirements before testing. Sources can include approved internal standards, architecture decisions, contracts, Google guidance and a properly obtained current CIS benchmark. Google describes product behavior and recommendations; it does not set your company's universal RTO, log retention, key rotation interval or risk appetite. Never assign invented benchmark control numbers or claim CIS conformance from this catalog. Basis: [Google security framework](https://docs.cloud.google.com/architecture/framework/security), [official CIS GCP benchmark page](https://www.cisecurity.org/benchmark/google_cloud_computing_platform), [CSA Cloud Controls Matrix](https://cloudsecurityalliance.org/research/cloud-controls-matrix).

Stratify the population by criticality, data sensitivity, exposure, privilege, region, architecture, change frequency and incident history. Inspect all known high-impact exceptions and privileged access paths where feasible. Select representative operating samples across the period and include contrary cases: terminated users, denied requests, failed backups, muted findings and emergency changes. Record the population, method, sample size, coverage and rationale in the [sampling plan](templates/sampling-plan.csv). A convenience sample supports conclusions about the sampled items; it does not justify a statistical prevalence estimate. This is the playbook's method, informed by [NIST assessment guidance](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final).

## P05 — Collect configuration evidence

**Script title:** Collect configuration evidence. **Description:** [P05.py](scripts/phases/P05.py) executes the combined operation set for the catalog; use individual control scripts for a tailored engagement or pilot. The plan identifies all required scopes and workpapers.

Run selected scripts into an access-controlled location outside the repository. Preserve the scope file, UTC timestamps, SDK version, exact generated command arguments, per-operation state, errors, hashes and evidence request list. Capture an engagement identifier in your evidence register and retain provider request/ticket references when available. The collector writes raw JSON and a final hash manifest. A hash supports later change detection; it does not prove source authenticity, authorized custody or completeness. Those require the [custodian and evidence register](templates/evidence-register.csv).

The operation register identifies focal permissions and references for every command. Uncapped list commands use gcloud pagination. Audit logs are deliberately sampled within the explicit UTC interval, and builds use a bounded sample. Reaching a cap is reported as Truncated; even a smaller log/build result remains Sampled. Warnings produce a review requirement. Nonzero exit, malformed JSON, missing required inputs and failed dependencies are preserved as gaps. Basis: [gcloud list limits](https://docs.cloud.google.com/sdk/gcloud/reference/asset/list), [logging read filters and limits](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read), [Cloud Build list](https://docs.cloud.google.com/sdk/gcloud/reference/builds/list).

Follow the control's specific review procedure. For IAM, combine ancestors, resource grants, conditions, group membership, deny and principal access boundaries. For storage, distinguish IAM from ACLs, signed URLs and inherited public access prevention. For networks, resolve effective policy and target attachment before asserting reachability. Basis: [IAM policy types](https://docs.cloud.google.com/iam/docs/policy-types), [storage public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention), [firewall policy evaluation](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview).

## P06 — Review operating effectiveness

**Script title:** Review operating effectiveness. **Description:** [P06.py](scripts/phases/P06.py) collects bounded logs, detector evidence and existing backup records, with requests for historical operating workpapers.

For each selected control, distinguish an enabled setting from a functioning process. Trace a known historical approved event from its originating ticket through source logging, routing, retained destination and alert response. Review prior restore reports for data integrity, elapsed time, dependency recovery and business acceptance. Trace onboarding/offboarding, key rotation, patching and incident closure to actual execution evidence. Use [R04](docs/FIELDWORK-RUNBOOKS.md#r04--logging-from-source-to-retained-evidence) and [R06](docs/FIELDWORK-RUNBOOKS.md#r06--recovery-without-changing-production).

Data Access logs are not universally enabled by default, and inherited audit configurations and exemptions matter. A configured sink does not establish successful destination delivery. Backup metadata does not establish successful application recovery. If historical evidence is unavailable, report a limitation or evidence gap rather than simulating a successful test. Basis: [audit log categories and defaults](https://docs.cloud.google.com/logging/docs/audit), [Data Access configuration](https://docs.cloud.google.com/logging/docs/audit/configure-data-access), [log routing](https://docs.cloud.google.com/logging/docs/routing/overview), [disaster recovery planning](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide).

## P07 — Challenge the findings

**Script title:** Challenge findings. **Description:** [P07.py](scripts/phases/P07.py) collects evidence relevant to effective IAM and storage access and opens a quality-review workpaper.

Write the claim, then identify one observation that would make it false. Look for that observation in the smallest appropriate evidence set. A public IAM binding may be neutralized by a relevant service control; a private network may still expose an application through another path; an empty finding list may reflect an activation or location gap. Retain counterevidence and explain why it changes or does not change the conclusion. Each control supplies a concrete falsification probe.

Use a second reviewer for critical/high findings and any conclusion that depends on complicated inheritance, business impact or incomplete evidence. Resolve facts with the owner and preserve disagreements. Keep inferred attack paths separate from demonstrated events. The collector's basic-role/public-binding detections are **review candidates**, not automatic vulnerabilities. Basis: [principal access boundaries](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies), [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention), [SCC coverage and service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers).

## P08 — Prioritize and agree actions

**Script title:** Prioritize and agree actions. **Description:** [P08.py](scripts/phases/P08.py) gathers findings metadata and produces management-response and ownership requests.

Document condition, adopted criterion, cause, credible impact, affected population, evidence and uncertainty. Agree likelihood and business impact with the risk owner. The following scale is a starting method, not a Google-imposed severity standard:

| Rating | Suggested engagement interpretation | Handling |
|---|---|---|
| Critical | Credible path to immediate material compromise or catastrophic service/data loss | Escalate promptly through the charter's named contact |
| High | Material control failure affecting sensitive data, privilege or critical recovery | Prioritize an owned action and interim controls |
| Medium | Meaningful weakness with constrained exposure or compensating controls | Schedule correction with measurable validation |
| Low | Limited exposure or operational hygiene deficiency | Assign a proportionate improvement |
| Observation | Improvement or uncertainty without enough evidence for a control failure | Track the evidence needed or improvement decision |

Record confidence independently: high, medium or low, with a reason. An evidence gap can itself be material, but does not prove the underlying asset is compromised. Negotiate due dates rather than embedding universal repair deadlines. Management may accept residual risk with accountable approval and expiry. Basis: [NIST assessment procedures](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final), [SCC finding management](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings).

## P09 — Report and hand over

**Script title:** Report and hand over. **Description:** [P09.py](scripts/phases/P09.py) creates the reporting evidence requests and unassessed quality-review workpaper. The auditor completes and approves the report.

Deliver an executive report, technical findings, control-assessment register, coverage/limitations appendix, evidence index and remediation plan. State organization/project scope, dates, criteria, material exclusions and the distinction between design and operating effectiveness. Summarize systemic themes with concrete examples and owners. Link every finding to evidence IDs and source criteria; link every recommendation to the failed control and intended outcome. Avoid a numeric score that masks untested controls.

If a score is requested, disclose numerator, denominator, weighting and treatment of Not assessed, Not applicable and evidence gaps. Show coverage alongside effectiveness. A score over tested controls must never be presented as coverage of all expected controls. Provide the private evidence package through the agreed channel, retain access and transfer records, and follow the retention decision. Basis: [NIST assessment planning and results](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final), [Google shared responsibility](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate).

## P10 — Retest and close

**Script title:** Retest and close. **Description:** [P10.py](scripts/phases/P10.py) acquires current relevant metadata and requests independent closure and restore evidence.

Re-run the affected control's script after the approved change, compare against the original evidence and repeat the original falsifying test. Confirm both the specific correction and related dependencies. For process failures, obtain an appropriate operating period or exercise result. Closing a change ticket is not enough to close the audit finding. Record verified closure, accepted residual risk or remaining work, with the reviewer and date. Basis: [NIST assessments](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final), [Google incident learning](https://docs.cloud.google.com/architecture/framework/operational-excellence/learn-from-failures).

## Assessment rules

| Audit status | Required basis |
|---|---|
| Not assessed | Default state; no opinion has been issued |
| Meets criterion | Sufficient relevant evidence supports the adopted criterion for the stated scope and period |
| Partially meets | Specific portions meet the criterion and defined exceptions remain |
| Does not meet | Evidence demonstrates a failure against an adopted applicable criterion |
| Evidence gap | The necessary evidence is unavailable, unreliable or incomplete |
| Not applicable | Applicability was evaluated and exclusion is justified and approved |

Record design and operating results separately. Collected, Sampled and NeedsReview are **collection states**, never audit opinions. A missing service, empty array, permission error or unsupported type must receive the disposition appropriate to its evidence. The method is informed by [NIST assessment procedures](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final); the exact labels are this toolkit's convention.

## Tailoring and maintenance

For regulated industries, add the exact adopted legal/contractual requirement and validate service eligibility and control packages with the accountable team. For acquisitions and multi-organization estates, use separate scope files and reconcile cross-organization access and data transfers. For AI, inspect application-level retrieval and tool authorization as well as cloud IAM; the cloud inventory cannot establish application behavior. Basis: [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview), [agent platform documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview), [Model Armor](https://docs.cloud.google.com/model-armor/overview).

Revisit documentation, SDK syntax, service tiers and supported asset types before every engagement. At research time, Google's SCC documentation describes an Enterprise-tier shutdown on 21 May 2027; budget documentation distinguishes alerts-only from supported spend-cap budgets; some Vertex AI documentation now uses Gemini Enterprise Agent Platform naming while existing API and CLI names remain in use. Do not rely on old names or generic claims without checking the actual deployment. Basis: [SCC tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers), [budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets), [AI data governance](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/data-governance).

The [CIS benchmark](https://www.cisecurity.org/benchmark/google_cloud_computing_platform), [CSA CCM](https://cloudsecurityalliance.org/research/cloud-controls-matrix), [NIST SP 800-53A](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final), [NIST SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), [Google SRE book](https://sre.google/sre-book/table-of-contents/) and [OWASP LLM project](https://owasp.org/www-project-top-10-for-large-language-model-applications/) provide independent or specialist perspectives. This repository does not reproduce a full licensed benchmark or claim a verified one-to-one framework crosswalk; the mapping template is deliberately blank until a qualified reviewer adopts a specific version.
