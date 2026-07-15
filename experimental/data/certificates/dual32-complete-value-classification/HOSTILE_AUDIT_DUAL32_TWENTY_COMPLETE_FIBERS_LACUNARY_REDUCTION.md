# Hostile audit: twenty complete fibers and residual nesting

## Verdict

The residual nesting and coprimality step in
`DUAL32_TWENTY_COMPLETE_FIBERS_LACUNARY_REDUCTION.md` is valid.  The shipped
verifier for that note checks only the deployed integer envelope, so this
audit separately checks the polynomial argument and exhausts small cyclic
analogues.

The strict inequality in the nesting hypothesis is load bearing:

```text
delta_c < G.
```

At the boundary `delta_c=G`, a residual is not determined by the common
leading string.  The exhaustive `F_7^*` analogue contains the profile
`(delta_1,delta_2)=(0,G)` and therefore tests this boundary explicitly.

## 1. The lag indexing is exact

Write

```text
Q_c=X^e + terms of degree <=e-G,
R_c=X^delta+r_1 X^(delta-1)+...+r_delta,
(f-c)/a=Q_cR_c
     =X^D+A_1X^(D-1)+A_2X^(D-2)+... .                 (1)
```

Every nonleading term of `Q_c` is at lag at least `G`.  Therefore, for
every `0<=j<G`, the coefficient at lag `j` in the product in (1) receives
exactly one contribution, from the leading `X^e` term of `Q_c`:

```text
r_j=A_j                    when j<=delta,
A_j=0                      when delta<j<G.             (2)
```

There is no omitted convolution term.  If
`delta_c<=delta_b<G`, equations (2) specify every coefficient of both
residuals and give

```text
R_b=X^(delta_b-delta_c)R_c.                            (3)
```

This is a full polynomial identity because the larger residual degree is
strictly below `G`.

## 2. Ramification does not break coprimality

The locator `Q_c` contains each deployed fiber root once.  If such a root is
ramified for `f-c`, the extra copy is legitimately left in `R_c`.  This
does not weaken the gcd step.  Any common divisor of `R_c` and `R_b` also
divides

```text
(f-c)/a and (f-b)/a,
```

whose difference is the nonzero constant `(b-c)/a`.  Hence

```text
gcd(R_c,R_b)=1                                         (4)
```

without a squarefreeness assumption on the residuals.

Combining (3)--(4), the smallest residual among the `delta<G` cells must be
`1`; every other such residual is a pure power of `X`; and at most one can
have positive degree.  The note's count of at least twenty complete fibers
therefore follows from its independently correct integer ledger.

## 3. Exhaustive cyclic analogues

The verifier scans every monic polynomial of degree at most four over

```text
F_7, F_11, F_13
```

on the full cyclic evaluation group `F_p^*`.  For degree `D`, it retains the
exact value-set extremizers

```text
|f(F_p^*)|=ceil((p-1)/D)
```

with positive gap

```text
G=(p-1)-(|V|-1)D.
```

For every retained polynomial and every value fiber it independently:

1. constructs the fiber locator and divides `f-c` by it;
2. checks the consecutive moment gap through `G-1`;
3. checks pairwise residual coprimality;
4. checks the complete common leading coefficient string;
5. checks (3) for every ordered pair with degrees below `G`.

The exhaustive profiles are

```text
F_7 : 42 extremizers,
F_11: 22 extremizers,
F_13: 52 extremizers.
```

The `F_7`, degree-four row has value-set size two, gap `G=2`, and residual
profile `[0,2]` for 21 normalized polynomials.  It produces no false
nesting at equality and confirms that the proof must retain `<G`, not
`<=G`.

## Scope

- **Passed:** residual factor construction, lag indexing, full nesting below
  `G`, ramification-safe coprimality, and the deployed arithmetic count.
- **Not claimed:** that the twenty-complete-fiber theorem closes the
  32-value classification.  It supplies the lacunary residual stated in the
  source note and nothing stronger.

## Replay

Run

```text
ruby --disable-gems -w work/verify_hostile_audit_dual32_twenty_complete_fibers_lacunary_reduction.rb
```
