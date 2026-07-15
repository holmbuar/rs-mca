# Global-covector weighted excess bound

## Theorem candidate

This theorem object is frozen for independent hostile audit.  No acceptance
status is asserted here; acceptance requires separate audit objects.

Let `k` be algebraically closed of characteristic zero or characteristic
`p>max(B,q+1)`.  Let a reduced arrangement of `B` projective lines be
preserved by a nonzero projective field

```text
X in H^0(P^2,T_{P^2}(q-1))
```

with isolated zero scheme.  Suppose its nonzero line-extactic divisor has
the factorization

```text
Xi=lambda f g,             deg(f)=B,             deg(g)=a=3q-B,
```

where `f` is the reduced arrangement equation.  Let

```text
E=(q^2+q+1)-R
```

be the Chern excess over the number `R` of distinct arrangement
intersections, let `U` be the total arrangement-line restriction deficit,
and put `S=E-U`.  (In the exact rank-15 source this is precisely the
nonnegative DPW slack.)  Then

```text
E+S=2E-U <= a(q+1).                                      (1)
```

No reducedness assumption is imposed on `g`, and its components may be
invariant, non-invariant, repeated, or arrangement lines.

For the deployed rank-15 cells, `p=2130706433`, `q<=25`, and `B<=71`, so
the displayed characteristic hypothesis is overwhelmingly satisfied.

## 1. A generic affine component of the field

Choose a projective line `L_infinity` which is neither a component of `fg`
nor incident to any field zero.  On the affine complement choose a generic
affine-linear coordinate `u`; later choose a complementary affine-linear
coordinate `v`.

The choice can be made with both of the following properties:

1. `X(u)` vanishes identically on no irreducible component of `fg`;
2. `du` is nonzero on the tangent direction of every arrangement line.

Indeed, constant affine covectors form a two-dimensional vector space and
span the cotangent space at every affine point.  For each component `C` of
`fg`, choose a point of `C` at which `X` is nonzero.  The covectors whose
contraction with `X` vanishes identically on `C` form a proper linear
subspace.  There are finitely many components, and the algebraically closed
field is infinite.  The tangent-direction conditions exclude only finitely
many further one-dimensional subspaces.

The affine differential `du` is the restriction of the global section

```text
alpha=z d(ell)-ell dz in H^0(P^2,Omega^1(2)),
```

where `u=ell/z`.  Hence

```text
h=<alpha,X> in H^0(P^2,O(q+1))                           (2)
```

and `h|A2=X(u)`.  Property 1 says that `h` and `fg` have no common
component.  In particular, `(g,h)` is a zero-dimensional complete
intersection of total length

```text
deg(g)deg(h)=a(q+1),                                     (3)
```

with the full multiplicity of a nonreduced `g` included.

## 2. Exact local intersection identity

Fix a field zero and translate the affine coordinates so it is the origin.
Write

```text
X=P partial_u+Q partial_v,       P=X(u)=h,
I=(P,Q),                         mu=length O/I.
```

Let `F` be the product of the `m` incident arrangement-line equations; take
`F=1` when the point is off the arrangement.  Up to a local unit, the
extactic equation is

```text
K=P X(Q)-Q X(P)=F g.                                     (4)
```

Modulo `P`,

```text
K=-Q^2 P_v mod P.                                        (5)
```

All intersections in the following identity are proper.  Properness with
`Q`, `F`, and `g` follows from isolated zeros and the generic choice in
Section 1.  If an irreducible local branch divided both `P` and `P_v`, then
(5), together with `gcd(P,Q)=1`, would make that branch divide `Fg`; this
would contradict the fact that `P=h` shares no component with `Fg`.
Therefore `gcd(P,P_v)=1` as well.

Taking local intersection numbers in (4)--(5) gives the exact identity

```text
i(P,g)=2mu+i(P,P_v)-i(P,F).                              (6)
```

## 3. Localizing `E`, `U`, and `E+S`

Every field zero lies on `fg`, because its first two extactic rows are
dependent.  Let `e` be its local contribution to `E`, and let `u_0` be its
local contribution to the total line-restriction deficit `U`.

If the zero is off the arrangement (`m=0`), then

```text
e=mu,                    u_0=0.                          (7)
```

At a smooth point of one arrangement line (`m=1`), the restriction order
of the field is `i(P,F)`, because `du` is nonzero on the line direction.
Thus

```text
e=mu,                    u_0=i(P,F).                     (8)
```

At an arrangement intersection (`m>=2`), let `r_j` be the restriction order
on the `j`th incident line.  The same generic-direction property gives

```text
i(P,F)=sum_j r_j,
e=mu-1,
u_0=sum_j(r_j-1)=i(P,F)-m.                               (9)
```

Since `E+S=2E-U`, its local summand `w=2e-u_0` is therefore

```text
m=0:  w=2mu,
m=1:  w=2mu-i(P,F),
m>=2: w=2mu-i(P,F)+m-2.                                 (10)
```

Comparing (6) and (10), the desired local payment

```text
w<=i(P,g)                                                 (11)
```

is automatic for `m=0,1,2`.  At an ordinary `m>=3` point it is exactly the
polar inequality

```text
i(P,P_v)>=m-2.                                           (12)
```

## 4. The ordinary-point polar inequality

At an ordinary `m`-fold line intersection, use the Saito basis

```text
R=u partial_u+v partial_v,
H=F_v partial_u-F_u partial_v,
det(R,H)=-mF.
```

