# KoalaBear boundary-prefix Q Lean package

Stdlib-only validation package for the finite shell compiler in
`kb_uq_boundary_prefix_tangent_rooted_shell_v1.md`.

It checks:

- no-root and one-root shell summation compilers;
- exact integer floor conversion from cross-multiplied packet data;
- the deployed sparse and uniform caps;
- the pruning dividend, post-Q reserve, and viable-window boundary arithmetic.

It does not prove the pointwise shell hypothesis or calculate the giant
binomial quotient.  Those boundaries are explicit in `CORRESPONDENCE.md`.

There is no Mathlib dependency.  Do not build locally in an agent session.
The authoritative build is the fork draft-PR Lean check.
