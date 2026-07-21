# C9 row-sharp one-key preflight on the deployed Mersenne-31 domain

**Date:** 2026-07-21

**Status:** `PROVED SCOPED FINITE STATEMENTS / CONDITIONAL GLOBAL USE / AWAITING_FORK_CI / AUDIT`

**Lane:** hard input 3, exact-residual C9 row-sharp max-fiber.

## 1. Scope

This packet replaces the earlier normalization-floor activity on the lane with
one exact positive C9 instance.  It proves the literal full-prefix inequality
consumed by the C9 semantic-producer boundary for one deployed-domain profile
and one key:

```text
(fullPrefixFiber leaf selectedKey).length
  <= compilerLoss * naturalScale
```

with

```text
compilerLoss = 1,
naturalScale = 2 = ceil(70/69).
```

The residual condition is carried separately and literally:

```text
x in residual
  <-> x in the complete fixed-weight slice
      and earlierOwner x = none.
```

The module imports no file from upstream PR #1020 or any other open PR.  Its
future producer adapter uses the proved inequality as one field and leaves the
actual SE2 projection explicit.

## 2. Source pins and byte-identity audit

The candidate was prepared against:

| repository object | SHA |
|---|---|
| fork `holmbuar/rs-mca:main` | `b410c7ee14488bb751c5a89df10cb5b0323e3669` |
| upstream `przchojecki/rs-mca:main` | `18cfc199d4612f5dfc01bf6c0155a65a1eaa3832` |
| prior lane head used only as branch ancestor | `5bf3657f5b0d2aa9ad5917d556ff2f30ffa1de86` |
| `experimental/grande_finale.tex` blob | `759678e30639972e4f64b438d3d6ba76ff3ddf8f` |
| `experimental/rs_mca_thresholds.tex` blob | `01302a797c502a05ed0b11ba949b8756e0aa2b22` |

Every imported Lean API was fetched independently from fork main and upstream
main.  The blob SHAs agree byte-for-byte:

| imported API | fork blob | upstream blob | verdict |
|---|---|---|---|
| `experimental/lean/asymptotic_spine/AsymptoticSpine/PrimitiveBoolean.lean` | `777273e4377c31c815062769803622c6226988d3` | `777273e4377c31c815062769803622c6226988d3` | `BYTE_IDENTICAL` |
| `experimental/lean/asymptotic_spine/AsymptoticSpine/EffectiveClosure.lean` | `9fb097e23d00e2f3ee3afeda021b86ba4192d2a4` | `9fb097e23d00e2f3ee3afeda021b86ba4192d2a4` | `BYTE_IDENTICAL` |
| `experimental/lean/asymptotic_spine/AsymptoticSpine/UniformClosedLedger.lean` | `deda34063f4629e245c37ba03e3cb3ab70502570` | `deda34063f4629e245c37ba03e3cb3ab70502570` | `BYTE_IDENTICAL` |
| `experimental/lean/m31_q_rooted_shell/M31QRootedShell/Deployed.lean` | `7e21ff098567d26aba7330fbb2722d5cb952fb09` | `7e21ff098567d26aba7330fbb2722d5cb952fb09` | `BYTE_IDENTICAL` |

The open producer PR is used only as a statement target.  Its relevant field is
not imported.  No declaration from open PR #1015, #1019, #1020, or the older
semantic-owner PR stack is a dependency.

## 3. Source-label map

| packet object | active source node |
|---|---|
| complete fixed-weight slice and residual | `sec:primitive-leaf` |
| image scale | `eq:image-ambient-scales` |
| primitive max-fiber Q | `def:primitive-q` |
| moment/max interface | `lem:logmoment-q` |
| power-sum/locator equivalence | `lem:newton-equivalence` |
| exact row atom | `def:q-row-atom` |
| M31 full-budget target | `prop:q-exact-target` |
| moment-order warning | `prop:q-moment-order-floor` |
| separate support-to-slope interface | `(SE2)`, `hyp:ray-compiler`, `prop:q-sp-no-ray` |
| separate profile-count obligation | `lem:profile-multiplicity` |
| exact completion boundary | `thm:exact-completion-certificate` |

