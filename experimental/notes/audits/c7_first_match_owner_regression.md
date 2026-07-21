# C7 raw payment, first-match ownership, and the deletion-aware ledger bridge

**Status:** `COUNTEREXAMPLE TO UNTRIMMED OWNERSHIP / PROVED FINITE REGRESSION / PROVED LOCAL BRIDGE / OPEN GLOBAL GAP`

## Verdict

A numerically valid raw C7-style one-slope payment is not by itself a semantic
C7 owner. The affine-Steiner quotient family in
`experimental/notes/thresholds/affine_steiner_quotient_owner.md` is an actual
Reed--Solomon regression: many witnesses collapse to one slope, but their
supports are complete fibres of a nontrivial quotient map. C1 therefore owns
and deletes that slope before C7.

The correct local C7 object is the assigned first-match image

```text
Z_C7_assigned(r) = Z_C7_raw(r) \ Z_<7(r),
```

not the untrimmed raw image. A surviving singleton is paid directly; a deleted
singleton contributes zero and is not installed as a realized profile.

## Lean regression

`AsymptoticSpine.C7OwnerRegression` proves:

1. `affineSteinerC1C7_firstMatch`:

   ```text
   firstMatchLeaves [] [[7],[7]] = [[7],[]].
   ```

2. `affineSteinerRawC7_numericallyPaid`: the raw C7 direct payment satisfies its
   own natural-scale inequality.
3. `affineSteinerRawC7_breaks_firstMatchOwnership`: installing both raw C1 and
   raw C7 profiles duplicates slope `7`.
4. `noClosedLineLedger_with_affineSteinerRawC7`: no
   `ClosedLineLedger 1 2` can have that untrimmed profile list.
5. `affineSteinerCorrectLine_totals`: after deletion, budget and natural total
   are both one.
6. `affineSteinerCorrectLedger_compiles`: the corrected one-line model compiles
   through `UniformClosedLedger`.

These are finite ownership consequences. The finite-field quotient theorem
remains in the cited source packet and is not reproved by this module.

## Deletion-aware producer and new module layout

Upstream commit `18cfc199` integrated the narrow producer modules. They remain
unchanged and expose:

```text
basePoleC7AssignedSlopes earlier raw = raw \ earlier,
basePoleC7DirectBudget earlier raw = |raw \ earlier|.
```

The deferred ledger consumer now lives in new modules:

- `C7BasePoleLedgerBridge` maps each surviving slope to
  `ProfilePayment.ofDirect .c7 [gamma] 1 1`, constructs `basePoleC7Line` and
  `basePoleC7Ledger`, and proves both totals equal the integrated
  `basePoleC7DirectBudget`;
- `C7BasePoleWitnessLedgerBridge` constructs rooted `c7Line` and `c7Ledger` from
  the integrated witness class and inherits the `q - 1` bound;
- `C7BasePoleLineExtension` appends the surviving profiles to an earlier line
  and proves exact budget and natural-scale telescopes.

Thus the regression and bridge are complementary: the former rejects double
charging, while the latter performs deletion before payment.

## Semantic repair

`SemanticAtlasOwnership` makes the owner boundary explicit. A row-derived C3
owner must be represented by `CertifiedC3Profile`; a
`WitnessLocalRefinement` cannot create first-match ownership. This prevents a
support-local factor from silently deleting C7 without a certified semantic
catalogue entry.

## Proof census

Across `C7OwnerRegression.lean` and the three bridge modules:

```text
sorry / sorryAx placeholders: 0
custom axiom declarations:     0
Mathlib imports:               0
```

Load-bearing declarations are followed by `#print axioms`; the fork draft-PR
Lean check is authoritative for compilation.

## Nonclaims

- No C7 survivor is asserted to exist on every received line.
- No earlier C1--C6 owner image is constructed by the bridge.
- No global atlas, whole-row completeness, row-wide `(UNIF)`, profile-envelope
  comparison, target comparison, or row closure is proved.
- No support count, pair moment, max-fibre bound, or chart estimate is
  substituted for the distinct-slope numerator.

## Replay support

The fail-closed support verifier is
`experimental/scripts/verify_c7_first_match_owner_regression.py`. It replays the
finite first-match fixtures and checks the declaration/import boundary. It is
an audit aid, not Lean proof validation.
