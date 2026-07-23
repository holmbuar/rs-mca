import Std

set_option maxRecDepth 1000000
set_option maxHeartbeats 0

/-!
# M31 quotient-band witnesses

This stdlib-only module certifies the finite premises of
`m31_quotient_band_swap_census_t16_mixing.md`.

The kernel checks the pinned quotient domain, the fourteen intact `T_64`
classes, the exact seven-class shell census, the class-locator
constant-difference premise, one direct deficiency-192 locator comparison,
the exact off-lattice `T_16` mixing pair, and the deployed integer arithmetic.

The general polynomial degree argument transferring the constant-difference
premise to all 3,432 supports is stated and audited in the note and in
`CORRESPONDENCE.md`; this module certifies every finite premise used there.
-/

namespace M31QuotientBandMixing.Witnesses

def fieldPrime : Nat := 2 ^ 31 - 1
def monicT2048Scale : Nat := 1073741824

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

def normOneGenerator : Fp2 :=
  { re := 1717986917, im := 1288490189 }

def quotientBase : Fp2 := fp2PowTwo 19 normOneGenerator
def quotientStep : Fp2 := fp2Mul quotientBase quotientBase

def iterateMul : Nat → Fp2 → Fp2 → List Fp2
  | 0, _, _ => []
  | n + 1, u, step => u :: iterateMul n (fp2Mul u step) step

def quotientUnits : List Fp2 :=
  iterateMul 1024 quotientBase quotientStep

def oddReps : List Nat :=
  (List.range 1024).map fun j => 2 * j + 1

def quotientLabels : List Nat :=
  quotientUnits.map fun u => (monicT2048Scale * u.re) % fieldPrime

def labelOfRep (r : Nat) : Nat :=
  quotientLabels.getD ((r - 1) / 2) 0

def noDuplicates [BEq α] : List α → Bool
  | [] => true
  | x :: xs => xs.all (fun y => !(y == x)) && noDuplicates xs

def chebyshevDouble (x : Nat) : Nat :=
  (2 * (x % fieldPrime) * (x % fieldPrime) + (fieldPrime - 1)) % fieldPrime

def chebyshevPowTwo : Nat → Nat → Nat
  | 0, x => x % fieldPrime
  | e + 1, x => chebyshevPowTwo e (chebyshevDouble x)

def puncturedReps : List Nat :=
  oddReps.filter fun r => !(r == 1) && !(r == 3)

def puncturedLabels : List Nat :=
  puncturedReps.map labelOfRep

def blockReps64 (a : Nat) : List Nat :=
  oddReps.filter fun r =>
    (r % 64 == a) || (r % 64 == 64 - a)

def intactClasses : List Nat :=
  [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]

def anchorClasses : List Nat :=
  [5, 7, 9, 11, 13, 15, 17]

def core31 : List Nat :=
  [63, 65, 127, 129, 191, 193, 255, 257, 319, 321, 383, 385, 447, 449, 511, 513, 575, 577, 639, 641, 703, 705, 767, 769, 831, 833, 895, 897, 959, 961, 1023]

def addPoly : List Nat → List Nat → List Nat
  | [], ys => ys.map fun y => y % fieldPrime
  | xs, [] => xs.map fun x => x % fieldPrime
  | x :: xs, y :: ys =>
      ((x + y) % fieldPrime) :: addPoly xs ys

def polyMulLinear (root : Nat) (poly : List Nat) : List Nat :=
  let negRoot := (fieldPrime - root % fieldPrime) % fieldPrime
  addPoly
    (poly.map fun coefficient => (negRoot * coefficient) % fieldPrime)
    (0 :: poly)

def locatorFromReps (reps : List Nat) : List Nat :=
  reps.foldl (fun poly r => polyMulLinear (labelOfRep r) poly) [1]

def locatorPrefix (depth : Nat) (reps : List Nat) : List Nat :=
  (((locatorFromReps reps).reverse.drop 1).take depth)

def isSubset (xs ys : List Nat) : Bool :=
  xs.all fun x => ys.contains x

def intersectionCard (xs ys : List Nat) : Nat :=
  (xs.filter fun x => ys.contains x).length

def deficiency (xs ys : List Nat) : Nat :=
  xs.length - intersectionCard xs ys

def choose {α : Type} (k : Nat) : List α → List (List α)
  | [] => if k == 0 then [[]] else []
  | x :: xs =>
      if k == 0 then
        [[]]
      else
        (choose (k - 1) xs).map (fun ys => x :: ys) ++ choose k xs

def familyClassSelections : List (List Nat) :=
  choose 7 intactClasses

def classDeficiency (classes : List Nat) : Nat :=
  64 * (anchorClasses.filter fun a => !(classes.contains a)).length

def supportFromClasses (classes : List Nat) : List Nat :=
  core31 ++ classes.flatMap blockReps64

