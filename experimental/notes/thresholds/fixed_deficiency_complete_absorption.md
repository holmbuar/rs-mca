# Sharp complete absorption at every fixed deficiency

## Theorem

Let `F` be any field, let `D subset F` contain `N` distinct points, and
choose nonzero weights `lambda_x`.  Use the weighted moment parity columns

```text
h_x=lambda_x(1,x,...,x^(R-1))^T,       x in D.          (1)
```

Fix integers

```text
N>=R=2t-d,       1<=d<t,                                (2)
```

and a nonconstant syndrome line `y_z=y_0+z y_1`.  For
`E subset D` put `V_E=span{h_x:x in E}`, and retain the complete set

```text
P={(gamma,c):
     Hc=y_gamma, wt(c)<=t,
     {y_0,y_1} not subset V_supp(c)}.                    (3)
```

No slope or witness selector is applied.  Then

```text
|P|<=binom(N,d+1).                                       (4)
```

This counts every distinct `(slope,error)` pair, including same-slope
multiplicity.  It is field-independent, characteristic-free, and valid for
arbitrary evaluation domains.

For `C=RS_F(D,N-R)` and agreement `a=N-t`, the exact
syndrome--secant correspondence gives

```text
B_C^MCA(a)<=binom(N,d+1),
B_C^CA(a) <=binom(N,d+1).                                (5)
```

The same bounds hold after restricting slopes to any challenge set.

The constant in (4) is sharp.  For every admissible deficiency, canonical
Lagrange lines described below realize every `(d+1)`-subset of their domain
as a distinct top-weight error pair and have no lower-weight pair.

## Status

`PROVED / AUDIT`.  The accompanying Lean module contains explicitly labelled
`UNPROVED STATEMENT TARGETS`; it is not a Lean proof.

This supersedes the complete sum in
`fixed_deficiency_kernel_minor_compiler.md`.  That packet proved the sharp
bound separately on every strictly beyond-half exact stratum and used the
safe generic-rank payment for the half-distance core.  The present proof
uses only the top degree-`t` locator kernel.  Every lower-weight error pads
its locator into sufficiently many top-kernel evaluation bases, so all
strata share one root-capacity ledger.

The deficiency-one theorem in
`first_beyond_half_complete_absorption.md` is the rank-two instance.  The
new ingredient is a general matroid basis-exchange count that replaces the
case analysis special to rank two.

For fixed `d`, (4) is `O_d(N^(d+1))`.  When `d` grows linearly, the sharp
binomial can be exponential; the theorem does not by itself establish the
profile-atlas bridge needed by the deployed tables.

## Proof

Put

```text
r=t-d=R-t,       k=d+1,       r+k=t+1.                  (6)
```

Here `r>=1` is the number of top recurrence rows and `k>=2` is the
generic top locator-kernel dimension.

### 1. Specialized top rank records the support size

Write the line moments as

```text
m_j(z)=(y_0)_j+z(y_1)_j,          0<=j<R,
```

and form the `r x (t+1)` top recurrence pencil

```text
M(z)=(m_(a+i)(z))_(0<=a<r, 0<=i<=t).                    (7)
```

At an actual pair with support `S` of size `s<=t` and nonzero weighted
amplitudes `w_x=lambda_x c(x)`,

```text
M(gamma)
 =V_r(S)^T diag(w_x:x in S) V_(t+1)(S).
```

The right Vandermonde matrix maps onto `F^S`, while the left matrix has
rank `min(r,s)`.  Hence

```text
rank M(gamma)=min(r,s).                                  (8)
```

### 2. Generic top-rank drop falls inside half distance

If the generic rank of `M(z)` is at most `r-1`, (8) forces

```text
s<=r-1
```

for every retained pair.  The half-distance generic-rank compiler at budget
`r-1` applies and gives

```text
|P|<=N+r-1.                                              (9)
```

This is at most `binom(N,k)`.  Indeed, if `r=1` then (9) is `N` and
`1<=k<=N-1`.  If `r>=2`, the parameter identities give

```text
2<=k<=N-3,       N>=2r+1,
```

so binomial unimodality and elementary arithmetic give

```text
binom(N,k)>=binom(N,2)>=N+r.
```

For the rest of the proof assume `M(z)` has full generic row rank `r` and
put

```text
K=ker_(F(z)) M(z),       dim K=k.                        (10)
```

### 3. A formal common domain root also falls inside half distance

Suppose every polynomial in `K` vanishes at some `x in D`.  Dividing by
`X-x` puts a `k`-dimensional space into the kernel of the transformed
`r x t` recurrence matrix built from

