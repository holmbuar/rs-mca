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

## Gate, corrected predecessor claim, and exact boundary

**Acceptance criterion 4 — `COUNTEREXAMPLE_NEW_FLOOR`.**

```text
route cut: PHASE_HISTOGRAM_LOCAL_MI_MA
successor: ACTUAL_LEAF_CROSS_HISTOGRAM_CANCELLATION_OR_DIRECT_SIDON
```

This successor audit branches from predecessor head
`927bd5081a3dc12c51d63ff9081e9bd77d6e3c91`.

The predecessor's general split-balanced subblock theorem and all of its printed
subblock integers were correct. One label was not: the identity

```text
A_eff-M-A_split=-25228452719583
```

is the exact signed sum outside the certified **split subblock**, not the exact
sum outside the complete phase histogram. Additional characters with the same
globally balanced phase histogram lie outside that subblock. This packet counts
the complete histogram and proves the corrected other-histogram debt

```text
A_other=-132551777828583.
```

The route cut is correspondingly precise. It refutes a proof interface that
assigns separate nonnegative budgets to phase histograms. It does not refute a
target-coupled signed method that combines different histograms before charging
them, nor a direct image-normalized Sidon/max-fiber theorem.

## Mathematical audit

The construction is the genuine degree-one RS map `g(t)=t` on
`K=F_(p^(N-2))`, where `p` is an odd prime, `r>=1`, `N=2pr`, `m=pr`,

```text
T={0,e_1,...,e_(N-2),u},
u=-(e_1+...+e_(m-1)),
S_*={e_1,...,e_(m-1),u},
Psi(S)=sum_(t in S)t.
```

Because `m-1>=2` and `-1!=0` in `F_p`, the basis expansion of `u` has at
least two nonzero coordinates. Thus `u` is neither zero nor a basis vector, and
`T` has exactly `N` distinct points.

Comparing basis coefficients in a collision shows that all incidence
differences vanish; equal cardinality rules out the only possible nonzero
common difference. Therefore `Psi` is injective on the `m`-slice and
`Psi^(-1)(0)={S_*}`. Hence

```text
M=L=binom(N,m),
A_eff=p^(N-2).
```

The nondegenerate trace pairing gives all effective characters as actual
`p`-th-root phases. A certified split-balanced subblock has

```text
H_(p,r)=(pr)!/(r!)^p,
B_split=H_(p,r)^2/p,
A_split=(H_(p,r)^2/p)*binom(2r,r).
```

Every character in the complete globally balanced histogram has exactly `2r`
copies of each phase and therefore the same positive coefficient

```text
[z^(pr)] prod_(j=0)^(p-1)(1+zeta_p^j z)^(2r)
 = [z^(pr)](1+z^p)^(2r)
 = binom(2r,r)>0.
```

Thus cancellation inside that histogram is zero, and its mass `A_hist` obeys
`A_hist>=A_split`. Elementary multinomial and central-binomial bounds give

```text
A_hist/A_eff >= A_split/A_eff
 >= p*2^(2r)/((pr+1)^(2(p-1))*(2r+1))
 = exp((log 2)N/p-O_p(log N))
```

for fixed odd `p`, while fixed `r>=2` and odd `p->infinity` gives
`A_hist/M=exp(Omega_r(N log N))` from the same certified subblock.

## Exact finite falsifier

At `p=3,r=5`:

```text
N=30
m=15
M=L=155117520
A_eff=3^28=22876792454961
split subblock count=190893214512
split subblock mass=48105090057024
                    =2*A_eff+2351505147102
complete balanced-histogram count=616779425262
complete balanced-histogram mass=155428415166024
                                =6*A_eff+18167660436258
split source-payment floor kappa>=310122
histogram source-payment floor kappa>=1002006
outside-split signed sum=-25228452719583
other-histogram signed debt=-132551777828583
```

The complete histogram count is the exact 29-term sum over attained-support
phase counts `(a_0,a_1,a_2)` satisfying

```text
a_0+a_1+a_2=15,
0<=a_j<=10,
a_0<=9,
a_1+2a_2=0 mod 3,
```

with summand

```text
15!/(a_0!a_1!a_2!)
*14!/((9-a_0)!(10-a_1)!(10-a_2)!).
```

Exact Fourier inversion at the unique zero target then yields

```text
M+A_hist+A_other=A_eff,
A_other=-132551777828583.
```

## Exact PROVED-declaration table

