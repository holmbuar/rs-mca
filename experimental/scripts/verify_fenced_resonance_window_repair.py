#!/usr/bin/env python3
"""
Repair verifier for experimental/notes/thresholds/fenced_resonance_window_repair.md

Repairs Theorem T1 of the integrated fenced_resonance_window.md (#691), which is
REFUTED AS PRINTED and carries a dropped hypothesis (found by a Codex team
read-only audit, verified firsthand):

  (A) T1's "a width-w trap resolves q ONLY IF q <= Q_res = 1/(2w)" is FALSE.
      Witness (the note's OWN verifier BLOCK 2, never cross-asserted): q=7, w=0.10
      gives a SINGLE trapped residue class, though 1/(2w)=5 -- a resolution ABOVE
      the printed ceiling.  Confinement degrades gradually (# admissible target
      residues ~ 2 floor(wq)+1); it does NOT vanish at w=1/(2q).
  (B) T1 states only "theta_2 = a/q rational" but its proof uses
      {theta_2 r^2 + theta_1 r + theta_0} in (1/q)Z + theta_0, which needs BOTH
      theta_2 = a/q AND theta_1 = a'/q with COMMON q.  That is exactly #663
      Proposition 5's hypothesis (bohr_gap_volume.md R3).  #691 dropped the theta_1
      clause everywhere T1 is stated or used.

Corrected statements (re-derived here, PROVED):
  T1'  under the common-q hypothesis a width-w trap confines the trapped residues
       to N(q,w) <= (2 floor(wq)+1)*M(a,a';q) classes mod q, M = max quadratic-
       congruence multiplicity (= 2^omega(q) for odd squarefree q, #663 Prop 5);
       a single class SYSTEM is GUARANTEED when w < 1/(2q) (sufficient, NOT
       necessary); the horn (O(1) classes, #657 Thm 2/3) forces 2 floor(wq)+1=O(1),
       i.e. q=O(1/w)=O(sqrt b), POLYNOMIAL since w >= sqrt(ln2/(2b)).
  T2'  host-smallness threshold q_cross=2^{beta b} (common-q carried), SURVIVES.
  T3'  empty window [q_cross, Q_res]=[2^{beta b}, 0.84932 sqrt b] empty for b>b_0;
       b_0 table (411/53/19/2) and constant 0.84932=1/sqrt(2 ln2) UNCHANGED; the
       constant's ROLE is reinterpreted (sufficient threshold, not a ceiling).
       "Bohr face = box face" (beta=0 == #682 residual line) is a T2-side fact and
       SURVIVES UNTOUCHED.  R4/P4 (decoupling) SURVIVE UNTOUCHED.

Usage:
  verify_fenced_resonance_window_repair.py [--check]     # default; asserts, RESULT: PASS n/n
  verify_fenced_resonance_window_repair.py --tamper-selftest  # confirms harness catches tampers

stdlib only; deterministic (fixed seeds); ASSERTS every number in the repair note.

Credit (public repo artifacts, by PR number): the q=7 counterexample to the printed
T1 and the dropped common-denominator hypothesis were found by a Codex team
read-only audit.  Results consumed read-only: #691 (the note under repair), #663
Prop 5 (bohr_gap_volume.md, full common-q hypothesis), #661 (exp_ilo_fourier.md,
Theorem B width), #657 (ilo_moment_structured.md, Theorem 2/3 rank-1 GAP consumer).
Image face only (f, L, Phi); no signed mu_n object entered.
"""
import sys, math, random
from fractions import Fraction
from collections import Counter

LN2 = math.log(2.0)
CONST = 1.0 / math.sqrt(2 * LN2)          # 0.849322 = 1/sqrt(2 ln2)

PASS = 0
FAIL = 0
def check(cond, msg):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print("  FAIL:", msg)
    return bool(cond)

# ------------------------------------------------------------------ primitives
def frac(x):
    return abs(x - round(x))

def omega(q):
    n, c, d = q, 0, 2
    while d * d <= n:
        if n % d == 0:
            c += 1
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        c += 1
    return c

def squarefree(q):
    d = 2
    while d * d <= q:
        if q % (d * d) == 0:
            return False
        d += 1
    return True

def maxfiber(a, ap, q):
    """M(a,a';q) = max_t #{ r in Z/q : a r^2 + a' r ≡ t (mod q) }."""
    cnt = Counter((a * r * r + ap * r) % q for r in range(q))
    return max(cnt.values())

