# Half-distance Hankel curve compiler for every transverse LineRay

## Theorem

Let `F` be any field, let `D subset F` contain `N` distinct points, and
choose nonzero column weights `lambda_x`.  For `N>=R` use the weighted
moment parity columns

```text
h_x=lambda_x(1,x,...,x^(R-1))^T,       x in D.          (1)
```

Fix `t>=1` with

```text
R>=2t,                                                    (2)
```

and a syndrome line `y_gamma=y_0+gamma y_1` with `y_1!=0`.  For
`E subset D` write `V_E=span{h_x:x in E}`.  Let

```text
P={(gamma,c):
     Hc=y_gamma, wt(c)<=t,
     {y_0,y_1} not subset V_supp(c)}.                    (3)
```

Thus `P` is the complete set of transverse sparse syndrome pairs; no
witness selector is used.  Put

```text
P_s={(gamma,c) in P:wt(c)=s}.
```

Then

```text
|P_0| <= 1,
|P_s| <= N*s                    for 1<=s<=t,             (4)

|P| = |{gamma:(gamma,c) in P}|
    <= 1 + N*t*(t+1)/2.                                  (5)
```

The equality in (5) says that same-slope multiplicity cannot occur in the
half-distance range.  The theorem is field-independent, characteristic-free,
and valid for every evaluation domain, not only a multiplicative subgroup.

For `C=RS_F(D,N-R)` and agreement `a=N-t`, the exact
syndrome--secant correspondence gives the direct corollary

```text
B_C^MCA(a) <= 1 + N*t*(t+1)/2,
B_C^CA(a)  <= 1 + N*t*(t+1)/2.                          (6)
```

The same inequalities hold after restricting slopes to any challenge set.

## Status

`PROVED / AUDIT`.  The accompanying Lean module contains explicitly
labelled `UNPROVED STATEMENT TARGETS`; it is not a Lean proof.

This is a hard-input-3 direct ray compiler at and below half the RS
minimum-distance redundancy.  Its new endpoint is `R=2t`.  In the strict
range `2t<R`, the BCHKS theorem already imported by
`experimental/rs_mca_thresholds.tex` is substantially stronger under its
stated hypotheses and often gives the exact `t+1` staircase.  No priority is
claimed over that result.

The repository's SPI deficiency-one packets already develop cofactor and
pseudo-remainder routes for the exact top-weight chart on root-of-unity
domains.  The present proof is a different closure: the actual-error
amplitude guard rules out cofactor rank-drop at every exact weight, and the
generic curve compiler counts the remaining split locators on arbitrary
domains.  Summing over all weights gives (5).

## Proof

### 1. Half distance removes same-slope multiplicity

Every nonzero word in the kernel of the weighted matrix (1) has weight at
least `R+1` by the Vandermonde/MDS property; when `R=N` the kernel is
zero.  If two pairs in `P` had the same slope, their error difference
would be a kernel word of weight at most

```text
2t<=R.
```

It must therefore be zero.  The errors, and hence the pairs, are equal.
This proves the pair/slope equality in (5).

The zero error can occur only when `y_0+gamma y_1=0`.  Since `y_1!=0`,
there is at most one such parameter, proving the first line of (4).

### 2. Every actual exact-weight moment Hankel matrix has full row rank

Fix `1<=s<=t`.  Write the coordinates of the syndrome line as affine
moment polynomials

```text
m_j(z)=(y_0)_j+z(y_1)_j,          0<=j<R.
```

The first `2s` coordinates exist by (2).  Form the `s x (s+1)` Hankel
pencil

```text
M_s(z)=(m_(r+i)(z))_(0<=r<s, 0<=i<=s).                  (7)
```

Take an actual pair `(gamma,c) in P_s` with support
`T={x_1,...,x_s}`, and put `w_x=lambda_x c(x)`.  Every `w_x` is nonzero.
At `z=gamma`, (7) has the exact factorization

