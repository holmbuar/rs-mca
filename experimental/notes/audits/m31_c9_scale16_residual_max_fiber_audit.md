---
workboard_item: "T"
row: "Mersenne-31 list auxiliary stress-test calibration"
object: "OTHER"
target_epsilon: "2^-100"
agreement: 1116023
B_star: 16777215
direct_statement: "Exact finite audit of the complete sixteen-root weight-eight C1-complement: residual max fiber two, 384 doubled keys, all and only complete-T_4 block swaps."
architecture: "DIRECT"
partition_digest: "N/A (DIRECT local C1-complement profile)"
atom_or_cell: "C9 / primitive-Q exact residual support fiber"
quantifier: "all realized first-three-power-sum keys of the exact local residual"
projection_and_unit: "support masks per prefix key; no slope/ray/codeword conversion"
claimed_bound: "max residual fiber = 2; exact image-normalized loss floor = 2"
status: "PROVED finite / AUDIT / COUNTEREXAMPLE_NEW_FLOOR"
impact: "ROUTE_CUT; criterion 4 primary, criterion 2 additional"
falsifier: "masks 5903 and 6128 at key (826664565,1588616718,1026140363)"
replay: "python3 experimental/scripts/verify_m31_c9_scale16_residual_max_fiber.py --check; python3 -O experimental/scripts/verify_m31_c9_scale16_residual_max_fiber.py --check; python3 experimental/scripts/verify_m31_c9_scale16_residual_max_fiber.py --tamper-selftest"
---

# Audit: M31 C9 sixteen-root residual max-fiber scale step

## 1. Audit verdict and scope

```text
COUNTEREXAMPLE_NEW_FLOOR
```

The eight-root residual injectivity theorem from upstream PR #1027 does not
scale to four complete `T_4` blocks.  On the exact sixteen-root complete
weight-eight slice, after deleting every C1 antipodal-quotient support, the
residual maximum fiber is exactly two.  There are exactly 384 doubled keys,
and their complete classification is the `T_4`-block-swap terminal

```text
M31_C9_SCALE16_T4_BLOCK_SWAP_RESIDUAL_LOSS_2.
```

The same packet also proves the positive bound requested by gate 2: every
realized residual key has support fiber at most two.

This audit is profile-local.  Its unit is **support masks per prefix key**.
It does not claim a distinct-slope, ray, codeword, or row-global numerator.

## 2. Preflight and branch discipline

| item | audited value |
|---|---|
| fork repository | `holmbuar/rs-mca` |
| upstream repository | `przchojecki/rs-mca` |
| upstream main read | `a3017697ad1594521d2779fe1d83bccd45d4c06e` |
| exact fork-main base | `4e5f0b77c98f075ea7c8822cd4859847a232bc2a` |
| fork/upstream relation | fork contains upstream head and is ahead only by fork integration history |
| requested ref | `gptpro/m31-c9-scale-step`, discovered as a stale empty pointer at `b410c7e...`; not moved or continued |
| fresh lane branch | `gptpro/m31-c9-scale-step-16roots` |
| forbidden paths | no file under `.github/` changed |
| predecessor | upstream PR #1027, read as source and scope reference only |
| open-PR imports | none |

Before branching, the ten latest upstream PR descriptions and the ten latest
fork draft-PR descriptions were read.  No active packet claimed the sixteen-root
successor.  The packet does not import or modify another lane's module.

## 3. Direct imported-API blob audit

Every directly imported repository API was read on both current fork main and
current upstream main.  The blobs are byte-identical.

| direct import | fork-main blob | upstream-main blob | identical |
|---|---|---|---|
| `AsymptoticSpine.EffectiveClosure` | `9fb097e23d00e2f3ee3afeda021b86ba4192d2a4` | `9fb097e23d00e2f3ee3afeda021b86ba4192d2a4` | yes |
| `AsymptoticSpine.UniformClosedLedger` | `deda34063f4629e245c37ba03e3cb3ab70502570` | `deda34063f4629e245c37ba03e3cb3ab70502570` | yes |
| `M31QRootedShell.Deployed` | `7e21ff098567d26aba7330fbb2722d5cb952fb09` | `7e21ff098567d26aba7330fbb2722d5cb952fb09` | yes |

