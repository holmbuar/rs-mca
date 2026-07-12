# Lower reserve, deep-remainder wall: the partial-occupancy atlas is built and decides negative

**Hard input:** 5 (lower reserve / unsafe-side comparison).

**Status:** `CONDITIONAL` (deep-remainder **field-drop route DECIDED-NEGATIVE**;
the wall is **load-bearing but empty**, blocker pinned). Finer labels: the
occupancy-atlas exhaustion, the constant-summand factorization, the degree-`c`
interlace identity, and the clean-slot characterization are **PROVED**; the
full-field alphabet fill and the per-instance domination are **PROVED-AT-TOYS**;
the exponential no-strengthening verdict is **CONDITIONAL** on
`prop:prefix-rigidity-full` (L2044) bounding non-field-drop concentration at
`e^{o(n)}` and on the prefix-fiber / field-drop framework of L6197; the
instance-level no-list clause is **REFUTED by #714** (label-factoring route,
independently verified) — Theorem DR, the atlas, and the field-drop closure
stand; the "O5c closes as a list problem" corollary is **WITHDRAWN**.

**Verdict.** PR **#699** paid route **O5c** for the quotient, Euclidean-remainder
(`w >= r`, `r < c`) and Chebyshev profile classes, and localised the ONE
remaining wall — the deep-remainder regime `w < r` — to a missing
"partial-occupancy atlas at the degree-`c` interlace" of
`prop:complete-support-factorization` (L3591--3594, named at L6325--6328). This
note **builds that atlas** and **decides it negative**: the atlas exists and
exhausts, but the per-cell fiber sum **provably cannot** be routed through the
collision-aware pole with a field drop, because in the deep regime **no depth-`w`
prefix slot is field-drop-clean**. Consequently **the field-drop route
cannot make any deep-remainder profile-list larger than the identity list**;
the object that blocks that route is the full-field remainder coefficient
`p_{jc}(R)` sitting additively in every quotient slot. **Correction (same
evening):** field-drop is not the only route — DannyExperiments' **#714**
exhibits a verified reciprocal-locator factorization (fixed remainder labels
cancel from the image-normalized average) whose pigeonhole beats the identity
floor inside a strictly deep cell (guaranteed list `6` vs identity floor `1`
over `F_169`).  The unconditional instance-level form of the old verdict is
therefore **REFUTED as printed** and the deep-remainder side **reopens as
payable** — see the Correction section below.

Target: `experimental/asymptotic_rs_mca_frontiers.tex` (read at `ea4eb07`).
Attacks the deep-remainder residual of route **O5c** of hard input 5, scoped by
the coverage audit **#693** (`lower_reserve_unsafe_side_coverage_audit.md`,
sections 3--4) and the wall localisation of **#699**
(`lower_reserve_o5c_profile_lists.md`, section 5).

**Consumes (never attacks or extends):**
- **#699** — `lower_reserve_o5c_profile_lists.md`: the O5c payment for the
  quotient / Euclidean-remainder / Chebyshev classes, the QR4 varying-summand
  observation (its G7), and the wall localisation discharged here.
- **#693** — lower-reserve / unsafe-side route audit: the O5c/O7 decomposition
  and the "any larger ... remainder-profile list" open statement.

Also consumes the in-paper theorems `prop:simple-pole-lower` (L6180),
`thm:collision-aware-pole` (4.2, L1997), `prop:exact-prefix-list` (4.1, L1965),
`prop:prefix-rigidity-full` (4.4, L2044),
`thm:exact-quotient-remainder-normal-form` (QR2/QR4, L3456),
`prop:complete-support-factorization` (L3577), and
`thm:exact-partial-occupancy` (PO1/PO2, L3608).

**Verifier:** `experimental/scripts/verify_lower_reserve_deep_remainder.py`
-> `RESULT: PASS 39/39` (`--check`), `RESULT: PASS 8/8` (`--tamper-selftest`),
~0.05 s, python3 stdlib only. It exhaustively recomputes the occupancy atlas over
`F_25` (square fold, `c=2`) and `F_13` (cube fold, `c=3`), the degree-`c`
interlace and the field-drop alphabet contrast over `F_25`, and the domination
numerics over `F_169`, and writes a JSON certificate to
`experimental/data/certificates/lower-reserve-deep-remainder/`.

