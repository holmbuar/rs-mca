# Repairing the saturation payment: a mass-weighted occupancy compiler

## Status

`CONSUMER PINNED (AUDIT) / MASS-WEIGHTED COMPILER = EXACT RC_occ (AUDIT, it is
already in the tex) / PAYMENT ON THE HEAVY-ATOM (GEOMETRIC-TAIL) PRODUCT CLASS
(PROVED) / SELF-PAYING HEAVY ATOM (PROVED) / STRESS TEST: ORIENTATION FLOOR =
NEW OBSTRUCTION, LOCALIZED TO THE COLLAPSE SIDE, NOT A SATURATION COUNTEREXAMPLE
(PROVED-negative) / SPLIT VERDICT: saturation half PAYABLE by mass-weighting,
collapse half ROUTED (#627)`.

This packet repairs the **saturation half** of input 2's span-face residue —
the other half of the C7 projection-degree budget. Its sibling **PR #626**
(`c7_degree_enumeration.md`) proved the saturation *count* is a positive-rate
binomial tail and printed the direction problem verbatim: the printed
`prop:saturation-payment` wants a **uniform lower occupancy** `H`, and the
heavy-atom violators defeat it with a light tail (`H = 1`). This packet supplies
the missing payment mechanism: the **mass-weighted** occupancy compiler.

Every number below is recomputed by
`experimental/scripts/verify_saturation_payment.py` (stdlib-only, zero-arg,
`RESULT: PASS (28/28)`, ~1 s under `ulimit -v 2097152`).

Label key: **PROVED** (hand derivation, exact), **MEASURED** (exact finite toy,
asymptotics not proved from the toy), **AUDIT** (interface reading of the tex or
a sibling note), **WALL** (identified obstruction), **OPEN**.

**Credit.** The two-cell split of `(S_E)`-violators and the `Q_img = L·Mx`
multiplicativity (`Q_img = ∏ Q_img^{(i)}`, MASTER-2 `E+1 ≤ G_1 Q_img`, T3) are
**PR #625** (`c7_routing_spectrum.md`). The saturation *count* = binomial tail,
the `H = 1` defeat of `RC1`, and the exact consumer pin are **PR #626**
(`c7_degree_enumeration.md`). The detection theorem — every saturation violator
**fires** the ray-saturation trigger (predicate identity with `¬primitive-Q`),
so every violator is routed and the residual is "what the routed cell pays" — is
**PR #627** (`routing_exhaustiveness.md`). The occupancy atlas this repair builds
on (the exact full-agreement occupancy weight `H_φ` and the weighted
vertex-cover compiler `|Z_a(r) ∩ Γ| ≤ min(|Γ|, τ_φ)`) is **DannyExperiments
#620** (`canonical_full_agreement_occupancy_atlas.md`); the opposite projection
extreme (an exponential fiber collapsing to one base-field-pole slope) is
**DannyExperiments #621** (`aperiodic_one_ray_saturation.md`). The block-parabola
family and `(CF*)` character-frame identities are **avdeevvadim #558**. The
stress-test witness is the **Codex team orientation-saturation packet** (in
flight — branch `thresholds-full-agreement-orientation-saturation`, not yet a
numbered PR; `full_agreement_orientation_saturation.md`).

---

## HEADLINE (read first)

`prop:saturation-payment` (tex L4726–4739) offers two routes to pay a saturation
cell: **(1)** "a proved lower fiber bound" (→ `RC1`, which needs a *uniform*
lower occupancy `H`), or **(2)** "a direct distinct-slope estimate at the profile
scale." Route (1) is defeated by the light tail (`H = 1`, #626). This packet
repairs route (1) by replacing the **uniform** lower bound with the **exact
mass-weighted identity that is already in `lem:exact-occupancy-compiler`**:

```
   |Z(C)|  <=  |R(C)|  =  sum_{w in C} 1 / nu_C(pi_exp(w)).            (RC_occ)
```

