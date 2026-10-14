# Control catalog

100 consultant-authored controls across 20 domains. Google references support product behavior; the auditor and organization adopt the criteria, sample design, severity and operating requirements. Each script collects metadata and creates a workpaper; it does not make an audit opinion.

[Main playbook](../PLAYBOOK.md) · [Run scripts](../scripts/README.md) · [CSV](control-catalog.csv)

## GOV — Governance and scope

Suggested accountable owner: **Cloud governance lead**.

### GOV-01 — Establish organizational ownership and scope

**Objective and applicability:** Establish organizational ownership and scope. All in-scope uses of governance and scope; document approved exclusions and service absence.

**Read-only evidence procedure:** Reconcile organization, folders, project numbers, business owners, lifecycle state and billing inventory with the signed scope. Record separately projects visible to the collector and the expected population.

**Required workpapers:** signed charter; independent project register; population reconciliation.

**Consultant assessment criterion:** Every expected project has a disposition, owner and applicable control set; unexplained inventory gaps remain open.

**Try to disprove the conclusion:** Find one billing-linked or CMDB project absent from the asset export and investigate visibility before declaring it retired.

**Script title:** Establish organizational ownership and scope. **Description:** collect reconcile organization project inventory, read project identity and lifecycle, read project billing association; create evidence requests and an unassessed review workpaper. [Open GOV-01.py](../scripts/controls/GOV-01.py).

**Operations:** `org_assets`, `project`, `billing_link` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [About resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) · [Asset types](https://docs.cloud.google.com/asset-inventory/docs/asset-types)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### GOV-02 — Allocate shared responsibility

**Objective and applicability:** Allocate shared responsibility. All in-scope uses of governance and scope; document approved exclusions and service absence.

**Read-only evidence procedure:** Map each material service to customer, Google and supplier duties, including data protection, IAM, patching and recovery. Assign evidence owners rather than treating managed services as fully outsourced security.

**Required workpapers:** responsibility matrix; service-owner approvals.

**Consultant assessment criterion:** The responsibility matrix covers all material services and has accountable owners.

**Try to disprove the conclusion:** Select one managed database and ask who proves database-user review and recoverability.

**Script title:** Allocate shared responsibility. **Description:** collect list enabled service apis, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open GOV-02.py](../scripts/controls/GOV-02.py).

**Operations:** `services`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Shared responsibilities and shared fate on Google Cloud](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### GOV-03 — Assess landing-zone design

**Objective and applicability:** Assess landing-zone design. All in-scope uses of governance and scope; document approved exclusions and service absence.

**Read-only evidence procedure:** Compare folder boundaries, production separation, centralized services and deployment ownership against the adopted enterprise foundation design. Trace an approved exception from architecture decision to resource.

**Required workpapers:** architecture diagrams; design decisions; exception register.

**Consultant assessment criterion:** Separation and centralized controls meet the documented design or have risk-accepted exceptions.

**Try to disprove the conclusion:** Look for a production workload in a sandbox project or inherited development administrator access.

**Script title:** Assess landing-zone design. **Description:** collect reconcile organization project inventory, read organization iam and audit configuration, read ancestor folder iam and audit configuration, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open GOV-03.py](../scripts/controls/GOV-03.py).

**Operations:** `org_assets`, `org_iam`, `folder_iam`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations) · [Decide a resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### GOV-04 — Review exceptions and policy ownership

**Objective and applicability:** Review exceptions and policy ownership. All in-scope uses of governance and scope; document approved exclusions and service absence.

**Read-only evidence procedure:** Join policy overrides and IAM changes to the exception register. Verify business justification, accountable approval, expiry, compensating evidence and review dates.

**Required workpapers:** exception register; policy baseline; review minutes.

**Consultant assessment criterion:** Each material exception has a current owner, time limit and tested compensating control.

**Try to disprove the conclusion:** Find a locally overridden constraint with no current approval.

**Script title:** Review exceptions and policy ownership. **Description:** collect list project organization-policy overrides, read project iam and audit configuration; create evidence requests and an unassessed review workpaper. [Open GOV-04.py](../scripts/controls/GOV-04.py).

**Operations:** `org_policies`, `project_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Organization Policy overview](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) · [Well-Architected Framework: Security, privacy, and compliance pillar](https://docs.cloud.google.com/architecture/framework/security)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### GOV-05 — Review project lifecycle and shutdown

**Objective and applicability:** Review project lifecycle and shutdown. All in-scope uses of governance and scope; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect labels, lifecycle states, enabled services and billing links. Trace creation approval, handover and one past retirement to retained evidence and revoked access.

**Required workpapers:** creation and retirement tickets; retention approvals.

**Consultant assessment criterion:** Creation and retirement records reconcile to inventory without orphaned ownership, data or access.

**Try to disprove the conclusion:** Select a retired project whose data export, billing liability or service account remains unexplained.

**Script title:** Review project lifecycle and shutdown. **Description:** collect read project identity and lifecycle, list enabled service apis, read project billing association, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open GOV-05.py](../scripts/controls/GOV-05.py).

**Operations:** `project`, `services`, `billing_link`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Create projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) · [Create and update labels for projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## IAM — Human identity and privileged access

Suggested accountable owner: **Identity and access lead**.

### IAM-01 — Resolve inherited privileged access

**Objective and applicability:** Resolve inherited privileged access. All in-scope uses of human identity and privileged access; document approved exclusions and service absence.

**Read-only evidence procedure:** Read organization, all ancestor folders, project and resource policies. Expand groups through authorized directory evidence and inspect custom role permissions, conditions, deny and principal boundary policies.

**Required workpapers:** group membership export; effective-access workpaper; access approvals.

**Consultant assessment criterion:** Each effective privileged access path is justified, assigned to an accountable identity and periodically reviewed.

**Try to disprove the conclusion:** A harmless-looking project policy conceals an organization-level group with broad access; trace a nested member.

**Script title:** Resolve inherited privileged access. **Description:** collect read organization iam and audit configuration, read ancestor folder iam and audit configuration, read project iam and audit configuration, inventory resource allow policies, list organization custom roles, list project custom roles; create evidence requests and an unassessed review workpaper. [Open IAM-01.py](../scripts/controls/IAM-01.py).

**Operations:** `org_iam`, `folder_iam`, `project_iam`, `asset_iam`, `org_roles`, `project_roles` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Using resource hierarchy for access control](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control) · [IAM policy types](https://docs.cloud.google.com/iam/docs/policy-types) · [Overview of IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### IAM-02 — Assess MFA and identity federation

**Objective and applicability:** Assess MFA and identity federation. All in-scope uses of human identity and privileged access; document approved exclusions and service absence.

**Read-only evidence procedure:** Reconcile privileged principals with Cloud Identity, Google Workspace or workforce IdP enforcement exports. Review phishing-resistant factors, federation trust, session policy and exemptions without assuming gcloud IAM proves MFA.

**Required workpapers:** IdP policy and membership exports; authentication review.

**Consultant assessment criterion:** Approved authentication requirements cover human privileged paths and exceptions have independent evidence.

**Try to disprove the conclusion:** Choose a privileged external principal excluded from the main employee MFA policy.

**Script title:** Assess MFA and identity federation. **Description:** collect read project iam and audit configuration, read organization iam and audit configuration, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open IAM-02.py](../scripts/controls/IAM-02.py).

**Operations:** `project_iam`, `org_iam`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) · [Deploy 2-Step Verification](https://support.google.com/a/answer/9176657)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### IAM-03 — Review joiner mover leaver controls

**Objective and applicability:** Review joiner mover leaver controls. All in-scope uses of human identity and privileged access; document approved exclusions and service absence.

**Read-only evidence procedure:** Join active bindings, external principals and group membership to HR and supplier lifecycle records. Sample terminations and role changes across the review period and inspect actual removal times.

**Required workpapers:** HR sample; directory membership; removal tickets.

**Consultant assessment criterion:** Access changes meet the company's approved service levels and retain evidence of review.

**Try to disprove the conclusion:** Select an offboarded contractor whose nested group still grants access.

**Script title:** Review joiner mover leaver controls. **Description:** collect inventory resource allow policies, read organization iam and audit configuration, read ancestor folder iam and audit configuration; create evidence requests and an unassessed review workpaper. [Open IAM-03.py](../scripts/controls/IAM-03.py).

**Operations:** `asset_iam`, `org_iam`, `folder_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys) · [Create and manage Google groups in the Google Cloud console](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### IAM-04 — Review emergency and time-bound privilege

**Objective and applicability:** Review emergency and time-bound privilege. All in-scope uses of human identity and privileged access; document approved exclusions and service absence.

**Read-only evidence procedure:** Identify emergency identities, standing roles and privileged-access approval arrangements. Inspect prior emergency exercises, vault access, activation expiry and monitoring records.

**Required workpapers:** emergency runbook; exercise record; privilege approvals.

**Consultant assessment criterion:** Emergency access remains usable under the stated failure scenario and accountable; temporary privilege expires as designed.

**Try to disprove the conclusion:** Challenge an emergency account dependent on the same unavailable IdP it is intended to bypass.

**Script title:** Review emergency and time-bound privilege. **Description:** collect read organization iam and audit configuration, read project iam and audit configuration, sample audit events within the approved window; create evidence requests and an unassessed review workpaper. [Open IAM-04.py](../scripts/controls/IAM-04.py).

**Operations:** `org_iam`, `project_iam`, `audit_logs` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Privileged Access Manager overview](https://docs.cloud.google.com/iam/docs/pam-overview) · [Ensure continuous access to Google Cloud](https://docs.cloud.google.com/docs/security/best-practices-continuous-access-to-google-cloud)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### IAM-05 — Assess deny and principal access boundaries

**Objective and applicability:** Assess deny and principal access boundaries. All in-scope uses of human identity and privileged access; document approved exclusions and service absence.

**Read-only evidence procedure:** Reconcile allow bindings with explicit deny rules, exceptions, principal-set bindings and boundary enforcement versions using resource metadata and owner exports when not inventoried.

**Required workpapers:** deny and boundary policy export; principal-set membership; access analysis.

**Consultant assessment criterion:** Access analysis includes applicable allow, deny and boundary effects; unsupported permission coverage is acknowledged.

**Try to disprove the conclusion:** Find a boundary that does not cover the permission relied on by the proposed compensating control.

**Script title:** Assess deny and principal access boundaries. **Description:** collect inventory resource configuration, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open IAM-05.py](../scripts/controls/IAM-05.py).

**Operations:** `assets`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) · [Principal access boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## WID — Workload identities and federation

Suggested accountable owner: **Platform identity lead**.

### WID-01 — Inventory service account ownership

**Objective and applicability:** Inventory service account ownership. All in-scope uses of workload identities and federation; document approved exclusions and service absence.

**Read-only evidence procedure:** Map service accounts, default identities, attached workloads and impersonation grants to owners and intended permissions. Inspect both use and administration of each identity.

**Required workpapers:** service account register; application ownership; impersonation analysis.

**Consultant assessment criterion:** Privileged machine identities have specific purposes and accountable owners; default identities receive no unexplained broad access.

**Try to disprove the conclusion:** A low-privileged deployer can attach or impersonate an overprivileged runtime identity.

**Script title:** Inventory service account ownership. **Description:** collect list service account identities, inventory resource allow policies, list compute engine instance configuration, list cloud run services; create evidence requests and an unassessed review workpaper. [Open WID-01.py](../scripts/controls/WID-01.py).

**Operations:** `service_accounts`, `asset_iam`, `instances`, `run_services` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Best practices for using service accounts securely](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts) · [Service account impersonation](https://docs.cloud.google.com/iam/docs/service-account-impersonation)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### WID-02 — Review user-managed service account keys

**Objective and applicability:** Review user-managed service account keys. All in-scope uses of workload identities and federation; document approved exclusions and service absence.

**Read-only evidence procedure:** List key metadata for every discovered service account. Reconcile key age, expiry, disabled status, owner and external storage with the approved key policy; do not read private key material.

**Required workpapers:** key exception register; rotation records; usage review.

**Consultant assessment criterion:** Every user-managed key is justified and managed within the company's approved lifecycle, with a keyless migration decision.

**Try to disprove the conclusion:** An unused service account still has an active externally held key with no custodian.

**Script title:** Review user-managed service account keys. **Description:** collect list service account identities, list service account key metadata; create evidence requests and an unassessed review workpaper. [Open WID-02.py](../scripts/controls/WID-02.py).

**Operations:** `service_accounts`, `sa_keys` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys) · [Create and delete service account keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### WID-03 — Validate federation trust boundaries

**Objective and applicability:** Validate federation trust boundaries. All in-scope uses of workload identities and federation; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect workload pools and provider issuer, audience, attribute mapping and condition. Trace external subject claims to IAM grants and repository or cloud ownership.

**Required workpapers:** federation design; provider export; subject-to-role mapping.

**Consultant assessment criterion:** Trust restricts intended external tenants and subjects; broad pools and impersonation grants are justified.

**Try to disprove the conclusion:** Test the reasoning with a forked repository or different external tenant that might satisfy a weak attribute condition; do not request tokens.

**Script title:** Validate federation trust boundaries. **Description:** collect list workload identity pools, read workload federation providers, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open WID-03.py](../scripts/controls/WID-03.py).

