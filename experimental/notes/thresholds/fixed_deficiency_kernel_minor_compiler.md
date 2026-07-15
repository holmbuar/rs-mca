# Fixed-deficiency kernel-minor compiler beyond half distance

## Theorem

Let `F` be any field, let `D subset F` contain `N` distinct points, and
choose nonzero weights `lambda_x`.  Use the weighted moment parity columns

```text
h_x=lambda_x(1,x,...,x^(R-1))^T,       x in D.          (1)
```

Fix a nonconstant syndrome line `y_z=y_0+z y_1`.  For
`E subset D` write `V_E=span{h_x:x in E}`, and retain the complete set

```text
P={(gamma,c):
     Hc=y_gamma, wt(c)<=t,
     {y_0,y_1} not subset V_supp(c)}.                    (2)
```

No slope or witness selector is used.

### Exact-stratum theorem

Fix an exact weight `s<R` strictly beyond the half-distance moment window:

```text
2s>=R+1.
```

Put

```text
r=R-s,
kappa=2s-R+1=s+1-r.                                     (3)
```

Thus `r>=1` and `kappa>=2`.  Let `P_s` be the exact-weight-`s` stratum
of (2).  Then

```text
|P_s|<=binom(N,kappa).                                   (4)
```

This counts every distinct `(slope,error)` pair, including same-slope
multiplicity.  It is field-independent and characteristic-free.

### Complete fixed-deficiency theorem

Now choose integers `t` and `d` with

```text
N>=R=2t-d,       1<=d<t.                                (5)
```

Let

```text
s_0=floor(R/2)
```

and let `rho_0` be the generic rank over `F(z)` of the leading
`s_0 x s_0` Hankel pencil.  Then

```text
|P_{<=s_0}|<=N+rho_0<=N+s_0,                             (6)

|P| <= N+rho_0
       + sum_(s=s_0+1)^t binom(N,2s-R+1)

    <= N+s_0
       + sum_(s=s_0+1)^t binom(N,2s-R+1).                (7)
```

For every fixed deficiency `d`, (7) is

```text
O_d(N^(d+1)).                                            (8)
```

The high-stratum kernel dimensions in (7) have one parity and increase by
two.  For example:

```text
d=1:  |P|<=N+(t-1)+binom(N,2),
d=2:  |P|<=N+(t-1)+binom(N,3),
d=3:  |P|<=N+(t-2)+binom(N,2)+binom(N,4).                (9)
```

For `C=RS_F(D,N-R)` and agreement `a=N-t`, the exact
syndrome--secant correspondence gives the same right-hand side in (7) as an
upper bound for both `B_C^MCA(a)` and `B_C^CA(a)`.  Restricting slopes to a
challenge set can only decrease the count.

## Status

`PROVED / AUDIT`.  The accompanying Lean module contains explicitly labelled
`UNPROVED STATEMENT TARGETS`; it is not a Lean proof.

**Superseded complete bound.**  The later packet
`fixed_deficiency_complete_absorption.md` absorbs the half-distance core and
every intermediate stratum into the top kernel-minor capacity, sharpening
(7) to the sharp single bound `|P|<=binom(N,d+1)`.  The exact-stratum theorem
and proof in this note remain valid and are reused there.

This packet generalizes
`first_beyond_half_kernel_pencil.md` from deficiency one to every fixed
deficiency.  It also sharpens the repository's general
fixed-generic-kernel-dimension payment.  That theorem safely charges a
dimension-`kappa` locator kernel one evaluation basis at a time and retains a
row-degree factor.  Here every actual support supplies many good bases, and
the exact GRS distance prevents same-slope reuse.  The row-degree factor
cancels exactly.

The result is a per-LineRay hard-input-3 payment.  It does not show that the
first-match atlas has bounded deficiency, and it becomes exponential when
`d` grows linearly.

## Proof of the exact-stratum theorem

### 1. Actual support gives full recurrence-row rank

Write the line moments as

```text
m_j(z)=(y_0)_j+z(y_1)_j,          0<=j<R.
```

For the exact weight `s` form the `r x (s+1)` recurrence pencil

```text
M_s(z)=(m_(a+i)(z))_(0<=a<r, 0<=i<=s).                  (10)
```

At an actual pair `(gamma,c)` with support `T` of size `s` and nonzero
weighted amplitudes `w_x=lambda_x c(x)`,

