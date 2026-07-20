import GrandeFinale.FirstMatchAddBack

/-!
# Conditional base-pole C7 numeric adapter

This module is an active-track finite adapter for the constant-coefficient
base-pole partition.  It deliberately begins after a separate source theorem
has supplied a duplicate-free raw distinct-slope list and its `q - 1` census.
It does not construct a finite field, an evaluation domain, Reed--Solomon
witnesses, support locators, a pole line, or the coefficient-to-slope law.

The C7 name is provenance metadata only.  No semantic owner, least-owner rule,
first-match atlas coverage theorem, line-list completeness theorem, row-wide
uniform estimate, target comparison, or row closure is manufactured here.

What is proved is finite list arithmetic at the active Grande Finale boundary:

* literal deletion of an earlier assigned-slope image;
* preservation of duplicate-free assigned slopes;
* unit direct distinct-slope payments for the survivors;
* loss lifting that preserves every local budget and weakens only the allowed
  global compiler loss;
* exact line-local budget and natural-scale telescopes; and
* regressions showing both double charging and atlas-order noncanonicity.

The outer supremum over received lines, when available, must be taken only after
these line-local profile sums.  This module never interchanges that order.
-/

namespace GrandeFinale.BasePoleC7NumericAdapter

open GrandeFinale.ExactProfileCompiler

/-! ## Numeric profile payments -/

/-- A purely numeric profile-payment interface.  The fields are explicit inputs;
none of them asserts semantic ownership or source-side witness coverage. -/
structure ProfilePayment (compilerLoss : Nat) where
  assignedSlopes : List Nat
  assignedSlopes_nodup : assignedSlopes.Nodup
  naturalScale : Nat
  residualBudget : Nat
  sidonBudget : Nat
  rayBudget : Nat
  residualLoss : Nat
  sidonLoss : Nat
  rayLoss : Nat
  residualToFull : residualBudget ≤ residualLoss * naturalScale
  imageNormalizedSidon : sidonBudget ≤ sidonLoss * residualBudget
  rayCompiler : rayBudget ≤ rayLoss * sidonBudget
  distinctSlopePayment : assignedSlopes.length ≤ rayBudget
  compilerLossDominates : rayLoss * sidonLoss * residualLoss ≤ compilerLoss

namespace ProfilePayment

/-- The explicit local inequalities telescope to payment at the allowed natural
scale. -/
theorem paidAtNaturalScale {compilerLoss : Nat}
    (profile : ProfilePayment compilerLoss) :
    profile.rayBudget ≤ compilerLoss * profile.naturalScale := by
  calc
    profile.rayBudget ≤ profile.rayLoss * profile.sidonBudget :=
      profile.rayCompiler
    _ ≤ profile.rayLoss * (profile.sidonLoss * profile.residualBudget) :=
      Nat.mul_le_mul_left profile.rayLoss profile.imageNormalizedSidon
    _ ≤ profile.rayLoss *
        (profile.sidonLoss * (profile.residualLoss * profile.naturalScale)) :=
      Nat.mul_le_mul_left profile.rayLoss
        (Nat.mul_le_mul_left profile.sidonLoss profile.residualToFull)
    _ = (profile.rayLoss * profile.sidonLoss * profile.residualLoss) *
        profile.naturalScale := by
      simp only [Nat.mul_assoc]
    _ ≤ compilerLoss * profile.naturalScale :=
      Nat.mul_le_mul_right profile.naturalScale profile.compilerLossDominates

/-- Direct distinct-slope payment.  This bypasses residual-moment and Sidon
routes rather than pretending that either route was proved. -/
def ofDirect (assignedSlopes : List Nat) (naturalScale compilerLoss : Nat)
    (hNodup : assignedSlopes.Nodup)
    (hPaid : assignedSlopes.length ≤ compilerLoss * naturalScale) :
    ProfilePayment compilerLoss where
  assignedSlopes := assignedSlopes
  assignedSlopes_nodup := hNodup
  naturalScale := naturalScale
  residualBudget := compilerLoss * naturalScale
  sidonBudget := compilerLoss * naturalScale
  rayBudget := compilerLoss * naturalScale
  residualLoss := compilerLoss
  sidonLoss := 1
  rayLoss := 1
  residualToFull := Nat.le_refl _
  imageNormalizedSidon := by simp
  rayCompiler := by simp
  distinctSlopePayment := hPaid
  compilerLossDominates := by simp

/-- Lift a profile from a smaller allowed compiler loss to a larger one.  All
assigned slopes, local scales, local budgets, and local inequalities are
preserved definitionally; only `compilerLossDominates` is weakened. -/
def liftLoss {small large : Nat} (profile : ProfilePayment small)
    (h : small ≤ large) : ProfilePayment large where
  assignedSlopes := profile.assignedSlopes
  assignedSlopes_nodup := profile.assignedSlopes_nodup
  naturalScale := profile.naturalScale
  residualBudget := profile.residualBudget
  sidonBudget := profile.sidonBudget
  rayBudget := profile.rayBudget
  residualLoss := profile.residualLoss
  sidonLoss := profile.sidonLoss
  rayLoss := profile.rayLoss
  residualToFull := profile.residualToFull
  imageNormalizedSidon := profile.imageNormalizedSidon
  rayCompiler := profile.rayCompiler
  distinctSlopePayment := profile.distinctSlopePayment
  compilerLossDominates := profile.compilerLossDominates.trans h

@[simp] theorem liftLoss_assignedSlopes {small large : Nat}
    (profile : ProfilePayment small) (h : small ≤ large) :
    (profile.liftLoss h).assignedSlopes = profile.assignedSlopes := rfl

