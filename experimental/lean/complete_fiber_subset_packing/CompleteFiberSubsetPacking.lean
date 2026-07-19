import DyadicCompleteFiberSlicingTarget

/-!
# Fixed-size subset packing

The elementary combinatorial kernel behind equation (2) of
`experimental/notes/l2/dyadic_complete_fiber_slicing_route_cut.md`.

The source application takes `ground = Q_c`, `objects` to be the fixed-`e`
list-polynomial family, and `block P = E_c(P)`.  The theorem below is stated
for arbitrary types and proves both finiteness and the exact floored binomial
quotient.
-/

namespace CompleteFiberSubsetPacking

noncomputable section

variable {α β : Type*}
local instance : DecidableEq α := Classical.decEq α

/-- Double-counting form of fixed-size subset packing. -/
private theorem finset_mul_choose_le
    (ground : Finset α) (blocks : Finset (Finset α))
    (e h : Nat)
    (hsub : ∀ A ∈ blocks, A ⊆ ground)
    (hcard : ∀ A ∈ blocks, A.card = e)
    (hinter : ∀ A ∈ blocks, ∀ B ∈ blocks, A ≠ B → (A ∩ B).card ≤ h) :
    blocks.card * e.choose (h + 1) ≤ ground.card.choose (h + 1) := by
  classical
  have hdisj : (↑blocks : Set (Finset α)).PairwiseDisjoint
      (fun A => A.powersetCard (h + 1)) := by
    intro A hA B hB hne
    change Disjoint (A.powersetCard (h + 1)) (B.powersetCard (h + 1))
    rw [Finset.disjoint_left]
    intro T hTA hTB
    have hTsubA : T ⊆ A := (Finset.mem_powersetCard.mp hTA).1
    have hTsubB : T ⊆ B := (Finset.mem_powersetCard.mp hTB).1
    have hTsub : T ⊆ A ∩ B := by
      intro x hx
      exact Finset.mem_inter.mpr ⟨hTsubA hx, hTsubB hx⟩
    have hTcard : T.card = h + 1 := (Finset.mem_powersetCard.mp hTA).2
    have hle : T.card ≤ (A ∩ B).card := Finset.card_le_card hTsub
    have hab := hinter A hA B hB hne
    omega
  have hunion : blocks.biUnion (fun A => A.powersetCard (h + 1)) ⊆
      ground.powersetCard (h + 1) := by
    intro T hT
    obtain ⟨A, hA, hTA⟩ := Finset.mem_biUnion.mp hT
    exact Finset.powersetCard_mono (hsub A hA) hTA
  calc
    blocks.card * e.choose (h + 1) =
        ∑ A ∈ blocks, (A.powersetCard (h + 1)).card := by
      symm
      apply Finset.sum_const_nat
      intro A hA
      rw [Finset.card_powersetCard, hcard A hA]
    _ = (blocks.biUnion (fun A => A.powersetCard (h + 1))).card :=
      (Finset.card_biUnion hdisj).symm
    _ ≤ (ground.powersetCard (h + 1)).card := Finset.card_le_card hunion
    _ = ground.card.choose (h + 1) := Finset.card_powersetCard _ _

/--
Fixed-size subset packing in the source's exact counting form.

