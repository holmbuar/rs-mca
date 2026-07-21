# C8/C9 semantic-producer port onto the integrated asymptotic spine

**Date:** 2026-07-21  
**Status:** `PROVED FINITE INTERFACE / CONDITIONAL GLOBAL USE / AUDIT`  
**Authority:** `agents.md`, `experimental/grande_finale.tex`, and the integrated
stdlib-only package `experimental/lean/asymptotic_spine`.  
**Port base:** fork `main` at
`b410c7ee14488bb751c5a89df10cb5b0323e3669`.  
**Source packet:** fork commit
`8ed92c753633398bfd5ba9fc7f042ac0f1c5cf6b`.

## Purpose and adaptation

This packet ports the unshipped C8/C9 producer unit after the integrated
closed-ledger interface and the reviewed narrow C7 bridge.  It adds only the
following modules:

```text
AsymptoticSpine/ClosedLedgerExtension.lean
AsymptoticSpine/C8ShallowClosureProducer.lean
AsymptoticSpine/C9ResidualMaxFiberProducer.lean
```

The package root imports those modules and the package README records their
proof boundary.  No integrated Lean file is rewritten, no declaration under
`m31_q_rooted_shell` is touched, and no pre-narrowing C7 declaration is
restored.

The four imported APIs used by the source packet are byte-identical between the
source commit and the port base:

| imported module | blob SHA on source and port base |
| --- | --- |
| `UniformClosedLedger.lean` | `deda34063f4629e245c37ba03e3cb3ab70502570` |
| `HighKappaCoverage.lean` | `cdb17177fe7f17a7e8b520d999fa925c5abfaea0` |
| `PrimitiveBoolean.lean` | `777273e4377c31c815062769803622c6226988d3` |
| `EffectiveClosure.lean` | `9fb097e23d00e2f3ee3afeda021b86ba4192d2a4` |

Thus no open pull request is a dependency.  In particular, this packet neither
imports nor recreates the broader pre-narrowing C7 stack.  Its C8 nonclaims
match the reviewed high-kappa compiler boundary: an actual shortening
certificate, a high-kappa semantic owner, and chart exhaustion remain external
inputs.

## Source-theorem boundary

The formalization is an adapter at the exact boundaries already separated in
Grande Finale v3:

- the ray interface and its nonautomatic nature are printed in
  `hyp:ray-compiler`, `prop:q-sp-no-ray`, and
  `prop:curve-degree-ray-compiler`;
- the paid one-parameter C8 model is `thm:bc-moving-root` and
  `cor:bc-one-pencil`;
- primitive max-fiber control is `def:primitive-q` and
  `lem:logmoment-q`;
- the deployed row-sharp target is `def:q-row-atom` and
  `prop:q-exact-target`; and
- subexponential profile multiplicity is a separate hypothesis in
  `lem:profile-multiplicity`.

The Lean modules do not strengthen any of those statements.  They formalize
how supplied C8 or C9 inputs become one `ProfilePayment` and how that payment is
appended to one already closed received line.

## 1. Shared one-profile closed-ledger extension

Namespace: `AsymptoticSpine.ClosedLineLedger`.

### Exact PROVED declarations

| declaration | exact statement |
| --- | --- |
| `assignedSlopeList_nodup` | The flattened assigned-slope list of a `ClosedLineLedger` is `Nodup`. |
| `listSum_append_extension` | For natural-number lists, `listSum (xs ++ ys) = listSum xs + listSum ys`. |
| `appendPayment` | Given one paid profile and explicit disjointness from every earlier assigned slope, constructs a ledger with profile cap increased by one, bad count increased by the new assigned-slope length, preserved first-match ownership, preserved numerical atlas coverage, and the enlarged profile-count bound. |
| `assignedSlopeList_appendPayment` | The new flattened slope list is exactly `earlier ++ profile.assignedSlopes`. |
| `appendPayment_budgetTotal` | The new line-local budget is exactly `line.budgetTotal + profile.rayBudget`. |
| `appendPayment_naturalTotal` | The new line-local natural total is exactly `line.naturalTotal + profile.naturalScale`. |
| `extensionToy_assignedSlopes` | The finite fixture appends `[7,9]` after `[4]`, giving `[4,7,9]`. |
| `extensionToy_totals` | The finite fixture has exact budget total `4` and exact natural total `2`. |

