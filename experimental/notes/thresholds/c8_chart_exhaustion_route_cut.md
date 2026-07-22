---
workboard_item: K3
row: KoalaBear MCA
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: Every chart in the finite asymptotic-spine C8 calibration has one fixed-priority first-match bucket; its post-deletion slopes are duplicate-free; the shallow chart is exactly the PR-1020 input shape; the one-pencil chart has slope cap 2; the sole remainder is named and unpaid.
architecture: DIRECT
partition_digest: not-applicable-direct-finite-calibration
atom_or_cell: C8 chart exhaustion route cut
quantifier: Every chart key and every slope in the four-chart finite spine calibration.
projection_and_unit: Distinct affine-slope identifiers after first-match deletion.
claimed_bound: shallow slopes 2 <= 4*(1+2)=12; KoalaBear one-pencil slopes 2 <= floor(2097152/981104)=2; one named deep residual [17].
status: PROVED
impact: ROUTE_CUT
falsifier: A fifth chart key, a duplicate post-deletion slope, a shallow leaf other than [7,9], a one-pencil leaf not covered by its moving-root incidence certificate, or any unnamed/deep-paid remainder invalidates the claim.
replay: python3 experimental/scripts/verify_c8_chart_exhaustion.py --check; python3 -O experimental/scripts/verify_c8_chart_exhaustion.py --check; python3 experimental/scripts/verify_c8_chart_exhaustion.py --tamper-selftest; source base 4e5f0b77c98f075ea7c8822cd4859847a232bc2a.
---

# C8 first-match chart construction and exact four-bucket exhaustion

**Date:** 2026-07-21  
**Lane:** `gptpro/c8-chart-exhaustion`  
**Activity:** `FORMALIZE` the finite/exact part of C8 chart construction and
exhaustion.  
**Status:** `PROVED FINITE SPINE CALIBRATION / PARTIAL EXHAUSTION / CONDITIONAL DEPLOYED RS USE`.  
**Authority:** current fork `main@4e5f0b77c98f075ea7c8822cd4859847a232bc2a`,
`experimental/grande_finale.tex` (Grande Finale v4), and the integrated
`AsymptoticSpine.FirstMatch`, `PrefixAtlas`, `EffectiveClosure`, and
`HighKappaCoverage` APIs.

## 1. Exact target proved

The asymptotic spine already contains one finite shallow balanced-core
calibration:

```text
bridge       = affineToyBridge
syndrome key = 1
SE2 supports = [1,3]
SE2 slopes   = [7,9]
bounds       = highKappaToyBounds
kernel label = 1000000.
```

Open upstream PR #1020 consumes exactly those six fields as its C8 shallow
`ProfileData` fixture and turns the supplied chart into a `ProfilePayment`.
This lane works one step earlier: it constructs the complete finite
first-match chart environment around that exact shallow input and proves its
chart and slope exhaustiveness.

The raw chart projections, in fixed first-match order, are

```text
C1-owned candidate:                [5]
supplied shallow candidate:        [5,7,9]
one-parameter pencil candidate:    [9,11,13]
deep higher-dimensional candidate: [13,17].
```

Applying the integrated `firstMatchLeaves` construction gives the literal
post-deletion charts

```text
[[5], [7,9], [11,13], [17]].
```

The overlaps are load-bearing:

- slope `5` is deleted from the shallow candidate because C1 owns it first;
- slope `9` is deleted from the pencil candidate because the supplied shallow
  chart owns it first; and
- slope `13` is deleted from the deep candidate because the one-pencil chart
  owns it first.

Thus this is not four disjoint lists stipulated in advance.  It is an explicit
raw-chart construction followed by actual first-match deletion.

## 2. Four buckets

The classifier is fixed before enumeration and uses this strict priority:

```text
C1--C7 owner
  > supplied shallow chart
  > certified one-parameter moving-root chart
  > DEEP_HIGHER_DIMENSIONAL_BALANCED_CORE_AFTER_C1_C7_SHALLOW_AND_ONE_PENCIL_DELETION.
```

### 2.1 Earlier-owned chart

The first calibration chart has raw and post-deletion slope list `[5]` and the
explicit semantic label `C1`.  In the generic packet, a chart is earlier-owned
if and only if

```text
exists owner : C8EarlierOwner,
  earlierOwner chart = some owner,
```

where `C8EarlierOwner` has exactly the constructors C1 through C7.  The later
tests are not inspected on this branch.

This is a genuine finite semantic owner in the calibration.  It is not a
claim that the deployed KoalaBear row already has a complete C1--C7 owner
function; that remains external.

### 2.2 Supplied shallow closure

The second post-deletion chart is exactly `[7,9]`, the slope list in
`highKappaToySE2`.  Its data are a field-for-field restatement of the #1020
producer input:

```text
PrefixFiberBridge
syndromeKey
SE2Certificate
chartInclusion
ShallowPrefixClosureBounds
kernelDim.
```

No open-PR module is imported.  After #1020 integrates, the adapter is a
one-record-constructor map with no mathematical conversion.

The integrated shallow closure theorem proves

```text
2 = slopes.length
  <= 2^2 * (1+2)
  = 12.
```

The proof uses the actual bridge, support projection, `(SE2)` injection, chart
inclusion, full-slice mass, image size, effective size, and prefix-power bound.
The printed kernel label `1000000` is inert, exactly as required by the
kernel-independent shallow theorem.

### 2.3 Paid one-parameter moving-root chart

The third post-deletion chart is `[11,13]`.  It carries the finite
cross-multiplied incidence certificate

```text
slopes.length * movingRootsPerSlope <= movingPoints
2 * 981104 <= 2097152.
```

This is the exact finite interface of `thm:bc-moving-root` and
`cor:bc-one-pencil`.  Since

```text
2097152 < 3 * 981104,
```

three counted parameters are impossible, so the chart has at most two distinct
slopes.  The list itself has length two, hence the cap is attained in the
calibration.

The certificate is not synthesized by the classifier.  A bounded-chart
membership proof returns the original certificate.  For a deployed RS chart,
proving that the residual locators form a genuine projective pencil and that
the slope parameter injects into the pencil parameter remains a semantic
input.

### 2.4 Sole named deep residual

The fourth post-deletion chart is `[17]`.  Its exact name is

```text
DEEP_HIGHER_DIMENSIONAL_BALANCED_CORE_AFTER_C1_C7_SHALLOW_AND_ONE_PENCIL_DELETION
```

and both Lean and the JSON certificate regression-lock that spelling.

The class is the exact complement of:

```text
no C1--C7 owner,
not the supplied shallow chart,
no supplied one-pencil certificate.
```

There is exactly one such chart in the finite calibration.  It is named and
enumerated; it is **not paid**.

## 3. Duplicate freedom and exhaustion

There are two distinct disjointness statements.

### 3.1 Chart-key disjointness

The four classifier fibres form a duplicate-free partition of the realized
chart keys.  Every realized key belongs to exactly one bucket.  This follows
from the total fixed-priority classifier and the integrated fibre-atlas theorem.

### 3.2 Slope-level first-match disjointness

The raw slope projections overlap, so chart-key uniqueness alone would not be
enough.  The module separately applies the integrated first-match leaf
construction and proves

```text
postDeletionSlopeCells.flatten = [5,7,9,11,13,17]
```

and

```text
postDeletionSlopeCells.flatten.Nodup.
```

Therefore no distinct affine-slope identifier is charged to two buckets.
First-match ownership is a theorem of the packet, not a prose convention.
The same first-match theorem proves that deletion preserves exactly the raw
covered slope union.

## 4. Lean declarations

The implementation is

```text
experimental/lean/asymptotic_spine/AsymptoticSpine/C8ChartExhaustion.lean
```

The load-bearing declarations are:

| declaration | statement |
| --- | --- |
| `C8ShallowClosureInput.slopes_paid` | Pays the actual shallow `(SE2)` slope list at `baseSize^prefixDepth * (1+average)`. |
| `C8MovingRootCertificate.slopes_length_le_two_of_three_mul_gt` | From `z*h<=N` and `N<3h`, proves `z<=2`. |
| `C8MovingRootCertificate.koalaBearMca_slopes_length_le_two` | Specializes the moving-root payment to `N=2097152`, `h=981104`. |
| `C8ChartExhaustionPacket.classify_eq_*_iff` | Gives the exact predicate for each of the four buckets. |
| `C8ChartExhaustionPacket.postDeletionSlopeCells_nodup` | Proves duplicate-free assigned slopes after actual first-match deletion. |
| `C8ChartExhaustionPacket.mem_postDeletionSlopeCells_iff` | Proves deletion preserves exactly the raw slope union. |
| `C8ChartExhaustionPacket.bucketAtlas_nodup` | Proves duplicate-free chart-key ownership. |
| `C8ChartExhaustionPacket.mem_bucketAtlas_flatten_iff` | Proves chart-key exhaustiveness. |
| `C8ChartExhaustionPacket.existsUnique_bucket` | Proves every realized chart lands in exactly one bucket. |
| `C8ChartExhaustionPacket.onePencilCertificate_of_mem` | Returns the supplied certificate from bounded-chart membership. |
| `c8Spine_postDeletionSlopeCells_exact` | Computes `[[5],[7,9],[11,13],[17]]`. |
| `c8Spine_shallow_paid` | Pays exactly the #1020 shallow input leaf. |
| `c8Spine_movingPencil_paid` | Pays the one-pencil leaf at exact cap two. |
| `c8Spine_bucketAtlas_exact` | Computes one chart key in each bucket. |
| `c8Spine_deepResidual_exact` | Computes the sole deep chart and slope list `[17]`. |

