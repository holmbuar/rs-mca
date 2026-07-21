# C7 base-pole closed-ledger bridge and semantic ownership packet

**Status:** `PROVED LOCAL BRIDGE / PROVED FINITE OWNERSHIP REGRESSIONS / CONDITIONAL GLOBAL USE / AUDIT`

## Integration context

Upstream commit `18cfc199` integrated the two prerequisite reviewed units:

1. `AsymptoticSpine.UniformClosedLedger`, the abstract finite
   `sup_line sum_profile` compiler; and
2. the narrow `C7BasePoleProducer` / `C7BasePoleWitnessProducer`, ending at the
   deletion-aware `directBudget` and the rooted witness slope image.

This packet is the deferred third unit from the #997 split. It does **not**
rewrite either integrated producer. The ledger layer is rebuilt in new modules
that import the narrow interfaces and `UniformClosedLedger`.

## Module layout

Integrated and unchanged:

- `AsymptoticSpine.C7BasePoleProducer`
- `AsymptoticSpine.C7BasePoleWitnessProducer`
- `AsymptoticSpine.UniformClosedLedger`

New bridge and ownership modules:

- `AsymptoticSpine.C7BasePoleLedgerBridge`
- `AsymptoticSpine.C7BasePoleWitnessLedgerBridge`
- `AsymptoticSpine.C7BasePoleLineExtension`
- `AsymptoticSpine.SemanticAtlasOwnership`
- `AsymptoticSpine.C7OwnerRegression`
- `AsymptoticSpine.C7SingletonPlantedAbsorption`

All six new modules, together with `UniformClosedLedger`, are imported by the
package root `AsymptoticSpine.lean`.

## Source-facing object

For one received base-pole line, the proved source theorem in
`experimental/notes/thresholds/aperiodic_one_ray_saturation.md` supplies:

```text
raw witness w
  -> locator constant coefficient d
  -> final slope slopeOfCoeff(d) = -d
  -> duplicate-free raw slope image
  -> at most q - 1 realized coefficients.
```

The integrated narrow producer takes a supplied earlier-owner slope image `E`
and defines the literal first-match residual

```text
Z_C7_assigned = Z_C7_raw \ E.
```

Its public numerical interface is

```text
basePoleC7DirectBudget earlier raw
  = |Z_C7_assigned|
  <= |Z_C7_raw|
  <= q - 1.
```

The new bridge consumes exactly that interface.

## Exact PROVED statements

### Raw-slope ledger layer

`C7BasePoleLedgerBridge.lean` proves:

- `basePoleC7Profile` installs one survivor as
  `ProfilePayment.ofDirect .c7 [gamma] 1 1`; no Sidon, residual, or ray theorem
  is fabricated;
- `basePoleC7Profiles_flatten_assignedSlopes` identifies the flattened profile
  image with the integrated post-deletion slope list;
- `basePoleC7Line_budgetTotal` and `basePoleC7Line_naturalTotal` identify both
  line-local sums with the survivor count;
- `basePoleC7Line_budgetTotal_eq_directBudget` and
  `basePoleC7Line_naturalTotal_eq_directBudget` identify both sums with the
  already-integrated `basePoleC7DirectBudget`;
- `basePoleC7Line_budgetTotal_le_raw` and
  `basePoleC7Line_naturalTotal_le_raw` bound both sums by the raw slope census;
- `basePoleC7Line_budgetTotal_le_qMinusOne` and
  `basePoleC7Line_naturalTotal_le_qMinusOne` apply a supplied source-side
  `qMinusOne` bound;
- `basePoleC7Ledger_compiles` replays the one-line ledger through
  `UniformClosedLedger.compile` without changing the summation order.

### Rooted witness hand-off

`C7BasePoleWitnessLedgerBridge.lean` proves:

- `c7Line_flatten_assignedSlopes` identifies the line image with the integrated
  rooted witness residual;
- `c7Line_budgetTotal_eq_directBudget` and
  `c7Line_naturalTotal_eq_directBudget` identify both rooted totals with
  `BasePoleC7WitnessClass.directBudget`;
- `c7Line_budgetTotal_le_qMinusOne` and
  `c7Line_naturalTotal_le_qMinusOne` inherit the source census;
- `c7Ledger_compiles` proves the rooted one-line compiler bound;
- `rootedFixture_compiles` checks the four-witness deletion fixture.

### Line-local append

`C7BasePoleLineExtension.lean` proves:

- the earlier ledger's flattened slope image is duplicate-free;
- appending only the post-earlier C7 residual preserves duplicate-free
  first-match ownership;
- `extendLine_flatten_assignedSlopes` gives the exact disjoint concatenation;
- `extendLine_budgetTotal` proves

  ```text
  combined budgetTotal
    = earlier budgetTotal + number of surviving C7 slopes;
  ```

- `extendLine_naturalTotal` proves the analogous natural-scale telescope;
- both added terms are at most `qMinusOne`;
- the executable fixture deletes raw slopes `100,102`, appends only `101,103`,
  and obtains budget and natural total `4 = 2 + 2`.

### Semantic ownership boundary

`SemanticAtlasOwnership.lean` proves a typed boundary:

- a semantic C3 owner must be a `CertifiedC3Profile` with a row-derived
  certificate kind, duplicate-free post-deletion slope list, natural scale, and
  direct payment;
- `WitnessLocalRefinement` has no constructor that creates an owner;
- `CertifiedC3ThenLater.line` composes certified C3 profiles before later paid
  profiles with explicit cross-disjointness, exhaustiveness, and profile caps;
- `CertifiedC3ThenLater.ledger_compiles` preserves the line-local
  `sup_line sum_profile` compiler.

`C7OwnerRegression.lean` and `C7SingletonPlantedAbsorption.lean` prove the two
finite regression suites listed in their dedicated audit notes.

## Proof and axiom census

The six new Lean modules contain:

```text
sorry / sorryAx placeholders: 0
custom axiom declarations:     0
Mathlib imports:               0
```

Every load-bearing theorem is listed by `#print axioms` in its module. The fork
draft-PR Lean build is the authoritative compilation check; green compilation
must be paired with this source-to-statement audit.

The finite-field locator theorem is not reproved in stdlib Lean. It enters only
through the explicit fields of the already-integrated
`BasePoleC7WitnessClass`, whose correspondence is audited in
`c7_base_pole_producer.md`.

## Semantic consequence

The local natural-scale payment is complete after an earlier slope image is
supplied: the literal survivor subset is paid and can be appended to the same
received line's earlier ledger.

This does not imply an atlas-independent nonempty C7 owner. The affine-Steiner
regression shows that an earlier C1 quotient can delete a raw C7-style slope.
The singleton-planted regression shows why witness-local support factors cannot
silently become earlier C3 owners; active semantic use requires the certified
row-derived interface.

## Conditional / open boundary

This packet does not prove:

- a fixed-before-line exhaustive C1--C9 semantic atlas;
- completeness over all received Reed--Solomon lines;
- nonempty C7 survival on every line;
- an asymptotic realized-profile census beyond the local raw bound;
- row-wide `(UNIF)`;
- residual-to-full add-back, C8 ray compilation, or C9 Sidon / MI--MA;
- profile-envelope comparison, target comparison, an adjacent safe row, or row
  closure.

The C8/C9 semantic producers are outside this packet.
