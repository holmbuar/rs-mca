# C8 chart-exhaustion finite route-cut preflight

**Date:** 2026-07-21  
**Status:** `AUDIT / PROVED FINITE INTERFACE / PARTIAL EXHAUSTION / PENDING_FORK_CI`  
**Branch:** `gptpro/c8-chart-exhaustion`  
**Branch base:** fork `main@4e5f0b77c98f075ea7c8822cd4859847a232bc2a`  
**Lean target:** `AsymptoticSpine.C8ChartExhaustion`  
**Toolchain:** Lean 4.31.0, stdlib only.

## Audit question

Does the packet prove a duplicate-free, exhaustive four-way C8 route cut while
keeping all semantic hypotheses explicit and refusing to pay the nonautomatic
deep ray boundary?

**Verdict:** `PROVED FINITE ROUTE CUT / OPEN SEMANTIC RS INSTANTIATION`.

The module constructs the partition from a total fixed-priority classifier.  It
does not assume a pre-partition, but it does assume the finite realized key list,
the C1--C7 semantic owner function, the one supplied shallow key, and optional
moving-root certificates.  Those are exactly the field/semantic interfaces that
must be instantiated by later RS work.

## Files in the packet

```text
experimental/lean/asymptotic_spine/AsymptoticSpine/C8ChartExhaustion.lean
experimental/notes/thresholds/c8_chart_exhaustion_route_cut.md
experimental/notes/audits/c8_chart_exhaustion_preflight.md
experimental/data/certificates/c8-chart-exhaustion/c8_chart_exhaustion.json
experimental/scripts/verify_c8_chart_exhaustion.py
experimental/lean/asymptotic_spine/AsymptoticSpine.lean
experimental/lean/asymptotic_spine/README.md
experimental/agents-log-entry-gptpro-c8-chart-exhaustion.md
```

No path under `.github/` is modified.  The live shared
`experimental/agents-log.md` is not read, reconstructed, or changed.

## Imported API provenance

The Lean module imports only the integrated
`AsymptoticSpine.PrefixAtlas` module.  Its transitive first-match/list utility
inputs are also recorded because they are load-bearing.  The blobs below are
the blobs at both the exact branch base and current fork `main` when the packet
was authored.

| imported API | blob SHA |
| --- | --- |
| `experimental/lean/asymptotic_spine/AsymptoticSpine/PrefixAtlas.lean` | `d14c5fc6d93e0386fc9fb6ebfe0d0c3debc35cb1` |
| `experimental/lean/asymptotic_spine/AsymptoticSpine/FirstMatch.lean` | `44592371660c453c1f8522abb9c0f9364e4dd43d` |
| `experimental/lean/asymptotic_spine/AsymptoticSpine/Util.lean` | `5e09daceb9fa4d3fb72e3c59244ec348b51352c2` |

There is no import from open PR #1011, #1012, or #1020.  Small route-cut data
needed by this packet are restated locally.  Post-integration adapters to a
future shallow producer or high-kappa compiler can therefore be one-line
constructors rather than dependencies of this validation lane.

## Exact declaration audit

Namespace `AsymptoticSpine` unless otherwise shown.

### Bucket and moving-root layer

| declaration | exact proved statement | status |
| --- | --- | --- |
| `c8ChartBuckets_nodup` | The ordered labels `[earlier, shallow, boundedPencil, deepResidual]` are duplicate-free. | `PROVED` |
| `mem_c8ChartBuckets` | Every `C8ChartBucket` constructor occurs in the fixed bucket list. | `PROVED` |
| `C8MovingRootCertificate.slopeCount_le_two_of_three_mul_gt` | From `z*h <= N` and `N < 3*h`, conclude `z <= 2`. | `PROVED` |
| `C8MovingRootCertificate.m31Mca_slopeCount_le_two` | If `N=2097152` and `h=981128`, conclude `z<=2`. | `PROVED` |
| `C8MovingRootCertificate.koalaBearMca_slopeCount_le_two` | If `N=2097152` and `h=981104`, conclude `z<=2`. | `PROVED` |

