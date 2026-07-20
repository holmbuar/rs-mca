# M31 Q rooted-shell Lean package

This is the stdlib-only Lean validation package for
`experimental/notes/thresholds/m31_q_rooted_shell_envelope.md`.

## Scope

The package kernel-checks:

- the generic rooted-shell excess summation compiler;
- the exact `3+7` deployed list/MCA deductions and integer reserves from the
  pinned scaled-floor packet values;
- the finite Chebyshev/twin-coset control showing `2+7` fails while `3+7`
  holds, including support shape, common prefix, distance, quotient-proxy,
  common-core, `T₂`-fiber, and non-product-closure checks.

It does **not** prove the open deployed local shell hypothesis, the gigantic
binomial quotient values, row-sharp Q, an adjacent safe row, or a complete
first-match ledger.

## Validation policy

There is no Mathlib dependency. Do not build this package locally in agent
sessions. Push the complete research packet to a fork branch and open a draft
PR targeting `holmbuar/rs-mca:main`; the repository's PR-triggered GitHub
Actions workflow is the authoritative Lean build.
