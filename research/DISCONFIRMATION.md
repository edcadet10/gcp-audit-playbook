# What changed after trying to break the design

The research and local experiments **revised the design before publication**. The [preregistered claim](preregistration.md) was that the collector could acquire scoped read-only evidence while preserving uncertainty. The current evidence supports that limited claim for the reviewed implementation and offline cases; it does not establish live organization coverage or audit effectiveness.

## Rejected assumptions

| Initial shortcut | Contrary evidence | Resulting design |
|---|---|---|
| Plausible CLI names are executable | Local SDK help rejected `build triggers list`, `logging exclusions list` and `ai datasets list` | Corrected to `builds triggers list`; sink exclusions come from sink metadata; Vertex AI datasets use supported Cloud Asset Inventory resource metadata |
| A guessed documentation path is a reference | Initial HTTP checks found 32 missing paths, including invalid command references | Located current Google documentation, reviewed redirects and regenerated references; final availability results are recorded separately |
| An asset export establishes the whole population | Google documents eventual consistency and supported-type/method limits | Independent reconciliation, native lists and explicit unsupported evidence requests |
| Project IAM is effective access | Ancestor inheritance, groups, conditions, deny and principal boundaries affect access | Ancestor collection and a required effective-access workpaper |
| Public prevention removes every sharing path | Signed URLs are outside Cloud Storage public access prevention | Signed-access governance is reviewed separately |
| Every budget is just an alert | Current Google documentation distinguishes alerts-only and supported spend-cap budgets | Inspect actual budget type, supported service and response behavior |
| An SCC tier recommendation stays current | Current tier documentation identifies Enterprise retirement on 21 May 2027 | Verify deployed tier, coverage and transition rather than prescribe a stale edition |
| A model training restriction implies zero retention | AI feature-specific retention and logging exceptions are documented | Review the actual model, grounding, logging, cache and contract configuration |
| Read-only means HTTP GET only | `getIamPolicy` and `entries.list` are semantic reads implemented with POST | Audit command/API semantics; permit only registered reads |
| CLI noninteractive mode alone is enough to explain read-only behavior | Installed SDK code includes an API-enablement prompt path | Explicitly disable that path in the SDK environment and require least-privileged access without enablement rights |

Sources: [asset support](https://docs.cloud.google.com/asset-inventory/docs/asset-types), [IAM inheritance](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control), [principal boundaries](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies), [public prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention), [budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets), [SCC tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers), [AI retention](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/data-governance), [getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/getIamPolicy), [entries.list](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list). Exact corrected CLI references are in the [operation register](../docs/SCRIPT-OPERATIONS.md).

## Experiments and measured results

The first local help probe tested 69 registered paths against installed SDK **582.0.0**. **Three failed**, triggering the corrections above. A second probe reported **69 valid command paths and no missing fixed flags**. The public [CLI report](cli-help-checks.json) contains command paths, synopsis, documented flags and output hashes rather than complete third-party help pages. The missing-SDK installer uses separately documented **589.0.0** portable archives; that is not a claim that live calls have been tested against both versions.

The first adversarial test run executed **34 tests, all passing**, using the actual dispatcher with fake CLI responses and patched subprocesses. It tested wrong organization and project identity, forged command paths, write verbs, forbidden flags, shell metacharacters, missing scope, denied reads, failed child enumeration, malformed JSON, timeouts, account mismatch, endpoint/credential overrides, sample caps, archive traversal, public-repository output rejection and workpaper path boundaries. Current counts and details are in [test-results.json](test-results.json). Additional tests may be added when a new concern is found; the machine-readable result records the latest run.

The tests also demonstrate what the system **does not claim**: a successful empty read is not a pass; a review candidate is not a vulnerability; a file hash does not prove restore effectiveness; and an offline plan must not install tools, authenticate or connect.

A subsequent first-login regression test **failed**: the noninteractive read environment also disabled verification-code prompts during authentication. The fix permits prompts only for the explicit authentication subprocess, while preserving disabled API-enablement prompting. The expanded suite then passed; the latest count is recorded in the test report and README.

## Source review method

Public documentation was searched through Google's primary sources and fetched into a local, uncommitted review cache. The register preserves URLs, titles, redirects, HTTP outcome and retrieval time. Review focused on the semantics driving controls: inheritance, provider defaults, service scope, edition availability, command syntax, resource support, evidence visibility and expected limitations. HTTP success alone does not prove a reference supports a claim. The source text is not republished as a documentation mirror.

An exact-string search initially failed to locate `aiplatform.googleapis.com/Dataset` because HTML word-break elements introduced spaces in the extracted text. Inspection of the surrounding supported-type table confirmed the type. This was a source-extraction false negative, not evidence that the product lacked dataset inventory support.

## What remains unproven

No customer organization, billing account or project was queried; no cloud authentication occurred during repository authoring. Tests do not establish sufficiency of actual IAM grants, quota projects, VPC restrictions, service activation, pagination behavior of every live SDK command, complete historical populations or correct control conclusions. Installation has not been exercised on every supported OS. Directory, Kubernetes, database-native, application and historical process evidence require the supplemental workpapers listed by each control. A representative authorized pilot and population reconciliation are mandatory parts of a real engagement.

**Updated claim:** retained with these limits. The repository provides documented read-only acquisition and review procedures, with tested failure handling; it does not automatically certify an organization's security or compliance.