**Operations:** `wif_pools`, `wif_providers`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Configure Workload Identity Federation with deployment pipelines](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines) · [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### WID-04 — Inspect service account escalation paths

**Objective and applicability:** Inspect service account escalation paths. All in-scope uses of workload identities and federation; document approved exclusions and service absence.

**Read-only evidence procedure:** Review serviceAccountUser, token creation, workload deployment and project-level permissions together. Trace who can modify code running as a sensitive service identity.

**Required workpapers:** privilege graph; deployment approvals.

**Consultant assessment criterion:** Privilege reviews cover combined deployment and identity capabilities, including cross-project service accounts.

**Try to disprove the conclusion:** Find an identity that cannot read data directly but can deploy code as an identity that can.

**Script title:** Inspect service account escalation paths. **Description:** collect inventory resource allow policies, read project iam and audit configuration, list organization custom roles, list project custom roles, list service account identities; create evidence requests and an unassessed review workpaper. [Open WID-04.py](../scripts/controls/WID-04.py).

**Operations:** `asset_iam`, `project_iam`, `org_roles`, `project_roles`, `service_accounts` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Roles for service account authentication](https://docs.cloud.google.com/iam/docs/service-account-permissions) · [Best practices for using service accounts securely](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### WID-05 — Review workload identity activity

**Objective and applicability:** Review workload identity activity. All in-scope uses of workload identities and federation; document approved exclusions and service absence.

**Read-only evidence procedure:** Join historical key, impersonation and workload-owner records to bounded audit samples. Ask for longer retained exports where the collection window is insufficient.

**Required workpapers:** activity review; log coverage matrix; automation schedules.

**Consultant assessment criterion:** Activity review can distinguish expected automation from unexplained identity use without treating absence of logs as inactivity.

**Try to disprove the conclusion:** A key appears unused only because the relevant service's Data Access logging was disabled.

**Script title:** Review workload identity activity. **Description:** collect sample audit events within the approved window, list service account identities, list service account key metadata; create evidence requests and an unassessed review workpaper. [Open WID-05.py](../scripts/controls/WID-05.py).

**Operations:** `audit_logs`, `service_accounts`, `sa_keys` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Identity and Access Management audit logging](https://docs.cloud.google.com/iam/docs/audit-logging) · [Service account credentials](https://docs.cloud.google.com/iam/docs/service-account-creds)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## ORG — Organization policies and guardrails

Suggested accountable owner: **Cloud governance lead**.

### ORG-01 — Verify effective organization policies

**Objective and applicability:** Verify effective organization policies. All in-scope uses of organization policies and guardrails; document approved exclusions and service absence.

**Read-only evidence procedure:** Read explicit overrides and effective values for the approved constraint list on every project. Compare against the organization's adopted baseline and conditions.

**Required workpapers:** constraint baseline; effective-policy comparison.

**Consultant assessment criterion:** Expected constraints are effective at the intended descendants; list output alone is insufficient.

**Try to disprove the conclusion:** A lower-level override or conditional tag changes the result for a sensitive project.

**Script title:** Verify effective organization policies. **Description:** collect list project organization-policy overrides, read a selected effective organization policy, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open ORG-01.py](../scripts/controls/ORG-01.py).

**Operations:** `org_policies`, `effective_policy`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Hierarchy evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy) · [Organization Policy overview](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### ORG-02 — Assess domain and external sharing restrictions

**Objective and applicability:** Assess domain and external sharing restrictions. All in-scope uses of organization policies and guardrails; document approved exclusions and service absence.

**Read-only evidence procedure:** Review applicable domain-restriction constraints, existing external IAM grants and exceptions. Separate prevention of new grants from historical access review.

**Required workpapers:** external-party register; sharing exceptions.

**Consultant assessment criterion:** The chosen sharing policy and actual external principals match approved collaboration needs.

**Try to disprove the conclusion:** An existing external grant predates a policy change and remains unexplained.

**Script title:** Assess domain and external sharing restrictions. **Description:** collect read a selected effective organization policy, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open ORG-02.py](../scripts/controls/ORG-02.py).

**Operations:** `effective_policy`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Restrict identities with domain-restricted sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### ORG-03 — Assess service account key guardrails

**Objective and applicability:** Assess service account key guardrails. All in-scope uses of organization policies and guardrails; document approved exclusions and service absence.

**Read-only evidence procedure:** Check effective key creation and upload restrictions, default service account grant constraints and exception projects. Reconcile guardrails with existing keys.

**Required workpapers:** key policy; exception approval; legacy key inventory.

**Consultant assessment criterion:** The intended prevention policies and legacy-key cleanup are both evidenced.

**Try to disprove the conclusion:** Key creation is blocked but old externally stored keys remain active.

**Script title:** Assess service account key guardrails. **Description:** collect read a selected effective organization policy, list service account key metadata, read project iam and audit configuration; create evidence requests and an unassessed review workpaper. [Open ORG-03.py](../scripts/controls/ORG-03.py).

**Operations:** `effective_policy`, `sa_keys`, `project_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Restrict IAM service account usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### ORG-04 — Review resource locations and sovereignty

**Objective and applicability:** Review resource locations and sovereignty. All in-scope uses of organization policies and guardrails; document approved exclusions and service absence.

**Read-only evidence procedure:** Map actual resource locations, backups and service-supported location constraints to contractual requirements. Identify global services and processing paths that need separate analysis.

**Required workpapers:** data-location register; contract requirements; service exceptions.

**Consultant assessment criterion:** Approved location requirements apply to the relevant resource types and operational copies; unsupported services are documented.

**Try to disprove the conclusion:** A primary region is approved while backups, logs or a global endpoint fall outside the reviewed requirement.

**Script title:** Review resource locations and sovereignty. **Description:** collect inventory resource configuration, read a selected effective organization policy; create evidence requests and an unassessed review workpaper. [Open ORG-04.py](../scripts/controls/ORG-04.py).

**Operations:** `assets`, `effective_policy` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Restrict resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) · [Overview of Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### ORG-05 — Review custom constraints and drift

**Objective and applicability:** Review custom constraints and drift. All in-scope uses of organization policies and guardrails; document approved exclusions and service absence.

**Read-only evidence procedure:** Compare current organization-policy resources with version-controlled definitions and approved change history. Inspect dry-run versus enforced state and resource-method coverage.

**Required workpapers:** policy-as-code repository export; change records.

**Consultant assessment criterion:** Guardrails relied upon by the audit are enforced for the intended operations, with reviewed changes and exceptions.

**Try to disprove the conclusion:** A custom rule exists only in dry-run or does not cover the update method being relied upon.

**Script title:** Review custom constraints and drift. **Description:** collect inventory resource configuration, list project organization-policy overrides, sample audit events within the approved window; create evidence requests and an unassessed review workpaper. [Open ORG-05.py](../scripts/controls/ORG-05.py).

**Operations:** `assets`, `org_policies`, `audit_logs` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Manage resources with custom constraints](https://docs.cloud.google.com/resource-manager/docs/custom-constraints)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## NET — Network and perimeter security

Suggested accountable owner: **Network security lead**.

### NET-01 — Resolve effective firewall exposure

**Objective and applicability:** Resolve effective firewall exposure. All in-scope uses of network and perimeter security; document approved exclusions and service absence.

**Read-only evidence procedure:** Review VPC rules, hierarchical policies, target tags or service accounts, priorities, direction and disabled status. Join to routes, instance interfaces and approved service exposure.

**Required workpapers:** effective-firewall export; network exposure register.

**Consultant assessment criterion:** Public and lateral paths are justified after effective rule evaluation; a single broad rule is a review candidate, not automatic proof of reachability.

**Try to disprove the conclusion:** A deny is shadowed by a higher-priority allow, or an apparent allow targets no instances.

**Script title:** Resolve effective firewall exposure. **Description:** collect list vpc firewall rules, list organization firewall policies, list vpc networks and peerings, list subnets and private access settings, list compute engine instance configuration, list vpc routes; create evidence requests and an unassessed review workpaper. [Open NET-01.py](../scripts/controls/NET-01.py).

**Operations:** `firewalls`, `firewall_policies`, `networks`, `subnets`, `instances`, `routes` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Firewall policies and rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) · [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### NET-02 — Assess external application protection

**Objective and applicability:** Assess external application protection. All in-scope uses of network and perimeter security; document approved exclusions and service absence.

**Read-only evidence procedure:** Map external forwarding rules to backend services and Cloud Armor policy attachment. Review rule action, preview mode, bypass endpoints, TLS configuration and owner-approved exposure.

**Required workpapers:** load-balancer architecture; TLS policy export; exception register.

**Consultant assessment criterion:** Each critical public service has the agreed protections on its actual serving path.

**Try to disprove the conclusion:** A protective policy exists but is unattached or all material rules run in preview.

**Script title:** Assess external application protection. **Description:** collect list forwarding rules, list load balancer backend services, list cloud armor policies, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open NET-02.py](../scripts/controls/NET-02.py).

**Operations:** `forwarding`, `backend`, `armor`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-overview) · [SSL policies overview](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### NET-03 — Inspect private access and egress

**Objective and applicability:** Inspect private access and egress. All in-scope uses of network and perimeter security; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect subnet private access, NAT configuration, routes, service endpoints and DNS resolution design. Reconcile permitted outbound destinations with application requirements.

**Required workpapers:** egress policy; flow-log analysis; network diagrams.

**Consultant assessment criterion:** Private access and egress controls match the approved traffic model and observable flows.

**Try to disprove the conclusion:** A private VM reaches an unintended destination through NAT or a transit route.

**Script title:** Inspect private access and egress. **Description:** collect list subnets and private access settings, list cloud routers and nat configuration, list vpc routes, list vpc networks and peerings, list cloud dns managed zones; create evidence requests and an unassessed review workpaper. [Open NET-03.py](../scripts/controls/NET-03.py).

**Operations:** `subnets`, `routers`, `routes`, `networks`, `dns` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) · [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) · [Cloud NAT overview](https://docs.cloud.google.com/nat/docs/overview)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### NET-04 — Assess VPC Service Controls

**Objective and applicability:** Assess VPC Service Controls. All in-scope uses of network and perimeter security; document approved exclusions and service absence.

**Read-only evidence procedure:** Read access policies and perimeter status, ingress, egress, restricted services, access levels and dry-run specifications. Reconcile perimeter project numbers and bridges to data flows.

**Required workpapers:** perimeter design; access-level export; dry-run review.

**Consultant assessment criterion:** The perimeter protects the intended supported services and approved cross-boundary paths in enforced configuration.

**Try to disprove the conclusion:** A protected project has an unrestricted service path, bridge or broad ingress identity condition.

**Script title:** Assess VPC Service Controls. **Description:** collect list access context manager policies, list vpc service controls perimeters, read project identity and lifecycle; create evidence requests and an unassessed review workpaper. [Open NET-04.py](../scripts/controls/NET-04.py).

**Operations:** `access_policies`, `perimeters`, `project` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) · [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### NET-05 — Review DNS and network telemetry

**Objective and applicability:** Review DNS and network telemetry. All in-scope uses of network and perimeter security; document approved exclusions and service absence.

**Read-only evidence procedure:** Review DNS zone visibility and DNSSEC where applicable, flow-log enablement and firewall logging on material paths. Obtain existing queries or flow samples and retention evidence.

**Required workpapers:** DNS settings export; flow evidence; network monitoring use cases.

**Consultant assessment criterion:** Telemetry supports the agreed detection use cases; name resolution and DNS change ownership are controlled.

**Try to disprove the conclusion:** A critical subnet or deny rule has no logging while a dashboard suggests complete network visibility.

**Script title:** Review DNS and network telemetry. **Description:** collect list cloud dns managed zones, list subnets and private access settings, list vpc firewall rules, read regional log bucket retention; create evidence requests and an unassessed review workpaper. [Open NET-05.py](../scripts/controls/NET-05.py).

**Operations:** `dns`, `subnets`, `firewalls`, `log_buckets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [DNS Security Extensions (DNSSEC) overview](https://docs.cloud.google.com/dns/docs/dnssec) · [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## HYB — Hybrid connectivity and shared networks

Suggested accountable owner: **Network platform lead**.

### HYB-01 — Review Shared VPC administration

**Objective and applicability:** Review Shared VPC administration. All in-scope uses of hybrid connectivity and shared networks; document approved exclusions and service absence.

**Read-only evidence procedure:** Identify host and service projects and network-user grants. Reconcile cross-project service identities and ownership of firewall, subnet and DNS changes.

**Required workpapers:** Shared VPC relationship export; responsibility matrix.

**Consultant assessment criterion:** Host and service project responsibilities and permissions preserve the approved separation.

**Try to disprove the conclusion:** A service-project deployer can alter shared host-network security unexpectedly.

**Script title:** Review Shared VPC administration. **Description:** collect inventory resource configuration, list vpc networks and peerings, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open HYB-01.py](../scripts/controls/HYB-01.py).