The moving-root structure is an incidence certificate, not a theorem that a
concrete residual family is a projective pencil.  Its semantic construction is
an explicit nonclaim below.

### Classifier exactness

| declaration | exact proved statement | status |
| --- | --- | --- |
| `C8ChartExhaustionPacket.bucketAtlas_eq_cells` | The atlas is definitionally the four classifier fibres in fixed order. | `PROVED` |
| `C8ChartExhaustionPacket.mem_bucketCell_iff` | `key` is in bucket `b` iff `key` is realized and `classify key=b`. | `PROVED` |
| `C8ChartExhaustionPacket.classify_eq_earlier_iff` | Earlier iff an explicit C1--C7 owner is present. | `PROVED` |
| `C8ChartExhaustionPacket.classify_eq_shallow_iff` | Shallow iff no earlier owner exists and the key is exactly the supplied shallow key. | `PROVED` |
| `C8ChartExhaustionPacket.classify_eq_boundedPencil_iff` | Bounded pencil iff no earlier owner exists, the key is not the shallow key, and an original moving-root certificate is present. | `PROVED` |
| `C8ChartExhaustionPacket.classify_eq_deepResidual_iff` | Deep residual iff no earlier owner, no shallow match, and no one-pencil certificate exists. | `PROVED` |
| `C8ChartExhaustionPacket.mem_earlierCell_iff` | Exact earlier-cell formula including realized-key membership. | `PROVED` |
| `C8ChartExhaustionPacket.mem_shallowCell_iff` | Exact supplied-shallow-cell formula including first-match deletion. | `PROVED` |
| `C8ChartExhaustionPacket.mem_boundedPencilCell_iff` | Exact bounded-pencil-cell formula including certificate existence. | `PROVED` |
| `C8ChartExhaustionPacket.mem_deepResidualCell_iff` | Exact final-complement formula for the sole named deep class. | `PROVED` |

### Exhaustion and duplicate freedom

| declaration | exact proved statement | status |
| --- | --- | --- |
| `C8ChartExhaustionPacket.bucketAtlas_nodup` | The flattened four-cell atlas is `Nodup`. | `PROVED` |
| `C8ChartExhaustionPacket.mem_bucketAtlas_flatten_iff` | A key occurs in the flattened atlas iff it occurs in the realized-key list. | `PROVED` |
| `C8ChartExhaustionPacket.mem_firstMatch_bucketAtlas_iff` | The generic first-match leaves cover exactly the realized-key list. | `PROVED` |
| `C8ChartExhaustionPacket.existsUnique_bucket` | Every realized key belongs to exactly one bucket cell. | `PROVED` |
| `C8ChartExhaustionPacket.onePencilCertificate_of_mem` | Membership in the bounded-pencil cell returns the supplied certificate; the classifier cannot synthesize one. | `PROVED` |

### Named residual and executable calibration

| declaration | exact proved statement | status |
| --- | --- | --- |
| `c8DeepResidualName_exact` | Locks the exact residual spelling `DEEP_HIGHER_DIMENSIONAL_BALANCED_CORE_AFTER_C1_C7_SHALLOW_AND_ONE_PENCIL_DELETION`. | `PROVED` |
| `c8Calibration_classification` | The four calibration keys classify respectively as earlier, shallow, bounded pencil, and deep. | `PROVED` |
| `c8Calibration_bucketAtlas_exact` | The calibration atlas is literally `[[earlierC4],[suppliedShallow],[movingPencil],[deepHigherDimensional]]`. | `PROVED` |
| `c8Calibration_deepResidual_exact` | The only calibration key in the deep cell is `deepHigherDimensional`. | `PROVED` |
| `c8Calibration_exhaustive` | The executable atlas is duplicate-free and covers exactly its four keys. | `PROVED` |
| `c8Calibration_m31Pencil_paid` | The M31 calibration pencil has slope count at most two through the generic moving-root theorem. | `PROVED` |

## Source correspondence

