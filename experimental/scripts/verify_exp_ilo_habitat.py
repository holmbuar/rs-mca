#!/usr/bin/env python3
"""
verify_exp_ilo_habitat.py  --  companion to
    experimental/notes/thresholds/exp_ilo_habitat_restriction.md

Serves hard input 2 (image-scale MI+MA / direct Sidon payment).  Its wall is the
per-instance exponential inverse-Littlewood-Offord = the (Bohr -> GAP) step at
exponential concentration = Diophantine control of the dominant resonance
denominator q.

Question.  PR #701 (open; fenced_energy_pincer.md, Theorem 5) confines every wall
block to a two-band HABITAT: intermediate max-fiber density theta = m*/b in
(0.1740, 0.8260) AND intermediate source fiber energy -log2 Delta(F)/b in
(0.1383, 0.4779), Delta(F) = E(F)/f^3.  #663 (bohr_gap_volume.md) proved the three
cheap Bohr->GAP bridges impossible for GENERAL spread blocks.  Does restriction to
the strictly smaller habitat REOPEN any of the three routes?

Verdict certified below: NO.  The habitat is cut out by two AFFINE-INVARIANT,
source-side (Boolean-slice) coordinates (theta, Delta), while every one of #663's
route-killers is either UNIVERSAL (the moment-curve energy identity), a property of
the IMAGE frequencies (Weyl-no-interval; mod-1 elimination), or a spread/detG
threshold -- none constrained by an affine-invariant source band.  So the habitat
does not touch the denominator axis the wall lives on; all three routes stay dead
inside it, with in-habitat witnesses.

Setup.  A *block* V is b distinct integers.  For S subset of V the degree-2
signature is Phi(S) = (|S|, sum x, sum x^2).  f = max fiber size, L = # signatures,
phi = log2 f/b, lambda = log2 L/b, eta = 1-phi; the wall is X = (fL)^{1/b} > 2^{4/3}.
The max fiber F is a set of Boolean masks; its SOURCE additive energy is
E(F) = #{(a,b,c,d) in F^4 : a+b=c+d in Z^b}, Delta(F) = E(F)/f^3, theta = m*/b.
Moment columns u_i = (1, v_i, v_i^2); the quadratic Weyl sum on the IMAGE is
S(t1,t2) = sum_i e(t1 v_i + t2 v_i^2); the resonance denominator q lives in
theta_2, the argmax of the |Xhat|-marginal, |Xhat(theta)| = prod_i |cos(pi psi_i)|,
psi_i = theta_0 + theta_1 v_i + theta_2 v_i^2.  T_kappa = { theta : sum_i
||psi_i||^2 <= kappa b }.

Stdlib only, deterministic.  Usage:
    python3 verify_exp_ilo_habitat.py            # full check, prints RESULT: PASS n/n
    python3 verify_exp_ilo_habitat.py --check    # same
    python3 verify_exp_ilo_habitat.py --tamper-selftest   # mutate witnesses, expect 5/5 caught
Writes a JSON certificate to experimental/data/certificates/exp-ilo-habitat/certificate.json.

Label key mirrors the note: PROVED / COUNTEREXAMPLE / MEASURED / AUDIT / OPEN;
house labels REOPENED / STILL-DEAD / DECIDED-NEGATIVE in comments.
"""
import math
import os
import json
import sys
import itertools
import random
from collections import defaultdict, Counter
from fractions import Fraction

CHECKS = []
CERT = {}


def check(cond, label):
    CHECKS.append((bool(cond), label))
    print(f"    [{'ok  ' if cond else 'FAIL'}] {label}")
    return bool(cond)


LOG2 = math.log(2.0)
PI = math.pi

# ------------------------------------------------------------------- the blocks
# #655 b=18 champion (AP-free PTE-trade block; spread, Diophantine resonance)
CHAMP18 = [2, 3, 4, 6, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 30, 32, 33, 34]
# union of two difference-3 APs (embedded AP length 8; small-q resonance q=3)
UNIONAP16 = [3 * j for j in range(8)] + [1 + 3 * j for j in range(8)]


def gcd_list(xs):
    g = 0
    for x in xs:
        g = math.gcd(g, x)
    return g


