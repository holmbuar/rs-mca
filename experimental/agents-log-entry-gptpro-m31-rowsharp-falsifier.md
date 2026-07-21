### 2026-07-21 - M31 fixed-remainder dyadic fold route cut

- **Agent/model:** GPT-5.6 Pro.
- **Files added or changed:** `experimental/notes/thresholds/m31_fixed_remainder_dyadic_route_cut.md`; `experimental/notes/audits/m31_fixed_remainder_dyadic_route_cut_audit.md`; `experimental/data/certificates/m31-fixed-remainder-dyadic-route-cut/m31_fixed_remainder_dyadic_route_cut.json`; `experimental/scripts/verify_m31_fixed_remainder_dyadic_route_cut.py`; new stdlib-only module `experimental/lean/sidon_effective_image/SidonEffectiveImage/M31DyadicBlockRouteCut.lean`; package root/metadata; this side entry.
- **Status:** PROVED / NAMED_ROUTE_CUT / ROW_OPEN.
- **What is being added:** Exhausts all 21 fixed-remainder dyadic Chebyshev complete-fiber scales on the deployed M31 list row. Scales `2^1` through `2^17`, including antipodal and `T_4` blocks, are exact C1 quotient/remainder profiles; the four larger scales have exact fixed-remainder caps `35,3,1,1`. A global scalar-domain automorphism is also forced to `+-1`, so its only nontrivial orbit family is the antipodal C1 case.
- **How it is useful:** Removes `M31_FIXED_REMAINDER_DYADIC_FOLD` from the post-C1 falsifier search. It records no ledger payment and no criterion-4 witness.
- **What to do next:** Attack `M31_VARIABLE_REMAINDER_ORIENTATION_RESIDUAL`: varying remainders, antipodal transversals, isolated local cosets, or a direct received-word construction. Do not reopen fixed-remainder dyadic block combinations.
