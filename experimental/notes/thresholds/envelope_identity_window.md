# The identity-dominance window: a sufficient criterion and its failure map

**Lane.** Hard input **(d)** of `agents.md` --- *"complete profile-envelope
comparison with the target"* --- and submission-strategy item 5, *"compare the
complete profile envelope, not only the identity prefix term, against the actual
target."* Our delta-audit (PR #524) verdicted this **OPEN GAP**: identity-
dominance is *"carried as an explicit premise; known false in general, so
genuinely conditional --- the tractable target is a sufficient
identity-dominance window criterion."* This packet proves that criterion, gives
its complement (the failure map), and names the wall.

**Target file:** `experimental/asymptotic_rs_mca_frontiers.tex` (worktree base
`4e3c4ee`). **No `.tex`/`.pdf` edited.**
**Verifier:** `experimental/scripts/verify_envelope_window.py` (stdlib-only,
zero-arg, `RESULT: PASS (13295 checks)`, ~0.12 s under `ulimit -v 2097152`;
recomputes every gated number: exponent identities, window/band edges,
crossing-in-band, target-threshold form, and an exact `F_{p^2}` census).

**Highest rung reached: 5 (all rungs traversed).**
**Verdict:** `PROVED` (window criterion, lower + upper agreement windows and the
target-threshold form; sufficient condition making `cor:intro-identity-frontier`
unconditional) **+** `WALL` (the zero-target right crossing `g*` is *never*
identity-dominant for a field-drop row) **+** exact failure map. **NO new
`COUNTEREXAMPLE`:** the sole exponential obstruction is the paper's own
`thm:smooth-quotient-obstruction`, which this packet re-derives and *locates*
inside the parameter space.

One-line headline: **the complete profile envelope beats the identity term on
exactly the band `((c-1)/(c-lambda))*H2 < g*beta < (1/lambda)*H2` around the
entropy crossing, where `(c,lambda)` is the row's cheapest complete-fiber
folding and its scaled-coefficient-field drop; identity-dominance is PROVED in
the two complementary windows (and everywhere when there is no field drop,
`lambda=1`, e.g. a prime image field), while the zero-target crossing `g*` sits
dead-centre in the failure band whenever `lambda<1` --- so the corollary's
identity specialization is unconditional precisely for generous targets
`tau >= tau0(rho,beta,c,lambda) > 0`.**

**Boundaries respected.** scottdhughes `(MI)`/`(MA)`/entropy-inverse
(#498/#501/#505) consumed as input, never attacked. Danny #529, latifkasuli
#518 untouched. Codex Lean envelope *definitions* (#517) not overlapped --- this
is a research criterion, not a formalization.

**Credit / differentiation.**
- **PR #524** (`asymptotic_profile_envelope_audit.md`) verified the obstruction
  *construction* reproduces exactly at `GF(11^2),GF(13^2),GF(17^2),GF(23^2)` and
  flagged the window criterion as the tractable target --- *theirs audits the
  counterexample; this packet proves the criterion and maps where dominance
  fails.*
- **LegaSage #520** (`profile_envelope_vs_target.json`,
  `hard_input:"d"`) audited the envelope formula
  `E = 1+(n-a+1)+sum(1+barN)` at *statement level*: dual-route exact integer
  redeploy, `E_complete > E_identity` on multi-profile toys, four deployed rows
  `U(a0)>B*>=U(a1)`. Its nonclaims are explicit: *"Does not prove closed ledger
  or e^{o(n)} domination"* and *"identity-dominant window holds at deployed
  scale"* is a `does_not_assert`. **Theirs pins the formula and the brackets;
  this packet supplies the missing domination criterion and its boundary.**
- **PR #534/#536** census machinery (exact prefix keys, prime-field arithmetic)
  is the pattern reused for the `F_{p^2}` census in section 2. **#535/#539**
  settle the *per-cell payment* (`(A4)` coverage, `(FI)` image scale); this lane
  is the complementary *envelope-vs-target* side.

---

## 1. Rung 1 --- Anatomy (exact extraction, gated by `file:line`)

### 1.1 The complete profile envelope (`eq:profile-envelope`, L858--862)

