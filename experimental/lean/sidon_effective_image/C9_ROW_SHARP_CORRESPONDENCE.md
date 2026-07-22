# Sidon effective-image package: M31 C9 row-sharp correspondence

**Package:** `experimental/lean/sidon_effective_image/`

**Lean:** `v4.31.0`, stdlib only

**Status:** `PROVED SCOPED FINITE SOURCE / AWAITING_FORK_CI / CONDITIONAL GLOBAL USE`

## Source target

The package formalizes the finite content of
`experimental/notes/thresholds/sidon_effective_image_mi_ma_c9_rowsharp.md` and
is audited in
`experimental/notes/audits/sidon_effective_image_c9_rowsharp_preflight.md`.

The exact future producer field is

```text
(fullPrefixFiber leaf selectedKey).length
  <= compilerLoss * naturalScale.
```

`M31C9RowSharp.fullPrefixFiber_rowSharp` has that expression definitionally,
with `compilerLoss=1` and `naturalScale=2=ceil(70/69)`.

## Imported integrated APIs

| module | blob SHA on fork and upstream main |
|---|---|
| `AsymptoticSpine/PrimitiveBoolean.lean` | `777273e4377c31c815062769803622c6226988d3` |
| `AsymptoticSpine/EffectiveClosure.lean` | `9fb097e23d00e2f3ee3afeda021b86ba4192d2a4` |
| `AsymptoticSpine/UniformClosedLedger.lean` | `deda34063f4629e245c37ba03e3cb3ab70502570` |
| `M31QRootedShell/Deployed.lean` | `7e21ff098567d26aba7330fbb2722d5cb952fb09` |

No open-PR module is imported.

## Declaration map

| Lean declaration | Source statement |
|---|---|
| `fullPoints_complete` | complete four-subset slice on the eight active points |
| `residual_exact` | exact owner complement: full-slice membership and `earlierOwner=none` |
| `scoped_residual_exact` | concrete local C1 antipodal-quotient owner-complement instance |
| `generator_norm_one` | printed quadratic-extension generator has norm one |
| `generator_half_order`, `generator_full_order` | exact powers `g^(2^30)=-1`, `g^(2^31)=1` |
| `domain_points_are_deployed_roots` | eight points lie in the roots of `T_(2^21)` over M31 |
| `antipodal_pairs_exact` | exact four antipodal fibers of `x -> x^2` |
| `t4_fibers_exact` | exact two complete `T_4` fibers |
| `full_slice_card` | local source mass `70` |
| `full_image_card` | local realized prefix image `69` |
| `c1_owned_support_card` | exact C1 antipodal-quotient owner mass `6` |
| `c1_owned_supports_valid` | exact shape and duplicate-free owner census |
| `residual_slice_card` | exact C1 complement mass `64` |
| `residual_prefix_injective` | first three power sums injective on the residual |
| `collision_full_fiber_exact` | unique full collision consists of the two complete `T_4` blocks |
| `collision_residual_fiber_empty` | earlier C1 quotient ownership removes the collision |
| `selected_not_c1Owned` | selected support is outside the exact C1 quotient owner |
| `selected_full_prefix_singleton` | selected complete prefix fiber is one support |
| `selected_residual_prefix_singleton` | selected residual prefix fiber is one support |
| `fullPrefixFiber_rowSharp` | exact loss-one future producer field |
| `imageNormalized_rowSharp` | cleared image-normalized loss `1*69<=70` |
| `slopes_paid` | genuine SE2 support projection plus exact max-fiber chain |
| `payment` | direct C9 payment; no synthetic Sidon stage |
| `payment_assignedSlopes` | assigned slopes remain exactly the supplied SE2 slopes |
| `payment_naturalScale`, `payment_rayBudget` | exact integral scale and direct ray budget are two |
| `deployed_dimensions` | exact M31 `n,m,w` and fixed-profile feasibility arithmetic |
| `loss_one_fits_deployed_budget` | exact integral local charge two versus `B*=2^24-1` |

## Proof boundary

The Lean module proves finite modular arithmetic, complete finite enumerations,
exact list/fiber identities, the owner-complement equation, and the generic
SE2-to-payment implication.  It does not formalize:

- the norm-one-group derivation of the printed roots;
- the arbitrary fixed-outside polynomial-convolution argument;
- an exhaustive deployed C1--C8 owner function;
- an actual received-line SE2 certificate;
- global profile multiplicity, add-back, or UNIF;
- image-normalized Sidon or effective MI+MA;
- a completed deployed row.

The first two are proved at source level in the threshold note; the remaining
items are explicit nonclaims and named obligations.

## Build and axiom contract

No local Lean build is permitted.  The fork draft-PR build is authoritative.
The module ends with `#print axioms` for its load-bearing theorems.

Static source census before CI:

```text
sorry: 0
admit: 0
sorryAx: 0
custom axioms: 0
unsafe: 0
Mathlib: 0
```
