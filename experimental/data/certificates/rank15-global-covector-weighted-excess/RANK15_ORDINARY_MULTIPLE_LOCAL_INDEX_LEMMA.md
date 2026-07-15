# Ordinary multiple-point local-index payment

## Lemma

Let `k` be algebraically closed and let `p=char(k)` be zero or prime to
`m>=3`.  At an ordinary `m`-fold point of a line arrangement, let a local
vector field `V` preserve all `m` branches and have an isolated zero.  If the
linear part of `V` is the zero scalar, then

```text
length k[[x,y]]/(V_x,V_y) >= m+1.                         (1)
```

Consequently the point consumes at least `m` units beyond its one support
unit in a global Chern zero count.  Since the point lies on exactly `m`
arrangement lines, the total number of lines forbidden by all non-simple
higher intersections is at most the total Chern excess `E`.

## Proof

Put `R=k[[x,y]]` and write the reduced homogeneous branch equation as

```text
f=prod_(i=1)^m ell_i.
```

Because `p` does not divide `m`, the logarithmic derivation module has the
Saito basis

```text
E=x partial_x+y partial_y,
delta=f_y partial_x-f_x partial_y,
det(E,delta)=-m f.                                        (2)
```

Thus

```text
V=A E+B delta.                                            (3)
```

Isolation implies `gcd(A,B)=1`; otherwise the common factor divides both
components of `V`.  Since `delta` has order `m-1>=2`, the scalar linear part
of `V` is `A(0) I`.  The zero-scalar hypothesis is therefore `A(0)=0`.

First suppose `A` is nonzero.  Choose a generic linear coordinate `x` such
that

1. `x=0` is not an arrangement branch;
2. the polar `f_y` is coprime to `A`;
3. `dx` is nonzero on the tangent vector of every branch.

Such a coordinate exists because the arrangement has finitely many branches
and factors, while `gcd(f_x,f_y)=1` for the reduced homogeneous `f` in the
present characteristic.  Write

```text
P=V(x)=Ax+Bf_y,             Q=V(y)=Ay-Bf_x.               (4)
```

All intersection numbers below are local at the origin.  Tangency and Euler's
identity give

```text
P f_x+Q f_y=mAf.
```

Intersecting with `P` yields

```text
I(P,Q)+I(P,f_y)=I(P,A)+I(P,f).                            (5)
```

Modulo `A`, equation (4) gives `P=Bf_y`; modulo `f_y`, it gives `P=Ax`.
The generic choices make the product intersections proper, hence

```text
I(P,A)=I(A,B)+I(A,f_y),
I(P,f_y)=I(A,f_y)+I(x,f_y).                               (6)
```

Since `x=0` is not a branch and `f` is homogeneous of degree `m`,

```text
I(x,f_y)=m-1.                                             (7)
```

For branch parametrizations `gamma_i(t)=t v_i`, write

```text
V(gamma_i(t))=lambda_i(t) gamma_i'(t).
```

The third generic-coordinate condition gives

```text
I(P,f)=sum_i ord_t lambda_i.                              (8)
```

Substitution of (6)--(8) into (5) proves the exact local formula

```text
ind_0(V)=I(P,Q)
        =sum_i ord_t lambda_i+I(A,B)-(m-1).               (9)
```

Because `A(0)=0`, restriction of (3) to every branch has the form

```text
lambda_i(t)=t A(gamma_i(t))+c_i t^(m-1) B(gamma_i(t)),
```

so every nonzero `lambda_i` has order at least two.  Isolation makes each
one nonzero.  Equation (9) therefore gives

```text
ind_0(V)>=2m-(m-1)=m+1.
```

If `A=0`, isolation forces `B` to be a unit.  Then `V` is a unit multiple of
`delta`, and

```text
ind_0(V)=I(f_x,f_y)=(m-1)^2>=m+1.                         (10)
```

This proves (1).

## Global conversion

Every arrangement intersection already contributes one support unit to the
global zero scheme.  If an ordinary `m`-fold intersection is non-simple,
(1) says its additional contribution is at least `m`.  Therefore

```text
sum_(non-simple P) valency(P)
 <=sum_(non-simple P)(local_length(P)-1)
 <=E.                                                     (11)
```

The earlier coarse term

```text
floor(E/3) max(15,m_residual,max)
```

may consequently be replaced by the sharp uniform payment `E`.  With `U`
the total restriction deficit and `D_double` the exact double-point count,
the corrected forbidden-line certificate is

```text
bad lines <= U+2D_double+E.                               (12)
```

The deployed characteristic `2,130,706,433` is larger than every arrangement
valency in the rank-15 census, so all characteristic hypotheses above hold.

