# Positive-depth cyclotomic LineRay curve: perfect fibers, sharp RC

## Claim

Let `F=F_q`, choose an integer `t>=2`, and assume

```text
t+1 divides q-1,                 N=q-1>=2t+2.
```

Put `D=F^*`, let `mu=mu_(t+1) subset F^*`, and use the `2t` moment
columns

```text
h_x=(1,x,...,x^(2t-1))^T,        x in D.
```

Their kernel is a generalized Reed--Solomon code.  For the standard
weighted parity columns `lambda_x h_x` of ordinary RS, replace every error
coordinate below by `c(x)/lambda_x`.  This nonzero diagonal rescaling
preserves supports, slopes, puncture clusters, and every count in the
claim.

Write `y_0=e_(t-1)` and `y_1=e_t`, with coordinates numbered from zero.
Then the complete set of weight-at-most-`t` syndrome-line pairs

```text
P={(gamma,c): Hc=y_0+gamma y_1, wt(c)<=t}
```

is exactly the `N=q-1` pairs indexed by `gamma in F^*`:

```text
T_gamma=-gamma(mu\{1}),
c_gamma(x)=1/Q'_(T_gamma)(x) on T_gamma, and 0 off T_gamma.       (1)
```

Every pair is transverse, every error has weight exactly `t`, and all
slopes are distinct.  The agreement is `a=N-t`, the kernel dimension is
`kappa=N-2t`, and the identity depth is

```text
w=a-kappa-1=t-1.                                                (2)
```

For the agreement supports `A_gamma=D\T_gamma`,

```text
Phi_(t-1)(A_gamma)=(gamma,0,...,0).                             (3)
```

Consequently this realized support slice has mass `N`, image size `N`,
maximum fiber one, and image-normalized scale one.  Its Q-style max-fiber
data are perfectly flat, but its exact slope/profile ratio is `N`.
Support injection plus max-fiber flatness therefore does not give a
constant-one positive-depth ray payment, even in GRS/RS-equivalent geometry.

The same family is a rational-normal locator curve of degree `t`.  Each
parameter has exactly `t` moving roots and each domain point occurs at
exactly `t` parameters, so the curve ray compiler gives

```text
|P|=|slopes|=N*t/t=N,                                          (4)
```

with equality.  Thus the family is paid by the existing curve branch with
a sharp linear factor.

## Status

`PROVED / COUNTEREXAMPLE / AUDIT` under the displayed finite-field
hypotheses.  The counterexample is only to a constant-one
`Q + support injection => RC` shortcut.  It is not a counterexample to the
printed compiler, which keeps Q and RC separate and permits a
subexponential curve loss.

The accompanying Lean file contains `UNPROVED STATEMENT TARGETS`; it is not
a Lean proof.

## Existing dependencies and credit

- `selector_free_exact_weight_all_pair.md` supplies the complete-pair
  exact-weight residual and its `R=t+1` depth-zero route cut.
- `depth_zero_identity_lineray_owner.md` proves that the preceding route cut
  is owned at constant one when the identity image has size one.
- `experimental/asymptotic_rs_mca_frontiers.tex`,
  `prop:curve-degree-ray-compiler` and
  `cor:automatic-locator-curve-ray`, supply the curve-degree RC consumer.
  The latter explicitly permits a residual locator when the fixed profile
  data and that locator determine the exact support; here
  `A_gamma=D\T_gamma` does exactly that.
- The same paper's `prop:q-sp-no-ray` already proves abstractly that Q and SP
  do not determine a ray image.  The construction here is an actual
  positive-depth GRS (and diagonally equivalent ordinary-RS) realization,
  not a relabelled abstract incidence.

The Lagrange-weight route-cut mechanism is due to Danny
(DannyExperiments).  The selector-free pair and realized-puncture interfaces
are due to Latif Kasuli and holmbuar.  This note supplies the cyclotomic
higher-depth classification and the sharp rational-normal-curve owner.

## Proof

### 1. The Lagrange moment identity

For a `t`-set `T`, put

