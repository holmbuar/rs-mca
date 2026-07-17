# The first deep-hole wall is an MDS dimension-lift / arc problem

## Status and scope

**PROVED** for the interpolation partition, collision ledger, MDS
dimension-lift equivalences, and local slope-map criterion below.  The full-field
`kappa=1`, odd-characteristic equality classification is **CITED** from
Segre's classical oval theorem, with the elementary graph-to-quadratic bridge
proved here.  The verifier exhausts the stated finite fixtures.  The Lean
module proves only the finite owner-image/collision algebra and pinned
binomial identities; it does not formalize weighted GRS interpolation or
Segre's theorem.

This packet resolves what information survives at the first residual wall
named by the all-pair paving compiler.  At

```text
d=R,                 t=R-1,
```

the ordinary design projection is vacuous: every `(kappa+1)`-set is already
covered by the complete pair family.  The missing datum is the algebraic
slope label.  In the nondegenerate regime `R>=2`, retaining that label
identifies exact PB5 pair-count equality with a one-step dimension lift to an
MDS supercode, equivalently with a nested maximal-interpolation-distance flag.

No general near-equality inverse, even-characteristic arc classification,
first-match catalogue assignment, new pair cap, target crossing, or paper
promotion is claimed.

## 1. Setup

Let `U` have `N` coordinates.  Let

```text
H : F^U -> F^R,
K = ker H,
kappa = N-R,
```

where `K` is the `[N,kappa,R+1]` weighted GRS code supplied by the paving
compiler.  Choose lifts `b_0,b_1` of nonconstant syndrome-line data
`y_0,y_1`, with `y_1 != 0`, and assume the literal direction distance is the
deep-hole value

```text
dist(b_1,K)=R.                                           (1)
```

Put

```text
r = kappa+1,
L = K + <b_1>.
```

The sum is direct.  Every nonzero word of `K` has weight at least `R+1`,
while every word with nonzero `b_1` coefficient has weight at least `R` by
(1).  The Singleton bound is attained, so

```text
L is an [N,r,R] MDS code.                               (2)
```

Now specialize to the first wall

```text
t=R-1,          a=N-t=kappa+1=r.                        (3)
```

Let `P_full` contain every distinct pair represented by an error

```text
e=b_0+l,          l in L,          wt(e)<=R-1.
```

The `b_1` coefficient of `l` is the slope and its `K` component is the code
translate, so errors and pairs are in bijection.  Transversality is automatic
here: if `y_1` lay in the span of fewer than `R` parity columns, it would have
a lift of weight `<R`, contradicting (1).

For a word `e`, write

```text
Z(e)={x in U:e(x)=0},          z(e)=|Z(e)|.
```

Condition (3) says that `e` belongs to `P_full` exactly when `z(e)>=r`.

## 2. Exact interpolation partition

### Theorem 1 (first-wall interpolation partition)

For every `r`-set `I subset U`, there is a unique word `e_I in b_0+L` that
vanishes on `I`.  The map

```text
I |-> e_I                                                   (4)
```

is onto `P_full`, and the fiber above `e` consists exactly of the `r`-subsets
of `Z(e)`.  Consequently

```text
sum_(e in P_full) binom(z(e),r) = binom(N,r).             (5)
```

**Proof.**  Every `r`-coordinate restriction of the `[N,r]` MDS code `L` is
an isomorphism.  Hence there is a unique `l_I in L` with
`l_I|I=-b_0|I`, and `e_I=b_0+l_I` is the required word.  Conversely, every
`e in P_full` has an `r`-subset of its zero set, so it occurs in the image.
Uniqueness says that `e_I=e` exactly when `I subset Z(e)`.  Counting all
`r`-sets by their owner proves (5).  `square`

Thus the weighted PB4 charge is an equality for the *complete* first-wall
family even when the augmented matrix is highly non-MDS.  The unweighted PB5
slack is not an uncovered-design leave; it is a collision ledger.

### Corollary 2 (exact retained-family slack split)

For any retained first-match subset `P subset P_full`,

```text
binom(N,r)-|P|
 = sum_(e in P)       (binom(z(e),r)-1)
 + sum_(e in P_full\P) binom(z(e),r).                    (6)
```

The first term is algebraic owner collision inside retained fibers.  The
second is exact charge deleted by earlier first-match owners.  A proof using
only the unlabelled block family loses this distinction.

## 3. Equality is exactly one more MDS extension

Let

```text
M = K + <b_1,b_0> = L + <b_0>,
A = [b_0  b_1  G],                                      (7)
```

