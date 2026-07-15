# Hostile audit 4: source, quantifiers, and constants for the weighted global-covector bound

## Verdict

```text
ACCEPT
confidence: high
```

I independently reconstructed the source handoff, the simultaneous-covector
quantifier, every local sign and support correction, the projective twist and
Bezout degree, and the tame-characteristic polar payment.  The canonical
theorem object is valid under its printed hypotheses and applies uniformly to
the five exact rank-15 cells.  In particular,

```text
E+S=2E-U <= (3q-B)(q+1).
```

This excludes all `12,607` exact states in `(q,B)=(24,69)` with minimum
integer gap `86-75=11`.  It does not close the other four cells, all of
`M=213`, affine rank at least 16, or either official question.

## Frozen object and independent replay evidence

```text
theorem
  work/RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS_BOUND.md
  sha256=6f998929209b534d39cb0d31fa6458f5bf63d9326255ec31e7f0f64ae7a5389e

claimant verifier (replayed separately; PASS)
  work/verify_rank15_poschar_global_covector_weighted_excess_bound.rb
  sha256=20d11b8b2294e4509d15539b28c96fa27e1c3c29695c33aa52848fc625d7cfa6

independent exact-state reconstruction
  work/audit_global_covector_weighted_excess_minima.rb
  sha256=ceb9e8fa47fc7d1e03d3c4ef69ceb0b72fffc222f7d54b6443b586e73e7dcd3a

byte-exact independent transcript
  work/audit_global_covector_weighted_excess_minima.expected.txt
  sha256=12488f13a9545c41a749a0fa348d078bf29f3c584ee8c93a92db8662ecc07a6d

exact source driver pinned by the reconstruction
  work/explore_rank15_m213_exact_localcost_driver.rb
  sha256=8cfcf7475dd153e5e101e0c97467d7d49b0336f902e806ce673dee13f8de533b
```

The independent reconstruction does not load, evaluate, transform, or invoke
either claimant impact wrapper or the claimant verifier.  It rebuilds the
deficiency moment profiles, uses a point-by-point Cauchy scan with an exact
integer-square-root bound, and rebuilds the unbounded residual multiplicity
partition DP.  Its expected transcript is pinned above rather than inferred
from the theorem table.

## 1. Exact rank-15 source handoff

The theorem is applied after exact divisorial deletion.  A source row supplies
a reduced arrangement of `B` distinct projective lines over the algebraic
closure of the deployed field, preserved by a degree-`q` projective field

```text
X in H^0(P^2,T(q-1))
```

with isolated zero scheme and exact positive minimal syzygy degree `q`.  These
are the hypotheses under which the accepted boundary-extactic argument proves
that the line extactic is nonzero.  Tangency makes every arrangement factor
divide the extactic, and the row degrees `1,q,2q-1` give total degree `3q`.
Consequently, for every one of the five cells,

```text
Xi=lambda f g,          deg(g)=a=3q-B>0.                 (A1)
```

This is not an extra genericity assumption and is not selected separately for
each local zero.

The source arithmetic localizes exactly, not just monotonically.  Put `R` for
the number of distinct arrangement intersections and `I` for their total
line incidence.  The exact driver uses

```text
C=q^2+q+1,
E=C-R,
U=B(q+1)-I,
S=DPW(B,q)-tau=E-U.                                     (A2)
```

In its profile coordinates, the same identities are printed as

```text
U=incidence_cap-incidence,
E=point_cap-residual_points,
E=U+S.
```

Thus the theorem's weight is exactly the enumerated quantity

```text
E+S=U+2S,
```

not a relabeled relaxation statistic.  The exact-state table is a necessary
superset of realizable arrangements, so eliminating a row by a universal
arrangement theorem is source-valid.

## 2. One simultaneous affine covector exists

Choose one projective line at infinity avoiding the finite field-zero scheme
and avoiding every component of `fg`.  On its affine complement the constant
covectors form one two-dimensional vector space `V`.  For an irreducible
component `C` of `fg`, choose an affine point of `C` outside the isolated zero
scheme.  At that point `X` is nonzero and `V` spans the cotangent space, so
some member of `V` detects `X`.  Therefore

```text
V_C={du in V : X(u)|_C is identically zero}
```

is a proper linear subspace.  Each arrangement tangent direction excludes
one further proper line in `V`.  There are finitely many components and
tangent directions, and the algebraically closed base field is infinite.
Their finite union cannot cover `V`.

Hence one fixed affine coordinate `u` simultaneously satisfies

```text
X(u) has no component in common with fg,
du is nonzero on every arrangement-line tangent.         (A3)
```

No pointwise change of covector is hidden here.  A complementary `v` is then
fixed, and only translations of the same `(u,v)` coordinates are made at
different zeros.

Writing `u=ell/z`, the differential is the restriction of

```text
alpha=z d(ell)-ell dz in H^0(P^2,Omega^1(2)).
```

Contraction with `X in T(q-1)` gives

```text
h=<alpha,X> in H^0(P^2,O(q+1)),      h|A2=X(u).           (A4)
```

The twist is `2+(q-1)=q+1`, not `q`.  By (A3), `gcd(g,h)=1`, including when
`g` is repeated, invariant, or has arrangement-line components.  Projective
Bezout therefore gives the full scheme-theoretic length

```text
sum_Z i_Z(g,h)=a(q+1).                                  (A5)
```

## 3. Exact local identity and properness

At a zero write

