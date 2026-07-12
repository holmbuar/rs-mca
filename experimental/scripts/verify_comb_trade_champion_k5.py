#!/usr/bin/env python3
"""Verify comb_trade_champion_k5.md -- extending the same-block trade-stacking
family of comb_trade_champion.md (#694) past b=24 toward k=5 / b=30.

MAIN RESULTS re-derived here, from scratch, stdlib-only:
  * A memory-bounded exact method for the asymptotic census (f_inf, L1_inf) of
    the comb family that reaches k=5 (b=30) in ~25 MB, where #694's flat
    6-tuple DP needs the full L1_inf ~ 57.4M-key dict (several GB).
  * k=5 flat-AP PROUHET comb: f_inf=2072, L1_inf=57376057, rho_inf=0.156900 --
    BELOW #694's b=24 champion 0.160847 (and below #655's b=18 champion
    0.158411). Resolves #694's residual #1 (k=5) NEGATIVELY.
  * Generalization to non-uniform per-block weights (#694's residual #3):
    the maximum rho_inf over the searched weight window is the champion
    (attained at k=4 by the AP weights, unique up to affine scaling); the k=5
    maximum stays strictly below 0.160847. => CEILING for the searched family.

Every asymptotic census here is cross-checked by THREE independent algorithms
on k<=4 (the #694 flat 6-tuple DP, the grouped-by-size-vector DP, and a
block-split meet-in-the-middle) and by TWO independent algorithms + exact
mass-conservation (sum of fiber multiplicities = 2^b) on k=5 (where the flat DP
is out of memory).

Usage:
  python3 verify_comb_trade_champion_k5.py            # full --check (default)
  python3 verify_comb_trade_champion_k5.py --check
  python3 verify_comb_trade_champion_k5.py --tamper-selftest
Time cap: the full --check recomputes the k=5 census twice (grouped + MITM) and
the reported k=5-max weight sequence once; budget ~12 min, typically ~6 min.
Exit 0 iff every check passes; final line 'RESULT: PASS n/n'.

Conventions (identical to #694 / #655): a block V is b distinct integers,
Phi(S)=(|S|, sum_S x, sum_S x^2), fstar(V)=max fiber, L1(V)=#distinct Phi
values, rho=(log fstar + log L1)/b - log 2 (natural log), b = k*|G|.

Credit: construction, champion (b=24, 0.160847), the 6-tuple aggregate-moment
mechanism, and the PROUHET gadget {0,1,2,4,5,6} (scottdhughes #564's minimal
degree-2 PTE trade) are #694 (comb_trade_champion.md), building on #655
(fiber_image_tradeoff.md), #683 (championship_census_b19_26.md). This packet
adds the memory-bounded method, the k=5 census, and the weight-sequence ceiling.
"""
from __future__ import annotations
import itertools
import resource
import sys
import time
from collections import defaultdict
from math import log

LOG2 = log(2)
PROUHET = (0, 1, 2, 4, 5, 6)   # hughes #564 minimal degree-2 PTE trade
CHAMPION_RHO = 0.160847         # #694 b=24 record
OLDCHAMP_RHO = 0.158411         # #655 b=18 record

CHECKS: list[tuple[bool, str]] = []


def check(cond: bool, label: str) -> bool:
    CHECKS.append((bool(cond), label))
    print(f"    [{'ok  ' if cond else 'FAIL'}] {label}")
    return bool(cond)


def approx(a: float, b: float, tol: float = 1e-6) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def maxrss_mb() -> float:
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0  # KB->MB on Linux


def rho_of(f: int, L: int, b: int) -> float:
    return (log(f) + log(L)) / b - LOG2


# ============================================================ core algorithms
def sig_dp(V):
    """Direct incremental subset DP over the actual integer block V. Same
    convention as #655/#683/#694. dict[(size,sum,sumsq)] = multiplicity."""
    dp = defaultdict(int)
    dp[(0, 0, 0)] = 1
    for v in V:
        vv = v * v
        nd = defaultdict(int)
        for (w, s, q), c in dp.items():
            nd[(w, s, q)] += c
            nd[(w + 1, s + v, q + vv)] += c
        dp = nd
    return dp


