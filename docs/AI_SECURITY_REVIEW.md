# AI security evidence review — development preview

ScopeLedger v0.9 adds local review of already-generated reports from garak, Promptfoo and ModelScan. This is original interoperability and decision-support code; external scanners, attack payloads, databases and AI models are not bundled.

| Evidence source | Review unit | Important limitation |
| --- | --- | --- |
| NVIDIA garak | Detector evaluations, probe/detector pairs | Incomplete run or unscored output is not a pass. |
| Promptfoo | Evaluation rows | Reported assertion failures and execution errors remain distinct; schema, exporter version and cache accounting are separate. |
| ModelScan | Scanned artifacts and operator findings | Missing skipped-file accounting is unknown, not zero. |

The console checks count consistency, records the original report SHA-256, excludes raw prompts, outputs, paths and issue messages from exported summaries, and can register aggregate review items in its local risk register. SHA-256 identifies bytes, not source authenticity. It does not run exploits or load model files.

## Example (illustrative only)

Suppose a model evaluation records 8 passes, 2 reported failures and 1 unscored output. A second evaluation records 1 pass, 1 assertion failure and 1 execution error. A model-file review records 1 high-severity finding, 2 scanned artifacts and 1 skipped artifact. Keep these denominators distinct. Do not combine them into a vulnerability count or a security score.

The current policy requests all three report categories and holds review eligibility if reports, scope, coverage, outcomes or tool-version evidence are incomplete, or if failures/errors/skips remain. The alternative state means eligible for human review only, not release approval. Baseline comparisons are conditional aggregate differences, not proof of identical test cases or remediation.

## Why a passing AI evaluation is not necessarily fresh evidence

In a Promptfoo v3 JSON export, the schema identifier describes the file format. The optional `metadata.promptfooVersion` describes the reported exporter version; the current upstream metadata generator uses the export-time VERSION. Neither establishes the evaluator binary at the time a stored evaluation was run. The optional `stats.cacheHits` field reports rows served from cache.

ScopeLedger v0.9.1 corrects a prior review-gate defect in which a schema identifier could satisfy the reported-version requirement. The new local adapter keeps those concepts separate and applies the following conservative policy to synthetic examples with all other checks satisfied:

| Export evidence | Reported outcome | Review eligibility |
| --- | --- | --- |
| Schema 3, exporter version absent | 10/10 passed | HOLD: reported version unknown |
| Reported exporter version, cache count absent | 10/10 passed | HOLD: freshness accounting unknown |
| Reported exporter version, 10 cached rows | 10/10 passed | HOLD: cached results present |
| Reported exporter version, explicitly zero cached rows | 10/10 passed | Eligible for manual review only |

Missing cache accounting is not converted to zero, and cached rows are not converted to failures. Invalid or contradictory cache counts are rejected. The conservative policy can hold older exports missing these optional fields. Baseline comparisons require known matching reported versions and explicit zero cached rows on both Promptfoo reports; this does not establish identical test cases or independently verify freshness. An authorized reviewer must confirm the actual evaluation version, configuration, coverage and model identity. A report with an explicit zero cache count is not proof of fresh execution.

On 2026-11-25 the owner-side development candidate passed 290 Node tests (including 15 targeted provenance tests), 15 existing Chromium checks and 13 additional Chromium checks using synthetic reports. The tested browser file-import and JSON/HTML export paths preserve bounded provenance, exclude the fixture's author and private paths, and issue no network requests. This is not real scanner compatibility, actual inference performance or security certification.

Source: [Promptfoo export metadata implementation](https://github.com/promptfoo/promptfoo/blob/main/src/util/output.ts), reviewed Git blob `10c2b2a528de7b8047cd423c5530b68b451b43ea`; [output and evaluation types](https://github.com/promptfoo/promptfoo/blob/main/src/types/index.ts), blob `70ecbd4aefebc609d74f8e3357f125f65db0ca58`. These are reviewed blob identities, not release tags.

## Why a review declaration must follow the evidence context

A review declaration is only useful when the reviewer can identify what it covers. Changing the registration asset, scope identifier or observation date after confirming the evaluation context requires a new review. Similarly, restoring a workspace must not silently reuse an unregistered dashboard session, even if the workspace has the same identifier.

In the v0.9.2 local development candidate, these changes reset the relevant review/comparability declarations. HTML exports include conditional baseline digests and per-tool comparison status, without the original paths, outputs or author metadata. A ModelScan report that claims zero scanned artifacts but lists nonempty scanned files is rejected as contradictory; genuine zero coverage remains incomplete.

| Illustrative input or action | Expected behavior |
| --- | --- |
| Change the approved scope after recording review | Re-review before registration |
| Restore an earlier workspace with the same ID | Clear the session-only AI dashboard |
| Zero scanned artifacts with a nonempty file list | Reject inconsistent evidence |
| Different report digest and declared comparable evaluation | Conditional per-tool delta only; no proof of remediation |

On 2026-11-26 the local candidate passed 296 Node tests and 40 Chromium checks using synthetic fixtures, including actual file-input, export and legacy checksum restore UI checks and Node encrypted workspace round-trip checks. This does not establish actual external scanner compatibility, Windows deployment, encrypted browser-vault operation or enterprise certification. The candidate remains unpublished for paid distribution.

## Source review and provenance

- [garak evaluator](https://github.com/NVIDIA/garak/blob/main/garak/evaluators/base.py) (blob b6ad3b4bb77609b69b948b2ec41bac4dbed05b0c) and [run lifecycle](https://github.com/NVIDIA/garak/blob/main/garak/command.py) (2fb56c1960d6e7fe6e9c03e1e3a9fb31b191e282); Apache-2.0.
- [Promptfoo result types](https://github.com/promptfoo/promptfoo/blob/main/src/types/results.ts) (8088bf8347bb3f94a845f22792350d0d28dbd5c0) and [output types](https://github.com/promptfoo/promptfoo/blob/main/src/types/index.ts) (70ecbd4aefebc609d74f8e3357f125f65db0ca58); MIT.
- [ModelScan report writer](https://github.com/protectai/modelscan/blob/main/modelscan/reports.py) (f09159b8dcedd9c90338e6e3368b910c74834b90), [result generator](https://github.com/protectai/modelscan/blob/main/modelscan/modelscan.py) (4442f5eb4f143811a45cbfd4fb61151ecddffede), [issue schema](https://github.com/protectai/modelscan/blob/main/modelscan/issues.py) (b254084889f24ec7bdcb2c6173dd5b4955369132); Apache-2.0.
- [OWASP AISVS](https://github.com/OWASP/AISVS); CC BY-SA 4.0, reference only.

No upstream implementation or third-party binaries are redistributed in this change. Compatibility is limited to the reviewed report contracts. Project names do not imply affiliation.

The new module was tested with synthetic report fixtures, including malformed counts, incomplete runs, errors, sensitive-string exclusion, duplicate imports and local risk-register integration. Actual externally generated evaluation results, tool-version compatibility and enterprise deployment remain unverified. The local review dashboard and separate team-vault prototype are not yet one integrated enterprise workflow.

[Request evaluation or purchase availability](https://github.com/alphastartix26-ops/scopeledger-local/issues/new?template=evaluation.yml). No paid download or checkout is currently active. Do not submit sensitive data.
