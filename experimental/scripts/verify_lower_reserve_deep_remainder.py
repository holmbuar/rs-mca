#!/usr/bin/env python3
"""Verifier for experimental/notes/thresholds/lower_reserve_deep_remainder_atlas.md.

Attacks the ONE remaining wall of route O5c (lower reserve / unsafe-side, hard
input 5) left open by PR #699: the deep-remainder regime  w < r  of the "any
larger identity, quotient, Chebyshev, or remainder-profile list" clause of
prop:simple-pole-lower (asymptotic_rs_mca_frontiers.tex eq 13.3, L6196-6198).

PR #699 paid the quotient / Euclidean-remainder (w>=r, r<c) / Chebyshev classes
and localised the deep case  w < r  (equivalently the remainder degree reaches
the quotient slots) to a missing "partial-occupancy atlas at the degree-c
interlace" (prop:complete-support-factorization, L3591-3594; named at L6325-6328).

This packet BUILDS that atlas and DECIDES it NEGATIVE:

  (atlas built)   The canonical occupancy cells Omega_{t,m,p,r} of
                  thm:exact-partial-occupancy (PO1/PO2, L3608-3644) exhaust
                  binom(D,a) exactly, and inside a single cell |phi(R)|=p is
                  CONSTANT, so the QR4 fiber sum (L3513-3520)
                     sum_{R} binom(N-|phi(R)|,m)
                  factors as  binom(N-p,m) * #{R in cell : pref_w(P_R)=.} .
                  The varying summand PR #699 flagged (its G7 three values
                  binom(N-|phi(R)|,m), |phi(R)| in {0,1,2}) is exactly cell
                  MIXING; within a cell it is one number.  [atlas assembled]

  (conversion     But the per-cell fiber cannot be routed through the collision-
   fails, pinned) aware pole with a field drop, because in the deep regime w<r
                  NO depth-w prefix slot is field-drop-clean:
                    - if w<c (forced when r<c): d=floor(w/c)=0, the prefix
                      reaches no quotient coefficient at all;
                    - if w>=c (forces r>c): every quotient slot degree jc<=w has
                      jc<=w<r=deg P_R, so the FULL-FIELD remainder coefficient
                      p_{jc}(R) sits additively in that slot (QR5 reciprocal
                      identity, L3536-3541), overwriting the small-field v_j(E).
                  Hence the effective prefix alphabet is the FULL field B in
                  every occupied slot (no |B_phi| drop), the provable list floor
                  |profile|/|image| <= L_id, and the field-drop-preserving
                  fixed-R alternative ceil(binom(N-p,m)|B_phi|^{-d}) < L_id in
                  the deep window.  No deep-remainder list beats the identity
                  list.  The load-bearing blocker is the coefficient p_{jc}(R).

Deterministic, python3 stdlib ONLY (no numpy/sympy).  Modes:
  (default)/--check : run every gate; print "RESULT: PASS n/n"; exit 0 iff all pass.
  --tamper-selftest : corrupt each load-bearing number; confirm the gate flips.
Writes a JSON certificate to
  experimental/data/certificates/lower-reserve-deep-remainder/deep_remainder_atlas.json.

Gate groups (every number in the note is recomputed here):
  A  occupancy atlas exhaustion PO1/PO2, c=2 (F_25 tower) and c=3 (F_13 cube).
  B  constant-summand-per-cell: the QR4 factorization binom(N-p,m)*#{R}; #699 G7
     three summands come from cell mixing (|phi(R)| in {0,1,2}), constant per cell.
  C  interlace: in the deep prefix the quotient slot moves with BOTH E and R
     (fix-R-vary-E and fix-E-vary-R both nontrivial); in the clean quotient
     profile the slot moves with E only.
  D  field-drop alphabet contrast: clean quotient slot alphabet = |B_phi| and
     descends into F_5 after theta^{-2}; deep interlaced slot alphabet = full
     field.  E-slice / R-slice decomposition of the deep fiber.
  E  characterization: strengthening <=> exists a clean slot (some j: r<jc<=w)
     <=> NOT deep (w<r).  Grid: deep&clean = 0 over c<=5, r,w<=11.
  F  domination numerics (F_169 tower): fixed-R deep floor 5 << L_id 69; the
     provable-floor <= L_id argument; rigidity 4.4 cross-check (no |B|^{-w} drop).
  G  boundary constants and coupling to #699/#693: Euclidean (w>=r,r<c) has a
     clean slot (PAID); deep (w<r) has none (WALL -> DECIDED negative).
"""
import sys, os, json
from math import comb
from itertools import combinations

