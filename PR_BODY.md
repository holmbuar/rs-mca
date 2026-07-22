M31 post-Johnson conversion contract
STATUS: PROVED_EXACT_CONVERSION_CONTRACT / CONDITIONAL_CS_BRIDGE / BCHKS_ROUTE_CUT / GCXK_SOURCE_SIGN_GUARD / AUDIT
- Claim: At agreement 1116023, CS25 converts CA numerator at most 16777214 for C=RS(1048576) into list size at most 16777215 for C⁺=RS(1048577), hence for C by inclusion.
- Status: The CS bridge is conditional. BCHKS25 is exactly vacuous for budget 16777215: its integer conclusion is at most q−1=21267647892944572736998860269687930880.
- Verifier: The exact checker supports `--check` and `--tamper-selftest`; stdlib Lean certifies the deployed arithmetic, Johnson boundary, conversion windows, and integer margins.
- Consumers: Lane M1 ordinary-list stress row, the four-row exact-completion compiler, and CA/MCA theorems evaluated at errors 981129 over F_((2^31−1)^4).
- Risk-limits: The adjacent MCA row is one error and one numerator too weak. No direct list upper theorem or counterexample is proved. GCXK remains source-sign guarded.
