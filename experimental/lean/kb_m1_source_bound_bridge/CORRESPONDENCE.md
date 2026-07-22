# Lean/source correspondence: KoalaBear v4 tangent source adapter

## Package boundary

`KbM1SourceBoundBridge.lean` imports only `Std`. It deliberately does not import
the existing `rs_mca_thresholds` package because that package has non-stdlib
transitive dependencies. The semantic translation theorem is therefore cited,
not duplicated or axiomatized.

## Source theorem

The source-bound semantic input is:

- `experimental/rs_mca_thresholds.tex`,
  `thm:exact-sparsification` and challenge-restricted equation (SP3);
- `experimental/lean/rs_mca_thresholds/RsMcaThresholds/ExactSparsification.lean`,
  `mcaBad_sub_mem_iff` and `exact_sparsification_challenge`.

Those statements prove that one codeword-pair translation chosen for the whole
received pair preserves the complete MCA-bad slope set, and that a non-column-far
pair admits a translated sparse pair with support union at most `n-a`.

The active packet fixes a public finite order and chooses the first such source
triple. That deterministic choice adds no mathematical hypothesis.

## Set-to-list interpretation

For the fixed translated pair, list each eligible source coordinate once and
map it to its coordinate ratio. The resulting list may repeat a slope. Every
slope in the source-coordinate tangent set occurs in the list, so the number of
distinct slopes is at most the list length. The source support cap gives list
length at most `n-a=981104`.

This duplicate-bearing enumeration is intentional: it avoids importing a
non-stdlib finite-set library while retaining the exact upper needed by the
bankability contract.

## Declaration map

| Lean declaration | Source claim |
|---|---|
| `TangentSourceData` | the eligible source-coordinate list, ratio map, and exact `length ≤ n-a` source cap |
| `tangentImageEnvelope_length_eq` | coordinate mapping preserves the enumeration length |
| `mem_tangentImageEnvelope_iff` | every enumerated ratio has an eligible source coordinate and conversely |
| `paidEnvelope_length_le_tangentCharge` | filtering to bad ratios leaves at most `981104` entries, hence at most that many distinct paid slopes |
| `firstOwner` | the frozen tangent, Q, balanced-core, residual chronology |
| `firstOwner_cases` | every affine slope receives one constructor-valued owner or `outside` |
| `activeOwner_cases_of_bad` | every bad affine slope is in one of the four active cells |
| `firstOwner_unique`, `activeOwners_pairwiseDisjoint` | first-match uniqueness and pairwise disjointness |
| `deployedConstantsExact` | `n-a=981104`, positivity, budget fit, and exact remaining reserve |
| `activePaymentIsStrictlySmallerThanLegacy` | only the new tangent atom is banked; the legacy total is not imported |

## Proof-status boundary

The changed Lean module proves the finite-list image bound, constructor-valued
first-match kernel, and exact integer arithmetic with no axioms. It does not
reprove the already checked semantic translation theorem, and it does not prove
a row-sharp upper for the active Q, balanced-core, or final residual cells. It
also does not transport the legacy M1 owner chronology.

Expected `#print axioms` output for every declaration listed above is `[]`.
