# M31 C9 scale step: exact T4-block swap doubling

```yaml
workboard_item: M1/T
row: Mersenne-31 list
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: On the exact sixteen-root weight-eight active slice, after the exact C1 antipodal-quotient deletion, the first realized residual prefix key has exactly two supports.
architecture: DIRECT
partition_digest: LOCAL_EXACT_C1_ANTIPODAL_COMPLEMENT_V1
atom_or_cell: C9 primitive prefix fiber, sixteen-root scale step
quantifier: complete weight-eight slice on the sixteen displayed deployed roots
projection_and_unit: supports per first-three-power-sum prefix key
claimed_bound: first residual fiber = 2; exhaustive replay residual maximum = 2
status: COUNTEREXAMPLE
impact: ROUTE_CUT
falsifier: any claim that the eight-root loss-one residual injectivity persists unchanged at sixteen roots
replay: python3 experimental/scripts/verify_m31_c9_scale_step.py --check
```

## Status

`COUNTEREXAMPLE_NEW_FLOOR`.

**Acceptance gate: criterion 4 — statement-changing counterexample / new obstruction floor.**

The named terminal is

```text
M31_C9_SCALE_STEP_T4_BLOCK_SWAP_DOUBLING.
```

The eight-root packet in upstream PR #1027 has an injective residual prefix map
after exact C1 antipodal-quotient deletion. At the next calibration—sixteen
roots, four complete `T_4` blocks, complete weight-eight slice—the first
residual key in canonical ascending-mask order already has a two-element fiber.
Thus loss-one injectivity does not survive scale.

The exact exhaustive census is stronger:

```text
full slice:
  supports = 12870
  realized keys = 12457
  fiber distribution = {1:12048, 2:408, 6:1}
  maximum fiber = 6

after exact C1 deletion:
  supports = 12800
  realized keys = 12416
  fiber distribution = {1:12032, 2:384}
  maximum fiber = 2
```

The Lean module kernel-checks the first doubled residual fiber and exact
domain/owner arithmetic. The certificate verifier independently recomputes the
complete distributions.

## 1. Exact domain derivation

Let

```text
p = 2^31 - 1,
g = (1717986917,1288490189) in F_p[i], i^2=-1.
```

The module checks

```text
g * conjugate(g) = 1,
g^(2^30) = -1,
g^(2^31) = 1.
```

For a norm-one element `u`, write `x(u)=(u+u^-1)/2`; in the chosen
representation this is the real coordinate. Use base exponents

```text
256, 768, 1280, 1792
```

and add `j*2^29`, `j=0,1,2,3`, to each. The resulting field elements are

```text
434373082,  614288294, 1713110565, 1533195353,
1984437538, 380812851,  163046109, 1766670796,
1244279234, 907334541,  903204413, 1240149106,
2066813671,1590029158, 80669976,  557454489.
```

All sixteen are distinct roots of `T_(2^21)`. Consecutive four-element blocks
are complete `T_4` fibers with values

```text
1884637334, 51044589, 1916935773, 116752674.
```

The exact antipodal pairs are

```text
(0,2), (1,3), (4,6), (5,7),
(8,10), (9,11), (12,14), (13,15).
```

Lean derives the displayed roots from the generator and separately checks the
Chebyshev recurrence and all antipodal equations.

## 2. Complete slice and exact C1 deletion

Encode an active support by a sixteen-bit mask. The full family is the complete
weight-eight slice

```text
Omega = {mask : popcount(mask)=8},
|Omega| = C(16,8)=12870.
```

The prefix key is

```text
Phi(S)=(sum x, sum x^2, sum x^3) in F_p^3.
```

The exact C1 owner is the antipodal quotient `x -> x^2`. A weight-eight support
is owned exactly when it is a union of four of the eight antipodal pairs. Hence

```text
|C1-owned| = C(8,4)=70,
|Omega_res| = 12870-70=12800.
```

The residual is literally the list filter `not c1Owned`; Lean proves

```text
S in Omega_res
  <-> S in Omega and earlierOwner(S)=none.
```

No support symmetry is called semantic ownership beyond this exact local C1
function.

