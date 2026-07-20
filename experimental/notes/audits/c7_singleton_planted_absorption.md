# Singleton planted profiles can absorb the entire base-pole C7 class

## Claim

Under the planted-block cell grammar currently printed in
`experimental/asymptotic_rs_mca_frontiers.tex`, a fixed atlas of singleton-root
profiles can own every positive-agreement witness before C7.

For each evaluation point `t in D`, take the planted profile

```text
P_t(X) = X - t,
C_t(r) = {witnesses (gamma,S,h) on r with t in S}.
```

The profiles are fixed before the received line.  Every witness with nonempty
support belongs to at least one `C_t`, so an ordering of these C3 profiles before
C7 assigns every bad slope to C3 and leaves the later C7 first-match slope image
empty.

On the base-pole family

```text
q = 2^r,
D = F_q^x,
n = q - 1,
m = 2^(r-1) - 1 > 0,
```

there are `n = q - 1 = exp(o(n))` such profiles.  Each profile has at most
`q = exp(o(n))` distinct slopes.  The field-cardinality bound therefore pays
each realized profile from the additive `1` in its natural profile term, with a
uniform subexponential loss.  Consequently this is not merely a set-theoretic
cover: it is a paid earlier atlas at the asymptotic interface scale.

Thus the raw constant-coefficient theorem

```text
C_d -> singleton slope {-d}
```

does not imply a nonempty semantic C7 owner under the current broad atlas
grammar.  The deletion-aware C7 producer remains correct, but for this valid
earlier atlas its assigned list is empty.

## Status

`COUNTEREXAMPLE / SEMANTIC OWNER AMBIGUITY / PROVED INTERFACE REGRESSION`

The combinatorial first-match statement and finite closed-ledger fixture are
kernel-checked in
`AsymptoticSpine.C7SingletonPlantedAbsorption`.  The asymptotic payment argument
is the direct field-cardinality estimate below and uses only the printed
subexponential-profile convention.

## Parameters

The general argument requires:

```text
agreement a >= 1,
finite evaluation domain D of size n,
line field of size q_line,
log n = o(n),
log q_line = o(n).
```

The base-pole family has `q_line = q = n + 1`, so both logarithmic conditions
hold.

No extension field, interleaving, CA/list conversion, or protocol denominator
is used:

```text
q_gen = q_line = q,
D = F_q^x.
```

## Existing paper dependency

The counterexample uses the following printed interfaces from
`experimental/asymptotic_rs_mca_frontiers.tex`.

1. **Planted-block cell.**  A profile is determined by a polynomial factor `P`
   common to every support locator in the cell.  For `P_t=X-t`, the cell is
   exactly the supports containing `t`.
2. **Sublinear planted block.**  `lem:planted-entropy` says that when
   `|P|=o(n)`, the loss is absorbed into the subexponential profile factor.
   A singleton has size `1=o(n)`.
3. **Paid cell scale.**  A realized cell is paid when

   ```text
   |Z_i^o| <= U_i <= exp(o(n)) (1 + Nbar_i).
   ```

   Since `1+Nbar_i >= 1`, the direct bound `U_i=q_line` is paid whenever
   `log q_line=o(n)`.
4. **First match.**  A slope is assigned to the first cell containing one of
   its witnesses.  Hence one singleton-root witness in an earlier C3 profile is
   enough to delete all later witnesses at that slope.

The compact predecessor `experimental/asymptotic_rs_mca.tex` informally calls
C3 a positive-density planted block.  If that positive-density restriction is
intended to be semantic and mandatory, it must be stated in the authoritative
atlas definition; the broader frontiers grammar currently admits the singleton
profiles above.

## Proof idea

Fix any ordering `t_1,...,t_n` of `D`, before the received line is known.
For a received line `r`, let

```text
Z_j(r) = {gamma : some witness (gamma,S,h) has t_j in S}.
```

Every positive-agreement witness has `S != empty`.  Therefore, for every bad
slope `gamma`, choose any witness `(gamma,S,h)` and any `t_j in S`.  Then
`gamma in Z_j(r)`.  Thus

