#!/usr/bin/env python3
"""verify_proth_rows_certificate_audit.py

Zero-arg, stdlib-only, deterministic verifier for
  experimental/data/certificates/proth-rows/proth_rows.json
and its companion note
  experimental/notes/audits/proth_rows_certificate_audit.md

STATUS: AUDIT.  This is an independent adversarial arithmetic + definition
recomputation of the four certified Proth prime rows printed in
experimental/rs_mca_thresholds.tex (Table tab:prize-proth-rows,
Proposition prop:proth-row-check, and the appendix certificate/budget
tables).  It recomputes EVERY number the note and JSON packet report,
using Python big integers only (no numpy/sympy/sage, no floating point in
any pass/fail path), and checks:

  * the Proth form p = u*2^s + 1, u odd, u < 2^s;
  * the primality witness a0 with a0^((p-1)/2) == -1 (mod p), plus an
    independent search for the smallest such witness and a fixed-base
    Miller-Rabin cross-check (corroboration; the Proth witness is the
    actual deterministic primality PROOF);
  * bits(p), p < 2^256, and n | p-1;
  * the budget B = floor(p / 2^128), the target B* = floor(2^-128 * |F|)
    with |Gamma| = |F| = p, and B* == B;
  * the exact remainder r_p = p - B*2^128 in (0, 2^128);
  * the quadratic-boundary values F_{n,k}(B-1) and F_{n,k}(B) from the
    paper's own definition F_{n,k}(r) = r^2 - n(3r - (n-k)), the printed
    signs F_{n,k}(B-1) >= 0 > F_{n,k}(B), and that they locate the smaller
    root at r_quad = B-1;
  * the half-open safe set [0, B/n) with unsafe endpoint.

It does NOT re-derive the MCA staircase theorems; it audits the finite
arithmetic, the sign conditions, the field/endpoint bookkeeping, and the
primality certificates that the rows are promoted on.

Usage:
  python3 verify_proth_rows_certificate_audit.py                 # normal run
  python3 verify_proth_rows_certificate_audit.py --tamper-selftest
Exit 0 iff all checks pass (normal) / all tampers are caught (self-test).
"""

import copy
import json
import os
import sys
from math import isqrt

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir))
JSON_PATH = os.path.join(
    REPO, "experimental", "data", "certificates", "proth-rows", "proth_rows.json"
)
NOTE_PATH = os.path.join(
    REPO, "experimental", "notes", "audits", "proth_rows_certificate_audit.md"
)

TWO128 = 1 << 128
TWO256 = 1 << 256
K = 1 << 40  # k = 2^40 for every row
MR_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


# ---------------------------------------------------------------------------
# arithmetic helpers (exact big integers only)
# ---------------------------------------------------------------------------
def F_nk(n, k, r):
    """Paper definition F_{n,k}(r) = r^2 - n(3r - (n-k)); tex line 1840/3904."""
    return r * r - n * (3 * r - (n - k))


def r_quad_by_sign(n, k, hint):
    """Largest integer r with F_{n,k}(r) >= 0 (the smaller root's floor).

    Located by the F-sign condition, NOT by floor((3n-isqrt(D))/2): the
    naive integer-sqrt form overshoots by 1 for three of the four rows.
    Starts from the naive estimate `hint` and adjusts to the exact value.
    """
    r = hint
    while F_nk(n, k, r) < 0:
        r -= 1
    while F_nk(n, k, r + 1) >= 0:
        r += 1
    return r


def naive_rquad_isqrt(n, k):
    """The treacherous closed-form evaluation (informational only)."""
    D = n * (5 * n + 4 * k)
    return (3 * n - isqrt(D)) // 2


def is_probable_prime_mr(n, bases):
    """Deterministic (for fixed bases) Miller-Rabin cross-check."""
    if n < 2:
        return False
    for p in bases:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in bases:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def smallest_proth_witness(p, cap=200):
    """Smallest a in [2, cap] with a^((p-1)/2) == -1 (mod p), else None."""
    e = (p - 1) // 2
    for a in range(2, cap + 1):
        if pow(a, e, p) == p - 1:
            return a
    return None


