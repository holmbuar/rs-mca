# Lean minimal closed-ledger / UNIF interface

**Date:** 2026-07-19.
**Handoff base:** `951ad203eee5343716e08683e01645db1366a8e4`.
**Replayed base:** upstream `9908454995f3f195cfe748f35a1135211609d066`.
**Status:** **FORMALIZATION / PROVED FINITE COMPILER UNDER EXPLICIT HYPOTHESES / CONDITIONAL RS INSTANTIATION / LEAN 4.31 REPLAY PASSED**.

## Claim

`experimental/lean/asymptotic_spine/AsymptoticSpine/UniformClosedLedger.lean`
formalizes the minimal finite compiler needed to consume semantic C1--C9 and
primitive payments without changing the order of the row supremum and profile
sum.

For each received line `r`, the module records a finite list of post-deletion
semantic profiles.  A profile keeps:

- its semantic owner (`C1`, ..., `C9`, or primitive);
- its assigned **distinct-slope** list after first match;
- its actual line/profile ray budget `U(r,lambda)`;
- its residual, image-normalized Sidon, and ray intermediates;
- its natural profile scale; and
- the three separately printed loss factors whose product must fit inside the
  declared compiler loss.

A line then exposes three independent obligations:

1. **first-match ownership:** assigned slope lists are disjoint;
2. **atlas exhaustiveness:** the producer supplies the numerical consequence
   that the assigned union covers the actual bad-slope numerator;
3. **profile-count control:** the number of realized semantic profiles is at
   most the printed cap.

`firstMatchOwnership` records no-duplication on the supplied slope lists but is
not consumed by the scalar proof of `compile`.  That proof consumes the
cardinal inequality `atlasExhaustive`; deriving it from actual witness coverage
and semantic first-match ownership remains a producer obligation.

The row package adds the line-local uniformity premise

```text
for every supplied ledger line r,
  sum_lambda naturalScale(r, lambda) <= envelope.
```

The theorem `UniformClosedLedger.compile` derives

```text
sup_r badCount(r) <= compilerLoss * envelope.
```

The proof therefore implements

```text
sup_r sum_lambda U(r, lambda)
```

rather than the generally larger quantity

```text
sum_lambda sup_r U(r, lambda).
```

This is a finite post-geometric interface.  `lines` is the producer-supplied
finite line list, not a proof that all received RS lines have been enumerated;
`atlasExhaustive` is a numerical coverage certificate, not a formal witness
membership theorem.  An RS--MCA instantiation must supply those semantic
bridges.  The type also does not enforce one global profile atlas fixed before
the received line or coherence of profile identities across different lines.
Likewise, `naturalTotal` is the profile sum only: the universal
`1 + (n-a+1)` terms in the literal envelope must be absorbed by the caller's
`envelope` or represented by additional paid profiles.

## Field and declaration map

| Declaration | Role | Source/interface anchor |
| --- | --- | --- |
| `ProfilePayment.owner` | Semantic C1--C9/primitive owner label only; constructing it proves no classification | `def:first-match`; admissibility conditions A2--A6 |
| `ProfilePayment.assignedSlopes` and `assignedSlopes_nodup` | One post-deletion first-match distinct-slope cell | `def:first-match`, `lem:first-match-bound` |
| `ClosedLineLedger.firstMatchOwnership` | No-duplication on the supplied flattened lists; an audit field not consumed by `compile` | `def:first-match`, `prop:first-match-sum-detail` |
| `ClosedLineLedger.atlasExhaustive` | Cardinal inequality consumed by the compiler; not itself a witness-coverage theorem | admissibility condition A2; `lem:first-match-bound` |
| `ProfilePayment.naturalScale` | Caller-supplied denominator-cleared integer representative of the profile scale; it must cover `1 + barN_lambda` for frontiers (1.6), while the compact envelope uses `barN_lambda` | `def:profile-payment`, `eq:profile-envelope` |
| `ProfilePayment.residualToFull` | Residual/post-deletion budget compared with the full profile scale | `lem:exact-profile-addback`; admissibility condition A2 |
| `ProfilePayment.imageNormalizedSidon` | Image-scale Sidon or MI/MA payment input | admissibility conditions A3--A5 |
| `ProfilePayment.rayCompiler` | Residual budget projected to distinct slopes | `hyp:ray-compiler`; admissibility condition A6 |
| `ProfilePayment.distinctSlopePayment` | The actual assigned slope cell is paid by `U(r,lambda)` | `def:profile-payment`, `lem:first-match-bound` |
| `UniformClosedLedger.windowUniformity` | Line-local `sum_lambda naturalScale <= envelope`, before the outer maximum | `eq:profile-envelope`; admissibility condition A7 |
| `UniformClosedLedger.lines` | Finite supplied family only; completeness over all received lines and fixed-before-line atlas coherence remain external | `thm:exact-finite-profile-compiler` boundary |
| `ProfilePayment.paidAtNaturalScale` | Composes the three local payment stages at one profile's own scale | local compiler chain only; no geometric input manufactured |
| `ProfilePayment.ofDirect` | Adapter for any separately proved direct distinct-slope payment | direct-payment branch of admissibility condition A6; intermediate stages are identities |
| `ClosedLineLedger` | First-match ownership, atlas exhaustiveness, and realized-profile cap for one line | semantic atlas boundary |
| `ClosedLineLedger.bad_le_budgetTotal` | `bad(r) <= sum_lambda U(r,lambda)` | first-match slope projection |
| `ClosedLineLedger.budgetTotal_le_loss_mul_naturalTotal` | Sum local payments inside one received line | natural-profile-scale payment |
| `UniformClosedLedger.rowProfileCountSup_le_profileCap` | Keeps profile-count control explicit | subexponential realized-profile obligation, finite form |
| `UniformClosedLedger.rowBudgetSup_le_loss_mul_rowNaturalSup` | Bounds `sup_r sum_lambda U(r,lambda)` directly, without interchanging maximum and sum | `(UNIF)` finite core |
| `UniformClosedLedger.rowBad_le_loss_mul_rowNaturalSup` | Correct `sup_r sum_lambda` composition | `(UNIF)` finite core |
| `UniformClosedLedger.compile` | Minimal closed-ledger compiler | complete finite interface under named hypotheses |
| `UniformClosedLedger.compile_to_target` | Explicit target comparison wrapper | target/profile-envelope comparison remains an input |
| `sup_sum_interchange_falsifier` | Two-line diagonal regression | refutes silent `sup/sum` interchange |

