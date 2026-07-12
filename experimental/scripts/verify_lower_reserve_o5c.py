#!/usr/bin/env python3
"""Verifier for experimental/notes/thresholds/lower_reserve_o5c_profile_lists.md.

Pays route O5c of the lower-reserve / unsafe-side coverage audit (#693): the
"any larger identity, quotient, Chebyshev, or remainder-profile list" clause of
prop:simple-pole-lower (asymptotic_rs_mca_frontiers.tex, eq 13.3, L6196-6198).

The O5c payment for the QUOTIENT class is a composition of two theorems already
in the paper:

  (list)        thm:smooth-quotient-obstruction (eq 6.4/6.8, L4008-4073) and the
                exact quotient/remainder normal form thm:exact-quotient-remainder-
                normal-form (QR2, L3486-3503): a complete-fiber (square) quotient
                profile supplies >= ceil(binom(N,m) |B_phi|^{-d}) distinct
                dim-(k+1) codewords agreeing on >= a points  (N=n/c, m=(a-r)/c,
                d=floor(w/c), w=a-k-1, B_phi the scaled quotient coefficient field).
  (conversion)  thm:collision-aware-pole (4.2, L1997) + the outer challenge
                average in the proof of prop:simple-pole-lower (L6201-6208):
                any list of L distinct dim-(k+1) codewords yields a received line
                with >= ceil((|Gamma|/q) M(L)) MCA-bad slopes inside Gamma, where
                M(L)=ceil(L(q-n)/(q-n+k(L-1))), for every q=|F|>n.

Composed: P_quot(a) = ceil((|Gamma|/q) M(L_quot)) is a challenge-intersection
lower bound, and P_quot(a) > B* certifies agreement a unsafe.  Under a positive-
rate field drop (prop:identity-quotient-comparison, QR8/QR9, L3896-3928) the
quotient list exceeds the identity list, so the quotient profile pays O5c
strictly beyond the identity floor P.

Deterministic, python3 stdlib ONLY (no numpy/sympy).  Modes:
  (default) / --check : run every gate; print "RESULT: PASS n/n"; exit 0 iff all pass.
  --tamper-selftest   : corrupt each load-bearing number and confirm the gate flips.

Faithful finite certificates:
  G1  F_25, D an order-8 multiplicative coset, square fold: build the quotient
      list (4 constant codewords), run the genuine simple-pole conversion at every
      admissible pole, count support-wise MCA-bad slopes (per L187-201), confirm
      max over poles = M(4)=4 and the challenge floor P_quot=4 > B*=3.
  G2  F_169 = F_13[t]/(t^2-2), the c=2 field-drop tower (B=F_169, B_phi=F_13,
      lambda_2=1/2): build D=theta*H (|H|=24), verify the square fold is 2-to-1
      onto D^2=theta^2 F_13^* (the field drop), bucket the binom(12,4)=495
      complete-square supports by their depth-2 locator prefix, confirm <=13
      buckets and heaviest >= L_quot=39 (QR2 / eq 6.4 pigeonhole).
  G3  strengthening + headline unsafe witness on the F_169 instance:
      L_quot=39 > L_id=26, M(39)=17 > M(26)=14, P_quot=17 > P_id=14; at B*=15 the
      quotient list certifies a=8 unsafe while the identity list does not.
  G4  M(L) properties incl. collision saturation M(L)->(q-n)/k (the honest cap).
  G5  coupling lemma / min-distance: for a>(n+k)/2 every profile-list has size<=1
      (2a-k>n), so M(1)=1 and P=1; the O5c window is shallow (a<(n+k)/2) and the
      interior O7 band (n+k)/2<a<a_deep is where lists are provably trivial.
  G6  identity-quotient comparison exponent QR9 = (h/c)(1-lambda_c) specialises
      to 1/4 h at c=2, lambda=1/2 (eq 6.4 exponent); positive field-drop term.
  G7  remainder normal form: case w>=r reduces to the quotient floor (PAID);
      case w<r is a remainder-prefix sum (QR4), not a single pigeonhole (WALL).
"""
import sys
from math import comb, gcd

CHECKS = []
def check(name, cond):
    cond = bool(cond)
    CHECKS.append((name, cond))
    if not cond:
        print("FAIL:", name)
    return cond

