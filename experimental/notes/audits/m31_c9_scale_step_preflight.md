# M31 C9 sixteen-root scale-step audit

**Date:** 2026-07-21

**Status:** `COUNTEREXAMPLE_NEW_FLOOR / KERNEL_VALIDATED / AUDIT`

**Lane:** `gptpro/m31-c9-scale-step`

## 1. Scope and acceptance gate

This packet tests whether the loss-one exact-residual prefix structure proved at
eight roots in upstream PR #1027 survives the next active-domain scale. It uses
sixteen actual roots of `T_(2^21)` over `F_(2^31-1)`, four complete `T_4`
blocks, and the complete weight-eight slice.

After the exact local C1 antipodal-quotient deletion, the first residual key in
ascending-mask order has two distinct supports:

```text
key            = (1625092085,1544193364,2053033192)
residual fiber = [383,61808]
```

Thus loss one does not persist unchanged.

**Acceptance gate:** criterion 4 — statement-changing counterexample / new
obstruction floor.

**Named terminal:**

```text
M31_C9_SCALE_STEP_T4_BLOCK_SWAP_DOUBLING
```

The exhaustive verifier additionally proves that two is the exact maximum fiber
size on this displayed C1-complement residual. This is a support-prefix route
cut, not a bankable row atom.

## 2. Workboard contract

```yaml
workboard_item: M1/T
row: Mersenne-31 list
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: On the exact sixteen-root weight-eight active slice, after exact C1 antipodal-quotient deletion, the first realized residual prefix key has two distinct supports.
architecture: DIRECT
partition_digest: LOCAL_EXACT_C1_ANTIPODAL_COMPLEMENT_V1
atom_or_cell: C9 primitive prefix fiber, sixteen-root scale step
quantifier: complete weight-eight slice on the sixteen displayed deployed roots
projection_and_unit: supports per first-three-power-sum prefix key
claimed_bound: first residual fiber = 2; exhaustive replay residual maximum = 2
status: COUNTEREXAMPLE
impact: ROUTE_CUT
falsifier: any claim that eight-root loss-one residual injectivity persists unchanged at sixteen roots
replay: python3 experimental/scripts/verify_m31_c9_scale_step.py --check
```

## 3. Source pins and imported-API blob parity

| repository object | SHA |
|---|---|
| fork base `holmbuar/rs-mca:main` | `b410c7ee14488bb751c5a89df10cb5b0323e3669` |
| upstream main at claim time | `a3017697ad1594521d2779fe1d83bccd45d4c06e` |
| `experimental/grande_finale.tex` blob | `8a5d9791900ca9eed773feba146b92ad296704ce` |
| `experimental/rs_mca_thresholds.tex` blob | `01302a797c502a05ed0b11ba949b8756e0aa2b22` |

Every imported integrated Lean API was fetched independently from fork and
upstream main:

| imported API | fork blob | upstream blob | verdict |
|---|---|---|---|
| `experimental/lean/asymptotic_spine/AsymptoticSpine/PrimitiveBoolean.lean` | `777273e4377c31c815062769803622c6226988d3` | `777273e4377c31c815062769803622c6226988d3` | `BYTE_IDENTICAL` |
| `experimental/lean/m31_q_rooted_shell/M31QRootedShell/Deployed.lean` | `7e21ff098567d26aba7330fbb2722d5cb952fb09` | `7e21ff098567d26aba7330fbb2722d5cb952fb09` | `BYTE_IDENTICAL` |

The module imports only those two integrated APIs. It does not import
`SidonEffectiveImage.M31C9RowSharp`, `SidonEffectiveImage.HalfSliceFalsifier`,
any open C9 producer, or any other open-PR module.

## 4. Source-label map

