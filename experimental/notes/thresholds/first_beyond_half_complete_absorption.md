# Complete absorption at the first beyond-half slice

## Theorem

Let `F` be any field, let `D subset F` contain `N` distinct points, and
choose nonzero weights `lambda_x`.  Use the weighted moment parity columns

```text
h_x=lambda_x(1,x,...,x^(R-1))^T,       x in D.          (1)
```

Fix a nonconstant syndrome line `y_z=y_0+z y_1` at

```text
N>=R=2t-1,       t>=2.                                  (2)
```

For `E subset D` put `V_E=span{h_x:x in E}`, and retain the complete set

```text
P={(gamma,c):
     Hc=y_gamma, wt(c)<=t,
     {y_0,y_1} not subset V_supp(c)}.                    (3)
```

No slope or witness selector is applied.  Then

```text
|P|<=binom(N,2).                                         (4)
```

This counts every distinct `(slope,error)` pair, including same-slope
multiplicity.  It is field-independent, characteristic-free, and valid for
arbitrary evaluation domains.

For `C=RS_F(D,N-R)` and agreement `a=N-t`, the exact
syndrome--secant correspondence gives

```text
B_C^MCA(a)<=binom(N,2),
B_C^CA(a) <=binom(N,2).                                  (5)
```

The same bounds hold after restricting the slopes to any challenge set.

## Status

`PROVED / AUDIT`.  The accompanying Lean module contains explicitly labelled
`UNPROVED STATEMENT TARGETS`; it is not a Lean proof.

This strictly sharpens the complete bound in
`first_beyond_half_kernel_pencil.md`.  That packet proved the sharp top-stratum
bound `|P_t|<=binom(N,2)` and added the safe half-distance payment
`N+t-1` for smaller weights.  The argument below shows that all lower strata
can instead be charged to unused roots of the same pair determinants.  The
two equality fixtures from the earlier packet have no lower pairs, so (4) is
sharp both for distinct slopes and for complete pairs with same-slope
multiplicity.

The mechanism is special to the two-dimensional generic locator kernel.
Nothing here claims that the complete fixed-deficiency sum can be absorbed
into its top binomial when the deficiency is at least two.

## Proof

Write the moment coordinates of the line as

```text
m_j(z)=(y_0)_j+z(y_1)_j,          0<=j<2t-1.
```

Form the top recurrence pencil

```text
M(z)=(m_(r+i)(z))_(0<=r<t-1, 0<=i<=t),                  (6)
```

an `(t-1) x (t+1)` matrix over `F[z]`.

### 1. Specialized rank records the support size

At an actual pair with support `S` of size `s<=t` and nonzero weighted
amplitudes `w_x=lambda_x c(x)`,

```text
M(gamma)
 =V_(t-1)(S)^T diag(w_x:x in S) V_(t+1)(S).
```

The right Vandermonde matrix maps onto `F^S` and the left one has rank
`min(s,t-1)`.  Hence

```text
rank M(gamma)=min(s,t-1).                                (7)
```

Let `rho` be the generic rank of `M(z)`.  There are three branches.

### 2. Generic rank drop falls inside half distance

If `rho<=t-2`, specialization and (7) force `s<=t-2` for every retained
pair.  The generic-rank deflation theorem at budget `t-2` applies because

```text
2(t-2)<R.
```

For `t>=3` it gives

```text
|P|<=N+t-2<=binom(N,2),                                  (8)
```

where the last inequality uses `N>=2t-1`.  When `t=2`, only the zero error
can remain, and a nonconstant line contains it at at most one parameter.

For the rest of the proof assume `rho=t-1`.  Then

```text
K=ker_(F(z)) M(z)
```

has dimension two.

### 3. A formal fixed root also falls inside half distance

Suppose every polynomial in `K` vanishes at some `x in D`.  Divide by
`X-x` and form the transformed moments

```text
n_j(z)=m_(j+1)(z)-x m_j(z).
```

The resulting `(t-1) x t` recurrence matrix has a two-dimensional kernel,
so its generic rank is at most `t-2`.  At an actual support `S`, however,
its rank is

```text
min(t-1,s)     if x notin S,
min(t-1,s-1)   if x in S.                               (9)
```

Consequently `s<=t-2` away from `x` and `s<=t-1` through `x`.  In
particular every retained pair has weight at most `t-1`.  The half-distance
generic-rank theorem gives

```text
|P|<=N+t-1<=binom(N,2)                                  (10)
```

for `t>=3`, and also for `t=2,N>=4`.

It remains only `t=2,N=3`.  Here `K` is the full two-dimensional space
`(X-x)F(z)[X]_(<=1)`, so the generic moment row is proportional to
`(1,x,x^2)`.  The whole syndrome line lies in `V_{x}`.  A singleton at
`x` is therefore common and rejected by transversality, while (9) excludes
singletons away from `x`.  Only the zero error can remain, at one parameter.

### 4. The remaining evaluation matroid is loopless of rank two

Assume now that `rho=t-1` and `K` has no common root in `D`.  Each
evaluation functional

```text
ev_x|K in K^*,       x in D,
```

is nonzero.  These functionals span `K^*`: otherwise a nonzero element of
`K` would vanish on all `N>=2t-1>t` domain points despite having degree at
most `t`.  They therefore define a loopless rank-two matroid on `D`.

Call an unordered pair `Y={x,x'}` *good* when its two evaluations are
independent.  Stack the two constant evaluation rows below `M(z)`:

```text
Delta_Y(z)=det [ M(z) ; ev_x ; ev_x' ].                  (11)
```

For good `Y` this is a nonzero polynomial.  Only the first `t-1` rows
vary affinely, so

```text
deg Delta_Y<=t-1.                                       (12)
```

### 5. Every error has at least `t-1` chargeable good pairs

Fix a retained pair with support `S` of size `s`, and put `j=t-s`.
Call a good pair `Y` *chargeable* when

```text
|Y minus S|<=j.                                         (13)
```

Multiplying the support locator `Q_S` by the roots in `Y minus S` gives
a polynomial of degree at most `t` that vanishes on both `S` and `Y`.
The moment factorization therefore puts it in the specialized kernel of the
stack in (11), and

```text
Delta_Y(gamma)=0.                                       (14)
```

Every retained support has at least `t-1` chargeable good pairs:

- If `s=t`, transversality forces the evaluations on `S` to span `K^*`.
  A loopless rank-two matroid on `t` points that has rank two has at least
  `t-1` bases.

- If `s=t-1`, chargeable pairs are precisely the good pairs meeting `S`.
  If `S` has rank one, any point in a different parallel class gives
  `s=t-1` cross pairs.  If `S` has rank two, it has at least `s-1`
  internal bases and every point outside `S` makes a further base with
  some point of `S`.

- If `s<=t-2`, every good domain pair is chargeable.  A loopless rank-two
  matroid on `N` points has at least `N-1>=t-1` bases.

For the first case, if the restriction to `S` had rank at most one, some
nonzero `L in K` would vanish on all `t` points.  Degree forces `L` to be a
multiple of `Q_S`, so `M(z)Q_S=0` identically.  The fixed-support recurrence
space is exactly `V_S`, placing both `y_0` and `y_1` there and contradicting
transversality.

### 6. A determinant root cannot be reused at one slope

Suppose two distinct errors at the same slope were both charged to `Y`.
Condition (13) gives

```text
|S union Y|<=t,       |S' union Y|<=t,
```

and therefore

```text
|S union S'|<=2t-2<R+1=2t.                              (15)
```

Their difference would be a nonzero kernel word supported on this union,
contradicting the weighted GRS minimum distance.  Thus a fixed root
`(gamma,Y)` is charged at most once.

Each retained pair supplies at least `t-1` roots by Section 5.  Each good
determinant has at most `t-1` roots by (12), and there are at most
`binom(N,2)` good pairs.  Double counting gives

```text
|P|(t-1)
 <= sum_(good Y) #{charged roots of Delta_Y}
 <= binom(N,2)(t-1).
```

Since `t>=2`, cancellation proves (4).

### 7. MCA and CA conversion

Apply the RS parity check to a received line.  If its syndrome direction is
zero, the received direction is a codeword and no support-wise noncontained
MCA or CA slope occurs.  Otherwise every MCA-bad explanation gives a pair in
(3).  Every CA-bad explanation does as well, because a common syndrome
support lifts to a common codeword support.  Projecting pairs to slopes can
only decrease cardinality, so (5) follows.

## Sharpness

The two fixtures from `first_beyond_half_kernel_pencil.md` attain the complete
bound.

- Over `F_11` with `D={0,1,2,3,4}` and `t=2`, one line has all ten
  domain pairs on ten distinct slopes.

- Over `F_7` with `D=F_7` and `t=2`, the line
  `y_gamma=(0,1,gamma)` has all 21 domain pairs, with three errors at each
  of seven slopes.

Both have no lower-weight pair, so `|P|=binom(N,2)`.

## Verification

The stdlib-only verifier and pinned certificate are

```text
experimental/scripts/verify_first_beyond_half_complete_absorption.py
experimental/data/certificates/first-beyond-half-complete-absorption/first_beyond_half_complete_absorption.json
```

They recompute:

- every affine syndrome line in eight complete `t=2` grids over
  `F_3,F_5,F_7,F_11,F_13,F_17`, including proper subdomains;
- deterministic weighted-GRS `t=3` samples over `F_7,F_11,F_13`;
- `158996` lines, `1261575` retained pairs, `1124501` distinct-slope
  incidences, and `137074` genuine same-slope excess;
- `1519244` chargeable good-pair incidences against independently recomputed
  root capacity `1619606`;
- all three generic-rank/fixed-root/loopless branches, including 39
  fixed-root lines and the minimal `t=2,N=3` fixed-root edge;
- both complete equality fixtures; and
- exact rank, padded-locator membership, determinant roots, nonreuse, root
  capacity, affine-line census, and bound slack at every audited line.

Run

```bash
python3 experimental/scripts/verify_first_beyond_half_complete_absorption.py --check
python3 experimental/scripts/verify_first_beyond_half_complete_absorption.py --tamper-selftest
python3 -O experimental/scripts/verify_first_beyond_half_complete_absorption.py --check
python3 -O experimental/scripts/verify_first_beyond_half_complete_absorption.py --tamper-selftest
```

The certificate is an exact recomputation with a SHA-256 payload digest.  The
tamper self-test mutates independent theorem, census, sharpness, fixed-root,
base-commit, and digest fields.

## Nonclaims

- No complete single-binomial absorption is claimed for deficiency at least
  two.
- No bound is claimed for `R<2t-1` in this packet.
- No ordinary worst-case RS list-size claim is made without the transverse
  line condition.
- No atlas, profile-envelope, primitive-survival, or deployed-row movement
  follows from this packet.
- The Lean file records interfaces only and is not a formal proof.
