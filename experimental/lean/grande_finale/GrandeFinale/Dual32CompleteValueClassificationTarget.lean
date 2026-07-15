import Mathlib

/-!
# Statement target: complete classification of deployed 32-valued phases

This is an intentionally unproved Lean statement target matching the theorem
proved by the accompanying note and exact certificate. It is not imported by
`GrandeFinale.lean` and is not Lean-certified.
-/

namespace GrandeFinale

open Polynomial

private abbrev Dual32Field := ZMod 2130706433

private def dual32Domain : Finset Dual32Field :=
  Finset.univ.filter (fun x => x ^ (2097152 : Nat) = 1)

theorem dual32_complete_value_classification_target
    (f : Polynomial Dual32Field)
    (hdegree : f.natDegree ≤ 67471) :
    (0 < f.natDegree ∧
        (dual32Domain.image fun x => f.eval x).card = 32) ↔
      ∃ a b : Dual32Field,
        a ≠ 0 ∧ f = C a * X ^ (65536 : Nat) + C b := by
  sorry

end GrandeFinale
