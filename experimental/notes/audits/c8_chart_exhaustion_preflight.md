---
workboard_item: K3
row: KoalaBear MCA
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: Audit the exact finite spine calibration theorem that constructs overlapping raw C8 charts, performs first-match deletion, classifies every chart into one of four buckets, pays only the supplied shallow and certified one-pencil leaves, and leaves one exactly named deep residual unpaid.
architecture: DIRECT
partition_digest: not-applicable-direct-finite-calibration
atom_or_cell: C8 chart exhaustion route cut
quantifier: Every chart key and every slope in the four-chart finite spine calibration.
projection_and_unit: Distinct affine-slope identifiers after first-match deletion.
claimed_bound: exact assigned cells [[5],[7,9],[11,13],[17]]; shallow 2<=12; one-pencil 2<=2; one unpaid deep slope [17].
status: AUDIT
impact: ROUTE_CUT
falsifier: Any mismatch between raw and assigned cells, duplicate charged slope, missing chart, additional deep class, shallow data not matching the PR-1020 fixture, or moving-root certificate not tied to the actual assigned pencil slopes.
replay: python3 experimental/scripts/verify_c8_chart_exhaustion.py --check; python3 -O experimental/scripts/verify_c8_chart_exhaustion.py --check; python3 experimental/scripts/verify_c8_chart_exhaustion.py --tamper-selftest; Lean validation only through the fork draft PR.
---

# C8 chart-exhaustion finite route-cut preflight

**Date:** 2026-07-21  
**Status:** `AUDIT / PROVED FINITE SPINE CALIBRATION / PARTIAL EXHAUSTION / GREEN_FORK_CI`  
**Branch:** `gptpro/c8-chart-exhaustion`  
**Branch base:** fork `main@4e5f0b77c98f075ea7c8822cd4859847a232bc2a`  
**Lean target:** `AsymptoticSpine.C8ChartExhaustion`  
**Toolchain:** Lean 4.31.0, stdlib only.

## 1. Audit question and result

Does the packet construct the **actual finite asymptotic-spine calibration**—not
an arbitrary four-label partition—and prove both chart-level and slope-level
first-match exhaustion while refusing to pay the nonautomatic deep ray boundary?

**Finite audit result:** yes.

The packet starts from the overlapping raw slope projections

```text
[[5], [5,7,9], [9,11,13], [13,17]]
```

and computes the post-deletion leaves

```text
[[5], [7,9], [11,13], [17]].
```

It then classifies the four realized chart keys, in the same order, as

```text
earlier C1 owner,
supplied shallow closure,
paid one-parameter moving-root chart,
DEEP_HIGHER_DIMENSIONAL_BALANCED_CORE_AFTER_C1_C7_SHALLOW_AND_ONE_PENCIL_DELETION.
```

The second leaf is exactly `highKappaToySE2.slopes`, with the same bridge,
syndrome key, inclusion, bounds, and kernel label used by the open #1020 C8
producer fixture.  The third leaf is exactly the slope list stored in its
moving-root certificate.  The fourth is the sole named and unpaid remainder.

The packet does **not** prove the deployed KoalaBear semantic owner function or
all-line C8 chart construction.  The finite calibration is proved; the global
K3 input remains open.

## 2. Complete upstream-intended packet

The validation branch contains every file intended for the eventual upstream
packet:

```text
experimental/lean/asymptotic_spine/AsymptoticSpine/C8ChartExhaustion.lean
experimental/lean/asymptotic_spine/AsymptoticSpine.lean
experimental/lean/asymptotic_spine/README.md
experimental/notes/thresholds/c8_chart_exhaustion_route_cut.md
experimental/notes/audits/c8_chart_exhaustion_preflight.md
experimental/data/certificates/c8-chart-exhaustion/c8_chart_exhaustion.json
experimental/scripts/verify_c8_chart_exhaustion.py
experimental/agents-log-entry-gptpro-c8-chart-exhaustion.md
```

No path under `.github/` is modified.  The shared
`experimental/agents-log.md` is neither read nor changed; the packet carries
only the required side-file suggestion.

## 3. Imported API provenance

The Lean module imports only integrated APIs:

```text
AsymptoticSpine.PrefixAtlas
AsymptoticSpine.HighKappaCoverage
```

Their load-bearing transitive dependencies are recorded below.  Each blob is
the exact blob at the branch base and current fork `main` when the packet was
constructed.

