import AsymptoticSpine.ClosedLedgerExtension
import AsymptoticSpine.PrimitiveBoolean
import AsymptoticSpine.EffectiveClosure

namespace AsymptoticSpine
namespace C9ResidualMaxFiber

/-!
# Exact post-deletion C9 max-fiber producer

The literal phrase "surviving C1--C8" is not an evaluable predicate on a bare
`PrimitiveBooleanLeaf`.  This module repairs that finite interface locally.
A `ProfileData` value carries an explicit earlier-owner function and proves that
the residual list is exactly the complement of those earlier owners inside the
complete fixed-weight slice.

For one residual prefix key, a supplied `(SE2)` certificate projects actual
post-deletion supports to distinct slopes.  A row-sharp max-fiber theorem on the
full prefix class then pays the residual C9 slope image by monotonicity.  The
payment is installed directly: no low-energy/Sidon assertion is manufactured.
This is the finite producer boundary suggested by the equivalence between the
positive-rate C9 moment statement and primitive Q/max-fiber control.

The module does not prove the row-sharp max-fiber hypothesis, construct the
actual C1--C8 predicates for an RS row, count all realized keys, establish a
separate asymptotic ray theorem beyond `(SE2)`, prove `(UNIF)`, compare with the
target, or close a deployed row.
-/

/-- The only owners allowed before the C9 residual. -/
inductive PreC9Owner where
  | c1 | c2 | c3 | c4 | c5 | c6 | c7 | c8
  deriving DecidableEq, Repr

/-- One exactly post-C1--C8 primitive prefix profile with a row-sharp full-fiber
bound and an actual distinct-slope support projection. -/
structure ProfileData (Key : Type) [DecidableEq Key] (compilerLoss : Nat) where
  leaf : PrimitiveBooleanLeaf Key
  earlierOwner : Vector Bool leaf.full.dimension → Option PreC9Owner
  residual_exact : ∀ x : Vector Bool leaf.full.dimension,
    x ∈ leaf.residual ↔ x ∈ leaf.full.points ∧ earlierOwner x = none
  syndromeKey : Key
  slopeCell : SE2Certificate (Vector Bool leaf.full.dimension) Nat
  supportsInResidual : List.Sublist slopeCell.supports
    (residualPrefixFiber leaf syndromeKey)
  naturalScale : Nat
  rowSharpMaxFiber :
    (fullPrefixFiber leaf syndromeKey).length ≤ compilerLoss * naturalScale

/-- Every selected slope support is literally outside the earlier C1--C8 owner
image, not merely declared "primitive" in prose. -/
theorem ProfileData.support_not_earlier
    {Key : Type} [DecidableEq Key] {compilerLoss : Nat}
    (data : ProfileData Key compilerLoss) {gamma : Nat}
    (hgamma : gamma ∈ data.slopeCell.slopes) :
    data.earlierOwner (data.slopeCell.supportOf gamma) = none := by
  have hchosen : data.slopeCell.supportOf gamma ∈
      data.slopeCell.slopes.map data.slopeCell.supportOf :=
    List.mem_map.mpr ⟨gamma, hgamma, rfl⟩
  have hsupport : data.slopeCell.supportOf gamma ∈ data.slopeCell.supports :=
    data.slopeCell.chosen_sublist.subset hchosen
  have hfiber : data.slopeCell.supportOf gamma ∈
      residualPrefixFiber data.leaf data.syndromeKey :=
    data.supportsInResidual.subset hsupport
  have hresidual : data.slopeCell.supportOf gamma ∈ data.leaf.residual := by
    unfold residualPrefixFiber mapFiber at hfiber
    exact (List.mem_filter.mp hfiber).1
  exact ((data.residual_exact _).mp hresidual).2

