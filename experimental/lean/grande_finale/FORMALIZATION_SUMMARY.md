# Grande Finale Formalization Summary

This package is a partial Lean formalization of
`experimental/grande_finale.tex`.

## Package Layout

- `GrandeFinale.lean`: core self-contained kernels for integer budgets,
  first-match ledgers, CA/MCA bad-slope monotonicity, moment inequalities, and
  finite packet arithmetic checks.
- `GrandeFinale/ChallengeIntersection.lean`: exact finite-group
  translate-intersection averaging, linear-code received-line shear invariance,
  challenge-restricted MCA numerators, and the ceiling-density transfer from a
  supplied full-field bad-slope floor.
- `GrandeFinale/CollisionAwarePole.lean`: polynomial root-collision
  averaging, exact distinct-value ceiling, finite codeword representatives,
  simple-pole support semantics, the full-field MCA numerator compiler in
  `thm:collision-aware-pole` / equation (4.2), and its proper-challenge
  composition.
- `GrandeFinale/QFourierTao.lean`: log-moment-to-Q reductions, including the
  finite bit-certificate inequality.
- `GrandeFinale/QEntropyInverse.lean`: deterministic atoms around the entropic
  inverse route, including the reverse moment/max-fiber inequality and
  Vandermonde rank rigidity.
- `GrandeFinale/LargestFiberMoment.lean`: exact largest-fiber normalized
  `q`-moment sandwich, its finite logarithmic lower bound, and the normalized
  Q-to-SP second-moment transfer.
- `GrandeFinale/ExactProfileCompiler.lean`: exact finite incidence double
  counting, residual moment payment with the full-slice mean, the literal
  natural floor in (FC1), and available/minimum first-match budgets in (FC2).
- `GrandeFinale/FirstMatchAddBack.lean`: ordered first-match
  disjointization, the exact finite family-union multiplier, full-slice
  overlap counting, and the weighted add-back formulas (AB1)--(AB3).
- `GrandeFinale/SubfieldConfinement.lean`: exact identification of a finite
  coefficient-vector base-domain RS code with the existing polynomial
  submodule, base-coordinate projection, same-support pair transfer, and MCA
  bad-slope confinement.
- `GrandeFinale/ExactPrefixList.lean`: the exact locator-prefix support/list
  correspondence, unique recovery of the full agreement support, and the
  no-extra-agreement clause from `prop:exact-prefix-list`.
- `GrandeFinale/PrefixPigeonhole.lean`: the explicit locator coefficient map,
  its equivalence with leading cancellation, and the literal natural-ceiling
  lower bound for both a prefix fiber and its complete polynomial list.
- `GrandeFinale/ExactListLine.lean`: the quotient explaining polynomial,
  exact agreement-set preservation, and the same-field bijection between a
  complete finite polynomial list and the MCA-bad slopes of a fixed
  separating simple-pole line.
- `GrandeFinale/QPrimitiveCollision.lean`: collision-tuple identities,
  trade-formulation kernels, low-support exclusion, and prefix-collision
  rigidity.
- `GrandeFinale/QFiniteTables.lean`: the four rows of `prop:q-exact-target` and
  `prop:q-moment-order-floor`, including exact integer inputs, budget-ratio
  truncations, printed-margin rounding, and the real-average versus
  ceiling-average moment-floor convention split.
- `GrandeFinale/SyndromeLine.lean`: supported-error syndrome spans, the exact
  support-wise syndrome-line normal form, fixed-support uniqueness,
  deduplicated finite-family incidence, and the exact MCA/syndrome numerator
  equality for a surjective syndrome map.
- `GrandeFinale/ProfileEnvelopeWindow.lean`: exact rational exponent algebra for
  the corrected per-folding identity-dominance windows, including finite-family
  intersection/union and the positive-crossing no-field-drop characterization.
- `GrandeFinale/BC.lean`: theorem-level reductions around the BC split-pencil
  ledger, including one-parameter moving-root and saturation kernels.
- `GrandeFinale/SP.lean`: theorem-level reductions around the SP ledger,
  including quotient pullback, coefficient-scale, top-stratum, and Q-implies-SP
  kernels.  The Q-implies-SP statement retains the manuscript's exact diagonal
  subtraction, both before and after normalization.
- `GrandeFinale/Frontier.lean`: composite-prefix descent, row-sharp Q atom
  scaffolding, finite BC chart-audit kernels, and extension-cell finite
  comparisons.

## Formalized Scope

The files formalize reusable theorem-level kernels and arithmetic facts from the
Grande Finale program.  They do not prove the full RS-MCA threshold theorem.