# ---------------------------------------------------------------------------
# per-row check battery -- recomputes every reported number
# ---------------------------------------------------------------------------
def verify_row(row):
    """Return list of (check_name, ok) tuples for one row."""
    out = []

    def chk(name, ok):
        out.append((name, bool(ok)))

    rate = row["rate"]
    e = row["e"]
    n = row["n"]
    s = row["proth_s"]
    a0 = row["proth_witness_a0"]
    u = int(row["proth_u"])
    p = int(row["p"])
    B = row["B"]

    # --- field / dimension ---
    chk("n == 2^e", n == (1 << e))
    chk("k == 2^40", K == (1 << 40))
    # rho = k/n = 2^40 / 2^e = 1/2^(e-40); label matches
    chk("rate label matches k/n", rate == {41: "1/2", 42: "1/4", 43: "1/8", 44: "1/16"}[e])

    # --- Proth form ---
    chk("p == u*2^s + 1", p == u * (1 << s) + 1)
    chk("u odd", (u & 1) == 1)
    chk("u < 2^s", u < (1 << s))
    chk("u odd flag matches JSON", ((u & 1) == 1) == row["u_odd"])
    chk("u<2^s flag matches JSON", (u < (1 << s)) == row["u_lt_2s"])

    # --- primality certificate ---
    wit_ok = pow(a0, (p - 1) // 2, p) == p - 1
    chk("a0^((p-1)/2) == -1 mod p (Proth witness)", wit_ok)
    chk("witness flag matches JSON", wit_ok == row["witness_pow_equals_p_minus_1"])
    sm = smallest_proth_witness(p)
    chk("smallest witness == JSON smallest_witness_a", sm == row["smallest_witness_a"])
    chk("printed a0 is a valid witness (a0 in witness set)", pow(a0, (p - 1) // 2, p) == p - 1)
    mr = is_probable_prime_mr(p, MR_BASES)
    chk("Miller-Rabin fixed-base cross-check prime", mr)
    chk("MR flag matches JSON", mr == row["miller_rabin_fixed_bases"])

    # --- field arithmetic (PC2) ---
    chk("bits(p) == JSON bits_p", p.bit_length() == row["bits_p"])
    chk("p < 2^256", (p < TWO256) == True and row["p_lt_2_256"] == (p < TWO256))
    ndiv = (p - 1) % n == 0
    chk("n | p-1", ndiv and row["n_divides_p_minus_1"] == ndiv)

    # --- budget B and target B* ---
    B_rec = p // TWO128
    chk("B == floor(p/2^128)", B_rec == B)
    # B* = floor(eps* * |Gamma|), Gamma = F, |Gamma| = |F_p| = p, eps* = 2^-128
    B_star_rec = (p * 1) // TWO128  # floor(2^-128 * p)
    chk("B* == floor(2^-128 * |F|)", B_star_rec == row["B_star"])
    chk("B* == B (no ledger merge; |Gamma|=|F|=p)", B_star_rec == B_rec and row["B_equals_B_star"])

    # --- exact remainder ---
    r_p = p - B_rec * TWO128
    chk("r_p == p - B*2^128 == JSON remainder", r_p == int(row["remainder_r_p"]))
    chk("0 < r_p < 2^128", 0 < r_p < TWO128 and row["r_p_in_open_interval_0_2128"])

    # --- quadratic boundary F_{n,k} (the sign conditions being audited) ---
    fB1 = F_nk(n, K, B - 1)
    fB = F_nk(n, K, B)
    chk("F_{n,k}(B-1) == JSON value", fB1 == int(row["F_B_minus_1"]))
    chk("F_{n,k}(B) == JSON value", fB == int(row["F_B"]))
    chk("sign F_{n,k}(B-1) >= 0", fB1 >= 0 and row["sign_F_B_minus_1_ge_0"])
    chk("sign F_{n,k}(B) < 0", fB < 0 and row["sign_F_B_lt_0"])
    chk("sign pair locates root: F(B-1) >= 0 > F(B)", fB1 >= 0 > fB)
    # F strictly decreasing on [0,n]: F' = 2r-3n < 0, and B <= n
    chk("F' < 0 at B-1 and B (decreasing, boundary in range)",
        (2 * (B - 1) - 3 * n) < 0 and (2 * B - 3 * n) < 0 and B <= n)

    # --- r_quad located by sign == B-1 ---
    rq = r_quad_by_sign(n, K, naive_rquad_isqrt(n, K))
    chk("r_quad (F-sign locator) == B-1", rq == B - 1)
    chk("r_quad == JSON r_quad", rq == row["r_quad"])
    chk("r_quad == B-1 flag matches JSON", (rq == B - 1) == row["r_quad_equals_B_minus_1"])

    # --- endpoint convention: half-open safe set [0, B/n), endpoint unsafe ---
    chk("safe_set string == [0, B/n)", row["safe_set"] == f"[0, {B}/2^{e})")
    chk("endpoint unsafe flag", row["endpoint_unsafe"] is True)

    # --- compiler-window hypothesis that PRODUCES the safe set (hypothesis-visibility) ---
    # cor:prize-window-compiler needs 1 <= B <= min(r_rho+1, n-k-1); B=r_rho+1 so
    # the binding constraint is B <= n-k-1 (tangent floor applies at radius B).
    nk1 = n - K - 1
    chk("n-k-1 == JSON n_minus_k_minus_1", nk1 == row["n_minus_k_minus_1"])
    chk("compiler hypothesis 1 <= B <= n-k-1 holds",
        (1 <= B <= nk1) and row["compiler_hyp_1_le_B_le_nk1"])

    return out


def verify_packet(packet):
    """Return (results, rows_detail) where results is a flat list of (label, ok)."""
    results = []
    # global constants
    results.append(("global: constants.two_128 == 2^128", int(packet["constants"]["two_128"]) == TWO128))
    results.append(("global: constants.two_256 == 2^256", int(packet["constants"]["two_256"]) == TWO256))
    results.append(("global: constants.k == 2^40", packet["constants"]["k"] == K))
    rows_detail = []
    for row in packet["rows"]:
        row_res = verify_row(row)
        rows_detail.append((row["rate"], row_res))
        for name, ok in row_res:
            results.append((f"[rho={row['rate']}] {name}", ok))
    return results, rows_detail


# ---------------------------------------------------------------------------
# tamper self-test
# ---------------------------------------------------------------------------
def count_pass(packet):
    results, _ = verify_packet(packet)
    return sum(1 for _, ok in results if ok), len(results)


def tamper_selftest(packet):
    base_pass, base_total = count_pass(packet)
    if base_pass != base_total:
        print(f"  PRECONDITION FAIL: clean packet does not fully pass ({base_pass}/{base_total})")
        return False
    guarded = [
        ("rows.0.p", lambda pk: pk["rows"][0].__setitem__("p", str(int(pk["rows"][0]["p"]) + 2))),
        ("rows.0.proth_u", lambda pk: pk["rows"][0].__setitem__("proth_u", str(int(pk["rows"][0]["proth_u"]) + 2))),
        ("rows.0.proth_s", lambda pk: pk["rows"][0].__setitem__("proth_s", pk["rows"][0]["proth_s"] + 1)),
        ("rows.0.proth_witness_a0", lambda pk: pk["rows"][0].__setitem__("proth_witness_a0", pk["rows"][0]["proth_witness_a0"] + 2)),
        ("rows.1.B", lambda pk: pk["rows"][1].__setitem__("B", pk["rows"][1]["B"] + 1)),
        ("rows.1.remainder_r_p", lambda pk: pk["rows"][1].__setitem__("remainder_r_p", str(int(pk["rows"][1]["remainder_r_p"]) + 1))),
        ("rows.2.F_B_minus_1", lambda pk: pk["rows"][2].__setitem__("F_B_minus_1", str(int(pk["rows"][2]["F_B_minus_1"]) + 1))),
        ("rows.2.F_B", lambda pk: pk["rows"][2].__setitem__("F_B", str(int(pk["rows"][2]["F_B"]) + 1))),
        ("rows.3.bits_p", lambda pk: pk["rows"][3].__setitem__("bits_p", pk["rows"][3]["bits_p"] + 1)),
        ("rows.3.smallest_witness_a", lambda pk: pk["rows"][3].__setitem__("smallest_witness_a", pk["rows"][3]["smallest_witness_a"] + 1)),
        ("rows.0.safe_set", lambda pk: pk["rows"][0].__setitem__("safe_set", "[0, 1)")),
        ("global.two_128", lambda pk: pk["constants"].__setitem__("two_128", str(TWO128 + 1))),
    ]
    all_caught = True
    for label, mut in guarded:
        pk = copy.deepcopy(packet)
        mut(pk)
        npass, ntot = count_pass(pk)
        caught = npass < ntot
        all_caught = all_caught and caught
        print(f"  tamper {label:28s}  {'CAUGHT' if caught else 'MISSED!'}  ({npass}/{ntot})")
    return all_caught


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    selftest = "--tamper-selftest" in sys.argv
    print("=" * 78)
    print(" verify_proth_rows_certificate_audit  --  AUDIT (finite arithmetic + signs)")
    print(" source: experimental/rs_mca_thresholds.tex  (four certified Proth rows)")
    print("=" * 78)

    if not os.path.isfile(JSON_PATH):
        print(f"FATAL: packet JSON missing: {JSON_PATH}")
        return 1
    with open(JSON_PATH, "r", encoding="utf-8") as fh:
        packet = json.load(fh)
    if not os.path.isfile(NOTE_PATH):
        print(f"WARNING: companion note missing: {NOTE_PATH}")

    if selftest:
        print(" TAMPER SELF-TEST: each corrupted datum must drop the pass count")
        ok = tamper_selftest(packet)
        print("=" * 78)
        print(f" SELF-TEST RESULT: {'all tampers CAUGHT' if ok else 'A TAMPER WAS MISSED'}")
        return 0 if ok else 1

    results, rows_detail = verify_packet(packet)
    for rate, row_res in rows_detail:
        rp = sum(1 for _, ok in row_res if ok)
        print(f"  rho={rate:4s}  {rp}/{len(row_res)} row checks pass"
              + ("" if rp == len(row_res) else "   <-- FAILURE"))
        for name, ok in row_res:
            if not ok:
                print(f"        FAIL: {name}")
    npass = sum(1 for _, ok in results if ok)
    ntot = len(results)
    print("=" * 78)
    if npass == ntot:
        print(f"RESULT: PASS ({npass}/{ntot})")
        print(" All printed constants reproduce; Proth witnesses valid; signs")
        print(" F_{n,k}(B-1) >= 0 > F_{n,k}(B) confirmed; B=B*=floor(p/2^128);")
        print(" endpoint half-open [0,B/n). This audits arithmetic only, not the")
        print(" underlying MCA staircase theorems.")
        return 0
    print(f"RESULT: FAIL ({npass}/{ntot})")
    for name, ok in results:
        if not ok:
            print(f"  FAIL: {name}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
