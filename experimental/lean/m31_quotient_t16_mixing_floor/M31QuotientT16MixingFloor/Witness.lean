import Std

set_option maxRecDepth 1000000
set_option maxHeartbeats 0

/-!
# M31 quotient `T_16` mixing floor

This unbuilt stdlib-only local draft is intended to certify the finite
support-level counterexample in `m31_quotient_t16_mixing_floor.md` after pickup
on the declared parent.

On the pinned 1,022-label quotient domain, one 479-label anchor has 1,225
full-`T_64` triple-swap neighbors and eight further `T_16`-mixed neighbors at
deficiency 192.  All 1,233 supports have the same first 32 nonleading locator
coefficients.  The mixed eight are not full-`T_64` exchanges.  The module also
checks `4 H_192 < p^32` and the coefficient-four compiler arithmetic.

No received word, first-match survivor, codeword, explanation, ray, slope, or
row-global payment is constructed.
-/

namespace M31QuotientT16MixingFloor.Witness

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

def oddT64Classes : List Nat :=
  [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]

def oddT16Classes : List Nat :=
  (List.range 64).map fun j => 2 * j + 1

def oddT32Classes : List Nat :=
  (List.range 32).map fun j => 2 * j + 1

def t64BlockReps (a : Nat) : List Nat :=
  oddReps.filter fun r =>
    (r % 64 == a) || (r % 64 == 64 - a)

def t16BlockReps (a : Nat) : List Nat :=
  oddReps.filter fun r =>
    (r % 256 == a) || (r % 256 == 256 - a)

def t32BlockReps (a : Nat) : List Nat :=
  oddReps.filter fun r =>
    (r % 128 == a) || (r % 128 == 128 - a)

def t64Tau (a : Nat) : Nat :=
  chebyshevPowTwo 6 ((2 * labelOfRep a) % fieldPrime)

def t16Rho (a : Nat) : Nat :=
  chebyshevPowTwo 4 ((2 * labelOfRep a) % fieldPrime)

def t32Rho (a : Nat) : Nat :=
  chebyshevPowTwo 5 ((2 * labelOfRep a) % fieldPrime)

def insideT64 : List Nat := [7, 9, 13, 19, 21, 23, 27]
def outsideT64 : List Nat := [5, 11, 15, 17, 25, 29, 31]

def residual31 : List Nat :=
  ((t64BlockReps 1).filter fun r => !(r == 1)).take 31

def canonicalSupport (seed : List Nat) : List Nat :=
  puncturedReps.filter fun r => seed.contains r

def anchor : List Nat :=
  canonicalSupport (residual31 ++ insideT64.flatMap t64BlockReps)

def choose : Nat → List α → List (List α)
  | 0, _ => [[]]
  | _ + 1, [] => []
  | k + 1, x :: xs =>
      (choose k xs).map (fun ys => x :: ys) ++ choose (k + 1) xs

def exchangedSupport (removed added : List Nat) : List Nat :=
  puncturedReps.filter fun r =>
    (anchor.contains r && !(removed.contains r)) || added.contains r

def classSwapSpecs : List (List Nat × List Nat) :=
  (choose 3 insideT64).flatMap fun removed =>
    (choose 3 outsideT64).map fun added => (removed, added)

def classSwapSupport (spec : List Nat × List Nat) : List Nat :=
  exchangedSupport
    (spec.1.flatMap t64BlockReps)
    (spec.2.flatMap t64BlockReps)

def classSwapNeighbors : List (List Nat) :=
  classSwapSpecs.map classSwapSupport

structure MixedSpec where
  removed : List Nat
  added : List Nat
  powerSumOne : Nat
  deriving Repr, BEq, DecidableEq