**Operations:** `assets`, `networks`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### HYB-02 — Assess VPN redundancy and authentication

**Objective and applicability:** Assess VPN redundancy and authentication. All in-scope uses of hybrid connectivity and shared networks; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect VPN tunnels, peer endpoints, routing and status evidence against the intended availability design. Review key custody from records without retrieving preshared secrets.

**Required workpapers:** VPN topology; key custody record; prior failover results.

**Consultant assessment criterion:** Redundancy and routing match the approved design, with current monitoring and prior failure-test evidence.

**Try to disprove the conclusion:** Two apparently redundant tunnels depend on the same unprotected peer device or connection.

**Script title:** Assess VPN redundancy and authentication. **Description:** collect list vpn tunnel configuration, list cloud routers and nat configuration, list vpc routes; create evidence requests and an unassessed review workpaper. [Open HYB-02.py](../scripts/controls/HYB-02.py).

**Operations:** `vpn`, `routers`, `routes` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) · [Best practices for Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/best-practices)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### HYB-03 — Assess Interconnect dependencies

**Objective and applicability:** Assess Interconnect dependencies. All in-scope uses of hybrid connectivity and shared networks; document approved exclusions and service absence.

**Read-only evidence procedure:** Map attachments, edge locations, router peers and provider circuits to business-critical paths. Review utilization and fault evidence from existing monitoring exports.

**Required workpapers:** provider circuit records; monitoring export; topology.

**Consultant assessment criterion:** Availability objectives account for provider, facility and routing dependencies.

**Try to disprove the conclusion:** Nominally redundant attachments share a failure domain omitted from the design.

**Script title:** Assess Interconnect dependencies. **Description:** collect list interconnect attachments, list cloud routers and nat configuration, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open HYB-03.py](../scripts/controls/HYB-03.py).

**Operations:** `interconnect`, `routers`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) · [Dedicated Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/redundancy)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### HYB-04 — Review peering and transit trust

**Objective and applicability:** Review peering and transit trust. All in-scope uses of hybrid connectivity and shared networks; document approved exclusions and service absence.

**Read-only evidence procedure:** Review peering, imported and exported routes, custom routes and network connectivity hubs found in asset metadata. Trace intended access across shared or acquired organizations.

**Required workpapers:** peering approvals; transit routing analysis.

**Consultant assessment criterion:** Each trust connection has an owner, purpose and reviewed reachability analysis.

**Try to disprove the conclusion:** A new peering or exported default route extends access beyond the approved boundary.

**Script title:** Review peering and transit trust. **Description:** collect list vpc networks and peerings, list vpc routes, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open HYB-04.py](../scripts/controls/HYB-04.py).

**Operations:** `networks`, `routes`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) · [NCC overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### HYB-05 — Assess hybrid administration access

**Objective and applicability:** Assess hybrid administration access. All in-scope uses of hybrid connectivity and shared networks; document approved exclusions and service absence.

**Read-only evidence procedure:** Trace SSH, RDP and administrative application access through IAP, VPN or equivalent controls. Review IAM conditions, instance login controls and existing access logs.

**Required workpapers:** administration design; IAP access policy export; access sample.

**Consultant assessment criterion:** Administrative access meets approved identity and network requirements, including emergency paths.

**Try to disprove the conclusion:** An external address and permissive rule bypass the documented administrative gateway.

**Script title:** Assess hybrid administration access. **Description:** collect list compute engine instance configuration, list vpc firewall rules, inventory resource allow policies, sample audit events within the approved window; create evidence requests and an unassessed review workpaper. [Open HYB-05.py](../scripts/controls/HYB-05.py).

**Operations:** `instances`, `firewalls`, `asset_iam`, `audit_logs` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Use IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding) · [About OS Login](https://docs.cloud.google.com/compute/docs/oslogin)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## CMP — Compute Engine and host security

Suggested accountable owner: **Compute platform lead**.

### CMP-01 — Review VM identity and metadata

**Objective and applicability:** Review VM identity and metadata. All in-scope uses of compute engine and host security; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect instance service accounts, access scopes, project and instance metadata, external addresses and sensitive startup configuration. Reconcile identity purpose with IAM privileges.

**Required workpapers:** VM baseline; identity mapping; metadata review.

**Consultant assessment criterion:** Runtime identity and metadata follow the approved baseline; exported values are handled as sensitive.

**Try to disprove the conclusion:** A VM uses a default overprivileged identity or a project SSH key unexpectedly applies.

**Script title:** Review VM identity and metadata. **Description:** collect list compute engine instance configuration, read compute project quotas and metadata, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open CMP-01.py](../scripts/controls/CMP-01.py).

**Operations:** `instances`, `project_info`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts) · [About VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### CMP-02 — Assess host login controls

**Objective and applicability:** Assess host login controls. All in-scope uses of compute engine and host security; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect OS Login metadata and exceptions, project-wide SSH keys, IAP path and administrative roles. Use guest-side authorized evidence for local accounts not represented in GCP APIs.

**Required workpapers:** guest account inventory; login policy; access review.

**Consultant assessment criterion:** All privileged host access paths are covered by current identity, MFA and lifecycle requirements.

**Try to disprove the conclusion:** A compliant OS Login setting coexists with an unmanaged local administrator account.

**Script title:** Assess host login controls. **Description:** collect list compute engine instance configuration, read compute project quotas and metadata, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open CMP-02.py](../scripts/controls/CMP-02.py).

**Operations:** `instances`, `project_info`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Set up OS Login](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin) · [About OS Login](https://docs.cloud.google.com/compute/docs/oslogin)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### CMP-03 — Review boot integrity and images

**Objective and applicability:** Review boot integrity and images. All in-scope uses of compute engine and host security; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect Shielded VM settings, image origin, image lifecycle and approved exceptions. Correlate vulnerability and configuration records for the operating system.

**Required workpapers:** image approval; integrity monitoring; vulnerability export.

**Consultant assessment criterion:** Image provenance and boot controls meet the adopted platform baseline.

**Try to disprove the conclusion:** A production image is outside the approved pipeline or an integrity exception has no owner.

**Script title:** Review boot integrity and images. **Description:** collect list compute engine instance configuration, list project-owned vm images, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open CMP-03.py](../scripts/controls/CMP-03.py).

**Operations:** `instances`, `images`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Shielded VM overview](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) · [Image management best practices](https://docs.cloud.google.com/compute/docs/images/image-management-best-practices)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### CMP-04 — Assess patching and vulnerability operations

**Objective and applicability:** Assess patching and vulnerability operations. All in-scope uses of compute engine and host security; document approved exclusions and service absence.

**Read-only evidence procedure:** Reconcile OS inventory and vulnerability or patch-management exports to the VM population. Sample overdue fixes, maintenance approvals and validated exceptions.

**Required workpapers:** patch compliance export; asset reconciliation; exception records.

**Consultant assessment criterion:** The approved remediation timelines are met across the entire VM population, including unmanaged hosts.

**Try to disprove the conclusion:** A healthy patch dashboard excludes an instance with no inventory agent.

**Script title:** Assess patching and vulnerability operations. **Description:** collect list compute engine instance configuration, inventory resource configuration, read security command center findings; create evidence requests and an unassessed review workpaper. [Open CMP-04.py](../scripts/controls/CMP-04.py).

**Operations:** `instances`, `assets`, `scc` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/overview) · [About Patch](https://docs.cloud.google.com/compute/vm-manager/docs/patch)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### CMP-05 — Inspect disks and deletion protection

**Objective and applicability:** Inspect disks and deletion protection. All in-scope uses of compute engine and host security; document approved exclusions and service absence.

**Read-only evidence procedure:** Review disk encryption references, attachment, snapshot schedules and instance deletion protection where applicable. Join backup coverage to business recovery requirements.

**Required workpapers:** disk classification; backup mapping; deletion policy.

**Consultant assessment criterion:** Data-bearing compute resources have approved protection, encryption and recovery arrangements.

**Try to disprove the conclusion:** An unattached sensitive disk or critical instance lacks the expected backup association.

**Script title:** Inspect disks and deletion protection. **Description:** collect list compute engine instance configuration, list persistent disk configuration, list disk snapshot metadata, list regional resource policies; create evidence requests and an unassessed review workpaper. [Open CMP-05.py](../scripts/controls/CMP-05.py).

**Operations:** `instances`, `disks`, `snapshots`, `schedules` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Protect resources with Cloud KMS keys](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption) · [Prevent accidental VM deletion](https://docs.cloud.google.com/compute/docs/instances/preventing-accidental-vm-deletion)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## GKE — Kubernetes and GKE

Suggested accountable owner: **Kubernetes platform lead**.

### GKE-01 — Assess cluster control-plane access

**Objective and applicability:** Assess cluster control-plane access. All in-scope uses of kubernetes and gke; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect cluster endpoint exposure, authorized networks, IAM integration and authentication settings. Reconcile private connectivity and administrator paths.

**Required workpapers:** cluster architecture; administrator review.

**Consultant assessment criterion:** Control-plane access matches the documented threat model and approved administrator population.

**Try to disprove the conclusion:** A private-node cluster still has an unintended public control-plane access path.

**Script title:** Assess cluster control-plane access. **Description:** collect list gke cluster configuration, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open GKE-01.py](../scripts/controls/GKE-01.py).

**Operations:** `clusters`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Best practices for hardening your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster) · [About network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### GKE-02 — Review Kubernetes RBAC and admission

**Objective and applicability:** Review Kubernetes RBAC and admission. All in-scope uses of kubernetes and gke; document approved exclusions and service absence.

**Read-only evidence procedure:** Use cluster configuration plus customer-provided metadata exports of roles, bindings, admission policies and workloads. Trace namespace administrators and cluster-wide privilege without reading Kubernetes Secret payloads.

**Required workpapers:** Kubernetes RBAC export; admission policy and results; namespace ownership.

**Consultant assessment criterion:** RBAC and admission enforcement constrain the intended workloads and administrators.

**Try to disprove the conclusion:** A namespace owner can create a privileged workload or bind an unintended cluster role.

**Script title:** Review Kubernetes RBAC and admission. **Description:** collect list gke cluster configuration, inventory resource allow policies, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open GKE-02.py](../scripts/controls/GKE-02.py).

**Operations:** `clusters`, `asset_iam`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Authorize actions in clusters using role-based access control](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control) · [Apply predefined Pod-level security policies using PodSecurity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### GKE-03 — Assess workload and node identity

**Objective and applicability:** Assess workload and node identity. All in-scope uses of kubernetes and gke; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect Workload Identity Federation settings, node service accounts and metadata protection. Trace Kubernetes service-account identity grants to Google APIs.

**Required workpapers:** Kubernetes service-account mapping; node identity review.

**Consultant assessment criterion:** Workloads have appropriately scoped identities and cannot rely on unnecessarily privileged node credentials.

**Try to disprove the conclusion:** A workload without its own grant can obtain access through an excessive node identity or deployment permission.

**Script title:** Assess workload and node identity. **Description:** collect list gke cluster configuration, list service account identities, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open GKE-03.py](../scripts/controls/GKE-03.py).

**Operations:** `clusters`, `service_accounts`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [About Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) · [Protecting cluster metadata](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/protecting-cluster-metadata)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### GKE-04 — Review cluster maintenance and supply chain

**Objective and applicability:** Review cluster maintenance and supply chain. All in-scope uses of kubernetes and gke; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect versions, release channels, maintenance exclusions and node update policy. Reconcile image admission, vulnerability evidence and supported-version requirements.

