# Singleton planted profiles and the C7 semantic-owner boundary

**Status:** `HISTORICAL-GRAMMAR COUNTEREXAMPLE / PROVED FINITE REGRESSION / ACTIVE SEMANTIC REPAIR`

## Claim and current interpretation

The now-archived broad atlas grammar in
`archived/asymptotic_rs_mca_frontiers.tex` admitted a predetermined common
support divisor `P` and treated sublinear planted factors as a subexponential
profile cost. Under that permissive historical reading, a fixed catalogue of
singleton roots

```text
P_t(X) = X - t,  t in D,
```

covers every positive-agreement witness before C7: each nonempty support
contains at least one `t`. Ordered first match can therefore assign all slopes
to those earlier C3 candidate cells and leave the later raw C7 image empty.

This remains a valid regression against an overbroad ownership rule, but the
archived grammar is not the active proof authority. The active repair in
`AsymptoticSpine.SemanticAtlasOwnership` requires a semantic C3 owner to carry a
certified row-derived profile. A witness-local singleton factor is only a
`WitnessLocalRefinement` and cannot create ownership by itself.

## Finite Lean regression

`AsymptoticSpine.C7SingletonPlantedAbsorption` uses four witness records:

```text
(10,{0,1}), (11,{1,2}), (12,{2,3}), (13,{3,0}).
```

The four raw singleton-root slope cells are

```text
[10,13], [10,11], [11,12], [12,13].
```

Appending the raw C7 cell `[10,11,12,13]` and taking ordered first match gives

```text
[10,13], [11], [12], [], [].
```

The final empty leaf is the assigned C7 image under that explicitly supplied
earlier order.

The module proves:

1. `singletonPlantedRawSlopeCells_eq`, the exact four raw candidate cells;
2. `singletonPlanted_absorbs_rawC7`, the exact ordered first-match leaves;
3. `singletonPlantedC3Line_totals`, with natural total `3` and direct budget
   `12` in the finite compiler-loss-`4` fixture;
4. `singletonPlantedRawC7_breaks_firstMatchOwnership`, showing that the
   untrimmed raw C7 payment duplicates all four slopes;
5. `noClosedLineLedger_with_singletonPlanted_then_rawC7`, excluding that
   duplicated profile list from `ClosedLineLedger`;
6. `singletonPlantedC3Ledger_compiles`, replaying the explicitly supplied
   earlier order through the line-local compiler.

## What the regression establishes

The base-pole raw theorem and ledger bridge remain valid. They pay the literal
post-earlier residual and permit that residual to be empty. What fails is the
stronger inference

```text
raw C7 payment exists
  => C7 must be a nonempty first-match owner independently of the atlas.
```

Conversely, the finite fixture does not authorize arbitrary singleton-root C3
owners in the active atlas. Such an owner must be constructed through a
`CertifiedC3Profile` whose provenance, post-deletion slope list, natural scale,
and payment are explicit.

## Historical asymptotic payment calculation

For provenance only, the archived base-pole discussion used

```text
D = F_q^×,
n = q - 1,
number of singleton candidate profiles = n,
per-profile direct distinct-slope bound <= q.
```

When `log q = o(n)`, both the catalogue size and direct field-cardinality loss
are subexponential. This explains why the old permissive grammar was a genuine
semantic ambiguity rather than a set-theoretic toy. It is not promoted here as
an active C3 theorem.

## Proof census

`C7SingletonPlantedAbsorption.lean` and
`SemanticAtlasOwnership.lean` contain:

```text
sorry / sorryAx placeholders: 0
custom axiom declarations:     0
Mathlib imports:               0
```

The modules print axiom dependencies for their load-bearing compiler theorems.
The fork draft-PR Lean check is authoritative for compilation.

## Nonclaims

- The packet does not prove that singleton-root profiles belong to the active
  semantic atlas.
- It does not prove a global C1--C9 atlas or completeness over all received
  lines.
- It does not prove C7 survivor nonemptiness or universal C7 emptiness.
- It does not establish row-wide `(UNIF)`, target comparison, an adjacent safe
  row, or row closure.
- It does not modify any active TeX proof authority.

## Required owner discipline

A later use must do one of the following explicitly:

1. construct a certified row-derived C3 profile and place it before C7;
2. choose a fixed semantic atlas whose C3 grammar excludes witness-local
   singleton factors;
3. place C7 before the relevant certified planted owner; or
4. accept that the certified earlier owner deletes the C7 residual.

In every case, deletion and the profile sum remain inside one received line
before the outer supremum.