| packet object | source node |
|---|---|
| complete fixed-weight leaf and residual | `sec:primitive-leaf` |
| realized-image normalization | `eq:image-ambient-scales` |
| primitive maximum fiber | `def:primitive-q` |
| moment/max interface | `lem:logmoment-q` |
| power sums versus locator coefficients | `lem:newton-equivalence` |
| finite row-sharp atom boundary | `def:q-row-atom` |
| deployed target | `prop:q-exact-target` |
| moment-order warning | `prop:q-moment-order-floor` |
| separate projection boundary | `(SE2)`, `hyp:ray-compiler`, `prop:q-sp-no-ray` |
| separate profile census | `lem:profile-multiplicity` |
| final integer composition | `thm:exact-completion-certificate` |

The packet changes only the local max-fiber premise. Supports, codewords, rays,
affine slopes, and list/MCA numerators remain separate objects.

## 5. Exact finite object and exhaustive census

The generator is

```text
g=(1717986917,1288490189) in F_p[i], p=2^31-1.
```

Four complete `T_4` blocks are derived from base exponents
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

The exact C1 owner deletes the `C(8,4)=70` unions of four antipodal pairs. The
stdlib verifier recomputes:

```text
full:     12870 supports, 12457 keys, {1:12048,2:408,6:1}, max 6
residual: 12800 supports, 12416 keys, {1:12032,2:384}, max 2
```

The doubled pair is

```text
383   = {0,1,2,3,4,5,6,8}
61808 = {4,5,6,8,12,13,14,15}.
```

It has common core `{4,5,6,8}` and exchanges complete blocks `{0,1,2,3}` and
`{12,13,14,15}`. Both exchanged blocks contribute `(0,2,0)`, so the prefix is
unchanged. Neither support is C1-owned.

## 6. Package boundary

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

The root imports only `SidonEffectiveImage.M31C9ScaleStep`. Lean is pinned to
4.31.0, stdlib only. The sibling path dependencies are recorded in
`lake-manifest.json`. No `.lake/`, build output, or `.github/` file is included.

## 7. Exact PROVED-declaration table

Namespace: `SidonEffectiveImage.M31C9ScaleStep`.

| declaration | exact statement/role |
|---|---|
| `residual_exact` | for any C1 label, `IsResidual S` iff `IsFullSupport S` and `earlierOwner S=none`. |
| `scoped_residual_exact` | the local C1--C8 constructor grammar, with only C1 nonempty, satisfies that exact complement equation. |
| `generator_norm_one` | the printed generator has norm one. |
| `generator_half_order` | `g^(2^30)=-1`. |
| `generator_full_order` | `g^(2^31)=1`. |
| `domain_derived_exact` | the norm-one derivation equals the sixteen printed residues. |
| `domain_nodup` | the sixteen roots are distinct. |
| `domain_points_are_deployed_roots` | every point satisfies `T_(2^21)(x)=0 mod p`. |
| `antipodal_pairs_exact` | all eight displayed antipodal pairs sum to zero modulo `p`. |
| `t4_fibers_exact` | the four blocks have the four displayed constant `T_4` values. |
| `firstGrowth_indices_exact` | mask `383` is `{0,1,2,3,4,5,6,8}`. |
| `firstGrowthMate_indices_exact` | mask `61808` is `{4,5,6,8,12,13,14,15}`. |
| `block0_key_exact`, `block3_key_exact` | the exchanged complete blocks both have key `(0,2,0)`. |
| `firstGrowth_full`, `firstGrowthMate_full` | both masks are valid sixteen-bit weight-eight supports. |
| `firstGrowth_not_c1Owned`, `firstGrowthMate_not_c1Owned` | neither mask is owned by the exact local C1 predicate. |
| `firstGrowth_survives`, `firstGrowthMate_survives` | both masks satisfy the exact residual predicate. |
| `firstGrowth_key_exact`, `firstGrowthMate_key_exact` | both masks have the printed key `(1625092085,1544193364,2053033192)`. |
| `firstGrowth_keys_equal` | the two residual supports have equal prefix key. |
| `firstGrowth_distinct` | the two support masks are unequal. |
| `no_earlier_residual_masks` | the residual-mask list below `383` is empty. |
| `first_growth_order_certificate` | mask `383` is residual and no smaller mask is residual. |
| `scale_step_not_injective` | the exact local residual prefix map is not injective. |
| `scale_step_fiber_floor_two` | there exist two distinct exact-residual supports with one prefix key. |
| `deployed_dimensions` | exact M31 row constants, active weight eight, fixed outside weight `981121`, and availability. |
| `loss_two_fits_deployed_budget` | `2<=16777215`; explicitly not a row allocation. |