def anchorSupport : List Nat :=
  supportFromClasses anchorClasses

def tripleSwapClasses : List Nat :=
  [11, 13, 15, 17, 19, 21, 23]

def tripleSwapSupport : List Nat :=
  supportFromClasses tripleSwapClasses

def blockLocator (a : Nat) : List Nat :=
  locatorFromReps (blockReps64 a)

def sameNonconstantBlockCoefficients (a : Nat) : Bool :=
  (blockLocator a).drop 1 == (blockLocator 5).drop 1

def allIntactReps : List Nat :=
  intactClasses.flatMap blockReps64

def fastBinomial (n k : Nat) : Nat :=
  (List.range k).foldl
    (fun value i => value * (n - i) / (i + 1))
    1

def H192 : Nat :=
  fastBinomial 479 192 * fastBinomial 543 192

def expectedH192 : Nat :=
  250306657071379809146712330966428990686412627706880861569476097211926513715638118988008071592368035074016933687250963576376001122774381719478502944898782144806538717279733256653844747778197374722693408393198745533043396789913740659616431432884514095828053347551969743776494179678510074205400

def Q32 : Nat := fieldPrime ^ 32
def M1022_479 : Nat := fastBinomial 1022 479

def t16Sigma (r : Nat) : Nat :=
  chebyshevPowTwo 4 ((2 * labelOfRep r) % fieldPrime)

def fiber16Reps (r0 : Nat) : List Nat :=
  oddReps.filter fun r => t16Sigma r == t16Sigma r0

def x16MinReps : List Nat :=
  [29, 15, 93, 21, 119, 95]

def y16MinReps : List Nat :=
  [33, 71, 9, 107, 7, 113]

def x16Sigmas : List Nat := x16MinReps.map t16Sigma
def y16Sigmas : List Nat := y16MinReps.map t16Sigma

def xExchangeReps : List Nat :=
  x16MinReps.flatMap fiber16Reps

def yExchangeReps : List Nat :=
  y16MinReps.flatMap fiber16Reps

def sumMod (xs : List Nat) : Nat :=
  xs.foldl (fun acc x => (acc + x) % fieldPrime) 0

def squareSumMod (xs : List Nat) : Nat :=
  xs.foldl (fun acc x => (acc + (x * x) % fieldPrime) % fieldPrime) 0

def pairProductSumMod : List Nat → Nat
  | [] => 0
  | x :: xs =>
      ((x * sumMod xs) % fieldPrime + pairProductSumMod xs) % fieldPrime

def polyFromValues (values : List Nat) : List Nat :=
  values.foldl (fun poly value => polyMulLinear value poly) [1]

def polyDifference (xs ys : List Nat) : List Nat :=
  List.zipWith (fun x y => (x + fieldPrime - y) % fieldPrime) xs ys

def core383 : List Nat :=
  (puncturedReps.filter fun r =>
      !(xExchangeReps.contains r) && !(yExchangeReps.contains r)).take 383

def mixingAnchor : List Nat := core383 ++ xExchangeReps
def mixingNeighbor : List Nat := core383 ++ yExchangeReps

def supportValid (support : List Nat) : Bool :=
  (support.length == 479) &&
  noDuplicates support &&
  isSubset support puncturedReps

theorem generator_norm_one :
    fp2Mul normOneGenerator (fp2Conj normOneGenerator) = fp2One := by decide

theorem generator_half_order :
    fp2PowTwo 30 normOneGenerator =
      ({ re := fieldPrime - 1, im := 0 } : Fp2) := by decide

theorem generator_full_order :
    fp2PowTwo 31 normOneGenerator = fp2One := by decide

theorem quotient_domain_exact :
    quotientLabels.length = 1024 ∧
    noDuplicates quotientLabels = true ∧
    puncturedReps.length = 1022 ∧
    puncturedLabels.length = 1022 ∧
    noDuplicates puncturedLabels = true := by native_decide

theorem intact_block_structure_exact :
    intactClasses.length = 14 ∧
    noDuplicates intactClasses = true ∧
    intactClasses.all (fun a =>
      ((blockReps64 a).length == 64) &&
      noDuplicates (blockReps64 a) &&
      isSubset (blockReps64 a) puncturedReps) = true ∧
    allIntactReps.length = 896 ∧
    noDuplicates allIntactReps = true ∧
    core31.length = 31 ∧
    noDuplicates core31 = true ∧
    isSubset core31 puncturedReps = true ∧
    (core31.all fun r => !(allIntactReps.contains r)) = true := by
  native_decide

theorem block_locators_differ_only_in_constant :
    intactClasses.all sameNonconstantBlockCoefficients = true := by
  native_decide