**Required workpapers:** version inventory; upgrade history; image provenance.

**Consultant assessment criterion:** The cluster and node population follows an approved support and upgrade policy with controlled exclusions.

**Try to disprove the conclusion:** An apparently current control plane masks old nodes or a long-lived maintenance exclusion.

**Script title:** Review cluster maintenance and supply chain. **Description:** collect list gke cluster configuration, read binary authorization admission policy, list artifact registry repositories; create evidence requests and an unassessed review workpaper. [Open GKE-04.py](../scripts/controls/GKE-04.py).

**Operations:** `clusters`, `binary`, `repositories` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [About release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) · [Maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### GKE-05 — Assess workload isolation and recovery

**Objective and applicability:** Assess workload isolation and recovery. All in-scope uses of kubernetes and gke; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect dataplane, network-policy and backup configuration; obtain actual policy coverage, persistent-volume mapping and past restore results. Treat Autopilot and Standard responsibilities separately.

**Required workpapers:** network-policy export; volume inventory; restore report.

**Consultant assessment criterion:** Isolation and recovery requirements are evidenced at workload level, including persistent state.

**Try to disprove the conclusion:** A network-policy capability is enabled but a sensitive namespace has no effective policy, or its volumes are outside backup scope.

**Script title:** Assess workload isolation and recovery. **Description:** collect list gke cluster configuration, inventory resource configuration, list disk snapshot metadata; create evidence requests and an unassessed review workpaper. [Open GKE-05.py](../scripts/controls/GKE-05.py).

**Operations:** `clusters`, `assets`, `snapshots` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Control communication between Pods and Services using network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) · [Backup for GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## RUN — Serverless and messaging

Suggested accountable owner: **Application platform lead**.

### RUN-01 — Review Cloud Run exposure and identity

**Objective and applicability:** Review Cloud Run exposure and identity. All in-scope uses of serverless and messaging; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect service ingress, revision configuration, authentication/IAM and runtime identities across all approved regions. Review direct service URLs and load-balancer paths together.

**Required workpapers:** service architecture; invoker review; region inventory.

**Consultant assessment criterion:** Public invocation and runtime privileges match the application's approved exposure.

**Try to disprove the conclusion:** A load balancer is protected while the underlying service remains invokable directly.

**Script title:** Review Cloud Run exposure and identity. **Description:** collect list cloud run services, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open RUN-01.py](../scripts/controls/RUN-01.py).

**Operations:** `run_services`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Restrict network endpoint ingress for Cloud Run services and instances](https://docs.cloud.google.com/run/docs/securing/ingress) · [Authentication overview](https://docs.cloud.google.com/run/docs/authenticating/overview)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### RUN-02 — Assess functions and event triggers

**Objective and applicability:** Assess functions and event triggers. All in-scope uses of serverless and messaging; document approved exclusions and service absence.

**Read-only evidence procedure:** Map functions to generation, runtime identity, ingress and event sources. Reconcile source ownership, authentication and supported runtime lifecycle.

**Required workpapers:** function inventory; trigger policy; runtime review.

**Consultant assessment criterion:** Each function and trigger has controlled invocation and maintained runtime dependencies.

**Try to disprove the conclusion:** An event path or old function generation is omitted from the application inventory.

**Script title:** Assess functions and event triggers. **Description:** collect list cloud run functions, inventory resource configuration, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open RUN-02.py](../scripts/controls/RUN-02.py).

**Operations:** `functions`, `assets`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Authorize access with IAM](https://docs.cloud.google.com/functions/docs/securing/managing-access-iam) · [Runtime support](https://docs.cloud.google.com/functions/docs/runtime-support)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### RUN-03 — Inspect scheduled and batch execution

**Objective and applicability:** Inspect scheduled and batch execution. All in-scope uses of serverless and messaging; document approved exclusions and service absence.

**Read-only evidence procedure:** Review Cloud Run jobs and Scheduler targets, service identities and authorization. Check whether embedded request bodies, arguments or environment values contain sensitive material.

**Required workpapers:** job ownership; failure records; target authorization.

**Consultant assessment criterion:** Automated jobs have least-privileged identities, reviewed destinations and failure handling.

**Try to disprove the conclusion:** A scheduler can call an unintended authenticated endpoint or silently fails without owner response.

**Script title:** Inspect scheduled and batch execution. **Description:** collect list cloud run jobs, list cloud scheduler jobs, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open RUN-03.py](../scripts/controls/RUN-03.py).

**Operations:** `run_jobs`, `scheduler`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Create jobs](https://docs.cloud.google.com/run/docs/create-jobs) · [Use authentication with HTTP targets](https://docs.cloud.google.com/scheduler/docs/http-target-auth)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### RUN-04 — Review messaging access and data lifecycle

**Objective and applicability:** Review messaging access and data lifecycle. All in-scope uses of serverless and messaging; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect topic and subscription IAM, push authentication, retention, dead-letter configuration and encryption references. Reconcile subscriber destinations and data sensitivity.

**Required workpapers:** messaging data flow; subscriber ownership; retention approval.

**Consultant assessment criterion:** Authorized publishers and subscribers, retention and delivery behavior match the approved data flow.

**Try to disprove the conclusion:** An external push endpoint or dead-letter topic retains sensitive data outside the documented boundary.

**Script title:** Review messaging access and data lifecycle. **Description:** collect list pub/sub topic configuration, list pub/sub subscription configuration, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open RUN-04.py](../scripts/controls/RUN-04.py).

**Operations:** `pubsub_topics`, `pubsub_subs`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Subscription properties](https://docs.cloud.google.com/pubsub/docs/subscription-properties) · [Authenticate to Pub/Sub](https://docs.cloud.google.com/pubsub/docs/authentication)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### RUN-05 — Assess runtime secrets and network dependencies

**Objective and applicability:** Assess runtime secrets and network dependencies. All in-scope uses of serverless and messaging; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect revision metadata, secret references, VPC connectivity and egress configuration. Obtain deployment records and existing health evidence without invoking workloads.

**Required workpapers:** deployment history; secret mapping; dependency diagram.

**Consultant assessment criterion:** Runtime dependencies, secret versions and network access follow the deployment baseline.

**Try to disprove the conclusion:** A new revision uses an unreviewed secret version or broad egress and remains outside the operating review.

**Script title:** Assess runtime secrets and network dependencies. **Description:** collect list cloud run services, list cloud run functions, list secret manager metadata, list secret version metadata; create evidence requests and an unassessed review workpaper. [Open RUN-05.py](../scripts/controls/RUN-05.py).

**Operations:** `run_services`, `functions`, `secrets`, `secret_versions` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Configure secrets for services](https://docs.cloud.google.com/run/docs/configuring/services/secrets) · [Compare Direct VPC egress and VPC connectors](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## STO — Cloud Storage and data protection

Suggested accountable owner: **Storage and data owner**.

### STO-01 — Assess public and external bucket access

**Objective and applicability:** Assess public and external bucket access. All in-scope uses of cloud storage and data protection; document approved exclusions and service absence.

**Read-only evidence procedure:** Join bucket metadata, IAM bindings, inherited public access prevention and approved external-sharing uses. If uniform access is off, request object ACL metadata separately; do not download objects.

**Required workpapers:** sharing register; ACL metadata when applicable; signed URL governance.

**Consultant assessment criterion:** Public and external access is intentional and governed across IAM, ACL and signed-access paths.

**Try to disprove the conclusion:** Public prevention is enabled but long-lived signed URLs or legacy object ACL exposure are absent from the review.

**Script title:** Assess public and external bucket access. **Description:** collect list cloud storage bucket metadata, inventory resource allow policies, read a selected effective organization policy; create evidence requests and an unassessed review workpaper. [Open STO-01.py](../scripts/controls/STO-01.py).

**Operations:** `buckets`, `asset_iam`, `effective_policy` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention) · [Signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### STO-02 — Review uniform access and granular permissions

**Objective and applicability:** Review uniform access and granular permissions. All in-scope uses of cloud storage and data protection; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect uniform bucket-level access, managed folders and resource IAM. Reconcile legacy bucket and object ACLs where uniform access is disabled.

**Required workpapers:** bucket permission review; managed-folder inventory; legacy ACL export.

**Consultant assessment criterion:** The actual permission system is covered by the access review, including managed folders.

**Try to disprove the conclusion:** A project-level review overlooks a bucket or managed-folder grant, or assumes IAM describes every object ACL.

**Script title:** Review uniform access and granular permissions. **Description:** collect list cloud storage bucket metadata, inventory resource allow policies, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open STO-02.py](../scripts/controls/STO-02.py).

**Operations:** `buckets`, `asset_iam`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) · [Managed folders](https://docs.cloud.google.com/storage/docs/managed-folders)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### STO-03 — Assess retention lifecycle and deletion recovery

**Objective and applicability:** Assess retention lifecycle and deletion recovery. All in-scope uses of cloud storage and data protection; document approved exclusions and service absence.

**Read-only evidence procedure:** Review retention policy, lock status, lifecycle rules, versioning and soft-delete settings against approved retention and recovery requirements.

**Required workpapers:** retention schedule; legal holds; recovery examples.

**Consultant assessment criterion:** Retention and deletion recovery work together with legal requirements and operational needs; locks are assessed without changing them.

**Try to disprove the conclusion:** A lifecycle action removes recoverable versions before the required recovery window.

**Script title:** Assess retention lifecycle and deletion recovery. **Description:** collect list cloud storage bucket metadata, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open STO-03.py](../scripts/controls/STO-03.py).

**Operations:** `buckets`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock) · [Soft delete overview](https://docs.cloud.google.com/storage/docs/soft-delete) · [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### STO-04 — Inspect bucket encryption and location

**Objective and applicability:** Inspect bucket encryption and location. All in-scope uses of cloud storage and data protection; document approved exclusions and service absence.

**Read-only evidence procedure:** Map storage location, default key references and object-encryption evidence to requirements. A default CMEK setting alone does not prove all existing objects use that key.

**Required workpapers:** encryption coverage export; location requirements; key dependency map.

**Consultant assessment criterion:** Location and encryption requirements are supported for current and historical data populations.

**Try to disprove the conclusion:** An object predates the default key change or a key's location conflicts with the assumed recovery design.

**Script title:** Inspect bucket encryption and location. **Description:** collect list cloud storage bucket metadata, inventory resource configuration, list cryptographic key configuration; create evidence requests and an unassessed review workpaper. [Open STO-04.py](../scripts/controls/STO-04.py).

**Operations:** `buckets`, `assets`, `keys` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) · [Bucket locations](https://docs.cloud.google.com/storage/docs/locations)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### STO-05 — Review storage logging and transfer paths

**Objective and applicability:** Review storage logging and transfer paths. All in-scope uses of cloud storage and data protection; document approved exclusions and service absence.

**Read-only evidence procedure:** Reconcile Data Access settings, bucket access patterns, storage-transfer resources and owner-provided transfer histories. Inspect service-agent permissions and external destinations.

**Required workpapers:** transfer-job export; access review; logging coverage.

**Consultant assessment criterion:** Material reads and transfers have the agreed authorization, telemetry and retention coverage.

**Try to disprove the conclusion:** An apparently inactive public object path produces no authenticated access log and is misclassified as unused.

**Script title:** Review storage logging and transfer paths. **Description:** collect list cloud storage bucket metadata, inventory resource allow policies, sample audit events within the approved window, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open STO-05.py](../scripts/controls/STO-05.py).

**Operations:** `buckets`, `asset_iam`, `audit_logs`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Cloud Audit Logs with Cloud Storage](https://docs.cloud.google.com/storage/docs/audit-logging) · [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## DAT — Databases and analytics

Suggested accountable owner: **Database and analytics lead**.

### DAT-01 — Review Cloud SQL access and exposure

**Objective and applicability:** Review Cloud SQL access and exposure. All in-scope uses of databases and analytics; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect public and private addresses, authorized networks, TLS requirements, flags and IAM database authentication. Request database-native user and grant evidence; project IAM is only part of the review.

**Required workpapers:** database user and grant export; connectivity design; engine baseline.

**Consultant assessment criterion:** Network paths and database identities meet the approved access model for each engine.

**Try to disprove the conclusion:** A private instance has an unmanaged database administrator or a TLS mode weaker than the documented baseline.

**Script title:** Review Cloud SQL access and exposure. **Description:** collect list cloud sql instance configuration, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open DAT-01.py](../scripts/controls/DAT-01.py).

