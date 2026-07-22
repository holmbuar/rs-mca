import Std

/-!
# Effective-image MI+MA half-slice falsifier

A stdlib-only exact regression for the `N = 8`, `m = 4` middle Hamming slice.
The boundary map sends a support to its binary incidence vector.  Its realized
image fibers are singletons, but the 35 middle-weight effective character
classes already contribute absolute Fourier mass 210.  The complete 127-character
effective dual has absolute mass 490, so the exact finite multiplier is
`kappa = 8` (and the middle classes alone already force `kappa >= 4`).

This module is a finite arithmetic/census regression.  It does not formalize
finite fields, asymptotics, an RS first-match leaf, or an MCA denominator.
-/

set_option maxRecDepth 8192

namespace SidonEffectiveImage.HalfSliceFalsifier

/-- All `k`-subsets of `{0, ..., n-1}`, represented as duplicate-free lists. -/
def choose : Nat → Nat → List (List Nat)
  | _, 0 => [[]]
  | 0, _ + 1 => []
  | n + 1, k + 1 =>
      (choose n k).map (fun s => n :: s) ++ choose n (k + 1)

/-- Executable powerset of a list. -/
def powerset : List Nat → List (List Nat)
  | [] => [[]]
  | x :: xs =>
      let tail := powerset xs
      tail ++ tail.map (fun s => x :: s)

/-- Boolean nonemptiness, avoiding any external finite-set API. -/
def nonemptyList {α : Type} : List α → Bool
  | [] => false
  | _ :: _ => true

/-- Duplicate-freeness, kept executable and stdlib-only. -/
def noDuplicates {α : Type} [BEq α] : List α → Bool
  | [] => true
  | x :: xs => !xs.contains x && noDuplicates xs

/-- Intersection cardinality for duplicate-free supports. -/
def interCard (A B : List Nat) : Nat :=
  (A.filter fun x => B.contains x).length

/-- One Walsh sign `(-1)^|S ∩ Y|`. -/
def walshTerm (S Y : List Nat) : Int :=
  if interCard S Y % 2 = 0 then 1 else -1

/-- Sum an integer list. -/
def sumInt : List Int → Int
  | [] => 0
  | z :: zs => z + sumInt zs

/-- Sum a natural-number list. -/
def sumNat : List Nat → Nat
  | [] => 0
  | z :: zs => z + sumNat zs

/-- Maximum of a natural-number list, with zero on the empty list. -/
def maxNatList : List Nat → Nat
  | [] => 0
  | z :: zs => Nat.max z (maxNatList zs)

/-- The complete `N = 8`, `m = 4` half slice. -/
def halfSlice : List (List Nat) := choose 8 4

/--
One representative from each complement-pair of middle-weight characters:
choose the representative containing coordinate zero.
-/
def middleRepresentatives : List (List Nat) :=
  halfSlice.filter fun Y => Y.contains 0

/--
All 128 characters of the even-parity effective span, represented uniquely by
binary vectors whose coordinate zero is fixed to zero.
-/
def effectiveRepresentatives : List (List Nat) :=
  powerset [1, 2, 3, 4, 5, 6, 7]

/-- The 127 nontrivial effective characters. -/
def nontrivialEffectiveRepresentatives : List (List Nat) :=
  effectiveRepresentatives.filter (fun Y => nonemptyList Y)

/-- Fixed-weight Walsh/Krawtchouk coefficient. -/
def walshCoefficient (Y : List Nat) : Int :=
  sumInt (halfSlice.map fun S => walshTerm S Y)

/-- Absolute Walsh coefficient. -/
def absWalsh (Y : List Nat) : Nat :=
  (walshCoefficient Y).natAbs

/-- Absolute mass contributed by the selected 35 effective characters. -/
def middleAbsoluteMass : Nat :=
  sumNat (middleRepresentatives.map absWalsh)

/-- Exact absolute mass over all 127 nontrivial effective characters. -/
def fullAbsoluteMass : Nat :=
  sumNat (nontrivialEffectiveRepresentatives.map absWalsh)

/-- Size of the fiber over one incidence-vector target. -/
def fiberSize (target : List Nat) : Nat :=
  (halfSlice.filter fun S => S == target).length

/-- Maximum realized-image fiber size. -/
def maxFiber : Nat :=
  maxNatList (halfSlice.map fiberSize)

/-- Source mass `M`. -/
def sourceMass : Nat := halfSlice.length

/-- Realized image size `L`; injectivity will identify it with `M`. -/
def realizedImageSize : Nat := halfSlice.length

