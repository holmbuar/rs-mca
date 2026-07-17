# Rank-16 fixed-27 residual specialization curve certificate

Claim: Under the integrated rank-two syzygetic hypotheses, the cubic and
quartic residuals are nonzero scalar normalizations of one label-degree-two or
label-degree-three specialization curve; a generator with a quadratic
whole-`B`-block factor supports at most two valid labels.
Status: PROVED local theorem with zero finite-ledger, recurrence, Grand List,
Grand MCA, or score payment.
Verifier: `verify_rank16_fixed27_residual_specialization_curve.py` is a
standard-library-only replay of the deployed constants, normalization and
divided-difference identities on finite-field fixtures, incidence floors, and
the quotient-ring Vandermonde terminal. The complete proof is in
`experimental/notes/l2/rank16_fixed27_residual_specialization_curve.md`.
Consumers: The rank-two fixed-27 cap-six problem after the integrated
quotient-line and block-wedge theorems.
Risk-limits: The packet does not reclaim the integrated dichotomy,
`e in {3,4}`, or the inherited quartic dimension-four theorem. It does not
exclude `kappa_B(g)<=1`, prove a uniform cap, aggregate source cells, close a
parent, or move the `0/2` score.

## Replay

From the repository root:

```text
python3 experimental/data/certificates/rank16-fixed27-residual-specialization-curve/verify_rank16_fixed27_residual_specialization_curve.py
python3 -O experimental/data/certificates/rank16-fixed27-residual-specialization-curve/verify_rank16_fixed27_residual_specialization_curve.py
python3 experimental/data/certificates/rank16-fixed27-residual-specialization-curve/verify_rank16_fixed27_residual_specialization_curve.py --tamper-selftest
```

The first two commands must be byte-identical and equal
`verify_rank16_fixed27_residual_specialization_curve.expected.txt`. The third
must print `TAMPER_SELFTEST: PASS`.

Verify the frozen files from this directory with:

```text
shasum -a 256 -c SHA256SUMS.txt
```

## What is and is not machine checked

The verifier checks every printed deployed integer, exact union floor,
finite-field scalar-normalization identity, all-nonzero divided-difference
dependence, and the Vandermonde argument over a quotient ring. It deliberately
rejects a manifest that replaces scalar normalization by literal equality.

The general polynomial argument is proved in the theorem note; the finite
fixtures are regression tests, not a finite search replacing that proof.
