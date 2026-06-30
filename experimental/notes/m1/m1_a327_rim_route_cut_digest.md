# M1 a=327 RIM route-cut digest

**Status:** AUDIT / COMPUTATIONAL_CERTIFICATE / ROUTE_CUT / PARTIAL /
EXPERIMENTAL.

**Source:** distilled from Scott Hughes's draft PR #145, "M1: add a=327 RIM
obstruction and pivot-certificate audit".

**Date:** 2026-06-30.

This digest keeps the useful audit facts from the large draft packet without
importing the full scan tree.  It is an interleaved-list route-cut audit for

```text
C = RS[F_17^32,H,256],    |H| = 512,
agreement target a = 327.
```

It does not improve the current board-facing interleaved-list record
`Lambda_mu(C,326) >= 7`.  It is not an MCA bad-slope row, not an `a=327`
witness, and not a global upper bound at `a=327`.

## Preserved audit facts

The tested nonquotient support design has

```text
support_count = 7,
support_size = 327,
max_pair_intersection = 254.
```

The associated reduced pairwise-overlap rank gate is full rank over
`GF(17^32)`:

```text
matrix_shape = 2882 x 382,
rank         = 382,
nullity      = 0.
```

Thus that tested support/RIM model cannot produce the desired non-diagonal
interpolation solution.

The pivot replay packet also reported full coverage of the previously tested
full-rank reduced matrices in this local lane:

```text
source_matrices = 34,
pivot_certified = 34.
```

The classes are:

```text
support_overlap_rref_pivot   = 20,
generic_pairwise_rref_pivot  = 6,
quotient_residual_rref_pivot = 8.
```

The rank-free rule audit is more limited:

```text
support_overlap:    20 matrices, 160 attempts, 0 successes,
generic_pairwise:    6 matrices,  48 attempts, 0 successes,
quotient_residual:   8 matrices,  88 attempts, 2 RREF-mimic successes.
```

No deterministic rank-free pivot theorem is banked by this digest.

## Why this is useful

For the v9 Hankel-certificate program, this packet is useful as a negative
local audit: a tested `a=327` interleaved-list RIM route is blocked by
full-rank reduced matrices, and the attempted rank-free metadata rules are not
yet enough to replace RREF-derived certificates.

This helps prioritize the next proof step: either turn the recurring RREF
pivots into a deterministic combinatorial pivot schedule, or abandon this
support/RIM lane as a route to an `a=327` certificate.

## Non-claims

This digest intentionally does not claim:

```text
MCA N_bad,
protocol soundness,
ordinary list decoding beyond the stated interleaved-list predicate,
a=327 interleaved-list certificate,
global Lambda_mu(C,327) <= 6,
global RIM full-rank theorem,
deterministic combinatorial pivot schedule,
exact Lambda_mu,
exact delta*_C,
improvement over PR #133.
```

## Verification

The digest verifier checks the self-contained JSON constants and non-claims:

```sh
python3 experimental/scripts/verify_m1_a327_rim_route_cut_digest.py
```