The packet makes no ambient/image substitution.  Its exact image-scale check is
`1*69<=70`, and its future producer field is the stronger integer inequality
`1<=1*2`.

## 4. Package and module layout

```text
experimental/lean/sidon_effective_image/
  .gitignore
  lean-toolchain
  lakefile.lean
  SidonEffectiveImage.lean
  SidonEffectiveImage/M31C9RowSharp.lean
  SOURCE_CORRESPONDENCE.md
```

The package is Lean `v4.31.0`, stdlib only.  It depends only on the integrated
sibling packages `asymptotic_spine` and `m31_q_rooted_shell`.  No
`lake-manifest.json`, `.lake/`, generated object, or workflow file is included.

## 5. Exact PROVED declaration table

Namespace: `SidonEffectiveImage.M31C9RowSharp`.

| declaration | exact statement and role |
|---|---|
| `fullPoints_complete` | `fullPoints` enumerates exactly all weight-four Boolean vectors on eight coordinates. |
| `fullPoints_nodup` | the complete slice has no duplicate supports. |
| `residual_exact` | for any owner label used as C1, membership in the displayed residual is equivalent to full-slice membership plus `earlierOwner=none`. |
| `scoped_residual_exact` | concrete local C1--C8 constructor grammar with only C1 nonempty satisfies the exact complement condition. |
| `generator_norm_one` | the printed `F_(p^2)` generator has norm one. |
| `generator_half_order`, `generator_full_order` | exact powers are `g^(2^30)=-1` and `g^(2^31)=1`, giving order `2^31`. |
| `domain_nodup` | the eight printed M31 field elements are distinct. |
| `domain_points_are_deployed_roots` | every printed point satisfies `T_(2^21)(x)=0 mod (2^31-1)`. |
| `antipodal_pairs_exact` | the four displayed pairs are exact `x -> x^2` fibers. |
| `t4_fibers_exact` | the first and last four points have the two printed constant `T_4` values. |
| `full_slice_card` | the complete active slice has `70` supports. |
| `full_image_card` | the first-three-power-sum image has `69` realized keys. |
| `c1_owned_support_card` | the scoped antipodal quotient owns exactly six complete-fiber supports. |
| `c1_owned_supports_valid` | those six supports are duplicate-free weight-four supports. |
| `residual_slice_card` | exact C1 quotient deletion retains `64` supports. |
| `residual_prefix_injective` | the residual key list is duplicate-free. |
| `collision_full_fiber_exact` | key `(0,2,0)` has exactly the two complete `T_4` blocks. |
| `collision_residual_fiber_empty` | exact C1 quotient deletion removes that collision fiber completely. |
| `selected_key_exact` | mask `51` has key `(1266428118,2,458186840)`. |
| `selected_not_c1Owned` | the selected mask contains no complete antipodal pair. |
| `selected_survives` | the selected support lies in the exact scoped residual. |
| `selected_not_earlier` | the scoped owner function returns `none` on the selected support. |
| `selected_full_prefix_singleton` | the complete full-prefix fiber at the selected key is exactly one support. |
| `selected_residual_prefix_singleton` | the corresponding residual fiber is the same singleton. |
| `fullPrefixFiber_rowSharp` | exact future producer field: `fullPrefixFiber.length <= 1*2`. |
| `imageNormalized_rowSharp` | cleared image-scale inequality `fullFiber*69<=70`. |
| `slopes_paid` | any genuine SE2 cell supported on the residual key has at most one slope. |
| `payment` | direct `.c9` `ProfilePayment 1`, with no synthetic Sidon stage. |
| `payment_owner` | the constructed payment owner is definitionally `.c9`. |
| `payment_assignedSlopes` | assigned slopes are exactly the supplied genuine SE2 slope list. |
| `payment_naturalScale`, `payment_rayBudget` | exact integral natural and ray budgets are both two. |
| `deployed_dimensions` | exact M31 values `w=67447`, `m=981129`, fixed outside size `981125`, availability, and `3<=w`. |
| `loss_one_fits_deployed_budget` | exact integer comparison `2<=16777215`. |

