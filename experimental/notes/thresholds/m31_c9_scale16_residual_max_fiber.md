---
workboard_item: "T"
row: "Mersenne-31 list auxiliary stress-test calibration"
object: "OTHER"
target_epsilon: "2^-100"
agreement: 1116023
B_star: 16777215
direct_statement: "On the complete weight-eight slice of sixteen derived T_(2^21) roots, after exact C1 antipodal-quotient deletion, every realized first-three-power-sum key has residual fiber at most two; exactly 384 keys have fiber two, and they are exactly complete-T_4 block swaps."
architecture: "DIRECT"
partition_digest: "N/A (DIRECT local C1-complement profile)"
atom_or_cell: "C9 / primitive-Q support fiber after exact C1 complete-fiber deletion"
quantifier: "all realized prefix keys in the exact sixteen-root C1-complement residual"
projection_and_unit: "support masks per first-three-power-sum prefix key; no slope/ray/codeword projection claimed"
claimed_bound: "max residual fiber = 2; minimal image-normalized residual loss = 2; integral natural-scale field remains 2 <= 1*2"
status: "PROVED finite census / COUNTEREXAMPLE_NEW_FLOOR"
impact: "ROUTE_CUT; acceptance criterion 4 primary and criterion 2 additionally"
falsifier: "canonical first doubled residual key (826664565,1588616718,1026140363) with masks 5903 and 6128"
replay: "python3 experimental/scripts/verify_m31_c9_scale16_residual_max_fiber.py --check; python3 -O experimental/scripts/verify_m31_c9_scale16_residual_max_fiber.py --check; python3 experimental/scripts/verify_m31_c9_scale16_residual_max_fiber.py --tamper-selftest"
---

# M31 C9 scale step: exact residual max fiber on sixteen deployed roots

## Status and acceptance gate

This packet performs one activity on one hard input: it **falsifies residual
injectivity at the next domain scale and replaces it by an exact constant-two
theorem**.

```text
Primary acceptance gate:   criterion 4
  statement-changing counterexample / new obstruction floor

Additional acceptance gate: criterion 2
  bound on the actual post-C1 survivor
```

The named terminal is

```text
M31_C9_SCALE16_T4_BLOCK_SWAP_RESIDUAL_LOSS_2.
```

The eight-root predecessor in upstream PR #1027 has an injective 64-support
residual after C1 deletion.  At sixteen roots the residual is no longer
injective.  The first growth is genuine but controlled:

```text
max residual fiber = 2,
exactly 384 residual keys have fiber 2,
every doubled residual key is a complete-T_4 block swap.
```

No deployed row atom is banked.  The result is a local, exact primitive-Q
support certificate and an obstruction floor for any scale-inductive
injectivity claim.

## 1. Source labels and statement type

The active proof authority is `experimental/grande_finale.tex` (Grande Finale
v4), especially:

- `def:primitive-q`, for the image-normalized max-fiber object;
- `lem:newton-equivalence`, for first-three power sums versus the first three
  locator coefficients on a fixed-weight slice;
- `eq:profile-envelope`, for the distinction between profile-local natural
  scale and the full row sum;
- `lem:profile-multiplicity`, for the separate fixed-outside/profile census;
- `hyp:ray-compiler`, for the separate support-to-ray obligation.

The live finite status authority is
`experimental/notes/frontier-adjacent/four_row_exact_completion_compiler_v1.md`,
Section 4.  It records `U_Q = null` on every deployed row.  This packet does
not replace that null by a row-global integer because it covers one fixed
local profile only and carries no received-line slope projection.

## 2. Exact norm-one derivation of four complete `T_4` blocks

Let

```text
p = 2^31 - 1 = 2,147,483,647
g = (1,717,986,917, 1,288,490,189) in F_p[i],  i^2 = -1.
```

The Lean module checks

```text
g * conjugate(g) = 1,
g^(2^30) = -1,
g^(2^31) = 1.
```

Use the four odd base exponents

```text
256, 768, 1280, 1792 = 256 * (1,3,5,7)
```

and, for each base, add `j*2^29` for `j=0,1,2,3`.  Taking the real coordinate
of the resulting norm-one powers gives the ordered domain

```text
  434373082,  614288294, 1713110565, 1533195353,
 1984437538,  380812851,  163046109, 1766670796,
 1244279234,  907334541,  903204413, 1240149106,
 2066813671, 1590029158,   80669976,  557454489.
```

The four consecutive blocks have exact `T_4` values

```text
1,884,637,334
   51,044,589
1,916,935,773
  116,752,674.
```

Every printed point is a root of `T_(2^21)`.  The eight antipodal pairs are

```text
(0,2), (1,3), (4,6), (5,7),
(8,10), (9,11), (12,14), (13,15).
```

Each complete four-point block has the same first-three-power-sum key

```text
(0,2,0).
```

The source does not trust the printed residues as assumptions:
`domain_derived_from_generator`, `domain_points_are_deployed_roots`,
`antipodal_pairs_exact`, and `t4_blocks_exact` are kernel-checked.

## 3. Complete weight-eight slice and exact C1 deletion

For a support mask `S` of Hamming weight eight, define

```text
Phi(S) = (sum_{x in S} x, sum_{x in S} x^2, sum_{x in S} x^3) in F_p^3.
```

The complete local slice has

