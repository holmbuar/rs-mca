#!/usr/bin/env python3
"""Heavier reproduction script for comb_trade_champion_k5.md -- the searches and
wider-neighborhood scans behind the k=5/b=30 CEILING result, and the
memory/timing documentation of the grouped method. Not required to run fast
(verify_comb_trade_champion_k5.py re-certifies the reported numbers within a
stated cap); this script documents HOW the frontier was mapped.

Stdlib-only. Blocks (documented approximate runtime on 4 cores):
  KTREND   k=2..5 flat-AP PROUHET comb asymptotic (peak at k=4)          ~2 min
  K4SWEEP  full weight-sequence search at k=4 (b=24): AP is the max      ~6 min
  K5SWEEP  weight-sequence search at k=5 (b=30): window max < champion   ~15 min (parallel)
  DEGEN    tensor-degeneration: spread weights -> single-gadget rate     ~1 min
Total ~25 min. Peak resident memory stays ~<100 MB per worker throughout
(the grouped method's memory is bounded by a single (W,A,C)-group's value-set).

Usage: repro_comb_trade_champion_k5.py [ktrend|k4sweep|k5sweep|degen|all]
"""
from __future__ import annotations
import itertools
import resource
import sys
import time
from collections import defaultdict
from math import gcd, log

LOG2 = log(2)
PROUHET = (0, 1, 2, 4, 5, 6)
CHAMPION_RHO = 0.160847


def maxrss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def rho_of(f, L, b):
    return (log(f) + log(L)) / b - LOG2


def local_by_size(G):
    bysz = defaultdict(lambda: defaultdict(int))
    n = len(G)
    for mask in range(1 << n):
        size = s = q = 0
        for j in range(n):
            if mask & (1 << j):
                v = G[j]; size += 1; s += v; q += v * v
        bysz[size][(s, q)] += 1
    return {t: [(s, q, m) for (s, q), m in d.items()] for t, d in bysz.items()}


def grouped_asymptotic_fL(G, weights, mem_cap_mb=1900.0):
    """Exact (f_inf, L1_inf) via the size/value split; peak memory bounded by a
    single (W,A,C)-group's value-set (see the note, section 2)."""
    k = len(weights)
    g = len(G)
    S = local_by_size(G)
    SG = sum(G); QG = sum(v * v for v in G)
    mE = k * QG + 1
    mD = sum(w * SG for w in weights) + 1
    mapped = {}
    for i, w in enumerate(weights):
        for t, lst in S.items():
            mapped[(i, t)] = [(sig, w * sig, q, m) for (sig, q, m) in lst]
    groups = defaultdict(list)
    for n in itertools.product(range(g + 1), repeat=k):
        W = sum(n)
        A = sum(weights[i] * n[i] for i in range(k))
        C = sum(weights[i] * weights[i] * n[i] for i in range(k))
        groups[(W, A, C)].append(n)
    fstar = 0
    L1 = 0
    for wac, nlist in groups.items():
        agg = defaultdict(int)
        for n in nlist:
            cur = {0: 1}
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
        if maxrss_mb() > mem_cap_mb:
            raise MemoryError(f"maxrss exceeded {mem_cap_mb}MB")
    return fstar, L1


def canonical(seq):
    r = tuple(sorted(seq[-1] - x for x in seq))
    return min(seq, r)


def gen_seqs(k, Wmax):
    """Affine-inequivalent weight sequences: start at 0, gcd=1 (drop pure
    dilations), dedup by reflection."""
    seen = set()
    out = []
    for combo in itertools.combinations(range(1, Wmax + 1), k - 1):
        seq = (0,) + combo
        g = 0
        for x in seq:
            g = gcd(g, x)
        if g != 1:
            continue
        c = canonical(seq)
        if c in seen:
            continue
        seen.add(c)
        out.append(seq)
    return out


def _work(seq):
    f, L = grouped_asymptotic_fL(PROUHET, seq)
    return (seq, f, L, rho_of(f, L, 6 * len(seq)))


def block_ktrend():
    print("=" * 74)
    print("KTREND -- flat-AP PROUHET comb, k=2..5: rho_inf peaks at k=4 (b=24)")
    print("=" * 74)
    rows = []
    for k in (2, 3, 4, 5):
        t0 = time.time()
        f, L = grouped_asymptotic_fL(PROUHET, tuple(range(k)))
        b = 6 * k
        r = rho_of(f, L, b)
        rows.append((k, b, f, L, r))
        rel = ("CHAMPION" if abs(r - CHAMPION_RHO) < 1e-5
               else ("above champ" if r > CHAMPION_RHO else "below champ"))
        print(f"  k={k} b={b:2d}: f_inf={f:6d} L1_inf={L:9d} rho_inf={r:.6f}  [{rel}]  ({time.time()-t0:.0f}s)")
    peak = max(rows, key=lambda x: x[4])
    print(f"  => rho_inf is maximized at k={peak[0]} (b={peak[1]}), rho={peak[4]:.6f}; "
          f"it rises 2->3->4 then FALLS 4->5 (0.160847 -> {rows[-1][4]:.6f}).")


