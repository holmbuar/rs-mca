# Sidon effective-image finite regression: source correspondence

## Scope

This package is the finite checker for Section 6 of
`experimental/notes/audits/sidon_effective_image_mi_ma_normalization_floor.md`.
It uses only Lean/Std and natural-number arithmetic modulo `11`.

It does not formalize Parseval, Cauchy--Schwarz, the asymptotic prime family,
semantic C1--C8 survival, residual add-back, or the completed-ray compiler.
Those claims remain source-level mathematics with the status printed in the
note.

## Theorem map

| Lean theorem | Source-level meaning | Status |
|---|---|---|
| `support_count` | `M=binom(10,5)=252` | finite regression |
| `support_shapes` | complete generated fixed-weight slice consists of duplicate-free five-subsets | finite regression |
| `realized_image_count` | realized power-sum image has `L=251` targets | finite regression |
| `max_fiber_eq_two` | exact full-slice maximum fiber is two | finite regression |
| `unique_double_target` | zero is the only doubled syndrome | finite regression |
| `displayed_collision` | the two printed supports form that doubled zero fiber | finite regression |
| `image_normalized_q_loss_below_two` | cleared image-normalized loss `maxFiber*L/M` is below two | finite regression |
| `two_coefficient_census_bound` | toy instance of the `p^2` locator-coefficient census | finite regression |
| `basis_values` | three moment-column differences are the printed vectors | finite regression |
| `effective_span_is_full` | an explicit inverse represents every vector of `F_11^3` | finite regression |
| `effective_ambient_count` | `A_eff=11^3=1331` | finite regression |
| `effective_span_over_image_gt_five` | exact sparse-image inequality `A_eff>5L` | finite regression |

## Build contract

The package is an independent Lake package rooted at
`experimental/lean/sidon_effective_image/`.  The fork draft-PR Lean workflow is
the authoritative build.  No local Lean build is claimed.

## Sorry and axiom census

```text
sorry declarations: 0
axiom declarations: 0
Mathlib imports: 0
external packages: 0
```

The file imports only `Std.Tactic.NativeDecide`.  The finite theorems are closed
by `native_decide`; compilation proves those decidable propositions, not the
source-level asymptotic theorem.
