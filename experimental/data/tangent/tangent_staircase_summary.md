# New result: high-agreement tangent staircase

## Main theorem

Let `C = RS[F,D,k]`, `|D| = n`, and let `LD_sw(C,a)` denote the maximum number of
finite slopes on a received line that have a support-wise noncontained
explanation at agreement at least `a`.

For every `a` with `k+1 <= a <= n`, there is a generic moving-root construction
showing

```text
LD_sw(C,a) >= n-a+1.
```

If additionally

```text
3a - 2n >= k,
```

then this tangent floor is exact:

```text
LD_sw(C,a) = n-a+1.
```

The lower bound is obtained by fixing a locator `B_A(X)` for `a-1` points and
moving one remaining root `t`.  The high-degree part of `(X-t)B_A(X)` is affine
in `t`, producing `n-a+1` distinct finite slopes.  The upper bound uses two bad
slopes to recover a common code line on their support intersection, then applies
the common-code-line residual budget.

## Consequence for the `F_17^32`, `n=512`, `k=256` row

For

```text
C = RS[GF(17^32), H, 256], |H| = 512,
```

the exact staircase range starts at

```text
a >= ceil((2n+k)/3) = 427.
```

Therefore

```text
LD_sw(C,a) = 513-a for every a >= 427.
```

The target budget is

```text
floor(17^32 / 2^128) = 6.
```

Hence

```text
LD_sw(C,506) = 7  -> unsafe: epsilon_mca > 2^-128
LD_sw(C,507) = 6  -> tangent staircase is within budget
```

Equivalently, under the finite-slope support-wise MCA convention, the agreement
staircase is pinned between `506` and `507`.  The largest safe integer Hamming
radius is `5`; integer radius `6` is already unsafe.  The normalized grid radii
are `5/512` and `6/512 = 3/256`.

## Effect on the previous agreement-353 target

Agreement `353` is not a frontier.  The moving-root tangent floor already gives

```text
LD_sw(C,353) >= 512 - 353 + 1 = 160.
```

The new target is to decide whether any non-tangent mechanism can survive past
agreement `507`.
