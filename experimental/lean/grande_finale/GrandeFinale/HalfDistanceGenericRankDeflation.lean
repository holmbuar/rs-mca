import GrandeFinale.DirectionDistanceAllPairs

/-!
# Generic-rank deflation for half-distance LineRays

This module contains **UNPROVED STATEMENT TARGETS**.  It records the
generic-rank, lower-weight root charge, deflated top-weight charge, and
MCA/CA numerator interfaces.  It does not claim a Lean proof.
-/

open scoped Classical

noncomputable section

namespace GrandeFinale
namespace HalfDistanceGenericRankDeflation

open DirectionDistanceAllPairs

set_option autoImplicit false

universe u v

variable {D : Type u} {F : Type v}
variable [Fintype D] [DecidableEq D]
variable [Field F] [DecidableEq F]

abbrev Pair (D : Type u) (F : Type v) := SlopeErrorPair D F

def genericRankBound (N rho : ℕ) : ℕ :=
  N + rho

def GenericRankPairConclusion
    (P : Finset (Pair D F)) (N t rho : ℕ) : Prop :=
  rho ≤ t ∧
    Set.InjOn (fun p : Pair D F => p.1) (↑P : Set (Pair D F)) ∧
    P.card ≤ genericRankBound N rho

/--
**UNPROVED STATEMENT TARGET (generic-rank all-pair compiler).**
-/
def genericRankAllPairTarget
    (P : Finset (Pair D F)) (N R t rho : ℕ) : Prop :=
  1 ≤ t →
    2 * t ≤ R →
    R ≤ N →
    GenericRankPairConclusion P N t rho

/--
**UNPROVED STATEMENT TARGET (one minor pays every lower weight).**
-/
def lowerWeightMinorTarget
    (lowerPairCount rho minorDegree : ℕ) : Prop :=
  minorDegree ≤ rho →
    lowerPairCount ≤ minorDegree →
    lowerPairCount ≤ rho

/--
**UNPROVED STATEMENT TARGET (fixed-root deflated top chart).**
-/
def deflatedExactWeightTarget
    (N rho g residualDegree topPairCount : ℕ) : Prop :=
  1 ≤ rho →
    2 * rho ≤ N →
    g ≤ rho →
    ((g = rho ∧ topPairCount ≤ 1) ∨
      (g < rho ∧
        residualDegree ≤ rho - g ∧
        topPairCount * (rho - g) ≤ (N - g) * residualDegree)) →
    topPairCount ≤ N - g

/--
**UNPROVED STATEMENT TARGET (MCA/CA numerator interface).**
-/
def genericRankNumeratorTarget
    (mcaNumerator caNumerator N R t rho : ℕ) : Prop :=
  2 * t ≤ R →
    R ≤ N →
    rho ≤ t →
    mcaNumerator ≤ genericRankBound N rho ∧
      caNumerator ≤ genericRankBound N rho

end HalfDistanceGenericRankDeflation
end GrandeFinale