where the columns of `G` form a basis of `K`.  Assume `1<=r<N`, equivalently
`R>=2` in this setup.

### Theorem 3 (equivalent first-wall inverse forms)

The following are equivalent.

1. `|P_full|=binom(N,r)`.
2. Every `e in P_full` has `z(e)=r`.
3. `b_0 notin L` and `dist(b_0,L)=N-r=R-1`.
4. `M` is an `[N,r+1,R-1]` MDS code.
5. Every `(r+1)`-row restriction of `A` has rank `r+1`.

When these conditions hold, the source data form the nested MDS/maximal-
interpolation-distance flag

```text
K                 [N,kappa,  R+1]
  subset L         [N,kappa+1,R]
  subset M         [N,kappa+2,R-1].                     (8)
```

**Proof.**  Equation (5) partitions `binom(N,r)` faces into nonempty fibers.
The number of fibers equals the number of faces exactly when every fiber is a
singleton, which is (1) iff (2).  Interpolation already supplies a coset word
with at least `r` zeros, so `dist(b_0,L)<=N-r`.  Condition (2) says no coset
word has more than `r` zeros, hence equality in this distance bound and
`b_0 notin L`; this proves (2) iff (3).  Nonzero words in `L` have weight at
least `R=N-r+1`, while nonzero words in the other cosets of `L` inside `M`
rescale to `b_0+L` and have weight at least `R-1=N-r`.  Thus (3) is exactly
the Singleton equality for the dimension-`r+1` code `M`, proving (3) iff (4).
Moreover, interpolation into any `r` coordinates gives `rho(L)<=N-r`, while
(3) supplies a word at that distance.  Thus `rho(L)=N-r` and `b_0` is a deep
hole in the maximal-distance sense; the bare phrase “deep hole” is not being
used as a substitute for (3).  Finally, a generator matrix generates an MDS
code exactly when every maximal
square row restriction has full rank, giving (4) iff (5).  `square`

For an arbitrary retained subset `P`, equality in PB5 still forces this
conclusion: `P subset P_full` and both have size at most `binom(N,r)`, so
`|P|=binom(N,r)` implies `P=P_full` and invokes Theorem 3.

This identifies the correct next-level inverse statistic.  The
`(kappa+1)`-basis census of `A` is automatically maximal by the MDS submatrix
`[b_1 G]`; exact first-wall equality is controlled by the
`(kappa+2)`-basis census, equivalently the MDS property of the whole `A`.

## 4. The missing label is a local slope map

Fix a `kappa`-set `J`.  Since `K` is MDS, for `i in {0,1}` there is a unique
`k_(i,J) in K` agreeing with `b_i` on `J`.  Put

```text
u_(i,J)=b_i-k_(i,J).
```

The word `u_(1,J)` vanishes on `J`.  Its weight is at least `R` by (1), while
`|U\J|=R`, so its zero set is exactly `J`.  Therefore

```text
Gamma_J(x) = -u_(0,J)(x)/u_(1,J)(x),      x in U\J,      (9)
```

is well-defined.

For a slope `gamma`, the corresponding core-pencil word is

```text
e_(J,gamma)=u_(0,J)+gamma u_(1,J),
```

and one has the exact fiber identity

```text
Z(e_(J,gamma))
 = J union Gamma_J^(-1)(gamma).                          (10)
```

Hence each complete core pencil partitions `U\J`, regardless of whether `M`
is MDS.  In particular its moving-zero capacity is always full at this wall.
The local collision deficit is

```text
R-|im Gamma_J|
 = sum_(gamma in im Gamma_J)(|Gamma_J^(-1)(gamma)|-1).   (11)
```

### Corollary 4 (slope-injectivity criterion)

The conditions of Theorem 3 are also equivalent to

```text
Gamma_J is injective for every kappa-set J.              (12)
```

Indeed a collision at `x!=x'` gives a coset word vanishing on
`J union {x,x'}`, an `(r+1)`-set.  Conversely, a coset word with at least
`r+1` zeros supplies such a collision after choosing `J` and two remaining
zeros.

This is why almost-Steiner or pencil-fullness arguments alone cannot resolve
the first wall.  Fullness is automatic.  The inverse problem is injectivity,
anti-concentration, or structural classification of the compatible family of
maps `Gamma_J`.

## 5. The design projection is information-theoretically empty here

At `R-t=1`, one has `a=r`.  Equation (4) already covers every `r`-set, so the
unlabelled equality design is only

```text
S(r,r,N)=binom(U,r).                                     (13)
```

