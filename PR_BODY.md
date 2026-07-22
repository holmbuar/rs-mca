Raise M31 quotient shell floor
STATUS: COUNTEREXAMPLE_NEW_FLOOR / ROUTE_CUT / OPEN_GAP
- Claim: A 3,432-support `T_64` family gives `d_64>=49`, `d_128>=441`, and `d_192>=1,225`; an independent `T_16` exchange gives `d_96>=1` and 47 matching nonleading locator coefficients.
- Status: Coefficient four remains arithmetically viable only in the narrowed necessary window `1,225<=b<=5,191`; no uniform cap, non-full `e=64` mixing, `5,192`-neighbor route kill, first-match payment, or row closure is proved.
- Verifier: `verify_m31_quotient_band_swap_census_t16_mixing.py --check` and `--tamper-selftest`; stdlib Lean package `m31_quotient_band_mixing` certifies the finite witnesses and exact arithmetic.
- Consumers: Pinned Mersenne-31 LIST stress-row quotient-shell calibration for the `(u,v)=(0,1)`, `c=2048`, depth-32 fixed-template profile.
- Risk-limits: Support-level only; the `e=96` witness kills full-class classification and zero off-lattice rigidity, not a capped off-lattice theorem. Shells `e>=214`, received-word realization, projection, add-back, and all other profiles remain open.
