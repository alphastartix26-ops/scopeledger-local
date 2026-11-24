# Executive briefing — v0.6.1

**Synthetic demonstration.** Transcribed from an actual HTML report exported from the local candidate in an isolated Chromium test. Report date: 2026-11-24 UTC. No actual customer assets or verified vulnerabilities are represented.

## Executive review

| Metric | Count |
| --- | ---: |
| Registered assets | 3 |
| Evidence batches | 3 |
| Active review cases | 13 |
| Raw evidence records | 14 |
| High / critical action queue (raw) | 5 |
| Unreviewed (raw) | 10 |
| Overdue (raw) | 1 |
| Expired acceptances | 0 |
| P0 (local policy) | 0 |
| P1 (local policy) | 6 |
| Declared dependency links | 2 |

CRITICAL 1 · HIGH 4 · MEDIUM 6 · LOW 1 · UNKNOWN 1 (active raw records). In-date acceptance 1; human-recorded closure 1. The P1 queue includes an UNKNOWN record; unknown severity is not low risk.

| Asset alias | Business importance | Active raw records | High / critical raw queue |
| --- | --- | ---: | ---: |
| Asset 01 | MISSION_CRITICAL | 10 | 3 |
| Asset 02 | HIGH | 2 | 2 |
| Asset 03 | STANDARD | 1 | 0 |

## Evidence coverage

- Asset 01: LOCAL, 11 records; 7 scanned / 0 partial / 1 skipped.
- Asset 02: TRIVY, 2 imported synthetic records; external scope unknown, warnings present.
- Asset 03: SARIF, 1 imported synthetic record; external scope unknown, warnings present.
- KEV and EPSS not loaded in this demonstration.
- 0 repeated observations grouped; 0 absent in later imports. Absence is not remediation.
- 2 operator-declared dependency links: impact-review scope only; not measured network reachability.

## Management actions

Review untriaged records, resolve overdue actions, reassess expiring acceptances, and verify evidence coverage with owners. Before closing any case, confirm remediation and the rescan scope. Record a human decision with a ticket reference. These counts are review records, not confirmed vulnerabilities or risk certification.

The exported executive report separates the raw evidence section from the reconciled decision queue. Names, paths and review notes are omitted. Local audit history and checksums are not tamper-proof signatures.
