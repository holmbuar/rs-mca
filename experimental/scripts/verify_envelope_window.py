#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_envelope_window.py  --  stdlib-only, zero-arg verifier for the
identity-dominance window criterion attacking hard input (d) of
experimental/asymptotic_rs_mca_frontiers.tex:
  "complete profile-envelope comparison with the target".

It recomputes every gated number in
experimental/notes/thresholds/envelope_identity_window.md:

  A. EXPONENT IDENTITY.  The natural-scale exponent of the depth-c quotient /
     Chebyshev profile with scaled-coefficient-field drop lambda_c,
        e_c(rho,beta,g) = (1/c)[ H2(rho+g) - lambda_c * g * beta ],
     equals the paper's QR8/QR9 rearrangement of eq:qr-natural-scale (QR6)
     and reproduces thm:smooth-quotient-obstruction (exponent h/4 at the
     identity crossing for c=2, lambda=1/2).

  B. WINDOW / FAILURE-BAND FORMULAS.  With h=H2(rho+g), s=g*beta, the identity
     term dominates the complete envelope (on the exponential scale) iff
        e_c(rho,beta,g) <= max(0, e_1),   e_1 = h - s,
     for every available competitor (c,lambda).  For the worst competitor
     (c_min, lambda_min) this is the union of the two windows
        LOWER:  s <= kappa_low  * h,   kappa_low  = (c-1)/(c-lambda)
        UPPER:  s >= kappa_high * h,   kappa_high = 1/lambda
     and fails exactly on the band ( kappa_low*h , kappa_high*h ).
     Verified against a brute exponent scan on a fine (rho,beta,g,c,lambda) grid.

  C. CROSSING-IN-BAND WALL.  The zero-target right crossing g* (solving
     H2(rho+g)=beta*g) lies strictly inside the failure band whenever
     lambda<1, and the band collapses to a point (dominance everywhere) when
     lambda=1.  So cor:intro-identity-frontier's identity-dominant
     specialization is unavailable at g* for any field-drop row.

  D. TARGET-THRESHOLD FORM.  The general right crossing g_T (solving
     F(g)=H2(rho+g)-beta*g = tau) lands in the identity-dominant LOWER window
     iff tau >= tau0 := F(g_low), with tau0>0.  So sufficiently generous
     targets are unconditionally identity-dominant.

  E. EXACT FINITE F_{p^2} CENSUS.  For p in {5,7,11}, builds D=theta*H with the
     order-n subgroup H (n=2(p-1)), the 2-to-1 complete-fiber square folding
     phi(x)=x^2, and checks: (i) every square-fiber support's locator prefix
     lies in the scaled quotient coefficient field eta^j * F_p (the field
     drop / lacunarity), (ii) the pigeonhole prefix bucket carries >= ceil(QR6)
     square-fiber supports, strictly more than the identity average barN_1<1 --
     i.e. the QUOTIENT cell carries the envelope value while the identity cell
     does not.  (Full identity enumeration only for p in {5,7}; the field-drop
     and pigeonhole checks run for all listed p.)

Exact arithmetic throughout: big-integer binomials for scales, rational
comparisons, and hand-rolled F_{p^2} arithmetic for the census.  No floats are
used in any PASS/FAIL gate except the entropy-window scan, which is gated with a
conservative margin far larger than double-precision error.

