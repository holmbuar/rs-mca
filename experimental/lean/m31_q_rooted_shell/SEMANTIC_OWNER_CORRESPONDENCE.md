# Semantic C1--C8 owner-or-envelope: source/Lean correspondence

## Authority and status

Source-facing note:

`experimental/notes/thresholds/m31_q_semantic_owner_shell.md`

Formal modules:

- `M31QRootedShell/SemanticOwner.lean`
- `M31QRootedShell/SemanticNaturalScale.lean`

Status:

```text
PROVED SEMANTIC INTERFACE AND COMPILERS
CONDITIONAL SEMANTIC SO3+7 INPUT
MANDATORY F_241 REGRESSION
OPEN DEPLOYED M31 RESIDUAL
```

The modules import the rooted-shell arithmetic and multiplicative route cut
from upstream PR #1005.  They do not repeat either proof or finite support
catalogue.

## Declaration map

| Source object | Lean declaration | Statement audit |
|---|---|---|
| ordered earlier-owner identifiers | `OwnerId` | Exactly C1 through C8; C9 is the residual. |
| executable fixed-before-line owner function | `FixedOwnerFunction`, `FixedOwnerFunction.classify` | Eight Boolean triggers are stored once and checked in literal C1--C8 order. |
| owner-free regression adapter | `allResidualOwnerFunction`, `allResidualOwnerFunction_classify` | Every trigger is false; every explanation is classified `none`. |
| received line -> explanation -> witness -> codeword -> ray -> slope | `SemanticChain` | Every map is explicit. Direct support/codeword/ray/slope projections have compatibility laws with the displayed chain. |
| natural prefix denominator | `NaturalProfileScale.denominator` | Literally `profileFieldCard ^ prefixDepth`. |
| integral natural average | `NaturalProfileScale.averageCeil` | `ceil(fullSupportMass / denominator)` through the local natural-number `ceilDiv`. |
| natural paid numerator | `NaturalProfileScale.naturalNumerator` | Literally `loss * (1 + averageCeil)`. |
| exact slope numerator and denominator | `ExactSlopeBudget` | Stores `U_owner`, positive `q_slope`, and `U_owner <= q_slope`; no equality with the prefix denominator is assumed. |
| distinct line-local slope image | `PaidSlopeProfile` | The slope list is duplicate-free and its cardinality is at most the exact numerator, which is at most the natural numerator. |
| semantic owner soundness | `PaidOwnerLedger` | The global owner function is separate from line-local profiles. Positive classification proves semantic validity and membership of the actual slope in the paid image. |
| one concrete earlier owner | `EarlierOwnerCertificate` | Stores the exact first-match equality `classify x = some owner`. |
| proposition-valued owner branch | `HasEarlierOwner` | Defined as `Nonempty (EarlierOwnerCertificate ...)`, so the semantic disjunction remains a proposition without erasing the concrete certificate type. |
| full chain preservation | `EarlierOwnerCertificate.preserves_chain` | Prints support/witness, codeword/witness, ray/codeword, slope/ray equalities and paid slope-image membership. |
| exact and natural budget chain | `EarlierOwnerCertificate.budget_chain` | Produces `#slopes <= U_owner <= q_slope` and `U_owner <= naturalNumerator`. |
| rooted semantic shell | `RootedShell` | One line, prefix target, anchor, shell, valid explanations, and duplicate-free support projections. |
| generic local rooted-shell inequality | `LocalEnvelopeAt` | Exact natural subtraction `Q * (degree-b) <= c * ambientShell`. |
| literal profile-scale inequality | `LocalNaturalEnvelopeAt`, `localNaturalEnvelopeAt_iff` | The coefficient is definitionally `profileFieldCard ^ prefixDepth`; this is the printed `q_prof^w` formula. |
| actual post-C1--C8 residual | `IsActualPostC1C8Residual` | Every shell explanation is classified `none` by the same global owner function. |
| generic semantic disjunction | `SemanticEnvelopeOrOwner` | Generic local envelope or a concrete explanation satisfying `HasEarlierOwner`. |
| literal natural-scale semantic disjunction | `SemanticNaturalEnvelopeOrOwner` | Specializes the generic coefficient to `NaturalProfileScale.denominator`. |
| owner branch impossible on actual residual | `actualResidual_has_no_certified_owner` | Contradicts `classify x = none` with the certificate's `classify x = some owner`. |
| actual-residual `3+7` compiler | `semantic_three_plus_seven_on_actual_residual` | The generic semantic disjunction at literal `(b,c)=(3,7)` implies the local envelope on the actual residual. |
| natural-scale actual-residual compiler | `semantic_natural_three_plus_seven_on_actual_residual` | Produces `q_prof^w * max(d-3,0) <= 7 H` on the actual residual. |
| violation-to-owner compiler | `violation_forces_certified_earlier_owner` | A strict generic local-envelope violation eliminates the first disjunct and returns the concrete owner certificate. |
| natural-scale violation compiler | `natural_violation_forces_certified_earlier_owner` | Uses the literal `profileFieldCard ^ prefixDepth` coefficient. |
| imported F_241 envelope failure | `f241_localEnvelope_fails` | Reuses PR #1005's `three_plus_seven_fails` after identifying the rooted degree. |
| exact F_241 natural scale | `f241NaturalScale`, `f241NaturalScale_denominator` | `q_prof=241`, `w=2`, full support mass `choose 20 10`, loss one, and denominator exactly the imported `q=58,081`. |
| mandatory generic F_241 owner regression | `f241_semantic_target_forces_certified_owner` | Every generic semantic disjunction on the ten-neighbor packet returns an earlier paid owner. |
| mandatory natural-scale F_241 owner regression | `f241_semantic_natural_target_forces_certified_owner` | The exact `241^2` target returns an earlier paid owner. |
| all-residual rejection | `f241_all_residual_rejects_semantic_target`, `f241_all_residual_rejects_semantic_natural_target` | An actual-residual declaration plus either semantic target would imply the false F_241 envelope. |
| explicit owner-free rejection | `f241_owner_free_function_rejects_semantic_target` | Instantiates the fixed all-false C1--C8 classifier and rejects the semantic target. |

