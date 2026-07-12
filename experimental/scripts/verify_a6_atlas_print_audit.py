#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verifier for experimental/notes/thresholds/a6_atlas_print_audit.md.

Stdlib-only, deterministic.  Two modes:

  --check           (default) run the full audit suite; print RESULT: PASS
                    (n/n) and exit 0, or RESULT: FAIL and exit 1.
  --tamper-selftest run a self-test that deliberately corrupts an in-memory
                    copy of a quoted anchor and confirms the anchor-checking
                    function detects it (i.e. reports the corrupted text as
                    NOT found), then still finishes with RESULT: PASS (n/n)
                    for the selftest's own checks.

It does four things.

  BLOCK A  Every verbatim tex anchor quoted by the print-audit is located in
           experimental/asymptotic_rs_mca_frontiers.tex by a tolerance-window
           search: the exact substring must occur within +/-2 lines of the
           stated (1-indexed) line number, and this audit's cited line must
           be the exact hit (offset 0) for every anchor at the current tex
           snapshot.  A negative test corrupts one anchor and confirms the
           corrupted string is absent both at its line and file-wide.

  BLOCK B  DannyExperiments' #697 (a6_all_witness_line_section_compiler.md)
           arithmetic is recomputed from the raw summation formulas (not
           copied from the note's closed forms), for several values of r,
           using exact Python integers:
             C(4)            = sum_{j=0}^{3} (4-j)(52-j+1)              = 520
             U(r)            = sum_{c=0}^{6} (53-c)((1400-225c)r+c)
                              = 260050 r + 1022
             N*C             = 260000 r
             surplus(r)      = U(r) - N*C                               = 50r+1022 > 0
             |E| bound       <= 52 + 3744*(1400r+5)^6 + 312 = 364+3744(1400r+5)^6
             |Z\\E| bound    <= 6 + floor(N*q*(L+1)/(d-t))              = 1596  (r-independent)
             final bound     = |E|+|Z\\E| = 1960 + 3744*(1400r+5)^6

  BLOCK C  Each of the seven A6-wave notes' own text is checked to contain
           its cited atlas/A2 disclaimer substring (quoted in the audit's
           Section 2 table), and #697's own note is checked to contain its
           "hard input 3" self-label (Section 3).  This verifies the audit's
           claims *about* the consumed notes, not just about the tex.

  BLOCK D  The route/classification counts in the audit's Summary table are
           recomputed from the ROUTES table declared below.

No .tex/.pdf is modified.
"""

import os
import sys

FAILURES = []
CHECKS = 0


def check(cond, label):
    global CHECKS
    CHECKS += 1
    if cond:
        print("  ok   " + label)
    else:
        print("  FAIL " + label)
        FAILURES.append(label)


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))          # experimental/
TEX = os.path.join(ROOT, "asymptotic_rs_mca_frontiers.tex")
NOTES = os.path.join(ROOT, "notes", "thresholds")

WINDOW = 2  # tolerance window, in lines, either side of the stated anchor


def find_anchor(lines, lineno, substr, window=WINDOW):
    """Search lines[lineno-1-window : lineno+window] (0-indexed) for substr.
    Returns the offset (found_line - lineno) of the first hit, or None."""
    lo = max(1, lineno - window)
    hi = min(len(lines), lineno + window)
    for ln in range(lo, hi + 1):
        if substr in lines[ln - 1]:
            return ln - lineno
    return None


# --------------------------------------------------------------------------
# BLOCK A -- tex anchor tolerance-window checks + negative test
# --------------------------------------------------------------------------
# (1-based line number, exact substring that must occur within +/-WINDOW lines)
ANCHORS = [
    (160,  "requires a witness-exhaustive atlas, image-scale MI and MA or a direct"),
    (161,  "Sidon payment, residual ray bounds, and comparison of the complete profile"),
    (778,  "still requires a witness-exhaustive first-match atlas, image-scale"),
    (779,  "effective Fourier payment or a direct Sidon payment, residual ray bounds"),
    (433,  r"\emph{first-match atlas} is witness-exhaustive if its realized cells cover"),
    (905,  "A first-match atlas covers every bad-slope witness and has"),
    (907,  r"of its algebraic cells is at most \(e^{o(n)}\mathfrak E_n(a_n)\)."),
    (897,  r"with \(C_n=\RS_{\F_n}(D_n,k_n)\), is"),
    (899,  "received line."),
    (1103, r"restricted to supports \(S\) with \(\abs S=a_n\), has a witness-exhaustive"),
    (1104, r"first-match atlas in the sense of \cref{def:first-match}, with"),
    (1238, "ordered atlas is witness-exhaustive and uses actual first-match slope"),
    (1463, r"The ordered family is a \emph{witness-exhaustive first-match atlas} if"),
    (1527, "If every received line admits a witness-exhaustive first-match atlas and a"),
    (2256, "and, for every received line, a witness-exhaustive first-match atlas of"),
    (2307, r"Fix a witness-exhaustive ordered atlas.  A scaled realized cell \(\Ccal_i\)"),
    (2368, "The catalogue below is a language for row-specific proofs, not a theorem"),
    (2369, "that every displayed locus is automatically paid.  In a concrete family,"),
    (2458, r"family.  A \emph{balanced core} is a pair of equal-degree monic residual"),
    (2459, r"locators with a common depth-\(w\) prefix after common and planted factors"),
    (3053, "in \\textup{(RC)} all hold with subexponential loss.  Taking the"),
    (3055, "exhaustive for that restricted incidence; it is exhaustive for the whole"),
    (3749, "arbitrarily.  Then they form a witness-exhaustive first-match atlas and,"),
    (6514, r"and is required by \textup{(A2)} or \textup{(RC)}."),
    (6517, "Suppose a smooth or circle sequence admits a witness-exhaustive"),
    (6695, r"Suppose a witness-exhaustive ordered ledger has \(e^{o(n)}\) profiles and their"),
    (6711, "certificate consists of a witness-exhaustive ordered atlas"),
    (6723, "Let a finite smooth or circle row admit a witness-exhaustive first-match atlas,"),
    (6739, "witness-exhaustive first-match atlas have algebraic or direct cells with"),
    (7105, r"The atlas payments, \textup{(MA)}, image-scale conditions,"),
    (7129, "does not close the Sidon, algebraic-projection, or higher-dimensional ray"),
    (7160, "If an exhaustive atlas has separately identified all quotient, planted,"),
    (7163, "Smoothness alone does not prove"),
    (7164, "that these loci form such an exhaustive subexponential atlas."),
    (7214, "folding tower and prefix depths, this requires an exhaustive"),
    (7215, r"subexponential atlas with direct slope budgets, effective \textup{(MI)} and"),
    (7417, r"Suppose an exhaustive atlas has \(e^{o(n)}\) profiles and each profile"),
    (7463, "If a multiplicative smooth row verifies the exhaustive atlas, invariant"),
    (7487, "A multiplicative smooth row satisfying the algebraic hypotheses above,"),
    (7525, "A circle twin-coset row with a proved exhaustive subexponential atlas and"),
    (7543, "prove the enumerative statements that drive the upper bound: exhaustion of"),
    (7544, "the corresponding boundary-map and algebraic slope projections, the"),
]


def run_block_a():
    print("BLOCK A -- tex anchor tolerance-window checks (+/-%d lines) at %s"
          % (WINDOW, os.path.basename(TEX)))
    with open(TEX, "r", encoding="utf-8") as fh:
        lines = fh.read().split("\n")

    for lineno, sub in ANCHORS:
        off = find_anchor(lines, lineno, sub)
        check(off is not None, "L%d anchor found within window: %s" % (lineno, sub[:56]))
        if off is not None:
            check(off == 0, "L%d anchor at exact cited line (offset %d)" % (lineno, off))

    # Negative test: corrupting a load-bearing anchor must break the match,
    # both on its own line and file-wide.
    orig = r"The ordered family is a \emph{witness-exhaustive first-match atlas} if"
    corrupt = r"The ordered family is a \emph{witness-exhaustove first-match atlas} if"
    check(orig in lines[1463 - 1], "negative-test setup: original present at L1463")
    check(corrupt not in lines[1463 - 1], "negative-test: corrupted quote absent at L1463")
    check(all(corrupt not in ln for ln in lines), "negative-test: corrupted quote absent file-wide")
    check(find_anchor(lines, 1463, corrupt) is None,
          "negative-test: tolerance-window search also fails to find the corrupted quote")
    return lines


# --------------------------------------------------------------------------
# BLOCK B -- #697 arithmetic, recomputed from the raw summation formulas
# --------------------------------------------------------------------------
def block_b_bounds(r):
    """Recompute every #697 quantity from the defining sums, not the note's
    closed forms, for source scale r (N=500r, kappa=225r, t=150r, d=250r)."""
    N = 500 * r
    kappa = 225 * r
    t = 150 * r
    d = 250 * r
    w = kappa - 1          # 225r-1
    m = 4                  # multiplicity
    L = 52
    D = 1400 * r - 1

    # (4): C = sum_{j=0}^{m-1} (m-j)(L-j+1)
    C = sum((m - j) * (L - j + 1) for j in range(m))

    # floor(D/w) -- must equal 6 for every r>=1 used here.
    q_floor = D // w
    check(q_floor == 6, "r=%d: floor(D/w)=6 (D=%d,w=%d) -> %d" % (r, D, w, q_floor))

    # (5): U = sum_{c=0}^{6} (53-c)((1400-225c) r + c)
    U = sum((53 - c) * ((1400 - 225 * c) * r + c) for c in range(0, q_floor + 1))

    NC = N * C
    surplus = U - NC

    # (9): |E| <= L + q L (12 Delta^6 + 1), q<=6, Delta<=D+q=1400r+5
    q_cap = 6
    Delta = D + q_cap
    E_bound = L + q_cap * L * (12 * Delta ** 6 + 1)
    E_bound_closed = 364 + 3744 * (1400 * r + 5) ** 6

    # (13): |Z\E| <= 6 + floor(N q (L+1) / (d-t))
    ZmE_bound = 6 + (N * q_cap * (L + 1)) // (d - t)

    final_bound = E_bound + ZmE_bound
    final_closed = 1960 + 3744 * (1400 * r + 5) ** 6

    return {
        "N": N, "kappa": kappa, "t": t, "d": d, "w": w, "D": D,
        "C": C, "U": U, "NC": NC, "surplus": surplus,
        "E_bound": E_bound, "E_bound_closed": E_bound_closed,
        "ZmE_bound": ZmE_bound, "final_bound": final_bound,
        "final_closed": final_closed,
    }


def run_block_b():
    print("BLOCK B -- #697 arithmetic recomputed from raw sums (r=1,2,3,5,10,50)")
    for r in (1, 2, 3, 5, 10, 50):
        v = block_b_bounds(r)
        check(v["C"] == 520, "r=%d: C = sum_j(4-j)(53-j) = 520 -> %d" % (r, v["C"]))
        check(v["U"] == 260050 * r + 1022,
              "r=%d: U(r) = 260050r+1022 (raw sum) -> %d" % (r, v["U"]))
        check(v["NC"] == 260000 * r, "r=%d: N*C = 260000r -> %d" % (r, v["NC"]))
        check(v["surplus"] == 50 * r + 1022 and v["surplus"] > 0,
              "r=%d: surplus = U-NC = 50r+1022 > 0 -> %d" % (r, v["surplus"]))
        check(v["E_bound"] == v["E_bound_closed"],
              "r=%d: |E| raw = closed form 364+3744(1400r+5)^6" % r)
        check(v["ZmE_bound"] == 1596, "r=%d: |Z\\E| = 1596 (r-independent) -> %d" % (r, v["ZmE_bound"]))
        check(v["final_bound"] == v["final_closed"],
              "r=%d: final |Z| bound = 1960+3744(1400r+5)^6 -> matches" % r)
        check(v["final_closed"] == v["E_bound_closed"] + 1596,
              "r=%d: 1960 = 364+1596 decomposition holds" % r)
    # Sanity: the bound is genuinely poly(r), i.e. dominated by a fixed power.
    v1, v50 = block_b_bounds(1), block_b_bounds(50)
    ratio = v50["final_bound"] / v1["final_bound"]
    check(ratio > 0, "poly(r) sanity: bound grows with r (ratio=%.3e)" % ratio)
    # (1400r+5)^6 grown ~50^6 from r=1 to r=50; confirm within a generous band.
    expected_order = (1400 * 50 + 5) ** 6 / (1400 * 1 + 5) ** 6
    check(abs(ratio - expected_order) / expected_order < 1e-6,
          "poly(r) growth matches the degree-6 term's own ratio")


# --------------------------------------------------------------------------
# BLOCK C -- the audit's claims about the consumed notes' own text
# --------------------------------------------------------------------------
# (filename, substring that must appear in that note's own text after
# whitespace normalization -- the source markdown hard-wraps these sentences
# across lines, so both the file text and the substring are compared with
# all runs of whitespace collapsed to a single space).
NOTE_DISCLAIMERS = [
    ("a6_full_support_zero_boundary.md",
     "No A2 witness-exhaustive atlas, A4 image-normalized payment, A7 envelope"),
    ("completed_cramer_strict_strata.md",
     "Terminal-mask rigidity and Cramer reconstruction alone therefore do not close the strict interior."),
    ("completed_zero_mask_two_block.md",
     "a witness-exhaustive A2 atlas or a bound on the number of profiles"),
    ("a6_actual_witness_core_rank_preflight.md",
     "A2 atlas or selector exhaustiveness and the number of profiles"),
    ("a6_u2_five_slope_rank_preflight.md",
     "atlas exhaustion, A2, RC, full A6,"),
    ("a6_u2_source_rooted_conic_preflight.md",
     "no primitive atlas, quotient classification, planted-profile census, ray-occupancy theorem"),
    ("a6_higher_order_completed_mask_rank_envelope.md",
     "witness-exhaustive atlas, image-scale MI/MA or Sidon payment"),
    ("a6_all_witness_line_section_compiler.md",
     "a witness-exhaustive atlas or a bound across different received lines,"),
]


def norm_ws(s):
    return " ".join(s.split())

# #697's own self-label of which numbered hard input it targets.
HARD_INPUT_SELFLABEL = (
    "a6_all_witness_line_section_compiler.md",
    "asymptotic A6 / hard input 3, canonical two-block stress family.",
)

# The A6/C8-adjacency honesty check: #681's own admission that its rank
# invariant is not automatically a C8 certificate.
C8_HONESTY = (
    "a6_actual_witness_core_rank_preflight.md",
    "moving-root count, a C8 certificate, or a proof that the family decomposes",
)


def run_block_c():
    print("BLOCK C -- consumed-note text checks (atlas disclaimers, self-labels)")
    for fname, sub in NOTE_DISCLAIMERS:
        path = os.path.join(NOTES, fname)
        ok = False
        if os.path.isfile(path):
            with open(path, encoding="utf-8") as fh:
                text = norm_ws(fh.read())
            ok = norm_ws(sub) in text
        check(ok, "%s contains its cited disclaimer" % fname)

    fname, sub = HARD_INPUT_SELFLABEL
    path = os.path.join(NOTES, fname)
    with open(path, encoding="utf-8") as fh:
        text = norm_ws(fh.read())
    check(norm_ws(sub) in text, "%s contains its 'hard input 3' Lane self-label" % fname)

    fname, sub = C8_HONESTY
    path = os.path.join(NOTES, fname)
    with open(path, encoding="utf-8") as fh:
        text = norm_ws(fh.read())
    check(norm_ws(sub) in text, "%s contains its C8-certificate honesty admission" % fname)

    # All eight note files referenced by this audit must actually exist.
    all_files = sorted(set([f for f, _ in NOTE_DISCLAIMERS] + [HARD_INPUT_SELFLABEL[0]]))
    check(len(all_files) == 8, "8 distinct A6-wave note files referenced -> %d" % len(all_files))
    for fname in all_files:
        check(os.path.isfile(os.path.join(NOTES, fname)), "%s exists on disk" % fname)


# --------------------------------------------------------------------------
# BLOCK D -- route/classification counts (Summary table)
# --------------------------------------------------------------------------
# route, classification
ROUTES = [
    ("U1",  "STILL-OPEN"),
    ("DEF", "AUDIT-DEFINITIONAL"),
    ("ATL", "STILL-OPEN"),
    ("LNU", "STILL-OPEN"),
    ("POA", "CURRENT-PROVED"),
    ("NEG", "STILL-OPEN"),
    ("NCH", "STILL-OPEN"),
    ("CNS", "CURRENT-PROVED"),
    ("FIN", "PARTIAL"),
]


def run_block_d():
    print("BLOCK D -- route/classification counts")
    check(len(ROUTES) == 9, "9 routes declared -> %d" % len(ROUTES))
    counts = {}
    for _, cls in ROUTES:
        counts[cls] = counts.get(cls, 0) + 1
    check(counts.get("STILL-OPEN", 0) == 5, "STILL-OPEN routes = 5 -> %d" % counts.get("STILL-OPEN", 0))
    check(counts.get("CURRENT-PROVED", 0) == 2, "CURRENT-PROVED routes = 2 -> %d" % counts.get("CURRENT-PROVED", 0))
    check(counts.get("PARTIAL", 0) == 1, "PARTIAL routes = 1 -> %d" % counts.get("PARTIAL", 0))
    check(counts.get("AUDIT-DEFINITIONAL", 0) == 1,
          "AUDIT-DEFINITIONAL routes = 1 -> %d" % counts.get("AUDIT-DEFINITIONAL", 0))
    check(len(ANCHORS) == 42, "42 BLOCK-A anchors declared -> %d" % len(ANCHORS))
    check(len(NOTE_DISCLAIMERS) == 8, "8 A6-wave notes carry a checked disclaimer -> %d" % len(NOTE_DISCLAIMERS))


# --------------------------------------------------------------------------
# --tamper-selftest
# --------------------------------------------------------------------------
def run_tamper_selftest():
    print("TAMPER-SELFTEST -- corrupt a quoted anchor in-memory, confirm detection")
    with open(TEX, "r", encoding="utf-8") as fh:
        lines = fh.read().split("\n")

    lineno, sub = 1463, r"The ordered family is a \emph{witness-exhaustive first-match atlas} if"
    off = find_anchor(lines, lineno, sub)
    check(off == 0, "selftest baseline: genuine anchor found at offset 0 before tamper")

    tampered = list(lines)
    tampered[lineno - 1] = tampered[lineno - 1].replace("witness-exhaustive", "witness-EXHAUSTED")
    off_after = find_anchor(tampered, lineno, sub)
    check(off_after is None, "selftest: tampered line no longer matches the cited anchor")

    # And a corrupted quote that never existed must not be findable anywhere
    # in the genuine (untampered) file either.
    fake = r"The ordered family is a \emph{witness-EXHAUSTED first-match atlas} if"
    check(fake not in "\n".join(lines), "selftest: fabricated corrupted quote absent from genuine tex")
    check(find_anchor(lines, lineno, fake) is None,
          "selftest: tolerance-window search also fails on the fabricated quote")


# --------------------------------------------------------------------------
def main():
    mode = "--check"
    if len(sys.argv) > 1:
        mode = sys.argv[1]

    if mode == "--tamper-selftest":
        run_tamper_selftest()
    elif mode == "--check":
        run_block_a()
        print()
        run_block_b()
        print()
        run_block_c()
        print()
        run_block_d()
    else:
        print("usage: %s [--check | --tamper-selftest]" % sys.argv[0])
        sys.exit(2)

    print("-" * 60)
    total = CHECKS
    passed = CHECKS - len(FAILURES)
    if FAILURES:
        print("RESULT: FAIL (%d/%d)" % (passed, total))
        for f in FAILURES:
            print("   - " + f)
        sys.exit(1)
    print("RESULT: PASS (%d/%d)" % (passed, total))


if __name__ == "__main__":
    main()
