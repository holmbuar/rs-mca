# Rtail fixed-27 support cap seven and seven-tail rigidity

## Result

Fix a 27-root core `C subset mu_128` and one contracted 37-moment syndrome.
Let `T_i subset mu_128\C` be distinct exact tails of size twenty representing
that syndrome.  Then there are at most seven tails.

If seven tails exist, write

```text
s_ij=|T_i intersect T_j|,
m_x=#{i:x in T_i},
P=sum_(i<j) s_ij=sum_x C(m_x,2),
delta=sum_(i<j)(2-s_ij)=42-P,
D=sum_x C(m_x-1,2).
```

Their union and multiplicities satisfy the exact rigidity identity

```text
|union_i T_i|=98+delta+D<=101,
delta+D<=3.                                           (1)
```

In particular:

1. at least eighteen of the twenty-one pairs intersect in exactly two
   roots;
2. no root belongs to five tails, and there is at most one fourfold root;
3. some anchor tail `T_0` intersects every other tail in exactly two roots.

If the literal nonzero tail coefficients are denoted `e_(i,x)`, put `Z`
for the total number of pairs `(i,j,x)` with

```text
x in T_i intersect T_j and e_(i,x)=e_(j,x),
```

and put

```text
X=sum_(i<j)(wt(e_i-e_j)-38).
```

Then

```text
delta=X+Z.                                            (2)
```

Consequently the six differences from the anchor in item 3 are all literal
minimum-weight 38 codewords, and the two coefficients at each of their
shared roots are unequal.  In the rational pair certificate, every anchor
pair therefore has a nonzero constant numerator `D_0i`.

This theorem proves the unconditional support cap seven and reduces the
desired cap six to the single near-extremal seven-tail case.  It does not
exclude that case and therefore does not prove the new common-27 payment.

## Proof

Two different exact tails give the same first 37 moments, so their
difference is a nonzero word of the length-101 punctured moment-kernel MDS
code with distance 38.  Its support lies in `T_i union T_j`, hence

```text
s_ij<=2.                                              (3)
```

If eight tails existed, second-order Bonferroni and (3) would give

```text
|union_(i=1)^8 T_i|
 >=8*20-sum_(i<j)s_ij
 >=160-2*C(8,2)=104,
```

but every tail lies in the 101-point complement of `C`.  Thus eight tails,
including every proposed order-eight rotation orbit, are impossible.

Now assume there are seven.  Put

```text
E=sum_x(m_x-1)=140-|union_i T_i|.
```

The elementary identity

```text
C(m,2)-(m-1)=C(m-1,2)
```

gives `P-E=D`.  Since `P=42-delta`, this rearranges to (1).  Both `delta`
and `D` are nonnegative integers.  Hence at most three pair-defect units
occur, while a point of multiplicity at least five would contribute at
least `C(4,2)=6` to `D`.

Every pair not having intersection two consumes at least one unit of
`delta`, so at most three edges of the seven-vertex pair graph are
defective.  Their endpoints cover at most six vertices.  A remaining vertex
is the asserted anchor.

For the value identity, let `z_ij` be the number of common roots at which
the two nonzero coefficients agree.  Directly,

```text
wt(e_i-e_j)=40-s_ij-z_ij.
```

Summing over the twenty-one pairs gives

```text
sum_(i<j) wt(e_i-e_j)=840-P-Z=798+delta-Z.
```

Every difference has weight at least 38, so subtracting `21*38=798` proves
(2).  An anchor pair has `s_0i=2`, and its distance inequality forces
`z_0i=0` and weight exactly 38.  The exact rational pair formula then has
numerator degree at most `2-s_0i=0`; it cannot be zero for two distinct
partial-fraction presentations, so it is a nonzero constant.

## Complete overlap profiles

Let `n_j=#{x:m_x=j}`.  Equation (1) permits exactly the following eleven
integer profiles:

```text
delta D | n1 n2 n3 n4 | union
0     0 | 56 42  0  0 |  98
0     1 | 59 39  1  0 |  99
0     2 | 62 36  2  0 | 100
0     3 | 65 33  3  0 | 101
0     3 | 64 36  0  1 | 101
1     0 | 58 41  0  0 |  99
1     1 | 61 38  1  0 | 100
1     2 | 64 35  2  0 | 101
2     0 | 60 40  0  0 | 100
2     1 | 63 37  1  0 | 101
3     0 | 62 39  0  0 | 101.
```

These are necessary overlap profiles, not existence claims.

## Replay

```bash
/usr/bin/ruby --disable-gems work/verify_rtail_fixed27_support_cap7_seven_tail_rigidity.rb
/usr/bin/ruby --disable-gems -w work/verify_rtail_fixed27_support_cap7_seven_tail_rigidity.rb
```

Both runs must byte-match the expected output and emit no stderr.
