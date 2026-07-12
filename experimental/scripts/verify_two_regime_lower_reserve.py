#!/usr/bin/env python3
"""Verify the superseding two-regime lower-reserve packet.

This zero-argument, stdlib-only wrapper reruns the 18-check realizability
verifier and adds seven packet checks for current source anchors, dependencies,
paste-ready formulas, non-promotion scope, and the complete JSON certificate.
It writes no files.
"""

import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "scripts" / "verify_pole_realizability.py"
NOTE = ROOT / "notes" / "thresholds" / "two_regime_lower_reserve_frontiers_packet.md"
TEX = ROOT / "asymptotic_rs_mca_frontiers.tex"
CERT = ROOT / "data" / "certificates" / "two_regime_lower_reserve.json"

checks = []


def check(name, condition):
    checks.append((name, bool(condition)))
    if not condition:
        print("FAIL:", name)


base = subprocess.run(
    [sys.executable, str(BASE)],
    text=True,
    capture_output=True,
    check=False,
)
check(
    "V1 base realizability verifier passes all 18 checks",
    base.returncode == 0 and "RESULT: PASS (18 checks)" in base.stdout,
)

tex = TEX.read_text(encoding="utf-8")
tex_lines = tex.splitlines()
note = NOTE.read_text(encoding="utf-8")
compact_note = "".join(note.split())

check(
    "V2 current introduction anchor is L715 after requested L714 insertion point",
    len(tex_lines) >= 715
    and tex_lines[714].strip() == r"\item For every challenge set,",
)
check(
    "V3 current SB2 anchor ends at L6228",
    len(tex_lines) >= 6228
    and r"P(a_-)>B^*" in tex_lines[6226]
    and tex_lines[6227].strip() == r"\]",
)
check(
    "V4 every source dependency used by the proof is present",
    all(
        label in tex
        for label in (
            r"\label{prop:exact-prefix-list}",
            r"\label{thm:collision-aware-pole}",
            r"\label{prop:universal-tangent-floor}",
            r"\label{cor:exact-deep-numerator}",
            r"\label{prop:prefix-rigidity-full}",
            r"\label{thm:unconditional-support-envelope-bracket}",
        )
    ),
)
check(
    "V5 note prints the combined reserve and both regime clauses",
    all(
        formula in compact_note
        for formula in (
            r"\max\{P(a),E(a)\}\leB_{C,\Gamma}^{\mathrm{MCA}}(a)\leU(a)",
            r"2a>n+k\quad\Longrightarrow\quadL(a)=P(a)=1",
            r"3(n-a)\len-k\quad\Longrightarrow\quadB_{C,\Gamma}^{\mathrm{MCA}}(a)=E(a)",
        )
    ),
)
check(
    "V6 packet is paste-ready at both anchors and declares no promotion",
    "after current L714" in note
    and "current L6228" in note
    and "No manuscript or PDF is changed by this packet." in note
    and "**Hard input served:** 5" in note
    and "| combined-reserve | PROVED |" in note
    and "| l3-disposition | AUDIT |" in note,
)

gated = re.search(
    r"deep-subset all n<=(\d+);\s+B1 rigidity (\d+) cases;\s+"
    r"B2 deep-P (\d+) cases;\s+D (\d+) cases",
    base.stdout,
)
zones = re.search(
    r"P>E useful=(\d+) \(all shallow non-deep\), P==E=(\d+), "
    r"P<E redundant=(\d+)",
    base.stdout,
)
metrics_ok = gated is not None and zones is not None
if metrics_ok:
    expected_certificate = {
        "schema": "rs-mca-two-regime-lower-reserve-v1",
        "status": "PROVED",
        "hard_input": 5,
        "source_commit": "ea4eb0784417ca5ab503a3c31a7eef6464ad100a",
        "claims": [
            {
                "id": "combined-reserve",
                "status": "PROVED",
                "statement": "max(P(a),E(a)) <= B_MCA(a) <= U(a)",
            },
            {
                "id": "upper-half-collapse",
                "status": "PROVED",
                "statement": "2a > n+k implies L(a)=P(a)=1",
            },
            {
                "id": "exact-deep",
                "status": "PROVED",
                "statement": "3(n-a) <= n-k implies B_MCA(a)=E(a)",
            },
            {
                "id": "l3-disposition",
                "status": "AUDIT",
                "statement": "the pole floor cannot overshoot in the deep range",
            },
        ],
        "anchors": {
            "intro_insert_after": 714,
            "intro_item_line": 715,
            "sb2_closing_line": 6228,
        },
        "verification": {
            "base_script": "experimental/scripts/verify_pole_realizability.py",
            "base_checks": 18,
            "packet_checks": 7,
            "grid": {
                "deep_subset_n_max": int(gated.group(1)),
                "rigidity_cases": int(gated.group(2)),
                "deep_p_cases": int(gated.group(3)),
                "all_reserve_cases": int(gated.group(4)),
            },
            "zone_census": {
                "pole_tighter_shallow": int(zones.group(1)),
                "equal": int(zones.group(2)),
                "tangent_tighter_or_pole_redundant": int(zones.group(3)),
            },
        },
    }
    certificate = json.loads(CERT.read_text(encoding="utf-8"))
else:
    expected_certificate = {}
    certificate = None
check(
    "V7 JSON certificate matches every recomputed field",
    metrics_ok and certificate == expected_certificate,
)

if base.returncode != 0:
    print(base.stdout)
    print(base.stderr, file=sys.stderr)

failed = [name for name, ok in checks if not ok]
if failed:
    print("RESULT: FAIL (%d/%d packet checks failed)" % (len(failed), len(checks)))
    sys.exit(1)

print("base_verifier=PASS checks=18")
print("source_anchor_checks=2")
print("dependency_checks=1")
print("packet_formula_scope_checks=2")
print("json_certificate_checks=1")
print("RESULT: PASS (7 packet checks; base verifier 18 checks)")