/-- Row-sharp full-prefix max-fiber control pays the actual post-deletion C9
slope list through `(SE2)` and residual monotonicity. -/
theorem ProfileData.slopes_paid
    {Key : Type} [DecidableEq Key] {compilerLoss : Nat}
    (data : ProfileData Key compilerLoss) :
    data.slopeCell.slopes.length ≤ compilerLoss * data.naturalScale := by
  calc
    data.slopeCell.slopes.length ≤ data.slopeCell.supports.length :=
      se2_support_injection data.slopeCell
    _ ≤ (residualPrefixFiber data.leaf data.syndromeKey).length :=
      data.supportsInResidual.length_le
    _ ≤ (fullPrefixFiber data.leaf data.syndromeKey).length :=
      residualPrefixFiber_length_le_fullPrefixFiber data.leaf data.syndromeKey
    _ ≤ compilerLoss * data.naturalScale := data.rowSharpMaxFiber

/-- Install the exact residual as a directly paid C9 profile.  The direct
adapter is intentional: the row-sharp max-fiber theorem has already supplied
the needed support payment, so inserting a synthetic Sidon stage would obscure
the proof boundary. -/
def ProfileData.payment
    {Key : Type} [DecidableEq Key] {compilerLoss : Nat}
    (data : ProfileData Key compilerLoss) : ProfilePayment compilerLoss :=
  ProfilePayment.ofDirect .c9 data.slopeCell.slopes data.naturalScale
    compilerLoss data.slopeCell.slopes_nodup data.slopes_paid

@[simp] theorem ProfileData.payment_owner
    {Key : Type} [DecidableEq Key] {compilerLoss : Nat}
    (data : ProfileData Key compilerLoss) :
    data.payment.owner = .c9 := rfl

@[simp] theorem ProfileData.payment_assignedSlopes
    {Key : Type} [DecidableEq Key] {compilerLoss : Nat}
    (data : ProfileData Key compilerLoss) :
    data.payment.assignedSlopes = data.slopeCell.slopes := rfl

/-- Append the exact C9 residual after an earlier closed line.  The explicit
slope disjointness proof prevents a support-level complement from being
silently confused with slope-level first match. -/
def ProfileData.extendLine
    {Key : Type} [DecidableEq Key] {compilerLoss profileCap : Nat}
    (data : ProfileData Key compilerLoss)
    (line : ClosedLineLedger compilerLoss profileCap)
    (hdisjoint : ∀ gamma ∈ line.assignedSlopeList,
      gamma ∉ data.slopeCell.slopes) :
    ClosedLineLedger compilerLoss (profileCap + 1) :=
  line.appendPayment data.payment hdisjoint

/-- Exact C9 ray-budget telescope inside one received line. -/
theorem ProfileData.extendLine_budgetTotal
    {Key : Type} [DecidableEq Key] {compilerLoss profileCap : Nat}
    (data : ProfileData Key compilerLoss)
    (line : ClosedLineLedger compilerLoss profileCap)
    (hdisjoint : ∀ gamma ∈ line.assignedSlopeList,
      gamma ∉ data.slopeCell.slopes) :
    (data.extendLine line hdisjoint).budgetTotal =
      line.budgetTotal + compilerLoss * data.naturalScale := by
  simpa [ProfileData.extendLine, ProfileData.payment] using
    (ClosedLineLedger.appendPayment_budgetTotal line data.payment hdisjoint)

/-- Exact C9 natural-scale telescope inside one received line. -/
theorem ProfileData.extendLine_naturalTotal
    {Key : Type} [DecidableEq Key] {compilerLoss profileCap : Nat}
    (data : ProfileData Key compilerLoss)
    (line : ClosedLineLedger compilerLoss profileCap)
    (hdisjoint : ∀ gamma ∈ line.assignedSlopeList,
      gamma ∉ data.slopeCell.slopes) :
    (data.extendLine line hdisjoint).naturalTotal =
      line.naturalTotal + data.naturalScale := by
  simpa [ProfileData.extendLine, ProfileData.payment] using
    (ClosedLineLedger.appendPayment_naturalTotal line data.payment hdisjoint)

#print axioms ProfileData.support_not_earlier
#print axioms ProfileData.slopes_paid
#print axioms ProfileData.extendLine_budgetTotal
#print axioms ProfileData.extendLine_naturalTotal

end C9ResidualMaxFiber
end AsymptoticSpine
