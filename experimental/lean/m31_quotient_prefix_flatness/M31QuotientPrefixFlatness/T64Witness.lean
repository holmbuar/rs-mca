import Std

set_option maxRecDepth 1000000
set_option maxHeartbeats 0

/-!
# M31 quotient prefix-flatness: explicit `T_64` block-swap witness

This stdlib-only module certifies the finite witness in
`m31_quotient_prefix_flatness_t64_witness.md`.

The pinned `c=2048`, `(u,v)=(0,1)` quotient domain has 1,022 labels after
removing the two labels occupied by the pinned active eight-root template.
Fourteen intact quotient `T_64` fibers remain.  An explicit 415-label common
set plus seven different intact 64-blocks gives one anchor and six distinct
deficiency-64 neighbors.  Direct locator multiplication verifies that all seven
supports have the printed first 32 coefficients (indeed the first 63).

The module also checks `4 H_64 < p^32`, so the six-star violates the proposed
`(Q-3+4)` pointwise shell condition.  It does not construct a received word,
first-match survivor, codeword, ray, slope, or row-global payment.
-/

namespace M31QuotientPrefixFlatness.T64Witness

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

def monicFold2048 (x : Nat) : Nat :=
  (monicT2048Scale * chebyshevPowTwo 11 x) % fieldPrime

def activeRoots : List Nat :=
  [ 434373082, 614288294, 1713110565, 1533195353
  , 1984437538, 380812851, 163046109, 1766670796 ]

def puncturedReps : List Nat :=
  oddReps.filter fun r => !(r == 1) && !(r == 3)

def puncturedLabels : List Nat :=
  puncturedReps.map labelOfRep

def oddClasses : List Nat :=
  [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]

def blockReps (a : Nat) : List Nat :=
  oddReps.filter fun r =>
    (r % 64 == a) || (r % 64 == 64 - a)

def blockLabels (a : Nat) : List Nat :=
  (blockReps a).map labelOfRep

def t64Tau (a : Nat) : Nat :=
  chebyshevPowTwo 6 ((2 * labelOfRep a) % fieldPrime)

def tauTable : List Nat :=
  [ 26164677, 1580223790, 280947147, 456695729
  , 579625837, 1013961365, 194696271, 505542828
  , 1641940819, 1952787376, 1133522282, 1567857810
  , 1690787918, 1866536500, 567259857, 2121318970 ]

def partial27 : List Nat :=
  [ 27, 37, 91, 101, 155, 165, 219, 229
  , 283, 293, 347, 357, 411, 421, 475, 485
  , 539, 549, 603, 613, 667, 677, 731, 741
  , 795, 805, 859, 869, 923, 933, 987 ]

def commonReps : List Nat :=
  blockReps 15 ++ blockReps 17 ++ blockReps 19 ++
  blockReps 21 ++ blockReps 23 ++ blockReps 25 ++ partial27

def anchor : List Nat := commonReps ++ blockReps 5
def neighbor1 : List Nat := commonReps ++ blockReps 7
def neighbor2 : List Nat := commonReps ++ blockReps 9
def neighbor3 : List Nat := commonReps ++ blockReps 11
def neighbor4 : List Nat := commonReps ++ blockReps 13
def neighbor5 : List Nat := commonReps ++ blockReps 29
def neighbor6 : List Nat := commonReps ++ blockReps 31

def neighbors : List (List Nat) :=
  [neighbor1, neighbor2, neighbor3, neighbor4, neighbor5, neighbor6]

def allSupports : List (List Nat) := anchor :: neighbors

def isSubset (xs ys : List Nat) : Bool :=
  xs.all fun x => ys.contains x

def intersectionCard (xs ys : List Nat) : Nat :=
  (xs.filter fun x => ys.contains x).length

def deficiency (xs ys : List Nat) : Nat :=
  xs.length - intersectionCard xs ys

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

def eta : List Nat :=
  [ 2144970186, 693846040, 254084710, 1501952290
  , 1904231690, 558873387, 1400618348, 1749425225
  , 2110682204, 1763030673, 102589073, 1770388691
  , 971529856, 948975681, 774218929, 1490251835
  , 2095038705, 838625156, 774891784, 644995098
  , 888552471, 1685238706, 1330006363, 1053276022
  , 1544945819, 100722017, 1420529349, 1803184017
  , 1196844108, 324775767, 591689729, 1982980281 ]

