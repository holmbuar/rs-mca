import Std

/-!
# Elimination of the M31 padded rank-two coloop terminal

The first three rows of a padded syzygy frame give columns in a three-dimensional
vector space over the coefficient field (or the polynomial fraction field).
The padded locator row gives a dependence among all 46 columns.  Its coefficient
at the distinguished extra column is a nonzero locator polynomial.  Therefore
that extra column cannot be a coloop: a coloop has zero coefficient in every
column dependence.

The small algebraic object is restated locally.  Its zero, addition, and
multiplication operations are explicit fields, so this stdlib-only module does
not import an external algebra hierarchy or an open-PR repository module.
It does not construct common-core add-back, prove row-sharp Q, pay list-interior
mass, or close an adjacent row.
-/

set_option autoImplicit false

namespace SidonEffectiveImage.M31RankTwoColoop

/-- Exact deployed constants carried by the padded rank-three source frame. -/
def markedSourceKeyFloor : Nat := 259881
def firstIndexBound : Nat := 20765
def firstTwoIndexBound : Nat := 41530
def firstThreeIndexBound : Nat := 62295
def shiftedLocatorCutoff : Nat := 67447

/-- Fold the old 45 coefficients in their canonical column order. -/
def foldOld45 {K : Type} (zero : K) (add : K → K → K)
    (term : Fin 45 → K) : K :=
  (List.ofFn term).foldl add zero

/--
The three padded syzygy rows, split into the old 45 columns and the distinguished
extra column.  `locatorRelation` is exactly the row-by-row syzygy equation.  The
four index hypotheses record the deployed padded-frame bounds supplied by the
source theorem; the no-coloop proof is stronger and needs only the relation and
the nonzero distinguished locator coefficient.
-/
structure PaddedThreeRowSyzygyFrame (K : Type) where
  zero : K
  add : K → K → K
  mul : K → K → K
  oldColumn : Fin 45 → Fin 3 → K
  extraColumn : Fin 3 → K
  oldLocator : Fin 45 → K
  extraLocator : K
  extraLocator_ne_zero : extraLocator ≠ zero
  locatorRelation :
    ∀ r : Fin 3,
      add
        (foldOld45 zero add (fun i => mul (oldLocator i) (oldColumn i r)))
        (mul extraLocator (extraColumn r)) = zero
  lambda1 : Nat
  lambda2 : Nat
  lambda3 : Nat
  lambda1_bound : lambda1 ≤ firstIndexBound
  lambda12_bound : lambda1 + lambda2 ≤ firstTwoIndexBound
  lambda123_bound : lambda1 + lambda2 + lambda3 ≤ firstThreeIndexBound
  below_cutoff : lambda1 + lambda2 + lambda3 < shiftedLocatorCutoff

/-- The exact row-wise column-dependence predicate used by the source matroid. -/
def ColumnRelation {K : Type} (frame : PaddedThreeRowSyzygyFrame K)
    (oldCoeff : Fin 45 → K) (extraCoeff : K) : Prop :=
  ∀ r : Fin 3,
    frame.add
      (foldOld45 frame.zero frame.add
        (fun i => frame.mul (oldCoeff i) (frame.oldColumn i r)))
      (frame.mul extraCoeff (frame.extraColumn r)) = frame.zero

/--
The old 45 columns have rank at most two when they all lie in the span of two
vectors, using the same coefficient-field operations carried by the frame.
This is the rank-two half of the source terminal.
-/
def OldColumnsRankAtMostTwo {K : Type}
    (frame : PaddedThreeRowSyzygyFrame K) : Prop :=
  ∃ u v : Fin 3 → K,
    ∀ i : Fin 45, ∃ a b : K,
      ∀ r : Fin 3,
        frame.oldColumn i r =
          frame.add (frame.mul a (u r)) (frame.mul b (v r))

/--
Dependence characterization of a coloop: every column dependence has zero
coefficient at the distinguished extra column.
-/
def ExtraIsColoop {K : Type}
    (frame : PaddedThreeRowSyzygyFrame K) : Prop :=
  ∀ (oldCoeff : Fin 45 → K) (extraCoeff : K),
    ColumnRelation frame oldCoeff extraCoeff → extraCoeff = frame.zero

/-- The exact sibling terminal named by the rank-46 compiler. -/
def RankTwoColoopTerminal {K : Type}
    (frame : PaddedThreeRowSyzygyFrame K) : Prop :=
  OldColumnsRankAtMostTwo frame ∧ ExtraIsColoop frame

/-- The padded locator row is a dependence with nonzero extra coefficient. -/
theorem paddedLocatorGivesNonzeroExtraDependence {K : Type}
    (frame : PaddedThreeRowSyzygyFrame K) :
    ∃ (oldCoeff : Fin 45 → K) (extraCoeff : K),
      extraCoeff ≠ frame.zero ∧ ColumnRelation frame oldCoeff extraCoeff := by
  refine ⟨frame.oldLocator, frame.extraLocator, frame.extraLocator_ne_zero, ?_⟩
  intro r
  exact frame.locatorRelation r

/-- No stated padded three-row syzygy frame has a coloop extra column. -/
theorem extraColumnIsNotColoop {K : Type}
    (frame : PaddedThreeRowSyzygyFrame K) :
    ¬ ExtraIsColoop frame := by
  intro hColoop
  have hRelation : ColumnRelation frame frame.oldLocator frame.extraLocator := by
    intro r
    exact frame.locatorRelation r
  have hZero : frame.extraLocator = frame.zero :=
    hColoop frame.oldLocator frame.extraLocator hRelation
  exact frame.extraLocator_ne_zero hZero

/-- `UNPAID_RANK2_COLOOP` is empty, even before the rank-at-most-two hypothesis is used. -/
theorem rankTwoColoopTerminalIsEmpty {K : Type}
    (frame : PaddedThreeRowSyzygyFrame K) :
    ¬ RankTwoColoopTerminal frame := by
  intro hTerminal
  exact extraColumnIsNotColoop frame hTerminal.2

/-- Pointwise elimination on every supplied list of marked source-key frames. -/
theorem everyMarkedFrameExcludesRankTwoColoop {K : Type}
    (frames : List (PaddedThreeRowSyzygyFrame K)) :
    ∀ frame ∈ frames, ¬ RankTwoColoopTerminal frame := by
  intro frame _hMem
  exact rankTwoColoopTerminalIsEmpty frame

/-- Kernel-checked deployed arithmetic retained from the padded-frame source. -/
theorem deployedConstantsExact :
    markedSourceKeyFloor = 259881 ∧
    firstIndexBound = 20765 ∧
    firstTwoIndexBound = 41530 ∧
    firstThreeIndexBound = 62295 ∧
    firstThreeIndexBound < shiftedLocatorCutoff := by
  decide

#print axioms paddedLocatorGivesNonzeroExtraDependence
#print axioms extraColumnIsNotColoop
#print axioms rankTwoColoopTerminalIsEmpty
#print axioms everyMarkedFrameExcludesRankTwoColoop
#print axioms deployedConstantsExact

end SidonEffectiveImage.M31RankTwoColoop
