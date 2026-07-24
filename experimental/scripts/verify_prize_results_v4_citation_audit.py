#!/usr/bin/env python3
"""Citation and source-pin verifier for experimental/proximity_prize_results_v4.tex.

Independent, deterministic, stdlib-only battery backing the bibliography /
source-pin audit note

    experimental/notes/audits/audit_prize_results_v4_citations_source_pins_v1.md

It re-derives every printed integer in the checked scope from first principles
or from the named in-repo source, reproduces the two orphan-citation and
digit-for-digit corridor findings, and checks that every pinned repository path
resolves at both the pin commit and the current source commit.

Scope note: this covers only the checked scope of the audit note.  It does NOT
recompute ChoComp26-attributed values (no in-repo source), the pull-request
linked citations, the ChoGF26 active-payment tables, or external ePrint theorem
numbers; those are the note's UNCHECKED list.

Usage:
    python3 verify_prize_results_v4_citation_audit.py                 # verbose battery
    python3 verify_prize_results_v4_citation_audit.py --check         # exit nonzero on any FAIL
    python3 verify_prize_results_v4_citation_audit.py --tamper-selftest  # inject one defect; must fail

Source commit:  f6a20fa39f8b3ebbf98056726c69133c82309e51
Pin commit:     5ecb9ab538a0a57dcb81018b17f32849049fb998
"""

import os
import re
import sys
import subprocess
from fractions import Fraction
from math import comb

# ---------------------------------------------------------------------------
# Repository geometry
# ---------------------------------------------------------------------------
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
V4 = os.path.join(ROOT, "experimental", "proximity_prize_results_v4.tex")
CORRIDOR_README = os.path.join(
    ROOT, "experimental", "data", "certificates",
    "corridor-unconditional-safe-edges", "README.md",
)
KB_PRIME_SOURCE = os.path.join(
    ROOT, "experimental", "Conjectures_and_Barriers_RS_MCA_v4_1.tex",
)
PIN_COMMIT = "5ecb9ab538a0a57dcb81018b17f32849049fb998"
SOURCE_COMMIT = "f6a20fa39f8b3ebbf98056726c69133c82309e51"
Q = 2 ** 128  # 2^{128} target denominator

# ---------------------------------------------------------------------------
# Expected constants (a --tamper-selftest run corrupts exactly one of these).
# ---------------------------------------------------------------------------
EXPECT = {
    "f17_floor": 6,
    "proth": [
        # (n, B = floor(p/2^128), explicit prime p)
        (2 ** 41, 389500552609,
         132540169958804033333249306710494641010898987122689),
        (2 ** 42, 1210584858040,
         411940680852499481698306614369841346700408394874881),
        (2 ** 43, 2879806199253,
         979947269755402568812854322316630667196565607677953),
        (2 ** 44, 6233898019554,
         2121285573237585848299875619011192262679065433997313),
    ],
    "lp_num": 1031427641435096867222903646984,
    "lp_den": 61254010871010657240949,
    "lp_floor": 16838532,
    "lp_decimal_prefix": "16838532.3143506",
    "m31_list_budget": 16777215,
    "cubic_cell": 16760701,
    "cw_two24": 16777216,  # 2^24
    "owner_star": 59838,
    "owner_branch": 63684220,
    "owner_core": 440837,
    "cell_N": 1053558,
    "kb_prime": 2130706433,          # p_KB = 2^31 - 2^24 + 1 (read back from source)
    "kb_budget": 274980728111395087,  # floor(p_KB^6 / 2^128)
    "kb_paid": 981104,
    "kb_reserve": 274980728110413983,
    "corridor": [512, 663, 769, 1092724518963, 1415997755216, 1644686143216],
    "orphans": {"CS25", "GG25"},
    "dropped_keys": ["RepoLog26", "BuarKBQ26", "Bua26b"],
    "n_pins": 18,
    "cap_edges": [(Fraction(1, 4), Fraction(1, 512), Fraction(383, 512)),
                  (Fraction(1, 8), Fraction(1, 512), Fraction(447, 512)),
                  (Fraction(1, 16), Fraction(1, 1024), Fraction(959, 1024))],
    # F7: the Acknowledgements name a mechanism the manuscript no longer uses.
    "attribution_sentence": ("Contributor-specific results are attributed in "
                             "theorem headings and bibliography entries"),
    "contributor_names": ["Buar", "Hughes", "Danny", "Avdeev", "Zafiria",
                          "Latif", "Hart"],
    "n_named_headings": 0,
    "n_source_lines": 33,
    "n_named_source_lines": 12,
    "v4_blob": "1abf81fae2fa9754a3cb04a9563b39a3d752716e",
}