This module is bookkeeping.  The explicit cross-owner disjointness argument is
not inferred from support deletion, and `appendPayment` does not construct the
profile's semantic owner or prove its payment.

## 2. C8 shallow-prefix residual producer

Namespace: `AsymptoticSpine.C8ShallowClosure`.

### Input object

`ProfileData Support Eff Raw` carries:

1. a `PrefixFiberBridge`;
2. one effective syndrome key;
3. an `(SE2)` distinct-slope certificate;
4. proof that the selected supports form a sublist of the reindexed ambient
   prefix chart;
5. `ShallowPrefixClosureBounds` for the full ambient slice; and
6. a residual-kernel-dimension label.

The compiler loss and natural scale are definitionally

```text
compilerLoss = baseSize ^ prefixDepth,
naturalScale = 1 + average.
```

### Exact PROVED declarations

| declaration | exact statement |
| --- | --- |
| `ProfileData.slopes_paid` | `slopeCell.slopes.length <= compilerLoss * naturalScale`, obtained from `balancedCoreShallowClosure_to_directRC`; the proof is independent of the printed kernel-dimension label. |
| `ProfileData.payment` | Constructs `ProfilePayment compilerLoss` by `ProfilePayment.ofDirect .c8` from the supplied slope list and the preceding inequality. |
| `ProfileData.payment_owner` | The constructed owner is exactly `.c8`. |
| `ProfileData.payment_assignedSlopes` | The assigned slopes are exactly `slopeCell.slopes`. |
| `ProfileData.extendLine` | Appends the C8 payment after an earlier closed line, assuming explicit slope-level cross-disjointness. |
| `ProfileData.extendLine_budgetTotal` | The exact new budget is `line.budgetTotal + compilerLoss * naturalScale`. |
| `ProfileData.extendLine_naturalTotal` | The exact new natural total is `line.naturalTotal + naturalScale`. |
| `fixture_assignedSlopes` | With kernel label `1000000`, earlier slope `[5]`, and C8 slopes `[7,9]`, the assigned list is exactly `[5,7,9]`. |
| `fixture_totals` | The same fixture has exact budget `16`, natural total `4`, and covered bad count `3`. |

The proved path is exactly

```text
supplied shallow residual chart
  -> SE2 support injection
  -> kernel-independent shallow direct RC
  -> direct C8 ProfilePayment
  -> line-local closed-ledger extension.
```

It is not a C8 chart compiler or chart-exhaustion theorem.

## 3. C9 exact-residual max-fiber producer

Namespace: `AsymptoticSpine.C9ResidualMaxFiber`.

### Exact post-deletion specification

`PreC9Owner` has precisely the constructors `c1` through `c8`.
`ProfileData Key compilerLoss` carries an explicit

```text
earlierOwner : support -> Option PreC9Owner
```

and the equality

```text
support in residual
  <-> support in the complete fixed-weight slice
      and earlierOwner support = none.
```

This makes “post-C1--C8 residual” an evaluable finite condition instead of an
informal adjective.

For one residual prefix key, the data additionally carry an `(SE2)` certificate
whose selected supports lie in the residual prefix fiber, a natural scale, and
the supplied row-sharp inequality

```text
fullPrefixFiber.length <= compilerLoss * naturalScale.
```

### Exact PROVED declarations