```text
n_j(z)=m_(j+1)(z)-x m_j(z).
```

That matrix has generic rank at most

```text
t-k=r-1.                                                (11)
```

At an actual support `S`, its specialized rank is

```text
min(r,s)     if x notin S,
min(r,s-1)   if x in S.                                 (12)
```

Thus `s<=r-1` away from `x` and `s<=r` through `x`.
Every retained error has weight at most `r`, and the half-distance theorem
gives

```text
|P|<=N+r.                                                (13)
```

For `r>=2` the binomial comparison in Section 2 proves (4).  When `r=1`
and `N>=t+2`, one has `k=t<=N-2` and
`binom(N,k)>=binom(N,2)>=N+1`.

The sole remaining edge is `r=1,N=t+1`.  Here `k=t`, and the
`k`-dimensional kernel is exactly

```text
K=(X-x)F(z)[X]_(<=t-1).
```

The moment row is therefore proportional to
`(1,x,...,x^t)`, so the whole syndrome line lies in `V_{x}`.  A singleton
at `x` is common and rejected by transversality, while (12) excludes every
singleton away from `x`.  Only the zero error can remain, at at most one
parameter.

### 4. The remaining evaluation matroid is loopless of rank `k`

Assume henceforth that `K` has no common root in `D`.  Every evaluation
functional

```text
ev_x|K in K^*,       x in D,
```

is nonzero.  Together they span `K^*`: otherwise a nonzero polynomial in
`K` would vanish at all `N>=R>t` domain points despite having degree at
most `t`.  The evaluations therefore define a loopless rank-`k` matroid
`M_K` on `D`.

For a `k`-subset `Y subset D` stack its constant evaluation rows below
the top recurrence pencil:

```text
Delta_Y(z)=det [ M(z) ; (ev_x)_(x in Y) ].               (14)
```

Call `Y` *good* when it is a basis of `M_K`.  Equivalently,
`Delta_Y` is nonzero.  Only the first `r` rows vary affinely, so

```text
deg Delta_Y<=r.                                         (15)
```

### 5. Transversality forces the necessary rank on every support

Fix a retained support `S` of size `s` and put

```text
j=t-s.
```

If `j>=k`, no support-rank statement is needed.  Suppose `j<k` and set

```text
h=k-j.                                                   (16)
```

We claim

```text
rank_(M_K)(S)>=h.                                        (17)
```

Let `Q_S=product_(x in S)(X-x)`.  The full space of degree-at-most-`t`
polynomials vanishing on `S` is

```text
W_S=Q_S F(z)[X]_(<=j),       dim W_S=j+1.                (18)
```

If the rank in (17) were at most `h-1`, rank-nullity for evaluation on
`K` would give

```text
dim(K intersect W_S)>=k-(h-1)=j+1.
```

Thus `W_S subset K`.  In particular

```text
Q_S, XQ_S, ..., X^j Q_S
```

all lie in `K`.  The `r` recurrence rows for these `j+1` shifted
locators cover every shift from zero through `r+j-1`.  There are

```text
r+j=R-s
```

such shifts, exactly the full fixed-support recurrence system for `S`.
Its equations are independent, and its `s`-dimensional solution space is
`V_S`.  Both `y_0` and `y_1` would lie in `V_S`, contradicting (3).
This proves (17).

### 6. Basis exchange constructs `r` chargeable bases

Call a good basis `Y` *chargeable for `S`* when

```text
|Y minus S|<=j.                                         (19)
```

We prove that every retained support has at least `r` chargeable bases.

First suppose `j>=k`.  Every basis is chargeable.  A loopless rank-`k`
matroid on `N` elements has at least `N-k+1` bases: start with one basis
and exchange each element outside it into a basis.  Moreover

```text
N-k+1>=2r>=r.                                           (20)
```

Now suppose `j<k` and use `h=k-j` from (16).  By (17), choose an
independent `h`-set `A subset S` and extend it to a basis `B` of `M_K`.
Put

```text
q=|B intersect S|>=h.
```

The following bases are distinct and chargeable:

1. `B` itself;
2. for each `x in S minus B`, a fundamental-circuit exchange
   `B-e_x+x`; and
3. if `q>h`, for `q-h` distinct points
   `y in D minus (B union S)`, a fundamental-circuit exchange
   `B-e_y+y`.

There are enough points for the third step because

```text
|D minus (B union S)|=N-k-s+q>=q-h,
```

the last inequality being equivalent to `N>=k+s-h=t`.  An exchange in
step 2 leaves at least `q` support elements in the basis.  An exchange in
step 3 loses at most one, leaving at least `q-1>=h`.  Therefore every
listed basis satisfies (19).  Their number is