The main remaining target is Q:

```text
primitive entropic inverse theorem / row-sharp prefix-fiber bound
```

The Lean files currently formalize deterministic pieces consumed by this target
and consequences that follow after Q is supplied.  The printed finite-Q table
data and its elementary integer relations are now pinned and kernel-checked.
This is not a proof of the row-sharp Q atom: the bit margins and moment floors
remain audited inputs rather than formal derivations of transcendental
logarithms or enormous binomial values.  The entropy-scale inverse
Littlewood-Offord / Balog-Szemeredi-Gowers step remains open.

The largest-fiber-moment module supplies the exact finite compiler arithmetic
in `lem:largest-fiber-log-detail` and `lem:q-to-sp-detail`. Its real-valued
finite-fiber statements strictly include the manuscript's nonnegative integer
case; sequence-level asymptotic notation remains outside this finite module.

The exact-profile compiler proves the finite arithmetic implications in
`thm:exact-finite-profile-compiler`. It treats the witness-exhaustive atlas,
the exact support-pair identity, and the certified incidence relation and
degrees as explicit inputs. It does not assert that those structural inputs
exist for an unrestricted row. Challenge-set intersection and the adjacent
unsafe/safe threshold comparison remain delegated to the package's existing
challenge and threshold results.

The first-match add-back module proves the finite disjoint-union identity
before summing cell budgets and records the exact overlap loss for full profile
slices. Its family-size-times-budget theorem is the finite combinatorial core
of `lem:profile-summation`; the sequence-level `e^{o(n)}` bookkeeping
remains outside the module. A witness-exhaustive atlas and the individual
profile payments remain explicit inputs.

The subfield-confinement module proves `thm:subfield-confinement-full` for an
arbitrary field extension modeled by `Algebra B F`. The evaluation domain and
received line are base-valued, while the code itself is the existing
extension-field `CollisionAwarePole.rsEval`. No finiteness or
finite-dimensionality is needed for same-support transfer; finite fields enter
only in the bad-slope cardinality corollary.

The exact-prefix-list module formalizes the algebraic bijection in equation
(4.1). It represents a fixed locator prefix by the equivalent leading-term
cancellation condition `degree (U - locator S) < K`, and proves that every
listed polynomial has exactly `m` agreements and a unique support. The
explicit coefficient-vector map, its pigeonhole fiber-size lower bound, and
the later separating-pole line bijection remain separate from this module.
`PrefixPigeonhole` supplies the first two as a separate layer, including the
literal ceiling rather than a floor-division relaxation, while `ExactListLine`
supplies the same-field fixed-pole line bijection. Its prefix-specific and
scalar-extension specializations remain separate targets.

The syndrome-line module is independent of Q.  It proves the generic
linear-code compiler behind `prop:syndrome-line-normal-form` and
`thm:syndrome-secant-exact` in the frontiers paper.  The Reed--Solomon
parity-check construction, rational-normal-curve interpretation, and reduction
from threshold witnesses to exact-cardinality supports remain separate.

The collision-aware-pole and challenge-intersection modules are independent
of Q and formalize complementary parts of the frontiers paper's simple-pole
route. `CollisionAwarePole` proves the exact equation-(4.2) full-field floor
from a supplied finite dimension-`k+1` Reed--Solomon codeword list, while
`ChallengeIntersection` transfers a supplied full-field floor to a proper
challenge set after a received-line shear. The direct composition is exported
as `collisionAwarePole_challenge_of_codewordList`. The prefix-list construction
and pigeonhole floor are supplied by `ExactPrefixList` and
`PrefixPigeonhole`, and `ExactListLine` proves the exact same-field fixed-pole
list--line conversion. A direct scalar-extension composition with a proved
separating-pole existence bound remains absent, so the modules do not yet
prove `prop:simple-pole-lower` or equation (13.3) end to end.

The profile-window module is also independent of Q. It proves exponent-level
dominance only after `h`, `s`, and every actual `(c,lambda)` pair are supplied.
QR6/QR8 normalization, folding-family exhaustiveness, (A2)/(A4)/(A7), and the
bridge to the full profile envelope remain explicit outside inputs.

## Build Note

Do not run `lake build` casually in this repository. Build only with the
pinned Lean/Mathlib versions and matching precompiled Mathlib cache.
Contributor audit notes report a full pinned build on 2026-07-11 with 8038
jobs, including `GrandeFinale.CollisionAwarePole`. Targeted module checks are
reported in the correspondence notes.
