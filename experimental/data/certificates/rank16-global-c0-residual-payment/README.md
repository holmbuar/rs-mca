# Rank-16 global `c=0` residual payment certificate

This directory contains deterministic ledgers and expected output for
`experimental/scripts/verify_rank16_global_c0_residual_payment.py`.

Run from the repository root:

```bash
python3 experimental/scripts/verify_rank16_global_c0_residual_payment.py
python3 -O experimental/scripts/verify_rank16_global_c0_residual_payment.py
python3 experimental/scripts/verify_rank16_global_c0_residual_payment.py \
  --tamper-selftest
python3 experimental/scripts/verify_rank16_global_c0_residual_payment.py \
  --write-profile-ledger /tmp/profile.csv \
  --write-johnson-ledger /tmp/johnson.csv
```

The profile ledger records all 1,792 dyadic profiles, the integrated `Q110`
status, deterministic `Q41` and `X175` ranks, and selected-owner flags. The
Johnson ledger records all 1,696 positive-denominator lower cells, their
exact local constants and caps, and the `J48` prefix.

The verifier also regenerates the integrated `#838` 1,682-row residual CSV
and compares it byte-for-byte with the repository certificate. `SHA256SUMS`
binds the new script, note, expected output, and generated ledgers.
