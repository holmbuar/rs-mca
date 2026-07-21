# Audit: RS phase-structured Sidon payment

**Date:** 2026-07-21

**Status:** `PROVED_SCOPED_PHASE_PAYMENT / KERNEL_VALIDATED / LOCAL_ONLY / OPEN_GAP globally`

```yaml
workboard_item: T
row: Mersenne-31 list analytic stress calibration
object: OTHER
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: Exact zero quadratic-locator phase aggregate on all realized p2 fibers of one explicit post-C1 RS leaf.
architecture: RS_PHASE_STRUCTURED_SIDON_PAYMENT
partition_digest: 66dff80464465ec96253a4c10d518dc488d29e83e9b6cd5272b2ac8a136e8f41
atom_or_cell: p2 quadratic-locator band on a 64-support owner complement
quantifier: all 64 residual supports and all 9 realized p2 keys
projection_and_unit: phase-weighted supports; not slopes or codewords
claimed_bound: phaseAwareL1 = phaseCollisionMoment = 0; unsignedCollisionMoment = 576
status: PROVED_SCOPED_PHASE_PAYMENT
impact: LOCAL_ONLY; acceptance criterion 2
falsifier: non-exact owner complement, non-root domain point, broken pairing, ambient normalization, or nonzero phase coefficient
replay: python3 experimental/scripts/verify_rs_phase_structured_sidon.py; python3 -O experimental/scripts/verify_rs_phase_structured_sidon.py
```

## 1. Base, branch, and overlap preflight

- Fork: `holmbuar/rs-mca`.
- Final candidate branch: `gptpro/rs-phase-structured-sidon-completion`.
- Pinned fork base: `4e5f0b77c98f075ea7c8822cd4859847a232bc2a`.
- Upstream main at lane start: `a3017697ad1594521d2779fe1d83bccd45d4c06e`.
- Fork main contains the upstream head plus fork-only CI history; no mathematical fork-only delta was imported.
- The requested branch name `gptpro/rs-phase-structured-sidon` was already occupied when mutation began.  In accordance with the branch-out rule, the final candidate is a fresh continuation branch from that exact head; the occupied branch itself was not modified by this completion pass.
- The ten newest upstream PR descriptions and ten newest fork draft-PR descriptions were inspected.  Upstream #1026 names this exact successor.  Upstream #1027 proves a loss-one key on the same finite leaf but does not prove the quadratic-locator phase cancellation established here.  No competing open PR was found for this `p2` cancellation theorem.
- No file under `.github/` is modified.

## 2. Imported API and proof-authority blob table

The Lean module imports only `Std`; it locally restates the finite leaf and owner-complement grammar.  Therefore no integrated `AsymptoticSpine.*` or `M31QRootedShell.*` API is imported.

| Imported integrated API | Fork blob | Upstream blob | Verdict |
|---|---|---|---|
| none | — | — | No applicable API comparison; module imports only `Std` |

The active TeX proof authority was nevertheless fetched independently from both repositories:

| proof authority | fork blob | upstream blob | verdict |
|---|---|---|---|
| `experimental/grande_finale.tex` | `8a5d9791900ca9eed773feba146b92ad296704ce` | `8a5d9791900ca9eed773feba146b92ad296704ce` | `BYTE_IDENTICAL` |

This satisfies the no-open-PR-import rule and avoids silently depending on `M31C9RowSharp`, `HalfSliceFalsifier`, or another lane module.

## 3. Source-label map

| packet object | active source node in `experimental/grande_finale.tex` |
|---|---|
| realized profile image and profile envelope | `eq:profile-envelope` |
| effective Fourier target and normalization | `eq:effective-fourier-span`, `lem:effective-span-fourier` |
| certified phase-dependent payment boundary | `def:effective-major-minor`, `def:effective-fourier-payment`, `def:major-arc-aggregate` |
| realized versus ambient image scale | `eq:image-ambient-scales`, `eq:full-image-certificate` |
| image-normalized primitive max-fiber boundary | `def:primitive-q`, `lem:logmoment-q` |
| actual RS Vandermonde structure | `lem:vandermonde`, `sec:prefix-coordinates` |
| power sums versus locator coefficients | `lem:newton-equivalence` |
| distinction between phase/Sidon and unsigned energy | `sec:sidon-split` |

