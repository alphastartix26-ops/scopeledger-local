# AI security evidence review — development preview

ScopeLedger v0.9 adds local review of already-generated reports from garak, Promptfoo and ModelScan. This is original interoperability and decision-support code; external scanners, attack payloads, databases and AI models are not bundled.

| Evidence source | Review unit | Important limitation |
| --- | --- | --- |
| NVIDIA garak | Detector evaluations, probe/detector pairs | Incomplete run or unscored output is not a pass. |
| Promptfoo | Evaluation rows | Reported assertion failures and execution errors remain distinct; schema version is not the actual tool version. |
| ModelScan | Scanned artifacts and operator findings | Missing skipped-file accounting is unknown, not zero. |

The console checks count consistency, records the original report SHA-256, excludes raw prompts, outputs, paths and issue messages from exported summaries, and can register aggregate review items in its local risk register. SHA-256 identifies bytes, not source authenticity. It does not run exploits or load model files.

## Example (illustrative only)

Suppose a model evaluation records 8 passes, 2 reported failures and 1 unscored output. A second evaluation records 1 pass, 1 assertion failure and 1 execution error. A model-file review records 1 high-severity finding, 2 scanned artifacts and 1 skipped artifact. Keep these denominators distinct. Do not combine them into a vulnerability count or a security score.

The current policy requests all three report categories and holds review eligibility if reports, scope, coverage, outcomes or tool-version evidence are incomplete, or if failures/errors/skips remain. The alternative state means eligible for human review only, not release approval. Baseline comparisons are conditional aggregate differences, not proof of identical test cases or remediation.

## Source review and provenance

- [garak evaluator](https://github.com/NVIDIA/garak/blob/main/garak/evaluators/base.py) (blob b6ad3b4bb77609b69b948b2ec41bac4dbed05b0c) and [run lifecycle](https://github.com/NVIDIA/garak/blob/main/garak/command.py) (2fb56c1960d6e7fe6e9c03e1e3a9fb31b191e282); Apache-2.0.
- [Promptfoo result types](https://github.com/promptfoo/promptfoo/blob/main/src/types/results.ts) (8088bf8347bb3f94a845f22792350d0d28dbd5c0) and [output types](https://github.com/promptfoo/promptfoo/blob/main/src/types/index.ts) (70ecbd4aefebc609d74f8e3357f125f65db0ca58); MIT.
- [ModelScan report writer](https://github.com/protectai/modelscan/blob/main/modelscan/reports.py) (f09159b8dcedd9c90338e6e3368b910c74834b90), [result generator](https://github.com/protectai/modelscan/blob/main/modelscan/modelscan.py) (4442f5eb4f143811a45cbfd4fb61151ecddffede), [issue schema](https://github.com/protectai/modelscan/blob/main/modelscan/issues.py) (b254084889f24ec7bdcb2c6173dd5b4955369132); Apache-2.0.
- [OWASP AISVS](https://github.com/OWASP/AISVS); CC BY-SA 4.0, reference only.

No upstream implementation or third-party binaries are redistributed in this change. Compatibility is limited to the reviewed report contracts. Project names do not imply affiliation.

The new module was tested with synthetic report fixtures, including malformed counts, incomplete runs, errors, sensitive-string exclusion, duplicate imports and local risk-register integration. Actual externally generated evaluation results, tool-version compatibility and enterprise deployment remain unverified. The local review dashboard and separate team-vault prototype are not yet one integrated enterprise workflow.

[Request evaluation or purchase availability](https://github.com/alphastartix26-ops/scopeledger-local/issues/new?template=evaluation.yml). No paid download or checkout is currently active. Do not submit sensitive data.