def trapped_residues(a, ap, q, w, th0=0.0):
    """# residues r in Z/q with ||(a r^2 + a' r)/q + th0|| <= w  (theta_2=a/q, theta_1=a'/q)."""
    return sum(1 for r in range(q) if frac((a * r * r + ap * r) / q + th0) <= w)

def n_targets(q, w, th0=0.0):
    """# admissible target residues s in Z/q with ||s/q + th0|| <= w  (= 2 floor(wq)+1 at th0=0)."""
    return sum(1 for s in range(q) if frac(s / q + th0) <= w)

def f_and_L(V):
    """Exact max fiber f and image size L of the degree-2 signature map (for P4)."""
    state = {(0, 0, 0): 1}
    for v in V:
        vv = v * v
        ns = dict(state)
        for (a, s, qq), c in state.items():
            k = (a + 1, s + v, qq + vv)
            ns[k] = ns.get(k, 0) + c
        state = ns
    return max(state.values()), len(state)

def width(eta, eps, b):                    # #661 Theorem B trap width
    return math.sqrt((LN2 / 2) * (eta + 1.0 / b) / eps)

def b0(beta, const=CONST):                 # smallest b with 2^{beta b} > const sqrt(b)
    b = 2
    while not (2 ** (beta * b) > const * math.sqrt(b)):
        b += 1
        if b > 10 ** 7:
            return None
    return b

# The GRID of (q,w) on which the corrected class-count bound is asserted.
GRID_Q = [3, 5, 7, 9, 11, 13, 16, 20, 25, 49, 81, 100, 121, 600]
GRID_W = [0.02, 0.05, 0.10, 0.20]

