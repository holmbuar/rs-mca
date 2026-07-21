import AsymptoticSpine.PrimitiveBoolean
import M31QRootedShell.Deployed

/-!
# Image-compensated effective MI+MA on one exact M31 primitive leaf

This stdlib-only module restates the eight-point Mersenne-31 fixed-weight
profile used by the scoped C9 row-sharp packet, without importing any open-PR
module.  It proves the exact C1 owner complement, the 70/69 full-slice
source/image census, the nonempty 64-support post-C1 residual, and an explicit
inverse for three moment-column differences.  The inverse is the finite
certificate that the effective difference span is the full ambient `F_p^3`.

The effective characters are split nonvacuously by the first ambient
coefficient: `a₁ = 0` is minor (excluding the trivial character), and `a₁ ≠ 0`
is major.  Because the effective span is full, the certified lift of each
minor character is the identity ambient lift.  The exact character counts are
`p^2-1` and `p^3-p^2`.

The final theorems are cleared-denominator arithmetic statements.  Given the
literal triangle bounds for the two absolute aggregate numerators, they prove

* `(L/A_eff) C_min ≤ 1`,
* `(L/A_eff) C_maj ≤ 69`, and
* `(L/A_eff) (1 + C_min + C_maj) ≤ 69`,

with `M=70`, `L=69`, and `A_eff=p^3`.  These are support-prefix aggregate
bounds.  The module does not manufacture a slope map, a row-wide owner atlas,
profile add-back, or an adjacent-row certificate.
-/

namespace SidonEffectiveImage.M31CompensatedAggregates

open AsymptoticSpine

abbrev Support := Vector Bool 8

/-- Three power-sum prefix coordinates, represented by canonical residues. -/
structure PrefixKey where
  p1 : Nat
  p2 : Nat
  p3 : Nat
  deriving Repr, BEq, DecidableEq

/-- Ambient/effective character coordinates, represented by residues. -/
structure CharacterRep where
  a1 : Nat
  a2 : Nat
  a3 : Nat
  deriving Repr, BEq, DecidableEq

/-- Three-coordinate vectors for the explicit span certificate. -/
structure Vec3 where
  x : Nat
  y : Nat
  z : Nat
  deriving Repr, BEq, DecidableEq

/-- A row-major `3 × 3` matrix over the represented prime field. -/
structure Mat3 where
  a00 : Nat
  a01 : Nat
  a02 : Nat
  a10 : Nat
  a11 : Nat
  a12 : Nat
  a20 : Nat
  a21 : Nat
  a22 : Nat
  deriving Repr, BEq, DecidableEq

/-- Exact Mersenne-31 coefficient field used by the deployed auxiliary row. -/
def fieldPrime : Nat := M31QRootedShell.Deployed.pM31

/-- Eight actual roots of `T_(2^21)` in the deployed Mersenne-31 domain. -/
def domain : List Nat :=
  [ 434373082, 614288294, 1713110565, 1533195353
  , 1984437538, 380812851, 163046109, 1766670796 ]

/-- Duplicate-free executable list predicate. -/
def noDuplicates [BEq α] : List α → Bool
  | [] => true
  | x :: xs => !xs.contains x && noDuplicates xs

/-- `T_(2n)(x)=2T_n(x)^2-1`, evaluated modulo the Mersenne prime. -/
def chebyshevDouble (x : Nat) : Nat :=
  (2 * (x % fieldPrime) * (x % fieldPrime) + (fieldPrime - 1)) % fieldPrime

/-- Evaluate `T_(2^e)` by repeated doubling. -/
def chebyshevPowTwo : Nat → Nat → Nat
  | 0, x => x % fieldPrime
  | e + 1, x => chebyshevPowTwo e (chebyshevDouble x)

/-- Boolean support vector encoded by an eight-bit mask. -/
def supportVector (mask : Nat) : Support :=
  Vector.ofFn fun i => Nat.testBit mask i.val

/-- Complete Boolean cube and complete weight-four slice. -/
def allPoints : List Support :=
  (List.range 256).map supportVector

def fullPoints : List Support :=
  allPoints.filter fun x => decide (boolWeight x = 4)

/-- Sum the selected domain values to the `e`-th power modulo the row prime. -/
def sumPowerMod (e : Nat) (x : Support) : Nat :=
  (x.toList.zip domain).foldl
    (fun acc pair =>
      if pair.1 then (acc + pair.2 ^ e % fieldPrime) % fieldPrime else acc)
    0