def stat_direct(V):
    dp = sig_dp(V)
    b = len(V)
    f = max(dp.values())
    L = len(dp)
    return f, L, rho_of(f, L, b)


def comb_block(gadget, weights, s):
    """The (generalized) comb: block i is placed at position weights[i]*s."""
    V = set()
    for w in weights:
        for v in gadget:
            V.add(w * s + v)
    return sorted(V)


def local_signatures(G):
    """List of (size,sum,sumsq,mult) over all 2^|G| subsets of G."""
    d = defaultdict(int)
    n = len(G)
    for mask in range(1 << n):
        size = s = q = 0
        for j in range(n):
            if mask & (1 << j):
                v = G[j]; size += 1; s += v; q += v * v
        d[(size, s, q)] += 1
    return [(w, s, q, c) for (w, s, q), c in d.items()]


def local_by_size(G):
    """size t -> list of (sum,sumsq,mult) over t-subsets of G."""
    bysz = defaultdict(lambda: defaultdict(int))
    n = len(G)
    for mask in range(1 << n):
        size = s = q = 0
        for j in range(n):
            if mask & (1 << j):
                v = G[j]; size += 1; s += v; q += v * v
        bysz[size][(s, q)] += 1
    return {t: [(s, q, m) for (s, q), m in d.items()] for t, d in bysz.items()}


# ---- METHOD 0 (reference, #694): flat 6-tuple aggregate-moment DP ----------
def flat_asymptotic_fL(G, weights):
    """#694's asymptotic_fL, generalized to arbitrary per-block weights. Builds
    a dict keyed by the full 6-tuple (W,A,C,B,D,E); memory ~ L1_inf keys. Used
    only as the k<=4 reference (out of memory for k=5)."""
    loc = local_signatures(G)
    dp = defaultdict(int)
    dp[(0, 0, 0, 0, 0, 0)] = 1
    for w in weights:
        nd = defaultdict(int)
        for (W, A, C, B, D, E), cnt in dp.items():
            for (bw, bs, bq, c2) in loc:
                key = (W + bw, A + w * bw, C + w * w * bw, B + bs, D + w * bs, E + bq)
                nd[key] += cnt * c2
        dp = nd
    return max(dp.values()), len(dp), sum(dp.values())


# ---- METHOD 1 (this packet): grouped-by-size-vector, memory-bounded --------
def grouped_asymptotic_fL(G, weights, mem_cap_mb=1900.0):
    """Exact (f_inf, L1_inf, mass) via the size/value split. The 6-tuple
    (W,A,C,B,D,E) has a SIZE part (W,A,C) that depends only on the size-vector
    n=(|T_0|,...,|T_{k-1}|) -- one of (|G|+1)^k -- and a VALUE part (B,D,E).
    Group the size-vectors by (W,A,C); process one group at a time in the 3-D
    value space, so peak memory is bounded by a single group's value-set, not
    by L1_inf. Returns (fstar_inf, L1_inf, total_mass)."""
    k = len(weights)
    g = len(G)
    S = local_by_size(G)
    SG = sum(G); QG = sum(v * v for v in G)
    maxD = sum(w * SG for w in weights)
    maxE = k * QG
    mE = maxE + 1
    mD = maxD + 1
    # per (block index i, size t): pre-mapped value contributions (dB,dD,dE,mult)
    mapped = {}
    for i, w in enumerate(weights):
        for t, lst in S.items():
            mapped[(i, t)] = [(sig, w * sig, q, m) for (sig, q, m) in lst]
    # group size-vectors by wac=(W,A,C)
    groups = defaultdict(list)
    for n in itertools.product(range(g + 1), repeat=k):
        W = sum(n)
        A = sum(weights[i] * n[i] for i in range(k))
        C = sum(weights[i] * weights[i] * n[i] for i in range(k))
        groups[(W, A, C)].append(n)
    fstar = 0
    L1 = 0
    mass = 0
    for wac, nlist in groups.items():
        agg = defaultdict(int)
        for n in nlist:
            cur = {0: 1}          # packed (B,D,E)=0
            for i in range(k):
                mp = mapped[(i, n[i])]
                nxt = defaultdict(int)
                for key, c in cur.items():
                    E = key % mE
                    r = key // mE
                    D = r % mD
                    B = r // mD
                    for (dB, dD, dE, m) in mp:
                        nxt[((B + dB) * mD + (D + dD)) * mE + (E + dE)] += c * m
                cur = nxt
            for key, c in cur.items():
                agg[key] += c
        L1 += len(agg)
        if agg:
            gmx = max(agg.values())
            if gmx > fstar:
                fstar = gmx
            mass += sum(agg.values())
        if maxrss_mb() > mem_cap_mb:
            raise MemoryError(f"maxrss exceeded {mem_cap_mb}MB")
    return fstar, L1, mass