After arbitrary first-match deletion, any subfamily of these minimal blocks
is compatible with the bare incidence inequalities.  Thus no theorem using
only block incidence, local pencil fullness, or leave size can emit an owner
at this wall.  It must consume the algebraic slope labels (9), their
cross-core compatibility, or an equivalent MDS/arc extension invariant.

At positive depth `R-t>=2`, design congruences become nontrivial, but they are
still insufficient by themselves: affine-geometry Steiner families and
noncompletable partial designs show that a genuine source-semantic hypothesis
remains necessary.

## 6. `kappa=1`: the label is a graph-secant slope

Now let `kappa=1`.  Because `K` is weighted GRS, choose its nonvanishing
multiplier word `v` so that `K=<v>`, and divide all words coordinatewise by
`v`.  This support-preserving linear automorphism sends `K` to the constant
code.  Write

```text
tilde_b_i(u)=b_i(u)/v(u).
```

Direction distance `d=R=N-1` says that `tilde_b_1` is injective.  If
`U=F_q`, then it is bijective; use `x=tilde_b_1(u)` as the coordinate and
write

```text
f(x)=-tilde_b_0(u).
```

For `J={x_0}`, equation (9) becomes the ordinary secant slope

```text
Gamma_(x_0)(x)
 = (f(x)-f(x_0))/(x-x_0).                               (14)
```

Thus Theorem 3 says that exact first-wall PB5 *pair-count* equality is
equivalent to the
graph

```text
G_f={(x,f(x)):x in F_q}
```

having no three collinear points.  Adding the vertical point at infinity
produces a `(q+1)`-arc, hence an oval in `PG(2,q)`.

### Corollary 5 (odd full-field equality is quadratic)

Let `q` be odd.  In the full-domain `kappa=1` chart, exact first-wall PB5
equality holds if and only if

```text
f(x)=A x^2+B x+C,             A!=0.                     (15)
```

Equivalently, in the original weighted coordinate labelling,

```text
-b_0(u)/v(u)
  =A (b_1(u)/v(u))^2+B (b_1(u)/v(u))+C,     A!=0.       (16)
```

The conclusion is quadratic only after both the weighted-code and direction
normalizations.  It is not necessarily quadratic in raw `b_1` or in a
pre-existing Vandermonde coordinate.  When `v=1`, (16) reduces to the
unweighted formula.