---

## 1. The obligation, and what a partial-occupancy atlas must provide

`prop:simple-pole-lower` ("Exact unsafe test", L6180) certifies `a_n` unsafe from
any list of `L` distinct dimension-`(k_n+1)` codewords agreeing on `>= a_n`
points, via the collision-aware pole `M(L)` (4.2) and the challenge average
`P = ceil((|Gamma_n|/q_n) M(L))` (L6201--6208). Its last sentence (L6196--6198)
allows `L_n` "replaced by any larger identity, quotient, Chebyshev, or
remainder-profile list proved for the dimension-`(k_n+1)` code."

**The list is a prefix fiber** (`prop:exact-prefix-list`, 4.1): for a prefix value
`z in B_n^w` (`w = a_n - k_n - 1`), the codewords agreeing with `U_z` on `>= a_n`
points are **exactly** `{U_z - Q_S : pref_w(Q_S) = z}`. So a profile-list of proved
size `>= L` is a pigeonhole `max_z #{S in profile : pref_w(Q_S) = z} >= L`. To beat
the identity floor `L_id = ceil(binom(n,a) |B|^{-w})` the pigeonhole must run over
a **smaller alphabet than `B^w`** — this is the **field drop**: the quotient
profile pigeonholes the depth-`d` quotient coefficients `v_1(E),...,v_d(E) in
eta^j B_phi` (a proper subfield coset), giving `L_quot = ceil(binom(N-|phi(R)|,m)
|B_phi|^{-d})`, `N = n/c`, `m = (a-r)/c`, `d = floor(w/c)`.

**The deep-remainder wall** (`w < r`, `#699` section 5). By QR2(ii) (QR4,
L3513--3520), the prefix fiber count becomes a **sum**
`sum_{R : pref_w(P_R) = T^{-1}(z)} binom(N-|phi(R)|, m)`, whose summands differ
with `|phi(R)|` (`#699` G7: `binom(12-|phi(R)|,4) in {495, 330, 210}`). There is
no single `L_quot` to pigeonhole. The obstruction named at L3591--3594 is the
**degree-`c` interlace**: once `|R| >= c`, the remainder coefficient `p_c(R)` and
the quotient coefficient `v_1(E)` collide at degree `c`, so the triangular
recovery of QR2(i) is lost.

**Stated exactly, a partial-occupancy atlas for this obligation must supply:**
1. **Cells.** A finite decomposition of the deep-remainder `a_n`-supports indexed
   by an occupancy pattern (which `phi`-fibers are complete, which are partially
   hit, by how much).
2. **Index set.** A reorganisation of the QR4 sum `sum_R binom(N-|phi(R)|,m)` in
   which the summand is **constant** on each cell (so it factors out of the
   fiber count).
3. **Per-cell inequality.** For each cell, a lower bound on the largest depth-`w`
   prefix fiber inside the cell that **runs over a subfield alphabet** (carries a
   field drop), so that it converts through the collision-aware pole the way
   `#699`'s single-pigeonhole quotient list did.
4. **Exhaustion.** A proof the cells tile `binom(D_n, a_n)`.

Requirements 1, 2, 4 are met by the atlas below. Requirement **3 provably
cannot be met** in the deep regime; that is the decision.

---

## 2. The atlas, BUILT: occupancy cells, exhaustion, and the constant summand

The cell index is exactly `thm:exact-partial-occupancy` (PO1/PO2, L3608--3644).
With `D = D_0 sqcup X`, `|X| = b`, `phi : D_0 ->> Q` of complete fibers of size
`c`, `N = |Q|`, the occupancy of `S subseteq D` is
`lambda_phi(S) = (t, m, p, r)`: `t = |S cap X|` exceptional points, `m` complete
fibers, `p` partially-hit fibers, `r` selected points in those partial fibers.

