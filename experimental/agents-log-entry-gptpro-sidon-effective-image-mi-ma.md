### 2026-07-21 - Effective-image MI+MA normalization floor

- **Agent/model:** GPT-5.6 Pro.
- **Files added or changed:** `experimental/notes/audits/sidon_effective_image_mi_ma_normalization_floor.md`, the new stdlib-only package `experimental/lean/sidon_effective_image/`, and this entry suggestion.
- **Status:** PROVED / COUNTEREXAMPLE_NEW_FLOOR / CONDITIONAL_ON_NAMED_INPUT.
- **What is being added:** The packet proves the exact image-compensated Fourier loss `(L/A_eff)(1+C_min+C_maj)`, proves the universal unweighted floor `1+C_min+C_maj >= A_eff/L`, and gives a deep fixed-density multiplicative-coset family where image-normalized Q has `p^2=exp(o(N))` loss but unweighted EFP/MI+MA needs `exp(Omega(N log N))`.  Lean checks the `p=11`, `M=252`, `L=251`, max-fiber-two, full-span regression.
- **How it is useful:** It rules out treating unweighted EFP as a universal image-scale C9 payment and isolates `IMAGE_COMPENSATED_EFFECTIVE_MI_MA_ON_ACTUAL_PRIMITIVE_LEAVES` as the exact remaining analytic input, with first-match survival and ray compilation still separate.
- **What to do next:** Prove the image-compensated minor and major aggregates, or a direct image-scale Q theorem, on one genuine post-C1--C8 primitive leaf; do not substitute `q_gen^R` for the realized image or identify `q_gen`, `q_line`, `q_chal`, and `q_list`.
