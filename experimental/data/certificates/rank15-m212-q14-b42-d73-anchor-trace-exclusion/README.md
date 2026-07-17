# Rank-15 `D=73` anchor-trace certificate

Claim: The exact affine `D=73` object left open by the integrated
`D=69..72` arrangement theorem is impossible because eight 6-secants around
one 10-point anchor force 29 repeated line pairs but only 28 are available.

Status: `PROVED / CONDITIONAL ARRANGEMENT INTERFACE`.

Verifier:

```text
python3 experimental/scripts/verify_rank15_m212_q14_b42_d73_anchor_trace_exclusion.py
python3 -O experimental/scripts/verify_rank15_m212_q14_b42_d73_anchor_trace_exclusion.py
python3 experimental/scripts/verify_rank15_m212_q14_b42_d73_anchor_trace_exclusion.py --tamper-selftest
```

The normal and optimized outputs must byte-match
`verify_rank15_m212_q14_b42_d73_anchor_trace_exclusion.expected.txt`.  The
script pins the integrated source transcript that labels the exact profile
`OPEN_D73`.  It checks the ledger arithmetic; the complete geometric proof is
in `experimental/notes/l2/rank15_m212_q14_b42_d73_anchor_trace_exclusion.md`.

Consumers: Conditional rank-15 arrangement geometry only.

Risk-limits: Zero source-child, recurrence-parent, or official-score payment.
No `D>=74` classification or exclusion is included.