def mixedSpecs : List MixedSpec :=
  [ { removed := [7, 9, 27, 37, 55, 71, 73, 77, 83, 109, 115, 119]
    , added := [5, 11, 17, 25, 39, 47, 53, 69, 79, 93, 99, 113]
    , powerSumOne := 752337374 }
  , { removed := [7, 21, 27, 37, 43, 71, 77, 83, 85, 107, 109, 115]
    , added := [5, 11, 17, 25, 39, 47, 53, 69, 79, 93, 99, 113]
    , powerSumOne := 752337374 }
  , { removed := [7, 23, 27, 37, 41, 71, 77, 83, 87, 105, 109, 115]
    , added := [5, 11, 17, 25, 39, 47, 53, 69, 79, 93, 99, 113]
    , powerSumOne := 752337374 }
  , { removed := [9, 37, 41, 51, 55, 83, 85, 101, 105, 107, 109, 115]
    , added := [5, 25, 31, 33, 47, 69, 75, 89, 93, 99, 111, 117]
    , powerSumOne := 1029303379 }
  , { removed := [13, 19, 21, 23, 27, 43, 45, 73, 77, 87, 91, 119]
    , added := [11, 17, 29, 35, 39, 53, 59, 81, 95, 97, 103, 123]
    , powerSumOne := 1118180268 }
  , { removed := [9, 13, 19, 45, 51, 55, 57, 73, 91, 101, 119, 121]
    , added := [15, 29, 35, 49, 59, 75, 81, 89, 103, 111, 117, 123]
    , powerSumOne := 1395146273 }
  , { removed := [13, 19, 21, 43, 45, 51, 57, 85, 91, 101, 107, 121]
    , added := [15, 29, 35, 49, 59, 75, 81, 89, 103, 111, 117, 123]
    , powerSumOne := 1395146273 }
  , { removed := [13, 19, 23, 41, 45, 51, 57, 87, 91, 101, 105, 121]
    , added := [15, 29, 35, 49, 59, 75, 81, 89, 103, 111, 117, 123]
    , powerSumOne := 1395146273 } ]

def mixedSupport (spec : MixedSpec) : List Nat :=
  exchangedSupport
    (spec.removed.flatMap t16BlockReps)
    (spec.added.flatMap t16BlockReps)

def mixedNeighbors : List (List Nat) :=
  mixedSpecs.map mixedSupport

def t32Removed : List Nat := [5, 21, 27, 29, 31, 39]
def t32Added : List Nat := [13, 19, 33, 37, 43, 63]
def t32PowerSumOne : Nat := 1122577494

def t32RemovedReps : List Nat := t32Removed.flatMap t32BlockReps
def t32AddedReps : List Nat := t32Added.flatMap t32BlockReps

def t32Core : List Nat :=
  (puncturedReps.filter fun r =>
    !(t32RemovedReps.contains r) && !(t32AddedReps.contains r)).take 287

def t32Anchor : List Nat := canonicalSupport (t32Core ++ t32RemovedReps)
def t32Neighbor : List Nat := canonicalSupport (t32Core ++ t32AddedReps)

def t64PairClosed (indices : List Nat) : Bool :=
  indices.all fun a => indices.contains (64 - a)


def allNeighbors : List (List Nat) :=
  classSwapNeighbors ++ mixedNeighbors

def allSupports : List (List Nat) := anchor :: allNeighbors

def isSubset (xs ys : List Nat) : Bool :=
  xs.all fun x => ys.contains x

def intersectionCard (xs ys : List Nat) : Nat :=
  (xs.filter fun x => ys.contains x).length

def deficiency (xs ys : List Nat) : Nat :=
  xs.length - intersectionCard xs ys

def prefixTail (root previous : Nat) : List Nat → List Nat
  | [] => []
  | coefficient :: coefficients =>
      ((coefficient + fieldPrime -
          ((root % fieldPrime) * (previous % fieldPrime)) % fieldPrime) % fieldPrime) ::
        prefixTail root coefficient coefficients

def prefixStep (root : Nat) : List Nat → List Nat
  | [] => []
  | leading :: coefficients =>
      leading :: prefixTail root leading coefficients

def locatorPrefix (depth : Nat) (reps : List Nat) : List Nat :=
  ((reps.foldl
      (fun coefficients r => prefixStep (labelOfRep r) coefficients)
      (1 :: List.replicate depth 0)).drop 1)