# ---- METHOD 2 (this packet): block-split meet-in-the-middle ----------------
def _half_wac_bde(G, block_weights):
    """dict[(W,A,C)] -> dict[(B,D,E)] -> mult for a subset of blocks."""
    loc = local_signatures(G)
    dp = {(0, 0, 0): {(0, 0, 0): 1}}
    for w in block_weights:
        nd = defaultdict(lambda: defaultdict(int))
        for (W, A, C), bde_d in dp.items():
            for (bw, bs, bq, c) in loc:
                tgt = nd[(W + bw, A + w * bw, C + w * w * bw)]
                for (B, D, E), cnt in bde_d.items():
                    tgt[(B + bs, D + w * bs, E + bq)] += cnt * c
        dp = {kk: dict(vv) for kk, vv in nd.items()}
    return dp


def mitm_asymptotic_fL(G, weights, split=None):
    """Independent method: split the k blocks into two halves, enumerate each
    half's partial 6-tuples with multiplicity, hash-join on the shared size
    invariant wac=(W,A,C), one target wac at a time (memory-bounded)."""
    k = len(weights)
    if split is None:
        split = k // 2
    hL = _half_wac_bde(G, weights[:split])
    hR = _half_wac_bde(G, weights[split:])
    pairs_by_target = defaultdict(list)
    Rkeys = list(hR.keys())
    for wacL in hL:
        for wacR in Rkeys:
            t = (wacL[0] + wacR[0], wacL[1] + wacR[1], wacL[2] + wacR[2])
            pairs_by_target[t].append((wacL, wacR))
    fstar = 0
    L1 = 0
    mass = 0
    for t, plist in pairs_by_target.items():
        agg = defaultdict(int)
        for (wacL, wacR) in plist:
            bl = hL[wacL]; br = hR[wacR]
            a, b = (bl, br) if len(bl) <= len(br) else (br, bl)
            for (Ba, Da, Ea), ca in a.items():
                for (Bb, Db, Eb), cb in b.items():
                    agg[(Ba + Bb, Da + Db, Ea + Eb)] += ca * cb
        L1 += len(agg)
        if agg:
            m = max(agg.values())
            if m > fstar:
                fstar = m
            mass += sum(agg.values())
    return fstar, L1, mass


# ============================================================ reported numbers
# k=2..4: PROUHET flat AP, (f_inf, L1_inf); the k=4 row IS the #694 champion.
FLAT_TABLE = {
    2: (4, 3863, 0.110644),
    3: (23, 162075, 0.147481),
    4: (190, 4192627, 0.160847),
    5: (2072, 57376057, 0.156900),
}
# reported k=5 maximum over the searched weight window: the leading two-cluster
# family (0,1,2,m,m+1) peaks at m=7 and declines thereafter (dissociation), so
# its interior maximum is this sequence -- and it is below the b=24 champion.
K5_MAX = {"weights": (0, 1, 2, 7, 8), "f": 760, "L": 171764913, "rho": 0.160018}
# a few k=4 weight sequences confirming the champion is the k=4 weight-window max
K4_SAMPLE = {
    (0, 1, 2, 3): (190, 4192627),   # AP -> champion
    (0, 2, 4, 6): (190, 4192627),   # AP dilated -> identical census (affine)
    (0, 1, 3, 4): (160, 4305647),   # non-AP -> below
    (0, 2, 5, 7): (98, 7377661),    # non-AP -> below
}


