# KoalaBear tangent-pruned Q correspondence

Status: **PROVED LOCAL / CONDITIONAL CAP**.

The source note is
`experimental/notes/frontier-adjacent/kb_uq_boundary_prefix_pruned_shell_v1.md`.

## Statement map

| Source claim | Lean declaration |
|---|---|
| Pointwise rooted-shell inequalities sum after exact cross multiplication | `KbUqBoundaryPrefix.localEnvelope_mul_le` |
| Column-far branch with one selected anchor | `KbUqBoundaryPrefix.rootedShellEnvelopeAnchored` |
| Tangent-pruned sparse branch with no leading anchor | `KbUqBoundaryPrefix.rootedShellEnvelopePruned` |
| A family above either compiled bound falsifies a local inequality | `localEnvelope_fails_of_large_anchored_family`, `localEnvelope_fails_of_large_pruned_family` |
| Root-count arithmetic gives at least `67473` source hits | `KbUqBoundaryPrefix.sourceIntersectionLower` |
| `67473=w+2`, shell counts, tangent reserve, and row constants | `KbUqBoundaryPrefix.deployedConstantsExact` |
| Conditional cap `57198030366` and sparse cap `57198030365` | `KbUqBoundaryPrefix.normalizedConditionalCapsExact` |
| Remaining reserve `274980670912383617` | `KbUqBoundaryPrefix.conditionalReserveExact` |
| Full-multiplier window edge and scalar-extension separation margin | `fullMultiplierBoundaryExact`, `scalarExtensionSeparationExact` |

## Manual source match

The Lean compiler consumes exactly the pointwise condition

```text
Q * (d_e-b) <= c H_e
```

with natural subtraction.  `rootedShellEnvelopeAnchored` contributes one root
slope; `rootedShellEnvelopePruned` does not.  This distinction is the correction
found by the adversarial pass: the extension-pole lower family is column-far,
whereas the source-support `w+2` theorem applies only after the non-column-far
tangent deletion.

The semantic proof that a tangent survivor is nonzero on every source-support
coordinate, the exact-support selection, and the polynomial root bound remain
source theorems cited in the note.  The local Lean theorem
`sourceIntersectionLower` checks the complete integer deduction once those
proved semantic inputs are instantiated.

The enormous values `floor(T_CF/p^w)` and `floor(T_SP/p^w)` are recomputed twice
by the packet verifier rather than reduced by Lean's kernel.  Lean checks every
deduction from the frozen quotient `57198030365`.

## Nonclaims

The package does not prove `KB_V4_PRUNED_Q_ROOTED_SHELL(0,1)`, an unconditional
`U_Q`, a refund, a balanced-core payment, or row closure.  It imports only
`Std`, contains no `sorry`, `admit`, `native_decide`, or added axiom, and does
not depend on Mathlib.
