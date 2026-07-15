import GrandeFinale.DirectionDistanceAllPairs

/-!
# Positive-depth cyclotomic LineRay curve

This module contains **UNPROVED STATEMENT TARGETS**.  It records the exact
numerical and realized-puncture interfaces of the cyclotomic rational-normal
curve construction.  It does not claim a Lean proof.
-/

open scoped Classical

noncomputable section

namespace GrandeFinale
namespace PositiveDepthCyclotomicLineRayCurve

open DirectionDistanceAllPairs

set_option autoImplicit false

universe u v

variable {D : Type u} {F : Type v}
variable [Fintype D] [DecidableEq D]
variable [Field F] [DecidableEq F]

abbrev Pair (D : Type u) (F : Type v) := SlopeErrorPair D F

def cyclotomicDepth (t : ℕ) : ℕ :=
  t - 1

def imageNormalizedScale (mass imageSize : ℕ) : ℕ :=
  mass / imageSize

def exactQDenominator (N t : ℕ) : ℤ :=
  (t : ℤ) ^ 2 -
    ((t - 1 : ℕ) : ℤ) * ((N - t - 1 : ℕ) : ℤ)

def CyclotomicPairConclusion
    (P : Finset (Pair D F)) (prefixTarget : Pair D F → F) : Prop :=
  P.card = Fintype.card D ∧
    Set.InjOn (fun p : Pair D F => p.1) (↑P : Set (Pair D F)) ∧
    Set.InjOn prefixTarget (↑P : Set (Pair D F)) ∧
    (∀ p ∈ P, prefixTarget p = p.1) ∧
    imageNormalizedScale P.card P.card = 1

def CyclotomicWeightedConclusion
    (P : Finset (Pair D F)) (v : D → F) (t : ℕ) : Prop :=
  weight v = t + 1 ∧
    (realizedWords P v).card = Fintype.card D - t ∧
    weightedPunctureBudget P v t = P.card

/--
**UNPROVED STATEMENT TARGET (positive-depth profile separation).**

The cyclotomic family has one pair, one slope, and one realized prefix target
per domain point, while its image-normalized profile scale is one.
-/
def positiveDepthProfileSeparationTarget
    (P : Finset (Pair D F)) (prefixTarget : Pair D F → F)
    (t : ℕ) : Prop :=
  2 ≤ t →
    CyclotomicPairConclusion P prefixTarget →
    cyclotomicDepth t = t - 1 ∧
      P.card = Fintype.card D

/--
**UNPROVED STATEMENT TARGET (sharp selector-free weighted puncture).**
-/
def cyclotomicWeightedPunctureSharpTarget
    (P : Finset (Pair D F)) (v : D → F) (t : ℕ) : Prop :=
  CyclotomicWeightedConclusion P v t →
    P.card = weightedPunctureBudget P v t

/--
**UNPROVED STATEMENT TARGET (sharp rational-normal-curve arithmetic).**

`curveDegree = movingRoots = t` makes the curve compiler return the exact
domain cardinality.
-/
def rationalNormalCurvePaymentTarget
    (N t curveDegree movingRoots rayCount : ℕ) : Prop :=
  0 < t →
    curveDegree = t →
    movingRoots = t →
    rayCount = N →
    rayCount * movingRoots = N * curveDegree

/--
**UNPROVED STATEMENT TARGET (double-negative exact stratum).**
-/
def exactResidualDoubleNegativeTarget (N t : ℕ) : Prop :=
  N * (t - 1) > 2 * t ^ 2 - 1 →
    exactQDenominator N t < 0

end PositiveDepthCyclotomicLineRayCurve
end GrandeFinale
