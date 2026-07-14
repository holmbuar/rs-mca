import GrandeFinale.DirectionDistanceAllPairs

/-!
# Quadratic completion at third recurrence depth

This module contains UNPROVED STATEMENT TARGETS.  It records finite interfaces
for the depth-three asymptotic sharpness theorem and does not claim a Lean
proof.
-/

open scoped Classical

noncomputable section

namespace GrandeFinale
namespace ThirdRecurrenceQuadraticCompletion

set_option autoImplicit false

/-- UNPROVED STATEMENT TARGET: depth-three parameter identities. -/
def parameterTarget (R t d : ℕ) : Prop :=
  4 ≤ t →
  R = t + 3 →
  d = t - 3 →
  R + d = 2 * t

/-- UNPROVED STATEMENT TARGET: quadratic-completion partition count. -/
def completionMultiplicityTarget
    (validCompletions pairCount t : ℕ) : Prop :=
  validCompletions = Nat.choose t 2 * pairCount

/-- UNPROVED STATEMENT TARGET: complete transverse pair interface. -/
def completePairTarget
    (pairCount lowerWeightCount q t : ℕ) : Prop :=
  4 ≤ t →
  t ≤ q →
  lowerWeightCount = 0 ∧ pairCount ≤ Nat.choose q (t - 2)

/--
UNPROVED STATEMENT TARGET: a finite form of the fixed-t asymptotic estimate.
-/
def asymptoticErrorTarget
    (pairCount q t errorConstant : ℕ) : Prop :=
  4 ≤ t →
  pairCount * Nat.factorial t ≤
      q ^ (t - 2) + errorConstant * q ^ (t - 3) ∧
    q ^ (t - 2) ≤
      pairCount * Nat.factorial t + errorConstant * q ^ (t - 3)

end ThirdRecurrenceQuadraticCompletion
end GrandeFinale