```text
M_s(gamma)
 =V_r(T)^T diag(w_x:x in T) V_(s+1)(T).                 (11)
```

The right Vandermonde matrix maps onto `F^T`.  Since
`r=s-kappa+1<=s-1`, the left Vandermonde matrix maps `F^T` onto `F^r`.
Thus

```text
rank M_s(gamma)=r.                                       (12)
```

If `P_s` is nonempty, the generic rank is therefore `r` and

```text
K_s=ker_(F(z)) M_s(z)
```

has dimension `kappa`.

### 2. One formal common domain root makes the stratum empty

Suppose every polynomial in `K_s` vanishes at some `x in D`.  Division by
`X-x` embeds the `kappa`-dimensional quotient into the kernel of the
`r x s` recurrence matrix built from

```text
n_j(z)=m_(j+1)(z)-x m_j(z).                              (13)
```

Hence that transformed matrix has generic rank at most

```text
s-kappa=r-1.                                             (14)
```

At an actual exact-`s` parameter, however,

```text
n_j(gamma)=sum_(a in T)w_a(a-x)a^j.                     (15)
```

If `x notin T`, (15) has `s` nonzero atoms.  If `x in T`, it has
`s-1` nonzero atoms.  In either case the transformed `r x s` Hankel matrix
has rank `r`, because `r<=s-1`.  This contradicts (14), since
specialization cannot increase polynomial-matrix rank.

Therefore an occupied exact stratum has no formal common domain root:

```text
for every x in D, evaluation ev_x|K_s is nonzero.         (16)
```

### 3. Transversality forces full evaluation rank on each support

Fix a retained support `T`.  We claim

```text
K_s -> F(z)^T                                             (17)
```

has rank `kappa`.  Otherwise its kernel contains a nonzero polynomial
`L`.  Since `deg L<=s` and `L` vanishes at the `s` distinct points of
`T`, it is a scalar multiple of

```text
Q_T(X)=product_(x in T)(X-x).
```

Thus `M_s(z)Q_T=0` identically.

For fixed `T`, the `r=R-s` shifted recurrence equations defined by `Q_T`
are independent: its monic coefficient gives distinct pivot positions.
Their solution space inside `F^R` therefore has dimension `R-r=s`.
It contains the `s`-dimensional weighted Vandermonde span `V_T`, so the two
spaces are equal.  The identity `M_s(z)Q_T=0` would put both `y_0` and
`y_1` in `V_T`, contradicting transversality.  This proves (17).

### 4. Every support supplies at least `r` evaluation bases

The `s` functionals

```text
ev_x|K_s,       x in T,
```

are nonzero by (16) and span the `kappa`-dimensional dual by (17).
Choose one basis `B` among them.  For each of the `s-kappa` remaining
functionals `e`, its fundamental circuit relative to `B` contains some
`b in B`, and replacing `b` by `e` gives another basis.  These bases are
distinct because each contains its own outside element.  Including `B`,
the number of evaluation bases inside `T` is at least

```text
1+(s-kappa)=s-kappa+1=r.                                 (18)
```

This elementary matroid count is the source of the cancellation below.

### 5. Stacked minors have exactly the compensating degree

For each `kappa`-subset `Y subset D`, stack its constant evaluation rows
under `M_s(z)`:

```text
Delta_Y(z)=det [M_s(z); E_Y].                            (19)
```

The stack is square because `r+kappa=s+1`.  The determinant is nonzero
exactly when the evaluations indexed by `Y` form a basis of `K_s^*`.
Call such `Y` good.  Only the first `r` rows vary affinely in `z`, so

```text
deg Delta_Y<=r.                                          (20)
```

If `Y subset T` for an actual locator, then `Q_T` is in the specialized
kernel of the entire stack.  Hence

```text
Delta_Y(gamma)=0.                                        (21)
```

By (18), every retained exact pair supplies at least `r` incidences with a
good `Y`.

For fixed `(gamma,Y)`, at most one retained exact error can contain `Y`.
Indeed, two distinct same-slope errors with supports `T,T'` containing
`Y` would differ by a nonzero GRS kernel word supported on at most

```text
|T union T'|<=2s-kappa=R-1<R+1,                          (22)
```

contradicting the GRS minimum distance `R+1`.

Each good `Delta_Y` has at most `r` roots.  Double counting (21), using
(18), (20), and (22), gives