/-- The active three-coordinate prefix key. -/
def prefixKey (x : Support) : PrefixKey :=
  { p1 := sumPowerMod 1 x
  , p2 := sumPowerMod 2 x
  , p3 := sumPowerMod 3 x }

/-- Exact C1 complete-fiber supports for the antipodal quotient `x ↦ x^2`. -/
def c1OwnedSupports : List Support :=
  [ supportVector 15, supportVector 85, supportVector 165
  , supportVector 90, supportVector 170, supportVector 240 ]

def c1Owned (x : Support) : Bool :=
  c1OwnedSupports.contains x

/-- The literal post-C1 residual inside the complete weight-four slice. -/
def residualPoints : List Support :=
  fullPoints.filter fun x => !c1Owned x

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem fullPoints_complete :
    ∀ x : Support, boolWeight x = 4 ↔ x ∈ fullPoints := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem fullPoints_nodup : fullPoints.Nodup := by decide

/-- Complete fixed-weight family on the eight moving coordinates. -/
def fullFamily : BoolFamily where
  dimension := 8
  weight := 4
  points := fullPoints
  points_nodup := fullPoints_nodup
  points_fixed := fun x hx => (fullPoints_complete x).mpr hx

/-- Scoped exact post-C1 primitive leaf. -/
def leaf : PrimitiveBooleanLeaf PrefixKey where
  full := fullFamily
  full_complete := fullPoints_complete
  residual := residualPoints
  residual_sublist := List.filter_sublist
  prefixKey := prefixKey

/-- Local copy of the exact pre-C9 constructor grammar.  Only C1 is nonempty in
this scoped profile. -/
inductive ScopedPreC9Owner where
  | c1 | c2 | c3 | c4 | c5 | c6 | c7 | c8
  deriving Repr, BEq, DecidableEq

/-- Owner function with a generic C1 label. -/
def earlierOwner {Owner : Type} (c1 : Owner) (x : Support) : Option Owner :=
  if c1Owned x then some c1 else none

def scopedEarlierOwner : Support → Option ScopedPreC9Owner :=
  earlierOwner .c1

/-- Exact owner-complement predicate required of a routed primitive leaf. -/
def IsExactOwnerComplement {Owner : Type} [DecidableEq Owner]
    (owner : Support → Option Owner) : Prop :=
  ∀ x : Support,
    x ∈ leaf.residual ↔ x ∈ leaf.full.points ∧ owner x = none

/-- The displayed residual is exactly the complement of the explicit C1 owner
inside the complete fixed-weight slice. -/
theorem residual_exact {Owner : Type} [DecidableEq Owner] (c1 : Owner) :
    IsExactOwnerComplement (earlierOwner c1) := by
  intro x
  show x ∈ residualPoints ↔ x ∈ fullPoints ∧ earlierOwner c1 x = none
  unfold residualPoints earlierOwner
  simp only [List.mem_filter]
  constructor
  · rintro ⟨hfull, hres⟩
    refine ⟨hfull, ?_⟩
    cases hcase : c1Owned x
    · rfl
    · rw [hcase] at hres
      exact absurd hres (by decide)
  · rintro ⟨hfull, hnone⟩
    refine ⟨hfull, ?_⟩
    cases hcase : c1Owned x
    · rfl
    · rw [hcase] at hnone
      simp at hnone

/-- Concrete C1--C8 owner-complement witness for this scoped profile. -/
theorem scoped_residual_exact :
    IsExactOwnerComplement scopedEarlierOwner := by
  unfold scopedEarlierOwner
  exact residual_exact ScopedPreC9Owner.c1

/-- Full and residual realized-key lists. -/
def fullKeyList : List PrefixKey := fullPoints.map prefixKey
def fullImage : List PrefixKey := fullKeyList.eraseDups
def residualKeyList : List PrefixKey := residualPoints.map prefixKey
def residualImage : List PrefixKey := residualKeyList.eraseDups

/-- One explicit support and key surviving the displayed earlier owner. -/
def selectedSupport : Support := supportVector 51
def selectedKey : PrefixKey :=
  { p1 := 1266428118, p2 := 2, p3 := 458186840 }

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem domain_nodup : noDuplicates domain = true := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem domain_points_are_deployed_roots :
    domain.all (fun x => chebyshevPowTwo 21 x == 0) = true := by decide

