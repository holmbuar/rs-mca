# Rank-15 exact two-flat cross-class extension through u=1,043,899

## Claim and ownership

Fix

```text
n = 2,097,152,   K = 1,048,576,   m = 1,116,047.
```

Let `F` be any field, let `H subset F` contain `n` distinct points, and let
`U:H -> F`. Put

```text
L_m(U) = {P in F[X] : deg P < K and |{x in H:P(x)=U(x)}| >= m}.
```

Let `A subset F[X]_{<K}` be an exact affine two-flat

```text
A = P_0 + span_F{V_1,V_2},
```

and define its actual universal agreement set by

```text
Z = {x in H : P(x)=U(x) for every P in A},   |Z|=u.
```

Then

```text
|A intersect L_m(U)| <= 211
```

for every

```text
1,043,899 <= u <= 1,043,957.                         (T)
```

Ownership is disjoint:

```text
#847:                 u=1,043,917..1,043,957;
#865 before this add: u=1,043,902..1,043,916;
this add:             u=1,043,899..1,043,901.
```

The exact next relaxation wall is `u=1,043,898`, where the optimized
capacity exceeds the demand by `1,918`.

## Literal source reduction

Assume for contradiction that `A intersect L_m(U)` contains 212 distinct
polynomials, and select exactly 212. Their affine parameters form a set
`S subset F^2` of size 212. For a fixed state put

```text
N = n-u,   a = m-u,   lambda = K-1-u.
```

For `x in H\Z`, the coordinate section

```text
A_x = {P in A : P(x)=U(x)}
```

is empty or a proper affine line. It cannot equal all of `A`, by actual
universality of `Z`. A nonempty section has universal count at least `u+1`.
The exact rank-one recurrence scan gives

```text
F_{m,1}(1,043,900) = 15,
```

with maximizers `v=1,045,969..1,048,575`. Thus every proper coordinate
section in the three new states contains at most 15 selected points.

Let `L_Z` be the monic locator of `Z`. Factor the directions as

```text
V_1 = L_Z G A_1,   V_2 = L_Z G A_2,   gcd(A_1,A_2)=1.
```

Set

```text
d = max(deg A_1,deg A_2),
r = |{x in H\Z:G(x)=0}|.
```

Then

```text
d + deg G <= lambda,   deg G >= r,   d <= lambda-r.   (1)
```

Coordinates where `G` vanishes are inactive. At every active coordinate,
division by the nonzero value `L_Z(x)G(x)` produces a literal affine line
in the parameter plane. For each represented projective normal direction
`nu`, meaning a direction with positive active-coordinate occupancy, let
`c_nu` be its active-coordinate count and let `h_nu` be the maximum number
of selected parameters on one parallel line of that direction. Coprimality
and the degree ledger give

```text
c_nu <= d,   sum_nu c_nu <= N-r,   1 <= h_nu <= 15.  (2)
```

Counting the required residual agreements gives

```text
212a <= sum_nu c_nu h_nu.                            (3)
```

Replace `d` by `lambda`, pad total directional weight to `N`, and use
zero-occupancy dummy directions only for that padding. These dummies are
not represented source directions and enter no incidence constraint. This
enlarges the right side of (3). Since

```text
N = 225 lambda + s,   0 < s < lambda,
```

the relaxed optimizer has 225 full-weight directions and one residual
direction of weight `s` and occupancy `hstar`.

## Inherited finite constraints

Choose a maximum-occupancy selected-parameter line in each represented
direction. Let `n_h` count chosen lines with `h` selected points. Any pair
of selected points lies on at most one chosen line, and at a selected point
distinct chosen lines use disjoint sets of other selected points. Hence

```text
sum_h C(h,2)n_h <= C(212,2),                          (4)
sum_{h=2}^{15} (h-1)r_h(p) <= 211.                   (5)
```

The exact mod-13 consequence, the three predecessor point-capacity cuts,
and the four cuts proved in the first #865 commit are reconstructed by the
verifier from their local knapsack inequalities. No output or Python module
from a pending PR is imported. The resulting eight resource functions are
discretely convex through occupancy 13, which gives the exact predecessor
full-incidence table

```text
hstar:  1    2    3    4    5    6    7    8    9   10   11   12   13   14   15
Ibase: 3271 3271 3271 3271 3271 3270 3270 3269 3269 3268 3267 3266 3265 3254 3253.
```

The source proof for these inherited constraints is contained in the exact
base note
`experimental/notes/l2/rank15_two_flat_u1043902_four_cut_extension.md`.

## New cross-occupancy-class cut

For one selected point `p`, retain classes 10 through 15 and write
`r_h=r_h(p)`. Define

