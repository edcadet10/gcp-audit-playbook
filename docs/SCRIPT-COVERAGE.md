# Script coverage

Every control, fieldwork step and engagement phase has one executable entry point. All share the same setup, authentication, scope verification and read dispatcher. **A mapped script does not replace interviews, directory evidence, data-plane ACL exports, prior exercises or an auditor's conclusion.**

| Procedure | Title and purpose | Script | Evidence operations |
|---|---|---|---|
| GOV-01 | Establish organizational ownership and scope | [GOV-01.py](../scripts/controls/GOV-01.py) | org_assets, project, billing_link |
| GOV-02 | Allocate shared responsibility | [GOV-02.py](../scripts/controls/GOV-02.py) | services, assets |
| GOV-03 | Assess landing-zone design | [GOV-03.py](../scripts/controls/GOV-03.py) | org_assets, org_iam, folder_iam, assets |
| GOV-04 | Review exceptions and policy ownership | [GOV-04.py](../scripts/controls/GOV-04.py) | org_policies, project_iam |
| GOV-05 | Review project lifecycle and shutdown | [GOV-05.py](../scripts/controls/GOV-05.py) | project, services, billing_link, assets |
| IAM-01 | Resolve inherited privileged access | [IAM-01.py](../scripts/controls/IAM-01.py) | org_iam, folder_iam, project_iam, asset_iam, org_roles, project_roles |
| IAM-02 | Assess MFA and identity federation | [IAM-02.py](../scripts/controls/IAM-02.py) | project_iam, org_iam, asset_iam |
| IAM-03 | Review joiner mover leaver controls | [IAM-03.py](../scripts/controls/IAM-03.py) | asset_iam, org_iam, folder_iam |
| IAM-04 | Review emergency and time-bound privilege | [IAM-04.py](../scripts/controls/IAM-04.py) | org_iam, project_iam, audit_logs |
| IAM-05 | Assess deny and principal access boundaries | [IAM-05.py](../scripts/controls/IAM-05.py) | assets, asset_iam |
| WID-01 | Inventory service account ownership | [WID-01.py](../scripts/controls/WID-01.py) | service_accounts, asset_iam, instances, run_services |
| WID-02 | Review user-managed service account keys | [WID-02.py](../scripts/controls/WID-02.py) | service_accounts, sa_keys |
| WID-03 | Validate federation trust boundaries | [WID-03.py](../scripts/controls/WID-03.py) | wif_pools, wif_providers, asset_iam |
| WID-04 | Inspect service account escalation paths | [WID-04.py](../scripts/controls/WID-04.py) | asset_iam, project_iam, org_roles, project_roles, service_accounts |
| WID-05 | Review workload identity activity | [WID-05.py](../scripts/controls/WID-05.py) | audit_logs, service_accounts, sa_keys |
| ORG-01 | Verify effective organization policies | [ORG-01.py](../scripts/controls/ORG-01.py) | org_policies, effective_policy, assets |
| ORG-02 | Assess domain and external sharing restrictions | [ORG-02.py](../scripts/controls/ORG-02.py) | effective_policy, asset_iam |
| ORG-03 | Assess service account key guardrails | [ORG-03.py](../scripts/controls/ORG-03.py) | effective_policy, sa_keys, project_iam |
| ORG-04 | Review resource locations and sovereignty | [ORG-04.py](../scripts/controls/ORG-04.py) | assets, effective_policy |
| ORG-05 | Review custom constraints and drift | [ORG-05.py](../scripts/controls/ORG-05.py) | assets, org_policies, audit_logs |
| NET-01 | Resolve effective firewall exposure | [NET-01.py](../scripts/controls/NET-01.py) | firewalls, firewall_policies, networks, subnets, instances, routes |
| NET-02 | Assess external application protection | [NET-02.py](../scripts/controls/NET-02.py) | forwarding, backend, armor, assets |
| NET-03 | Inspect private access and egress | [NET-03.py](../scripts/controls/NET-03.py) | subnets, routers, routes, networks, dns |
| NET-04 | Assess VPC Service Controls | [NET-04.py](../scripts/controls/NET-04.py) | access_policies, perimeters, project |
| NET-05 | Review DNS and network telemetry | [NET-05.py](../scripts/controls/NET-05.py) | dns, subnets, firewalls, log_buckets |
| HYB-01 | Review Shared VPC administration | [HYB-01.py](../scripts/controls/HYB-01.py) | assets, networks, asset_iam |
| HYB-02 | Assess VPN redundancy and authentication | [HYB-02.py](../scripts/controls/HYB-02.py) | vpn, routers, routes |
| HYB-03 | Assess Interconnect dependencies | [HYB-03.py](../scripts/controls/HYB-03.py) | interconnect, routers, assets |
| HYB-04 | Review peering and transit trust | [HYB-04.py](../scripts/controls/HYB-04.py) | networks, routes, assets |
| HYB-05 | Assess hybrid administration access | [HYB-05.py](../scripts/controls/HYB-05.py) | instances, firewalls, asset_iam, audit_logs |
| CMP-01 | Review VM identity and metadata | [CMP-01.py](../scripts/controls/CMP-01.py) | instances, project_info, asset_iam |
| CMP-02 | Assess host login controls | [CMP-02.py](../scripts/controls/CMP-02.py) | instances, project_info, asset_iam |
| CMP-03 | Review boot integrity and images | [CMP-03.py](../scripts/controls/CMP-03.py) | instances, images, assets |
| CMP-04 | Assess patching and vulnerability operations | [CMP-04.py](../scripts/controls/CMP-04.py) | instances, assets, scc |
| CMP-05 | Inspect disks and deletion protection | [CMP-05.py](../scripts/controls/CMP-05.py) | instances, disks, snapshots, schedules |
| GKE-01 | Assess cluster control-plane access | [GKE-01.py](../scripts/controls/GKE-01.py) | clusters, asset_iam |
| GKE-02 | Review Kubernetes RBAC and admission | [GKE-02.py](../scripts/controls/GKE-02.py) | clusters, asset_iam, assets |
| GKE-03 | Assess workload and node identity | [GKE-03.py](../scripts/controls/GKE-03.py) | clusters, service_accounts, asset_iam |
| GKE-04 | Review cluster maintenance and supply chain | [GKE-04.py](../scripts/controls/GKE-04.py) | clusters, binary, repositories |
| GKE-05 | Assess workload isolation and recovery | [GKE-05.py](../scripts/controls/GKE-05.py) | clusters, assets, snapshots |
| RUN-01 | Review Cloud Run exposure and identity | [RUN-01.py](../scripts/controls/RUN-01.py) | run_services, asset_iam |
| RUN-02 | Assess functions and event triggers | [RUN-02.py](../scripts/controls/RUN-02.py) | functions, assets, asset_iam |
| RUN-03 | Inspect scheduled and batch execution | [RUN-03.py](../scripts/controls/RUN-03.py) | run_jobs, scheduler, asset_iam |
| RUN-04 | Review messaging access and data lifecycle | [RUN-04.py](../scripts/controls/RUN-04.py) | pubsub_topics, pubsub_subs, asset_iam |
| RUN-05 | Assess runtime secrets and network dependencies | [RUN-05.py](../scripts/controls/RUN-05.py) | run_services, functions, secrets, secret_versions |
| STO-01 | Assess public and external bucket access | [STO-01.py](../scripts/controls/STO-01.py) | buckets, asset_iam, effective_policy |
| STO-02 | Review uniform access and granular permissions | [STO-02.py](../scripts/controls/STO-02.py) | buckets, asset_iam, assets |
| STO-03 | Assess retention lifecycle and deletion recovery | [STO-03.py](../scripts/controls/STO-03.py) | buckets, assets |
| STO-04 | Inspect bucket encryption and location | [STO-04.py](../scripts/controls/STO-04.py) | buckets, assets, keys |
| STO-05 | Review storage logging and transfer paths | [STO-05.py](../scripts/controls/STO-05.py) | buckets, asset_iam, audit_logs, assets |
| DAT-01 | Review Cloud SQL access and exposure | [DAT-01.py](../scripts/controls/DAT-01.py) | sql, asset_iam |
| DAT-02 | Assess SQL availability and recovery | [DAT-02.py](../scripts/controls/DAT-02.py) | sql, sql_backups, assets |
| DAT-03 | Review BigQuery access and fine-grained controls | [DAT-03.py](../scripts/controls/DAT-03.py) | assets, asset_iam, audit_logs |
| DAT-04 | Assess BigQuery lifecycle and query governance | [DAT-04.py](../scripts/controls/DAT-04.py) | assets, asset_iam, audit_logs |
| DAT-05 | Assess other managed data platforms | [DAT-05.py](../scripts/controls/DAT-05.py) | spanner, redis, assets, asset_iam |
| KEY-01 | Review Secret Manager access and replication | [KEY-01.py](../scripts/controls/KEY-01.py) | secrets, asset_iam, assets |
| KEY-02 | Assess secret rotation and version lifecycle | [KEY-02.py](../scripts/controls/KEY-02.py) | secrets, secret_versions, run_services |
| KEY-03 | Assess KMS purpose and separation of duties | [KEY-03.py](../scripts/controls/KEY-03.py) | keyrings, keys, asset_iam |
| KEY-04 | Review key lifecycle and availability | [KEY-04.py](../scripts/controls/KEY-04.py) | keys, assets |
| KEY-05 | Assess CMEK and external key dependencies | [KEY-05.py](../scripts/controls/KEY-05.py) | assets, keys |
| LOG-01 | Verify Data Access audit coverage | [LOG-01.py](../scripts/controls/LOG-01.py) | org_iam, folder_iam, project_iam, services |
| LOG-02 | Review routing sinks and exclusions | [LOG-02.py](../scripts/controls/LOG-02.py) | org_sinks, sinks, exclusions, asset_iam |
| LOG-03 | Assess retention location and protected access | [LOG-03.py](../scripts/controls/LOG-03.py) | log_buckets, assets, asset_iam |
| LOG-04 | Prove an existing event's end-to-end trace | [LOG-04.py](../scripts/controls/LOG-04.py) | audit_logs, sinks, log_metrics |
| LOG-05 | Assess integrity and evidence visibility | [LOG-05.py](../scripts/controls/LOG-05.py) | asset_iam, audit_logs, project_iam |
| SEC-01 | Assess Security Command Center coverage | [SEC-01.py](../scripts/controls/SEC-01.py) | scc, org_assets, assets |
| SEC-02 | Review finding triage and suppression | [SEC-02.py](../scripts/controls/SEC-02.py) | scc, assets |
| SEC-03 | Validate detection use cases | [SEC-03.py](../scripts/controls/SEC-03.py) | audit_logs, log_metrics, scc |
| SEC-04 | Assess incident readiness and containment authority | [SEC-04.py](../scripts/controls/SEC-04.py) | org_iam, asset_iam, assets |
| SEC-05 | Review incident lessons and closure | [SEC-05.py](../scripts/controls/SEC-05.py) | scc, audit_logs |
| BCP-01 | Map recovery objectives to dependencies | [BCP-01.py](../scripts/controls/BCP-01.py) | assets, billing_link |
| BCP-02 | Review backup coverage and immutability | [BCP-02.py](../scripts/controls/BCP-02.py) | snapshots, schedules, sql_backups, assets, asset_iam |
| BCP-03 | Assess restore evidence | [BCP-03.py](../scripts/controls/BCP-03.py) | snapshots, sql_backups, assets |
| BCP-04 | Review regional and zonal failure readiness | [BCP-04.py](../scripts/controls/BCP-04.py) | instances, clusters, sql, project_info |
| BCP-05 | Assess recovery operations and ownership | [BCP-05.py](../scripts/controls/BCP-05.py) | assets, asset_iam |
| DEV-01 | Review source and build trigger trust | [DEV-01.py](../scripts/controls/DEV-01.py) | build_triggers, asset_iam |
| DEV-02 | Assess build identity and secrets | [DEV-02.py](../scripts/controls/DEV-02.py) | builds, build_triggers, assets, asset_iam |
| DEV-03 | Review artifact access and vulnerability governance | [DEV-03.py](../scripts/controls/DEV-03.py) | repositories, asset_iam, clusters, run_services |
| DEV-04 | Assess deployment approvals and admission | [DEV-04.py](../scripts/controls/DEV-04.py) | deploy, binary, clusters, run_services |
| DEV-05 | Review infrastructure drift and change evidence | [DEV-05.py](../scripts/controls/DEV-05.py) | assets, audit_logs, effective_policy |
| AI-01 | Inventory AI services and accountable uses | [AI-01.py](../scripts/controls/AI-01.py) | ai_endpoints, ai_models, ai_datasets, services, assets |
| AI-02 | Assess AI data use and retention | [AI-02.py](../scripts/controls/AI-02.py) | ai_datasets, assets, audit_logs |
| AI-03 | Review AI endpoint and runtime access | [AI-03.py](../scripts/controls/AI-03.py) | ai_endpoints, asset_iam, service_accounts |
| AI-04 | Assess agent tools and retrieval boundaries | [AI-04.py](../scripts/controls/AI-04.py) | assets, asset_iam |
| AI-05 | Review AI evaluation and operational oversight | [AI-05.py](../scripts/controls/AI-05.py) | ai_models, ai_endpoints, assets |
| OPS-01 | Assess observability against service objectives | [OPS-01.py](../scripts/controls/OPS-01.py) | assets, log_metrics |
| OPS-02 | Review quotas and capacity risk | [OPS-02.py](../scripts/controls/OPS-02.py) | project_info, assets |
| OPS-03 | Assess maintenance and support lifecycle | [OPS-03.py](../scripts/controls/OPS-03.py) | clusters, functions, sql, assets |
| OPS-04 | Review operational change and access | [OPS-04.py](../scripts/controls/OPS-04.py) | audit_logs, builds, asset_iam |
| OPS-05 | Assess service ownership and incident learning | [OPS-05.py](../scripts/controls/OPS-05.py) | project, assets, scc |
| FIN-01 | Reconcile billing and project accountability | [FIN-01.py](../scripts/controls/FIN-01.py) | billing_link, project, assets |
| FIN-02 | Review budgets and spend control behavior | [FIN-02.py](../scripts/controls/FIN-02.py) | budgets, billing_link |
| FIN-03 | Assess allocation and cost reporting | [FIN-03.py](../scripts/controls/FIN-03.py) | assets, project, billing_link |
| FIN-04 | Review optimization decisions and commitments | [FIN-04.py](../scripts/controls/FIN-04.py) | instances, disks, assets, project_info |
| FIN-05 | Assess cost anomalies and abuse readiness | [FIN-05.py](../scripts/controls/FIN-05.py) | budgets, audit_logs, scc |
| COM-01 | Map obligations to system scope | [COM-01.py](../scripts/controls/COM-01.py) | services, assets |
| COM-02 | Assess classification and data discovery | [COM-02.py](../scripts/controls/COM-02.py) | assets, buckets, ai_datasets |
| COM-03 | Review privacy lifecycle and deletion evidence | [COM-03.py](../scripts/controls/COM-03.py) | assets, buckets, audit_logs |
| COM-04 | Assess regulated workload controls | [COM-04.py](../scripts/controls/COM-04.py) | assets, effective_policy, audit_logs |
| COM-05 | Review audit evidence and assurance closure | [COM-05.py](../scripts/controls/COM-05.py) | assets |
| P01 | Authorize and scope | [P01.py](../scripts/phases/P01.py) | org_assets, project, billing_link, services, assets |
| P02 | Prepare tooling and access | [P02.py](../scripts/phases/P02.py) | org_iam, folder_iam, project_iam, asset_iam, org_roles, project_roles, org_assets, project, billing_link |
| P03 | Reconcile the population | [P03.py](../scripts/phases/P03.py) | org_assets, project, billing_link, services, assets |
| P04 | Establish the baseline and sample | [P04.py](../scripts/phases/P04.py) | org_policies, project_iam, effective_policy, assets |
| P05 | Collect configuration evidence | [P05.py](../scripts/phases/P05.py) | org_assets, project, billing_link, services, assets, org_iam, folder_iam, org_policies, project_iam, asset_iam, org_roles, project_roles, audit_logs, service_accounts, instances, run_services, sa_keys, wif_pools, wif_providers, effective_policy, firewalls, firewall_policies, networks, subnets, routes, forwarding, backend, armor, routers, dns, access_policies, perimeters, log_buckets, vpn, interconnect, project_info, images, scc, disks, snapshots, schedules, clusters, binary, repositories, functions, run_jobs, scheduler, pubsub_topics, pubsub_subs, secrets, secret_versions, buckets, keys, sql, sql_backups, spanner, redis, keyrings, org_sinks, sinks, exclusions, log_metrics, build_triggers, builds, deploy, ai_endpoints, ai_models, ai_datasets, budgets |
| P06 | Review operating effectiveness | [P06.py](../scripts/phases/P06.py) | audit_logs, sinks, log_metrics, scc, snapshots, sql_backups, assets |
| P07 | Challenge findings | [P07.py](../scripts/phases/P07.py) | org_iam, folder_iam, project_iam, asset_iam, org_roles, project_roles, buckets, effective_policy, assets |
| P08 | Prioritize and agree actions | [P08.py](../scripts/phases/P08.py) | scc, assets |
| P09 | Report and hand over | [P09.py](../scripts/phases/P09.py) | assets, services |
| P10 | Retest and close | [P10.py](../scripts/phases/P10.py) | snapshots, sql_backups, assets |
| R01-S01 | Establish organizational ownership and scope | [R01-S01.py](../scripts/steps/R01-S01.py) | org_assets, project, billing_link |
| R01-S02 | Review project lifecycle and shutdown | [R01-S02.py](../scripts/steps/R01-S02.py) | project, services, billing_link, assets |
| R01-S03 | Reconcile billing and project accountability | [R01-S03.py](../scripts/steps/R01-S03.py) | billing_link, project, assets |
| R01-S04 | Review resource locations and sovereignty | [R01-S04.py](../scripts/steps/R01-S04.py) | assets, effective_policy |
| R01-S05 | Review audit evidence and assurance closure | [R01-S05.py](../scripts/steps/R01-S05.py) | assets |
| R02-S01 | Resolve inherited privileged access | [R02-S01.py](../scripts/steps/R02-S01.py) | org_iam, folder_iam, project_iam, asset_iam, org_roles, project_roles |
| R02-S02 | Assess deny and principal access boundaries | [R02-S02.py](../scripts/steps/R02-S02.py) | assets, asset_iam |
| R02-S03 | Inventory service account ownership | [R02-S03.py](../scripts/steps/R02-S03.py) | service_accounts, asset_iam, instances, run_services |
| R02-S04 | Validate federation trust boundaries | [R02-S04.py](../scripts/steps/R02-S04.py) | wif_pools, wif_providers, asset_iam |
| R02-S05 | Inspect service account escalation paths | [R02-S05.py](../scripts/steps/R02-S05.py) | asset_iam, project_iam, org_roles, project_roles, service_accounts |
| R03-S01 | Resolve effective firewall exposure | [R03-S01.py](../scripts/steps/R03-S01.py) | firewalls, firewall_policies, networks, subnets, instances, routes |
| R03-S02 | Assess external application protection | [R03-S02.py](../scripts/steps/R03-S02.py) | forwarding, backend, armor, assets |
| R03-S03 | Review Cloud Run exposure and identity | [R03-S03.py](../scripts/steps/R03-S03.py) | run_services, asset_iam |
| R03-S04 | Assess public and external bucket access | [R03-S04.py](../scripts/steps/R03-S04.py) | buckets, asset_iam, effective_policy |
| R03-S05 | Review BigQuery access and fine-grained controls | [R03-S05.py](../scripts/steps/R03-S05.py) | assets, asset_iam, audit_logs |
| R04-S01 | Verify Data Access audit coverage | [R04-S01.py](../scripts/steps/R04-S01.py) | org_iam, folder_iam, project_iam, services |
| R04-S02 | Review routing sinks and exclusions | [R04-S02.py](../scripts/steps/R04-S02.py) | org_sinks, sinks, exclusions, asset_iam |
| R04-S03 | Assess retention location and protected access | [R04-S03.py](../scripts/steps/R04-S03.py) | log_buckets, assets, asset_iam |
| R04-S04 | Prove an existing event's end-to-end trace | [R04-S04.py](../scripts/steps/R04-S04.py) | audit_logs, sinks, log_metrics |
| R04-S05 | Assess integrity and evidence visibility | [R04-S05.py](../scripts/steps/R04-S05.py) | asset_iam, audit_logs, project_iam |
| R05-S01 | Assess classification and data discovery | [R05-S01.py](../scripts/steps/R05-S01.py) | assets, buckets, ai_datasets |
| R05-S02 | Inspect bucket encryption and location | [R05-S02.py](../scripts/steps/R05-S02.py) | buckets, assets, keys |
| R05-S03 | Review BigQuery access and fine-grained controls | [R05-S03.py](../scripts/steps/R05-S03.py) | assets, asset_iam, audit_logs |
| R05-S04 | Assess KMS purpose and separation of duties | [R05-S04.py](../scripts/steps/R05-S04.py) | keyrings, keys, asset_iam |
| R05-S05 | Review key lifecycle and availability | [R05-S05.py](../scripts/steps/R05-S05.py) | keys, assets |
| R06-S01 | Map recovery objectives to dependencies | [R06-S01.py](../scripts/steps/R06-S01.py) | assets, billing_link |
| R06-S02 | Review backup coverage and immutability | [R06-S02.py](../scripts/steps/R06-S02.py) | snapshots, schedules, sql_backups, assets, asset_iam |
| R06-S03 | Assess restore evidence | [R06-S03.py](../scripts/steps/R06-S03.py) | snapshots, sql_backups, assets |
| R06-S04 | Review regional and zonal failure readiness | [R06-S04.py](../scripts/steps/R06-S04.py) | instances, clusters, sql, project_info |
| R06-S05 | Assess recovery operations and ownership | [R06-S05.py](../scripts/steps/R06-S05.py) | assets, asset_iam |
| R07-S01 | Review source and build trigger trust | [R07-S01.py](../scripts/steps/R07-S01.py) | build_triggers, asset_iam |
| R07-S02 | Assess build identity and secrets | [R07-S02.py](../scripts/steps/R07-S02.py) | builds, build_triggers, assets, asset_iam |
| R07-S03 | Assess deployment approvals and admission | [R07-S03.py](../scripts/steps/R07-S03.py) | deploy, binary, clusters, run_services |
| R07-S04 | Assess agent tools and retrieval boundaries | [R07-S04.py](../scripts/steps/R07-S04.py) | assets, asset_iam |
| R07-S05 | Review AI evaluation and operational oversight | [R07-S05.py](../scripts/steps/R07-S05.py) | ai_models, ai_endpoints, assets |
| R08-S01 | Assess Security Command Center coverage | [R08-S01.py](../scripts/steps/R08-S01.py) | scc, org_assets, assets |
| R08-S02 | Validate detection use cases | [R08-S02.py](../scripts/steps/R08-S02.py) | audit_logs, log_metrics, scc |
| R08-S03 | Assess observability against service objectives | [R08-S03.py](../scripts/steps/R08-S03.py) | assets, log_metrics |
| R08-S04 | Review budgets and spend control behavior | [R08-S04.py](../scripts/steps/R08-S04.py) | budgets, billing_link |
| R08-S05 | Review audit evidence and assurance closure | [R08-S05.py](../scripts/steps/R08-S05.py) | assets |