```text
M_s(gamma)
  =V_s(T)^T diag(w_x:x in T) V_(s+1)(T),                (8)
```

where `V_d(T)` has rows indexed by `T` and columns `1,x,...,x^(d-1)`.
The first Vandermonde matrix in (8) is square and invertible, the diagonal
matrix is invertible, and `V_(s+1)(T)` has row rank `s`.  Hence

```text
rank M_s(gamma)=s.                                      (9)
```

This simple amplitude-rank fact is important: an actual exact-weight
witness can never occur on the rank-drop locus of its square Hankel chart.
Rank tests without the nonzero-amplitude guard do not have this conclusion.

### 3. Cofactors give a degree-at-most-`s` locator curve

For `0<=i<=s` let

```text
C_(s,i)(z)=(-1)^i det(M_s(z) with column i deleted),
L_s(z,X)=sum_(i=0)^s C_(s,i)(z)X^i.                    (10)
```

The signed cofactor vector lies in the kernel of `M_s(z)`.  Every entry of
the determinant is affine in `z`, so

```text
deg_z C_(s,i)<=s.                                       (11)
```

If all cofactors vanish identically, `M_s` has generic rank below `s`;
by (9), `P_s` is empty.  Otherwise divide all nonzero cofactors by their
common polynomial gcd.  This removes every finite base point and gives a
primitive projective locator family of parameter degree

```text
delta_s<=s.                                             (12)
```

At an actual pair, (9) says the kernel is one-dimensional.  The error
locator

```text
Q_T(X)=product_(x in T)(X-x)
```

lies in that kernel by the moment recurrence.  Therefore `L_s(gamma,X)`
is a nonzero scalar multiple of `Q_T`.  In particular its top coefficient
does not vanish at a selected parameter, and the cofactor curve recovers the
exact support rather than only a necessary annihilator.

### 4. Transversality makes the locator assignment injective

Suppose two distinct parameters `gamma!=gamma'` in `P_s` had the same
support `T`.  Both syndrome points lie in `V_T`, so subtraction gives

```text
(gamma-gamma')y_1 in V_T.
```

Thus `y_1 in V_T`, and then
`y_0=y_gamma-gamma y_1 in V_T`.  This contradicts the transverse clause
in (3).  Hence the selected parameter-to-locator assignment is injective.

This is exactly why the hypothesis in (3) is necessary.  A line contained
in one `V_T` can have a fixed support at every field parameter.  Such a
common-support line is paid before the residual LineRay compiler; its
lower-weight amplitude-cancellation parameters may remain as the familiar
tangent ratios and are counted in their own `P_s` strata.

### 5. Moving-root payment

For the primitive locator family in (10), define its formal common domain
roots

```text
G_s={x in D:L_s(z,x)=0 identically in F[z]},
g_s=|G_s|.                                               (13)
```

Every selected exact-`s` locator contains these roots.  If `g_s<s`, each
selected support supplies `s-g_s` moving-root incidences.  For a fixed
`x in D\G_s`, the nonzero polynomial `L_s(z,x)` has degree at most
`delta_s`, so it vanishes at at most `delta_s` parameters.  Double counting
gives the sharper chart bound

```text
|P_s|(s-g_s) <= (N-g_s)delta_s.                          (14)
```

Using `delta_s<=s` and `s-g_s>=1` yields

```text
|P_s| <= (N-g_s)s/(s-g_s) <= N*s.                       (15)
```

If `g_s=s`, the degree-`s` locator has all its roots fixed and the support
is constant.  Transversality then permits at most one selected parameter,
which also satisfies `|P_s|<=Ns`.  This proves (4), and summing
`1+sum_(s=1)^t Ns` proves (5).

Equations (12)--(14) are a direct instance of the existing
`prop:curve-degree-ray-compiler`.  The proof above spells out the elementary
root-incidence count so that no projective-geometry assumption is hidden.

### 6. MCA and CA conversion