The complete fiber identity `[383,61808]`, full/residual cardinalities,
histograms, and exact residual maximum two are checked by the separate exhaustive
certificate verifier, not silently promoted beyond the Lean declarations above.

## 8. Certificate replay

Canonical files:

```text
experimental/data/certificates/m31-c9-scale-step/m31_c9_scale_step.json
experimental/scripts/verify_m31_c9_scale_step.py
```

Replay:

```text
python3 experimental/scripts/verify_m31_c9_scale_step.py --check
python3 -O experimental/scripts/verify_m31_c9_scale_step.py --check
```

Both modes pass and recompute the generator arithmetic, roots, `T_4` blocks,
all `65536` masks, the complete weight-eight slice, exact C1 deletion, both
fiber histograms, exact maxima, and the first doubled residual key.

## 9. Lean validation and axiom census

### Authoritative fork run

```text
Fork draft PR: holmbuar/rs-mca#82
Validated theorem head: a1087a4a1b5adffa2dfe03585cbe8b609ef2c961
Workflow run: 29852634611 (Lean build — PR #82)
Package job: experimental/lean/sidon_effective_image
Artifact: lean-build-log-0, id 8504001192
Result: Build completed successfully (19 jobs)
Explicit targets: SidonEffectiveImage and SidonEffectiveImage.M31C9ScaleStep
Lean: 4.31.0
```

No local Lean build was used.

### Static census

```text
sorry: 0
admit: 0
sorryAx: 0
custom axiom declarations: 0
unsafe declarations: 0
native_decide: 0
Mathlib imports: 0
```

### Printed kernel census

- `generator_norm_one`, `generator_half_order`, `generator_full_order`,
  `domain_derived_exact`, `domain_points_are_deployed_roots`,
  `antipodal_pairs_exact`, `t4_fibers_exact`, `firstGrowth_distinct`,
  `deployed_dimensions`, and `loss_two_fits_deployed_budget` are axiom-free.
- The exact owner/complement, support-membership, key-equality, first-mask,
  noninjectivity, and two-witness declarations use only standard `propext`.
- No printed declaration uses `sorryAx`, a custom axiom, `Classical.choice`, or
  `Quot.sound`.

The final note-stamp commit changes documentation only. The fork PR reruns the
same explicit Lean targets at the final head before branch-ready handoff.

## 10. Explicit nonclaims

This packet does **not** prove:

- an exhaustive fixed-before-line C1--C8 owner function for the complete row;
- that C1 is the only earlier owner globally;
- a received word, line, explanation, codeword, ray, affine slope, list
  numerator, or MCA numerator;
- a bankable `U_Q`, `U_paid`, `U_BC`, `U_list_int`, or `U_new`;
- profile multiplicity, residual-to-full add-back, SE2, ray compilation, or
  line-local `UNIF`;
- that every residual key has size two (most are singleton);
- a theorem beyond the displayed sixteen-root active slice;
- an adjacent row, stable-paper theorem, official score, or prize claim.

## 11. Exact consequence

Any scale-stable C9 theorem retaining loss one after only the exact antipodal C1
deletion is false. A successor must route complete-`T_4` block swaps earlier,
accept and pay factor two, or prove a stronger residual/prefix chronology that
removes the displayed pair.

# COUNTEREXAMPLE_NEW_FLOOR