# Theorem-class environments whose optional-argument brackets carry the heading.
HEADING_RE = re.compile(
    r"\\begin\{(?:theorem|proposition|lemma|corollary|conjecture)\}\[[^]]*\]"
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def is_probable_prime(n, witnesses=(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)):
    """Deterministic Miller-Rabin for the sizes here (fixed small-base set)."""
    if n < 2:
        return False
    for p in witnesses:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in witnesses:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def ceil_div(a, b):
    return -(-a // b)


def git_object_exists(commit, path):
    try:
        r = subprocess.run(["git", "cat-file", "-e", f"{commit}:{path}"],
                           cwd=ROOT, capture_output=True)
        return r.returncode == 0
    except Exception:
        return False


def git_blob_sha(*args):
    """`git <args>` returning a single blob sha, or None when git is unavailable."""
    try:
        r = subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True)
        return r.stdout.decode().strip() if r.returncode == 0 else None
    except Exception:
        return None


def parse_corridor_readme(text):
    """The Habock column is the only bold column in the safe-edge table."""
    return [int(x.replace(",", "")) for x in re.findall(r"\*\*([\d,]+)\s*\(", text)]


def parse_v4_corridor(text):
    rows = []
    for line in text.splitlines():
        m = re.match(r"\s*(?:length-\$1024\$|prize scale).*?&.*?&\s*\$?(\d+)\$?\s*&", line)
        if m:
            rows.append(int(m.group(1)))
    return rows


def cite_and_bibitem_keys(text):
    bibstart = text.find(r"\begin{thebibliography}")
    body, bib = text[:bibstart], text[bibstart:]
    cited = set()
    for m in re.finditer(r"\\cite[a-zA-Z]*(?:\[[^\]]*\])?\{([^}]*)\}", body):
        for k in m.group(1).split(","):
            cited.add(k.strip())
    defined = [m.group(1).strip()
               for m in re.finditer(r"\\bibitem(?:\[[^\]]*\])?\{([^}]*)\}", bib)]
    return cited, defined


def extract_pin_paths(text):
    return re.findall(r"blob/" + PIN_COMMIT + r"/([^}]+)\}", text)


def read_kb_prime(text):
    m = re.search(r"p_\{\\rm KB\}=2\^\{31\}-2\^\{24\}\+1=(\d+)", text)
    return int(m.group(1)) if m else None


# ---------------------------------------------------------------------------
# The battery.  Each check appends (name, passed, detail).
# ---------------------------------------------------------------------------
def run_battery():
    results = []

    def add(name, passed, detail=""):
        results.append((name, bool(passed), detail))

    v4 = read(V4)

    # 1. exact F_{17^32} threshold
    got = (17 ** 32) // Q
    add("F17 floor(17^32/2^128)==6", got == EXPECT["f17_floor"], f"got {got}")
    add("F17 safe set [0,6/512) printed in v4", "[0,6/512)" in v4)

    # 2. four Proth rows: floor, primality, n | p-1
    for n, B, p in EXPECT["proth"]:
        add(f"Proth n={n}: floor(p/2^128)={B}", p // Q == B, f"got {p // Q}")
        add(f"Proth n={n}: p is prime (Miller-Rabin)", is_probable_prime(p))
        add(f"Proth n={n}: n divides p-1", (p - 1) % n == 0)
        add(f"Proth n={n}: prime printed in v4", str(p) in v4)

    # 3. Delsarte LP optimum
    num, den = EXPECT["lp_num"], EXPECT["lp_den"]
    add("LP optimum floor==16838532", num // den == EXPECT["lp_floor"],
        f"got {num // den}")
    add("LP optimum decimal prefix 16838532.3143506",
        f"{num / den:.7f}".startswith(EXPECT["lp_decimal_prefix"]),
        f"got {num / den:.10f}")
    add("LP optimum > M31 list budget 16777215",
        num > EXPECT["m31_list_budget"] * den)
    add("LP optimum decimal printed in v4", EXPECT["lp_decimal_prefix"] in v4)

    # 4. cubic-cell bound below 2^24
    add("cubic cell 16760701 < 2^24 (16777216)",
        EXPECT["cubic_cell"] < EXPECT["cw_two24"])
    add("cubic cell inequality printed in v4",
        str(EXPECT["cubic_cell"]) in v4 and str(EXPECT["cw_two24"]) in v4)

    # 5. owner-star concentration
    os_val = ceil_div(EXPECT["owner_branch"] * comb(EXPECT["owner_core"], 8),
                      comb(EXPECT["cell_N"], 8))
    add("owner-star ceil(63684220*C(440837,8)/C(1053558,8))==59838",
        os_val == EXPECT["owner_star"], f"got {os_val}")

    # 6. KoalaBear reserve (prime read back from repo source, not hardcoded blind)
    kb_src = read(KB_PRIME_SOURCE)
    kb_read = read_kb_prime(kb_src)
    add("KB prime read from Conjectures source == 2^31-2^24+1",
        kb_read == EXPECT["kb_prime"] == 2 ** 31 - 2 ** 24 + 1, f"read {kb_read}")
    if kb_read:
        q6 = kb_read ** 6
        add("KB floor(p^6/2^128)==274980728111395087",
            q6 // Q == EXPECT["kb_budget"], f"got {q6 // Q}")
        add("KB reserve floor(p^6/2^128)-981104==274980728110413983",
            q6 // Q - EXPECT["kb_paid"] == EXPECT["kb_reserve"],
            f"got {q6 // Q - EXPECT['kb_paid']}")
        add("KB reserve printed in v4", str(EXPECT["kb_reserve"]) in v4)

    # 7. universal-cap terminal edges 1-rho-2^-9 / 2^-10
    for rho, eps, edge in EXPECT["cap_edges"]:
        add(f"cap edge 1-{rho}-{eps}=={edge}", 1 - rho - eps == edge)
        add(f"cap edge {edge.numerator}/{edge.denominator} printed in v4",
            f"{edge.numerator}/{edge.denominator}" in v4
            or f"{edge.numerator}/2^" in v4)

    # 8. corridor six integers: README bold == v4 tab:corridor == hardcoded expected
    readme_vals = parse_corridor_readme(read(CORRIDOR_README))
    v4_vals = parse_v4_corridor(v4)
    add("corridor: README bold column == expected six",
        readme_vals == EXPECT["corridor"], f"README {readme_vals}")
    add("corridor: v4 tab:corridor == expected six",
        v4_vals == EXPECT["corridor"], f"v4 {v4_vals}")
    add("corridor: README == v4 (digit-for-digit)", readme_vals == v4_vals)

    # 9. citation hygiene: every \cite resolves; exactly CS25,GG25 orphaned
    cited, defined = cite_and_bibitem_keys(v4)
    orphans = {k for k in defined if k not in cited}
    dangling = {k for k in cited if k not in defined}
    add("no dangling \\cite (every cite has a \\bibitem)", dangling == set(),
        f"dangling {sorted(dangling)}")
    add("orphan \\bibitem set == {CS25, GG25}", orphans == EXPECT["orphans"],
        f"orphans {sorted(orphans)}")

    # 10. deliberately dropped keys are fully absent
    for k in EXPECT["dropped_keys"]:
        add(f"dropped key '{k}' absent from v4", k not in v4)

    # 11. eighteen blob-pins resolve at BOTH the pin commit and the source commit
    paths = extract_pin_paths(v4)
    add(f"pin count == {EXPECT['n_pins']}", len(paths) == EXPECT["n_pins"],
        f"found {len(paths)}")
    all_pin_ok = True
    for p in paths:
        at_pin = git_object_exists(PIN_COMMIT, p)
        at_src = git_object_exists(SOURCE_COMMIT, p)
        if not (at_pin and at_src):
            all_pin_ok = False
            add(f"pin path resolves at both commits: {p}", False,
                f"pin={at_pin} source={at_src}")
    add("all pinned paths resolve at pin commit AND source commit", all_pin_ok)

    # 12. the v4 text read above IS the blob pinned at the source commit, so
    #     every content check in this battery is a check against pinned content.
    on_disk_blob = git_blob_sha("hash-object", V4)
    pinned_blob = git_blob_sha(
        "rev-parse", f"{SOURCE_COMMIT}:experimental/proximity_prize_results_v4.tex")
    add("v4 read here == v4 blob pinned at the source commit",
        on_disk_blob is not None and on_disk_blob == EXPECT["v4_blob"]
        and (pinned_blob is None or pinned_blob == EXPECT["v4_blob"]),
        f"on-disk {on_disk_blob} pinned {pinned_blob}")

    # 13. F7: the Acknowledgements name an attribution mechanism v4 dropped.
    names = EXPECT["contributor_names"]
    add("acknowledgements attribution sentence present in v4",
        EXPECT["attribution_sentence"] in v4)
    headings = HEADING_RE.findall(v4)
    named_headings = [h for h in headings if any(n in h for n in names)]
    add(f"contributor names in theorem-class headings == "
        f"{EXPECT['n_named_headings']}",
        len(named_headings) == EXPECT["n_named_headings"],
        f"found {len(named_headings)}: {named_headings[:3]}")
    source_lines = [ln for ln in v4.splitlines() if "\\source{" in ln]
    add(f"\\source lines == {EXPECT['n_source_lines']}",
        len(source_lines) == EXPECT["n_source_lines"],
        f"found {len(source_lines)}")
    named_sources = [ln for ln in source_lines if any(n in ln for n in names)]
    add(f"\\source lines naming a contributor == "
        f"{EXPECT['n_named_source_lines']}",
        len(named_sources) == EXPECT["n_named_source_lines"],
        f"found {len(named_sources)}")

    return results


# ---------------------------------------------------------------------------
# Drivers
# ---------------------------------------------------------------------------
def report(results, verbose):
    npass = sum(1 for _, ok, _ in results if ok)
    nfail = len(results) - npass
    if verbose:
        for name, ok, detail in results:
            tag = "PASS" if ok else "FAIL"
            extra = "" if (ok or not detail) else f"   [{detail}]"
            print(f"  [{tag}] {name}{extra}")
        print(f"\nsummary: {npass} passed, {nfail} failed, {len(results)} total")
    else:
        for name, ok, detail in results:
            if not ok:
                print(f"  [FAIL] {name}   [{detail}]")
        print(f"summary: {npass}/{len(results)} passed")
    return nfail


def main(argv):
    mode = argv[1] if len(argv) > 1 else "--run"

    if mode == "--tamper-selftest":
        # Inject one defect at a time, each in isolation, and confirm the
        # battery catches every one.  Each injection targets a different check
        # family: exact arithmetic, source-pin integrity, and the F7
        # attribution-mechanism group.
        injections = [
            ("owner_star", 59838, 59839),
            ("v4_blob", EXPECT["v4_blob"], "0" * 40),
            ("n_named_headings", 0, 1),
            ("n_source_lines", 33, 32),
            ("n_named_source_lines", 12, 11),
            ("attribution_sentence", EXPECT["attribution_sentence"],
             "Contributor-specific results are attributed by carrier pigeon"),
        ]
        missed = []
        for key, good, bad in injections:
            print(f"[tamper-selftest] injecting defect: {key} -> {bad!r}")
            EXPECT[key] = bad
            nfail = report(run_battery(), verbose=False)
            EXPECT[key] = good
            if nfail == 0:
                missed.append(key)
                print(f"[tamper-selftest] ERROR: defect in {key} was NOT caught.")
        if missed:
            print(f"[tamper-selftest] ERROR: uncaught injections: {missed}")
            return 2
        print(f"[tamper-selftest] PASS: battery caught all "
              f"{len(injections)} injected defects; exiting nonzero as designed.")
        return 1

    verbose = (mode != "--check")
    results = run_battery()
    nfail = report(results, verbose=verbose)
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
