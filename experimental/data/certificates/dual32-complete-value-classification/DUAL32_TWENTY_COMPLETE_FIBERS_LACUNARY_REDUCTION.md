# A 32-value phase has at least twenty complete cyclotomic fibers

## Result

Let `F` be a field whose characteristic does not divide

```text
n=2,097,152=32q,       q=65,536,
```

and suppose `H=mu_n subset F`.  Let `f in F[X]` be nonconstant of actual
degree

```text
q<=D<=67,471
```

and assume that `|f(H)|=32`.  For `c in f(H)` put

```text
E_c={x in H:f(x)=c},       e_c=|E_c|,
Q_c(X)=product_(x in E_c)(X-x),
delta_c=D-e_c.
```

Then:

1. at least twenty values `c` satisfy `delta_c=0`; equivalently,
   `f-c` is a scalar multiple of the squarefree divisor `Q_c` of
   `X^n-1` and has all `D` roots in `H`;
2. after writing `a` for the leading coefficient of `f`, the existence of
   any such complete fiber forces

```text
f(X)=aX^D+A(X),
deg A<=32D-n=32(D-q)<=61,920.                         (1)
```

Thus every deployed nonquotient 32-value phase is a lacunary polynomial
with at least twenty distinct additive shifts dividing `X^n-1`.  The
quotient solution `f=aX^q+b` has all thirty-two fibers complete.  This note
does not yet prove that it is the only solution.

## 1. Consecutive moment gap in every level locator

Put

```text
G=n-31D.
```

The deployed range gives

```text
G>=2,097,152-31*67,471=5,551>0.                       (2)
```

For a fixed value `c`, the Lagrange level idempotent

```text
I_c(X)=product_(b in f(H), b!=c) (f(X)-b)/(c-b)
```

has degree at most `31D=n-G`.  On `H` it is the indicator of `E_c`.
Fourier interpolation on `H` therefore gives

```text
sum_(x in E_c) x^j=0,       1<=j<=G-1.                (3)
```

Newton identities are invertible in the deployed characteristic and turn
(3) into the exact leading gap

```text
Q_c(X)=X^e_c + terms of degree at most e_c-G.          (4)
```

As usual, a negative upper degree means that the lower term is zero.

## 2. Residual factors share one leading coefficient string

Normalize `f` by its leading coefficient and put

```text
F_c=(f-c)/a=Q_c R_c,
```

where `R_c` is monic of degree `delta_c`.  All roots in `E_c` occur at
least once in `f-c`, so this factorization is literal even if a root is
ramified.  Moreover

```text
gcd(R_c,R_b)=1       for c!=b,                         (5)
```

because `f-c` and `f-b` differ by the nonzero constant `b-c`.

Write

```text
f/a=X^D+A_1 X^(D-1)+A_2 X^(D-2)+... .
```

For every `0<=j<G`, equation (4) shows that the coefficient at lag `j` in
`Q_cR_c` can only come from the leading monomial of `Q_c`.  Hence:

```text
[X^(delta_c-j)]R_c=A_j       if j<=delta_c,
A_j=0                        if delta_c<j<G.           (6)
```

Consequently, whenever

```text
delta_c<=delta_b<G,
```

the complete coefficient lists in (6) give

```text
R_b=X^(delta_b-delta_c) R_c.                           (7)
```

This is a polynomial identity, not merely a prefix congruence: both
residual degrees are below `G`.

## 3. At least twenty residuals are constant

The thirty-two fibers partition `H`, so

```text
sum_c delta_c=32D-n=32(D-q).                           (8)
```

Write `s=D-q`, where `0<=s<=1,935`.  Then

```text
sum_c delta_c=32s,       G=q-31s.
```

The exact endpoint inequality

```text
32s<12(q-31s)       for 0<=s<=1,935                  (9)
```

shows that at most eleven residual degrees can be at least `G`.  Thus at
least twenty-one values have `delta_c<G`.

Order those small residual degrees.  Apply (7) to the smallest one and any
other.  Pairwise coprimality (5) forces the smallest residual to be the
constant polynomial `1`.  Every other small residual is therefore a pure
power of `X`.  Two positive such powers would have a nonconstant gcd, again
contradicting (5).  Hence at most one of the at least twenty-one small
residuals has positive degree.  At least twenty satisfy

```text
R_c=1,       delta_c=0.                               (10)
```

This proves the first assertion.

## 4. Lacunary consequence

For a value satisfying (10), equation (4) applied to

```text
(f-c)/a=Q_c
```

shows that all coefficients of `f` at degrees `D-1,...,D-G+1` vanish.
Since

```text
D-G=D-(n-31D)=32D-n,
```

this is precisely (1).

## Scope

The theorem is source-valid for the Boolean-moment dual phase in
`DUAL_32_VALUE_GATE.md`.  It removes no signed Fourier aggregate by itself.
The remaining exact classification problem is now:

```text
f=aX^D+A,  deg A<=32(D-q),
at least twenty distinct c have f-c | X^n-1
    => ? D=q and A is constant.
```

That implication is not asserted here.

## Replay

Run

```text
ruby --disable-gems -w work/verify_dual32_twenty_complete_fibers_lacunary_reduction.rb
```

The verifier checks every deployed integer endpoint and the exact minimum
number of small and complete residuals supplied by the proof.