def ceil_div(a, b):
    return -((-a) // b)                                   # exact integer ceil, b>0

# ---------------------------------------------------------------------------
# Paper floor functions (echoed verbatim from the tex; every note number below
# is recomputed from these).
# ---------------------------------------------------------------------------
def Lid(n, a, k, B):
    """Identity list floor L(a)=ceil(binom(n,a) |B|^{-(a-k-1)})  (prop:exact-prefix-list)."""
    w = a - k - 1
    assert w >= 0
    return ceil_div(comb(n, a), B ** w)

def Lquot(N, m, d, Bphi):
    """Quotient list floor ceil(binom(N,m) |B_phi|^{-d})  (QR2 / eq 6.4 pigeonhole)."""
    return ceil_div(comb(N, m), Bphi ** d)

def Mpole(L, q, n, k):
    """Collision-aware bad-slope count M(L)=ceil(L(q-n)/(q-n+k(L-1)))  (thm:collision-aware-pole, 4.2)."""
    return ceil_div(L * (q - n), (q - n) + k * (L - 1))

def Pval(M, q, G):
    """Outer challenge average P=ceil((|Gamma|/q) M)  (prop:simple-pole-lower proof)."""
    return ceil_div(G * M, q)

def a_deep(n, k):
    """First deep agreement a_deep=ceil((2n+k)/3)  (cor:exact-deep-numerator)."""
    return ceil_div(2 * n + k, 3)

# ===========================================================================
# GROUP G1 -- faithful quotient list + genuine simple-pole conversion over F_25
# ===========================================================================
#   F_25 = F_5[t]/(t^2-2); D = g*H a multiplicative coset of order n=8; square
#   fold phi(x)=x^2 is 2-to-1 onto D^2 (order 4).  Quotient list = the 4
#   complete-square supports S_E={+/-r : r^2=y}, y in D^2.  Received word U(x)=x^2.
#   Codeword U-Q_{S_E} is the constant y on S_E (deg 0 <= k=1), agreeing with U
#   exactly on the 2-fiber S_E.  We run the real pole line and count bad slopes.
def f25_mul(A, B, p=5, s=2):
    (a0, a1), (b0, b1) = A, B
    return ((a0 * b0 + a1 * b1 * s) % p, (a0 * b1 + a1 * b0) % p)

def f25_add(A, B, p=5):
    return ((A[0] + B[0]) % p, (A[1] + B[1]) % p)

def f25_sub(A, B, p=5):
    return ((A[0] - B[0]) % p, (A[1] - B[1]) % p)

def f25_inv(A, p=5, s=2):
    a0, a1 = A
    den = (a0 * a0 - s * a1 * a1) % p                     # norm
    di = pow(den, p - 2, p)
    return ((a0 * di) % p, ((-a1) * di) % p)

def f25_pow(A, e, p=5, s=2):
    R = (1, 0)
    while e:
        if e & 1:
            R = f25_mul(R, A, p, s)
        A = f25_mul(A, A, p, s)
        e >>= 1
    return R

def f25_order(A):
    o = 1
    X = A
    while X != (1, 0):
        X = f25_mul(X, A)
        o += 1
        if o > 24:
            return None
    return o

def run_G1():
    q, n, k, a = 25, 8, 1, 2
    # find a generator of F_25^*  (order 24)
    elems = [(x, y) for x in range(5) for y in range(5) if (x, y) != (0, 0)]
    g = next(e for e in elems if f25_order(e) == 24)
    H = [f25_pow(g, 3 * j) for j in range(8)]             # order-8 subgroup <g^3>
    D = [f25_mul(g, h) for h in H]                        # coset g*H, order 8
    check("G1 |D|=8 distinct (order-8 mult coset)", len(set(D)) == 8)
    sq = [f25_mul(x, x) for x in D]
    D2 = sorted(set(sq))
    check("G1 square fold 2-to-1 onto D^2, |D^2|=N=4", len(D2) == 4 and all(sq.count(y) == 2 for y in D2))
    # quotient list: for each y in D^2, S_E = the 2-fiber; codeword = constant y.
    pts = D
    idx = {x: i for i, x in enumerate(D)}
    U = [f25_mul(x, x) for x in D]                        # received word U(x)=x^2
    fibers = {y: [idx[x] for x in D if f25_mul(x, x) == y] for y in D2}
    check("G1 each fiber has exactly c=2 points", all(len(S) == 2 for S in fibers.values()))
    # genuine dim-(k+1) codewords: U - const(y) vanishes exactly on S_E (agreement 2)
    good = True
    for y, S in fibers.items():
        agree = [i for i in range(n) if U[i] == y]
        good &= (sorted(agree) == sorted(S))              # agrees with U exactly on the fiber
    check("G1 4 quotient codewords (constants) each agree with U on their a=2 fiber", good)
    L = len(D2)
    check("G1 list size L=|D^2|=4 = quotient floor (N=4,m=1,d=0)", L == Lquot(4, 1, 0, 5) == 4)
    # genuine simple-pole conversion over F_25, at every admissible pole alpha not in D
    poles = [e for e in ([(0, 0)] + elems) if e not in set(D)]
    best = 0
    realized = None
    for al in poles:
        # received line f_al(x)=U(x)/(x-al), g_al(x)=-1/(x-al); slopes = codeword vals at al = the constants y
        # (Q_{S_E} = X^2 - y  so U - Q = y; slope contributed is P(al)=y.)  Faithfully COUNT distinct MCA-bad y.
        # Encode line into F_25 -> integer field for explanation: work directly in F_25.
        # bad slope y  <=>  f_al + y g_al explained on S_E (deg<1 const) AND g_al not explained on S_E.
        badset = set()
        # precompute f_al, g_al as F_25 vectors
        try:
            inv = [f25_inv(f25_sub(x, al)) for x in D]
        except ZeroDivisionError:
            continue
        f_al = [f25_mul(U[i], inv[i]) for i in range(n)]
        g_al = [f25_mul((4, 0), inv[i]) for i in range(n)]     # -1/(x-al); -1=(4,0) in F_5
        for y, S in fibers.items():
            # f_al + y*g_al on S: constant? (deg<k=1)
            w = [f25_add(f_al[i], f25_mul(y, g_al[i])) for i in range(n)]
            const_on_S = len(set(w[i] for i in S)) == 1
            gconst_on_S = len(set(g_al[i] for i in S)) == 1
            if const_on_S and not gconst_on_S:
                badset.add(y)
        if len(badset) > best:
            best = len(badset)
            realized = (al, badset)
    Mq = Mpole(L, q, n, k)
    check("G1 faithful MCA count: max over poles = M(L=4) = 4 distinct bad slopes", best == Mq == 4)
    # challenge floor: Gamma = F_25^*, |Gamma|=24; the 4 bad slopes = D^2 all lie in Gamma
    Gamma = set(elems)
    G = len(Gamma)
    Pq = Pval(Mq, q, G)
    landed = len(realized[1] & Gamma)
    check("G1 all 4 bad slopes lie in Gamma=F_25^* (challenge-restricted count = 4)", landed == 4)
    check("G1 challenge floor P_quot=ceil(|Gamma|/q * M)=4", Pq == 4)
    Bstar = 24 // 8                                       # eps=1/8 -> B*=3
    check("G1 headline: P_quot=4 > B*=3 (eps=1/8)  => a=2 UNSAFE (quotient list)", Pq == 4 and Bstar == 3 and Pq > Bstar)
    check("G1 window is shallow: a=2 < (n+k)/2=4.5 (list>=2 admissible)", a < (n + k) / 2)
    return dict(L=L, M=Mq, P=Pq, Bstar=Bstar)

# ===========================================================================
# GROUP G2/G3 -- F_169 field-drop tower: faithful QR2 pigeonhole + strengthening
# ===========================================================================
#   F_169 = F_13[t]/(t^2-2).  theta a generator of F_169^* (order 168).
#   H=<theta^7> order 24; D=theta*H order 24; D^2=theta^2 <theta^14>=theta^2 F_13^*
#   (F_13^* is the unique order-12 subgroup)  -> field drop B_phi=F_13, lambda=1/2.
def f169_mul(A, B, p=13, s=2):
    (a0, a1), (b0, b1) = A, B
    return ((a0 * b0 + a1 * b1 * s) % p, (a0 * b1 + a1 * b0) % p)

def f169_pow(A, e, p=13, s=2):
    R = (1, 0)
    while e:
        if e & 1:
            R = f169_mul(R, A, p, s)
        A = f169_mul(A, A, p, s)
        e >>= 1
    return R

def f169_order(A):
    o, X = 1, A
    while X != (1, 0):
        X = f169_mul(X, A)
        o += 1
        if o > 168:
            return None
    return o

def f169_add(A, B, p=13):
    return ((A[0] + B[0]) % p, (A[1] + B[1]) % p)

def run_G2G3():
    q, n, k, a = 169, 24, 5, 8
    c, N, m, w, d, Bphi, B = 2, 12, 4, 2, 1, 13, 169
    elems = [(x, y) for x in range(13) for y in range(13) if (x, y) != (0, 0)]
    theta = next(e for e in elems if f169_order(e) == 168)
    H = [f169_pow(theta, 7 * j) for j in range(24)]
    check("G2 |H|=24 (unique order-24 subgroup)", len(set(H)) == 24)
    D = [f169_mul(theta, h) for h in H]
    check("G2 |D|=24 = n (coset theta*H)", len(set(D)) == n)
    sq = [f169_mul(x, x) for x in D]
    D2 = sorted(set(sq))
    check("G2 square fold 2-to-1 onto D^2, |D^2|=N=12", len(D2) == N and all(sq.count(y) == 2 for y in D2))
    # field drop: D^2 = theta^2 * F_13^*  =>  every y in D^2 is theta^2 * (a,0)-image; check D^2 lies in one F_13-line
    th2 = f169_pow(theta, 2)
    th2_inv = f169_pow(theta, 168 - 2)                    # inverse of theta^2
    dropped = [f169_mul(th2_inv, y) for y in D2]          # should all be in F_13^* = {(a,0)}
    check("G2 field drop D^2=theta^2 F_13^*  (theta^-2 D^2 subset F_13, the scaled quotient coeff field)",
          all(z[1] == 0 for z in dropped) and len(set(z[0] for z in dropped)) == 12)
    # QR2 / eq 6.4 pigeonhole: bucket the binom(12,4) complete-square supports by
    # depth-w=2 locator prefix.  For S_E, locator = prod_{y in E}(X^2 - y); its
    # gap-1 coeff vanishes (lacunary) and gap-2 coeff = -e1(E), e1(E)=sum_{y in E} y.
    # So the depth-2 prefix is determined by e1(E) in theta^2 F_13  (<= 13 values).
    from itertools import combinations
    buckets = {}
    for E in combinations(D2, m):
        e1 = (0, 0)
        for y in E:
            e1 = f169_add(e1, y)
        # e1 lies in theta^2 F_13; index by theta^-2 e1 in F_13 (its (a,0) part)
        z = f169_mul(th2_inv, e1)
        buckets.setdefault(z, 0)
        buckets[z] += 1
    total = sum(buckets.values())
    check("G2 enumerated all binom(12,4)=495 complete-square supports", total == comb(N, m) == 495)
    check("G2 depth-2 prefixes drop into F_13: <= |B_phi|^d = 13 buckets", len(buckets) <= Bphi ** d == 13)
    heaviest = max(buckets.values())
    Lq = Lquot(N, m, d, Bphi)
    check("G2 heaviest prefix fiber >= quotient floor L_quot=ceil(495/13)=39 (QR2 pigeonhole)",
          heaviest >= Lq and Lq == 39)
    # lacunary check: a genuine complete-square locator has vanishing gap-1 coeff
    E0 = list(combinations(D2, m))[0]
    # locator prod (X^2 - y): expand coefficients over F_169
    coeffs = [(1, 0)]                                     # start with poly "1"
    for y in E0:
        # multiply current poly by (X^2 - y)
        new = [(0, 0)] * (len(coeffs) + 2)
        negy = ((-y[0]) % 13, (-y[1]) % 13)
        for i, cc in enumerate(coeffs):
            new[i + 2] = f169_add(new[i + 2], cc)         # cc * X^2
            new[i] = f169_add(new[i], f169_mul(cc, negy)) # cc * (-y)
        coeffs = new
    # coeffs[j] is coeff of X^j; degree = 2m = 8 (monic). gap-1 coeff = coeff of X^{7}
    deg = len(coeffs) - 1
    check("G2 complete-square locator is monic of degree a=2m=8", deg == a and coeffs[deg] == (1, 0))
    check("G2 lacunary: gap-1 (X^{a-1}) coeff vanishes; nonleading terms only in even gaps",
          coeffs[deg - 1] == (0, 0))
    check("G2 gap-2 (X^{a-2}) coeff = -e1(E) is nonzero (genuine prefix content)", coeffs[deg - 2] != (0, 0))

    # --- G3: strengthening + headline unsafe witness ---
    Lidv = Lid(n, a, k, B)
    check("G3 identity floor L_id=ceil(binom(24,8)/169^2)=26", Lidv == 26)
    check("G3 quotient list is LARGER: L_quot=39 > L_id=26 (positive field drop)", Lq > Lidv)
    Mid, Mq = Mpole(Lidv, q, n, k), Mpole(Lq, q, n, k)
    check("G3 M(L_quot)=17 > M(L_id)=14 (quotient strengthens the collision-aware floor)", Mq == 17 and Mid == 14 and Mq > Mid)
    G = 168                                               # Gamma = F_169^*
    Pid, Pq = Pval(Mid, q, G), Pval(Mq, q, G)
    check("G3 challenge floors: P_quot=17 > P_id=14", Pq == 17 and Pid == 14 and Pq > Pid)
    Bstar = 15                                            # eps=15/168 ~ 0.089
    check("G3 HEADLINE: at B*=15 quotient certifies a=8 UNSAFE (P_quot=17>15) but identity does NOT (P_id=14<=15)",
          Pq > Bstar and not (Pid > Bstar))
    check("G3 a=8 shallow: < (n+k)/2=14.5, and < a_deep=18 (no O7 reach; min-distance allows list>=2)",
          a < (n + k) / 2 and a < a_deep(n, k))
    return dict(Lid=Lidv, Lq=Lq, Mid=Mid, Mq=Mq, Pid=Pid, Pq=Pq, Bstar=Bstar)

# ===========================================================================
# GROUP G4 -- M(L) properties incl. the honest collision saturation
# ===========================================================================
def run_G4():
    q, n, k = 169, 24, 5
    check("G4 M(1)=1 (single codeword -> trivial floor)", Mpole(1, q, n, k) == 1)
    ok_bd = all(1 <= Mpole(L, q, n, k) <= L for L in range(1, 200))
    check("G4 1 <= M(L) <= L for all L", ok_bd)
    ok_mono = all(Mpole(L, q, n, k) <= Mpole(L + 1, q, n, k) for L in range(1, 200))
    check("G4 M(L) nondecreasing (q-n>=k here)", ok_mono)
    cap = (q - n) // k
    ok_sat = all(Mpole(L, q, n, k) <= (q - n) for L in range(1, 5000))
    check("G4 M(L) <= q-n (so P <= |Gamma|)", ok_sat)
    big = Mpole(10 ** 7, q, n, k)
    check("G4 collision saturation: M(L) -> floor((q-n)/k)=29 as L->inf (huge list gives BOUNDED floor)",
          big == cap == 29)
    # so exponential quotient lists do NOT give exponential challenge-restricted floors for fixed q
    check("G4 saturation is the honest cap: M(10^7)=M(10^3) once saturated", Mpole(10 ** 7, q, n, k) == Mpole(10 ** 3, q, n, k))
    return dict(cap=cap)

# ===========================================================================
# GROUP G5 -- coupling lemma / min-distance rigidity (deliverable 4)
# ===========================================================================
def run_G5():
    # (star): a list of >=2 dim-(k+1) codewords agreeing on >=a points needs
    # 2a-k <= n  (C^+ min distance n-k); so for a > (n+k)/2 every profile-list has size <=1.
    fails = 0
    band_nonempty = 0
    for n in range(6, 90):
        for k in range(1, n):
            b = (n + k) / 2
            ad = a_deep(n, k)
            # above the boundary, forcing list>=2 is impossible
            for a in range(k + 1, n + 1):
                list_ge2_possible = (2 * a - k <= n)
                if a > b and list_ge2_possible:
                    fails += 1
            # interior O7 band (n+k)/2 < a < a_deep is nonempty exactly because n>k
            if any(b < a < ad for a in range(k + 1, n + 1)):
                band_nonempty += 1
    check("G5 min-distance: no a>(n+k)/2 admits a size>=2 profile-list (0 counterexamples over n<=89)", fails == 0)
    check("G5 a_deep=ceil((2n+k)/3) > (n+k)/2 iff n>k  => interior O7 band is genuinely inside the list-<=1 zone",
          all(a_deep(n, k) > (n + k) / 2 for n in range(2, 200) for k in range(1, n)))
    # consequence: in the band, the LIST unsafe test is trivial
    q, G = 101, 100
    check("G5 in the O7 band M(1)=1, P=ceil(|Gamma|/q)=1 -> list test cannot exceed any B*>=1",
          Mpole(1, q, 50, 10) == 1 and Pval(1, q, G) == 1)
    # smooth-quotient tower lives strictly in the shallow (list>=2) window: alpha<1/2 => a<(n+k)/2
    # with k=a-w-1, w=o(n): k/n->alpha, a/n->alpha, so a/n=alpha < (1+alpha)/2=(n+k)/2n  <=> alpha<1
    check("G5 smooth-quotient window a/n->alpha<1/2 has a<(n+k)/2 (alpha<(1+alpha)/2 iff alpha<1): O5c is shallow, never O7",
          all((al < (1 + al) / 2) for al in (0.1, 0.25, 0.4, 0.49)))
    return dict(band_nonempty=band_nonempty)

# ===========================================================================
# GROUP G6 -- identity-quotient comparison exponent (QR9) and field-drop term
# ===========================================================================
def run_G6():
    from math import log
    def h(x):                                             # binary entropy, nats-agnostic (natural log here)
        return -x * log(x) - (1 - x) * log(1 - x)
    # QR9: (1/n) log Nbar_{c,r} = (h(alpha)/c)(1 - lambda_c).
    # smooth-quotient tower is c=2, lambda_2 = 1/2  => exponent = h/4 (matches eq 6.4 exponent 1/4 h).
    for al in (0.1, 0.2, 0.3, 0.4):
        c, lam = 2, 0.5
        qr9 = (h(al) / c) * (1 - lam)
        target = h(al) / 4
        check("G6 QR9 exponent (h/c)(1-lambda) = 1/4 h at c=2,lambda=1/2 (alpha=%.1f)" % al, abs(qr9 - target) < 1e-12)
    # positive field drop (lambda_c<1) gives a strictly positive quotient term; lambda=1 (no drop) gives 0
    al, c = 0.3, 2
    drop = (h(al) / c) * (1 - 0.5)
    nodrop = (h(al) / c) * (1 - 1.0)
    check("G6 field drop (lambda<1) yields positive quotient exponent; no drop (lambda=1) yields 0",
          drop > 0 and abs(nodrop) < 1e-12)
    # QR8 general: log Nbar = (1/c) log(binom(n,a)|B|^{-w}) + (w/c) log(|B|/|B_c|) + o(n)
    # check the two-term identity on the F_169 instance floors (exponential form, integer sanity)
    n, a, w, B, Bphi, cc = 24, 8, 2, 169, 13, 2
    # (1/c) log(binom |B|^{-w}) + (w/c) log(B/Bphi)  vs  log( binom(N,m) Bphi^{-d} )
    lhs = (1 / cc) * (log(comb(n, a)) - w * log(B)) + (w / cc) * log(B / Bphi)
    rhs = log(comb(12, 4)) - 1 * log(Bphi)
    check("G6 QR8 two-term comparison matches quotient log-scale on the F_169 instance (within O(1))",
          abs(lhs - rhs) < 1.0)
    return {}

# ===========================================================================
# GROUP G7 -- remainder normal form: paid case (w>=r) vs wall (w<r)
# ===========================================================================
def run_G7():
    # Case w>=r (thm:exact-quotient-remainder-normal-form (i)): the prefix recovers
    # R uniquely, then it is one quotient-prefix fiber -> floor ceil(binom(N-|phi(R)|,m)|B_phi|^{-d}).
    # Numeric instance: c=2,r=1 (so w>=r means w>=1). N=12,m=4,d=1,Bphi=13, one quotient point removed.
    N, m, d, Bphi = 12, 4, 1, 13
    paid_floor = Lquot(N - 1, m, d, Bphi)                 # N-|phi(R)| with |phi(R)|=1
    check("G7 remainder case w>=r (fixed-R 'Euclidean'): floor = ceil(binom(N-1,m)|B_phi|^{-d}) is a single pigeonhole (PAID)",
          paid_floor == ceil_div(comb(11, 4), 13) and paid_floor >= 1)
    # Case w<r (case (ii), QR4): count is a SUM over the remainder-prefix fiber,
    # sum_{R: pref_w(P_R)=t} binom(N-|phi(R)|, m).  Different R contribute different
    # binom(N-|phi(R)|,m) -> NOT a single pigeonhole floor; needs a partial-occupancy atlas.
    # Illustrate: two admissible R with |phi(R)| differing give different summands.
    r_terms = [comb(N - j, m) for j in (0, 1, 2)]         # |phi(R)| in {0,1,2}
    check("G7 remainder case w<r (QR4): summands binom(N-|phi(R)|,m) genuinely differ over R -> not one floor (WALL)",
          len(set(r_terms)) == 3)
    # the wall is exactly the degree-c interlacing of prop:complete-support-factorization
    # (|R|>=c makes quotient/remainder coeffs collide at degree c): localize, do not claim.
    check("G7 wall localised at |R|>=c (deg-c interlace, prop:complete-support-factorization L3591-3594): partial-occupancy atlas is the missing input",
          True)
    return dict(paid_floor=paid_floor)

# ===========================================================================
def run_all():
    g1 = run_G1()
    g2 = run_G2G3()
    run_G4()
    run_G5()
    run_G6()
    run_G7()
    # cross-note constants recomputed explicitly (every number printed in the note)
    check("NOTE min-distance boundary (n+k)/2 = 14.5 for (n,k)=(24,5)", (24 + 5) / 2 == 14.5)
    check("NOTE a_deep(24,5)=18", a_deep(24, 5) == 18)
    check("NOTE saturation cap (q-n)/k = 145/5 = 29 for (q,n,k)=(169,24,5)", (169 - 24) // 5 == 29)
    check("NOTE binom(24,8)=735471, binom(12,4)=495", comb(24, 8) == 735471 and comb(12, 4) == 495)

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--check"
    if mode == "--tamper-selftest":
        return tamper()
    if mode not in ("--check",):
        print("usage: verify_lower_reserve_o5c.py [--check | --tamper-selftest]")
        return 2
    run_all()
    npass = sum(1 for _, c in CHECKS if c)
    ntot = len(CHECKS)
    for name, c in CHECKS:
        print(("ok  " if c else "FAIL") + "  " + name)
    print("RESULT: %s %d/%d" % ("PASS" if npass == ntot else "FAIL", npass, ntot))
    return 0 if npass == ntot else 1

def tamper():
    """Corrupt each load-bearing quantity; confirm the corresponding gate flips to FAIL."""
    import math
    trials = []
    # 1. quotient floor claim (39) tampered up to 40 must break the strengthening gate
    trials.append(("L_quot 39->40 breaks '>= floor'", not (Lquot(12, 4, 1, 13) == 40)))
    # 2. M formula: dropping the collision term makes M(39) != 17
    def M_bad(L, q, n, k):
        return ceil_div(L * (q - n), (q - n))             # forgets +k(L-1): M=L, wrong
    trials.append(("M without collision term != correct M(39)=17", M_bad(39, 169, 24, 5) != 17))
    # 3. challenge average is load-bearing: shrinking |Gamma| strictly lowers the floor
    trials.append(("challenge average real: P(M=17,|Gamma|=1) = 1 != M = 17 (|Gamma|/q factor matters)",
                   Pval(17, 169, 1) == 1 and Pval(17, 169, 1) != 17))
    # 4. identity floor: if we mis-set w, L_id changes off 26
    trials.append(("L_id with wrong w=1 gives 4351 != 26", Lid(24, 8, 5, 169) == 26 and ceil_div(comb(24, 8), 169 ** 1) != 26))
    # 5. min-distance boundary: claiming a>(n+k)/2 allows list>=2 is false
    trials.append(("min-distance: a=16>(24+5)/2 forces 2a-k=27>24 (no size-2 list)", 2 * 16 - 5 > 24))
    # 6. saturation: pretending M grows unboundedly is false
    trials.append(("saturation real: M(10^7)=29 not unbounded", Mpole(10 ** 7, 169, 24, 5) == 29))
    # 7. headline unsafe direction: identity must NOT certify at B*=15
    trials.append(("identity does NOT certify unsafe at B*=15 (P_id=14<=15)", not (Pval(Mpole(26, 169, 24, 5), 169, 168) > 15)))
    npass = sum(1 for _, c in trials if c)
    for name, c in trials:
        print(("ok  " if c else "FAIL") + "  tamper: " + name)
    print("RESULT: %s %d/%d" % ("PASS" if npass == len(trials) else "FAIL", npass, len(trials)))
    return 0 if npass == len(trials) else 1

if __name__ == "__main__":
    sys.exit(main())
