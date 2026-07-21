# M31 C9 sixteen-root scale-step preflight

**Date:** 2026-07-21

**Status:** `COUNTEREXAMPLE_NEW_FLOOR / KERNEL_VALIDATION_PENDING / AUDIT`

**Lane:** `gptpro/m31-c9-scale-step`

## 1. Scope and acceptance gate

This packet tests whether the loss-one exact-residual prefix structure proved at
eight roots in upstream PR #1027 survives the next active-domain scale. It uses
sixteen actual roots of `T_(2^21)` over `F_(2^31-1)`, arranged as four complete
`T_4` blocks, and the complete weight-eight slice.

The exact earlier owner is the C1 antipodal quotient: a support is deleted iff
it is a union of four of the eight antipodal pairs. In canonical ascending-mask
order, the first surviving support already shares its first-three-power-sum key
with a second surviving support:

```text
key            = (1625092085,1544193364,2053033192)
residual fiber = [383,61808]
fiber size     = 2
```

Thus the predecessor's loss-one statement does not persist unchanged.

**Acceptance gate:** criterion 4 — statement-changing counterexample / new
obstruction floor.

**Named terminal:** `M31_C9_SCALE_STEP_T4_BLOCK_SWAP_DOUBLING`.

The exhaustive certificate additionally proves that two is the exact maximum
fiber size on this displayed C1-complement residual. This remains a local
support-prefix route cut, not a bankable row atom.

## 2. Exact workboard contract

```yaml
workboard_item: M1/T
row: Mersenne-31 list
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: On the exact sixteen-root weight-eight active slice, after exact C1 antipodal-quotient deletion, the first realized residual prefix key has exactly two supports.
architecture: DIRECT
partition_digest: LOCAL_EXACT_C1_ANTIPODAL_COMPLEMENT_V1
atom_or_cell: C9 primitive prefix fiber, sixteen-root scale step
quantifier: complete weight-eight slice on the sixteen displayed deployed roots
projection_and_unit: supports per first-three-power-sum prefix key
claimed_bound: first residual fiber = 2; exhaustive replay residual maximum = 2
status: COUNTEREXAMPLE
impact: ROUTE_CUT
falsifier: any claim that the eight-root loss-one residual injectivity persists unchanged at sixteen roots
replay: python3 experimental/scripts/verify_m31_c9_scale_step.py --check
```

## 3. Source pins and imported-API blob parity

| repository object | SHA |
|---|---|
| fork `holmbuar/rs-mca:main` | `b410c7ee14488bb751c5a89df10cb5b0323e3669` |
| upstream `przchojecki/rs-mca:main` | `a3017697ad1594521d2779fe1d83bccd45d4c06e` |
| `experimental/grande_finale.tex` blob | `8a5d9791900ca9eed773feba146b92ad296704ce` |
| `experimental/rs_mca_thresholds.tex` blob | `01302a797c502a05ed0b11ba949b8756e0aa2b22` |

Every imported integrated Lean API was fetched independently from fork and
upstream main:

| imported API | fork blob | upstream blob | verdict |
|---|---|---|---|
| `experimental/lean/asymptotic_spine/AsymptoticSpine/PrimitiveBoolean.lean` | `777273e4377c31c815062769803622c6226988d3` | `777273e4377c31c815062769803622c6226988d3` | `BYTE_IDENTICAL` |
| `experimental/lean/m31_q_rooted_shell/M31QRootedShell/Deployed.lean` | `7e21ff098567d26aba7330fbb2722d5cb952fb09` | `7e21ff098567d26aba7330fbb2722d5cb952fb09` | `BYTE_IDENTICAL` |

The module imports only those two APIs. It does not import
`SidonEffectiveImage.M31C9RowSharp`, `SidonEffectiveImage.HalfSliceFalsifier`,
any open C9 producer, or any other open-PR module.

## 4. Source-label map

