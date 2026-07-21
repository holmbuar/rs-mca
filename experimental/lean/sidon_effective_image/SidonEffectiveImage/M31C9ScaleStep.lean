import AsymptoticSpine.PrimitiveBoolean
import M31QRootedShell.Deployed

/-!
# M31 C9 scale step: exact residual noninjectivity at sixteen roots

This stdlib-only module moves the eight-root calibration of upstream PR #1027
to sixteen actual roots of `T_(2^21)` over `F_(2^31-1)`, arranged as four
complete `T_4` blocks. It kernel-checks two distinct weight-eight supports
which survive the exact C1 antipodal-quotient deletion and have the same first
three power sums. It also checks that no smaller mask survives, so the first
residual key already grows.

The complete 12,870-support fiber census is replayed independently by the
packet's stdlib verifier. This module proves the statement-changing witness,
not a list or MCA numerator theorem.
-/

namespace SidonEffectiveImage.M31C9ScaleStep

open AsymptoticSpine

set_option maxRecDepth 4000000
set_option maxHeartbeats 0

abbrev Support := Nat

structure PrefixKey where
  p1 : Nat
  p2 : Nat
  p3 : Nat
  deriving Repr, BEq, DecidableEq

def fieldPrime : Nat := M31QRootedShell.Deployed.pM31
def deployedPrefixDepth : Nat := M31QRootedShell.Deployed.w
def deployedBudget : Nat := M31QRootedShell.Deployed.Bstar
def deployedLength : Nat := 2 ^ 21
def deployedComplementWeight : Nat := M31QRootedShell.Deployed.listM
def activeWeight : Nat := 8
def fixedOutsideWeight : Nat := deployedComplementWeight - activeWeight
def outsideAvailable : Nat := deployedLength - 16

structure Fp2 where
  re : Nat
  im : Nat
  deriving Repr, BEq, DecidableEq

def fp2One : Fp2 := { re := 1, im := 0 }

def fp2Mul (a b : Fp2) : Fp2 :=
  { re := ((a.re * b.re) % fieldPrime + fieldPrime -
      (a.im * b.im) % fieldPrime) % fieldPrime
  , im := ((a.re * b.im) % fieldPrime +
      (a.im * b.re) % fieldPrime) % fieldPrime }

def fp2Conj (a : Fp2) : Fp2 :=
  { re := a.re % fieldPrime
  , im := (fieldPrime - a.im % fieldPrime) % fieldPrime }

def fp2PowTwo : Nat → Fp2 → Fp2
  | 0, u => u
  | e + 1, u => fp2PowTwo e (fp2Mul u u)

def fp2PowSmall (a : Fp2) : Nat → Fp2
  | 0 => fp2One
  | e + 1 => fp2Mul (fp2PowSmall a e) a

def normOneGenerator : Fp2 :=
  { re := 1717986917, im := 1288490189 }

def blockBases : List Nat := [256, 768, 1280, 1792]
def quarterTurn : Fp2 := fp2PowTwo 29 normOneGenerator
def quarterShifts : List Fp2 :=
  (List.range 4).map (fp2PowSmall quarterTurn)

def derivedBlock (base : Nat) : List Nat :=
  let u := fp2PowSmall normOneGenerator base
  quarterShifts.map fun shift => (fp2Mul u shift).re

def derivedDomain : List Nat := blockBases.flatMap derivedBlock

def domain : List Nat :=
  [ 434373082, 614288294, 1713110565, 1533195353
  , 1984437538, 380812851, 163046109, 1766670796
  , 1244279234, 907334541, 903204413, 1240149106
  , 2066813671, 1590029158, 80669976, 557454489 ]

def noDuplicates [BEq α] : List α → Bool
  | [] => true
  | x :: xs => !xs.contains x && noDuplicates xs

def chebyshevDouble (x : Nat) : Nat :=
  (2 * (x % fieldPrime) * (x % fieldPrime) + (fieldPrime - 1)) % fieldPrime

def chebyshevPowTwo : Nat → Nat → Nat
  | 0, x => x % fieldPrime
  | e + 1, x => chebyshevPowTwo e (chebyshevDouble x)

def supportVector (mask : Support) : Vector Bool 16 :=
  Vector.ofFn fun i => Nat.testBit mask i.val

def maskWeight (mask : Support) : Nat :=
  boolWeight (supportVector mask)

def isFullSupport (mask : Support) : Bool :=
  decide (mask < 2 ^ 16) && decide (maskWeight mask = activeWeight)

def IsFullSupport (mask : Support) : Prop :=
  isFullSupport mask = true

