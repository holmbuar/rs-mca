import GrandeFinale.DirectionDistanceAllPairs

/-!
# Complete absorption at the first beyond-half slice

This module contains **UNPROVED STATEMENT TARGETS**.  It records the sharp
complete all-pair and MCA/CA numerator interfaces at `R+1=2t`.  It does not
claim a Lean proof.
-/

open scoped Classical

noncomputable section

namespace GrandeFinale
namespace FirstBeyondHalfCompleteAbsorption

open DirectionDistanceAllPairs

set_option autoImplicit false

universe u v

variable {D : Type u} {F : Type v}
variable [Fintype D] [DecidableEq D]
variable [Field F] [DecidableEq F]

abbrev Pair (D : Type u) (F : Type v) := SlopeErrorPair D F

def completeAbsorptionBound (N : ℕ) : ℕ :=
  Nat.choose N 2

/--
**UNPROVED STATEMENT TARGET (complete first beyond-half all-pair compiler).**
-/
def completeAllPairTarget
    (P : Finset (Pair D F)) (N R t : ℕ) : Prop :=
  2 ≤ t →
    R + 1 = 2 * t →
    R ≤ N →
    P.card ≤ completeAbsorptionBound N

/--
**UNPROVED STATEMENT TARGET (MCA/CA numerator interface).**
-/
def completeNumeratorTarget
    (mcaNumerator caNumerator N R t : ℕ) : Prop :=
  2 ≤ t →
    R + 1 = 2 * t →
    R ≤ N →
    mcaNumerator ≤ completeAbsorptionBound N ∧
      caNumerator ≤ completeAbsorptionBound N

/--
**UNPROVED STATEMENT TARGET (the pinned equality fixtures).**
-/
def completeSharpnessTarget
    (N completePairCount : ℕ) : Prop :=
  completePairCount = Nat.choose N 2

end FirstBeyondHalfCompleteAbsorption
end GrandeFinale