```text
M_full = C(16,8) = 12,870.
```

The exact C1 complete-fiber owner is the antipodal quotient `x -> x^2`.
A weight-eight support is C1-owned exactly when it is the union of four of
the eight antipodal pairs.  Hence

```text
|C1| = C(8,4) = 70,
M_res = 12,870 - 70 = 12,800.
```

The residual is defined literally by filtering the complete slice, and Lean
proves the owner-complement equivalence

```text
S in residual
  <-> S in full slice and earlierOwner(S) = none.
```

## 4. Exact fiber spectrum

The complete and residual spectra are:

| slice | support mass | image size | singleton keys | doubled keys | sixfold keys | max fiber |
|---|---:|---:|---:|---:|---:|---:|
| full | 12,870 | 12,457 | 12,048 | 408 | 1 | 6 |
| post-C1 residual | 12,800 | 12,416 | 12,032 | 384 | 0 | 2 |

The unique sixfold full key is

```text
(0,4,0)
```

with masks

```text
255, 3855, 4080, 61455, 61680, 65280.
```

These are precisely the six unions of two complete `T_4` blocks and all are
deleted by C1.

The first repeated residual key in canonical ascending-mask order is

```text
z_grow = (826664565, 1588616718, 1026140363),
fiber(z_grow) = [5903, 6128].
```

In support-index form,

```text
5903 = {0,1,2,3,8,9,10,12},
6128 = {4,5,6,7,8,9,10,12}.
```

The common remainder is mask `5888 = {8,9,10,12}`.  The collision swaps the
first complete `T_4` block for the second and keeps the remainder fixed.

## 5. Classification of all 384 doubled residual keys

Choose two of the four complete `T_4` blocks.  On the eight coordinates outside
those blocks, choose a four-point remainder.  Replacing one selected block by
the other preserves the first three power sums because every complete block
has key `(0,2,0)`.

For a fixed block pair there are `C(8,4)=70` remainders.  Exactly
`C(4,2)=6` are unions of two of the four remaining antipodal pairs; those make
both resulting weight-eight supports C1-owned and are deleted.  Thus the
surviving candidate count is

```text
C(4,2) * (C(8,4) - C(4,2))
  = 6 * (70 - 6)
  = 384.
```

The exhaustive certificate proves that these 384 candidates give 384 distinct
keys and that their key set is exactly the set of doubled residual keys.
Therefore the first obstruction is not an unexplained collision cloud: it is
the terminal `T_4`-block-swap symmetry, with exact multiplicity two.

## 6. Exact normalization and the honest scale conclusion

For the residual,

```text
M = 12,800,
L = 12,416,
H = max fiber = 2.
```

A one-loss image-normalized inequality fails:

```text
H*L = 24,832 > 12,800 = M.
```

Loss two holds:

```text
H*L = 24,832 <= 25,600 = 2*M.
```

Hence the minimal integer image-normalized loss is exactly two.  This is the
new obstruction floor.

At the producer-style **integral** natural scale, however,

```text
ceil(M_full/L_full) = ceil(12,870/12,457) = 2,
ceil(M/L)           = ceil(12,800/12,416) = 2,
H <= 1 * 2.
```

Thus every surviving key still satisfies the literal small-constant field with
`compilerLoss = 1` and `naturalScale = 2`.  Both statements must be retained:
injectivity and real-average loss one fail, while the integer scale-two bound
survives.

## 7. Exact deployed-profile embedding

Using the same complement-side embedding as #1027, fix

```text
m - 8 = 981,121
```

outside complement points and choose eight points from the displayed
sixteen-root active set.  Availability is literal:

```text
981,121 <= 2,097,136 = 2^21 - 16.
```

With the outside locator fixed, the first three global locator coefficients
recover the first three active coefficients by the unitriangular product
identities.  Since `w=67,447 >= 3` and `p>3`, Newton equivalence identifies the
active coefficient fiber with the printed power-sum fiber.

This embeds the finite local obstruction into an exact fixed-outside deployed
profile.  It does not pay the number of outside profiles or prove that the
profile survives a row-global first-match atlas.

## 8. Validation boundary

Lean 4.31.0, stdlib only:

- one new module, `SidonEffectiveImage/M31C9ScaleStep.lean`;
- file-scope `maxRecDepth 1000000` and unbounded heartbeats;
- no `native_decide`;
- zero intended `sorry`, `admit`, `sorryAx`, custom axioms, unsafe
  declarations, or Mathlib imports;
- `#print axioms` for every load-bearing theorem.

The JSON verifier independently recomputes the norm-one domain, roots,
complete and residual enumerations, spectra, first collision, block-swap
classification, source blob pins, and mutation rejection.  Python is replay
only; fork Lean CI is the proof-validation gate.

## 9. Explicit nonclaims

- No row-global `U_Q` integer is banked.
- No fixed-before-line exhaustive C1--C8 owner function is proved.
- No received-line witness, `(SE2)` certificate, ray, slope, or codeword
  projection is constructed.
- No profile multiplicity, residual-to-full add-back, line-local `UNIF`, or
  summed adjacent-row certificate is proved.
- No import from `M31C9RowSharp`, `HalfSliceFalsifier`, or another open-PR
  module is used.
- No stable-paper theorem, safe agreement, official score, or prize claim is
  changed.
