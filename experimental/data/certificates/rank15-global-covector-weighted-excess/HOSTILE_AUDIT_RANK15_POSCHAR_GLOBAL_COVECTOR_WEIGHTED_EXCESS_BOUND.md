# Hostile audit: global-covector weighted excess bound

## Verdict

**ACCEPT (high confidence)** for
`RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS_BOUND.md` at audited SHA-256

```text
6f998929209b534d39cb0d31fa6458f5bf63d9326255ec31e7f0f64ae7a5389e.
```

Under its stated hypotheses, the proof establishes the genuinely stronger
universal inequality

```text
E+S=2E-U <= (3q-B)(q+1).                                 (A)
```

The proof does not classify the residual divisor and does not require it to
be reduced. Its decisive new ingredient is the ordinary-point polar payment
`i(P,P_v)>=m-2`. The argument was reconstructed independently below; the
exact five-cell replay was also rerun from the source-locked enumerator.

## 1. One affine covector satisfies all global requirements

First choose a line `L_infinity` which contains none of the finitely many
field zeros and is not one of the finitely many components of `fg`. Every
component of `fg` then has a dense affine part on which `X` is nonzero at a
general point, because the zero scheme of `X` is finite.

Constant affine covectors form a two-dimensional space. For an irreducible
component `C` of `fg`, the condition `du(X)|_C=0` is linear and proper: at an
affine point `x in C` with `X(x)!=0`, constant covectors span the cotangent
fiber and one detects `X(x)`. For each arrangement-line tangent direction,
the condition that `du` kill it is also one proper one-dimensional subspace.
Avoiding the finite union gives a single nonzero `du` such that simultaneously

```text
h=X(u) shares no component with fg,
du is nonzero on every arrangement-line tangent direction.             (1)
```

A complementary affine-linear coordinate `v` then exists. The projective
section `z d(ell)-ell dz` restricts to `du`, so its contraction with
`X in H^0(T(q-1))` is a genuine global section of `O(q+1)`. Thus the affine
choice neither loses the projective line at infinity nor changes the degree
of `h`.

This also handles arrangement components repeated inside `g`: (1) is imposed
on the reduced support of the entire product `fg`, while Bezout later retains
the multiplicity.

## 2. Exact local identity and every properness condition

At a field zero, translate the affine coordinates and write

```text
X=P partial_u+Q partial_v,       P=X(u)=h,
I=(P,Q),                         mu=length O/I.
```

If `F` is the product of the `m` incident arrangement branches (`F=1` off
the arrangement), the extactic identity is, up to a local unit,

```text
Fg=K=P X(Q)-Q X(P).
```

Modulo `P`, since `X(P)=P P_u+Q P_v`,

```text
Fg=-Q^2 P_v mod P.                                      (2)
```

All four intersections used after (2) are proper.

* `gcd(P,Q)=1` because the field zero is isolated.
* `gcd(P,F)=gcd(P,g)=1` because the global choice makes `h=P` share no
  component with `fg`.
* If an irreducible branch `D` divided both `P` and `P_v`, equation (2)
  would imply `D|Fg`, contradicting the preceding item. Hence
  `gcd(P,P_v)=1`.

Additivity of proper plane-curve intersection multiplicity applied to (2)
therefore gives the exact identity

```text
i(P,g)=2mu+i(P,P_v)-i(P,F).                              (3)
```

The local unit relating `K` and `Fg` has intersection number zero and does
not alter (3).

## 3. Exact localization of `E`, `U`, and the weighted summand

Let `e` be the local contribution to `E` and `u_0` the local line-restriction
contribution to `U`. The choice that `du` does not kill any arrangement-line
tangent makes the order of `P=X(u)` on each incident line equal to the
intrinsic restriction order.

The complete table is

| stratum | `e` | `u_0` | `w=2e-u_0` |
|---|---:|---:|---:|
| off arrangement, `m=0` | `mu` | `0` | `2mu` |
| one smooth arrangement line, `m=1` | `mu` | `i(P,F)` | `2mu-i(P,F)` |
| arrangement intersection, `m>=2` | `mu-1` | `i(P,F)-m` | `2mu-i(P,F)+m-2` |

At an intersection, the last row follows from

```text
i(P,F)=sum_j r_j,
u_0=sum_j(r_j-1)=i(P,F)-m.
```

Summing gives `sum e=E`, `sum u_0=U`, and hence `sum w=2E-U=E+S` exactly.
There is no extra subtraction at a smooth point and no missing support unit
at a crossing.

