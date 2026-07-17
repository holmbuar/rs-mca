# Rank-16 fixed-26 polynomial cross-minor lift

**Claim.** In one literal fixed-26 source cell, source-normalized divided
differences satisfy a nonzero polynomial four-cycle lift and a hierarchy of
`g`-divisible cross minors.  A 25-edge collision class on eight labels
therefore has a valid `K_{4,4}` whose `4 x 4` cross minor either vanishes
identically or forces the number of evaluation partitions with a block of
size at least five to be at most `51,988`.

**Status.** Proved local theorem, conditional on the fixed-26 compiler and
collision-class inputs at PR #862 head
`d2b11f1914dea4cb4a7670736cf00d1422c878de`.  The theorem makes no finite
or asymptotic payment.  The official score remains `0/2`.

**Verifier.**
`experimental/scripts/verify_rank16_fixed26_polynomial_cross_minor_lift.py`
replays the numerical degree ledger, exhausts all complements of 25-edge
graphs on eight labels, checks the partition-to-determinant implication, and
runs semantic mutations.  The algebraic proof below is not
computation-dependent.

## Literal source cell

Work over the deployed field and subgroup

```text
p = 2,130,706,433,       H = mu_(2^21),
n = 2,097,152,           B = 32,768,
a = 67,472,              r = 63,601,
d = 28,897.
```

Fix one canonical received word and actual first-match owner, one monic
degree-`a` generator `g` with `gcd(g, X^n-1)=1`, one projective residue ray,
one 26-label core `C`, and one non-global collision class
`Y={y_0,...,y_7}` containing at least 25 actual valid edges.  All polynomials
below belong to this same source cell.

Put `T=X^B mod g`.  The fixed-26 compiler provides representatives `V_y`
and source-normalized divided differences

```text
V_y - V_z = (y-z) U_yz,
U_yz = rem_g(xi ((T-y)(T-z))^(-1)).                 (1)
```

For an exact-degree valid edge, the monic residual locator is
`R_yz=q_yz U_yz` for one nonzero scalar `q_yz`.  The minor identities below
must use the `U_yz` from (1).  Independently monic-normalizing each matrix
entry destroys the common source normalization and is not permitted.

Every edge called valid below retains all inherited filters: exact degree,
squarefree complete splitting over `H`, avoidance of selected complete
fibres, no extra complete q64 fibre, residual footprint at least four,
nonpaired ownership, all earlier-owner exclusions, and the actual canonical
first-match test.

## Theorem

### 1. Source coordinates and evaluation partitions

Let `phi(Z)=prod_i (Z-y_i)` and

```text
U_Y  = rem_g(xi phi(T)^(-1)),
p_ij = phi(Z)/((Z-y_i)(Z-y_j)),
U_ij = rem_g(U_Y p_ij(T)).                              (2)
```

The map from degree-at-most-six polynomials to the span of the `U_ij` is
injective in the non-global branch.  Scaled evaluation at the eight labels
identifies its image with

```text
H_0 = {(z_0,...,z_7): sum_i z_i=0},
p_ij |-> (e_i-e_j)/(y_i-y_j).                           (3)
```

Thus the 28 projective pair directions are the literal `A_7` root
directions.  In particular, the zero graph of any linear functional on
their span is a disjoint union of cliques.

For `x in H`, define a partition `pi_x` of `Y` by
`i ~ j` exactly when `V_{y_i}(x)=V_{y_j}(x)`.  Equation (1) gives

```text
U_ij(x)=0  iff  i and j lie in one block of pi_x.        (4)
```

For valid edges, scalar normalization preserves (4).  Hence gcd degrees of
valid locators count literal common roots in `H`, and

```text
sum_(x in H) #{valid edges internal to pi_x} = |E| r.    (5)
```

### 2. Nonzero four-cycle lift

For distinct `a,b,c,d` such that `{a,c},{b,d},{a,b},{c,d}` are valid,
the residue identity in the quotient algebra is

```text
U_ac U_bd = U_ab U_cd  (mod g).
```

Therefore

```text
Delta_abcd := U_ac U_bd - U_ab U_cd = g K_abcd,
deg K_abcd <= 2r-a = 59,730.                             (6)
```

This polynomial is nonzero.  Otherwise every root of the squarefree
`U_ac` would be a root of `U_ab` or `U_cd`.  The inherited adjacent-edge
gcd theorem bounds each intersection by `d`, giving

