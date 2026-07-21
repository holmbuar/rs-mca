---
workboard_item: T
row: FAMILY-LEVEL RS TRACE-LINEAR PHASE OBSTRUCTION
object: OTHER
target_epsilon: NOT_INSTANTIATED
agreement: NOT_INSTANTIATED
B_star: NOT_INSTANTIATED
direct_statement: The affine-basis degree-one RS trace-phase family has a complete globally balanced cyclotomic phase histogram with no within-histogram cancellation, an exact p=3,r=5 histogram falsifier, a fixed-order exponential image-compensated floor, and a growing-order super-exponential raw floor for histogram-local nonnegative payments.
architecture: DIRECT
partition_digest: NOT_APPLICABLE_DIRECT
atom_or_cell: RS_PHASE_STRUCTURED_SIDON_PAYMENT
quantifier: Every odd prime p and integer r>=1 in the declared family; finite kernel arithmetic at p=3,r=5.
projection_and_unit: effective-character coherent Fourier histogram mass; not slopes, rays, codewords, or a deployed row atom
claimed_bound: A_hist>=A_split and A_split/A_eff >= p*2^(2r)/((pr+1)^(2(p-1))*(2r+1)); finite A_hist=155428415166024>6*3^28.
status: COUNTEREXAMPLE
impact: ROUTE_CUT
falsifier: A nonnegative histogram-local MI+MA payment must pay the complete balanced histogram; exact inversion forces other histograms to have signed sum -132551777828583 at p=3,r=5.
replay: python3 experimental/scripts/verify_sidon_effective_image_cyclotomic_phase_floor.py --check; python3 -O experimental/scripts/verify_sidon_effective_image_cyclotomic_phase_floor.py --check
---

# Audit: trace-linear cyclotomic phase floor

## Gate, predecessor correction, and claim boundary

**Acceptance criterion 4 — `COUNTEREXAMPLE_NEW_FLOOR`.**

```text
route cut: PHASE_HISTOGRAM_LOCAL_MI_MA
successor: ACTUAL_LEAF_CROSS_HISTOGRAM_CANCELLATION_OR_DIRECT_SIDON
```

This is a hostile successor audit of predecessor lane head
`927bd5081a3dc12c51d63ff9081e9bd77d6e3c91`.

The predecessor's general split-balanced subblock theorem was correct. Its
finite number

```text
A_eff-M-A_split=-25228452719583
```

was also correct as the signed sum outside that **subblock**. The phrase
“exact cross-histogram debt” was too strong, because additional characters of
the same globally balanced histogram lie outside the split-balanced subset.
This packet fixes the statement by counting the complete balanced histogram.
The corrected exact other-histogram debt is

```text
A_other=-132551777828583.
```

The construction remains the genuine degree-one RS map `g(t)=t` on
`K=F_(p^(N-2))`, with evaluation domain
`T={0,e_1,...,e_(N-2),u}` and `u=-(e_1+...+e_(m-1))`.
The threshold note now proves domain distinctness explicitly, then proves
injectivity, the unique attained zero target, trace-code parametrization, the
split subblock formula, the complete-histogram formula, and the two asymptotic
regimes.

The route cut is exact but narrow: it refutes nonnegative **histogram-local**
MI+MA replacements. It does not refute a target-coupled signed argument that
combines different histograms before charging them.

## Exact PROVED declaration table

| Declaration | Exact statement | Authority |
|---|---|---|
| `TRACE_LINEAR_DOMAIN` | `T` has exactly `N` distinct elements | threshold note; exhaustive regression |
| `TRACE_LINEAR_PHASE_CODE` | trace pairing gives all basis phases with `y_0=0`, `y_u=-sum_(i<m)y_i` | threshold note |
| `FIXED_WEIGHT_INJECTIVE_ZERO_TARGET` | `M=L=binom(N,m)` and `Psi^(-1)(0)={S_*}` | threshold note; exhaustive regression |
| `SPLIT_BALANCED_BLOCK_COUNT` | `B_split=H_(p,r)^2/p`, `H=(pr)!/(r!)^p` | threshold note |
| `BALANCED_HISTOGRAM_COHERENCE` | every globally balanced character has coefficient `binom(2r,r)>0` | threshold note; exact cyclotomic verifier |
| `FIXED_ORDER_COMPENSATED_FLOOR` | `A_hist/A_eff >= A_split/A_eff >= p*2^(2r)/((pr+1)^(2(p-1))*(2r+1))` | threshold note |
| `GROWING_ORDER_RAW_FLOOR` | fixed `r>=2`, odd `p->infinity`: `A_hist/M>=A_split/M=exp(Omega_r(N log N))` | threshold note |
| `REGRESSION_COMPLETE_HISTOGRAM` | at `p=3,r=2`, exactly 3900 balanced-histogram characters, coefficient 6, mass 23400 | exhaustive verifier |
| `FINITE_COMPLETE_HISTOGRAM_COUNT` | at `p=3,r=5`, complete histogram count `616779425262` | threshold note; verifier; Lean frozen 29-term formula |
| `regression_phase_code_size_exact` | `3^10=59049` | Lean |
| `regression_source_mass_exact` | `binom(12,6)=924` | Lean |
| `regression_split_balanced_block_count_exact` | split regression block `=2700` | Lean + exhaustive verifier |
| `regression_cyclotomic_coefficient_exact` | coefficient `=6` | Lean + exact cyclotomic verifier |
| `regression_split_balanced_block_mass_exact` | split regression sum `=16200` | Lean + exhaustive verifier |
| `source_mass_exact` | `binom(30,15)=155117520` | Lean |
| `effective_target_size_exact` | `3^28=22876792454961` | Lean |
| `half_balanced_count_exact` | `756756` | Lean |
| `anchored_complement_balanced_count_exact` | `252252` | Lean |
| `split_balanced_block_count_exact` | `190893214512` | Lean |
| `cyclotomic_coefficient_exact` | `252` | Lean |
| `split_balanced_block_mass_exact` | `48105090057024` | Lean |
| `split_balanced_double_gap_exact` | `A_split=2*A_eff+2351505147102` | Lean |
| `balanced_histogram_count_exact` | complete histogram count `616779425262` | Lean frozen formula + verifier completeness check |
| `balanced_histogram_mass_exact` | complete histogram mass `155428415166024` | Lean |
| `balanced_histogram_six_gap_exact` | `A_hist=6*A_eff+18167660436258` | Lean |
| `split_balanced_block_exceeds_double_effective_target` | `2*A_eff<A_split` | Lean |
| `balanced_histogram_exceeds_six_effective_targets` | `6*A_eff<A_hist` | Lean |
| `split_source_payment_kappa_floor` | `A_split<=(kappa-1)M` implies `310122<=kappa` | Lean |
| `histogram_source_payment_kappa_floor` | `A_hist<=(kappa-1)M` implies `1002006<=kappa` | Lean |
| `outside_split_subblock_signed_sum_exact` | `A_eff-M-A_split=-25228452719583` | Lean |
| `other_histogram_signed_debt_exact` | `A_eff-M-A_hist=-132551777828583` | Lean |
| `exact_histogram_fourier_balance` | `M+A_hist-132551777828583=A_eff` | Lean |
| `no_nonnegative_histogram_balance` | no natural other-histogram remainder closes the balance | Lean |

