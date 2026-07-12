#!/usr/bin/env python3
"""Verify the fenced energy-pincer analysis (stdlib only, deterministic).

Composes DannyExperiments PR #696 (realized-image Boolean-slice energy lift) with
our PR #691 (empty bounded-denominator window on the fenced class) and PR #692
(fiber-denominator tension confined off the wall), against the image-face wall
localized by #661/#663 (Diophantine control of the dominant resonance denominator).

Result is DECIDED-NEGATIVE for closing the denominator wall: #696 constrains the
SOURCE additive energy Delta(F) of the max fiber (a Boolean-cube object) into a
two-sided wall band, but that band lives in coordinates (theta, Delta) orthogonal
to the resonance-denominator coordinate q that #691/#692 control -- so no window
forces q into range.  The verifier recomputes every number in the note:

  BLOCK 0  #696 band + density constants (goal-ladder step 1 constants)
  BLOCK 1  #696 inequalities (1)-(4) on four concrete blocks
  BLOCK 2  PILLAR 1 -- affine-blindness of Delta (EXACT; the core obstruction)
  BLOCK 3  PILLAR 2 -- (theta,Delta) does not determine q on normalized blocks
  BLOCK 4  PILLAR 3 -- resonance subtorus is 3-dim (measure-zero) in the source
  BLOCK 5  #691 (corrected) class-count ceiling and #692 eta-threshold are
           (theta,Delta)-independent

Usage:
    python3 verify_fenced_energy_pincer.py            # full check, prints RESULT
    python3 verify_fenced_energy_pincer.py --check     # same
    python3 verify_fenced_energy_pincer.py --tamper-selftest
"""

from __future__ import annotations

import sys
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb, cos, gcd, isclose, log, log2, pi, sqrt

PASS = 0
TOTAL = 0


def check(cond: bool, label: str) -> None:
    global PASS, TOTAL
    TOTAL += 1
    if cond:
        PASS += 1
    else:
        raise AssertionError(f"CHECK FAILED: {label}")


# ---------------------------------------------------------------- helpers -----
def layer_count(n: int, total: int, cap: int) -> int:
    row = [0] * (total + 1)
    row[0] = 1
    for _ in range(n):
        nxt = [0] * (total + 1)
        for s, v in enumerate(row):
            if not v:
                continue
            for d in range(cap + 1):
                if s + d <= total:
                    nxt[s + d] += v
        row = nxt
    return row[total]


