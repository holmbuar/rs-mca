# The dense-shell sign dichotomy: Chebyshev-cubing orbits, an alternating-cone proof, and the certified transfer tail

## Status

```text
Status: PROVED (D1, the orbit form): on dense words the scan states are
        exact rationals u_k = n_k/3^k with 3 u_{k+1} - u_k = d_k in
        {+-1}; the cosine states c_k = cos(2 pi u_k) satisfy the
        Chebyshev-cubing relation c_k = T3(c_{k+1}) backward from the
        forced anchor c_1 = -1/2, and the squared-sine states
        a_k = sin^2(pi u_k) form a backward orbit of
        S(a) = a(3 - 4a)^2 from a_1 = 3/4, confined to (1/4, 1).
        With mu = arcsine on [0,1],
            hatf(xi) = 4^B * E_mu[ prod_{k<=B} (x - a_k) ],
        and the full S-preimage product is the cubic identity
        prod_{S(z)=A}(x - z) = (S(x) - A)/16.
      + PROVED (D2, the coupling): dense scans keep |u_k| > 1/6; inner
        states (|u_k| < 1/4, i.e. roots a_k < 1/2) are ISOLATED, never
        first, and force the EXACT predecessor identity
        |u_{k-1}| = 1/4 + 3 delta (opposite signs), where
        delta = 1/4 - |u_k| lies in (0, 1/12) STRICTLY (integer form:
        |n_{k-1}| = 3^{k-1} - |n_k|; 6|n| = 3^k is impossible).
      + THEOREM (D3+D4, the dichotomy): for EVERY B >= 1 and every xi
        in the dense shell {s3 = B},
            sign(hatf(xi)) = (-1)^B  (strictly nonzero).
        Proof: the shifted-Chebyshev coefficients of the partial
        products keep the alternating cone sign(coeff_j) = (-1)^{k-j};
        outer roots preserve it entrywise, and each isolated inner
        root, COMPOSED with its coupled predecessor, gives a flipped
        2-step matrix with off-diagonals
        (sin 6 pi delta - sin 2 pi delta)/2 >= 0 and diagonals
        >= 1/8 - (1/4) sin 2 pi delta sin 6 pi delta > 0 (strict
        because delta < 1/12 strictly).  Full proof in section 3;
        mechanism verified at every prefix of every dense word,
        B <= 12; the dichotomy exhaustively at B <= 13 (middle-
        coefficient route), with the second route (4^B * cone-walk a_0)
        cross-checked to agree at B <= 10.
      + COMPUTED (D5, extremal structure): min |hatf|/C(2B,B) table to
        9 decimals (B <= 13); min |hatf| grows along each parity chain
        (>= 1.49 for all B <= 13); the even-B argmin has exactly ONE
        adjacent-equal defect (B >= 4) while the odd-B argmin IS the
        alternating word; the alternating orbit is EXACT (PROVED):
        u_m = (-1)^{m-1}(3^m + (-1)^{m-1})/(4 * 3^m), so
        c_m = (-1)^m sin(pi/(2*3^m)) -> the T3 fixed point c = 0
        (u = +-1/4) at rate 3^{-m}; alt/C(B, floor(B/2)) rises to
        0.919865 (even, B = 12) and falls to 0.393593 (odd, B = 13).
        The Theta(C(B, B/2)) sharp-min law is CONJECTURAL (the proved
        content is the sign and the computed table).
      + PROVED (D6, the certified tail; closes #842's named C3 open
        step): the adjoint Chebyshev DP's iterates are entire; branch
        maps send the rho-ellipse of [-1/2,1/2] into the disk
        D_{(1+R)/3} inside it (R = 1.3, rho = 2R + sqrt(4R^2-1) = 5),
        so level suprema obey M_L <= lam^L with
        lam = 4 cosh(2 pi (rho - 1/rho)/12) = 24.85, and the
        K-truncation error is at most 4 lam^B rho^{-K}/(rho - 1):
        a poly(B, log(1/eps)) CERTIFIED evaluation.  Instantiated:
        certified 4.0e-9 at B = 6, K = 24 (observed 3.2e-13).
LANE: hard input 2 -- twelfth packet of the arc; the first of the
        three product-profile emission steps banked in #842 (positivity
        pin proof + rigor bound; the emission arithmetic on top
        remains).  Upgrades #842 C5 from COMPUTED pin to THEOREM (and
        sharpens it: one-signedness at every B with sign (-1)^B, not
        only positivity at even B); the mandatory instance family for
        the omega-capped greedy machinery (#818/#820/#824) is now
        provably sign-pure, so omega = h_+ degenerates to |h| (even B)
        or 0 (odd B) on dense shells -- the #820 sign-mixing pathology
        CANNOT occur there.  Fence (N1) respected: nothing here pays
        or claims lower reserve.
```

