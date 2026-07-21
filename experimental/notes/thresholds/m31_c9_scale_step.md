# M31 C9 scale step: exact T4-block swap doubling

```yaml
workboard_item: M1/T
row: Mersenne-31 list
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: On the exact sixteen-root weight-eight active slice, after exact C1 antipodal-quotient deletion, the first realized residual prefix key has two distinct supports.
architecture: DIRECT
partition_digest: LOCAL_EXACT_C1_ANTIPODAL_COMPLEMENT_V1
atom_or_cell: C9 primitive prefix fiber, sixteen-root scale step
quantifier: complete weight-eight slice on the sixteen displayed deployed roots
projection_and_unit: supports per first-three-power-sum prefix key
claimed_bound: first residual fiber = 2; exhaustive replay residual maximum = 2
status: COUNTEREXAMPLE
impact: ROUTE_CUT
falsifier: any claim that eight-root loss-one residual injectivity persists unchanged at sixteen roots
replay: python3 experimental/scripts/verify_m31_c9_scale_step.py --check
```

## Status

`COUNTEREXAMPLE_NEW_FLOOR`.

**Acceptance criterion 4:** statement-changing counterexample / new obstruction
floor.

**Named terminal:**

```text
M31_C9_SCALE_STEP_T4_BLOCK_SWAP_DOUBLING
```

Upstream PR #1027 proved an injective residual prefix map on eight roots after
exact C1 antipodal-quotient deletion. At the next scale—sixteen roots, four
complete `T_4` blocks, and the complete weight-eight slice—the first residual
key already has two supports. Loss one therefore does not persist unchanged.

## Exact domain

Let `p=2^31-1` and

```text
g=(1717986917,1288490189) in F_p[i], i^2=-1.
```

Lean checks `Norm(g)=1`, `g^(2^30)=-1`, and `g^(2^31)=1`. From base exponents
`256,768,1280,1792` and quarter turns `j*2^29`, it derives exactly

```text
434373082,  614288294, 1713110565, 1533195353,
1984437538, 380812851,  163046109, 1766670796,
1244279234, 907334541,  903204413, 1240149106,
2066813671,1590029158, 80669976,  557454489.
```

All are distinct roots of `T_(2^21)`. The consecutive four-point blocks have
constant `T_4` values

```text
1884637334, 51044589, 1916935773, 116752674.
```

The exact antipodal pairs are `(0,2),(1,3)` inside each block.

## Complete slice and exact C1 complement

A support is a sixteen-bit mask of weight eight. Its active prefix is

```text
Phi(S)=(sum x, sum x^2, sum x^3) in F_p^3.
```

The local C1 owner holds exactly when every antipodal pair is wholly selected or
wholly unselected. On the weight-eight slice these are the `C(8,4)=70` unions
of four antipodal pairs. The Lean residual predicate is the literal Boolean
complement and proves, for an arbitrary C1 label,

```text
IsResidual(S)
  <-> IsFullSupport(S) and earlierOwner(S)=none.
```

## First doubled key

The first residual mask in ascending order is

```text
S0=383={0,1,2,3,4,5,6,8}.
```

Its distinct mate is

```text
S1=61808={4,5,6,8,12,13,14,15}.
```

Both survive C1 and have the same key

```text
z*=(1625092085,1544193364,2053033192).
```

They share `{4,5,6,8}` and exchange complete blocks `{0,1,2,3}` and
`{12,13,14,15}`. Each exchanged block contributes `(0,2,0)`, so the prefix is
unchanged.

Lean kernel-checks that both masks are distinct full supports, both satisfy the
exact residual predicate, both have key `z*`, and no smaller mask survives. It
therefore proves residual prefix noninjectivity and an explicit two-witness
fiber floor.

The independent exhaustive verifier strengthens the witness to

```text
fullPrefixFiber(z*)     = [383,61808],
residualPrefixFiber(z*) = [383,61808].
```

## Exhaustive census

The verifier enumerates all `65536` masks and recomputes the exact distributions:

```text
full slice:
  supports = 12870
  keys = 12457
  histogram = {1:12048,2:408,6:1}
  maximum = 6

exact C1 complement:
  supports = 12800
  keys = 12416
  histogram = {1:12032,2:384}
  maximum = 2
```

Replay:

```text
python3 experimental/scripts/verify_m31_c9_scale_step.py --check
python3 -O experimental/scripts/verify_m31_c9_scale_step.py --check
```

## Deployed embedding and impact

At the M31 list row,

```text
n=2097152, m=981129, w=67447.
```

Fixing `m-8=981121` outside points is available because
`981121<=2097136=n-16`. For one such fixed outside locator, Newton's triangular
relations transport equality of the three active power sums into equality of
the corresponding full locator-prefix coordinates.

The local floor is therefore factor two under this exact residual definition.
The literal comparison `2<=16777215` is true but is not a row allocation and
does not bank `U_Q`.

A successor must route complete-`T_4` block swaps earlier, accept and pay the
factor-two loss, or prove a stronger prefix/residual chronology that removes the
pair.

## Explicit nonclaims

- No exhaustive deployed C1-C8 owner function.
- No claim that C1 is the only earlier owner globally.
- No received word, line, codeword, ray, affine slope, list numerator, or MCA
  numerator.
- No bankable row atom, profile census, add-back, SE2, ray compiler, or UNIF.
- No theorem beyond the displayed sixteen-root active slice.
- No adjacent-row certificate, stable-paper theorem, score, or prize claim.