| imported API | blob SHA |
| --- | --- |
| `experimental/lean/asymptotic_spine/AsymptoticSpine/PrefixAtlas.lean` | `d14c5fc6d93e0386fc9fb6ebfe0d0c3debc35cb1` |
| `experimental/lean/asymptotic_spine/AsymptoticSpine/FirstMatch.lean` | `44592371660c453c1f8522abb9c0f9364e4dd43d` |
| `experimental/lean/asymptotic_spine/AsymptoticSpine/Util.lean` | `5e09daceb9fa4d3fb72e3c59244ec348b51352c2` |
| `experimental/lean/asymptotic_spine/AsymptoticSpine/EffectiveClosure.lean` | `9fb097e23d00e2f3ee3afeda021b86ba4192d2a4` |
| `experimental/lean/asymptotic_spine/AsymptoticSpine/HighKappaCoverage.lean` | `cdb17177fe7f17a7e8b520d999fa925c5abfaea0` |

There is no import from open PR #1011, #1012, or #1020.  The six-field shallow
input is restated locally with the same fields, so a post-integration adapter is
one record constructor and introduces no mathematical hypothesis.

## 4. Actual first-match construction audit

### 4.1 Raw charts are not already disjoint

The raw calibration contains deliberate overlaps:

| chart | raw slopes | overlap deleted by |
| --- | --- | --- |
| `earlierC1` | `[5]` | none |
| `suppliedShallow` | `[5,7,9]` | C1 deletes `5` |
| `movingPencil` | `[9,11,13]` | shallow deletes `9` |
| `deepHigherDimensional` | `[13,17]` | pencil deletes `13` |

This guards against a vacuous theorem that merely assumes four disjoint cells.
`C8ChartExhaustionPacket.postDeletionSlopeCells` is definitionally
`firstMatchLeaves [] rawSlopeCells`.

### 4.2 Exact assigned cells

`c8Spine_postDeletionSlopeCells_exact` proves

```text
postDeletionSlopeCells
  = [[5], c8SpineShallowInput.slopeCell.slopes,
     c8SpineMovingPencil.slopes, c8SpineDeepResidualSlopes]
  = [[5], [7,9], [11,13], [17]].
```

`c8Spine_postDeletionSlopeFlatten_exact` computes the flattened assigned list
as `[5,7,9,11,13,17]`.

### 4.3 Slope-level disjointness

`C8ChartExhaustionPacket.postDeletionSlopeCells_nodup` applies the integrated
first-match theorem and proves the flattened assigned slope list is `Nodup`.
`mem_postDeletionSlopeCells_iff` proves that deletion preserves exactly the raw
covered slope union.  Consequently there is neither double charging nor an
uncovered calibration slope.

## 5. Four-bucket classifier audit

The classifier order is hard-coded:

```text
some C1--C7 owner
  -> earlier
else exact shallow key
  -> shallow
else some supplied moving-root certificate
  -> boundedPencil
else
  -> deepResidual.
```

The four `classify_eq_*_iff` declarations prove the exact predicate of each
branch.  In particular:

- an earlier owner wins even if a later predicate also holds;
- only the exact supplied shallow key reaches the shallow branch;
- a one-pencil membership proof returns the original certificate; and
- the deep branch is the exact complement, not a catch-all with a hidden
  payment.

The integrated fibre-atlas theorem proves the chart-key buckets are duplicate-
free and cover exactly the realized keys.  `existsUnique_bucket` proves each
realized chart has one and only one bucket.

The closed computation

```text
c8Spine_bucketAtlas_exact
```

gives

```text
[[earlierC1], [suppliedShallow], [movingPencil],
 [deepHigherDimensional]].
```

## 6. Shallow #1020-input audit

The local `C8ShallowClosureInput` has exactly the producer-facing fields:

```text
bridge
syndromeKey
slopeCell
chartInclusion
bounds
kernelDim.
```

The calibration value is

```text
bridge        = affineToyBridge
syndromeKey   = 1
slopeCell     = highKappaToySE2
chartInclusion= by decide
bounds        = highKappaToyBounds
kernelDim     = 1000000.
```

Direct source checks:

```text
fullSlice            = [0,1,2,3,4]
syndrome fibre at 1  = [1,3]
raw translated key   = 11
SE2 supports         = [1,3]
SE2 slopes           = [7,9]
baseSize             = 2
prefixDepth          = 2
imageSize            = 3
effectiveSize        = 4
average              = 2
compilerLoss         = 4
naturalScale         = 3.
```

`c8Spine_shallowSlopes_exact` proves the supplied slopes are `[7,9]`, exactly
the second first-match leaf.  `c8Spine_shallow_paid` applies the integrated
kernel-independent shallow theorem and proves

```text
2 <= 4 * 3 = 12.
```

This is precisely the data consumed by #1020.  This packet does not duplicate
its closed-ledger extension or claim the open module is integrated.

## 7. One-pencil audit

`C8MovingRootCertificate` stores the actual assigned slope list, its `Nodup`
proof, available moving points, moving roots per slope, positivity, and the
cross-multiplied incidence inequality.

