import Std

/-!
# KoalaBear active-v4 source-coordinate tangent owner

This stdlib-only module formalizes the finite-list and first-owner kernels of
the K1 gate-(B) packet. The semantic source theorem that one fixed sparse
translation preserves the complete MCA-bad slope set is already formalized in
`RsMcaThresholds.ExactSparsification`; this module adds no assumption and does
not import that package's non-stdlib dependency graph.

A duplicate-bearing coordinate image is enough for an upper bound on the
number of distinct slopes: every paid slope occurs in the list, while list
length counts source coordinates with multiplicity.
-/

set_option autoImplicit false

namespace KbM1SourceBoundBridge

def basePrime : Nat := 2130706433
def extensionDegree : Nat := 6
def domainSize : Nat := 2097152
def codeDimension : Nat := 1048576
def agreement : Nat := 1116048
def tangentCharge : Nat := 981104
def budget : Nat := 274980728111395087
def remainingBudget : Nat := 274980728110413983
def legacyM1Paid : Nat := 422354730332

/--
Eligible source coordinates for one fixed received line after the canonical
sparse translation. `slopeAt` is the source-coordinate ratio. Repetitions in
the mapped list are retained, so its length is automatically an upper bound on
the number of distinct image slopes.
-/
structure TangentSourceData (D F : Type) where
  eligible : List D
  slopeAt : D → F
  eligible_card_le : eligible.length ≤ tangentCharge

def tangentImageEnvelope {D F : Type}
    (data : TangentSourceData D F) : List F :=
  data.eligible.map data.slopeAt

def paidEnvelope {D F : Type}
    (bad : F → Bool) (data : TangentSourceData D F) : List F :=
  (tangentImageEnvelope data).filter bad

/-- Mapping source coordinates does not change the duplicate-bearing list
length. -/
theorem tangentImageEnvelope_length_eq {D F : Type}
    (data : TangentSourceData D F) :
    (tangentImageEnvelope data).length = data.eligible.length := by
  simp [tangentImageEnvelope]

/-- Every entry of the source-coordinate image comes from an eligible source
coordinate. -/
theorem mem_tangentImageEnvelope_iff {D F : Type}
    (data : TangentSourceData D F) (γ : F) :
    γ ∈ tangentImageEnvelope data ↔
      ∃ x, x ∈ data.eligible ∧ data.slopeAt x = γ := by
  simp [tangentImageEnvelope]

/-- Filtering the source-coordinate image by the bad-slope predicate leaves at
most `981104` entries, hence at most that many distinct paid slopes. -/
theorem paidEnvelope_length_le_tangentCharge {D F : Type}
    (bad : F → Bool) (data : TangentSourceData D F) :
    (paidEnvelope bad data).length ≤ tangentCharge := by
  calc
    (paidEnvelope bad data).length
        ≤ (tangentImageEnvelope data).length := by
          simpa [paidEnvelope] using
            (List.length_filter_le bad (tangentImageEnvelope data))
    _ = data.eligible.length := tangentImageEnvelope_length_eq data
    _ ≤ tangentCharge := data.eligible_card_le

/-- The four active cells plus the outside case. -/
inductive Owner where
  | paid
  | q
  | bc
  | new
  | outside
  deriving DecidableEq, Repr

/-- Public, non-oracular first-match chronology. On the deployed packet,
`tangent` is exact membership in the canonical source-coordinate image, while
`qCertified` and `bcCertified` are the active-v4 certificate predicates. -/
def firstOwner {F : Type}
    (bad tangent qCertified bcCertified : F → Bool) (γ : F) : Owner :=
  if bad γ then
    if tangent γ then .paid
    else if qCertified γ then .q
    else if bcCertified γ then .bc
    else .new
  else .outside

/-- Every slope receives exactly one constructor-valued owner. -/
theorem firstOwner_cases {F : Type}
    (bad tangent qCertified bcCertified : F → Bool) (γ : F) :
    firstOwner bad tangent qCertified bcCertified γ = .paid ∨
    firstOwner bad tangent qCertified bcCertified γ = .q ∨
    firstOwner bad tangent qCertified bcCertified γ = .bc ∨
    firstOwner bad tangent qCertified bcCertified γ = .new ∨
    firstOwner bad tangent qCertified bcCertified γ = .outside := by
  cases hbad : bad γ <;>
  cases htan : tangent γ <;>
  cases hq : qCertified γ <;>
  cases hbc : bcCertified γ <;>
  simp [firstOwner, hbad, htan, hq, hbc]

/-- A bad slope is exhaustively assigned to one of the four active cells. -/
theorem activeOwner_cases_of_bad {F : Type}
    (bad tangent qCertified bcCertified : F → Bool) (γ : F)
    (hbad : bad γ = true) :
    firstOwner bad tangent qCertified bcCertified γ = .paid ∨
    firstOwner bad tangent qCertified bcCertified γ = .q ∨
    firstOwner bad tangent qCertified bcCertified γ = .bc ∨
    firstOwner bad tangent qCertified bcCertified γ = .new := by
  cases htan : tangent γ <;>
  cases hq : qCertified γ <;>
  cases hbc : bcCertified γ <;>
  simp [firstOwner, hbad, htan, hq, hbc]

/-- The constructor-valued first owner is unique. -/
theorem firstOwner_unique {F : Type}
    (bad tangent qCertified bcCertified : F → Bool) (γ : F)
    (o₁ o₂ : Owner)
    (h₁ : firstOwner bad tangent qCertified bcCertified γ = o₁)
    (h₂ : firstOwner bad tangent qCertified bcCertified γ = o₂) :
    o₁ = o₂ := by
  exact h₁.symm.trans h₂

