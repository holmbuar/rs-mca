# Complete profile-envelope comparison with the target: an exact deployed-shape census

**Lane.** Hard input **4** of `agents.md`: *"complete profile-envelope comparison
with the target"* --- and the submission-strategy ask *"compare the complete
profile envelope, not only the identity prefix term, against the actual target
and lower reserve."* The maintainer's new exact-threshold paper
(`experimental/rs_mca_thresholds.tex`) compares only the **identity-prefix**
term `L(a)` against the target (SB1--SB4); the named gap is the **complete**
envelope. This packet supplies the piece the assembly ledger explicitly
disclaims: a *deployed-shape numeric certificate* built by **exact enumeration**
of every envelope term from actual supports over actual finite fields, at the
realized-image scale of PO5.

**Target files (read, none edited):** `experimental/rs_mca_thresholds.tex`,
`experimental/asymptotic_rs_mca_frontiers.tex` (base commit `c35a6da`).
**No `.tex`/`.pdf` edited.**
**Verifier:** `experimental/scripts/verify_profile_envelope_target_comparison.py`
(stdlib-only, deterministic, exact `Fraction`/bigint, `RESULT: PASS (71/71)`,
1.9 s / 14 MB under `ulimit -v 2097152`; `--tamper-selftest` flips one stored
ground-truth integer and confirms a gate then fails). It recomputes **every**
integer and ratio quoted below.
**Certificate:**
`experimental/data/certificates/profile-envelope-target-comparison/cert.json`.
**Lean shadow (decidable, `native_decide`, no `sorry`, no mathlib):**
`experimental/lean/profile_envelope_target_comparison/`.

## Status (per component; route-scoped; hypotheses visible in-sentence)

- **(a) STATE** --- `PROVED` (definitional). The complete comparison object,
  the realized-image normalization, and the exact "passes as identity-dominant"
  inequality are stated in section 1, consuming `eq:profile-envelope` (1.6).
- **(b) COMPUTE** --- `COMPUTED` (exact enumeration, section 2). Every envelope
  term (identity; power-quotient at **every** scale `c | n`; every remainder
  `r < c`; the cheapest field-drop square) is enumerated from actual supports
  over `GF(13)`, `GF(7^2)`, `GF(11^2)`, `GF(41)`, at realized-image scale.
- **(c-i) DECIDE (prime rows)** --- `PROVED` + exact. On a row whose base field
  `B` is **prime** (`|B|=p`, no proper subfield, so every folding has field-drop
  ratio `lambda_c = 1`) *and* whose identity slice satisfies `(FI)`, the identity
  term dominates the **entire** certified profile envelope; the identity-prefix
  comparison SB1 / (1.9) **is** the complete comparison for that row.
- **(c-ii) DECIDE (subfield-tower rows)** --- `COUNTEREXAMPLE` (route-scoped;
  **the paper's own** `thm:smooth-quotient-obstruction`, realized to the
  integer; **NOT a new floor**). On the `B = F_{p^2}`, `B_phi = F_p` tower, the
  `c=2` field-drop square slice **beats the formal identity budget**
  `C(n,a)|B|^{-w}` at every tested row, so the identity-prefix comparison is
  **incomplete** there.
- **(c-iii) SHARPENING** --- `COMPUTED` (new sub-finding). On the *smooth
  coset* `D=theta H` the **identity** slice's realized image *also* collapses
  (exactly a factor `p` at `n=20`), so `(FI)`-for-identity is itself nontrivial
  at deployed shape: the realized-scale comparison couples to hard input **2**
  through the identity term, not only through the quotient. This sharpens the
  completeness reduction, which routed input 4 -> 2 only via the quotient.
- **(d) EXTEND** --- `COMPUTED` at `n=20` (the smallest tower where the deep
  `c=2` crossing `barN_1 >= 1` is enumerable); structural extension to deployed
  `n` is the exponent reduction already proved in the completeness ledger.

**Headline.** *The complete comparison is identity-dominant **iff** no realized
folding admits a positive-rate scaled-quotient field drop **and** the identity
slice satisfies `(FI)`. Prime base fields force the first (across all scales and
remainders, verified exactly); the `F_{p^2}` tower violates it via the paper's
own square obstruction; and the smooth coset additionally violates `(FI)` for
the identity, coupling the realized-scale verdict to input 2.*

---

## Interfaces (consumed, not reproved; credit by author)