Subtracting the table from (3) shows

```text
i(P,g)-w = i(P,P_v)                 for m=0,1,
i(P,g)-w = i(P,P_v)-(m-2)           for m>=2.             (4)
```

Thus nonnegativity handles `m=0,1,2`; only `m>=3` needs a new estimate.

## 4. Ordinary-point polar estimate

At an ordinary `m`-fold point, `m<=B<p` permits the Saito basis

```text
R=u partial_u+v partial_v,
H=F_v partial_u-F_u partial_v,
det(R,H)=-mF.
```

Writing `X=AR+CH` gives

```text
P=X(u)=Au+C F_v.                                         (5)
```

The line `u=0` is not an arrangement branch by the tangent-direction choice.
Thus, for a nonzero constant `c`,

```text
F(0,v)=c v^m,
P(0,v)=m c C(0,v)v^(m-1).                               (6)
```

The restriction `C(0,v)` is not identically zero. Otherwise `u|C`, and (5)
would make `u|P` and `u|P_v`; then (2), with `u` absent from `F`, would force
`u|g`, contrary to `gcd(P,g)=1`. Therefore

```text
n:=ord_v P(0,v)=i(P,u)>=m-1.                             (7)
```

The characteristic guard is exactly strong enough. The global contraction
has degree `q+1`, so its dehomogenization `P` has affine degree at most
`q+1`. Since `P(0,v)` is nonzero,

```text
n<=deg P<=q+1<p.                                         (8)
```

Consequently the coefficient `n` survives differentiation and
`ord_v P_v(0,v)=n-1`.

Set `M=O/(P,P_v)`. Section 2 proves that `M` has finite length. Passing to a
quotient cannot increase length, and direct reduction modulo `u` gives

```text
length M
 >=length M/uM
 =length k[[v]]/(P(0,v),P_v(0,v))
 =n-1.                                                    (9)
```

Equations (7)--(9) yield

```text
i(P,P_v)>=n-1>=m-2,                                      (10)
```

which is precisely the missing case in (4). This Artin-quotient proof is
valid in the stated tame positive characteristic and does not import a
characteristic-zero Teissier formula.

## 5. Points where `g` is a unit and the global sum

Every field zero lies on `fg`, but it need not lie on `g`. If `g` is a local
unit, define `i(P,g)=0`. The proved local inequality then forces `w<=0`;
such a point may have a negative weighted local summand, but it does not
invalidate the sum. Termwise,

```text
sum_(field zeros) w <= sum_(field zeros) i(P,g).
```

The right-hand summands are nonnegative and supported on a subset of the
complete intersection `V(g,h)`. Since `g,h` have no common component,
scheme-theoretic Bezout, including repeated components of `g`, gives

```text
E+S
 <=sum_(Z in V(g,h)) i_Z(g,h)
 =deg(g)deg(h)
 =(3q-B)(q+1).
```

No unjustified deletion of a negative `w` occurs: all `w` are retained on
the left, while the nonnegative intersection lengths are enlarged on the
right.

## 6. Independent exact replay

The hash-locked impact wrapper was rerun live against
`explore_rank15_m213_exact_localcost_driver.rb` at SHA-256
`8cfcf7475dd153e5e101e0c97467d7d49b0336f902e806ce673dee13f8de533b`.
The exact results match the theorem table:

| `(q,B,a)` | raw | `W` range | cap | survivors |
|---|---:|---:|---:|---:|
| `(24,69,3)` | 12,607 | `86..120` | 75 | 0 |
| `(24,68,4)` | 16,027 | `96..132` | 100 | 919 |
| `(25,71,4)` | 225 | `95..107` | 104 | 215 |
| `(25,70,5)` | 350 | `106..119` | 130 | 350 |
| `(25,69,6)` | 559 | `117..132` | 156 | 559 |

Therefore the theorem closes the residual-cubic cell `q24/B69` with exact
minimum gap `86-75=11`. It does not close the other four replayed cells.

## 7. Scope and hypothesis guards

The following are load-bearing: isolated zeros; nonzero extactic
factorization; one covector avoiding every component of `fg`; an ordinary
reduced line arrangement; `p>B` so `m` is invertible; and `p>q+1` so the
leading order `n` does not disappear under differentiation. Dropping the
tame characteristic guard permits the standard failure `P=u-v^p`, for which
`P_v=0`. Dropping component avoidance destroys both the local properness and
global Bezout steps.