| Lean object | source theorem/problem boundary |
| --- | --- |
| `bucketAtlas_nodup`, `mem_firstMatch_bucketAtlas_iff` | integrated first-match disjointization, source `lem:first-match` / `def:cells` lineage |
| `mem_bucketAtlas_flatten_iff` | integrated prefix-atlas totality |
| `C8MovingRootCertificate` and cap-two theorems | `experimental/grande_finale.tex`, `thm:bc-moving-root` and `cor:bc-one-pencil` |
| absence of a deep payment | `hyp:ray-compiler`, `prop:q-sp-no-ray`, and `prop:curve-degree-ray-compiler` boundary |
| semantic/global nonclaim | `agents.md`, Lane K3: exhaustive BC coverage in distinct affine-slope units remains a live input |

The source is now Grande Finale v4.  The packet formalizes the inherited finite
route-cut boundary and does not claim that the former v3 completion architecture
is unconditional.

## Duplicate-freedom audit

The order is semantic and fixed before enumeration:

```text
C1--C7 owner > supplied shallow > bounded pencil > named deep residual.
```

An earlier owner therefore removes a key even if it is also the supplied shallow
key or carries a pencil certificate.  The shallow key removes the key before a
pencil certificate is inspected.  Only the remaining keys reach the one-pencil
test.  The deep class is the exact complement.  Because the classifier has one
value and the key list is duplicate-free, the integrated fibre-atlas theorem
proves that the flattened buckets are duplicate-free.  Disjointness is a theorem,
not a prose remark.

## Certificate replay audit

The JSON certificate records:

- the exact base SHA and packet schema;
- the four fixed bucket names and priority order;
- one chart in each calibration bucket;
- the exact shallow chart ID;
- the exact deep residual spelling;
- the M31 moving-root certificate; and
- both active-row cap-two arithmetic checks.

`experimental/scripts/verify_c8_chart_exhaustion.py --check` recomputes the
classification and arithmetic from the JSON.  It rejects duplicate chart IDs,
wrong priority, multiple shallow/deep calibration keys, a mismatched expected
bucket, an invalid incidence inequality, or a false cap.  The script is a replay
certificate; Lean remains the proof validation authority.

## Axiom and source census

Static source census for the new Lean module before CI:

```text
Mathlib imports:              0
sorry:                        0
admit:                        0
sorryAx occurrences:          0
custom axiom declarations:    0
unsafe declarations:          0
native_decide:                0
```

The module ends with `#print axioms` for every load-bearing theorem and each
executable calibration theorem.  The expected dependencies are standard Lean
principles inherited from list equality/filtering and quotient-based list
reasoning.  The exact printed kernel output is not claimed until the fork draft
PR build completes.

## Kernel validation record

At authoring time:

```text
fork draft PR:          pending creation
explicit changed target: AsymptoticSpine.C8ChartExhaustion
package root target:    AsymptoticSpine
Lean version:           4.31.0
result:                 PENDING_FORK_CI
```

This section intentionally does not claim a green build before GitHub Actions
has run.  A green build will establish elaboration and kernel checking of the
Lean declarations only; it will not prove any external RS semantic field.

## Explicit nonclaims

The packet does not prove any of the following:

- a complete fixed-before-line RS C1--C8 semantic owner function;
- completeness over all received RS lines;
- a realized-profile count or row-uniform sum;
- nonempty late buckets on every line;
- the actual reindexed prefix-fibre/SE2 data of the supplied shallow chart;
- a shallow `ProfilePayment` or closed-ledger append from open PR #1020;
- an actual common-core shortening certificate or high-kappa owner from open
  PR #1011;
- a theorem that every bounded key is a genuine projective pencil;
- deep-prefix MI/MA, Sidon, primitive Q/SP, or direct deep ray payment;
- a higher-dimensional balanced-core ray compiler;
- exact residual add-back, target comparison, deployed adjacent-row closure, or
  an official score change.

## Final audit verdict

```text
PROVED FINITE ROUTE CUT
PARTIAL EXHAUSTION
OPEN SEMANTIC RS INSTANTIATION
PENDING_FORK_CI
```

The packet advances the chart-exhaustion hard input by replacing an untyped
“other C8 charts” remainder with one exact, duplicate-free residual class.  It
does not pay that class and therefore does not cross the nonautomatic ray
boundary.
