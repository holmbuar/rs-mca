# Heavy-fiber admissibility transfer: hereditary emission reduces to plain emission on the locator-prefix chart

## Status

`CONDITIONAL (the transfer) + PROVED core lemmas + route-scoped COUNTEREXAMPLE.
HARD INPUT 2 SERVED: image-scale MI+MA / direct Sidon payment (agents.md's five).
This packet decides the heavy-fiber interface obligation named in avdeevvadim's
PR #716 (primitive_signed_payment_barrier_v1.md Sec 3, 7.2;
owner_rooted_dense_band_localization_v1.md Sec 10): is the restriction of an
admissible first-match residual to a single heavy Phi-syndrome fiber itself an
admissible rooted profile AT THE ORIGINAL M/L NORMALIZATION -- i.e. does #716's
"hereditary" hypothesis reduce to plain (non-hereditary) emission for the
atlas's actual packets?  VERDICT (route-scoped): YES on the unprofiled
locator/power-sum prefix chart (eq:exact-power-sum-map) -- every heavy
Phi-syndrome fiber is a depth-R locator-prefix fiber, which the manuscript's
own prefix-to-line compiler realizes as an admissible rooted packet -- PROVIDED
R<char(B) when the power-sum presentation is used (elementary presentation:
every characteristic) and R<=m-2.  The reduction is NOT available via the
power-sum chart when R>=char(B): obstruction = Newton non-invertibility, and
the transfer must then go through the elementary locator chart.  Along the way
a sharpening: the band FAILURE transfers to the whole first-match residual b
directly (pigeonhole over the K_N complete bands), so the residual open gap is
purely rooted-packet admissibility of the submask, not band-failure transfer.`

Label key (agents.md dialect): **PROVED** / **CONDITIONAL** / **CONJECTURAL** /
**EXPERIMENTAL** / **AUDIT** / **COUNTEREXAMPLE**.  Every number below is
recomputed with exact arithmetic (Fraction / integer / GF(2^k)) by
`experimental/scripts/verify_heavy_fiber_admissibility_transfer.py`
(stdlib-only, deterministic, `--check` -> `RESULT: PASS (77/77)`,
`--tamper-selftest` catches `4/4`, ~0.06 s).  Machine-readable certificate:
`experimental/data/certificates/heavy-fiber-admissibility-transfer/heavy_fiber_admissibility_transfer.json`.
No `.tex`/`.pdf` is edited.  PR numbers are the consumed notes' own lane labels;
note files are cited by path and exist at this snapshot.

## Interfaces

This packet discharges, on the locator-prefix chart, the first of the two proof
obligations that **avdeevvadim's PR #716** leaves open in its "What remains
open" list (`owner_rooted_dense_band_localization_v1.md` Sec 10):

> ```text
> Heavy-fiber interface:
>   prove hereditary mask admissibility or a source-algebraic heavy-fiber inverse.
> ```

and the exact request of `primitive_signed_payment_barrier_v1.md` Sec 7.2 /
Thm 3.1 / Sec 8: "either require hereditary source-algebraic emission **or**
prove that a heavy source-fiber mask is an admissible owner-rooted input at the
original image normalization ... Removing `hereditary` would require an
additional lemma transferring a heavy fiber of the whole residual to an
admissible owner-rooted packet without Fourier cancellation from the other
fibers."  The transfer lemma is Sec 4-5 below; its four admissibility clauses
are #716's own (barrier Sec 8 guardrail: weighted Vandermonde columns / one
complete dyadic `|tau|` band / first-match residual mask / owners on one
received affine line).  The point-mass identity (barrier Prop 1.1) and the
uniform positive owner weight (barrier Sec 2) are re-derived exactly in check A.