`Std` is the Lean standard library, not a repository API.  The root
`SidonEffectiveImage.lean` imports only
`SidonEffectiveImage.M31C9ScaleStep`.  The new module does not import
`M31C9RowSharp`, `HalfSliceFalsifier`, or any open-PR module.

## 4. Source-label map

| packet statement | active source label or live authority | correspondence |
|---|---|---|
| max fiber on realized image | `experimental/grande_finale.tex`, `def:primitive-q` | the residual `max_s f_s` object, at exact finite scale |
| first three power sums versus locator coefficients | `experimental/grande_finale.tex`, `lem:newton-equivalence` | valid because support weight is fixed and `3 < p` |
| local realized-image average | `experimental/grande_finale.tex`, `eq:profile-envelope` | `M/L`, kept separate from ambient `p^w` |
| outside-profile multiplicity | `experimental/grande_finale.tex`, `lem:profile-multiplicity` | explicitly not paid |
| support-to-ray conversion | `experimental/grande_finale.tex`, `hyp:ray-compiler` | explicitly not claimed |
| deployed Q atom status | `experimental/notes/frontier-adjacent/four_row_exact_completion_compiler_v1.md`, Section 4 | remains `null` row-globally |

The packet translates the older shorthand into the active v4 object: an exact
finite primitive-Q support fiber after one literal earlier-owner deletion.

## 5. Exact PROVED declaration table

All statements are in
`SidonEffectiveImage.M31C9ScaleStep`.

| declaration | exact statement audited | proof mode |
|---|---|---|
| `residual_exact` | for every mask, residual membership iff complete weight-eight membership and the supplied C1 owner returns `none` | structural Lean proof |
| `scoped_residual_exact` | the local C1--C8 grammar instantiates the exact complement; only C1 is nonempty in this profile | structural Lean proof |
| `generator_norm_one` | the printed generator has norm one in the explicit `Fp2` arithmetic | kernel `decide` |
| `generator_half_order` | `g^(2^30)=-1` | kernel `decide` |
| `generator_full_order` | `g^(2^31)=1` | kernel `decide` |
| `domain_derived_from_generator` | the sixteen printed roots equal the real coordinates of the sixteen stated generator powers | kernel `decide` |
| `domain_points_are_deployed_roots` | all sixteen points satisfy `T_(2^21)(x)=0` by repeated Chebyshev doubling | kernel `decide` |
| `antipodal_pairs_exact` | all eight printed pairs sum to zero modulo `p` | kernel `decide` |
| `t4_fibers_exact` | the four consecutive blocks are complete `T_4` fibers with the four printed values | kernel `decide` |
| `t4_prefix_keys_equal` | every complete block has first-three-power-sum key `(0,2,0)` | kernel `decide` |
| `scale_step_summary_exact` | full and residual masses, image sizes, fiber histograms, exact maxima, sixfold deleted key, first collision, all 384 block swaps, both natural-scale ceilings, and exact loss-one/loss-two inequalities equal the printed summary | exhaustive kernel `decide` |
| `residual_max_fiber_exact` | residual maximum fiber is exactly `2` | consequence of exact summary |
| `residual_doubled_key_count_exact` | exactly `384` residual keys have fiber `2` | consequence of exact summary |
| `residual_image_normalized_loss_two_exact` | image-normalized loss one fails and loss two holds | exact integer consequence |
| `integral_loss_one_at_scale_two` | literal integer field `2 <= 1*2` holds | exact integer consequence |
| `deployed_dimensions` | `w=67447`, `m=981129`, fixed outside weight `981121`, outside availability `2097136`, and availability inequality | kernel `decide` |
| `local_charge_fits_deployed_budget` | local integer charge `2` fits `B*=16777215` | kernel `decide`; not a row allocation |

The exhaustive summary uses 1,024 exact `p1` buckets only to avoid a global
quadratic `eraseDups`.  Equality of keys cannot cross buckets because the
bucket is a function of the key's first coordinate.  Inside each bucket the
actual complete list is deduplicated and every exact multiplicity is counted.
The independent verifier uses a separate dictionary enumeration and obtains
the same spectrum and obstruction classification.

## 6. Exact arithmetic and obstruction floor

### Full slice

