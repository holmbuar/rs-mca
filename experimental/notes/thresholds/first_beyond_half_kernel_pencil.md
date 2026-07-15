# The first beyond-half-distance kernel-pencil compiler

## Theorem

Let `F` be any field, let `D subset F` contain `N` distinct points, and
choose nonzero column weights `lambda_x`.  Use the weighted moment parity
columns

```text
h_x=lambda_x(1,x,...,x^(R-1))^T,       x in D.          (1)
```

Fix `t>=2` at the first slice beyond the half-distance moment window:

```text
N>=R=2t-1.                                               (2)
```

Let `y_z=y_0+z y_1` be a nonconstant syndrome line.  For
`E subset D` put `V_E=span{h_x:x in E}`, and retain every distinct
transverse pair

```text
P={(gamma,c):
     Hc=y_gamma, wt(c)<=t,
     {y_0,y_1} not subset V_supp(c)}.                    (3)
```

No slope or witness selector is applied.  Write `P_t` for the exact-weight
`t` stratum and `P_<t` for all smaller weights.  Let `rho` be the generic
rank over `F(z)` of the leading `(t-1) x (t-1)` Hankel pencil.  Then

```text
|P_t|  <= binom(N,2),                                    (4)
|P_<t| <= N+rho <= N+t-1,                                (5)

|P| <= binom(N,2)+N+rho
    <= binom(N+1,2)+t-1.                                 (6)
```

The top bound (4) counts every `(slope,error)` pair, including multiple
errors at one slope.  Consequently the number of distinct retained slopes is
bounded by the same right-hand side.

For `C=RS_F(D,N-R)` and agreement `a=N-t`, the exact
syndrome--secant correspondence gives

```text
B_C^MCA(a) <= binom(N+1,2)+t-1,
B_C^CA(a)  <= binom(N+1,2)+t-1.                          (7)
```

The same bounds hold after restricting slopes to any challenge set.  They are
field-independent, characteristic-free, and valid on arbitrary evaluation
domains.

When `t=1` and `R=1`, no nonzero weight-one support is transverse because
one nonzero parity column spans the one-dimensional syndrome space.  Only the
zero error can remain, at at most one parameter.  Thus (6) is still a valid
coarse bound, with the sharper value `|P|<=1`.

## Status

`PROVED / AUDIT`.  The accompanying Lean module contains explicitly labelled
`UNPROVED STATEMENT TARGETS`; it is not a Lean proof.

This is a direct hard-input-3 compiler at the first genuinely
underdetermined moment slice.  The preceding half-distance packet applies to
`R>=2t`.  Here the degree-`t` recurrence pencil has a two-dimensional generic
kernel, so a single cofactor locator no longer exists.  Pair determinants in
that kernel replace it and give the quadratic payment (4).

The result is complementary to the repository's general fixed-kernel and
balanced-core payments.  Those charge an arbitrary kernel-dimension-two chart
by choosing evaluation pairs one at a time.  The present argument uses the
exact Hankel support rank and charges every good root pair of every retained
top locator; the factor `t-1` then cancels on both sides.

The published proximity-gap literature treats related affine-space questions
strictly below half the minimum distance.  Here the GRS distance is
`R+1=2t` and the error budget is exactly `t`.  This packet concerns the
repository's transverse complete-LineRay object at that boundary and makes no
priority claim over ordinary list-decoding or proximity-gap results.

## Proof

### 1. Lower weights fall back inside half distance

Put `u=t-1`.  Then

```text
2u=2t-2<R=2t-1.                                         (8)
```

The generic-rank deflation theorem from
`half_distance_generic_rank_deflation.md` applies verbatim to every retained
pair of weight at most `u`.  With `rho` as in the theorem statement, it gives

```text
|P_<t|<=N+rho<=N+t-1.                                   (9)
```

It also says that same-slope multiplicity is impossible in this lower
stratum: the difference of two such errors would be a nonzero GRS kernel word
of weight at most `2t-2<R+1`.

Only the exact top weight `t` remains.

### 2. The top recurrence kernel has dimension two

Write the moment coordinates of the line as

```text
m_j(z)=(y_0)_j+z(y_1)_j,          0<=j<2t-1.
```

Form the `(t-1) x (t+1)` Hankel recurrence pencil

```text
M(z)=(m_(r+i)(z))_(0<=r<t-1, 0<=i<=t).                  (10)
```

