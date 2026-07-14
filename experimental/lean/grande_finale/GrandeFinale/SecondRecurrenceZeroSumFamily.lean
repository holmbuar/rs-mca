import GrandeFinale.DirectionDistanceAllPairs

/-!
# Exact zero-sum family at second recurrence depth

This module contains UNPROVED STATEMENT TARGETS.  It records finite count and
sharpness interfaces for the second-recurrence zero-sum line.  It does not
claim a Lean proof.
-/

open scoped Classical

noncomputable section

namespace GrandeFinale
namespace SecondRecurrenceZeroSumFamily

set_option autoImplicit false

/-- UNPROVED STATEMENT TARGET: exact zero-sum support count. -/
def exactPairCountTarget (q t pairCount : ℕ) : Prop :=
  3 ≤ t →
  t ≤ q →
  q * pairCount = Nat.choose q t

/-- UNPROVED STATEMENT TARGET: second-recurrence parameter identities. -/
def parameterTarget (R t d : ℕ) : Prop :=
  3 ≤ t →
  R = t + 2 →
  d = t - 2 →
  R + d = 2 * t

/--
UNPROVED STATEMENT TARGET: cross-multiplied complete-pair sharpness ratio.
-/
def exactRatioTarget (q t pairCount : ℕ) : Prop :=
  3 ≤ t →
  t ≤ q →
  q * t * pairCount = (q - t + 1) * Nat.choose q (t - 1)

/-- UNPROVED STATEMENT TARGET: complete and transverse family interface. -/
def completeTransverseFamilyTarget
    (pairCount lowerWeightCount q t : ℕ) : Prop :=
  3 ≤ t →
  t ≤ q →
  lowerWeightCount = 0 ∧
    q * pairCount = Nat.choose q t ∧
    pairCount ≤ Nat.choose q (t - 1)

end SecondRecurrenceZeroSumFamily
end GrandeFinale
