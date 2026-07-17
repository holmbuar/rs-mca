# Rank-16 fixed-27 residual specialization curve

Claim: Under the integrated rank-two syzygetic hypotheses, the normalized
fixed-27 residuals are nonzero scalar normalizations of specializations of one
`F_p[X,Y]` polynomial of label degree at most two in the cubic branch and at
most three in the quartic branch. A separate argument excludes three labels
whenever the root-free generator contains a quadratic whole-`B`-block factor.
Status: PROVED local source theorem. It makes zero finite-ledger, recurrence,
Grand List, Grand MCA, or official-score payment.
Verifier: `experimental/data/certificates/rank16-fixed27-residual-specialization-curve/verify_rank16_fixed27_residual_specialization_curve.py`
replays the deployed arithmetic, scalar-normalization and divided-difference
identities on exact finite-field fixtures, and the quotient-ring Vandermonde
terminal. The algebraic proof is below.
Consumers: The surviving rank-two fixed-27 cap-six problem after the integrated
quotient-line obstruction and block-wedge theorem.
Risk-limits: This note consumes, and does not reclaim, the block-wedge
dichotomy, `e in {3,4}`, or the inherited quartic dimension-four bound. It
does not prove the fixed-27 cap six, an all-core owner, a rank-16 parent, or
either official prize question.

## Provenance and source cell

This packet is based at
`origin/main@7f278167e1e51f968896229ae438ea5a76398f90`. It consumes the
integrated theorem in
`experimental/notes/l2/rank16_fixed27_block_wedge_stratification.md` and no
pending-PR theorem. In particular, the following are inherited hypotheses,
not new conclusions:

1. the literal fixed-27 post-core source equation;
2. quotient affine rank two;
3. the syzygetic branch and its primitive vector;
4. `e = deg a_0` lying in `{3,4}`; and
5. the coordinate formula `c_ij=a_j(y_i)/a_0(y_i)`.

Work over

```text
p = 2130706433,
H = mu_(2^21) in F_p^x,
B = 32768,
t = 981105,
a = 67472,
D = t-27B = 96369,
d = D-B = 63601,
w = D-a = 28897.
```

Fix one 27-element `q64` core, one root-free generator `g`, one syndrome
representative/projective ray, and one normalized source cell. Seven distinct
labels `y_i in mu_64` outside the core have

```text
A_i(X) = (X^B-y_i) R_i(X) = q_i h(X) + g(X) W_i(X),
q_i != 0,
deg g = a,
g(x) != 0 for every x in H,
deg R_i = d,
deg W_i <= w.
```

Each `R_i` is monic, squarefree, and split over `H`; it also has no additional
complete `q64` fibre. Normalize

```text
P_i = q_i^(-1) A_i,
rho_i = q_i^(-1) R_i.
```

Choose an actual affine anchor and independent directions as in the integrated
rank-two theorem:

```text
P_i = H_0 + g(c_i1 E_1 + c_i2 E_2),
deg E_j <= w.
```

The consumed primitive syzygy is

```text
a_0(X^B) H_0
  + g(a_1(X^B) E_1 + a_2(X^B) E_2) = 0,                (1)
a_0(X^B) = g(X) s(X),
e = deg a_0 in {3,4},
a_0(y) != 0 for every y in mu_64,
c_ij = a_j(y_i)/a_0(y_i).                               (2)
```

The integrated theorem also supplies

```text
c_ij a_0(T)-a_j(T) = (T-y_i)b_ij(T),
deg b_ij <= e-1.                                        (3)
```

## Exact theorem

Put `T=X^B`. Under the hypotheses above, the following assertions hold.

### 1. Residual specialization curve

There is a polynomial `mathcal R(X,Y) in F_p[X,Y]` with

```text
deg_X mathcal R <= d = 63601,
deg_Y mathcal R <= e-1,                                  (4)
```

such that every actual label satisfies

```text
mathcal R(X,y_i) = a_0(y_i) rho_i(X)
                  = a_0(y_i) q_i^(-1) R_i(X).            (5)
```

Let

```text
ell(Y) = coefficient of X^d in mathcal R(X,Y).
```

Then

```text
ell(y_i) = a_0(y_i) q_i^(-1) != 0,
R_i(X) = ell(y_i)^(-1) mathcal R(X,y_i),
q_i = a_0(y_i) ell(y_i)^(-1).                            (6)
```

Equation (6) is load-bearing. The monic residual `R_i` is a **nonzero scalar
normalization** of a specialization. The theorem does not claim the false
literal equality `R_i=mathcal R(X,y_i)`.