**Proposition A (exhaustion; PROVED, verbatim PO1/PO2).** The cells
`Omega_{t,m,p,r}` partition `binom(D, a)`, with exact count
`|Omega_{t,m,p,r}| = binom(b,t) binom(N,p) binom(N-p,m) [x^r]((1+x)^c - 1 - x^c)^p`
and add-back `sum_{t+cm+r=a} |Omega_{t,m,p,r}| = binom(b+cN, a)`.

*Verified exhaustively* (verifier group A): over `F_25` (square fold, `c=2`,
`b=0`, `N=4`, so `(1+x)^2-1-x^2 = 2x`) PO1 is exact on every cell and PO2 holds
for `a = 0..8`; the `a=4` partition is `(0,0,4,4)->16`, `(0,1,2,2)->48`,
`(0,2,0,0)->6`, summing to `70 = binom(8,4)`. Over `F_13` (cube fold, `c=3`,
`N=4`, `(1+x)^3-1-x^3 = 3x(1+x)`) PO1/PO2 hold for `a = 0..7`, exercising the
`p < r` cells (a partial fiber may hold `2` of `3` points) that `c=2` never
produces.

**Proposition B (constant summand; PROVED).** For every `S in Omega_{t,m,p,r}`,
the partial part `R(S)` has `|phi(R(S))| = p`, a cell constant. Hence the QR4 sum,
restricted to one cell, has a **single** summand and factors:
```text
  #{S in Omega_{t,m,p,r} : pref_w(Q_S) = z}
     = binom(N - p, m) * #{R in cell : pref_w(P_R) = T^{-1}(z)}.
```

*Proof.* A fiber lies in `E(S)` iff all `c` of its points are in `S`; the partial
fibers are exactly the `p` fibers meeting `R(S)`, so `|phi(R(S))| = p` by
definition of the cell. Fixing the partial-fiber set fixes `phi(R)`, hence
`E in binom(Q setminus phi(R), m)` ranges over `binom(N-p, m)` sets independently
of `R`; this is the QR4 count with `|phi(R)| = p` frozen. `QED`

This **resolves the varying-summand difficulty** `#699` flagged: the three values
`binom(12-|phi(R)|,4) in {495, 330, 210}` are three **different cells**
(`p in {0,1,2}`), not three terms of one prefix fiber. Within a cell the summand
is one number. (Verifier group B reproduces `[495, 330, 210]` and confirms
`|phi(R)| = p = 2` is constant across all 48 supports of the `F_25` cell
`(0,1,2,2)`.)

So the atlas assembles: cells (Proposition A), a constant per-cell summand
(Proposition B), exhaustion (PO2). What remains is the per-cell field drop —
requirement 3.

---

## 3. The blocker: the degree-`c` interlace and the clean-slot dichotomy

Take reciprocal polynomials (`A^vee(Z) = Z^{deg A} A(Z^{-1})`) and
`Phi(Z) = Z^c phi(Z^{-1})`. The exact identity QR5 (L3536--3541) reads
```text
  Q_S^vee(Z) = P_R^vee(Z) ( Phi(Z)^m + sum_{j=1}^m v_j(E) Z^{cj} Phi(Z)^{m-j} ).
```
A depth-`w` prefix slot at **degree `l`** is *field-drop-clean* when its value is a
quotient coefficient `v_j(E) in eta^j B_phi` (subfield coset) plus terms in
already-cleaned lower slots — i.e. when `l = jc` **and** `deg P_R = r < jc` (no
remainder coefficient reaches degree `jc`). A quotient list gains its drop
precisely from clean slots.

**Lemma I (interlace; PROVED, from QR5).** If `r >= jc` for some `j >= 1` with
`jc <= w`, then the coefficient of `Z^{jc}` in `Q_S^vee` equals
`p_{jc}(R) + f(p_1,...,p_{jc-1}, v_1,...,v_j, Phi)`, where the leading term
`p_{jc}(R)` is a symmetric function of the (arbitrary) partial-fiber points and is
**not confined to any proper subfield coset** of `B`. That slot is therefore a
**full-field** slot: it carries no `B_phi` drop.