The general theorem proves

```text
z*h <= N and N < 3h  ->  z <= 2.
```

The calibration certificate is

```text
slopes = [11,13]
N      = 2097152
h      = 981104.
```

Both inequalities are exact integers.  `c8Spine_movingPencil_paid` proves the
actual assigned slope list has length at most two.  The verifier separately
checks that its claimed cap is exact, not merely safe:

```text
2h <= N < 3h.
```

The source-semantic premise that a deployed chart is a genuine projective
pencil with slope-to-parameter injection remains explicit.  No certificate is
manufactured for a chart lacking that premise.

## 8. Deep-boundary audit

The exact residual name is

```text
DEEP_HIGHER_DIMENSIONAL_BALANCED_CORE_AFTER_C1_C7_SHALLOW_AND_ONE_PENCIL_DELETION
```

and `c8DeepResidualName_exact` regression-locks it.
`c8Spine_deepResidual_exact` proves the unique deep calibration key is
`deepHigherDimensional` and its exact assigned slope list is `[17]`.

No declaration maps that chart to `DirectRC`, `A6RayCondition`,
`ProfilePayment`, Q, SP, MI, MA, a curve cover, or a higher-dimensional ray
bound.  This is deliberate.  The packet respects the boundaries named by

```text
hyp:ray-compiler
prop:q-sp-no-ray
prop:curve-degree-ray-compiler.
```

## 9. Exact PROVED declaration table

Namespace `AsymptoticSpine` unless shown otherwise.

| declaration | exact statement | source match |
| --- | --- | --- |
| `c8ChartBuckets_nodup` | Fixed four-bucket order is duplicate-free. | finite classifier |
| `mem_c8ChartBuckets` | Every bucket constructor is in the fixed order. | finite classifier |
| `C8ShallowClosureInput.slopes_paid` | Exact supplied `(SE2)` leaf is paid at `baseSize^prefixDepth*(1+average)`. | `EffectiveClosure`, `HighKappaCoverage`, #1020 input boundary |
| `C8MovingRootCertificate.slopes_length_le_two_of_three_mul_gt` | `zh<=N` and `N<3h` imply `z<=2`. | `thm:bc-moving-root` |
| `C8MovingRootCertificate.koalaBearMca_slopes_length_le_two` | KoalaBear active constants imply cap two. | `cor:bc-one-pencil` |
| `C8MovingRootCertificate.m31Mca_slopes_length_le_two` | M31 active constants imply cap two. | same finite specialization |
| `C8ChartExhaustionPacket.mem_bucketCell_iff` | Exact bucket membership formula. | finite classifier |
| `C8ChartExhaustionPacket.classify_eq_earlier_iff` | Earlier iff an explicit C1--C7 owner exists. | first-match semantic boundary |
| `C8ChartExhaustionPacket.classify_eq_shallow_iff` | Shallow iff no earlier owner and exact shallow key. | #1020 input boundary |
| `C8ChartExhaustionPacket.classify_eq_boundedPencil_iff` | Pencil iff earlier/shallow tests fail and a certificate exists. | moving-root boundary |
| `C8ChartExhaustionPacket.classify_eq_deepResidual_iff` | Deep iff all first three tests fail. | explicit residual cut |
| `C8ChartExhaustionPacket.rawSlopeCells_nodup` | Every raw chart projection is duplicate-free. | finite chart data |
| `C8ChartExhaustionPacket.postDeletionSlopeCells_nodup` | Flattened first-match leaves are duplicate-free. | integrated `FirstMatch` |
| `C8ChartExhaustionPacket.mem_postDeletionSlopeCells_iff` | First-match leaves cover exactly the raw slope union. | integrated `FirstMatch` |
| `C8ChartExhaustionPacket.bucketAtlas_nodup` | Flattened chart-key buckets are duplicate-free. | integrated `PrefixAtlas` |
| `C8ChartExhaustionPacket.mem_bucketAtlas_flatten_iff` | Chart-key buckets cover exactly the realized keys. | integrated `PrefixAtlas` |
| `C8ChartExhaustionPacket.existsUnique_bucket` | Every realized chart key has a unique bucket. | exact exhaustion |
| `C8ChartExhaustionPacket.onePencilCertificate_of_mem` | Bounded membership returns the original certificate. | non-oracular payment guard |
| `c8DeepResidualName_exact` | Locks exact deep-residual spelling. | route-cut requirement |
| `c8Spine_postDeletionSlopeCells_exact` | Computes `[[5],[7,9],[11,13],[17]]`. | finite spine calibration |
| `c8Spine_postDeletionSlopeFlatten_exact` | Computes `[5,7,9,11,13,17]`. | finite spine calibration |
| `c8Spine_firstMatchOwnership_nodup` | Assigned calibration slopes are duplicate-free. | first-match disjointness |
| `c8Spine_shallowSlopes_exact` | Shallow leaf is exactly `[7,9]`. | #1020 fixture |
| `c8Spine_shallow_paid` | Shallow leaf satisfies the direct finite closure bound. | #1020 producer input |
| `c8Spine_movingPencil_paid` | Pencil leaf satisfies exact cap two. | moving-root theorem |
| `c8Spine_classification_exact` | Four chart keys reach the four expected branches. | finite spine calibration |
| `c8Spine_bucketAtlas_exact` | One chart key occurs in each bucket. | exact chart exhaustion |
| `c8Spine_deepResidual_exact` | Unique deep key and exact slope `[17]`. | exact named residual |
| `c8Spine_everyChart_exactlyOneBucket` | Every realized calibration key has exactly one bucket. | exact chart exhaustion |

