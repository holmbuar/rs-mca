---
workboard_item: M1
row: Mersenne-31 list at 2^-100
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: Audit the exact eight-point post-C1 leaf and the image-compensated absolute minor/major aggregate theorem with identity effective-character lifts.
architecture: DIRECT
partition_digest: M31-EIGHT-POINT-C1-COMPLEMENT-V1
atom_or_cell: C9_IMAGE_COMPENSATED_EFFECTIVE_MI_MA
quantifier: Every declaration in M31CompensatedAggregates.lean and every exact enumeration, span, partition, and compensation gate in the canonical JSON certificate.
projection_and_unit: Prefix-support fibers and source-normalized effective Fourier aggregate ceilings only; slopes, codewords, and row budgets remain external.
claimed_bound: Exact full/residual census 70/69/64/64; full effective span p^3; compensated minor <=1, major <=69, full multiplier <=69.
status: PROVED
impact: LOCAL_ONLY
falsifier: A statement/source mismatch, non-identical imported API blob, failed mutation, non-green Lean target, unexpected axiom, or any failed exact integer gate.
replay: Fork draft PR CI plus normal/optimized certificate and tamper replay.
---

# Audit: M31 image-compensated effective aggregates

## 1. Audit verdict and gate

This packet satisfies acceptance criterion **2**: it bounds an explicit
nonempty post-C1 primitive residual on the actual Mersenne-31 Chebyshev domain.
It does not claim deployed row closure.

The mathematical result is not an interface-only adapter.  The packet fixes the
actual eight field points, enumerates the complete weight-four slice, proves the
literal earlier-owner complement, supplies a two-sided span inverse, chooses a
nonempty certified minor/major partition, bounds the whole absolute major sum,
and checks the exact image-compensated constants.

## 2. Pinned provenance

| Object | Fork/main | Upstream/main | Verdict |
|---|---:|---:|---|
| base commit | `4e5f0b77c98f075ea7c8822cd4859847a232bc2a` | upstream integrated at `a3017697ad1594521d2779fe1d83bccd45d4c06e` | fork already synchronized through Grande Finale v4 |
| `experimental/grande_finale.tex` | blob `8a5d9791900ca9eed773feba146b92ad296704ce` | same integrated v4 content | source authority pinned |

The branch is `gptpro/image-compensated-aggregates`, created from the exact fork
base above.  No file under `.github/` is touched.

## 3. Imported integrated API parity

The new module directly imports only the following integrated APIs.  Connector
reads of fork `main` and upstream `main` returned the same blob SHA in every row.

| Direct import | fork blob | upstream blob | Byte-identical |
|---|---|---|---|
| `AsymptoticSpine.PrimitiveBoolean` — `experimental/lean/asymptotic_spine/AsymptoticSpine/PrimitiveBoolean.lean` | `777273e4377c31c815062769803622c6226988d3` | `777273e4377c31c815062769803622c6226988d3` | yes |
| `M31QRootedShell.Deployed` — `experimental/lean/m31_q_rooted_shell/M31QRootedShell/Deployed.lean` | `7e21ff098567d26aba7330fbb2722d5cb952fb09` | `7e21ff098567d26aba7330fbb2722d5cb952fb09` | yes |

No open-PR module is imported.  In particular, the module does not import
`M31C9RowSharp`, `HalfSliceFalsifier`, or a producer module.  The small support,
owner, prefix, and matrix definitions needed for this packet are restated in the
new module.

## 4. Exact PROVED declaration table

All declarations are in
`SidonEffectiveImage.M31CompensatedAggregates`.

| Lean declaration | Exact statement audited | Mathematical source/boundary | Status |
|---|---|---|---|
| `residual_exact` | residual membership iff full-slice membership and the generic C1 owner is absent | literal owner-complement definition | PROVED |
| `scoped_residual_exact` | the local C1--C8 grammar instantiates the exact owner complement | only C1 is nonempty in this scoped profile | PROVED |
| `domain_points_are_deployed_roots` | all eight printed residues satisfy the `T_(2^21)` recurrence | actual M31 Chebyshev domain | PROVED |
| `antipodal_pairs_exact` | the four displayed pairs sum to zero modulo `p` | C1 quotient geometry | PROVED |
| `t4_fibers_exact` | the first and last four points are complete, distinct `T_4` fibers | doubled-key ownership check | PROVED |
| `full_slice_card` | complete weight-four slice has `70` supports | exhaustive `8`-bit enumeration | PROVED |
| `full_image_card` | first-three-power-sum image has `69` keys | exhaustive prefix enumeration | PROVED |
| `residual_slice_card` | deleting the six C1 owners leaves `64` supports | exact owner deletion | PROVED |
| `residual_prefix_injective` | the residual prefix-key list is duplicate-free | exhaustive post-deletion enumeration | PROVED |
| `residual_image_card` | residual realized image has `64` keys | exact image census | PROVED |
| `selected_key_exact` | mask `51` has the printed prefix key | exact prefix arithmetic | PROVED |
| `selected_residual_prefix_singleton` | the selected post-owner residual fiber is exactly one support | genuine scoped survivor | PROVED |
| `selected_not_earlier` | mask `51` is a genuine survivor of the displayed owner | exact owner-complement theorem | PROVED |
| `basis_matrix_exact` | the three moment-column differences equal the printed matrix | `eq:effective-fourier-span` input | PROVED |
| `basis_inverse_certificate` | printed inverse is two-sided modulo `p` | proves `V_g=F_p^3`, hence `A_eff=p^3` | PROVED |
| `character_partition` | every nontrivial character is minor (`a1=0`) or major (`a1!=0`) | `def:effective-major-minor` | PROVED |
| `character_partition_disjoint` | the two character classes are disjoint | certified partition | PROVED |
| `certifiedAmbientLift_eq` | effective-to-ambient lift is identity | full effective span | PROVED |
| `partition_nonempty` | explicit minor and major witnesses exist | excludes vacuous major route | PROVED |
| `source_image_constants_exact` | literal constants `M=70`, `L=69` match the executable slice | image normalization | PROVED |
| `character_count_partition` | `1+(p^2-1)+(p^3-p^2)=p^3` | exact dual census | PROVED |
| `compensated_minor_count` | `69(p^2-1) <= p^3` | cleared `(L/A_eff) C_min <=1` count gate | PROVED |
| `compensated_major_count` | `69(p^3-p^2) <=69p^3` | cleared `(L/A_eff) C_maj <=69` count gate | PROVED |
| `compensated_minor_of_triangle` | any minor absolute-mass ceiling satisfying the literal triangle count obtains compensated loss one | all hypotheses explicit | PROVED |
| `compensated_major_of_triangle` | any major absolute-mass ceiling satisfying the literal triangle count obtains compensated loss `69` | real whole-major aggregate; all hypotheses explicit | PROVED |
| `compensated_full_of_triangle` | trivial character plus both aggregate ceilings obtains multiplier `69` | exact compensated Fourier triangle inequality | PROVED |
| `deployed_constants` | prints `p`, `w`, `listM`, and `B_star` separately | denominator/row metadata only | PROVED |