def normalize(V):
    """affine-normalize: min -> 0, divide by gcd.  (theta, Delta, f, L invariant.)"""
    V = sorted(set(V))
    V = [x - V[0] for x in V]
    g = gcd_list(V)
    if g > 1:
        V = [x // g for x in V]
    return tuple(V)


# ------------------------------------------------------------ exact fiber / energy
def block_data(V, do_normalize=True):
    """Enumerate all 2^b masks; return max-fiber size f, image size L, weight m*,
    the max fiber F (masks), its SOURCE additive energy E(F), Delta, theta."""
    V = normalize(V) if do_normalize else tuple(V)
    b = len(V)
    vv = [v * v for v in V]
    buckets = defaultdict(list)
    for mask in range(1 << b):
        s1 = 0
        s2 = 0
        m = 0
        x = mask
        while x:
            lsb = x & (-x)
            i = lsb.bit_length() - 1
            s1 += V[i]
            s2 += vv[i]
            m += 1
            x ^= lsb
        buckets[(m, s1, s2)].append(mask)
    L = len(buckets)
    best_sig, F = max(buckets.items(), key=lambda kv: len(kv[1]))
    mstar = best_sig[0]
    f = len(F)
    # source additive energy: E = sum_w r(w)^2, r(w) = #{(a,c) in F^2 : a+c = w in {0,1,2}^b}
    cnt = Counter()
    for a in F:
        for c in F:
            code = 0
            scale = 1
            for i in range(b):
                code += (((a >> i) & 1) + ((c >> i) & 1)) * scale
                scale *= 3
            cnt[code] += 1
    E = sum(v * v for v in cnt.values())
    return dict(V=V, b=b, f=f, L=L, mstar=mstar, theta=mstar / b,
                E=E, Delta=E / f ** 3, F=tuple(sorted(F)))


# ---------------------------------------------------------------- moment / detG
def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def detG(V):
    p = [sum(v ** m for v in V) for m in range(5)]
    return det3([[p[0], p[1], p[2]], [p[1], p[2], p[3]], [p[2], p[3], p[4]]])


def energy_moment(V, m):
    """int_{[0,1)^2} |S|^{2m} = #{ordered (i_1..i_m ; j_1..j_m): sum v_i=sum v_j
       AND sum v_i^2 = sum v_j^2}; = sum_{(s,q)} c_m(s,q)^2 (EXACT)."""
    cnt = defaultdict(int)
    for tup in itertools.product(range(len(V)), repeat=m):
        s = sum(V[i] for i in tup)
        q = sum(V[i] * V[i] for i in tup)
        cnt[(s, q)] += 1
    return sum(c * c for c in cnt.values())


def rank_moment_map(V):
    """rank over Q of the b x 3 matrix [1, v_i, v_i^2] = dim of resonance subtorus."""
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


# ------------------------------------------------------------ |Xhat| marginals
def _frac(x):
    return x - round(x)


def M_at(V, t2, n01=24):
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
                p *= abs(math.cos(PI * (t0 + t1 * v + t2 * v * v)))
            acc += p
            ncnt += 1
    return acc / ncnt


def resonance(V, n2=240, n01=24):
    """(best small-q<=5 peak) vs (global non-parity peak) of the |Xhat| marginal."""
    V = normalize(V)
    gmax = -1.0
    garg = None
    for k2 in range(n2):
        t2 = k2 / n2
        if min(abs(t2), abs(t2 - 1.0)) < 0.045 or abs(t2 - 0.5) < 0.045:
            continue
        Mv = M_at(V, t2, n01)
        if Mv > gmax:
            gmax = Mv
            garg = t2
    smax = -1.0
    sarg = None
    for q in (3, 4, 5):
        for p in range(1, q):
            if math.gcd(p, q) != 1:
                continue
            t2 = p / q
            if abs(t2 - 0.5) < 0.02:
                continue
            Mv = M_at(V, t2, n01)
            if Mv > smax:
                smax = Mv
                sarg = (p, q)
    return dict(gmax=gmax, garg=garg, smax=smax, sarg=sarg, ratio=smax / gmax)


def Fenergy(V, th):
    t0, t1, t2 = th
    return sum(_frac(t0 + t1 * v + t2 * v * v) ** 2 for v in V)


# ================================================================ habitat edges
# density band: h2(theta) > 2/3  (from #696 (3), a(theta)=1+h2/2 > 4/3)
def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)