/-- No slope can belong to two different active cells. -/
theorem activeOwners_pairwiseDisjoint {F : Type}
    (bad tangent qCertified bcCertified : F → Bool) (γ : F) :
    ¬ (firstOwner bad tangent qCertified bcCertified γ = .paid ∧
       firstOwner bad tangent qCertified bcCertified γ = .q) ∧
    ¬ (firstOwner bad tangent qCertified bcCertified γ = .paid ∧
       firstOwner bad tangent qCertified bcCertified γ = .bc) ∧
    ¬ (firstOwner bad tangent qCertified bcCertified γ = .paid ∧
       firstOwner bad tangent qCertified bcCertified γ = .new) ∧
    ¬ (firstOwner bad tangent qCertified bcCertified γ = .q ∧
       firstOwner bad tangent qCertified bcCertified γ = .bc) ∧
    ¬ (firstOwner bad tangent qCertified bcCertified γ = .q ∧
       firstOwner bad tangent qCertified bcCertified γ = .new) ∧
    ¬ (firstOwner bad tangent qCertified bcCertified γ = .bc ∧
       firstOwner bad tangent qCertified bcCertified γ = .new) := by
  have differentOwners (o₁ o₂ : Owner) (hne : o₁ ≠ o₂) :
      ¬ (firstOwner bad tangent qCertified bcCertified γ = o₁ ∧
         firstOwner bad tangent qCertified bcCertified γ = o₂) := by
    rintro ⟨h₁, h₂⟩
    exact hne (h₁.symm.trans h₂)
  exact ⟨
    differentOwners .paid .q (by decide),
    differentOwners .paid .bc (by decide),
    differentOwners .paid .new (by decide),
    differentOwners .q .bc (by decide),
    differentOwners .q .new (by decide),
    differentOwners .bc .new (by decide)⟩

/-- Compatibility name for the source-coordinate image upper: the duplicate-
bearing image list has length at most the eligible source-coordinate list. -/
theorem tangentImage_card_le_support {D F : Type}
    (data : TangentSourceData D F) :
    (tangentImageEnvelope data).length ≤ data.eligible.length := by
  simp [tangentImageEnvelope]

/-- Compatibility name for the active paid-cell upper. -/
theorem paidCell_card_le_tangentCharge {D F : Type}
    (bad : F → Bool) (data : TangentSourceData D F) :
    (paidEnvelope bad data).length ≤ tangentCharge :=
  paidEnvelope_length_le_tangentCharge bad data

/-- Compatibility name for pairwise first-match exclusion. -/
theorem activeCells_pairwiseDisjoint {F : Type}
    (bad tangent qCertified bcCertified : F → Bool) (γ : F) :
    ¬ (firstOwner bad tangent qCertified bcCertified γ = .paid ∧
       firstOwner bad tangent qCertified bcCertified γ = .q) ∧
    ¬ (firstOwner bad tangent qCertified bcCertified γ = .paid ∧
       firstOwner bad tangent qCertified bcCertified γ = .bc) ∧
    ¬ (firstOwner bad tangent qCertified bcCertified γ = .paid ∧
       firstOwner bad tangent qCertified bcCertified γ = .new) ∧
    ¬ (firstOwner bad tangent qCertified bcCertified γ = .q ∧
       firstOwner bad tangent qCertified bcCertified γ = .bc) ∧
    ¬ (firstOwner bad tangent qCertified bcCertified γ = .q ∧
       firstOwner bad tangent qCertified bcCertified γ = .new) ∧
    ¬ (firstOwner bad tangent qCertified bcCertified γ = .bc ∧
       firstOwner bad tangent qCertified bcCertified γ = .new) :=
  activeOwners_pairwiseDisjoint bad tangent qCertified bcCertified γ

/-- Compatibility name for exact four-cell exhaustion on a bad slope. -/
theorem activeCells_union {F : Type}
    (bad tangent qCertified bcCertified : F → Bool) (γ : F)
    (hbad : bad γ = true) :
    firstOwner bad tangent qCertified bcCertified γ = .paid ∨
    firstOwner bad tangent qCertified bcCertified γ = .q ∨
    firstOwner bad tangent qCertified bcCertified γ = .bc ∨
    firstOwner bad tangent qCertified bcCertified γ = .new :=
  activeOwner_cases_of_bad bad tangent qCertified bcCertified γ hbad

/-- Exact deployed row arithmetic and the positive gate-(B) payment. -/
theorem deployedConstantsExact :
    domainSize - agreement = tangentCharge ∧
    codeDimension < agreement ∧
    0 < tangentCharge ∧
    tangentCharge < budget ∧
    budget - tangentCharge = remainingBudget := by
  decide

/-- The re-proof banks only the tangent charge, not the legacy M1 stack. -/
theorem activePaymentIsStrictlySmallerThanLegacy :
    tangentCharge < legacyM1Paid := by
  decide

#print axioms tangentImageEnvelope_length_eq
#print axioms mem_tangentImageEnvelope_iff
#print axioms paidEnvelope_length_le_tangentCharge
#print axioms firstOwner_cases
#print axioms activeOwner_cases_of_bad
#print axioms firstOwner_unique
#print axioms activeOwners_pairwiseDisjoint
#print axioms tangentImage_card_le_support
#print axioms paidCell_card_le_tangentCharge
#print axioms activeCells_pairwiseDisjoint
#print axioms activeCells_union
#print axioms deployedConstantsExact
#print axioms activePaymentIsStrictlySmallerThanLegacy

end KbM1SourceBoundBridge