**Proof.**  The forward direction uses B. Segre's theorem that every oval in
the Desarguesian plane `PG(2,q)` of odd order is a nondegenerate conic.  The
original source is
[Segre, *Ovals in a finite projective plane* (1955)]
(https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C436473E65277F46C5A60279667CE257/S0008414X00030534a.pdf/ovals-in-a-finite-projective-plane.pdf);
a modern proof is [Muller, arXiv:1311.3082]
(https://arxiv.org/abs/1311.3082).

Write a homogeneous conic through the vertical point `P_inf=(0:1:0)` as

```text
a X^2+b X Y+d X Z+e Y Z+g Z^2=0.                       (17)
```

On the affine graph this reads

```text
(b x+e)f(x)+a x^2+d x+g=0.                              (18)
```

If `b!=0`, then at `x=-e/b` equation (18) either has no graph point or the
conic contains the whole vertical line, contradicting respectively the full
graph or nondegeneracy.  Hence `b=0`; then `e!=0`, and (18) makes `f`
quadratic.  Its quadratic coefficient is nonzero because a line is not an
arc.  Conversely a nondegenerate quadratic graph meets every nonvertical
line in at most two points, so it is an arc and Theorem 3 applies.  `square`

This is a source-level curve classification.  The packet does not silently
identify it with a particular printed first-match cell; that semantic bridge
must match the catalogue's actual predicates.  In even characteristic the
oval classification has nonconic families, so no analogue of (15) is claimed.

For the quadratic equality case, a secant through distinct `x,y` has

```text
gamma=A(x+y)+B,             z=C-Axy.                    (19)
```

At each fixed slope, `x+y` is fixed.  Because `q` is odd, the resulting
involution has one fixed point and `(q-1)/2` unordered nonfixed pairs.  Thus
every one of the `q` slopes carries exactly `(q-1)/2` pair owners.  This
attains the fixed-slope cap proved in upstream PR #817, but does not create a
new numerical bound.

### Candidate-payment crosswalk; no catalogue assignment

At the first wall, `a=r=kappa+1`, so the identity-prefix depth is zero.
The theorem in
`experimental/notes/thresholds/depth_zero_identity_lineray_owner.md` supplies
the exact candidate scale `binom(N,r)` for a complete transverse family.
That note explicitly does **not** prove atlas exhaustivity or assignment to
the identity owner, so neither does this crosswalk.

Independently, all original error differences in a `kappa=1` chart lie in
`<v,b_1>` (and hence, after normalization, in `<1,x>`), so their affine
dimension is at most `s=2`.  The all-pair theorem in
`experimental/notes/thresholds/all_lineray_affine_core_set_pair.md` therefore
gives, for the quadratic equality family,

```text
|P_full| <= binom(s+t,s)=binom(q,2).
```

The rank observation does not use quadraticity: every retained subfamily in
a fixed `kappa=1` chart has rank at most two.  More generally, differences
lie in `L`, so their affine rank is at most `r=kappa+1`; the sublinear-`kappa`
regime matches the sublinear-rank payment.  These are theorem-level candidate
payments.  Applying them as *earlier* first-match owners still requires the
catalogue predicate and ordering audit disclaimed above.

## 7. Near equality does not imply exact quadratic structure

The exact result has no literal relative-slack stability.  Let `q>=5` be odd
and set

```text
f(0)=-1,                 f(x)=x^2 for x!=0.             (20)
```

The reduced polynomial `x^2-1+x^(q-1)` has degree `q-1`, so this function is
not quadratic.  A line through the moved point `(0,-1)` and `(x,x^2)` has
slope `x+x^(-1)`.  It contains a second unchanged conic point exactly at
`x^(-1)`.  Removing the fixed points `x=+-1` leaves exactly `(q-3)/2`
unordered reciprocal pairs, hence exactly that many trisecants.  No line has
four graph points.  Each trisecant collapses three unordered point-pair labels
to one owner, costing two owners, and all other secants remain distinct.
Therefore

```text
T=(q-3)/2,
|P_full|=binom(q,2)-2T=binom(q,2)-(q-3).                 (21)
```

The perturbed function is nonquadratic but has relative pair count

```text
|P_full|/binom(q,2)=1-2(q-3)/(q(q-1))=1-O(1/q).         (22)
```

This does not refute a robust theorem that emits a curve plus a small planted
exception: the example is deliberately one edit from the conic.  It does
rule out the overstrong conclusion that `o(1)` relative PB5 slack forces exact
quadratic equality with no exceptional coordinates.

## 8. Verification and formal scope

Run

```bash
python3 experimental/scripts/verify_first_wall_mds_extension_inverse.py --check
python3 experimental/scripts/verify_first_wall_mds_extension_inverse.py --tamper-selftest
python3 -O experimental/scripts/verify_first_wall_mds_extension_inverse.py --check
python3 -O experimental/scripts/verify_first_wall_mds_extension_inverse.py --tamper-selftest
```

The verifier recomputes:

- an `[8,4,5]` interpolation code over `F_11`, one MDS dimension lift and one
  collision extension;
- every coset word, owner fiber, zero-set binomial charge, augmented rank,
  next-level dependent set, and local slope-map collision in those fixtures;
- the weighted `F_5` normalization regression that satisfies (16) but refutes
  the corresponding raw-`b_1` quadratic formula;
- all functions `F_5 -> F_5` and `F_7 -> F_7`, confirming that the
  arc functions are exactly the nondegenerate quadratics on those grids; and
- one-point quadratic perturbations over several odd prime fields, including
  the exact trisecant and pair-deficit formula (21).

The Lean module `GrandeFinale/FirstWallMDSExtensionInverse.lean` proves the
finite image cap, equality/injectivity criterion, collision partition, and
pinned binomial values.  Weighted-GRS interpolation, the MDS equivalence, and
Segre's theorem remain outside its formal scope.

## 9. Ledger impact

1. The first wall is not an almost-Steiner completion problem: its weighted
   incidence capacity is already exactly full.
2. Unweighted PB5 slack splits exactly into retained collision excess and
   earlier-owner deletion charge by (6).
3. For `R>=2`, exact equality is a nested maximal-distance/MDS
   dimension-lift flag, testable either by the next-level row census or by
   injectivity of every local slope map.
4. For `kappa=1` over a full odd field, equality is a quadratic graph/oval.
5. The depth-zero family matches exact identity and affine-core candidate
   payments, but this packet does not prove their catalogue precedence.  The
   remaining target is the positive-depth, linear-rank compatibility problem
   after literal earlier-owner deletion, with explicit exceptional-coordinate
   accounting.  No numerical frontier moves here.