## Relation to existing formalizations

This module does not replace the exact finite-field locator-prefix theorem

```text
GrandeFinale.PrefixAtlasBridge.B_MCA_rsEval_le_of_linewise_prefixBudgets.
```

That theorem proves a fixed-row RS implication once line-dependent prefix-cell
budgets and their uniform line sum are supplied.  The new module sits one level
above that structural partition: it names the semantic owner, natural profile
scale, residual/Sidon/ray chain, realized profile cap, and the final line-local
uniformity premise.  Conversely, it does not reconstruct the finite-field RS
witness catalogue already available in the Grande Finale package.

The module also complements rather than duplicates:

- `FirstMatch.lean`, which proves abstract first-match disjointization;
- `PrefixAtlas.lean`, which proves raw totality but no payment;
- `AddBack.lean`, which proves one residual-to-full sufficiency theorem;
- `EffectiveClosure.lean`, which supplies scoped support-to-ray adapters; and
- `ProfileEnvelope.lean`, whose target compiler currently consumes aggregate
  closed-ledger inputs.

## Adversarial regression

`sup_sum_interchange_falsifier` uses two lines and two profiles:

```text
line 0 budgets = [1,0]
line 1 budgets = [0,1].
```

It proves by kernel computation that

```text
sup_line sum_profile = 1,
sum_profile sup_line = 2.
```

Thus independently maximizing every profile and then summing is not an
equivalent or sharp replacement for `(UNIF)`, even in the smallest diagonal
example.

## Verification

Run from the repository root:

```sh
cd experimental/lean/asymptotic_spine
lake build AsymptoticSpine.UniformClosedLedger
lake build
```

Replayed from a clean package on Lean `v4.31.0`.  The handoff initially failed
at the final four-factor reassociation in `paidAtNaturalScale`; replacing the
non-closing `rw [Nat.mul_assoc]` with `simp only [Nat.mul_assoc]` repaired that
proof without changing its statement.  The focused build passed with 7 jobs
and the full package passed with 28 jobs.

The source contains `#print axioms` checks for the public compiler chain and
both executable fixtures.  The compiler chain reports only the expected
kernel/library principles `propext` and, where lists are involved, `Quot.sound`;
the diagonal falsifier reports no axioms.  No `sorryAx` appears.

## Exact remaining work

The formalization makes the missing work smaller and typed; it does not solve
it.  A genuine RS instantiation still has to construct:

- an executable semantic C1--C9/primitive owner on actual witnesses/slopes;
- natural-scale payments for every realized profile;
- the residual-to-full comparison where deletion changes the mean;
- image-normalized Sidon/MI--MA on actual C9 survivors;
- a direct ray compiler for the remaining C8/C9 profiles;
- a subexponential profile cap along the row sequence; and
- the uniform line-local envelope comparison and final target inequality.

The next useful packet is an instantiation on one actual post-prefix residual
class.  A support count, pair moment, max-fiber theorem, or fixed-chart bound is
not enough unless it supplies the fields through distinct slopes.

## Nonclaims

This packet does **not** claim:

- a semantic C1--C9 classification for any deployed row;
- a proof of C7, C8, C9, Q, SP, or BC;
- a new Sidon/MI--MA theorem;
- a new balanced-core ray bound;
- asymptotic subexponential profile count or window uniformity;
- identity dominance or a complete profile-envelope comparison;
- a finite adjacent safe row, threshold improvement, or prize claim; or
- completeness of the supplied line list, fixed-before-line atlas coherence,
  or identification of `rowBad` with the actual RS--MCA numerator.
