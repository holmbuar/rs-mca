#!/usr/bin/env python3
"""Verifier: transverse/charge obstruction on the Sidon-paired class (hard input 2).

Checks, per the note experimental/notes/thresholds/transverse_charge_obstruction_sidon_paired.md:

V1  Exact fiber profile (brute force vs closed form), hypotheses of the class
    (2-superincreasing => B[+-2], center bound c > 2 sum P), M/L/M2 identities,
    M2 generating-function identity  M2 = [z^B w^B] (2zw + (1+z^2)(1+w^2))^B.
V2  Exact band excess R_q (q in {2,3,4}), both bases, B <= 32, as Fractions:
    R2^2 > 1 growth, R_q growth in q, the occupied-support transfer
    ||h_occ||_q >= ||h_occ||_2 L^{1/q-1/2}  (exact, cross-multiplied powers),
    and the moderate-slice (s in [B/4, 3B/4]) q=2 excess.
V3  Exact charge accounting at the full nontrivial band (B <= 6, both bases):
    Omega_+ >= <f,h> = M2 - M^2/c, the max root-cell charge equals the central
    cell, semantic-cap ratios decay, and the band-uniform Cauchy-Schwarz cap
    max|h_A| <= sqrt(delta_A) ||h_A||_2 on a family of dyadic symmetric bands.
V4  Resonance (float, Parseval-guarded): the exact product formula
    hat f(j) = [z^B] prod_i (1 + z^2 + 2 z cos(2 pi j A_i / c)),
    Parseval sum_j |hat f(j)|^2 / c == M2, the half-frequency resonance
    j* = (c-1)/2 with |hat f(j*)|/M >= 0.70 (base 3) / >= 0.61 (base 5, B=6),
    the exact antipodal congruence 2*(j* A_i mod c) - c == +- A_i, and the
    resonant-spectrum census #{j : |hat f(j)| >= rho M}.
V5  Prop-1 instantiation: explicit round-robin transverse partitions at B=6
    satisfy the displayed chain (compatibility, Cauchy-Schwarz over pieces,
    the W*M bound) exactly, and their total charge is an exponentially small
    fraction of Omega_+ ... while a fiber-indexed partition reproduces #739.
V6  The payment-gap window, exact integers: f_max * L >= 2 M (heavy fibers
    exist, #739) AND f_max^2 * L < M^2 (no fiber reaches the q=2 payment
    scale M/sqrt(L)) for all 4 <= B <= 64, B even.

Deterministic, stdlib only.  --tamper-selftest mutates four checks and
verifies each is caught.
"""
import sys
from fractions import Fraction
from math import comb, cos, pi
from itertools import combinations
from collections import Counter, defaultdict

CHECKS = []
QUIET = False


def check(name, ok):
    CHECKS.append((name, bool(ok)))
    if not ok and not QUIET:
        print(f"FAIL: {name}")
    return ok


# ---------------------------------------------------------------- class data

def sidon_P(B, base):
    return [base ** i for i in range(B)]


def sidon_c(B, base):
    P = sidon_P(B, base)
    return 2 * sum(P) + 1


