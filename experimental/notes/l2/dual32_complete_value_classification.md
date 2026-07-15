# Complete Classification of Deployed 32-Valued Dual Phases

## Claim

Let

```text
p=2,130,706,433,  n=2,097,152,  H=mu_n subset F_p^*.
```

If a nonconstant polynomial `f in F_p[X]` has `deg f<=67,471`, then

```text
|f(H)|=32
```

if and only if

```text
f(X)=aX^65,536+b  for a in F_p^*, b in F_p.
```

## Status

**PROVED / AUDIT.** The complete proof chain and two independent hostile
audits are frozen under
`experimental/data/certificates/dual32-complete-value-classification/`.
The Lean file is only an unproved statement target.

## Proof Chain

The first theorem proves that any deployed 32-valued phase has at least twenty
complete cyclotomic fibers and, after leading-coefficient normalization,

```text
f=X^D+A,  deg A<=Delta=32D-n.
```

For the centered degree-32 value polynomial `P`, reverse the identity
`P(f)=(X^n-1)E`. With

```text
B(z)=z^D f(z^-1),  C(z)=z^Delta E(z^-1),
```

centering removes the degree-31 coefficient and gives
`z^(2D) | (B^32-C)`. Differentiation and the strict degree gate force

```text
B*C_prime=32*B_prime*C,  hence C=B^32.
```

Every positive exponent of `B` is at least `G=n-31D`, while throughout the
deployed range

```text
32G-Delta>=115,712.
```

Thus `B=1`. The cyclic image-size calculation then forces `D=65,536`.

## Consumer

This makes the complete 32-value Fourier major arc exactly the
one-dimensional quotient line. There is no nonquotient 32-value phase.

## Exact Remaining Wall

No signed estimate is proved for phases with at least 33 values. The official
Boolean-moment fiber ceiling still needs the nonquotient signed aggregate, or
an equivalent direct max-fiber theorem. Value count `>=33` plus the individual
degree fiber cap is insufficient by itself.

## Replay

```bash
ruby --disable-gems -w experimental/scripts/verify_dual32_twenty_complete_fibers_lacunary_reduction.rb
ruby --disable-gems -w experimental/scripts/verify_hostile_audit_dual32_twenty_complete_fibers_lacunary_reduction.rb
ruby --disable-gems -w experimental/scripts/verify_dual32_complete_value_classification.rb
ruby --disable-gems -w experimental/scripts/verify_hostile_audit_dual32_complete_value_classification.rb
```