theorem antipodal_pairs_exact :
    (434373082 + 1713110565) % fieldPrime = 0 ∧
    (614288294 + 1533195353) % fieldPrime = 0 ∧
    (1984437538 + 163046109) % fieldPrime = 0 ∧
    (380812851 + 1766670796) % fieldPrime = 0 := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem t4_fibers_exact :
    (domain.take 4).all (fun x => chebyshevPowTwo 2 x == 1884637334) = true ∧
    (domain.drop 4).all (fun x => chebyshevPowTwo 2 x == 51044589) = true := by
  decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem full_slice_card : fullPoints.length = 70 := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem full_image_card : fullImage.length = 69 := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem c1_owned_support_card : c1OwnedSupports.length = 6 := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem residual_slice_card : residualPoints.length = 64 := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem residual_prefix_injective : residualKeyList.Nodup := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem residual_image_card : residualImage.length = 64 := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem selected_key_exact : prefixKey selectedSupport = selectedKey := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem selected_survives : selectedSupport ∈ leaf.residual := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem selected_residual_prefix_singleton :
    residualPrefixFiber leaf selectedKey = [selectedSupport] := by decide

theorem selected_not_earlier : scopedEarlierOwner selectedSupport = none := by
  exact ((scoped_residual_exact selectedSupport).mp selected_survives).2

/-! ## Explicit full-effective-span certificate -/

/-- Coordinatewise subtraction modulo the deployed prime. -/
def subMod (a b : Nat) : Nat := (a + fieldPrime - (b % fieldPrime)) % fieldPrime

def subVec (a b : Vec3) : Vec3 :=
  { x := subMod a.x b.x
  , y := subMod a.y b.y
  , z := subMod a.z b.z }

/-- Moment column `g(t)=(t,t^2,t^3)`. -/
def momentColumn (t : Nat) : Vec3 :=
  { x := t % fieldPrime
  , y := (t ^ 2) % fieldPrime
  , z := (t ^ 3) % fieldPrime }

/-- The first three differences from the first domain column. -/
def basis1 : Vec3 := subVec (momentColumn 614288294) (momentColumn 434373082)
def basis2 : Vec3 := subVec (momentColumn 1713110565) (momentColumn 434373082)
def basis3 : Vec3 := subVec (momentColumn 1533195353) (momentColumn 434373082)

/-- Matrix whose columns are the three displayed moment differences. -/
def basisMatrix : Mat3 :=
  { a00 := basis1.x, a01 := basis2.x, a02 := basis3.x
  , a10 := basis1.y, a11 := basis2.y, a12 := basis3.y
  , a20 := basis1.z, a21 := basis2.z, a22 := basis3.z }

/-- Explicit inverse of `basisMatrix` modulo the deployed prime. -/
def basisInverse : Mat3 :=
  { a00 := 1072773236, a01 := 2033842811, a02 := 1680180098
  , a10 := 970446555,  a11 := 113640836,  a12 := 1821586645
  , a20 := 1074710411, a21 := 2033842811, a22 := 467303549 }

/-- Multiply two represented `3 × 3` matrices modulo the deployed prime. -/
def matMul (a b : Mat3) : Mat3 :=
  { a00 := (a.a00*b.a00 + a.a01*b.a10 + a.a02*b.a20) % fieldPrime
  , a01 := (a.a00*b.a01 + a.a01*b.a11 + a.a02*b.a21) % fieldPrime
  , a02 := (a.a00*b.a02 + a.a01*b.a12 + a.a02*b.a22) % fieldPrime
  , a10 := (a.a10*b.a00 + a.a11*b.a10 + a.a12*b.a20) % fieldPrime
  , a11 := (a.a10*b.a01 + a.a11*b.a11 + a.a12*b.a21) % fieldPrime
  , a12 := (a.a10*b.a02 + a.a11*b.a12 + a.a12*b.a22) % fieldPrime
  , a20 := (a.a20*b.a00 + a.a21*b.a10 + a.a22*b.a20) % fieldPrime
  , a21 := (a.a20*b.a01 + a.a21*b.a11 + a.a22*b.a21) % fieldPrime
  , a22 := (a.a20*b.a02 + a.a21*b.a12 + a.a22*b.a22) % fieldPrime }

def identityMatrix : Mat3 :=
  { a00 := 1, a01 := 0, a02 := 0
  , a10 := 0, a11 := 1, a12 := 0
  , a20 := 0, a21 := 0, a22 := 1 }

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem basis_matrix_exact :
    basisMatrix =
      { a00 := 179915212, a01 := 1278737483, a02 := 1098822271
      , a10 := 887084793, a11 := 0,          a12 := 887084793
      , a20 := 1154236547, a21 := 503705255, a22 := 1496952355 } := by
  decide