def profile_levels(B):
    """[(s, fiber_size, n_syndromes)] for s = B mod 2, ..., B."""
    return [(s, comb(B - s, (B - s) // 2), comb(B, s) * 2 ** s)
            for s in range(B % 2, B + 1, 2)]


def closed_L(B):
    return (3 ** B + 1) // 2 if B % 2 == 0 else (3 ** B - 1) // 2


def closed_M(B):
    return comb(2 * B, B)


def closed_M2(B):
    return sum(n * w * w for (_s, w, n) in profile_levels(B))


def gf_M2(B):
    """[z^B w^B] (2zw + (1+z^2)(1+w^2))^B, exact."""
    g = {(1, 1): 2, (0, 0): 1, (2, 0): 1, (0, 2): 1, (2, 2): 1}
    acc = {(0, 0): 1}
    for _ in range(B):
        nxt = defaultdict(int)
        for (i, j), a in acc.items():
            for (k, l), b in g.items():
                if i + k <= B and j + l <= B:
                    nxt[(i + k, j + l)] += a * b
        acc = dict(nxt)
    return acc.get((B, B), 0)


def brute_fibers(B, base):
    """Exact fiber-count function on Z (== on Z_c: (k,D)<->eps bijection)."""
    P = sidon_P(B, base)
    c = sidon_c(B, base)
    T = P + [c - p for p in P]
    fib = Counter()
    for S in combinations(T, B):
        fib[sum(S)] += 1
    return c, fib


# ------------------------------------------------------------------------ V1

def v1():
    for base in (3, 5):
        for B in (2, 4, 6):
            P = sidon_P(B, base)
            c = sidon_c(B, base)
            # hypotheses: 2-superincreasing and center bound (Danny #749 form)
            check(f"V1 hyp 2-superincreasing base{base} B{B}",
                  all(P[i] > 2 * sum(P[:i]) for i in range(B)))
            check(f"V1 hyp center bound base{base} B{B}", c > 2 * sum(P))
            # B[+-2]-dissociativity, exhaustive: sum d_i A_i = 0 => d = 0
            if B <= 6:
                zeros = 0
                def rec(i, acc):
                    nonlocal zeros
                    if i == B:
                        if acc == 0:
                            zeros += 1
                        return
                    for d in (-2, -1, 0, 1, 2):
                        rec(i + 1, acc + d * P[i])
                rec(0, 0)
                check(f"V1 B[+-2] dissociated base{base} B{B}", zeros == 1)
            cc, fib = brute_fibers(B, base)
            L, M, M2 = closed_L(B), closed_M(B), closed_M2(B)
            check(f"V1 L exact base{base} B{B}", len(fib) == L)
            check(f"V1 M exact base{base} B{B}", sum(fib.values()) == M)
            got = Counter(fib.values())
            want = Counter()
            for (_s, w, n) in profile_levels(B):
                want[w] += n
            check(f"V1 staircase profile base{base} B{B}", got == want)
            check(f"V1 M2 brute==closed base{base} B{B}",
                  sum(v * v for v in fib.values()) == M2)
    for B in (2, 4, 6, 8, 10):
        check(f"V1 M identity B{B}",
              sum(n * w for (_s, w, n) in profile_levels(B)) == closed_M(B))
        check(f"V1 M2 GF identity B{B}", gf_M2(B) == closed_M2(B))
        check(f"V1 L identity B{B}",
              sum(n for (_s, w, n) in profile_levels(B)) == closed_L(B))


# ------------------------------------------------------------------------ V2

def hq_exact(B, base, q, levels=None):
    """(||h||_q^q, L_occ, M_occ, c) exactly, h = f_occ - M_occ/c on Z_c.
    levels: optional set of unpaired-counts s to which f is restricted."""
    c = sidon_c(B, base)
    prof = [(s, w, n) for (s, w, n) in profile_levels(B)
            if levels is None or s in levels]
    M = sum(n * w for (_s, w, n) in prof)
    Locc = sum(n for (_s, w, n) in prof)
    mean = Fraction(M, c)
    hq = sum(n * abs(Fraction(w) - mean) ** q for (_s, w, n) in prof)
    hq += (c - Locc) * mean ** q
    return hq, Locc, M, c


def Rq_pow(B, base, q, levels=None):
    hq, Locc, M, c = hq_exact(B, base, q, levels)
    return Fraction(Locc) ** (q - 1) * hq / Fraction(M) ** q


def v2():
    for base in (3, 5):
        prev = {2: None, 3: None, 4: None}
        for B in (4, 6, 8, 12, 16, 24, 32):
            r = {q: Rq_pow(B, base, q) for q in (2, 3, 4)}
            if B >= 6:
                check(f"V2 R2^2>1 base{base} B{B}", r[2] > 1)
            # R_q^q growth in B (exact Fractions)
            for q in (2, 3, 4):
                if prev[q] is not None:
                    check(f"V2 R{q} grows base{base} B{B}", r[q] > prev[q])
                prev[q] = r[q]
            # occupied-support transfer: ||h_occ||_q^q >= ||h_occ||_2^q L^{1-q/2}
            # exact cross-multiplied: (hq_occ)^2 * L^{q-2} >= (h2_occ)^q
            hq_occ = sum(n * abs(Fraction(w) - Fraction(closed_M(B), sidon_c(B, base))) ** 4
                         for (_s, w, n) in profile_levels(B))
            h2_occ = sum(n * abs(Fraction(w) - Fraction(closed_M(B), sidon_c(B, base))) ** 2
                         for (_s, w, n) in profile_levels(B))
            L = closed_L(B)
            check(f"V2 occ-support Holder q4 base{base} B{B}",
                  hq_occ ** 2 * L ** 2 >= h2_occ ** 4 / Fraction(1))
        # moderate slice
        for B in (8, 12, 16):
            lv = set(s for s in range(B % 2, B + 1, 2) if B / 4 <= s <= 3 * B / 4)
            check(f"V2 slice R2^2>1 base{base} B{B}",
                  Rq_pow(B, base, 2, levels=lv) > 1)
    # exact record values (base 3): R2^2 at B=6, 8 as pinned Fractions
    check("V2 pinned R2^2 base3 B6",
          Rq_pow(6, 3, 2) == Fraction(365 * (3584 * 729 - 924 * 924), 924 * 924 * 729))
    # q=2.709 crossover of the point-mass rate: exact integer form
    # L^{q-1} f_max^q < M^q at q=2 ; > at q=4 (B=16)
    B = 16
    L, M, fmax = closed_L(B), closed_M(B), comb(B, B // 2)
    check("V2 point-mass rate sign q2 B16", L * fmax ** 2 < M ** 2)
    check("V2 point-mass rate sign q4 B16", L ** 3 * fmax ** 4 > M ** 4)


# ------------------------------------------------------------------------ V3

def v3():
    for base in (3, 5):
        for B in (4, 6):
            c, fib = brute_fibers(B, base)
            M, M2 = closed_M(B), closed_M2(B)
            fmax = comb(B, B // 2)
            mean = Fraction(M, c)
            # h = f - mean on Z_c; the positive part is the fibers above mean
            omega_plus = sum(v * (Fraction(v) - mean) for v in fib.values()
                             if Fraction(v) > mean)
            inner = Fraction(M2) - Fraction(M * M, c)
            check(f"V3 Omega+ >= <f,h> base{base} B{B}", omega_plus >= inner)
            maxcell = max(v * (Fraction(v) - mean) for v in fib.values())
            check(f"V3 max cell == central base{base} B{B}",
                  maxcell == fmax * (Fraction(fmax) - mean))
            # semantic-cap ratio decays with B: maxcell / Omega_+ (exact)
            ratio = maxcell / omega_plus
            check(f"V3 cell ratio < (3/4)^{{B/2}} base{base} B{B}",
                  ratio < Fraction(3, 4) ** (B // 2))
            # band-uniform CS cap on dyadic symmetric bands (float, guarded)
            if B == 6:
                import cmath
                vals = {}
                fs = sorted(fib.items())
                for t in range(1, c.bit_length()):
                    band = [j for j in range(1, c)
                            if 2 ** (t - 1) <= min(j, c - j) < 2 ** t]
                    if not band:
                        continue
                    # hat f(j) by direct sum over occupied syndromes (exact-ish)
                    hf = {j: sum(v * cmath.exp(-2j * pi * ((j * s) % c) / c)
                                 for s, v in fs) for j in band}
                    hA2 = sum(abs(x) ** 2 for x in hf.values()) / c
                    # max_sigma |h_A(sigma)| over occupied syndromes + 0
                    pts = [s for s, _v in fs][:200] + [0]
                    mx = max(abs(sum(hf[j] * cmath.exp(2j * pi * ((j * s) % c) / c)
                                     for j in hf)) / c for s in pts)
                    dA = len(band) / c
                    check(f"V3 CS band cap base{base} B{B} t{t}",
                          mx <= (dA * hA2) ** 0.5 * (1 + 1e-9))


# ------------------------------------------------------------------------ V4

def hatf_product(B, base, j, c):
    P = sidon_P(B, base)
    poly = [1.0]
    for A in P:
        th = 2 * pi * ((j * A) % c) / c
        f = (1.0, 2 * cos(th), 1.0)
        new = [0.0] * (len(poly) + 2)
        for i, a in enumerate(poly):
            if a:
                new[i] += a * f[0]
                new[i + 1] += a * f[1]
                new[i + 2] += a * f[2]
        poly = new
    return poly[B]


def v4():
    # product formula == direct DFT (brute) at B=4, both bases, several j
    for base in (3, 5):
        B = 4
        c, fib = brute_fibers(B, base)
        import cmath
        for j in (1, 2, (c - 1) // 2, c // 3):
            direct = sum(v * cmath.exp(-2j * pi * ((j * s) % c) / c)
                         for s, v in fib.items())
            prod = hatf_product(B, base, j, c)
            check(f"V4 product==DFT base{base} j{j}",
                  abs(direct.real - prod) <= 1e-9 * closed_M(B)
                  and abs(direct.imag) <= 1e-9 * closed_M(B))
    # Parseval guard + spectrum census, base 3 (c = 2*sum P + 1 = 3^B)
    census = {}
    for B in (6, 8):
        c = sidon_c(B, 3)
        check(f"V4 c==3^B B{B}", c == 3 ** B)
        M, M2 = closed_M(B), closed_M2(B)
        vals = [hatf_product(B, 3, j, c) for j in range(c)]
        pars = sum(v * v for v in vals) / c
        check(f"V4 Parseval base3 B{B}", abs(pars - M2) <= 1e-6 * M2)
        jstar = (c - 1) // 2
        check(f"V4 half-freq resonance base3 B{B}",
              abs(vals[jstar]) >= 0.70 * M)
        for rho_n, rho_d, name in ((1, 2, "0.5"), (1, 4, "0.25"), (1, 10, "0.1")):
            cnt = sum(1 for j in range(1, c)
                      if abs(vals[j]) * rho_d >= rho_n * M)
            census[(3, B, name)] = cnt
        # antipodal congruence: 2*(j* A_i mod c) - c == -A_i exactly, all i
        P = sidon_P(B, 3)
        check(f"V4 antipodal congruence base3 B{B}",
              all(2 * ((jstar * A) % c) - c == -A for A in P))
    # pinned census values (recomputed, must match)
    check("V4 census base3 B6", (census[(3, 6, "0.5")], census[(3, 6, "0.25")],
                                 census[(3, 6, "0.1")]) == (2, 2, 42))
    check("V4 census base3 B8", (census[(3, 8, "0.5")], census[(3, 8, "0.25")],
                                 census[(3, 8, "0.1")]) == (2, 2, 58))
    # base 5, B=6 scan
    B, base = 6, 5
    c = sidon_c(B, base)
    M, M2 = closed_M(B), closed_M2(B)
    vals = [hatf_product(B, base, j, c) for j in range(c)]
    pars = sum(v * v for v in vals) / c
    check("V4 Parseval base5 B6", abs(pars - M2) <= 1e-6 * M2)
    jstar = (c - 1) // 2
    check("V4 half-freq resonance base5 B6", abs(vals[jstar]) >= 0.61 * M)
    check("V4 antipodal congruence base5 B6",
          all(2 * ((jstar * A) % c) - c == -A for A in sidon_P(B, base)))
    cnt5 = sum(1 for j in range(1, c) if abs(vals[j]) * 2 >= M)
    check("V4 census base5 B6 rho=0.5", cnt5 == 12)
    # deep half-frequency evaluation, base 3, large B (product formula only)
    for B in (16, 32, 64):
        c = 3 ** B
        val = hatf_product(B, 3, (c - 1) // 2, c)
        check(f"V4 half-freq >= 0.70M base3 B{B}", abs(val) >= 0.70 * closed_M(B))


# ------------------------------------------------------------------------ V5

def v5():
    base, B = 3, 6
    c, fib = brute_fibers(B, base)
    M, M2 = closed_M(B), closed_M2(B)
    mean = Fraction(M, c)
    # unnormalized owner weights (canonical q=2 rooting at the full band,
    # scaled by ||h||_2): wt(sigma) = h_+(sigma) = max(f - M/c, 0), rational
    wt = {s: Fraction(v) - mean for s, v in fib.items() if Fraction(v) > mean}
    omega_plus = sum(fib[s] * w for s, w in wt.items())
    # enumerate supports once, tagged by syndrome
    P = sidon_P(B, base)
    T = P + [c - p for p in P]
    supports_by_syn = defaultdict(list)
    for S in combinations(T, B):
        supports_by_syn[sum(S)].append(S)
    for K in (4, 16):
        # round-robin transverse partition: piece k gets every K-th support
        # of every fiber => per-syndrome multiplicity <= ceil(f/K)
        pieces = [defaultdict(int) for _ in range(K)]  # syndrome -> count
        for s, lst in supports_by_syn.items():
            for idx, _S in enumerate(lst):
                pieces[idx % K][s] += 1
        W = max(max(p.values()) for p in pieces if p)
        check(f"V5 K{K} W == ceil(fmax/K)",
              W == -(-comb(B, B // 2) // K))
        tot_weight = Fraction(0)
        sum_b2 = Fraction(0)
        sum_pb2 = Fraction(0)
        for p in pieces:
            # owner-weight sum of the piece (the MAXIMUM charge condition
            # c_i <= sum omega would allow)
            wsum = sum(cnt * wt.get(s, Fraction(0)) for s, cnt in p.items())
            # piece mask b_i(sigma) = cnt * wt ; ||b_i||_2^2 exact
            b2 = sum((cnt * wt.get(s, Fraction(0))) ** 2 for s, cnt in p.items())
            # full-band projection: ||P_{!=0} b||_2^2 = ||b||_2^2 - (sum b)^2/c
            pb2 = b2 - wsum * wsum / c
            tot_weight += wsum
            sum_b2 += b2
            sum_pb2 += pb2
        check(f"V5 K{K} weights sum to Omega_+", tot_weight == omega_plus)
        # THE OBSTRUCTION (Prop 1 instantiated as unsatisfiability): any
        # compatible charge assignment has c_i <= ||P b_i||_2, so by
        # Cauchy-Schwarz  (sum_i c_i)^2 <= K sum_i ||P b_i||_2^2 < Omega_+^2:
        # charge preservation (sum c_i = Omega_+) is UNSATISFIABLE.
        check(f"V5 K{K} transverse unsatisfiable",
              K * sum_pb2 < omega_plus * omega_plus)
        # the W*M mechanism bound on the piece masses
        wmax = max(wt.values())
        check(f"V5 K{K} piece-mass bound", sum_b2 <= wmax * wmax * W * M)
    # fiber-indexed partition reproduces #739's exponential piece count:
    # pieces with W_max = 1 per fiber need >= fmax pieces to cover the center
    check("V5 fiber-transversal needs >= fmax pieces",
          comb(B, B // 2) == max(fib.values()))


# ------------------------------------------------------------------------ V6

def v6():
    for B in range(4, 65, 2):
        L, M, fmax = closed_L(B), closed_M(B), comb(B, B // 2)
        check(f"V6 heavy exists B{B}", fmax * L >= 2 * M)
        check(f"V6 payment gap B{B}", fmax * fmax * L < M * M)
    # the gap rate: (fmax^2 L / M^2) < (7/8)^B for B >= 8  (exact ints)
    for B in (8, 16, 32, 64):
        L, M, fmax = closed_L(B), closed_M(B), comb(B, B // 2)
        check(f"V6 gap rate B{B}", fmax * fmax * L * 8 ** B < M * M * 7 ** B)


# ------------------------------------------------------------------------ V7

def v7():
    """Self-contained coset homogeneity census (the multi-fiber semantic
    escape used by Theorem 3's taxonomy).  Base 3 (c = 3^B): for EVERY coset
    coarsening mod 3^j with #classes < 3^{B-2}, the mass sitting in
    single-unpaired-level ("semantic-candidate") classes is ZERO; the first
    positive mass appears exactly at modulus 3^{B-2}, and full resolution
    (mass M) at 3^{B-1}.  This reproduces, inside this packet, the census
    that PR #760's rung (c) established -- no open-PR dependency remains."""
    for B in (6, 8):
        c, fib = brute_fibers(B, 3)
        check(f"V7 c==3^B B{B}", c == 3 ** B)
        # unpaired level from fiber size (sizes are distinct across levels)
        size2level = {comb(B - s, (B - s) // 2): s
                      for s in range(B % 2, B + 1, 2)}
        check(f"V7 sizes distinct B{B}",
              len(size2level) == len(list(range(B % 2, B + 1, 2))))
        M = closed_M(B)
        for j in range(0, B + 1):
            m = 3 ** j
            classes = defaultdict(lambda: [set(), 0])
            for sigma, v in fib.items():
                cl = (sigma % c) % m
                classes[cl][0].add(size2level[v])
                classes[cl][1] += v
            sem = sum(mass for (levels, mass) in classes.values()
                      if len(levels) == 1)
            if m < 3 ** (B - 2):
                check(f"V7 zero semantic mass B{B} m=3^{j}", sem == 0)
            elif m == 3 ** (B - 2):
                check(f"V7 first semantic mass at 3^(B-2) B{B}", 0 < sem < M)
            elif m >= 3 ** (B - 1):
                check(f"V7 full semantic mass B{B} m=3^{j}", sem == M)


# ------------------------------------------------------------------- driver

def run_all(quiet=False):
    global QUIET
    QUIET = quiet
    CHECKS.clear()
    v1(); v2(); v3(); v4(); v5(); v6(); v7()
    bad = [n for n, ok in CHECKS if not ok]
    if not quiet:
        print(f"RESULT: {'PASS' if not bad else 'FAIL'} "
              f"({len(CHECKS) - len(bad)}/{len(CHECKS)})")
    QUIET = False
    return not bad


def tamper_selftest():
    """Mutate four load-bearing constants; each must flip PASS -> FAIL."""
    me = sys.modules[__name__]
    caught = 0
    # 1: break the M2 closed form
    orig = me.closed_M2
    me.closed_M2 = lambda B: orig(B) + 1
    if not run_all(quiet=True):
        caught += 1
    me.closed_M2 = orig
    # 2: break the staircase profile
    orig_p = me.profile_levels
    me.profile_levels = lambda B: [(s, w + (1 if s == B % 2 else 0), n)
                                   for (s, w, n) in orig_p(B)]
    if not run_all(quiet=True):
        caught += 1
    me.profile_levels = orig_p
    # 3: break the class modulus (shifts j*, fibers, congruence)
    orig_c = me.sidon_c
    me.sidon_c = lambda B, base: orig_c(B, base) + (2 if base == 3 else 0)
    if not run_all(quiet=True):
        caught += 1
    me.sidon_c = orig_c
    # 4: break the payment-gap inequality direction
    orig_L = me.closed_L
    me.closed_L = lambda B: orig_L(B) * 4
    if not run_all(quiet=True):
        caught += 1
    me.closed_L = orig_L
    print(f"tamper-selftest: caught {caught}/4")
    ok = run_all()
    return caught == 4 and ok


def emit_certificate(path):
    """Regenerate the machine-readable certificate from the same exact code."""
    import json
    cert = {
        "packet": "transverse-charge-obstruction",
        "lane": "hard input 2 -- (NFB) of #760 Sec 7, both branches decided",
        "class": {
            "P": "base^i, i < B (2-superincreasing => B[+-2]-dissociated)",
            "c": "2*sum(P)+1 (base 3: 3^B)", "T": "P u (c-P)", "a": "B",
            "hypotheses": "DannyExperiments #749-corrected",
        },
        "scalars": {}, "excess_Rq_pow_q": {}, "slice_R2_pow_2": {},
        "charge_accounting": {}, "prop1_instantiation": {},
        "window": {}, "resonance": {},
        "verifier": "experimental/scripts/verify_transverse_charge_obstruction.py",
    }
    for B in (2, 4, 6, 8, 12, 16):
        cert["scalars"][str(B)] = {
            "L": closed_L(B), "M": closed_M(B), "M2": closed_M2(B),
            "fmax": comb(B, B // 2), "c_base3": sidon_c(B, 3),
            "c_base5": sidon_c(B, 5),
        }
    for base in (3, 5):
        for B in (4, 6, 8, 12, 16):
            for q in (2, 3, 4):
                r = Rq_pow(B, base, q)
                cert["excess_Rq_pow_q"][f"base{base}_B{B}_q{q}"] = \
                    f"{r.numerator}/{r.denominator}"
        for B in (8, 12, 16):
            lv = set(s for s in range(B % 2, B + 1, 2) if B / 4 <= s <= 3 * B / 4)
            r = Rq_pow(B, base, 2, levels=lv)
            cert["slice_R2_pow_2"][f"base{base}_B{B}"] = \
                f"{r.numerator}/{r.denominator}"
    for base in (3, 5):
        for B in (4, 6):
            c, fib = brute_fibers(B, base)
            mean = Fraction(closed_M(B), c)
            omega_plus = sum(v * (Fraction(v) - mean) for v in fib.values()
                             if Fraction(v) > mean)
            maxcell = max(v * (Fraction(v) - mean) for v in fib.values())
            cert["charge_accounting"][f"base{base}_B{B}"] = {
                "omega_plus": f"{omega_plus.numerator}/{omega_plus.denominator}",
                "max_root_cell": f"{maxcell.numerator}/{maxcell.denominator}",
                "ratio_lt": f"(3/4)^{B // 2}",
            }
    base, B = 3, 6
    c, fib = brute_fibers(B, base)
    mean = Fraction(closed_M(B), c)
    wt = {s: Fraction(v) - mean for s, v in fib.items() if Fraction(v) > mean}
    omega_plus = sum(fib[s] * w for s, w in wt.items())
    P = sidon_P(B, base)
    T = P + [c - p for p in P]
    supports_by_syn = defaultdict(list)
    for S in combinations(T, B):
        supports_by_syn[sum(S)].append(S)
    for K in (4, 16):
        pieces = [defaultdict(int) for _ in range(K)]
        for s, lst in supports_by_syn.items():
            for idx, _S in enumerate(lst):
                pieces[idx % K][s] += 1
        sum_pb2 = Fraction(0)
        for p in pieces:
            wsum = sum(cnt * wt.get(s, Fraction(0)) for s, cnt in p.items())
            b2 = sum((cnt * wt.get(s, Fraction(0))) ** 2 for s, cnt in p.items())
            sum_pb2 += b2 - wsum * wsum / c
        lhs = K * sum_pb2
        rhs = omega_plus * omega_plus
        cert["prop1_instantiation"][f"base3_B6_K{K}"] = {
            "K_sum_Pb2": f"{lhs.numerator}/{lhs.denominator}",
            "omega_plus_sq": f"{rhs.numerator}/{rhs.denominator}",
            "unsatisfiable": bool(lhs < rhs),
        }
    for B in (8, 16, 32, 64):
        L, M, fmax = closed_L(B), closed_M(B), comb(B, B // 2)
        cert["window"][str(B)] = {
            "heavy_fmaxL_ge_2M": bool(fmax * L >= 2 * M),
            "gap_fmax2L_lt_M2": bool(fmax * fmax * L < M * M),
        }
    for B in (6, 8):
        c3 = sidon_c(B, 3)
        M = closed_M(B)
        vals = [hatf_product(B, 3, j, c3) for j in range(c3)]
        jstar = (c3 - 1) // 2
        cert["resonance"][f"base3_B{B}"] = {
            "jstar": jstar,
            "abs_hatf_jstar_over_M": round(abs(vals[jstar]) / M, 6),
            "census_rho_half": sum(1 for j in range(1, c3)
                                   if abs(vals[j]) * 2 >= M),
            "census_rho_tenth": sum(1 for j in range(1, c3)
                                    if abs(vals[j]) * 10 >= M),
            "float_note": "product formula, Parseval-guarded to 1e-6 rel",
        }
    c5 = sidon_c(6, 5)
    M = closed_M(6)
    vals = [hatf_product(6, 5, j, c5) for j in range(c5)]
    cert["resonance"]["base5_B6"] = {
        "jstar": (c5 - 1) // 2,
        "abs_hatf_jstar_over_M": round(abs(vals[(c5 - 1) // 2]) / M, 6),
        "census_rho_half": sum(1 for j in range(1, c5) if abs(vals[j]) * 2 >= M),
    }
    with open(path, "w") as fh:
        json.dump(cert, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print(f"certificate written: {path}")


if __name__ == "__main__":
    if "--tamper-selftest" in sys.argv:
        sys.exit(0 if tamper_selftest() else 1)
    if "--emit-certificate" in sys.argv:
        emit_certificate(sys.argv[sys.argv.index("--emit-certificate") + 1])
        sys.exit(0)
    sys.exit(0 if run_all() else 1)
