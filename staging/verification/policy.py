"""Trusted route inventory and a small offline classifier for staging policy admission."""
import hashlib
import json
import math
from collections import Counter


# Labels describe the origin, and cannot be altered by the GitHub policy.
INVENTORY = {
    "/health": ("public", False, False),
    "/catalog": ("public", False, False),
    "/hours": ("public", False, False),
    "/team-notes": ("staff", False, True),
    "/admin": ("admin", True, True),
}
BASELINE = {"version": 1, "public_routes": ["/health", "/catalog"]}
ESSENTIAL = frozenset(BASELINE["public_routes"])

# Labeled examples of routes being granted anonymous access. Each training case
# describes a different synthetic resource; the staging route names are held out.
TRAINING = (
    ("opening-times", "public", False, False, 0), ("faq", "public", False, False, 0),
    ("storefront", "public", False, False, 0), ("contact-page", "public", False, False, 0),
    ("uptime", "public", False, False, 0), ("news", "public", False, False, 0),
    ("returns-guide", "public", False, False, 0), ("release-notes", "public", False, False, 0),
    ("staff-directory", "staff", False, True, 1), ("supplier-pricing", "staff", False, True, 1),
    ("support-inbox", "staff", False, True, 1), ("internal-invoices", "staff", False, True, 1),
    ("shift-changes", "staff", True, True, 1), ("ops-settings", "admin", True, True, 1),
    ("billing-console", "admin", True, True, 1), ("admin-events", "admin", False, True, 1),
)


class ExposureModel:
    """Laplace-smoothed categorical naive Bayes trained on the local labeled examples."""
    def __init__(self):
        self.counts = Counter()
        self.feature_counts = Counter()
        for _, tier, writes, internal, risk in TRAINING:
            self.counts[risk] += 1
            for i, value in enumerate((tier, writes, internal)):
                self.feature_counts[risk, i, value] += 1

    def score(self, features):
        logs = []
        for label in (0, 1):
            n = self.counts[label]
            logp = math.log((n + 1) / (len(TRAINING) + 2))
            for i, (value, classes) in enumerate(zip(features, (3, 2, 2))):
                logp += math.log((self.feature_counts[label, i, value] + 1) / (n + classes))
            logs.append(logp)
        return 1 / (1 + math.exp(logs[0] - logs[1]))


MODEL = ExposureModel()


def assess(policy):
    if (not isinstance(policy, dict) or set(policy) != {"version", "public_routes"}
            or type(policy["version"]) is not int or policy["version"] != 1):
        raise ValueError("invalid policy version or fields")
    routes = policy["public_routes"]
    if (not isinstance(routes, list) or len(routes) > len(INVENTORY)
            or any(type(p) is not str or p not in INVENTORY for p in routes)
            or len(routes) != len(set(routes))):
        raise ValueError("unknown or duplicate route")
    reasons = []
    scores = {}
    if not ESSENTIAL.issubset(routes):
        reasons.append("availability: required public route removed")
    for path in routes:
        risk = MODEL.score(INVENTORY[path])
        scores[path] = round(risk, 4)
        if risk >= 0.80:
            reasons.append(f"model: anonymous exposure of {path} (tier={INVENTORY[path][0]})")
        if path == "/admin":
            reasons.append("invariant: administration is never anonymous")
    return {"decision": "block" if reasons else "allow", "reasons": reasons, "scores": scores}


def blob_id(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def decode(data):
    def unique(pairs):
        obj = dict(pairs)
        if len(obj) != len(pairs):
            raise ValueError("duplicate JSON key")
        return obj
    return json.loads(data.decode("utf-8"), object_pairs_hook=unique)