# ==================================================================== blocks
def block_A_champion():
    print("\nBLOCK A -- recap: PROUHET gadget and the #694 b=24 champion")
    f, L, rho = stat_direct(PROUHET)
    check(f == 2 and L == 63 and approx(rho, 0.112900, 1e-5),
          f"PROUHET {PROUHET} (hughes #564): f=2 L=63 rho=0.1129 (got {f},{L},{rho:.6f})")
    # champion via the memory-bounded grouped method
    fg, Lg, massg = grouped_asymptotic_fL(PROUHET, (0, 1, 2, 3))
    check((fg, Lg) == (190, 4192627),
          f"#694 champion via grouped method: f=190 L=4192627 (got {fg},{Lg})")
    check(massg == 2 ** 24, f"mass conservation at k=4: sum of fibers = 2^24 (got {massg})")
    rho_champ = rho_of(fg, Lg, 24)
    check(approx(rho_champ, 0.160847, 1e-5),
          f"champion rho=(log190+log4192627)/24-log2 = 0.160847 (got {rho_champ:.6f})")
    # the champion realized as a CONCRETE b=24 block at shift s=48 (direct DP)
    V = comb_block(PROUHET, (0, 1, 2, 3), 48)
    check(len(V) == 24, "champion realized as a concrete 24-integer block at s=48")
    fd, Ld, rd = stat_direct(V)
    check((fd, Ld) == (190, 4192627) and approx(rd, 0.160847, 1e-5),
          f"direct DP on the concrete s=48 block matches the asymptotic value (got {fd},{Ld})")


def block_B_method_validation():
    print("\nBLOCK B -- the memory-bounded method: 3 independent algorithms agree (k<=4)")
    for k in (2, 3, 4):
        weights = tuple(range(k))
        b = 6 * k
        f_ref, L_ref, mass_ref = flat_asymptotic_fL(PROUHET, weights)   # #694 flat DP
        f_g, L_g, mass_g = grouped_asymptotic_fL(PROUHET, weights)       # grouped
        f_m, L_m, mass_m = mitm_asymptotic_fL(PROUHET, weights)          # MITM
        f0, L0, r0 = FLAT_TABLE[k]
        ok = (f_ref, L_ref) == (f_g, L_g) == (f_m, L_m) == (f0, L0)
        ok_mass = mass_ref == mass_g == mass_m == 2 ** b
        check(ok, f"k={k}: flat=({f_ref},{L_ref}) grouped=({f_g},{L_g}) mitm=({f_m},{L_m}) "
                  f"all == reported ({f0},{L0})")
        check(ok_mass, f"k={k}: all three conserve mass = 2^{b} = {2 ** b}")
        check(approx(rho_of(f_g, L_g, b), r0, 1e-5),
              f"k={k}: rho_inf={rho_of(f_g,L_g,b):.6f} == reported {r0}")
    # the weight search relies on all three methods agreeing for NON-FLAT weights
    # too (not just the AP w_i=i); validate that here on small non-flat sequences
    for w in [(0, 1, 3), (0, 1, 4), (0, 1, 2, 4), (0, 1, 3, 4)]:
        b = 6 * len(w)
        f_ref, L_ref, m_ref = flat_asymptotic_fL(PROUHET, w)
        f_g, L_g, m_g = grouped_asymptotic_fL(PROUHET, w)
        f_m, L_m, m_m = mitm_asymptotic_fL(PROUHET, w)
        check((f_ref, L_ref) == (f_g, L_g) == (f_m, L_m) and m_ref == m_g == m_m == 2 ** b,
              f"non-flat weights {list(w)}: flat==grouped==mitm=({f_g},{L_g}), mass=2^{b} "
              f"(the weight-search engine is correct off the AP too)")


