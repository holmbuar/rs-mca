### 2026-07-21 - M31 deployed C1--C8 owner coverage and all-key C9 census

- **Agent/model:** GPT-5.6 Pro.
- **Files added or changed:** `experimental/lean/sidon_effective_image/`;
  `experimental/notes/thresholds/m31_c9_owner_coverage.md`;
  `experimental/notes/audits/m31_c9_owner_coverage_audit.md`;
  `experimental/data/certificates/m31-c9-owner-coverage/m31_c9_owner_coverage.json`;
  `experimental/scripts/verify_m31_c9_owner_coverage.py`;
  `experimental/agents-log-entry-gptpro-m31-c9-owner-coverage.md`.
- **Status:** PROVED / FORMALIZATION / AUDIT.
- **What is being added:** An executable first-match C1--C8 classifier on all
  seventy weight-four supports of the eight-root deployed M31 profile.  C1 owns
  six supports, all later first-match cells are empty, and every one of the
  sixty-four residual keys has an exact singleton full-prefix fiber; the
  stdlib-only Lean module and independent JSON replay certify the exhaustive
  result.
- **How it is useful:** This satisfies acceptance criterion 2 for
  `M31_C9_GLOBAL_OWNER_COMPLEMENT_AND_KEY_COVERAGE` and removes upstream
  #1027's one-key scope restriction on the exact local profile, without
  claiming profile multiplicity, SE2, UNIF, or an adjacent row.
- **What to do next:** Use the complete owner/key table only as the finite
  profile-local input; the fixed-outside profile census and genuine
  received-line support-to-slope projection remain separate obligations.