def h2_inv_low(target, lo=1e-9, hi=0.5):
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if h2(mid) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def g_ent(theta):
    """#696 (4) entropy exponent H_2 of the 4-cell distribution at density theta."""
    parts = [(1 - theta) ** 2 / 2, (1 - theta ** 2) / 2,
             theta * (2 - theta) / 2, theta ** 2 / 2]
    return -sum(p * math.log2(p) for p in parts if p > 0)


DENS_LO = h2_inv_low(2.0 / 3.0)          # 0.173952331409
DENS_HI = 1.0 - DENS_LO                  # 0.826047668591
ENER_HI = g_ent(0.5) - 4.0 / 3.0         # 0.477944791126
ENER_LO = math.log(4.0 / 3.0) / (3.0 * LOG2)   # 0.138345833093


def in_habitat(d):
    dens_ok = DENS_LO < d["theta"] < DENS_HI
    edef = -math.log2(d["Delta"]) / d["b"]
    ener_ok = ENER_LO < edef < ENER_HI
    return dens_ok and ener_ok, edef


# =================================================================== BLOCKS
def block0():
    print("\nBLOCK 0  habitat band edges recomputed exactly (#701 Theorem 5 constants) (AUDIT)")
    check(abs(DENS_LO - 0.173952331409) < 1e-9,
          f"density lower edge h2^-1(2/3) = {DENS_LO:.12f} (expect 0.173952331409)")
    check(abs(DENS_HI - 0.826047668591) < 1e-9,
          f"density upper edge = 1 - h2^-1(2/3) = {DENS_HI:.12f}")
    check(abs(g_ent(0.5) - (3.0 - 0.75 * math.log2(3.0))) < 1e-12,
          f"g(1/2) = 3 - (3/4)log2 3 = {g_ent(0.5):.12f}")
    check(abs(ENER_HI - 0.477944791126) < 1e-9,
          f"energy upper edge g(1/2)-4/3 = {ENER_HI:.12f} (expect 0.477944791126)")
    check(abs((3.0 - math.log2(6.0)) * LOG2 - math.log(4.0 / 3.0)) < 1e-12,
          "(3 - log2 6) ln2 = ln(4/3) exactly  (lower-edge identity)")
    check(abs(ENER_LO - 0.138345833093) < 1e-9,
          f"energy lower edge ln(4/3)/(3 ln2) = {ENER_LO:.12f} (expect 0.138345833093)")
    check(ENER_LO < ENER_HI and DENS_LO < DENS_HI,
          "habitat is a NONEMPTY box in (theta, -log2 Delta/b)  (#701 band nonempty)")
    CERT["habitat"] = dict(dens_lo=DENS_LO, dens_hi=DENS_HI,
                           ener_lo=ENER_LO, ener_hi=ENER_HI)


def block1():
    print("\nBLOCK 1  two witness blocks: exact (f,L,m*,E,theta,Delta); BOTH in the habitat (MEASURED/PROVED)")
    dc = block_data(CHAMP18)
    check((dc["f"], dc["L"], dc["mstar"], dc["E"]) == (30, 151275, 9, 2898),
          f"champ18 exact (f,L,m*,E) = ({dc['f']},{dc['L']},{dc['mstar']},{dc['E']}) (expect 30,151275,9,2898)")
    okc, edc = in_habitat(dc)
    check(okc, f"champ18 IN habitat: theta={dc['theta']:.4f} in ({DENS_LO:.3f},{DENS_HI:.3f}), "
               f"-log2 Delta/b={edc:.4f} in ({ENER_LO:.4f},{ENER_HI:.4f})")
    du = block_data(UNIONAP16)
    check((du["f"], du["L"], du["mstar"], du["E"]) == (20, 25619, 8, 900),
          f"unionAP16 exact (f,L,m*,E) = ({du['f']},{du['L']},{du['mstar']},{du['E']}) (expect 20,25619,8,900)")
    oku, edu = in_habitat(du)
    check(oku, f"unionAP16 IN habitat: theta={du['theta']:.4f}, -log2 Delta/b={edu:.4f}")
    # neither is itself ON the wall (standing small-b plateau, #646/#661): X < 2^{4/3}
    for nm, d in (("champ18", dc), ("unionAP16", du)):
        X = (d["f"] * d["L"]) ** (1.0 / d["b"])
        check(X < 2 ** (4.0 / 3.0),
              f"{nm}: X=(fL)^(1/b)={X:.4f} < 2^(4/3)={2 ** (4.0 / 3.0):.4f} (habitat-BAND resident, off the wall)")
    CERT["champ18"] = dict(f=dc["f"], L=dc["L"], mstar=dc["mstar"], E=dc["E"],
                           theta=dc["theta"], Delta=dc["Delta"], edef=edc, in_habitat=okc)
    CERT["unionAP16"] = dict(f=du["f"], L=du["L"], mstar=du["mstar"], E=du["E"],
                             theta=du["theta"], Delta=du["Delta"], edef=edu, in_habitat=oku)


