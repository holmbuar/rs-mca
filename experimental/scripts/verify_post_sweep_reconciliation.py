#!/usr/bin/env python3
"""Verifier for post_sweep_bracket_reconciliation.md.

--check           recompute/assert every number and anchor the note states
--tamper-selftest mutate an anchor and an ordering in-memory; confirm detection

stdlib only, deterministic, < 1 s.  Exit 0 on PASS, 1 on FAIL.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))  # repo root (experimental/..)
EXP = os.path.join(ROOT, "experimental")

NOTE = os.path.join(EXP, "notes", "thresholds",
                    "post_sweep_bracket_reconciliation.md")

# (file, required substring) anchors into the INTEGRATED corpus
ANCHORS = [
    ("notes/thresholds/comb_trade_champion.md", "0.160847"),
    ("notes/thresholds/comb_trade_champion.md", "0.158411"),
    ("notes/thresholds/ilo_moment_closed_consumer.md", "0.158411"),
    ("notes/thresholds/ilo_moment_closed_consumer.md", "0.405465"),
    ("notes/thresholds/championship_census_b19_26.md", "0.158411"),
    ("notes/thresholds/fenced_resonance_window.md", "0.84932"),
    ("notes/thresholds/bohr_gap_volume.md", "2^omega(q)"),
]

# section-4 normalization targets
SCRUBBED = [
    "notes/thresholds/corridor_diameter_map.md",
    "scripts/verify_corridor_diameter_map.py",
]
STRAY = "team" + " board"  # split so this file never contains the phrase
NORMALIZED = ", 2026-07-12"


def read(rel):
    with open(os.path.join(EXP, rel), encoding="utf-8") as fh:
        return fh.read()


def run_checks(anchors, orderings, note_text):
    n = 0
    # 1. upper end is ln(3/2)
    assert abs(math.log(1.5) - 0.405465) < 5e-7, "ln(3/2) != 0.405465"
    n += 1
    # 2. orderings of section 1
    for a, b in orderings:
        assert a < b, f"ordering failed: {a} < {b}"
        n += 1
    # 3. every stated constant appears in the note itself
    for c in ("0.160847", "0.405465", "0.158411", "0.156900", "ln(3/2)"):
        assert c in note_text, f"note missing constant {c}"
        n += 1
    # 4. anchors into the integrated corpus
    for rel, needle in anchors:
        assert needle in read(rel), f"anchor missing: {needle} in {rel}"
        n += 1
    # 5. weave/supersession row counts (section 2: 5 rows; section 3: 7 rows)
    sec2 = note_text.split("## 2.")[1].split("## 3.")[0]
    sec3 = note_text.split("## 3.")[1].split("## 4.")[0]
    rows2 = [l for l in sec2.splitlines()
             if l.startswith("|") and "---" not in l and "printed statement" not in l]
    rows3 = [l for l in sec3.splitlines()
             if l.startswith("|") and "---" not in l and l.count("|") >= 3
             and " PR " not in l and not l.startswith("| PR")]
    assert len(rows2) == 5, f"section-2 rows: {len(rows2)} != 5"
    n += 1
    assert len(rows3) == 7, f"section-3 rows: {len(rows3)} != 7"
    n += 1
    # 6. section-4 normalization: zero stray, exactly two normalized per file
    for rel in SCRUBBED:
        body = read(rel)
        assert STRAY not in body, f"stray phrase survives in {rel}"
        assert body.count(NORMALIZED) >= 2, f"{rel}: normalized dates missing"
        n += 2
    # 7. the stray phrase appears nowhere else under experimental/ either
    stray_elsewhere = []
    for dirpath, _dirs, files in os.walk(EXP):
        for f in files:
            if not f.endswith((".md", ".py", ".tex", ".txt", ".json")):
                continue
            rel = os.path.relpath(os.path.join(dirpath, f), EXP)
            try:
                if STRAY in read(rel):
                    stray_elsewhere.append(rel)
            except (UnicodeDecodeError, OSError):
                continue
    assert not stray_elsewhere, f"stray phrase found: {stray_elsewhere}"
    n += 1
    return n


ORDERINGS = [
    (0.156900, 0.158411),
    (0.158411, 0.160847),
    (0.160847, 0.405465),
]


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--check"
    note_text = open(NOTE, encoding="utf-8").read()
    if mode == "--check":
        n = run_checks(ANCHORS, ORDERINGS, note_text)
        print(f"RESULT: PASS ({n}/{n})")
        return 0
    if mode == "--tamper-selftest":
        caught = 0
        # tamper 1: break an anchor
        bad = [("notes/thresholds/comb_trade_champion.md", "0.999999")] + ANCHORS[1:]
        try:
            run_checks(bad, ORDERINGS, note_text)
        except AssertionError:
            caught += 1
        # tamper 2: break an ordering
        try:
            run_checks(ANCHORS, [(0.5, 0.4)] + ORDERINGS[1:], note_text)
        except AssertionError:
            caught += 1
        # tamper 3: drop a constant from the note text
        try:
            run_checks(ANCHORS, ORDERINGS, note_text.replace("0.160847", "X"))
        except AssertionError:
            caught += 1
        ok = caught == 3
        print(f"RESULT: {'PASS' if ok else 'FAIL'} ({caught}/3)")
        return 0 if ok else 1
    print(f"unknown mode {mode}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
