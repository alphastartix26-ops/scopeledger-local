# Evidence-led security review checklist

Free workflow checklist for authorized internal security reviews. It is not a penetration-testing guide, compliance certificate or a guarantee of vulnerability coverage.

| Gate | Evidence to review |
| --- | --- |
| Scope | Asset, owner, approved scope ID, source tool and version |
| Coverage | Scanned, partial, skipped, unsupported; missing evidence must remain unknown |
| Identity | CVE where applicable, component, installed version, target and scope |
| Threat context | CVSS version/source, dated KEV and EPSS; do not treat missing values as zero |
| Business context | Criticality, exposure and verified operator-declared dependencies |
| Reconciliation | Separate raw observations and review cases; keep version/scope changes distinct |
| Decision | Human reviewer, owner, rationale, due date and acceptance review date |
| Retest | Same authorized scope, tool coverage and version; absence does not establish remediation |
| Reporting | Executive aliases and aggregates; raw reports only to authorized reviewers |
| Backup | Encrypted export, read-back verification, controlled storage, recovery drill |

For a concrete walkthrough, see the [synthetic executive report](../samples/EXECUTIVE_V061.md) and [free local exercise](../demo/README.md).
