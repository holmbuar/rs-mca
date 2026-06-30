# M1 packet-sift popularity digest

**Status:** PROVED-LOCAL / CONDITIONAL / AUDIT.

**Source:** distilled from AllenGrahamHart's PR #157, "M1: packet-sift
popularity gate package".

**Date:** 2026-06-30.

This digest keeps the reusable core of the packet-sift package without
importing the full broad PR tree.  It is an M1 proof-program note, not a full
M1 theorem, not a finite-row threshold, and not a leaderboard result.

## Where it fits

Use this only after quotient-periodic, tangent/common-code-line,
fixed-root/root-slice, endpoint-star, singular chart, and denominator
exceptions have been separated.  The remaining branch is a sparse packet
family whose support is claimed to be too small.  The packet-sift argument
turns that claim into a concrete high-overlap obligation, and the
popularity-gate argument turns bounded algebraic gates into a support floor.

In the v9 Hankel atlas language, this is a candidate tool for the singular
residual buckets.  It supplies local accounting; it does not supply the missing
model-entry theorem.

## Packet overlap burden

Let `P_1,...,P_K` be packets of size `s`, let

```text
B = |P_1 union ... union P_K|,
I(omega) = #{i : omega in P_i}.
```

Then

```text
sum_omega I(omega) = K s,
sum_omega I(omega)^2 = K s + 2 sum_{i<j} |P_i cap P_j|.
```

Cauchy's inequality gives, for any support budget `R >= B`,

```text
sum_{i<j} |P_i cap P_j| >= K s (K s - R)/(2R).     (PO)
```

Thus if every packet pair has overlap at most `Lambda`, then

```text
B >= ceil( K s^2 / (s + (K-1)Lambda) ).            (PF)
```

This is the local reason a small residual support forces large pairwise
packet overlap.

## Endpoint-star sift

Assume each packet label has a two-point endpoint support, at most `h` labels
lie over any fixed endpoint support, and at most `D` endpoint supports contain
any fixed endpoint.  Endpoint-sharing label pairs contribute at most

```text
K h (D-1) s
```

overlap mass.  After paying this endpoint channel, the overlap forced onto
endpoint-disjoint pairs is at least

```text
Omega_disj =
  K s (K s - R)/(2R) - K h (D-1)s.                 (ES)
```

If every endpoint-disjoint packet pair has overlap at most `Lambda`, then

```text
B >= ceil(
  K^2 s^2 /
  (K s + 2K h(D-1)s + K(K-1)Lambda)
).                                                 (EF)
```

So the next target is not arbitrary overlap.  It is high overlap between
endpoint-disjoint packet supports, unless the family is already in a charged
near-star or endpoint-template branch.

## Popularity divisor gate

Fix a center packet and a residue point `x`.  Suppose endpoint-disjoint
high-overlap leaves containing `x` have a parameter `theta` with fiber
multiplicity at most `mu`, and suppose all relevant parameters lie in an
exceptional set of size at most `E` plus the zeros of nonzero gates of degrees
`d_1,...,d_r`.  Then

```text
pop_x <= mu (E + d_1 + ... + d_r).                 (DG)
```

The projective version is identical with nonzero homogeneous binary forms on
`P^1`.

This is only useful once the actual Hankel/Kummer chart produces nonzero
bounded-degree gates.  If a cleared gate vanishes identically, that branch is
not closed; it becomes a named residual obstruction.

## Equal-line local cap

In the equal-line split-fiber chart isolated in PR #157, the local ledger has
six exceptional projective fibers and a nonzero quadratic gate.  Therefore

```text
U_eq(mu) = 8 mu.
```

In the injective finite-slope `z` branch, the map to the projective leaf
parameter has degree two, so `mu <= 2` and

```text
U_eq,z = 16.
```

Substituting a uniform popularity cap `U` into the packet floor gives the
support floor used by the package.  Define

```text
T_U = floor(s U/(Lambda+1)),
d_U = h(2D-1)T_U,

M_degen(K,d) =
  binom(K,2),                  if d >= K-1,
  dK - binom(d+1,2),           if 0 <= d < K-1.
```

Then the equal-line packet-sift floor is

```text
F_eq =
ceil(
  K^2 s^2 /
  (
    K s
    + 2K h(D-1)s
    + K(K-1)Lambda
    + 2(s-Lambda) M_degen(K,d_U)
  )
).
```

If `F_eq` beats the intended support budget, the residual family must enter
one of the following named alternatives:

```text
large support,
near-star endpoint template,
model-entry failure,
multiplicity failure,
charged quotient/tangent/fixed-root/endpoint/singular exception.
```

## What remains open

The missing theorem is the nonlocal model-entry statement:

```text
After the charged branches are removed, endpoint-independent high-overlap
stars enter the ordinary projective equal-line split-fiber chart with bounded
leaf-parameter multiplicity.
```

Proving this would close the equal-line packet branch with explicit constants.
Refuting it would produce a new residual obstruction floor that should be
labelled in the v9 Hankel atlas.

## Verification

The dependency-free digest verifier checks the Cauchy floors, endpoint-star
sift inequalities, divisor-gate root-count cap, and equal-line substitutions:

```sh
python3 experimental/scripts/verify_m1_packet_sift_popularity_digest.py
```