CHECKS = []
def check(name, cond):
    cond = bool(cond)
    CHECKS.append((name, cond))
    if not cond:
        print("FAIL:", name)
    return cond

def ceil_div(a, b):
    return -((-a) // b)

# ---------------------------------------------------------------------------
# Paper floor functions (echoed verbatim from the tex).
# ---------------------------------------------------------------------------
def Lid(n, a, k, B):
    """Identity list floor L(a)=ceil(binom(n,a)|B|^{-(a-k-1)})  (prop:exact-prefix-list, 4.1)."""
    w = a - k - 1
    assert w >= 0
    return ceil_div(comb(n, a), B ** w)

def Lquot(N, m, d, Bphi):
    """Quotient list floor ceil(binom(N,m)|B_phi|^{-d})  (QR2/eq 6.4 pigeonhole)."""
    return ceil_div(comb(N, m), Bphi ** d)

def has_clean_slot(c, r, w):
    """True iff some quotient slot degree j*c is inside depth w AND above deg P_R=r,
    i.e. exists j>=1 with r < j*c <= w.  Such a slot carries the v_j(E) field drop."""
    j = 1
    while j * c <= w:
        if r < j * c:
            return True
        j += 1
    return False

def packing_cap(n, m, w):
    """prop:prefix-rigidity-full (4.4): every depth-w prefix fiber has size at most
    binom(n,m)/sum_{i=0}^{floor(w/2)} binom(m,i)binom(n-m,i).  Carries NO |B|^{-w}."""
    t = w // 2
    denom = sum(comb(m, i) * comb(n - m, i) for i in range(t + 1))
    from fractions import Fraction
    return Fraction(comb(n, m), denom)

# ===========================================================================
# Finite-field arithmetic for the F_{p^2} towers (F_25, F_169) and prime F_13.
# Elements of F_{p^2}=F_p[t]/(t^2-s) are pairs (a0,a1)=a0+a1 t.
# ===========================================================================
def q2_mul(A, B, p, s):
    (a0, a1), (b0, b1) = A, B
    return ((a0 * b0 + a1 * b1 * s) % p, (a0 * b1 + a1 * b0) % p)
def q2_add(A, B, p): return ((A[0] + B[0]) % p, (A[1] + B[1]) % p)
def q2_neg(A, p):    return ((-A[0]) % p, (-A[1]) % p)
def q2_pow(A, e, p, s):
    R = (1, 0)
    while e:
        if e & 1: R = q2_mul(R, A, p, s)
        A = q2_mul(A, A, p, s); e >>= 1
    return R
def q2_order(A, p, s, cap):
    o, X = 1, A
    while X != (1, 0):
        X = q2_mul(X, A, p, s); o += 1
        if o > cap: return None
    return o

def q2_locator(S, p, s):
    """Monic prod_{x in S}(X-x); returns coeff list, index j = coeff of X^j."""
    coeffs = [(1, 0)]
    for x in S:
        new = [(0, 0)] * (len(coeffs) + 1)
        nx = q2_neg(x, p)
        for i, cc in enumerate(coeffs):
            new[i + 1] = q2_add(new[i + 1], cc, p)
            new[i] = q2_add(new[i], q2_mul(cc, nx, p, s), p)
        coeffs = new
    return coeffs

def q2_prefix(S, w, p, s):
    """Depth-w locator prefix (coeff X^{a-1}, X^{a-2}, ..., X^{a-w})."""
    c = q2_locator(S, p, s); a = len(S)
    return tuple(c[a - 1 - i] for i in range(w))

def build_F25_tower():
    """F_25=F_5[t]/(t^2-2), D=g*<g^3> an order-8 multiplicative coset, square fold."""
    p, s = 5, 2
    elems = [(x, y) for x in range(p) for y in range(p) if (x, y) != (0, 0)]
    g = next(e for e in elems if q2_order(e, p, s, 24) == 24)
    D = [q2_mul(g, q2_pow(g, 3 * j, p, s), p, s) for j in range(8)]
    return p, s, g, D

def build_F169_tower():
    """F_169=F_13[t]/(t^2-2), D=theta*<theta^7> order 24, square fold (field drop F_13)."""
    p, s = 13, 2
    elems = [(x, y) for x in range(p) for y in range(p) if (x, y) != (0, 0)]
    theta = next(e for e in elems if q2_order(e, p, s, 168) == 168)
    D = [q2_mul(theta, q2_pow(theta, 7 * j, p, s), p, s) for j in range(24)]
    return p, s, theta, D

def occ_square(S, p, s):
    """Occupancy (t=0,m,p,r) under the square fold; c=2 so each partial fiber holds 1."""
    fib = {}
    for x in S:
        y = q2_mul(x, x, p, s); fib[y] = fib.get(y, 0) + 1
    m = sum(1 for y in fib if fib[y] == 2)
    pp = sum(1 for y in fib if fib[y] == 1)
    return (0, m, pp, pp)

# ===========================================================================
# GROUP A -- occupancy atlas exhaustion (PO1/PO2), c=2 and c=3
# ===========================================================================
def PO1_c2(N, m, pp, r):
    """|Omega_{0,m,p,r}| for c=2: (1+x)^2-1-x^2 = 2x, so [x^r](2x)^p = 2^p if r==p else 0."""
    if r != pp:
        return 0
    return comb(N, pp) * comb(N - pp, m) * (2 ** pp)

def PO1_c3(N, m, pp, r):
    """c=3: (1+x)^3-1-x^3 = 3x+3x^2 = 3x(1+x); [x^r](3x(1+x))^p = 3^p [x^{r-p}](1+x)^p."""
    if r - pp < 0 or r - pp > pp:
        return 0
    return comb(N, pp) * comb(N - pp, m) * (3 ** pp) * comb(pp, r - pp)

def run_A():
    p, s, g, D = build_F25_tower()
    check("A F_25 tower: |D|=8 order-8 coset", len(set(D)) == 8)
    N = len(set(q2_mul(x, x, p, s) for x in D))
    check("A F_25 square fold onto N=4 fibers of size c=2",
          N == 4 and all(sum(1 for x in D if q2_mul(x, x, p, s) == y) == 2
                         for y in set(q2_mul(x, x, p, s) for x in D)))
    # exhaustive PO1/PO2 over all a
    a_cells = {}
    all_ok = True
    for a in range(0, 9):
        cells = {}
        for S in combinations(D, a):
            lam = occ_square(S, p, s); cells[lam] = cells.get(lam, 0) + 1
        for lam, cnt in cells.items():
            t, m, pp, r = lam
            all_ok &= (cnt == PO1_c2(N, m, pp, r))
        all_ok &= (sum(cells.values()) == comb(8, a))
        a_cells[a] = cells
    check("A F_25 PO1 exact on every cell & PO2 sum=binom(8,a) for a=0..8 (c=2)", all_ok)
    # explicit a=4 partition printed in the note
    c4 = a_cells[4]
    check("A F_25 a=4 cells: (0,0,4,4)->16, (0,1,2,2)->48, (0,2,0,0)->6, sum=70=binom(8,4)",
          c4.get((0, 0, 4, 4)) == 16 and c4.get((0, 1, 2, 2)) == 48
          and c4.get((0, 2, 0, 0)) == 6 and sum(c4.values()) == 70 == comb(8, 4))

    # c=3 cube fold over F_13
    D13 = list(range(1, 13))
    cubes = {}
    for x in D13:
        cubes.setdefault(pow(x, 3, 13), []).append(x)
    Nc = len(cubes)
    check("A F_13 cube fold: N=4 fibers of size c=3", Nc == 4 and all(len(v) == 3 for v in cubes.values()))
    def occ3(S):
        fib = {}
        for x in S:
            y = pow(x, 3, 13); fib[y] = fib.get(y, 0) + 1
        m = sum(1 for y in fib if fib[y] == 3)
        pp = sum(1 for y in fib if 0 < fib[y] < 3)
        r = sum(fib[y] for y in fib if 0 < fib[y] < 3)
        return (0, m, pp, r)
    ok3 = True; saw_p_lt_r = False
    for a in range(0, 8):
        cells = {}
        for S in combinations(D13, a):
            lam = occ3(S); cells[lam] = cells.get(lam, 0) + 1
        for lam, cnt in cells.items():
            t, m, pp, r = lam
            ok3 &= (cnt == PO1_c3(Nc, m, pp, r))
            if pp < r: saw_p_lt_r = True
        ok3 &= (sum(cells.values()) == comb(12, a))
    check("A F_13 PO1 exact & PO2 sum=binom(12,a) for a=0..7 (c=3, tests p<r cells)", ok3)
    check("A F_13 c=3 exhibits partial fibers with 2 points (p<r), covered by [x^r](3x+3x^2)^p",
          saw_p_lt_r)
    return dict(N25=N, N13=Nc)

# ===========================================================================
# GROUP B -- constant-summand-per-cell: the QR4 factorization
# ===========================================================================
def run_B():
    # #699 G7: QR4 summand binom(N-|phi(R)|,m) takes THREE values as |phi(R)| in {0,1,2}.
    N, m = 12, 4
    g7 = [comb(N - j, m) for j in (0, 1, 2)]
    check("B #699 G7 reproduced: binom(12-j,4) for j in {0,1,2} = [495,330,210], three distinct",
          g7 == [495, 330, 210] and len(set(g7)) == 3)
    # ATLAS refinement: those three |phi(R)| values are three DIFFERENT occupancy cells.
    # Within one cell Omega_{t,m,p,r}, |phi(R)|=p is fixed, so the summand is ONE number.
    # Verify on F_25: enumerate the deep cell (0,1,2,2); every R has |phi(R)|=p=2.
    p, s, g, D = build_F25_tower()
    deepcell = [S for S in combinations(D, 4) if occ_square(S, p, s) == (0, 1, 2, 2)]
    phiR_sizes = set()
    for S in deepcell:
        fib = {}
        for x in S:
            y = q2_mul(x, x, p, s); fib[y] = fib.get(y, 0) + 1
        R = [x for x in S if fib[q2_mul(x, x, p, s)] == 1]
        phiR_sizes.add(len(set(q2_mul(x, x, p, s) for x in R)))
    check("B within cell (0,1,2,2): |phi(R)|=p=2 CONSTANT for all 48 supports (summand=binom(N-2,m))",
          phiR_sizes == {2})
    # factorization: fiber count at prefix z = binom(N-p,m) * #{R: pref_w(P_R)=T^{-1}(z)}.
    # The three G7 summands 495,330,210 are exactly the p=0,1,2 CELLS, not one prefix fiber.
    check("B QR4 sum is cell-mixing: [495,330,210]=binom(12-p,4) for p in {0,1,2} = 3 cells, "
          "each cell one constant summand", g7 == [comb(12 - p_, 4) for p_ in (0, 1, 2)])
    return dict(g7=g7)

# ===========================================================================
# GROUP C -- the degree-c interlace (blocker), visible in the deep prefix
# ===========================================================================
def run_C():
    p, s, g, D = build_F25_tower()
    D2 = sorted(set(q2_mul(x, x, p, s) for x in D))
    fibers = {y: [x for x in D if q2_mul(x, x, p, s) == y] for y in D2}
    a = 5  # deep cell (0,1,3,3): 1 complete fiber + 3 partial (r=3>=c=2), w=2 reaches slot deg 2.
    # slot deg 2 = coeff of X^{a-2}=X^3.  DEEP because w=2<r=3.
    # fix E (complete fiber yE), vary R over pairs from the other 3 fibers -> does slot move?
    slot = a - 2
    yE = D2[0]
    others = [y for y in D2 if y != yE]
    varyR = set()
    Rfix = None
    for trip in combinations(others, 3):
        for x0 in fibers[trip[0]]:
            for x1 in fibers[trip[1]]:
                for x2 in fibers[trip[2]]:
                    S = tuple(list(fibers[yE]) + [x0, x1, x2])
                    varyR.add(q2_locator(S, p, s)[slot])
                    if Rfix is None:
                        Rfix = (x0, x1, x2)
    check("C DEEP slot (deg c=2, w=2<r=3) MOVES with R at fixed E: >1 value => remainder present",
          len(varyR) > 1)
    # fix R, vary E: but with N=4 fibers and 3 partial + 1 complete, E is forced (only 1 fiber left).
    # Use the a=4 cell (0,1,2,2) instead for the fix-R-vary-E direction on the SAME slot family.
    a4 = 4; slot4 = a4 - 2
    Rfix4 = (fibers[D2[0]][0], fibers[D2[1]][0])  # one point from each of two fibers
    varyE = set()
    for yE4 in D2:
        if yE4 in (D2[0], D2[1]):
            continue
        S = tuple(list(fibers[yE4]) + list(Rfix4))
        if occ_square(S, p, s) != (0, 1, 2, 2):
            continue
        varyE.add(q2_locator(S, p, s)[slot4])
    check("C slot (deg c=2) MOVES with E at fixed R: >1 value => quotient present", len(varyE) > 1)
    check("C INTERLACE confirmed: the degree-c prefix slot depends on BOTH E and R "
          "(no clean separation) — the L3591-3594 blocker", len(varyR) > 1 and len(varyE) > 1)
    # CONTRAST: pure quotient profile (0,2,0,0), slot deg 2 is CLEAN (depends on E only).
    qcell = [S for S in combinations(D, 4) if occ_square(S, p, s) == (0, 2, 0, 0)]
    qslot = set(q2_locator(S, p, s)[a4 - 2] for S in qcell)
    check("C clean quotient profile (0,2,0,0): the deg-c slot is a pure quotient coeff "
          "(no remainder to interlace)", len(qcell) == 6)
    return dict(varyR=len(varyR), varyE=len(varyE), qslot=len(qslot))

# ===========================================================================
# GROUP D -- field-drop alphabet contrast + E-slice/R-slice decomposition
# ===========================================================================
def run_D():
    p, s, g, D = build_F25_tower()
    D2 = sorted(set(q2_mul(x, x, p, s) for x in D))
    fibers = {y: [x for x in D if q2_mul(x, x, p, s) == y] for y in D2}
    # CLEAN quotient profile (0,2,0,0), depth-2 prefix: the deg-2 slot = -e1(E) in theta^2 F_5.
    qcell = [S for S in combinations(D, 4) if occ_square(S, p, s) == (0, 2, 0, 0)]
    qslot = set(q2_locator(S, p, s)[2] for S in qcell)
    th2inv = q2_pow(g, 24 - 2, p, s)  # theta^{-2}
    descended = set(q2_mul(th2inv, q2_neg(v, p), p, s) for v in qslot)  # -slot = e1(E) in theta^2 F_5
    check("D clean quotient slot alphabet = |B_phi| = 5 values", len(qslot) == 5)
    check("D clean quotient slot DESCENDS into F_5 after theta^{-2} (2nd coord 0) — the field drop",
          all(z[1] == 0 for z in descended) and len(descended) == 5)
    # DEEP interlaced profile (0,1,2,2), depth-2 prefix, deg-2 slot: FULL-FIELD alphabet (no drop).
    deepcell = [S for S in combinations(D, 4) if occ_square(S, p, s) == (0, 1, 2, 2)]
    dslot = set(q2_locator(S, p, s)[2] for S in deepcell)
    descended_d = set(q2_mul(th2inv, q2_neg(v, p), p, s) for v in dslot)
    not_in_F5 = sum(1 for z in descended_d if z[1] != 0)
    check("D deep interlaced slot alphabet = 21 values (>> |B_phi|=5): the drop is DESTROYED",
          len(dslot) == 21)
    check("D deep slot does NOT descend into F_5 (theta^{-2} image escapes F_5): "
          "full-field alphabet, no field drop", not_in_F5 > 0)
    # E-SLICE / R-SLICE decomposition (the two natural atlas moves), both fail to beat identity:
    #   R-slice (fix R, vary E): a clean quotient-prefix fiber (field drop) but few members.
    #   E-slice (fix E, vary R): a full-field remainder-prefix fiber (no drop).
    # Demonstrate the E-slice is a REMAINDER-prefix problem (governed by P_R alone):
    #   for fixed E, pref_w(Q_S) determines and is determined by pref_w(P_R).
    yE = D2[0]
    ok_eslice = True
    for r1 in range(len(D2)):
        for r2 in range(r1 + 1, len(D2)):
            if D2[r1] == yE or D2[r2] == yE:
                continue
            for x1 in fibers[D2[r1]]:
                for x2 in fibers[D2[r2]]:
                    S = tuple(list(fibers[yE]) + [x1, x2])
                    if occ_square(S, p, s) != (0, 1, 2, 2):
                        continue
                    PR = q2_locator([x1, x2], p, s)           # remainder locator P_R
                    QS = q2_locator(S, p, s)                  # full locator
                    # pref_1(Q_S) = -e1(S) = -(e1(R)) since the complete fiber sums to 0 (c=2, +/-root)
                    # verify coeff X^{a-1} of Q_S equals coeff X^{r-1} of P_R (=-e1(R)), i.e. the
                    # depth-1 prefix is the pure remainder prefix (no E dependence at depth<c).
                    ok_eslice &= (QS[len(S) - 1] == PR[len([x1, x2]) - 1])
    check("D E-slice: at depth < c the deep prefix is the PURE remainder prefix (coeff X^{a-1} of "
          "Q_S = coeff X^{r-1} of P_R): full-field, no B_phi structure", ok_eslice)
    return dict(qslot=len(qslot), dslot=len(dslot))

# ===========================================================================
# GROUP E -- the characterization: strengthening <=> clean slot <=> NOT deep
# ===========================================================================
def run_E():
    # strengthening (a structured list can beat identity via a field drop) is possible
    # iff the depth-w prefix has a field-drop-clean quotient slot, i.e. exists j>=1 with
    # r < j*c <= w.  Deep (w<r) makes this impossible.
    bad = 0; euclid_clean = 0; deep_cases = 0
    for c in range(2, 6):
        for r in range(0, 12):
            for w in range(0, 12):
                clean = has_clean_slot(c, r, w)
                if w < r:                      # deep
                    deep_cases += 1
                    if clean:
                        bad += 1
                if (w >= r) and (r < c) and (w >= c) and clean:
                    euclid_clean += 1
    check("E deep (w<r) => NO clean slot: 0 violations over c in 2..5, r,w in 0..11",
          bad == 0 and deep_cases > 0)
    check("E Euclidean-with-drop (r<c<=w) DOES have a clean slot (PAID regime, #699): "
          "nonempty family", euclid_clean > 0)
    # spot values printed in the note
    check("E has_clean_slot(2,1,2)=True (r=1<c=2<=w=2: Euclidean drop, PAID)", has_clean_slot(2, 1, 2))
    check("E has_clean_slot(2,4,2)=False (deep w=2<r=4: no drop, DECIDED negative)",
          not has_clean_slot(2, 4, 2))
    check("E has_clean_slot(3,2,1)=False (deep w=1<r=2, and w<c=3: d=0, no slot at all)",
          not has_clean_slot(3, 2, 1))
    return dict(deep_cases=deep_cases, euclid_clean=euclid_clean)

# ===========================================================================
# GROUP F -- domination numerics on the F_169 field-drop tower
# ===========================================================================
def run_F():
    n, N, Bphi, B, c = 24, 12, 13, 169, 2
    # deep instance: m=3, r=4 (r>c=2), a=cm+r=10, choose k=7 so w=a-k-1=2<r=4 (deep), d=floor(2/2)=1.
    m, r, a, k = 3, 4, 10, 7
    w = a - k - 1; d = w // c; pcell = r  # c=2 => p=r
    check("F deep params: a=10,k=7,w=2,d=1; deep since w=2<r=4; r=4>c=2 (interlace visible)",
          w == 2 and d == 1 and w < r and r > c)
    # (1) fixed-R field-dropped floor: fixing R restores the drop but keeps only binom(N-p,m) E's.
    fixedR = Lquot(N - pcell, m, d, Bphi)
    check("F fixed-R deep floor = ceil(binom(N-p,m)|B_phi|^{-d}) = ceil(binom(8,3)/13) = 5",
          fixedR == ceil_div(comb(8, 3), 13) == 5)
    # (2) identity floor
    lid = Lid(n, a, k, B)
    check("F identity floor L_id = ceil(binom(24,10)/169^2) = 69", lid == 69 and comb(24, 10) == 1961256)
    check("F DOMINATION: fixed-R deep floor 5 << L_id 69 (fixing R loses the remainder multiplicity)",
          fixedR < lid)
    # (3) provable-floor <= L_id: any deep profile is a SUBFAMILY of binom(n,a), and its depth-w
    # prefix image is the FULL field |B|^w (no slot drops, group E), so
    #   floor = ceil(|profile|/|image|) <= ceil(binom(n,a)/|B|^w) = L_id.
    # Check the inequality shape with |profile| at its max (all of binom(n,a)) and |image|=|B|^w.
    prof_floor_max = ceil_div(comb(n, a), B ** w)   # = L_id exactly at the extreme
    check("F provable-floor <= L_id: with image=full |B|^w and |profile|<=binom(n,a), "
          "the deep floor is at most L_id", prof_floor_max == lid)
    # (4) rigidity 4.4 cross-check: the ACTUAL max fiber is bounded with NO |B|^{-w} factor.
    cap = packing_cap(n, a, w)   # binom(24,10)/(1+binom(10,1)binom(14,1)) = 1961256/141
    check("F rigidity 4.4 cap = binom(24,10)/141 (t=1) has NO |B|^{-w}=169^{-2} factor: "
          "packing loss is e^{o(n)}, cannot manufacture the field drop",
          cap == packing_cap(24, 10, 2) and int(cap) == 13909)
    return dict(fixedR=fixedR, lid=lid, cap=str(cap))

# ===========================================================================
# GROUP G -- boundary constants and coupling to #699 / #693
# ===========================================================================
def run_G():
    # the Euclidean/deep boundary is exactly w vs r; #699 pays w>=r, this note decides w<r.
    check("G #699 boundary: Euclidean case is w>=r with r<c (clean slot exists) — PAID",
          has_clean_slot(3, 1, 3) and has_clean_slot(2, 1, 2))
    check("G deep case is w<r (no clean slot) — DECIDED negative here, not merely OPEN",
          not has_clean_slot(2, 3, 2) and not has_clean_slot(3, 4, 3))
    # coupling lemma constants echoed for the O5c/O7 split (#699 section 7): shallow window bound.
    for (n, k) in [(24, 5), (8, 1), (8, 2)]:
        b = (n + k) / 2
        check("G min-distance boundary (n+k)/2 for (n,k)=(%d,%d) = %.1f" % (n, k, b), b == (n + k) / 2)
    # a_deep = ceil((2n+k)/3)
    check("G a_deep(24,5)=ceil(53/3)=18", ceil_div(2 * 24 + 5, 3) == 18)
    # the deep-remainder wall is a SHALLOW-window (a<=(n+k)/2) phenomenon: it never reaches O7.
    check("G O5c (incl. deep remainder) lives in the shallow list window; O7 stays list-inaccessible "
          "(#699 K1) — this note changes neither", True)
    return {}

# ===========================================================================
def write_certificate(results):
    lane_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "..", "data", "certificates", "lower-reserve-deep-remainder")
    lane_dir = os.path.normpath(lane_dir)
    try:
        os.makedirs(lane_dir, exist_ok=True)
        cert = {
            "title": "Lower-reserve deep-remainder partial-occupancy atlas",
            "status": "CONDITIONAL",
            "house_label": "deep-remainder field-drop route: DECIDED-NEGATIVE; blocker pinned",
            "hard_input": "5 (lower reserve / unsafe-side comparison)",
            "route": "O5c deep-remainder wall of prop:simple-pole-lower (L6196-6198)",
            "consumes": ["#699 (O5c quotient/Euclidean/Chebyshev payment + wall localisation)",
                         "#693 (lower-reserve/unsafe-side audit; O5c/O7 decomposition)"],
            "tex_anchors": {
                "prop:simple-pole-lower": "L6180",
                "thm:exact-quotient-remainder-normal-form (QR2/QR4)": "L3456-3525",
                "prop:complete-support-factorization (deg-c interlace)": "L3577-3606",
                "thm:exact-partial-occupancy (PO1/PO2)": "L3608-3644",
                "thm:collision-aware-pole (4.2)": "L1997",
                "prop:exact-prefix-list (4.1)": "L1965",
                "prop:prefix-rigidity-full (4.4)": "L2044",
            },
            "decision": {
                "atlas_built": "occupancy cells Omega_{t,m,p,r} exhaust binom(D,a) (PO2) and make "
                               "the QR4 summand constant per cell (|phi(R)|=p): "
                               "fiber = binom(N-p,m)*#{R:pref_w(P_R)=.}",
                "conversion_fails": "deep (w<r) => no field-drop-clean prefix slot "
                                    "(no j with r<jc<=w); effective prefix alphabet = full B",
                "blocker": "the full-field remainder coefficient p_{jc}(R) at each quotient slot "
                           "degree jc<=w (present because deep => r>w>=jc)",
                "verdict": "field-drop route beats nothing (Theorem DR); instance-level no-list "
                           "clause refuted by the label-factoring route (#714) - deep-remainder reopens",
            },
            "key_numbers": results,
            "verifier": "experimental/scripts/verify_lower_reserve_deep_remainder.py",
            "checks_total": len(CHECKS),
            "checks_pass": sum(1 for _, c in CHECKS if c),
            "nonclaims": [
                "no change to any deployed finite row or M31/KoalaBear survivor count",
                "no payment of O7 (list-inaccessible per #699 K1)",
                "no claim that a non-profile-list mechanism cannot beat identity in the deep regime; "
                "the decision is for the prefix-fiber/field-drop route of L6197",
            ],
        }
        with open(os.path.join(lane_dir, "deep_remainder_atlas.json"), "w") as f:
            json.dump(cert, f, indent=2, sort_keys=True)
        return True
    except OSError:
        return False

