# Conditional C7 base-pole ledger adapter and atlas-order packet

**Status:** `PROVED FINITE ADAPTER UNDER EXPLICIT INPUTS / COUNTEREXAMPLE TO ATLAS-INDEPENDENT C7 OWNERSHIP / CONDITIONAL RS INSTANTIATION / AUDIT`

## Integration context

Upstream commit `18cfc199` integrated the two prerequisite reviewed units:

1. `AsymptoticSpine.UniformClosedLedger`, the abstract finite
   `sup_line sum_profile` numeric compiler; and
2. the narrow `C7BasePoleProducer` / `C7BasePoleWitnessProducer`, ending at the
   deletion-aware `directBudget` interface.

This packet is the deferred third unit from the #997 split. It does **not**
rewrite either integrated producer or `UniformClosedLedger`. The adapter layer
is rebuilt in new modules importing those stable interfaces.

The asymptotic-spine package is an interface/provenance formalization. The
active TeX sources remain the proof authorities; no C1--C9 label in this Lean
package is self-authenticating semantic evidence.

## Module layout

Integrated and unchanged:

- `AsymptoticSpine.C7BasePoleProducer`
- `AsymptoticSpine.C7BasePoleWitnessProducer`
- `AsymptoticSpine.UniformClosedLedger`

New adapter and regression modules:

- `AsymptoticSpine.C7BasePoleLedgerBridge`
- `AsymptoticSpine.C7BasePoleWitnessLedgerBridge`
- `AsymptoticSpine.C7BasePoleLineExtension`
- `AsymptoticSpine.SemanticAtlasOwnership`
- `AsymptoticSpine.C7OwnerRegression`
- `AsymptoticSpine.C7SingletonPlantedAbsorption`

All six new modules are imported by the package root `AsymptoticSpine.lean`.

## Source-facing assumptions versus kernel-checked arithmetic

The source note
`experimental/notes/thresholds/aperiodic_one_ray_saturation.md` records a
base-pole theorem of the form

```text
raw witness w
  -> locator constant coefficient d
  -> final slope slopeOfCoeff(d) = -d
  -> duplicate-free raw slope image
  -> at most q - 1 realized coefficients.
```

Lean does not reprove that finite-field theorem here.
`BasePoleC7WitnessClass` assumes the witness catalogue, coefficient map, exact
slope law, injectivity, and `q - 1` census as explicit fields. Its executable
fixture uses natural numbers and is not an RS instantiation.

Given a raw numeric slope list and supplied earlier assigned list `E`, the
integrated narrow producer defines

```text
Z_C7_assigned = Z_C7_raw \ E
```

and exposes

```text
basePoleC7DirectBudget earlier raw
  = |Z_C7_assigned|
  <= |Z_C7_raw|.
```

The `q - 1` inequality enters only through a supplied source-facing bound. The
new modules kernel-check the finite deletion, payment, append, and compiler
arithmetic conditional on those inputs.

## Exact PROVED statements

### Raw-slope ledger layer

`C7BasePoleLedgerBridge.lean` proves:

- `basePoleC7Profile` installs one surviving numeric slope as
  `ProfilePayment.ofDirect .c7 [gamma] 1 1`; no Sidon, residual, or ray theorem
  is manufactured;
- `basePoleC7Profiles_flatten_assignedSlopes` identifies the flattened profile
  list with the integrated post-deletion list;
- `basePoleC7Line_budgetTotal` and `basePoleC7Line_naturalTotal` identify both
  local totals with the survivor count;
- `basePoleC7Line_budgetTotal_eq_directBudget` and
  `basePoleC7Line_naturalTotal_eq_directBudget` identify both totals with the
  already-integrated `basePoleC7DirectBudget`;
- the raw-list and supplied `qMinusOne` bounds for both totals;
- `basePoleC7Ledger_compiles`, a one-line numeric compiler theorem preserving
  `sum_profile` inside the supplied line.

### Conditional witness-data hand-off

`C7BasePoleWitnessLedgerBridge.lean` proves, for any supplied
`BasePoleC7WitnessClass`:

- `c7Line_flatten_assignedSlopes`;
- `c7Line_budgetTotal_eq_directBudget` and
  `c7Line_naturalTotal_eq_directBudget`;
- the two supplied-`qMinusOne` bounds;
- `c7Ledger_compiles` and the natural-number `rootedFixture_compiles` replay.

These are adapter theorems under the structure's explicit fields, not a
kernel-checked construction of actual RS witnesses.

### Generic line-local append

`C7BasePoleLineExtension.lean` proves:

- `ProfilePayment.liftLoss`, which preserves assigned slopes, natural scale,
  residual budget, Sidon budget, ray budget, and all local inequalities while
  weakening only `compilerLossDominates`;
- the lifted C7 profile list has the same post-deletion slope image, unit ray
  budget total, and unit natural total;
- for every `compilerLoss >= 1`, appending only the post-earlier C7 residual to a
  `ClosedLineLedger compilerLoss profileCap` preserves duplicate-free numeric
  ownership and profile-count control;
- `extendLine_flatten_assignedSlopes` gives the exact disjoint concatenation;
- `extendLine_budgetTotal` proves

  ```text
  combined budgetTotal
    = earlier budgetTotal + number of surviving C7 slopes;
  ```

- `extendLine_naturalTotal` proves the analogous natural-scale telescope;
- both added terms are at most the supplied `qMinusOne`;
- the loss-one fixture yields totals `4 = 2 + 2`;
- the loss-three fixture proves the earlier budget `6` becomes `8`, while the
  natural sum becomes `4`, confirming that lifting does not inflate the two
  local C7 ray budgets.

### Labeled numeric atlas-order boundary

The historical filename `SemanticAtlasOwnership.lean` is retained, but its
contents are deliberately numeric/interface-only:

- `C3ProvenanceLabel` is metadata and proves no gcd, resultant, ramification,
  quotient, locator, witness, or least-owner theorem;
- `LabeledC3Payment` packages a supplied numeric direct payment;
- `WitnessLocalRefinement` is metadata with no owner constructor;
- `LabeledC3ThenLater.line` consumes explicit disjointness, exhaustiveness, and
  profile caps supplied by the caller;
- `LabeledC3ThenLater.ledger_compiles` preserves the line-local compiler order
  for a supplied finite line list.

No active semantic-atlas policy is selected. The two regression modules prove
the finite atlas-order facts listed in their dedicated audits.

## Proof and axiom census

The six new Lean modules contain:

```text
sorry / sorryAx placeholders: 0
custom axiom declarations:     0
Mathlib imports:               0
```

Every load-bearing theorem is listed by `#print axioms`. The fork draft-PR Lean
build is authoritative for compilation; green compilation is paired with this
source-to-statement audit. Any ordinary Lean foundations printed by the build
artifact are reported separately and are not custom axioms.

## Exact consequence

Conditional on the supplied raw list, earlier assigned list, duplicate-free
fields, and source-side census, the literal survivor subset is paid at unit
natural scale and can be appended to the same supplied line at any compiler
loss at least one. The append preserves the exact local budget and natural
scale telescopes.

The regressions show only that atlas order matters:

- an earlier duplicate assignment excludes an untrimmed raw C7 payment; and
- under a broader supplied singleton-root order, the later C7 residual can be
  empty.

They do not prove which atlas policy is active or that any concrete RS line has
those supplied numeric cells.

## Conditional / open boundary

This packet does not prove:

- the finite-field base-pole source theorem in Lean;
- a concrete RS semantic C7 owner or atlas-independent C7 survivor;
- a fixed-before-line exhaustive C1--C9 semantic atlas;
- completeness over all received Reed--Solomon lines;
- an asymptotic realized-profile census beyond the local raw-list cap;
- actual row-wide `(UNIF)`;
- residual-to-full add-back, C8 ray compilation, or C9 Sidon / MI--MA;
- profile-envelope comparison, target comparison, an adjacent safe row,
  threshold improvement, prize claim, or row closure.

The C8/C9 producers are outside this packet.
