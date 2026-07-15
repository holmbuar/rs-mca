# Hostile audit: complete classification of deployed 32-value phases

## Verdict

The proof in `DUAL32_COMPLETE_VALUE_CLASSIFICATION.md` is valid.  Its
classification

```text
|f(mu_(2^21))|=32, deg f<=67,471
  iff f=aX^65,536+b
```

follows from the independently audited complete-fiber/lacunary precursor.
The centering sign, reverse identity, `z^(2D)` contact, differential
valuation, and final degree inequality all survive hostile checking.

Source audited:

```text
DUAL32_COMPLETE_VALUE_CLASSIFICATION.md
sha256=5264d6d7a067513b7aa6124ac0a4e6915c9dd28a552194c8b8987ea920d3fd13
```

## 1. The centering sign

Write

```text
P(Y)=Y^32+p_1Y^31+... .
```

The exact centered pair is

```text
u=p_1/32,
f_c=f+u,
P_c(Y)=P(Y-u).                                        (1)
```

Then

```text
P_c(f_c)=P(f),
[Y^31]P_c=p_1-32u=0.                                  (2)
```

Thus “translate `P` in the opposite direction” in the source means the
substitution `Y -> Y-u`; it is not `P(Y+u)`.  Translation changes only the
constant term of the lacunary remainder `A`, so it preserves
`deg A<=Delta` and every fiber statement.

## 2. The reverse identity and its signs

After leading-coefficient normalization, put

```text
f=X^D+A,
Delta=32D-n,
B(z)=z^D f(z^-1),
C(z)=z^Delta E(z^-1).
```

Both reverse polynomials have constant term one.  Since

```text
f(z^-1)=z^-D B(z),
E(z^-1)=z^-Delta C(z),
z^-n-1=z^-n(1-z^n),
n+Delta=32D,
```

the centered identity `P(f)=(X^n-1)E` becomes exactly

```text
B^32+p_2z^(2D)B^30+...+p_32z^(32D)
  =(1-z^n)C.                                          (3)
```

There is no lost sign: the right side is `1-z^n`, not `z^n-1`.
Consequently

```text
B^32-C
 =-p_2z^(2D)B^30-...-p_32z^(32D)-z^nC.               (4)
```

The deployed inequality `n>2D` makes every term on the right divisible by
`z^(2D)`.  This proves the claimed contact order.

## 3. Differential elimination

Let `H_0=B^32-C`.  From `z^(2D)|H_0`, one has

```text
z^(2D-1) | B H_0'-32B'H_0
              =32B'C-BC'.                            (5)
```

But

```text
deg(32B'C-BC')<=D+Delta-1<2D-1                       (6)
```

because `Delta<D`.  Hence

```text
BC'=32B'C.                                            (7)
```

The degree comparison in (6) is strict by one on both sides and has no
endpoint leak.

## 4. Valuations in positive characteristic

Over an algebraic closure, let a linear factor have multiplicities `m` in
`B` and `e` in `C`.  If it occurs on both sides of (7), comparison of the
first nonzero local coefficients gives

```text
e=32m.                                                 (8)
```

A factor on only one side makes the lower-valuation side of (7) nonzero and
is impossible.  The only positive-characteristic escape would be a
multiplicity killed by the derivative.  It cannot occur here:

```text
deg B<=67,471<p,
deg C<=61,920<p,
32!=0 in F_p.
```

Thus all relevant `m,e` are strictly below `p`, and (8) is legitimate.
Since `B(0)=C(0)=1`, the scalar factor is one and

```text
C=B^32.                                                (9)
```

## 5. Final degree contradiction

From

```text
B=z^D f(z^-1)=1+z^D A(z^-1),
deg A<=Delta,
```

every positive exponent of `B` is at least

```text
D-Delta=n-31D=G.                                      (10)
```

If `B` is nonconstant, `deg B>=G`, so (9) gives

```text
deg C=32deg B>=32G.                                   (11)
```

At the worst deployed endpoint

```text
D=67,471,
Delta=61,920,
G=5,551,
32G-Delta=115,712>0.                                  (12)
```

Thus (11) contradicts `deg C<=Delta`.  The source's shorter calculation
`32G>Delta iff 65,536>32(D-65,536)` is exact throughout the interval.
Therefore `B=1`, the centered phase is `X^D`, and the cyclic image-size
calculation forces `D=65,536`.

## 6. Small cyclic regressions

The independent verifier exhausts monic lacunary polynomials

```text
f=X^D+A, deg A<=Delta=mD-n
```

on several proper cyclic subgroups over `F_41`, retaining only those with
exactly `m` values.  Every tested row satisfies the abstract proof gates

```text
char(F)>mD,
n>2D,
mG>Delta,
G=n-(m-1)D.
```

The quotient row `(n,m,D,Delta)=(8,4,2,0)` has exactly the expected 41
constant translates of `X^2`.  The exhaustive positive-`Delta` rows

```text
(8,3,3,1), (10,3,4,2), (20,3,7,1)
```

have no candidates, as the proof predicts.

As a hostile guardrail, over `F_7` the polynomial

```text
f=X^4+X^2
```

takes exactly two values on `F_7^*` and is nonmonomial after centering.  It
fails both indispensable gates `char(F)>mD` and `n>2D`; the verifier checks
that it is rejected.  This prevents silently generalizing the valuation and
contact argument outside their stated range.

## Scope

- **Passed:** the complete structural classification of 32-valued deployed
  phases.
- **Inherited input:** the complete-fiber/lacunary precursor, independently
  audited in
  `HOSTILE_AUDIT_DUAL32_TWENTY_COMPLETE_FIBERS_LACUNARY_REDUCTION.md`.
- **Not proved:** any signed estimate for phases having at least 33 values.
  The official score therefore does not move from this classification
  alone.

## Replay

Run

```text
ruby --disable-gems -w work/verify_hostile_audit_dual32_complete_value_classification.rb
```