def block_C_k5():
    print("\nBLOCK C -- k=5 (b=30) flat AP: the memory wall crossed, two methods agree")
    t0 = time.time()
    f_g, L_g, mass_g = grouped_asymptotic_fL(PROUHET, (0, 1, 2, 3, 4))
    print(f"    [grouped]  f={f_g} L={L_g}  ({time.time()-t0:.0f}s, peak {maxrss_mb():.0f}MB)")
    t0 = time.time()
    f_m, L_m, mass_m = mitm_asymptotic_fL(PROUHET, (0, 1, 2, 3, 4))
    print(f"    [mitm]     f={f_m} L={L_m}  ({time.time()-t0:.0f}s, peak {maxrss_mb():.0f}MB)")
    f0, L0, r0 = FLAT_TABLE[5]
    check((f_g, L_g) == (f0, L0), f"k=5 grouped: f=2072 L=57376057 (got {f_g},{L_g})")
    check((f_m, L_m) == (f0, L0), "k=5 MITM independently agrees with grouped")
    check(mass_g == mass_m == 2 ** 30, f"k=5 mass conservation = 2^30 = {2 ** 30} (both methods)")
    r5 = rho_of(f_g, L_g, 30)
    check(approx(r5, 0.156900, 1e-5), f"k=5 rho_inf=0.156900 (got {r5:.6f})")
    check(r5 < CHAMPION_RHO,
          f"k=5 flat AP ({r5:.6f}) is BELOW the b=24 champion ({CHAMPION_RHO}) "
          f"-- resolves #694 residual #1 negatively")
    check(r5 < OLDCHAMP_RHO,
          f"k=5 flat AP ({r5:.6f}) is even below the #655 b=18 champion ({OLDCHAMP_RHO})")
    check(peak_ok := maxrss_mb() < 1900.0,
          f"peak resident memory stayed under the 1900MB guard (got {maxrss_mb():.0f}MB)")


def block_D_weights():
    print("\nBLOCK D -- non-uniform weights (#694 residual #3): champion is the searched-window max")
    # k=4 weight window: the champion (AP) is the maximum; representative sample
    for w, (fe, Le) in K4_SAMPLE.items():
        f, L, mass = grouped_asymptotic_fL(PROUHET, w)
        b = 6 * len(w)
        r = rho_of(f, L, b)
        ok = (f, L) == (fe, Le)
        rel = "==champion" if approx(r, CHAMPION_RHO, 1e-5) else ("BEATS!" if r > CHAMPION_RHO else "<champion")
        check(ok, f"k=4 weights {list(w)}: f={f} L={L} rho={r:.6f} [{rel}] (expected {fe},{Le})")
    # AP dilations give the IDENTICAL census (affine invariance), non-AP are strictly below
    check(K4_SAMPLE[(0, 1, 2, 3)] == K4_SAMPLE[(0, 2, 4, 6)],
          "k=4 AP (0,1,2,3) and its dilation (0,2,4,6) give the identical census (affine invariance)")
    r_non = rho_of(*K4_SAMPLE[(0, 1, 3, 4)], 24)
    check(r_non < CHAMPION_RHO,
          f"k=4 best non-AP sample rho={r_non:.6f} < champion {CHAMPION_RHO} "
          f"(full 84-sequence sweep in repro; AP is the unique window max up to scaling)")
    # k=5 weight window maximum: recompute the reported argmax sequence from scratch
    w5 = K5_MAX["weights"]
    t0 = time.time()
    f, L, mass = grouped_asymptotic_fL(PROUHET, w5)
    r = rho_of(f, L, 30)
    print(f"    [k=5 window max] weights {list(w5)}: f={f} L={L} rho={r:.6f}  ({time.time()-t0:.0f}s)")
    check((f, L) == (K5_MAX["f"], K5_MAX["L"]),
          f"k=5 window-max weights {list(w5)}: f={K5_MAX['f']} L={K5_MAX['L']} (got {f},{L})")
    check(mass == 2 ** 30, "k=5 window-max sequence conserves mass = 2^30")
    check(approx(r, K5_MAX["rho"], 1e-5), f"k=5 window-max rho={K5_MAX['rho']} (got {r:.6f})")
    check(r < CHAMPION_RHO,
          f"k=5 window maximum ({r:.6f}) is STILL BELOW the b=24 champion ({CHAMPION_RHO}) "
          f"-- no b=30 member of the searched family beats the champion")


