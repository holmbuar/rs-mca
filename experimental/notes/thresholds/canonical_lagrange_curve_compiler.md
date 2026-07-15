# Canonical-Lagrange LineRay curve compiler: all pairs at most `N`

## Claim

Let `F` be any field, let `D subset F` contain `N` distinct points, and let

```text
h_x=(1,x,...,x^(R-1))^T,        x in D,
```

with `N>=R>=2t` and `t>=1`.  Write `Hc=sum_x c(x)h_x`.  Fix a syndrome
line

```text
y_gamma=y_0+gamma y_1,          y_1!=0,
```

whose first `t` moment coordinates have the canonical Lagrange
normalization

```text
(y_gamma)_0=...=(y_gamma)_(t-2)=0,
(y_gamma)_(t-1)=1                                      (1)
```

for every `gamma`.  Thus the direction vanishes on these coordinates.
The next `t` coordinates are necessarily affine functions

```text
(y_gamma)_(t-1+r)=ell_r(gamma)=a_r+gamma b_r,
1<=r<=t.                                                (2)
```

Let

```text
P={(gamma,c): Hc=y_gamma, wt(c)<=t},
Z={gamma:(gamma,c) in P for some c}.                    (3)
```

Then every pair has weight exactly `t`, there is at most one pair over
each slope, and the first `2t` rows canonically construct a monic locator
polynomial

```text
Q_gamma(X)=X^t-e_1(gamma)X^(t-1)+...+(-1)^t e_t(gamma), (4)
```

whose coefficient of elementary degree `j` has parameter degree at most
`j`.

Define the formal common domain-root set

```text
G={x in D: Q_z(x)=0 identically in F[z]},        g=|G|. (5)
```

If `Q_z` is nonconstant, put `h=t-g`.  Its residual locator

```text
R_z(X)=Q_z(X)/product_(x in G)(X-x)                     (6)
```

has `X`-degree `h` and parameter-curve degree at most `h`.  Consequently

```text
|P|=|Z| <= N-g <= N.                                    (7)
```

If `Q_z` is constant, then `|P|=|Z|<=1`, which also satisfies (7) whenever
`P` is nonempty.  Thus (7) holds in every case.

This is an all-pair statement.  It assumes neither transversality nor a
witness selector; common-support pairs are counted too.  It is independent
of the field size and valid in every characteristic.  For weighted GRS
parity columns `lambda_x h_x`, the diagonal change
`c(x)=lambda_x e(x)` gives the identical statement and preserves supports.

## Status and ownership

`PROVED / AUDIT`.  The accompanying Lean file contains explicitly labelled
`UNPROVED STATEMENT TARGETS`; it is not a Lean proof.

The result supplies a direct hard-input-3 ray payment on the entire
canonical Lagrange chart.  It is an automatic specialization of the
existing curve-degree consumer
`prop:curve-degree-ray-compiler`; the new content is the division-free
recognition that every line satisfying (1) has residual locator degree

```text
delta <= moving roots = t-g.                            (8)
```

The earlier positive-depth cyclotomic packet is the sharp `g=0` family:
for `t+1 | q-1`, `D=F_q^*`, and

```text
ell_1(gamma)=gamma,       ell_2=...=ell_t=0,
```

all `N=q-1` nonzero slopes occur.  Hence the universal factor `N` in (7)
cannot be improved on this chart.

For agreement `a=N-t` and kernel dimension `kappa=N-R`, the identity
depth is

```text
w=a-kappa-1=R-t-1>=t-1.                                 (9)
```

At `R=2t`, this is exactly the positive-depth `w=t-1` boundary realized by
the cyclotomic family.  When `R>2t`, the later syndrome coordinates only
prune the candidate locator parameters, so the same bound remains valid.

## Proof

### 1. Every sparse witness is the Lagrange error on a `t`-set

For a word `c`, let

```text
L_c(f)=sum_(x in D)c(x)f(x).
```

Equation (1) says that on polynomials of degree at most `t-1`,

```text
L_c(f)=[X^(t-1)]f.                                      (10)
```

Suppose `c` had support `T` of size `s<t`.  The monic degree-`t-1`
polynomial

```text
X^(t-1-s) product_(x in T)(X-x)
```

vanishes on `T`.  Its left side in (10) is zero while its right side is
one, a contradiction.  Hence every pair in (3) has support size exactly
`t`.

For a `t`-set `T`, the first `t` moment equations are a nonsingular
Vandermonde system.  Their unique solution is

```text
c_T(x)=1/Q'_T(x) on T,       c_T(x)=0 off T,
Q_T(X)=product_(x in T)(X-x).                            (11)
```

Lagrange coefficient extraction then gives

```text
L_(c_T)(X^(t-1+r))=h_r(T),       r>=0,                  (12)
```

where `h_r` is the complete homogeneous symmetric polynomial and
`h_0=1`.  Thus (2) forces

```text
h_r(T)=ell_r(gamma),              1<=r<=t.              (13)
```

### 2. The first `2t` moments determine one locator

Let `e_0=1` and define `e_j(z)` from the affine polynomials `ell_i(z)` by
the division-free recurrence

```text
e_j(z)=sum_(i=1)^j (-1)^(i-1)e_(j-i)(z)ell_i(z).        (14)
```

This is the coefficient identity

```text
(sum_(j>=0)(-1)^j e_j u^j)
(sum_(r>=0)h_r u^r)=1.
```

Induction in (14) gives

