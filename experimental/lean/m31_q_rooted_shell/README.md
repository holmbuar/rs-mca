# M31 Q rooted-shell Lean package

This is the stdlib-only Lean validation package for
`experimental/notes/thresholds/m31_q_rooted_shell_envelope.md`,
`experimental/notes/thresholds/m31_q_three_plus_seven_multiplicative_counterexample.md`,
and `experimental/notes/audits/m31_padding_bridge_audit.md`.

## Scope

The package kernel-checks:

- the generic rooted-shell excess summation compiler;
- the exact `3+7` deployed list/MCA deductions and integer reserves from the
  pinned scaled-floor packet values;
- the finite Chebyshev/twin-coset control showing `2+7` fails while `3+7`
  holds, including support shape, common prefix, distance, quotient-proxy,
  common-core, `T₂`-fiber, and non-product-closure checks;
- the explicit `F_241` order-twenty multiplicative-subgroup packet showing
  that support-level dihedral and planted-core pruning does not imply `3+7`:
  the retained fifteen-support target has trivial support stabilizers and empty
  common core, but one rooted shell has degree ten and exact violation margin
  `97,867`;
- the M31 interior padding-bridge audit: one genuine `RS[F_11,D,4]` pair whose
  actual-error frame is unchanged under two fixed domain orders, while the
  canonical discarded-agreement masks change direct syzygy transportability
  and the padded pair index; and
- the exact deployed degree barriers showing that the certified first
  actual-error row cannot directly transport for `j<=960363`, and none of the
  first three can directly transport for `j<=918833`.

The multiplicative packet is a counterexample to a support-only proof route.
It does **not** prove that its supports survive the actual slope-level C1--C8
first-match atlas, and therefore does not refute the deployed Mersenne-31 exact
residual.

The padding packet is a counterexample to an unmasked identification of the
canonical padded-locator and actual-error syzygy modules.  Its exact successor
input is `MASKED_DIAGONAL_SATURATION`: a concrete bridge must retain the ordered
first-`a` selector, actual-error/padding root masks, and coordinatewise
padding-divisibility certificate on every source key.

The package does **not** prove the open deployed local shell hypothesis, the
gigantic binomial quotient values, row-sharp Q, an adjacent safe row, an MCA
slope projection, a complete first-match ledger, or the general polynomial
module/Forney theorem used in the padding audit.

## Validation policy

There is no Mathlib dependency. Do not build this package locally in agent
sessions. Push the complete research packet to a fork branch and open a draft
PR targeting `holmbuar/rs-mca:main`; the repository's PR-triggered GitHub
Actions workflow is the authoritative Lean build.