Consequently, the cubic residual span has dimension at most three and the
quartic residual span has dimension at most four. The quartic numerical span
cap is inherited from the integrated block-wedge theorem; the new conclusion
is that the residuals lie on the displayed degree-at-most-three specialization
curve. The cubic cap improves the inherited split-block dimension six to
dimension three.

For any `e+1` actual labels `y_i0,...,y_ie`, one has

```text
sum_(nu=0)^e [
  a_0(y_i_nu) q_i_nu^(-1)
  / product_(mu != nu)(y_i_nu-y_i_mu)
] R_i_nu(X) = 0.                                        (7)
```

Every coefficient in (7) is nonzero. Thus every four cubic residuals and
every five quartic residuals admit an all-nonzero dependence.

### 2. Common base, occupancy, gcd, and union package

Define

```text
Base = {x in H : mathcal R(x,Y) is identically zero in Y}.
```

Then

```text
Base = Z_H(E_1) intersect Z_H(E_2),
|Base| <= w = 28897.                                     (8)
```

Outside `Base`, a point of `H` is a root of at most `e-1` of the seven
residuals. For distinct `i,j`,

```text
deg gcd(R_i,R_j) <= w = 28897.                            (9)
```

Writing `U=union_i Z_H(R_i)`, the exact deployed lower bounds are

```text
|U| >= 150361  when e=3,
|U| >= 109873  when e=4.                                 (10)
```

Neither bound exceeds the available deployed-root universe, so (10) is not a
nonexistence theorem.

### 3. Quadratic whole-block exclusion

Suppose independently that

```text
g(X) = b(X^B) r(X),
deg b = 2.
```

After scaling, take `b` monic. Necessarily

```text
deg r = a-2B = 1936 > 0.                                 (11)
```

Then one literal normalized source cell has at most two valid labels. In
particular, it cannot contain a seven-label rank-two family.

Define

```text
kappa_B(g) = max{deg b : 0 != b in F_p[T], b(X^B) divides g(X)}.
```

Because `a<3B`, one always has `kappa_B(g)<=2`. A seven-label family therefore
forces the exact local wall

```text
kappa_B(g) <= 1.                                         (12)
```

This excludes the monomial generator `X^67472`, two distinct complete
external `q64` factors, a repeated complete factor, and an irreducible
quadratic composition factor.

## Proof

### Residual curve and scalar normalization

First, (3) forces `deg a_1,deg a_2<=e`. If some `a_j` had degree greater than
`e=deg a_0`, its leading term could not cancel in `c_ij a_0-a_j`; division by
`T-y_i` would give `deg b_ij>=e`, contrary to (3).

Define

```text
N(X,Y) = a_0(Y)H_0(X)
       + g(X)(a_1(Y)E_1(X)+a_2(Y)E_2(X)).                (13)
```

Substitution `Y=X^B` makes (13) zero by (1). The polynomial remainder theorem
in `F_p[X,Y]`, viewed in the variable `Y`, therefore gives

```text
N(X,Y) = (X^B-Y) mathcal R(X,Y).                         (14)
```

All terms in (13) have `X`-degree at most `D`, while `X^B-Y` is monic of
`X`-degree `B`; hence `deg_X mathcal R<=D-B=d`. The `Y`-degree of (13) is at
most `e`, and division by the linear factor in `Y` gives
`deg_Y mathcal R<=e-1`. This proves (4).

At `Y=y_i`, (2) gives

```text
N(X,y_i) = a_0(y_i)P_i(X)
          = a_0(y_i)(X^B-y_i)rho_i(X).
```

Canceling `X^B-y_i` in (14) proves (5). Since `R_i` is monic, comparison of
the `X^d` coefficient proves (6). Formula (7) is the vanishing `e`-th divided
difference of the degree-at-most-`e-1` polynomial
`Y -> mathcal R(X,Y)`. Distinctness of the labels and the nonvanishing in (6)
make all its coefficients nonzero.

### Common base and root incidence

The polynomials `a_0,a_1,a_2` are linearly independent. Otherwise a constant
relation among them, divided at the seven labels by nonzero `a_0(y_i)`, would
put all affine coordinate points `(c_i1,c_i2)` on one line, contrary to
quotient affine rank two.

For `x in H`, equation (14) shows that `mathcal R(x,Y)` is identically zero
exactly when `N(x,Y)` is. Independence of the three `a_j` then gives

```text
H_0(x)=g(x)E_1(x)=g(x)E_2(x)=0.
```

Root-freeness of `g` gives `E_1(x)=E_2(x)=0`. Conversely, if both directions
vanish, (1) and `a_0(x^B)!=0` give `H_0(x)=0`. This proves (8); independence
and `deg E_j<=w` give the cardinality bound.

