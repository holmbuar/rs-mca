# Dense-shell PROP-TAIL: DISCHARGED (certified-census, CONDITIONAL) via the deep-base equilibrium chain

Stacked on the predecessor packet (`experimental/notes/thresholds/dense_shell_inv_tail_closure.md`,
PR #885), which reduced #880's |K| = 1 class-sum dichotomy (unconditional persistence
of three certified floors for all levels j >= 49) to a single named scalar residual,
(PROP-TAIL): the cross-index spread of the sibling entrywise ratio profile,
`rho_prop@i<17(n) <= 1.02560749`, persisting for all n beyond the level-60 grid the
predecessor certified. This packet reduces that scalar from an opaque numeric
persistence claim to a **certified contraction frame** — an exact reduction lemma, an
exact spectral gap, a certified one-step recursion, and a joint induction — and then
**closes it**: the deep-base equilibrium route (base `J0* = 500`, floor pad
`f* = 99/100`, contraction gate `theta* = theta_band`, a certified band-uniform constant
from gate V15-IA, not a fixed number) clears the arithmetic slot on **finite checks**,
certified by an exact-Fraction, lam-minced interval-arithmetic census of the tangent
seminorm (gate V15-IA) feeding an exact-Fraction minced interval-arithmetic forcing
census (gate V17-IA), plus a re-certified floor family at the deep base (gate F3) plus
full base coverage to `n = 500` (gate V18). **The discharge holds as a certified-census
theorem MODULO the enumerated computed clauses** (Section 8.4: LAM-BOX, SIB-BAND, FOLD,
FLOOR-PERSIST) — its two load-bearing gates certify a **forced-proportional surrogate**
(`c^+ = lam c^-`) of the real cascade, so the STATUS is **CONDITIONAL**, not PROVED. The
contraction gate `theta* = theta_band` is a certified band-uniform constant from gate
V15-IA, not an asserted number.

## 0. Status (S0)

**(PROP-TAIL) DISCHARGED as a certified-census theorem MODULO the enumerated computed
clauses (Section 8.4) — STATUS: CONDITIONAL.** House form: **PROVED (equilibrium chain,
sufficiency) + census-closed (gates F3 / MAG-BOX / V15-IA / V17-IA / V18), conditional on
the four computed clauses (LAM-BOX, SIB-BAND, FOLD, FLOOR-PERSIST)**. The composed
theorem (Section 7) is PROVED-given-gates; every core gate it depends on is green at the
shipped triple `(J0*, f*, theta*) = (500, 99/100, theta_band)`, where **`theta_band` is
itself a certified band-uniform output of gate V15-IA** (Section 5), not an asserted
constant. The two load-bearing gates (V15-IA, V17-IA) certify the **forced-proportional
surrogate** `c^+ = lam c^-` of the cascade; the residual computed content (the magnitude
box the gates box-max over, the real non-proportional cascade, the window fold, and floor
persistence for `n > 500`) is enumerated explicitly in Section 8.4. Certified equilibrium
arithmetic (exact values; final gate comparisons are exact Fraction; gates V15-IA /
V17-IA / V18):

```
    theta_band                  = 0.6020244   (certified band-uniform sup, gate V15-IA,
                                                exact Fraction 1505061/2500000, lam-minced
                                                rigorous enclosure, folded by the certified
                                                Window Lemma factor <=57/50)
    F_box(500, 99/100)          = 0.02687612  (certified sup, width-2 minced-IA, Fraction, gate V17-IA)
    tau*                        = 0.07585533  (exact-Fraction lower bound TAU_STAR_FR
                                                = 0.075855330599169 <= 3 log(1.02560749))
    threshold (1-theta*)*tau*   = 0.03018857  (theta*=theta_band; final comparison exact Fraction)
    margin                      = 11.0%       (F_box 0.02687612 <= 0.03018857 clears the threshold)

    equilibrium chain (gate-printed):
      F_box/(1-theta_band)      = 0.06753207  <= tau* = 0.07585533   [OK]
      (1/3)*0.06753207          = 0.02251069  <= log(TARGET) = 0.02528511
      exp(0.02251069)           = 1.022766    <= TARGET = 1.02560749  [OK]

    sup_{n>=500} V_17(n) <= max(V_17(500), F_box/(1-theta_band))
                          = max(0.00111699, 0.06753207)
                          = 0.06753207                         (the forcing dominates)

    log rho_prop@i<17(n) <= (1/3) * 0.06753207 = 0.02251069    (for all n >= 500, Lemma 1)
    ln(1.02560749)                             = 0.02528511
                            0.02251069 < 0.02528511            margin 11.0%
```

for all `n >= 500`; the deep grid (gate V18) covers `48 <= n <= 500` directly (every
tested level `rho_prop@i<17(n) <= 1.02560749`, monotone non-increasing), so **the
target holds for every `n >= 48`**, discharging (PROP-TAIL) modulo the Section 8.4
computed clauses.

**The contraction gate, precisely.** The discharge-determining contraction gate is
`theta* = theta_band`, a certified band-uniform output of gate V15-IA (Section 5): an
exact-Fraction, lam-minced rigorous enclosure of the Lemma A1 tangent seminorm over the
*entire* certified LC ratio box, not merely a tested grid or the realized profile.
Certified `theta_band = 0.6020244`; at the shipped anchor `(500, 99/100)` the forcing
census clears with an 11.0% margin. The grid census (`theta_tot`, `theta_win`, `N_free`)
is retained as an **informational robustness cross-check** (gate `V15-GRID`) — it is
comfortably consistent with the certified band (`theta_tot`'s worst grid value `0.3766`
sits well inside `theta_band = 0.602`), but is not part of the certified chain.

**PROVED** (elementary; no finite check needed beyond exact rational/interval
arithmetic):
- the **reduction lemma** (Section 2, Lemma 1): `log rho_prop@i<17(n) <= (1/3) V_17(n)`,
  where `V_17(n)` is a *single-level* windowed tangent spread — proved by the
  fundamental theorem of calculus plus a triangle inequality, removing the two-branch
  coupling from the target;
- `theta~(t) <= 1/5` (Section 4, Lemma 3) via the **exact polynomial identity**
  `75(1-x^2) - (6+3x)^2 = -3(2x-1)(14x+13)`, `x = cos(2 pi t/3) in [1/2, cos(pi/9)]`,
  verified coefficient-by-coefficient over the rationals; equality only at `x = 1/2`
  (the domain's edge, `t = 1/2`);
- the **exact 3-term cascade** `L = T1 (share-variation) + T2 (smoothed deviation) +
  T3 (a'-source)`, imported from the predecessor's differential-cascade machinery
  (Section 3);
- the **tangent-half corner-sufficiency closed form** (Lemma A1, Section 5): for fixed
  profiles, the map from child log-derivative deviations to the deviation term `T2` is
  linear, and its induced oscillation-seminorm has an exact closed form (an LP-vertex
  identity — no sampling loss in the tangent direction);
- the **band-uniform tangent census** (Section 5, gate V15-IA, one of the two
  load-bearing certificates): an exact-Fraction, lam-minced rigorous enclosure of Lemma
  A1's seminorm over the *entire* certified LC ratio box (not the realized profile, not a
  tested grid) — `theta_band = 0.6020244`, certified for every `n >= J0*`, feeding
  gate V17-IA's threshold directly;
- the **window lemma's asymptotic fact** `289/256 <= 57/50` (Section 6, Lemma W1) —
  an exact rational inequality;
- the **triangle steps** (Section 6, Lemma W3, and the second inequality of Lemma 1):
  subadditivity of `max - min`, no hypotheses;