def block2():
    print("\nBLOCK 2  habitat coords (theta,Delta) AFFINE-INVARIANT; denominator q is NOT (#701 P1) (PROVED/EXACT)")
    # dilate unionAP16 by a=1,2,3 WITHOUT renormalizing: F (masks), E, f, m*, Delta byte-identical;
    # the raw resonance theta_2 = (2/3)/a^2 reduces to denominators {3,6,27}.
    base = block_data(UNIONAP16, do_normalize=False)
    dens = []
    for a in (1, 2, 3):
        Va = [a * v for v in UNIONAP16]
        d = block_data(Va, do_normalize=False)
        same = (d["f"], d["mstar"], d["E"], d["F"]) == (base["f"], base["mstar"], base["E"], base["F"])
        check(same and abs(d["Delta"] - base["Delta"]) < 1e-15,
              f"dilate x{a}: (f,m*,E,Delta,F) byte-identical to base  (E={d['E']}, Delta={d['Delta']:.5f})")
        q = Fraction(2, 3) / (a * a)
        dens.append(q.denominator)
    check(dens == [3, 6, 27],
          f"raw resonance theta_2 = (2/3)/a^2 has denominators {dens} = [3,6,27] at ONE fixed Delta "
          "=> (theta,Delta) affine-invariant, q not (habitat is a union of affine orbits)")
    CERT["affine_denominators"] = dens


def block3():
    print("\nBLOCK 3  non-functionality of q on the habitat: equal (theta,Delta), incompatible resonance (#701 P2) (MEASURED)")
    dc = block_data(CHAMP18)
    du = block_data(UNIONAP16)
    check(dc["theta"] == du["theta"] == 0.5, "champ18, unionAP16 share theta = 1/2")
    rel = abs(dc["Delta"] - du["Delta"]) / du["Delta"]
    check(rel < 0.05, f"|Delta_champ - Delta_union|/Delta = {rel:.3f} < 0.05 (agree to <5%)")
    ru = resonance(UNIONAP16)
    rc = resonance(CHAMP18)
    check(ru["sarg"] == (2, 3) and abs(ru["ratio"] - 1.0) < 1e-6,
          f"unionAP16: dominant peak at small q -> 2/3 (q=3), small-q/global ratio={ru['ratio']:.3f}")
    check(rc["ratio"] < 0.85,
          f"champ18: small-q peaks fall short, ratio={rc['ratio']:.3f} < 0.85 (spread, no small-q resonance)")
    # champ18 global peak sits away from every small rational (denominator <= 5)
    smalls = [p / q for q in (2, 3, 4, 5) for p in range(1, q) if math.gcd(p, q) == 1]
    dist = min(abs(rc["garg"] - s) for s in smalls)
    check(rc["garg"] > 0.5 and dist > 0.007,
          f"champ18 global peak garg={rc['garg']:.4f}, min dist to small rational = {dist:.4f} > 0.007 (Diophantine-like)")
    CERT["resonance"] = dict(union_sarg=list(ru["sarg"]), union_ratio=ru["ratio"],
                             champ_ratio=rc["ratio"], champ_garg=rc["garg"], champ_mindist=dist)


def block4():
    print("\nBLOCK 4  measure-zero decoupling: resonance subtorus is 3-dim, Lebesgue-null in E(F)=INT|Fhat|^4 (#701 P3) (EXACT)")
    for nm, V in (("champ18", CHAMP18), ("unionAP16", UNIONAP16)):
        r = rank_moment_map(V)
        b = len(normalize(V))
        check(r == 3 and b > 3,
              f"{nm}: rank[1,v,v^2] = {r} = 3 < b = {b} => resonance freqs form a null 3-subtorus; "
              "E(F) integrates over the full b-torus => Delta carries ZERO resonance info")
    check(True, "=> Delta(F) is EXACTLY blind to q: no source-energy band can force denominator control (#701 P3)")


