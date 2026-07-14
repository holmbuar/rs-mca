# Generic-rank deflation for half-distance LineRays

## Theorem

Let `F` be any field, let `D subset F` contain `N` distinct points,
and choose nonzero column weights `lambda_x`.  For `N>=R` use the
weighted moment parity columns

```text
h_x=lambda_x(1,x,...,x^(R-1))^T,       x in D.          (1)
```

Fix `t>=1` with

```text
R>=2t,                                                    (2)
```

and an affine syndrome line `y_z=y_0+z y_1` with `y_1!=0`.  For
`E subset D` write `V_E=span{h_x:x in E}`, and let

```text
P={(gamma,c):
     Hc=y_gamma, wt(c)<=t,
     {y_0,y_1} not subset V_supp(c)}.                    (3)
```

Write the moment coordinates of the line as

```text
m_j(z)=(y_0)_j+z(y_1)_j,          0<=j<R,
```

form the leading `t x t` Hankel pencil

```text
K_t(z)=(m_(i+j)(z))_(0<=i,j<t),
```

and put

```text
rho=rank_(F(z)) K_t(z).                                  (4)
```

Then the complete transverse pair family satisfies

```text
|P|=|{gamma:(gamma,c) in P}|
   <= N+rho
   <= N+t.                                                (5)
```

More precisely, all weights larger than `rho` are absent, all weights
strictly smaller than `rho` together contribute at most `rho` pairs,
and the exact-weight-`rho` stratum contributes at most `N`.  If its
primitive locator has `g` formal fixed domain roots, the last charge
sharpens to `N-g`.

For `C=RS_F(D,N-R)` and agreement `a=N-t`, the exact
syndrome--secant correspondence gives

```text
B_C^MCA(a) <= N+rho <= N+t,
B_C^CA(a)  <= N+rho <= N+t.                              (6)
```

The same inequalities hold after restricting slopes to any challenge set.
They are field-independent, characteristic-free, and require neither a
witness selector nor a multiplicative evaluation domain.

## Status

`PROVED / AUDIT`.  The accompanying Lean module contains explicitly
labelled `UNPROVED STATEMENT TARGETS`; it is not a Lean proof.

This packet strictly sharpens the predecessor
`half_distance_hankel_curve_lineray.md`, whose safe all-weight sum was
`1+Nt(t+1)/2`.  The improvement comes from two global facts that were not
used there: one generic-rank minor pays every lower-weight parameter at once,
and formal fixed roots can be annihilated before compiling the top-weight
locator.  The endpoint `R=2t` is included.

In the strict range `2t<R`, the BCHKS theorem already imported by
`experimental/rs_mca_thresholds.tex` is substantially stronger under its
stated hypotheses and often gives the exact `t+1` staircase.  No priority
or improvement over that result is claimed.

## Proof

### 1. Actual support size is exactly Hankel rank

Take a pair `(gamma,c) in P` of exact weight `s`, with support
`T`.  Put `w_x=lambda_x c(x)`; every `w_x` is nonzero.  The specialized
leading Hankel matrix factors as

```text
K_t(gamma)=V_t(T)^T diag(w_x:x in T) V_t(T),             (7)
```

where `V_t(T)` is the `s x t` matrix with columns
`1,x,...,x^(t-1)`.  Since `s<=t`, this Vandermonde matrix has row rank
`s`.  It is a surjection `F^t -> F^s`; its transpose is an injection
`F^s -> F^t`; and the diagonal middle map is invertible.  Consequently

```text
rank K_t(gamma)=s.                                       (8)
```

Specialization cannot increase rational-function rank.  Equations (4) and
(8) therefore imply `s<=rho`, so no larger weight occurs.

### 2. One minor pays every lower weight

If `rho>0`, choose any nonzero `rho x rho` minor
`Delta(z)` of `K_t(z)`.  Each matrix entry is affine in `z`, hence

```text
deg Delta<=rho.                                          (9)
```

Every selected pair of weight `s<rho` has
`rank K_t(gamma)=s<rho` by (8), so `Delta(gamma)=0`.
This includes the zero error, whose Hankel matrix has rank zero.

There cannot be two pairs in `P` at one parameter: their difference would
be a kernel word of weight at most `2t<=R`, whereas every nonzero word in
the weighted Vandermonde kernel has weight at least `R+1`.  Thus the root
count in (9) gives the single global charge

```text
|{(gamma,c) in P:wt(c)<rho}|<=rho.                       (10)
```

When `rho=0`, (8) permits only the zero error.  Since `y_1!=0\), it can
occur at at most one parameter.

### 3. Compile the top-weight locator

Assume the exact-weight-`rho` stratum is nonempty.  The first `2rho`
moments exist because `rho<=t` and `R>=2t`.  Form the
`rho x (rho+1)` recurrence pencil

```text
M_rho(z)=(m_(r+i)(z))_(0<=r<rho, 0<=i<=rho).             (11)
```

Its signed maximal cofactors give a projective locator
`L(z,X)`.  At every actual top-weight parameter the square
Vandermonde/amplitude factorization gives full row rank, so the cofactor
vector is nonzero and recovers exactly

```text
Q_T(X)=product_(x in T)(X-x).                            (12)
```

Removing the polynomial gcd of the cofactors makes `L` primitive without
losing a selected parameter.

Let

```text
Gset={x in D:L(z,x)=0 identically in F[z]},
g=|Gset|,
G(X)=product_(x in Gset)(X-x).                           (13)
```

Every selected top-weight support contains `Gset`.  If `g=rho`, the
support is fixed, and transversality permits at most one selected parameter.
Since `N>=2t>=2rho`, this already obeys the desired `N-g` charge.

It remains to handle `g<rho`.

### 4. Annihilate fixed atoms before taking cofactors

Write `G(X)=sum_(j=0)^g G_j X^j` and define transformed affine moments

```text
n_r(z)=sum_(j=0)^g G_j m_(r+j)(z).                       (14)
```

At a selected parameter with support `T`, the moment representation gives

```text
n_r(gamma)
 =sum_(x in T) w_x G(x)x^r
 =sum_(x in T\\Gset) w_x G(x)x^r.                       (15)