```text
Psi(r) = B + sum_h C_h r_h + sum_{10<=h<=k<=15} L_hk Q_hk(r),             (6)
Q_hh(r)=C(r_h,2),   Q_hk(r)=r_h r_k for h<k,
B=1,000,000,000,009.
```

The linear coefficients are

```text
C10=-35,686,639,872  C11=-59,318,449,143
C12=C13=C14=C15=-66,666,666,667.
```

The nonzero quadratic coefficients are

```text
L10,11=4,088,463,951   L10,12=4,915,294,705
L10,13=2,733,666,212   L10,14=1,549,694,453
L10,15=  180,418,024   L11,11=10,467,842,606
L11,12=10,549,862,864  L11,13=6,974,378,531
L11,14=4,406,162,092   L12,12=9,468,952,463
L12,13=6,453,906,223   L12,14=2,463,237,973
L13,13=3,794,562,793   L13,14=1,624,704,129
L14,14=1,450,158,934.
```

All `L_hk` are nonnegative. Exact enumeration of all nonnegative integer
vectors satisfying

```text
9r_10+10r_11+11r_12+12r_13+13r_14+14r_15 <= 211     (7)
```

checks 139,979 local types and proves `Psi(r)>=0`. Equality occurs only at

```text
(r_10,r_11,r_12,r_13,r_14,r_15)=(1,2,0,0,0,13).     (8)
```

Classes at most 9 may be discarded, leaving a vector satisfying (7).
Summing (6) over the 212 selected points, use

```text
sum_p C(r_h(p),2) <= C(n_h,2),
sum_p r_h(p)r_k(p) <= n_h n_k for h<k.               (9)
```

Both bounds count pairs of retained chosen lines meeting at a selected
point; a pair of distinct-direction affine lines meets in at most one point.
Because every quadratic coefficient is nonnegative, every actual profile
must satisfy

```text
D(n) = 212B + sum_h C_h h n_h
       + sum_h L_hh C(n_h,2)
       + sum_{h<k} L_hk n_h n_k >= 0.                (10)
```

## Exact finite exclusion

The verifier enumerates every profile at every predecessor incidence layer
that can meet the three state demands. It first applies all inherited source
constraints, then (10). The largest value of `D(n)` in every newly removed
layer is strictly negative. The scan covers 75,485 inherited-valid profiles
across the relevant layers; its per-layer counts and maxima are printed in
the expected transcript.

The strengthened exact full-incidence table is

```text
hstar: 1    2    3    4    5    6    7    8    9    10   11   12   13   14   15
Inew:  3270 3270 3270 3270 3269 3269 3269 3269 3268 3267 3267 3265 3262 3254 3253.
```

The three source states then have exact capacities

```text
u          lambda  N decomposition       hstar  capacity    212(m-u)   margin
1,043,901  4,674   225*4,674+1,601       8      15,292,114  15,294,952  -2,838
1,043,900  4,675   225*4,675+1,377       8      15,293,591  15,295,164  -1,573
1,043,899  4,676   225*4,676+1,153       4      15,295,132  15,295,376    -244.
```

Each contradicts (3). This proves the three new entries and hence (T).

## Exact next wall

At `u=1,043,898`, the strengthened relaxation has the profile

```text
n_15=187, n_14=5, n_13=23, n_10=6, n_9=4, n_4=1.
```

Its capacity is `15,297,506`, versus demand `15,295,588`, for surplus
`1,918`. Every current resource has nonnegative slack, including cross-cut
slack `46,334,353,108`. The profile is not claimed geometrically realizable
and is not a Reed-Solomon counterexample.

## Recurrence consumer and nonclaims

The independent recurrence replay inserts only the three new dimension-2
entries. Exactly three `D_2` states change, by at most 5. Dimensions 3 through
15 change at zero states. The rank-15 parent remains

```text
283,039,300,733,528,044,
```

still `8,185,190,237,340,452` above the target
`274,854,110,496,187,592`.

This theorem does not claim `u<=1,043,898`, a source counterexample, a
rank-15 parent saving, rank-16 payment, Grand List, Grand MCA, or official
score movement. The official score remains `0/2`.

## Replay

From the repository root:

```bash
python3 experimental/scripts/verify_rank15_u1043899_crossclass_extension.py
python3 -O experimental/scripts/verify_rank15_u1043899_crossclass_extension.py
python3 -m py_compile experimental/scripts/verify_rank15_u1043899_crossclass_extension.py
cmp experimental/data/certificates/rank15-two-flat-u1043899-crossclass-extension/verify_rank15_u1043899_crossclass_extension.expected.txt <output>
```

The verifier is standard-library only and uses explicit `require` checks, so
the proof gates remain active under `python -O`.