| Declaration | Exact statement | Authority |
|---|---|---|
| `TRACE_LINEAR_DOMAIN` | `T` has exactly `N` distinct elements | threshold note; exhaustive regression |
| `TRACE_LINEAR_PHASE_CODE` | trace pairing gives all basis phases with `y_0=0`, `y_u=-sum_(i<m)y_i` | threshold note |
| `FIXED_WEIGHT_INJECTIVE_ZERO_TARGET` | `M=L=binom(N,m)` and `Psi^(-1)(0)={S_*}` | threshold note; exhaustive regression |
| `SPLIT_BALANCED_BLOCK_COUNT` | `B_split=H_(p,r)^2/p` | threshold note |
| `BALANCED_HISTOGRAM_COHERENCE` | every globally balanced character has coefficient `binom(2r,r)>0` | threshold note; exact cyclotomic verifier |
| `FIXED_ORDER_COMPENSATED_FLOOR` | displayed fixed-`p` exponential lower bound | threshold note |
| `GROWING_ORDER_RAW_FLOOR` | fixed `r>=2`, odd `p->infinity`: `exp(Omega_r(N log N))` | threshold note |
| `REGRESSION_COMPLETE_HISTOGRAM` | at `p=3,r=2`: 3900 characters, coefficient 6, mass 23400 | exhaustive verifier |
| `FINITE_COMPLETE_HISTOGRAM_COUNT` | at `p=3,r=5`: count `616779425262` | threshold note; verifier; Lean frozen 29-term sum |
| `regression_phase_code_size_exact` | `3^10=59049` | Lean |
| `regression_source_mass_exact` | `binom(12,6)=924` | Lean |
| `regression_split_balanced_block_count_exact` | `2700` | Lean + verifier |
| `regression_cyclotomic_coefficient_exact` | `6` | Lean + verifier |
| `regression_split_balanced_block_mass_exact` | `16200` | Lean + verifier |
| `source_mass_exact` | `binom(30,15)=155117520` | Lean |
| `effective_target_size_exact` | `3^28=22876792454961` | Lean |
| `half_balanced_count_exact` | `756756` | Lean |
| `anchored_complement_balanced_count_exact` | `252252` | Lean |
| `split_balanced_block_count_exact` | `190893214512` | Lean |
| `cyclotomic_coefficient_exact` | `252` | Lean |
| `split_balanced_block_mass_exact` | `48105090057024` | Lean |
| `split_balanced_double_gap_exact` | `A_split=2*A_eff+2351505147102` | Lean |
| `balanced_histogram_count_exact` | `616779425262` | Lean frozen sum + verifier completeness |
| `balanced_histogram_mass_exact` | `155428415166024` | Lean |
| `balanced_histogram_six_gap_exact` | `A_hist=6*A_eff+18167660436258` | Lean |
| `split_balanced_block_exceeds_double_effective_target` | `2*A_eff<A_split` | Lean |
| `balanced_histogram_exceeds_six_effective_targets` | `6*A_eff<A_hist` | Lean |
| `split_source_payment_kappa_floor` | subblock payment implies `310122<=kappa` | Lean |
| `histogram_source_payment_kappa_floor` | histogram payment implies `1002006<=kappa` | Lean |
| `outside_split_subblock_signed_sum_exact` | `A_eff-M-A_split=-25228452719583` | Lean |
| `other_histogram_signed_debt_exact` | `A_eff-M-A_hist=-132551777828583` | Lean |
| `exact_histogram_fourier_balance` | exact complete-histogram balance | Lean |
| `no_nonnegative_histogram_balance` | no natural nonnegative remainder closes the balance | Lean |

Every row is **PROVED** at its displayed scope. The packet is a family-level
route cut, not a deployed-row payment.

## Certificate replay

Certificate:
`experimental/data/certificates/sidon-effective-image-cyclotomic-phase-floor/sidon_effective_image_cyclotomic_phase_floor.json`.

Verifier:
`experimental/scripts/verify_sidon_effective_image_cyclotomic_phase_floor.py`.

The Python-stdlib verifier independently uses exact arithmetic in
`Z[zeta_3]`. It exhausts all `3^10` trace-linear phase words and all
`binom(12,6)` supports at `p=3,r=2`; checks the complete character sum, distinct
domain, singleton fibers, split subblock, complete balanced histogram, and
unique zero target; checks the `p=3,r=5` 29-term formula and both payment floors;
checks a grid of general lower bounds; and rejects eight mutations. No floating
point decides a gate.