At an actual exact-weight-`t` pair with support `T` and nonzero weighted
amplitudes `w_x=lambda_x c(x)`,

```text
M(gamma)
 =V_(t-1)(T)^T diag(w_x:x in T) V_(t+1)(T).             (11)
```

The right Vandermonde matrix maps onto `F^T`, the diagonal map is invertible,
and the left matrix maps `F^T` onto `F^(t-1)`.  Hence

```text
rank M(gamma)=t-1.                                       (12)
```

If `P_t` is nonempty, (12) forces the generic rank of `M(z)` to be `t-1`.
Therefore

```text
K=ker_(F(z)) M(z)
```

is a two-dimensional space of polynomials in `X` of degree at most `t`.

### 3. A formal common domain root kills the whole top stratum

Suppose some `x in D` is a common root of every polynomial in `K`.  Then

```text
K subset (X-x) F(z)[X]_(<=t-1).                          (13)
```

Define transformed moments

```text
n_r(z)=m_(r+1)(z)-x m_r(z)
```

and let `N_x(z)` be their `(t-1) x t` recurrence matrix.  Dividing the two
independent elements of `K` by `X-x` puts two independent vectors in
`ker N_x(z)`.  Thus

```text
rank_(F(z)) N_x(z)<=t-2.                                 (14)
```

At any actual top-weight parameter, however,

```text
n_r(gamma)=sum_(a in T) w_a(a-x)a^r.                    (15)
```

If `x notin T`, (15) has `t` distinct atoms and its
`(t-1) x t` Hankel matrix has row rank `t-1`.  If `x in T`, the atom at
`x` is killed and the remaining `t-1` atoms still give rank `t-1`.  In
both cases this contradicts (14), because specialization cannot increase
polynomial-matrix rank.

Therefore:

```text
one formal common domain root  =>  P_t is empty.          (16)
```

For the rest of the proof assume `P_t` is nonempty.  Then evaluation at every
`x in D` is a nonzero functional on `K`.

### 4. Transversality forces two evaluation classes on every top support

Fix `(gamma,c) in P_t` with support `T` and locator

```text
Q_T(X)=product_(x in T)(X-x).
```

We claim that restriction

```text
K -> F(z)^T                                               (17)
```

has rank two.  Otherwise some nonzero `L in K` vanishes on all `t` points
of `T`.  Since `deg L<=t`, it is a scalar multiple of `Q_T`.  Hence
`M(z)Q_T=0` identically, so both coefficient matrices satisfy

```text
M_0 Q_T=0,       M_1 Q_T=0.                              (18)
```

For a fixed `t`-set `T`, the `t-1` recurrence equations in (18) are
independent.  Their solution space in `F^(2t-1)` has dimension `t` and
contains the `t`-dimensional Vandermonde span `V_T`.  The two spaces are
equal.  Equation (18) would therefore put both `y_0` and `y_1` in `V_T`,
contradicting (3).  This proves the claim.

The `t` nonzero evaluation functionals

```text
ev_x|K,       x in T,
```

thus occupy at least two projective classes in the two-dimensional dual
space `K^*`.  Among `t` nonzero vectors spanning a plane, the minimum number
of unordered independent pairs is attained by class sizes `t-1` and `1`.
Consequently every retained top support contains at least

```text
t-1                                                       (19)
```

independent evaluation pairs.

### 5. Stacked determinants pay every good root pair

For `Y={x,x'} subset D`, let `E_Y` be the two constant evaluation rows at
`x` and `x'`, and define

```text
Delta_Y(z)=det [ M(z) ; E_Y ].                            (20)
```

The stack is square of size `t+1`.  The determinant is nonzero exactly when
`ev_x|K` and `ev_x'|K` are independent.  Call such `Y` good.  Only the first
`t-1` rows vary affinely with `z`, so

```text
deg Delta_Y<=t-1.                                        (21)
```

If `Y subset T` for an actual top locator, then `Q_T` lies in the specialized
kernel of the whole stack.  Hence

```text
Delta_Y(gamma)=0.                                        (22)
```

By (19), each retained top pair supplies at least `t-1` incidences
`((gamma,c),Y)` with a good `Y subset supp(c)`.

A fixed good pair `Y` can be used by at most one top error at one slope.  If
two distinct same-slope errors both contained `Y`, their difference would be
a nonzero GRS kernel word supported on the union of two `t`-sets sharing two
coordinates.  Its weight would be at most