The hypothesis `p>B>=m` makes `m` invertible.  Write

```text
X=A R+C H.
```

Then

```text
P=X(u)=A u+C F_v.                                        (13)
```

The line `u=0` is not one of the arrangement branches by the generic choice
of `du`.  Since `F` is a product of `m` distinct linear forms through the
origin,

```text
F(0,v)=c v^m,             c!=0,
F_v(0,v)=m c v^(m-1).
```

Restriction of (13) to `u=0` yields

```text
P(0,v)=m c C(0,v)v^(m-1).                                (14)
```

The series `C(0,v)` cannot vanish identically.  If it did, then `u|C` and
(13) would give `u|P` and `u|P_v`.  Equation (5) would give `u|K`; since
`u` is not an arrangement branch, (4) would force `u|g`.  This contradicts
the component avoidance of Section 1.  Consequently

```text
i(P,u)=ord_v P(0,v)>=m-1.                                (15)
```

We already know `gcd(P,P_v)=1`, so the polar Artin algebra

```text
M=O/(P,P_v)
```

has finite length.  Put `n=i(P,u)=ord_v P(0,v)`.  Because `P` is an affine
polynomial of degree at most `q+1<p` and `u=0` is not a component, `n<p`.
Hence the leading coefficient `n` remains nonzero in `k`, and

```text
ord_v P_v(0,v)=n-1.
```

Quotienting the finite-length module `M` further by `u` can only decrease
length.  Therefore

```text
i(P,P_v)=length M
 >=length M/uM
  =length k[[v]]/(P(0,v),P_v(0,v))
  =n-1
  =i(P,u)-1.                                             (16)
```

This is a direct Artin-length proof of the needed polar inequality, not an
appeal to a characteristic-zero Milnor or Teissier formula.  Equations
(15)--(16) give

```text
i(P,P_v)>=i(P,u)-1>=m-2,
```

which proves (12).

This is the only extra local input needed for the weighted, rather than
unweighted, global bound.

## 5. Global sum

Sum (11) over all field zeros.  At a point not on `g`, the right side of
(11) is zero, so the same local inequality gives `w<=0`; retaining that
summand on the left and zero on the right causes no omission.  The
field-zero intersections form a subset of the complete intersection
`(g,h)`, so (3) gives

```text
E+S=2E-U
    =sum_(field zeros) w
   <=sum_(field zeros) i(P,g)
   <=sum_(Z in V(g,h)) i_Z(g,h)
    =a(q+1).
```

This proves (1).

## 6. Exact five-cell impact

The source-locked exact-state replay gives the following complete table,
where `W=E+S`, `cap=a(q+1)`, and `survivors` counts rows satisfying the new
necessary bound.

| `(q,B,a)` | raw states | `W` range | cap | survivors |
|---|---:|---:|---:|---:|
| `(24,69,3)` | 12,607 | `86..120` | 75 | 0 |
| `(24,68,4)` | 16,027 | `96..132` | 100 | 919 |
| `(25,71,4)` | 225 | `95..107` | 104 | 215 |
| `(25,70,5)` | 350 | `106..119` | 130 | 350 |
| `(25,69,6)` | 559 | `117..132` | 156 | 559 |

Thus (1) independently closes the residual-cubic cell, with minimum gap
`86-75=11`, but it does not close any residual-degree-four, five, or six
cell.  It is a bankable structural theorem, not a full `M=213` closure.

The source-locked impact driver and its generic exact-state source are:

```text
work/explore_rank15_m213_covector_weight_impact.rb
  sha256=099fab039f0812b9aeb5dce7acdcdc588f43520074ef1ae358a6d6fcfe0e5be2
work/explore_rank15_m213_exact_localcost_driver.rb
  sha256=8cfcf7475dd153e5e101e0c97467d7d49b0336f902e806ce673dee13f8de533b
```

## 7. Exact hypotheses and failure modes

The proof uses all of the following, and none should be silently dropped.

1. **Isolated field zeros.**  This gives `gcd(P,Q)=1` and makes the Chern and
   local intersection lengths finite.
2. **Nonzero extactic factorization.**  The identity `K=unit*Fg` is
   load-bearing.
3. **Generic component avoidance.**  If `h=X(u)` shares a component with
   `Fg`, both the local polar argument and global Bezout can become improper.
4. **Ordinary reduced line intersection and `p` not dividing `m`.**  These
   give the Saito basis and the term `m c v^(m-1)` in (14).
5. **Tame characteristic (`p>q+1` suffices).**  It makes
   `n=i(P,u)<=deg(P)<=q+1` nonzero in `k`, so restriction and differentiation
   give `ord P_v(0,v)=n-1`.  In the target cells this follows already from
   `p>B>q+1`.

Concrete omitted-hypothesis checks:

* Without logarithmic tangency/Saito structure, `P=u-v^n` has
  `i(P,P_v)=n-1`; choosing `n<m-1` violates (12).
* In characteristic `p`, `P=u-v^p` has `P_v=0`; the polar is improper and
  the tame formula cannot be invoked.
* If `p|m`, the coefficient `m c` in (14) vanishes and
  `det(R,H)=-mF` is not a Saito basis identity.
* If the chosen `u=0` is an arrangement branch, (14) is false as stated.
  The finite forbidden-direction exclusion in Section 1 is therefore
  substantive, not cosmetic.