def sumPowerMod (e : Nat) (mask : Support) : Nat :=
  ((List.range 16).zip domain).foldl
    (fun acc pair =>
      if Nat.testBit mask pair.1
      then (acc + pair.2 ^ e % fieldPrime) % fieldPrime
      else acc)
    0

def prefixKey (mask : Support) : PrefixKey :=
  { p1 := sumPowerMod 1 mask
  , p2 := sumPowerMod 2 mask
  , p3 := sumPowerMod 3 mask }

def sameBit (mask : Support) (i j : Nat) : Bool :=
  Nat.testBit mask i == Nat.testBit mask j

def c1Owned (mask : Support) : Bool :=
  sameBit mask 0 2 &&
  sameBit mask 1 3 &&
  sameBit mask 4 6 &&
  sameBit mask 5 7 &&
  sameBit mask 8 10 &&
  sameBit mask 9 11 &&
  sameBit mask 12 14 &&
  sameBit mask 13 15

def isResidual (mask : Support) : Bool :=
  isFullSupport mask && !c1Owned mask

def IsResidual (mask : Support) : Prop :=
  isResidual mask = true

inductive ScopedPreC9Owner where
  | c1 | c2 | c3 | c4 | c5 | c6 | c7 | c8
  deriving Repr, BEq, DecidableEq

def earlierOwner {Owner : Type} (c1 : Owner) (mask : Support) : Option Owner :=
  if c1Owned mask then some c1 else none

def scopedEarlierOwner : Support → Option ScopedPreC9Owner :=
  earlierOwner .c1

def IsExactOwnerComplement {Owner : Type} [DecidableEq Owner]
    (owner : Support → Option Owner) : Prop :=
  ∀ mask : Support,
    IsResidual mask ↔ IsFullSupport mask ∧ owner mask = none

theorem residual_exact {Owner : Type} [DecidableEq Owner] (c1 : Owner) :
    IsExactOwnerComplement (earlierOwner c1) := by
  intro mask
  unfold IsResidual isResidual IsFullSupport earlierOwner
  cases hfull : isFullSupport mask <;>
    cases hown : c1Owned mask <;> simp [hfull, hown]

theorem scoped_residual_exact :
    IsExactOwnerComplement scopedEarlierOwner := by
  unfold scopedEarlierOwner
  exact residual_exact ScopedPreC9Owner.c1

def firstGrowthSupport : Support := 383
def firstGrowthMate : Support := 61808
def firstGrowthKey : PrefixKey :=
  { p1 := 1625092085, p2 := 1544193364, p3 := 2053033192 }

def block0Mask : Support := 15
def block3Mask : Support := 61440
def t4BlockKey : PrefixKey := { p1 := 0, p2 := 2, p3 := 0 }

def selectedIndices (mask : Support) : List Nat :=
  (List.range 16).filter fun i => Nat.testBit mask i

def earlierResidualMasks : List Support :=
  (List.range firstGrowthSupport).filter isResidual

def ResidualPrefixInjective : Prop :=
  ∀ a b : Support,
    IsResidual a → IsResidual b → prefixKey a = prefixKey b → a = b

theorem generator_norm_one :
    fp2Mul normOneGenerator (fp2Conj normOneGenerator) = fp2One := by decide

theorem generator_half_order :
    fp2PowTwo 30 normOneGenerator =
      ({ re := fieldPrime - 1, im := 0 } : Fp2) := by decide

theorem generator_full_order :
    fp2PowTwo 31 normOneGenerator = fp2One := by decide

theorem domain_derived_exact : derivedDomain = domain := by decide

theorem domain_nodup : noDuplicates domain = true := by decide

theorem domain_points_are_deployed_roots :
    domain.all (fun x => chebyshevPowTwo 21 x == 0) = true := by decide

theorem antipodal_pairs_exact :
    (434373082 + 1713110565) % fieldPrime = 0 ∧
    (614288294 + 1533195353) % fieldPrime = 0 ∧
    (1984437538 + 163046109) % fieldPrime = 0 ∧
    (380812851 + 1766670796) % fieldPrime = 0 ∧
    (1244279234 + 903204413) % fieldPrime = 0 ∧
    (907334541 + 1240149106) % fieldPrime = 0 ∧
    (2066813671 + 80669976) % fieldPrime = 0 ∧
    (1590029158 + 557454489) % fieldPrime = 0 := by decide

