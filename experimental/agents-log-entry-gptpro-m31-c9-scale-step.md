## 2026-07-21 — M31 C9 sixteen-root scale step

- **Lane / activity:** `gptpro/m31-c9-scale-step`; falsify loss-one persistence for the exact-residual C9 prefix fiber at the next active-domain scale.
- **Result:** `COUNTEREXAMPLE_NEW_FLOOR`. On sixteen actual `T_(2^21)` roots arranged as four complete `T_4` blocks, the complete weight-eight slice has `12870` supports. Exact C1 antipodal-quotient deletion removes `70`; the first residual key has fiber `[383,61808]`, so loss one fails. Exhaustive replay gives residual histogram `{1:12032,2:384}` and exact maximum `2`.
- **Named terminal:** `M31_C9_SCALE_STEP_T4_BLOCK_SWAP_DOUBLING` (acceptance criterion 4).
- **Validation:** stdlib Lean module `SidonEffectiveImage.M31C9ScaleStep`, zero `sorry`/custom axioms/native decision; certificate and independent stdlib verifier included. Fork draft-PR CI is the compiler authority.
- **What to do next:** route complete-`T_4` block swaps earlier, or accept/pay the exact factor-two scale loss before testing the next domain scale.