```text
Q_T(X)=product_(x in T)(X-x),
c_T(x)=1/Q'_T(x) on T, and 0 off T.
```

If `h_r(T)` is the complete homogeneous symmetric polynomial of degree
`r`, Lagrange coefficient extraction gives

```text
sum_(x in T) c_T(x)x^j =
  0                         for 0<=j<=t-2,
  1                         for j=t-1,
  h_(j-t+1)(T)              for j>=t.                       (5)
```

For

```text
T_1=-(mu\{1}),
```

the elementary symmetric functions are `e_j(T_1)=1` for `0<=j<=t`.
Indeed its locator is

```text
Q_(T_1)(X)=X^t-X^(t-1)+...+(-1)^t
          =(X^(t+1)+(-1)^t)/(X+1).                         (6)
```

The complete-homogeneous generating function is therefore

```text
sum_(r>=0) h_r(T_1)z^r
  =(1+z)/(1-(-z)^(t+1)).
```

Hence

```text
h_1(T_1)=1,             h_2(T_1)=...=h_t(T_1)=0.           (7)
```

Scaling by `gamma` gives `h_1(T_gamma)=gamma` and
`h_2(T_gamma)=...=h_t(T_gamma)=0`.  Equations (5)--(7) prove

```text
Hc_gamma=e_(t-1)+gamma e_t.
```

### 2. Classification of every weight-at-most-`t` pair

Suppose `Hc=y_0+gamma y_1` and `wt(c)<=t`, with support `T`.
If `|T|<t`, the first `|T|` zero moment equations form a square
Vandermonde system and force every nonzero coefficient of `c` to vanish,
contradicting the moment-one coordinate at degree `t-1`.  Thus `|T|=t`.

The first `t` moment equations now uniquely give the Lagrange weights in
(5).  The remaining equations say

```text
h_1(T)=gamma,            h_2(T)=...=h_t(T)=0.              (8)
```

The elementary/complete-homogeneous recurrence, which uses no division by
small integers, gives

```text
e_j(T)=gamma^j,           1<=j<=t.
```

Therefore

```text
Q_T(X)=X^t-gamma X^(t-1)+...+(-gamma)^t
      =(X^(t+1)+(-1)^t gamma^(t+1))/(X+gamma).             (9)
```

There is no squarefree `t`-set for `gamma=0`.  For `gamma!=0`, (9) has
the `t` distinct roots `-gamma(mu\{1})`, because `t+1` divides `q-1`.
This proves the exact classification (1) and the count `|P|=q-1`.

Projection to the first `t` rows also shows that `y_1=e_t` is not in the
column span of any `T_gamma`: zero moments through degree `t-1` force all
`t` coefficients to vanish before the degree-`t` coordinate can equal one.
Thus every retained pair is transverse.

### 3. Positive-depth identity profile

The Vandermonde kernel is an
`[N,N-2t,2t+1]` generalized Reed--Solomon code, so

```text
kappa=N-2t,       a=N-t,       w=a-kappa-1=t-1.
```

Since `D=F^*`, `Q_D(X)=X^N-1`; all of its coefficients immediately below
the leading term vanish.  From

```text
Q_D=Q_(A_gamma)Q_(T_gamma)
```

and the coefficients in (9), recursive coefficient comparison gives

```text
c_1(A_gamma)=gamma,
c_2(A_gamma)=...=c_(t-1)(A_gamma)=0.
```

This proves (3).  The prefix is an injective function of the slope, so on
this curve slice

```text
support mass=N,       realized image=N,
max fiber=1,          barN_img=1,          slopes=N.       (10)
```

Equation (10) is the exact positive-depth obstruction to a constant-one
support-fiber shortcut.  The missing factor is realized boundary-image
occupancy.

### 4. The selector-free weighted puncture budget is sharp

Let `J=mu` and put

```text
v(x)=1/Q'_J(x) on J, and 0 off J.
```

The locator `Q_J=X^(t+1)-1` has vanishing elementary coefficients through
degree `t`, so (5), now for a `(t+1)`-set, gives `Hv=e_t=y_1`.
No support of size at most `t` can lift `y_1`, by the same Vandermonde
argument.  Hence the minimum-lift weight is