theorem family_selection_census :
    familyClassSelections.length = 3432 ∧
    noDuplicates familyClassSelections = true ∧
    familyClassSelections.all (fun cs =>
      (cs.length == 7) && noDuplicates cs &&
      cs.all fun c => intactClasses.contains c) = true := by
  native_decide

theorem round2_full_class_swap_census :
    fastBinomial 7 1 * fastBinomial 6 1 = 42 ∧
    fastBinomial 7 2 * fastBinomial 6 2 = 315 ∧
    fastBinomial 7 3 * fastBinomial 6 3 = 700 := by
  native_decide

theorem rooted_shell_census :
    (familyClassSelections.filter fun cs => classDeficiency cs == 64).length = 49 ∧
    (familyClassSelections.filter fun cs => classDeficiency cs == 128).length = 441 ∧
    (familyClassSelections.filter fun cs => classDeficiency cs == 192).length = 1225 ∧
    (familyClassSelections.filter fun cs => classDeficiency cs == 256).length = 1225 ∧
    (familyClassSelections.filter fun cs => classDeficiency cs == 320).length = 441 ∧
    (familyClassSelections.filter fun cs => classDeficiency cs == 384).length = 49 ∧
    (familyClassSelections.filter fun cs => classDeficiency cs == 448).length = 1 := by
  native_decide

theorem anchor_and_triple_swap_exact :
    supportValid anchorSupport = true ∧
    supportValid tripleSwapSupport = true ∧
    deficiency anchorSupport tripleSwapSupport = 192 ∧
    locatorPrefix 63 anchorSupport = locatorPrefix 63 tripleSwapSupport := by
  native_decide

theorem degree_transfer_arithmetic :
    31 + 6 * 64 = 415 ∧
    479 - 415 - 1 = 63 := by decide

theorem H192_exact : H192 = expectedH192 := by native_decide

theorem four_H192_lt_Q32 : 4 * H192 < Q32 := by native_decide

theorem shell_192_floor_zero : (4 * H192) / Q32 = 0 := by native_decide

theorem quotient_average_arithmetic :
    M1022_479 / Q32 = 3614119 ∧
    (M1022_479 + Q32 - 1) / Q32 = 3614120 ∧
    (4 * M1022_479) / Q32 = 14456476 := by
  native_decide

theorem intercept_1225_compiler_arithmetic :
    1 + 1225 * 447 + 14456476 = 15004052 ∧
    15004052 ≤ 16777215 ∧
    16777215 - 15004052 = 1773163 ∧
    1225 ≤ 5191 := by decide

theorem t16_fibers_exact :
    (x16MinReps ++ y16MinReps).all (fun r =>
      ((fiber16Reps r).length == 16) &&
      noDuplicates (fiber16Reps r) &&
      isSubset (fiber16Reps r) puncturedReps) = true ∧
    xExchangeReps.length = 96 ∧
    yExchangeReps.length = 96 ∧
    noDuplicates xExchangeReps = true ∧
    noDuplicates yExchangeReps = true ∧
    (xExchangeReps.all fun r => !(yExchangeReps.contains r)) = true := by
  native_decide

theorem t16_power_sum_relation :
    x16Sigmas =
      [583555490, 812986380, 849605071, 1093071961, 1362440376, 2022380190] ∧
    y16Sigmas =
      [125103457, 197700101, 785043271, 1054411686, 1079800039, 1334497267] ∧
    sumMod x16Sigmas = 281588527 ∧
    sumMod y16Sigmas = 281588527 ∧
    squareSumMod x16Sigmas = 1888686693 ∧
    squareSumMod y16Sigmas = 1888686693 ∧
    pairProductSumMod x16Sigmas = 1950190555 ∧
    pairProductSumMod y16Sigmas = 1950190555 ∧
    polyDifference (polyFromValues x16Sigmas) (polyFromValues y16Sigmas) =
      [1030524974, 16043166, 1710076578, 1294116245, 0, 0, 0] := by
  native_decide

theorem mixing_supports_exact :
    core383.length = 383 ∧
    noDuplicates core383 = true ∧
    supportValid mixingAnchor = true ∧
    supportValid mixingNeighbor = true ∧
    deficiency mixingAnchor mixingNeighbor = 96 := by
  native_decide

theorem mixing_prefix_exact :
    locatorPrefix 47 mixingAnchor = locatorPrefix 47 mixingNeighbor ∧
    locatorPrefix 48 mixingAnchor ≠ locatorPrefix 48 mixingNeighbor := by
  native_decide

theorem mixing_is_off_lattice :
    deficiency mixingAnchor mixingNeighbor = 96 ∧
    96 % 64 = 32 := by native_decide

#print axioms block_locators_differ_only_in_constant
#print axioms rooted_shell_census
#print axioms four_H192_lt_Q32
#print axioms t16_power_sum_relation
#print axioms mixing_prefix_exact

end M31QuotientBandMixing.Witnesses