```text
1+(s-q)+(q-h)
 =s-h+1
 =(t-j)-(d+1-j)+1
 =t-d
 =r.                                                     (21)
```

This exact cancellation is the combinatorial heart of the theorem.

### 7. Every chargeable basis is a determinant root

For an actual pair `(gamma,c)` with support `S` and a chargeable `Y`,
multiply `Q_S` by the roots in `Y minus S`.  Condition (19) makes the
degree at most `s+j=t`.  The resulting polynomial vanishes on `S` and
`Y`, so the moment factorization puts it in the specialized kernel of the
stack in (14).  Hence

```text
Delta_Y(gamma)=0.                                       (22)
```

A fixed root `(gamma,Y)` cannot be reused by two distinct errors at the
same slope.  If supports `S,S'` were both charged to `Y`, then

```text
|S union Y|<=t,       |S' union Y|<=t,
```

and, since `|Y|=k=d+1`,

```text
|S union S'|
 <=2t-k
 =2t-d-1
 =R-1
 <R+1.                                                   (23)
```

The difference of the two errors would be a nonzero weighted-GRS kernel
word of weight below the minimum distance `R+1`, a contradiction.

Every retained pair supplies at least `r` distinct roots by Section 6.
Every good determinant receives at most `r` roots by (15), and there are
at most `binom(N,k)` good bases.  Double counting gives

```text
|P|r
 <=sum_(good Y) #{charged roots of Delta_Y}
 <=binom(N,k)r.
```

Since `r>=1` and `k=d+1`, cancellation proves (4).

### 8. MCA and CA conversion

Apply the RS parity check to a received line.  If its syndrome direction is
zero, the received direction is a codeword and no support-wise noncontained
MCA or CA slope occurs.  Otherwise every MCA-bad explanation gives a pair in
(3).  Every CA-bad explanation does as well, because a common syndrome
support lifts to a common codeword support.  Projecting pairs to slopes can
only decrease cardinality, proving (5).

## Consumer bridge: the complete strict-beyond-half window

Use the active threshold paper's notation: length `n`, code dimension `K`,
agreement `a`, redundancy `R=n-K`, and error budget `t=n-a`.  Define

```text
d=2t-R=n+K-2a.                                         (BH1)
```

Then `d>=1` is exactly the strict beyond-half-distance condition
`2(n-a)>n-K`.  On the exact-agreement grid `a>=K+1`, the other hypothesis
`d<t` is automatic because it is equivalent to `K<a`.  Consequently the
theorem gives the unconditional finite-row compiler

```text
K+1 <= a <= floor((n+K-1)/2)
    ==> B_C^MCA(a), B_C^CA(a)
          <= binom(n,n+K-2a+1).                        (BH2)
```

This is a bound for the complete domain-wide witness set.  It therefore does
not require a witness atlas, a fixed support-union chart, a smooth domain, or
an image-normalized profile estimate.  It also survives arbitrary first-match
deletion: every residual pair set is a subset of the set counted in (3).

### Exact target certificate

For a nonempty challenge set `Gamma`, put

```text
B*=floor(epsilon |Gamma|).
```

At any agreement in (BH2), the literal comparison

```text
binom(n,n+K-2a+1) <= B*                                (BH3)
```

is an unconditional safe-side certificate.  It does not identify the first
safe agreement without a matching unsafe construction at the preceding grid
point; in particular, the universal tangent floor is generally much smaller
than the binomial in (BH3).

### Exact asymptotic scale

Let `K_n/n -> rho`, `a_n/n -> alpha`, and put

```text
theta=1+rho-2alpha.
```

Whenever `0<theta<1`, Stirling's formula applied directly to (BH2) gives

```text
limsup (1/n) log_2 B_Cn^MCA(a_n) <= H_2(theta),         (BH4)
```

and the same statement for CA.  Thus a target budget with exponent strictly
larger than `H_2(theta)` pays this region with a linear bit reserve, without
any of the conditional profile-envelope inputs.

At the moving midpoint, write

```text
a_n=(n+K_n)/2-s_n+O(1).
```

Then `d_n=2s_n+O(1)`.  If `s_n=o(n)`, elementary entropy asymptotics give

```text
log binom(n,d_n+1)=o(n).                               (BH5)
```

Hence the complete MCA and CA numerators are subexponential throughout every
sublinear-width strict-beyond-half window.  The correct sufficient condition
is `d_n=o(n)`, not the cruder `d_n=o(n/log n)` obtained from
`binom(n,d+1)<=n^(d+1)`.

