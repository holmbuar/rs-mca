# Rank-16 value-fiber moment route cut at `u=1,043,459`

## Verdict

`RIGOROUS SOURCE-SPECIFIC RELAXATION COUNTERMODEL; NO STATE PAYMENT.`

This packet was derived at `origin/main`
`9262f63cf093a7510a2df435f220390f59e2bcd5` and rebased and replayed at
`c35a6da31ed0905afcbaaefe4eb0f242572ebb35`.  The consumed source note has
unchanged blob SHA `90be3164bc9a31d86374d5c0e2d3659968494e47`.  Its verifier independently
reconstructs the child-state Hahn cap; it does not consume a pending PR or
alter the base-field/code-field versus `p^6` challenge-denominator ledger.

Shorten a putative list at `u=1,043,459` through one more agreement coordinate.
The independently reconstructed child theorem gives the certified section
ceiling

```text
B=41,358,983,685,320,209.
```

Double counting agreement incidences then improves the general spherical
ceiling to

```text
L <= floor(NB/a)=600,370,193,369,924,877,               (1)
```

but this remains `2.1843...` times the target

```text
T=274,854,110,496,187,592.
```

The full field-value partition does not close that factor.  There is an exact
integral occupancy model at the right side of (1), hence strictly above `T`,
which satisfies simultaneously:

1. the exact minimum agreement incidence total;
2. every child-section ceiling `q_x<=B`;
3. exact Hahn caps on **every** agreement and nonagreement value fiber;
4. the full `p=2,130,706,433` value-bucket partition at every coordinate;
5. the Reed--Solomon pair equal-value/root budget; and
6. even the stronger affine-independent cubic equal-value/root budget with
   **zero** collinear allowance.

Thus agreement shortening plus pair and cubic polynomial value-fiber moments,
used only through these aggregate constraints, cannot pay `u=1,043,459`.
Any successful source theorem at this wall must retain information discarded
by the occupancy relaxation, such as cross-coordinate fixed-syndrome/Padé
compatibility, a canonical gcd owner with controlled multiplicity, or a
higher structural invariant.

## 1. Source-valid constraints

Let `Z` be the actual universal agreement set, `|Z|=u`, and put

```text
N=n-u       =1,053,693,
a=m-u       =72,588,
h=K-u-1     =5,116.
```

For a residual evaluation coordinate `x` and a field value `v`, let

```text
n_(x,v)=#{listed P : P(x)=v},
q_x=n_(x,U(x)).
```

Every candidate has at least `a` residual agreements with the received word,
so

```text
sum_x q_x >= L a.                                       (2)
```

The `q_x` candidates in one agreement bucket share the common agreement subset
`Z union {x}`; it need not be their actual maximal universal set.  Removing
this specified subset and choosing exactly `m` agreements lets the audited
Hahn theorem at `u+1=1,043,460` give

```text
q_x<=B.                                                  (3)
```

There is a stronger asymmetric statement for every other value.  Fix
`v!=U(x)` and change only the received symbol at `x` from `U(x)` to `v`.
Every candidate in the `v`-fiber gains one agreement, so it is a list for
threshold `m+1` sharing the common agreement subset `Z union {x}`.  Removing
that specified subset and selecting exactly `m+1` agreements gives residual
supports with exact constant-weight parameters

```text
N'=1,053,692,       a'=72,588,       h'=5,115.
```

An exact degree-five Hahn certificate, with active distances

```text
67,473, 67,587, 67,588, 67,701, 67,702,
```

therefore gives the uniform nonagreement value-fiber ceiling

```text
n_(x,v)<=C=28,334,997,835,769,598       for v!=U(x).     (4)
```

Two distinct degree-`<K` candidates already agree on `Z`, so they can have at
most `h` further equal-value coordinates.  Double counting equal-value pairs
gives the exact source inequality

```text
sum_(x,v) binom(n_(x,v),2) <= h binom(L,2).              (5)
```

For three affinely independent candidates, divide two independent difference
polynomials by the universal locator of `Z`.  Both quotients have degree at
most `h`; their gcd has degree at most `h-1`, because gcd degree `h` would make
the quotients scalar multiples.  A collinear triple can contribute one extra
coordinate.  Let `C_collinear` denote the number of unordered collinear
triples of listed candidates.  Hence the source-valid cubic inequality is

```text
sum_(x,v) binom(n_(x,v),3)
 <=(h-1)binom(L,3)+C_collinear.                          (6)
```

The model below satisfies the strictly stronger inequality obtained by
setting `C_collinear=0`.  It therefore survives any nonnegative collinear
correction, including one bounded using the proved line ceiling 15.

## 2. Exact integral occupancy model

Let

```text
L=600,370,193,369,924,877.
```

Write `La=Nq+r`.  Exact division gives

```text
q=41,358,983,685,320,208=B-1,
r=1,043,532.
```

Assign `q_x=B` at exactly `r` coordinates and `q_x=B-1` at the remaining
`N-r` coordinates.  Then

```text
sum_x q_x=La,       max_x q_x=B,                        (7)
```

so (2) and (3) hold exactly.  At each coordinate, retain this distinguished
agreement bucket and distribute the remaining `L-q_x` items as evenly as
possible among the other `p-1` field values.  This gives a literal integral
partition into all `p` value buckets at every coordinate.  Every
nonagreement bucket then has size at most

```text
262,359,564 < C,                                         (8)
```

so the pointwise offset-fiber theorem (4) also holds with enormous room.

The exact pair count of these buckets is

```text
901,205,540,550,566,667,931,568,949,443,065,569,399,
```

whereas the right side of (5) is

```text
922,016,696,124,650,847,653,056,349,242,555,964,616.
```

The pair budget therefore has positive slack

```text
20,811,155,574,084,179,721,487,399,799,490,395,217.     (9)
```

The exact cubic count is

```text
12,424,314,017,670,523,947,730,899,534,775,908,638,224,058,405,553,538,731,
```

while the stronger zero-collinearity ceiling `(h-1) binom(L,3)` is

```text
184,481,047,371,623,982,946,630,266,765,953,291,441,653,069,991,854,646,250.
```

Thus the cubic slack is

```text
172,056,733,353,953,458,998,899,367,231,177,382,803,429,011,586,301,107,519. (10)
```

Only `0.067347...` of the stronger cubic budget is used.  The obstruction is
therefore not a rounding accident or a narrowly missed third-moment gain.

## 3. Exact implication

The construction is a feasible point of the aggregate value-fiber relaxation
at `L>T`.  Consequently no argument whose entire retained data are (2)--(6),
the pointwise agreement/error fiber caps (3)--(4), and local integral
value-bucket partitions can deduce `L<=T`.

The strongest positive conclusion from those inputs alone remains (1), still
short by a factor `2.184...` against the target.

## Nonclaims

- The occupancy model is not asserted to be realizable by Reed--Solomon
  polynomials or by a genuine list.
- No state is eliminated and no official score moves.
- The cut does not address higher moments with affine-dependence corrections,
  cross-coordinate bucket consistency, fixed-syndrome equations, Padé minors,
  or canonical gcd-owner multiplicities.
- The obsolete `u=1,043,581` endpoint calibration is not used.

## Replay

```text
ruby --disable-gems -w experimental/scripts/verify_rank16_u1043459_value_fiber_moment_route_cut.rb
```