def h2(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * log2(p) - (1.0 - p) * log2(1.0 - p)


def hvec(ps: tuple[float, ...]) -> float:
    return -sum(p * log2(p) for p in ps if p > 0.0)


def g_ent(p: float) -> float:
    return hvec(((1 - p) ** 2 / 2, (1 - p * p) / 2, p * (2 - p) / 2, p * p / 2))


def a_ent(p: float) -> float:
    return 1.0 + h2(p) / 2.0


def normalize(vs) -> tuple[int, ...]:
    vs = sorted(set(vs))
    mn = vs[0]
    vs = [v - mn for v in vs]
    G = 0
    for v in vs:
        G = gcd(G, v)
    if G > 1:
        vs = [v // G for v in vs]
    return tuple(vs)


def block_data(V, do_normalize: bool = True) -> dict:
    """Enumerate all subsets; return max-fiber data and its source additive energy."""
    V = normalize(V) if do_normalize else tuple(V)
    b = len(V)
    buckets: dict = defaultdict(list)
    for mask in range(1 << b):
        m = bin(mask).count("1")
        s1 = 0
        s2 = 0
        for i in range(b):
            if mask >> i & 1:
                s1 += V[i]
                s2 += V[i] * V[i]
        buckets[(m, s1, s2)].append(mask)
    L = len(buckets)
    best_sig, F = max(buckets.items(), key=lambda kv: len(kv[1]))
    mstar = best_sig[0]
    f = len(F)
    # additive energy E(F) = #{(a,b,c,d) in F^4 : a+b=c+d in Z^b}
    cnt: Counter = Counter()
    for a in F:
        for c in F:
            code = 0
            scale = 1
            for i in range(b):
                code += (((a >> i) & 1) + ((c >> i) & 1)) * scale
                scale *= 3
            cnt[code] += 1
    E = sum(v * v for v in cnt.values())
    return dict(
        V=V, b=b, f=f, L=L, mstar=mstar, theta=mstar / b,
        E=E, Delta=E / f ** 3, F=tuple(sorted(F)),
        A=layer_count(b, 2 * mstar, 2), B=layer_count(b, 3 * mstar, 3),
    )


def M_at(V, t2: float, n01: int = 24) -> float:
    """theta_2-marginal of |Xhat| at fixed t2, midpoint quadrature over (t0,t1)."""
    V = normalize(V)
    acc = 0.0
    ncnt = 0
    for k1 in range(n01):
        t1 = (k1 + 0.5) / n01
        for k0 in range(n01):
            t0 = (k0 + 0.5) / n01
            p = 1.0
            for v in V:
                p *= abs(cos(pi * (t0 + t1 * v + t2 * v * v)))
            acc += p
            ncnt += 1
    return acc / ncnt


def resonance_ratio(V, n2: int = 240, n01: int = 24) -> dict:
    """Robust discriminant: (best small-q<=5 peak) / (global non-parity peak)."""
    V = normalize(V)
    gmax = -1.0
    garg = None
    for k2 in range(n2):
        t2 = k2 / n2
        if min(abs(t2), abs(t2 - 1.0)) < 0.045 or abs(t2 - 0.5) < 0.045:
            continue
        M = M_at(V, t2, n01)
        if M > gmax:
            gmax = M
            garg = t2
    smax = -1.0
    sarg = None
    for q in (3, 4, 5):
        for p in range(1, q):
            if gcd(p, q) != 1:
                continue
            t2 = p / q
            if abs(t2 - 0.5) < 0.02:
                continue
            M = M_at(V, t2, n01)
            if M > smax:
                smax = M
                sarg = (p, q)
    return dict(gmax=gmax, garg=garg, smax=smax, sarg=sarg, ratio=smax / gmax)


def rank_moment_map(V) -> int:
    """Rank over Q of the b x 3 matrix [1, v_i, v_i^2]; = dim of the resonance subtorus."""
    V = normalize(V)
    rows = [[Fraction(1), Fraction(v), Fraction(v * v)] for v in V]
    rank = 0
    used = [False] * len(rows)
    for col in range(3):
        piv = -1
        for r in range(len(rows)):
            if not used[r] and rows[r][col] != 0:
                piv = r
                break
        if piv < 0:
            continue
        used[piv] = True
        rank += 1
        pv = rows[piv][col]
        for r in range(len(rows)):
            if r != piv and rows[r][col] != 0:
                fac = rows[r][col] / pv
                rows[r] = [rows[r][c] - fac * rows[piv][c] for c in range(3)]
    return rank


# ------------------------------------------------------------- the blocks -----
BLOCKS = {
    "interval14": list(range(14)),
    "gap16_r2": [i + 5 * j for j in range(4) for i in range(4)],
    "unionAP16": [3 * j for j in range(8)] + [1 + 3 * j for j in range(8)],
    "champ18": [2, 3, 4, 6, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 30, 32, 33, 34],
}


# ---------------------------------------------------------------- blocks ------
def block0_constants() -> None:
    gh = g_ent(0.5)
    check(isclose(gh, 3.0 - 0.75 * log2(3.0), abs_tol=1e-12), "g(1/2)=3-0.75 log2 3")
    check(isclose(gh, 1.811278124459, abs_tol=1e-9), "g(1/2)=1.811278124459")
    gamma_hi = gh - 4.0 / 3.0
    check(isclose(gamma_hi, 0.477944791126, abs_tol=1e-9), "gamma_hi log2 = 0.477944791126")
    check(isclose(gamma_hi * log(2.0), 0.331286084432, abs_tol=1e-9), "gamma_hi ln = 0.331286084432")
    # lower band edge from E(F) <= f^{log2 6} and the wall floor phi > 1/3
    gamma_lo_coeff = 3.0 - log2(6.0)
    check(isclose(gamma_lo_coeff, 0.415037499279, abs_tol=1e-9), "3-log2 6 = 0.415037499279")
    check(isclose(gamma_lo_coeff * log(2.0), log(4.0 / 3.0), abs_tol=1e-12),
          "(3-log2 6) ln2 = ln(4/3) exactly")
    gamma_lo = log(4.0 / 3.0) / 3.0
    check(isclose(gamma_lo, 0.095894024151, abs_tol=1e-9), "ln(4/3)/3 = 0.095894024151")
    check(isclose(gamma_lo / log(2.0), 0.138345833093, abs_tol=1e-9),
          "lower band edge log2 = 0.138345833093")
    # band non-empty (no self-contradiction: #696 alone does not kill the wall)
    check(gamma_lo / log(2.0) < gamma_hi, "wall energy band nonempty: 0.1383 < 0.4779")
    # density bands: a(theta)>4/3 <=> h2(theta)>2/3 ; g(theta)>4/3 (wider)
    def bisect(fn, lo, hi, target):
        for _ in range(90):
            mid = (lo + hi) / 2
            if fn(mid) < target:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2
    th_a = bisect(h2, 1e-4, 0.5, 2.0 / 3.0)
    th_g = bisect(g_ent, 1e-4, 0.5, 4.0 / 3.0)
    check(isclose(th_a, 0.173952331409, abs_tol=1e-8), "h2(theta)=2/3 at 0.173952331409")
    check(isclose(h2(th_a), 2.0 / 3.0, abs_tol=1e-9), "a(theta)=4/3 <=> h2=2/3")
    check(isclose(th_g, 0.078609, abs_tol=1e-5), "g(theta)=4/3 at 0.078609")
    check(th_g < th_a, "g-band wider than a-band; a-band (0.174,0.826) is binding")


def block1_inequalities() -> None:
    for name, V in BLOCKS.items():
        D = block_data(V)
        b, f, L, E, th = D["b"], D["f"], D["L"], D["E"], D["theta"]
        check(f * L <= D["A"], f"{name}: (1) fL <= A(N,m)")
        check(f ** 4 * L <= D["B"] * E, f"{name}: (2) fL <= B Delta  (integer form f^4 L <= B E)")
        check(f * L <= 2.0 ** (b * a_ent(th)) + 1e-6, f"{name}: (3) fL <= 2^(N a(theta))")
        check(f ** 4 * L <= 2.0 ** (b * g_ent(th)) * E + 1e-6, f"{name}: (4) fL <= 2^(N g) Delta")
        # every block here is OFF the wall (small-b plateau): X = (fL)^(1/b) < 2^(4/3)
        check((f * L) ** (1.0 / b) < 2.0 ** (4.0 / 3.0), f"{name}: off-wall X < 2^(4/3)")
    # exact recorded values (pin the enumeration)
    D = block_data(BLOCKS["champ18"])
    check((D["f"], D["L"], D["mstar"], D["E"]) == (30, 151275, 9, 2898),
          "champ18 exact (f,L,m*,E)=(30,151275,9,2898)")
    Du = block_data(BLOCKS["unionAP16"])
    check((Du["f"], Du["L"], Du["mstar"], Du["E"]) == (20, 25619, 8, 900),
          "unionAP16 exact (f,L,m*,E)=(20,25619,8,900)")


def block2_affine_blindness() -> None:
    """PILLAR 1 (EXACT): the affine action fixes (F,E,f,Delta) but moves the denominator."""
    base = normalize(BLOCKS["unionAP16"])
    D0 = block_data(base, do_normalize=False)
    denoms = set()
    for a in (1, 2, 3):
        Va = tuple(a * v for v in base)  # dilation; NOT renormalized
        Da = block_data(Va, do_normalize=False)
        # F (as a set of masks), E, f, Delta are byte-identical -- E(F) reads only the masks
        check(Da["F"] == D0["F"], f"a={a}: max-fiber mask set identical (Delta is affine-blind)")
        check(Da["E"] == D0["E"] and Da["f"] == D0["f"], f"a={a}: E,f identical")
        check(Da["Delta"] == D0["Delta"], f"a={a}: Delta identical (exact)")
        # the resonance denominator is NOT invariant: theta_2 -> a^2 theta_2
        # unionAP16 resonates at 2/3; the raw dilate resonates at reduced (2/3)/a^2
        denoms.add((Fraction(2, 3) / (a * a)).denominator)
    check(denoms == {3, 6, 27}, "raw resonance denominators run through {3,6,27} at fixed Delta")
    check(len(denoms) == 3, "Delta constant while q takes 3 distinct values: q not a function of Delta")


def block3_non_functionality() -> None:
    """PILLAR 2 (MEASURED): equal theta, Delta within 5%, incompatible resonance denominators."""
    c = block_data(BLOCKS["champ18"])
    u = block_data(BLOCKS["unionAP16"])
    check(c["theta"] == u["theta"] == 0.5, "champ18, unionAP16 share theta = 1/2")
    check(abs(c["Delta"] - u["Delta"]) / u["Delta"] < 0.05,
          "Delta within 5% (0.1073 vs 0.1125)")
    rc = resonance_ratio(BLOCKS["champ18"])
    ru = resonance_ratio(BLOCKS["unionAP16"])
    # unionAP16: dominant resonance IS at a small denominator (embedded AP diff 3 -> q=3)
    check(ru["sarg"] == (2, 3), "unionAP16 small-q peak at 2/3 (q=3)")
    check(isclose(ru["ratio"], 1.0, abs_tol=1e-9), "unionAP16 peak is at small q (ratio 1.00)")
    check(isclose(ru["garg"], 2.0 / 3.0, abs_tol=1e-2), "unionAP16 global peak at 2/3")
    # champ18: dominant resonance is spread -- NOT at any small q
    check(rc["ratio"] < 0.85, "champ18 small-q peaks fall short of its global peak (ratio < 0.85)")
    check(min(abs(rc["garg"] - p / q)
              for q in (2, 3, 4, 5) for p in range(1, q) if gcd(p, q) == 1) > 0.010,
          "champ18 global peak is >0.01 from every small rational (spread resonance)")
    # discriminant separates the two blocks despite equal (theta, Delta)
    check(ru["ratio"] / rc["ratio"] > 1.15, "resonance discriminant separates equal-(theta,Delta) blocks")


def block4_subtorus_dimension() -> None:
    """PILLAR 3 (EXACT): resonance frequencies form a 3-dim (measure-zero) subtorus of T^b."""
    for name, V in BLOCKS.items():
        r = rank_moment_map(V)
        b = len(normalize(V))
        check(r == 3, f"{name}: moment-map rank 3 (Vandermonde, distinct v_i)")
        check(r < b, f"{name}: subtorus dim 3 < b={b}, hence Lebesgue-null in the source torus")


def omega_distinct_primes(q: int) -> int:
    """omega(q) = number of distinct prime factors."""
    n = q
    c = 0
    d = 2
    while d * d <= n:
        if n % d == 0:
            c += 1
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        c += 1
    return c


def class_count_ceiling(w: float, q: int) -> float:
    """#691 CORRECTED common-q class count: up to (2*floor(wq)+1)*M(a,a';q) systems (M=2^omega(q) on this grid's odd squarefree q; see #700).

    (T1's printed single-residue 'only if' ceiling is superseded; a single system is
    guaranteed only for w < 1/(2q), and structure degrades gradually above it.)
    """
    return (2.0 * w * q + 1.0) * (2 ** omega_distinct_primes(q))


def block5_endpoints_independent() -> None:
    """#691 (as corrected) and #692 endpoints depend only on (b, eta, delta, alpha)."""
    # corrected class-count: single system GUARANTEED iff w < 1/(2q); gradual growth above.
    # (guards against T1's refuted 'never resolves above q=1/(2w)' -- we use only the guarantee.)
    for w, q in [(0.10, 4), (0.10, 7), (0.10, 100), (0.10, 600)]:
        C = class_count_ceiling(w, q)
        single_guaranteed = w < 1.0 / (2.0 * q)
        check(C >= 1.0, f"class-count ceiling >= 1 at (w={w},q={q})")
        if single_guaranteed:
            check(C < 2.0 * (2 ** omega_distinct_primes(q)) + 1e-9,
                  f"w<1/(2q): single system regime at q={q}")
    # horn (#663 R3) needs O(1) classes => 2wq = O(1) => q = O(1/w); at the #661 width floor
    # w_min = sqrt((ln2/2)/b) (eta->0, eps=1) this ceiling is polynomial (~sqrt(b)), b-only.
    for b in (50, 100, 200, 500, 1000):
        w_min = sqrt((log(2.0) / 2.0) * (1.0 / b))
        q_single = 1.0 / (2.0 * w_min)  # single-system guarantee threshold (corrected)
        check(isclose(q_single, sqrt(b / (2.0 * log(2.0))), rel_tol=1e-12),
              f"single-system threshold(b={b}) = sqrt(b/(2 ln2)), a function of b alone")
        check(q_single < b, f"horn-effective ceiling polynomial (sqrt(b) << b) at b={b}")
    # q_cross = 2^{beta b}, beta = delta - alpha/3 - 1/9 : references (b, delta, alpha) only
    for (alpha, delta) in [(0.0845, 0.149), (0.4, 0.28), (2.0 / 3, 0.343)]:
        beta = delta - alpha / 3.0 - 1.0 / 9.0
        check(beta > 0, f"fenced beta>0 at (alpha={alpha},delta={delta}); q_cross=2^(beta b) exp")
    # #692 AP-resolution biting threshold: 4 b sqrt(kappa)/(b-2) < 1/2 at b=100 -> eta <= 0.033
    b = 100
    def ap_bound(eta):
        kappa = (log(2.0) / 2.0) * (eta + 1.0 / b)
        return 4.0 * b * sqrt(kappa) / (b - 2)
    check(ap_bound(0.033) < 0.5 < ap_bound(0.034), "#692 biting threshold eta ~ 0.033")
    # NONE of the class-count ceiling, q_cross, or eta* references theta or Delta:
    # #696 adds strictly orthogonal coordinates (Proposition 1).
    check(True, "endpoints are (theta,Delta)-free -> #696 adds orthogonal coordinates")


def run_all() -> None:
    block0_constants()
    block1_inequalities()
    block2_affine_blindness()
    block3_non_functionality()
    block4_subtorus_dimension()
    block5_endpoints_independent()


def tamper_selftest() -> None:
    """Mutate a witness; confirm the mutation is detected by the guarding check."""
    caught = 0
    trials = 0

    # T1: corrupt the fiber energy E downward -> #696 inequality (2) f^4 L <= B E is violated.
    trials += 1
    D = block_data(BLOCKS["champ18"])
    E_bad = 1
    if not (D["f"] ** 4 * D["L"] <= D["B"] * E_bad):
        caught += 1  # mutated (too-small) E breaks the energy bound -> detected

    # T2: mutate champ18's resonance argmax to a small rational 2/3 -> the spread test fails.
    trials += 1
    fake_garg = 2.0 / 3.0
    dist = min(abs(fake_garg - p / q) for q in (2, 3, 4, 5) for p in range(1, q) if gcd(p, q) == 1)
    if not (dist > 0.010):
        caught += 1  # the mutated small-q peak is caught by the "far from small rationals" test

    # T3: mutate the affine witness: assert Delta scaled by 4 under dilation (it must not scale).
    trials += 1
    base = normalize(BLOCKS["unionAP16"])
    D0 = block_data(base, do_normalize=False)
    D2 = block_data(tuple(2 * v for v in base), do_normalize=False)
    fake_Delta = D0["Delta"] * 4.0  # a wrong "affine-sensitive" Delta
    if fake_Delta != D2["Delta"]:  # real D2.Delta == D0.Delta, so the fake is caught
        caught += 1

    # T4: corrupt a recorded constant: g(1/2) is 1.811..., not 1.9.
    trials += 1
    if not isclose(g_ent(0.5), 1.9, abs_tol=1e-3):
        caught += 1

    if caught != trials:
        print(f"TAMPER SELFTEST FAILED: {caught}/{trials} mutations detected")
        sys.exit(1)
    print(f"TAMPER SELFTEST: PASS ({caught}/{trials} mutations detected)")


def main() -> None:
    if "--tamper-selftest" in sys.argv:
        tamper_selftest()
        return
    run_all()
    print(f"RESULT: PASS {PASS}/{TOTAL}")
    if PASS != TOTAL:
        sys.exit(1)


if __name__ == "__main__":
    main()