```text
r <= deg gcd(U_ac,U_ab)+deg gcd(U_ac,U_cd)
  <= 2d = 57,794,
```

contrary to `r=63,601`.  The strict gap is `r-2d=5,807`.

Because `g` is root-free on `H`, every common `H`-root of the two products
in (6) is a root of `K_abcd`.  Thus

```text
deg gcd(R_ac R_bd, R_ab R_cd) <= 59,730.                 (7)
```

When all six edges on the four labels are valid, comparison of the induced
four-label partitions also gives the exact four-triangle overlap identity.
Writing `G_ijk` for the common triangle gcd and `G_abcd` for the six-edge
gcd,

```text
deg G_abc + deg G_abd + deg G_acd + deg G_bcd
  - 2 deg G_abcd <= 59,730.                              (8)
```

### 3. Higher source-normalized cross minors

Let `A_0=(a_1,...,a_s)` and `B_0=(b_1,...,b_s)` be disjoint ordered label
sets, `2<=s<=4`, with every cross pair in the collision class.  Define

```text
Delta_(A_0,B_0) = det(U_(a_i,b_j))_(1<=i,j<=s).          (9)
```

The compiler identity has the row-compatible form

```text
(X^B-a_i) U_(a_i,b_j) = V_(b_j) + g Q_(a_i,b_j).        (10)
```

Multiply row `i` in (9) by `X^B-a_i`, then subtract the first row from
all later rows.  The last `s-1` rows acquire a factor `g`.  Since every
`X^B-a_i` is coprime to the root-free generator `g`, Gauss's lemma in the
polynomial UFD gives

```text
g^(s-1) divides Delta_(A_0,B_0).                         (11)
```

If the determinant is nonzero, its unique quotient satisfies

```text
deg(Delta/g^(s-1)) <= sr-(s-1)a
                    = r-(s-1)(a-r).                     (12)
```

The exact thresholds are

```text
s=2: 59,730;    s=3: 55,859;    s=4: 51,988.            (13)
```

### 4. Dense eight-label dichotomy

A graph with at least 25 of the 28 edges on eight vertices has a `K_{4,4}`.
Indeed, its complement has at most three edges; the connected components of
that complement can be divided into two groups of four vertices, so no
missing edge crosses the resulting `4+4` partition.

Fix such a valid partition `Y=A_0 sqcup B_0`.  Let

```text
Delta = det(U_ab)_(a in A_0,b in B_0),
N_5 = #{x in H: pi_x has a block of size at least five}.
```

Exactly one of the following holds:

1. `Delta=0`, producing the literal 24-term source-normalized determinant
   syzygy; or
2. `Delta=g^3 K`, where `K!=0`, `deg K<=51,988`, and `N_5<=51,988`.

For the second assertion, if a block `D` of `pi_x` has size at least five,
put `u=|D cap A_0|` and `v=|D cap B_0|`.  The `u` corresponding matrix rows
can be nonzero only in the `4-v` columns outside `D`, while `u>4-v`.
Hall's condition fails, so `Delta(x)=0`.  Since `g(x)!=0`, every such `x`
is a distinct root of `K`, proving the bound.

## Source and novelty audit

PR #862 owns the fixed-26 divided-difference compiler, collision collapse,
simultaneous Krylov bounds, anchor independence, adjacent-edge gcd bound,
split S-unit triangles, and scalar resultant four-cycle.  The new layer is
the nonzero polynomial lift (6), the product/triangle overlap bounds, the
`g^(s-1)` cross-minor hierarchy (11)-(13), and the exact `K_{4,4}`
zero-minor/root-excess dichotomy.

PR #872 conditionally reduces its separate global residual arithmetic to
`T-3`.  PR #873 proves that fixed 26/27 cores are not multiplicity-one global
owners.  Nothing here is multiplied over cores or charged to either global
ledger.

## Nonclaims and exact remaining wall

This theorem does **not**:

- exclude a source-valid seven-star or construct one;
- prove that the `4 x 4` determinant is nonzero;
- prove that `N_5>=51,989`;
- turn collision candidates into valid edges;
- prove G64-CAP, cap 116, or a global first-match aggregation;
- pay a rank-16 parent, Grand List, or Grand MCA.

The exact next wall is the source-normalized determinant-rank dichotomy:
either show that vanishing valid `3 x 3` and `4 x 4` minors force an already
owned global/rank-two source branch, or force a nonzero order-`s` minor to
have more than `55,859` roots for `s=3` or `51,988` roots for `s=4`.
