#!/usr/bin/env sage
# -*- mode: python -*-
r"""
D3: combinatorial structure of the EXTREMAL E_3-saturators (defines the "structured"
alternative in the shared BGK inverse-theorem lemma).  Step 3 ruled out GEOMETRIC
structure (pencil monodromy is full S_{ell-1} for extremal AND random), so we probe
ADDITIVE/MULTIPLICATIVE-combinatorial structure, extremal vs random:

  (A) how E_3 = ell-2 is realized: fiber-size mu_b distribution over mu_ell-cosets;
  (B) heavy-fiber exponent-set structure: for a coset with a big fiber (value v hit m
      times), the exponent set J = {j : Gamma(zeta^j b) = v} <= Z/ell -- is J an AP /
      structured?  (its difference multiset J-J);
  (C) multiplicative & additive ENERGY of the value set V = Gamma(mu_ell) vs random baseline;
  (D) DIRECTIONS / Carlitz-McConnel: difference quotients (Gamma(x)-Gamma(y))/(x-y),
      x,y in mu_ell -- do EXTREMAL Gamma concentrate them in few multiplicative classes?
"""
import random
from collections import Counter

def setup(gm, p, ell):
    F = GF(p); g = F.multiplicative_generator(); nb = (p-1)//ell
    zeta = g**nb; H = [zeta**j for j in range(ell)]           # mu_ell (as field elts), H[j]=zeta^j
    Rx = PolynomialRing(F, 'X'); X = Rx.gen()
    Gam = sum(F(gm[r-1])*X**r for r in range(1, ell))
    return F, g, nb, zeta, H, Gam

def E3_and_fibers(gm, p, ell):
    F, g, nb, zeta, H, Gam = setup(gm, p, ell)
    E3 = 0; mu_list = []; heavy = []   # heavy: (coset_i, mu_b, heavy_value, exponent_set)
    for i in range(nb):
        b = g**i
        vals = [Gam(b*H[j]) for j in range(ell)]
        cnt = Counter(vals); mu = max(cnt.values()); mu_list.append(mu)
        if mu >= 3:
            E3 += mu - 2
            v = max(cnt, key=lambda k: cnt[k])
            J = frozenset(j for j in range(ell) if vals[j] == v)
            heavy.append((i, mu, v, J))
    return E3, mu_list, heavy

def ap_test(J, ell):
    # is J (subset of Z/ell) an arithmetic progression?  (difference multiset most-common step)
    J = sorted(J)
    if len(J) < 2: return None, {}
    diffs = Counter((a-b) % ell for a in J for b in J if a != b)
    top_step, top_cnt = diffs.most_common(1)[0]
    is_ap = (top_cnt == len(J)-1) or (top_cnt >= 2*(len(J)-1))  # AP-ish signal (heuristic)
    return top_step, dict(diffs.most_common(4))

def mult_add_energy(V, p):
    # DISTINCT value set (disentangle from fiber multiplicity): E_x = #{(a,b,c,d) in V_set: a*b=c*d}
    from collections import Counter as C
    Vs = [v for v in set(V) if v != 0]
    prods = C(); sums = C()
    for a in Vs:
        for b in Vs:
            prods[a*b] += 1; sums[a+b] += 1
    Ex = sum(c*c for c in prods.values()); Ep = sum(c*c for c in sums.values())
    m = len(Vs)
    base = m*m + (m**4)/p if p else m*m       # generic-set baseline ~ m^2 + m^4/p
    return Ex, Ep, m, float(base)

def moments(gm, p, ell):
    # M_2 = sum_b sum_v N_b(v)^2, M_3 = ... N_b(v)^3  (the actual coincidence 'energy' the lemma bounds)
    F, g, nb, zeta, H, Gam = setup(gm, p, ell)
    M2 = 0; M3 = 0
    for i in range(nb):
        b = g**i
        c = Counter(Gam(b*H[j]) for j in range(ell))
        for v in c.values():
            M2 += v*v; M3 += v*v*v
    # generic (Poisson) baseline: each coset ~ ell values, N~1 => M2 ~ nb*ell + coincidences
    return M2, M3, nb*ell