**Operations:** `sql`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [IAM authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication) · [Authorize with authorized networks](https://docs.cloud.google.com/sql/docs/postgres/authorize-networks) · [Configure SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### DAT-02 — Assess SQL availability and recovery

**Objective and applicability:** Assess SQL availability and recovery. All in-scope uses of databases and analytics; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect availability type, backups, point-in-time recovery and replica configuration for the actual database engine. Review past restore records and dependent encryption keys.

**Required workpapers:** recovery objectives; backup history; restore results.

**Consultant assessment criterion:** The selected configuration and demonstrated restore capability meet approved RPO and RTO.

**Try to disprove the conclusion:** A successful backup exists but point-in-time recovery is unavailable for the incident window.

**Script title:** Assess SQL availability and recovery. **Description:** collect list cloud sql instance configuration, list existing cloud sql backup records, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open DAT-02.py](../scripts/controls/DAT-02.py).

**Operations:** `sql`, `sql_backups`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Cloud SQL backups overview](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups) · [About high availability](https://docs.cloud.google.com/sql/docs/postgres/high-availability)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### DAT-03 — Review BigQuery access and fine-grained controls

**Objective and applicability:** Review BigQuery access and fine-grained controls. All in-scope uses of databases and analytics; document approved exclusions and service absence.

**Read-only evidence procedure:** Use dataset and table asset metadata plus approved exports of row policies, policy tags, masking rules and authorized views. Trace inherited IAM, dataset ACLs and data-sharing links.

**Required workpapers:** dataset ACL export; row and column policy metadata; sharing register.

**Consultant assessment criterion:** Sensitive data access is justified at dataset, table, row and column levels where required; metadata-only coverage is documented.

**Try to disprove the conclusion:** An authorized view or broad dataset grant bypasses the intended interpretation of a masking control.

**Script title:** Review BigQuery access and fine-grained controls. **Description:** collect inventory resource configuration, inventory resource allow policies, sample audit events within the approved window; create evidence requests and an unassessed review workpaper. [Open DAT-03.py](../scripts/controls/DAT-03.py).

**Operations:** `assets`, `asset_iam`, `audit_logs` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Introduction to BigQuery row-level security](https://docs.cloud.google.com/bigquery/docs/row-level-security-intro) · [Introduction to column-level access control](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro) · [Authorized views](https://docs.cloud.google.com/bigquery/docs/authorized-views)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### DAT-04 — Assess BigQuery lifecycle and query governance

**Objective and applicability:** Assess BigQuery lifecycle and query governance. All in-scope uses of databases and analytics; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect dataset locations, encryption, expirations, reservations and job-history evidence supplied by owners. Review copies, extracts and scheduled transfers without running SQL jobs.

**Required workpapers:** job-history metadata; transfer schedules; data retention matrix.

**Consultant assessment criterion:** Retention, processing locations and query/export use match approved data and cost policies.

**Try to disprove the conclusion:** A dataset expiry looks compliant while extracted tables persist in another project or bucket.

**Script title:** Assess BigQuery lifecycle and query governance. **Description:** collect inventory resource configuration, inventory resource allow policies, sample audit events within the approved window; create evidence requests and an unassessed review workpaper. [Open DAT-04.py](../scripts/controls/DAT-04.py).

**Operations:** `assets`, `asset_iam`, `audit_logs` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Manage datasets](https://docs.cloud.google.com/bigquery/docs/managing-datasets) · [BigQuery audit logs overview](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs) · [Export table data to Cloud Storage](https://docs.cloud.google.com/bigquery/docs/exporting-data)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### DAT-05 — Assess other managed data platforms

**Objective and applicability:** Assess other managed data platforms. All in-scope uses of databases and analytics; document approved exclusions and service absence.

**Read-only evidence procedure:** Identify Spanner, Firestore, Bigtable, AlloyDB, Redis and data-processing services from inventory. Apply service-specific access, network, encryption, availability and backup tests using owner-provided metadata where native collectors are absent.

**Required workpapers:** service-specific configuration exports; native grants; restore evidence.

**Consultant assessment criterion:** Every material data platform has an explicit evidence plan; absence of a dedicated collector is not treated as absence of risk.

**Try to disprove the conclusion:** A critical Firestore or Bigtable service is omitted because only SQL instances were enumerated.

**Script title:** Assess other managed data platforms. **Description:** collect list spanner instances, list memorystore redis instances, inventory resource configuration, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open DAT-05.py](../scripts/controls/DAT-05.py).

**Operations:** `spanner`, `redis`, `assets`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Security, privacy, risk, and compliance for Spanner](https://docs.cloud.google.com/spanner/docs/security-privacy-compliance) · [Security for server client libraries](https://docs.cloud.google.com/firestore/docs/security/overview) · [Bigtable access control with IAM](https://docs.cloud.google.com/bigtable/docs/access-control) · [AlloyDB overview](https://docs.cloud.google.com/alloydb/docs/overview)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## KEY — Secrets and cryptographic keys

Suggested accountable owner: **Cryptography and secrets owner**.

### KEY-01 — Review Secret Manager access and replication

**Objective and applicability:** Review Secret Manager access and replication. All in-scope uses of secrets and cryptographic keys; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect secret metadata, replication, IAM, labels and owners. Trace read and administration privileges while never accessing secret payloads.

**Required workpapers:** secret ownership; consumer mapping; access review.

**Consultant assessment criterion:** Secret access and location are justified and match the documented consuming workloads.

**Try to disprove the conclusion:** A broad project-level Secret Accessor grant exposes unrelated application secrets.

**Script title:** Review Secret Manager access and replication. **Description:** collect list secret manager metadata, inventory resource allow policies, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open KEY-01.py](../scripts/controls/KEY-01.py).

**Operations:** `secrets`, `asset_iam`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Secret Manager best practices](https://docs.cloud.google.com/secret-manager/docs/best-practices) · [Access control with IAM](https://docs.cloud.google.com/secret-manager/docs/access-control)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### KEY-02 — Assess secret rotation and version lifecycle

**Objective and applicability:** Assess secret rotation and version lifecycle. All in-scope uses of secrets and cryptographic keys; document approved exclusions and service absence.

**Read-only evidence procedure:** List version metadata, status and dates; inspect rotation notifications, automation records and deployment version references. A rotation schedule is not proof the secret changed.

**Required workpapers:** rotation execution records; version-to-deployment mapping.

**Consultant assessment criterion:** Rotation and revocation operate within approved requirements and applications consume intended versions.

**Try to disprove the conclusion:** A configured rotation topic has no functioning subscriber or workloads still use an old enabled version.

**Script title:** Assess secret rotation and version lifecycle. **Description:** collect list secret manager metadata, list secret version metadata, list cloud run services; create evidence requests and an unassessed review workpaper. [Open KEY-02.py](../scripts/controls/KEY-02.py).

**Operations:** `secrets`, `secret_versions`, `run_services` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [About rotation schedules](https://docs.cloud.google.com/secret-manager/docs/rotation-recommendations) · [View secret version details](https://docs.cloud.google.com/secret-manager/docs/view-secret-version)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### KEY-03 — Assess KMS purpose and separation of duties

**Objective and applicability:** Assess KMS purpose and separation of duties. All in-scope uses of secrets and cryptographic keys; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect key rings, algorithms, protection level, IAM and encrypt/decrypt versus administration permissions. Map key projects and service agents to protected resources.

**Required workpapers:** key inventory; custody matrix; access review.

**Consultant assessment criterion:** Key administration and use align with the approved custody and separation model.

**Try to disprove the conclusion:** A data administrator can also grant themselves decryption access to the same sensitive dataset.

**Script title:** Assess KMS purpose and separation of duties. **Description:** collect list cloud kms key rings, list cryptographic key configuration, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open KEY-03.py](../scripts/controls/KEY-03.py).

**Operations:** `keyrings`, `keys`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Separation of duties](https://docs.cloud.google.com/kms/docs/separation-of-duties) · [Access control with IAM](https://docs.cloud.google.com/kms/docs/iam)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### KEY-04 — Review key lifecycle and availability

**Objective and applicability:** Review key lifecycle and availability. All in-scope uses of secrets and cryptographic keys; document approved exclusions and service absence.

**Read-only evidence procedure:** Review primary versions, rotation and destruction schedule evidence. Reconcile disabled or pending-destruction versions with active data and backup dependencies.

**Required workpapers:** key-version metadata export; destruction approvals; dependency mapping.

**Consultant assessment criterion:** Key lifecycle changes preserve required availability and approved cryptographic policy.

**Try to disprove the conclusion:** A retained backup depends on a key version scheduled for destruction before retention ends.

**Script title:** Review key lifecycle and availability. **Description:** collect list cryptographic key configuration, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open KEY-04.py](../scripts/controls/KEY-04.py).

**Operations:** `keys`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Key rotation](https://docs.cloud.google.com/kms/docs/key-rotation) · [Key version states](https://docs.cloud.google.com/kms/docs/key-states)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### KEY-05 — Assess CMEK and external key dependencies

**Objective and applicability:** Assess CMEK and external key dependencies. All in-scope uses of secrets and cryptographic keys; document approved exclusions and service absence.

**Read-only evidence procedure:** Map required CMEK coverage and EKM or HSM requirements to actual resource metadata and service support. Review provider outages, key access and previous recovery evidence.

**Required workpapers:** CMEK coverage matrix; external-key contract; recovery evidence.

**Consultant assessment criterion:** The adopted encryption model is implemented where required and its operational dependencies are understood.

**Try to disprove the conclusion:** A CMEK label is present while the service resource uses provider-managed encryption, or EKM recovery is untested.

**Script title:** Assess CMEK and external key dependencies. **Description:** collect inventory resource configuration, list cryptographic key configuration; create evidence requests and an unassessed review workpaper. [Open KEY-05.py](../scripts/controls/KEY-05.py).

**Operations:** `assets`, `keys` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) · [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## LOG — Audit logging and evidence retention

Suggested accountable owner: **Security logging lead**.

### LOG-01 — Verify Data Access audit coverage

**Objective and applicability:** Verify Data Access audit coverage. All in-scope uses of audit logging and evidence retention; document approved exclusions and service absence.

**Read-only evidence procedure:** Read organization, ancestor-folder and project auditConfigs, service exceptions and exempted principals. Map enabled services to the required ADMIN_READ, DATA_READ and DATA_WRITE coverage.

**Required workpapers:** service logging matrix; effective auditConfig analysis.

**Consultant assessment criterion:** The adopted logging matrix is effectively configured and inherited exemptions are explicitly reviewed.

**Try to disprove the conclusion:** An empty project auditConfig is interpreted without inspecting inherited settings, or an exemption suppresses the chosen principal.

**Script title:** Verify Data Access audit coverage. **Description:** collect read organization iam and audit configuration, read ancestor folder iam and audit configuration, read project iam and audit configuration, list enabled service apis; create evidence requests and an unassessed review workpaper. [Open LOG-01.py](../scripts/controls/LOG-01.py).

**Operations:** `org_iam`, `folder_iam`, `project_iam`, `services` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Cloud Audit Logs overview](https://docs.cloud.google.com/logging/docs/audit) · [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### LOG-02 — Review routing sinks and exclusions

**Objective and applicability:** Review routing sinks and exclusions. All in-scope uses of audit logging and evidence retention; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect project and organization sinks, inclusion and exclusion filters, destination ownership and writer grants. Review intercepting behavior and aggregated child scope.

**Required workpapers:** sink destination IAM; delivery metrics; filter review.

**Consultant assessment criterion:** Required events reach approved destinations without unintended filtering or privilege gaps.

**Try to disprove the conclusion:** A central sink exists but its writer lacks destination access or its filter excludes the target event.

**Script title:** Review routing sinks and exclusions. **Description:** collect read organization aggregated logging sinks, read project logging sinks, read sink exclusion filters, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open LOG-02.py](../scripts/controls/LOG-02.py).

**Operations:** `org_sinks`, `sinks`, `exclusions`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Route log entries](https://docs.cloud.google.com/logging/docs/routing/overview) · [Collate and route organization- and folder-level logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### LOG-03 — Assess retention location and protected access

**Objective and applicability:** Assess retention location and protected access. All in-scope uses of audit logging and evidence retention; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect log bucket retention, location, access restrictions and lock state across all used locations. Reconcile SIEM and archive retention outside Cloud Logging.

**Required workpapers:** retention matrix; SIEM settings; bucket access review.

**Consultant assessment criterion:** The retention and access model satisfies the adopted evidence requirements across every copy.

**Try to disprove the conclusion:** Only global buckets were checked while a regional bucket holds the relevant events for a shorter period.

**Script title:** Assess retention location and protected access. **Description:** collect read regional log bucket retention, inventory resource configuration, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open LOG-03.py](../scripts/controls/LOG-03.py).

