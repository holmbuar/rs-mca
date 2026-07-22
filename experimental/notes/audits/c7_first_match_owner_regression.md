# C7 raw payment, atlas order, and the deletion-aware numeric adapter

**Status:** `COUNTEREXAMPLE TO ATLAS-INDEPENDENT C7 OWNERSHIP / PROVED FINITE REGRESSION / CONDITIONAL RS INSTANTIATION / OPEN GLOBAL GAP`

## Verdict

A numerically valid raw C7-style one-slope payment is not by itself a semantic
C7 owner. The affine-Steiner quotient note
`experimental/notes/thresholds/affine_steiner_quotient_owner.md` provides the
source provenance: in that RS family, many witnesses collapse to one slope and
the supports are complete fibres of a nontrivial quotient map, so the printed
source owner is earlier than C7.

The Lean module does not reprove that algebra or construct an actual owner. It
checks the finite numeric consequence of supplying two overlapping cells:
ordered first match keeps the earlier value and leaves the later C7 list empty.
The local adapter must therefore consume the post-earlier list

```text
Z_C7_assigned = Z_C7_raw \ Z_earlier,
```

rather than append the untrimmed raw image.

## Lean regression

`AsymptoticSpine.C7OwnerRegression` proves:

1. `affineSteinerC1C7_firstMatch`:

   ```text
   firstMatchLeaves [] [[7],[7]] = [[7],[]].
   ```

2. `affineSteinerRawC7_numericallyPaid`: the raw C7 direct payment satisfies its
   own arithmetic inequality.
3. `affineSteinerRawC7_breaks_firstMatchOwnership`: installing both supplied
   profile lists duplicates value `7`.
4. `noClosedLineLedger_with_affineSteinerRawC7`: no
   `ClosedLineLedger 1 2` can have that untrimmed profile list.
5. `affineSteinerCorrectLine_totals`: after list-level deletion, budget and
   natural total are both one.
6. `affineSteinerCorrectLedger_compiles`: the corrected one-line numeric model
   compiles through `UniformClosedLedger`.

These are finite list/payment statements. They do not prove that the fixture's
natural numbers are actual RS slopes, that C1 is the least owner on a received
line, or that the supplied line list is complete.

## Deletion-aware adapter and module layout

Upstream commit `18cfc199` integrated the narrow producer modules. They remain
unchanged and expose:

```text
basePoleC7AssignedSlopes earlier raw = raw \ earlier,
basePoleC7DirectBudget earlier raw = |raw \ earlier|.
```

The deferred consumer lives in new modules:

- `C7BasePoleLedgerBridge` installs unit direct payments, constructs
  `basePoleC7Line` / `basePoleC7Ledger`, and proves both totals equal the
  integrated `basePoleC7DirectBudget`;
- `C7BasePoleWitnessLedgerBridge` consumes the explicit fields of
  `BasePoleC7WitnessClass`; its witness/field theorem is assumed rather than
  formalized here;
- `C7BasePoleLineExtension` lifts the unit C7 payments to any compiler loss at
  least one without changing their ray budgets, then proves exact budget and
  natural-scale append telescopes.

The regression rejects double charging; the adapter performs deletion before
payment.

## Atlas-policy boundary

The historical module name `SemanticAtlasOwnership` now contains only
`LabeledC3Payment` and `LabeledC3ThenLater`, a numeric interface whose provenance
labels prove no semantic classification. It does not select whether C3 should
use positive-density blocks, named row-derived factors, singleton exclusions,
a different order, or another policy.

Thus the packet exposes the required boundary but does not solve the global
semantic-atlas problem.

## Proof census

Across `C7OwnerRegression.lean` and the three bridge modules:

```text
sorry / sorryAx placeholders: 0
custom axiom declarations:     0
Mathlib imports:               0
```

Load-bearing declarations are followed by `#print axioms`; the exact-head fork
Lean check is authoritative for compilation.

## Nonclaims

- No concrete RS semantic C7 owner or survivor is proved.
- No earlier C1--C6 owner image is constructed by the adapter.
- No finite-field base-pole or affine-Steiner theorem is reproved in Lean.
- No global atlas, received-line completeness, actual row-wide `(UNIF)`,
  profile-envelope comparison, target comparison, adjacent safe row, or row
  closure is proved.
- No support count, pair moment, max-fibre bound, or chart estimate is
  substituted for the numeric distinct-slope list.

## Replay support

The fail-closed support verifier is
`experimental/scripts/verify_c7_first_match_owner_regression.py`. It replays the
finite first-match fixtures and checks the declaration/import boundary under
both ordinary and optimized Python. It is an audit aid, not Lean validation.