# ================================================================== the checks
def run_checks():
    print("=" * 74)
    print("BLOCK A -- REFUTATION: T1's 'resolves only if q<=1/(2w)' is FALSE (q=7 witness)")
    print("=" * 74)
    # The explicit negative control AGAINST the old form: q=7, w=0.10, theta_1=0
    # (=0/q, common q OK).  A SINGLE trapped class, though q=7 > 1/(2w)=5.
    w = 0.10
    C7 = trapped_residues(1, 0, 7, w)                  # theta_2=1/7, theta_1=0
    old_ceiling = 1.0 / (2 * w)                        # = 5, the printed Q_res
    check(C7 == 1, "q=7,w=0.10: single trapped residue class (C=1)")
    check(7 > old_ceiling, "q=7 lies ABOVE the printed ceiling 1/(2w)=5")
    # => the OLD predicate  [resolved (C small) => q <= 1/(2w)]  is refuted:
    old_form_holds = not (C7 <= 4 and 7 > old_ceiling)  # old form would forbid this row
    check(not old_form_holds,
          "OLD FORM REFUTED: a single-class resolution (C=1) occurs at q=7 > 1/(2w)=5")
    print(f"  q=7,w=0.10: trapped classes = {C7}, printed ceiling 1/(2w) = {old_ceiling:.0f}  "
          f"=> 'NEVER resolves q>{old_ceiling:.0f}' is FALSE")
    # the full transition row (theta_1=0), asserting the corrected count, not a ceiling
    for q in [7, 20, 100, 600]:
        C = trapped_residues(1, 0, q, w)
        tgt = 2 * math.floor(w * q) + 1                 # 2 floor(wq)+1 admissible targets
        M = maxfiber(1, 0, q)
        check(C <= tgt * M, f"transition q={q}: C={C} <= (2floor(wq)+1)*M = {tgt*M}")
        print(f"    q={q:3d}: C={C:3d}  targets(2floor(wq)+1)={tgt:3d}  M={M:2d}  bound={tgt*M:4d}")
    # confinement grows continuously ~2wq (does NOT vanish at w=1/(2q))
    grow = [trapped_residues(1, 0, 200, ww) for ww in [0.01, 0.02, 0.04, 0.08]]
    check(all(grow[i] < grow[i + 1] for i in range(len(grow) - 1)),
          "confinement degrades GRADUALLY: trapped count strictly increases with w")

    print("=" * 74)
    print("BLOCK B -- CORRECTED class-count bound N(q,w) <= (2floor(wq)+1)*M on the grid")
    print("=" * 74)
    rows = 0
    for q in GRID_Q:
        for w in GRID_W:
            C = trapped_residues(1, 0, q, w)
            tgt = 2 * math.floor(w * q) + 1
            M = maxfiber(1, 0, q)
            check(C <= tgt * M, f"grid q={q} w={w}: N={C} <= (2floor(wq)+1)*M={tgt*M}")
            rows += 1
    print(f"  asserted N(q,w) <= (2floor(wq)+1)*M(a,a';q) on all {rows} grid rows (incl. q=7,w=0.10)")
    # M = 2^omega(q) on the ODD SQUAREFREE sub-grid (the #663 Prop 5 regime)
    for q in [3, 5, 7, 11, 13, 15, 35, 105, 1001]:
        check(maxfiber(1, 1, q) <= 2 ** omega(q),
              f"odd sqfree q={q}: quadratic-congruence multiplicity <= 2^omega(q)")
    # the NAIVE (2wq+1)*2^omega form is NOT universal: it FAILS at q=81, a'=0, small w
    wsmall = 1.0 / 200                                   # only target t=0 admissible
    C81 = trapped_residues(1, 0, 81, wsmall)
    naive = (2 * math.floor(wsmall * 81) + 1) * (2 ** omega(81))
    check(C81 > naive,
          "naive (2floor(wq)+1)*2^omega FAILS at q=81,a'=0 (degenerate t=0 fiber) -> M needed")
    check(C81 <= (2 * math.floor(wsmall * 81) + 1) * maxfiber(1, 0, 81),
          "corrected bound with M holds at q=81")
    print(f"  q=81,a'=0,w={wsmall:.4f}: N={C81}, naive 2^omega bound={naive} (FAILS), "
          f"M={maxfiber(1,0,81)} (bound holds) -> T1' carries M explicitly")

    print("=" * 74)
    print("BLOCK C -- DROPPED HYPOTHESIS: T1 needs theta_1 = a'/q too (common q)")
    print("=" * 74)
    g = (math.sqrt(5) - 1) / 2                            # golden: NOT of the form a'/q
    q = 7
    res0 = sorted(set(r % q for r in range(0, q * 60) if frac((r * r) / q + 0.0 * r) <= 0.06))
    res3 = sorted(set(r % q for r in range(0, q * 60) if frac((r * r) / q + (3 / q) * r) <= 0.06))
    resG = sorted(set(r % q for r in range(0, q * 60) if frac((r * r) / q + g * r) <= 0.06))
    check(len(res0) <= 2, "theta_1=0/7 (common q): trapped in <=2 classes mod 7")
    check(len(res3) <= 2, "theta_1=3/7 (common q): trapped in <=2 classes mod 7")
    check(len(resG) == q, "theta_1=golden (NOT a'/q): ALL 7 residues admissible -- NO structure")
    print(f"  theta_2=1/7: theta_1=0/7 -> {res0}; theta_1=3/7 -> {res3}; theta_1=golden -> {resG}")
    print("  => without the common-q clause the resolution mechanism collapses (dropped hyp is load-bearing)")

    print("=" * 74)
    print("BLOCK D -- SURVIVING sufficient regime w<1/(2q) & the constant 0.84932")
    print("=" * 74)
    check(abs(CONST - 0.849322) < 1e-5, "constant 1/sqrt(2 ln2) = 0.84932")
    # w < 1/(2q) => single target UNIFORMLY in theta_0 (the honest sufficient guarantee)
    for q in [3, 5, 7, 20, 97]:
        wc = 1.0 / (2 * q)
        worst = max(n_targets(q, wc * 0.99, th0) for th0 in [0.0, 0.5 / q, 0.25 / q, 0.5])
        check(worst == 1, f"q={q}: w<1/(2q) => single target for ALL theta_0 (sufficient)")
    # the q=7 witness: single class at w=0.10 > 1/(2*7)=0.0714 (favorable theta_0=0) -> accidental
    check(1.0 / (2 * 7) < 0.10 < 1.0 / 7,
          "q=7,w=0.10 is in the accidental strip 1/(2q) < w < 1/q (single only for favorable theta_0)")
    # width & the guaranteed-single-class ceiling 0.84932 sqrt(b)
    for b in [50, 100, 200, 500, 1000]:
        wmin = width(1e-12, 1.0, b)                      # eps=1, eta->0
        Qres = 1.0 / (2 * wmin)
        check(abs(Qres - CONST * math.sqrt(b)) < 1e-6 * (CONST * math.sqrt(b)) + 1e-9,
              f"guaranteed-single-class ceiling = 0.84932 sqrt(b) at b={b}")
        check(width(0.05, 0.5, b) >= wmin, f"eps<1 or eta>0 only widens w (shrinks ceiling) at b={b}")
    print(f"  1/sqrt(2 ln2) = {CONST:.6f}; ceiling 0.84932 sqrt(b): "
          f"b=100 -> {CONST*10:.3f}, b=1000 -> {CONST*math.sqrt(1000):.3f} (POLYNOMIAL)")

    print("=" * 74)
    print("BLOCK E -- T2' host-smallness threshold (common-q carried) SURVIVES")
    print("=" * 74)
    # dividing out a common difference q cuts delta by exactly log2(q)/b; (f,L) fixed
    Vint = list(range(16))
    f0, L0 = f_and_L(Vint)
    d0 = math.log2(max(Vint)) / 16
    for q in [8, 256, 65536]:
        Vq = [q * v for v in Vint]
        fq, Lq = f_and_L(Vq)
        dq = math.log2(max(Vq)) / 16
        check((fq, Lq) == (f0, L0), f"dilation by q={q}: (f,L) fixed")
        check(abs(dq - (d0 + math.log2(q) / 16)) < 1e-9, f"dilation by q={q}: delta += log2(q)/b")
    # fenced: 3 delta > alpha+1/3 => trivial box bound useless, horn must cut delta
    alpha_0 = 0.084497
    for al, dfen in [(alpha_0, alpha_0 / 3 + 1 / 9 + 0.01),
                     (0.4, 0.4 / 3 + 1 / 9 + 0.02),
                     (2 / 3, 2 / 3 / 3 + 1 / 9 + 0.01)]:
        beta = dfen - al / 3 - 1 / 9
        check(beta > 0, f"fenced beta>0 at alpha={al:.3f}")
        check(3 * dfen > al + 1 / 3, f"3 delta > alpha+1/3 (box useless) at alpha={al:.3f}")
    print("  dividing out q cuts delta by log2(q)/b (host stays diameter-scaled); "
          "3 delta > alpha+1/3 on the fence (box bound useless)")

    print("=" * 74)
    print("BLOCK F -- T3' EMPTY WINDOW (corrected ceiling): b_0 table & Bohr=box face")
    print("=" * 74)
    # the b_0(beta) table -- UNCHANGED from #691 (constant 0.84932 survives)
    expected = {0.0100: 411, 0.0500: 53, 0.1000: 19, 0.1928: 2, 0.2222: 2, 0.3000: 2}
    for beta, exp in expected.items():
        bb0 = b0(beta)
        check(bb0 == exp, f"b_0({beta}) = {exp}")
        check(bb0 is not None and 2 ** (beta * bb0) > CONST * math.sqrt(bb0),
              f"window empty for b>=b_0 at beta={beta}")
        check(2 ** (beta * (4 * bb0)) > CONST * math.sqrt(4 * bb0),
              f"gap q_cross/Q_res widens at 4 b_0, beta={beta}")
        print(f"  beta={beta:.4f}: b_0={bb0}  (2^(beta*b0)={2**(beta*bb0):.2f} > 0.849 sqrt(b0)={CONST*math.sqrt(bb0):.2f})")
    # the horn cannot exploit exponential q: at q >> 1/w the class count ~ 2wq (no O(1) resolution)
    w = 0.05
    for q in [2000, 8000, 32000]:
        C = trapped_residues(1, 3, q, w)                 # generic a'=3
        check(C >= 0.5 * (2 * w * q),
              f"large q={q}: trapped count ~2wq={2*w*q:.0f} (exponential-regime, no O(1) resolution)")
    print(f"  large-q (w={w}): trapped count tracks 2wq -> no accidental O(1)-class resolution at exp q")
    # Bohr face = box face: beta=0 <=> delta = (alpha+1/3)/3 (#682 residual line) -- T2-side, untouched
    for al in [alpha_0, 0.4, 2 / 3]:
        check(abs((al / 3 + 1 / 9) - (al + 1 / 3) / 3) < 1e-12,
              f"Bohr=box face: crossover delta(beta=0) == residual line at alpha={al:.3f}")
    # NEGATIVE control: emptiness HINGES on Q_res polynomial; an exp ceiling 2^{b/4} would open it
    check(2 ** (0.25 * 100) > 2 ** (0.10 * 100), "NEGATIVE: fake exp ceiling 2^{b/4} would open window at beta=0.10")
    check(not (2 ** (0.25 * 100) > 2 ** (0.30 * 100)), "control: even fake exp ceiling shut at beta=0.30")
    print("  Bohr=box face (beta=0 == #682 residual line) SURVIVES untouched (T2-side identity)")

    print("=" * 74)
    print("BLOCK G -- R4/P4 decoupling SURVIVES: generic Bohr subset is Sidon (f=1)")
    print("=" * 74)
    trapR = [v for v in range(6001) if frac(1 * v * v / 97 + 0.11 * v) <= 0.10]   # rational q=97
    gg = (math.sqrt(5) - 1) / 2
    trapG = [v for v in range(4001) if frac(gg * v * v + 0.30 * v) <= 0.06]        # #663 golden
    for name, trap in [("rational-q97", trapR), ("golden", trapG)]:
        sc = 0
        for seed in range(8):
            random.seed(1000 + seed)
            V = sorted(random.sample(trap, 14))
            if f_and_L(V)[0] == 1:
                sc += 1
        check(sc == 8, f"{name}: all sampled b=14 Bohr subsets are Sidon (f=1) -- P4 survives")
    check(f_and_L(list(range(14)))[0] > 1, "NEGATIVE: interval (additive) has f>1 (fiber is additive)")
    print(f"  rational-q97 |B|={len(trapR)}, golden |B|={len(trapG)}: generic subsets Sidon (metric != additive)")