Label key (agents.md dialect): **PROVED** / **CONDITIONAL** / **CONJECTURAL** /
**EXPERIMENTAL** / **AUDIT** / **COUNTEREXAMPLE**; COMPUTED marks exact
deterministic scans (sibling usage).  Verifier:
`experimental/scripts/verify_dense_shell_sign_dichotomy.py` (stdlib only,
deterministic, `RESULT: PASS (23/23)`, `--tamper-selftest` catches `7/7`).
Lean skeleton: `experimental/lean/dense_shell_sign_dichotomy/` (stdlib-only,
builds; the integer coupling theorem, the parity impossibility, the
alternating closed form, and the S-cubic ring identity).

## 1. Setting and the object

Fix the base-3 chart at level `B` (c = 3^B).  For `xi` in the dense shell
(all `B` balanced digits of `xi` nonzero; `2^B` residues) the #842/#827
weight

```text
hatf(xi) = [z^B] prod_{i<B} (1 + 2 cos(2 pi xi 3^i / 3^B) z + z^2)
```

is the middle coefficient of the palindromic root-on-circle polynomial
attached to the shell (equivalently `sum_{s == B (2)} C(B-s, (B-s)/2)
W_s(xi)`, the parity-weighted shell sums; equivalently `C(2B,B)` times the
band occupancy weight).  #842 pinned `hatf > 0` on the dense shell at
B in {6, 8} (C5) and left both the proof and the C3 rigor bound open.
This note proves the sign law at every B and closes the rigor bound.

Angles here are the IFS scan states of #842 C1: `u_k = ((xi/3^k))` in
balanced fractional parts, `u_k = (d_{k-1} + u_{k-1})/3` (digits
0-indexed, states 1-indexed: step k consumes digit `d_{k-1}`).  The
defining product's angle `xi 3^i/3^B = xi/3^{B-i}` is the scan state
`u_{B-i}`, so the i-indexed product is a REORDERING of the k = 1..B
scan-state product -- order-independent for the coefficient
extraction.

## 2. The orbit form (D1) and the coupling (D2)

**D1.** From `3 u_{k+1} - u_k = d_k in {+-1}` (exact, denominators 3^k)
and `cos 3t = T3(cos t)`:

```text
c_k = T3(c_{k+1}),   k = 1..B-1,   c_1 = cos(2 pi/3) = -1/2 forced,
```

so the angle multiset of a dense word is a backward orbit of the
Chebyshev cube T3(x) = 4x^3 - 3x.  Substituting `x = cos^2 psi` in the
circle-mean form of the middle coefficient,

```text
hatf(xi) = 4^B * (1/pi) int_0^1 prod_{k<=B} (x - a_k) dx/sqrt(x(1-x)),
a_k = sin^2(pi u_k),  a_k = S(a_{k+1}),  S(a) = a(3-4a)^2,  a_1 = 3/4,
```

i.e. an arcsine-measure mean of a real-rooted polynomial whose root
multiset is a backward S-orbit (S is T3 conjugated to [0,1]; the arcsine
law is its invariant measure; a = 1/2 is the fixed point corresponding to
u = +-1/4, c = 0).  Dense words are exactly those whose orbit stays in
(1/4, 1): a zero digit forces `|u_{k+1}| = |u_k|/3 <= 1/6` while nonzero
digits force `|u_{k+1}| >= 1/6`, with both boundary values unattainable
(denominator parity).  The three S-preimages of A satisfy the monic cubic
`(S(x) - A)/16`, giving `(e1, e2, e3) = (3/2, 9/16, A/16)` -- recorded for
the sequel (sparse/mixed shells exclude one branch).