Every load-bearing theorem is followed by `#print axioms` at module end.

## 5. Source-label map

| packet object | active source boundary |
| --- | --- |
| first-match slope leaves | integrated `AsymptoticSpine.FirstMatch`; `lem:first-match` / `def:cells` lineage |
| total chart-key fibres | integrated `AsymptoticSpine.PrefixAtlas` |
| shallow bridge and `(SE2)` payment | integrated `EffectiveClosure` and `HighKappaCoverage`; exact #1020 producer input boundary |
| one-pencil payment | `experimental/grande_finale.tex`, `thm:bc-moving-root`, `cor:bc-one-pencil` |
| refusal to infer rays from Q/SP | `experimental/grande_finale.tex`, `prop:q-sp-no-ray` |
| nonautomatic deep boundary | `hyp:ray-compiler` and `prop:curve-degree-ray-compiler` |
| live direct benchmark context | `agents.md`, K3: exhaustive balanced-core coverage in distinct affine-slope units |

Grande Finale v4 is the current architecture.  The listed labels are used where
the inherited theorem interfaces retain those names.  No archived or open-PR
module is treated as integrated authority.

## 6. Imported API blob table

The Lean module imports only integrated files.  These blobs are identical at
the exact branch base and current fork `main` when the packet was constructed:

| integrated API | blob SHA |
| --- | --- |
| `PrefixAtlas.lean` | `d14c5fc6d93e0386fc9fb6ebfe0d0c3debc35cb1` |
| `FirstMatch.lean` | `44592371660c453c1f8522abb9c0f9364e4dd43d` |
| `Util.lean` | `5e09daceb9fa4d3fb72e3c59244ec348b51352c2` |
| `EffectiveClosure.lean` | `9fb097e23d00e2f3ee3afeda021b86ba4192d2a4` |
| `HighKappaCoverage.lean` | `cdb17177fe7f17a7e8b520d999fa925c5abfaea0` |

There is no dependency on open PR #1011, #1012, or #1020.

## 7. Certificate replay

The canonical packet is

```text
experimental/data/certificates/c8-chart-exhaustion/c8_chart_exhaustion.json
```

and the independent stdlib verifier is

```text
experimental/scripts/verify_c8_chart_exhaustion.py.
```

It recomputes:

1. the fixed bucket priority;
2. raw-to-post-deletion first-match leaves;
3. duplicate-free chart IDs and assigned slopes;
4. exact raw and assigned slope lists;
5. exact #1020 shallow fixture data and arithmetic;
6. exact KoalaBear one-pencil incidence and cap;
7. both active MCA cap-two arithmetic checks;
8. one and only one deep chart; and
9. the exact deep residual spelling.

Its tamper self-test mutates the residual name, first-match overlap, shallow
slope list, moving-root constant, and bucket priority; every mutation must be
rejected.

## 8. Proof status and nonclaims

### PROVED

- construction of four overlapping raw chart projections at the finite spine
  calibration;
- exact post-deletion slope cells `[[5],[7,9],[11,13],[17]]`;
- chart-key and slope-level duplicate freedom;
- exact exhaustive and unique four-bucket chart classification;
- exact #1020 shallow input shape and direct finite shallow payment;
- exact one-pencil moving-root payment at cap two; and
- exact singleton named deep remainder.

### External named inputs

- a deployed RS C1--C7 owner function on every received line;
- deployed field-specific prefix bridge, `(SE2)` certificate, chart inclusion,
  and shallow bounds;
- proof that each bounded deployed chart is a genuine one-parameter locator
  pencil with slope-to-parameter injection;
- an actual RS common-core shortening certificate, the optional stretch goal
  named by #1011;
- any high-kappa semantic owner theorem;
- realized-profile count, add-back, `UNIF`, target comparison, and row
  certificate.

### Explicit nonclaims

This packet does **not** prove:

- deployed KoalaBear C8 exhaustion over all received lines;
- that any late bucket is nonempty on every line;
- the #1011 shortening/high-kappa semantic inputs;
- the #1020 `ProfilePayment` or closed-ledger append;
- deep-prefix MI/MA, image-normalized Sidon, primitive Q/SP, or direct deep ray
  payment;
- a curve-degree or higher-dimensional balanced-core ray compiler;
- an exact `U_BC` row atom, adjacent safe row, official score, or Grande Finale
  row closure.

The packet is therefore an exact finite route cut and a faithful producer
calibration, not a deployed-row payment.  The one residual is explicit and the
nonautomatic ray boundary is not crossed.
