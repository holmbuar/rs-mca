# M31 quotient-prefix-flatness witness: source correspondence

## Mathematical source

The proof source is
`experimental/notes/thresholds/m31_quotient_prefix_flatness_t64_witness.md`.

The exact expanded supports and target are frozen in
`experimental/data/certificates/m31-quotient-prefix-flatness-t64-witness/m31_quotient_prefix_flatness_t64_witness.json`.

## Lean declarations

| Source claim | Lean declaration |
|---|---|
| norm-one generator and exact order data | `generator_norm_one`, `generator_half_order`, `generator_full_order` |
| 1,024 distinct quotient labels and 1,022-point puncture | `quotient_domain_exact` |
| quotient labels are the deployed `T_1024` roots after rescaling | `quotient_labels_are_T1024_roots` |
| pinned active eight roots puncture `q_1,q_3` | `active_profile_punctures_exact` |
| sixteen exact 64-point quotient fibers and printed values | `t64_fibers_exact` |
| 415-point common core | `common_core_exact` |
| seven distinct valid 479-subsets of `Q'` | `supports_exact` |
| printed depth-32 target for all seven supports | `all_prefixes_match_eta` |
| stronger first-63 coefficient equality | `first_sixty_three_coefficients_match` |
| six distinct deficiency-64 neighbors | `six_deficiency_64_neighbors` |
| exact `H_64` integer | `H64_exact` |
| `4 H_64 < p^32` and floor zero | `four_H64_lt_Q32`, `shell_floor_zero` |
| strict failure of `(Q-3+4)` using the six listed neighbors | `Q_minus_3_plus_4_violated` |
| conditional `(6+4)` budget arithmetic only | `conditional_b6_c4_arithmetic` |

## Proof boundary

The declarations certify an explicit support-level quotient-prefix witness.
They do not certify received-word realization, first-match survival, a
codeword/ray/slope projection, a row-global `U_Q`, or a replacement `(6+4)`
hypothesis. `native_decide` is used only for finite closed computations; the
module declares no custom axioms and contains no `sorry` or `admit`.
