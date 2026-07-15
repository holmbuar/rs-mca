import GrandeFinale.DirectionDistanceAllPairs

/-!
# First beyond-half-distance kernel-pencil compiler

This module contains **UNPROVED STATEMENT TARGETS**.  It records the
two-dimensional kernel-pencil top-stratum, complete all-pair, and MCA/CA
numerator interfaces at `R+1=2t`.  It does not claim a Lean proof.
-/

open scoped Classical

noncomputable section

namespace GrandeFinale
namespace FirstBeyondHalfKernelPencil

open DirectionDistanceAllPairs

set_option autoImplicit false

universe u v

variable {D : Type u} {F : Type v}
variable [Fintype D] [DecidableEq D]
variable [Field F] [DecidableEq F]

abbrev Pair (D : Type u) (F : Type v) := SlopeErrorPair D F

def firstBeyondHalfPairBound (N t : ℕ) : ℕ :=
  Nat.choose N 2 + N + t - 1

def FirstBeyondHalfPairConclusion
    (P : Finset (Pair D F)) (N t : ℕ) : Prop :=
  (P.filter fun p => weight p.2 = t).card ≤ Nat.choose N 2 ∧
    P.card ≤ firstBeyondHalfPairBound N t

/--
**UNPROVED STATEMENT TARGET (two-dimensional top kernel pencil).**
-/
def topKernelPencilTarget
    (topPairCount N t : ℕ) : Prop :=
  2 ≤ t →
    topPairCount ≤ Nat.choose N 2

/--
**UNPROVED STATEMENT TARGET (first beyond-half all-pair compiler).**
-/
def firstBeyondHalfAllPairTarget
    (P : Finset (Pair D F)) (N R t : ℕ) : Prop :=
  2 ≤ t →
    R + 1 = 2 * t →
    R ≤ N →
    FirstBeyondHalfPairConclusion P N t

/--
**UNPROVED STATEMENT TARGET (the `t=1` edge case).**
-/
def weightOneEdgeTarget
    (P : Finset (Pair D F)) (R : ℕ) : Prop :=
  R = 1 →
    P.card ≤ 1

/--
**UNPROVED STATEMENT TARGET (MCA/CA numerator interface).**
-/
def firstBeyondHalfNumeratorTarget
    (mcaNumerator caNumerator N R t : ℕ) : Prop :=
  2 ≤ t →
    R + 1 = 2 * t →
    R ≤ N →
    mcaNumerator ≤ firstBeyondHalfPairBound N t ∧
      caNumerator ≤ firstBeyondHalfPairBound N t

end FirstBeyondHalfKernelPencil
end GrandeFinale