def directions(gm, p, ell):
    # difference quotients over mu_ell; distinct NONZERO count + concentration in mu_ell-cosets.
    # NB: zero quotients = pairs with Gamma(x)=Gamma(y) (the E_3 coincidences) -> separated, not counted
    # as "directions". mu_ell-coset label of q is q^ell (constant on cosets since zeta^ell=1), NOT q^nb.
    F, g, nb, zeta, H, Gam = setup(gm, p, ell)
    quotients = []
    for a in range(ell):
        for b in range(ell):
            if a == b: continue
            xa, xb = H[a], H[b]
            quotients.append((Gam(xa)-Gam(xb))/(xa-xb))
    nz = [q for q in quotients if q != 0]
    zero = len(quotients) - len(nz)
    distinct_nz = len(set(nz))
    labels = Counter(q**ell for q in nz)            # true mu_ell-coset label
    top = labels.most_common(1)[0][1] if labels else 0
    return len(quotients), distinct_nz, zero, len(labels), top

def analyze(tag, gm, p, ell):
    E3, mu_list, heavy = E3_and_fibers(gm, p, ell)
    mudist = dict(sorted(Counter(mu_list).items()))
    F, g, nb, zeta, H, Gam = setup(gm, p, ell)
    V = [Gam(H[j]) for j in range(ell)]        # value set on the base coset mu_ell (b=1)
    Ex, Ep, mdist, base = mult_add_energy(V, p)
    M2, M3, mbase = moments(gm, p, ell)
    nq, distinct_nz, zero, nclass, topclass = directions(gm, p, ell)
    print("  %-20s E_3=%2d  mu-dist=%s  #heavy=%d" % (tag, E3, mudist, len(heavy)))
    print("       moments: M_2=%d M_3=%d  (Poisson-ish baseline nb*ell=%d)" % (M2, M3, mbase))
    print("       DISTINCT value-set (m=%d): mult-energy E_x=%d add-energy E_p=%d (generic base~%.0f)"
          % (mdist, Ex, Ep, base))
    print("       directions (nonzero): %d/%d pairs -> %d distinct; top TRUE mu_ell-class hit %d  [#zero(coincidence) pairs=%d]"
          % (nq-zero, nq, distinct_nz, topclass, zero))
    if heavy:
        i, mu, v, J = max(heavy, key=lambda h: h[1])
        step, dd = ap_test(J, ell)
        print("       heaviest fiber: coset#%d mu=%d  exponent-set J=%s  top diff-step=%s dist=%s"
              % (i, mu, sorted(J), step, dd))
    return E3

def main():
    SAT = [("EXTREMAL l=11", 331, 11, [97,29,97,239,171,92,143,155,270,1]),
           ("EXTREMAL l=13", 313, 13, [254,289,29,276,242,219,201,261,79,232,133,1]),
           ("EXTREMAL l=17", 103, 17, [30,82,52,3,7,90,70,30,27,71,85,33,12,85,66,0])]
    print("D3: extremal E_3-saturator combinatorial structure vs random\n -- EXTREMAL --")
    for (tag,p,ell,gm) in SAT: analyze(tag, gm, p, ell)
    print(" -- RANDOM (E_3~0) --")
    for (p,ell) in [(331,11),(313,13),(103,17)]:
        rng = random.Random(int(9*p+ell))
        for k in range(2):
            gm=[rng.randrange(p) for _ in range(ell-1)]
            if any(gm): analyze("random l=%d #%d"%(ell,k), gm, p, ell)
    print("\n READ (Codex-verified): the ONLY clean extremal-vs-random separator is the coincidence")
    print(" moment M_2/M_3 (near-definitional). DISTINCT value-set mult/add energy does NOT separate")
    print(" (the multiset signal was fiber multiplicity); directions/Carlitz-McConnel concentration does")
    print(" NOT separate (top true mu_ell-class ~equal extremal vs random); heavy fibers are not APs.")
    print(" => the extremal structure is NOT a named combinatorial object at toy scale -> corroborates")
    print(" D1: L1's E_3<=ell-2 is a RANK statement (dim Syz<=K), not a moment/energy inverse theorem.")
    return 0

import sys; sys.exit(main())
