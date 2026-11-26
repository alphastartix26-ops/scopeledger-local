# ScopeLedger Executive

**Turn existing security evidence into a human review queue and executive briefing.**

`Local Review Edition v0.9.2` · `Korean UI / English reports` · `One named operator`

[**Purchase the local edition — US$44 one-time**](https://alphastartix.gumroad.com/l/cbrtll) · [Free synthetic workflow exercise](demo/README.md) · [한국어](README.ko.md)

## Current availability — November 27, 2026

The early commercial local edition is available on Gumroad. The checkout price is US$44 before applicable taxes; localized prices may vary. The purchase delivers one ZIP containing the standalone HTML application, setup guide, supported-format and AI-review guides, synthetic SARIF sample, license/support terms, validation record and integrity manifest. No subscription or paid API is required by the app. One named operator may use the delivered version for authorized internal/client review and commercial report output; software redistribution and multi-user sharing are not included. Installation/defect support is available by receipt reply for 30 days; a 14-day refund window applies without limiting mandatory rights.

On November 27, 2026, the ZIP downloaded from a Gumroad test receipt matched the published package in size (75,516 bytes) and SHA-256 (`01485a7f389ecbdbf974c62d32cba929402febbc291680d730946f4e0741d721`). On Windows, the code inside that ZIP saved an encrypted workspace and restored its complete contents in a fresh Node process. The Windows browser interface still awaits a separate check.

## Included workflow

| Task | Delivered scope |
| --- | --- |
| Evidence intake | 22 heuristic configuration checks; bounded SARIF 2.1.0, Trivy SchemaVersion 2 and Gitleaks JSON imports |
| Review | Scoped reconciliation, raw versus grouped counts, human decisions, owners, due dates and acceptance expiry |
| Context | Manual threat-context inputs and operator-declared asset dependencies |
| Response planning | Rule-based suggestions; no model execution |
| AI evidence | Bounded aggregate garak, Promptfoo v3 and ModelScan report review; missing evidence remains HOLD |
| Reports and storage | English executive HTML, internal CSV and encrypted workspace backup with read-back comparison |

No scanner binaries, native runner, AI model, automated threat-feed synchronization, team server, SSO/RBAC, hosted service or enterprise certification are included. Optional integration panels are hidden/disabled in this edition. The separate team/native prototypes described in historical development notes are not part of the purchase.

## Validation and limits

- Re-run on Windows with Node.js 24.19.0: **296/296 engine regression tests** and **9/9 archive-admission tests** passed. The shipped HTML scripts parse; the included synthetic SARIF sample is accepted by the engine. Original owner/evaluation archive manifests were verified.
- **This exact package's Windows browser UI and encrypted browser save/read-back/restore remain unverified.** The automation tool rejected local-file navigation; that restriction was not bypassed. Node cryptography checks do not establish browser UI compatibility.
- The original v0.9.2 source archive records 40 prior synthetic Chromium UI checks; those are historical upstream results, not new validation of the delivered Windows edition wrapper.
- Actual externally generated scanner/version combinations, Firefox/Safari, mobile operation and enterprise deployment are not validated. Test synthetic data and backup recovery in an approved browser before real work. Do not bypass organizational controls.
- Findings are heuristic review items, not proof of exploitability, complete scan coverage, compliance or safety. Source hashes are fingerprints, not signatures. Session data is not autosaved; exports and source reports need separate protection. Forgotten backup passphrases cannot be recovered.

## Explore before purchasing

[Free synthetic exercise](demo/README.md) · [Synthetic executive report](samples/EXECUTIVE_V061.md) · [Risk-review checklist](docs/RISK_REVIEW_CHECKLIST.md) · [AI report contract notes](docs/AI_SECURITY_REVIEW.md)

The public exercise illustrates an earlier workflow and is not the paid application. All examples are synthetic, not customer results. Do not post confidential evidence in GitHub issues.

[Version history](CHANGELOG.md) · [Security and responsible use](SECURITY.md)

Commercial source and buyer distribution files remain private; this repository contains public documentation and synthetic examples only.
