M31 T16 mixing floor
STATUS: COUNTEREXAMPLE / COUNTEREXAMPLE_NEW_FLOOR / SUPPORT-LEVEL ONLY
- Claim: On the pinned c=2048, (u,v)=(0,1) quotient profile, one 479-subset anchor has 1,233 distinct depth-32-prefix neighbors at deficiency 192: 1,225 triple-T64 swaps and 8 non-T64 T16-mixed neighbors.
- Status: A1 full-T64 classification is false and every coefficient-four uniform intercept must satisfy b>=1,233. Coefficient four remains arithmetically viable exactly for 1,233<=b<=5,191; the M31 LIST row remains open.
- Verifier: `verify_m31_quotient_t16_mixing_floor.py --check` and `--tamper-selftest`; stdlib-only `M31QuotientT16MixingFloor.Witness` states the 1,233-neighbor census, T16/T32 identities, shell floor zero, and compiler arithmetic.
- Consumers: The pinned M31 quotient-prefix rooted-shell calibration at deficiency 192, including the uniform-intercept window and the classification assumptions used to seek a band cap.
- Risk-limits: Support-level pinned-profile result only. No first-match survival, received word, codeword, explanation, ray, slope, uniform band cap, B1 non-class e=64 witness, B2 degree 5,192 witness, or row-global U_Q is proved.