Paper labels (both drafts):
- `eq:profile-envelope` (1.6, frontiers L858--862) --- the image-normalized
  envelope `E_n(a)=1+(n-a+1)+sup_line sum_lambda (1+barN_lambda)`, with
  `barN_lambda=|Omega_lambda|/L_lambda`, `L_lambda=|Phi_lambda(Omega_lambda)|`.
- `rem:intro-delta-scope` (thresholds L584--595) --- the two points (larger
  realized-image scale; projection to distinct slopes) where a near-capacity
  claim needs new input; the profile envelope is where the first lives.
- `thm:unconditional-support-envelope-bracket` SB1--SB4 (thresholds L3720--3759)
  --- the finite bracket `L(a),P(a),U(a)`; only the identity `L(a)` is compared.
- `thm:smooth-quotient-obstruction` (frontiers 6.1--6.4') --- the `F_{p^2}`
  tower, `barN_1=C(n,a)|B|^{-w} in [1,|B|^2)` (6.3) and
  `L_sq <= p^{w/2}`, `barN_sq >= exp((h/4)n)` (6.4'). **Reproduced exactly here.**
- `prop:necessary-quotient-envelope` (6.13) and
  `prop:identity-quotient-comparison` QR6--QR9 --- the quotient natural scale
  `C(N,m)|B_phi|^{-floor(w/c)}` and its exponent `e_c=(1/c)(h-lambda_c s)`.
- `rem PO5` (thresholds L3527--3553) --- the realized-image group `G_lambda`
  fixes the correct Fourier denominator and *does not assert the realized image
  fills the affine group*: the exact `(FI)`/collapse question this packet
  measures.
- `thm:deep-regime-upper` (`n-a+1`) --- the separate deep term of (1.6).

Prior in-tree packets (this packet **consumes and extends**, does not duplicate):
- **`profile_envelope_completeness.md`** (Holm Buar) --- the class-exponent
  reduction `E_n = max(0,e_1,max_c e_c)`, the identity-dominance band, and the
  exact add-back. Its explicit nonclaim is *"the multi-scale and add-back checks
  are **structural, not a deployed-scale numeric certificate**."* **This packet
  supplies exactly that deployed-scale certificate**, and sharpens the reduction
  with the `(FI)`-for-identity finding.
- **`envelope_identity_window.md`** (Holm Buar, PR #542) --- the identity-
  dominance window criterion `(DOM)`, its wall, and an exact `F_{p^2}` **square**
  census for the single cheapest folding `(c=2,r=0)`. **This packet reproduces
  that census byte-for-byte (section A) and extends it to the full scale
  inventory (every `c|n`, every `r<c`), a prime control, and the deep crossing.**
- **`profile_envelope_vs_target.md`/`.json`** (LegaSage #520) --- the envelope
  *formula* and four deployed adjacent-row brackets at statement level. Consumed.
- **`asymptotic_profile_envelope_audit.md`** (#524) --- reproduces the
  obstruction *construction* at `GF(11^2..23^2)`. Consumed as the evidence base.
- scottdhughes `(MI)`/`(MA)`/entropy-inverse (#498/#501/#505),
  `fi_full_image_primitive.md`, `c7_collapse_image_degree.md` (#528/#534/#535/
  #635): the per-cell `(FI)`/Sidon payment (hard input 2) --- consumed as the
  target of the reduction, **never attacked**.

**Fences respected.** No emission-based lower-reserve payment
(`thm:aperiodic-one-ray-saturation`: a heavy fiber can collapse to one slope).
Every image-scale count normalized by the realized image `L_lambda` (PO5), never
the ambient codomain `A_lambda`. No route killed by the three proved barriers
(`prop:pairwise-overlap-limit`, `drc:prop-recurrence-nonadditive`,
`prop:no-growing-prime-density`) is re-attempted.

---

## 1. The complete-comparison object (rung a, `PROVED` definitional)

**One boundary map, many slices.** Every realized profile `lambda` is a slice
`Omega_lambda subseteq C(D,a)` scored by the **same** global depth-`w` locator
prefix `Phi_w(S)=(c_1(S),...,c_w(S))`, `w=a-k-1`, `c_i` the coefficients of
`Q_S(X)=prod_{x in S}(X-x)` just below the leading term. Following (1.6)/PO5,

```
   L_lambda   = | Phi_w(Omega_lambda) |            (REALIZED image, not codomain)
   barN_lambda= | Omega_lambda | / L_lambda         (average full-slice fiber, 1.6)
```

The **identity** slice is `Omega_id=C(D,a)` (`barN_id=C(n,a)/L_id`); the
**power-quotient of scale `c`** is `Omega_c={phi^{-1}(E) sqcup R}` for the
complete `c`-fiber folding `phi(x)=x^c` (`|R|=r<c`, `m=(a-r)/c`). For a complete-
square-fiber support `Q_S = V_E(X^c)` is lacunary and, on the tower,
field-dropped: its nonzero prefix coordinates lie in `eta^j B_phi`, so
`L_sq <= |B_phi|^{floor(w/c)}` --- an **exact algebraic identity**, not a bound.

**The complete profile envelope** (1.6): `E_n(a) = 1 + (n-a+1) +
sup_line sum_lambda (1+barN_lambda)`, the sum over identity, power-quotient
(every `c`), Chebyshev, planted, and remainder profiles.

**The exact "passes as identity-dominant" inequality.** The complete comparison
*reduces to the identity comparison at agreement `a`* iff

```
   (ID)   barN_lambda(a)  <=  barN_id(a)      for every realized profile lambda,
```

at realized-image scale. Then `E_n(a) = e^{o(n)} barN_id(a)`, the safe-side
target certificate (13.2) `2^{ell_n} E_n(a) <= B*_n` is met by the identity
budget `barN_id = L(a)`, and the SB1 bracket / delta-formula crossing `g_{T,n}`
is the **true** envelope crossing. When `(ID)` fails, the safe-side budget must
use the larger `barN_lambda`, so the safe threshold `a*` moves **up** and
`delta* = 1-rho-g_env < 1-rho-g_{T,n}` --- a strictly worse certified radius.
The paper compares only the identity `L(a)`; **(ID) over the non-identity terms
is the complete comparison.**

*Hypothesis note.* The paper's obstruction (6.3) uses the **formal** identity
budget `barN_1^formal := C(n,a)|B|^{-w}` (the free pigeonhole budget); using it
in place of `barN_id` in `(ID)` is legitimate only when the identity slice
satisfies `(FI)` `L_id >= e^{-o(n)}|B|^w`. Section 2.3 shows `(FI)` is itself
nontrivial at deployed shape.

---

## 2. Exact deployed-shape census (rung b, `COMPUTED`)

All rows use `w = a-k-1`; every integer is recomputed by the verifier. Caps are
printed, not hidden: full identity enumeration is done at `n<=20`
(`C(20,10)=184756`); no larger row is enumerated.

### 2.1 Cross-check of #542 (verifier section A)

The `F_{p^2}` square census of `envelope_identity_window.md` reproduces exactly:

| `p` | `n` | `a` | `|Omega_sq|=C(N,m)` | distinct prefixes `L_sq` | max bucket | `QR6=ceil(C(N,m)/p)` |
|----|----|----|----|----|----|----|
| 5  | 8  | 4  | 6  | 5 (`=p`) | 2 | 2 |
| 7  | 12 | 4  | 15 | 7 (`=p`) | 3 | 3 |
| 11 | 20 | 4  | 45 | 11 (`=p`) | 5 | 5 |

`L_sq = p` (the field drop) and the max bucket equals the QR6 pigeonhole ---
byte-identical to #542.

### 2.2 The decisive prime-vs-tower rows (verifier sections B, C, E)

Realized-image census, `a=6,k=3,w=2` at `n=12` and `a=10,k=7,w=2` at `n=20`
(`|Omega|`, `L` = realized image, `barN=|Omega|/L`):

| row | `|B|` | identity `(|Omega|,L_id,barN_id)` | square `(|Omega|,L_sq,barN_sq)` | formal `barN_1` | field drop? | verdict |
|---|---|---|---|---|---|---|
| **prime `GF(13)`** `n=12` | 13 | `(924, 169, 5.4675)` | `(20, 13, 1.5385)` | `924/169=5.47` | **no** (`L_sq=13=|B|`) | identity **dominates** |
| **tower `GF(49)`** `n=12` | 49 | `(924, 319, 2.897)` | `(20, 7, 2.857)` | `924/2401=0.385` | **yes** (`L_sq=7=p`) | square **beats formal id** |
| **tower `GF(121)`** `n=20` | 121 | `(184756, 1331, 138.8)` | `(252, 11, 22.909)` | `184756/14641=12.62` | **yes** (`L_sq=11=p`) | square **beats formal id** |
| **prime `GF(41)`** `n=20` | 41 | `(184756, 1681, 109.9)` | `(252, 41, 6.146)` | `184756/1681=109.9` | **no** (`L_sq=41=|B|`) | identity **dominates** |

Exact cross-multiplied decisions (all `native_decide`-checked):
- prime domination `barN_id >= barN_sq`: `924*13 = 12012 >= 3380 = 20*169` (`GF(13)`).
- tower obstruction `barN_sq > barN_1^formal`: `20*2401 = 48020 > 6468 = 924*7`
  (`GF(49)`); `252*14641 = 3689532 > 2032316 = 184756*11` (`GF(121)`).

**Full scale inventory (verifier sections B, F).** At `n=12` the complete-fiber
folding scales are `c in {2,3,4,6}`, with admissible remainders `r<c`. On the
**prime** `GF(13)` row every quotient/remainder cell is accounted by the identity
term *or* the deep term `n-a+1=7` (the shallow `w<c` cells `c in {3,4,6}` have
lacunarily trivial prefixes and land at the deep term, never a field-drop
competitor). On the **tower**, the sole cell exceeding the formal identity budget
is the `c=2, r=0` field-drop square --- confirming `sum=max` over the scale
inventory with the leader identified.

### 2.3 The `(FI)`-for-identity sharpening (verifier section E; new)

Measured realized identity image `L_id` vs formal codomain `|B|^w`:

| row | `L_id` | `|B|^w` | `(FI)`? | note |
|---|---|---|---|---|
| prime `GF(41)` `n=20` | 1681 | `41^2=1681` | **holds** | prime subgroup fills the codomain |
| tower `GF(121)` `n=20` | 1331 | `11^4=14641` | **fails** | smooth coset collapses by exactly `p=11` (`1331=11^3`) |
| generic 20-subset of `GF(121)` | `>=7342` and climbing | 14641 | (fills) | collapse is **specific to the smooth coset** `D=theta H` |

So on the very smooth coset `D=theta H` that the obstruction uses, the
**identity** slice's realized image collapses too (`1331*11=14641` exactly).
Using realized image for *both* terms at `n=20` gives `barN_id^real=138.8 >
barN_sq=22.9` (identity would win); using the **formal** identity budget
`12.62 < 22.9` (square wins). The verdict at deployed shape therefore hinges on
an identity-side `(FI)`/flatness estimate --- i.e., hard input **2** applied to
the identity term, not only the quotient.

### 2.4 Target comparison (verifier section D)

At the `n=20` tower crossing, the safe-side budget (1.6)/(13.2) with the
integer-ceiled terms is `E_identity = 1+(n-a+1)+(1+ceil(barN_1^formal)) = 26`
versus the complete `E_complete = 26 + (1+ceil(barN_sq)) = 50`. A cryptographic
target `B* = 26` is then certified **safe** by the identity budget but
**unsafe** by the complete envelope: the identity-prefix comparison is
*incomplete* exactly here. (Illustrative small target; the finite rows are toy
scale, the mechanism exact.)

---

## 3. Decision (rung c)

**(c-i) Prime-field / no-drop identity dominance --- `PROVED`.**
On a row with prime base field `|B|=p` (forcing `lambda_c=1` for every folding,
since `B_phi subseteq B` has no proper subfield) *and* identity `(FI)`, every
non-identity envelope term obeys `(ID)`:
the power-quotient exponent `e_c = (1/c)(h - lambda_c s) = (1/c)(h-s) <=
max(0, h-s) = max(0, e_1)` (with `h=H_2(rho+g)`, `s=g beta`), because
`(h-s)/c <= h-s` when `h>=s` and `<= 0` when `h<s`; planted (`x2^b`), remainder
(`w>=r` exact / `w<r` reduces to a prefix problem `x e^{o(n)}`), and
balanced-core (`(RC)`/add-back) contribute no new exponent
(`profile_envelope_completeness.md` class inventory). Hence
`E_n = e^{o(n)} barN_id` and SB1/(1.9) is the complete comparison. Verified
exactly at `GF(13)` `n=12` (all scales) and `GF(41)` `n=20` (deep saturated,
`(FI)` holds).

**(c-ii) Subfield-tower obstruction --- `COUNTEREXAMPLE` (route-scoped; NOT
new).** On `B=F_{p^2}`, `B_phi=F_p`, the `c=2` field-drop square slice satisfies
`barN_sq >= C(n/2,a/2) p^{-w/2}` (QR6, from the exact lacunary identity
`Q_S=V_E(X^2)`) and beats the **formal** identity budget `C(n,a)|B|^{-w}` at
every tested row. This is precisely `thm:smooth-quotient-obstruction`, realized
to the integer; it is **the paper's own** exponential competitor `e_2=h/4` at
the crossing, **not a new floor** (concurring with `envelope_identity_window.md`:
the sole exponential obstruction is the paper's). Named term: the scaled
quotient coefficient field `B_phi=F_p`; named regime: positive-rate field drop
`1 - log|B_phi|/log|B| = 1/2`.

**(c-iii) Reduction, sharpened --- `PROVED` (reduction) + new coupling.**
The complete comparison reduces to the single scalar test *"does any realized
folding admit a positive-rate scaled-quotient field drop `lambda_c<1` with live
prefix entropy?"* (input-2/PO4 territory) **and** *"does the identity slice
satisfy `(FI)`?"*. The completeness ledger established the first (routing input
4 -> input 2 through the quotient's `(FI)`/Sidon payment). **New here:** the
exact enumeration exhibits that the identity slice's own `(FI)` fails on the
smooth coset, so the reduction couples to input 2 through the identity term as
well --- a strictly larger dependency than the quotient-only routing. No
independent open analytic core beyond inputs 2 (`(FI)`/Sidon, now for identity
*and* quotient) and 3 (`(RC)`).

---

## 4. The residual, pinned (`OPEN`, = input 2 for identity *and* quotient)

> **(PEU-id)** For a ledger-admissible smooth/circle row, the identity slice's
> realized image satisfies `(FI)` `L_id >= e^{-o(n)} |B|^w` uniformly, so the
> formal identity budget `C(n,a)|B|^{-w}` is the realized-scale identity term.

Given `(PEU-id)` (identity flatness) and the quotient-side `(PEU)` of
`profile_envelope_completeness.md` (quotient flatness), the complete comparison
closes through the proved wrapper. Both are hard input 2 (image-scale
`(MI)/(MA)`/Sidon), now seen to be required on the identity term too. This is
**not** an independent open object of input 4.

---

## 5. Per-claim ledger

| # | Claim | Status |
|---|-------|--------|
| C1 | `(ID)` states the complete comparison; formal-vs-realized identity budget distinguished | `PROVED` (defn; sec 1) |
| C2 | #542 square census reproduced (`L_sq=p`, max bucket `=QR6`) at `p in {5,7,11}` | `COMPUTED` (sec A) |
| C3 | prime `GF(13)`/`GF(41)`: identity dominates every scale/remainder, `(FI)` holds | `PROVED`+exact (sec B,E,F) |
| C4 | tower `GF(49)`/`GF(121)`: `c=2` field drop beats formal identity budget | `COUNTEREXAMPLE` (paper's own; sec C,E) |
| C5 | `Q_S=V_E(X^c)` lacunary + `B_phi=F_p`: `L_sq <= p^{floor(w/c)}` exact | `PROVED` (identity; sec C) |
| C6 | full scale inventory `c in {2,3,4,6}`: sum=max, single leader identified | `COMPUTED` (sec B,F) |
| C7 | `(FI)`-for-identity fails on smooth coset (`L_id=11^3<11^4`), holds on prime subgroup and generic domain | `COMPUTED` (new; sec E) |
| C8 | target: identity-safe / complete-unsafe strict move at the `n=20` crossing | `COMPUTED` (sec D) |
| C9 | reduction: input 4 = proved wrapper o (identity+quotient `(FI)` = input 2) + `(RC)` | `PROVED` (reduction) / `OPEN` (PEU) |

## 6. Flagged for independent re-derivation

1. **`(FI)`-for-identity generality (C7).** The `n=20` collapse is exactly a
   factor `p`; whether it is bounded (subexponential, so the square exponent
   `h/4` still dominates asymptotically) or can itself grow is an identity-side
   flatness question --- confirm it is input 2, not a new object.
2. **Formal-vs-realized budget (C1).** The paper's `barN_1=C(n,a)|B|^{-w}` (6.3)
   is the free budget; re-check that promoting the obstruction to realized scale
   is exactly the `(FI)` upgrade `(PEU-id)` and carries no hidden content.
