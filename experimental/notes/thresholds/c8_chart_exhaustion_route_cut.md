# C8 first-match chart construction and exact four-bucket exhaustion

**Date:** 2026-07-21  
**Lane:** `gptpro/c8-chart-exhaustion`  
**Activity:** `FORMALIZE` one hard input: exhaustive first-match/residual chart coverage.  
**Status:** `PROVED FINITE ROUTE CUT / PARTIAL EXHAUSTION / CONDITIONAL RS INSTANTIATION`  
**Authority:** current fork `main` at `4e5f0b77c98f075ea7c8822cd4859847a232bc2a`,
`experimental/grande_finale.tex` (Grande Finale v4), and the integrated
stdlib-only prefix-atlas/first-match modules.

## Claim

Fix one received line and a finite, duplicate-free list of realized C8 chart
keys.  Supply:

1. an explicit semantic owner function with codomain `Option C8EarlierOwner`,
   where `C8EarlierOwner` has exactly the constructors C1 through C7;
2. one chart key designated as the supplied shallow closure input; and
3. for any chart already proved to be a genuine one-parameter locator pencil,
   an optional moving-root incidence certificate.

Classify a key in the following fixed order:

```text
earlier C1--C7 owner
  > the one supplied shallow key
  > certified one-parameter moving-root chart
  > DEEP_HIGHER_DIMENSIONAL_BALANCED_CORE_AFTER_C1_C7_SHALLOW_AND_ONE_PENCIL_DELETION.
```

Then the four classifier fibres are a duplicate-free, exhaustive partition of
the supplied realized chart keys.  Every key belongs to exactly one fibre, and
each fibre has an exact `iff` characterization.  In particular, the deep fibre
is exactly the complement of the first three tests; it is named but not paid.

For a supplied one-pencil certificate with `N` available moving points, `h`
moving roots per counted slope, and actual distinct-slope count `z`, the finite
interface stores the division-free incidence inequality

```text
z * h <= N.
```

Whenever `N < 3*h`, this implies `z <= 2`.  At the active `n=2^21` MCA
calibrations this applies to

```text
Mersenne-31: h = 981128,
KoalaBear:   h = 981104.
```

## Exact object and quantifiers

The Lean object is

```text
C8ChartExhaustionPacket Key
```

with fields

```text
keys                    : List Key
keys_nodup              : keys.Nodup
earlierOwner            : Key -> Option C8EarlierOwner
suppliedShallowKey       : Key
onePencilCertificate    : Key -> Option C8MovingRootCertificate.
```

The theorem is finite and universal over the key type and over every packet
carrying those fields.  No field, denominator, support multiplicity, or
received-line quantifier is hidden: those semantic data are not inferred by
this finite compiler and remain obligations of an RS instantiation.

The classifier itself constructs the post-deletion route cut.  It does not take
a pre-partition or disjointness proof as input.  Duplicate freedom follows from
`keys_nodup` and the integrated fibre-atlas theorem; coverage follows because
the classifier is total; first-match coverage follows from the integrated
`firstMatchLeaves` theorem.

## Four buckets

### (a) Earlier owned

A key is in the first bucket exactly when

```text
key in keys
and exists owner : C8EarlierOwner,
    earlierOwner key = some owner.
```

The owner type has only C1--C7 constructors.  Merely assigning a constructor is
not an RS classification theorem; a concrete packet must construct the owner
function from its semantic chronology.

### (b) Supplied shallow closure

A key is in the shallow bucket exactly when

```text
key in keys
and earlierOwner key = none
and key = suppliedShallowKey.
```

Thus there is only one shallow chart key in the classifier interface, and an
earlier owner wins if the supplied key was already absorbed.  This is the
finite route-cut shape consumed by the shallow C8 producer after integration;
this packet deliberately does not import open PR #1020.

### (c) Paid bounded chart

A key is in the bounded-pencil bucket exactly when

```text
key in keys
and earlierOwner key = none
and key != suppliedShallowKey
and exists certificate,
    onePencilCertificate key = some certificate.
```

The certificate records the actual chart slope count and the moving-root
incidence inequality.  It is the finite cross-multiplied interface of
`thm:bc-moving-root` and `cor:bc-one-pencil`.  The certificate does not assert
that an arbitrary chart is a pencil; the slope-to-pencil injection and genuine
locator-pencil semantics must be proved before constructing it.

### (d) One named deep residual

A key is in the final bucket exactly when

```text
key in keys
and earlierOwner key = none
and key != suppliedShallowKey
and onePencilCertificate key = none.
```

The bucket name is exactly

