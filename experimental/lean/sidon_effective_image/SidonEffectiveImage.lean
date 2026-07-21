import Std

/-!
# C9 full-prefix owner-refund floor

This stdlib-only module mirrors the exact finite boundary of the C9 producer
without importing an open-PR module.  It keeps the post-C1--C8 residual as the
literal owner complement, keeps the `(SE2)` support projection genuine, and
isolates the arithmetic obstruction created when a full-prefix payment is used
inside a ledger that also pays an earlier owner.

The deployed Mersenne-31 list constants checked here are finite arithmetic only.
The module does not enumerate the deployed support slice and does not prove the
row-sharp Q inequality.
-/

namespace SidonEffectiveImage

/-- The only semantic owners allowed before C9. -/
inductive PreC9Owner where
  | c1 | c2 | c3 | c4 | c5 | c6 | c7 | c8
  deriving DecidableEq, Repr, BEq

/-- Exact post-C1--C8 residual: full-slice membership plus no earlier owner. -/
def residualOf {Support : Type} (full : List Support)
    (earlierOwner : Support → Option PreC9Owner) : List Support :=
  full.filter (fun x => decide (earlierOwner x = none))

/-- The complementary earlier-owned part of the same full prefix fiber. -/
def ownedOf {Support : Type} (full : List Support)
    (earlierOwner : Support → Option PreC9Owner) : List Support :=
  full.filter (fun x => decide (earlierOwner x ≠ none))

/-- Standalone two-clause residual condition used by the C9 producer. -/
theorem mem_residualOf_iff {Support : Type} {full : List Support}
    {earlierOwner : Support → Option PreC9Owner} {x : Support} :
    x ∈ residualOf full earlierOwner ↔
      x ∈ full ∧ earlierOwner x = none := by
  simp [residualOf]

/-- The canonical owner complement is an exact cardinality partition. -/
theorem residual_owned_length {Support : Type}
    (earlierOwner : Support → Option PreC9Owner) :
    ∀ full : List Support,
      (residualOf full earlierOwner).length +
          (ownedOf full earlierOwner).length = full.length := by
  intro full
  induction full with
  | nil => simp [residualOf, ownedOf]
  | cons x xs ih =>
      by_cases h : earlierOwner x = none
      · simp [residualOf, ownedOf, h, ih]
      · simp [residualOf, ownedOf, h, ih]

/-- A finite genuine `(SE2)` support projection, matching the integrated API. -/
structure SE2Certificate (Support Slope : Type) where
  supports : List Support
  slopes : List Slope
  supportOf : Slope → Support
  supports_nodup : supports.Nodup
  slopes_nodup : slopes.Nodup
  chosen_sublist : List.Sublist (slopes.map supportOf) supports

/-- Distinct slopes inject into their selected noncommon supports. -/
theorem se2_support_injection {Support Slope : Type}
    (certificate : SE2Certificate Support Slope) :
    certificate.slopes.length ≤ certificate.supports.length := by
  simpa using certificate.chosen_sublist.length_le

/-- Standalone mirror of the load-bearing C9 profile fields.

The final field is deliberately the exact open-PR statement:
`fullPrefixFiber.length ≤ compilerLoss * naturalScale`.
-/
structure C9ProfileData (Support Slope : Type) where
  fullPrefixFiber : List Support
  earlierOwner : Support → Option PreC9Owner
  slopeCell : SE2Certificate Support Slope
  supportsInResidual : List.Sublist slopeCell.supports
    (residualOf fullPrefixFiber earlierOwner)
  compilerLoss : Nat
  naturalScale : Nat
  rowSharpMaxFiber :
    fullPrefixFiber.length ≤ compilerLoss * naturalScale

/-- Every selected `(SE2)` support is literally outside the earlier-owner image. -/
theorem C9ProfileData.support_not_earlier {Support Slope : Type}
    (data : C9ProfileData Support Slope) {gamma : Slope}
    (hgamma : gamma ∈ data.slopeCell.slopes) :
    data.earlierOwner (data.slopeCell.supportOf gamma) = none := by
  have hchosen : data.slopeCell.supportOf gamma ∈
      data.slopeCell.slopes.map data.slopeCell.supportOf :=
    List.mem_map.mpr ⟨gamma, hgamma, rfl⟩
  have hsupport : data.slopeCell.supportOf gamma ∈ data.slopeCell.supports :=
    data.slopeCell.chosen_sublist.subset hchosen
  have hresidual : data.slopeCell.supportOf gamma ∈
      residualOf data.fullPrefixFiber data.earlierOwner :=
    data.supportsInResidual.subset hsupport
  exact (mem_residualOf_iff.mp hresidual).2

/-- The exact C9 direct-payment chain: genuine `(SE2)`, residual inclusion,
full-prefix monotonicity, and the supplied full-prefix field. -/
theorem C9ProfileData.slopes_paid {Support Slope : Type}
    (data : C9ProfileData Support Slope) :
    data.slopeCell.slopes.length ≤ data.compilerLoss * data.naturalScale := by
  calc
    data.slopeCell.slopes.length ≤ data.slopeCell.supports.length :=
      se2_support_injection data.slopeCell
    _ ≤ (residualOf data.fullPrefixFiber data.earlierOwner).length :=
      data.supportsInResidual.length_le
    _ ≤ data.fullPrefixFiber.length := by
      unfold residualOf
      exact List.filter_sublist.length_le
    _ ≤ data.compilerLoss * data.naturalScale := data.rowSharpMaxFiber

