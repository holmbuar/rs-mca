import GrandeFinale.DirectionDistanceAllPairs

/-!
# Fixed-deficiency kernel-minor compiler

This module contains **UNPROVED STATEMENT TARGETS**.  It records the sharp
exact-stratum binomial bound, the complete fixed-deficiency all-pair bound,
and the MCA/CA numerator interface.  It does not claim a Lean proof.
-/

open scoped BigOperators Classical

noncomputable section

namespace GrandeFinale
namespace FixedDeficiencyKernelMinorCompiler

open DirectionDistanceAllPairs

set_option autoImplicit false

universe u v

variable {D : Type u} {F : Type v}
variable [Fintype D] [DecidableEq D]
variable [Field F] [DecidableEq F]

abbrev Pair (D : Type u) (F : Type v) := SlopeErrorPair D F

def fixedDeficiencyPairBound (N R t : ℕ) : ℕ :=
  N + R / 2 +
    ∑ s ∈ Finset.Icc (R / 2 + 1) t,
      Nat.choose N (2 * s - R + 1)

/--
**UNPROVED STATEMENT TARGET (one strictly beyond-half exact stratum).**
-/
def exactKernelMinorTarget
    (exactPairCount N R s kappa : ℕ) : Prop :=
  2 ≤ kappa →
    s < R →
    R + kappa = 2 * s + 1 →
    exactPairCount ≤ Nat.choose N kappa

/--
**UNPROVED STATEMENT TARGET (complete fixed-deficiency all-pair compiler).**
-/
def fixedDeficiencyAllPairTarget
    (P : Finset (Pair D F)) (N R t d : ℕ) : Prop :=
  1 ≤ d →
    d < t →
    R + d = 2 * t →
    R ≤ N →
    P.card ≤ fixedDeficiencyPairBound N R t

/--
**UNPROVED STATEMENT TARGET (MCA/CA numerator interface).**
-/
def fixedDeficiencyNumeratorTarget
    (mcaNumerator caNumerator N R t d : ℕ) : Prop :=
  1 ≤ d →
    d < t →
    R + d = 2 * t →
    R ≤ N →
    mcaNumerator ≤ fixedDeficiencyPairBound N R t ∧
      caNumerator ≤ fixedDeficiencyPairBound N R t

end FixedDeficiencyKernelMinorCompiler
end GrandeFinale