## 6. Definitionally aligned future adapter

After the producer module is integrated, the row-sharp field is filled by one
line:

```text
rowSharpMaxFiber :=
  SidonEffectiveImage.M31C9RowSharp.fullPrefixFiber_rowSharp
```

The remaining producer fields are not hidden by this packet:

```text
leaf               := SidonEffectiveImage.M31C9RowSharp.leaf,
earlierOwner       := SidonEffectiveImage.M31C9RowSharp.earlierOwner .c1,
residual_exact      := SidonEffectiveImage.M31C9RowSharp.residual_exact .c1,
syndromeKey         := SidonEffectiveImage.M31C9RowSharp.selectedKey,
rowSharpMaxFiber    := SidonEffectiveImage.M31C9RowSharp.fullPrefixFiber_rowSharp,
slopeCell           := a genuine SE2 certificate,
supportsInResidual  := its literal sublist proof,
naturalScale        := 2.
```

`slopes_paid` repeats the producer's intended chain on integrated APIs.  The
payment is direct because the max-fiber theorem is already supplied.

## 7. Kernel validation and axiom census

### Current state

```text
Fork draft-PR Lean compilation: AWAITING_FORK_CI
Local Lean build: NOT RUN
```

The project process makes the fork draft PR authoritative.  No local Lean build
or alternative compiler was used.

### Static source census before CI

```text
sorry: 0
admit: 0
sorryAx: 0
custom axiom declarations: 0
unsafe declarations: 0
Mathlib imports: 0
external packages: 0
```

The module ends with `#print axioms` for the exact residual theorem, deployed
root and `T_4` checks, residual injectivity, singleton key, row-sharp field,
image-normalized inequality, SE2 payment, deployed dimensions, and budget
comparison.

Green CI, once available, will prove compilation and kernel checking only.  It
will not establish the global semantic nonclaims below.

## 8. Statement audit

### Exact match

The declaration `fullPrefixFiber_rowSharp` has the same left- and right-hand
expression as the target producer field:

```text
(fullPrefixFiber leaf selectedKey).length
  <= compilerLoss * naturalScale.
```

No conversion theorem, arithmetic weakening, or polynomial multiplier is
inserted.  Here both printed factors are one.

### Residual discipline

The residual theorem is two-line and standalone.  It is not replaced by a
provenance tag, a support symmetry label, or the assertion that the selected
support “looks primitive.”  The concrete scoped owner function returns C1 on exactly the six unions of
two antipodal `x -> x^2` fibers and `none` otherwise.

### Slope discipline

No support cardinality is called an MCA numerator.  `slopes_paid` requires a
real `SE2Certificate` argument.  The code never constructs a dummy slope list
from the support list and never inserts a fake Sidon payment.

## 9. Explicit nonclaims

This packet does **not** prove:

- an exhaustive fixed-before-line C1--C9 atlas;
- that the scoped C1 quotient owner is the complete deployed-row owner function;
- survival of the selected support under every actual C1--C8 predicate;
- a row-wide theorem for all M31 prefix keys;
- a profile count for the fixed outside locator;
- residual-to-full add-back across all profiles;
- image-normalized Sidon, minor-arc, or major-arc estimates;
- a received-line SE2 certificate for every realized key;
- line-local UNIF, profile-envelope comparison, list-interior payment, or
  extension/quotient completion;
- an adjacent safe row, stable-paper theorem, official score, or prize claim.

## 10. Exact remaining obligation

```text
CONDITIONAL_ON_NAMED_INPUT:
M31_C9_GLOBAL_OWNER_COMPLEMENT_AND_KEY_COVERAGE
```

A closing packet must cover every actual surviving key at the deployed row with
loss-one row-sharp bounds or give an exact counterexample, while retaining the
actual owner function, SE2 projection, profile census, add-back, and line-local
sum.
