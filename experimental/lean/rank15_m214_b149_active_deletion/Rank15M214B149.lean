import Mathlib.Data.Finset.Card

/-!
Statement target for the rank-15 M214 active-deletion theorem.

This file deliberately exposes the finite-incidence hypotheses while leaving
projective realizability abstract. It is an unproved formalization target, not
a Lean certificate for the geometric argument.
-/

namespace Rank15M214B149

structure ActiveArrangement where
  characteristic : Nat
  markedPoints : Nat
  activeLines : Nat
  incidentLines : Fin markedPoints -> Finset (Fin activeLines)
  projectivelyRealizable : Prop

def ExactFifteenFold (A : ActiveArrangement) : Prop :=
  ∀ point, (A.incidentLines point).card = 15

def EveryLineActive (A : ActiveArrangement) : Prop :=
  ∀ line, ∃ point, line ∈ A.incidentLines point

def Admissible (A : ActiveArrangement) : Prop :=
  (A.characteristic = 0 ∨ 214 < A.characteristic) ∧
  149 ≤ A.markedPoints ∧
  A.markedPoints ≤ A.activeLines ∧
  A.activeLines ≤ 214 ∧
  A.projectivelyRealizable ∧
  ExactFifteenFold A ∧
  EveryLineActive A

axiom no_m214_b149_active_arrangement (A : ActiveArrangement) :
  ¬ Admissible A

end Rank15M214B149