Every load-bearing declaration has a terminal `#print axioms` command.

## 10. Certificate and independent verifier

Canonical JSON:

```text
experimental/data/certificates/c8-chart-exhaustion/c8_chart_exhaustion.json
```

Verifier:

```text
experimental/scripts/verify_c8_chart_exhaustion.py
```

The verifier independently recomputes the raw-to-leaf deletion, bucket
classification, duplicate-freedom, exact shallow data, shallow payment,
KoalaBear pencil payment, both active cap-two specializations, imported blob
table, nonclaim set, and exact residual spelling.

The tamper self-test must reject five mutations:

1. changed deep name;
2. changed raw overlap/first-match leaf;
3. changed shallow `(SE2)` slope;
4. changed moving-root constant; and
5. changed bucket priority.

Python replay supports audit and packaging; it is not Lean validation.

## 11. Axiom and source census

Static source census for the new Lean module:

```text
Mathlib imports:              0
sorry:                        0
admit:                        0
sorryAx occurrences:          0
custom axiom declarations:    0
unsafe declarations:          0
native_decide:                0
```

The green build's terminal `#print axioms` output contains only standard Lean
principles:

- `propext` on the finite classifier, uniqueness, and closed computations;
- `Quot.sound` on list/filter, first-match, shallow-closure, and moving-root
  proofs; and
- `Classical.choice` only in the executable shallow/post-deletion fixtures that
  transitively use decidable finite-list constructions.

`c8DeepResidualName_exact` is axiom-free.  There are no custom axiom
declarations, `sorry`, `admit`, or `sorryAx` dependencies.

## 12. Kernel validation record

Fork draft PR #90 validated the complete upstream-intended packet at head
`ba47b3bf8b32744f12728b6ecbf589e8297f7d22` in workflow run
`29853996330` (`Lean build — PR #90`, run number 187).

The workflow first built the explicit changed targets:

```text
lake build AsymptoticSpine AsymptoticSpine.C8ChartExhaustion
```

and then built the package default target:

```text
lake build
```

Both invocations completed successfully with 30 jobs on Lean 4.31.0.  The build
artifact was `lean-build-log-0`, digest
`sha256:3003b219c5552d839f019da3026fc424a00f85bdea8b5b80c2cf11f216a5546a`.
The log contains no Lean errors.  Its only module-local diagnostics are
non-fatal unused-`simp`-argument linter warnings; they do not alter statements
or axiom dependencies.

Two earlier validation heads exposed stdlib-surface syntax issues and were
repaired without changing any theorem statement:

```text
225bf338...  unsupported by_contra tactic spelling
4e411264...  unsupported exists-unique notation
ba47b3bf...  explicit by_cases and expanded uniqueness statement; GREEN
```

Green CI proves elaboration and kernel checking of the Lean statements only; it
does not prove the external deployed-RS semantic inputs.

## 13. Explicit nonclaims

This packet does not prove:

- a complete deployed KoalaBear C1--C7 semantic owner function;
- C8 chart completeness over all received lines;
- deployed field-specific shallow prefix data;
- the actual RS common-core shortening certificate named by #1011;
- a high-kappa semantic owner;
- the #1020 `ProfilePayment` / closed-ledger producer;
- a general theorem that any bounded chart is a genuine one-parameter pencil;
- deep-prefix MI/MA, image-normalized Sidon, primitive Q/SP, or direct deep ray
  payment;
- a curve-degree or higher-dimensional balanced-core ray compiler;
- a realized-profile count, add-back, row-wide `UNIF`, target comparison,
  bankable `U_BC`, adjacent safe row, or official score change.

The exact remaining K3 theorem is a deployed, all-received-line instantiation
of this route cut—or a sharper direct theorem—in actual distinct-slope units,
with the named deep residual either proved absent, earlier-owned, or paid by an
independently justified ray theorem.

# OPEN GAP