**D2.** Call state k INNER if `|u_k| < 1/4` (root `a_k < 1/2`), OUTER
otherwise.  On dense words:

- `u_1 = +-1/3` is outer; inner states never occur first.
- An inner state at k forces `|d_{k-1} + u_{k-1}| = 3(1/4 - delta) < 3/4`
  with `delta = 1/4 - |u_k|`, which is only possible with
  `sign(u_{k-1}) = -d_{k-1}` and then EXACTLY

```text
  |u_{k-1}| = 1/4 + 3 delta,      0 < delta < 1/12  (both strict),
```

  integer form `|n_{k-1}| = 3^{k-1} - |n_k|`; strictness because
  `6|n| = 3^k` forces `2 | 3^k`.  Micro-example: word `(d_0, d_1) =
  (+1, -1)`: `u_1 = 1/3` (outer), `u_2 = (-1 + 1/3)/3 = -2/9` (inner,
  `delta = 1/36`), and indeed `|u_1| = 1/3 = 1/4 + 3/36` with
  `sign(u_1) = +1 = -d_1`.  In particular the predecessor is outer,
  and the successor of an inner state is outer
  (`|u_{k+1}| >= (1 - 1/4)/3 = 1/4`, strict): inner states are ISOLATED.

## 3. The dichotomy theorem (D3 + D4)

**Theorem.** For every `B >= 1` and every dense `xi`:
`sign(hatf(xi)) = (-1)^B`, strictly.

*Proof.*  Work on [0,1] in shifted Chebyshev basis `Tt_j(x) = T_j(2x-1)`
(so the arcsine mean is the `Tt_0` coefficient and
`hatf = 4^B * coeff_0(g_B)` for `g_k = prod_{m<=k}(x - a_m)`).
Multiplication acts tridiagonally:

```text
 (x - a) Tt_j = Tt_{j+1}/4 + (1/2 - a) Tt_j + Tt_{j-1}/4    (j >= 1)
 (x - a) Tt_0 = Tt_1/2     + (1/2 - a) Tt_0.
```

Say `g_k` is in the ALTERNATING CONE if `sign(coeff_j) = (-1)^{k-j}` for
all j (zeros allowed).  Write `coeff_j = (-1)^{k-j} b_j`, `b_j >= 0`; a
step with root a sends

```text
 (-1)^{k+1-j} coeff'_j = w_{j-1} b_{j-1} + b_{j+1}/4 + (a - 1/2) b_j,
```

with `w_0 = 1/2`, `w_j = 1/4` (j >= 1), `b_{-1} = 0`.

(i) *Outer step* (`a > 1/2`, strict since `|u| = 1/4` is unattainable):
all three coefficients are nonnegative -- the cone is preserved, and
`b'_0 >= (a - 1/2) b_0 > 0`, `b'_1 >= b_0/2 > 0` keep `b_0, b_1`
strictly positive.

(ii) *Coupled pair* (inner root at step k, its predecessor at k-1).
For an inner root the diagonal `a - 1/2` is strictly NEGATIVE, so a
lone inner step cannot preserve the cone entrywise -- this is exactly
why the pairing is needed.  By D2 the two drifts are EXACTLY

```text
 a_{k-1} - 1/2 = + (1/2) sin(6 pi delta),
 a_k     - 1/2 = - (1/2) sin(2 pi delta),         0 < delta < 1/12.
```

In flipped coordinates each single step is the matrix `N_a` with
off-diagonal entries `w` (nonnegative) and diagonal `a - 1/2`; the pair
acts as `C = N_inner N_pred`, whose entries are

```text
 C[j+-2, j] = w w'                                        >= 0,
 C[j+-1, j] = w ((a_pred - 1/2) + (a_inner - 1/2))
            = w (sin 6 pi delta - sin 2 pi delta)/2       >= 0,
 C[j, j]    = (a_pred - 1/2)(a_inner - 1/2) + (up-down paths)
            >= 1/8 - (1/4) sin 2 pi delta sin 6 pi delta  > 0,
```

