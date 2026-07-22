# Lean correspondence: KoalaBear boundary-prefix Q shell compiler

## Scope

`KbUqBoundaryPrefix.lean` is the stdlib-only formal companion to
`experimental/notes/frontier-adjacent/kb_uq_boundary_prefix_tangent_rooted_shell_v1.md`.
It formalizes only the finite summation compiler and the reported ledger
arithmetic.

| Lean declaration | Paper/note statement |
|---|---|
| `LocalEnvelope` | pointwise hypothesis `KB_TANGENT_ROOTED_Q_SHELL(b,c)` after cross multiplication |
| `degreeSum_le_intercept_add_excess` | `d_e <= b + max(d_e-b,0)` summed over shells |
| `localEnvelope_mul_le` | sum of the pointwise shell inequalities |
| `excessSum_le_scaledFloor` | exact conversion from a strict cross-multiplied bracket to an integer floor |
| `shellCompilerNoRoot` | non-column-far tangent-zero-anchor compiler `(C-sparse)` |
| `shellCompilerWithRoot` | column-far selected-root compiler `(C-far)` |
| `deployed_sparse_cap` | `3*913632 + 400386212557 = 400388953453` |
| `deployed_uniform_cap` | `1 + 3*981104 + 400386212557 = 400389155870` |
| `deployed_pruning_dividend` | displayed pruning dividend `202417` |
| `deployed_remaining_reserve` | exact post-Q reserve `274980327721258113` |
| window declarations | the exact `(54192,4807520)` corner and the two one-step failures |

## Source theorem boundary

The module does not formalize the following already-integrated semantic facts:

- `thm:exact-sparsification` and `(SP3)`;
- `RsMcaThresholds.ExactSparsification.mcaBad_sub_mem_iff`;
- exact-card witness selection from
  `GrandeFinale.RSExactCardWitnessBridge`;
- support-to-slope injectivity from the proof of `(PO6)` in
  `thm:canonical-partial-occupancy-atlas`;
- the frozen tangent deletion from upstream PR #1049;
- active Q membership from `prop:q-boundary-divisor`.

Those are source-bound in the note and manifest.  The only unproved input is the
single pointwise finite shell hypothesis itself.

## Giant arithmetic boundary

Lean intentionally does not reconstruct `C(2097152,1116048)` or
`2130706433^67471`.  The independent Python verifier computes those integers by
both direct combinatorics and prime-valuation reconstruction, then supplies the
exact floor `400386212557` whose downstream arithmetic Lean checks.

## Nonclaims

This module does not prove the shell hypothesis, an unconditional Q maximum,
semantic first-match exhaustivity, a balanced-core payment, a final residual
payment, a refund, a row refutation, or row closure.  A declaration is certified
only after the fork CI package build succeeds and its statement is manually
matched to the note.
