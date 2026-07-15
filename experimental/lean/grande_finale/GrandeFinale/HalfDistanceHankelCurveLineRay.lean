import GrandeFinale.DirectionDistanceAllPairs

/-!
# Half-distance Hankel curve LineRay compiler

This module contains **UNPROVED STATEMENT TARGETS**.  It records the exact
weight-stratified, all-pair, and MCA-numerator interfaces of the
half-distance cofactor construction.  It does not claim a Lean proof.
-/

open scoped Classical

noncomputable section

namespace GrandeFinale
namespace HalfDistanceHankelCurveLineRay

open DirectionDistanceAllPairs

set_option autoImplicit false

universe u v

variable {D : Type u} {F : Type v}
variable [Fintype D] [DecidableEq D]
variable [Field F] [DecidableEq F]

abbrev Pair (D : Type u) (F : Type v) := SlopeErrorPair D F

def halfDistancePairBound (N t : ℕ) : ℕ :=
  1 + N * t * (t + 1) / 2

def HalfDistancePairConclusion
    (P : Finset (Pair D F)) (N t : ℕ) : Prop :=
  Set.InjOn (fun p : Pair D F => p.1) (↑P : Set (Pair D F)) ∧
    P.card ≤ halfDistancePairBound N t ∧
    ∀ s, 1 ≤ s → s ≤ t →
      (P.filter fun p => weight p.2 = s).card ≤ N * s

/--
**UNPROVED STATEMENT TARGET (half-distance all-pair compiler).**
-/
def halfDistanceAllPairTarget
    (P : Finset (Pair D F)) (N R t : ℕ) : Prop :=
  1 ≤ t →
    2 * t ≤ R →
    R ≤ N →
    HalfDistancePairConclusion P N t

/--
**UNPROVED STATEMENT TARGET (one exact-weight cofactor curve).**
-/
def exactWeightCurveTarget
    (N s g delta pairCount : ℕ) : Prop :=
  1 ≤ s →
    g < s →
    delta ≤ s →
    pairCount * (s - g) ≤ (N - g) * delta →
    pairCount ≤ N * s

/--
**UNPROVED STATEMENT TARGET (MCA/CA numerator interface).**
-/
def halfDistanceNumeratorTarget
    (mcaNumerator caNumerator N R t : ℕ) : Prop :=
  2 * t ≤ R →
    R ≤ N →
    mcaNumerator ≤ halfDistancePairBound N t ∧
      caNumerator ≤ halfDistancePairBound N t

end HalfDistanceHankelCurveLineRay
end GrandeFinale