/-- Effective even-parity target size `2^7`. -/
def effectiveTargetSize : Nat := 128

/-- Ambient binary target size `2^8`. -/
def ambientTargetSize : Nat := 256

/-- Every enumerated object is a distinct four-subset of eight coordinates. -/
def halfSliceShapeCheck : Bool :=
  halfSlice.length == 70 &&
  noDuplicates halfSlice &&
  halfSlice.all fun S =>
    S.length == 4 && noDuplicates S && S.all fun i => decide (i < 8)

/-- The 35 selected character supports are distinct middle-weight supports. -/
def representativeShapeCheck : Bool :=
  middleRepresentatives.length == 35 &&
  noDuplicates middleRepresentatives &&
  middleRepresentatives.all fun Y =>
    Y.length == 4 && Y.contains 0

/-- The coordinate-zero gauge gives exactly 128 distinct effective characters. -/
def effectiveRepresentativeShapeCheck : Bool :=
  effectiveRepresentatives.length == 128 &&
  nontrivialEffectiveRepresentatives.length == 127 &&
  noDuplicates effectiveRepresentatives &&
  effectiveRepresentatives.all fun Y =>
    Y.all fun i => decide (1 ≤ i ∧ i < 8)

/-- Every selected middle-weight character has Krawtchouk magnitude six. -/
def middleMagnitudeCheck : Bool :=
  middleRepresentatives.all fun Y => absWalsh Y == 6

/-- Every realized-image fiber is a singleton. -/
def singletonFiberCheck : Bool :=
  halfSlice.all fun target => fiberSize target == 1

theorem half_slice_shapes : halfSliceShapeCheck = true := by decide

theorem representative_shapes : representativeShapeCheck = true := by decide

theorem effective_representative_shapes :
    effectiveRepresentativeShapeCheck = true := by decide

theorem source_mass_exact : sourceMass = 70 := by decide

theorem realized_image_size_exact : realizedImageSize = 70 := by decide

theorem representative_count_exact : middleRepresentatives.length = 35 := by decide

theorem middle_walsh_magnitudes_exact : middleMagnitudeCheck = true := by decide

theorem middle_absolute_mass_exact : middleAbsoluteMass = 210 := by decide

theorem full_absolute_mass_exact : fullAbsoluteMass = 490 := by decide

theorem singleton_fibers : singletonFiberCheck = true := by decide

theorem max_fiber_exact : maxFiber = 1 := by decide

/-- Exact image-normalized Q equality: `maxFiber = M / L = 1`. -/
theorem image_normalized_q_exact :
    maxFiber * realizedImageSize = sourceMass := by decide

/-- The ambient/image discrepancy is bounded by the elementary factor `N+1=9`. -/
theorem ambient_image_gap_polynomial :
    ambientTargetSize ≤ 9 * realizedImageSize := by decide

/-- The effective/image discrepancy is bounded by the same elementary factor. -/
theorem effective_image_gap_polynomial :
    effectiveTargetSize ≤ 9 * realizedImageSize := by decide

/--
The selected effective characters alone force `kappa >= 4` in every inequality

`middleAbsoluteMass <= (kappa - 1) * sourceMass`.

The full nontrivial effective-dual mass can only be larger.
-/
theorem kappa_floor_of_middle_mass
    (kappa : Nat)
    (h : middleAbsoluteMass ≤ (kappa - 1) * sourceMass) :
    4 ≤ kappa := by
  rw [middle_absolute_mass_exact, source_mass_exact] at h
  omega

/-- The complete effective dual forces the exact finite floor `kappa >= 8`. -/
theorem kappa_floor_of_full_mass
    (kappa : Nat)
    (h : fullAbsoluteMass ≤ (kappa - 1) * sourceMass) :
    8 ≤ kappa := by
  rw [full_absolute_mass_exact, source_mass_exact] at h
  omega

/-- `kappa = 7` is falsified by the complete nontrivial effective dual. -/
theorem kappa_seven_fails :
    (7 - 1) * sourceMass < fullAbsoluteMass := by decide

/-- At `kappa = 8`, the full absolute mass saturates the finite inequality. -/
theorem kappa_eight_exact_balance :
    fullAbsoluteMass = (8 - 1) * sourceMass := by decide

/-- `kappa = 3` is already falsified by the selected character classes. -/
theorem kappa_three_fails :
    (3 - 1) * sourceMass < middleAbsoluteMass := by decide

end SidonEffectiveImage.HalfSliceFalsifier