| packet object | source node |
|---|---|
| complete fixed-weight leaf and residual | `sec:primitive-leaf` |
| image normalization | `eq:image-ambient-scales` |
| primitive maximum fiber | `def:primitive-q` |
| moment/max interface | `lem:logmoment-q` |
| power sums versus locator coefficients | `lem:newton-equivalence` |
| finite row-sharp atom | `def:q-row-atom` |
| deployed row target | `prop:q-exact-target` |
| moment-order warning | `prop:q-moment-order-floor` |
| separate projection boundary | `(SE2)`, `hyp:ray-compiler`, `prop:q-sp-no-ray` |
| separate profile census | `lem:profile-multiplicity` |
| final integer composition | `thm:exact-completion-certificate` |

The terminal changes the local max-fiber statement only. Supports, codewords,
rays, affine slopes, and list/MCA numerators remain distinct.

## 5. Exact finite object

The packet uses the predecessor generator

```text
g=(1717986917,1288490189) in F_p[i], p=2^31-1.
```

It derives four complete `T_4` blocks from base exponents
`256,768,1280,1792` and quarter turns `j*2^29`. The sixteen roots are

```text
434373082,  614288294, 1713110565, 1533195353,
1984437538, 380812851,  163046109, 1766670796,
1244279234, 907334541,  903204413, 1240149106,
2066813671,1590029158, 80669976,  557454489.
```

The four `T_4` values are

```text
1884637334, 51044589, 1916935773, 116752674.
```

The exact C1 owner deletes the `C(8,4)=70` unions of four antipodal pairs.
The complete and residual distributions are

```text
full:     12870 supports, 12457 keys, {1:12048,2:408,6:1}, max 6
residual: 12800 supports, 12416 keys, {1:12032,2:384}, max 2
```

The first full support is mask `255` and is C1-owned. The first residual mask is
`383`. The doubled pair is

```text
383   = {0,1,2,3,4,5,6,8}
61808 = {4,5,6,8,12,13,14,15}.
```

They share `{4,5,6,8}` and exchange complete blocks `{0,1,2,3}` and
`{12,13,14,15}`. Each exchanged block has first-three-power-sum contribution
`(0,2,0)`. Neither support is a union of antipodal pairs, so both survive.

## 6. Package and ship boundary

```text
experimental/lean/sidon_effective_image/
  .gitignore
  lean-toolchain
  lakefile.lean
  lake-manifest.json
  SidonEffectiveImage.lean
  SidonEffectiveImage/M31C9ScaleStep.lean
experimental/data/certificates/m31-c9-scale-step/m31_c9_scale_step.json
experimental/scripts/verify_m31_c9_scale_step.py
experimental/notes/thresholds/m31_c9_scale_step.md
experimental/notes/audits/m31_c9_scale_step_preflight.md
experimental/agents-log-entry-gptpro-m31-c9-scale-step.md
```

The root imports only `SidonEffectiveImage.M31C9ScaleStep`. The package is Lean
4.31.0, stdlib only. The path dependencies are recorded in
`lake-manifest.json`. No `.lake/`, build output, or `.github/` file is changed.

## 7. Exact PROVED-declaration table

Namespace: `SidonEffectiveImage.M31C9ScaleStep`.