For the frontiers paper's ray interface this is stronger than a per-chart
compiler in the range (BH5): `|Z_lambda^o|<=exp(o(n))` for every residual
profile, and indeed the union over all profiles already obeys the same
domain-wide bound.  No profile-count factor needs to be introduced.

### Orthogonality to the augmented paving-basis compiler

DannyExperiments' upstream PR #764 proves a different complete-pair bound.
Specialized to the full domain, where its residual-kernel dimension is
`kappa=n-R=K`, its field-independent term is

```text
floor(binom(n,K+1) / binom(a-1,K)).                     (BH6)
```

Once that theorem is available on the same base, (BH2) and (BH6) may be
combined by taking their minimum.  They cannot be multiplied: (BH2) charges
top-locator evaluation bases and cancels a determinant root degree, whereas
(BH6) charges bases of an augmented lift/kernel row matroid.  No injection or
independent product charge between those two owner sets has been proved.  At
`a=K+1` the two displayed bounds agree with the canonical Lagrange family;
near the half-distance midpoint, (BH2) supplies the collapsing top-kernel term
that (BH6) generally does not.

The crossover is logarithmic in the code dimension on every fixed-deficiency
slice.  Write `r=t-d`, so

```text
R=2r+d,       n=2r+d+K.
```

Before taking the floor, (BH6) is exactly

```text
P(n,K,r)
 =binom(n,K+1)/binom(r+K-1,K)
 =n/(K+1) product_(j=0)^(K-1)
      (n-1-j)/(r+K-1-j).                              (BH7)
```

For fixed `d` and `K=O(log n)`, one has `r=n/2+O(log n)` and the logarithm
of the accumulated product error is `O_d(K^2/r)=o(1)`.  Therefore

```text
P(n,K,r)=(1+o(1)) n 2^K/(K+1),
binom(n,d+1)=(1+o(1)) n^(d+1)/(d+1)!.                  (BH8)
```

Their ratio is

```text
P(n,K,r)/binom(n,d+1)
 =(1+o(1)) (d+1)! 2^K / ((K+1)n^d).                   (BH9)
```

Thus the paving term is smaller below, and the top-kernel term is smaller
above, the transition

```text
K=d log_2 n + log_2 log_2 n + O_d(1).
```

In particular, the two results cover genuinely different parameter axes:
the paving denominator is decisive at bounded or very small code dimension,
while (BH2) is decisive for fixed deficiency and constant positive rate.

## Sharpness: canonical Lagrange lines

Fix any `d>=1`, put

```text
t=d+1,       R=t+1,       k=d+1=t,
```

and choose a field and domain with `N>=t+1` distinct points.  Take unit
column weights and the syndrome line

```text
y_z=(0,...,0,1,z) in F^(t+1).                            (24)
```

For every `t`-subset `S subset D`, assign the nonzero amplitudes

```text
w_x=1 / product_(a in S minus {x})(x-a).
```

The Lagrange identities give

```text
sum_(x in S) w_x x^j = 0          for 0<=j<t-1,
sum_(x in S) w_x x^(t-1) = 1,
sum_(x in S) w_x x^t = sum_(x in S) x.
```

Thus `S` supplies a top error at slope `gamma=sum_(x in S)x`.  The single
recurrence row is not identically zero on `Q_S`, so every pair is
transverse.  No smaller support occurs: for `s<t`, its first `s` moments
would all vanish, and the square Vandermonde matrix forces all amplitudes to
zero.  Consequently

```text
|P|=binom(N,t)=binom(N,d+1).
```

Slope collisions are harmless because (4) counts all pairs.

The MCA and CA numerator bounds are also sharp, over suitable fields and
domains, at this minimal-agreement edge.  Suppose the `t`-subset-sum map on
`D` is injective.  Formula (24) then gives a different slope for every
`t`-support.  The line is column-far: a support of size below `t` cannot carry
even one line point by the Vandermonde argument above, while for a `t`-support
the locator recurrence on `y_z` is the nonzero affine equation
`z=sum_(x in S)x`, so it cannot contain the whole syndrome line.  Therefore

```text
B_C^MCA(K+1)=B_C^CA(K+1)=binom(N,t),
K=N-t-1.                                                (25)
```

This has an explicit family over prime fields.  Choose a prime `p>2^N` and

```text
D={1,2,4,...,2^(N-1)} subset F_p.
```

Every subset sum lies between zero and `2^N-1`, so there is no modular
wraparound, and uniqueness of binary expansion separates all subset sums.
Thus (25) is genuine distinct-slope equality, not merely pair-multiplicity
sharpness.

