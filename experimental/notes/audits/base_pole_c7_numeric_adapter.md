# Conditional base-pole C7 numeric adapter and atlas-order regressions

**Status:** PROVED FINITE ADAPTER UNDER EXPLICIT INPUTS / COUNTEREXAMPLE TO ATLAS-INDEPENDENT C7 OWNERSHIP / CONDITIONAL RS INSTANTIATION / AUDIT

## Scope

This packet ports the useful finite arithmetic from the earlier asymptotic-spine draft into the active `experimental/lean/grande_finale/` formalization track.  The Lean module is intentionally self-contained and numeric.  It consumes, rather than proves, a source-facing theorem that supplies:

1. a duplicate-free list of distinct raw slopes for one received line;
2. a bound of that list by a supplied `q - 1` census; and
3. a supplied earlier assigned-slope image on the same line.

The adapter deletes the earlier image from the raw list, installs one unit direct distinct-slope payment for every survivor, and appends those profiles to a prior line-local numeric profile list.  The result preserves duplicate-free assigned slopes and proves the exact telescopes

```text
combined direct budget
  = prior direct budget + number of surviving slopes

combined natural-scale sum
  = prior natural-scale sum + number of surviving slopes.
```

The compiler loss is generic.  `ProfilePayment.liftLoss` lifts a profile from loss `small` to loss `large` under `small <= large`; it preserves assigned slopes, natural scale, residual budget, Sidon budget, ray budget, all local inequalities, and weakens only the global loss-dominance field.  Consequently the appended C7 profiles retain unit local budgets even when the surrounding compiler allows a larger loss.

## Active Grande Finale correspondence

The active authority is `experimental/grande_finale.tex`, and the primary Lean track is `experimental/lean/grande_finale/`.  This module maps to that track as follows.

| Adapter object | Active-track interpretation |
|---|---|
| `basePoleSurvivors earlier raw` | the exact two-cell first-match residual chart, `raw \ earlier` |
| `basePoleSurvivors_toFinset_eq_firstMatchCell` | literal agreement with `GrandeFinale.FirstMatchAddBack.firstMatchCell` for the later cell |
| `ProfilePayment.toPrimitiveCellBudget` | the direct distinct-slope branch of `GrandeFinale.ExactProfileCompiler.PrimitiveCellBudget` |
| `basePoleUnitProfile` and `unitProfiles` | unit natural-scale direct payment, with no invented residual-moment or Sidon theorem |
| `budgetTotal_extendProfiles` | exact line-local direct-payment add-back |
| `naturalTotal_extendProfiles` | exact line-local profile-envelope add-back |
| `budgetTotal_extendProfiles_le_prior_add_qMinusOne` | saturation/effective-image census consumed as a separately supplied source bound |

All sums in the module are line-local.  An outer supremum over received lines may be taken only after these profile sums have been formed.  The module does not replace `sup_line sum_profile` by `sum_profile sup_line`.

This is a finite adapter, not a formalization of the full active-source package.  In particular, it does not prove `def:admissible-sequence`, the asymptotic comparison in `eq:profile-envelope`, a source-side saturation theorem, or the exact completion ledger.  It supplies one reusable direct-payment component that can be inserted only after those surrounding hypotheses are separately established.

## Source boundary and conditional RS instantiation

`BasePoleSlopeSource` is an interface with four fields: the raw slope list, duplicate-freeness, `qMinusOne`, and the list-length bound.  Those fields are assumptions.  The module does **not** formalize:

- a finite field or the domain `D = F_q^×`;
- Reed--Solomon codewords or witnesses;
- support locators or constant coefficients;
- the base-pole received line;
- the law `d ↦ -d` or its injectivity;
- the claim that the supplied raw list is the actual bad-slope image; or
- completeness over all received lines.

A concrete RS theorem may instantiate this interface later, but this PR does not provide that theorem.  The natural-number fixtures are executable arithmetic regressions only.

## Atlas-order regressions

The module retains two negative controls.

1. **Affine-Steiner double charge.**  When an earlier owner and the raw later class contain the same slope, appending the untrimmed later payment duplicates that slope.  First-match deletion makes the later residual empty.
2. **Singleton-root atlas noncanonicity.**  A broad earlier singleton-root slope image can delete every later raw slope, while an empty earlier image leaves the same raw list intact.

The second regression does not select a semantic policy.  It establishes only:

```text
COUNTEREXAMPLE / ACTIVE-ATLAS NONCANONICITY / POLICY DECISION REQUIRED
```

Possible policy choices include restricting planted cells to positive-density blocks, requiring named row-derived factors, excluding singleton-root profiles from a canonical atlas, placing the constant-coefficient cell earlier, or accepting earlier planted ownership and an empty later residual.  No one choice is installed as an authoritative theorem here.

## Relationship to PR #987

PR #987 remains the owner of the older `UniformClosedLedger` interface.  This packet does not copy `UniformClosedLedger.lean`, its audit note, its root import, or its README/log material.  The active-track module is independently self-contained and uses the already integrated `GrandeFinale.FirstMatchAddBack` and `GrandeFinale.ExactProfileCompiler` APIs.

## Explicit nonclaims

This packet does not prove:

- a concrete RS semantic C7 owner or a least-owner theorem;
- an atlas-independent nonempty C7 survivor;
- a complete first-match atlas;
- completeness of a supplied received-line list;
- actual row-wide `UNIF`;
- the profile-envelope-to-target comparison;
- a finite adjacent safe row, threshold improvement, row closure, prize result, or protocol claim.

Support counts, explanation states, pair moments, witness rays, and distinct MCA slopes remain separate objects.  Only the supplied distinct-slope list and its finite payment are manipulated here.

## Reproducibility

The intended clean-state checks are:

```text
git diff --check
cd experimental/lean/grande_finale
lake build GrandeFinale.BasePoleC7NumericAdapter
lake build
cd ../../..
python3 experimental/scripts/verify_base_pole_c7_numeric_adapter.py
python3 -O experimental/scripts/verify_base_pole_c7_numeric_adapter.py
```

The changed Lean file should also be searched for `sorry`, `admit`, declaration-level `axiom`, and `unsafe`; the printed `#print axioms` reports should be inspected; and generated `.lake/build` artifacts must not be committed.

For provenance, fork run `29760744796` explicitly checked out the earlier PR head `5ff44f4af7b72e767782991cbe281a0c4525848c` and completed the old asymptotic-spine build in 34 jobs.  The originally cited run `29758247044` checked a different commit and did not validate that PR head.  Neither old run validates this rewritten active-track module, so publication requires a fresh exact-head build.
