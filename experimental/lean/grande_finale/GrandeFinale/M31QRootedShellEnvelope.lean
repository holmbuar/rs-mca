import Mathlib

/-!
# Mersenne-31 row-sharp Q rooted-shell envelope

This module replaces the standalone Python validation of the rooted-shell
packet by kernel-checked Lean statements.  It proves the finite summation
compiler, checks the deployed `3+7` arithmetic for both Mersenne-31 rows, and
formalizes the explicit `2+7` counterexample on a finite Chebyshev control.

The astronomically large binomial quotient that produces each packet floor is
kept as packet input, following the existing finite-certificate convention in
`GrandeFinale.lean`.  Every deduction from those packet floors, including the
integer reserves, is proved here.
-/

open scoped BigOperators Classical

namespace GrandeFinale
namespace M31QRootedShellEnvelope

set_option autoImplicit false

/-- Summing a rooted shell excess bound.  The local hypothesis is the exact
integer form `Q * max(degree-b,0) ≤ c * shellSize`; natural subtraction already
implements the maximum with zero. -/
theorem shellExcessSum_le
    {ι : Type*} [DecidableEq ι]
    (shells : Finset ι) (degree shellSize : ι → ℕ)
    (Q b c totalShell : ℕ)
    (hQ : 0 < Q)
    (hlocal : ∀ e ∈ shells, Q * (degree e - b) ≤ c * shellSize e)
    (htotal : ∑ e in shells, shellSize e ≤ totalShell) :
    ∑ e in shells, degree e ≤
      b * shells.card + (c * totalShell) / Q := by
  have hdegree :
      ∑ e in shells, degree e ≤
        ∑ e in shells, (b + (degree e - b)) := by
    exact Finset.sum_le_sum fun e he => by omega
  have hexcessMul :
      Q * (∑ e in shells, (degree e - b)) ≤ c * totalShell := by
    calc
      Q * (∑ e in shells, (degree e - b)) =
          ∑ e in shells, Q * (degree e - b) := by
            rw [Finset.mul_sum]
      _ ≤ ∑ e in shells, c * shellSize e := by
            exact Finset.sum_le_sum fun e he => hlocal e he
      _ = c * (∑ e in shells, shellSize e) := by
            rw [Finset.mul_sum]
      _ ≤ c * totalShell := Nat.mul_le_mul_left c htotal
  have hexcess :
      ∑ e in shells, (degree e - b) ≤ (c * totalShell) / Q := by
    exact (Nat.le_div_iff_mul_le hQ).2 (by
      simpa [Nat.mul_comm] using hexcessMul)
  calc
    ∑ e in shells, degree e ≤
        ∑ e in shells, (b + (degree e - b)) := hdegree
    _ = b * shells.card + ∑ e in shells, (degree e - b) := by
        simp [Finset.sum_add_distrib, Nat.mul_comm]
    _ ≤ b * shells.card + (c * totalShell) / Q :=
        Nat.add_le_add_left hexcess _

/-- Rooted-shell envelope.  `hfamily` is the rooted partition of all members
other than the anchor, `hshellCount` bounds the number of admissible shells,
and `htotal` is the Johnson-shell tail bound. -/
theorem rootedShellEnvelope
    {ι : Type*} [DecidableEq ι]
    (shells : Finset ι) (degree shellSize : ι → ℕ)
    (Q b c totalShell familyCard shellCount : ℕ)
    (hQ : 0 < Q)
    (hfamily : familyCard ≤ 1 + ∑ e in shells, degree e)
    (hshellCount : shells.card ≤ shellCount)
    (hlocal : ∀ e ∈ shells, Q * (degree e - b) ≤ c * shellSize e)
    (htotal : ∑ e in shells, shellSize e ≤ totalShell) :
    familyCard ≤ 1 + b * shellCount + (c * totalShell) / Q := by
  have hsum := shellExcessSum_le shells degree shellSize Q b c totalShell
    hQ hlocal htotal
  have hb : b * shells.card ≤ b * shellCount :=
    Nat.mul_le_mul_left b hshellCount
  omega

namespace Deployed

/-- Mersenne-31 base prime. -/
def pM31 : ℕ := 2147483647

/-- Official auxiliary-row integer budget. -/
def Bstar : ℕ := 16777215

/-- Shared deployed prefix depth. -/
def w : ℕ := 67447

/-- Mersenne-31 list-row complement size and admissible shell count. -/
def listM : ℕ := 981129
def listShellCount : ℕ := 913682

/-- Packet-certified value `floor (7 * choose n m / p^w)` for the list row. -/
def listScaledFloor : ℕ := 13955739

/-- The resulting rooted-shell upper bound. -/
def listBound : ℕ := 1 + 3 * listShellCount + listScaledFloor

/-- Mersenne-31 MCA-row complement size and admissible shell count. -/
def mcaM : ℕ := 981128
def mcaShellCount : ℕ := 913681

/-- Packet-certified value `floor (7 * choose n m / p^w)` for the MCA row. -/
def mcaScaledFloor : ℕ := 12268894

def mcaBound : ℕ := 1 + 3 * mcaShellCount + mcaScaledFloor

theorem pM31_eq : pM31 = 2 ^ 31 - 1 := by norm_num [pM31]

theorem Bstar_formula : pM31 ^ 4 / 2 ^ 100 = Bstar := by native_decide

