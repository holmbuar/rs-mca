---
workboard_item: T
row: FAMILY-LEVEL RS TRACE-LINEAR PHASE OBSTRUCTION
object: OTHER
target_epsilon: NOT_INSTANTIATED
agreement: NOT_INSTANTIATED
B_star: NOT_INSTANTIATED
direct_statement: The affine-basis degree-one RS trace-phase family has a coherent cyclotomic phase block with no within-block cancellation, an exact p=3,r=5 finite falsifier, a fixed-order exponential image-compensated floor, and a growing-order super-exponential raw floor.
architecture: DIRECT
partition_digest: NOT_APPLICABLE_DIRECT
atom_or_cell: RS_PHASE_STRUCTURED_SIDON_PAYMENT
quantifier: Every odd prime p and integer r>=1 in the declared family; finite kernel arithmetic at p=3,r=5.
projection_and_unit: effective-character coherent Fourier block mass; not slopes, rays, codewords, or a deployed row atom
claimed_bound: A_phase/A_eff >= p*2^(2r)/((pr+1)^(2(p-1))*(2r+1)); finite A_phase=48105090057024>2*3^28.
status: COUNTEREXAMPLE
impact: ROUTE_CUT
falsifier: A nonnegative histogram-local MI+MA payment must pay a coherent block whose exact compensated mass is already >2 at p=3,r=5; exact inversion forces a negative cross-histogram debt.
replay: python3 experimental/scripts/verify_sidon_effective_image_cyclotomic_phase_floor.py --check; python3 -O experimental/scripts/verify_sidon_effective_image_cyclotomic_phase_floor.py --check
---

# Audit: trace-linear cyclotomic phase floor

## Gate and claim boundary

**Acceptance criterion 4 — `COUNTEREXAMPLE_NEW_FLOOR`.**

```text
route cut: PHASE_HISTOGRAM_LOCAL_MI_MA
successor: ACTUAL_LEAF_CROSS_HISTOGRAM_CANCELLATION_OR_DIRECT_SIDON
```

The construction is the genuine degree-one RS map `g(t)=t` on
`K=F_(p^(N-2))`, with evaluation domain
`T={0,e_1,...,e_(N-2),u}` and
`u=-(e_1+...+e_(m-1))`. Effective characters are trace-linear phases, not
assigned phase words. The threshold note proves injectivity, the unique attained
zero target, the trace-code parametrization, the coherent block formula, and
the two asymptotic regimes.

## Exact PROVED table

| Declaration | Exact statement | Authority |
|---|---|---|
| `TRACE_LINEAR_PHASE_CODE` | trace pairing gives all basis phases and `y_u=-sum_(i<m)y_i` | threshold note |
| `FIXED_WEIGHT_INJECTIVE_ZERO_TARGET` | `M=L=binom(N,m)` and `Psi^(-1)(0)={S_*}` | threshold note |
| `CYCLOTOMIC_BLOCK_COUNT` | block count `H_(p,r)^2/p`, `H=(pr)!/(r!)^p` | threshold note |
| `CYCLOTOMIC_BLOCK_COHERENCE` | every block coefficient is `binom(2r,r)>0`; signed block sum equals block mass | threshold note |
| `FIXED_ORDER_COMPENSATED_FLOOR` | `A_phase/A_eff >= p*2^(2r)/((pr+1)^(2(p-1))*(2r+1))` | threshold note |
| `GROWING_ORDER_RAW_FLOOR` | fixed `r>=2`, odd `p->infinity`: `A_phase/M=exp(Omega_r(N log N))` | threshold note |
| `regression_phase_code_size_exact` | `3^10=59049` | Lean |
| `regression_source_mass_exact` | `binom(12,6)=924` | Lean |
| `regression_coherent_block_count_exact` | coherent regression block `=2700` | Lean + exhaustive verifier |
| `regression_cyclotomic_coefficient_exact` | coefficient `=6` | Lean + exact cyclotomic verifier |
| `regression_coherent_block_mass_exact` | coherent regression sum `=16200` | Lean + exhaustive verifier |
| `source_mass_exact` | `binom(30,15)=155117520` | Lean |
| `effective_target_size_exact` | `3^28=22876792454961` | Lean |
| `half_balanced_count_exact` | `756756` | Lean |
| `anchored_complement_balanced_count_exact` | `252252` | Lean |
| `coherent_block_count_exact` | `190893214512` | Lean |
| `cyclotomic_coefficient_exact` | `252` | Lean |
| `coherent_block_mass_exact` | `48105090057024` | Lean |
| `coherent_block_double_gap_exact` | `A_phase=2*A_eff+2351505147102` | Lean |
| `coherent_block_exceeds_double_effective_target` | `2*A_eff<A_phase` | Lean |
| `source_payment_kappa_floor` | `A_phase<=(kappa-1)M` implies `310122<=kappa` | Lean |
| `signed_complement_debt_exact` | `A_eff-M-A_phase=-25228452719583` | Lean |
| `exact_fourier_balance` | `M+A_phase-25228452719583=A_eff` | Lean |
| `no_nonnegative_blockwise_balance` | no natural remainder closes that balance | Lean |