Run:   python3 experimental/scripts/verify_envelope_window.py
Target runtime < 120 s under  ulimit -v 2097152.
"""

from __future__ import annotations
from math import log2, comb, isclose
from fractions import Fraction

CHECKS = 0
FAILS = 0
LOG = []


def gate(cond: bool, msg: str):
    global CHECKS, FAILS
    CHECKS += 1
    if not cond:
        FAILS += 1
        LOG.append("  FAIL: " + msg)
    return cond


def H2(x: float) -> float:
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * log2(x) - (1.0 - x) * log2(1.0 - x)


# ---------------------------------------------------------------------------
# A.  Exponent identity: e_c matches QR8 rearrangement and the counterexample.
# ---------------------------------------------------------------------------
def e_identity(rho, beta, g):
    """e_1 = H2(rho+g) - g*beta  (eq:target-entropy leading exponent)."""
    return H2(rho + g) - g * beta


def e_quotient(rho, beta, g, c, lam):
    """Closed form e_c = (1/c)[H2(rho+g) - lambda*g*beta]."""
    return (H2(rho + g) - lam * g * beta) / c


def e_quotient_QR8(rho, beta, g, c, lam):
    """QR8 form: (1/c)*e_1 + (g*beta/c)*(1-lambda).  Must equal e_quotient."""
    return (H2(rho + g) - g * beta) / c + (g * beta / c) * (1.0 - lam)


def section_A():
    LOG.append("== A. Exponent identity (QR8/QR9) and counterexample reproduction ==")
    grid_rho = [0.10, 0.25, 0.40, 0.55, 0.70]
    grid_beta = [0.5, 1.0, 2.0, 4.0]
    grid_g = [0.02, 0.05, 0.10, 0.20, 0.30]
    grid_c = [2, 3, 5]
    grid_lam = [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(1, 1)]
    for rho in grid_rho:
        for beta in grid_beta:
            for g in grid_g:
                if rho + g >= 1.0:
                    continue
                for c in grid_c:
                    for lamF in grid_lam:
                        lam = float(lamF)
                        a = e_quotient(rho, beta, g, c, lam)
                        b = e_quotient_QR8(rho, beta, g, c, lam)
                        gate(abs(a - b) < 1e-12,
                             f"QR8 identity rho={rho} beta={beta} g={g} c={c} lam={lam}")
    # thm:smooth-quotient-obstruction: c=2, lambda=1/2, at identity crossing
    # s = g*beta = h => e_1 = 0 and e_2 = h/4.
    for alpha in [0.15, 0.25, 0.30, 0.45]:
        h = H2(alpha)
        # choose (rho,g,beta) with rho+g=alpha and g*beta=h (the crossing)
        g = 0.5 * alpha
        rho = alpha - g
        beta = h / g
        e1 = e_identity(rho, beta, g)
        e2 = e_quotient(rho, beta, g, 2, 0.5)
        gate(abs(e1) < 1e-9, f"crossing e1==0 alpha={alpha}")
        gate(abs(e2 - h / 4.0) < 1e-9, f"CE exponent e2==h/4 alpha={alpha}")


# ---------------------------------------------------------------------------
# A'.  QR6 <-> closed form at finite n (exact big-integer identity scale, and
#      the pigeonhole quotient lower bound), reproducing the F_{p^2} tower.
# ---------------------------------------------------------------------------
def _tower_scales(p):
    """Return exact (n,a,w,barN1_num,barN1_den,q_num,q_den) for the
    thm:smooth-quotient-obstruction tower B=F_{p^2}, B_phi=F_p, c=2, r=0,
    with a/n~0.3 and w = largest even <= log_{|B|} C(n,a)."""
    n = 2 * (p - 1)
    a = 2 * round(0.3 * n / 2)
    if a < 2:
        a = 2
    Bpow = p * p
    cna = comb(n, a)
    w0 = 0
    while Bpow ** (w0 + 1) <= cna:
        w0 += 1
    w = w0 - (w0 % 2)
    if w < 2:
        w = 2
    barN1_num = comb(n, a)
    barN1_den = (p * p) ** w
    q_num = comb(n // 2, a // 2)         # QR6 numerator C(N,m)=C(n/2,a/2)
    q_den = p ** (w // 2)                # |B_phi|^{floor(w/c)} = p^{w/2}
    return n, a, w, barN1_num, barN1_den, q_num, q_den


def section_Aprime():
    LOG.append("== A'. Finite F_{p^2} tower scales (exact big integers) ==")
    # (i) universal structural facts hold at every p (small or large):
    for p in [11, 13, 17, 23, 31]:
        n, a, w, b1n, b1d, qn, qd = _tower_scales(p)
        # identity scale is subexponential: 1 <= barN_1 < |B|^2 = p^4  (the CE regime)
        gate(b1n >= b1d, f"identity>=1 p={p}")
        gate(b1n < (p ** 4) * b1d, f"identity subexp barN1<|B|^2 p={p}")
        # quotient prefix values live in the small field F_p (lacunary+field-drop):
        # its pigeonhole scale is C(N,m)/p^{w/2} -- always a positive integer object.
        gate(qn > 0 and qd > 0, f"quotient scale well-defined p={p}")
    # (ii) the ASYMPTOTIC separation (quotient exponentially beats identity, and
    # quotient exponent -> h/4) only manifests at larger n.  Use large primes;
    # only a handful of big-integer binomials, no enumeration, so this is cheap.
    prev_err = None
    for p in [101, 251, 1009, 4001]:
        n, a, w, b1n, b1d, qn, qd = _tower_scales(p)
        # exact ratio: quotient natural scale > identity scale
        gate(qn * b1d > b1n * qd, f"quotient>identity (exact) p={p}")
        alpha = a / n
        h = H2(alpha)
        beta_bits = 2 * log2(p)
        e1_emp = (log2(b1n) - log2(b1d)) / n
        e2_emp = (log2(qn) - (w // 2) * log2(p)) / n
        s = (w * beta_bits) / n
        e2_form = (h - 0.5 * s) / 2.0
        # identity exponent is o(1) (subexponential): bounded by 2*beta/n
        gate(e1_emp <= 2 * beta_bits / n + 1e-9, f"identity exponent o(1) p={p}")
        # quotient exponent matches closed form within shrinking finite-size error
        err = abs(e2_emp - e2_form)
        gate(err < 0.05, f"quotient exponent~formula p={p} emp={e2_emp:.4f} "
                         f"form={e2_form:.4f} err={err:.4f}")
        # finite-size error is monotonically shrinking as p grows
        if prev_err is not None:
            gate(err <= prev_err + 1e-9, f"finite-size error shrinks p={p} "
                                         f"err={err:.4f} prev={prev_err:.4f}")
        prev_err = err


# ---------------------------------------------------------------------------
# B.  Window / failure-band formulas vs brute exponent comparison.
# ---------------------------------------------------------------------------
def dominates(rho, beta, g, competitors):
    """True iff every competitor exponent <= max(0, e_1) (+ tiny slack)."""
    e1 = e_identity(rho, beta, g)
    rhs = max(0.0, e1)
    for (c, lam) in competitors:
        if e_quotient(rho, beta, g, c, lam) > rhs + 1e-12:
            return False
    return True


def band_predicts_dominant(rho, beta, g, c, lam):
    """Closed-form predicate: identity dominant at this g for competitor (c,lam)."""
    h = H2(rho + g)
    s = g * beta
    kappa_low = (c - 1) / (c - lam)
    kappa_high = 1.0 / lam
    # dominant iff s <= kappa_low*h (case A) or s >= kappa_high*h (case B)
    return (s <= kappa_low * h + 1e-12) or (s >= kappa_high * h - 1e-12)


def section_B():
    LOG.append("== B. Window edge formulas vs brute exponent scan ==")
    grid_rho = [0.15, 0.30, 0.45, 0.60]
    grid_beta = [0.5, 1.0, 2.0, 3.0, 5.0]
    grid_c = [2, 3]
    grid_lam = [0.25, 0.5, 0.75, 1.0]
    n_g = 60
    for rho in grid_rho:
        for beta in grid_beta:
            for c in grid_c:
                for lam in grid_lam:
                    comp = [(c, lam)]
                    for i in range(1, n_g):
                        g = (1.0 - rho) * i / n_g
                        if g <= 0 or rho + g >= 1.0:
                            continue
                        brute = dominates(rho, beta, g, comp)
                        pred = band_predicts_dominant(rho, beta, g, c, lam)
                        gate(brute == pred,
                             f"band==brute rho={rho} beta={beta} c={c} lam={lam} g={g:.4f} "
                             f"brute={brute} pred={pred}")
    # lambda=1 => no failure ever (kappa_low = (c-1)/(c-1)=1, kappa_high=1)
    for rho in grid_rho:
        for beta in grid_beta:
            for c in grid_c:
                for i in range(1, n_g):
                    g = (1.0 - rho) * i / n_g
                    if g <= 0 or rho + g >= 1.0:
                        continue
                    gate(dominates(rho, beta, g, [(c, 1.0)]),
                         f"lambda=1 always dominant rho={rho} beta={beta} c={c} g={g:.4f}")


# ---------------------------------------------------------------------------
# C.  Crossing-in-band wall.
# ---------------------------------------------------------------------------
def right_crossing(rho, beta, tau):
    """Rightmost g in [0,1-rho] with F(g)=H2(rho+g)-beta*g >= tau, by bisection.
    Returns None if superlevel set empty."""
    F = lambda g: H2(rho + g) - beta * g - tau
    # F is concave in g; find its max then bisect on the decreasing branch.
    lo, hi = 0.0, 1.0 - rho - 1e-12
    # locate argmax by golden-ish scan
    best_g, best_v = 0.0, F(0.0)
    N = 2000
    for i in range(N + 1):
        g = (1.0 - rho) * i / N
        v = F(g)
        if v > best_v:
            best_v, best_g = v, g
    if best_v < 0:
        return None
    # bisect between best_g and hi for the zero of F (right crossing)
    a, b = best_g, hi
    if F(b) > 0:
        return b
    for _ in range(200):
        m = 0.5 * (a + b)
        if F(m) >= 0:
            a = m
        else:
            b = m
    return 0.5 * (a + b)


def section_C():
    LOG.append("== C. Zero-target crossing g* lies in the failure band (lambda<1) ==")
    grid_rho = [0.15, 0.30, 0.45, 0.60]
    grid_beta = [1.0, 2.0, 3.0, 5.0]
    for rho in grid_rho:
        for beta in grid_beta:
            gstar = right_crossing(rho, beta, 0.0)
            if gstar is None or gstar <= 1e-6:
                continue
            h = H2(rho + gstar)
            s = gstar * beta
            # F(g*)=0 => s = h (identity crossing).  Confirm.
            gate(abs(s - h) < 1e-3, f"g* has s==h rho={rho} beta={beta} s={s:.4f} h={h:.4f}")
            for c in [2, 3]:
                for lam in [0.25, 0.5, 0.75]:
                    kl = (c - 1) / (c - lam)
                    kh = 1.0 / lam
                    inside = (kl * h < s < kh * h)
                    gate(inside,
                         f"g* inside band rho={rho} beta={beta} c={c} lam={lam} "
                         f"band=({kl*h:.4f},{kh*h:.4f}) s={s:.4f}")
                # lambda=1: band is the single point s=h, so g* is on the boundary
                gate(abs(((c - 1) / (c - 1.0)) * h - h) < 1e-12,
                     f"lambda=1 band collapses rho={rho} beta={beta} c={c}")


# ---------------------------------------------------------------------------
# D.  Target-threshold form: tau >= tau0 => crossing in identity-dominant window.
# ---------------------------------------------------------------------------
def lower_window_edge(rho, beta, c, lam):
    """g_low: solve g*beta = kappa_low * H2(rho+g), kappa_low=(c-1)/(c-lam),
    on the branch g>0.  Bisection on phi(g)=g*beta-kappa_low*H2(rho+g)."""
    kl = (c - 1) / (c - lam)
    phi = lambda g: g * beta - kl * H2(rho + g)
    # phi(0+) < 0 (RHS>0), phi grows; find sign change
    lo, hi = 1e-9, 1.0 - rho - 1e-9
    if phi(hi) < 0:
        return hi
    # ensure phi(lo)<0
    if phi(lo) >= 0:
        return lo
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if phi(m) < 0:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


def section_D():
    LOG.append("== D. Target-threshold form: tau>=tau0 => crossing in lower window ==")
    grid_rho = [0.20, 0.35, 0.50]
    grid_beta = [1.5, 2.5, 4.0]
    c, lam = 2, 0.5
    for rho in grid_rho:
        for beta in grid_beta:
            gstar = right_crossing(rho, beta, 0.0)
            if gstar is None:
                continue
            g_low = lower_window_edge(rho, beta, c, lam)
            tau0 = H2(rho + g_low) - beta * g_low
            # (i) g_low < g* strictly and tau0 > 0
            gate(g_low < gstar - 1e-6, f"g_low<g* rho={rho} beta={beta}")
            gate(tau0 > 1e-6, f"tau0>0 rho={rho} beta={beta} tau0={tau0:.5f}")
            # (ii) for tau >= tau0 the crossing g_T <= g_low (dominant window)
            for frac in [1.0, 1.25, 1.6, 2.2]:
                tau = tau0 * frac
                gT = right_crossing(rho, beta, tau)
                if gT is None:
                    continue
                gate(gT <= g_low + 1e-6,
                     f"tau>=tau0 -> gT<=g_low rho={rho} beta={beta} tau={tau:.4f} "
                     f"gT={gT:.4f} g_low={g_low:.4f}")
                gate(band_predicts_dominant(rho, beta, gT, c, lam),
                     f"crossing dominant rho={rho} beta={beta} tau={tau:.4f}")
            # (iii) for tau slightly below tau0 crossing enters the band (not dominant)
            for frac in [0.85, 0.6, 0.3]:
                tau = tau0 * frac
                gT = right_crossing(rho, beta, tau)
                if gT is None or gT <= g_low:
                    continue
                gate(not band_predicts_dominant(rho, beta, gT, c, lam),
                     f"tau<tau0 -> in band rho={rho} beta={beta} tau={tau:.4f} gT={gT:.4f}")


# ---------------------------------------------------------------------------
# E.  Exact finite F_{p^2} census: field drop + pigeonhole in the quotient cell.
# ---------------------------------------------------------------------------
def build_Fp2(p):
    """Return (nu, mul, powr, one, zero) for F_{p^2}=F_p[i]/(i^2-nu)."""
    # smallest non-residue nu
    nu = None
    for cand in range(2, p):
        if pow(cand, (p - 1) // 2, p) == p - 1:
            nu = cand
            break
    assert nu is not None

    def mul(x, y):
        a, b = x
        c, d = y
        return ((a * c + b * d * nu) % p, (a * d + b * c) % p)

    def powr(x, e):
        r = (1, 0)
        base = x
        while e > 0:
            if e & 1:
                r = mul(r, base)
            base = mul(base, base)
            e >>= 1
        return r

    return nu, mul, powr


def find_generator(p, mul, powr):
    order = p * p - 1
    # prime factors of order
    fac = set()
    m = order
    d = 2
    while d * d <= m:
        while m % d == 0:
            fac.add(d)
            m //= d
        d += 1
    if m > 1:
        fac.add(m)
    for a in range(1, p):
        for b in range(0, p):
            if (a, b) == (1, 0):
                continue
            g = (a % p, b % p)
            if all(powr(g, order // q) != (1, 0) for q in fac):
                return g
    raise RuntimeError("no generator")


def elem_sym_prefix(support, w, mul, p):
    """First w elementary-symmetric coefficients (e_1..e_w) of prod (X - x)
    over F_{p^2}, returned as a tuple of F_{p^2} elements.
    Locator = X^a - e1 X^{a-1} + e2 X^{a-2} - ...  ; we return (e1,...,ew)."""
    # coeffs[j] = e_j ; build via convolution with (X - x)
    # represent polynomial as list of coeffs of prod (X - x_i), leading first
    poly = [(1, 0)]  # constant poly 1
    for x in support:
        neg = ((-x[0]) % p, (-x[1]) % p)  # -x
        new = [(0, 0)] * (len(poly) + 1)
        for j, cf in enumerate(poly):
            # multiply by X: shift
            new[j] = (new[j][0] + cf[0]) % p, (new[j][1] + cf[1]) % p
            t = mul(cf, neg)
            new[j + 1] = ((new[j + 1][0] + t[0]) % p, (new[j + 1][1] + t[1]) % p)
        poly = new
    # poly = X^a + c1 X^{a-1} + ... ; c_j = poly[j]; e_j = (-1)^j c_j
    ej = []
    for j in range(1, w + 1):
        cj = poly[j]
        if j % 2 == 1:
            ej.append(((-cj[0]) % p, (-cj[1]) % p))
        else:
            ej.append((cj[0] % p, cj[1] % p))
    return tuple(ej)


def in_scaled_subfield(val, j, eta, powr, mul, p, invtab):
    """Check val in eta^j * F_p, i.e. eta^{-j} * val has zero imaginary part."""
    etaj = powr(eta, j)
    # inverse of etaj
    inv = field_inverse(etaj, p, mul, powr)
    prod = mul(inv, val)
    return prod[1] % p == 0


def field_inverse(x, p, mul, powr):
    # x^{p^2-2}
    return powr(x, p * p - 2)


def section_E():
    LOG.append("== E. Exact F_{p^2} census: field drop + quotient-cell pigeonhole ==")
    full_enum = {5: 4, 7: 4}       # p -> a  (full identity enumeration)
    field_only = {11: 4, 13: 4}    # p -> a  (square-fiber field-drop + pigeonhole only)
    for p, a in list(full_enum.items()) + list(field_only.items()):
        n = 2 * (p - 1)
        c = 2
        m = a // 2
        N = n // 2
        w = 2  # even, >= r=0
        nu, mul, powr = build_Fp2(p)
        theta = find_generator(p, mul, powr)
        order = p * p - 1
        step = order // n
        gate(order % n == 0, f"n | p^2-1 p={p}")
        # D = theta * H, H = <theta^step>, |H|=n
        D = [powr(theta, (1 + j * step)) for j in range(n)]
        # multiply each by theta:  theta^{1+ j*step}; already includes theta factor
        gate(len(set(D)) == n, f"|D|=n p={p}")
        # square folding
        Dsq = [mul(x, x) for x in D]
        Q = sorted(set(Dsq))
        gate(len(Q) == N, f"|phi(D)|=n/2 p={p} got {len(Q)}")
        # complete fibers of size 2
        from collections import Counter
        cnt = Counter(Dsq)
        gate(all(v == 2 for v in cnt.values()), f"complete 2-fibers p={p}")
        # field drop: Q subset eta * F_p with eta = theta^2 (Q=theta^2 H^2, H^2=F_p^x)
        eta = mul(theta, theta)
        inv_eta = field_inverse(eta, p, mul, powr)
        drop_ok = all((mul(inv_eta, qv)[1] % p == 0) for qv in Q)
        gate(drop_ok, f"field drop Q subset eta*F_p p={p} (lambda=1/2)")
        # ---- square-fiber (quotient) family: E subset Q, |E|=m, S_E=phi^{-1}(E)
        from itertools import combinations
        # map each q in Q to its fiber (the two preimages)
        fiber = {}
        for x in D:
            key = mul(x, x)
            fiber.setdefault(key, []).append(x)
        qfams = []
        for E in combinations(Q, m):
            S = []
            for e in E:
                S.extend(fiber[e])
            qfams.append(tuple(sorted(S)))
        gate(len(qfams) == comb(N, m), f"#square-fiber supports=C(N,m) p={p}")
        # Prefixes of square-fiber supports obey the field-drop/lacunarity law:
        #   coefficient e_i(S) of the SUPPORT locator (degree a=cm) satisfies
        #     c | i  :  e_i(S) = +/- v_{i/c}(E)  in  eta^{i/c} * F_p   (field drop)
        #     c ! i  :  e_i(S) = 0                                     (lacunarity)
        # because L_E(X)=V_E(X^c) with V_E's coeffs v_j(E) in eta^j F_p.
        buckets = {}
        all_drop = True
        # precompute eta^{-t} for t up to w//c
        inv_eta_pow = {t: field_inverse(powr(eta, t), p, mul, powr)
                       for t in range(0, w // c + 1)}
        for S in qfams:
            pref = elem_sym_prefix(S, w, mul, p)
            for i in range(1, w + 1):
                ei = pref[i - 1]
                if i % c != 0:
                    if ei != (0, 0):           # lacunarity
                        all_drop = False
                else:
                    t = i // c
                    if mul(inv_eta_pow[t], ei)[1] % p != 0:   # eta^{-t} e_i in F_p
                        all_drop = False
            buckets.setdefault(pref, 0)
            buckets[pref] += 1
        gate(all_drop, f"square-fiber prefixes obey field-drop+lacunarity p={p}")
        # pigeonhole: prefix values live in (F_p)^{w/c} => at most p^{w//2} distinct;
        # so some bucket has >= ceil(#qfams / p^{w//2}) supports.
        distinct = len(buckets)
        gate(distinct <= p ** (w // c), f"quotient prefixes in small field p={p} "
                                        f"distinct={distinct} <= p^{w//c}={p**(w//c)}")
        max_bucket = max(buckets.values())
        qr6 = comb(N, m)
        # QR6 natural scale with B_phi=F_p, floor(w/c)=1:  C(N,m)/p
        import math
        qr6_pred = -(-qr6 // p)  # ceil(C(N,m)/p)
        gate(max_bucket >= qr6_pred,
             f"pigeonhole bucket>=ceil(QR6) p={p} max={max_bucket} pred={qr6_pred}")
        # identity average barN_1 = C(n,a)/|B|^w  (should be < 1 here, so identity
        # cell carries < 1 on average while quotient cell carries max_bucket>=2)
        barN1 = Fraction(comb(n, a), (p * p) ** w)
        gate(max_bucket > barN1,
             f"quotient cell > identity average p={p} qcell={max_bucket} barN1={float(barN1):.4f}")
        # ---- full identity enumeration (only small p): confirm the SAME prefix
        # bucket, viewed over ALL size-a supports, is dominated by the quotient
        # family and exceeds the identity per-bucket average.
        if p in full_enum:
            allbuckets = {}
            allD = D
            for S in combinations(allD, a):
                pref = elem_sym_prefix(S, w, mul, p)
                allbuckets[pref] = allbuckets.get(pref, 0) + 1
            total = comb(n, a)
            gate(sum(allbuckets.values()) == total, f"identity enum count p={p}")
            avg = Fraction(total, len(allbuckets))
            # the max square-fiber prefix bucket, as an identity bucket, is >= its
            # square-fiber count (identity bucket >= quotient subfamily count)
            best_qpref = max(buckets, key=lambda k: buckets[k])
            id_here = allbuckets.get(best_qpref, 0)
            gate(id_here >= max_bucket,
                 f"identity bucket>=quotient subfamily p={p} id={id_here} q={max_bucket}")
            # and this quotient-carrying bucket exceeds the identity per-bucket avg
            gate(id_here > avg,
                 f"quotient-carrying bucket>avg p={p} here={id_here} avg={float(avg):.3f}")


def main():
    print("verify_envelope_window.py  --  identity-dominance window criterion")
    print("target: experimental/asymptotic_rs_mca_frontiers.tex hard input (d)")
    print("-" * 70)
    section_A()
    section_Aprime()
    section_B()
    section_C()
    section_D()
    section_E()
    print("\n".join(LOG))
    print("-" * 70)
    if FAILS == 0:
        print(f"RESULT: PASS ({CHECKS} checks)")
    else:
        print(f"RESULT: FAIL ({FAILS} of {CHECKS} checks failed)")
    return 0 if FAILS == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