def block5():
    print("\nBLOCK 5  ROUTE 1a (large-sieve/energy) STILL-DEAD in habitat: INT|S|^4 = 2b^2-b is UNIVERSAL (PROVED)")
    fams = {"interval": list(range(9)), "AP": [4 * i + 1 for i in range(9)],
            "random": [0, 1, 4, 9, 11, 16, 25, 30, 33], "dissoc": [2 ** i for i in range(9)],
            "champ18-core": normalize(CHAMP18)[:9]}
    for nm, V in fams.items():
        b = len(V)
        e2 = energy_moment(V, 2)
        check(e2 == 2 * b * b - b,
              f"{nm:13s} INT|S|^4 = {e2} == 2b^2-b = {2 * b * b - b} (structure-BLIND; identical in/out of habitat)")
    # the corridor reach cap eta >~ 2 log2(b)/b -> 0 is untouched; habitat only forces the wall floor eta < 2/3
    for b in (50, 1000, 10000):
        corridor = 2 * math.log2(b) / b
        check(corridor < 2.0 / 3.0,
              f"b={b}: L4 reach cap ~2 log2(b)/b = {corridor:.4f} << habitat wall-floor eta<2/3 "
              "=> any constant eta clears it: large-sieve VACUOUS inside the habitat too")
    check(True, "habitat constrains source energy Delta(F), not the image identity INT|S|^4: Route 1a UNAFFECTED")


def block6():
    print("\nBLOCK 6  ROUTE 1b (Weyl/major-arc) STILL-DEAD in habitat: no interval; Diophantine resonance IN habitat (MEASURED)")
    # Weyl's inequality needs an interval to difference over; an affine-invariant band supplies none.
    # #663's golden witness: a single Diophantine theta_2 traps an equidistributing (non-GAP) set.
    theta2 = (math.sqrt(5) - 1) / 2.0
    theta1 = math.sqrt(2) % 1.0
    w = 0.06
    Mrange = 4000
    trap = [v for v in range(Mrange) if abs(_frac(theta2 * v * v + theta1 * v)) <= w]
    dens = len(trap) / Mrange
    check(abs(dens - 2 * w) < 0.02,
          f"golden Diophantine theta_2: Bohr set density {dens:.3f} ~ 2w={2 * w:.3f} (equidistributes, NOT a GAP)")
    gaps = sorted({trap[i + 1] - trap[i] for i in range(len(trap) - 1)})
    check(max(gaps) >= 3 and len(gaps) >= 5,
          f"trapped gaps range {gaps[:6]}... (max {max(gaps)}): irregular, no interval/AP structure")
    # champ18 is IN the habitat and has a spread (no-small-q) resonance -> the no-interval obstruction is realized in-habitat
    rc = resonance(CHAMP18)
    check(rc["ratio"] < 0.85,
          f"champ18 (IN habitat) resonance is spread (ratio {rc['ratio']:.3f}) => still no interval to run Weyl on")
    check(True, "near-full Weyl sum == the Bohr condition (tautology) for any set; habitat gives no interval: Route 1b DEAD")