Every row is **PROVED** at its displayed scope. The general theorem is a
family-level route cut, not a deployed-row payment.

## Replay

Certificate:
`experimental/data/certificates/sidon-effective-image-cyclotomic-phase-floor/sidon_effective_image_cyclotomic_phase_floor.json`.

Verifier:
`experimental/scripts/verify_sidon_effective_image_cyclotomic_phase_floor.py`.

It is Python-stdlib-only and independently implements exact arithmetic in
`Z[zeta_3]`. At `p=3,r=2` it exhausts all `3^10` trace-linear phase words and
all `binom(12,6)` supports. It checks the complete character sum, domain
distinctness, singleton fibers, the split subblock, the complete balanced
histogram, and the unique zero target. At `p=3,r=5` it checks the exact
29-triple complete-histogram formula, both payment floors, the exact signed
other-histogram debt, a grid of general lower bounds, and eight fail-closed
mutations. No floating point decides a gate.

```text
python3 experimental/scripts/verify_sidon_effective_image_cyclotomic_phase_floor.py --check
python3 -O experimental/scripts/verify_sidon_effective_image_cyclotomic_phase_floor.py --check
RESULT: PASS (6762 exact checks, 8 rejected mutations, mode=full-enumeration)
```

## Source labels and provenance

| Packet statement | `experimental/grande_finale.tex` label |
|---|---|
| degree-one RS map | `eq:exact-power-sum-map` |
| effective target/Fourier denominator | `eq:effective-fourier-span`, `lem:effective-span-fourier` |
| separately paid nonnegative aggregate | `def:effective-fourier-payment` |
| phase-aware major aggregation | `def:major-arc-aggregate` |
| source/image scales | `eq:image-ambient-scales`, `def:primitive-q` |
| small-characteristic boundary | `rem:small-characteristic-cycles` |
| positive shallow theorem boundary | `thm:unconditional-shallow-mi-ma` |

Base fork main: `4e5f0b77c98f075ea7c8822cd4859847a232bc2a`.
Upstream main: `a3017697ad1594521d2779fe1d83bccd45d4c06e`.
Predecessor lane head: `927bd5081a3dc12c51d63ff9081e9bd77d6e3c91`.
Successor branch: `gptpro/rs-phase-floor-hunt-pro-audit`.

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

## Lean census and workflow preflight

```text
package: experimental/lean/sidon_effective_image
toolchain: Lean 4.31.0
stdlib only; Mathlib imports 0
repository API imports 0; open-PR imports 0
native_decide 0
sorry 0; admit 0; custom axioms 0; unsafe declarations 0
autoImplicit false
root imports only SidonEffectiveImage.CyclotomicPhaseFloor
lakefile requires 0
```

The predecessor CI failed twice before compilation because
`leanprover/lean-action@v1.5.0` unconditionally rejects a package without
`lake-manifest.json`, even when the lakefile has no `require`. The successor
packet adds the canonical empty manifest generated for this package shape; no
`.lake/` content or build output is committed.

Fork CI record: **AWAITING_SUCCESSOR_FORK_CI**.

Axiom output record: **AWAITING_SUCCESSOR_FORK_CI**. The revised module ends
with `#print axioms` for every theorem in the Lean section of the PROVED table.

## Explicit nonclaims

- No actual post-C1--C8 Mersenne-31 or KoalaBear survivor is constructed.
- No first-match owner complement, profile census, row atom, row numerator,
  slope/ray compiler, line-local uniformity theorem, adjacent-row certificate,
  safe radius, score, or prize claim changes.
- The theorem does not refute a global target-coupled signed method that combines
  different histograms before assigning nonnegative budgets.
- It proves no lower bound on the true MCA or list numerator.
- `K`, `F_p`, the effective target, and deployed row fields remain distinct; no
  extension-field result is transferred to a live row.
- Green CI proves compilation only; the statement/source audit is the table
  above.

COUNTEREXAMPLE_NEW_FLOOR