## Source-statement comparison

The research note asks for

```text
q_prof^w * max(d_e(A)-3,0) <= 7 H_e
or
an excess neighbor has a certified earlier paid slope owner.
```

`SemanticNaturalEnvelopeOrOwner` is the exact finite interface.  The owner
certificate is stronger than a support tag because its type includes semantic
validity, the entire witness/codeword/ray/slope chain, membership in a
deduplicated line-local slope image, the exact slope numerator and slope
denominator, and the owner's natural prefix-profile scale.

On `IsActualPostC1C8Residual`, the owner branch is contradictory, so
`semantic_natural_three_plus_seven_on_actual_residual` yields the literal
natural-scale inequality.  Conversely, a strict violation of the first branch
yields the owner certificate through
`natural_violation_forces_certified_earlier_owner`.

## Proof boundary

Lean kernel-checks the types, finite logical compilers, budget propagation, the
literal natural normalization, and the F_241 regression.  The following remain
hypotheses or future instantiations:

- the actual deployed Reed--Solomon explanation and witness types;
- the row-uniform executable definitions of all eight C1--C8 triggers;
- the theorem that every positive trigger has its printed paid slope profile;
- `SemanticNaturalEnvelopeOrOwner` for every deployed rooted shell;
- row-sharp Q, an adjacent safe row, and the global summed completion ledger.

The F_241 source packet contains supports but no received line, explanation,
codeword ray, or slope.  Therefore its quotient/dihedral and common-core facts
cannot construct `EarlierOwnerCertificate`.  The regression proves that an
owner-free/support-only adapter cannot pass the semantic target.

## Validation policy

The package is stdlib-only and targets Lean `v4.31.0`.  The package root
`M31QRootedShell.lean` imports both semantic modules.  The authoritative build
is the fork draft-PR GitHub Actions run; no local Lean build is claimed.