/-- Two-sided inverse certificate; mathematically this proves that the effective
difference span is all of the ambient three-dimensional space. -/
theorem basis_inverse_certificate :
    matMul basisMatrix basisInverse = identityMatrix ∧
    matMul basisInverse basisMatrix = identityMatrix := by decide

/-! ## Nonvacuous certified effective major/minor partition -/

/-- The trivial ambient/effective character. -/
def zeroCharacter : CharacterRep := { a1 := 0, a2 := 0, a3 := 0 }

/-- Minor characters have first coefficient zero, excluding the trivial one. -/
def IsMinor (a : CharacterRep) : Prop :=
  a.a1 = 0 ∧ a ≠ zeroCharacter

/-- Major characters have nonzero first coefficient. -/
def IsMajor (a : CharacterRep) : Prop :=
  a.a1 ≠ 0

/-- Every nontrivial character belongs to one of the two displayed parts. -/
theorem character_partition (a : CharacterRep) (h : a ≠ zeroCharacter) :
    IsMinor a ∨ IsMajor a := by
  by_cases h1 : a.a1 = 0
  · exact Or.inl ⟨h1, h⟩
  · exact Or.inr h1

/-- The displayed minor and major parts are disjoint. -/
theorem character_partition_disjoint (a : CharacterRep) :
    ¬ (IsMinor a ∧ IsMajor a) := by
  intro h
  exact h.2 h.1.1

/-- Identity ambient lift, valid because `basis_inverse_certificate` certifies
that the effective difference span is the full ambient space. -/
def certifiedAmbientLift (a : CharacterRep) : CharacterRep := a

@[simp] theorem certifiedAmbientLift_eq (a : CharacterRep) :
    certifiedAmbientLift a = a := rfl

/-- Explicit witnesses that both parts of the partition are nonempty. -/
def minorWitness : CharacterRep := { a1 := 0, a2 := 1, a3 := 0 }
def majorWitness : CharacterRep := { a1 := 1, a2 := 0, a3 := 0 }

theorem partition_nonempty :
    IsMinor minorWitness ∧ IsMajor majorWitness := by decide

/-! ## Exact image-compensated aggregate arithmetic -/

/-- Full-slice mass and realized-image size. -/
def sourceMass : Nat := 70
def realizedImageSize : Nat := 69

/-- Effective group size certified by the full-span inverse. -/
def effectiveSize : Nat := fieldPrime ^ 3

/-- Exact counts for the displayed split of the nontrivial effective dual. -/
def minorCharacterCount : Nat := fieldPrime ^ 2 - 1
def majorCharacterCount : Nat := effectiveSize - fieldPrime ^ 2

/-- Exact finite loss constants in cleared-denominator form. -/
def minorAggregateLoss : Nat := 1
def majorAggregateLoss : Nat := 69
def fullAggregateLoss : Nat := 69

/-- The literal support/image constants agree with the executable leaf census. -/
theorem source_image_constants_exact :
    sourceMass = fullPoints.length ∧
    realizedImageSize = fullImage.length := by decide

/-- The displayed minor/major counts partition every nontrivial effective
character exactly. -/
theorem character_count_partition :
    1 + minorCharacterCount + majorCharacterCount = effectiveSize := by decide

/-- Count-level compensated minor bound:
`L (p^2-1) ≤ A_eff`. -/
theorem compensated_minor_count :
    realizedImageSize * minorCharacterCount ≤
      minorAggregateLoss * effectiveSize := by decide

/-- Count-level compensated major bound:
`L (p^3-p^2) ≤ 69 A_eff`. -/
theorem compensated_major_count :
    realizedImageSize * majorCharacterCount ≤
      majorAggregateLoss * effectiveSize := by decide

/-- Given the literal triangle estimate for the absolute minor aggregate
numerator, the image-compensated normalized minor loss is at most one. -/
theorem compensated_minor_of_triangle
    (minorMass : Nat)
    (hminor : minorMass ≤ minorCharacterCount * sourceMass) :
    realizedImageSize * minorMass ≤
      minorAggregateLoss * effectiveSize * sourceMass := by
  calc
    realizedImageSize * minorMass
        ≤ realizedImageSize * (minorCharacterCount * sourceMass) :=
          Nat.mul_le_mul_left realizedImageSize hminor
    _ = (realizedImageSize * minorCharacterCount) * sourceMass := by
          simp [Nat.mul_assoc]
    _ ≤ (minorAggregateLoss * effectiveSize) * sourceMass :=
          Nat.mul_le_mul_right sourceMass compensated_minor_count
    _ = minorAggregateLoss * effectiveSize * sourceMass := by
          simp [Nat.mul_assoc]

