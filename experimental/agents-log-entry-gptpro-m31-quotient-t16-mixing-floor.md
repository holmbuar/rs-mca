### 2026-07-22 - M31 quotient T16 mixing floor

- **Agent/model:** GPT-5.6 Pro.
- **Files added or changed:** `experimental/notes/thresholds/m31_quotient_t16_mixing_floor.md`; `experimental/scripts/verify_m31_quotient_t16_mixing_floor.py`; `experimental/data/certificates/m31-quotient-t16-mixing-floor/m31_quotient_t16_mixing_floor.json`; `experimental/lean/m31_quotient_t16_mixing_floor/M31QuotientT16MixingFloor.lean`; `experimental/lean/m31_quotient_t16_mixing_floor/M31QuotientT16MixingFloor/Witness.lean`.
- **Status:** COUNTEREXAMPLE / COUNTEREXAMPLE_NEW_FLOOR / SUPPORT-LEVEL ONLY; UNPINNED LOCAL DRAFT.
- **What is being added:** On the pinned M31 `(u,v)=(0,1)` quotient profile, one 479-subset anchor has 1,233 certified same-depth-32-prefix neighbors at deficiency 192: 1,225 full-`T_64` triple swaps and eight non-class `T_16` mixings. This falsifies A1 and raises the coefficient-four intercept floor to 1,233.
- **How it is useful:** It narrows the arithmetically viable uniform-intercept window to `1233 <= b <= 5191` while leaving coefficient four open. It also supplies an independent non-class `T_32` pair and exact support/shell/compiler replay data.
- **What to do next:** Pick up on intended branch `gptpro/m31-quotient-t16-mixing-floor` from parent `5b8bbc2083583460dd3d9b23b8d8fca6701f7ae6`, apply repository source-blob pins, replay the locally hashed artifacts end-to-end, and validate the stdlib-only Lean package through the fork draft PR.