| declaration | exact statement |
| --- | --- |
| `ProfileData.support_not_earlier` | For every selected slope, its chosen supporting point has `earlierOwner = none`. |
| `ProfileData.slopes_paid` | The chain `selected slopes <= selected supports <= residual prefix fiber <= full prefix fiber <= compilerLoss * naturalScale` pays the actual C9 slope list. |
| `ProfileData.payment` | Constructs `ProfilePayment compilerLoss` by `ProfilePayment.ofDirect .c9`; no synthetic Sidon stage is inserted. |
| `ProfileData.payment_owner` | The constructed owner is exactly `.c9`. |
| `ProfileData.payment_assignedSlopes` | The assigned slopes are exactly `slopeCell.slopes`. |
| `ProfileData.extendLine` | Appends the exact residual payment after an earlier closed line, assuming separate slope-level disjointness. |
| `ProfileData.extendLine_budgetTotal` | The exact new budget is `line.budgetTotal + compilerLoss * naturalScale`. |
| `ProfileData.extendLine_naturalTotal` | The exact new natural total is `line.naturalTotal + naturalScale`. |

The row-sharp max-fiber inequality is a field of `ProfileData`, not a theorem of
this module.  This is the intended finite boundary of `def:primitive-q` and the
row target `def:q-row-atom`.

## Kernel validation and axiom census

Fork draft PR #70 ran the explicit target build

```text
lake build AsymptoticSpine
  AsymptoticSpine.C8ShallowClosureProducer
  AsymptoticSpine.C9ResidualMaxFiberProducer
  AsymptoticSpine.ClosedLedgerExtension
```

and then the package default target.  Both builds completed successfully with
33 jobs on Lean 4.31.0.  This validates compilation of every new module as an
explicit target as well as the package root.

Static and build-log census for the three ported modules:

```text
Mathlib imports: 0
sorry: 0
admit: 0
sorryAx occurrences: 0
custom axiom declarations: 0
unsafe declarations: 0
```

The printed axiom dependencies are exactly standard Lean principles:

- `ClosedLedgerExtension`: `assignedSlopeList_nodup` uses no axioms;
  `listSum_append_extension` uses `propext`; the remaining printed theorems use
  `propext` and `Quot.sound`.
- `C8ShallowClosureProducer`: the three structural/payment theorems use
  `propext` and `Quot.sound`; the two executable fixtures additionally use
  `Classical.choice`.
- `C9ResidualMaxFiberProducer`: every printed theorem uses only `propext` and
  `Quot.sound`.

Green CI proves elaboration and kernel checking of these statements.  It does
not discharge any external mathematical field in `ProfileData` or any global
nonclaim below.

## Explicit nonclaims

This packet does **not** prove any of the following:

- a fixed-before-line exhaustive C1--C9 atlas;
- completeness over all received lines;
- nonempty C8 or C9 survival on every line;
- subexponential realized profile count;
- C8 first-match chart construction or chart exhaustion;
- an actual Reed--Solomon common-core shortening certificate;
- the high-kappa C8 semantic owner;
- deep-prefix C8 MI/MA, Sidon payment, or direct deep ray payment;
- a structure-sensitive higher-dimensional balanced-core ray theorem;
- the row-sharp C9 max-fiber inequality;
- image-normalized C9 Sidon or effective MI+MA;
- concrete Reed--Solomon C1--C8 owner predicates;
- an independent C9 ray theorem beyond the supplied `(SE2)` certificate;
- general residual-to-full add-back;
- row-wide `(UNIF)` or the required `sup_line sum_profile` bound;
- profile-envelope or target comparison;
- a deployed adjacent-row certificate; or
- Grande Finale v3 row closure.

In particular, no row ledger atom is numerically moved by this port.  The C8
producer begins only after one actual shallow chart has been supplied, and the
C9 producer begins only after an exact owner complement, one slope projection,
and a row-sharp full-prefix bound have been supplied.

## Successor obligation

The next mathematical inputs remain the two hard statements already isolated
by the active spine:

1. exhaust actual post-deletion C8 charts into an earlier semantic owner, the
   supplied shallow closure, a paid bounded chart, or one explicitly named deep
   residual; and
2. prove row-sharp max-fiber control on an exact post-C1--C8 C9 residual, or an
   image-normalized Sidon/MI+MA theorem that implies that control, while
   retaining the genuine slope projection.

Only after those inputs, an honest realized-profile census, add-back, and the
line-local `(UNIF)` sum can the global completion ledger be instantiated.