/-- Given the literal triangle estimate for the absolute major aggregate
numerator, the image-compensated normalized major loss is at most 69. -/
theorem compensated_major_of_triangle
    (majorMass : Nat)
    (hmajor : majorMass ≤ majorCharacterCount * sourceMass) :
    realizedImageSize * majorMass ≤
      majorAggregateLoss * effectiveSize * sourceMass := by
  calc
    realizedImageSize * majorMass
        ≤ realizedImageSize * (majorCharacterCount * sourceMass) :=
          Nat.mul_le_mul_left realizedImageSize hmajor
    _ = (realizedImageSize * majorCharacterCount) * sourceMass := by
          simp [Nat.mul_assoc]
    _ ≤ (majorAggregateLoss * effectiveSize) * sourceMass :=
          Nat.mul_le_mul_right sourceMass compensated_major_count
    _ = majorAggregateLoss * effectiveSize * sourceMass := by
          simp [Nat.mul_assoc]

/-- Combining the trivial character with the two real absolute aggregates gives
the exact image-compensated Fourier triangle multiplier 69. -/
theorem compensated_full_of_triangle
    (minorMass majorMass : Nat)
    (hminor : minorMass ≤ minorCharacterCount * sourceMass)
    (hmajor : majorMass ≤ majorCharacterCount * sourceMass) :
    realizedImageSize * (sourceMass + minorMass + majorMass) ≤
      fullAggregateLoss * effectiveSize * sourceMass := by
  have hsum :
      sourceMass + minorMass + majorMass ≤
        sourceMass + minorCharacterCount * sourceMass +
          majorCharacterCount * sourceMass :=
    Nat.add_le_add (Nat.add_le_add (Nat.le_refl sourceMass) hminor) hmajor
  have hinside :
      sourceMass + minorMass + majorMass ≤ effectiveSize * sourceMass := by
    calc
      sourceMass + minorMass + majorMass
          ≤ sourceMass + minorCharacterCount * sourceMass +
              majorCharacterCount * sourceMass := hsum
      _ = (1 + minorCharacterCount + majorCharacterCount) * sourceMass := by
            simp [Nat.add_mul, Nat.add_assoc]
      _ = effectiveSize * sourceMass := by
            rw [character_count_partition]
  calc
    realizedImageSize * (sourceMass + minorMass + majorMass)
        ≤ realizedImageSize * (effectiveSize * sourceMass) :=
          Nat.mul_le_mul_left realizedImageSize hinside
    _ = fullAggregateLoss * effectiveSize * sourceMass := by
          simp [realizedImageSize, fullAggregateLoss, Nat.mul_assoc]

/-- Exact deployed constants retained as separate row data; no row charge is
claimed by the aggregate theorem. -/
theorem deployed_constants :
    fieldPrime = 2147483647 ∧
    M31QRootedShell.Deployed.w = 67447 ∧
    M31QRootedShell.Deployed.listM = 981129 ∧
    M31QRootedShell.Deployed.Bstar = 16777215 := by decide

#print axioms residual_exact
#print axioms scoped_residual_exact
#print axioms domain_points_are_deployed_roots
#print axioms antipodal_pairs_exact
#print axioms t4_fibers_exact
#print axioms full_slice_card
#print axioms full_image_card
#print axioms residual_slice_card
#print axioms residual_prefix_injective
#print axioms residual_image_card
#print axioms selected_key_exact
#print axioms selected_residual_prefix_singleton
#print axioms selected_not_earlier
#print axioms basis_matrix_exact
#print axioms basis_inverse_certificate
#print axioms character_partition
#print axioms character_partition_disjoint
#print axioms certifiedAmbientLift_eq
#print axioms partition_nonempty
#print axioms source_image_constants_exact
#print axioms character_count_partition
#print axioms compensated_minor_count
#print axioms compensated_major_count
#print axioms compensated_minor_of_triangle
#print axioms compensated_major_of_triangle
#print axioms compensated_full_of_triangle
#print axioms deployed_constants

end SidonEffectiveImage.M31CompensatedAggregates