The theorem below is a signed phase aggregate on one exact survivor.  It does not manufacture the unsigned primitive-Q conclusion, a full effective-dual `(MI)+(MA)` theorem, or the separate support-to-slope compiler.

## 4. Exact PROVED declaration table

Namespace: `SidonEffectiveImage.RSPhaseStructuredSidon`.

| Lean declaration | exact statement audited | source/proof role |
|---|---|---|
| `field_prime_exact` | `p=2147483647` | deployed field |
| `full_slice_card` | complete moving weight-four slice has 70 supports | full family |
| `c1_owned_card` | the explicit earlier C1 list has six supports | owner census |
| `residual_slice_card` | explicit owner complement has 64 supports | genuine survivor |
| `owner_complement_exact` | residual membership equals full-slice membership and absence of the explicit C1 owner | first-match deletion |
| `antipodal_pairs_exact` | four printed domain pairs sum to zero modulo `p` | RS involution |
| `c1_antipodal_owner_exact` | C1 masks are exactly all unions of two complete antipodal pairs | semantic owner shape |
| `domain_nodup` | the eight active field elements are distinct | domain validity |
| `domain_points_are_deployed_roots` | all eight points satisfy `T_(2^21)(x)=0` modulo `p` | actual deployed RS domain |
| `quadratic_phase_defined_on_residual` | Euler phase is always `+1` or `-1` on the residual | locator phase |
| `cancellation_pair_count` | the printed involution has 32 pairs | pairing census |
| `paired_masks_nodup` | the 64 printed endpoints are duplicate-free | fixed-point-free pairing |
| `pairing_exhausts_residual` | the 32 pairs cover all 64 survivors | exhaustive involution |
| `pairing_cancels_p2_phase` | every pair preserves `p2` and has opposite locator phase | cancellation theorem |
| `realized_image_card` | corrected effective image is `A_eff=L=9` | corrected normalization |
| `realized_fiber_sizes` | exact sizes `[8,8,8,8,16,4,4,4,4]` | unsigned comparison |
| `phase_coefficients_zero` | every realized signed coefficient is zero | phase payment |
| `phase_aware_l1_exact` | phase-aware L1 aggregate is zero | MI+MA-style aggregate |
| `phase_collision_moment_exact` | signed collision moment is zero | Sidon-moment analogue |
| `unsigned_collision_moment_exact` | unsigned collision moment on the same fibers is 576 | absolute-mass contrast |
| `max_unsigned_fiber_exact` | largest unsigned fiber is 16 | obstruction contrast |
| `natural_scale_exact` | `ceil(64/9)=8` | realized-image scale |
| `phase_multiplier_one_payment` | exact multiplier-one phase inequality | scoped payment |
| `image_compensated_phase_payment` | same payment after multiplication by realized `A_eff=9` | corrected compensation |
| `deployed_dimensions` | exact M31 row constants and outside-support embedding | deployed calibration |
| `phase_scale_fits_deployed_budget` | local scale `8` is at most `2^24-1` | arithmetic context only |

Every finite statement carries its displayed object.  No global owner, profile census, slope compiler, add-back theorem, or ambient `q_gen^R` normalization is hidden in a definition.

## 5. Certificate and independent replay

Canonical certificate:

`experimental/data/certificates/rs-phase-structured-sidon/rs_phase_structured_sidon.json`

Independent stdlib verifier:

`experimental/scripts/verify_rs_phase_structured_sidon.py`

The verifier recomputes:

- the 70 weight-four masks;
- the six exact C1 complete-fiber masks;
- the 64-support owner complement;
- all eight `T_(2^21)` root checks and four antipodal identities;
- every locator constant and Euler phase;
- the nine realized `p2` keys and all fiber sizes;
- the 32 cancellation pairs and exact cover;
- phase coefficients, phase L1, signed and unsigned moments, maximum fiber, and natural scale;
- deployed outside-support arithmetic.

It includes live-gate mutations: restoring one C1 support, deleting one residual support, or perturbing one domain point must fail the corresponding cancellation/provenance gate.

Exact replay before publication:

```text
python3 experimental/scripts/verify_rs_phase_structured_sidon.py
python3 -O experimental/scripts/verify_rs_phase_structured_sidon.py
```

Both returned:

```text
PASS: exact RS owner-complement phase cancellation
VERDICT: PROVED_SCOPED_PHASE_PAYMENT
```

Python is replay only; Lean is the proof validation authority.

## 6. Lean validation and axiom census

Package layout:

```text
experimental/lean/sidon_effective_image/
  lean-toolchain
  lakefile.lean
  lake-manifest.json
  SidonEffectiveImage.lean
  SidonEffectiveImage/RSPhaseStructuredSidon.lean
```

- Lean: `v4.31.0`.
- Imports: `Std` only.
- Root: `SidonEffectiveImage.lean`, importing only `SidonEffectiveImage.RSPhaseStructuredSidon`.
- Manifest: generated empty-package manifest; there are no path or external requires.
- Draft validation PR: `holmbuar/rs-mca#83`.
- Green code-and-manifest head: `a60a1e2a09115ba7fc125fb0e62cbbda37be6739`.
- Authoritative workflow run: `29851893305`.
- Build job: `experimental/lean/sidon_effective_image`, job `88706611240`.
- Explicit target build: `lake build SidonEffectiveImage SidonEffectiveImage.RSPhaseStructuredSidon` — passed.
- Default package target: `lake build` — passed.
- Build result: `Build completed successfully (4 jobs)` for both invocations.

Two earlier runs failed in Lean setup before elaboration because the inherited packet lacked the repository's explicit Lake package/root form and generated manifest.  The only repairs were `lakefile.lean` packaging and the empty `lake-manifest.json`; no definition, theorem, hypothesis, certificate value, or note claim changed.

Static source census:

```text
sorry: 0
admit: 0
sorryAx: 0
native_decide: 0
custom axiom declarations: 0
unsafe declarations: 0
Mathlib imports: 0
external packages: 0
```

The green build printed 19 load-bearing axiom reports:

- axiom-free: `field_prime_exact`, `antipodal_pairs_exact`, `domain_points_are_deployed_roots`, and `deployed_dimensions`;
- dependent only on Lean's standard `propext`: `owner_complement_exact`, `c1_antipodal_owner_exact`, `quadratic_phase_defined_on_residual`, `pairing_exhausts_residual`, `pairing_cancels_p2_phase`, `realized_image_card`, `realized_fiber_sizes`, `phase_coefficients_zero`, `phase_aware_l1_exact`, `phase_collision_moment_exact`, `unsigned_collision_moment_exact`, `natural_scale_exact`, `phase_multiplier_one_payment`, `image_compensated_phase_payment`, and `phase_scale_fits_deployed_budget`.

No printed declaration depends on `sorryAx`, a custom axiom, `Classical.choice`, or `Quot.sound`.

Green CI certifies compilation and kernel checking only.  The statement/source match and semantic scope are audited in Sections 3–4.

## 7. Exact nonclaims and remaining conditionals

This packet does **not**:

- prove cancellation after refining `p2` to every full depth-`w` prefix key;
- prove a full three-coordinate or full-prefix C9 max-fiber/Sidon theorem;
- prove that signed phase cancellation bounds an unsigned support, codeword, ray, or slope count;
- import or instantiate the open C9 producer;
- prove exhaustive fixed-before-line global C1--C8 ownership;
- assert that the six-mask local owner is the complete deployed-row owner function;
- count all fixed-outside profiles;
- prove residual-to-full add-back, line-local `UNIF`, or target-envelope comparison;
- bank `U_Q`, `U_BC`, `U_list_int`, or another exact deployed-row atom;
- prove an adjacent safe row or Prize claim.

The named remaining input is:

```text
M31_FULL_PREFIX_PHASE_EXTENSION_OR_ROW_WIDE_C9_COVERAGE.
```

It must extend the involution to the full surviving prefix partition, prove an equivalent full-prefix phase-aware moment, or route every coordinate not preserved by the involution to an earlier certified owner.  Slope projection, profile census, add-back, and line-local summation remain separate obligations.

## 8. Acceptance gate

**Criterion 2 is met.**  The theorem bounds a genuine post-C1 survivor on actual Mersenne-31 RS domain points after an explicit owner deletion.  The exact phase-aware payment is zero at the realized image scale, while the unsigned collision moment on the same support fibers is 576.  This is a theorem about cancellation that absolute mass does not see; it is not an interface or adapter.

OPEN GAP