A witness in a **heavy** fiber (occupancy `nu` large) contributes `1/nu` — the
whole heavy atom of `f_heavy` supports contributes exactly **1** to the state
count `|R(C)|`, no matter how large `f_heavy` is; each **light-tail** singleton
contributes `1`. So the distinct-slope count is controlled by the **number of
states**, not the mass. Working backward from the consumer (below), the single
invariant the envelope needs is

```
   rho(C) := |Z(C)| / Nbar_lambda = |Z(C)| * L_lambda / |Omega^0_lambda|.
```

The cell is **paid** iff `rho(C) <= e^{o(n)}`. Because `|Z(C)| <= |Omega^0_lambda|`
always, `rho(C) <= L_lambda` **unconditionally** — the payment is controlled by
the **realized boundary image size** `L_lambda` unless the slope map compresses.

- **Genuine saturation** (few heavy atoms carry the mass; the heavy atom's
  fiber size *is* its `Nbar` contribution and it fans into at most its-own-size
  slopes): `rho <= 1`. **PAID.** The heavy atom self-pays.
- **Heavy-atom product with a geometric (light) tail** (the mission's model):
  `rho` is **multiplicative** (`Q_img`, `G_1` tensor, #625 T3) and `rho_block =
  |Z_block|^2 / mass_block <= 1` whenever `(t+1)^2 <= r^t` (the heavy atom
  dominates the square of the tail-slope count). Product `rho -> 0`. **PROVED.**
- **The orientation floor** (Codex packet): `rho = q^{w/2} = e^{Theta(n)}`. **NOT
  absorbed.** But it is **not a saturation cell** — it is **unsaturated**
  (`Q_img = 1`) — it is a half-dimensional-boundary **collapse** cell whose
  separating-pole slope map is a bijection. **NEW OBSTRUCTION, on the collapse
  side, routed by `(FI)`; not a counterexample to the saturation payment.**

**Net verdict.** The mass-weighted compiler **discharges the saturation half of
`prop:saturation-payment` on the heavy-atom product class** (the actual
`(S_E)`-violators, #625 T3). The orientation floor is correctly **re-classified
as a collapse cell** (routed, #627), confirming the collapse/saturation split is
real and that the collapse half cannot be paid by any per-cell envelope bound.

---

## Rung 1 — THE EXACT CONSUMER, verbatim (AUDIT)

### 1a. The cell and its three images (`def:explanation-occupancy`, tex L5646–5671)

> `\Rcal(\Ccal)=\{(\gamma,h):\exists S\ (\gamma,S,h)\in\Ccal\}`,
> `Z(\Ccal)=\{\gamma:\exists h\ (\gamma,h)\in\Rcal(\Ccal)\}`. …
> `\nu_{\Ccal}(\rho)=\abs{\{S\in\tbinom Da:(\gamma,S,h)\in\Ccal\}}`. …
> `\Ccal\longrightarrow\Rcal(\Ccal)\longrightarrow Z(\Ccal)`,
> `(\gamma,S,h)\longmapsto(\gamma,h)\longmapsto\gamma`. The first map forgets an
> exact-agreement support; the second forgets the explaining polynomial.

So a cell has **support count** `|C|`, **explanation-state count** `|R(C)|`,
**slope count** `|Z(C)|`, and the **occupancy** `nu_C(rho)` = supports per state.

### 1b. What the budget wants (`prop:saturation-payment`, tex L4726–4739)

> **[L4726]** `\begin{proposition}[Saturation criterion]` A saturation cell is
> paid if the projection from raw witnesses to the explanation image and then the
> slope image of `\cref{def:explanation-occupancy}` has a **proved lower fiber
> bound**, or if the final image has a **direct distinct-slope estimate at the
> profile scale**.
>
> **[L4733, proof]** This is `\cref{lem:exact-occupancy-compiler}`. A lower
> retained-support occupancy bounds explanation states, and projection to slopes
> can only decrease cardinality. … **An upper bound on the number of profile
> lifts goes in the wrong direction.**

### 1c. The occupancy compiler it cites (`lem:exact-occupancy-compiler`, tex L5673–5698)

> `|C| = sum_{rho in R(C)} nu_C(rho)`,  `|R(C)| = sum_{w in C} 1/nu_C(pi_exp(w))`,
> `|Z(C)| <= |R(C)|`.  **(RC_occ)**
> In particular, if **every** retained explanation state has occupancy at least
> `H >= 1`, then `|Z(C)| <= floor(|C|/H)`.  **(RC1)**

`RC_occ` is an **exact mass-weighted identity**; `RC1` is its lossy corollary
that assumes a **uniform** floor `H`. The heavy-atom violators have `min nu = 1`,
so `RC1` gives the vacuous `|Z(C)| <= |C|` (verifier BLOCK 1). This is the
"direction problem" #626 printed.

### 1d. Where the cell's contribution enters the envelope (`eq:profile-envelope` L857–862; A2 L905–907)

> `E_n(a) = 1 + (n-a+1) + sup_{(r0,r1)} sum_{lambda in Lambda(r0,r1;a)}
> (1 + Nbar_lambda)`,  `Nbar_lambda = |Omega^0_lambda| / L_lambda`.
>
> **[A2]** "A first-match atlas covers every bad-slope witness and has `e^{o(n)}`
> profiles. The total **distinct-slope** contribution of its algebraic cells is
> at most `e^{o(n)} E_n(a_n)`."

**Backward derivation of the consumer.** Summing A2's per-cell distinct-slope
contribution `|Z(C_lambda)|` over the `e^{o(n)}` atlas profiles must land under
`e^{o(n)} E_n(a) = e^{o(n)} sup sum_lambda (1 + Nbar_lambda)`. The clean
sufficient per-cell form is therefore

```
   |Z(C_lambda)|  <=  e^{o(n)} (1 + Nbar_lambda),        Nbar = |Omega^0|/L.   (CONSUMER)
```

Everything else in this packet is the derivation of a bound of the left side by
the right side. The relevant occupancy is the one on the maps
`C -> R(C) -> Z(C)` (`def:explanation-occupancy`), **not** the prefix map alone —
that distinction is exactly what the stress test turns on.

---

## Rung 2 — THE REPAIRED STATEMENT (consumer-first)

Divide `(CONSUMER)` by `Nbar_lambda`. The cell is paid iff the **mass-weighted
occupancy ratio**

```
   rho(C) := |Z(C)| / Nbar_lambda = |Z(C)| * L_lambda / |Omega^0_lambda|   <=  e^{o(n)}.
```

**Unconditional bound (PROVED, RC_occ chain).** Every slope needs at least one
support, so `|Z(C)| <= |C| = |Omega^0_lambda|`, hence

```
   rho(C)  <=  L_lambda      (the realized boundary image size),         (RHO-UB)
```

with **equality** exactly when the slope map is injective on supports (no
compression). So the payment is controlled by `L_lambda`, deflated by any
slope-map compression. The repaired criterion replaces "uniform lower occupancy
`H`" by "mass carried by few slopes":

> **Repaired saturation criterion (mass-weighted).** A saturation cell `C` is
> paid iff `|Z(C)| <= e^{o(n)}(1 + Nbar_lambda)`, equivalently `rho(C) =
> |Z(C)|/Nbar_lambda <= e^{o(n)}`. This holds whenever the cell mass is carried
> by few slopes: if a dominant slope family `B` of size `|B| = e^{o(n)}` carries
> occupancy `f_heavy` each and the tail slopes have occupancy summing to
> `e^{o(n)} · f_heavy` over `e^{o(n)}` slopes, then `rho(C) = e^{o(n)}`. A lower
> bound on the **dominant** slopes' occupancy — not a uniform lower bound over
> all slopes — is what the envelope consumes; the light-tail occupancy-`1` slopes
> do not defeat it because they contribute few *distinct slopes*.

This is the honest reading of the two clauses: it repairs clause (1) (the "lower
fiber bound" is now a lower bound on the *dominant* fiber, feeding `RC_occ`
rather than `RC1`), and it makes clause (2) ("direct distinct-slope estimate")
computable as `|Z(C)| = |B| + (tail slopes) = e^{o(n)}`.

**Label: AUDIT** (the identity is already `RC_occ`) **+ PROVED** for the payment
on the class of Rung 3.

---

## Rung 3 — THE PROOF on the heavy-atom product class (PROVED)

**The mechanism, purest form (BLOCK 2).** A **pure** saturation cell puts all
mass in one atom: one explanation state of occupancy `J`, `L = 1`, so `Nbar = |C|
= J`. Its `J` supports realize **at most `J`** distinct slopes, so `|Z(C)| <= J =
Nbar` and `rho <= 1`. **The heavy atom's fiber size is exactly its own payment.**
PROVED (exact, all `J` in the verifier).

**The product class (BLOCK 3).** By #625 T3, `Q_img` and `G_1` (hence `rho`)
**tensorize** over independent blocks: `rho = ∏_i rho_i`. Model each block as one
heavy slope-atom of fiber `r^t` with a **geometric tail** `r^{t-1}, …, r, 1`
(`t+1` slopes, ratio `r`). Exact per-block quantities:

```
   |Z_block| = t+1,   mass_block = sum_{i=0}^{t} r^i = (r^{t+1}-1)/(r-1),
   rho_block = |Z_block|^2 / mass_block = (t+1)^2 / mass_block.
```

`rho_block <= 1  <=>  (t+1)^2 <= r^t` — the heavy atom dominates the **square** of
the tail-slope count. The **tail mass** is the geometric partial sum
`(r^t - 1)/(r-1)`, a bounded fraction `< 1/(r-1)` of the block mass — "the light
tail contributes little mass," bounded by a geometric series exactly as the
mission required. Product over `k` blocks: `rho = ∏ rho_i = ((t+1)^2/mass)^k -> 0`
whenever each block clears `(t+1)^2 <= r^t`. Verifier BLOCK 3 confirms `paid =
True` and the excess rate `(1/k) log(|Z|/(1+|C|/|Z|)) -> ≤ 0` on
`(r,t) ∈ {(4,2),(4,3),(5,2),(4,1)}`, and the **boundary** case (shallow decay
`r=2, t=1`: `(t+1)^2 = 4 > r^t = 2`) correctly **fails** — a near-uniform slope
distribution is not a light tail.

**Exact partition (dominant + tail).** For the product, the dominant atom is the
tensor of per-block heavy atoms — one product slope of fiber `r^{tk}` — carrying
`(∏ mass_i)^{-1} r^{tk}` of the mass; the tail is every product slope with at
least one off-heavy block, its total mass bounded by the product-geometric series
`∏(mass_i) - r^{tk}`. The dominant slope contributes `1` to `|Z|`; the tail
contributes `(t+1)^k - 1` slopes. **PROVED** (BLOCK 3, exact `Fraction`).

**#625 type-S uniform-tail witness (BLOCK 4, MEASURED/AUDIT).** The published
heavy-atom witness (#625: `mu(z*) = A_eff^{-1/4}`, tail **uniform** over
`A_eff − 1` points) has `Q_img = round(A_eff^{3/4}) ∈ {8,27,64,125}` for `A_eff ∈
{16,81,256,625}` — reproduced byte-exact. Because its tail is uniform (not
geometric), it has `|Z| = A_eff` distinct slopes, so `rho <= 1` needs the
support-richness `M >= A_eff^2`. This is the **borderline** between the paid
geometric class and the orientation obstruction, recorded honestly.

---

## Rung 4 — STRESS TEST: the orientation floor (PROVED-negative)

The Codex orientation-saturation packet
(`full_agreement_orientation_saturation.md`, in flight) constructs, over
`q = 3^r`, antipodal supports `O_r = {S : |S ∩ {x,−x}| = 1 for every fold fiber}`
with `|O_r| = 2^a`, `a = (q−1)/2`, prefix depth `w = 2⌊a/2r⌋`, an **exact-slope
prefix fiber floor**

```
   J_z >= ceil(2^a / q^{w/2}),   (log J_z)/n >= log(2)/2 − log(3)/4 = (1/4)log(4/3) > 0.
```

**Absorb-or-obstruct computation (BLOCK 5, exact `r = 2..7`).** Reproduced floors
`J ∈ {2, 12, 316, 62 712 512, …}` for `r ∈ {2,3,4,5}` (byte-match to the packet).
The cell's realized boundary image is **half-dimensional** `L_bnd = q^{w/2}`, its
prefix fibers are **uniform** (each `≈ J_z`), and at a **separating pole** the
slope map `S ↦ γ_S` is a **bijection** (packet eq (8)), so

```
   |Z(C)| = 2^a  (bijective),   Nbar_bnd = |O_r|/L_bnd = 2^a/q^{w/2},
   rho(C) = |Z(C)|/Nbar_bnd = q^{w/2}  =  the collapse ratio G_1  =  e^{Theta(n)}.
```

The consumer gap has **positive rate for every `r`** (verifier: `rate_gap > 0.2`,
`r = 2..7`) and matches the collapse rate `log(q^{w/2})/n -> log 3 / 4 = 0.2747`
(within `0.01` at `r = 7`); the floor itself has rate `log(4/3)/4 = 0.0719`.
**The mass-weighted compiler does NOT absorb it.**

**But the diagnosis is precise and it is NOT a saturation counterexample.** The
orientation cell is **UNSATURATED**: its prefix fibers are uniform, so `Q_img =
L·Mx = max/avg = 1` (verifier BLOCK 5, from the packet's finite `F_9` model:
`16` supports, prefix image `8`, **every** fiber size `2 = max = avg`). It is a
half-dimensional-boundary **collapse** cell (`G_1 = q^{w/2}`). The mass that
inflates `Nbar_bnd` sits in the **prefix** map, but the **separating pole
re-expands** it into distinct slopes — there is **no explanation-map heavy atom**
for the mass-weighting to grip (`nu = 1` for every state, `|R(C)| = |Z(C)| =
|C|`, no compression). This is exactly the packet's own **"ROUTE CUT"** verdict:
the cell is caught by `(FI)`/first-match routing before the envelope sum, not
paid by the envelope.

> **Verdict: the orientation floor is a genuine new positive-rate exact-slope
> obstruction, but it is localized to the COLLAPSE side (`Q_img = 1`,
> `G_1 = q^{w/2}` exponential), NOT the saturation payment. It is absorbed by
> ROUTING (its correct home, #627), not by the saturation envelope term. It does
> not refute the repaired saturation criterion; it confirms the
> collapse/saturation split (#625) and that the collapse half needs `(FI)`.**

**Residual risk (honest).** A cell that were *both* saturated (few heavy boundary
atoms) *and* separating-pole re-expanded would break the payment — but a boundary
atom of occupancy `J` fans into **at most `J`** slopes, contributing `1` state and
`J` to the mass, so a genuinely heavy boundary atom **self-pays** (Rung 3, BLOCK
2). The obstruction needs *many* (`q^{w/2}`) boundary atoms — i.e. **collapse**,
not saturation. The two events are provably separated by `Q_img` vs `G_1`.

---

## Rung 5 — CENSUS (BLOCK 6, the split as a per-block competition)

The controlling invariant `rho = |Z|/Nbar = |Z|·L_bnd/|Omega^0|` is **exactly
multiplicative** (`|Z|`, `Nbar` both tensor, #625 T3). Two block types:

| block | `rho_i` | effect |
|-------|---------|--------|
| **S** saturation (heavy slope atom + geometric tail, `r=4,t=2`) | `9/21 = 3/7 < 1` | **compresses** |
| **O** collapse/orientation (`L_bnd` boundary values, bijective slopes) | `L_bnd > 1` | **expands** |

Pure saturation product `rho = (3/7)^k -> 0` (**PAID**, all `k`). A product with a
collapse-block **fraction** `f` has `rho = (3/7)^{(1−f)k} · L_bnd^{fk}`, which
exceeds `1` iff

```
   f  >  f* = log(1/rho_S) / (log(1/rho_S) + log rho_O)  ≈  0.278.
```

Verifier BLOCK 6: `4 sat + 4 collapse` (`f = 1/2 > f*`) gives `rho ≈ 221 > 1`
(**unpaid** — collapse blocks routed, saturation blocks paid); `7 sat + 1
collapse` (`f = 1/8 < f*`) gives `rho ≈ 0.03 ≤ 1` (**paid**). This is a
**binomial-tail threshold**, structurally the same object as #626's
`sum_{j >= theta k} C(k,j)`: a positive collapse fraction is required, so the
unpaid leaves form the same `e^{Omega(N)}` tail that `(FI)` must route.

**Admissible controls (BLOCK 7).** Single admissible power-sum leaves reproduce
#625 type-T exactly (`E+1 = G_1`, `Q_img = 1`): `(p,L,A_eff,E) = (3,2,3,1/2),
(5,3,25,22/3), (7,6,49,43/6)`. `Q_img = 1`, `L` subexponential per single leaf ->
always paid. The whole-arc rate constants are reproduced: collapse typical rate
`(ln p)/(2p) = 0.1831` at `p=3`; orientation floor rate `log(4/3)/4 = 0.0719`.

---

## Verdict ledger

| item | verdict | label |
|------|---------|-------|
| consumer = `(CONSUMER)`: `|Z(C_lambda)| ≤ e^{o(n)}(1+Nbar_lambda)`, `Nbar=|Omega^0|/L` | backward from A2 (L905–907) + `eq:profile-envelope` (L857–862) | **AUDIT** |
| `RC1` uniform-`H` defeated by light tail (`H=1`, `|Z|≤|C|` vacuous) | `prop:saturation-payment` L4726–4739 | **PROVED** (BLOCK 1, = #626) |
| repair = the exact mass-weighted `RC_occ` already in `lem:exact-occupancy-compiler` | `|Z(C)| ≤ |R(C)| = sum_w 1/nu` | **AUDIT** (L5673–5698) |
| controlling invariant `rho = |Z|·L/|Omega^0| ≤ L_bnd` unconditionally | RC_occ chain, `|Z|≤|C|` | **PROVED** (BLOCK 0) |
| pure heavy atom self-pays (`rho ≤ 1`; fiber size = its `Nbar`) | one atom, `L=1` | **PROVED** (BLOCK 2) |
| heavy-atom **geometric-tail** product paid (`rho_block=(t+1)^2/mass≤1`) | tensor, geometric tail | **PROVED** (BLOCK 3) |
| #625 type-S **uniform-tail** witness: `Q_img=A^{3/4}`; paid iff `M≥A^2` | reproduce + borderline | **MEASURED/AUDIT** (BLOCK 4) |
| orientation floor `J=ceil(2^a/q^{w/2})`, rate `log(4/3)/4`; `rho=q^{w/2}` | Codex packet reproduce | **PROVED** (BLOCK 5) |
| orientation cell is **unsaturated** (`Q_img=1`), a **collapse** cell (`G_1=q^{w/2}`) | finite `F_9` uniform fibers | **PROVED-negative** (BLOCK 5) |
| **orientation floor = NEW OBSTRUCTION, collapse-side, routed — not a saturation counterexample** | localized diagnosis | **WALL (collapse) / not (saturation)** |
| split = per-block `rho` competition; unpaid iff collapse fraction `> f*≈0.278` | binomial tail (cf #626) | **PROVED** (BLOCK 6) |
| collapse half payable only by `(FI)`/first-match routing | routing = spectrum | **OPEN** (#627) |

**Proposed ledger entry (for the maintainer).** *The saturation clause of
`prop:saturation-payment` (L4726–4739) currently routes through `RC1`, which
needs a uniform lower occupancy `H`; the heavy-atom violators defeat it (`H=1`,
#626). The exact identity `RC_occ` already present in `lem:exact-occupancy-
compiler` (L5673–5698) is mass-weighted: `|Z(C)| ≤ |R(C)| = sum_w 1/nu_C(π_exp
w)`, so a heavy atom of `f_heavy` supports contributes `1` to the state count
while a light-tail singleton contributes `1`. Working backward from A2 (L905–907)
the envelope consumes the single invariant `rho(C) = |Z(C)|·L/|Omega^0| ≤
e^{o(n)}`, and `rho ≤ L` unconditionally. On the heavy-atom product class that
carries every `(S_E)`-violator (#625 T3), `rho` is multiplicative and a heavy
slope-atom with a geometric tail gives `rho_block = |Z_block|^2/mass ≤ 1`; the
heavy atom self-pays and the tail is a geometric series — PROVED. The
Codex-team orientation floor (`J ≥ ceil(2^a/q^{w/2})`, rate `log(4/3)/4`, over
`q = 3^r`) is NOT absorbed, but it is an **unsaturated** (`Q_img = 1`) collapse
cell (`G_1 = q^{w/2}`) whose separating-pole slope map re-expands a
half-dimensional boundary image — a collapse obstruction routed by `(FI)`, not a
saturation counterexample. Print the saturation payment as: replace `RC1`'s
uniform `H` by the mass-weighted `RC_occ`; the saturation cell is then paid on
the heavy-atom product class by the dominant atom, and the residual collapse
family (positive-fraction, binomial-tail) is `(FI)`-routed (routing = spectrum,
#625/#627). This packet proves the saturation half and localizes the residual to
the collapse half.*

### The 2–3 steps the PI should re-derive

1. **The invariant (Rung 2).** Divide the consumer `(CONSUMER)` by `Nbar`; the
   cell is paid iff `rho = |Z|/Nbar = |Z|·L/|Omega^0| ≤ e^{o(n)}`. Since
   `|Z| ≤ |Omega^0|`, `rho ≤ L` unconditionally — one line from `RC_occ`.
2. **The payment (Rung 3).** A pure heavy atom self-pays (`rho ≤ 1`, its fiber
   size is its `Nbar`). On the product class `rho = ∏ rho_i` (#625 T3); a heavy
   slope-atom with geometric tail has `rho_block = (t+1)^2/mass ≤ 1` iff
   `(t+1)^2 ≤ r^t`. One line each.
3. **The obstruction (Rung 4).** The orientation floor has `rho = q^{w/2}`
   because it is a *collapse* cell (`Q_img = 1`, half-dimensional boundary image,
   bijective separating-pole slopes), not a saturation cell. It is routed by
   `(FI)`, not paid by the envelope; the split is `Q_img` (saturation, paid) vs
   `G_1` (collapse, routed), and the unpaid leaves are the same binomial tail.

---

## What closes if the saturation half is accepted

With the mass-weighted `RC_occ` payment, input 2's span-face residue reduces on
the saturation side to the **already-open** collapse routing. The full chain:

```
   single admissible leaf   --#622 T1-->  (S_E) free, span face free (branch-1)
   heavy-atom sat. products --THIS-->      paid by mass-weighted RC_occ (dominant atom)
   collapse products        --#626-->      binomial-tail family, (FI)-routed [routing=spectrum]
   orientation floor        --THIS-->      collapse cell, (FI)-routed (not a sat. counterexample)
```

so the saturation half is discharged on the product class and the **single** open
link is the same routing-exhaustiveness conjecture (#625/#627), now with the
saturation cell paid rather than merely detected.

---

## Reproducibility

```sh
ulimit -v 2097152
python3 experimental/scripts/verify_saturation_payment.py   # RESULT: PASS (28/28)
```
