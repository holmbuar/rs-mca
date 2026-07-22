# C8 high-kappa owner compiler: source/Lean correspondence

## Scope

This audit maps
`AsymptoticSpine/C8HighKappaOwner.lean` to the current C8 proof boundary. The
module is a stdlib-only finite compiler. It does not formalize finite fields,
Reed--Solomon polynomial division, an actual semantic owner, or the deep
analytic payment.

## Source authorities

| Source | Consumed statement |
| --- | --- |
| `experimental/notes/thresholds/common_core_cover_obstruction.md`, Theorem 2.1(2), equations (2.3)--(2.6) | Fixed-core shortening is a slope-preserving witness bijection; after shortening, `k'=k-|K|` and the residual kernel is computed in the shortened row. |
| `experimental/notes/audits/balanced_core_factored_rank_audit.md` | Retaining the original `k` after common-core shortening is false; the exact parameter is the shortened dimension. |
| `experimental/notes/thresholds/a4_covers_high_kappa.md` | Shallow-prefix closure is independent of the residual kernel label and transfers to residual subfamilies by inclusion. |
| `AsymptoticSpine/EffectiveClosure.lean` | Duplicate-free `(SE2)` support-to-slope injection, `DirectRC`, and the prefix-residual closure theorem. |
| `AsymptoticSpine/HighKappaCoverage.lean` | Kernel-labelled shallow-prefix direct `(RC)` and `(A6)` routing. |

The source-side construction of the shortening certificate remains an explicit
input. The Lean module proves what follows once that certificate is supplied.

## Declaration map

| Lean declaration | Exact proved statement | Proof status / source boundary |
| --- | --- | --- |
| `SlopePreservingShortening` | Typed original and shortened `(SE2)` certificates with equal slope lists, exact support-list image, and commuting support-for-slope map. | Interface matching Theorem 2.1(2); construction is conditional input. |
| `SlopePreservingShortening.slopes_length_eq` | Original and shortened distinct-slope list lengths are equal. | PROVED from `slopes_eq`. |
| `SlopePreservingShortening.supports_length_eq` | Fixed-core shortening preserves the displayed support-projection cardinality. | PROVED from `supports_eq` and `List.length_map`. |
| `SlopePreservingShortening.supportBudget_addBack` | A shortened support budget pays the original distinct-slope numerator with factor one. | PROVED from shortened `(SE2)` and exact slope equality. |
| `SlopePreservingShortening.directRC_addBack` | `DirectRC` on the shortened slope list is `DirectRC` on the original list. | PROVED; zero-loss add-back. |
| `SlopePreservingShortening.kernelIndependentDirectRC_addBack` | Kernel-labelled shallow direct `(RC)` transfers unchanged. | PROVED; zero-loss add-back. |
| `SlopePreservingShortening.shallowClosure_addBack` | The existing shallow-prefix closure on the shortened chart pays the original slope cell. | PROVED from `HighKappaCoverage` plus exact slope equality. |
| `SlopePreservingShortening.shallowClosure_to_A6_addBack` | The transferred direct `(RC)` supplies the direct branch of `(A6)`. | PROVED. |
| `FactoredKernelLedger` | Keeps original dimension, factored core, shortened dimension, residual core, and kernel in one typed ledger. | Interface for the factor-aware MDS rank law. |
| `FactoredKernelLedger.kernel_le_shortened` | `kappa <= k'`. | PROVED from `kappa=k'-c_res`. |
| `FactoredKernelLedger.kernel_eq_shortened_of_maximal` | If the residual common core is empty, `kappa=k'`. | PROVED. |
| `FactoredKernelLedger.kernel_eq_sub_core_of_maximal` | Under maximal-core removal, `kappa=k-|K|`. | PROVED; exact correction to the stale raw-`k` reading. |
| `FactoredKernelLedger.highKernel_iff_smallCore` | For `cutoff<=k`, `cutoff<kappa` iff `|K|<k-cutoff`, under maximal-core removal. | PROVED finite natural-number arithmetic. |
| `C8OwnerOrPayment` | Literal terminal `earlierOwner OR slopeCount<=budget`. | Definition only. |
| `ownerOrPayment_of_kernelDichotomy` | High-kappa earlier owner plus small-kappa shortened support payment closes the original cell. | PROVED finite compiler; both mathematical branch inputs are explicit. |
| `ownerOrPayment_of_maximalCoreThreshold` | Same compiler with the high-kappa owner premise restated as a small maximal-core premise. | PROVED from the exact equivalence. |
| `c8Toy_smallKernel_payment` | Exact finite small-kernel branch fixture. | PROVED regression only. |
| `c8Toy_highKernel_owner` | Exact finite high-kernel owner fixture. | PROVED regression only. |
| `c8Toy_highKernel_iff_smallCore` | Exact finite arithmetic fixture for the equivalence. | PROVED regression only. |

## Proof census

```text
sorry: 0
custom axioms: 0
unsafe declarations: 0
```

The module prints the axiom report for every public theorem listed above.
Authoritative build status is recorded by the fork draft PR. A green build
certifies compilation of the finite statements only; it does not certify the
external RS shortening construction or any conditional semantic/analytic
input.

## Explicit conditional inputs

The following are not proved by this packet:

1. an actual received line and first-match C8 cell;
2. a fixed common core and the polynomial witness bijection of Theorem 2.1(2);
3. maximality of the factored core when the high-kappa/small-core equivalence is
   used;
4. an earlier semantic owner for every high-kappa residual;
5. a shortened support payment for every small-kappa residual outside the
   existing shallow-prefix regime;
6. deep-prefix `(MI)`/`(MA)`, Sidon, chart exhaustion, residual-to-full add-back
   beyond the exact fixed-core equality, or `UNIF`;
7. any finite adjacent-row inequality or ledger movement.

## Statement audit

The module intentionally does not claim that a raw prefix family is an actual
first-match residual. `SlopePreservingShortening` begins only after the semantic
cell and its duplicate-free slope/support certificates have been supplied. It
also does not identify `kernelDim` with the original dimension. The equality
`kappa=k-|K|` requires the explicit `MaximalCoreRemoved` hypothesis.

No field or denominator is present in the finite compiler, so no base,
extension, line, profile, list, or challenge denominator can be merged by the
formalization. Concrete consumers must print those ledgers separately.