Outside `Base`, the nonzero polynomial `mathcal R(x,Y)` has degree at most
`e-1`, proving the occupancy claim. The affine coordinate points are distinct:
if `c_i=c_j`, then `P_i=P_j`, and division by `X^B-y_i` would put the forbidden
extra complete factor `X^B-y_j` in `rho_i`.

If `x in H` is a common root of `R_i,R_j`, subtracting the two normalized
source equations gives

```text
0 = g(x)((c_i1-c_j1)E_1(x)+(c_i2-c_j2)E_2(x)).
```

The direction combination is a nonzero polynomial of degree at most `w`, so
all common roots are among at most `w` roots. This proves (9).

Put `c=|Base|` and `m=e-1`. Seven degree-`d` squarefree residuals contribute
`7d` root incidences. Base roots have occupancy seven, and all other roots
have occupancy at most `m`, so

```text
7d <= 7c + m(|U|-c),
|U| >= c + ceil(7(d-c)/m).                               (15)
```

The right side is decreasing for `0<=c<=w`, so its minimum is at `c=w`.
Substitution of `d-w=34704` gives exactly (10).

### Quadratic whole-block terminal

Write each degree-`d<2B` residual uniquely as

```text
rho_i = U_i + X^B Z_i,
deg U_i < B,
deg Z_i <= d-B = 30833 < B.                              (16)
```

With `T=X^B`,

```text
P_i = -y_i U_i + T(U_i-y_i Z_i) + T^2 Z_i.              (17)
```

For `i!=j`, the fixed-syndrome equation gives

```text
P_i-P_j = gL_ij = b(T)rL_ij.
```

Thus `Q_ij=(P_i-P_j)/b(T)` has degree at most
`D-2B=30833<B`. Writing
`b(T)=T^2+beta_1 T+beta_0` and comparing the three blocks in (17) gives,
modulo `r`, common residue classes

```text
Z     = [Z_i],
C_1   = [U_i-y_i Z_i],
C_0   = [-y_i U_i]
```

with

```text
C_0 + y_i C_1 + y_i^2 Z = 0                             (18)
```

in `F_p[X]/(r)`. Three distinct labels make (18) a Vandermonde system. Its
determinant is a nonzero field scalar, hence a unit even if the quotient ring
has zero divisors. Therefore `C_0=C_1=Z=0`, so `r` divides both `U_i` and
`Z_i`, and hence every `rho_i`.

But each `rho_i` is a nonzero scalar multiple of a polynomial split over
`H`. A nonconstant divisor `r` must then split over `H`, while `r` divides the
generator `g`, which has no root in `H`. This contradicts (11), proving the
two-label cap and (12).

## Source compiler

Before fixed-core cancellation, the full locator is `L_i=G_C A_i`, where

```text
G_C(X) = product_(z in C)(X^B-z),
L_i == q_i h_src (mod g).
```

Every root of `G_C` lies in `H`, while `g` is root-free there. Hence `G_C` is
invertible modulo `g`. The canonical post-core representative

```text
h = rem_g(G_C^(-1) h_src)
```

gives the literal equation used above and `deg W_i<=D-a=w`. No abstract
support family or unowned residual family is substituted.

## Finite ledger, consumers, and exact remaining wall

This theorem makes zero finite-ledger payment. The conditional fixed-27
numbers remain, without being charged,

```text
cap 6 total = 271769678181377208,
target margin = 3084432314810384,
cap 7 total = 300964056749491576,
target excess = 26109946253303984.
```

There is no recurrence payment and the official score remains `0/2`.

The local consumer is now exact: a surviving rank-two seven-label source cell
must have

```text
e in {3,4},
kappa_B(g) <= 1,
R_i(X) = ell(y_i)^(-1) mathcal R(X,y_i),
deg_Y mathcal R <= e-1,
```

while preserving complete splitting, squarefreeness, selected-fibre
avoidance, no extra `q64` fibre, residual footprint at least four, and `q32`
nonpairing. Even a local cap does not enter the global ledger until a disjoint
source-cell aggregation over every core, generator, syndrome, and ray is
proved.

The exact remaining walls are:

1. **Local:** exclude or construct the `e in {3,4}`, `kappa_B(g)<=1`
   specialization-curve families.
2. **Global:** prove a source-cell-disjoint aggregation compatible with the
   integrated first-match owner.

## Explicit nonclaims

This note does not claim:

- the block-wedge dichotomy, primitive syzygy, `e in {3,4}`, or inherited
  quartic dimension-four bound as new work;
- literal equality between monic residuals and curve specializations;
- exclusion of the `kappa_B(g)<=1` wall;
- a uniform fixed-27 cap six;
- a seven-label counterexample;
- payment of one fixed core or a global first-match profile;
- a recurrence parent saving or rank-16 closure;
- a Grand List or Grand MCA theorem; or
- an official score change.