For a received RS line `r_0+gamma r_1`, apply the parity check to get
`y_i=Hr_i`.  An explanation at agreement at least `N-t` gives an error
`c` of weight at most `t` with `Hc=y_0+gamma y_1`.

If `y_1=0`, any such error has `y_0 in V_supp(c)`, and of course
`y_1 in V_supp(c)`.  Thus every close support is common and there are no
MCA- or CA-bad slopes.  Otherwise `y_1!=0` and the theorem applies.

For MCA, failure to explain the received pair on the same support is
equivalent to

```text
{y_0,y_1} not subset V_supp(c).
```

Thus every MCA-bad slope appears in (3).  For CA, a column-far pair cannot
have `y_0,y_1 in V_supp(c)`, because those two lifts would give a common
support of size at least `N-t`.  Hence every CA-bad slope also appears in
(3).  Equation (6) follows.

## Endpoint calibration and sharp lower scale

At the exact endpoint `R=2t`, the positive-depth cyclotomic family from
`positive_depth_cyclotomic_lineray_curve.md` has

```text
D=F_q^*,       t+1 divides q-1,
|P_t|=N=q-1.
```

Its degree-`t` cofactor locator curve has no fixed roots and exactly
`Nt` root incidences, so (14) returns `N` with equality on that chart.
Therefore the endpoint cannot have a universal constant or `t+1`
numerator: linear dependence on `N` is genuinely necessary.  The present
upper bound leaves a polynomial factor gap, at most `t` on one exact-weight
stratum and `Theta(t^2)` after the safe all-weight sum.

This also explains the boundary with prior work:

- the imported BCHKS completion assumes the strict inequality `2t<R`;
- at `R=2t` its denominator `R-2t` vanishes and the exact `t+1` staircase
  can fail by the cyclotomic `N`-pair family;
- the cofactor curve still supplies a field-independent polynomial endpoint
  payment; and
- nothing here applies when `R<2t`, the genuinely beyond-half-distance
  residual band.

## Verification

The stdlib-only verifier and pinned certificate are

```text
experimental/scripts/verify_half_distance_hankel_curve_lineray.py
experimental/data/certificates/half-distance-hankel-curve-lineray/half_distance_hankel_curve_lineray.json
```

It recomputes:

- every affine syndrome line in five complete prime-field grids, including
  characteristic two, a proper evaluation subdomain, and `t in {1,2}`:
  `293918` lines total;
- `494285` actual transverse pair incidences on those lines;
- `284216` nonempty exact-weight cofactor families, with locator recovery,
  amplitude-rank nonvanishing, content removal, support injectivity, and
  moving-root capacity checked independently;
- `4855` nonconstant families with formal fixed domain roots;
- `16000` deterministic weighted-GRS `t=3` lines at `R=2t` and
  `R=2t+1`, totaling `27216` additional transverse incidences;
- the sharp cyclotomic endpoint with `12` pairs and `36` root incidences;
  and
- a fully sparse common-support line whose five full-support parameters are
  rejected while its two lower-weight tangent ratios are retained.

Run

```bash
python3 experimental/scripts/verify_half_distance_hankel_curve_lineray.py --check
python3 experimental/scripts/verify_half_distance_hankel_curve_lineray.py --tamper-selftest
python3 -O experimental/scripts/verify_half_distance_hankel_curve_lineray.py --check
python3 -O experimental/scripts/verify_half_distance_hankel_curve_lineray.py --tamper-selftest
```

The certificate is an exact recomputation with a SHA-256 payload digest.
The tamper self-test changes six independent fields and requires all six
corruptions to be rejected.

## Nonclaims

- No exact endpoint numerator is claimed beyond (4)--(5).
- No improvement over BCHKS is claimed in its strict half-distance range.
- No bound is proved for `R<2t`.
- No atlas, profile-envelope, primitive-survival, or deployed-row movement
  follows from this packet.
- The Lean file records interfaces only and is not a formal proof.