def eta : List Nat :=
  [ 1034127669, 50736831, 297947808, 2001416587
  , 582486197, 1119161472, 2092060217, 691570973
  , 351942517, 1850514162, 230010785, 1719889839
  , 1235349562, 568398669, 1689825028, 515651434
  , 18957312, 672550470, 1519314673, 322573603
  , 116542290, 1792409170, 753121918, 223352466
  , 1193775763, 493795963, 257600683, 1893789609
  , 1766068826, 431705051, 1355303332, 141998040 ]

def supportValid (support : List Nat) : Bool :=
  (support.length == 479) &&
  noDuplicates support &&
  isSubset support puncturedReps

def isCertifiedNeighbor (support : List Nat) : Bool :=
  supportValid support &&
  (locatorPrefix 32 support == eta) &&
  (deficiency anchor support == 192) &&
  !(support == anchor)

def sumMod (xs : List Nat) : Nat :=
  xs.foldl (fun total x => (total + x) % fieldPrime) 0

def sumSquaresMod (xs : List Nat) : Nat :=
  xs.foldl
    (fun total x => (total + (x % fieldPrime) * (x % fieldPrime)) % fieldPrime)
    0

def mixedMomentValid (spec : MixedSpec) : Bool :=
  let removedValues := spec.removed.map t16Rho
  let addedValues := spec.added.map t16Rho
  (sumMod removedValues == spec.powerSumOne) &&
  (sumMod addedValues == spec.powerSumOne) &&
  (sumSquaresMod removedValues == 6) &&
  (sumSquaresMod addedValues == 6)

def fastBinomial (n k : Nat) : Nat :=
  (List.range k).foldl
    (fun value i => value * (n - i) / (i + 1))
    1

def H192 : Nat :=
  fastBinomial 479 192 * fastBinomial 543 192

def expectedH192 : Nat :=
  250306657071379809146712330966428990686412627706880861569476097211926513715638118988008071592368035074016933687250963576376001122774381719478502944898782144806538717279733256653844747778197374722693408393198745533043396789913740659616431432884514095828053347551969743776494179678510074205400

def Q32 : Nat := fieldPrime ^ 32

def rootedDegree : Nat := allNeighbors.length

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

theorem quotient_labels_are_T1024_roots :
    quotientLabels.all
      (fun q => chebyshevPowTwo 10 ((2 * q) % fieldPrime) == 0) = true := by
  native_decide

theorem nested_fibers_exact :
    oddT64Classes.all (fun a =>
      ((t64BlockReps a).length == 64) &&
      noDuplicates (t64BlockReps a) &&
      (t64BlockReps a).all
        (fun r => chebyshevPowTwo 6 ((2 * labelOfRep r) % fieldPrime) == t64Tau a)) = true ∧
    oddT16Classes.all (fun a =>
      ((t16BlockReps a).length == 16) &&
      noDuplicates (t16BlockReps a) &&
      (t16BlockReps a).all
        (fun r => chebyshevPowTwo 4 ((2 * labelOfRep r) % fieldPrime) == t16Rho a)) = true ∧
    oddT32Classes.all (fun a =>
      ((t32BlockReps a).length == 32) &&
      noDuplicates (t32BlockReps a) &&
      (t32BlockReps a).all
        (fun r => chebyshevPowTwo 5 ((2 * labelOfRep r) % fieldPrime) == t32Rho a)) = true := by
  native_decide

theorem anchor_exact :
    residual31 =
      [ 63, 65, 127, 129, 191, 193, 255, 257
      , 319, 321, 383, 385, 447, 449, 511, 513
      , 575, 577, 639, 641, 703, 705, 767, 769
      , 831, 833, 895, 897, 959, 961, 1023 ] ∧
    anchor.length = 479 ∧
    noDuplicates anchor = true ∧
    isSubset anchor puncturedReps = true ∧
    locatorPrefix 32 anchor = eta := by native_decide

theorem class_swap_census :
    classSwapSpecs.length = 1225 ∧
    classSwapNeighbors.length = 1225 ∧
    noDuplicates classSwapNeighbors = true ∧
    classSwapNeighbors.all isCertifiedNeighbor = true := by native_decide