Adjacent results used for orientation, credited to their authors' lanes:
**#713** (`experimental/notes/thresholds/atlas_cat_cell_ledger.md`) names class
**C8** as "a pair of equal-degree monic residual locators with a common depth-`w`
prefix" -- the balanced-core prefix structure whose single-fiber case is exactly
the object realized here; **#708**
(`experimental/notes/thresholds/rooted_order_two_band_reduction.md`) roots an
order-two band failure at an actual same-boundary residual support pair, the
zero-loss analogue of check A's whole-residual band failure; **#711**
(`experimental/notes/thresholds/exp_ilo_habitat_restriction.md`) isolates the
residual wall to image-denominator control -- the analytic content that survives
after this structural transfer is exactly its `q`-control.  The Newton
power-sum/elementary equivalence used here is the manuscript's own
(`asymptotic_rs_mca_frontiers.tex` L4137-4139, L4983-4986, eq:exact-power-sum-map
L4815-4819); it is the fiber form of `prefix_flatness_power_sum_lean.md`
(cited by #713).

---

## 1. Setup and conventions

Notation follows #716 / #708.  Let `\Omega^0` be a full profile slice, `M=|\Omega^0|`,
`\Phi:\Omega^0\to G` a prefix syndrome map into a finite abelian group of order
`H=|G|`, `L=|\Phi(\Omega^0)|`, and `\bar N=M/L`.  Let `\Omega^\circ\subseteq\Omega^0`
be the primitive first-match residual (`def:primitive-first-match-residual`),
`W=|\Omega^\circ|`, and

```text
f(s) = |\Omega^\circ \cap \Phi^{-1}(s)|,   b = the residual count function,
```

(so #716's `f=W\,1_{\{s_0\}}` is the pushforward of the single heavy fiber).
The nonzero dual is partitioned into complete symmetric dyadic `|tau|`-bands
`A`, `K_N=2+\lceil\log_2 n\rceil` of them (`n` = number of columns), with
`\delta_A=|A|/H` and `P_A` the (self-adjoint) band projection.  The band excess
is `R_A(f)=(L^{1-1/q}/M)\,\|P_A f\|_q`.

The **source chart** is the unprofiled locator/power-sum prefix chart
(`eq:exact-power-sum-map`, L4815-4819): for the moment curve `v_t=(t,\ldots,t^R)`
over the coefficient field `B`,

```text
\Phi(S) = \sum_{t\in S} v_t = (p_1(S),...,p_R(S)),    p_j(S)=\sum_{t\in S} t^j,
```

and the depth-`R` locator prefix is `\Phi_R(S)=(c_1(S),\ldots,c_R(S))`, the top
`R` coefficients of the monic locator `Q_S(X)=\prod_{t\in S}(X-t)` (equivalently
the elementary symmetric functions `e_1,\ldots,e_R` up to sign; manuscript
L559-568, L1224-1225).  Support size is `m=a`.

## 2. Sharpened gap lemma (PROVED)

### Lemma 2.1 (whole-residual band failure)

Let `b` be the count function of a full profile of mass `M` over `G`, and fix a
syndrome `s_0` with `b(s_0)=W`.  Then

```text
b(s_0) - M/H = \sum_A (P_A b)(s_0)                                        (2.1)
```

(sum over the `K_N` complete nonzero bands), hence some band `A^\star` satisfies

```text
|(P_{A^\star} b)(s_0)| >= (W - M/H)/K_N,     \|P_{A^\star} b\|_q >= |(P_{A^\star} b)(s_0)|,
```

and therefore

```text
R_{A^\star}(b) = (L^{1-1/q}/M)\,\|P_{A^\star} b\|_q
             >= (L^{1-1/q}/M)\,(W - M/H)/K_N.                            (2.2)
```

**Proof.** `(2.1)` is Fourier inversion at `s_0` minus the trivial character,
using `\hat b(0)=\sum_s b(s)=M`.  The pigeonhole and the pointwise bound
`\|g\|_q\ge|g(s_0)|` (`q\ge1`) give the rest. `\square`

**Consequence (the sharpening).** Under #716 Cor 1.2's heaviness
`WL/M\ge e^{2\eta N}` and `\log L/q=o(N)`, `(2.2)` gives
`R_{A^\star}(b)\ge e^{\eta N}` for the WHOLE residual `b`, not only for the
artificial point mask `f=W\,1_{\{s_0\}}`: with `L\le H`, `W\ge (M/L)e^{2\eta N}\ge (M/H)e^{2\eta N}\gg M/H`,
so `W-M/H\ge W/2` and `R_{A^\star}(b)\ge (WL/M)L^{-1/q}/(2K_N)\ge e^{2\eta N-o(N)}`.
This matches the point-mass scale of barrier Prop 1.1 exactly.  **So the "band-failure
transfer" half of the interface is closed: the open residual gap is purely the
rooted-packet admissibility of the fiber submask.**  Check A verifies `(2.1)`,
the pigeonhole, `(2.2)`, the point-mass identity `(P_A f)(s_0)=W\delta_A`, and
the uniform positive owner weight `c=\|P_A f\|_q/W>0`, exactly, on `G=(F_2)^5`.

(This does not root `b`: on the whole residual the norming-dual weights
`\omega(S)=\mathrm{Re}\,\overline{(P_A g)(\Phi(S))}` are signed -- this is exactly
#716's signed-payment boundary and the reason one restricts to a single fiber to
recover uniform positive rooting.)

## 3. The four admissibility clauses under fiber restriction

#716 (barrier Sec 8) calls a mask an admissible rooted packet when

```text
(i)   its columns are certified weighted Vandermonde columns;
(ii)  its orbit union is one complete dyadic |tau| band;
(iii) its mask is a first-match residual;
(iv)  its owner words lie on one received affine line.
```

Three of the four are **hereditary** -- preserved when a residual is restricted
to a fiber `\Phi^{-1}(s_0)`, because they are per-support or universally
quantified conditions closed under sub-collections:

```text
(i)   the columns v_t are the ambient moment columns; a fiber submask uses a
      sub-multiset of the SAME certified columns/weights.        [hereditary]
(ii)  the fiber pushforward W*1_{s0} is spectrally flat (|hat f(gamma)|=W for
      every gamma), so ANY single complete band receives it.     [hereditary]
(iv)  the owners of a sub-collection are a subset of the residual's owners, all
      on the same received line.                                 [hereditary]
```

Clause **(iii)** is the crux and is *not* automatically hereditary: restricting
to `\Phi^{-1}(s_0)` is a syndrome condition, not a slope-deletion condition, so
`\Omega^\circ\cap\Phi^{-1}(s_0)` need not be a first-match residual of the
original chart.  Sec 4 resolves it.

## 4. Fiber-coincidence and clause (iii) (PROVED, finite-verified)

### Theorem 4.1 (Newton fiber-coincidence)

Fix the source chart of Sec 1 with `R<\operatorname{char}(B)`.  Then for every
`s_0`,

```text
\Phi^{-1}(s_0) = \Phi_R^{-1}(z),     z = (Newton image of s_0),           (4.1)
```

i.e. the power-sum syndrome fiber equals a single depth-`R` locator-prefix
fiber.  Moreover any two distinct supports in it satisfy

```text
|S \cap S'| <= a - R - 1        (Johnson distance >= R+1).                (4.2)
```

**Proof.** Newton's identities relate `(p_1,\ldots,p_R)` and `(e_1,\ldots,e_R)`
by a triangular change of variables with diagonal `1,2,\ldots,R`, invertible
when `R<\operatorname{char}(B)` (manuscript L4137-4139, L4983-4986); this gives
`(4.1)`.  For `(4.2)`: if `|S\cap S'|=a-r` then `Q_S-Q_{S'}=\prod_{S\cap S'}(X-t)\cdot g`
with `\deg g\le r-1`; top-`R` agreement of `Q_S,Q_{S'}` forces
`e_j(S\setminus S')=e_j(S'\setminus S)` for `j\le R`, impossible for `r\le R`
(elementary symmetric determine an `r`-set), so `r\ge R+1`. `\square`

**Clause (iii) discharged on the prefix chart.** The residual restricted to the
fiber is a first-match EXCISION of one full-slice fiber -- "a first-match
residual only deletes supports from a full-slice fiber" (manuscript L3123,
`prop:effective-mi-ma-flatness` proof).  By `(4.1)` that full-slice fiber is the
complete depth-`R` prefix fiber `\Fcal_z`, which the manuscript's prefix-to-line
compiler realizes by **one** received line for `RS_F(D,m-R-1)` with the fiber,
slope set, and exact-`m` witness incidence in bijection (L695-705,
`thm:prefix-to-line-hardness`, `cor:exact-prefix-ray-realization`), valid for
`0<=R<=m-2` over any scalar extension `F` with `|F| - n > (m-R-1)\binom{|\Fcal_z|}{2}`
(the theorem's own size condition; carried here as (H3)).  The bijection makes the owners **distinct**, so on that line the
excised sub-collection is itself a whole first-match residual: each slope owns
exactly one support and the deleted (paid) supports are exactly the removed
slopes.  Thus all four clauses hold for the fiber submask, and the normalization
is unchanged (`M=|\Omega^0|`, `L=|\Phi(\Omega^0)|` are source-side; only `k`
becomes `m-R-1`).

**Census (check B, PROVED for the tabulated instances).** For `F_p`,
`p\in\{7,11,13\}`, `d\in\{2,3\}`, `a=d+2`, the power-sum and elementary
partitions of `C(T,a)` coincide, `#ps-fibers=#es-fibers`, and the Johnson bound
`(4.2)` holds:

| p | d | a | \|C(T,a)\| | ps-fibers | es-fibers | heaviest fiber | max\|S∩S'\| | a−d−1 | coincide |
|---|---|---|-----------|-----------|-----------|----------------|-------------|-------|----------|
| 7 | 2 | 4 | 35   | 28   | 28   | 2 | 1 | 1 | yes |
| 7 | 3 | 5 | 21   | 21   | 21   | 0 | 0 | 1 | yes |
| 11| 2 | 4 | 330  | 110  | 110  | 3 | 1 | 1 | yes |
| 11| 3 | 5 | 462  | 451  | 451  | 2 | 0 | 1 | yes |
| 13| 2 | 4 | 715  | 169  | 169  | 7 | 1 | 1 | yes |
| 13| 3 | 5 | 1287 | 1105 | 1105 | 3 | 1 | 1 | yes |

(Over these small fields `\binom{p}{a}\le p^d` forces most `d=3` fibers to be
light; the STRUCTURAL claims -- coincidence, Johnson, clause heredity -- hold for
every fiber regardless of size.  Genuine exponential heaviness is exhibited
separately in Sec 7.)  Check B also verifies the three hereditary clauses on a
deterministic mock residual (excision, sub-multiset columns, one prefix label).

## 5. Transfer theorem (CONDITIONAL)

### Theorem 5.1 (hereditary reduces to plain emission on the prefix chart)

Assume the source chart of Sec 1 and:

```text
(H1) the chart is the unprofiled locator/power-sum prefix chart (eq:exact-power-sum-map);
(H2) power-sum coordinates are used only when R<char(B); otherwise the elementary
     locator coordinates are used (this is exactly clause (i) / def:admissible-sequence (A5));
(H3) R <= m-2, and the realizing line is taken over a scalar extension F of the
     line field satisfying |F| - n > (m-R-1)*C(|F_z|,2), where |F_z| is the
     prefix-fiber cardinality (this is L695-705's own realizability condition;
     for exponentially heavy fibers the extension is mandatory and large);
(H4) the packet is a genuine primitive first-match residual whose atlas (A2) is
     witness-exhaustive on the depth-R prefix chart (so "earlier cell" is meaningful).
```

Then every heavy `\Phi`-syndrome fiber submask `f=W\,1_{\{s_0\}}` of the residual
is an admissible rooted packet (clauses (i)-(iv)) at the original `M/L`
normalization.  Consequently **#716's hereditary source-algebraic emission
hypothesis reduces to plain (non-hereditary) emission**: applying plain emission
to the per-fiber realizing line (a whole first-match residual by Sec 4) yields
the same rooted semantic packet #716 asks hereditary emission to produce.

**Proof.** Under (H2), Theorem 4.1 gives `\Phi^{-1}(s_0)=\Fcal_z` (power-sum via
Newton, or elementary by definition).  Sec 3 gives clauses (i),(ii),(iv);
Sec 4 gives clause (iii) via L3123 + L695-705 under (H3),(H4).  The point mass
roots with uniform positive weight (barrier Sec 2), so the realized packet is a
genuine admissible rooted profile. `\square`

**Scope.** This is a reduction of #716's *interface hypothesis*, not a proof of
the source-algebraic emission theorem itself: it removes "hereditary", leaving
#716's plain emission / charge-preserving signed-or-semantic dichotomy exactly
as stated.  (H4) is the one clause that is atlas-internal rather than
self-contained; it is (A2) for the prefix chart and is discharged by
ledger-admissibility, not re-proved here.

## 6. Char-boundary route-cut (COUNTEREXAMPLE to the power-sum route when R>=char)

### Proposition 6.1 (power-sum route is dead for R>=char)

When `R>=\operatorname{char}(B)` the power-sum syndrome fiber is in general NOT a
single locator-prefix fiber, so the transfer of Sec 5 is unavailable via the
power-sum chart; obstruction = Newton non-invertibility (the diagonal
`2,\ldots,R` meets `0` modulo the characteristic).

**Witness (check C, exact).** Over `GF(8)=F_2[x]/(x^3+x+1)`, `d=R=3`, `a=4`, the
power-sum partition of `C(T,4)` has 35 classes while the elementary partition has
63: they **split**, and 28 power-sum fibers merge `>=2` distinct prefixes.  The
supports

```text
S1 = {0,1,2,4},   S2 = {3,5,6,7}
```

share power sums `\Phi(S_1)=\Phi(S_2)=(7,3,7)` but have distinct locator prefixes
`\Phi_3(S_1)=(7,5,3)\ne(7,6,1)=\Phi_3(S_2)` (`e_1=7` agrees, as `p_1=e_1` in every
characteristic; `e_2,e_3` diverge because `p_{2j}=p_j^2` collapses in char 2 --
manuscript `rem:binary-ambient-image`).  So `\Phi^{-1}(7,3,7)` is not a
locator-prefix fiber; a depth-3 realization does not apply to it.

This does **not** refute Theorem 5.1: (H2) mandates the elementary chart here,
on which `\Phi_3^{-1}(z)` is a prefix fiber by definition and the transfer holds.
The proposition is precisely the demonstration that hypothesis (H2)
`R<\operatorname{char}(B)` is **necessary and load-bearing** for the power-sum
presentation, matching (A5) L939 ("Every use of power-sum coordinates satisfies
`R_N<\operatorname{char}B_N`; small-characteristic leaves instead retain
elementary coordinates") and the caveat L4206-4207 ("no Newton-coordinate
equivalence between the elementary and power-sum fibers is asserted").

## 7. Heaviness witness (PROVED, finite)

To exhibit an actually exponential heavy fiber that is nonetheless a single
depth-1 prefix fiber, we replay the superincreasing construction of the adjacent
dense-band note (#716 Sec 6).  With `A_i=5^i`, `C=2\sum_i A_i+1`,
`T=\{A_i\}\cup\{C-A_i\}` (`|T|=2B`), `a=B`, and `\Phi(S)=\sum_{t\in S}t`
(a depth-1 power sum = `e_1`), check D verifies exactly:

| B | N=2B | a | M=C(2B,B) | L=(3^B+1)/2 | W=C(B,B/2) | s_0=BC/2 | max\|S∩S'\| | WL/M |
|---|------|---|-----------|-------------|------------|----------|-------------|------|
| 2 | 4  | 2 | 6   | 5   | 2  | 61     | 0 | 5/3     |
| 4 | 8  | 4 | 70  | 41  | 6  | 3122   | 2 | 123/35  |
| 6 | 12 | 6 | 924 | 365 | 20 | 117183 | 4 | 1825/231 |

The fiber at `s_0` is exactly the subset-sum level set, has constant `e_1=s_0`
(a single depth-1 prefix fiber), obeys `|S\cap S'|\le a-2` (Johnson `>=2`), and
`WL/M` grows like `(3/2)^B` -- an admissible heavy fiber discharged by Sec 5 with
`R=1<\operatorname{char}` and `k=a-2`, matching the note's realization.  This is
the fully worked instance of the transfer: heavy, admissible, and rooted, with no
appeal to hereditary emission.

## Nonclaims

- **Not** a proof of source-algebraic emission, the primitive Q / max-fiber
  inverse, A4, or the Proximity Prize.  Theorem 5.1 removes #716's "hereditary"
  qualifier; #716's plain emission / signed-or-semantic dichotomy remains open
  exactly as it stands.
- **Not** an image-scale MI/MA or Sidon payment.  The analytic content (#711's
  image-denominator `q`-control) is untouched; this packet is the structural
  transfer that precedes it.
- **Not** a claim that the whole residual `b` roots positively -- Sec 2 notes the
  whole-residual weights are signed; only the single-fiber submask roots
  positively.  Lemma 2.1 transfers the band FAILURE, not the positive rooting.
- Hypothesis (H4) is atlas-internal ((A2) for the prefix chart), assumed from
  ledger-admissibility, not re-proved here.  Theorem 5.1 is therefore
  **CONDITIONAL**, with its lemmas (2.1, 4.1) and the census / route-cut /
  heaviness witnesses PROVED.
- The realizing line lives over a scalar extension of the line field large
  enough for L695-705's condition `|F| - n > (m-R-1)*C(|F_z|,2)`; **no claim**
  that the original deployed line field suffices for exponentially heavy
  fibers.  The extension is the manuscript's own compiler device and is
  line-field-side only: the source-side objects `M`, `L`, the fiber, and the
  `M/L` normalization are field-unchanged (no `q_gen`/`q_line` merge).
- The census is exhaustive only for the tabulated `(p,d,a)`; it is finite
  evidence for the finite-field structural claims, not an asymptotic statement.
- No claim about char `<= R` beyond Prop 6.1's route-cut: the elementary chart
  still transfers there; only the power-sum presentation is cut.

## Consumers

- `asymptotic_rs_mca_frontiers.tex`: discharges the "hereditary" qualifier on
  the heavy-fiber input to `def:primitive-first-match-residual` /
  `def:admissible-sequence` (A2)/(A5) for the locator-prefix chart; paste-ready
  as a remark after `eq:exact-power-sum-map` (L4815-4819) and the prefix-to-line
  realization (L695-705).
- #716 (`primitive_signed_payment_barrier_v1.md`, `owner_rooted_dense_band_localization_v1.md`):
  closes the first Sec-10 obligation (heavy-fiber interface) on this chart;
  sharpens the open gap (Lemma 2.1) to rooted-packet admissibility only.
- #713 (CAT ledger): the C8 single-fiber balanced-core case is realized;
  #708 (order-two rooting): the same-boundary residual pair is the order-two
  shadow of the whole-residual band failure (Lemma 2.1).
