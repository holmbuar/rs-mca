# Director audit: fixed-27 cap-seven rigidity

## Verdict

`PASS AT THE STATED SUPPORT-AND-VALUE SCOPE.`

The theorem uses only the literal length-101 punctured moment-kernel MDS
distance `38`, the 101-point complement of a fixed 27-core, and exact integer
incidence identities.

For two distinct size-20 tails in one contracted 37-moment syndrome, distance
at least 38 gives pair intersection at most two.  Second-order Bonferroni then
forces eight tails to occupy at least

```text
8*20 - 2*C(8,2) = 104 > 101,
```

so the uniform support multiplicity is at most seven.

For seven tails, writing `m_x` for point multiplicities gives

```text
P - (140-|union|) = sum_x C(m_x-1,2) = D,
P = 42-delta,
|union| = 98+delta+D <= 101.
```

Thus at most three of the 21 pair edges are defective.  Their endpoints
cover at most six tails, leaving an anchor with six size-two intersections.
The exact value identity follows from

```text
wt(e_i-e_j)=40-s_ij-z_ij
```

and summation: `delta = X+Z`.  Every anchor difference therefore has weight
38 and unequal coefficients at both shared roots.

The final constant-numerator statement is also correctly scoped.  In the
standard partial-fraction pair identity, 37 vanished moments factor out the
order-37 term, leaving numerator degree at most `2-s_ij`; for an anchor pair
this is degree zero.  Uniqueness of partial fractions and nonzero tail
coefficients make that constant nonzero.

The replay exhausts all nonnegative multiplicity profiles allowed by
`delta+D<=3` and reproduces the eleven displayed profiles.  No existence of a
seven-tail family is asserted.  The exact remaining theorem wall is to exclude
that near-extremal case and improve cap seven to cap six.
