import Mathlib

/-!
# Dyadic complete-fiber slicing: statement target

This file records the general source-realized complete-fiber intersection
theorem from
`experimental/notes/l2/dyadic_complete_fiber_slicing_route_cut.md`.

The paper proof is given in that note. This Mathlib-facing target has one
explicit `sorry`; it is not a formal proof certificate. The total order is
part of the data because it canonically selects the first `m` agreement
points for every list polynomial.
-/

namespace DyadicCompleteFiberSlicing

variable {F : Type*} [Field F]

/-- Agreement points of `P` with the arbitrary received word `U` on `H`. -/
noncomputable def agreementSet
    (H : Subgroup Fˣ) [Fintype H] (U : H → F) (P : Polynomial F) : Finset H := by
  classical
  exact Finset.univ.filter fun x => P.eval ((x : Fˣ) : F) = U x

/-- The first exactly `m` agreement points in the fixed total order. -/
noncomputable def canonicalSupport
    (H : Subgroup Fˣ) [Fintype H] [LinearOrder H]
    (m : Nat) (U : H → F) (P : Polynomial F) : Finset H := by
  classical
  exact (agreementSet H U P).filter fun x =>
    ((agreementSet H U P).filter fun y => y < x).card < m

/-- Membership in the received-word list at degree bound `K` and agreement `m`. -/
def inReceivedList
    (H : Subgroup Fˣ) [Fintype H]
    (K m : Nat) (U : H → F) (P : Polynomial F) : Prop :=
  P.natDegree < K ∧ m ≤ (agreementSet H U P).card

/-- The image `Q_c` of the power map `x ↦ x^c` on `H`. -/
noncomputable def powerImage
    (H : Subgroup Fˣ) [Fintype H] (c : Nat) : Finset F := by
  classical
  exact Finset.univ.image fun x : H => ((x : Fˣ) : F) ^ c

/-- Power-map image values whose complete fibers lie in `S`. -/
noncomputable def completeFiberSet
    (H : Subgroup Fˣ) [Fintype H] (c : Nat) (S : Finset H) : Finset F := by
  classical
  exact (powerImage H c).filter fun y =>
    ∀ x : H, ((x : Fˣ) : F) ^ c = y → x ∈ S

/--
STATEMENT TARGET (UNPROVED).

Exact hypotheses: an arbitrary field; a finite multiplicative subgroup `H`
of order `n`; `1 ≤ K ≤ m ≤ n`; a fixed total order on `H`; an
arbitrary received word; two distinct degree-`< K` list polynomials with at
least `m` agreements; and a divisor `c ∣ n`. The conclusion is the complete
fiber intersection ceiling `floor((K-1)/c)` for their canonical first-`m`
supports.
-/
theorem completeFiberIntersection_STATEMENT_TARGET_UNPROVED
    (H : Subgroup Fˣ) [Fintype H] [LinearOrder H]
    (n K m c : Nat)
    (hcard : Fintype.card H = n)
    (hrange : 1 ≤ K ∧ K ≤ m ∧ m ≤ n)
    (hc : c ∣ n)
    (U : H → F)
    (P Q : Polynomial F)
    (hP : inReceivedList H K m U P)
    (hQ : inReceivedList H K m U Q)
    (hne : P ≠ Q) :
    ((completeFiberSet H c (canonicalSupport H m U P)) ∩
      completeFiberSet H c (canonicalSupport H m U Q)).card ≤
      (K - 1) / c := by
  sorry

end DyadicCompleteFiberSlicing