```text
DEEP_HIGHER_DIMENSIONAL_BALANCED_CORE_AFTER_C1_C7_SHALLOW_AND_ONE_PENCIL_DELETION
```

and is regression-locked in Lean and in the JSON certificate.  This packet does
not apply deep-prefix MI/MA, primitive Q/SP, a curve-degree compiler, or any
direct deep ray theorem to this class.

## Exact finite calibration

The executable calibration has four chart keys:

| key | earlier owner | supplied shallow | moving-root certificate | bucket |
| --- | --- | --- | --- | --- |
| `earlierC4` | C4 | no | none | earlier |
| `suppliedShallow` | none | yes | none | shallow |
| `movingPencil` | none | no | M31 `N=2097152`, `h=981128`, `z=2` | bounded pencil |
| `deepHigherDimensional` | none | no | none | named deep residual |

Lean proves that the bucket atlas is literally

```text
[[earlierC4], [suppliedShallow], [movingPencil], [deepHigherDimensional]].
```

The stdlib verifier independently replays the same priority rule, uniqueness,
incidence arithmetic, active-row cap-two calculations, and exact deep-residual
spelling from the shipped JSON certificate.

## Source-label map

| packet statement | active source boundary |
| --- | --- |
| total first-match disjointization | integrated `AsymptoticSpine.FirstMatch`; source `lem:first-match` / `def:cells` lineage |
| realized prefix/chart keys form a disjoint total atlas | integrated `AsymptoticSpine.PrefixAtlas`; prefix-atlas totality interface |
| moving-root cross-multiplied certificate | `experimental/grande_finale.tex`, `thm:bc-moving-root` |
| primitive one-pencil cap | `experimental/grande_finale.tex`, `cor:bc-one-pencil` |
| Q/SP do not automatically determine rays | `experimental/grande_finale.tex`, `prop:q-sp-no-ray` |
| nonautomatic ray boundary | `experimental/grande_finale.tex`, `hyp:ray-compiler` and `prop:curve-degree-ray-compiler` |
| current direct benchmark requiring exhaustive BC slope coverage | `agents.md`, Lane K3 |

The current source is Grande Finale v4.  The inherited v3 labels above are used
only where they remain the named theorem interfaces in that file; the packet
does not treat the older v3 global completion claim as current authority.

## Proof status and ledger impact

### PROVED

- fixed-priority construction of the four finite chart buckets;
- exact bucket membership formulas;
- duplicate-free flattened atlas;
- exact coverage of every supplied realized chart key;
- exact first-match coverage after `firstMatchLeaves`;
- unique bucket membership for each realized key;
- extraction of the original moving-root certificate from every bounded-pencil
  membership proof;
- generic `N < 3h` implication `z <= 2` from `zh <= N`;
- exact Mersenne-31 and KoalaBear active-row cap-two arithmetic; and
- a four-key executable calibration with exactly one named deep key.

### CONDITIONAL / external inputs

- the actual RS realized chart-key list on a received line;
- the semantic C1--C7 owner function;
- the field-specific reindexed prefix-fibre bridge and SE2 certificate for the
  supplied shallow key;
- proof that a bounded key is a genuine one-parameter locator pencil with
  slope-to-parameter injection;
- an actual common-core shortening certificate;
- any high-kappa earlier-owner theorem;
- profile count, residual add-back, line-local `UNIF`, target comparison, and
  an adjacent-row certificate.

### Explicit nonclaims

This packet does **not** prove:

- complete RS C8 chart construction over all received lines;
- that any late bucket is nonempty on every line;
- the open #1011 shortening/high-kappa semantic inputs;
- the open #1020 shallow `ProfilePayment` producer;
- deep-prefix MI/MA or Sidon payment;
- direct payment of the named deep residual;
- a higher-dimensional ray compiler;
- row-sharp Q, a deployed safe row, or Grande Finale row closure.

Accordingly the packet is a precise partial exhaustion result, not an
unconditional C8 payment theorem.  Its value is that the remainder is one exact
class rather than an informal phrase such as “all other charts.”

## Reproducibility

Lean module:

```text
experimental/lean/asymptotic_spine/AsymptoticSpine/C8ChartExhaustion.lean
```

Certificate and verifier:

```text
experimental/data/certificates/c8-chart-exhaustion/c8_chart_exhaustion.json
experimental/scripts/verify_c8_chart_exhaustion.py
```

Authoritative compilation is the fork draft-PR build on Lean 4.31.0, stdlib
only.  No local Lean build is used.  Green compilation checks the finite Lean
statements and their explicit inputs; it does not discharge the semantic RS
inputs listed above.
