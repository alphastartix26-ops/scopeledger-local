# ScopeLedger Executive

**Turn security findings into an evidence-led executive decision queue.**

`v0.9.0 development candidate` · `Local-first` · `One-time license planned`

Security teams already have scanners. The difficult part is deciding what matters, what is still unresolved, and what the executive team needs to see. ScopeLedger is a single-operator review console for authorized projects and imported security evidence.

![Illustration of a synthetic executive report, not a product screenshot](executive-report-preview.svg)

**[Try the free synthetic workflow exercise](demo/README.md)** · **[Read the latest sample executive briefing](samples/EXECUTIVE_V061.md)** · **[Request evaluation / purchase availability](https://github.com/alphastartix26-ops/scopeledger-local/issues/new?template=evaluation.yml)** · [한국어](README.ko.md)


## Latest development: AI security evidence review

The v0.9.0 development candidate adds local garak, Promptfoo and ModelScan report adapters, separate failure/error/coverage counts, conditional baseline comparison, conservative review gating and aggregate risk-register integration. See [AI security evidence review](docs/AI_SECURITY_REVIEW.md) for the supported contracts, illustrative example and source provenance. This module has been tested with synthetic reports; actual scanner execution and version compatibility remain unverified. The separate v0.8 team-vault prototype provides workspace ACLs, TOTP, audit-chain checks and encrypted recovery; it is not an integrated enterprise release. The public exercise and older sample below still illustrate the earlier workflow.

## What the earlier local workflow does

| Decision workflow | Scope |
| --- | --- |
| Evidence intake | 22 heuristic configuration rules; limited SARIF, Trivy and Gitleaks imports; optional Trivy/Gitleaks/Bandit execution adapters |
| Risk reconciliation | Exact scoped Trivy dependency identity grouping, version and patch evidence, raw versus grouped counts |
| Threat context | Dated CISA KEV, FIRST EPSS and NVD input; local collection adapters; explicit missing/stale evidence |
| Remediation review | Human decisions, ownership, due dates, acceptance expiry, repeat-observation comparison |
| Dependency context | Operator-declared asset dependencies and bounded direct/indirect impact review |
| Evidence-based advisor | Deterministic remediation-review suggestions; optional local Ollama ordering adapter |
| Reporting and backup | English executive HTML, internal CSV, AES-256-GCM encrypted backup, current-workspace verification and exit warning |

The full application currently has a Korean interface and English executive HTML export. Scanner binaries, AI models and threat databases are not bundled. The public exercise is a separate synthetic demo, not the paid application.

## See the workflow

1. Review the [sample executive report](samples/EXECUTIVE_V061.md): 13 active review cases, 14 raw evidence records, 3 registered assets, 2 declared dependency links. These are synthetic demonstration observations, not customer results.
2. Download [the synthetic exercise](demo/ScopeLedger_Demo.html) from GitHub and open it locally. Select a risk, change review status, and compare how the executive action queue changes.
3. Use the [risk-review checklist](docs/RISK_REVIEW_CHECKLIST.md) to evaluate how a review process handles stale evidence, repeat observations and human decisions.
4. If this workflow would help your team, [request evaluation / purchase availability](https://github.com/alphastartix26-ops/scopeledger-local/issues/new?template=evaluation.yml). Do not share sensitive data.

## Commercial availability

**Planned initial price: KRW 59,000 equivalent, one-time payment.** Final checkout currency and terms will be displayed only after seller onboarding, product eligibility review, and delivery verification. No recurring subscription is planned. No payment or order is accepted here today. Evaluation requests are non-binding and free; please do not send payment information.

## Evaluation boundaries

This is a local single-operator development candidate, not an enterprise-certified security platform. No SSO/RBAC, centrally encrypted multi-user store, SIEM/EDR integration or authenticated immutable audit is provided. External scanner/model/feed integration and scheduled operation require separate installation and real-environment verification. The local engine is heuristic; imported records do not prove exploitable vulnerabilities, complete coverage or remediation. Registered dependency relationships are not network discovery or attack paths. The checksums are not signatures. Successful secure-context browser vault verification and actual Windows and enterprise deployment remain unverified. Use authorized data only.

[Version history](CHANGELOG.md) · [Security and responsible use](SECURITY.md)

The public exercise and sample material are provided for evaluation. The commercial application source and private distribution files are not published here.