```text
mass                  12,870
realized image        12,457
fiber histogram       1^12048, 2^408, 6^1
maximum               6
```

The sixfold key is `(0,4,0)`, with masks

```text
255, 3855, 4080, 61455, 61680, 65280.
```

All six masks are unions of two complete `T_4` blocks and are C1-owned.

### Exact C1 complement

```text
C1-owned supports     70 = C(8,4)
residual mass         12,800
residual image        12,416
fiber histogram       1^12032, 2^384
maximum               2
```

The canonical first repeated key is

```text
(826664565,1588616718,1026140363)
```

with exact residual fiber `[5903,6128]`.

### Minimal image-normalized loss

```text
2 * 12,416 = 24,832 > 12,800,
2 * 12,416 = 24,832 <= 2 * 12,800 = 25,600.
```

Therefore the least integer `kappa` satisfying

```text
maxFiber * imageCard <= kappa * residualMass
```

is exactly `kappa=2`.

The integer ceiling of both the full and residual averages is also two, so the
producer-shaped field still has compiler loss one at integral scale two.
The audit does not conflate those facts.

## 7. Certificate and replay audit

Certificate:

```text
experimental/data/certificates/m31-c9-scale16-residual-max-fiber/
  m31_c9_scale16_residual_max_fiber.json
```

Verifier:

```text
experimental/scripts/verify_m31_c9_scale16_residual_max_fiber.py
```

The stdlib verifier independently checks:

1. canonical JSON;
2. Git blob SHAs of all direct repository imports;
3. SHA-256 of the Lean module;
4. forbidden imports/tokens (`native_decide`, predecessor/open-PR modules,
   `sorry`, `admit`, custom `axiom`);
5. norm-one, half-order, and full-order generator arithmetic;
6. all sixteen derived roots and four exact `T_4` values;
7. complete weight-eight and exact C1-complement enumerations;
8. both fiber histograms and exact maxima;
9. the canonical first repeated residual key;
10. all 384 doubled residual keys equal the 384 distinct surviving block-swap
    keys;
11. mutation rejection.

Replay commands:

```text
python3 experimental/scripts/verify_m31_c9_scale16_residual_max_fiber.py --check
python3 -O experimental/scripts/verify_m31_c9_scale16_residual_max_fiber.py --check
python3 experimental/scripts/verify_m31_c9_scale16_residual_max_fiber.py --tamper-selftest
python3 -O experimental/scripts/verify_m31_c9_scale16_residual_max_fiber.py --tamper-selftest
```

## 8. Lean validation and axiom census

Validation state at initial packet creation:

```text
PENDING_FORK_DRAFT_PR_CI
```

No local Lean build was run.  The authoritative target is the fork draft PR
check for `experimental/lean/sidon_effective_image`, Lean 4.31.0.

Intended source census before CI:

```text
sorry/admit/sorryAx: 0
custom axiom declarations: 0
native_decide: 0
unsafe declarations: 0
Mathlib imports: 0
```

The module ends with `#print axioms` for every load-bearing declaration.  This
section must be replaced by the exact green run, explicit module targets, and
printed axiom output before the branch is declared ready.

## 9. Explicit nonclaims

- No row-global `U_Q` integer or completion atom is supplied.
- No exhaustive fixed-before-line C1--C8 atlas is proved.
- No claim is made that only C1 is nonempty on the deployed row.
- No received line, explanation, witness, codeword, ray, or distinct slope is
  constructed.
- No `(SE2)` certificate or support-to-slope injection is instantiated.
- No outside-profile census, residual add-back, line-local `UNIF`, profile
  envelope, or summed adjacent-row certificate is proved.
- The local comparison `2 <= B*` is not treated as an available row allocation.
- No stable TeX theorem, deployed safe agreement, official score, or prize
  claim changes.
- No file under `.github/` is modified.
- No open-PR module is imported.

## 10. Acceptance-gate conclusion

**Criterion 4 (primary):** met.  The scale-inductive injectivity statement is
false; the first exact obstruction has residual multiplicity two and is named
and classified.

**Criterion 2 (additional):** met.  On the actual sixteen-root post-C1
survivor, every realized prefix key has fiber at most two.

```text
COUNTEREXAMPLE_NEW_FLOOR
```
