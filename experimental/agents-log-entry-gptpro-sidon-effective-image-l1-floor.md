### 2026-07-21 - Effective-image MI+MA absolute-dual-mass floor

- **Agent/model:** GPT-5.6 Pro.
- **Files added or changed:** `experimental/notes/thresholds/sidon_effective_image_mi_ma_l1_floor.md`; new stdlib-only package `experimental/lean/sidon_effective_image/`; `experimental/agents-log-entry-gptpro-sidon-effective-image-l1-floor.md`; `experimental/agents-log.md`.
- **Status:** PROVED / COUNTEREXAMPLE_NEW_FLOOR / CONDITIONAL_ON_NAMED_INPUT.
- **What is being added:** The binary middle-slice incidence map has exact image-normalized Q and zero Sidon-heavy moment, with only polynomial image/ambient loss, but its absolute effective-dual Fourier mass forces `kappa >= 1 + binom(2r,r)/2`.  The `N=8` Lean regression checks `M=L=70`, 35 middle coefficients of magnitude 6, all 128 effective character classes, full nontrivial mass 490, singleton fibers, and exact multiplier `kappa=8`.
- **How it is useful:** This identifies `ABSOLUTE_EFFECTIVE_DUAL_L1_FLOOR`: effective-image normalization does not make absolute `(MI)+(MA)` equivalent to the v3 Sidon moment payment.  Hard input 3 is narrowed to the named residual `RS_PHASE_STRUCTURED_SIDON_PAYMENT` on actual post-C1--C8 RS leaves.
- **What to do next:** Prove direct image-normalized `def:sidon-paid-cell` or a cancellation-sensitive phase-structured replacement on genuine weighted Vandermonde/rational first-match residuals; do not infer that payment from normalization alone.
