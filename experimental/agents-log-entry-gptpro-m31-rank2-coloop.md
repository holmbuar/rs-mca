### 2026-07-21 - M31 padded rank-two coloop elimination

- **Agent/model:** GPT-5.6 Pro.
- **Files added or changed:** `experimental/notes/thresholds/m31_rank2_coloop_elimination.md`; `experimental/notes/audits/m31_rank2_coloop_audit.md`; `experimental/lean/sidon_effective_image/`; `experimental/data/certificates/m31-rank2-coloop-elimination/`; `experimental/scripts/verify_m31_rank2_coloop_elimination.py`; this entry side-file.
- **Status:** PROVED / AUDIT / ROUTE CUT.
- **What is being added:** The padded locator row gives a full-support dependence among the 46 columns of every intrinsic padded three-row syzygy frame, with nonzero coefficient at the distinguished extra column.  Therefore that column is never a coloop and `UNPAID_RANK2_COLOOP` is empty on every marked rank-46 key.
- **How it is useful:** It kills one exact Mersenne-31 list terminal (acceptance criterion 3) without touching common-core add-back and without contradicting the `F_11` direct-transport counterpacket.
- **What to do next:** Audit the green fork-CI axiom output, then address the separately owned common-core add-back, row-sharp Q, and list-interior terminals; no adjacent-row closure follows from this packet alone.