```text
2t-2<R+1=2t,
```

contradicting the GRS minimum distance.  Combining this fact with (21), each
good `Y` receives at most `t-1` top-pair incidences over all slopes.

Double counting now gives

```text
|P_t|(t-1)
 <= sum_(good Y) #{top pairs charged to Y}
 <= binom(N,2)(t-1).
```

Since `t>=2`, cancellation proves (4).  Adding (9) proves (6).

### 6. MCA and CA conversion

Apply the RS parity check to a received line.  If its syndrome direction is
zero, the second received direction is a codeword and no support-wise
noncontained MCA or CA slope occurs.  Otherwise every MCA-bad explanation
gives a pair in (3).  Every CA-bad explanation does as well, because a common
syndrome support would lift to a common codeword support.  The slope
projection is no larger than the complete pair set, so (7) follows.

## Sharpness

Both meanings of (4) are sharp.

### Distinct-slope equality

Over `F_11` take

```text
D={0,1,2,3,4},       t=2,       R=3,
y_0=(1,0,7),         y_1=(5,1,9).
```

The line has ten transverse top pairs on ten distinct slopes and no lower
pair.  Their supports are exactly all `binom(5,2)=10` unordered domain pairs.
Thus the top slope projection itself attains (4).

### Same-slope all-pair equality

Over `F_7` take `D=F_7`, `t=2`, `R=3`, and

```text
y_gamma=(0,1,gamma).
```

For every unordered pair `{a,b}`, the nonzero amplitudes

```text
w_a=(a-b)^(-1),       w_b=-(a-b)^(-1)
```

give moments

```text
(0,1,a+b).
```

Thus every one of the `binom(7,2)=21` supports occurs exactly once.  At each
slope `gamma`, the three pairs with `a+b=gamma` are disjoint; the seven
slope fibers are the near-perfect-matching factorization of `K_7`.  This
attains (4) as an all-pair bound with same-slope multiplicity three.

The complete bound (6) is not claimed to be sharp: both equality fixtures
have an empty lower stratum.

## Verification

The stdlib-only verifier and pinned certificate are

```text
experimental/scripts/verify_first_beyond_half_kernel_pencil.py
experimental/data/certificates/first-beyond-half-kernel-pencil/first_beyond_half_kernel_pencil.json
```

It recomputes:

- every affine syndrome line in eight complete `t=2` prime-field grids over
  `F_3,F_5,F_7,F_11,F_13,F_17`, including proper subdomains:
  `142996` lines;
- `28000` deterministic weighted-GRS `t=3` lines over
  `F_7,F_11,F_13`;
- `1287159` retained transverse pairs and `1150138` distinct-slope
  incidences, including `137021` genuine same-slope top-pair excess;
- `1232889` top pairs in `164655` nonempty kernel-pencil families;
- `1370283` good support-pair incidences against an independently recomputed
  root capacity of `1710321`;
- `54270` lower pairs and `44857` lower generic-rank deflation families;
- exact Hankel rank, recurrence-kernel membership, transversality,
  fixed-kernel-root exclusion, projective evaluation-pair capacity, and
  same-slope support disjointness at every retained pair; and
- both sharp equality fixtures plus a fixed-root `t=3` pencil whose two
  formal common roots force an empty top stratum.

Run

```bash
python3 experimental/scripts/verify_first_beyond_half_kernel_pencil.py --check
python3 experimental/scripts/verify_first_beyond_half_kernel_pencil.py --tamper-selftest
python3 -O experimental/scripts/verify_first_beyond_half_kernel_pencil.py --check
python3 -O experimental/scripts/verify_first_beyond_half_kernel_pencil.py --tamper-selftest
```

The certificate is an exact recomputation with a SHA-256 payload digest.
The tamper self-test mutates independent theorem, census, sharpness,
fixed-root, base-commit, and digest fields.

## Nonclaims

- No bound is proved for `R<2t-1`.
- No exact complete numerator is claimed; only the top stratum is calibrated
  sharply.
- No comparison with ordinary worst-case RS list size is asserted without
  the transverse line condition.
- No atlas, profile-envelope, primitive-survival, or deployed-row movement
  follows from this packet.
- No priority claim over BCHKS or other proximity-gap/list-decoding work is
  made.
- The Lean file records interfaces only and is not a formal proof.
