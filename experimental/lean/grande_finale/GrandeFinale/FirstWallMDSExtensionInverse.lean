import Mathlib

/-!
# First-wall MDS dimension-lift inverse: finite counting companion

This module formalizes the finite owner-map consequences used at the first
wall.  A finite set of basis witnesses maps to its set of pair owners.  The
owner census is at most the witness census, and equality is equivalent to
injectivity of the owner map on the witness set.  It also records the exact
fiber partition behind the weighted occupancy ledger.

The Reed--Solomon linear algebra that constructs the owner map, and the
equivalence between injectivity and the augmented MDS condition, remain in the
mathematical note; they are not asserted by this abstract counting module.
-/

open scoped BigOperators

namespace GrandeFinale
namespace FirstWallMDSExtensionInverse

set_option autoImplicit false

universe u v

variable {Basis : Type u} {Owner : Type v}

/-- The realized owner set of a finite basis-witness family. -/
def ownerImage [DecidableEq Owner] (basis : Finset Basis)
    (owner : Basis -> Owner) : Finset Owner :=
  basis.image owner

/-- The witnesses in `basis` assigned to one owner. -/
def ownerFiber [DecidableEq Owner] (basis : Finset Basis)
    (owner : Basis -> Owner) (value : Owner) : Finset Basis :=
  basis.filter fun witness => owner witness = value

/-- The number of realized owners never exceeds the number of witnesses. -/
theorem ownerImage_card_le [DecidableEq Owner] (basis : Finset Basis)
    (owner : Basis -> Owner) :
    (ownerImage basis owner).card <= basis.card := by
  exact Finset.card_image_le

/-- Owner-count equality is exactly injectivity on the witness family. -/
theorem ownerImage_card_eq_iff_injOn [DecidableEq Owner]
    (basis : Finset Basis) (owner : Basis -> Owner) :
    (ownerImage basis owner).card = basis.card <->
      Set.InjOn owner (basis : Set Basis) := by
  simpa [ownerImage] using
    (Finset.card_image_iff (s := basis) (f := owner))

/-- The complete finite-type owner census is bounded by the domain size. -/
theorem finite_ownerImage_card_le [Fintype Basis] [DecidableEq Owner]
    (owner : Basis -> Owner) :
    (ownerImage (Finset.univ : Finset Basis) owner).card <=
      Fintype.card Basis := by
  simpa [ownerImage] using
    (Finset.card_image_le
      (s := (Finset.univ : Finset Basis)) (f := owner))

/-- On a complete finite domain, owner-count equality is ordinary injectivity. -/
theorem finite_ownerImage_card_eq_iff_injective
    [Fintype Basis] [DecidableEq Owner] (owner : Basis -> Owner) :
    (ownerImage (Finset.univ : Finset Basis) owner).card =
        Fintype.card Basis <->
      Function.Injective owner := by
  simpa [ownerImage] using
    (Finset.card_image_iff
      (s := (Finset.univ : Finset Basis)) (f := owner))

/-- Exact partition of the witness census by its realized owner fibers. -/
theorem card_eq_sum_ownerFiber [DecidableEq Owner]
    (basis : Finset Basis) (owner : Basis -> Owner) :
    basis.card =
      ∑ value ∈ ownerImage basis owner,
        (ownerFiber basis owner value).card := by
  simpa [ownerImage, ownerFiber] using
    (Finset.card_eq_sum_card_fiberwise
      (s := basis) (t := basis.image owner) (f := owner)
      (fun witness hwitness => Finset.mem_image_of_mem owner hwitness))

/-! ## Pinned first-wall arithmetic -/

/-- The rank-four F11 fixture has seventy first-wall basis sets. -/
theorem choose_eight_four : Nat.choose 8 4 = 70 := by
  norm_num [Nat.choose]

/-- `8` witnesses taken `3` at a time give `56` first-wall basis sets. -/
theorem choose_eight_three : Nat.choose 8 3 = 56 := by
  norm_num [Nat.choose]

/-- `7` witnesses taken `3` at a time give `35` first-wall basis sets. -/
theorem choose_seven_three : Nat.choose 7 3 = 35 := by
  norm_num [Nat.choose]

/-- The six-coordinate, rank-three sanity fixture has twenty basis sets. -/
theorem choose_six_three : Nat.choose 6 3 = 20 := by
  norm_num [Nat.choose]

/-- The non-MDS sanity fixture still exhausts the weighted twenty-set ledger. -/
theorem f7_nonMDS_weighted_occupancy :
    12 * Nat.choose 3 3 + 2 * Nat.choose 4 3 = Nat.choose 6 3 := by
  norm_num [Nat.choose]

end FirstWallMDSExtensionInverse
end GrandeFinale