```

Every remaining amplitude is nonzero.  Put `h=rho-g`.  The
`h x (h+1)` Hankel pencil built from the first `2h` transformed moments
therefore has full row rank `h` at every selected top-weight parameter.
Its primitive cofactor locator has parameter degree at most `h` and
recovers exactly the residual locator

```text
Q_(T\\Gset)(X).                                          (16)
```

There are enough source moments: the largest index used in (14) is
`2h-1+g=2rho-g-1<2rho<=R`.

The residual generic rank is `h` because it is `h` at one selected
specialization.  Hence its generic kernel is one-dimensional.  The quotient
`L/G` lies in that kernel, so it agrees projectively with the residual
cofactor curve over `F(z)`.  In particular the residual family has no
formal domain root outside `Gset`; otherwise the original primitive
locator would have had another formal root.

### 5. Moving-root payment after deflation

Each selected residual locator has `h` domain roots and no formal fixed
one.  For each `x in D\\Gset`, its evaluation at `x` is a nonzero
polynomial in `z` of degree at most `h`.  Double-counting root
incidences gives

```text
|P_rho| h <= (N-g)h,
|P_rho|   <= N-g <= N.                                  (17)
```

Combining (10) and (17) proves `|P|<=N+rho`.  The
`rho=0` case was already bounded by one, and `N>=2`, so (5) holds in
all cases.

Transversality is also what makes the locator assignment injective: if two
different parameters used one support `T`, subtraction would place
`y_1` in `V_T`, and then `y_0` in `V_T`, contradicting (3).

### 6. MCA and CA conversion

For a received RS line, apply the parity check to obtain the syndrome line.
If `y_1=0`, every close support contains both syndrome directions, so no
MCA- or CA-bad slope occurs.  Otherwise, an MCA-bad explanation supplies
exactly a transverse pair in (3).  A CA-bad explanation does too, since a
common syndrome support would lift to a common codeword support.  Equation
(6) follows from (5).

## Endpoint calibration

At `R=2t`, the positive-depth cyclotomic family from
`positive_depth_cyclotomic_lineray_curve.md` has

```text
D=F_q^*,       t+1 divides q-1,       |P_t|=N=q-1.
```

For that family `rho=t`, the rank minor is a nonzero constant, there are
no lower-weight pairs, and the deflated degree is `t` with no fixed root.
Thus the top-weight `N` charge is attained exactly.  Linear dependence on
`N` at the endpoint is unavoidable, while the additive `rho` allowance
for rank-drop parameters is not asserted to be sharp.

## Verification

The stdlib-only verifier and pinned certificate are

```text
experimental/scripts/verify_half_distance_generic_rank_deflation.py
experimental/data/certificates/half-distance-generic-rank-deflation/half_distance_generic_rank_deflation.json
```

The verifier independently recomputes:

- all `293918` affine syndrome lines in five complete prime-field grids,
  including characteristic two, a proper evaluation subdomain, and
  `t in {1,2}`;
- `494285` exhaustive transverse pair incidences and `32182`
  lower-weight selected parameters;
- `284067` nonempty deflation families and `4860` families with formal
  fixed roots, checking transformed-moment annihilation, residual locator
  recovery, quotient agreement, degree, and root capacity;
- `16000` deterministic weighted-GRS `t=3` lines at `R=2t` and
  `R=2t+1`, with `27247` transverse pair incidences;
- the rank identity `rank K_t(gamma)=wt(c)` at every selected pair; and
- the sharp 12-pair cyclotomic fixture over `F_13^*`.

The maximum observed pair count in every exhaustive and sampled grid was at
most `N`, stronger than the certified theorem but not promoted as a claim.

Run

```bash
python3 experimental/scripts/verify_half_distance_generic_rank_deflation.py --check
python3 experimental/scripts/verify_half_distance_generic_rank_deflation.py --tamper-selftest
python3 -O experimental/scripts/verify_half_distance_generic_rank_deflation.py --check
python3 -O experimental/scripts/verify_half_distance_generic_rank_deflation.py --tamper-selftest
```

The certificate is an exact recomputation with a SHA-256 payload digest.
The tamper self-test must reject every independent corruption in both normal
and optimized Python modes.

## Nonclaims

- No universal `N` upper bound is claimed; the additive rank-drop charge
  may be real even though it was absent from the searched grids.
- No exact endpoint numerator is claimed.
- No improvement over BCHKS is claimed in its strict `2t<R` range.
- No bound is proved for `R<2t`.
- No atlas, profile-envelope, primitive-survival, or deployed-row movement
  follows from this packet.
- The Lean file records interfaces only and is not a formal proof.
