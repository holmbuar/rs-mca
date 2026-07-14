import GrandeFinale.DirectionDistanceAllPairs

/-!
# Sharp complete absorption at fixed deficiency

This module contains **UNPROVED STATEMENT TARGETS**.  It records the sharp
complete all-pair and MCA/CA numerator interfaces for `R=2t-d`.  It does not
claim a Lean proof.
-/

open scoped Classical

noncomputable section

namespace GrandeFinale
namespace FixedDeficiencyCompleteAbsorption

open DirectionDistanceAllPairs

set_option autoImplicit false

universe u v

variable {D : Type u} {F : Type v}
variable [Fintype D] [DecidableEq D]
variable [Field F] [DecidableEq F]

abbrev Pair (D : Type u) (F : Type v) := SlopeErrorPair D F

def completePairBound (N d : ℕ) : ℕ :=
  Nat.choose N (d + 1)

/--
**UNPROVED STATEMENT TARGET (chargeable top-kernel basis count).**
-/
def chargeableBasisTarget
    (chargeableCount t d : ℕ) : Prop :=
  1 ≤ d →
    d < t →
    t - d ≤ chargeableCount

/--
**UNPROVED STATEMENT TARGET (sharp complete fixed-deficiency compiler).**
-/
def completeAllPairTarget
    (P : Finset (Pair D F)) (N R t d : ℕ) : Prop :=
  1 ≤ d →
    d < t →
    R + d = 2 * t →
    R ≤ N →
    P.card ≤ completePairBound N d

/--
**UNPROVED STATEMENT TARGET (MCA/CA numerator interface).**
-/
def completeNumeratorTarget
    (mcaNumerator caNumerator N R t d : ℕ) : Prop :=
  1 ≤ d →
    d < t →
    R + d = 2 * t →
    R ≤ N →
    mcaNumerator ≤ completePairBound N d ∧
      caNumerator ≤ completePairBound N d

/--
**UNPROVED STATEMENT TARGET (active-paper agreement notation).**

The equation `2 * a + d = N + K` is the subtraction-free form of
`d = N + K - 2 * a`; `K < a` is equivalent to `d < N - a` once the row
identities hold.
-/
def strictBeyondHalfAgreementTarget
    (mcaNumerator caNumerator N K a d : ℕ) : Prop :=
  K < a →
    1 ≤ d →
    2 * a + d = N + K →
    mcaNumerator ≤ completePairBound N d ∧
      caNumerator ≤ completePairBound N d

/-- Literal finite safe-side comparison once the numerator theorem is supplied. -/
def finiteTargetCertificateTarget
    (mcaNumerator targetBudget N K a d : ℕ) : Prop :=
  K < a →
    1 ≤ d →
    2 * a + d = N + K →
    mcaNumerator ≤ completePairBound N d →
    completePairBound N d ≤ targetBudget →
    mcaNumerator ≤ targetBudget

/--
**UNPROVED STATEMENT TARGET (canonical Lagrange equality).**
-/
def canonicalSharpnessTarget
    (completePairCount N d : ℕ) : Prop :=
  completePairCount = completePairBound N d

/--
**UNPROVED STATEMENT TARGET (distinct-slope canonical numerator equality).**
-/
def canonicalNumeratorSharpnessTarget
    (mcaNumerator caNumerator N d : ℕ) : Prop :=
  mcaNumerator = completePairBound N d ∧
    caNumerator = completePairBound N d

end FixedDeficiencyCompleteAbsorption
end GrandeFinale