The complex Fourier triangle step itself is the elementary paper proof: every
coefficient is a sum of 70 unit-modulus terms.  The stdlib-only Lean module
formalizes the exact finite leaf, span/lift certificate, partition, count gates,
and the cleared arithmetic implication from the literal aggregate ceilings.  It
does not pretend that Lean's natural-number ceilings are a formal construction
of complex absolute values.

## 5. Source-label map

| Grande Finale v4 label | Packet declaration or proof |
|---|---|
| `eq:effective-fourier-span` | `basis_matrix_exact`, `basis_inverse_certificate` |
| `lem:effective-span-fourier` | paper proof of the full-fiber triangle inequality and residual monotonicity |
| `def:effective-major-minor` | `character_partition`, `character_partition_disjoint`, `certifiedAmbientLift_eq`, `partition_nonempty` |
| `def:aggregate-minor-payment` | minor absolute sum and `compensated_minor_of_triangle` |
| `def:major-arc-aggregate` | nonempty whole major sum and `compensated_major_of_triangle` |
| `lem:sparse-major-payment` | exact character-count times `M` triangle envelope |
| `prop:effective-mi-ma-flatness` | consumer boundary; this packet inserts the necessary `L/A_eff` compensation explicitly |

The support-to-slope boundary is deliberately absent.  No support count is
silently called an MCA numerator.

## 6. Certificate audit

Files:

```text
experimental/data/certificates/
  sidon-effective-image-image-compensated-aggregates/
  m31_image_compensated_aggregates.json

experimental/scripts/verify_m31_image_compensated_aggregates.py
```

The verifier is stdlib-only and independently recomputes:

- all `70` weight-four support masks;
- the `69` full prefix keys and unique doubled key;
- the six exact C1 owner masks;
- the `64` residual supports and `64` residual keys;
- every Chebyshev-root, antipodal, and `T_4`-fiber check;
- the moment-difference matrix and both inverse products;
- `p^2-1`, `p^3-p^2`, and the exact partition identity;
- all three cleared compensated inequalities and their printed slacks.

Replay before publication:

```text
python3 experimental/scripts/verify_m31_image_compensated_aggregates.py --check
  PASS
python3 -O experimental/scripts/verify_m31_image_compensated_aggregates.py --check
  PASS
python3 experimental/scripts/verify_m31_image_compensated_aggregates.py --tamper-selftest
  PASS, 10/10 rejected
python3 -O experimental/scripts/verify_m31_image_compensated_aggregates.py --tamper-selftest
  PASS, 10/10 rejected
```

## 7. Lean validation and axiom census

```text
Lean toolchain: 4.31.0
stdlib only: yes
Mathlib imports: 0
native_decide: 0
sorry/admit/sorryAx: 0 by source census
custom axiom declarations: 0 by source census
fork draft PR: AWAITING_CREATION
workflow run: AWAITING_FORK_CI
module/root result: AWAITING_FORK_CI
#print axioms result: AWAITING_FORK_CI
```

Green CI will prove compilation only.  The declaration/source comparison is the
table in Section 4.

## 8. Explicit nonclaims

1. The local owner complement is not an exhaustive deployed C1--C8 atlas.
2. The packet proves no all-key M31 max-fiber theorem and sets no `U_Q` atom.
3. The packet proves no `(SE2)` slope injection, ray compiler, codeword count,
   list numerator, or MCA numerator.
4. No profile count, residual-to-full add-back, owner disjointization, line-local
   sum, or `UNIF` theorem is supplied.
5. The exact finite constants are not promoted to a uniform asymptotic family.
6. The result uses absolute values inside both aggregates and claims no phase
   cancellation theorem.
7. `q_gen`, `q_line`, `q_chal`, and `q_list` remain distinct.
8. No stable TeX, deployed endpoint, official score, or prize claim changes.

NO ISSUE