| declaration | exact role |
|---|---|
| `residual_exact` | residual membership iff full-slice membership and `earlierOwner=none`, generic in the C1 label. |
| `scoped_residual_exact` | concrete C1--C8 grammar with only C1 nonempty satisfies that equation. |
| `generator_norm_one` | printed generator has norm one. |
| `generator_half_order` | `g^(2^30)=-1`. |
| `generator_full_order` | `g^(2^31)=1`. |
| `domain_derived_exact` | norm-one derivation equals the sixteen printed residues. |
| `domain_nodup` | sixteen roots are distinct. |
| `domain_points_are_deployed_roots` | every point is a `T_(2^21)` root modulo `p`. |
| `antipodal_pairs_exact` | all eight displayed antipodal pairs sum to zero modulo `p`. |
| `t4_fibers_exact` | four blocks have the four displayed constant `T_4` values. |
| `full_slice_card` | complete weight-eight slice has `12870` supports. |
| `c1_owned_support_card` | exact antipodal owner deletes `70` supports. |
| `residual_slice_card` | exact C1 complement has `12800` supports. |
| `residual_head_exact` | first residual support is mask `383`. |
| `firstGrowth_indices_exact` | mask `383` has the displayed support. |
| `firstGrowthMate_indices_exact` | mask `61808` has the displayed support. |
| `block0_key_exact`, `block3_key_exact` | exchanged complete blocks both have key `(0,2,0)`. |
| `firstGrowth_key_exact` | mask `383` has the printed growth key. |
| `firstGrowthMate_key_exact` | mask `61808` has the same key. |
| `firstGrowth_not_c1Owned`, `firstGrowthMate_not_c1Owned` | neither support is C1-owned. |
| `firstGrowth_survives`, `firstGrowthMate_survives` | both supports are in the exact residual. |
| `firstGrowth_full_fiber_exact` | full fiber is exactly `[383,61808]`. |
| `firstGrowth_residual_fiber_exact` | residual fiber remains exactly `[383,61808]`. |
| `first_residual_key_exact` | the first residual support has the printed key. |
| `scale_step_fiber_size` | residual fiber size is exactly `2`. |
| `scale_step_not_loss_one` | residual fiber size is not at most `1`. |
| `scale_step_loss_two` | the witness fiber is bounded by `2`. |
| `deployed_dimensions` | exact row constants, active weight eight, outside size `981121`, and availability. |
| `loss_two_fits_deployed_budget` | local constant `2` is below `16777215`; this is not a row allocation. |

The exhaustive histogram and residual maximum-two statement are replayed by the
certificate verifier and are not silently promoted to a broader Lean theorem.

## 8. Certificate, independent replay, and static census

Files:

```text
experimental/data/certificates/m31-c9-scale-step/m31_c9_scale_step.json
experimental/scripts/verify_m31_c9_scale_step.py
```

Pre-push SHA-256 values:

```text
certificate: 5f83447d204052a0cf123a75cb98671222019cf251ffc53018a4d0473f4eea2c
verifier:    12c1262dc7f6005f791638ef4640a758a49c197c4a8631da9d17e81e588da2c0
Lean module: 0e384e37b44749e55a830a5a71b8606892ec86af0b9d847a7e97a96f09ad7e53
```

Replay:

```text
python3 experimental/scripts/verify_m31_c9_scale_step.py --check
python3 -O experimental/scripts/verify_m31_c9_scale_step.py --check
```

Both modes pass and recompute every domain, support, owner, key, and histogram
integer from scratch.

Static preflight:

```text
sorry: 0
admit: 0
sorryAx: 0
custom axiom declarations: 0
unsafe declarations: 0
native_decide: 0
Mathlib imports: 0
```

The module ends with `#print axioms` for all load-bearing domain, owner,
cardinality, doubled-fiber, loss-one falsifier, deployed-dimension, and budget
declarations.

## 9. Fork draft-PR Lean validation

```text
Fork draft PR: PENDING
Candidate head: PENDING
Workflow run: PENDING
Lean result: PENDING
Axiom census from build log: PENDING
```

The fork workflow is the compiler authority; no local Lean build is used. Green
CI proves compilation and kernel checking only. This section will be stamped
after the first green candidate run, then the audit-only stamp will be replayed
at the final head.

## 10. Explicit nonclaims

This packet does **not** prove:

- an exhaustive fixed-before-line C1--C8 owner function for the complete row;
- that C1 is the only earlier owner globally;
- a received word, line, explanation, codeword, ray, or affine-slope
  realization of the doubled support fiber;
- a list or MCA numerator lower bound;
- a bankable `U_Q`, `U_paid`, `U_BC`, `U_list_int`, or `U_new`;
- profile multiplicity, add-back, SE2 projection, ray compilation, or `UNIF`;
- that every residual key has size two (most are singleton);
- a theorem beyond the displayed sixteen-root active slice;
- an adjacent row, stable-paper theorem, official score, or prize claim.

## 11. Exact consequence

Any scale-stable C9 theorem retaining loss one after only the exact antipodal C1
deletion is false. A successor must route complete-`T_4` block swaps earlier,
accept and pay exact factor two, or prove a stronger residual/prefix chronology
that removes the displayed pair.

# COUNTEREXAMPLE_NEW_FLOOR