Every row is **PROVED**. The `p=3,r=5` row is the criterion-4 falsifier; the
`p=3,r=2` row is an exhaustive regression.

## Replay

Certificate:
`experimental/data/certificates/sidon-effective-image-cyclotomic-phase-floor/sidon_effective_image_cyclotomic_phase_floor.json`.

Verifier:
`experimental/scripts/verify_sidon_effective_image_cyclotomic_phase_floor.py`.

It is stdlib-only. At `p=3,r=2` it exhausts all `3^10` trace-linear phase
words and all `binom(12,6)` supports, using exact arithmetic in
`Z[zeta_3]`. It also checks the `p=3,r=5` formulas, a grid of general lower
bounds, and five fail-closed mutations. No floating point decides a gate.

```text
python3 experimental/scripts/verify_sidon_effective_image_cyclotomic_phase_floor.py --check
python3 -O experimental/scripts/verify_sidon_effective_image_cyclotomic_phase_floor.py --check
RESULT: PASS (2841 exact checks, 5 rejected mutations, mode=full-enumeration)
```

## Source labels and provenance

| Packet statement | `experimental/grande_finale.tex` label |
|---|---|
| degree-one RS map | `eq:exact-power-sum-map` |
| effective target/Fourier denominator | `eq:effective-fourier-span`, `lem:effective-span-fourier` |
| separately paid block | `def:effective-fourier-payment` |
| phase-aware major aggregation | `def:major-arc-aggregate` |
| source/image scales | `eq:image-ambient-scales`, `def:primitive-q` |
| small-characteristic boundary | `rem:small-characteristic-cycles` |
| positive shallow theorem boundary | `thm:unconditional-shallow-mi-ma` |

Base fork main: `4e5f0b77c98f075ea7c8822cd4859847a232bc2a`.
Upstream main: `a3017697ad1594521d2779fe1d83bccd45d4c06e`.
The fork was ahead by 15 and behind by 0 at branch time.

### Imported integrated API SHA table

The module imports only `Std`: no `AsymptoticSpine.*`, no
`M31QRootedShell.*`, and no open-PR module. Hence the required imported-API
identity set is empty.

| Imported integrated API | Fork blob | Upstream blob | Result |
|---|---:|---:|---|
| none (`import Std` only) | -- | -- | **VACUOUSLY BYTE-IDENTICAL** |

| Proof source | Fork blob | Upstream blob | Result |
|---|---|---|---|
| `experimental/grande_finale.tex` | `8a5d9791900ca9eed773feba146b92ad296704ce` | `8a5d9791900ca9eed773feba146b92ad296704ce` | **BYTE-IDENTICAL** |
| `experimental/rs_mca_thresholds.tex` | `01302a797c502a05ed0b11ba949b8756e0aa2b22` | `01302a797c502a05ed0b11ba949b8756e0aa2b22` | **BYTE-IDENTICAL** |

## Lean census

```text
package: experimental/lean/sidon_effective_image
toolchain: Lean 4.31.0
stdlib only; Mathlib imports 0
repository API imports 0; open-PR imports 0
native_decide 0
sorry 0; admit 0; custom axioms 0; unsafe declarations 0
root imports only SidonEffectiveImage.CyclotomicPhaseFloor
lakefile requires 0; no lake-manifest.json required
```

Fork CI record: **AWAITING_FORK_CI**.

Axiom output record: **AWAITING_FORK_CI**. The module ends with `#print axioms`
for every load-bearing declaration.

## Explicit nonclaims

- No actual post-C1--C8 Mersenne-31 or KoalaBear survivor is constructed.
- No first-match owner complement, profile census, row atom, row numerator,
  slope/ray compiler, line-local uniformity theorem, adjacent-row certificate,
  safe radius, score, or prize claim changes.
- The theorem does not exclude a global target-coupled method that cancels
  different histograms before assigning nonnegative budgets.
- `K`, `F_p`, the effective target, and deployed row fields remain distinct;
  no extension-field result is transferred to a live row.
- Green CI proves compilation only; the statement/source audit is the table
  above.

COUNTEREXAMPLE_NEW_FLOOR
