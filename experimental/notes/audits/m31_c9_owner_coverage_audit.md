# Audit: deployed M31 C1--C8 owner coverage and all-key C9 loss-one packet

```yaml
workboard_item: M31_C9_GLOBAL_OWNER_COMPLEMENT_AND_KEY_COVERAGE / Lane A part 1
row: Mersenne-31 list auxiliary row
object: exact local Q-profile on eight deployed T_(2^21) roots
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: every actual post-C1--C8 key in the frozen 64-support residual has singleton full-prefix fiber
architecture: local first-match C1,C2,C3,C4,C5,C6,C7,C8
partition_digest: sha256:c6a154c32e8950762a992e8631bfa49e62762d43bf374cbf8674b5c417d3952e
atom_or_cell: post-C1--C8 C9 prefix keys
quantifier: every one of 70 supports and every one of 64 residual keys
projection_and_unit: support-prefix fiber cardinality; slope projection remains external
claimed_bound: 64/64 full fibers equal 1; no counterexample
status: PROVED_SCOPED / KERNEL_VALIDATION_PENDING
impact: acceptance criterion 2; predecessor one-key restriction removed on the exact local profile
falsifier: a residual key with full fiber size at least 2
replay: python3 experimental/scripts/verify_m31_c9_owner_coverage.py --check
```

**Date:** 2026-07-21  
**Branch:** `gptpro/m31-c9-owner-coverage`  
**Pinned fork base:** `4e5f0b77c98f075ea7c8822cd4859847a232bc2a`  
**Pinned upstream main:** `a3017697ad1594521d2779fe1d83bccd45d4c06e`  
**Audit verdict:** `FIXED`.

## 1. Scope and acceptance gate

Upstream PR #1027 proved one selected key, mask `51`, after a six-support C1
deletion.  Its named successor was
`M31_C9_GLOBAL_OWNER_COMPLEMENT_AND_KEY_COVERAGE`.

This packet performs the finite first half in full:

1. it defines executable local raw predicates for C1 through C8;
2. it applies the fixed priority order to all `70` weight-four supports;
3. it prints the complete owner decision table;
4. it forms the exact `64`-support owner complement;
5. it classifies every surviving realized key; and
6. it proves that all `64` have singleton full-prefix fibers.

No key is a counterexample.  The packet therefore satisfies criterion **2**:
it bounds genuine post-C1--C8 survivors.  It is not an interface-only packet.

## 2. Overlap audit

The ten latest upstream PR descriptions read before work were #1027, #1026,
#1025, #1024, #1020, #1014, #1012, #1011, #1009, and #1006.  The ten latest
fork draft descriptions were #78, #79, #76, #77, #75, #73, #74, #71, #70,
and #72.