For a received line `(r0,r1)` and agreement `a`, with `Lambda(r0,r1;a)` the
realized profiles whose first-match cells are nonempty,
```
   E_n(a) = 1 + (n - a + 1) + sup_{(r0,r1)} sum_{lambda in Lambda} (1 + barN_lambda),
   barN_lambda = |Omega^0_lambda| / L_lambda    (average full-slice fiber at realized image scale).
```
The three summands are the **universal** term `1` (tangent floor), the **deep**
term `n-a+1`, and the **profile sum**. The sum *"includes the identity profile
and all quotient, Chebyshev, planted, and remainder profiles that meet that
line"* (L867--868); with subexponentially many profiles *"the sum and maximum
have the same exponential scale"* (L869--870).

### 1.2 The identity term (`prop:exact-prefix-list` L1965; `eq:target-entropy` L6108--6112)

The identity profile's scale is the exact prefix-list size
```
   barN_1(a) = C(n,a) * |B|^{-(a-k-1)},        w := a-k-1 = prefix equations,
   (1/n) log2 barN_1 = H2(rho+g) - beta*g + o(1),   rho=k/n, beta=log2|B|, a=k+1+gn+O(1).
```
So on the exponential scale the identity exponent is `e_1 := H2(rho+g) - g*beta`
with agreement fraction `alpha = rho+g` and prefix rate `g = w/n`.

### 1.3 The dominance premise `(A7)` and `cor:intro-identity-frontier`

`(A7)` (`def:admissible-sequence` item 7, L946--953): the envelope *"including
all quotient subfields B_phi with phi(D) subset eta*B_phi (the scaled quotient
coefficient fields) ... is used in the final budget; **it is not replaced by the
identity term unless that comparison is proved for the row.**"*

A window is **identity-dominant** (L1004--1008) when *"the entire profile
envelope is, up to e^{o(n)}, bounded by the identity scale together with the
universal constant and deep terms."* `cor:intro-identity-frontier` (L1010--1050)
consumes exactly
```
   (IDW)    E_n(a) <= e^{o(n)} ( 1 + (n-a) + barN_1(a) ).
```
Under (IDW) the frontier reduces to the one-variable crossing
`g*(rho,beta)=sup{g: H2(rho+g) >= beta*g}` and `delta* = 1-rho-g* + o(1)`.

### 1.4 The printed counterexample (known-false-in-general)

The paper flags (IDW) as false in general in three places, all pointing to the
same construction:
- L889--890: *"The countertheorem is exactly a row for which a quotient profile
  in `E_n` is exponentially larger than the ambient identity term."*
- `thm:smooth-quotient-obstruction` (L3985+): the tower `B0=F_p subset B=F_{p^2}`,
  `n=2(p-1)`, `D=theta*H`, square folding `phi(x)=x^2` (`c=2`), gives an identity
  scale `1 <= barN_1 < |B|^2 = e^{o(n)}` (subexponential) but a square-fiber
  quotient family of scale `>= C(n/2,a/2) p^{-w/2} = exp((h(alpha)/4 + o(1)) n)`
  --- **exponentially larger.**
- `sec:expanded-ledger-proofs` L6948--6957: the quotient budget *"need not be
  comparable with the identity term; `thm:smooth-quotient-obstruction` gives an
  explicit exponential separation."*
- `cor:frontier-final` L6913--6922: the frontier *"reduces to the zero of
  `H2(rho+g)-beta*g` only in the stated identity-dominant, subexponential-target
  regime."*

The exponent engine is `prop:identity-quotient-comparison` (QR6--QR9,
L3884--3948): the depth-`c`, remainder-`r`, field-drop-`lambda_c` quotient
profile has **natural scale** (a *proved pigeonhole lower bound*, QR6 L3887--3894)
```
   barN_{c,r}(w) = C(N-|phi(R)|, m) * |B_phi|^{-floor(w/c)},   N=n/c, m=(a-r)/c,
```
and (QR8, L3911--3916)
```
   (1/n) log2 barN_{c,r}(w) = (1/c)( H2(rho+g) - g*beta ) + (g*beta/c)(1 - lambda_c) + o(1),
   lambda_c = log|B_c| / log|B| in (0,1].
```

