### 2026-07-21 - M31 C9 sixteen-root residual fiber doubling

- **Agent/model:** GPT-5.6 Pro.
- **Files added or changed:** `experimental/lean/sidon_effective_image/`,
  `experimental/notes/thresholds/m31_c9_scale16_residual_max_fiber.md`,
  `experimental/notes/audits/m31_c9_scale16_residual_max_fiber_audit.md`,
  `experimental/data/certificates/m31-c9-scale16-residual-max-fiber/`,
  `experimental/scripts/verify_m31_c9_scale16_residual_max_fiber.py`, and this
  entry suggestion.
- **Status:** PROVED FINITE / COUNTEREXAMPLE / AUDIT.
- **What is being added:** The exact #1027 scale successor on sixteen derived
  `T_(2^21)` roots.  After deleting all 70 C1 antipodal-quotient supports from
  the complete weight-eight slice, the 12,800-support residual has 12,416 keys,
  maximum fiber two, and exactly 384 doubled keys.  Every doubled key is a
  complete-`T_4` block swap; the minimal image-normalized residual loss is
  exactly two.
- **How it is useful:** It gives an exact bound on the actual scaled
  C1-complement and cuts off residual injectivity as a scale-stable C9/Q route.
  The integral natural-scale field remains `2 <= 1*2`, but real-average loss
  one does not.
- **What to do next:** Review the block-swap terminal against any proposed
  row-global C1--C8 owner map before using this local profile in a deployed
  `U_Q` or slope ledger.