def supportValid (support : List Nat) : Bool :=
  (support.length == 479) &&
  noDuplicates support &&
  isSubset support puncturedReps

def isCertifiedNeighbor (support : List Nat) : Bool :=
  supportValid support &&
  (locatorPrefix 32 support == eta) &&
  (deficiency anchor support == 64) &&
  !(support == anchor)

def fastBinomial (n k : Nat) : Nat :=
  (List.range k).foldl
    (fun value i => value * (n - i) / (i + 1))
    1

def H64 : Nat :=
  fastBinomial 479 64 * fastBinomial 543 64

def expectedH64 : Nat :=
  586374616784432967317447344396311850952251481404090129066339701269086144611744331859382537679275957595113162682732279972248681107329260801825759429939073953027297000

def Q32 : Nat := fieldPrime ^ 32

def listedRootedDegree : Nat := neighbors.length

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

theorem active_profile_punctures_exact :
    activeRoots.all (fun x => chebyshevPowTwo 21 x == 0) = true ∧
    activeRoots.map monicFold2048 =
      [ labelOfRep 1, labelOfRep 1, labelOfRep 1, labelOfRep 1
      , labelOfRep 3, labelOfRep 3, labelOfRep 3, labelOfRep 3 ] ∧
    labelOfRep 1 = 778433895 ∧
    labelOfRep 3 = 173262001 := by native_decide

theorem t64_fibers_exact :
    oddClasses.map t64Tau = tauTable ∧
    oddClasses.all (fun a =>
      ((blockReps a).length == 64) &&
      noDuplicates (blockReps a) &&
      (blockLabels a).all
        (fun q => chebyshevPowTwo 6 ((2 * q) % fieldPrime) == t64Tau a)) =
      true := by native_decide

theorem common_core_exact :
    commonReps.length = 415 ∧
    noDuplicates commonReps = true ∧
    isSubset commonReps puncturedReps = true ∧
    partial27.length = 31 ∧
    isSubset partial27 (blockReps 27) = true := by native_decide

theorem supports_exact :
    allSupports.length = 7 ∧
    allSupports.all supportValid = true ∧
    noDuplicates allSupports = true := by native_decide

theorem all_prefixes_match_eta :
    allSupports.all (fun support => locatorPrefix 32 support == eta) = true := by
  native_decide

theorem first_sixty_three_coefficients_match :
    allSupports.all
      (fun support => locatorPrefix 63 support == locatorPrefix 63 anchor) =
      true := by native_decide

theorem six_deficiency_64_neighbors :
    neighbors.length = 6 ∧
    noDuplicates neighbors = true ∧
    neighbors.all isCertifiedNeighbor = true := by native_decide

theorem H64_exact : H64 = expectedH64 := by native_decide

theorem four_H64_lt_Q32 : 4 * H64 < Q32 := by native_decide

theorem shell_floor_zero : (4 * H64) / Q32 = 0 := by native_decide

theorem Q_minus_3_plus_4_violated :
    Q32 * (listedRootedDegree - 3) > 4 * H64 := by native_decide

theorem conditional_b6_c4_arithmetic :
    1 + 6 * 447 + 14456476 = 14459159 ∧
    14459159 ≤ 16777215 ∧
    16777215 - 14459159 = 2318056 := by decide

#print axioms generator_norm_one
#print axioms generator_full_order
#print axioms quotient_domain_exact
#print axioms quotient_labels_are_T1024_roots
#print axioms active_profile_punctures_exact
#print axioms t64_fibers_exact
#print axioms common_core_exact
#print axioms supports_exact
#print axioms all_prefixes_match_eta
#print axioms first_sixty_three_coefficients_match
#print axioms six_deficiency_64_neighbors
#print axioms H64_exact
#print axioms four_H64_lt_Q32
#print axioms shell_floor_zero
#print axioms Q_minus_3_plus_4_violated
#print axioms conditional_b6_c4_arithmetic

end M31QuotientPrefixFlatness.T64Witness