```text
d=t+1.                                                       (11)
```

Exactly the `t+1` slopes `gamma in -mu` have
`T_gamma=J\{-gamma}`.  Their realized punctured word is zero, and they
form one cluster of size `t+1`.  Every other `T_gamma` lies in a
multiplicative `mu`-coset disjoint from `J`; its realized word has weight
`t`, and those words are distinct.  Thus

```text
|W_P|=N-t,
cluster sizes=(t+1,1,...,1),

sum_(w in W_P) floor(d/max(1,d+wt(w)-t))
  =(t+1)+(N-t-1)=N=|P|.                                  (12)
```

So the exact selector-free weighted-puncture bound is attained globally,
not only on one local cluster.

### 5. Sharp rational-normal-curve payment

The error locators form the projective rational normal curve

```text
[s:u] -> [s^t,-s^(t-1)u,s^(t-2)u^2,...,(-u)^t] in P^t.    (13)
```

Its pullback hyperplane degree is `delta=t`.  There is no common root.
For a fixed `x in D`, the condition `x in T_gamma` has exactly `t`
solutions in `gamma`, and each selected parameter has exactly `t` roots
in `D`.  The moving-root incidence count is therefore exactly

```text
N*t=|slopes|*t.
```

The curve-degree ray compiler gives (4) with equality.  This is the
correct positive-depth owner of (10).

### 6. The exact-weight double-negative stratum is real

With the fixed minimum lift `J`, the family has only two exact punctured
weights:

```text
|P_0|=t+1,               |P_t|=N-t-1.
```

For the `j=t` stratum, put

```text
M=N-t-1,       d=t+1,       Delta=t.
```

The two exact-weight denominators of
`selector_free_exact_weight_all_pair.md` satisfy

```text
Q_t=t^2-(t-1)M=2t^2-1-(t-1)N,
Xi_t=(t+1)Q_t.                                             (14)
```

Hence, whenever

```text
N(t-1)>2t^2-1,
```

both denominators are strictly negative while the stratum has
`N-t-1` genuine pairs.  Equation (4), not either spherical denominator,
pays it.  This is a positive-depth route classification rather than a
claim that the residual is exponential.

## Reproducibility

Run

```bash
python3 experimental/scripts/verify_positive_depth_cyclotomic_lineray_curve.py --check
python3 -O experimental/scripts/verify_positive_depth_cyclotomic_lineray_curve.py --check
python3 experimental/scripts/verify_positive_depth_cyclotomic_lineray_curve.py --tamper-selftest
python3 -m json.tool experimental/data/certificates/positive-depth-cyclotomic-lineray-curve/positive_depth_cyclotomic_lineray_curve.json
```

The verifier checks a 558-row symbolic parameter grid, constructs seven
prime-field families, recomputes every Lagrange syndrome, complement
prefix, curve/root incidence, puncture cluster, and exact denominator, and
exhausts every `t`-support in four small fixtures to confirm completeness.

The Lean statement surface is

```text
experimental/lean/grande_finale/GrandeFinale/PositiveDepthCyclotomicLineRayCurve.lean
```

## Ledger impact and nonclaims

This serves hard input 3 on an explicit positive-depth family.  It proves
that:

- depth zero is special because its realized identity image is a singleton;
- at positive depth, actual GRS/diagonally equivalent RS support injection and
  perfect image-normalized fibers can still lose the full realized image size;
- the printed rational-curve RC mechanism recovers that factor exactly; and
- the selector-free weighted-puncture inequality can be globally sharp on
  the same family.

It does **not**:

- claim that this cyclotomic curve survives primitive first-match routing;
- refute Q, SP, RC, or the printed conditional compiler;
- prove an exhaustive atlas or pay higher-dimensional balanced cores;
- prove a row-sharp MI/MA, Sidon, or full profile-envelope comparison;
- move a deployed finite row or change stable paper TeX/PDF; or
- claim Lean certification.
