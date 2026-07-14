import GrandeFinale.DirectionDistanceAllPairs

/-!
# All-depth sparse-splitting sharpness

This module contains UNPROVED STATEMENT TARGETS for the literature-dependent
Morse-monodromy and finite-field Chebotarev theorem.  It is not a Lean proof.
-/

open scoped Classical

noncomputable section

namespace GrandeFinale
namespace AllDepthSparseSplitSharpness

set_option autoImplicit false

/-- UNPROVED STATEMENT TARGET: all-depth parameter identities. -/
def parameterTarget (R t d r : ℕ) : Prop :=
  1 ≤ d →
  1 ≤ r →
  t = d + r →
  R = t + r →
  R + d = 2 * t

/-- UNPROVED STATEMENT TARGET: complete pair upper interface. -/
def completePairTarget (pairCount q d : ℕ) : Prop :=
  pairCount ≤ Nat.choose q (d + 1)

/--
UNPROVED STATEMENT TARGET: finite two-sided form of the Chebotarev asymptotic.
-/
def chebotarevErrorTarget
    (pairCount q t d errorScale : ℕ) : Prop :=
  pairCount * Nat.factorial t ≤
      q ^ (d + 1) + errorScale ∧
    q ^ (d + 1) ≤
      pairCount * Nat.factorial t + errorScale

end AllDepthSparseSplitSharpness
end GrandeFinale
