# Fieldwork runbooks

Eight five-step investigations. Each step has an executable read-only evidence procedure. Run from the repository root; plan mode is offline. Human review and requested workpapers are necessary to complete the step. See [collection instructions](../scripts/README.md) and [assessment rules](../PLAYBOOK.md#assessment-rules).

## R01 — Population and evidence completeness

### Step 1: Establish organizational ownership and scope

**Procedure:** Reconcile organization, folders, project numbers, business owners, lifecycle state and billing inventory with the signed scope. Record separately projects visible to the collector and the expected population.

**Acceptable evidence:** signed charter; independent project register; population reconciliation.

**Challenge:** Find one billing-linked or CMDB project absent from the asset export and investigate visibility before declaring it retired.

**Decision criterion:** Every expected project has a disposition, owner and applicable control set; unexplained inventory gaps remain open.

**Script:** [R01-S01.py](../scripts/steps/R01-S01.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Establish organizational ownership and scope
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R01-S01.py --plan
```

**Google references:** [About resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) · [Asset types](https://docs.cloud.google.com/asset-inventory/docs/asset-types)

### Step 2: Review project lifecycle and shutdown

**Procedure:** Inspect labels, lifecycle states, enabled services and billing links. Trace creation approval, handover and one past retirement to retained evidence and revoked access.

**Acceptable evidence:** creation and retirement tickets; retention approvals.

**Challenge:** Select a retired project whose data export, billing liability or service account remains unexplained.

**Decision criterion:** Creation and retirement records reconcile to inventory without orphaned ownership, data or access.

**Script:** [R01-S02.py](../scripts/steps/R01-S02.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Review project lifecycle and shutdown
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R01-S02.py --plan
```

**Google references:** [Create projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) · [Create and update labels for projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels)

### Step 3: Reconcile billing and project accountability

**Procedure:** Read billing associations for approved projects and compare with finance-approved account and cost-center records. Billing account scope requires explicit independent approval.

**Acceptable evidence:** finance project register; billing account approvals; cost allocation.

**Challenge:** A project absent from the operations register still produces charges.

**Decision criterion:** Every billed project has an accountable owner, cost center and approved billing association.

**Script:** [R01-S03.py](../scripts/steps/R01-S03.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Reconcile billing and project accountability
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R01-S03.py --plan
```

**Google references:** [Manage your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account) · [View projects linked to Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/how-to/view-linked)

### Step 4: Review resource locations and sovereignty

**Procedure:** Map actual resource locations, backups and service-supported location constraints to contractual requirements. Identify global services and processing paths that need separate analysis.

**Acceptable evidence:** data-location register; contract requirements; service exceptions.

**Challenge:** A primary region is approved while backups, logs or a global endpoint fall outside the reviewed requirement.

**Decision criterion:** Approved location requirements apply to the relevant resource types and operational copies; unsupported services are documented.

**Script:** [R01-S04.py](../scripts/steps/R01-S04.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Review resource locations and sovereignty
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R01-S04.py --plan
```

**Google references:** [Restrict resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) · [Overview of Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview)

### Step 5: Review audit evidence and assurance closure

**Procedure:** Check findings against criteria, affected population, reproducible evidence and contrary explanations. Require owners, agreed actions, due dates, risk acceptance and independent retest before closure.

**Acceptable evidence:** finding register; quality review; management responses; closure evidence.

**Challenge:** A high-severity finding relies on truncated data or is marked closed after a change ticket without retest evidence.

**Decision criterion:** The report distinguishes observed facts, inference, limitations and management decisions; no unsupported compliance claim remains.

**Script:** [R01-S05.py](../scripts/steps/R01-S05.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Review audit evidence and assurance closure
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R01-S05.py --plan
```

**Google references:** [Well-Architected Framework: Security, privacy, and compliance pillar](https://docs.cloud.google.com/architecture/framework/security) · [SP 800-53A Rev. 5, Assessing Security and Privacy Controls in Information Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final)

## R02 — Effective privilege and machine identity

### Step 1: Resolve inherited privileged access

**Procedure:** Read organization, all ancestor folders, project and resource policies. Expand groups through authorized directory evidence and inspect custom role permissions, conditions, deny and principal boundary policies.

**Acceptable evidence:** group membership export; effective-access workpaper; access approvals.

**Challenge:** A harmless-looking project policy conceals an organization-level group with broad access; trace a nested member.

**Decision criterion:** Each effective privileged access path is justified, assigned to an accountable identity and periodically reviewed.

**Script:** [R02-S01.py](../scripts/steps/R02-S01.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Resolve inherited privileged access
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R02-S01.py --plan
```

**Google references:** [Using resource hierarchy for access control](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control) · [IAM policy types](https://docs.cloud.google.com/iam/docs/policy-types) · [Overview of IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview)

### Step 2: Assess deny and principal access boundaries

**Procedure:** Reconcile allow bindings with explicit deny rules, exceptions, principal-set bindings and boundary enforcement versions using resource metadata and owner exports when not inventoried.

**Acceptable evidence:** deny and boundary policy export; principal-set membership; access analysis.

**Challenge:** Find a boundary that does not cover the permission relied on by the proposed compensating control.

**Decision criterion:** Access analysis includes applicable allow, deny and boundary effects; unsupported permission coverage is acknowledged.

**Script:** [R02-S02.py](../scripts/steps/R02-S02.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Assess deny and principal access boundaries
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R02-S02.py --plan
```

**Google references:** [Deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) · [Principal access boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies)

### Step 3: Inventory service account ownership

**Procedure:** Map service accounts, default identities, attached workloads and impersonation grants to owners and intended permissions. Inspect both use and administration of each identity.

**Acceptable evidence:** service account register; application ownership; impersonation analysis.

**Challenge:** A low-privileged deployer can attach or impersonate an overprivileged runtime identity.

**Decision criterion:** Privileged machine identities have specific purposes and accountable owners; default identities receive no unexplained broad access.

**Script:** [R02-S03.py](../scripts/steps/R02-S03.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Inventory service account ownership
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R02-S03.py --plan
```

**Google references:** [Best practices for using service accounts securely](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts) · [Service account impersonation](https://docs.cloud.google.com/iam/docs/service-account-impersonation)

### Step 4: Validate federation trust boundaries

**Procedure:** Inspect workload pools and provider issuer, audience, attribute mapping and condition. Trace external subject claims to IAM grants and repository or cloud ownership.

**Acceptable evidence:** federation design; provider export; subject-to-role mapping.

**Challenge:** Test the reasoning with a forked repository or different external tenant that might satisfy a weak attribute condition; do not request tokens.

**Decision criterion:** Trust restricts intended external tenants and subjects; broad pools and impersonation grants are justified.

**Script:** [R02-S04.py](../scripts/steps/R02-S04.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Validate federation trust boundaries
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R02-S04.py --plan
```

**Google references:** [Configure Workload Identity Federation with deployment pipelines](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines) · [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation)

### Step 5: Inspect service account escalation paths

**Procedure:** Review serviceAccountUser, token creation, workload deployment and project-level permissions together. Trace who can modify code running as a sensitive service identity.

**Acceptable evidence:** privilege graph; deployment approvals.

**Challenge:** Find an identity that cannot read data directly but can deploy code as an identity that can.

**Decision criterion:** Privilege reviews cover combined deployment and identity capabilities, including cross-project service accounts.

**Script:** [R02-S05.py](../scripts/steps/R02-S05.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Inspect service account escalation paths
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R02-S05.py --plan
```

**Google references:** [Roles for service account authentication](https://docs.cloud.google.com/iam/docs/service-account-permissions) · [Best practices for using service accounts securely](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts)

## R03 — Public exposure and data paths

### Step 1: Resolve effective firewall exposure

**Procedure:** Review VPC rules, hierarchical policies, target tags or service accounts, priorities, direction and disabled status. Join to routes, instance interfaces and approved service exposure.

**Acceptable evidence:** effective-firewall export; network exposure register.

**Challenge:** A deny is shadowed by a higher-priority allow, or an apparent allow targets no instances.

**Decision criterion:** Public and lateral paths are justified after effective rule evaluation; a single broad rule is a review candidate, not automatic proof of reachability.

**Script:** [R03-S01.py](../scripts/steps/R03-S01.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Resolve effective firewall exposure
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R03-S01.py --plan
```

**Google references:** [Firewall policies and rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) · [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls)

### Step 2: Assess external application protection

**Procedure:** Map external forwarding rules to backend services and Cloud Armor policy attachment. Review rule action, preview mode, bypass endpoints, TLS configuration and owner-approved exposure.

**Acceptable evidence:** load-balancer architecture; TLS policy export; exception register.

**Challenge:** A protective policy exists but is unattached or all material rules run in preview.

**Decision criterion:** Each critical public service has the agreed protections on its actual serving path.

**Script:** [R03-S02.py](../scripts/steps/R03-S02.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Assess external application protection
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R03-S02.py --plan
```

**Google references:** [Security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-overview) · [SSL policies overview](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts)

### Step 3: Review Cloud Run exposure and identity

**Procedure:** Inspect service ingress, revision configuration, authentication/IAM and runtime identities across all approved regions. Review direct service URLs and load-balancer paths together.

**Acceptable evidence:** service architecture; invoker review; region inventory.

**Challenge:** A load balancer is protected while the underlying service remains invokable directly.

**Decision criterion:** Public invocation and runtime privileges match the application's approved exposure.

**Script:** [R03-S03.py](../scripts/steps/R03-S03.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Review Cloud Run exposure and identity
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R03-S03.py --plan
```

**Google references:** [Restrict network endpoint ingress for Cloud Run services and instances](https://docs.cloud.google.com/run/docs/securing/ingress) · [Authentication overview](https://docs.cloud.google.com/run/docs/authenticating/overview)

### Step 4: Assess public and external bucket access

**Procedure:** Join bucket metadata, IAM bindings, inherited public access prevention and approved external-sharing uses. If uniform access is off, request object ACL metadata separately; do not download objects.

**Acceptable evidence:** sharing register; ACL metadata when applicable; signed URL governance.

**Challenge:** Public prevention is enabled but long-lived signed URLs or legacy object ACL exposure are absent from the review.

**Decision criterion:** Public and external access is intentional and governed across IAM, ACL and signed-access paths.

**Script:** [R03-S04.py](../scripts/steps/R03-S04.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Assess public and external bucket access
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R03-S04.py --plan
```

**Google references:** [Public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention) · [Signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls)

### Step 5: Review BigQuery access and fine-grained controls

**Procedure:** Use dataset and table asset metadata plus approved exports of row policies, policy tags, masking rules and authorized views. Trace inherited IAM, dataset ACLs and data-sharing links.

**Acceptable evidence:** dataset ACL export; row and column policy metadata; sharing register.

**Challenge:** An authorized view or broad dataset grant bypasses the intended interpretation of a masking control.

**Decision criterion:** Sensitive data access is justified at dataset, table, row and column levels where required; metadata-only coverage is documented.

**Script:** [R03-S05.py](../scripts/steps/R03-S05.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Review BigQuery access and fine-grained controls
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R03-S05.py --plan
```

**Google references:** [Introduction to BigQuery row-level security](https://docs.cloud.google.com/bigquery/docs/row-level-security-intro) · [Introduction to column-level access control](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro) · [Authorized views](https://docs.cloud.google.com/bigquery/docs/authorized-views)

## R04 — Logging from source to retained evidence

### Step 1: Verify Data Access audit coverage

**Procedure:** Read organization, ancestor-folder and project auditConfigs, service exceptions and exempted principals. Map enabled services to the required ADMIN_READ, DATA_READ and DATA_WRITE coverage.

**Acceptable evidence:** service logging matrix; effective auditConfig analysis.

**Challenge:** An empty project auditConfig is interpreted without inspecting inherited settings, or an exemption suppresses the chosen principal.

**Decision criterion:** The adopted logging matrix is effectively configured and inherited exemptions are explicitly reviewed.

**Script:** [R04-S01.py](../scripts/steps/R04-S01.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Verify Data Access audit coverage
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R04-S01.py --plan
```

**Google references:** [Cloud Audit Logs overview](https://docs.cloud.google.com/logging/docs/audit) · [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)

### Step 2: Review routing sinks and exclusions

**Procedure:** Inspect project and organization sinks, inclusion and exclusion filters, destination ownership and writer grants. Review intercepting behavior and aggregated child scope.

**Acceptable evidence:** sink destination IAM; delivery metrics; filter review.

**Challenge:** A central sink exists but its writer lacks destination access or its filter excludes the target event.

**Decision criterion:** Required events reach approved destinations without unintended filtering or privilege gaps.

**Script:** [R04-S02.py](../scripts/steps/R04-S02.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Review routing sinks and exclusions
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R04-S02.py --plan
```

**Google references:** [Route log entries](https://docs.cloud.google.com/logging/docs/routing/overview) · [Collate and route organization- and folder-level logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks)

### Step 3: Assess retention location and protected access

**Procedure:** Inspect log bucket retention, location, access restrictions and lock state across all used locations. Reconcile SIEM and archive retention outside Cloud Logging.

**Acceptable evidence:** retention matrix; SIEM settings; bucket access review.

**Challenge:** Only global buckets were checked while a regional bucket holds the relevant events for a shorter period.

**Decision criterion:** The retention and access model satisfies the adopted evidence requirements across every copy.

**Script:** [R04-S03.py](../scripts/steps/R04-S03.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Assess retention location and protected access
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R04-S03.py --plan
```

**Google references:** [Configure log buckets](https://docs.cloud.google.com/logging/docs/buckets) · [Route log entries](https://docs.cloud.google.com/logging/docs/storage)

### Step 4: Prove an existing event's end-to-end trace

**Procedure:** Select a known historical approved administrative or data event from a ticket. Trace it through source logging, sink routing, destination and detection within a bounded UTC window.

**Acceptable evidence:** known-event record; source and destination evidence; timing comparison.

**Challenge:** The source event is present but disappears after routing, or the sampled log window omits the ticket time.

**Decision criterion:** The specific event is attributable and retrievable with expected fields and timing; the sample's limits are documented.

**Script:** [R04-S04.py](../scripts/steps/R04-S04.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Prove an existing event's end-to-end trace
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R04-S04.py --plan
```

**Google references:** [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language) · [Understanding audit logs](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs)

### Step 5: Assess integrity and evidence visibility

**Procedure:** Review log administration, private-log viewing, deletion and sink modification privileges. Reconcile coverage counts and missing-access errors before concluding about activity.

**Acceptable evidence:** evidence-access matrix; error register; log administrator review.

**Challenge:** The collector receives no private entries because it lacks Private Logs Viewer permissions.

**Decision criterion:** The audit can explain who can read or affect evidence and where visibility is incomplete.

**Script:** [R04-S05.py](../scripts/steps/R04-S05.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Assess integrity and evidence visibility
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R04-S05.py --plan
```

**Google references:** [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control) · [Best practices for Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit/best-practices)

## R05 — Sensitive data and cryptographic dependencies

### Step 1: Assess classification and data discovery

**Procedure:** Compare data classification and existing discovery/profile results with storage, databases, datasets and AI inventories. Inspect coverage, location, job recency and exclusions without initiating scans.

**Acceptable evidence:** classification register; discovery profile export; coverage reconciliation.

**Challenge:** A current discovery dashboard excludes a new project, unstructured store or encrypted dataset.

**Decision criterion:** Classification covers the material data population, with explicit unsupported or unscanned areas.

**Script:** [R05-S01.py](../scripts/steps/R05-S01.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Assess classification and data discovery
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R05-S01.py --plan
```

**Google references:** [Overview of sensitive data discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles)

### Step 2: Inspect bucket encryption and location

**Procedure:** Map storage location, default key references and object-encryption evidence to requirements. A default CMEK setting alone does not prove all existing objects use that key.

**Acceptable evidence:** encryption coverage export; location requirements; key dependency map.

**Challenge:** An object predates the default key change or a key's location conflicts with the assumed recovery design.

**Decision criterion:** Location and encryption requirements are supported for current and historical data populations.

**Script:** [R05-S02.py](../scripts/steps/R05-S02.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Inspect bucket encryption and location
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R05-S02.py --plan
```

**Google references:** [Customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) · [Bucket locations](https://docs.cloud.google.com/storage/docs/locations)

### Step 3: Review BigQuery access and fine-grained controls

**Procedure:** Use dataset and table asset metadata plus approved exports of row policies, policy tags, masking rules and authorized views. Trace inherited IAM, dataset ACLs and data-sharing links.

**Acceptable evidence:** dataset ACL export; row and column policy metadata; sharing register.

**Challenge:** An authorized view or broad dataset grant bypasses the intended interpretation of a masking control.

**Decision criterion:** Sensitive data access is justified at dataset, table, row and column levels where required; metadata-only coverage is documented.

**Script:** [R05-S03.py](../scripts/steps/R05-S03.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Review BigQuery access and fine-grained controls
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R05-S03.py --plan
```

**Google references:** [Introduction to BigQuery row-level security](https://docs.cloud.google.com/bigquery/docs/row-level-security-intro) · [Introduction to column-level access control](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro) · [Authorized views](https://docs.cloud.google.com/bigquery/docs/authorized-views)

### Step 4: Assess KMS purpose and separation of duties

**Procedure:** Inspect key rings, algorithms, protection level, IAM and encrypt/decrypt versus administration permissions. Map key projects and service agents to protected resources.

**Acceptable evidence:** key inventory; custody matrix; access review.

**Challenge:** A data administrator can also grant themselves decryption access to the same sensitive dataset.

**Decision criterion:** Key administration and use align with the approved custody and separation model.

**Script:** [R05-S04.py](../scripts/steps/R05-S04.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Assess KMS purpose and separation of duties
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R05-S04.py --plan
```

**Google references:** [Separation of duties](https://docs.cloud.google.com/kms/docs/separation-of-duties) · [Access control with IAM](https://docs.cloud.google.com/kms/docs/iam)

### Step 5: Review key lifecycle and availability

**Procedure:** Review primary versions, rotation and destruction schedule evidence. Reconcile disabled or pending-destruction versions with active data and backup dependencies.

**Acceptable evidence:** key-version metadata export; destruction approvals; dependency mapping.

**Challenge:** A retained backup depends on a key version scheduled for destruction before retention ends.

**Decision criterion:** Key lifecycle changes preserve required availability and approved cryptographic policy.

**Script:** [R05-S05.py](../scripts/steps/R05-S05.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Review key lifecycle and availability
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R05-S05.py --plan
```

**Google references:** [Key rotation](https://docs.cloud.google.com/kms/docs/key-rotation) · [Key version states](https://docs.cloud.google.com/kms/docs/key-states)

## R06 — Recovery without changing production

### Step 1: Map recovery objectives to dependencies

**Procedure:** Join critical services to data stores, identities, keys, DNS, networking and provider dependencies. Obtain business-approved RPO and RTO, including data-loss tolerance.

**Acceptable evidence:** business impact analysis; dependency map; approved RPO/RTO.

**Challenge:** A database meets its RTO while identity or DNS recovery prevents the business application from operating.

**Decision criterion:** Recovery objectives cover the complete service chain and have accountable owners.

**Script:** [R06-S01.py](../scripts/steps/R06-S01.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Map recovery objectives to dependencies
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R06-S01.py --plan
```

**Google references:** [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide) · [Well-Architected Framework: Reliability pillar](https://docs.cloud.google.com/architecture/framework/reliability)

### Step 2: Review backup coverage and immutability

**Procedure:** Reconcile data-bearing resources with snapshot, SQL backup, GKE backup and Backup and DR metadata. Inspect retention, separation, vault protection and administration.

**Acceptable evidence:** backup coverage matrix; vault settings export; administrator review.

**Challenge:** The same compromised administrator can erase production data and every retained backup.

**Decision criterion:** All required data has a mapped backup mechanism and approved protection from common administrative failure.

**Script:** [R06-S02.py](../scripts/steps/R06-S02.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Review backup coverage and immutability
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R06-S02.py --plan
```

**Google references:** [Backup vaults for immutable and indelible backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault) · [Create schedules for disk snapshots](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots)

### Step 3: Assess restore evidence

**Procedure:** Read existing backup metadata and hash supplied prior restore reports. Review restored scope, timestamp, data integrity checks, elapsed time and business acceptance.

**Acceptable evidence:** dated restore reports; integrity checks; business sign-off.

**Challenge:** A report says successful but omits application integrity checks or restores only an empty database.

**Decision criterion:** Prior restore evidence demonstrates the agreed objective for the sampled system; missing exercises remain a gap.

**Script:** [R06-S03.py](../scripts/steps/R06-S03.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Assess restore evidence
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R06-S03.py --plan
```

**Google references:** [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide) · [Restore an instance using a backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restoring)

### Step 4: Review regional and zonal failure readiness

**Procedure:** Inspect multi-zone or regional configurations and compare capacity, quotas and dependencies to the failover design. Evaluate existing exercises and their assumptions.

**Acceptable evidence:** failover design; capacity evidence; prior exercise.

**Challenge:** A secondary region shares a key, network or quota bottleneck that prevents recovery.

**Decision criterion:** The adopted failure scenario is covered by realistic capacity and independent dependencies.

**Script:** [R06-S04.py](../scripts/steps/R06-S04.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Review regional and zonal failure readiness
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R06-S04.py --plan
```

**Google references:** [Build highly available systems through resource redundancy](https://docs.cloud.google.com/architecture/framework/reliability/design-scale-high-availability)

### Step 5: Assess recovery operations and ownership

**Procedure:** Review recovery runbooks, access prerequisites, communications and retrospective improvements. Verify named owners can locate retained evidence and necessary approvals.

**Acceptable evidence:** runbook review; access checklist; exercise action log.

**Challenge:** An offline recovery step requires a console or repository available only in the failed environment.

**Decision criterion:** Runbooks remain usable under the scenario and material exercise findings are resolved or accepted.

**Script:** [R06-S05.py](../scripts/steps/R06-S05.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Assess recovery operations and ownership
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R06-S05.py --plan
```

**Google references:** [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide)

## R07 — Source to production and AI tools

### Step 1: Review source and build trigger trust

**Procedure:** Inspect Cloud Build triggers, event filters, approval settings, repository connections and execution identities. Reconcile branch protection and contributor permissions from the source platform.

**Acceptable evidence:** repository protection export; pipeline design; trigger approvals.

**Challenge:** A pull request can edit the pipeline that runs with a production service account.

**Decision criterion:** Untrusted changes cannot silently obtain production deployment authority through the approved pipeline.

**Script:** [R07-S01.py](../scripts/steps/R07-S01.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Review source and build trigger trust
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R07-S01.py --plan
```

**Google references:** [Gate builds on approval](https://docs.cloud.google.com/build/docs/securing-builds/gate-builds-on-approval)

### Step 2: Assess build identity and secrets

**Procedure:** Review build service accounts, worker pools, network access and secret references. Inspect a bounded sample of historical builds without triggering builds.

**Acceptable evidence:** build configuration export; secret mapping; identity review.

**Challenge:** An untrusted build can impersonate the same identity that deploys production.

**Decision criterion:** Build privileges and secret availability are appropriate to repository trust and deployment purpose.

**Script:** [R07-S02.py](../scripts/steps/R07-S02.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Assess build identity and secrets
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R07-S02.py --plan
```

**Google references:** [Configure access for the default Cloud Build service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account) · [Use secrets from Secret Manager](https://docs.cloud.google.com/build/docs/securing-builds/use-secrets)

### Step 3: Assess deployment approvals and admission

**Procedure:** Inspect delivery pipelines, Binary Authorization policy and approved attestor evidence. Trace one deployed artifact to source, build, approval and admission result.

**Acceptable evidence:** release sample; attestation metadata; admission results.

**Challenge:** Policy exists but enforcement permits all images or a production target bypasses the pipeline.

**Decision criterion:** Production admission and approval requirements are effective, with controlled break-glass use.

**Script:** [R07-S03.py](../scripts/steps/R07-S03.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Assess deployment approvals and admission
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R07-S03.py --plan
```

**Google references:** [Binary Authorization overview](https://docs.cloud.google.com/binary-authorization/docs/overview) · [Promote your release and manage approvals](https://docs.cloud.google.com/deploy/docs/promote-release)

### Step 4: Assess agent tools and retrieval boundaries

**Procedure:** Use application-supplied agent manifests, tool definitions, retrieval ACL design and existing evaluation traces. Review delegated identity and approval of consequential actions without invoking tools.

**Acceptable evidence:** agent tool inventory; retrieval ACL evidence; prior adversarial evaluations.

**Challenge:** A prompt or retrieved document can cause a tool to access another user's data or perform an unapproved action.

**Decision criterion:** Agents enforce user-specific data access and approved tool authority at execution time.

**Script:** [R07-S04.py](../scripts/steps/R07-S04.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Assess agent tools and retrieval boundaries
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R07-S04.py --plan
```

**Google references:** [Scale your agents](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview) · [Model Armor overview](https://docs.cloud.google.com/model-armor/overview)

### Step 5: Review AI evaluation and operational oversight

**Procedure:** Inspect model/version approvals, evaluation criteria, safety filters, monitoring, rollback and incident records. Sample completed evaluations for representative failure modes.

**Acceptable evidence:** evaluation reports; model approvals; AI incident records.

**Challenge:** A model passes generic quality tests but fails the business's sensitive-data or tool-authorization scenarios.

**Decision criterion:** The production use has approved quality, safety and security acceptance criteria plus monitored failure handling.

**Script:** [R07-S05.py](../scripts/steps/R07-S05.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Review AI evaluation and operational oversight
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R07-S05.py --plan
```

**Google references:** [Gen AI evaluation service overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview) · [Safety and content filters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-filters)

## R08 — Operating assurance and management decisions

### Step 1: Assess Security Command Center coverage

**Procedure:** Reconcile activation scope, edition, data location, services, detectors and project population with expected coverage. Read findings and record activation or permission failures.

**Acceptable evidence:** SCC configuration export; coverage matrix; detector status.

**Challenge:** An empty finding list comes from a location without the organization's findings or a disabled detector.

**Decision criterion:** Finding absence is interpreted only after coverage is demonstrated; tier-dependent gaps have compensating evidence.

**Script:** [R08-S01.py](../scripts/steps/R08-S01.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Assess Security Command Center coverage
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R08-S01.py --plan
```

**Google references:** [Security Command Center service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) · [Security Command Center overview](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)

### Step 2: Validate detection use cases

**Procedure:** Map priority threats to required logs, analytics, alert routes and past incident or exercise records. Inspect existing test results rather than injecting attacks.

**Acceptable evidence:** detection catalog; prior exercise results; alert routing export.

**Challenge:** A detection rule is enabled but depends on a disabled Data Access log source.

**Decision criterion:** The agreed use cases have demonstrated signal delivery and response evidence.

**Script:** [R08-S02.py](../scripts/steps/R08-S02.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Validate detection use cases
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R08-S02.py --plan
```

**Google references:** [Overview of Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) · [Configure log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts)

### Step 3: Assess observability against service objectives

**Procedure:** Join workload inventory to approved SLIs, SLOs, dashboards, alerts and escalation owners from monitoring exports. Review existing incidents and error budgets.

**Acceptable evidence:** SLO register; monitoring policy export; incident sample.

**Challenge:** An infrastructure dashboard is green while the business transaction is unavailable.

**Decision criterion:** Critical user journeys have measurable objectives and actionable monitoring.

**Script:** [R08-S03.py](../scripts/steps/R08-S03.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Assess observability against service objectives
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R08-S03.py --plan
```

**Google references:** [Well-Architected Framework: Reliability pillar](https://docs.cloud.google.com/architecture/framework/reliability) · [Service monitoring](https://docs.cloud.google.com/monitoring/slo-monitoring)

### Step 4: Review budgets and spend control behavior

**Procedure:** Inspect budgets for explicitly approved accounts, filters, thresholds and recipients. Determine whether a budget is alerts-only or a supported spend-cap configuration and inspect actual handling.

**Acceptable evidence:** budget approvals; notification delivery; response records.

**Challenge:** An alerts-only threshold is mistaken for an enforced stop, or notification reaches an unattended mailbox.

**Decision criterion:** Budget behavior and alert response match the adopted cost-control requirement; no generic assumption that every budget caps spending.

**Script:** [R08-S04.py](../scripts/steps/R08-S04.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Review budgets and spend control behavior
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R08-S04.py --plan
```

**Google references:** [Create, edit, or delete budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets)

### Step 5: Review audit evidence and assurance closure

**Procedure:** Check findings against criteria, affected population, reproducible evidence and contrary explanations. Require owners, agreed actions, due dates, risk acceptance and independent retest before closure.

**Acceptable evidence:** finding register; quality review; management responses; closure evidence.

**Challenge:** A high-severity finding relies on truncated data or is marked closed after a change ticket without retest evidence.

**Decision criterion:** The report distinguishes observed facts, inference, limitations and management decisions; no unsupported compliance claim remains.

**Script:** [R08-S05.py](../scripts/steps/R08-S05.py). Description: collect the mapped configuration, record acquisition gaps, and create this step's evidence requests and assessment workpaper.

```sh
# Title: Preview Review audit evidence and assurance closure
# Description: Display the documented evidence plan without connecting.
python scripts/steps/R08-S05.py --plan
```

**Google references:** [Well-Architected Framework: Security, privacy, and compliance pillar](https://docs.cloud.google.com/architecture/framework/security) · [SP 800-53A Rev. 5, Assessing Security and Privacy Controls in Information Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final)