```text
union_j Z_j(r) = Z_a(r).
```

Ordered first-match disjointization gives

```text
Z_a(r) = disjoint_union_j Z_j^o(r),
```

before C7 is reached.  Hence

```text
Z_C7^o(r) = empty.
```

For payment, use the actual distinct-slope bound

```text
|Z_j^o(r)| <= q_line.
```

There are at most `n` realized singleton profiles, so line-locally

```text
sum_j |Z_j^o(r)|
  <= q_line * #{realized singleton profiles}
  <= exp(o(n)) * sum_j (1 + Nbar_j).
```

The `exp(o(n))` factor is uniform because both `n` and `q_line` are
subexponential.  This is a direct slope-image payment.  No support count, pair
moment, max-fibre estimate, or fixed-chart estimate is substituted for the MCA
numerator.

Indeed, first-match disjointness gives the sharper identity

```text
sum_j |Z_j^o(r)| = |Z_a(r)| <= q_line,
```

but the coarser per-profile bound already satisfies the printed paid-cell
interface.

## Ledger impact

This result changes the interpretation of the base-pole C7 work.

- `C7BasePoleProducer` and its rooted extension are valid deletion-aware
  adapters.
- They do not establish a nonempty C7 semantic owner.
- Under the printed broad planted-cell grammar, the fixed singleton-root C3
  atlas is an earlier paid owner and makes the C7 residual empty.
- Therefore a theorem asserting actual C7 survival must name a stricter,
  globally fixed atlas whose C3 grammar excludes this absorption.

The required order remains

```text
sup_line sum_profile,
```

because singleton-profile first match and the profile sum are performed inside
one received line before the outer supremum.

## Constants

For the base-pole family:

```text
number of fixed singleton C3 profiles = n = q - 1,
per-profile direct slope bound         = q,
coarse total direct budget             <= q(q - 1),
actual first-match total               <= q,
log(q(q - 1))                          = o(n).
```

At the finite Lean fixture:

```text
compilerLoss = 4,
three realized nonempty C3 profiles,
naturalTotal = 3,
budgetTotal  = 12,
badCount     = 4,
later C7 assigned slope list = empty.
```

## Reproducibility

Lean module:

```text
experimental/lean/asymptotic_spine/AsymptoticSpine/C7SingletonPlantedAbsorption.lean
```

Commands:

```text
cd experimental/lean/asymptotic_spine
lake build AsymptoticSpine.C7SingletonPlantedAbsorption
lake build
```

The executable fixture uses four witnesses with overlapping nonempty supports:

```text
(10,{0,1}), (11,{1,2}), (12,{2,3}), (13,{3,0}).
```

The four raw singleton-root slope cells are

```text
[10,13], [10,11], [11,12], [12,13].
```

With the raw C7 cell `[10,11,12,13]` placed last, first match is

```text
[10,13], [11], [12], [], [].
```

The final empty list is the assigned C7 image.

## Required semantic repair

At least one of the following must be made explicit before claiming a nonempty
base-pole C7 owner.

1. Restrict C3 to positive-density planted blocks.
2. Require planted factors to arise from a named row-dependent common-factor or
   resultant mechanism, excluding arbitrary singleton support roots.
3. Fix a canonical atlas that omits the singleton-root profiles and prove that
   choice before the received line.
4. Place the direct constant-coefficient saturation profiles before such
   sublinear planted profiles.
5. Accept that C7 is empty and record C3 as the semantic owner.

Without one of these repairs, `C7-SURV` is not merely unproved; it is false for a
valid paid atlas admitted by the printed grammar.

## Nonclaims

- This does not refute the raw base-pole singleton-slope theorem.
- This does not invalidate the deletion-aware C7 adapter.
- This does not prove that the maintainers intended singleton planted blocks to
  be semantic C3 owners; it proves that the current broad definition admits
  them.
- This does not change any finite deployed threshold or target comparison.
- This does not prove global row closure; it isolates an owner-definition
  ambiguity in the first hard input, the witness-exhaustive semantic atlas.