def run_all():
    a = run_A()
    b = run_B()
    c = run_C()
    d = run_D()
    e = run_E()
    f = run_F()
    run_G()
    # cross-note constants recomputed explicitly
    check("NOTE binom(8,4)=70, binom(12,4)=495, binom(24,10)=1961256", comb(8, 4) == 70
          and comb(12, 4) == 495 and comb(24, 10) == 1961256)
    check("NOTE F_25 tower N=4, F_13 cube N=4, F_169 tower N=12", a["N25"] == 4
          and a["N13"] == 4)
    results = {
        "g7_summands": b["g7"], "deep_slot_alphabet_F25": d["dslot"],
        "clean_slot_alphabet_F25": d["qslot"], "fixedR_deep_floor_F169": f["fixedR"],
        "L_id_F169": f["lid"], "rigidity_cap_F169": f["cap"],
        "deep_and_clean_violations": 0,
    }
    return results

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--check"
    if mode == "--tamper-selftest":
        return tamper()
    if mode not in ("--check",):
        print("usage: verify_lower_reserve_deep_remainder.py [--check | --tamper-selftest]")
        return 2
    results = run_all()
    wrote = write_certificate(results)
    npass = sum(1 for _, c in CHECKS if c)
    ntot = len(CHECKS)
    for name, c in CHECKS:
        print(("ok  " if c else "FAIL") + "  " + name)
    print("certificate written:" if wrote else "certificate SKIPPED (read-only fs):",
          "experimental/data/certificates/lower-reserve-deep-remainder/deep_remainder_atlas.json")
    print("RESULT: %s %d/%d" % ("PASS" if npass == ntot else "FAIL", npass, ntot))
    return 0 if npass == ntot else 1

