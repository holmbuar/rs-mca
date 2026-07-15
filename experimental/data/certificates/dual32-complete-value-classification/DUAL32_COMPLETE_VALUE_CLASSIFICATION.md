# Complete classification of deployed 32-value dual phases

## Theorem

Let

```text
p=2,130,706,433,
n=2,097,152=32q,       q=65,536,
H=mu_n subset F_p^*.
```

If a nonconstant polynomial `f in F_p[X]` has

```text
deg f<=67,471,       |f(H)|=32,
```

then, and only then,

```text
f(X)=aX^65,536+b       for a in F_p^*, b in F_p.      (1)
```

Thus the one-dimensional quotient line in `DUAL_32_AGGREGATE_INTERFACE.md`
is the complete 32-value Fourier major arc.  There is no nonquotient
32-value phase.

This is a classification theorem, not the signed estimate for phases having
at least 33 values.  The official one-row ceiling still requires that
nonquotient aggregate (or a direct max-fiber theorem).

## 1. Complete fibers and the lacunary form

Write `D=deg f`.  The elementary fiber-degree bound gives

```text
D>=ceil(n/32)=q.
```

By `DUAL32_TWENTY_COMPLETE_FIBERS_LACUNARY_REDUCTION.md`, at least twenty
value fibers are complete degree-`D` divisors of `X^n-1`.  In particular,
after dividing by the leading coefficient and rescaling the value set, one
has

```text
f(X)=X^D+A(X),
deg A<=Delta:=32D-n=32(D-q)<=61,920.                   (2)
```

Put

```text
G=n-31D=q-31(D-q).
```

In the deployed range,

```text
G>=5,551,
32G>Delta.                                             (3)
```

The first inequality is the consecutive moment gap.  For the second, write
`s=D-q<=1,935`; then `32G>Delta` is exactly `q>32s`, and
`65,536>61,920`.

## 2. Center the value polynomial

Let

```text
P(Y)=product_(c in f(H))(Y-c)
    =Y^32+p_1Y^31+... .
```

Translate `f` by `p_1/32` and translate `P` in the opposite direction.
This preserves degree, fiber sizes, complete divisibility, and (2), and it
makes the degree-31 coefficient of the new value polynomial zero.  Relabel
the centered pair as `f,P`.  Thus

```text
P(Y)=Y^32+p_2Y^30+...+p_32.                            (4)
```

Because `P(f)` vanishes on all simple roots of `X^n-1`, there is a monic
polynomial `E` of degree `Delta` such that

```text
P(f)=(X^n-1)E.                                         (5)
```

## 3. Reverse-polynomial contact of order `2D`

At infinity put

```text
B(z)=z^D f(z^-1),             B(0)=1,
C(z)=z^Delta E(z^-1),         C(0)=1.                 (6)
```

Both are ordinary polynomials, with

```text
deg B<=D,       deg C<=Delta.
```

Multiplying (5), after substituting `X=z^-1`, by `z^(32D)` and using
`n+Delta=32D` gives the exact identity

```text
B^32+p_2 z^(2D)B^30+p_3 z^(3D)B^29+...+p_32 z^(32D)
  =(1-z^n)C.                                           (7)
```

Since `n>2D`, equation (7) implies

```text
H_0(z):=B(z)^32-C(z)       is divisible by z^(2D).    (8)
```

This is the load-bearing use of centering: without removing `p_1`, the
contact order would only be `D`.

## 4. The differential rigidity

Differentiate (8) and eliminate the derivative of `B^32`:

```text
B H_0'-32B'H_0 = 32B'C-BC'.                            (9)
```

The left side is divisible by `z^(2D-1)`.  The right side has degree at
most

```text
D+Delta-1<2D-1.                                       (10)
```

It must therefore vanish identically:

```text
BC'=32B'C.                                             (11)
```

Factor over an algebraic closure.  If an irreducible factor occurs in `B`
with multiplicity `m` and in `C` with multiplicity `e`, valuation in (11)
gives

```text
e=32m.
```

A factor occurring on only one side is likewise impossible.  The relevant
multiplicities are below the characteristic, and `32` is invertible.  Since
`B(0)=C(0)=1`, it follows that

```text
C=B^32.                                                (12)
```

If `B` were nonconstant, (2) would make every nonconstant exponent of `B`
at least

```text
D-deg A>=D-Delta=G.
```

Hence `deg B>=G`, and (12) would give

```text
deg C=32 deg B>=32G>Delta,
```

contrary to `deg C<=Delta`.  Therefore

```text
B=1,
```

so the centered polynomial is exactly `f=X^D`.

## 5. Recover the exponent

The power map on the cyclic group `H` has image size

```text
|X^D(H)|=n/gcd(n,D).
```

This is 32, so `gcd(n,D)=q=2^16`.  But

```text
q<=D<=67,471<2q.
```

The only integer in this interval having gcd `2^16` with `2^21` is
`D=q`.  Undoing the centering, value scaling, and leading-coefficient
normalization gives (1).

Conversely, `aX^q+b` takes exactly the 32 values `b+a mu_32` on `H`, so
every polynomial in (1) is an extremizer.

## Exact interface and nonclaim

The theorem proves the previously conditional statement

```text
|f_alpha(H)|=32, alpha!=0
  iff f_alpha(X)=aX^65,536+b.
```

For the Boolean moment dual the constant term is invisible, leaving exactly
the character line `Q={a e_q}`.  The quotient contribution is therefore the
literal one already bounded in
`DUAL32_QUOTIENT_FIBER_CENTRAL_LATTICE_PAYMENT.md`.

No inequality for

```text
sum_(alpha notin Q) psi(-alpha dot z) C(alpha)
```

is proved here.  The official score remains unchanged until that signed
aggregate, or an equivalent direct list theorem, is paid.

## Replay

```text
ruby --disable-gems -w work/verify_dual32_complete_value_classification.rb
```

The verifier checks all deployed degree, gap, contact-order, and exponent
endpoints.  The algebraic proof is characteristic-free for
`char(F)>32D`; independent hostile audit must additionally test centering,
reverse-polynomial signs, and the valuation step.