```text
|P_s| r
 <= sum_(good Y) #{retained pairs charged to Y}
 <= binom(N,kappa) r.
```

Since `r>=1`, cancellation proves (4).

## Proof of the complete fixed-deficiency theorem

For all weights at most `s_0=floor(R/2)`, the generic-rank deflation theorem
applies because `R>=2s_0`.  It pays the complete lower pair family at
`N+rho_0<=N+s_0`.

For each remaining exact weight `s_0<s<=t`, the integer

```text
kappa_s=2s-R+1
```

is at least two, so (4) gives `|P_s|<=binom(N,kappa_s)`.  Summing the
disjoint weight strata proves (7).  Under `R=2t-d`, the largest kernel
dimension is `kappa_t=d+1` and the number of high strata depends only on
`d`, proving (8).

The MCA and CA conversion is the same exact syndrome--secant conversion used
in the two predecessor packets: every bad slope produces a transverse pair
in (2), and the slope projection is no larger than the complete pair set.

## Sharpness of every exact-stratum constant

For every `d>=1` choose the minimal permitted

```text
t=d+1,       R=t+1=d+2.
```

On any domain `D` with `N>=R` take the line

```text
y_gamma=(0,...,0,1,gamma) in F^(t+1),                    (23)
```

where the `1` is in moment coordinate `t-1`.  For every `t`-subset
`T subset D`, put

```text
w_x=1/Q'_T(x),       x in T.
```

The Lagrange identities give

```text
sum_(x in T) w_x x^j =
  0                  for 0<=j<t-1,
  1                  for j=t-1,
  sum_(x in T)x      for j=t.                            (24)
```

Thus every `t`-subset occurs on (23), at slope equal to its root sum.  The
direction recurrence evaluates to the monic coefficient of `Q_T`, so every
pair is transverse.  Here `kappa=d+1=t` and

```text
|P_t|=binom(N,t)=binom(N,d+1).                           (25)
```

Therefore (4) is exactly sharp for every kernel dimension, as a complete
all-pair theorem.  Slopes may carry multiple supports; the bound is about the
complete pair object.

## Verification

The stdlib-only verifier and pinned certificate are

```text
experimental/scripts/verify_fixed_deficiency_kernel_minor_compiler.py
experimental/data/certificates/fixed-deficiency-kernel-minor-compiler/fixed_deficiency_kernel_minor_compiler.json
```

It recomputes:

- `39000` exhaustive affine lines in the `d=2,t=3,R=4` grids over
  `F_5` on domains of sizes four and five;
- `27000` deterministic weighted-GRS lines spanning
  `(d,t) in {(2,3),(2,4),(3,4),(3,5),(4,5)}`;
- `299658` retained pairs, `245647` slope incidences, and `54011`
  same-slope excess pairs;
- `244591` strictly beyond-half pairs in `67722` occupied exact-stratum
  families;
- `385043` good evaluation-basis incidences against independently
  recomputed root capacity `844345`;
- recurrence rank, locator recovery, formal-root exclusion, matroid basis
  floor, determinant degree/root capacity, same-slope basis nonreuse, and the
  complete sum at every audited line;
- exact canonical-Lagrange equality for deficiencies `d=1,2,3,4,5` over
  `F_7`, with pair counts `21,35,35,21,7`; and
- a `d=2,t=4` fixed-kernel-root pencil whose two formal common roots force
  an empty exact top stratum.

Run

```bash
python3 experimental/scripts/verify_fixed_deficiency_kernel_minor_compiler.py --check
python3 experimental/scripts/verify_fixed_deficiency_kernel_minor_compiler.py --tamper-selftest
python3 -O experimental/scripts/verify_fixed_deficiency_kernel_minor_compiler.py --check
python3 -O experimental/scripts/verify_fixed_deficiency_kernel_minor_compiler.py --tamper-selftest
```

The certificate is an exact recomputation with a SHA-256 payload digest.

## Nonclaims

- If `d` grows linearly, the binomial sum in (7) can be exponential; this
  packet does not prove the full residual ray compiler.
- The complete sum (7) is not claimed to be exact, even though every
  individual high-stratum constant (4) is sharp over the permitted range.
- No result is claimed when `t>=R`, where the recurrence row window can
  disappear.
- No atlas, profile-envelope, primitive-survival, or deployed-row movement
  follows from this packet.
- No published-priority claim is made.
- The Lean file records interfaces only and is not a formal proof.
