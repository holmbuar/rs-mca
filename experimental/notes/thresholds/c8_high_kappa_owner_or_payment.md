# C8 high-kappa owner-or-payment compiler after common-core shortening

## Claim

Fix one actual first-match C8 balanced-core cell on one received line. Suppose a
fixed common agreement core has been removed by the slope-preserving shortening
map of `experimental/notes/thresholds/common_core_cover_obstruction.md`,
Theorem 2.1(2), and suppose the original and shortened support projections are
supplied as duplicate-free `(SE2)` certificates.

Then the following finite statements hold.

1. A support budget on the shortened chart pays the original distinct-slope
   cell with **no add-back factor**.
2. A direct `(RC)` inequality, or the kernel-independent shallow-prefix closure
   theorem, transfers from the shortened chart to the original slope cell with
   unchanged numerator, loss, average, and kernel label.
3. With original dimension `k`, factored core size `c`, shortened dimension
   `k-c`, residual common-core size `c_res`, and shortened kernel `kappa`, the
   exact ledger is

   ```text
   kappa = (k - c) - c_res.
   ```

   Only after the maximal common core is removed (`c_res=0`) may one write
   `kappa=k-c`.
4. For every cutoff `kappa_0`, if every cell with `kappa>kappa_0` has an earlier
   certified semantic owner and every cell with `kappa<=kappa_0` has a
   shortened support payment, then the original cell is either earlier-owned
   or budget-paid.
5. Under maximal-core removal, the high-kernel condition is exactly the
   small-core condition

   ```text
   kappa_0 < kappa  <->  c < k - kappa_0.
   ```

   Thus the owner theorem may equivalently be stated on the maximal common-core
   size.

## Status

`PROVED FINITE COMPILER / AUDIT / CONDITIONAL SEMANTIC OWNER`.

The Lean statements are proved in
`experimental/lean/asymptotic_spine/AsymptoticSpine/C8HighKappaOwner.lean`.
They contain no `sorry` and introduce no custom axioms. Authoritative
compilation is the fork draft-PR Lean build; no local Lean build is part of this
packet.

This packet does **not** prove the high-kappa semantic owner theorem, deep-prefix
`(MI)`/`(MA)`, a Sidon payment, actual chart exhaustion, or a deployed safe row.

## Parameters and ledgers

The compiler is deliberately finite and type-generic. A concrete consumer must
still print and keep separate:

```text
B                 generated/base field controlling locator coefficients
F                 ambient/codeword and slope field
q_line            line-sampling denominator
q_prof^w          natural prefix denominator
n, k, R=n-k       original RS row
K, c=|K|          factored common core
k'=k-c            shortened dimension
c_res             residual common-core size after the chosen factor
kappa=k'-c_res    shortened error-union kernel dimension
U_owner           earlier-owner slope numerator, when that branch fires
U_C8              residual C8 distinct-slope numerator
```

No equality between these fields or denominators is asserted by the Lean
module.

## Existing paper dependency

The source-side fixed-core construction is Theorem 2.1(2) of
`experimental/notes/thresholds/common_core_cover_obstruction.md`. It maps

```text
(gamma, S, h)
  -> (gamma, S \ K, (h-g0-gamma*g1)/Q_K)
```

and proves preservation of slope, exact agreement, noncommonness, error
support, and depth-`w` locator prefix. The factor-aware kernel correction is
recorded in
`experimental/notes/audits/balanced_core_factored_rank_audit.md` and in the
corrected `balanced_core_kappa_growth.md` / `a4_covers_high_kappa.md` notes.

The existing Lean input is
`AsymptoticSpine.HighKappaCoverage`: shallow-prefix closure depends on ambient
slice data and not on the kernel-dimension label. The new module supplies the
missing fixed-core add-back and owner-or-payment composition around that input.

## Proof idea

### Exact shortening certificate

`SlopePreservingShortening` stores:

```text
original SE2 certificate
shortened SE2 certificate
support-shortening map
exact equality of the duplicate-free slope lists
exact image description of the support lists
commutation of the chosen support-for-slope maps
```

Because the slope lists are literally equal, the original numerator is the
shortened numerator. The shortened `(SE2)` support injection therefore pays the
original cell without multiplying by the number of core choices or by an
add-back constant.

### Factor-aware kernel arithmetic

`FactoredKernelLedger` records both the factored core and a possible residual
common core. The MDS rank formula is kept in the exact form

```text
shortenedDimension = originalDimension - factoredCoreSize
kernelDim = shortenedDimension - residualCoreSize.
```

This blocks the stale inference `kappa=k` after shortening. If and only if the
full common core has been removed, `residualCoreSize=0` and
`kappa=k-factoredCoreSize`. Natural-number arithmetic then gives the exact
high-kernel/small-core equivalence.

### Owner-or-payment composition

Split on `kernelDim<=cutoff`.

- On the small-kernel branch, apply the supplied shortened support budget and
  the zero-loss add-back theorem.
- On the high-kernel branch, apply the supplied earlier-owner theorem.

The result is the literal C8 terminal

```text
earlier semantic owner OR original distinct-slope numerator <= budget.
```

## Ledger impact

The packet adds **no numerical ledger atom**. It supplies a proof-carrying
composition rule that future C8 packets may use without confusing:

- raw versus shortened dimension;
- support count versus distinct-slope count;
- a fixed core versus the maximal common core; or
- shortened payment versus original-line add-back.

For shallow-prefix charts, the existing ambient closure theorem now compiles
through a supplied fixed-core shortening certificate to the original C8 slope
cell. For deep-prefix charts, the exact open input is unchanged: construct a
semantic earlier owner on the high-kernel branch or prove a direct natural-scale
payment.

## Constants

All compiler equalities are literal finite equalities. No asymptotic constant,
`e^{o(n)}` factor, or unstated ceiling is introduced. The finite fixtures use

```text
k=9, c=5, c_res=0, kappa=4   (small-kernel payment branch)
k=9, c=3, c_res=0, kappa=6   (high-kernel owner branch)
cutoff=4.
```

They are regression fixtures only, not RS field instances.

## Reproducibility

Authoritative validation is triggered by the fork draft PR and builds the
changed module as an explicit Lean target under
`experimental/lean/asymptotic_spine` with Lean `v4.31.0`, stdlib only.

The correspondence and proof-boundary audit is in
`experimental/lean/asymptotic_spine/C8_HIGH_KAPPA_OWNER_CORRESPONDENCE.md`.

## What to do next

Instantiate `SlopePreservingShortening` on one actual post-first-match C8 cell.
For that same fixed owner function, prove either:

```text
kappa > kappa_0 -> a concrete earlier paid semantic owner
```

or a direct deep-prefix natural-scale bound on the shortened residual. A
counterexample must preserve the received line, exact witness, common-core
shortening, first-match deletion, and distinct-slope projection; a raw prefix
support family is not a falsifier.