@[simp] theorem liftLoss_naturalScale {small large : Nat}
    (profile : ProfilePayment small) (h : small ≤ large) :
    (profile.liftLoss h).naturalScale = profile.naturalScale := rfl

@[simp] theorem liftLoss_residualBudget {small large : Nat}
    (profile : ProfilePayment small) (h : small ≤ large) :
    (profile.liftLoss h).residualBudget = profile.residualBudget := rfl

@[simp] theorem liftLoss_sidonBudget {small large : Nat}
    (profile : ProfilePayment small) (h : small ≤ large) :
    (profile.liftLoss h).sidonBudget = profile.sidonBudget := rfl

@[simp] theorem liftLoss_rayBudget {small large : Nat}
    (profile : ProfilePayment small) (h : small ≤ large) :
    (profile.liftLoss h).rayBudget = profile.rayBudget := rfl

/-- Active-track adapter: one numeric direct profile becomes the direct branch
of `ExactProfileCompiler.PrimitiveCellBudget`.  The C7 label is not used as a
semantic theorem. -/
def toPrimitiveCellBudget {compilerLoss : Nat}
    (profile : ProfilePayment compilerLoss) : PrimitiveCellBudget where
  actual := profile.assignedSlopes.length
  moment := none
  direct := some profile.rayBudget
  available := by simp
  momentSound := by
    intro u h
    simp at h
  directSound := by
    intro d h
    simp only [Option.some.injEq] at h
    subst d
    exact profile.distinctSlopePayment

@[simp] theorem toPrimitiveCellBudget_actual {compilerLoss : Nat}
    (profile : ProfilePayment compilerLoss) :
    profile.toPrimitiveCellBudget.actual = profile.assignedSlopes.length := rfl

@[simp] theorem toPrimitiveCellBudget_merged {compilerLoss : Nat}
    (profile : ProfilePayment compilerLoss) :
    mergedBudget profile.toPrimitiveCellBudget.moment
      profile.toPrimitiveCellBudget.direct = profile.rayBudget := rfl

end ProfilePayment

/-! ## Line-local numeric sums -/

/-- Flattened assigned-slope image of a supplied profile list.  This is numeric
data, not a proof that the list covers all bad slopes on a received line. -/
def assignedSlopeImage {compilerLoss : Nat}
    (profiles : List (ProfilePayment compilerLoss)) : List Nat :=
  (profiles.map (fun profile => profile.assignedSlopes)).flatten

/-- Sum of direct distinct-slope budgets inside one received line. -/
def budgetTotal {compilerLoss : Nat}
    (profiles : List (ProfilePayment compilerLoss)) : Nat :=
  (profiles.map (fun profile => profile.rayBudget)).sum

/-- Sum of natural profile scales inside one received line. -/
def naturalTotal {compilerLoss : Nat}
    (profiles : List (ProfilePayment compilerLoss)) : Nat :=
  (profiles.map (fun profile => profile.naturalScale)).sum

@[simp] theorem assignedSlopeImage_append {compilerLoss : Nat}
    (left right : List (ProfilePayment compilerLoss)) :
    assignedSlopeImage (left ++ right) =
      assignedSlopeImage left ++ assignedSlopeImage right := by
  simp [assignedSlopeImage]

@[simp] theorem budgetTotal_append {compilerLoss : Nat}
    (left right : List (ProfilePayment compilerLoss)) :
    budgetTotal (left ++ right) = budgetTotal left + budgetTotal right := by
  simp [budgetTotal]

@[simp] theorem naturalTotal_append {compilerLoss : Nat}
    (left right : List (ProfilePayment compilerLoss)) :
    naturalTotal (left ++ right) = naturalTotal left + naturalTotal right := by
  simp [naturalTotal]

/-- Duplicate-free assigned slopes are bounded by the sum of local ray budgets. -/
theorem assignedSlopeImage_length_le_budgetTotal {compilerLoss : Nat} :
    ∀ profiles : List (ProfilePayment compilerLoss),
      (assignedSlopeImage profiles).length ≤ budgetTotal profiles
  | [] => by simp [assignedSlopeImage, budgetTotal]
  | profile :: profiles => by
      change profile.assignedSlopes.length +
          (assignedSlopeImage profiles).length ≤
        profile.rayBudget + budgetTotal profiles
      exact Nat.add_le_add profile.distinctSlopePayment
        (assignedSlopeImage_length_le_budgetTotal profiles)

/-- Local profile payments sum before any outer supremum over received lines. -/
theorem budgetTotal_le_loss_mul_naturalTotal {compilerLoss : Nat} :
    ∀ profiles : List (ProfilePayment compilerLoss),
      budgetTotal profiles ≤ compilerLoss * naturalTotal profiles
  | [] => by simp [budgetTotal, naturalTotal]
  | profile :: profiles => by
      change profile.rayBudget + budgetTotal profiles ≤
        compilerLoss * (profile.naturalScale + naturalTotal profiles)
      rw [Nat.mul_add]
      exact Nat.add_le_add profile.paidAtNaturalScale
        (budgetTotal_le_loss_mul_naturalTotal profiles)

/-- Numeric line-local compiler; no completeness or outer-line theorem is
included. -/
theorem assignedSlopeImage_length_le_loss_mul_naturalTotal
    {compilerLoss : Nat} (profiles : List (ProfilePayment compilerLoss)) :
    (assignedSlopeImage profiles).length ≤
      compilerLoss * naturalTotal profiles :=
  (assignedSlopeImage_length_le_budgetTotal profiles).trans
    (budgetTotal_le_loss_mul_naturalTotal profiles)

end GrandeFinale.BasePoleC7NumericAdapter