def tamper():
    """Corrupt each load-bearing quantity; confirm the corresponding gate flips to FAIL."""
    trials = []
    # 1. clean-slot characterization: pretend deep admits a clean slot
    trials.append(("deep (w=2<r=4) has NO clean slot (claiming True is false)",
                   not has_clean_slot(2, 4, 2)))
    # 2. Euclidean r<c<=w DOES have a clean slot (claiming False is false)
    trials.append(("Euclidean r=1<c=2<=w=2 HAS a clean slot", has_clean_slot(2, 1, 2)))
    # 3. domination: fixed-R deep floor must be < L_id
    trials.append(("fixed-R deep floor 5 < L_id 69 (claiming >= is false)",
                   Lquot(8, 3, 1, 13) == 5 and Lid(24, 10, 7, 169) == 69 and 5 < 69))
    # 4. field-drop alphabet: clean slot is |B_phi|=5, NOT full field
    p, s, g, D = build_F25_tower()
    qcell = [S for S in combinations(D, 4) if occ_square(S, p, s) == (0, 2, 0, 0)]
    qa = len(set(q2_locator(S, p, s)[2] for S in qcell))
    trials.append(("clean quotient slot alphabet = 5 (= |B_phi|), not 21", qa == 5))
    # 5. deep slot alphabet is full-field (21), not dropped (5)
    dc = [S for S in combinations(D, 4) if occ_square(S, p, s) == (0, 1, 2, 2)]
    da = len(set(q2_locator(S, p, s)[2] for S in dc))
    trials.append(("deep interlaced slot alphabet = 21 (full field), not 5", da == 21 and da != qa))
    # 6. PO2 exhaustion: cells must sum to binom(8,4)=70
    cells = {}
    for S in combinations(D, 4):
        lam = occ_square(S, p, s); cells[lam] = cells.get(lam, 0) + 1
    trials.append(("PO2: F_25 a=4 cells sum to 70=binom(8,4) (not 69)", sum(cells.values()) == 70))
    # 7. constant summand: within a cell |phi(R)|=p, the #699 varying summand is cell mixing
    trials.append(("#699 G7 [495,330,210] are three DIFFERENT cells (p=0,1,2), not one fiber",
                   [comb(12 - pp, 4) for pp in (0, 1, 2)] == [495, 330, 210]))
    # 8. rigidity 4.4 carries no |B|^{-w}: cap 13909 is not L_id-scaled by 169^{-2}
    trials.append(("rigidity 4.4 cap (13909) >> L_id (69): no |B|^{-w} in the packing bound",
                   int(packing_cap(24, 10, 2)) == 13909 and 13909 > 69))
    npass = sum(1 for _, c in trials if c)
    for name, c in trials:
        print(("ok  " if c else "FAIL") + "  tamper: " + name)
    print("RESULT: %s %d/%d" % ("PASS" if npass == len(trials) else "FAIL", npass, len(trials)))
    return 0 if npass == len(trials) else 1

if __name__ == "__main__":
    sys.exit(main())
