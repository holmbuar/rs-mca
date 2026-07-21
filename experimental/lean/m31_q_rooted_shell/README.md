# M31 Q rooted-shell Lean package

This is the stdlib-only Lean validation package for
`experimental/notes/thresholds/m31_q_rooted_shell_envelope.md` and
`experimental/notes/thresholds/m31_q_three_plus_seven_multiplicative_counterexample.md`.

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
  `97,867`.

The multiplicative packet is a counterexample to a support-only proof route.
It does **not** prove that its supports survive the actual slope-level C1--C8
first-match atlas, and therefore does not refute the deployed Mersenne-31 exact
residual.

The package does **not** prove the open deployed local shell hypothesis, the
gigantic binomial quotient values, row-sharp Q, an adjacent safe row, an MCA
slope projection, or a complete first-match ledger.

## Validation policy

There is no Mathlib dependency. Do not build this package locally in agent
sessions. Push the complete research packet to a fork branch and open a draft
PR targeting `holmbuar/rs-mca:main`; the repository's PR-triggered GitHub
Actions workflow is the authoritative Lean build.
