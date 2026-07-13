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
- `GrandeFinale/RSParityKernel.lean`: barycentric weighted Vandermonde columns,
  at-most-`R` column independence, parity-map surjectivity, Lagrange moment
  annihilation, and exact identification of the parity kernel with the
  injective Reed--Solomon evaluation code.
- `GrandeFinale/RSSupportHyperplanes.lean`: exact identification of
  supported-error syndrome images with weighted-column spans, their dimensions,
  codimension-one functional kernels, and injectivity across exact `(R-1)`
  supports.
- `GrandeFinale/RSExactSupportUpper.lean`: exact reduction from threshold
  witnesses to exact-cardinality supports and the literal full-field
  `choose |D| a` support-atlas upper bound for injective Reed--Solomon codes.
- `GrandeFinale/RSFirstAdjacentRow.lean`: exact Reed--Solomon composition of
  the parity kernel, support hyperplanes, separating line, and support upper
  bound, proving the full-field AD1 numerator equality.
- `GrandeFinale/RSFirstAdjacentThreshold.lean`: exact first-safe proposition,
  its uniqueness, and both literal target-budget implications in AD2.
- `GrandeFinale/ExactAdjacentRow.lean`: exact finite avoidance of the `M`
  syndrome hyperplanes and `choose M 2` collision hyperplanes, followed by the
  generic syndrome-secant and support-wise MCA lower-bound compiler.
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

The syndrome-line module is independent of Q.  It proves the generic
linear-code compiler behind `prop:syndrome-line-normal-form` and
`thm:syndrome-secant-exact` in the frontiers paper. The RS parity-kernel module
supplies its weighted Vandermonde parity-check construction and exact kernel
identification, while the support-hyperplane module supplies the distinct
`(R-1)`-support kernel family. The exact-support-upper module supplies the
threshold-to-exact-cardinality reduction and the resulting support-atlas upper
bound, and the exact-adjacent-row module supplies the field-separation and
generic syndrome compiler. The first-adjacent-row module composes these pieces
to prove AD1 with the literal binomial constant and field-size gate. The
first-adjacent-threshold module then derives both AD2 implications on the exact
integer agreement grid.

The collision-aware-pole and challenge-intersection modules are independent
of Q and formalize complementary parts of the frontiers paper's simple-pole
route. `CollisionAwarePole` proves the exact equation-(4.2) full-field floor
from a supplied finite dimension-`k+1` Reed--Solomon codeword list, while
`ChallengeIntersection` transfers a supplied full-field floor to a proper
challenge set after a received-line shear. The direct composition is exported
as `collisionAwarePole_challenge_of_codewordList`. The prefix-list construction
and list-size floor remain explicit upstream inputs, so the modules do not
prove `prop:simple-pole-lower` or equation (13.3) end to end.

The profile-window module is also independent of Q. It proves exponent-level
dominance only after `h`, `s`, and every actual `(c,lambda)` pair are supplied.
QR6/QR8 normalization, folding-family exhaustiveness, (A2)/(A4)/(A7), and the
bridge to the full profile envelope remain explicit outside inputs.

## Build Note

Do not run `lake build` casually in this repository. Build only with the
pinned Lean/Mathlib versions and matching precompiled Mathlib cache.
Contributor audit notes report a full pinned build on 2026-07-11 with 8038
jobs, including `GrandeFinale.CollisionAwarePole`; this integration did not
rerun Lake.