theorem class_swaps_match_exactly_sixty_three :
    classSwapNeighbors.all
      (fun support => locatorPrefix 63 support == locatorPrefix 63 anchor) = true ∧
    classSwapNeighbors.all
      (fun support => !(locatorPrefix 64 support == locatorPrefix 64 anchor)) = true := by
  native_decide

theorem mixed_moment_identities :
    mixedSpecs.length = 8 ∧
    mixedSpecs.all mixedMomentValid = true := by native_decide

theorem eight_mixed_neighbors :
    mixedNeighbors.length = 8 ∧
    noDuplicates mixedNeighbors = true ∧
    mixedNeighbors.all isCertifiedNeighbor = true ∧
    mixedNeighbors.all (fun support => !(classSwapNeighbors.contains support)) = true := by
  native_decide

theorem mixed_neighbors_match_exactly_forty_seven :
    mixedNeighbors.all
      (fun support => locatorPrefix 47 support == locatorPrefix 47 anchor) = true ∧
    mixedNeighbors.all
      (fun support => !(locatorPrefix 48 support == locatorPrefix 48 anchor)) = true := by
  native_decide

theorem one_thousand_two_hundred_thirty_three_distinct_neighbors :
    allNeighbors.length = 1233 ∧
    noDuplicates allNeighbors = true ∧
    allNeighbors.all isCertifiedNeighbor = true := by native_decide

theorem A1_full_T64_classification_false :
    mixedNeighbors.length > 0 ∧
    mixedNeighbors.all (fun support => !(classSwapNeighbors.contains support)) = true := by
  native_decide

theorem secondary_T32_A1_falsifier :
    t32Core.length = 287 ∧
    t32RemovedReps.length = 192 ∧
    t32AddedReps.length = 192 ∧
    noDuplicates t32Anchor = true ∧
    noDuplicates t32Neighbor = true ∧
    t32Anchor.length = 479 ∧
    t32Neighbor.length = 479 ∧
    deficiency t32Anchor t32Neighbor = 192 ∧
    sumMod (t32Removed.map t32Rho) = t32PowerSumOne ∧
    sumMod (t32Added.map t32Rho) = t32PowerSumOne ∧
    t64PairClosed t32Removed = false ∧
    t64PairClosed t32Added = false ∧
    locatorPrefix 63 t32Anchor = locatorPrefix 63 t32Neighbor ∧
    locatorPrefix 64 t32Anchor ≠ locatorPrefix 64 t32Neighbor := by
  native_decide

theorem H192_exact : H192 = expectedH192 := by native_decide

theorem four_H192_lt_Q32 : 4 * H192 < Q32 := by native_decide

theorem shell_floor_zero : (4 * H192) / Q32 = 0 := by native_decide

theorem every_intercept_at_most_1232_fails :
    Q32 * (rootedDegree - 1232) > 4 * H192 := by native_decide

theorem coefficient_four_window_arithmetic :
    1233 * 447 = 551151 ∧
    1 + 1233 * 447 + 14456476 = 15007628 ∧
    15007628 ≤ 16777215 ∧
    16777215 - 15007628 = 1769587 ∧
    1 + 5191 * 447 + 14456476 = 16776854 ∧
    16776854 ≤ 16777215 ∧
    1 + 5192 * 447 + 14456476 = 16777301 ∧
    16777301 > 16777215 := by decide

#print axioms generator_norm_one
#print axioms generator_full_order
#print axioms quotient_domain_exact
#print axioms quotient_labels_are_T1024_roots
#print axioms nested_fibers_exact
#print axioms anchor_exact
#print axioms class_swap_census
#print axioms class_swaps_match_exactly_sixty_three
#print axioms mixed_moment_identities
#print axioms eight_mixed_neighbors
#print axioms mixed_neighbors_match_exactly_forty_seven
#print axioms one_thousand_two_hundred_thirty_three_distinct_neighbors
#print axioms A1_full_T64_classification_false
#print axioms secondary_T32_A1_falsifier
#print axioms H192_exact
#print axioms four_H192_lt_Q32
#print axioms shell_floor_zero
#print axioms every_intercept_at_most_1232_fails
#print axioms coefficient_four_window_arithmetic

end M31QuotientT16MixingFloor.Witness
