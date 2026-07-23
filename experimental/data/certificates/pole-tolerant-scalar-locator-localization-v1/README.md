# Pole-tolerant scalar-locator localization certificate

This packet corroborates the two local theorems in
`experimental/notes/m2/pole_tolerant_scalar_locator_localization.md`.

Run from the repository root:

```bash
python3 experimental/scripts/verify_pole_tolerant_scalar_locator_localization.py --check
python3 -O experimental/scripts/verify_pole_tolerant_scalar_locator_localization.py --check
python3 experimental/scripts/verify_pole_tolerant_scalar_locator_localization.py --tamper-selftest
python3 -O experimental/scripts/verify_pole_tolerant_scalar_locator_localization.py --tamper-selftest
```

The checker uses only the Python standard library.  It binds the current
`experimental/grande_finale.tex` scalar-locator definition by Git-blob hash,
replays exact finite-field localization and cancellation fixtures, exhausts a
small `g=m` boundary instance, and rejects changes to the source pin, theorem
scope, nonclaims, and M31 row constants.

The checker does not prove the universal theorem, a CAP25/CA input, an active
first-match adapter, or a deployed payment.  Those nonclaims are sealed in
`certificate.json`.
