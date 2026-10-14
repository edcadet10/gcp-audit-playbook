# Documented read operations

The code register is [operations.py](../scripts/operations.py). Each entry is a fixed command path; scope values cannot supply command strings. Permissions below are the focal read permissions, not a guarantee that they alone satisfy all ancestor, service usage or supporting calls. Confirm least privilege during the pilot using [Google's IAM role reference](https://docs.cloud.google.com/iam/docs/understanding-roles) and [Cloud Asset Inventory permissions](https://docs.cloud.google.com/asset-inventory/docs/roles-permissions). Never grant Owner or Editor to make a collector work.

No output file flags, cloud exports to buckets, data queries, secret payload reads, API enablement, role changes or remediations are dispatched. Binary Authorization `policy export` is a documented semantic read to stdout. gcloud handles server pagination for uncapped list operations; inventory consistency and visibility still require reconciliation.

## assets — Inventory resource configuration

Collect supported resource metadata. Reconcile unsupported types, indexing delay and service-native inventories; this is not an authoritative census by itself.

- **Command:** `gcloud asset list --content-type=resource`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `cloudasset.assets.listResource`.
- **Documentation:** [gcloud asset list](https://docs.cloud.google.com/sdk/gcloud/reference/asset/list)

## asset_iam — Inventory resource allow policies

Search allow-policy bindings in the selected project. Does not resolve group membership, ancestor inheritance, deny policies, principal access boundaries or all data-plane ACLs.

- **Command:** `gcloud asset search-all-iam-policies`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `cloudasset.assets.searchAllIamPolicies`.
- **Documentation:** [gcloud asset search-all-iam-policies](https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies)

## org_assets — Reconcile organization project inventory

Reconcile organization project inventory; returns configuration metadata for auditor review.

- **Command:** `gcloud asset list --content-type=resource --asset-types=cloudresourcemanager.googleapis.com/Project,cloudresourcemanager.googleapis.com/Folder`
- **Scope expansion:** `organization`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `cloudasset.assets.listResource`.
- **Documentation:** [gcloud asset list](https://docs.cloud.google.com/sdk/gcloud/reference/asset/list)

## org_iam — Read organization IAM and audit configuration

Read organization IAM and audit configuration; returns configuration metadata for auditor review.

- **Command:** `gcloud organizations get-iam-policy`
- **Scope expansion:** `organization`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `resourcemanager.organizations.getIamPolicy`.
- **Documentation:** [gcloud organizations get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/get-iam-policy)

## folder_iam — Read ancestor folder IAM and audit configuration

Read ancestor folder IAM and audit configuration; returns configuration metadata for auditor review.

- **Command:** `gcloud resource-manager folders get-iam-policy`
- **Scope expansion:** `folder`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `resourcemanager.folders.getIamPolicy`.
- **Documentation:** [gcloud resource-manager folders get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/folders/get-iam-policy)

## project_iam — Read project IAM and audit configuration

Read project IAM and audit configuration; returns configuration metadata for auditor review.

- **Command:** `gcloud projects get-iam-policy`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `resourcemanager.projects.getIamPolicy`.
- **Documentation:** [gcloud projects get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy)

## project — Read project identity and lifecycle

Read project identity and lifecycle; returns configuration metadata for auditor review.

- **Command:** `gcloud projects describe`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `resourcemanager.projects.get`.
- **Documentation:** [gcloud projects describe](https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe)

## services — List enabled service APIs

List enabled service APIs; returns configuration metadata for auditor review.

- **Command:** `gcloud services list --enabled`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `serviceusage.services.list`.
- **Documentation:** [gcloud services list](https://docs.cloud.google.com/sdk/gcloud/reference/services/list)

## org_policies — List project organization-policy overrides

Lists explicit project policies. Effective inheritance is reviewed separately using the effective_policy operation; an empty list is not unrestricted or compliant by itself.

- **Command:** `gcloud org-policies list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `orgpolicy.policies.list`.
- **Documentation:** [gcloud org-policies list](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list)

## effective_policy — Read a selected effective organization policy

Read a selected effective organization policy; returns configuration metadata for auditor review.

- **Command:** `gcloud org-policies describe --effective`
- **Scope expansion:** `constraint`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `orgpolicy.policies.get`.
- **Documentation:** [gcloud org-policies describe](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/describe)

## org_roles — List organization custom roles

List organization custom roles; returns configuration metadata for auditor review.

- **Command:** `gcloud iam roles list`
- **Scope expansion:** `organization`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `iam.roles.list`.
- **Documentation:** [gcloud iam roles list](https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/list)

## project_roles — List project custom roles

List project custom roles; returns configuration metadata for auditor review.

- **Command:** `gcloud iam roles list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `iam.roles.list`.
- **Documentation:** [gcloud iam roles list](https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/list)

## service_accounts — List service account identities

List service account identities; returns configuration metadata for auditor review.

- **Command:** `gcloud iam service-accounts list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `iam.serviceAccounts.list`.
- **Documentation:** [gcloud iam service-accounts list](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/list)

## sa_keys — List service account key metadata

List user-managed key IDs, validity and status; never download key material. Google-managed keys are deliberately excluded.

- **Command:** `gcloud iam service-accounts keys list --managed-by=user`
- **Scope expansion:** `service_account`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `iam.serviceAccountKeys.list`.
- **Documentation:** [gcloud iam service-accounts keys list](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list)

## wif_pools — List workload identity pools

List workload identity pools; returns configuration metadata for auditor review.

- **Command:** `gcloud iam workload-identity-pools list --location=global`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `iam.workloadIdentityPools.list`.
- **Documentation:** [gcloud iam workload-identity-pools list](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/list)

## wif_providers — Read workload federation providers

Read workload federation providers; returns configuration metadata for auditor review.

- **Command:** `gcloud iam workload-identity-pools providers list --location=global`
- **Scope expansion:** `pool`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `iam.workloadIdentityPoolProviders.list`.
- **Documentation:** [gcloud iam workload-identity-pools providers list](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/list)

## networks — List VPC networks and peerings

List VPC networks and peerings; returns configuration metadata for auditor review.

- **Command:** `gcloud compute networks list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `compute.networks.list`.
- **Documentation:** [gcloud compute networks list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/list)

## subnets — List subnets and private access settings

List subnets and private access settings; returns configuration metadata for auditor review.

- **Command:** `gcloud compute networks subnets list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `compute.subnetworks.list`.
- **Documentation:** [gcloud compute networks subnets list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list)

## firewalls — List VPC firewall rules

Collect VPC rules including disabled state, logging, priority and targets. Does not calculate effective hierarchical or network firewall policies.

- **Command:** `gcloud compute firewall-rules list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `compute.firewalls.list`.
- **Documentation:** [gcloud compute firewall-rules list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/list)

## firewall_policies — List organization firewall policies

List organization firewall policies; returns configuration metadata for auditor review.

- **Command:** `gcloud compute firewall-policies list`
- **Scope expansion:** `organization`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `compute.firewallPolicies.list`.
- **Documentation:** [gcloud compute firewall-policies list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/list)

## routes — List VPC routes

List VPC routes; returns configuration metadata for auditor review.

- **Command:** `gcloud compute routes list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `compute.routes.list`.
- **Documentation:** [gcloud compute routes list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes/list)

## routers — List Cloud Routers and NAT configuration

List Cloud Routers and NAT configuration; returns configuration metadata for auditor review.

- **Command:** `gcloud compute routers list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `compute.routers.list`.
- **Documentation:** [gcloud compute routers list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/list)

## forwarding — List forwarding rules

List forwarding rules; returns configuration metadata for auditor review.

- **Command:** `gcloud compute forwarding-rules list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `compute.forwardingRules.list`.
- **Documentation:** [gcloud compute forwarding-rules list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/list)

## backend — List load balancer backend services

List load balancer backend services; returns configuration metadata for auditor review.

- **Command:** `gcloud compute backend-services list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `compute.backendServices.list`.
- **Documentation:** [gcloud compute backend-services list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/list)

## armor — List Cloud Armor policies

List Cloud Armor policies; returns configuration metadata for auditor review.

- **Command:** `gcloud compute security-policies list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `compute.securityPolicies.list`.
- **Documentation:** [gcloud compute security-policies list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/list)

## dns — List Cloud DNS managed zones

List Cloud DNS managed zones; returns configuration metadata for auditor review.

- **Command:** `gcloud dns managed-zones list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `dns.managedZones.list`.
- **Documentation:** [gcloud dns managed-zones list](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/list)

## vpn — List VPN tunnel configuration

List VPN tunnel configuration; returns configuration metadata for auditor review.

- **Command:** `gcloud compute vpn-tunnels list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `compute.vpnTunnels.list`.
- **Documentation:** [gcloud compute vpn-tunnels list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/list)

## interconnect — List Interconnect attachments

List Interconnect attachments; returns configuration metadata for auditor review.

- **Command:** `gcloud compute interconnects attachments list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `compute.interconnectAttachments.list`.
- **Documentation:** [gcloud compute interconnects attachments list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/list)

## access_policies — List Access Context Manager policies

List Access Context Manager policies; returns configuration metadata for auditor review.

- **Command:** `gcloud access-context-manager policies list`
- **Scope expansion:** `organization`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `accesscontextmanager.policies.list`.
- **Documentation:** [gcloud access-context-manager policies list](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/list)

## perimeters — List VPC Service Controls perimeters

List VPC Service Controls perimeters; returns configuration metadata for auditor review.

- **Command:** `gcloud access-context-manager perimeters list`
- **Scope expansion:** `access_policy`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `accesscontextmanager.servicePerimeters.list`.
- **Documentation:** [gcloud access-context-manager perimeters list](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/list)

## instances — List Compute Engine instance configuration

List Compute Engine instance configuration; returns configuration metadata for auditor review.

- **Command:** `gcloud compute instances list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `compute.instances.list`.
- **Documentation:** [gcloud compute instances list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list)

## disks — List persistent disk configuration

List persistent disk configuration; returns configuration metadata for auditor review.

- **Command:** `gcloud compute disks list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `compute.disks.list`.
- **Documentation:** [gcloud compute disks list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/list)

## images — List project-owned VM images

List project-owned VM images; returns configuration metadata for auditor review.

- **Command:** `gcloud compute images list --no-standard-images`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `compute.images.list`.
- **Documentation:** [gcloud compute images list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/list)

## snapshots — List disk snapshot metadata

List disk snapshot metadata; returns configuration metadata for auditor review.

- **Command:** `gcloud compute snapshots list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `compute.snapshots.list`.
- **Documentation:** [gcloud compute snapshots list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/list)

## schedules — List regional resource policies

List regional resource policies; returns configuration metadata for auditor review.

- **Command:** `gcloud compute resource-policies list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `compute.resourcePolicies.list`.
- **Documentation:** [gcloud compute resource-policies list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/list)

## clusters — List GKE cluster configuration

Collect control-plane, networking, node and workload identity configuration. Does not inspect live Kubernetes RBAC, workloads, admission results or network-policy enforcement.

- **Command:** `gcloud container clusters list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `container.clusters.list`.
- **Documentation:** [gcloud container clusters list](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/list)

## run_services — List Cloud Run services

List Cloud Run services; returns configuration metadata for auditor review.

- **Command:** `gcloud run services list`
- **Scope expansion:** `region`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `run.services.list`.
- **Documentation:** [gcloud run services list](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/list)

## run_jobs — List Cloud Run jobs

List Cloud Run jobs; returns configuration metadata for auditor review.

- **Command:** `gcloud run jobs list`
- **Scope expansion:** `region`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `run.jobs.list`.
- **Documentation:** [gcloud run jobs list](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/list)

## functions — List Cloud Run functions

List Cloud Run functions; returns configuration metadata for auditor review.

- **Command:** `gcloud functions list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `cloudfunctions.functions.list`.
- **Documentation:** [gcloud functions list](https://docs.cloud.google.com/sdk/gcloud/reference/functions/list)

## scheduler — List Cloud Scheduler jobs

List Cloud Scheduler jobs; returns configuration metadata for auditor review.

- **Command:** `gcloud scheduler jobs list`
- **Scope expansion:** `location`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `cloudscheduler.jobs.list`.
- **Documentation:** [gcloud scheduler jobs list](https://docs.cloud.google.com/sdk/gcloud/reference/scheduler/jobs/list)

## pubsub_topics — List Pub/Sub topic configuration

List Pub/Sub topic configuration; returns configuration metadata for auditor review.

- **Command:** `gcloud pubsub topics list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `pubsub.topics.list`.
- **Documentation:** [gcloud pubsub topics list](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/list)

## pubsub_subs — List Pub/Sub subscription configuration

List Pub/Sub subscription configuration; returns configuration metadata for auditor review.

- **Command:** `gcloud pubsub subscriptions list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `pubsub.subscriptions.list`.
- **Documentation:** [gcloud pubsub subscriptions list](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/list)

## buckets — List Cloud Storage bucket metadata

Collect bucket controls; never list or read object contents. Object ACL evidence is a separate customer-provided metadata workpaper when uniform access is disabled.

- **Command:** `gcloud storage buckets list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `storage.buckets.list`.
- **Documentation:** [gcloud storage buckets list](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/list)

## sql — List Cloud SQL instance configuration

List Cloud SQL instance configuration; returns configuration metadata for auditor review.

- **Command:** `gcloud sql instances list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `cloudsql.instances.list`.
- **Documentation:** [gcloud sql instances list](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/list)

## sql_backups — List existing Cloud SQL backup records

List existing Cloud SQL backup records; returns configuration metadata for auditor review.

- **Command:** `gcloud sql backups list`
- **Scope expansion:** `sql_instance`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `cloudsql.backupRuns.list`.
- **Documentation:** [gcloud sql backups list](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list)

## spanner — List Spanner instances

List Spanner instances; returns configuration metadata for auditor review.

- **Command:** `gcloud spanner instances list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `spanner.instances.list`.
- **Documentation:** [gcloud spanner instances list](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instances/list)

## redis — List Memorystore Redis instances

List Memorystore Redis instances; returns configuration metadata for auditor review.

- **Command:** `gcloud redis instances list`
- **Scope expansion:** `region`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `redis.instances.list`.
- **Documentation:** [gcloud redis instances list](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/list)

## secrets — List Secret Manager metadata

Read secret configuration only. Secret payload access is not permitted by this collector.

- **Command:** `gcloud secrets list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `secretmanager.secrets.list`.
- **Documentation:** [gcloud secrets list](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/list)

## secret_versions — List secret version metadata

List secret version metadata; returns configuration metadata for auditor review.

- **Command:** `gcloud secrets versions list`
- **Scope expansion:** `secret`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `secretmanager.versions.list`.
- **Documentation:** [gcloud secrets versions list](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/versions/list)

## keyrings — List Cloud KMS key rings

List Cloud KMS key rings; returns configuration metadata for auditor review.

- **Command:** `gcloud kms keyrings list`
- **Scope expansion:** `location`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `cloudkms.keyRings.list`.
- **Documentation:** [gcloud kms keyrings list](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keyrings/list)

## keys — List cryptographic key configuration

List cryptographic key configuration; returns configuration metadata for auditor review.

- **Command:** `gcloud kms keys list`
- **Scope expansion:** `keyring`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `cloudkms.cryptoKeys.list`.
- **Documentation:** [gcloud kms keys list](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/list)

## sinks — Read project logging sinks

Read project logging sinks; returns configuration metadata for auditor review.

- **Command:** `gcloud logging sinks list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `logging.sinks.list`.
- **Documentation:** [gcloud logging sinks list](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/list)

## org_sinks — Read organization aggregated logging sinks

Read organization aggregated logging sinks; returns configuration metadata for auditor review.

- **Command:** `gcloud logging sinks list`
- **Scope expansion:** `organization`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `logging.sinks.list`.
- **Documentation:** [gcloud logging sinks list](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/list)

## exclusions — Read sink exclusion filters

Read exclusions embedded in sink configuration, including the _Default sink. The GA CLI does not expose a logging exclusions list command.

- **Command:** `gcloud logging sinks list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `logging.sinks.list`.
- **Documentation:** [gcloud logging sinks list](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/list)

## log_buckets — Read regional log bucket retention

Read regional log bucket retention; returns configuration metadata for auditor review.

- **Command:** `gcloud logging buckets list`
- **Scope expansion:** `location`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `logging.buckets.list`.
- **Documentation:** [gcloud logging buckets list](https://docs.cloud.google.com/sdk/gcloud/reference/logging/buckets/list)

## log_metrics — List logs-based metrics

List logs-based metrics; returns configuration metadata for auditor review.

- **Command:** `gcloud logging metrics list`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `logging.logMetrics.list`.
- **Documentation:** [gcloud logging metrics list](https://docs.cloud.google.com/sdk/gcloud/reference/logging/metrics/list)

## audit_logs — Sample audit events within the approved window

Bounded metadata and payload sample of audit events in an explicit UTC window. Always classified Sampled, or Truncated at the limit; never proof of full event coverage. Logs can contain sensitive values.

- **Command:** `gcloud logging read`
- **Scope expansion:** `logs`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `logging.logEntries.list; logging.privateLogEntries.list for Data Access`.
- **Documentation:** [gcloud logging read](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read)

## scc — Read Security Command Center findings

Read findings for the selected organization and SCC location. Availability depends on activation, location, tier and permissions; an empty response is not a clean bill of health.

- **Command:** `gcloud scc findings list`
- **Scope expansion:** `scc`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `securitycenter.findings.list`.
- **Documentation:** [gcloud scc findings list](https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list)

## repositories — List Artifact Registry repositories

List Artifact Registry repositories; returns configuration metadata for auditor review.

- **Command:** `gcloud artifacts repositories list`
- **Scope expansion:** `location`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `artifactregistry.repositories.list`.
- **Documentation:** [gcloud artifacts repositories list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/list)

## build_triggers — Read Cloud Build triggers

Read Cloud Build triggers; returns configuration metadata for auditor review.

- **Command:** `gcloud builds triggers list`
- **Scope expansion:** `region`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `cloudbuild.builds.list`.
- **Documentation:** [gcloud builds triggers list](https://docs.cloud.google.com/sdk/gcloud/reference/builds/triggers/list)

## builds — Sample existing Cloud Build execution metadata

Bounded sample of the most recent 100 builds; statuses and provenance links require review. Reaching 100 is marked Truncated; fewer is still Sampled.

- **Command:** `gcloud builds list --limit=100`
- **Scope expansion:** `region`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `cloudbuild.builds.list`.
- **Documentation:** [gcloud builds list](https://docs.cloud.google.com/sdk/gcloud/reference/builds/list)

## deploy — Read Cloud Deploy delivery pipelines

Read Cloud Deploy delivery pipelines; returns configuration metadata for auditor review.

- **Command:** `gcloud deploy delivery-pipelines list`
- **Scope expansion:** `region`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `clouddeploy.deliveryPipelines.list`.
- **Documentation:** [gcloud deploy delivery-pipelines list](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/delivery-pipelines/list)

## binary — Read Binary Authorization admission policy

Despite the verb export, this returns the existing policy to stdout; no --destination or cloud write is used.

- **Command:** `gcloud container binauthz policy export`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `binaryauthorization.policy.get`.
- **Documentation:** [gcloud container binauthz policy export](https://docs.cloud.google.com/sdk/gcloud/reference/container/binauthz/policy/export)

## ai_endpoints — List Vertex AI endpoints

List Vertex AI endpoints; returns configuration metadata for auditor review.

- **Command:** `gcloud ai endpoints list`
- **Scope expansion:** `region`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `aiplatform.endpoints.list`.
- **Documentation:** [gcloud ai endpoints list](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/list)

## ai_models — List Vertex AI model metadata

List Vertex AI model metadata; returns configuration metadata for auditor review.

- **Command:** `gcloud ai models list`
- **Scope expansion:** `region`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `aiplatform.models.list`.
- **Documentation:** [gcloud ai models list](https://docs.cloud.google.com/sdk/gcloud/reference/ai/models/list)

## ai_datasets — Inventory supported Vertex AI dataset metadata

Use Cloud Asset Inventory for supported Vertex AI dataset resources; reconcile with owner-provided native dataset exports and unsupported generative data stores.

- **Command:** `gcloud asset list --content-type=resource --asset-types=aiplatform.googleapis.com/Dataset`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `cloudasset.assets.listResource`.
- **Documentation:** [gcloud asset list](https://docs.cloud.google.com/sdk/gcloud/reference/asset/list)

## billing_link — Read project billing association

Read project billing association; returns configuration metadata for auditor review.

- **Command:** `gcloud billing projects describe`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `billing.resourceAssociations.list / resourcemanager.projects.get as applicable`.
- **Documentation:** [gcloud billing projects describe](https://docs.cloud.google.com/sdk/gcloud/reference/billing/projects/describe)

## budgets — List explicitly approved billing budgets

Billing accounts are separate authorization scopes, not proven by project ancestry. Only explicitly approved billing account IDs are read.

- **Command:** `gcloud billing budgets list`
- **Scope expansion:** `billing`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `billing.budgets.list`.
- **Documentation:** [gcloud billing budgets list](https://docs.cloud.google.com/sdk/gcloud/reference/billing/budgets/list)

## project_info — Read Compute project quotas and metadata

Read Compute project quotas and metadata; returns configuration metadata for auditor review.

- **Command:** `gcloud compute project-info describe`
- **Scope expansion:** `project`; see [scope and fan-out rules](COLLECTION-GUIDE.md).
- **Focal permissions:** `compute.projects.get`.
- **Documentation:** [gcloud compute project-info describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/describe)