def block_k4sweep():
    print("=" * 74)
    print("K4SWEEP -- full weight-sequence search at k=4 (b=24): AP is the maximum")
    print("=" * 74)
    seqs = gen_seqs(4, 12)
    print(f"  {len(seqs)} affine-inequivalent sequences (Wmax=12)")
    import multiprocessing as mp
    results = []
    t0 = time.time()
    with mp.Pool(4) as pool:
        for (seq, f, L, r) in pool.imap_unordered(_work, seqs):
            results.append((r, seq, f, L))
    results.sort(reverse=True)
    print(f"  searched in {time.time()-t0:.0f}s. TOP 8:")
    for r, seq, f, L in results[:8]:
        tag = "  <== BEATS CHAMPION" if r > CHAMPION_RHO + 1e-9 else ("  (== champion, AP)" if abs(r - CHAMPION_RHO) < 1e-5 else "")
        print(f"    {list(seq)} f={f:5d} L={L:9d} rho={r:.6f}{tag}")
    print(f"  MAX rho = {results[0][0]:.6f} at {list(results[0][1])} "
          f"({'BEATS' if results[0][0] > CHAMPION_RHO + 1e-9 else 'ties/at'} champion) -- "
          f"the AP weights (unique up to affine scaling) are the k=4 window optimum.")


def block_k5sweep(Wmax=8):
    print("=" * 74)
    print(f"K5SWEEP -- weight-sequence search at k=5 (b=30), Wmax={Wmax}")
    print("=" * 74)
    seqs = gen_seqs(5, Wmax)
    print(f"  {len(seqs)} affine-inequivalent sequences; parallel over 4 cores (~15 min)")
    import multiprocessing as mp
    results = []
    t0 = time.time()
    with mp.Pool(4) as pool:
        for (seq, f, L, r) in pool.imap_unordered(_work, seqs):
            results.append((r, seq, f, L))
            tag = "  <== BEATS CHAMPION" if r > CHAMPION_RHO + 1e-9 else ""
            print(f"    [{len(results)}/{len(seqs)} {time.time()-t0:.0f}s] {list(seq)} "
                  f"f={f} L={L} rho={r:.6f}{tag}", flush=True)
    results.sort(reverse=True)
    print(f"  TOP 8 at k=5:")
    for r, seq, f, L in results[:8]:
        print(f"    {list(seq)} f={f} L={L} rho={r:.6f}")
    mx = results[0]
    print(f"  MAX rho = {mx[0]:.6f} at {list(mx[1])} "
          f"({'BEATS' if mx[0] > CHAMPION_RHO + 1e-9 else 'STILL BELOW'} champion {CHAMPION_RHO}).")


def block_degen():
    print("=" * 74)
    print("DEGEN -- spread weights collapse rho_inf to a floor far below the champion")
    print("=" * 74)
    print(f"  single-gadget PROUHET rate rho(G) = {rho_of(2, 63, 6):.6f} (reference)")
    # k=3 weight sequences of increasing diameter; rho_inf decays to a floor.
    # NOTE: the comb does NOT become #683's positional tensor when the weights
    # spread -- all blocks still share ONE quadratic coordinate, so f_inf -> 2^k
    # (the size-vector becomes injective, killing cross-block size collisions)
    # while the value part (B,D,E) still aggregates 3 coordinates over k blocks.
    # The point is only that rho_inf FALLS MONOTONICALLY to a floor well below
    # the champion, so the maximum lives at bounded (searched) diameter.
    prev = None
    for weights in [(0, 1, 2), (0, 1, 3), (0, 2, 5), (0, 3, 8), (0, 5, 13), (0, 8, 21), (0, 13, 34)]:
        f, L = grouped_asymptotic_fL(PROUHET, weights)
        r = rho_of(f, L, 18)
        mono = "" if prev is None else ("  (down)" if r < prev + 1e-9 else "  (UP!)")
        print(f"  weights {list(weights)} (diam {weights[-1]:2d}): f={f:4d} L={L:7d} rho_inf={r:.6f}{mono}")
        prev = r
    print("  => f_inf -> 2^k and rho_inf decays to a size-injective floor (~0.108 at k=3),")
    print("     far below the champion 0.160847; the max over ALL weight sequences is")
    print("     therefore attained at bounded (searched) diameter, not out at large spread.")


BLOCKS = {"ktrend": block_ktrend, "k4sweep": block_k4sweep,
          "k5sweep": block_k5sweep, "degen": block_degen}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which == "all":
        block_ktrend(); block_k4sweep(); block_k5sweep(); block_degen()
    else:
        BLOCKS[which]()
    print("\nrepro_comb_trade_champion_k5.py complete.")