```text
python3 experimental/scripts/verify_sidon_effective_image_cyclotomic_phase_floor.py --check
python3 -O experimental/scripts/verify_sidon_effective_image_cyclotomic_phase_floor.py --check
RESULT: PASS (6762 exact checks, 8 rejected mutations, mode=full-enumeration)
```

## Source-label and blob map

| Packet statement | `experimental/grande_finale.tex` label |
|---|---|
| degree-one RS map | `eq:exact-power-sum-map` |
| effective target/Fourier denominator | `eq:effective-fourier-span`, `lem:effective-span-fourier` |
| separately paid nonnegative aggregate | `def:effective-fourier-payment` |
| phase-aware major aggregation | `def:major-arc-aggregate` |
| source/image scales | `eq:image-ambient-scales`, `def:primitive-q` |
| small-characteristic boundary | `rem:small-characteristic-cycles` |
| positive shallow theorem boundary | `thm:unconditional-shallow-mi-ma` |

```text
base fork main: 4e5f0b77c98f075ea7c8822cd4859847a232bc2a
upstream main: a3017697ad1594521d2779fe1d83bccd45d4c06e
predecessor head: 927bd5081a3dc12c51d63ff9081e9bd77d6e3c91
successor branch: gptpro/rs-phase-floor-hunt-pro-audit
```

The Lean module imports only `Std`. Therefore the required imported integrated
API set (`AsymptoticSpine.*`, `M31QRootedShell.*`) is empty.

| Imported integrated API | Fork blob | Upstream blob | Result |
|---|---:|---:|---|
| none (`import Std` only) | -- | -- | **VACUOUSLY BYTE-IDENTICAL** |

| Proof source | Fork blob | Upstream blob | Result |
|---|---|---|---|
| `experimental/grande_finale.tex` | `8a5d9791900ca9eed773feba146b92ad296704ce` | `8a5d9791900ca9eed773feba146b92ad296704ce` | **BYTE-IDENTICAL** |
| `experimental/rs_mca_thresholds.tex` | `01302a797c502a05ed0b11ba949b8756e0aa2b22` | `01302a797c502a05ed0b11ba949b8756e0aa2b22` | **BYTE-IDENTICAL** |

## Lean validation and axiom census

```text
package: experimental/lean/sidon_effective_image
toolchain: Lean 4.31.0
root: SidonEffectiveImage.lean
explicit module: SidonEffectiveImage.CyclotomicPhaseFloor
stdlib only; Mathlib imports 0
repository API imports 0; open-PR imports 0
native_decide 0
sorry 0; admit 0; sorryAx 0; custom axioms 0; unsafe declarations 0
autoImplicit false
lakefile requires 0
lake-manifest: canonical empty package manifest
```

The predecessor draft failed twice before compilation because the pinned
`leanprover/lean-action@v1.5.0` setup rejects a package without
`lake-manifest.json` even when its lakefile has no `require`. The successor adds
the canonical empty manifest. The first successor compile then exposed that
`Nat.choose` and `Nat.factorial` were unavailable from this `Std` import; the
module now restates executable `binomial` and `factorial` definitions locally.

Fork draft PR `#92` validated head
`6280e4693c7c1f21895cd816f60e471267788e0b` in workflow run `29853883779`.
The workflow built both explicit targets

```text
SidonEffectiveImage
SidonEffectiveImage.CyclotomicPhaseFloor
```

and replayed the package default target. All builds succeeded on Lean 4.31.0.

The `#print axioms` output reports:

- every exact equality, count, mass, gap, inequality, and signed-balance theorem
  is axiom-free;
- `split_source_payment_kappa_floor`,
  `histogram_source_payment_kappa_floor`, and
  `no_nonnegative_histogram_balance` depend only on standard `propext` and
  `Quot.sound` through `omega`;
- no theorem depends on `sorryAx`, a custom axiom, or `Classical.choice`.

Green CI certifies compilation only; theorem/source correspondence is the table
above.

## Explicit nonclaims

- No actual post-C1--C8 Mersenne-31 or KoalaBear survivor is constructed.
- No first-match owner complement, profile census, row atom, true numerator,
  slope/ray compiler, line-local uniformity theorem, adjacent-row certificate,
  safe radius, score, or prize claim changes.
- No lower bound for the true MCA or list numerator is proved.
- A target-coupled signed cross-histogram method is not refuted.
- `K`, `F_p`, the effective target, and deployed row fields remain distinct; no
  extension-field payment transfers to a live row.

COUNTEREXAMPLE_NEW_FLOOR