```text
X=P partial_u+Q partial_v,        P=X(u)=h,
I=(P,Q),                          mu=length O/I.
```

Isolation gives `gcd(P,Q)=1`.  If `F` is the reduced product of the `m`
incident arrangement branches, the affine extactic determinant is, up to a
unit,

```text
K=P X(Q)-Q X(P)=F g.
```

Reduction modulo `P` gives the load-bearing sign

```text
K=-Q^2 P_v mod P.                                      (A6)
```

Property (A3) gives proper intersections of `P` with `F` and `g`.  If a
branch divided both `P` and `P_v`, (A6) and `gcd(P,Q)=1` would make it divide
`Fg`, contradicting (A3).  Thus `gcd(P,P_v)=1`.  Additivity of proper local
intersection numbers now gives exactly

```text
i(P,g)=2mu+i(P,P_v)-i(P,F).                             (A7)
```

This also handles a nonreduced `g`: its full multiplicity remains on both
sides of the divisor identity.

## 4. Source support corrections and polar payment

The local contributions to `E` and `U` are:

| support | `e` | `u_0` |
|---|---:|---:|
| off arrangement, `m=0` | `mu` | `0` |
| smooth arrangement, `m=1` | `mu` | `i(P,F)` |
| ordinary intersection, `m>=2` | `mu-1` | `i(P,F)-m` |

The last row subtracts one baseline Chern point and one baseline restriction
zero on each of the `m` incident lines.  Because `du` is nonzero on every
line tangent, the line restriction orders sum to `i(P,F)`; no tangent factor
is lost.  Therefore the local summand `w=2e-u_0` is

```text
m=0:  2mu,
m=1:  2mu-i(P,F),
m>=2: 2mu-i(P,F)+m-2.                                  (A8)
```

Comparing (A7) and (A8), only

```text
i(P,P_v)>=m-2                                           (A9)
```

is needed at an ordinary `m>=3` point.

Let `R=u partial_u+v partial_v` and
`H=F_v partial_u-F_u partial_v`.  Since `p>B>=m`, the identity
`det(R,H)=-mF` is a genuine Saito basis identity and the logarithmic field
has the form `X=A R+C H`.  Thus

```text
P=A u+C F_v.
```

The level line `u=0` is not an arrangement branch by (A3), so

```text
F(0,v)=c v^m,
P(0,v)=m c C(0,v)v^(m-1).                               (A10)
```

If `C(0,v)` vanished identically, then `u` would divide `C`, `P`, and `P_v`;
(A6) would force `u|g`, contradicting (A3).  Hence

```text
n=i(P,u)>=m-1.
```

Also `n<=deg(P)<=q+1<p`, so differentiation retains a nonzero leading
coefficient and `ord_v P_v(0,v)=n-1`.  Since
`O/(P,P_v)` has finite length,

```text
i(P,P_v)
 >= length k[[v]]/(P(0,v),P_v(0,v))
 =n-1
 >=m-2.                                                (A11)
```

This is an Artin-quotient argument valid in the printed tame characteristic;
it does not import a characteristic-zero Milnor or Teissier formula.

## 5. Global sum and points outside the residual divisor

Every field zero lies on `fg`.  If such a zero is not on `g`, then `g` is a
local unit, so `i(P,g)=0`; (A7)--(A11) force its local weight `w<=0`.  Thus it
is legitimate to retain that weight on the left and zero on the right.
Summing over all zeros and then enlarging to the complete intersection gives

```text
E+S=sum w
 <=sum_(field zeros) i(P,g)
 <=sum_(Z in V(g,h)) i_Z(g,h)
 =a(q+1).
```

No residual support point is omitted, and negative local weights do not
reverse an inequality.

## 6. Omitted-hypothesis attacks

The following failures confirm that the printed hypotheses are substantive.

1. Without logarithmic tangency, `P=u-v^n` can have
   `i(P,P_v)=n-1<m-2`; the Saito lower bound is then unavailable.
2. If the fixed covector shares a component with `Fg`, `P` and `P_v` can
   share that component and both the local identity and Bezout become
   improper.
3. In characteristic `p`, `P=u-v^p` has `P_v=0`; the printed
   `p>q+1>=n` gate excludes this cancellation.
4. If `p|m`, then `det(R,H)=-mF=0` and (A10) loses its leading term; the
   printed `p>B` gate excludes it.
5. If `u=0` is an arrangement branch, `F(0,v)=0`, not `c v^m`; the finite
   tangent-direction exclusions in (A3) are therefore load-bearing.

No counterexample satisfying all printed hypotheses survives these attacks.

## 7. Independent constants and exact replay

The deployed characteristic gate is immediate:

```text
p=2,130,706,433 > max(B,q+1)
```

for every cell.  The independent reconstruction and its pinned transcript
give:

| `(q,B,a)` | raw | `E+S` range | cap `a(q+1)` | survivors |
|---|---:|---:|---:|---:|
| `(24,69,3)` | 12,607 | `86..120` | 75 | 0 |
| `(24,68,4)` | 16,027 | `96..132` | 100 | 919 |
| `(25,71,4)` | 225 | `95..107` | 104 | 215 |
| `(25,70,5)` | 350 | `106..119` | 130 | 350 |
| `(25,69,6)` | 559 | `117..132` | 156 | 559 |

The cap identities are respectively `3*25=75`, `4*25=100`, `4*26=104`,
`5*26=130`, and `6*26=156`.  The cubic cell is empty with a gap of eleven;
the survivor counts in the other cells are necessary-state diagnostics only.