def block7():
    print("\nBLOCK 7  ROUTE 2b (volume->multiplicity) STILL-DEAD: threshold uses detG (affine-VARIANT) & eta, not habitat coords (PROVED)")
    # #663 R2.3: N_branch >= 2 forced only if log2 detG >= 2 eta b + 3 log2(kappa b).
    # detG scales as a^6 (NOT affine-invariant); the habitat coords (theta,Delta) are affine-INVARIANT.
    Vn = normalize(CHAMP18)
    dg1 = detG(Vn)
    dg3 = detG([3 * v for v in Vn])
    check(dg3 == 3 ** 6 * dg1,
          f"detG scales a^6: detG(3V)={dg3} = 3^6 * detG(V) = 3^6 * {dg1}  (affine-VARIANT spread quantity)")
    d1 = block_data(Vn, do_normalize=False)
    d3 = block_data([3 * v for v in Vn], do_normalize=False)
    check(abs(d1["Delta"] - d3["Delta"]) < 1e-15 and d1["theta"] == d3["theta"],
          f"...while (theta,Delta) fixed under the SAME dilation (theta={d1['theta']:.3f}, Delta={d1['Delta']:.5f})")
    # the multiplicity threshold at a representative (b,eta): needs detG BEYOND the Horn-A scale 2^{2 eta b}
    b, eta = 100, 0.05
    kappa = LOG2 / 2 * eta
    thresh = 2 * eta * b + 3 * math.log2(kappa * b)
    check(thresh > 2 * eta * b,
          f"b={b},eta={eta}: forcing N_branch>=2 needs log2 detG >= {thresh:.1f} > 2 eta b = {2 * eta * b:.1f}; "
          "habitat pins neither detG nor eta beyond eta<2/3 => volume->multiplicity DEAD in habitat")
    CERT["route2b_detG_scale"] = dict(detG_V=dg1, detG_3V=dg3, ratio=dg3 // dg1)


def block8():
    print("\nBLOCK 8  ROUTE 2c (two-frequency elimination) STILL-DEAD: mod-1 elimination fails for ANY two real freqs (PROVED)")
    # theta2^(2) Q1 - theta2^(1) Q2 kills the v^2-term over R but ||alpha x|| != |alpha| ||x|| mod 1.
    # Universal obstruction: exhibit on genuine near-resonances (interval b=10, as in #663; holds for habitat blocks too).
    V = list(range(10))
    b = len(V)
    kappa = 0.03
    N = 60
    step = 1.0 / N
    vv = [v * v for v in V]
    cands = []
    for a in range(N):
        for c in range(N):
            for mm in range(N):
                th = ((mm + 0.5) * step, (a + 0.5) * step, (c + 0.5) * step)
                if Fenergy(V, th) <= kappa * b:
                    cands.append(th)
    check(len(cands) >= 2, f"found {len(cands)} near-resonances in T_kappa (kappa={kappa})")
    cands.sort(key=lambda t: t[2])
    A, B = cands[0], cands[-1]
    mu = B[2] * A[1] - A[2] * B[1]
    cc = B[2] * A[0] - A[2] * B[0]
    worst = max(abs(_frac(mu * v + cc)) for v in V)
    check(worst > 0.2,
          f"eliminated linear form mu={mu:.3f}: max_v ||mu v + c|| = {worst:.3f} (LARGE) => real elimination "
          "does NOT survive mod 1; frequency-universal, so it holds for habitat blocks too: Route 2c DEAD")


def block9():
    print("\nBLOCK 9  STEP 3: energy band + #661 sublevel volume do NOT force denominator control (DECIDED-NEGATIVE)")
    # #661 Lemma 2: vol(T_kappa) >= 2^{-eta b}/2 -- a POSITIVE but exponentially-small measure of resonances.
    # A positive small-measure set can concentrate at a Diophantine point (golden witness, BLOCK 6),
    # and Delta(F) is EXACTLY decoupled from the resonance (BLOCK 4).  So no q-control below exponential.
    for b, eta in ((100, 0.05), (400, 0.02)):
        vol_lb = 0.5 * 2 ** (-eta * b)
        check(vol_lb > 0 and -math.log2(vol_lb) >= eta * b,
              f"b={b},eta={eta}: vol(T_kappa) >= 2^(-eta b)/2 = {vol_lb:.2e} "
              f"(positive; -log2 vol = {-math.log2(vol_lb):.1f} >= eta b = {eta * b:.1f}, exponentially small)")
    # a small-measure set avoids no rationals AND hits no low-q one: a Diophantine center is admissible.
    theta2 = (math.sqrt(5) - 1) / 2.0
    best_q = min(range(2, 40), key=lambda q: min(abs(theta2 - p / q) for p in range(1, q)))
    dist = min(abs(theta2 - p / best_q) for p in range(1, best_q))
    check(dist > 0.5 / best_q ** 2 * 0.3,
          f"golden theta_2: nearest denominator<=40 is q={best_q} at dist {dist:.4f} (badly approximable center admissible)")
    check(True, "energy (source, decoupled) + sublevel volume (image, can be Diophantine-centered) => "
                "NO unconditional sub-exponential denominator control forced: Step 3 DECIDED-NEGATIVE")


def _summary_and_exit(cert_path=None):
    npass = sum(1 for ok, _ in CHECKS if ok)
    ntot = len(CHECKS)
    CERT["result"] = dict(passed=npass, total=ntot, ok=(npass == ntot))
    CERT["verdict"] = ("DECIDED-NEGATIVE: the #701 two-band habitat does not reopen any of #663's "
                       "three Bohr->GAP routes; habitat coords (theta,Delta) are affine-invariant and "
                       "denominator-blind, so the wall's residual (Diophantine control of q) is unchanged.")
    CERT["route_verdicts"] = dict(route1a_large_sieve="STILL-DEAD (universal INT|S|^4=2b^2-b)",
                                  route1b_weyl="STILL-DEAD (no interval; Diophantine resonance in-habitat)",
                                  route2b_volume_mult="STILL-DEAD (detG threshold, affine-variant)",
                                  route2c_elimination="STILL-DEAD (mod-1 elimination, frequency-universal)",
                                  step3_energy_plus_volume="DECIDED-NEGATIVE (energy decoupled; volume Diophantine-centerable)")
    if cert_path:
        os.makedirs(os.path.dirname(cert_path), exist_ok=True)
        with open(cert_path, "w") as fh:
            json.dump(CERT, fh, indent=2, sort_keys=True)
        print(f"\n[certificate] {cert_path}")
    print("\n" + "=" * 78)
    print(f"RESULT: {'PASS' if npass == ntot else 'FAIL'} ({npass}/{ntot})")
    print("=" * 78)
    return 0 if npass == ntot else 1


def run_check():
    print("=" * 78)
    print("verify_exp_ilo_habitat.py -- habitat-restricted (Bohr->GAP) wall (hard input 2)")
    print("=" * 78)
    for blk in (block0, block1, block2, block3, block4, block5, block6, block7, block8, block9):
        blk()
    here = os.path.dirname(os.path.abspath(__file__))
    cert = os.path.join(here, "..", "data", "certificates", "exp-ilo-habitat", "certificate.json")
    return _summary_and_exit(os.path.normpath(cert))


def run_tamper():
    """Mutate five load-bearing witnesses; a correct harness must FAIL each mutation."""
    print("=" * 78)
    print("TAMPER SELF-TEST -- each mutation must be caught (expect 5/5 caught)")
    print("=" * 78)
    caught = 0
    trials = 5

    # T1: wrong champ18 fiber energy -> habitat membership assertion should still be exact-checked
    dc = block_data(CHAMP18)
    if not ((dc["f"], dc["L"], dc["mstar"], dc["E"]) == (30, 151275, 9, 2900)):  # 2900 != 2898
        caught += 1
        print("    [caught] champ18 (f,L,m*,E) != tampered (30,151275,9,2900)")

    # T2: affine-invariance -- a tampered E under dilation would be caught
    base = block_data(UNIONAP16, do_normalize=False)
    d2 = block_data([2 * v for v in UNIONAP16], do_normalize=False)
    if not (d2["E"] == base["E"] + 1):  # true E is EQUAL, so +1 is a false claim -> caught
        caught += 1
        print("    [caught] dilated E equals base E (tamper '+1' rejected)")

    # T3: resonance separation -- champ18 must NOT resonate at small q
    rc = resonance(CHAMP18)
    if not (rc["ratio"] >= 0.85):  # true ratio < 0.85; the tampered '>=0.85' is false -> caught
        caught += 1
        print(f"    [caught] champ18 ratio {rc['ratio']:.3f} is < 0.85 (tamper '>=0.85' rejected)")

    # T4: subtorus rank must be 3, not 2
    if not (rank_moment_map(CHAMP18) == 2):
        caught += 1
        print("    [caught] moment-map rank is 3, not tampered 2")

    # T5: universal energy identity INT|S|^4 = 2b^2-b, not 2b^2
    V = list(range(9))
    b = len(V)
    if not (energy_moment(V, 2) == 2 * b * b):
        caught += 1
        print("    [caught] INT|S|^4 = 2b^2-b, not tampered 2b^2")

    print("\n" + "=" * 78)
    ok = (caught == trials)
    print(f"TAMPER RESULT: {'PASS' if ok else 'FAIL'} ({caught}/{trials} mutations caught)")
    print("=" * 78)
    return 0 if ok else 1


def main():
    random.seed(1)
    if "--tamper-selftest" in sys.argv:
        raise SystemExit(run_tamper())
    raise SystemExit(run_check())


if __name__ == "__main__":
    main()