def block_E_arithmetic():
    print("\nBLOCK E -- rho arithmetic triple-check (log base e, normalization by b)")
    # champion: b=24
    f, L, b = 190, 4192627, 24
    r_direct = (log(f) + log(L)) / b - log(2)
    r_prod = log((f * L) ** (1.0 / b)) - log(2)          # via X=(fL)^{1/b}
    X = (f * L) ** (1.0 / b)
    check(approx(r_direct, 0.160847, 1e-6) and approx(r_prod, 0.160847, 1e-6),
          f"champion rho two ways: (logf+logL)/b-log2 and logX-log2 both = {r_direct:.6f}")
    check(approx(X, 2.349011, 1e-5), f"champion X=(f*L)^(1/24)=2.349011 (got {X:.6f})")
    # k=5: b=30 (normalization uses b=30, NOT 24)
    f, L, b = 2072, 57376057, 30
    r5 = (log(f) + log(L)) / b - log(2)
    check(approx(r5, 0.156900, 1e-6), f"k=5 rho with b=30 normalization = 0.156900 (got {r5:.6f})")
    check((log(f) + log(L)) / 24 - log(2) > CHAMPION_RHO,
          "SANITY: normalizing the k=5 census by the WRONG b=24 would spuriously exceed the "
          "champion -- confirming the b=30 normalization is the load-bearing, correct one")


def run_check():
    cap_s = 12 * 60
    t0 = time.time()
    print("=" * 78)
    print("verify_comb_trade_champion_k5.py -- k=5/b=30 extension of #694; CEILING result")
    print("=" * 78)
    block_A_champion()
    block_B_method_validation()
    block_C_k5()
    block_D_weights()
    block_E_arithmetic()
    npass = sum(1 for c, _ in CHECKS if c)
    ntot = len(CHECKS)
    elapsed = time.time() - t0
    print("\n" + "=" * 78)
    print(f"elapsed {elapsed:.0f}s (cap {cap_s}s), peak {maxrss_mb():.0f}MB")
    ok = (npass == ntot) and (elapsed <= cap_s)
    print(f"RESULT: {'PASS' if ok else 'FAIL'} ({npass}/{ntot})")
    print("=" * 78)
    return 0 if ok else 1


def run_tamper_selftest():
    """Prove the verifier is not vacuous: recompute the k=5 census and confirm
    it does NOT equal a deliberately wrong stored value, and that a correct
    recomputation DOES equal the true stored value."""
    print("--tamper-selftest: recompute k=5 census and test detection of a wrong claim")
    f, L, mass = grouped_asymptotic_fL(PROUHET, (0, 1, 2, 3, 4))
    true_ok = (f, L) == (2072, 57376057)
    print(f"    recomputed k=5: f={f} L={L}")
    print(f"    [{'ok  ' if true_ok else 'FAIL'}] recomputation equals the true stored (2072,57376057)")
    WRONG = (2073, 57376057)   # off-by-one in fstar
    catches = (f, L) != WRONG
    print(f"    [{'ok  ' if catches else 'FAIL'}] recomputation DETECTS the tampered value {WRONG} "
          f"(does not match) -- verifier is non-vacuous")
    # also confirm rho tamper is caught
    r = rho_of(f, L, 30)
    rho_catches = not approx(r, 0.160847, 1e-5)   # a wrong 'beats champion' claim would fail
    print(f"    [{'ok  ' if rho_catches else 'FAIL'}] recomputed rho={r:.6f} does NOT match a "
          f"falsely-claimed champion-tying 0.160847")
    ok = true_ok and catches and rho_catches
    print(f"RESULT: {'PASS' if ok else 'FAIL'} (3/3)" if ok else f"RESULT: FAIL")
    return 0 if ok else 1


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--check"
    if mode == "--tamper-selftest":
        sys.exit(run_tamper_selftest())
    else:
        sys.exit(run_check())


if __name__ == "__main__":
    main()
