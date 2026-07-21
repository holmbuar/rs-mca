# Audit: RS phase-structured Sidon payment

```yaml
workboard_item: T
row: Mersenne-31 list analytic stress calibration
object: OTHER
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: Exact zero quadratic-locator phase aggregate on all realized p2 fibers of one explicit post-C1 RS leaf.
architecture: DIRECT_SCOPED_LEAF
partition_digest: 66dff80464465ec96253a4c10d518dc488d29e83e9b6cd5272b2ac8a136e8f41
atom_or_cell: RS_PHASE_STRUCTURED_SIDON_PAYMENT / p2 quadratic-locator band
quantifier: all 64 residual supports and all 9 realized p2 keys
projection_and_unit: phase-weighted supports; not slopes/codewords
claimed_bound: phaseAwareL1 = phaseCollisionMoment = 0
status: PROVED
impact: LOCAL_ONLY; acceptance criterion 2
falsifier: non-exact owner complement, non-root domain point, broken pairing, ambient normalization, or nonzero phase coefficient
replay: python3 experimental/scripts/verify_rs_phase_structured_sidon.py; python3 -O experimental/scripts/verify_rs_phase_structured_sidon.py
```

## 1. Base and overlap preflight

- Fork: `holmbuar/rs-mca`
- Branch: `gptpro/rs-phase-structured-sidon`
- Pinned fork base: `4e5f0b77c98f075ea7c8822cd4859847a232bc2a`
- Upstream main at lane start: `a3017697ad1594521d2779fe1d83bccd45d4c06e`
- Fork main contains the upstream head plus fork-only CI workflow commits; no mathematical fork-only delta was imported.
- The ten newest upstream PR descriptions and ten newest fork draft-PR descriptions were inspected. #1026 names this exact successor. #1027 proves a loss-one key on the same finite leaf but does not prove phase cancellation. No active lane owns this quadratic-locator `p2` cancellation theorem.

No file under `.github/` is modified.

## 2. Imported API blob table

The Lean module imports only `Std`; it locally restates the finite leaf and owner-complement grammar. Therefore no integrated `AsymptoticSpine.*` or `M31QRootedShell.*` API is imported.

| Imported integrated API | Fork blob | Upstream blob | Verdict |
|---|---|---|---|
| none | — | — | No applicable blob comparison; module imports only `Std` |

This satisfies the no-open-PR-import rule and avoids silently depending on `M31C9RowSharp`, `HalfSliceFalsifier`, or another lane module.

## 3. Exact proved declaration table

| Lean declaration | Exact statement audited | Source/proof role |
|---|---|---|
| `field_prime_exact` | `p=2147483647` | deployed field |
| `full_slice_card` | complete moving weight-four slice has 70 supports | full family |
| `residual_slice_card` | explicit owner complement has 64 supports | genuine survivor |
| `owner_complement_exact` | residual membership equals full-slice membership and absence of the explicit C1 owner | first-match deletion |
| `antipodal_pairs_exact` | four printed domain pairs sum to zero mod `p` | RS involution |
| `c1_antipodal_owner_exact` | C1 masks are exactly all unions of two complete antipodal pairs | semantic owner shape |
| `domain_points_are_deployed_roots` | all eight points satisfy `T_(2^21)(x)=0` mod `p` | actual deployed RS domain |
| `quadratic_phase_defined_on_residual` | Euler phase is always `±1` on the residual | locator phase |
| `pairing_exhausts_residual` | the 32 printed pairs are a duplicate-free cover of all 64 survivors | exhaustive involution |
| `pairing_cancels_p2_phase` | every pair preserves `p2` and has opposite locator phase | cancellation theorem |
| `realized_image_card` | `A_eff=L=9` | corrected normalization |
| `realized_fiber_sizes` | exact sizes `[8,8,8,8,16,4,4,4,4]` | unsigned comparison |
| `phase_coefficients_zero` | every realized signed coefficient is zero | phase payment |
| `phase_aware_l1_exact` | phase-aware L1 aggregate is zero | MI+MA-style aggregate |
| `phase_collision_moment_exact` | signed collision moment is zero | Sidon-moment analogue |
| `unsigned_collision_moment_exact` | unsigned collision moment is 576 | absolute-mass contrast |
| `natural_scale_exact` | `ceil(64/9)=8` | realized image scale |
| `phase_multiplier_one_payment` | exact multiplier-one phase inequality | scoped payment |
| `image_compensated_phase_payment` | same payment after multiplying by realized `A_eff=9` | corrected compensation |
| `deployed_dimensions` | exact M31 row constants and outside-support embedding | deployed calibration |
| `phase_scale_fits_deployed_budget` | local scale `8` is at most `2^24-1` | arithmetic context only |

Every finite statement carries its full displayed object; no global owner, profile census, slope compiler, or add-back theorem is hidden in a definition.

## 4. Certificate and independent replay

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

Local exact replay before publication:

```text
python3 experimental/scripts/verify_rs_phase_structured_sidon.py
python3 -O experimental/scripts/verify_rs_phase_structured_sidon.py
```

Both return `VERDICT: PROVED_SCOPED_PHASE_PAYMENT`.

## 5. Lean validation and axiom census

- Package: `experimental/lean/sidon_effective_image`
- Lean: `v4.31.0`
- Imports: `Std` only
- Root: `SidonEffectiveImage.lean`, importing only `SidonEffectiveImage.RSPhaseStructuredSidon`
- `sorry`: 0 by source audit and green compilation
- `admit`: 0 by source audit and green compilation
- `native_decide`: 0 by source audit
- custom axioms: 0
- CI draft PR: `holmbuar/rs-mca#81`, `CI: M31 RS phase-structured cancellation`
- Recorded validation head SHA: `5ccf797ade4b73c586141c7dd5a4203d174c2c29`
- `lean/sidon_effective_image`: **SUCCESS**
- Workflow run: `29851661095` (`Lean build — PR #81`, run number 152)
- Build-log artifact: `lean-build-log-0`, artifact `8503607048`, digest `sha256:3677164b0313522c23eeb9541264b577f670be91fdc0c51355498939738a587e`
- Explicit targets built: `SidonEffectiveImage` and `SidonEffectiveImage.RSPhaseStructuredSidon`
- Default package target built: `SidonEffectiveImage`
- `#print axioms` census: `field_prime_exact`, `antipodal_pairs_exact`, `domain_points_are_deployed_roots`, and `deployed_dimensions` depend on no axioms; every other printed declaration depends only on standard `propext`. No declaration depends on `sorryAx`, a custom axiom, `Classical.choice`, or `Quot.sound`.

Green CI certifies compilation only; the declaration/source match is the table in Section 3.

## 6. Explicit nonclaims

This packet does not:

- prove a full three-coordinate C9 max-fiber or Sidon theorem;
- prove that phase cancellation bounds an unsigned support/codeword/slope count;
- import or instantiate the open C9 producer;
- prove exhaustive fixed-before-line C1--C8 ownership;
- count all fixed-outside profiles;
- prove residual-to-full add-back, line-local `UNIF`, or target-envelope comparison;
- bank `U_Q`, `U_BC`, `U_list_int`, or another exact deployed row atom;
- prove an adjacent safe row or Prize claim.

## 7. Acceptance gate

**Criterion 2 is met.** The theorem bounds a genuine post-C1 survivor on actual Mersenne-31 RS domain points after an explicit owner deletion. The exact phase-aware payment is zero at the realized image scale. The packet is not an interface or adapter.

OPEN GAP