# ================================================================== tamper self-test
def tamper_selftest():
    """Confirm the harness would CATCH (a) a reinstated false ceiling and (b) a corrupted number."""
    caught = 0
    total = 0
    # tamper 1: reinstate the false 'resolution => q <= 1/(2w)'. It must be violated by q=7.
    total += 1
    w = 0.10
    C7 = trapped_residues(1, 0, 7, w)
    old_form_true = (C7 <= 4) <= (7 <= 1.0 / (2 * w))   # 'resolved => q<=1/(2w)'
    if not old_form_true:                               # predicate is FALSE -> tamper caught
        caught += 1
        print("  tamper 1 CAUGHT: reinstated false ceiling 'resolved => q<=1/(2w)' is violated by q=7 (C=1)")
    else:
        print("  tamper 1 SLIPPED: false ceiling not caught")
    # tamper 2: corrupt the b_0 table (claim b_0(0.10)=18 instead of 19).
    total += 1
    if b0(0.10) != 18:                                  # corruption differs from truth -> caught
        caught += 1
        print(f"  tamper 2 CAUGHT: corrupted b_0(0.10)=18 != true {b0(0.10)}")
    else:
        print("  tamper 2 SLIPPED: b_0 corruption not caught")
    # tamper 3: corrupt the class-count bound (drop the target-count factor) -> must fail on a grid row.
    total += 1
    q, ww = 100, 0.10
    C = trapped_residues(1, 0, q, ww)
    bad_bound = maxfiber(1, 0, q)                        # M alone, WITHOUT (2floor(wq)+1)
    if C > bad_bound:                                    # dropped factor -> bound violated -> caught
        caught += 1
        print(f"  tamper 3 CAUGHT: class-count bound without the (2floor(wq)+1) factor fails "
              f"(N={C} > M={bad_bound} at q={q})")
    else:
        print("  tamper 3 SLIPPED: dropped-factor bound not caught")
    print("=" * 74)
    if caught == total:
        print(f"TAMPER-SELFTEST: PASS ({caught}/{total} tampers caught)")
        return 0
    print(f"TAMPER-SELFTEST: FAIL ({caught}/{total} tampers caught)")
    return 1

# ================================================================== main
def main():
    args = sys.argv[1:]
    if "--tamper-selftest" in args:
        sys.exit(tamper_selftest())
    # default and --check both run the assertion suite
    run_checks()
    print("=" * 74)
    if FAIL == 0:
        print(f"RESULT: PASS {PASS}/{PASS}")
        sys.exit(0)
    else:
        print(f"RESULT: FAIL {PASS}/{PASS + FAIL} ({FAIL} failing)")
        sys.exit(1)

if __name__ == "__main__":
    main()