```text
deg_z e_j <= j.                                         (15)
```

For an actual pair, (13)--(14) identify these polynomials at `z=gamma`
with the elementary symmetric functions of `T`.  Therefore (4) specializes
to `Q_T`.

It follows at once that a slope has at most one weight-at-most-`t` error:
the first `2t` rows determine `Q_T`, its root set, and then the weights
(11).  Moreover, if two retained slopes had the same locator, their errors
would be equal, so

```text
(gamma-gamma')y_1=0.
```

Since `y_1!=0`, the slopes would be equal.  Thus the retained parameter
assignment is injective even if the full polynomial map `z -> Q_z` is not
generically one-to-one.

### 3. Removing fixed roots also removes their degree cost

Every factor `X-x` with `x in G` divides `Q_z` in `F[z][X]`.  The factors
are distinct and pairwise coprime, so their product divides, proving (6).
Write `G(X)=product_(x in G)(X-x)` and `h=t-g`.

Let `H_Q(u)`, `H_G(u)`, and `H_R(u)` denote the formal
complete-homogeneous generating series belonging to the three monic
locators.  Since `Q_z=G R_z`,

```text
H_Q(u)=H_G(u)H_R(u).
```

Therefore, for `0<=r<=h`,

```text
h_r(R_z)
 =sum_(j=0)^min(g,r) (-1)^j e_j(G) h_(r-j)(Q_z)
 =sum_(j=0)^min(g,r) (-1)^j e_j(G) ell_(r-j)(z),        (16)
```

where `ell_0=1`.  Every term on the right is affine in `z`.
Applying the same recurrence (14), now to `R_z`, shows that its elementary
coefficient of degree `j` has parameter degree at most `j`.  After
homogenizing at the actual maximum coefficient degree, (6) defines a
rational parameter curve of degree

```text
delta<=h.                                               (17)
```

This fixed-factor calculation is the point that sharpens the coarse
`delta<=t` estimate.  The degree falls in lockstep with the number of
moving roots.

### 4. Moving-root double count

Assume first that `Q_z` is nonconstant.  Then `h>0`.  Every retained
`R_gamma` has exactly `h` distinct roots in `D\G`.  For a fixed
`x in D\G`, the evaluation `R_z(x)` is a nonzero polynomial in `z` of
degree at most `h`, so it vanishes at at most `h` field elements.
Counting the incidences

```text
{(gamma,x): gamma in Z, x in D\G, R_gamma(x)=0}
```

in the two orders gives

```text
|Z|h <= (N-g)h.
```

Division by `h` proves (7).  This is also exactly the existing
curve-degree compiler with `delta/h<=1`.

If `Q_z` is constant and no pair is retained, there is nothing to prove.
Otherwise its `t` roots and its Lagrange weights give one fixed error `c`.
The equation

```text
Hc=y_0+gamma y_1
```

has at most one solution because `y_1!=0`.  In this nonempty case all
`t` roots lie in `D`, so `g=t`; since `N>=R>=2t`,
`1<=N-g`.  This completes every edge case.

## Relation to existing threshold theorems

This theorem is deliberately narrower than an arbitrary-line MCA theorem.
Its hypothesis is the literal normalization (1), not a conclusion of the
first-match atlas.

- For `R>=3t`, the repository's deep exact theorem gives a stronger general
  bound, so (7) is mainly a structural crosscheck there.
- The useful new strip is `2t<=R<3t`, where the deep theorem is unavailable
  and the quadratic exact condition `t^2>=N(3t-R)` can fail badly.
- At `R=2t`, the cyclotomic family proves that `N` actual pairs can occur,
  even with perfect positive-depth prefix fibers.  The curve compiler, not a
  constant-one profile shortcut, owns them.
- The theorem does not prove that primitive first-match witnesses land in
  this normalization, that there are subexponentially many such charts, or
  that any deployed threshold row moves.

Thus this packet closes one concrete positive-depth LineRay chart and names
the exact remaining bridge: atlas/profile structure must place the unpaid
witnesses into canonical Lagrange charts (or into another already paid
compiler).

## Verification

The stdlib-only verifier and exact pinned certificate are

```text
experimental/scripts/verify_canonical_lagrange_curve_compiler.py
experimental/data/certificates/canonical-lagrange-curve-compiler/canonical_lagrange_curve_compiler.json
```

The verifier recomputes:

- every nonconstant affine tuple `(ell_1,...,ell_t)` in five complete grids,
  including characteristic two and totaling `120266` locator families;
- `840628` finite-field parameter specializations and `838570`
  nonfixed-coordinate root-capacity checks;
- `92068` actual split-locator parameters;
- `2058` nonconstant families with a formal fixed domain root, checking the
  residual degree drop and `N-g` bound rather than only the `g=0` branch;
- a constant-locator line whose later syndrome row leaves exactly one pair;
  and
- five cyclotomic fixtures totaling `76` pairs, each attaining `|P|=N`.

Run

```bash
python3 experimental/scripts/verify_canonical_lagrange_curve_compiler.py --check
python3 experimental/scripts/verify_canonical_lagrange_curve_compiler.py --tamper-selftest
python3 -O experimental/scripts/verify_canonical_lagrange_curve_compiler.py --check
python3 -O experimental/scripts/verify_canonical_lagrange_curve_compiler.py --tamper-selftest
```

The certificate is recomputed exactly and protected by a SHA-256 payload
digest.  The tamper self-test changes five independent fields and requires
all five corruptions to be rejected.