(entries of the SEMI-INFINITE coefficient operator -- every index has
an up-neighbor; a hard finite truncation severs the top row's up-down
path and shows a spurious negative diagonal there, which never touches
the active support since deg g_{k-2} = k-2 sits strictly below the
working degree), using `0 < 2 pi delta < 6 pi delta <= pi/2` (sin is
increasing there) for the off-diagonals, and for the diagonals that the two path terms
contribute at least `1/16 + 1/16` (j >= 2), `1/16 + 1/8` (j = 1),
`1/8` (j = 0) while the drift product is at most `(1/4) sin(pi/6) sin(pi/2)
= 1/8`, with equality only at the excluded `delta = 1/12`.  So C is
entrywise nonnegative with strictly positive diagonal: the cone is
preserved across the pair, and `b_0, b_1` stay strictly positive.

(iii) *Induction.*  `g_0 = 1` is in the (k = 0) cone.  Scan the word left
to right: an outer step extends the cone by (i); an inner step at k
extends it by applying (ii) to the cone vector at k-2 (inner states are
isolated and never first, so step k-1 is outer and the pairs are
disjoint; the intermediate prefix k-1 is covered by (i)).  After B steps
`coeff_0(g_B) = (-1)^B b_0` with `b_0 > 0`.  Multiply by 4^B.  QED.

Two remarks.  (1) The coupling is LOAD-BEARING, not decorative: replacing
each inner root by the decoupled worst case `a = 1/4^+` already breaks
the cone at B = 4 (the verifier carries this as a permanent tamper).
(2) Pairing the inner root with its SUCCESSOR instead fails -- the
successor's drift `(1/2) sin(2 pi delta / 3 +-)` is too weak and the
off-diagonal goes negative (also tamper-pinned).  The backward 3x
amplification `|u_{k-1}| - 1/4 = 3 (1/4 - |u_k|)` is exactly what the
cone needs.

## 4. Extremal structure (D5, computed; alternating orbit proved)

```text
 B   min|hatf|/C(2B,B)   min|hatf|   argmin defects   alt/C(B,fl(B/2))
 2   0.275450607           1.653          0              0.826352
 3   0.074879982           1.498          0 (= alt)      0.499200
 4   0.069334809           4.853          1              0.899855
 5   0.017425961           4.391          0 (= alt)      0.439134
 6   0.017726367          16.379          1              0.911639
 7   0.004256358          14.608          0 (= alt)      0.417366
 8   0.004491629          57.807          1              0.916033
 9   0.001051826          51.140          0 (= alt)      0.405871
10   0.001131476         209.047          1              0.918382
11   0.000261061         184.161          0 (= alt)      0.398616
12   0.000284287         768.755          1              0.919865
13   0.000064939         675.406          0 (= alt)      0.393593
```

- The min/C(2B,B) ratio tracks `2^{-B}`: the minimizers hug the T3 fixed
  point.  PROVED for the alternating word `d_j = (-1)^j` (d_0 = +1; the
  global sign flip gives the mirror orbit): its orbit is exactly
  `u_m = (-1)^{m-1}(3^m + (-1)^{m-1})/(4 3^m)`, so
  `c_m = (-1)^m sin(pi/(2 3^m))` -> 0 geometrically and
  `prod (t + c_m) -> t^B`; its arcsine mean is `2^{-B} C(B, B/2)`-scale.
  The sharp constant (`min = ~0.83 C(B, B/2)` even, `~0.39 C(B,(B-1)/2)`
  odd, both slowly drifting) is left CONJECTURAL/COMPUTED.
- Odd-B minima sit AT the alternating word; even-B minima at its
  one-defect neighbors.  This and #824's deepest-instance word
  (r = 1367, the alternating (-1,0)-word at k = 7) are the same
  phenomenon: extremals live on the quantified approach to u = +-1/4.
- min|hatf| itself GROWS along each parity chain -- one-signedness comes
  with a comfortable computed floor (>= 1.49 up to B = 13), even though
  no proved uniform constant is claimed here.

## 5. The certified transfer tail (D6; closes #842 C3's open step)