Every object in `objects` owns an `e`-element block inside `ground`; distinct
objects have block intersection at most `h`; and `h+1 ≤ e`.  Then the object
set is finite and its cardinality is at most
`choose(|ground|,h+1) / choose(e,h+1)`.
-/
theorem subsetPacking_finite_and_ncard_le
    (ground : Finset α) (objects : Set β) (block : β → Finset α)
    (e h : Nat)
    (hsub : ∀ b ∈ objects, block b ⊆ ground)
    (hcard : ∀ b ∈ objects, (block b).card = e)
    (hinter : ∀ b₁ ∈ objects, ∀ b₂ ∈ objects,
      b₁ ≠ b₂ → (block b₁ ∩ block b₂).card ≤ h)
    (he : h + 1 ≤ e) :
    objects.Finite ∧
      objects.ncard ≤ ground.card.choose (h + 1) / e.choose (h + 1) := by
  classical
  have hinj : Set.InjOn block objects := by
    intro b₁ hb₁ b₂ hb₂ hblocks
    by_contra hne
    have hi := hinter b₁ hb₁ b₂ hb₂ hne
    have hinterCard : (block b₁ ∩ block b₂).card = e := by
      rw [hblocks, Finset.inter_self, hcard b₂ hb₂]
    omega
  have himageSub : block '' objects ⊆
      (ground.powersetCard e : Finset (Finset α)) := by
    rintro A ⟨b, hb, rfl⟩
    exact Finset.mem_powersetCard.mpr ⟨hsub b hb, hcard b hb⟩
  have himageFinite : (block '' objects).Finite :=
    (ground.powersetCard e).finite_toSet.subset himageSub
  have hobjectsFinite : objects.Finite := himageFinite.of_finite_image hinj
  refine ⟨hobjectsFinite, ?_⟩
  let objectFinset := hobjectsFinite.toFinset
  let blocks := objectFinset.image block
  have hblockInj : Set.InjOn block objectFinset := by
    intro b₁ hb₁ b₂ hb₂
    exact hinj (hobjectsFinite.mem_toFinset.mp hb₁)
      (hobjectsFinite.mem_toFinset.mp hb₂)
  have hblocksCard : blocks.card = objectFinset.card := by
    exact Finset.card_image_of_injOn hblockInj
  have hblocksSub : ∀ A ∈ blocks, A ⊆ ground := by
    intro A hA
    obtain ⟨b, hb, rfl⟩ := Finset.mem_image.mp hA
    exact hsub b (hobjectsFinite.mem_toFinset.mp hb)
  have hblocksSized : ∀ A ∈ blocks, A.card = e := by
    intro A hA
    obtain ⟨b, hb, rfl⟩ := Finset.mem_image.mp hA
    exact hcard b (hobjectsFinite.mem_toFinset.mp hb)
  have hblocksInter : ∀ A ∈ blocks, ∀ B ∈ blocks,
      A ≠ B → (A ∩ B).card ≤ h := by
    intro A hA B hB hne
    obtain ⟨b₁, hb₁, rfl⟩ := Finset.mem_image.mp hA
    obtain ⟨b₂, hb₂, rfl⟩ := Finset.mem_image.mp hB
    apply hinter b₁ (hobjectsFinite.mem_toFinset.mp hb₁)
      b₂ (hobjectsFinite.mem_toFinset.mp hb₂)
    intro heq
    subst b₂
    exact hne rfl
  have hmul := finset_mul_choose_le ground blocks e h
    hblocksSub hblocksSized hblocksInter
  have hden : 0 < e.choose (h + 1) := Nat.choose_pos he
  apply (Nat.le_div_iff_mul_le hden).2
  rw [Set.ncard_eq_toFinset_card objects hobjectsFinite, ← hblocksCard]
  exact hmul

section SourceConnector

variable {F : Type*} [Field F]
local instance : DecidableEq F := Classical.decEq F

open DyadicCompleteFiberSlicing

/-- The source's fixed-`e` family of received-list polynomials. -/
noncomputable def fixedFiberPolynomialSet
    (H : Subgroup Fˣ) [Fintype H] [LinearOrder H]
    (K m c e : Nat) (U : H → F) : Set (Polynomial F) :=
  {P | inReceivedList H K m U P ∧
    (completeFiberSet H c (canonicalSupport H m U P)).card = e}

/--
PROVED source equation (2), with `N_c` represented definitionally by
`(powerImage H c).card`.

For every field, finite ordered multiplicative subgroup, admissible
`1 ≤ K ≤ m ≤ n`, divisor `c ∣ n`, arbitrary received word, and fixed
`e ≥ floor((K-1)/c)+1`, the fixed-`e` received-list family is finite and
obeys the exact subset-packing quotient.
-/
theorem completeFiberSubsetPacking
    (H : Subgroup Fˣ) [Fintype H] [LinearOrder H]
    (n K m c e : Nat)
    (hHcard : Fintype.card H = n)
    (hrange : 1 ≤ K ∧ K ≤ m ∧ m ≤ n)
    (hc : c ∣ n)
    (U : H → F)
    (he : (K - 1) / c + 1 ≤ e) :
    (fixedFiberPolynomialSet H K m c e U).Finite ∧
      (fixedFiberPolynomialSet H K m c e U).ncard ≤
        (powerImage H c).card.choose ((K - 1) / c + 1) /
          e.choose ((K - 1) / c + 1) := by
  classical
  apply subsetPacking_finite_and_ncard_le
      (ground := powerImage H c)
      (objects := fixedFiberPolynomialSet H K m c e U)
      (block := fun P => completeFiberSet H c (canonicalSupport H m U P))
      (e := e) (h := (K - 1) / c)
  · intro P hP y hy
    exact (Finset.mem_filter.mp hy).1
  · intro P hP
    exact hP.2
  · intro P hP Q hQ hne
    exact completeFiberIntersection H n K m c hHcard hrange hc U P Q
      hP.1 hQ.1 hne
  · exact he

end SourceConnector

end

end CompleteFiberSubsetPacking
