"""Title: Google Cloud read-operation register.
Description: Fixed command paths, scopes, and permissions used by the collector.
Reference: https://docs.cloud.google.com/sdk/gcloud/reference
No scope file can supply a command, flag, URL, or log expression.
"""

OPERATIONS = {}

def add(key, title, command, scope="project", flags=(), permission="", note=""):
    path = command.split()
    OPERATIONS[key] = dict(id=key, title=title, command=path, scope=scope,
        flags=list(flags), permission=permission,
        source="https://docs.cloud.google.com/sdk/gcloud/reference/" + "/".join(path),
        description=note or title + "; returns configuration metadata for auditor review.")

add("assets", "Inventory resource configuration", "asset list", flags=["--content-type=resource"], permission="cloudasset.assets.listResource", note="Collect supported resource metadata. Reconcile unsupported types, indexing delay and service-native inventories; this is not an authoritative census by itself.")
add("asset_iam", "Inventory resource allow policies", "asset search-all-iam-policies", permission="cloudasset.assets.searchAllIamPolicies", note="Search allow-policy bindings in the selected project. Does not resolve group membership, ancestor inheritance, deny policies, principal access boundaries or all data-plane ACLs.")
add("org_assets", "Reconcile organization project inventory", "asset list", "organization", ["--content-type=resource", "--asset-types=cloudresourcemanager.googleapis.com/Project,cloudresourcemanager.googleapis.com/Folder"], "cloudasset.assets.listResource")
add("org_iam", "Read organization IAM and audit configuration", "organizations get-iam-policy", "organization", permission="resourcemanager.organizations.getIamPolicy")
add("folder_iam", "Read ancestor folder IAM and audit configuration", "resource-manager folders get-iam-policy", "folder", permission="resourcemanager.folders.getIamPolicy")
add("project_iam", "Read project IAM and audit configuration", "projects get-iam-policy", permission="resourcemanager.projects.getIamPolicy")
add("project", "Read project identity and lifecycle", "projects describe", permission="resourcemanager.projects.get")
add("services", "List enabled service APIs", "services list", flags=["--enabled"], permission="serviceusage.services.list")
add("org_policies", "List project organization-policy overrides", "org-policies list", permission="orgpolicy.policies.list", note="Lists explicit project policies. Effective inheritance is reviewed separately using the effective_policy operation; an empty list is not unrestricted or compliant by itself.")
add("effective_policy", "Read a selected effective organization policy", "org-policies describe", "constraint", ["--effective"], "orgpolicy.policies.get")
add("org_roles", "List organization custom roles", "iam roles list", "organization", permission="iam.roles.list")
add("project_roles", "List project custom roles", "iam roles list", permission="iam.roles.list")
add("service_accounts", "List service account identities", "iam service-accounts list", permission="iam.serviceAccounts.list")
add("sa_keys", "List service account key metadata", "iam service-accounts keys list", "service_account", ["--managed-by=user"], "iam.serviceAccountKeys.list", "List user-managed key IDs, validity and status; never download key material. Google-managed keys are deliberately excluded.")
add("wif_pools", "List workload identity pools", "iam workload-identity-pools list", flags=["--location=global"], permission="iam.workloadIdentityPools.list")
add("wif_providers", "Read workload federation providers", "iam workload-identity-pools providers list", "pool", ["--location=global"], "iam.workloadIdentityPoolProviders.list")
add("networks", "List VPC networks and peerings", "compute networks list", permission="compute.networks.list")
add("subnets", "List subnets and private access settings", "compute networks subnets list", permission="compute.subnetworks.list")
add("firewalls", "List VPC firewall rules", "compute firewall-rules list", permission="compute.firewalls.list", note="Collect VPC rules including disabled state, logging, priority and targets. Does not calculate effective hierarchical or network firewall policies.")
add("firewall_policies", "List organization firewall policies", "compute firewall-policies list", "organization", permission="compute.firewallPolicies.list")
add("routes", "List VPC routes", "compute routes list", permission="compute.routes.list")
add("routers", "List Cloud Routers and NAT configuration", "compute routers list", permission="compute.routers.list")
add("forwarding", "List forwarding rules", "compute forwarding-rules list", permission="compute.forwardingRules.list")
add("backend", "List load balancer backend services", "compute backend-services list", permission="compute.backendServices.list")
add("armor", "List Cloud Armor policies", "compute security-policies list", permission="compute.securityPolicies.list")
add("dns", "List Cloud DNS managed zones", "dns managed-zones list", permission="dns.managedZones.list")
add("vpn", "List VPN tunnel configuration", "compute vpn-tunnels list", permission="compute.vpnTunnels.list")
add("interconnect", "List Interconnect attachments", "compute interconnects attachments list", permission="compute.interconnectAttachments.list")
add("access_policies", "List Access Context Manager policies", "access-context-manager policies list", "organization", permission="accesscontextmanager.policies.list")
add("perimeters", "List VPC Service Controls perimeters", "access-context-manager perimeters list", "access_policy", permission="accesscontextmanager.servicePerimeters.list")
add("instances", "List Compute Engine instance configuration", "compute instances list", permission="compute.instances.list")
add("disks", "List persistent disk configuration", "compute disks list", permission="compute.disks.list")
add("images", "List project-owned VM images", "compute images list", flags=["--no-standard-images"], permission="compute.images.list")
add("snapshots", "List disk snapshot metadata", "compute snapshots list", permission="compute.snapshots.list")
add("schedules", "List regional resource policies", "compute resource-policies list", permission="compute.resourcePolicies.list")
add("clusters", "List GKE cluster configuration", "container clusters list", permission="container.clusters.list", note="Collect control-plane, networking, node and workload identity configuration. Does not inspect live Kubernetes RBAC, workloads, admission results or network-policy enforcement.")
add("run_services", "List Cloud Run services", "run services list", "region", permission="run.services.list")
add("run_jobs", "List Cloud Run jobs", "run jobs list", "region", permission="run.jobs.list")
add("functions", "List Cloud Run functions", "functions list", permission="cloudfunctions.functions.list")
add("scheduler", "List Cloud Scheduler jobs", "scheduler jobs list", "location", permission="cloudscheduler.jobs.list")
add("pubsub_topics", "List Pub/Sub topic configuration", "pubsub topics list", permission="pubsub.topics.list")
add("pubsub_subs", "List Pub/Sub subscription configuration", "pubsub subscriptions list", permission="pubsub.subscriptions.list")
add("buckets", "List Cloud Storage bucket metadata", "storage buckets list", permission="storage.buckets.list", note="Collect bucket controls; never list or read object contents. Object ACL evidence is a separate customer-provided metadata workpaper when uniform access is disabled.")
add("sql", "List Cloud SQL instance configuration", "sql instances list", permission="cloudsql.instances.list")
add("sql_backups", "List existing Cloud SQL backup records", "sql backups list", "sql_instance", permission="cloudsql.backupRuns.list")
add("spanner", "List Spanner instances", "spanner instances list", permission="spanner.instances.list")
add("redis", "List Memorystore Redis instances", "redis instances list", "region", permission="redis.instances.list")
add("secrets", "List Secret Manager metadata", "secrets list", permission="secretmanager.secrets.list", note="Read secret configuration only. Secret payload access is not permitted by this collector.")
add("secret_versions", "List secret version metadata", "secrets versions list", "secret", permission="secretmanager.versions.list")
add("keyrings", "List Cloud KMS key rings", "kms keyrings list", "location", permission="cloudkms.keyRings.list")
add("keys", "List cryptographic key configuration", "kms keys list", "keyring", permission="cloudkms.cryptoKeys.list")
add("sinks", "Read project logging sinks", "logging sinks list", permission="logging.sinks.list")
add("org_sinks", "Read organization aggregated logging sinks", "logging sinks list", "organization", permission="logging.sinks.list")
add("exclusions", "Read sink exclusion filters", "logging sinks list", permission="logging.sinks.list", note="Read exclusions embedded in sink configuration, including the _Default sink. The GA CLI does not expose a logging exclusions list command.")
add("log_buckets", "Read regional log bucket retention", "logging buckets list", "location", permission="logging.buckets.list")
add("log_metrics", "List logs-based metrics", "logging metrics list", permission="logging.logMetrics.list")
add("audit_logs", "Sample audit events within the approved window", "logging read", "logs", permission="logging.logEntries.list; logging.privateLogEntries.list for Data Access", note="Bounded metadata and payload sample of audit events in an explicit UTC window. Always classified Sampled, or Truncated at the limit; never proof of full event coverage. Logs can contain sensitive values.")
add("scc", "Read Security Command Center findings", "scc findings list", "scc", permission="securitycenter.findings.list", note="Read findings for the selected organization and SCC location. Availability depends on activation, location, tier and permissions; an empty response is not a clean bill of health.")
add("repositories", "List Artifact Registry repositories", "artifacts repositories list", "location", permission="artifactregistry.repositories.list")
add("build_triggers", "Read Cloud Build triggers", "builds triggers list", "region", permission="cloudbuild.builds.list")
add("builds", "Sample existing Cloud Build execution metadata", "builds list", "region", ["--limit=100"], "cloudbuild.builds.list", "Bounded sample of the most recent 100 builds; statuses and provenance links require review. Reaching 100 is marked Truncated; fewer is still Sampled.")
add("deploy", "Read Cloud Deploy delivery pipelines", "deploy delivery-pipelines list", "region", permission="clouddeploy.deliveryPipelines.list")
add("binary", "Read Binary Authorization admission policy", "container binauthz policy export", permission="binaryauthorization.policy.get", note="Despite the verb export, this returns the existing policy to stdout; no --destination or cloud write is used.")
add("ai_endpoints", "List Vertex AI endpoints", "ai endpoints list", "region", permission="aiplatform.endpoints.list")
add("ai_models", "List Vertex AI model metadata", "ai models list", "region", permission="aiplatform.models.list")
add("ai_datasets", "Inventory supported Vertex AI dataset metadata", "asset list", flags=["--content-type=resource", "--asset-types=aiplatform.googleapis.com/Dataset"], permission="cloudasset.assets.listResource", note="Use Cloud Asset Inventory for supported Vertex AI dataset resources; reconcile with owner-provided native dataset exports and unsupported generative data stores.")
add("billing_link", "Read project billing association", "billing projects describe", permission="billing.resourceAssociations.list / resourcemanager.projects.get as applicable")
add("budgets", "List explicitly approved billing budgets", "billing budgets list", "billing", permission="billing.budgets.list", note="Billing accounts are separate authorization scopes, not proven by project ancestry. Only explicitly approved billing account IDs are read.")
add("project_info", "Read Compute project quotas and metadata", "compute project-info describe", permission="compute.projects.get")

# Explicitly audited semantic exception: export of an existing policy is a read.
READ_VERBS = {"list", "describe", "get-iam-policy", "search-all-iam-policies", "read"}
READ_EXCEPTIONS = {("container", "binauthz", "policy", "export")}