**Lemma.**  Let the adjoint DP act on functions of `u in [-1/2, 1/2]` by
`(T g)(u) = sum_{d in {-1,1}} lambda_d 2 cos(2 pi (d+u)/3) g((d+u)/3)`
with `|lambda_d| <= 1`, `g_0 = 1`.  Fix R = 1.3 and
`rho = 2R + sqrt(4R^2 - 1) = 5.0`, so the Bernstein ellipse `E_rho` of
[-1/2, 1/2] has semi-axes (R, (rho - 1/rho)/4 = 1.2).  Then:

1. every iterate `g_L` is entire, and
   `sup_{E_rho} |g_L| <= lam^L` with
   `lam = 2 * 2 cosh(2 pi (rho - 1/rho)/12) = 24.85`
   (the branch maps send `E_rho` into the disk of radius
   `(1 + R)/3 = 0.767 <= 1.2`, inside `E_rho`, and
   `|2 cos(2 pi w)| <= 2 cosh(2 pi |Im w|)` with
   `|Im w| <= (rho - 1/rho)/12` there);
2. hence the Chebyshev coefficients of `g_L` on [-1/2, 1/2] satisfy
   `|a_j| <= 2 lam^L rho^{-j}`, and the degree-K truncation (equivalently
   the K-node interpolant) carries total error at most

```text
   eps(B, K) <= 4 lam^B rho^{-K} / (rho - 1)
```

   (the 4 = 2 from the Bernstein coefficient bound `|a_j| <= 2 M rho^{-j}`
   times 2 from interpolation aliasing on top of truncation).

So certified accuracy eps needs only
`K >= (B log lam + log(4/((rho-1) eps))) / log rho` -- poly(B, log(1/eps)),
which is the rigor statement #842's C3 left open.  The constant is
branch-count-specific: `lam = (#branches) * 2 cosh(2 pi (rho - 1/rho)/12)`
-- two branches (d in {-1,+1}) on the dense shell as instantiated here;
general symmetric product profiles use three branches (d = 0 included)
and rescale by `max_j |lambda_j|`, changing lam's prefactor but not the
poly(B, log(1/eps)) shape.  Instantiated by the
verifier (dense-shell instance, brute cross-check): certified 2.5e-6 /
6.4e-12 (B = 4, K = 16/24) and 1.5e-3 / 4.0e-9 (B = 6, K = 16/24),
observed errors <= 4e-13 throughout.  The bound is deliberately
a-priori and conservative (the observed rho_eff is ~17); conditioning of
individual small factors (the 1/4-approach of section 4) affects RELATIVE
error of tiny class data, not this additive certificate -- state class
data with the additive bar.

## 6. Nonclaims

- No claim about hatf off the dense shell: full-group nonnegativity is
  FALSE even at even B (first negatives at B = 4 live at s3 = 3), so no
  convolution-square/positive-definiteness structure exists on the whole
  group.
- No proved sharp-min law (the Theta(C(B, B/2)) constant and its parity
  limits are computed/conjectural), and no proved uniform positive
  constant floor -- the theorem is the sign, strictness, and the
  computed table.
- No emission arithmetic yet: this packet supplies sign purity and
  certified evaluation; the product-profile emission packet (budgets,
  schedule, adequacy on product profiles) is the remaining named step.
- Nothing here touches lower reserve or the (N1) fence.

## 7. Consumers and provenance

- **#842** (transfer certificate): C5 pin -> THEOREM (sharpened to the
  parity dichotomy); C3 rigor bound -> PROVED (section 5).  The two open
  steps named there are now closed; only the emission arithmetic
  remains of the three.
- **#827** (shell-mass law): the first failing single shell (B = 12,
  even) has a provably one-signed positive spectrum; its |hatf|-mass
  identities need no absolute values.
- **#820/#824** (omega-sound floor, adequacy): on dense shells omega =
  h_+ is |h| (even B) or 0 (odd B) classwide -- the sign-mixing overpay
  anatomy of #820 is impossible on this family at every depth.
- **#818** (emission arithmetic): dense-shell class budgets are
  one-signed sums, so the cube ell^1 there is |sum| -- no absolute
  values needed when the emission arithmetic is ported to product
  profiles.
- **#816** (rank-one product law): the T3-backward-orbit form is the
  non-hierarchy analogue of the top-character localization there.
- Method precedent: the coupled-pair cone argument is self-contained;
  the S-preimage cubic is recorded for the sparse/mixed-shell sequel.