This numerator equality is an explicit superincreasing-domain specialization
of the already proved exact first-adjacent theorem and the depth-zero identity
LineRay owner.  It is recorded here only to show that the new complete
fixed-deficiency upper bound has no smaller universal slope constant at its
minimal-agreement edge; no new adjacent-row theorem is claimed.

## Sharpness at every fixed recurrence depth

The polynomial degree in (4) is not an artifact of the depth-one equality
family.  Fix a recurrence depth r>=1, put t=d+r, and take the full domain
F_q along powers q=p^nu of a prime not dividing t(t-1).  The line

    y_z=e_(t-1)+z e_(t+r-1)

has complete pair set indexed by the square-free, completely split sparse
polynomials

    X^t+a_d X^d+...+a_0.

A Morse slice has geometric monodromy S_t; finite-field Chebotarev then gives

    |P|=q^(d+1)/t!+O_(t,p)(q^(d+1/2)),
    |P|/binom(q,d+1) -> (d+1)!/(d+r)! > 0.              (26)

Thus d+1 is the necessary complete-pair exponent at every fixed interior
depth.  The exact depth-two zero-sum family and elementary depth-three
quadratic-completion family recover the same leading constants with stronger
finite error terms.  Full details and literature dependencies are in
all_depth_sparse_split_sharpness.md.

These full-domain families have repeated slopes and do not replace the
distinct-slope equality (25).  They establish interior complete-pair
sharpness, not an interior MCA/CA numerator lower bound.

## Verification

The stdlib-only verifier and pinned certificate are

```text
experimental/scripts/verify_fixed_deficiency_complete_absorption.py
experimental/data/certificates/fixed-deficiency-complete-absorption/fixed_deficiency_complete_absorption.json
```

They recompute:

- `56117` exhaustive and deterministic sampled affine lines across
  deficiencies one through four;
- two complete deficiency-two grids over `F_5` with `N=4,5`, both of
  which attain the sharp top binomial;
- `238849` retained pairs, `199976` distinct-slope incidences, and
  `38873` genuine same-slope excess;
- `33248` lines containing at least two different retained weights;
- `402552` chargeable top-basis incidences against an independently
  recomputed root capacity of `481911`;
- every generic-rank, formal-fixed-root, loopless, and empty branch, including
  the minimal `r=1,N=t+1` edge;
- canonical equality fixtures for `d=1,...,5`;
- distinct-slope canonical fixtures for `d=1,...,5` on the superincreasing
  domain `{1,2,4,...,64} subset F_257`, attaining MCA/CA numerator equality;
  and
- exact recurrence rank, support-restriction rank, chargeability, padded
  locator membership, determinant roots, same-slope nonreuse, root capacity,
  affine-line census, and complete-binomial slack.

An additional complete positive-kernel census over F_7 at
N=6,R=5,t=3,d=1 enumerated all 6,725,201 affine lines.  It found 13,465,901
transverse pairs on 13,304,621 slope incidences, 161,280 same-slope excess,
and maximum pair count 5 on any line.  Thus this smallest full positive-kernel
grid has slack 10 against the universal top bound 15 and is also below the
independent paving cap 7.  All four proof branches occur, including 1,680
formal-fixed-root lines and 1,069,170 mixed-weight lines.  This is a finite
strictness audit, not a smaller universal theorem.

Run

```bash
python3 experimental/scripts/verify_fixed_deficiency_complete_absorption.py --check
python3 experimental/scripts/verify_fixed_deficiency_complete_absorption.py --tamper-selftest
python3 -O experimental/scripts/verify_fixed_deficiency_complete_absorption.py --check
python3 -O experimental/scripts/verify_fixed_deficiency_complete_absorption.py --tamper-selftest
```

The certificate is an exact recomputation with a SHA-256 payload digest.  The
tamper self-test mutates independent theorem, census, sharpness, edge-branch,
base-commit, and digest fields.

## Nonclaims

- At constant rate, `binom(N,d+1)` can remain exponential when `d` has
  positive linear density; the theorem is not an owner-free subexponential
  compiler throughout the whole beyond-half region.
- No bound is claimed here for `d>=t`, equivalently `R<=t`.
- No ordinary worst-case RS list-size claim is made without the transverse
  line condition.
- No first-match atlas or primitive-survival theorem follows from this packet.
  The complete bound bypasses those inputs only where its literal target
  comparison succeeds; no deployed row movement is claimed.
- The Lean file records interfaces only and is not a formal proof.