## 3. The first doubled residual key

The first weight-eight mask is `255`, the union of the first four antipodal
pairs, and is deleted. The first support in the exact residual order is

```text
383 = {0,1,2,3,4,5,6,8}.
```

Its key is

```text
z*=(1625092085,1544193364,2053033192).
```

The full and residual fibers are both exactly

```text
Phi^-1(z*) = [383,61808],
61808 = {4,5,6,8,12,13,14,15}.
```

Both supports survive C1. They share the core

```text
{4,5,6,8}
```

and exchange the complete `T_4` blocks

```text
{0,1,2,3}  <->  {12,13,14,15}.
```

Both complete blocks contribute the same first-three-power-sum key

```text
(0,2,0).
```

Therefore the swap is invisible to the active prefix. This proves

```text
not (residualPrefixFiber(z*).length <= 1),
residualPrefixFiber(z*).length = 2.
```

The obstruction is not an average effect or an arbitrary collision: it is an
explicit complete-block exchange that survives the exact displayed owner.

## 4. Exhaustive fiber census

The stdlib verifier enumerates all `65536` masks, retains the `12870`
weight-eight supports, evaluates every prefix key with exact integer modular
arithmetic, and computes both full and residual histograms.

Before deletion:

```text
12048 keys have fiber 1,
  408 keys have fiber 2,
    1 key  has fiber 6.
```

After exact C1 deletion:

```text
12032 keys have fiber 1,
  384 keys have fiber 2.
```

Thus the residual maximum is exactly two on this slice. The Lean theorem is
narrower and kernel-checks the first exact doubled fiber; the verifier carries
the exhaustive maximum-two census.

## 5. Embedding at the deployed M31 list row

The active support is embedded into the complement-side profile with

```text
n = 2097152,
m = 981129,
w = 67447.
```

Fix `m-8=981121` complement points outside the sixteen active roots. The
availability gate is literal:

```text
981121 <= 2097136 = n-16.
```

For a fixed outside locator, equality of the full depth-`w` locator prefix
implies equality of the first three active locator coefficients by the usual
unitriangular product identities. Since `p>3`, Newton's triangular identities
identify those coefficients with the three power sums used here.

This embeds the collision in one exact fixed-outside profile. It does not count
all possible outside locators or prove that the profile survives every actual
C1-C8 owner.

## 6. Ledger impact

The local scale floor is now

```text
loss >= 2
```

for the displayed residual definition at sixteen roots. The constant itself is
numerically below the literal row budget,

```text
2 <= 16777215,
```

but that comparison is not a row allocation and does not bank `U_Q`.

A successor must do at least one of:

1. route complete-`T_4` block swaps to an earlier semantic owner;
2. accept and pay exact factor two at this scale; or
3. refine the prefix/residual so the pair no longer survives, while proving the
   revised first-match chronology.

A scale induction that simply copies the eight-root injectivity statement is
false.

## 7. Validation and replay

Lean module:

```text
experimental/lean/sidon_effective_image/
  SidonEffectiveImage/M31C9ScaleStep.lean
```

Certificate and verifier:

```text
experimental/data/certificates/m31-c9-scale-step/m31_c9_scale_step.json
experimental/scripts/verify_m31_c9_scale_step.py
```

Replay:

```text
python3 experimental/scripts/verify_m31_c9_scale_step.py --check
python3 -O experimental/scripts/verify_m31_c9_scale_step.py --check
```

The verifier is stdlib only. Lean is 4.31.0, stdlib only, no `native_decide`,
zero sorry and zero custom axioms. The package imports no predecessor/open-PR
module.

## 8. Explicit nonclaims

- No exhaustive fixed-before-line C1-C8 owner theorem for the full deployed row.
- No claim that C1 is the only earlier owner globally.
- No received word or line-level list/MCA numerator.
- No support-to-codeword, ray, or affine-slope projection.
- No profile multiplicity, residual add-back, UNIF, or exact row certificate.
- No bankable `U_Q` or allocation of the row budget.
- No statement beyond the displayed sixteen-root active slice.
- No stable-paper promotion, official score, or prize claim.