theorem listShellCount_eq : listShellCount = listM - w := by native_decide

theorem listBound_eq : listBound = 16696786 := by native_decide

theorem listBound_le_budget : listBound ≤ Bstar := by native_decide

theorem listReserve_eq : Bstar - listBound = 80429 := by native_decide

/-- Intercept two would fit the deployed budget, but the finite Chebyshev
counterexample below refutes its local shell hypothesis. -/
theorem list_two_plus_seven_fits :
    1 + 2 * listShellCount + listScaledFloor ≤ Bstar := by native_decide

/-- Intercept four is already too expensive at the binding list row. -/
theorem list_four_plus_seven_exceeds :
    Bstar < 1 + 4 * listShellCount + listScaledFloor := by native_decide

theorem mcaShellCount_eq : mcaShellCount = mcaM - w := by native_decide

theorem mcaBound_eq : mcaBound = 15009938 := by native_decide

theorem mcaBound_le_budget : mcaBound ≤ Bstar := by native_decide

theorem mcaReserve_eq : Bstar - mcaBound = 1767277 := by native_decide

end Deployed

namespace Toy

abbrev F := ZMod 127

/-- A 16-point finite Chebyshev control domain. -/
def domain : Fin 16 → F :=
  ![5, 39, 89, 42, 22, 125, 9, 53, 122, 88, 38, 85, 105, 2, 118, 74]

/-- Negation partner on the control domain. -/
def partner : Fin 16 → Fin 16 :=
  ![8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7]

def t2 (x : F) : F := 2 * x ^ 2 - 1

def anchor : Finset (Fin 16) :=
  [0, 1, 3, 4, 7, 8, 13, 14].toFinset

def neighbors : Fin 6 → Finset (Fin 16) :=
  ![
    [0, 2, 5, 6, 10, 11, 12, 15].toFinset,
    [2, 3, 6, 9, 10, 11, 12, 15].toFinset,
    [2, 4, 5, 6, 9, 10, 11, 15].toFinset,
    [2, 5, 6, 9, 10, 11, 12, 14].toFinset,
    [2, 5, 6, 9, 10, 12, 13, 15].toFinset,
    [2, 5, 7, 9, 10, 11, 12, 15].toFinset
  ]

def prefix1 (S : Finset (Fin 16)) : F := ∑ i in S, domain i

def exchangeDistance (A B : Finset (Fin 16)) : ℕ :=
  A.card - (A ∩ B).card

def negationClosed (S : Finset (Fin 16)) : Prop :=
  ∀ i ∈ S, partner i ∈ S

def commonCore : Finset (Fin 16) :=
  Finset.univ.filter fun x => x ∈ anchor ∧ ∀ j : Fin 6, x ∈ neighbors j

def rootedDegree (e : ℕ) : ℕ :=
  (Finset.univ.filter fun j : Fin 6 =>
    exchangeDistance anchor (neighbors j) = e).card

def ambientShell7 : ℕ := Nat.choose 8 7 * Nat.choose 8 7

theorem partner_is_negation :
    ∀ i : Fin 16, domain (partner i) = -domain i := by native_decide

/-- The displayed pairs are exactly the fibers of the Chebyshev map `T₂`. -/
theorem t2_fibers :
    ∀ i j : Fin 16,
      t2 (domain i) = t2 (domain j) ↔ j = i ∨ j = partner i := by
  native_decide

/-- The control is not a multiplicative subgroup in disguise. -/
theorem not_product_closed :
    ¬ ∃ k : Fin 16, domain k = domain 0 * domain 1 := by native_decide

theorem anchor_card : anchor.card = 8 := by native_decide

theorem neighbor_cards : ∀ j : Fin 6, (neighbors j).card = 8 := by
  native_decide

theorem anchor_prefix : prefix1 anchor = 22 := by native_decide

theorem neighbor_prefixes : ∀ j : Fin 6, prefix1 (neighbors j) = 22 := by
  native_decide

theorem anchor_neighbor_distance :
    ∀ j : Fin 6, exchangeDistance anchor (neighbors j) = 7 := by
  native_decide

theorem anchor_not_negationClosed : ¬ negationClosed anchor := by native_decide

theorem neighbors_not_negationClosed :
    ∀ j : Fin 6, ¬ negationClosed (neighbors j) := by native_decide

/-- The seven displayed supports have no planted common core. -/
theorem commonCore_empty : commonCore = ∅ := by native_decide

theorem rootedDegree_seven : rootedDegree 7 = 6 := by native_decide

theorem ambientShell7_eq : ambientShell7 = 64 := by native_decide

/-- Exact failure of the stronger `2+7` local envelope. -/
theorem two_plus_seven_fails :
    7 * ambientShell7 < 127 * (rootedDegree 7 - 2) := by native_decide

/-- The same rooted configuration satisfies the neighboring `3+7` inequality. -/
theorem three_plus_seven_holds :
    127 * (rootedDegree 7 - 3) ≤ 7 * ambientShell7 := by native_decide

end Toy

#print axioms shellExcessSum_le
#print axioms rootedShellEnvelope
#print axioms Deployed.listBound_le_budget
#print axioms Toy.two_plus_seven_fails
#print axioms Toy.three_plus_seven_holds

end M31QRootedShellEnvelope
end GrandeFinale
