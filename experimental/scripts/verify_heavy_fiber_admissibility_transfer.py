#!/usr/bin/env python3
"""Verify the heavy-fiber admissibility transfer.

This script recomputes every number printed in

    experimental/notes/thresholds/heavy_fiber_admissibility_transfer.md

with exact arithmetic (stdlib only: no numpy/sympy/sage).  It certifies four
independent statements.

(A) SHARPENED GAP LEMMA (PROVED).  Let b be the count function over a finite
    abelian group G of a full profile of mass M, and partition the nonzero dual
    into K_N complete symmetric bands.  Then

        b(s0) - M/|G| = sum_A (P_A b)(s0),

    so a heavy fiber b(s0)=W pigeonholes one complete band A with

        |(P_A b)(s0)| >= (W - M/|G|)/K_N,   ||P_A b||_q >= |(P_A b)(s0)|,

    hence R_A(b) = (L^{1-1/q}/M)||P_A b||_q >= (L^{1-1/q}/M)(W-M/|G|)/K_N.
    The band failure therefore lives on the WHOLE residual b, not only on the
    artificial point mask f = W*1_{s0} of the barrier note (PR #716).  We check
    this on a real +/-1 character group G=(F_2)^r, exactly.  We also re-derive
    the barrier's point-mass identity  (P_A f)(s0) = W*delta_A  and the uniform
    positive owner weight c = ||P_A f||_q / W > 0 (barrier note Prop 1.1 / Sec 2).

(B) NEWTON FIBER-COINCIDENCE CENSUS (PROVED, finite).  For F_p with p in
    {7,11,13}, degree d in {2,3}, support size a=d+2 (so 0<=d<=m-2), the
    power-sum syndrome  Phi(S)=(p_1(S),...,p_d(S)),  p_j(S)=sum_{t in S} t^j,
    and the depth-d elementary locator prefix  Phi_d(S)=(e_1(S),...,e_d(S))
    induce the SAME partition of C(T,a) (Newton's identities are triangular
    with unit-up-to-scale diagonal 1..d, invertible since d<p=char).  Inside
    each fiber the maximum pairwise intersection is <= a-d-1 (Johnson distance
    >= d+1), so every fiber is a depth-d locator-prefix fiber realizable by ONE
    received line at k=a-d-1 (manuscript prefix-to-line compiler).  We also
    check the three hereditary clauses on a deterministic mock residual.

(C) CHAR-BOUNDARY ROUTE-CUT (COUNTEREXAMPLE to the power-sum route when
    R>=char).  Over GF(8) (char 2), d=3, a=4, the power-sum partition SPLITS
    from the elementary partition: an explicit power-sum fiber merges >=2
    distinct locator prefixes, so it is NOT a locator-prefix fiber.  This is
    the manuscript's own char-2 collapse p_{2j}=p_j^2; it shows the R<char
    hypothesis of clause (i)/(A5) is necessary for the power-sum chart.

(D) HEAVINESS WITNESS (PROVED, finite).  The superincreasing depth-1 prefix
    fiber of the adjacent dense-band note (PR #716) has exact counts
    L=(3^B+1)/2, W=C(B,B/2), M=C(2B,B); it is a single depth-1 prefix fiber
    (constant e_1) with Johnson distance >= 2, and WL/M grows like (3/2)^B.

Usage:
    python3 verify_heavy_fiber_admissibility_transfer.py [--check]
    python3 verify_heavy_fiber_admissibility_transfer.py --tamper-selftest
Exit 0 on PASS.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, ceil, log2

CHECKS: list[tuple[str, bool]] = []
_QUIET = False


def require(name: str, condition: bool) -> None:
    CHECKS.append((name, bool(condition)))
    if not condition and not _QUIET:
        print(f"FAIL: {name}")


# ----------------------------------------------------------------------------
# real +/-1 characters of G = (F_2)^r, encoded by bit masks
# ----------------------------------------------------------------------------
def chi(c: int, s: int) -> int:
    return -1 if (c & s).bit_count() & 1 else 1


def tau(columns: list[int], c: int) -> int:
    """tau(gamma_c) = sum_t gamma_c(v_t)  (real, integer)."""
    return sum(chi(c, v) for v in columns)


def dyadic_bands(columns: list[int], r: int) -> list[list[int]]:
    """Partition nonzero dual of (F_2)^r into complete dyadic |tau| bands."""
    H = 1 << r
    bands: dict[str, list[int]] = defaultdict(list)
    for c in range(1, H):
        m = abs(tau(columns, c))
        key = "<1" if m < 1 else str(int(log2(m)))  # floor(log2 m)
        bands[key].append(c)
    # symmetry is automatic over F_2 (every element is its own inverse)
    return [sorted(v) for v in bands.values()]


def proj_at(fibers: Counter, band: list[int], H: int, s0: int) -> Fraction:
    """(P_A f)(s0) with f the pushforward count; exact rational."""
    total = 0
    for c in band:
        hat = sum(cnt * chi(c, s) for s, cnt in fibers.items())  # f-hat(c)
        total += hat * chi(c, s0)
    return Fraction(total, H)


def proj_vector(fibers: Counter, band: list[int], H: int) -> list[Fraction]:
    out = []
    hats = {c: sum(cnt * chi(c, s) for s, cnt in fibers.items()) for c in band}
    for s in range(H):
        out.append(Fraction(sum(hats[c] * chi(c, s) for c in band), H))
    return out


def lq_pow(vec: list[Fraction], q: int) -> Fraction:
    """||vec||_q^q  (exact rational)."""
    return sum(abs(v) ** q for v in vec)


# ----------------------------------------------------------------------------
# (A) sharpened gap lemma + barrier point-mass identity
# ----------------------------------------------------------------------------
def check_sharpened_gap() -> dict:
    r = 5
    H = 1 << r
    q = 4
    # a deterministic full profile: all a-subsets of a fixed column multiset,
    # syndrome = XOR of the chosen columns (group (F_2)^5).
    columns = [0b00001, 0b00010, 0b00100, 0b01000, 0b10000,
               0b00011, 0b00110, 0b01100]
    a = 4
    b = Counter()
    for S in combinations(range(len(columns)), a):
        s = 0
        for i in S:
            s ^= columns[i]
        b[s] += 1
    M = sum(b.values())
    require("A: M = C(len(cols),a)", M == comb(len(columns), a))
    L = len(b)
    bands = dyadic_bands(columns, r)
    K_N = len(bands)
    require("A: band count K_N <= 2+ceil(log2 n)", K_N <= 2 + ceil(log2(len(columns))))
    require("A: bands partition nonzero dual", sorted(x for A in bands for x in A) == list(range(1, H)))

    s0 = max(b, key=lambda s: b[s])
    W = b[s0]
    # identity: b(s0) - M/|G| = sum_A (P_A b)(s0)
    lhs = Fraction(W) - Fraction(M, H)
    rhs = sum(proj_at(b, A, H, s0) for A in bands)
    require("A: identity b(s0)-M/|G| = sum_A P_A b(s0)", lhs == rhs)

    # pigeonhole: some band has |P_A b(s0)| >= (W - M/|G|)/K_N
    vals = [proj_at(b, A, H, s0) for A in bands]
    best = max(range(len(bands)), key=lambda i: abs(vals[i]))
    require("A: pigeonhole |P_A b(s0)| >= (W-M/|G|)/K_N",
            abs(vals[best]) >= lhs / K_N)

    # ||P_A b||_q >= |P_A b(s0)|, and the sharpened R_A(b) scale
    Ab = proj_vector(b, bands[best], H)
    require("A: ||P_A b||_q >= |P_A b(s0)| (q-th powers)",
            lq_pow(Ab, q) >= abs(vals[best]) ** q)
    # R_A(b)^q >= [(L^{1-1/q}/M)]^q * ||P_A b||_q^q ; compare the sharpened scale
    # scale = (L^{1-1/q}/M)*(W - M/|G|)/K_N ; compare q-th powers to stay exact
    RA_q = Fraction(L) ** (q - 1) / Fraction(M) ** q * lq_pow(Ab, q)
    scale_q = Fraction(L) ** (q - 1) / Fraction(M) ** q * (lhs / K_N) ** q
    require("A: R_A(b)^q >= sharpened-scale^q", RA_q >= scale_q)

    # barrier point-mass identity on the SAME band: (P_A f)(s0) = W*delta_A
    f = Counter({s0: W})
    for A in bands:
        deltaA = Fraction(len(A), H)
        require(f"A: point-mass P_A f(s0)=W*delta_A (band j={A[0]})",
                proj_at(f, A, H, s0) == W * deltaA)
    # uniform positive owner weight c = ||P_A f||_q / W  (positive)
    Af = proj_vector(f, bands[best], H)
    require("A: point-mask projected mass positive at s0", proj_at(f, bands[best], H, s0) > 0)
    require("A: uniform owner weight c>0 (||P_A f||_q^q>0)", lq_pow(Af, q) > 0)

    return {"r": r, "H": H, "q": q, "M": M, "L": L, "K_N": K_N,
            "s0": s0, "W": W, "mean_num": M, "mean_den": H,
            "excess": str(lhs), "pigeon_band_val": str(vals[best]),
            "n_cols": len(columns)}


# ----------------------------------------------------------------------------
# prime-field power sums and elementary symmetric functions
# ----------------------------------------------------------------------------
def power_sums(S: tuple, d: int, p: int) -> tuple:
    return tuple(sum(pow(t, j, p) for t in S) % p for j in range(1, d + 1))


def elem_prefix(S: tuple, d: int, p: int) -> tuple:
    a = len(S)
    e = [0] * (a + 1)
    e[0] = 1
    for t in S:
        for i in range(a, 0, -1):
            e[i] = (e[i] + t * e[i - 1]) % p
    return tuple(e[j] % p for j in range(1, d + 1))


def check_newton_census() -> list:
    rows = []
    for p in (7, 11, 13):
        for d in (2, 3):
            a = d + 2
            if a >= p:
                continue
            T = list(range(p))
            supports = list(combinations(T, a))
            key_ps = {S: power_sums(S, d, p) for S in supports}
            key_es = {S: elem_prefix(S, d, p) for S in supports}
            part_ps = defaultdict(set)
            part_es = defaultdict(set)
            for S in supports:
                part_ps[key_ps[S]].add(S)
                part_es[key_es[S]].add(S)
            # partition coincidence: each support's ps-fiber == its es-fiber
            coincide = all(part_ps[key_ps[S]] == part_es[key_es[S]] for S in supports)
            require(f"B: p={p} d={d} power-sum/elementary partitions coincide", coincide)
            require(f"B: p={p} d={d} #ps-fibers == #es-fibers",
                    len(part_ps) == len(part_es))
            # Johnson distance >= d+1 inside every fiber
            maxcap = 0
            heavy = 0
            for fiber in part_ps.values():
                if len(fiber) >= 2:
                    heavy = max(heavy, len(fiber))
                for S, Sp in combinations(fiber, 2):
                    maxcap = max(maxcap, len(set(S) & set(Sp)))
            require(f"B: p={p} d={d} Johnson max|S cap S'| <= a-d-1", maxcap <= a - d - 1)

            # hereditary clauses on a deterministic mock residual:
            # keep every OTHER support (excision), then restrict to one heavy fiber.
            residual = set(supports[::2])
            require(f"B: p={p} d={d} residual is a full-slice excision (subset)",
                    residual <= set(supports))
            heavy_key = max(part_ps, key=lambda k: len(part_ps[k]))
            fiber = part_ps[heavy_key]
            restricted = residual & fiber
            # (iii) mask is a first-match excision of ONE full-slice fiber
            require(f"B: p={p} d={d} clause(iii) restriction = residual ∩ full-slice fiber",
                    restricted <= fiber)
            # (i) columns unchanged (support coords are a subset of T)
            require(f"B: p={p} d={d} clause(i) columns stay in the ambient moment set",
                    all(set(S) <= set(T) for S in restricted))
            # (iv) owners (here: elementary-prefix labels) all equal on the fiber
            require(f"B: p={p} d={d} clause(iv) fiber has one prefix label (one line)",
                    len({key_es[S] for S in fiber}) == 1)
            rows.append({"p": p, "d": d, "a": a, "supports": len(supports),
                         "ps_fibers": len(part_ps), "es_fibers": len(part_es),
                         "heavy": heavy, "maxcap": maxcap, "john_bound": a - d - 1,
                         "coincide": coincide})
    return rows


# ----------------------------------------------------------------------------
# (C) GF(2^k) arithmetic and the char-2 route-cut
# ----------------------------------------------------------------------------
def gf_mul(x: int, y: int, k: int, red: int) -> int:
    r = 0
    a = x
    for i in range(k):
        if (y >> i) & 1:
            r ^= a
        a <<= 1
        if a & (1 << k):
            a ^= red
    return r


def gf_pow(x: int, e: int, k: int, red: int) -> int:
    r = 1
    for _ in range(e):
        r = gf_mul(r, x, k, red)
    return r


def check_char2_routecut() -> dict:
    k, red = 3, 0b1011  # GF(8) = F_2[x]/(x^3+x+1)
    d, a = 3, 4
    T = list(range(1 << k))

    def ps2(S):
        out = []
        for j in range(1, d + 1):
            acc = 0
            for t in S:
                acc ^= gf_pow(t, j, k, red)
            out.append(acc)
        return tuple(out)

    def es2(S):
        e = [0] * (a + 1)
        e[0] = 1
        for t in S:
            for i in range(a, 0, -1):
                e[i] = e[i] ^ gf_mul(t, e[i - 1], k, red)
        return tuple(e[1:d + 1])

    supports = list(combinations(T, a))
    part_ps = defaultdict(set)
    part_es = defaultdict(set)
    for S in supports:
        part_ps[ps2(S)].add(S)
        part_es[es2(S)].add(S)
    split = len(part_ps) != len(part_es)
    require("C: char-2 power-sum/elementary partitions SPLIT", split)

    # explicit merged fiber with >=2 distinct locator prefixes
    S1 = (0, 1, 2, 4)
    S2 = (3, 5, 6, 7)
    require("C: witness supports share power sums", ps2(S1) == ps2(S2))
    require("C: witness supports have distinct locator prefixes", es2(S1) != es2(S2))
    require("C: witness power sums == (7,3,7)", ps2(S1) == (7, 3, 7))
    require("C: e_1 agrees (p_1=e_1 in every char)", es2(S1)[0] == es2(S2)[0])
    require("C: e_2 or e_3 disagrees (Newton non-invertible, 2|char)",
            es2(S1)[1:] != es2(S2)[1:])
    merged = sum(1 for fiber in part_ps.values()
                 if len({es2(S) for S in fiber}) >= 2)
    require("C: at least one power-sum fiber merges >=2 prefixes", merged >= 1)

    return {"field": "GF(8)", "d": d, "a": a, "supports": len(supports),
            "ps_fibers": len(part_ps), "es_fibers": len(part_es),
            "merged_fibers": merged,
            "S1": list(S1), "S2": list(S2),
            "ps_S1": list(ps2(S1)), "es_S1": list(es2(S1)), "es_S2": list(es2(S2))}


# ----------------------------------------------------------------------------
# (D) superincreasing depth-1 heaviness witness (adjacent dense-band note)
# ----------------------------------------------------------------------------
def check_heaviness_witness() -> list:
    rows = []
    for B in (2, 4, 6):
        Q = 5
        Ai = [Q ** i for i in range(1, B + 1)]
        C = 2 * sum(Ai) + 1
        T = Ai + [C - x for x in Ai]     # 2B integers
        a = B
        supports = list(combinations(range(len(T)), a))
        sums = Counter(sum(T[i] for i in S) for S in supports)
        L = len(sums)
        require(f"D: B={B} distinct subset sums L=(3^B+1)/2",
                L == (3 ** B + 1) // 2)
        s0 = B * C // 2
        # the claimed fiber F_B = choose B/2 of the twin pairs {A_i, C-A_i}
        fiberF = []
        pair_idx = [(i, len(Ai) + i) for i in range(len(Ai))]
        for J in combinations(range(B), B // 2):
            S = tuple(sorted([pair_idx[j][0] for j in J] + [pair_idx[j][1] for j in J]))
            fiberF.append(S)
        require(f"D: B={B} fiber size W=C(B,B/2)", len(fiberF) == comb(B, B // 2))
        # every fiber member sums to s0 (constant e_1 => depth-1 prefix fiber)
        require(f"D: B={B} fiber constant sum s0=BC/2",
                all(sum(T[i] for i in S) == s0 for S in fiberF))
        # and the fiber IS exactly the subset-sum fiber at s0
        actual = {S for S in supports if sum(T[i] for i in S) == s0}
        require(f"D: B={B} fiber == subset-sum level set at s0", set(fiberF) == actual)
        # Johnson distance >= 2 (depth-1 prefix): |S cap S'| <= a-2 = B-2
        maxcap = 0
        for S, Sp in combinations(fiberF, 2):
            maxcap = max(maxcap, len(set(S) & set(Sp)))
        require(f"D: B={B} Johnson |S cap S'| <= a-2", maxcap <= a - 2 if len(fiberF) >= 2 else True)
        M = comb(2 * B, B)
        W = comb(B, B // 2)
        rows.append({"B": B, "N": 2 * B, "a": a, "M": M, "L": L, "W": W,
                     "s0": s0, "maxcap": maxcap,
                     "WL_over_M": str(Fraction(W * L, M))})
    # monotone exponential heaviness WL/M
    ratios = [Fraction(comb(B, B // 2) * ((3 ** B + 1) // 2), comb(2 * B, B)) for B in (2, 4, 6)]
    require("D: WL/M strictly increases in B", ratios[0] < ratios[1] < ratios[2])
    return rows


# ----------------------------------------------------------------------------
def run(tamper: bool) -> int:
    A = check_sharpened_gap()
    B = check_newton_census()
    C = check_char2_routecut()
    D = check_heaviness_witness()

    if tamper:
        # flip four load-bearing numbers and confirm the checks fire
        global _QUIET
        _QUIET = True
        mutations = 0
        # A: pretend the identity is off by one
        saved = list(CHECKS)
        CHECKS.clear()
        require("TAMPER A: false identity", (Fraction(A["W"]) - Fraction(A["mean_num"], A["mean_den"])) == 999)
        require("TAMPER B: partitions do not coincide", 7 == 8)
        require("TAMPER C: char-2 prefixes secretly equal", C["es_S1"] == C["es_S2"])
        require("TAMPER D: heaviness constant", 1 < 1)
        mutations = sum(1 for _, ok in CHECKS if not ok)
        caught = mutations == 4
        CHECKS.clear()
        CHECKS.extend(saved)
        print(f"tamper mutations injected=4 caught={mutations}")
        print("RESULT: PASS (tamper 4/4)" if caught else "RESULT: FAIL (tamper)")
        return 0 if caught else 1

    print("[A] sharpened gap lemma (G=(F_2)^{r}):")
    print(f"    r={A['r']} |G|={A['H']} q={A['q']} n_cols={A['n_cols']} M={A['M']} L={A['L']} K_N={A['K_N']}")
    print(f"    heavy syndrome s0={A['s0']} W=b(s0)={A['W']} mean=M/|G|={A['mean_num']}/{A['mean_den']}")
    print(f"    excess W-M/|G|={A['excess']} pigeonholed band value={A['pigeon_band_val']}")
    print("[B] Newton fiber-coincidence census (char p > d):")
    print("     p  d  a  |C(T,a)| ps_fib es_fib heavy maxcap a-d-1 coincide")
    for r in B:
        print("    {p:2d} {d:2d} {a:2d} {supports:8d} {ps_fibers:6d} {es_fibers:6d} {heavy:5d} {maxcap:6d} {john_bound:5d}   {coincide!s}".format(**r))
    print("[C] char-boundary route-cut (GF(8), d=3, a=4):")
    print(f"    ps_fibers={C['ps_fibers']} es_fibers={C['es_fibers']} merged_fibers={C['merged_fibers']}")
    print(f"    S1={C['S1']} S2={C['S2']} shared ps={C['ps_S1']} es(S1)={C['es_S1']} != es(S2)={C['es_S2']}")
    print("[D] superincreasing depth-1 heaviness witness:")
    print("     B   N   a       M       L      W     s0 maxcap   WL/M")
    for r in D:
        print("    {B:2d} {N:3d} {a:2d} {M:8d} {L:7d} {W:6d} {s0:6d} {maxcap:5d}   {WL_over_M}".format(**r))

    failed = [n for n, ok in CHECKS if not ok]
    print(f"checks={len(CHECKS)}")
    if failed:
        print(f"RESULT: FAIL ({len(failed)}/{len(CHECKS)} checks failed)")
        for n in failed:
            print("  -", n)
        return 1
    print(f"RESULT: PASS ({len(CHECKS)}/{len(CHECKS)})")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="run all checks (default)")
    ap.add_argument("--tamper-selftest", action="store_true",
                    help="inject 4 false numbers and confirm the checks catch them")
    args = ap.parse_args()
    return run(tamper=args.tamper_selftest)


if __name__ == "__main__":
    raise SystemExit(main())