**Lemma II (clean-slot dichotomy; PROVED).** A depth-`w` prefix has a
field-drop-clean quotient slot **iff** there exists `j >= 1` with `r < jc <= w`.
Consequently:
```text
  deep regime  w < r  =>  NO field-drop-clean slot exists.
```
*Proof.* A clean slot needs `jc <= w` and `jc > r`, i.e. `r < jc <= w`. If
`w < r` then `jc <= w < r < jc` is impossible for any `j`. Two sub-cases exhaust
the deep regime: if `w < c` (forced when `r < c`) then `floor(w/c) = 0` and the
prefix reaches no quotient coefficient at all; if `w >= c` (which forces `r > c`)
then every quotient slot `jc <= w` has `jc <= w < r = deg P_R`, so Lemma I makes
it full-field. `QED`

**Verified** (verifier groups C, E). Over `F_25`, the degree-`c` prefix slot in
the deep regime **depends on both `R` and `E`**: in the deep cell `(0,1,3,3)`
(`r=3`, `w=2 >= c=2`, one complete fiber `E` plus three partial points `R`),
fixing `E` and varying `R` moves it (`>1` value); in the deep cell `(0,1,2,2)`
(fixing the partial points `R` and varying the complete fiber `E`) it also moves
(`>1` value). No clean separation — the interlace is live in the prefix. In the
clean quotient profile `(0,2,0,0)` the same slot is a pure quotient coefficient. The characterization `has_clean_slot`
has **0** deep-and-clean violations over `c in 2..5`, `r, w in 0..11`; spot
values `has_clean_slot(2,1,2)=True` (Euclidean, `r=1<c=2<=w=2`, PAID),
`has_clean_slot(2,4,2)=False` (deep `w=2<r=4`), `has_clean_slot(3,2,1)=False`
(deep with `d=0`).

The **contrast is the whole story** (verifier group D, `F_25`, `B = F_25`,
`B_phi = F_5`, `lambda_2 = 1/2`): the clean quotient slot takes exactly `5 =
|B_phi|` values and, after descaling by `theta^{-2}`, **descends into `F_5`** (its
second coordinate is `0`) — a genuine field drop. The deep interlaced slot takes
`21` values (full-field scale) and its `theta^{-2}`-image **escapes `F_5`** — the
drop is destroyed.

---

## 4. The decision (CORRECTED by #714, see below): the field-drop route beats nothing

**Theorem DR (deep-remainder domination).** Let `phi : D -> Q` be a `c`-fold
complete-fiber folding (`def:structured-folding`), `B_phi subsetneq B` a proper
scaled quotient coefficient field. Fix an agreement `a = cm + r` with window
`w = a - k - 1` in the **deep regime `w < r`**, and consider the
ranging-remainder profile (`phi`, `c`, `r` fixed; `E` and `R` range). Then, over
every `q = |F| > n` and every `emptyset != Gamma subseteq F`:

1. **[Full effective alphabet]** Every occupied depth-`w` prefix slot is
   full-field (Lemma II), so the profile's prefix image has size
   `|image| = |B|^w (1 - o(1))`. Since the profile is a subfamily of
   `binom(D,a)`, its provable pigeonhole floor is
   `ceil(|profile| / |image|) <= ceil(binom(n,a) / |B|^w) (1 + o(1)) =
   L_id (1 + o(1))`: one cannot *prove* a list larger than identity this way.
2. **[Fixed-`R` alternative]** Freezing `R` restores a clean quotient-prefix
   fiber (drop `|B_phi|^{-d}`, `d = floor(w/c)`) but retains only `binom(N-p,m)`
   codewords, giving floor `ceil(binom(N-p,m) |B_phi|^{-d})`, which in the deep
   window (`m` forced small by `r > w`) is `< L_id`.
3. **[No `|B|^{-w}` from concentration]** The remainder-prefix map
   `R |-> pref_w(P_R)` carries no subfield structure; its fiber concentration is
   bounded by `prop:prefix-rigidity-full` (4.4) at `e^{o(n)}`, which "does not
   supply the random factor `|B|^{-w}`" (L2053--2054).