theorem t4_fibers_exact :
    (domain.take 4).all (fun x => chebyshevPowTwo 2 x == 1884637334) = true ∧
    ((domain.drop 4).take 4).all
      (fun x => chebyshevPowTwo 2 x == 51044589) = true ∧
    ((domain.drop 8).take 4).all
      (fun x => chebyshevPowTwo 2 x == 1916935773) = true ∧
    (domain.drop 12).all
      (fun x => chebyshevPowTwo 2 x == 116752674) = true := by decide

theorem firstGrowth_indices_exact :
    selectedIndices firstGrowthSupport = [0, 1, 2, 3, 4, 5, 6, 8] := by decide

theorem firstGrowthMate_indices_exact :
    selectedIndices firstGrowthMate = [4, 5, 6, 8, 12, 13, 14, 15] := by decide

theorem block0_key_exact : prefixKey block0Mask = t4BlockKey := by decide
theorem block3_key_exact : prefixKey block3Mask = t4BlockKey := by decide

theorem firstGrowth_full : IsFullSupport firstGrowthSupport := by decide
theorem firstGrowthMate_full : IsFullSupport firstGrowthMate := by decide

theorem firstGrowth_not_c1Owned :
    c1Owned firstGrowthSupport = false := by decide

theorem firstGrowthMate_not_c1Owned :
    c1Owned firstGrowthMate = false := by decide

theorem firstGrowth_survives : IsResidual firstGrowthSupport := by decide

theorem firstGrowthMate_survives : IsResidual firstGrowthMate := by decide

theorem firstGrowth_key_exact :
    prefixKey firstGrowthSupport = firstGrowthKey := by decide

theorem firstGrowthMate_key_exact :
    prefixKey firstGrowthMate = firstGrowthKey := by decide

theorem firstGrowth_keys_equal :
    prefixKey firstGrowthSupport = prefixKey firstGrowthMate := by
  rw [firstGrowth_key_exact, firstGrowthMate_key_exact]

theorem firstGrowth_distinct :
    firstGrowthSupport ≠ firstGrowthMate := by decide

/-- Exact ascending-order certificate: no smaller mask is a residual support. -/
theorem no_earlier_residual_masks : earlierResidualMasks = [] := by decide

theorem first_growth_order_certificate :
    earlierResidualMasks = [] ∧ IsResidual firstGrowthSupport :=
  ⟨no_earlier_residual_masks, firstGrowth_survives⟩

/-- The exact C1-complement residual prefix map is not injective. -/
theorem scale_step_not_injective : ¬ ResidualPrefixInjective := by
  intro hinj
  have heq := hinj firstGrowthSupport firstGrowthMate
    firstGrowth_survives firstGrowthMate_survives firstGrowth_keys_equal
  exact firstGrowth_distinct heq

/-- Two explicit distinct residual witnesses occupy one prefix key. -/
theorem scale_step_fiber_floor_two :
    ∃ a b : Support,
      a ≠ b ∧ IsResidual a ∧ IsResidual b ∧ prefixKey a = prefixKey b := by
  exact ⟨firstGrowthSupport, firstGrowthMate, firstGrowth_distinct,
    firstGrowth_survives, firstGrowthMate_survives, firstGrowth_keys_equal⟩

theorem deployed_dimensions :
    deployedPrefixDepth = 67447 ∧
    deployedComplementWeight = 981129 ∧
    activeWeight = 8 ∧
    fixedOutsideWeight = 981121 ∧
    outsideAvailable = 2097136 ∧
    fixedOutsideWeight ≤ outsideAvailable ∧
    3 ≤ deployedPrefixDepth := by decide

theorem loss_two_fits_deployed_budget : 2 ≤ deployedBudget := by decide

#print axioms residual_exact
#print axioms scoped_residual_exact
#print axioms generator_norm_one
#print axioms generator_half_order
#print axioms generator_full_order
#print axioms domain_derived_exact
#print axioms domain_points_are_deployed_roots
#print axioms antipodal_pairs_exact
#print axioms t4_fibers_exact
#print axioms block0_key_exact
#print axioms block3_key_exact
#print axioms firstGrowth_survives
#print axioms firstGrowthMate_survives
#print axioms firstGrowth_key_exact
#print axioms firstGrowthMate_key_exact
#print axioms firstGrowth_keys_equal
#print axioms firstGrowth_distinct
#print axioms no_earlier_residual_masks
#print axioms first_growth_order_certificate
#print axioms scale_step_not_injective
#print axioms scale_step_fiber_floor_two
#print axioms deployed_dimensions
#print axioms loss_two_fits_deployed_budget

end SidonEffectiveImage.M31C9ScaleStep