Only #1027 owns this exact finite successor.  The nearby packets concern
effective-image MI+MA floors (#1024/#1026), the C8/C9 producer interface
(#1020), generic semantic-owner types (#1009), C7/C8 compilers
(#1011/#1012), or M31 padding and masked-diagonal terminals
(#1014/#1025).  None classifies all seventy supports or all sixty-four
surviving keys of this local profile.  No open-PR module is imported.

## 3. Imported API byte identity

The module has exactly two direct integrated package imports.

| imported API | fork-main blob | upstream-main blob | verdict |
|---|---|---|---|
| `experimental/lean/asymptotic_spine/AsymptoticSpine/PrimitiveBoolean.lean` | `777273e4377c31c815062769803622c6226988d3` | `777273e4377c31c815062769803622c6226988d3` | `BYTE_IDENTICAL` |
| `experimental/lean/m31_q_rooted_shell/M31QRootedShell/Deployed.lean` | `7e21ff098567d26aba7330fbb2722d5cb952fb09` | `7e21ff098567d26aba7330fbb2722d5cb952fb09` | `BYTE_IDENTICAL` |

Authority blobs used by the notes are:

| source | blob |
|---|---|
| `experimental/grande_finale.tex` | `8a5d9791900ca9eed773feba146b92ad296704ce` |
| `experimental/rs_mca_thresholds.tex` | `01302a797c502a05ed0b11ba949b8756e0aa2b22` |
| `tex/cs25_cap_v13_2.tex` | `5ceff5dbc4b1ac4cef53eae7eada32046e4bafeb` |

## 4. Package layout

```text
experimental/lean/sidon_effective_image/
  .gitignore
  lean-toolchain
  lakefile.lean
  lake-manifest.json
  SidonEffectiveImage.lean
  SidonEffectiveImage/M31C9OwnerCoverage.lean
```

The root imports only `SidonEffectiveImage.M31C9OwnerCoverage`.  The lakefile
requires only the integrated `asymptotic_spine` and `m31_q_rooted_shell`
packages.  The manifest records those path dependencies and the inherited
`staircase_logic` dependency.  No `.lake/`, generated build output, workflow,
or `.github/` file is included.

## 5. Exact first-match semantics

The first-match order is literal:

```text
C1 -> C2 -> C3 -> C4 -> C5 -> C6 -> C7 -> C8.
```

The local predicates and their proof boundaries are:

| case | executable local predicate | audit meaning |
|---|---|---|
| C1 | membership in the six unions of two antipodal pairs | exact complete fibers of `x -> x^2` |
| C2 | all four selected values have the same `T_4` value | exact complete `T_4` fibers |
| C3 | the active common core of all seventy supports is nonempty | exact planted block fixed throughout this profile |
| C4 | selected active values contain a duplicate | repeated-root active locator defect |
| C5 | active extension degree exceeds one | extension/descent branch |
| C6 | `6(b-a)(c-a)(c-b)=0 mod p` for the first three selected roots | rank drop of the active power-sum Jacobian |
| C7 | the full prefix fiber has size greater than one | effective-image collapse |
| C8 | the post-C1--C7 prefix fiber has size greater than one | surviving same-prefix balanced-core mate |

The raw counts are

```text
C1=6, C2=2, C3=0, C4=0, C5=0, C6=0, C7=2, C8=0.
```

Both C2 and C7 detect exactly masks `15` and `240`; C1 owns both first.  The
first-match census is therefore

```text
C1=6, C2=C3=C4=C5=C6=C7=C8=0, residual=64.
```

This is the actual executable owner function for the frozen local profile, not
the predecessor's generic constructor label.  It is not claimed to classify
other fixed-outside profiles or arbitrary received-line explanation states.

## 6. Exact PROVED declaration table

Namespace: `SidonEffectiveImage.M31C9OwnerCoverage`.

| declaration | exact statement and role |
|---|---|
| `fullPoints_complete` | `fullPoints` enumerates exactly all weight-four Boolean vectors on eight coordinates. |
| `fullPoints_nodup` | the complete slice is duplicate-free. |
| `residual_exact` | residual membership is exactly full-slice membership plus `earlierOwner = none`. |
| `firstMatchOrder_exact` | the priority list is exactly C1 through C8 in order. |
| `deployed_dimensions` | checks `p`, `w`, complement weight, fixed-outside size, availability, and `3 <= w`. |
| `domain_nodup` | the eight printed field elements are distinct. |
| `domain_points_are_deployed_roots` | every point satisfies `T_(2^21)(x)=0 mod p`. |
| `antipodal_pairs_exact` | the four displayed index pairs sum to zero modulo `p`. |
| `t4_fibers_exact` | the first and last four points have the two printed constant `T_4` values. |
| `full_slice_card` | the complete weight-four slice has cardinality `70`. |
| `full_image_card` | its first-three-power-sum image has cardinality `69`. |
| `common_active_core_empty` | the planted active common core is empty. |
| `active_extension_is_base_field` | the active extension degree is exactly one. |
| `raw_trigger_counts` | exact raw C1--C8 counts `6,2,0,0,0,0,2,0`. |
| `c2_raw_hits_preempted` | every raw C2 support is raw C1. |
| `c7_raw_hits_preempted` | every raw C7 support is raw C1. |
| `first_match_owner_counts` | exact first-match counts `6,0,0,0,0,0,0,0` and residual `64`. |
| `owner_table_card` | the executable owner table has one row per support, `70` total. |
| `residual_masks_card` | the residual mask list has cardinality `64`. |
| `residual_points_match_masks` | vector residual and mask residual agree exactly. |
| `residual_key_table_card` | the key certificate has `64` rows. |
| `residual_prefix_injective` | all residual realized keys are distinct. |
| `collision_full_fiber_exact` | the unique doubled full key `(0,2,0)` has masks `15` and `240`. |
| `collision_removed_by_first_match` | that doubled key has empty post-owner residual fiber. |
| `all_residual_key_rows_loss_one` | all 64 certificate rows have full and residual fibers exactly `[mask]`. |
| `no_counterexample_key` | the exhaustive counterexample mask list is empty. |
| `all_residual_rows_rowSharp` | every residual full fiber satisfies `length <= 1*2`. |
| `all_residual_rows_imageNormalized` | every residual key satisfies `fullFiber*69 <= 70`. |
| `loss_one_fits_deployed_budget` | exact integer comparison `2 <= 16777215`. |

The module ends with `#print axioms` for the owner complement, order,
deployed-domain checks, raw and first-match censuses, residual equality,
collision deletion, all-key loss-one theorem, empty falsifier, normalized
bound, and deployed budget comparison.

## 7. Machine certificate and replay

Files:

```text
experimental/data/certificates/m31-c9-owner-coverage/m31_c9_owner_coverage.json
experimental/scripts/verify_m31_c9_owner_coverage.py
```

The canonical compact JSON contains every one of the `70` owner rows and every
one of the `64` residual key rows.  Its partition digest is

```text
sha256:c6a154c32e8950762a992e8631bfa49e62762d43bf374cbf8674b5c417d3952e
```

and its current file digest is

```text
sha256:46713b57f47456fc7b07cf5d22a8ecd6e1ea8bade1b0484b96ae9fce699c3091
```

The independent stdlib verifier recomputes all arithmetic and exact tables.  It
uses explicit exceptions rather than `assert`, so optimized mode checks the
same gates.  Local replay results:

```text
python3 ... --check                 PASS
python3 -O ... --check              PASS
python3 ... --tamper-selftest       PASS (4/4 rejected)
python3 -O ... --tamper-selftest    PASS (4/4 rejected)
```

The four mutations alter an owner, the priority order, a full fiber, and an
imported blob pin.

## 8. Static source census

```text
sorry: 0
admit: 0
sorryAx: 0
custom axiom declarations: 0
native_decide: 0
Mathlib imports: 0
unsafe declarations: 0
```

Lean version: `v4.31.0`, stdlib only.

## 9. Fork CI and kernel axiom census

```text
validation_state: PENDING_FORK_DRAFT_CI
fork_draft_pr: PENDING
head_sha: PENDING
workflow_run: PENDING
lean_result: PENDING
axiom_census: PENDING
```

No local Lean build is run.  This section must be replaced with the final fork
run and printed axiom census before the branch is declared ready.

## 10. Statement audit and nonclaims

The load-bearing theorem is stronger than the predecessor's producer field:
each residual key has exact full fiber one.  The producer-shaped weakening is

```text
full fiber length <= compilerLoss * naturalScale = 1 * 2.
```

No support cardinality is called an MCA slope numerator.  A received-line
`SE2Certificate` remains external.  The packet does not prove or claim:

- fixed-outside profile multiplicity;
- a received-line semantic explanation or slope construction;
- image-normalized Sidon or MI+MA;
- a general residual-to-full add-back theorem;
- row-wide UNIF;
- list-interior, balanced-core, extension, or quotient payment;
- an adjacent-row upper ledger, safe agreement, official score, or prize claim.

The packet changes exactly one statement: the predecessor's one-key theorem is
replaced, on the same frozen deployed profile, by exhaustive all-surviving-key
coverage.

# FIXED