/-- If the full-prefix field is charged against a remaining budget while an
owned subfamily is paid separately, the residual plus the owned floor must fit
inside that same remaining budget. -/
theorem residual_plus_ownerFloor_le_budget {Support : Type}
    (full : List Support) (earlierOwner : Support → Option PreC9Owner)
    (ownerFloor budget : Nat)
    (hOwnerFloor : ownerFloor ≤ (ownedOf full earlierOwner).length)
    (hFull : full.length ≤ budget) :
    (residualOf full earlierOwner).length + ownerFloor ≤ budget := by
  calc
    (residualOf full earlierOwner).length + ownerFloor ≤
        (residualOf full earlierOwner).length +
          (ownedOf full earlierOwner).length :=
      Nat.add_le_add_left hOwnerFloor _
    _ = full.length := residual_owned_length earlierOwner full
    _ ≤ budget := hFull

/-- Mersenne-31 base-field order used by the prefix map. -/
def qGen : Nat := 2 ^ 31 - 1

/-- Quartic list field; this denominator is separate from `qGen`. -/
def qList : Nat := qGen ^ 4

/-- Exact list-row budget `floor(qList / 2^100)`. -/
def rowBudget : Nat := qList / (2 ^ 100)

/-- Exact `c=2048` fixed-remainder floor imported from the integrated
fixed-remainder certificate.  The companion stdlib replay independently
recomputes `ceil(binomial(1023,544) / qGen^32)`. -/
def c2048OwnerFloor : Nat := 6796405

/-- Budget left after paying that earlier quotient/fixed-remainder cell. -/
def residualAllowance : Nat := rowBudget - c2048OwnerFloor

/-- Maximum residual compatible with applying the *full-prefix* field at the
remaining budget while the owner floor remains in the same prefix fiber. -/
def fullPrefixResidualCap : Nat := residualAllowance - c2048OwnerFloor

/-- First cardinality that falsifies the remaining-budget full-prefix field. -/
def falsifierResidual : Nat := fullPrefixResidualCap + 1

/-- Fail-closed exact arithmetic gate for the deployed M31 owner-refund cut. -/
def m31ArithmeticCheck : Bool :=
  qGen == 2147483647 &&
  qList == 21267647892944572736998860269687930881 &&
  rowBudget == 16777215 &&
  c2048OwnerFloor == 6796405 &&
  residualAllowance == 9980810 &&
  fullPrefixResidualCap == 3184405 &&
  falsifierResidual == 3184406 &&
  decide (3184405 + 6796405 = 9980810) &&
  decide (9980810 + 6796405 = 16777215) &&
  decide (16777215 + 6796405 = 23573620) &&
  decide (9980810 < 3184406 + 6796405)

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
/-- Kernel-checked M31 ledger arithmetic from the integrated exact owner floor.
The large binomial ceiling itself is replayed by the companion stdlib verifier. -/
theorem m31_arithmetic_check : m31ArithmeticCheck = true := by decide

/-- Exact deployed falsifier interface.  A prefix key with at least `6,796,405`
earlier-owned supports and at least `3,184,406` residual supports cannot satisfy
the full-prefix field at the remaining budget `9,980,810`. -/
theorem m31_full_bound_fails_of_falsifier {Support : Type}
    (full : List Support) (earlierOwner : Support → Option PreC9Owner)
    (hOwnerFloor : 6796405 ≤ (ownedOf full earlierOwner).length)
    (hResidual : 3184406 ≤ (residualOf full earlierOwner).length) :
    ¬ full.length ≤ 9980810 := by
  intro hFull
  have hCut :
      (residualOf full earlierOwner).length + 6796405 ≤ 9980810 :=
    residual_plus_ownerFloor_le_budget full earlierOwner 6796405 9980810
      hOwnerFloor hFull
  have hImpossible : 3184406 + 6796405 ≤ 9980810 :=
    Nat.le_trans (Nat.add_le_add_right hResidual 6796405) hCut
  exact (by decide : ¬ (3184406 + 6796405 ≤ 9980810)) hImpossible

/-! A small executable regression for exact owner complement plus genuine SE2. -/

def toyFull : List Nat := List.range 8

def toyOwner (x : Nat) : Option PreC9Owner :=
  if x < 3 then some .c1 else none

/-- Three distinct slopes choose three distinct residual supports. -/
def toySE2 : SE2Certificate Nat Nat where
  supports := [3, 4, 5]
  slopes := [101, 102, 103]
  supportOf := fun gamma => gamma - 98
  supports_nodup := by decide
  slopes_nodup := by decide
  chosen_sublist := by decide

/-- The toy profile has the exact same full-prefix field shape as C9. -/
def toyProfile : C9ProfileData Nat Nat where
  fullPrefixFiber := toyFull
  earlierOwner := toyOwner
  slopeCell := toySE2
  supportsInResidual := by decide
  compilerLoss := 8
  naturalScale := 1
  rowSharpMaxFiber := by decide

/-- Executable regression: owner complement and slope payment both compute. -/
def toyCheck : Bool :=
  residualOf toyFull toyOwner == [3, 4, 5, 6, 7] &&
  ownedOf toyFull toyOwner == [0, 1, 2] &&
  toyProfile.slopeCell.slopes.length == 3 &&
  decide (toyProfile.slopeCell.slopes.length ≤
    toyProfile.compilerLoss * toyProfile.naturalScale)

/-- Kernel-checked toy owner-complement/SE2 regression. -/
theorem toy_check : toyCheck = true := by decide

#print axioms mem_residualOf_iff
#print axioms residual_owned_length
#print axioms se2_support_injection
#print axioms C9ProfileData.support_not_earlier
#print axioms C9ProfileData.slopes_paid
#print axioms residual_plus_ownerFloor_le_budget
#print axioms m31_arithmetic_check
#print axioms m31_full_bound_fails_of_falsifier
#print axioms toy_check

end SidonEffectiveImage