- the **deep-base forcing census** (Section 8.1, gate V17-IA, one of the two
  load-bearing certificates): `F_box(500, 99/100) <= (1-theta_band) tau*` via an
  exact-Fraction, minced interval-arithmetic enclosure of the box-certified forcing at
  width-2 locality (every index `i`'s marginal range, not merely the two endpoints) — a
  rigorous upper bound, not a corner-sample estimate;
- the **re-certified floor family at the deep base** (Section 8.1, gate F3):
  positivity, LC-compatibility, and the `i = 0` halving-convention cross-check hold at
  `J0* = 500`, pad `f* = 99/100`, over the full 41-parent grid.

**COMPUTED — informational grid views** (a finite, reproducible measurement, not a
proof; these specific items are robustness cross-checks, not gates the discharge rests
on — the computed inputs that DO feed the certified chain are enumerated separately in
Section 8.4):
- `theta_tot in [0.3662, 0.3766]` over `n in {60,...,500}` — **flat**, and **binding at
  the parent `t = 1/6`, not the edge** (a correction to a naive edge-only reading, see
  Section 10); comfortably inside the certified `theta_band = 0.602` at every level
  tested — a robustness cross-check, not the gate the discharge rests on (gate
  `V15-GRID`, informational);
- `theta_win in [0.1971, 0.2032]` over the same grid — flat, binding at the edge `t ->
  1/2`;
- forcing tables `F_ext(n)*n^2 in [182.4, 187.8]` and `Curv(n)*n^2 in [100.4, 109.1]`,
  both flat/decaying, with a **hairline non-monotonicity in `Curv*n^2` at n = 300**
  (an uptick of +0.002, ~0.002% relative) flagged as most likely finite-difference
  noise at that small a raw value, not a real turn;
- the bridge weight `w(n) ~ 0.61` (range `[0.6084, 0.6115]`, informational/alpha-only —
  not used by the shipped equilibrium chain, Section 2);
- the deep grid to `n = 500`: `rho_prop@i<17(n) <= 1.02560749` at every gated level,
  monotone non-increasing, margin growing from `+1.7e-5` at `n=48` to `+0.0254` at
  `n=500`;
- the crossover `V_17(n) <= tau* := 3 log(1.02560749) = 0.075855...` at **exactly**
  `n = 62` (`V_17(61) = 0.0761 > tau*`, `V_17(62) = 0.0737 <= tau*`, full-integer scan) —
  informational (the deep grid to `n=500` already covers the base directly; the
  equilibrium route does not need this crossover, only the sharp/R-c strengthening
  would);
- the mu-sign / monotone-cone tightener `theta~0.376` for the *sharp* `C/n^2` law stays
  COMPUTED/informational only — checked and found **NOT** to carry as a clean
  finite corner certificate (Section 8.3); **not needed** for this discharge, which
  uses only the certified band-uniform `theta_band` gate.

## 1. Objects and conventions (self-contained)

Level vectors `G_n(t)`, `t in [1/6, 1/2]`. Flipped-positive half-weight coordinates
`c_0 = b_0`, `c_i = b_i/2`, even-extended (`c_{-1-k} := c_k`). One branch step is exact
`Z`-convolution with the tridiagonal kernel `K_d = (1/4, d, 1/4)`, `d(t) = -cos(2 pi
t)/2`; children `t_pm = (1 pm t)/3`; the aggregated step

```
    c(G_n(t)) = K_{d(t_+)} * c(G_{n-1}(t_+)) + K_{d(t_-)} * c(G_{n-1}(t_-)).      (STEP)
```

Mass factor `a(t) = sin^2(pi t) = 1/2 + d(t)`; `a'(t) = pi sin(2 pi t)`. Write
`rc_i := c_{i+1}/c_i` (band ratio), `L_i(n,t) := d/dt log c_i(G_n(t))` (the *tangent*
object this packet's frame is built on), and the *sibling* ratio and its cross-index
spread (the predecessor's S7 object, V13's convention):

```
    g_i(n,t) := c_i(G_n(t_-)) / c_i(G_n(t_+)),
    rho_prop@i<W(n) := sup_t  max_{i<W} g_i / min_{i<W} g_i.
```

**Operative window**: `i < 17` (indices 0..16, `OPWIN = 17`), the corner-vector length
the predecessor's census (V12) consumes. **Honest child-read window**: `i < 18`
(indices 0..17, `CWIN = 18`) — the tridiagonal step reads one index beyond the output
window (Section 6). The windowed single-level tangent spread and its threshold:

```
    V_W(n) := sup_t [ max_{i<W} L_i(n,t) - min_{i<W} L_i(n,t) ],
    TARGET := 1.02560749,   tau* := 3 * log(TARGET) = 0.07585533...
```

**Imported facts** (established in the predecessor packet, re-used here without
re-proof): the c-vector is nonincreasing (`rc_i <= 1` for every `j >= 5`, PROVED);
level-48-anchored floors `rc_i(n,t) >= (49/50) rc_i(48,t)` persist for all `n >= 48`
(certified, since `rc_i` drifts upward in `n`); the output c-ratios stay non-increasing
under the predecessor's corner census (output log-concavity, "output-LC" — see the
precision note in Section 10 for an honest caveat on this specific clause); the
degenerate CLT limit `c_i(n,t) ~ c_0 exp(-beta i^2/n)`, `beta = 0.6191` (COMPUTED, a
fitted asymptotic, not proved); and the differential cascade `Dc(G_n) = (1/3)[K_{d+} *
Dc^+ + a'(t_+) c^+] - (1/3)[K_{d-} * Dc^- + a'(t_-) c^-]` (PROVED, chain rule), which
Section 3's cascade below re-derives for the tangent object `L`.

## 2. Lemma 1 — the reduction. PROVED.

> **Lemma 1.** For every level `n` with `c_i(G_n(t)) > 0` on `i < 17`, `t in [1/6,1/2]`
> (guaranteed by the caps/floors above):
> ```
>     log rho_prop@i<17(n)  <=  sup_t (2t/3) * sup_{tau in [t_-,t_+]} spread_{i<17} L(n,tau)
>                            <=  (1/3) * V_17(n).
> ```

*Proof.* Fix `t`. For each `i`, `log g_i(n,t) = log c_i(G_n(t_-)) - log c_i(G_n(t_+)) =
-integral_{t_-}^{t_+} L_i(n,tau) dtau` (fundamental theorem of calculus). For any two
indices `i, i' < 17`, `log g_i - log g_{i'} = -integral(L_i - L_{i'}) dtau <=
integral spread_{i<17} L(n,tau) dtau`. Taking `max_i, min_{i'}`, then `sup_t`:
`spread_{i<17} log g_i(n,t) <= (t_+ - t_-) sup_{tau in [t_-,t_+]} spread_{i<17}
L(n,tau)`. Since `t_+ - t_- = 2t/3 <= 1/3` and `[t_-,t_+] subset [1/6,1/2]`, the RHS is
`<= (1/3) V_17(n)`. QED.

**What this buys.** `rho_prop` is a *two-branch* object (it compares the two
children); Lemma 1 bounds it by a *single-profile* object `V_17(n)` — the coupling
survives only in the *recursion* for `V_17` (Sections 3-5), never in the target itself.
This is the entire reduction: everything after this lemma is about bounding one
single-level tangent spread, not a sibling pair.

**Tightness (informational).** The ratio of the loose bound `(1/3)V_17(n)` to the
sharp integral form is a *bridge weight* `w(n)`, COMPUTED flat at `~0.61` (gate V19,
Section 11) — the `(1/3)`-form alone overstates by a nearly-constant `1/0.611 = 1.637x`
factor. The certified spine below (Section 7) uses the loose `(1/3)` form plus decay,
never the tight integral, so `w` plays no role in the beta-spine discharge; it is kept
only as an alpha-route, informational cross-check (Section 9(iii), Section 11's V19).

## 3. Lemma 2 — the exact 3-term cascade. PROVED structure, COMPUTED reconstruction.

Write `c^pm := c(G_{n-1}(t_pm))`, `W^pm := K_{d(t_pm)} * c^pm` (so `c(G_n) = W^+ +
W^-` by (STEP)), branch shares `sigma^pm_i := W^pm_i / c_i(G_n)`
(`sigma^+_i + sigma^-_i = 1`), child log-derivatives `L^pm_k := L_k(n-1, t_pm)`, split
`L^pm_k = Lambda^pm + delta^pm_k` about the **window-mean reference scalar**
`Lambda^pm := mean_{k<18} L^pm_k` (the choice is not free: the Lemma A1 seminorm
`(1/2) sum_k |Delta_k - mu|` is the operator norm over ZERO-SUM deviations, and only the
window-mean makes `delta^pm` zero-sum; with a non-zero-sum `delta` the row-sum mass
differs and `osc(T2)/osc(delta)` is unbounded — adding a constant to `delta` leaves
`osc(delta)=0` but `osc(T2)!=0`. The choice is sound and costs nothing:
`osc(delta) = spread(L) = V_17(n-1)` is shift-invariant, unchanged by the reference).
Then, from the chain rule applied to (STEP) (the predecessor's differential-cascade
machinery, re-derived here for `L` rather than `Dc`), **exactly**:

```
  L_i(n,t) = (1/3)[ Lambda^+ sigma^+_i - Lambda^- sigma^-_i ]                       (T1, share-variation)
           + (1/3)[ (K_{d+}*(delta^+ (x) c^+))_i - (K_{d-}*(delta^- (x) c^-))_i ] / c_i(G_n)   (T2, smoothed deviation)
           + (1/3)[ a'(t_+)(c^+_i - c^-_i) - a'(t/3) c^-_i ] / c_i(G_n).            (T3, a'-source)
```

**COMPUTED**: reconstruction `max_i |T1+T2+T3 - L_i| <= 4e-11` at every tested `(n,t)`.
`T2` alone carries the recursion (it is the only term reading the *child deviations*
`delta^pm`, whose spread is `V_17(n-1)`); `T1, T3` are forcing terms driven by the
child *profiles*, not their tangent deviations.

## 4. Lemma 3 — the leading contraction, closed form. PROVED.

> **Lemma 3.** In the identical-sibling limit (`c^+ = c^- =: c`, `delta^+ = delta^- =:
> delta`), `T2` reduces to `T2_i = theta~(t) delta_i (1 + O(1/n))` with
> ```
>     theta~(t) = (d_+ - d_-) / (3(a_+ + a_-)) = sqrt(3) sin(2 pi t/3) / (6 + 3 cos(2 pi t/3)),
> ```
> increasing on `[1/6, 1/2]`, `theta~(1/6) = 0.0672`, `theta~(1/2) = 1/5`. Hence
> `theta~(t) <= 1/5` on the whole domain, with the **maximum at the binding edge**
> `t = 1/2` (equality there).

*Proof.* The two kernels differ only in the center weight, `K_{d+} - K_{d-} = (d_+ -
d_-) delta_0`, so the `T2` numerator collapses to `(1/3)(d_+ - d_-) delta_i c_i`; the
denominator `c_i(G_n) = (a_+ + a_-) c_i (1 + O(1/n))` by the trace identity `a_+ + a_-
= 1 - d(t/3)`. Dividing gives the closed form; `d_+ - d_- = (sqrt(3)/2) sin(2 pi t/3)`
and `a_+ + a_- = 1 + (1/2) cos(2 pi t/3)` by product-to-sum on `d(s) = -cos(2 pi s)/2`.
For the bound: set `x = cos(2 pi t/3)`. Squaring (both sides nonnegative on the
domain), `theta~(t) <= 1/5` is equivalent to `75(1-x^2) <= (6+3x)^2`, i.e.
```
    75(1-x^2) - (6+3x)^2  <=  0.
```
**Exact polynomial identity** (Fraction-verified, coefficient-by-coefficient in `x`):
```
    75(1-x^2) - (6+3x)^2  =  -3(2x-1)(14x+13).
```
On the domain `t in [1/6,1/2] => x = cos(2 pi t/3) in [1/2, cos(pi/9)]` (cos decreasing):
`(2x-1) >= 0` (equality only at `x = 1/2`, i.e. `t = 1/2`) and `(14x+13) >= 20 > 0`, so
`-3(2x-1)(14x+13) <= 0` throughout, equality only at the edge. QED.

This is **the spectral gap the predecessor's shape-analysis could not see**: it lives
in the *tangent* (log-derivative) direction, not in the profile itself — the
predecessor's own refutation of a uniform full-profile contraction (`theta_j -> 1` as
`n` grows, no geometric contraction on the *shape*) is a fact about a different object.

## 5. The tangent corner-sufficiency certificate (Lemma A1)

`T2_i` is, for **fixed** child profiles `(c^+,c^-)`, a **linear** map of the deviation
vectors `(delta^+, delta^-)`:
```
   T2_i = sum_k M^+_{ik} delta^+_k + sum_k M^-_{ik} delta^-_k,
   M^pm_{ik} = (1/3) (K_{d(t_pm)})_{ik} c^pm_k / o_i,     o := K_{d+}c^+ + K_{d-}c^- = c(G_n(t)).
```
`osc_{i<17}(T2) = max_{i,i'} (T2_i - T2_{i'})` is then a max of linear functionals of
`(delta^+, delta^-)` — convex and positively homogeneous, hence a **seminorm**; its
extreme over the polytope `{osc(delta^pm) <= 1}` sits at vertices.

> **Lemma A1 (tangent seminorm, PROVED).** Take the deviations `delta^pm` about the
> **window-mean reference** `Lambda^pm = mean_{k<18} L^pm_k` (so `delta^pm` is zero-sum,
> Section 3 — the seminorm below is the operator norm over ZERO-SUM deviations, and the
> window-mean is the choice that realizes it). With `Delta^pm_k := M^pm_{ik} -
> M^pm_{i'k}`, `mu^pm := mean_k Delta^pm`,
> ```
>   ||delta -> T2||_{osc<-osc}  =  max_{0<=i<i'<17}  (1/2)[ sum_k |Delta^+_k - mu^+| + sum_k |Delta^-_k - mu^-| ],
> ```
> an exact LP-vertex identity — **no sampling loss in the tangent direction**.

`K_d` is tridiagonal (`(K_d)_{ik}` nonzero only for `|i-k| <= 1`, plus the
even-extension doubling at `i=0`), so each row of `M^pm` has at most 3 nonzero entries
and the sum above is cheap and exact (rational, given rational inputs).

**What is (and is not) rigorously certified here.** Lemma A1 makes the *tangent*
direction exact: for any FIXED profile pair `(c^+,c^-)`, the seminorm formula above is
the true operator norm, not an estimate. The grid gate `V15-GRID` (informational,
Section 11) evaluates that exact formula only at the *realized* profiles on a 41-parent
grid at each tested level `n` (**COMPUTED** — a grid measurement at the actual cascade,
not a box census). The **profile** direction does *not* enjoy the predecessor's V12
Möbius corner-sufficiency (the seminorm, as an `osc`/max-min object, is a difference of
terms with *different denominators* `o_i, o_{i'}`, hence a degree-`(2,2)` rational in
each profile ratio, not a Möbius function — the same structural boundary the precision
note of Section 10 documents for V12's own out-LC clause).

**The band-uniform enclosure (gate V15-IA).** Under the SAME forced
sibling-proportionality reduction gate V17-IA already uses (`c^+ = lam c^-`, `lam` in
the certified magnitude box), `M^pm_{ik}` reduces to `(1/3) w_ik lam^{[pm=+]}
(c^-_k/c^-_i)/(A+B P_i)` (`A = lam d_+ + d_-`, `B = lam+1`, `P_i` as in Lemma C0). For
**fixed** `lam`, the diagonal entry depends on `(rc_{i-1},rc_i)` only via the scalar
`P_i` (reuse its own tight closed-form box), and the off-diagonal entries are — by direct
partial-derivative computation, no assumption — strictly coordinatewise monotone in
**both** `(rc_{i-1},rc_i)` simultaneously, with a sign independent of `lam`, so their
extremes sit at exactly two `(rc_{i-1},rc_i)` points (a monotone-path argument). Each
entry is Möbius in `lam` — but the **seminorm** is a sum of `|differences of
Möbius-in-lam entries with different denominators|`, so it is **not** itself Möbius in
`lam` and can attain its maximum at an interior `lam`; an endpoint-in-`lam` sufficiency
argument would therefore be **unsound**. The rigorous fix is to **mince `lam` into
panels** (`LAM_MINCE = 24`), hull each Möbius-in-`lam` entry over each panel, and take
the outer max over panels — a genuine rigorous enclosure over the shared-`lam` box (all
entries in a given panel evaluation share one `lam` sub-interval, respecting the
shared-`lam` constraint; a per-entry-independent-`lam` bound would be strictly looser,
Section 9(iv)). Cross-validated against 36,000 random LC-feasible profile draws (0
violations). **Certified**: `theta_band = 0.6020244` (exact Fraction `1505061/2500000`,
window-folded, `J0*=500, f*=99/100`) — comfortably inside the gate's own unconditional
sanity ceiling `0.9`, and consistent with the realized `theta_tot approx 0.35-0.38` (the
realized deviation is far from the seminorm's own worst-case vertex). This forced-
proportional surrogate is what the load-bearing gates certify; the real cascade is
non-proportional, and that gap is enumerated as computed clause (SIB-BAND) in Section
8.4. `theta_band` feeds gate V17-IA's threshold as `theta*` (Section 8.1) — the
discharge's contraction gate is a **certified band-uniform constant**, not a grid
measurement.

## 6. Window lemmas (W1-W3)

The tridiagonal step means the output index `i = 16` (the top of the operative window)
reads child index `k = 17` — one beyond the operative window. Three lemmas unify this
bookkeeping.

> **Lemma W1 (child-window factor).** The one-step contraction census on the operative
> output window `i < 17` reads child `L`-deviations on `i < 18`, and
> ```
>     spread_{i<18}(L)  <=  (V_18/V_17) * spread_{i<17}(L),   V_18/V_17 -> 289/256 = 1.128906...  (n -> infinity),
> ```
> certified by the finite check `sup_{n,t} spread_{i<18}(L)/spread_{i<17}(L) <= 57/50 =
> 1.14` (measured max `1.1322` at `n = 48`, decreasing thereafter).

The asymptotic ratio comes from the degenerate CLT tangent profile `L_i propto -i^2`,
giving `mu_k := L_{k+1} - L_k propto (2k+1)`, hence `V_W propto (W-1)^2`
(`V_18/V_17 -> 17^2/16^2` exactly, an elementary consequence of the quadratic profile).
**Label**: the arithmetic fact `289/256 <= 57/50` is PROVED (exact rational
comparison); but the fold factor `57/50` actually used by the gates is a **COMPUTED
(grid-measured) bound** — it is `sup_{n,t}` over the FINITE grid (measured max `1.1322`
at `n = 48`, decreasing thereafter) resting on a COMPUTED CLT quadratic-profile ansatz
(`L_i propto -i^2`), gated by V16b, **not proved for all `n`**. It is enumerated as
computed clause **(FOLD)** in Section 8.4.

> **Lemma W2 (census window for curvature objects, PROVED read-set).** Any gate
> certifying `Curv_{i<17} := sup_t spread_{i<17}[(K_d * c)_i/c_i]` (or `F_ext`'s
> `T3`-ratio) must sample `c_0, ..., c_17` — the operative corner vector (`c_0..c_16`,
> 17 values) extended by **one** index. A census truncated at `c_16` undercounts
> `Curv_{i<17}` by a measured factor of `1.14`-`1.15` (gate V16b's structural check).

*Why*: the top row's curvature term is `P_16 = (1/4)(rc_16 + 1/rc_15)`, and `rc_16 =
c_17/c_16` needs the 18th c-value. This is not a numerical coincidence; it is the
tridiagonal read-set, confirmed by V16b's direct comparison of the correctly-computed
spread against the one-index-short proxy.

> **Lemma W3 (triangle, PROVED, no hypotheses).**
> `V_17(n) = sup_t spread_{i<17}(T1+T2+T3) <= sup_t [spread(T1) + spread(T2) +
> spread(T3)]`, by subadditivity of `max - min`.

The COMPUTED "alignment" of `T1,T2,T3` (all three monotone in `i`, near-equal to the
sum to `<1%`) is a tightness remark only; the discharge chain (Section 7) never needs
the near-equality, only the `<=` direction.

## 7. THE THEOREM — the composed discharge, parametric in the forcing input

Notation: `B(n)` = the predecessor's step-closed bundle at level `n` (`{caps, LC,
floors >= 0.98 r_i(48,t), sigma <= sigma_max(t), rho_prop@i<17 <= TARGET}`, certified
step-closed there by its own corner census); `V_17(n)` as above; `tau* = 3
log(TARGET) = 0.075855...`.

> **IH `H(m)`:** `B(m)` holds **and** `V_17(m) <= v_m`, `{v_m}` a tracked ceiling (base:
> measured on the grid; step: the recursion below).

> **Composed Theorem (parametric).** Assume: **(G-theta)** the contraction gate
> `theta_tot <= theta*` with `theta* < 1` certified (Section 4's exact `theta~ <= 1/5`
> plus Section 5's band-uniform tangent seminorm plus Lemma W1's window fold; gate
> V15-IA/V16/V16b — `theta*` is itself `theta_band`, V15-IA's certified output);
> **(G-F)** the forcing gate `F(m) <= Phi(m)` certified (gate V17); **(Base)** the deep
> grid establishes `H(m)` for `48 <= m <= J*` (gates V13-style census + V18). Then, for
> the arithmetic recursion `v_m := theta* v_{m-1} + Phi(m-1)`, **if `v_m <= tau*` for
> all `m > J*`**, `H(n)` holds for all `n >= 48` — i.e. `rho_prop@i<17(n) <= TARGET` for
> all `n`, and **(PROP-TAIL) is DISCHARGED**.

**The step `H(n-1) => H(n)`, labeled:**
- **(i) V-recursion.** By the exact cascade (Lemma 2, PROVED structure) and `osc(sum)
  <= sum osc` (Lemma W3, PROVED), `V_17(n) <= osc(T2) + osc(T1+T3)`. Gate (G-theta)
  bounds the `T2` + sibling multiplier by `theta* V_17(n-1)` (Sections 4-6: `theta~ <=
  1/5` exact + the tangent seminorm + the window fold); gate (G-F) bounds the
  curvature-only residual `osc(T1+T3)|_{g equiv const} = F(n-1) <= Phi(n-1)`. Hence
  `V_17(n) <= theta* V_17(n-1) + Phi(n-1) <= theta* v_{n-1} + Phi(n-1) =: v_n`.
  **PROVED-given-gates.**
- **(ii) Reduction.** Lemma 1 (PROVED): `log rho_prop@i<17(n) <= (1/3) V_17(n) <= (1/3)
  v_n`. If `v_n <= tau*`, `rho_prop@i<17(n) <= TARGET` — the `rho_prop` clause of
  `B(n)`. **PROVED-given (i) + the arithmetic slot.**
- **(iii) Box closure.** With `rho_prop@i<17(n) <= TARGET` established, the
  predecessor's own step machinery (its corner census + assembly) closes the remaining
  clauses of `B(n)` (`{caps, LC, floors, sigma}`) exactly as it already does in the
  predecessor packet. **PROVED (sufficiency)-given-gates** (that packet's own label for
  this step). `H(n)` holds. **Floor persistence for `n > 500` specifically** is not
  re-derived here: it composes from the predecessor packet's monotone-drift machinery
  re-anchored at the `(500, 99/100)` floors (`rc_i` drifts upward in `n`, so the
  level-500 floors persist upward). That machinery is **COMPUTED in the predecessor and
  imported** here — enumerated as computed clause **(FLOOR-PERSIST)** in Section 8.4.

Base = the deep grid (`48 <= n <= J*`), well-founded (single intra-level edge,
acyclic, matching the predecessor's own joint-induction argument).

### 7.1 The arithmetic slot — INSTANTIATED (R-a, the deep-base equilibrium)

Iterating `v_n = theta* v_{n-1} + Phi(n-1)` (`theta* < 1`, elementary geometric-sum,
PROVED):

| route | forcing `Phi(m)` | closed bound `v_n` | slot condition | grid `J*` |
|---|---|---|---|---|
| **R-a** (deep-base, constant) — **INSTANTIATED** | `F_box(500,99/100) = 0.02687612` (certified constant, gate V17-IA) | `max(v_500, F_box/(1-theta_band)) = 0.06753207` | `F_box/(1-theta_band) = 0.06753207 <= tau* = 0.07585533` — **CLEARS, 11.0% margin** | `J* = 500` (gates F3/MAG-BOX/V15-IA/V17-IA/V18) |
| R-b (sandwich, `O(1/n)`) — strengthening, not needed | `c_1/m`, `c_1 = 3/8` (leading, at `kappa=3/2`) | `[c_1/(1-theta*)]/n * (1+o(1))` | crosses `tau*` at `n* approx c_1/((1-theta*)tau*)` | `~250-300` |
| R-c (sharp, `O(1/n^2)`) — strengthening, not needed | `B_crv/m^2`, `B_crv/(1-theta*) = 282` (explained, `= 185/0.657`) | `[B_crv/(1-theta*)]/n^2 * (1+o(1))` | `<= tau*` for `n >= 62` | `~62-80` |

**R-a closes the slot.** With the certified `theta_band = 0.6020244` (gate V15-IA,
Section 5) and the certified `F_box(500, 99/100) = 0.02687612` (gate V17-IA, Section
8.1), `F_box/(1-theta_band) = 0.06753207 <= tau* = 0.07585533` — an 11.0% margin — so
`v_n <= 0.06753207` for all `n > 500`, and by (ii), `log rho_prop@i<17(n) <=
(1/3)(0.06753207) = 0.02251069 < ln(1.02560749) = 0.02528511` for all `n >= 500`. The
deep grid (gate V18) directly covers `48 <= n <= 500`. **Every hypothesis of the
Composed Theorem is discharged on finite checks, with `theta*` itself a certified
band-uniform constant, not an asserted one** — no decay-rate input, no Edgeworth content,
Edgeworth-free and mu-sign-free throughout. The remaining computed inputs to this
certified chain (the magnitude box the gates box-max over, the forced-proportional
surrogate, the window fold, floor persistence) are enumerated as computed clauses in
Section 8.4, which is why the STATUS is CONDITIONAL. R-b/R-c remain open as
**strengthenings** toward the sharp `C/n^2` law (Section 8.2-8.3) — genuinely
interesting, but **not needed** for this discharge.

### 7.2 The firewall (what this theorem does NOT give)

- **Magnitude `kappa_c` is untouched.** The whole chain is **spread-only** (Lemma 1
  bounds a spread; `V_17` is a spread; `T1/T2/T3`'s common reference scalar `Lambda` is
  invariant and never appears in the bound). It is structurally incapable of proving
  `kappa_c -> 1` — consistent with the flat-at-`~1.29` measured magnitude. Any claim
  about the magnitude would be a category error against this frame.
- **Window-specific.** The theorem is for the **operative window `i < 17`** at the
  target `1.02560749`. `i < 10` decays faster and is informational only (as in the
  predecessor); nothing is claimed for `i >= 17` or window-free.
- **The sharp `C/n^2` law** still requires the **R-c** row specifically (Section 8.3,
  CONJECTURAL) — the discharged R-a route gives a constant-forcing equilibrium
  sufficient for (PROP-TAIL), not the sharp rate.
- **General `K` / other windows** remain outside this packet's scope (unchanged from
  the predecessor).
- **The binding scope pin** (repository experimental-ledger track only) is stated once,
  in full, in Section 12 — it applies here without repetition.

## 8. THE RESIDUAL LADDER — R-a INSTANTIATED (this packet); R-b/R-c open strengthenings

Section 7.1's arithmetic slot needs exactly one of three statements. **R-a is
INSTANTIATED**, discharging (PROP-TAIL) modulo the Section 8.4 computed clauses; R-b and
R-c remain open **strengthenings** toward the sharp `C/n^2` law — genuinely interesting
future work, but not needed for the discharge itself.

### 8.1 (R-a) Deep-base box feasibility — INSTANTIATED

The certified box (caps `rc_i <= 1`; floors `rc_i >= f* rc_i(J0,t)`; output-LC)
certifies, via the curvature normal form `Curv(n) = sup_t spread_{i<17}[(K_d*c)_i/c_i]
= sup_t spread_{i<17}(P_i)` (`P_i` as in Lemma W2), only a **CONSTANT** bound in `n` —
the floors are level-`J0` constants, and nothing in caps/floors/LC shrinks with `n`.
At the **shipped-then** base `J0 = 48` this constant missed the requirement by `~3.9x`
(`box F_const(48) = 0.196` vs required `(1-theta_tot)tau* = 0.657 * 0.075855 = 0.0498`,
using the edge-only `theta_tot=0.343` reading; the corrected sup-over-`t` reading up to
`0.376` worsens the miss slightly further, to `~4.1x`). **Re-basing closes it.** Raising
the certified base to `J0* = 500` — re-running the corner census with floors anchored
there (gate F3: positivity, LC-compatibility, and the `i=0` halving convention all
verified over the 41-parent grid) and certifying the forcing at that base via an exact,
non-sampled interval-arithmetic enclosure (gate V17-IA) — gives, at the anchor
`f* = 99/100`:

```
    F_box(500, 99/100)          = 0.02687612  (certified sup, width-2 minced-IA, exact Fraction)
    required (1-theta_band)*tau* = 0.03018857 (theta_band = 0.6020244, gate V15-IA's certified band-uniform output)
    margin                      = 11.0%       (CLEARS)
```

**Method, honestly.** A naive "corner-sample the two window endpoints `i=0,16` and rely
on the child ratio profile being monotone across the whole box" gives a numerically
close but *unrigorous* estimate (it rests on a monotonicity fact that is true on the
measured/realized cascade but not proved to hold at every point of the certified box).
Gate V17-IA instead computes a marginal interval for **every** index `i = 0..16`
(mincing each ratio's range and enclosing every LC-feasible adjacent panel pair,
in exact Fraction arithmetic, no sampling), which is provably a valid upper bound
regardless of that monotonicity question. Deriving the threshold: Lemma 1 gives
`log rho_prop <= (1/3)V_17(n)`; the V-recursion at constant forcing gives the
equilibrium ceiling `F_box/(1-theta_band)`, which must sit `<= tau*` — exactly this
gate's check (`tau*` enters as the exact-Fraction lower bound `TAU_STAR_FR =
0.075855330599169`, and the final comparison is exact Fraction). **Status: R-a CLEARED
at `(500, 99/100)` with an 11.0% margin, conditional on the Section 8.4 computed
clauses.** The contraction gate `theta*` is a certified band-uniform constant (gate
V15-IA), not an asserted one resting on a grid measurement; the grid census `theta_tot`
is retained purely as an informational robustness cross-check (Section 0), comfortably
inside `theta_band` at every level tested to `n=500`.

### 8.2 (R-b) The two-sided sandwich — open strengthening, not needed

> **Sandwich hypothesis.** On the operative window, uniformly in `t` and for `n >=
> J0`: `l_0 := log(rc_0) >= -c_0/n` with `c_0 = 5/8` (a rational `>= beta = 0.6191`);
> and `D2_i := l_i - l_{i-1} >= -kappa/n` for `1 <= i <= 16`, `kappa = 3/2` (a rational
> `>= kappa_hat`, the measured worst-case constant). The upper sides (`l_i <= 0`,
> `D2_i <= 0`) are log-concavity, already available (proved on one branch, computed in
> general).

> **Lemma C2 (sandwich => `O(1/n)`, PROVED given the hypothesis).** Under the
> sandwich, `|l_i| <= (c_0 + 16 kappa)/n` on the window, giving
> `Curv(n) <= (kappa/4)(1/n) + O(1/n^2) = O(1/n)` with **leading rational constant
> `c_1 = kappa/4 = 3/8`**.

**Honest status of the hypothesis.** Neither one-sided bound is proved. Both are
*drift-type* (`1/n`) statements, and they inherit exactly the difficulty (R-a)
identified: the certified box gives only constant lower bounds on log-ratios, not
`1/n` ones — the sandwich's content is genuinely new, not a repackaging of the box. The
**natural proof handle is a quantitative no-spike tower**: the predecessor's no-spike
hierarchy (`ns(Delta), ns^2(Delta), ...`, entrywise nonnegative at every level tested)
is a *sign* statement; a **quantitative** bound on its second application would pin
`D2_i >= -kappa/n` directly. This quantification is not carried out here — it is the
single most promising open sub-problem this packet identifies, since it would close
(R-b) non-circularly and without any Edgeworth-type input. **Label**: the two
constants `c_0 = 5/8`, `kappa = 3/2` are COMPUTED (measured `kappa_hat approx 1.442`,
`c_0 approx beta approx 0.619`, both comfortably inside the stated rationals); Lemma
C2 is PROVED *given* the sandwich; the sandwich itself is CONJECTURAL (unproved, no
counterexample found either).

### 8.3 (R-c) The single-branch Edgeworth-1 curvature lemma — open strengthening, not needed

> **Residual Lemma (curvature-uniformity).** `Curv(n) = O(1/n^2)` — the kernel-smoothing
> factor `(K_d * c)_i / c_i` is index-uniform over the operative window to *second*
> order, not merely bounded.

This is the sharp form: with `l_i = log rc_i`, the exact-Gaussian profile has `l_i -
l_{i-1}` constant in `i`, so `Curv`'s leading term vanishes identically and only the
`O(1/n^2)` deviation from Gaussian survives — this is genuine Edgeworth content, but a
**single-branch, single-level** statement about one convolution, not the coupled
two-branch remainder a naive approach to (PROP-TAIL) would otherwise require. If
proved, it gives the **explained constant** `B_crv/(1-theta*) = 185/0.657 = 282`,
matching the independently-measured `V_17(n)*n^2` almost exactly (Section 7.1) — i.e.
the `C/n^2` law with a constant that is a fixed-point balance, not a fit. **Label**:
CONDITIONAL / CONJECTURAL — not attempted beyond the identification of its exact scope
(a relative-`O(1/n^2)` Edgeworth expansion of a single convolution, uniform in `i` over
a fixed window) in this packet.

### 8.4 Computed clauses (the remaining computed inputs to the certified chain)

The discharge is a certified-census theorem **modulo** the following four computed
inputs. Each is monitored by a named gate; none is a proof valid for all `n`. Their
existence is exactly why the STATUS is **CONDITIONAL** rather than PROVED (PROVED would
require zero computed clauses, which (LAM-BOX) alone precludes).

**(LAM-BOX) — the sibling-proportionality magnitude box.**
- *Asserts*: both load-bearing gates box-max the seminorm/forcing over a fixed magnitude
  box — `lam in [0.72, 0.95]`, `Lambda^+ in [-1.16, -0.82]`, `Lambda^- in [-0.66, -0.35]`
  — which is a **measured + padded** range, not a proved interval.
- *Gate*: MAG-BOX verifies that the realized `lam`, `Lambda^+`, `Lambda^-`, and the
  per-entry ratios `rho_i = c^+_i/c^-_i` lie inside that box at every grid level.
- *Evidence*: realized `lam in [0.7759, 0.9190]`, `Lambda^+ in [-1.1429, -0.8883]`,
  `Lambda^- in [-0.6334, -0.3788]`, per-entry `rho_i in [0.7734, 0.9259]` — all inside
  the computed boxes; worst headroom `0.0172` (the `Lambda^+` floor, thin, ~1.5%).
- *Upgrade*: a proved interval for `lam`/`Lambda^pm` from the exact mass recursion plus
  explicit `a'(t)` bounds.

**(SIB-BAND) — the forced-proportional surrogate vs the real cascade.**
- *Asserts*: the load-bearing gates certify the **forced-proportional surrogate**
  `c^+ = lam c^-`; the real cascade is non-proportional (`c^+_i = lam w_i c^-_i` by the
  IH `rho_prop <= R*`, per-entry sibling wobble `w_i in [1/R*, R*]`).
- *Gate*: SIB-BAND prints the wobble-extended censuses.
- *Evidence (the gap, stated honestly)*: at the shipped anchor `(500, 99/100)`, the
  wobble-extended forcing `F_box_wob = 0.0571211` **EXCEEDS** the threshold `0.0280937`
  by **103.3%** — the extension does **NOT** close. The tighter, still-sound
  geometric-center band `[1/sqrt R*, sqrt R*]` narrows the gap but also misses at feasible
  depth: at `(500, 99/100)` it gives `F_box_wob = 0.0417911` (miss by 43%), clearing only
  at a much deeper base (`J0 >= 800`, pad `999/1000`, +4.6% — build cost ~240s, beyond
  this packet's certified grid depth). The full `[1/R*, R*]` band cannot clear at **any**
  depth (its ratio-box-collapsed deep-base limit `F_box = 0.0321` already exceeds the
  threshold ~`0.028`).
- *Upgrade*: certify the wobble-extended census at a deep enough base, or a
  stated-modulus Lipschitz bound of the real-vs-proportional discrepancy absorbed by the
  box-sup slack.

**(FOLD) — the 57/50 child-window fold.**
- *Asserts*: the Window Lemma (W1) fold factor `spread_{i<18}/spread_{i<17} <= 57/50`.
- *Gate*: V16b (grid-measured; measured max `1.1322` at `n=48`, decreasing).
- *Evidence*: `sup_{n,t}` over the finite grid plus a COMPUTED CLT quadratic-profile
  ansatz; not proved for all `n`.
- *Upgrade*: a proved uniform bound on `spread_{i<18}/spread_{i<17}`.

**(FLOOR-PERSIST) — floor persistence for `n > 500`.**
- *Asserts*: the level-500 floors persist for all `n > 500`.
- *Gate*: composed from the predecessor packet's monotone-drift machinery at the
  re-anchored `(500, 99/100)` floors (F3 re-certifies the floors AT the base).
- *Evidence*: COMPUTED in the predecessor packet and imported here (`rc_i` drifts upward
  in `n`).
- *Upgrade*: a self-contained persistence proof at the deep anchor.

## 9. ROUTE-CUT RESULTS (valuable negatives)

Four routes were tested and are now closed with quantified margins — recording them
prevents re-litigating dead ends.

**(i) The rate-free equilibrium bound at a base `<= 100`, on the certified corner
family, is REFUTED.** The natural "no decay needed" route bounds the source term
`s(t)` (share-variation + a'-source) by its value over the *whole* certified band,
rather than at the realized trajectory. That band-wide census — filtered by the
`rho_prop <= TARGET` constraint (the load-bearing restriction: without it the source
inflates further) — realizes `BAND s_sup approx 0.2886`, against a `0.10` ceiling: a
route-breaking miss. Because the band is **level-independent** (its value does not
depend on `n`) while the *realized* trajectory keeps shrinking, the **inflation factor
grows with `n`**: `4.76x` at `n = 60`, worsening to `13.34x` at `n = 100`. This is
reproduced as an explicit negative control by gate V17's informational sub-check
(Section 11).

**(ii) The whole-map empirical contraction ratio is CIRCULAR for an equilibrium
argument.** Fitting `spread(n+1) approx theta_emp(n) spread(n) + s_emp(n)` directly
to the raw sibling spread sequence gives a clean law `theta_emp(n) approx 1 -
2.98/n` — drifting to 1, the *same functional shape* as the (separately, already-known)
refuted full-profile contraction. Since `spread(n) -> 0` regardless of which fixed
`theta < 1` one substitutes, "find a fixed `theta_win` with the residual `s(n)`
bounded" is numerically easy for *essentially any* `theta_win < 1` sampled against this
drifting empirical fit — it demonstrates nothing about the true one-step map. The
content has to come from a **structural** contraction argument on a *fixed-size*
channel (Sections 4-5's `theta~`/`theta_tot`, genuinely flat, not curve-fit), not from
fitting the raw drifting recursion.

**(iii) The naive `(1/3)`-bridge form of Lemma 1 misses the discharge target by
`3.8%`, and the "certifiable-without-integral" sharp variant is a dead end.** Using
`(1/3) V_17(60)` directly as the equilibrium ceiling gives `0.0262`, against the target
`log(1.02560749) = 0.02528` — a miss. A natural attempt to tighten this *without*
computing an integral — replacing `sup_tau` over the full domain by the local sup over
just `[t_-, t_+]`, paired with the sharp gap `(2t/3)` rather than the loose `1/3` — is
numerically **IDENTICAL** to the loose `(1/3) V_17(n)` bound (ratio `1.0000` at every
tested level): at the binding locus `t = 1/2`, `[t_-,t_+]` *is* the full domain, so the
"sharp, no-integral" variant provides no tightening at all. Only the **true weighted
integral** (the `w(n) approx 0.61` bridge weight, gate V19) recovers the tighter bound
— and it is informational/alpha-only here (Section 7.2), since the beta spine
(Section 7) closes via decay, not via this tighter constant.

**(iv) A shared box parameter must be held fixed across a composite object's
sub-terms.** `lam` (the sibling-proportionality scalar, Section 5) is *one shared* box
variable, not a per-matrix-entry one. Extremizing `lam` separately for each entry of
each row (a valid marginal bound, in the same style V17-IA's own per-index marginal
bounding uses) and combining the results can combine entries at `lam` values no single
box point realizes *simultaneously*, inflating the certified `theta_band`. The lam-minced
census (Section 5) instead respects the shared-`lam` constraint — every entry in a given
panel evaluation shares one `lam` sub-interval, and each Möbius-in-`lam` entry is hulled
over that panel — so a single-panel, per-entry-independent-`lam` bound is strictly
looser. Recorded because the "independently extremize a shared parameter per sub-object"
pattern is easy to reach for by default in this style of certificate and is not
automatically wrong (V17-IA's own per-index `P_i` marginal bounding is a legitimate use
of the same pattern) — it is specifically wrong to do it with a variable, like `lam`,
that a single composite object (the seminorm over a *pair* of rows) must hold fixed
across all of its own sub-terms.

## 10. CORRECTIONS (house discipline)

Plain statements of drift/error found and fixed against earlier material that
fed into this packet.

- The child log-derivative profile is `mu_k propto (2k+1)`, **not** `(k+1)` — an
  earlier window-growth constant used the wrong profile exponent (Section 6,
  Lemma W1).
- The honest child-read window for the one-step contraction census is `i < 18`, **not**
  `i < 19` — an earlier window was one index wider than the tridiagonal
  read-set requires (safe, but loose; corrected in Lemma W1/W2).
- The `C(I0)/j^2` law's "stable to 3 digits" characterization holds **only for `j <=
  64`**: extended to `j = 200` on a deep grid, all four tested window constants
  (`I0 = 4,8,12,17`) drift **down** by `1.4%-3.6%`, stable to only ~1-2 digits over
  that range — a real, if benign (decay if anything slightly faster than a fixed-`C`
  law predicts), scoping correction to an earlier "stable to 3 digits" claim.
- A claim that "`Curv = O(1/n)` from caps/floors/LC alone (no Gaussian cancellation),
  constant `~16 beta`" is **INCORRECT as stated**. That derivation silently imports the
  drift formula `rc_i approx 1 - (2i+1)beta/n` (itself only COMPUTED, a fitted CLT
  law) to get the `1/n` spread of `rc_i` across the window. **From caps/floors/LC
  alone, the certified bound is a CONSTANT** (Section 8.1's Lemma C1/normal form), not
  `O(1/n)` — the box has no mechanism to shrink with `n` on its own. This correction is
  the substance of Section 8.1's honest miss-by-3.9x finding: there is no free `O(1/n)`
  bound sitting in the caps/floors box waiting to be extracted.
- The `--fallback` flag switches the whole triple atomically to a **legacy,
  informational** alternative chain `(J0 = 430, f = 49/50, theta* = 1/2 fixed)`; it is
  not part of the certified primary claim.

**Precision note on the predecessor's V12 (#885)**: the predecessor's corner census
certifies its **cap** and **floor** clauses by a genuine corner-sufficiency theorem
(each is a single output ratio, or its offset by a constant, hence a Möbius function of
each input ratio, extremal at box corners — a proved reduction). Its **output-LC**
clause (`r'_i - r'_{i+1} >= 0`, a *difference* of two output ratios with *different
denominators*) is **not** covered by that theorem: as a function of a single input
ratio it is a degree-`(2,2)` rational, not Möbius, and need not be monotone on the box.
The predecessor's output-LC check is therefore **corner-sampled, empirically clean —
not corner-proved**. This is exactly the same structural boundary Section 5 documents
for the tangent seminorm's profile direction. **Impact, stated honestly**: this does
not touch the predecessor's cap/floor clauses (still corner-proved) or any of its
gated numeric outcomes — this reading is consistent with the predecessor's `-1e-6`
output-LC tolerance, which never binds (its measured margin `-1.4e-8` sits well inside
it), and no gate's PASS/FAIL changes under this reading. This note documents the
precision gap for the record; it is not a retraction of any shipped claim.

## 11. Verifier map

`experimental/scripts/verify_dense_shell_prop_tail_reduction.py`. **The default run IS
the discharge**: base anchor `J0* = 500`, pad `f* = 99/100`. Flags: `--quick` (dev
subset, shallow `J0 <= 200` — not a certified claim at that depth; V17-IA expectedly
misses at the shallow anchor), `--table` (per-level `rho`/`V_17` table), `--fallback`
(legacy informational alternative chain `(J0 = 430, f = 49/50, theta* = 1/2 fixed)`, not
part of the certified claim), and `--tamper-selftest`. **8 core gates determine the
RESULT**; 4 informational gates plus the SIB-BAND gap gate are printed, not counted
(SIB-BAND is deliberately marked FAIL to keep the surrogate-vs-real gap visible). Every
gate's message states its operative index window. The full run measures **~165s** (8/8
core PASS).

- **F3 FLOORS** [core]. Re-certifies the floor family `r_i(J0*, t)` over the 41-parent
  grid, `i < 18`: positivity, LC-compatibility (non-increasing + floor `<=` actual `<=`
  cap), and the `i=0` b-vs-c halving-convention cross-check. The base-anchor
  certificate F3/MAG-BOX/V15-IA/V17-IA all consume. All checks PASS at `J0*=500,
  f*=99/100` (0 violations).
- **MAG-BOX** [core, **verifies computed clause (LAM-BOX)**]. Verifies that the realized
  sibling-proportionality magnitudes lie inside the COMPUTED magnitude box that both
  load-bearing gates box-max over (`lam in [0.72, 0.95]`, `Lambda^+ in [-1.16, -0.82]`,
  `Lambda^- in [-0.66, -0.35]`): realized `lam in [0.7759, 0.9190]`, `Lambda^+ in
  [-1.1429, -0.8883]`, `Lambda^- in [-0.6334, -0.3788]`, per-entry `rho_i = c^+_i/c^-_i
  in [0.7734, 0.9259]`, all inside the boxes at every grid level. Worst headroom `0.0172`
  (the `Lambda^+` floor, thin, ~1.5%). See Section 8.4 (LAM-BOX).
- **V15-IA THETA-BAND** [core, **load-bearing**]. The certified band-uniform enclosure of
  the Lemma A1 tangent seminorm (Section 5) over the *entire* certified LC ratio box, not
  the realized profile or a tested grid, folded by the certified Window Lemma factor
  `<=57/50`. The seminorm is a sum of `|differences of Möbius functions with different
  denominators|`, so it is **not** Möbius in `lam` and can attain an interior-`lam`
  maximum; the gate is therefore a **lam-minced rigorous enclosure** (`LAM_MINCE = 24`
  panels — mince `lam`, hull each Möbius-in-`lam` entry per panel, outer max over panels),
  **not** an endpoint-in-`lam` sufficiency claim. Certified `theta_band = 0.6020244`
  (exact Fraction `1505061/2500000`) — comfortably inside its own unconditional sanity
  ceiling `9/10`. This value is passed directly to gate V17-IA as `theta_star`; the two
  gates are chained, not independent checks of a shared fixed constant.
- **V16 THETASYMB** [core]. The exact Fraction polynomial identity of Lemma 3 plus the
  domain sign argument. `decide`-friendly (rational coefficients); no tamper.
- **V16b WINDOW** [core]. Lemma W1's asymptotic fact `289/256 <= 57/50` (exact
  rational), the grid check `sup spread_{i<18}(L)/spread_{i<17}(L) <= 57/50` (measured
  `1.1322` at `n=48`), and Lemma W2's structural read-set check.
- **V17 FORCING** [core]. `F_ext(n)*n^2` and `Curv(n)*n^2` bounded `<= 200` at the edge
  locus (measured worst `187.83` / `109.09`). Its message also reports, inline and
  **INFORMATIONAL**, the G2/alpha route-cut negative control of Section 9(i): the
  rho_prop-constrained band census, confirmed to **exceed** a `0.10` ceiling (`0.2886`).
- **V17-IA FORCING** [core, **load-bearing**]. The minced interval-arithmetic census of
  `F_box(J0*, f*) <= (1-theta_band)*tau*`: an exact-Fraction, width-2-locality enclosure
  (every index `i=0..16`'s marginal range, not only the two endpoints), box-maxed over
  the sibling-proportionality magnitude parameters (the forced-proportional surrogate).
  Certified `F_box(500, 99/100) = 0.02687612` vs threshold `(1-theta_band)*tau* =
  0.03018857` — **11.0% margin, PASS**. `tau*` enters as the exact-Fraction lower bound
  `TAU_STAR_FR = 0.075855330599169 (<= 3 log(TARGET))`, and the final PASS/FAIL
  comparison is exact Fraction. The gate also prints the equilibrium chain
  (`F_box/(1-theta_band) = 0.06753207 <= tau* = 0.07585533`; `(1/3)* = 0.02251069 <=
  log(TARGET) = 0.02528511`; `exp = 1.022766 <= TARGET = 1.02560749`), the locus, and the
  documented outward slop (`1e-9`, six orders of magnitude past the cascade's own
  floating-point precision).
- **V18 VTRACK** [core]. The deep-grid `rho_prop@i<17(n) <= 1.02560749` over
  `n in {48,...,500}` (18 levels, including the `340/400/430/450/500` deep tail),
  monotone non-increasing, the `V_17(n)` values at every tested level (`0.1236` at
  `n=48` down to `0.00112` at `n=500`), the `tau*` crossover (confirmed `n=62`), and an
  explicit base-coverage check (`max(grid) >= expect_max`). The `--table` flag prints the
  full per-level `rho`/`V_17` table.
- **V15-GRID THETA** [informational]. `theta_tot <= 1/2` and `theta_win <= 27/100`, grid
  census over 41 parents to `n = 500`; plus the closed-form tangent seminorm `N_free <=
  0.9` (Lemma A1, evaluated at realized profiles only). Measured worst: `theta_tot =
  0.3766`, `theta_win = 0.2032`, `N_free = 0.4974` — a robustness cross-check, comfortably
  inside the certified `theta_band`, not part of the certified chain.
- **V15-CERT** [informational, grid-sampled cross-ref]. A grid-sampled tangent-seminorm
  cross-reference `theta_cert := N_free * (57/50 window fold) ~= 0.567` — a grid-sampled
  (not band-uniform) view, retained as a cross-check against the band-uniform V15-IA
  enclosure.
- **V17-INFO** [informational]. The G2/alpha route-cut negative control (see V17
  above).
- **V19 BRIDGE** [informational/alpha-only]. `w(n) <= 0.62` (measured worst `0.6115`).
  Not part of the RESULT tally: the shipped equilibrium chain never uses the tight
  integral bridge, only the loose `(1/3)` form plus the certified constant forcing.
- **SIB-BAND** [informational gap gate — **marked FAIL to keep the gap visible; verifies
  computed clause (SIB-BAND)**]. Prints the wobble-extended censuses at the shipped
  anchor (per-entry sibling wobble `w_i in [1/R*, R*]`): `theta_band_wob = 0.629641`,
  `F_box_wob = 0.0571211` vs threshold `0.0280937` — the extended forcing **EXCEEDS** the
  threshold by **103.3%**, so the extension does **NOT** close. The tighter, still-sound
  geometric-center band `[1/sqrt R*, sqrt R*]` gives `F_box_wob = 0.0417911` (miss by 43%)
  at `(500, 99/100)`, clearing only at `J0 >= 800` / pad `999/1000` / +4.6% (beyond this
  packet's certified grid depth); the full `[1/R*, R*]` band cannot clear at any depth
  (deep-base limit `F_box = 0.0321 > ~0.028`). Deliberately marked **FAIL** so the
  surrogate-vs-real gap stays visible. See Section 8.4 (SIB-BAND).

Tamper suite (13, each isolated to one report/info line): `f3-corrupt` (F3 — a `>1` pad
breaks the floor-`<=`-actual ordering), `magbox-shrink` (**MAG-BOX** — shrinks the
magnitude box so a realized `lam`/`Lambda^pm`/`rho_i` falls outside, flipping MAG-BOX to
FAIL), `theta-tot-gate` (`V15-GRID`, informational), `nfree-corrupt` (`V15-GRID` seminorm
corruption, informational), `theta-ia-tighten` (grazes gate V15-IA's own sanity ceiling
from `9/10` to `1/2`, isolated: the certified `theta_band` value itself, and hence gate
V17-IA's downstream line, is untouched), `theta-ia-sign` (**V15-IA** — flips the seminorm
enclosure's `max -> min` direction, caught by a realized-seminorm floor consistency check;
isolated because a *lower* `theta_band` only relaxes V17-IA, so the sign error cannot
silently pass through the load-bearing chain), `window-bound` (V16b), `forcing-bound`
(V17), `v17ia-graze` (V17-IA threshold graze — shrinks the threshold `20%`, flipping the
margin PASS to FAIL), `c1-target` (V18), `vtrack-level-drop` (V18 deep-level corruption —
drops the grid's top level, caught by the base-coverage check), `g2-ceiling` (the V17
informational sub-check — honest substitute), `bridge-w-gate` (V19, informational). All 13
confirmed isolated to their own line at full (`J0*=500`) depth; no other gate's outcome
changes under any tamper.

**Lean layer**: `experimental/lean/prop_tail_reduction/` — a statement-level companion
package (stdlib-only, no mathlib, no `sorry`, `decide`-only kernel checks, builds
clean). Scope, exactly: (1) Lemma 3's ring identity `75(1-x^2)-(6+3x)^2 =
-3(2x-1)(14x+13)` on `Int` coefficient lists, plus a denominator-cleared sign
corollary (`x = p/q`) certifying the polynomial inequality `theta~ <= 1/5` reduces to
*post-squaring* — the trig substitution `x = cos(2 pi t/3)` and the squaring step
itself stay informal/analytic; (2) Lemma W1's rational fact `289*50 <= 57*256` (i.e.
`289/256 <= 57/50`); (3) the deep-grid `rho_prop@i<17(j)` table and the `V_17` vs.
`tau*` crossover-at-`n=62` table, both transcribed from this packet's printed decimals
to exact rationals at printed precision, with threshold + strict-monotonicity checks
on the transcribed table itself (not a re-derivation of the underlying floating-point
computation). Everything else in this note — Lemma 1's reduction, Lemma 2's cascade,
Lemma A1's tangent seminorm (including the band-uniform enclosure, gate V15-IA), Lemma
W2's read-set argument, the composed theorem, and the residual ladder's strengthenings
(R-b/R-c) — stays informal by design; the Lean package does not claim otherwise.

**New socket for the statement layer (this packet, not built here).** The discharge's
own arithmetic (Section 0/8.1) is entirely rational comparisons once the certified
values are printed: `F_box`'s numerator vs the threshold `(1-theta_band)*tau*`'s
numerator (both exact Fractions, gates V15-IA/V17-IA), `2*F_box` vs `tau*` (the
equilibrium-ceiling check), and the grid-500 `rho_prop`/`V_17` table (an extension, by 6
rows, of the same transcribed-table pattern (3) already uses). A sibling may extend the
Lean package with these as additional `decide`-checkable rational facts — `theta_band` is
itself an exact Fraction (`1505061/2500000`) and would transcribe the same way as the
other rational facts here; none of that is attempted in this packet.

## 12. (PROP-TAIL) consumer framing

**Scope.** This section, and this packet generally, concerns only this repository's
experimental-profile-ledger track: #880's `|K| = 1` dense-shell class-sum dichotomy and
#885's INV-TAIL closure chain. It makes no claim about, and is not on the critical path
of, any separately submitted manuscript's conditionals — those are a distinct
obligation, out of scope here.

**What #885/#880 gain now.** Before this packet, (PROP-TAIL) was a single opaque
numeric persistence claim: "the measured monotone decay of a cross-index spread,
certified on a grid to `n = 60`, continues." This packet first reduced that scalar to a
certified structural frame — an exact reduction (Lemma 1) that removes the two-branch
coupling from the target; an exact spectral gap (Lemma 3, `theta~ <= 1/5`, closed
form); a certified one-step recursion with an exact tangent-direction seminorm
(Lemma A1) and a corrected window bookkeeping (Lemmas W1-W3); a composed joint
induction (Section 7) — and then **closed it** as a certified-census theorem MODULO the
enumerated computed clauses (Section 8.4): the deep-base equilibrium route (R-a, Section
8.1) clears the arithmetic slot on finite checks, certified by an exact-Fraction,
lam-minced interval-arithmetic census of the tangent seminorm (gate V15-IA) feeding an
exact-Fraction minced interval-arithmetic forcing census (gate V17-IA) at a re-certified
floor family (gate F3, magnitude box verified by MAG-BOX) with full base coverage to
`n = 500` (gate V18). **(PROP-TAIL) is DISCHARGED as a certified-census theorem MODULO
the enumerated computed clauses (LAM-BOX, SIB-BAND, FOLD, FLOOR-PERSIST; Section 8.4) —
STATUS CONDITIONAL**, given this packet's own certified gate set
(F3/MAG-BOX/V15-IA/V16/V16b/V17/V17-IA/V18). The two load-bearing gates certify the
forced-proportional surrogate `c^+ = lam c^-`.

**What #885/#880 gain now, concretely.** #885's own (PROP-TAIL) conditional is **closed
modulo the Section 8.4 computed clauses** by this packet's certificates. #885's INV-TAIL
closure chain therefore becomes **unconditional at every `B` modulo those computed
clauses** on this repository's experimental-ledger track, and with it #880's `|K| = 1`
dense-shell class-sum dichotomy becomes **unconditional at every `B` modulo those
clauses**, given this packet's green certificates together with #885's own certified
chain. The two open items (R-b's sandwich, R-c's sharp Edgeworth-1 lemma) are
**strengthenings** toward the sharp `C/n^2` law, not obligations the discharge itself
carries — they remain independently attackable future work (Section 8.2-8.3), and the
mu-sign tightener (Section 0, Section 8.1's honesty note) is a recorded NEGATIVE (does
not carry as a clean finite corner check) that the discharge does not need. General `K`
remains conjectural and unaffected by this packet (unchanged from the predecessor).