---

## 2. Rung 2 --- Exact computation: which cell carries envelope value

### 2.1 Closed-form competitor exponent (algebraic identity, `PROVED`)

Rearranging QR8 (verifier section A, 4800 grid checks + the counterexample):
```
   e_c(rho,beta,g) = (1/c) [ H2(rho+g) - lambda_c * g * beta ] = (1/c)[ h - lambda_c * s ],
```
writing `h := H2(rho+g)`, `s := g*beta`. Sanity: at the identity crossing
`s=h` (so `e_1=0`), `c=2`, `lambda=1/2` gives `e_2 = h/4`, **byte-matching**
`thm:smooth-quotient-obstruction`'s exponent `h(alpha)/4`.

### 2.2 Envelope-exponent reduction (`PROVED`, given ledger-admissibility for the upper direction)

**Lemma (envelope exponent).** On the exponential scale
```
   (1/n) log2 E_n(a) = max( 0 , e_1 , max_{(c,lambda)} e_c ) + o(1).
```
*Proof sketch.* The `1` and `n-a+1` terms are linear in `n`, exponent `0`. The
profile sum is a sup over subexponentially many profiles, so its exponent is the
max over profiles of `(1/n)log2 barN_lambda`. Each **quotient/Chebyshev** profile
is budgeted at its natural scale `barN_{c,r}(w)` with exponent `e_c` (QR8, and
`sec:expanded-ledger-proofs` L6952--6955 *"Its correct budget is therefore its
own term barN_lambda"*). **Planted / remainder** profiles multiply a quotient
term by `<= 2^b` planted choices (L3866--3867) or, for `w>=r`, recover `R`
exactly (`thm:exact-quotient-remainder-normal-form`(i), L3486--3492; L3950--3960)
--- an `e^{o(n)}` perturbation, no new exponent. **Balanced-core / partial-
occupancy** profiles are bounded *by* the envelope via `(RC)` and the add-back
lemma (`thm:exact-partial-occupancy`, `lem:exact-profile-addback`), not new
terms. Hence the exponential competitors are exactly the field-drop quotient
terms `e_c`. `[]`
- **Lower (failure) direction is UNCONDITIONAL:** QR6 is a proved pigeonhole
  lower bound, so `E_n(a) >= barN_{c,r}(w) = exp(e_c n + o(n))` with no Sidon
  hypothesis.
- **Upper (domination) direction is CONDITIONAL** on the ledger-admissibility
  the compiler already assumes ((A2)/(A4): each profile's `barN_lambda` is at its
  proved natural scale; the matching upper bound is the Sidon/flatness content of
  `(A4)`, settled per-cell by #535). This is exactly the content of (A7)'s
  clause *"unless that comparison is proved for the row."*

**Corollary (dominance predicate).** Since identity is itself a profile and
`e_1 <= max(0,e_1)`, (IDW) holds iff **every** competitor obeys
```
   (DOM)     e_c(rho,beta,g) <= max( 0 , e_1(rho,beta,g) ).
```

### 2.3 Exact finite `F_{p^2}` census (`EXPERIMENTAL` evidence; scope: toy, illustrates the mechanism)

Verifier section E builds `D=theta*H` in `F_{p^2}` with the order-`n` subgroup,
the genuine 2-to-1 square folding, and enumerates. Attacks label:
`thm:smooth-quotient-obstruction` mechanism at exact small scale. Results (all
gated):

| p | n | a | c | lambda | #sq-fiber supports C(N,m) | distinct prefixes | max quotient bucket | QR6 = ceil(C(N,m)/p) | identity avg barN_1 |
|---|---|---|---|--------|---------------------------|-------------------|---------------------|----------------------|---------------------|
| 5 | 8 | 4 | 2 | 1/2 | 6 | 5 (= p) | 2 | 2 | 0.112 |
| 7 | 12 | 4 | 2 | 1/2 | 15 | 7 (= p) | 3 | 3 | 0.206 |
| 11 | 20 | 4 | 2 | 1/2 | 45 | 11 (= p) | 5 | 5 | 0.331 |

Every square-fiber support's locator prefix obeys **field-drop + lacunarity**:
`e_i(S)=0` when `c!i`, and `e_{cj}(S) in eta^j * F_p` (the scaled subfield),
so the whole quotient family's prefixes land in `(F_p)^{floor(w/c)}` --- at most
`p` values, confirmed exactly. Pigeonhole then forces a prefix bucket of size
`>= ceil(C(N,m)/p)` (QR6), while the identity per-bucket average is `barN_1<1`.
**The quotient cell carries the envelope value (2, 3, 5); the identity cell
carries less than one.** For `p in {5,7}` the full `C(n,a)`-support identity
enumeration confirms the same prefix bucket, as an identity bucket, exceeds the
identity per-bucket average.

---

## 3. Rung 3 --- The window criterion (`PROVED`)

Solve (DOM) for the worst competitor. `e_c=(h-lambda s)/c` is decreasing in `c`
(numerator `>=0`) and in `lambda`, so the binding competitor is the row's
**cheapest** folding `c_min` with its **deepest** field drop `lambda_min`. Write
`(c,lambda)=(c_min,lambda_min)`.

**Theorem (identity-dominance window).** Let a ledger-admissible row have
smallest complete-fiber folding degree `c>=2` and scaled-coefficient-field drop
`lambda = log|B_c|/log|B| in (0,1]` (set `lambda=1` if no folding lands in a
proper scaled subfield). Then (DOM) --- hence (IDW), given admissibility ---
holds exactly on the union of two windows in the prefix rate `g` (equivalently
`s=g*beta`, `h=H2(rho+g)`):
```
   LOWER window:   s <= kappa_low  * h,   kappa_low  = (c-1)/(c-lambda)  in (0,1],
   UPPER window:   s >= kappa_high * h,   kappa_high = 1/lambda          in [1,inf).
```
*Proof.* Two cases of `max(0,e_1)`.
- **Case A, `e_1>=0` (`h>=s`):** (DOM) is `(h-lambda s)/c <= h-s`
  `<=> s(c-lambda) <= h(c-1) <=> s <= h(c-1)/(c-lambda) = kappa_low*h`. Since
  `kappa_low<=1`, this sub-window lies in `{s<=h}`, consistent with Case A.
- **Case B, `e_1<0` (`h<s`):** RHS `=0`, (DOM) is `h-lambda s <= 0`
  `<=> s >= h/lambda = kappa_high*h`. Since `kappa_high>=1`, consistent with `s>h`.
Between the edges (`kappa_low*h < s < kappa_high*h`) no case is satisfiable, so
(DOM) fails. `[]`

Verifier section B checks the closed-form windows against a brute exponent scan
over `(rho in {.15,.30,.45,.60}) x (beta in {.5,1,2,3,5}) x (c in {2,3}) x
(lambda in {.25,.5,.75,1}) x 60` values of `g`: `band == brute` at every point,
and `lambda=1` is dominant everywhere.

**Clean sufficient conditions (each `PROVED`, ledger-visible):**
1. **No field drop (`lambda=1`).** Then `kappa_low=kappa_high=1`, the band is a
   single point `s=h`, and (DOM) holds for all `g` (with equality at the
   crossing, absorbed by `e^{o(n)}`). **A prime image field `B` (no proper
   subfield) forces `lambda=1`**, as does any row on which no complete-fiber
   folding `phi` has `phi(D)` inside a proper `eta*B_c`. In this case
   `cor:intro-identity-frontier` is **unconditional on the entire admissible
   window**, including the crossing `g*`.
2. **Generous target (target-threshold form).** For a field-drop row
   (`lambda<1`), the general right crossing `g_T` solving
   `F(g)=H2(rho+g)-beta*g = tau` lands in the LOWER window iff
   ```
      tau >= tau0 := F(g_low),   g_low solves  g*beta = kappa_low * H2(rho+g),
   ```
   and `tau0 = F(g_low) > 0` because `g_low < g*` (verified section D). So for
   every target with normalized bit rate `tau_n = (1/n)log2(1+B*_n) >= tau0`,
   the crossing is identity-dominant and `delta* = 1-rho-g_T+o(1)` holds
   unconditionally (given admissibility). This is the *"beta/target above a
   threshold"* window: **large budgets pull the crossing left, into the
   identity-dominant region.**

---

## 4. Rung 4 --- Failure map (`PROVED` unconditionally on the failure side)

**Failure band.** For a row with cheapest field-drop folding `(c,lambda)`,
`lambda<1`, identity-dominance **provably fails** (envelope exponentially exceeds
the identity RHS, via the unconditional QR6 lower bound) exactly on
```
   kappa_low * H2(rho+g) < g*beta < kappa_high * H2(rho+g),
   i.e.   (c-1)/(c-lambda) * H2  <  g*beta  <  (1/lambda) * H2.
```
The binding competitor is the depth-`c` field-drop quotient; its excess over the
identity RHS is `e_c - max(0,e_1) > 0` throughout the band, peaking at the
crossing where `e_c - 0 = e_c = (1-lambda)h/c` (for `c=2,lambda=1/2`: `h/4`).

**Wall (`WALL`): the zero-target crossing is never identity-dominant.** The
right crossing of the frontier at zero target, `g* = sup{g: H2(rho+g)>=beta*g}`,
satisfies `s = g**beta = h = H2(rho+g*)` (it *is* the identity crossing). For any
`lambda<1` and any `c>=2`,
```
   kappa_low * h = (c-1)/(c-lambda) * h  <  h  <  h/lambda = kappa_high * h,
```
so `s=h` is **strictly inside** the failure band. Verifier section C confirms
this at every tested `(rho,beta,c,lambda)`. Hence for a field-drop row the
corollary's identity specialization is **unavailable at the crossing** used to
state `delta* = 1-rho-g*`; only the target-threshold window (rung 3, item 2) or
a no-field-drop row (item 1) rescues it. This is the precise, named boundary of
the "known-false-in-general" premise.

**Failure realized (`thm:smooth-quotient-obstruction`).** That construction is
the point `c=2, lambda=1/2`, `s=h` (its `w` is chosen so `barN_1` is
subexponential, i.e. exactly the crossing). It sits at the band's centre with
excess `h/4`. This packet adds *no new floor*; it shows the printed
counterexample is the deepest point of a two-parameter band, and everything
outside the band is safe.

### 4.1 Dead cheap routes (checked)
- **"Take beta large to escape."** No: for fixed field-drop `(c,lambda<1)` the
  crossing `g*` is in the band for *every* `beta` (section C sweeps `beta` up to
  5). Increasing `beta` moves `g*` but never out of the band; only a *target*
  `tau>0` (not the field size) shifts the *applied* crossing into the window.
- **"Higher folding degree `c` is harmless."** Weakly true (larger `c` widens
  the safe lower window, `kappa_low=(c-1)/(c-lambda)` increasing in `c`), but any
  finite `c` still leaves `g*` in the band when `lambda<1`; `c` does not remove
  the wall.
- **"Planted/remainder profiles could dominate independently."** No: they are
  `e^{o(n)}` perturbations of a quotient term (2.2), never a new exponent.
- **"Second moment / raw support count closes it."** No --- excluded by
  `def:closed-asymptotic-ledger` L1120--1122 (*"a support-pair moment alone does
  not close a ledger"*); the envelope is a distinct-slope statement.

---

## 5. Per-claim label ledger

| # | Claim | Status |
|---|-------|--------|
| C1 | `e_c=(1/c)(H2(rho+g)-lambda*g*beta)` equals QR8; `=h/4` at the CE crossing | `PROVED` (algebra; verifier A) |
| C2 | Envelope exponent `= max(0,e_1,max e_c)`; competitors are field-drop quotients only | `PROVED` (reduction 2.2); upper direction `CONDITIONAL` on (A2)/(A4) admissibility |
| C3 | (IDW) `<=>` (DOM) `e_c <= max(0,e_1)` for all competitors | `PROVED` |
| C4 | Window = `{s<=kappa_low*h} U {s>=kappa_high*h}`, `kappa_low=(c-1)/(c-lambda)`, `kappa_high=1/lambda` | `PROVED` (verifier B: band==brute) |
| C5 | `lambda=1` (prime image field / no scaled-subfield folding) `=>` global dominance, corollary unconditional | `PROVED` |
| C6 | Failure band `(kappa_low*h, kappa_high*h)`; envelope provably exceeds identity there | `PROVED` unconditionally (QR6 pigeonhole lower bound) |
| C7 | Zero-target crossing `g*` (`s=h`) strictly inside the band for every `lambda<1` (WALL) | `PROVED` (verifier C) |
| C8 | Target-threshold: `tau>=tau0=F(g_low)>0` `=>` crossing in lower window, corollary unconditional | `PROVED` (verifier D) |
| C9 | `F_{p^2}` census: quotient cell carries `>=ceil(C(N,m)/p)`; identity avg `<1` | `EXPERIMENTAL` evidence, toy scope (verifier E) |
| C10 | No new obstruction floor beyond `thm:smooth-quotient-obstruction` | `AUDIT` |

---

## 6. Proposed paper changes --- ledger entries (for `experimental/asymptotic_rs_mca.md`; NO tex edits here)

> **Entry: identity-dominance window criterion (hard input d).**
> **Source:** this packet (`envelope_identity_window.md`,
> `verify_envelope_window.py`). **Status:** `PROVED` (criterion + wall) /
> `CONDITIONAL` (upper direction on (A2)/(A4)) / `EXPERIMENTAL` (toy census).
> **Paper impact (suggested, not applied):**
> 1. After `cor:intro-identity-frontier` (L1050), add a remark stating the
>    explicit window: with cheapest folding `(c,lambda)`, (IDW) holds iff
>    `g*beta <= ((c-1)/(c-lambda))H2(rho+g)` or `g*beta >= (1/lambda)H2(rho+g)`,
>    and record the **prime-image-field / `lambda=1`** sufficient condition that
>    makes the corollary unconditional on the whole window.
> 2. Strengthen the `cor:frontier-final` scope clause (L6920) from *"only in the
>    stated identity-dominant regime"* to the quantitative form: unconditional
>    when `tau_n >= tau0(rho,beta,c,lambda)` (target-threshold window), i.e. the
>    zero-target reduction fails precisely at small targets because `g*` is the
>    band centre.
> 3. Cross-reference `prop:identity-quotient-comparison` (QR8/QR9) as the exact
>    engine: the failure band is `((c-1)/(c-lambda))h < s < h/lambda`, and
>    `thm:smooth-quotient-obstruction` is its centre point `c=2,lambda=1/2,s=h`.
> **Nonclaims.** Does not prove the (A4) Sidon upper bound (that is the per-cell
> payment, #535); does not close the deployed finite rows; the census is a toy
> illustration, not a deployed-scale statement.
> **Next action:** a human/PI re-derivation of the reduction lemma (2.2), then
> (if accepted) fold items 1--3 into the corollary's statement so the frontier's
> conditional scope is a checkable inequality on `(rho,beta,c,lambda,tau)`.

---

## 7. Flagged for PI re-derivation

1. **The reduction lemma (2.2)** --- that field-drop quotient terms are the only
   exponential competitors --- rests on the paper's own claims that
   planted/remainder are `e^{o(n)}` (L3866--3867, L3950--3960) and that
   balanced-core/partial-occupancy are envelope-bounded via `(RC)`/add-back.
   These citations should be re-checked at statement level before the criterion
   is promoted; the *failure* side (C6/C7) does not depend on the lemma and is
   unconditional.
2. **Upper-direction conditionality** --- (DOM) `=> ` (IDW) uses (A2)/(A4) to
   place each profile at its natural scale. Confirm this is the same
   admissibility the compiler already assumes (it is, per `(A7)`), so the
   criterion adds no hidden hypothesis.
3. **`kappa_low` monotonicity / `g_low<g*`** --- used for `tau0>0` (C8);
   verified numerically on the tested grid, worth a one-line analytic check.

**Recommended next lane.** *Lower reserve / unsafe-side comparison* (hard input
e): the unsafe test `prop:simple-pole-lower` (`P(a)`) is the mirror of this
envelope side; the same field-drop quotient list feeds the *lower* construction,
so a "quotient-list reserve" criterion --- when a field-drop quotient list
strictly beats the identity list on the unsafe side --- would pair with this
window to close both brackets of `thm:unconditional-support-envelope-bracket`.