**Operations:** `log_buckets`, `assets`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Configure log buckets](https://docs.cloud.google.com/logging/docs/buckets) · [Route log entries](https://docs.cloud.google.com/logging/docs/storage)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### LOG-04 — Prove an existing event's end-to-end trace

**Objective and applicability:** Prove an existing event's end-to-end trace. All in-scope uses of audit logging and evidence retention; document approved exclusions and service absence.

**Read-only evidence procedure:** Select a known historical approved administrative or data event from a ticket. Trace it through source logging, sink routing, destination and detection within a bounded UTC window.

**Required workpapers:** known-event record; source and destination evidence; timing comparison.

**Consultant assessment criterion:** The specific event is attributable and retrievable with expected fields and timing; the sample's limits are documented.

**Try to disprove the conclusion:** The source event is present but disappears after routing, or the sampled log window omits the ticket time.

**Script title:** Prove an existing event's end-to-end trace. **Description:** collect sample audit events within the approved window, read project logging sinks, list logs-based metrics; create evidence requests and an unassessed review workpaper. [Open LOG-04.py](../scripts/controls/LOG-04.py).

**Operations:** `audit_logs`, `sinks`, `log_metrics` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language) · [Understanding audit logs](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### LOG-05 — Assess integrity and evidence visibility

**Objective and applicability:** Assess integrity and evidence visibility. All in-scope uses of audit logging and evidence retention; document approved exclusions and service absence.

**Read-only evidence procedure:** Review log administration, private-log viewing, deletion and sink modification privileges. Reconcile coverage counts and missing-access errors before concluding about activity.

**Required workpapers:** evidence-access matrix; error register; log administrator review.

**Consultant assessment criterion:** The audit can explain who can read or affect evidence and where visibility is incomplete.

**Try to disprove the conclusion:** The collector receives no private entries because it lacks Private Logs Viewer permissions.

**Script title:** Assess integrity and evidence visibility. **Description:** collect inventory resource allow policies, sample audit events within the approved window, read project iam and audit configuration; create evidence requests and an unassessed review workpaper. [Open LOG-05.py](../scripts/controls/LOG-05.py).

**Operations:** `asset_iam`, `audit_logs`, `project_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control) · [Best practices for Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit/best-practices)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## SEC — Detection and incident response

Suggested accountable owner: **Security operations lead**.

### SEC-01 — Assess Security Command Center coverage

**Objective and applicability:** Assess Security Command Center coverage. All in-scope uses of detection and incident response; document approved exclusions and service absence.

**Read-only evidence procedure:** Reconcile activation scope, edition, data location, services, detectors and project population with expected coverage. Read findings and record activation or permission failures.

**Required workpapers:** SCC configuration export; coverage matrix; detector status.

**Consultant assessment criterion:** Finding absence is interpreted only after coverage is demonstrated; tier-dependent gaps have compensating evidence.

**Try to disprove the conclusion:** An empty finding list comes from a location without the organization's findings or a disabled detector.

**Script title:** Assess Security Command Center coverage. **Description:** collect read security command center findings, reconcile organization project inventory, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open SEC-01.py](../scripts/controls/SEC-01.py).

**Operations:** `scc`, `org_assets`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Security Command Center service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) · [Security Command Center overview](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### SEC-02 — Review finding triage and suppression

**Objective and applicability:** Review finding triage and suppression. All in-scope uses of detection and incident response; document approved exclusions and service absence.

**Read-only evidence procedure:** Sample active findings, muted records and ticket links. Evaluate severity, exploitability, asset criticality, owner, age and suppression justification.

**Required workpapers:** triage queue; mute rules; ticket samples.

**Consultant assessment criterion:** Material findings receive timely owned decisions under approved response targets.

**Try to disprove the conclusion:** A long-lived mute hides a recurring public exposure with no expiry or risk acceptance.

**Script title:** Review finding triage and suppression. **Description:** collect read security command center findings, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open SEC-02.py](../scripts/controls/SEC-02.py).

**Operations:** `scc`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Review and manage findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings) · [Mute findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### SEC-03 — Validate detection use cases

**Objective and applicability:** Validate detection use cases. All in-scope uses of detection and incident response; document approved exclusions and service absence.

**Read-only evidence procedure:** Map priority threats to required logs, analytics, alert routes and past incident or exercise records. Inspect existing test results rather than injecting attacks.

**Required workpapers:** detection catalog; prior exercise results; alert routing export.

**Consultant assessment criterion:** The agreed use cases have demonstrated signal delivery and response evidence.

**Try to disprove the conclusion:** A detection rule is enabled but depends on a disabled Data Access log source.

**Script title:** Validate detection use cases. **Description:** collect sample audit events within the approved window, list logs-based metrics, read security command center findings; create evidence requests and an unassessed review workpaper. [Open SEC-03.py](../scripts/controls/SEC-03.py).

**Operations:** `audit_logs`, `log_metrics`, `scc` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Overview of Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) · [Configure log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### SEC-04 — Assess incident readiness and containment authority

**Objective and applicability:** Assess incident readiness and containment authority. All in-scope uses of detection and incident response; document approved exclusions and service absence.

**Read-only evidence procedure:** Review contacts, evidence preservation, organization access, service-account revocation and network isolation procedures. Compare responsibilities against a previous incident or tabletop.

**Required workpapers:** incident plan; contact roster; tabletop report.

**Consultant assessment criterion:** Responders can identify authorized decision makers and required access during the stated scenario.

**Try to disprove the conclusion:** A responder's emergency credentials depend on the affected identity service or cannot access the evidence project.

**Script title:** Assess incident readiness and containment authority. **Description:** collect read organization iam and audit configuration, inventory resource allow policies, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open SEC-04.py](../scripts/controls/SEC-04.py).

**Operations:** `org_iam`, `asset_iam`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Operations best practices](https://docs.cloud.google.com/architecture/blueprints/security-foundations/operation-best-practices) · [Google security overview](https://docs.cloud.google.com/docs/security/overview/whitepaper)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### SEC-05 — Review incident lessons and closure

**Objective and applicability:** Review incident lessons and closure. All in-scope uses of detection and incident response; document approved exclusions and service absence.

**Read-only evidence procedure:** Trace a sample of historical incidents through scope, root-cause evidence, notification decisions and verified corrective actions. Compare recurring SCC findings and logs.

**Required workpapers:** incident sample; postmortems; closure evidence.

**Consultant assessment criterion:** Closure includes validation of the failed control and documented residual risk.

**Try to disprove the conclusion:** A closed incident recurs with the same underlying access path.

**Script title:** Review incident lessons and closure. **Description:** collect read security command center findings, sample audit events within the approved window; create evidence requests and an unassessed review workpaper. [Open SEC-05.py](../scripts/controls/SEC-05.py).

**Operations:** `scc`, `audit_logs` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Well-Architected Framework: Operational excellence pillar](https://docs.cloud.google.com/architecture/framework/operational-excellence/learn-from-failures)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## BCP — Business continuity and recovery

Suggested accountable owner: **Business continuity lead**.

### BCP-01 — Map recovery objectives to dependencies

**Objective and applicability:** Map recovery objectives to dependencies. All in-scope uses of business continuity and recovery; document approved exclusions and service absence.

**Read-only evidence procedure:** Join critical services to data stores, identities, keys, DNS, networking and provider dependencies. Obtain business-approved RPO and RTO, including data-loss tolerance.

**Required workpapers:** business impact analysis; dependency map; approved RPO/RTO.

**Consultant assessment criterion:** Recovery objectives cover the complete service chain and have accountable owners.

**Try to disprove the conclusion:** A database meets its RTO while identity or DNS recovery prevents the business application from operating.

**Script title:** Map recovery objectives to dependencies. **Description:** collect inventory resource configuration, read project billing association; create evidence requests and an unassessed review workpaper. [Open BCP-01.py](../scripts/controls/BCP-01.py).

**Operations:** `assets`, `billing_link` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide) · [Well-Architected Framework: Reliability pillar](https://docs.cloud.google.com/architecture/framework/reliability)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### BCP-02 — Review backup coverage and immutability

**Objective and applicability:** Review backup coverage and immutability. All in-scope uses of business continuity and recovery; document approved exclusions and service absence.

**Read-only evidence procedure:** Reconcile data-bearing resources with snapshot, SQL backup, GKE backup and Backup and DR metadata. Inspect retention, separation, vault protection and administration.

**Required workpapers:** backup coverage matrix; vault settings export; administrator review.

**Consultant assessment criterion:** All required data has a mapped backup mechanism and approved protection from common administrative failure.

**Try to disprove the conclusion:** The same compromised administrator can erase production data and every retained backup.

**Script title:** Review backup coverage and immutability. **Description:** collect list disk snapshot metadata, list regional resource policies, list existing cloud sql backup records, inventory resource configuration, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open BCP-02.py](../scripts/controls/BCP-02.py).

**Operations:** `snapshots`, `schedules`, `sql_backups`, `assets`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Backup vaults for immutable and indelible backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault) · [Create schedules for disk snapshots](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### BCP-03 — Assess restore evidence

**Objective and applicability:** Assess restore evidence. All in-scope uses of business continuity and recovery; document approved exclusions and service absence.

**Read-only evidence procedure:** Read existing backup metadata and hash supplied prior restore reports. Review restored scope, timestamp, data integrity checks, elapsed time and business acceptance.

**Required workpapers:** dated restore reports; integrity checks; business sign-off.

**Consultant assessment criterion:** Prior restore evidence demonstrates the agreed objective for the sampled system; missing exercises remain a gap.

**Try to disprove the conclusion:** A report says successful but omits application integrity checks or restores only an empty database.

**Script title:** Assess restore evidence. **Description:** collect list disk snapshot metadata, list existing cloud sql backup records, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open BCP-03.py](../scripts/controls/BCP-03.py).

**Operations:** `snapshots`, `sql_backups`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide) · [Restore an instance using a backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restoring)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### BCP-04 — Review regional and zonal failure readiness

**Objective and applicability:** Review regional and zonal failure readiness. All in-scope uses of business continuity and recovery; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect multi-zone or regional configurations and compare capacity, quotas and dependencies to the failover design. Evaluate existing exercises and their assumptions.

**Required workpapers:** failover design; capacity evidence; prior exercise.

**Consultant assessment criterion:** The adopted failure scenario is covered by realistic capacity and independent dependencies.

**Try to disprove the conclusion:** A secondary region shares a key, network or quota bottleneck that prevents recovery.

**Script title:** Review regional and zonal failure readiness. **Description:** collect list compute engine instance configuration, list gke cluster configuration, list cloud sql instance configuration, read compute project quotas and metadata; create evidence requests and an unassessed review workpaper. [Open BCP-04.py](../scripts/controls/BCP-04.py).

**Operations:** `instances`, `clusters`, `sql`, `project_info` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Build highly available systems through resource redundancy](https://docs.cloud.google.com/architecture/framework/reliability/design-scale-high-availability)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### BCP-05 — Assess recovery operations and ownership

**Objective and applicability:** Assess recovery operations and ownership. All in-scope uses of business continuity and recovery; document approved exclusions and service absence.

**Read-only evidence procedure:** Review recovery runbooks, access prerequisites, communications and retrospective improvements. Verify named owners can locate retained evidence and necessary approvals.

**Required workpapers:** runbook review; access checklist; exercise action log.

**Consultant assessment criterion:** Runbooks remain usable under the scenario and material exercise findings are resolved or accepted.

**Try to disprove the conclusion:** An offline recovery step requires a console or repository available only in the failed environment.

**Script title:** Assess recovery operations and ownership. **Description:** collect inventory resource configuration, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open BCP-05.py](../scripts/controls/BCP-05.py).

**Operations:** `assets`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## DEV — Software delivery and supply chain

Suggested accountable owner: **DevSecOps lead**.

### DEV-01 — Review source and build trigger trust

**Objective and applicability:** Review source and build trigger trust. All in-scope uses of software delivery and supply chain; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect Cloud Build triggers, event filters, approval settings, repository connections and execution identities. Reconcile branch protection and contributor permissions from the source platform.

**Required workpapers:** repository protection export; pipeline design; trigger approvals.

**Consultant assessment criterion:** Untrusted changes cannot silently obtain production deployment authority through the approved pipeline.

**Try to disprove the conclusion:** A pull request can edit the pipeline that runs with a production service account.

**Script title:** Review source and build trigger trust. **Description:** collect read cloud build triggers, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open DEV-01.py](../scripts/controls/DEV-01.py).

**Operations:** `build_triggers`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Gate builds on approval](https://docs.cloud.google.com/build/docs/securing-builds/gate-builds-on-approval)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### DEV-02 — Assess build identity and secrets

**Objective and applicability:** Assess build identity and secrets. All in-scope uses of software delivery and supply chain; document approved exclusions and service absence.

**Read-only evidence procedure:** Review build service accounts, worker pools, network access and secret references. Inspect a bounded sample of historical builds without triggering builds.

**Required workpapers:** build configuration export; secret mapping; identity review.

**Consultant assessment criterion:** Build privileges and secret availability are appropriate to repository trust and deployment purpose.

**Try to disprove the conclusion:** An untrusted build can impersonate the same identity that deploys production.

**Script title:** Assess build identity and secrets. **Description:** collect sample existing cloud build execution metadata, read cloud build triggers, inventory resource configuration, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open DEV-02.py](../scripts/controls/DEV-02.py).

**Operations:** `builds`, `build_triggers`, `assets`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Configure access for the default Cloud Build service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account) · [Use secrets from Secret Manager](https://docs.cloud.google.com/build/docs/securing-builds/use-secrets)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### DEV-03 — Review artifact access and vulnerability governance

**Objective and applicability:** Review artifact access and vulnerability governance. All in-scope uses of software delivery and supply chain; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect repository locations, format, IAM and cleanup policies; obtain scan status, SBOM and exception evidence for deployed digests.

**Required workpapers:** deployed digest register; scan export; SBOM; exceptions.

**Consultant assessment criterion:** Deployed artifacts have attributable provenance and reviewed vulnerabilities under the adopted policy.

**Try to disprove the conclusion:** A clean repository summary excludes the exact digest running in production.

**Script title:** Review artifact access and vulnerability governance. **Description:** collect list artifact registry repositories, inventory resource allow policies, list gke cluster configuration, list cloud run services; create evidence requests and an unassessed review workpaper. [Open DEV-03.py](../scripts/controls/DEV-03.py).

**Operations:** `repositories`, `asset_iam`, `clusters`, `run_services` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Access control with IAM](https://docs.cloud.google.com/artifact-registry/docs/access-control) · [Container scanning overview](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### DEV-04 — Assess deployment approvals and admission

**Objective and applicability:** Assess deployment approvals and admission. All in-scope uses of software delivery and supply chain; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect delivery pipelines, Binary Authorization policy and approved attestor evidence. Trace one deployed artifact to source, build, approval and admission result.

**Required workpapers:** release sample; attestation metadata; admission results.

**Consultant assessment criterion:** Production admission and approval requirements are effective, with controlled break-glass use.

**Try to disprove the conclusion:** Policy exists but enforcement permits all images or a production target bypasses the pipeline.

**Script title:** Assess deployment approvals and admission. **Description:** collect read cloud deploy delivery pipelines, read binary authorization admission policy, list gke cluster configuration, list cloud run services; create evidence requests and an unassessed review workpaper. [Open DEV-04.py](../scripts/controls/DEV-04.py).

**Operations:** `deploy`, `binary`, `clusters`, `run_services` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Binary Authorization overview](https://docs.cloud.google.com/binary-authorization/docs/overview) · [Promote your release and manage approvals](https://docs.cloud.google.com/deploy/docs/promote-release)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### DEV-05 — Review infrastructure drift and change evidence

**Objective and applicability:** Review infrastructure drift and change evidence. All in-scope uses of software delivery and supply chain; document approved exclusions and service absence.

**Read-only evidence procedure:** Compare current resource exports with approved infrastructure-as-code state and change records. Trace risky IAM, firewall and policy changes in the audit sample.

**Required workpapers:** IaC export; drift report; change sample.

**Consultant assessment criterion:** Material drift is identified, owned and reconciled to approved changes.

**Try to disprove the conclusion:** A console change weakens a guardrail while the repository still shows the compliant setting.

**Script title:** Review infrastructure drift and change evidence. **Description:** collect inventory resource configuration, sample audit events within the approved window, read a selected effective organization policy; create evidence requests and an unassessed review workpaper. [Open DEV-05.py](../scripts/controls/DEV-05.py).

**Operations:** `assets`, `audit_logs`, `effective_policy` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations) · [Best practices for general style and structure](https://docs.cloud.google.com/docs/terraform/best-practices/general-style-structure)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## AI — AI and agent governance

Suggested accountable owner: **AI platform and data governance leads**.

### AI-01 — Inventory AI services and accountable uses

**Objective and applicability:** Inventory AI services and accountable uses. All in-scope uses of ai and agent governance; document approved exclusions and service absence.

**Read-only evidence procedure:** Inventory Vertex AI endpoints, models and datasets across approved regions; reconcile managed generative services, agent runtimes and external model integrations from application records.

**Required workpapers:** AI use-case register; provider inventory; application data flow.

**Consultant assessment criterion:** All material AI uses have owners, data classifications, model/provider records and approved purposes.

**Try to disprove the conclusion:** An application calls a managed model API without a dedicated endpoint and is missed by endpoint inventory.

**Script title:** Inventory AI services and accountable uses. **Description:** collect list vertex ai endpoints, list vertex ai model metadata, inventory supported vertex ai dataset metadata, list enabled service apis, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open AI-01.py](../scripts/controls/AI-01.py).

**Operations:** `ai_endpoints`, `ai_models`, `ai_datasets`, `services`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Introduction to machine learning on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform) · [Overview of models on Agent Platform](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/overview)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### AI-02 — Assess AI data use and retention

**Objective and applicability:** Assess AI data use and retention. All in-scope uses of ai and agent governance; document approved exclusions and service absence.

**Read-only evidence procedure:** Review model-specific data governance, prompt logging, grounding, caches, tuning data and retention settings against the actual contract and feature. Do not equate training restrictions with zero retention.

**Required workpapers:** feature and retention matrix; contracts; data approvals.

**Consultant assessment criterion:** Approved data handling addresses each enabled feature and provider, with documented exceptions.

**Try to disprove the conclusion:** A zero-retention assertion overlooks grounding, abuse-monitoring or optional logging behavior.

**Script title:** Assess AI data use and retention. **Description:** collect inventory supported vertex ai dataset metadata, inventory resource configuration, sample audit events within the approved window; create evidence requests and an unassessed review workpaper. [Open AI-02.py](../scripts/controls/AI-02.py).

**Operations:** `ai_datasets`, `assets`, `audit_logs` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Gemini Enterprise Agent Platform and zero data retention](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/data-governance) · [Gemini Enterprise Agent Platform and zero data retention](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/vertex-ai-zero-data-retention)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### AI-03 — Review AI endpoint and runtime access

**Objective and applicability:** Review AI endpoint and runtime access. All in-scope uses of ai and agent governance; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect endpoint networking, IAM, service identities, keys and data-store permissions. Reconcile who can deploy, invoke, tune or change the runtime.

**Required workpapers:** AI access review; endpoint architecture; runtime identity mapping.

**Consultant assessment criterion:** AI service privilege and exposure match the approved use and sensitive-data boundary.

**Try to disprove the conclusion:** An endpoint deployer can substitute a model that runs under a more privileged identity.

**Script title:** Review AI endpoint and runtime access. **Description:** collect list vertex ai endpoints, inventory resource allow policies, list service account identities; create evidence requests and an unassessed review workpaper. [Open AI-03.py](../scripts/controls/AI-03.py).

**Operations:** `ai_endpoints`, `asset_iam`, `service_accounts` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Agent Platform access control with IAM](https://docs.cloud.google.com/vertex-ai/docs/general/access-control) · [VPC Service Controls with Gemini Enterprise Agent Platform](https://docs.cloud.google.com/vertex-ai/docs/general/vpc-service-controls)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### AI-04 — Assess agent tools and retrieval boundaries

**Objective and applicability:** Assess agent tools and retrieval boundaries. All in-scope uses of ai and agent governance; document approved exclusions and service absence.

**Read-only evidence procedure:** Use application-supplied agent manifests, tool definitions, retrieval ACL design and existing evaluation traces. Review delegated identity and approval of consequential actions without invoking tools.

**Required workpapers:** agent tool inventory; retrieval ACL evidence; prior adversarial evaluations.

**Consultant assessment criterion:** Agents enforce user-specific data access and approved tool authority at execution time.

**Try to disprove the conclusion:** A prompt or retrieved document can cause a tool to access another user's data or perform an unapproved action.

**Script title:** Assess agent tools and retrieval boundaries. **Description:** collect inventory resource configuration, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open AI-04.py](../scripts/controls/AI-04.py).

**Operations:** `assets`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Scale your agents](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview) · [Model Armor overview](https://docs.cloud.google.com/model-armor/overview)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### AI-05 — Review AI evaluation and operational oversight

**Objective and applicability:** Review AI evaluation and operational oversight. All in-scope uses of ai and agent governance; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect model/version approvals, evaluation criteria, safety filters, monitoring, rollback and incident records. Sample completed evaluations for representative failure modes.

**Required workpapers:** evaluation reports; model approvals; AI incident records.

**Consultant assessment criterion:** The production use has approved quality, safety and security acceptance criteria plus monitored failure handling.

**Try to disprove the conclusion:** A model passes generic quality tests but fails the business's sensitive-data or tool-authorization scenarios.

**Script title:** Review AI evaluation and operational oversight. **Description:** collect list vertex ai model metadata, list vertex ai endpoints, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open AI-05.py](../scripts/controls/AI-05.py).

**Operations:** `ai_models`, `ai_endpoints`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Gen AI evaluation service overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview) · [Safety and content filters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-filters)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## OPS — Operational excellence and service health

Suggested accountable owner: **SRE and operations lead**.

### OPS-01 — Assess observability against service objectives

**Objective and applicability:** Assess observability against service objectives. All in-scope uses of operational excellence and service health; document approved exclusions and service absence.

**Read-only evidence procedure:** Join workload inventory to approved SLIs, SLOs, dashboards, alerts and escalation owners from monitoring exports. Review existing incidents and error budgets.

**Required workpapers:** SLO register; monitoring policy export; incident sample.

**Consultant assessment criterion:** Critical user journeys have measurable objectives and actionable monitoring.

**Try to disprove the conclusion:** An infrastructure dashboard is green while the business transaction is unavailable.

**Script title:** Assess observability against service objectives. **Description:** collect inventory resource configuration, list logs-based metrics; create evidence requests and an unassessed review workpaper. [Open OPS-01.py](../scripts/controls/OPS-01.py).

**Operations:** `assets`, `log_metrics` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Well-Architected Framework: Reliability pillar](https://docs.cloud.google.com/architecture/framework/reliability) · [Service monitoring](https://docs.cloud.google.com/monitoring/slo-monitoring)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### OPS-02 — Review quotas and capacity risk

**Objective and applicability:** Review quotas and capacity risk. All in-scope uses of operational excellence and service health; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect project quotas and obtain service-specific regional quota and utilization exports. Compare peak, growth and failover requirements to available headroom.

**Required workpapers:** quota register; utilization evidence; capacity plan.

**Consultant assessment criterion:** Approved capacity scenarios are covered by current quota and realistic resource availability.

**Try to disprove the conclusion:** A failover region has nominal architecture support but insufficient quota or capacity reservations.

**Script title:** Review quotas and capacity risk. **Description:** collect read compute project quotas and metadata, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open OPS-02.py](../scripts/controls/OPS-02.py).

**Operations:** `project_info`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview) · [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### OPS-03 — Assess maintenance and support lifecycle

**Objective and applicability:** Assess maintenance and support lifecycle. All in-scope uses of operational excellence and service health; document approved exclusions and service absence.

**Read-only evidence procedure:** Reconcile service versions, runtimes, release channels and dependencies to supported lifecycles. Review maintenance exclusions, support plans and upgrade ownership.

**Required workpapers:** support matrix; upgrade plan; provider notices.

**Consultant assessment criterion:** Unsupported or soon-retiring dependencies have an approved transition or exception.

**Try to disprove the conclusion:** A function runtime or GKE node pool remains unsupported despite a maintained application repository.

**Script title:** Assess maintenance and support lifecycle. **Description:** collect list gke cluster configuration, list cloud run functions, list cloud sql instance configuration, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open OPS-03.py](../scripts/controls/OPS-03.py).

**Operations:** `clusters`, `functions`, `sql`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [GKE release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule) · [Runtime support](https://docs.cloud.google.com/functions/docs/runtime-support)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### OPS-04 — Review operational change and access

**Objective and applicability:** Review operational change and access. All in-scope uses of operational excellence and service health; document approved exclusions and service absence.

**Read-only evidence procedure:** Trace sampled production changes to approvals, tests, deployment records and post-change verification. Include emergency changes and supplier access.

**Required workpapers:** change samples; emergency approvals; supplier access review.

**Consultant assessment criterion:** Changes have accountable authorization and sufficient validation for their risk.

**Try to disprove the conclusion:** A sensitive console change bypassed normal deployment approval without emergency review.

**Script title:** Review operational change and access. **Description:** collect sample audit events within the approved window, sample existing cloud build execution metadata, inventory resource allow policies; create evidence requests and an unassessed review workpaper. [Open OPS-04.py](../scripts/controls/OPS-04.py).

**Operations:** `audit_logs`, `builds`, `asset_iam` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Well-Architected Framework: Operational excellence pillar](https://docs.cloud.google.com/architecture/framework/operational-excellence/manage-change)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### OPS-05 — Assess service ownership and incident learning

**Objective and applicability:** Assess service ownership and incident learning. All in-scope uses of operational excellence and service health; document approved exclusions and service absence.

**Read-only evidence procedure:** Reconcile ownership labels and on-call records with real responders, dependency owners and postmortem actions.

**Required workpapers:** service catalog; on-call roster; postmortem actions.

**Consultant assessment criterion:** Critical services have current operational owners and improvements tied to recurring failure modes.

**Try to disprove the conclusion:** A labeled owner has left or a repeated failure has no tracked corrective action.

**Script title:** Assess service ownership and incident learning. **Description:** collect read project identity and lifecycle, inventory resource configuration, read security command center findings; create evidence requests and an unassessed review workpaper. [Open OPS-05.py](../scripts/controls/OPS-05.py).

**Operations:** `project`, `assets`, `scc` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Well-Architected Framework: Operational excellence pillar](https://docs.cloud.google.com/architecture/framework/operational-excellence/learn-from-failures) · [Create and update labels for projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## FIN — Cost governance and billing

Suggested accountable owner: **FinOps and finance leads**.

### FIN-01 — Reconcile billing and project accountability

**Objective and applicability:** Reconcile billing and project accountability. All in-scope uses of cost governance and billing; document approved exclusions and service absence.

**Read-only evidence procedure:** Read billing associations for approved projects and compare with finance-approved account and cost-center records. Billing account scope requires explicit independent approval.

**Required workpapers:** finance project register; billing account approvals; cost allocation.

**Consultant assessment criterion:** Every billed project has an accountable owner, cost center and approved billing association.

**Try to disprove the conclusion:** A project absent from the operations register still produces charges.

**Script title:** Reconcile billing and project accountability. **Description:** collect read project billing association, read project identity and lifecycle, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open FIN-01.py](../scripts/controls/FIN-01.py).

**Operations:** `billing_link`, `project`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Manage your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account) · [View projects linked to Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/how-to/view-linked)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### FIN-02 — Review budgets and spend control behavior

**Objective and applicability:** Review budgets and spend control behavior. All in-scope uses of cost governance and billing; document approved exclusions and service absence.

**Read-only evidence procedure:** Inspect budgets for explicitly approved accounts, filters, thresholds and recipients. Determine whether a budget is alerts-only or a supported spend-cap configuration and inspect actual handling.

**Required workpapers:** budget approvals; notification delivery; response records.

**Consultant assessment criterion:** Budget behavior and alert response match the adopted cost-control requirement; no generic assumption that every budget caps spending.

**Try to disprove the conclusion:** An alerts-only threshold is mistaken for an enforced stop, or notification reaches an unattended mailbox.

**Script title:** Review budgets and spend control behavior. **Description:** collect list explicitly approved billing budgets, read project billing association; create evidence requests and an unassessed review workpaper. [Open FIN-02.py](../scripts/controls/FIN-02.py).

**Operations:** `budgets`, `billing_link` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Create, edit, or delete budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### FIN-03 — Assess allocation and cost reporting

**Objective and applicability:** Assess allocation and cost reporting. All in-scope uses of cost governance and billing; document approved exclusions and service absence.

**Read-only evidence procedure:** Reconcile labels and tags to approved allocation rules and existing billing-export configuration. Request owner-supplied query results; do not submit BigQuery jobs from the collector.

**Required workpapers:** billing-export settings; allocation report; finance reconciliation.

**Consultant assessment criterion:** Material costs can be assigned and reconciled with finance at the agreed level.

**Try to disprove the conclusion:** Unlabeled shared infrastructure or credits distort the reported cost allocation.

**Script title:** Assess allocation and cost reporting. **Description:** collect inventory resource configuration, read project identity and lifecycle, read project billing association; create evidence requests and an unassessed review workpaper. [Open FIN-03.py](../scripts/controls/FIN-03.py).

**Operations:** `assets`, `project`, `billing_link` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) · [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### FIN-04 — Review optimization decisions and commitments

**Objective and applicability:** Review optimization decisions and commitments. All in-scope uses of cost governance and billing; document approved exclusions and service absence.

**Read-only evidence procedure:** Compare idle resource and utilization evidence with existing recommendations, commitments and business demand. Validate savings assumptions and contractual terms with finance.

**Required workpapers:** utilization report; recommendation export; commitment register.

**Consultant assessment criterion:** Optimization recommendations account for reliability, commitment coverage and real workload demand.

**Try to disprove the conclusion:** An idle-looking disaster recovery resource is proposed for removal without its recovery role.

**Script title:** Review optimization decisions and commitments. **Description:** collect list compute engine instance configuration, list persistent disk configuration, inventory resource configuration, read compute project quotas and metadata; create evidence requests and an unassessed review workpaper. [Open FIN-04.py](../scripts/controls/FIN-04.py).

**Operations:** `instances`, `disks`, `assets`, `project_info` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [What is Active Assist](https://docs.cloud.google.com/recommender/docs/overview) · [Optimize costs with Committed Use Discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### FIN-05 — Assess cost anomalies and abuse readiness

**Objective and applicability:** Assess cost anomalies and abuse readiness. All in-scope uses of cost governance and billing; document approved exclusions and service absence.

**Read-only evidence procedure:** Correlate spending anomalies, identity activity and public exposure with approved workloads. Review response authority and previous cost incidents.

**Required workpapers:** anomaly history; cost response procedure; incident sample.

**Consultant assessment criterion:** Unexpected spend has a defined detection and response path with accountable decisions.

**Try to disprove the conclusion:** A compromised workload can consume large resources before anyone acts on the cost alert.

**Script title:** Assess cost anomalies and abuse readiness. **Description:** collect list explicitly approved billing budgets, sample audit events within the approved window, read security command center findings; create evidence requests and an unassessed review workpaper. [Open FIN-05.py](../scripts/controls/FIN-05.py).

**Operations:** `budgets`, `audit_logs`, `scc` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [View and manage cost anomalies](https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

## COM — Compliance privacy and assurance

Suggested accountable owner: **Compliance and privacy leads**.

### COM-01 — Map obligations to system scope

**Objective and applicability:** Map obligations to system scope. All in-scope uses of compliance privacy and assurance; document approved exclusions and service absence.

**Read-only evidence procedure:** Identify applicable contracts, jurisdictional requirements and adopted frameworks with the organization. Map obligations to services, data, controls and evidence owners rather than assuming provider certification transfers.

**Required workpapers:** obligation register; scope decisions; control crosswalk.

**Consultant assessment criterion:** Every adopted requirement has an applicability decision and evidence mapping approved by the accountable team.

**Try to disprove the conclusion:** A provider attestation is offered as proof that customer IAM or retention configuration complies.

**Script title:** Map obligations to system scope. **Description:** collect list enabled service apis, inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open COM-01.py](../scripts/controls/COM-01.py).

**Operations:** `services`, `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [<!-- "> '> --><title>](https://docs.cloud.google.com/security/compliance/overview) · [Well-Architected Framework: Security, privacy, and compliance pillar](https://docs.cloud.google.com/architecture/framework/security)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### COM-02 — Assess classification and data discovery

**Objective and applicability:** Assess classification and data discovery. All in-scope uses of compliance privacy and assurance; document approved exclusions and service absence.

**Read-only evidence procedure:** Compare data classification and existing discovery/profile results with storage, databases, datasets and AI inventories. Inspect coverage, location, job recency and exclusions without initiating scans.

**Required workpapers:** classification register; discovery profile export; coverage reconciliation.

**Consultant assessment criterion:** Classification covers the material data population, with explicit unsupported or unscanned areas.

**Try to disprove the conclusion:** A current discovery dashboard excludes a new project, unstructured store or encrypted dataset.

**Script title:** Assess classification and data discovery. **Description:** collect inventory resource configuration, list cloud storage bucket metadata, inventory supported vertex ai dataset metadata; create evidence requests and an unassessed review workpaper. [Open COM-02.py](../scripts/controls/COM-02.py).

**Operations:** `assets`, `buckets`, `ai_datasets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Overview of sensitive data discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### COM-03 — Review privacy lifecycle and deletion evidence

**Objective and applicability:** Review privacy lifecycle and deletion evidence. All in-scope uses of compliance privacy and assurance; document approved exclusions and service absence.

**Read-only evidence procedure:** Trace selected data flows through collection, purpose, sharing, retention, deletion and backups using owner-provided records. Resolve legal hold and recovery obligations with the accountable team.

**Required workpapers:** data-flow map; deletion request samples; processor register.

**Consultant assessment criterion:** The adopted privacy requirements are supported across copies and processors; technical settings alone do not prove legal compliance.

**Try to disprove the conclusion:** A deleted primary record persists in extracts, logs or a downstream AI dataset without an approved retention basis.

**Script title:** Review privacy lifecycle and deletion evidence. **Description:** collect inventory resource configuration, list cloud storage bucket metadata, sample audit events within the approved window; create evidence requests and an unassessed review workpaper. [Open COM-03.py](../scripts/controls/COM-03.py).

**Operations:** `assets`, `buckets`, `audit_logs` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [GDPR and Google Cloud](https://docs.cloud.google.com/security/compliance/gdpr) · [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### COM-04 — Assess regulated workload controls

**Objective and applicability:** Assess regulated workload controls. All in-scope uses of compliance privacy and assurance; document approved exclusions and service absence.

**Read-only evidence procedure:** Identify Assured Workloads, access approvals, transparency logs, regional restrictions and contractual support commitments where applicable. Inspect actual control package and exceptions.

**Required workpapers:** control-package export; contracts; access approval records.

**Consultant assessment criterion:** Claims about sovereign or regulated operation match deployed controls, service eligibility and contract terms.

**Try to disprove the conclusion:** A project label claims a regulated package while the workload or service is outside its supported boundary.

**Script title:** Assess regulated workload controls. **Description:** collect inventory resource configuration, read a selected effective organization policy, sample audit events within the approved window; create evidence requests and an unassessed review workpaper. [Open COM-04.py](../scripts/controls/COM-04.py).

**Operations:** `assets`, `effective_policy`, `audit_logs` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Overview of Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview) · [Overview of Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview) · [Overview of Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.

### COM-05 — Review audit evidence and assurance closure

**Objective and applicability:** Review audit evidence and assurance closure. All in-scope uses of compliance privacy and assurance; document approved exclusions and service absence.

**Read-only evidence procedure:** Check findings against criteria, affected population, reproducible evidence and contrary explanations. Require owners, agreed actions, due dates, risk acceptance and independent retest before closure.

**Required workpapers:** finding register; quality review; management responses; closure evidence.

**Consultant assessment criterion:** The report distinguishes observed facts, inference, limitations and management decisions; no unsupported compliance claim remains.

**Try to disprove the conclusion:** A high-severity finding relies on truncated data or is marked closed after a change ticket without retest evidence.

**Script title:** Review audit evidence and assurance closure. **Description:** collect inventory resource configuration; create evidence requests and an unassessed review workpaper. [Open COM-05.py](../scripts/controls/COM-05.py).

**Operations:** `assets` — exact commands, permissions and sources in the [operation register](../docs/SCRIPT-OPERATIONS.md).

**Google documentation:** [Well-Architected Framework: Security, privacy, and compliance pillar](https://docs.cloud.google.com/architecture/framework/security) · [SP 800-53A Rev. 5, Assessing Security and Privacy Controls in Information Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final)

**Response if the criterion fails:** Agree a change with the service owner against the failed criterion, assess dependencies and rollback, implement through change control, then obtain independent retest evidence. Collection scripts do not remediate.

**Reassessment:** At initial engagement and material change; recurring interval follows the approved risk plan.