Consequently the deep-remainder profile-list is `<= L_id (1 + o(1))` on the
exponential scale: **no larger list than identity exists in the deep regime**, so
the "any larger remainder-profile list" clause of L6197 is, for `w < r`, either
vacuous or unpayable by a field drop. The load-bearing blocker is the full-field
coefficient `p_{jc}(R)` (Lemma I).

*Every hypothesis is used:* `w < r` (deep) drives Lemma II; `B_phi subsetneq B`
(positive-rate drop) is what a strengthening would need and what is destroyed;
`q > n` and `Gamma` are the ambient collision-aware-pole hypotheses carried
verbatim from `prop:simple-pole-lower`; the exponential clause of (1)/(3) is
conditional on (4.4) governing non-field-drop concentration.

**Domination numerics** (verifier group F, `F_169` tower, `B_phi = F_13`,
`lambda_2 = 1/2`; deep instance `a=10`, `k=7`, `w=2 < r=4`, `d=1`, `p=r=4`,
`m=3`):
```text
  fixed-R deep floor  = ceil(binom(N-p,m) |B_phi|^{-d}) = ceil(binom(8,3)/13) = 5
  identity floor      = L_id = ceil(binom(24,10)/169^2) = 69
  rigidity 4.4 cap    = binom(24,10)/141 ~ 13909   (NO |B|^{-w} = 169^{-2} factor)
```
The field-drop-preserving list is `5`, dwarfed by `L_id = 69`; the rigidity cap
confirms the actual fiber carries only `e^{o(n)}` packing slack, never the
`|B|^{-w}` the drop would need.

---

## 5. What remains between this packet and O5c fully paid

With `#699` (quotient / Euclidean / Chebyshev) and this note (deep remainder),
the "any larger ... profile list" clause of L6197 is accounted for **across all
regimes** on the field-drop route:

| profile class | regime | O5c status |
|---|---|---|
| identity (O5a) | all | **PAID** (`prop:exact-prefix-list`) |
| quotient / Chebyshev | shallow, positive-rate drop | **PAID** (#699 Lemma O5c-Q) |
| remainder, Euclidean | `w >= r`, `r < c` (clean slot) | **PAID** (#699) |
| remainder, deep | `w < r` (no clean slot) | **DECIDED**: dominated by identity |

The remaining honest gap is **not** a deep-remainder list. It is the possibility,
outside the prefix-fiber / field-drop framework of L6197, of a **non-list**
unsafe mechanism in the deep window that exploits remainder structure by some
route other than a locator-prefix pigeonhole (e.g. a second-moment or
incidence bound in the spirit of the `#693` `D1` corner). Theorem DR closes the
**profile-list** route for `w < r`; a mechanism of a different kind is neither
supplied nor excluded here. Separately, route **O7** stays `OPEN` and remains
list-inaccessible (`#699` K1): the deep-remainder wall is a shallow-window
phenomenon and this note changes neither the O7 band nor any deployed finite row.

**Sharpest remaining statement.** *In the deep window `w < r`, every certified
profile-list (identity, quotient, Chebyshev, remainder) has floor `<= L_id`; the
unsafe test there is the identity test, and any strengthening must come from a
non-prefix-fiber mechanism, whose existence in the interior band is exactly route
O7's open content.*

---

## 6. Per-claim labels

| # | claim | verdict | basis |
|---|---|---|---|
| A1 | occupancy cells `Omega_{t,m,p,r}` exhaust `binom(D,a)`; PO1 exact | **PROVED** | `thm:exact-partial-occupancy`; group A, `F_25`/`F_13` exhaustive |
| A2 | within a cell `|phi(R)| = p` constant, so QR4 factors `binom(N-p,m) * #{R}` | **PROVED** | Proposition B; group B |
| A3 | `#699` G7's three summands `{495,330,210}` are cell mixing, not one fiber | **PROVED** | group B (`binom(12-p,4)`, `p in {0,1,2}`) |
| I1 | degree-`c` interlace: `p_{jc}(R)` sits full-field in every quotient slot with `jc <= w < r` | **PROVED** | Lemma I (QR5); group C |
| I2 | clean slot exists iff `exists j: r < jc <= w`; deep `w < r` => none | **PROVED** | Lemma II; group E (0 violations) |
| D1 | clean quotient slot alphabet `= |B_phi|`, descends into `F_5`; deep slot full-field | **PROVED-AT-TOYS** | group D (`5` vs `21` over `F_25`) |
| D2 | fixed-R deep floor `5 << L_id 69` on `F_169`; field-drop-preserving list is small | **PROVED-AT-TOYS** | group F |
| DR | field-drop route beats nothing (Theorem DR, stands); instance-level no-list clause REFUTED by #714; asymptotic clause OPEN under (4.4)/L6197 | **PARTIALLY REFUTED** | #714 counterexample verified: guaranteed list 6 vs identity floor 1, strict-deep F_169 cell |
| -- | any non-list deep-window mechanism; O7; any safe-side / prize-threshold claim | **OPEN / NOT CLAIMED** | section 5 |

---

## Correction (2026-07-12, same evening — #714)

DannyExperiments' **#714** ("Correct the deep-remainder profile image ledger")
proves, for every nonempty canonical partial-occupancy cell `Omega_{t,m,p,r}`
with `J_{t,p,r}` fixed remainder labels and `d = min(m, floor(w/c))`, the
reciprocal-locator factorization `|Phi_w(Omega_{t,m,p,r})| <= J_{t,p,r} *
|B_phi|^d` — valid at arbitrary remainder degree including the strict-deep
regime `w < r`, because the fixed remainder labels preserve the descended
quotient image and cancel from the image-normalized average.  One prefix fiber
then has size `>= ceil(binom(N-p,m)/|B_phi|^d)`.  Verified instance
(independent rerun at gate): `(n,a,k,w,c,m,p,r) = (24,12,8,3,2,4,4,4)` over
`F_169` — realized image `86,320` (analytic bound `102,960 = 7,920 * 13`),
max fiber `20`, **guaranteed list `6` vs identity floor `1`**.

**What stands:** the partial-occupancy atlas (exhaustion, constant-summand
factorization, degree-`c` interlace), the clean-slot characterization, and
**Theorem DR** — the field-drop conversion remains impossible for `w < r`.
**What is refuted:** this note's printed instance-level verdict ("no
deep-remainder profile-list is larger than the identity list") and its
corollary that O5c closes as a list problem.  **What reopens:** the
deep-remainder side of O5c as a payable route via label factoring; the new
open question is whether the #714 mechanism scales to `e^{Theta(n)}` families
or is capped at `e^{o(n)}` by `prop:prefix-rigidity-full` (L2044) — neither
direction is proved here or in #714 (its own Nonclaims).

Credit: counterexample by **DannyExperiments (#714)**, verified independently
before this correction.

## 7. Nonclaims

This note does **not** claim:
- a deep-remainder profile-list of size `> L_id`, nor that O5c's deep case is
  "paid" in the sense of a new larger list — it is **decided negative**: the
  largest deep-remainder list is the identity list.
- that **no** mechanism can render the deep window unsafe — only that the
  **prefix-fiber / field-drop** route (the content of L6197) cannot, for `w < r`.
  A non-list mechanism is neither built nor refuted.
- any payment of **O7** or of the interior entropy crossing (`#699` section 7
  proves lists cannot reach it; unchanged here).
- any change to a deployed finite row, or to any `M31` / KoalaBear survivor
  count; the finite witnesses are RS toy scales (`F_25`, `F_13`, `F_169`).
- a general-characteristic statement: the alphabet-fill and domination facts are
  `PROVED-AT-TOYS`; the exponential verdict is `CONDITIONAL` on
  `prop:prefix-rigidity-full`.
- any edit to the paper TeX.

---

## 8. Replay

```bash
python3 experimental/scripts/verify_lower_reserve_deep_remainder.py --check
# -> RESULT: PASS 39/39            (~0.05 s, stdlib only; writes JSON certificate)
python3 experimental/scripts/verify_lower_reserve_deep_remainder.py --tamper-selftest
# -> RESULT: PASS 8/8
```
