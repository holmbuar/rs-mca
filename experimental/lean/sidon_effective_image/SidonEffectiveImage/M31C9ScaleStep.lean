import AsymptoticSpine.EffectiveClosure
import AsymptoticSpine.UniformClosedLedger
import M31QRootedShell.Deployed
import Std

set_option maxRecDepth 1000000
set_option maxHeartbeats 0

/-!
# M31 C9 scale step: sixteen deployed roots and the first residual doubling

This stdlib-only module scales the exact finite calibration of upstream PR #1027
from eight roots in two complete `T_4` blocks to sixteen roots in four complete
`T_4` blocks.  The domain is re-derived from the same norm-one generator, the
complete weight-eight slice is enumerated, and the exact C1 antipodal-quotient
supports are deleted before the residual prefix fibers are counted.

The residual is no longer injective.  Its exact maximum fiber is two, attained
on 384 keys.  Every doubled residual key is a complete-`T_4` block swap, and the
first such key in ascending support-mask order is printed explicitly.  Thus the
minimal image-normalized residual loss grows from one in the eight-root packet
to two here, although the literal integral natural-scale inequality remains
`2 ≤ 1 * 2`.

This is a finite Q-support certificate.  It does not construct received-line
witnesses, an `(SE2)` projection, a slope payment, a global first-match atlas,
profile multiplicity, add-back, `UNIF`, or a deployed row certificate.
-/

namespace SidonEffectiveImage.M31C9ScaleStep

open AsymptoticSpine

abbrev Support := Nat

/-- Three first power sums, represented by canonical Mersenne-prime residues. -/
structure PrefixKey where
  p1 : Nat
  p2 : Nat
  p3 : Nat
  deriving Repr, BEq, DecidableEq

/-- Exact deployed Mersenne-31 list-row calibration inherited from integrated
`M31QRootedShell.Deployed`. -/
def fieldPrime : Nat := M31QRootedShell.Deployed.pM31
def deployedPrefixDepth : Nat := M31QRootedShell.Deployed.w
def deployedBudget : Nat := M31QRootedShell.Deployed.Bstar
def deployedLength : Nat := 2 ^ 21
def deployedComplementWeight : Nat := M31QRootedShell.Deployed.listM
def fixedOutsideWeight : Nat := deployedComplementWeight - 8
def outsideAvailable : Nat := deployedLength - 16

/-- Quadratic extension arithmetic `a+b*i`, with `i^2=-1`, represented by
canonical natural residues. -/
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

/-- Repeated squaring: `fp2PowTwo e u = u^(2^e)`. -/
def fp2PowTwo : Nat → Fp2 → Fp2
  | 0, u => u
  | e + 1, u => fp2PowTwo e (fp2Mul u u)

/-- Bitwise exponentiation for exponents below `2^31`. -/
def fp2Pow31 (u : Fp2) (e : Nat) : Fp2 :=
  (List.range 31).foldl
    (fun acc i =>
      if Nat.testBit e i then fp2Mul acc (fp2PowTwo i u) else acc)
    fp2One

/-- Stereographic norm-one generator used in #1027. -/
def normOneGenerator : Fp2 :=
  { re := 1717986917, im := 1288490189 }

/-- Four odd base exponents; adjoining the four `2^29` translates gives four
complete `T_4` blocks. -/
def baseExponents : List Nat := [256, 768, 1280, 1792]

def domainExponents : List Nat :=
  baseExponents.flatMap fun base =>
    (List.range 4).map fun j => base + j * 2 ^ 29

def derivedDomain : List Nat :=
  domainExponents.map fun e => (fp2Pow31 normOneGenerator e).re

/-- Sixteen actual deployed `T_(2^21)` roots, ordered by four complete `T_4`
blocks. -/
def domain : List Nat :=
  [ 434373082, 614288294, 1713110565, 1533195353
  , 1984437538, 380812851, 163046109, 1766670796
  , 1244279234, 907334541, 903204413, 1240149106
  , 2066813671, 1590029158, 80669976, 557454489 ]

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

/-- Hamming weight of the low sixteen bits of a support mask. -/
def maskWeight (mask : Support) : Nat :=
  (List.range 16).foldl
    (fun acc i => if Nat.testBit mask i then acc + 1 else acc) 0

def allMasks : List Support := List.range (2 ^ 16)

def fullSupports : List Support :=
  allMasks.filter fun mask => maskWeight mask == 8

def weightFourMasks : List Support :=
  allMasks.filter fun mask => maskWeight mask == 4

/-- Sum selected domain values to the `e`-th power modulo the row prime. -/
def sumPowerMod (e : Nat) (mask : Support) : Nat :=
  ((List.range 16).zip domain).foldl
    (fun acc pair =>
      if Nat.testBit mask pair.1 then
        (acc + pair.2 ^ e % fieldPrime) % fieldPrime
      else acc)
    0

def prefixKey (mask : Support) : PrefixKey :=
  { p1 := sumPowerMod 1 mask
  , p2 := sumPowerMod 2 mask
  , p3 := sumPowerMod 3 mask }

/-- The eight antipodal pairs, two in each `T_4` block. -/
def antipodalPairs : List (Nat × Nat) :=
  [(0, 2), (1, 3), (4, 6), (5, 7),
   (8, 10), (9, 11), (12, 14), (13, 15)]

/-- C1 owns exactly the weight-eight unions of four complete antipodal pairs. -/
def c1Owned (mask : Support) : Bool :=
  antipodalPairs.all fun pair =>
    Nat.testBit mask pair.1 == Nat.testBit mask pair.2

def c1OwnedSupports : List Support :=
  fullSupports.filter c1Owned

def residualSupports : List Support :=
  fullSupports.filter fun mask => !c1Owned mask

/-- Local exact prefix fibers, definitionally using the integrated `mapFiber`. -/
def fullPrefixFiber (z : PrefixKey) : List Support :=
  mapFiber fullSupports prefixKey z

def residualPrefixFiber (z : PrefixKey) : List Support :=
  mapFiber residualSupports prefixKey z

/-- Local copy of the exact pre-C9 constructor grammar. -/
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
    mask ∈ residualSupports ↔ mask ∈ fullSupports ∧ owner mask = none

theorem residual_exact {Owner : Type} [DecidableEq Owner] (c1 : Owner) :
    IsExactOwnerComplement (earlierOwner c1) := by
  intro mask
  unfold residualSupports earlierOwner
  simp only [List.mem_filter]
  cases h : c1Owned mask <;> simp [h]

theorem scoped_residual_exact :
    IsExactOwnerComplement scopedEarlierOwner := by
  unfold scopedEarlierOwner
  exact residual_exact ScopedPreC9Owner.c1

/-- Bucketed exact multiplicity computation.  Equal keys always lie in the same
bucket because the bucket is a function of `p1`; bucketing only avoids a
quadratic global `eraseDups`. -/
def bucketCount : Nat := 128

def keyBucket (z : PrefixKey) : Nat := z.p1 % bucketCount

structure KeyMultiplicity where
  key : PrefixKey
  multiplicity : Nat
  deriving Repr, BEq, DecidableEq

def multiplicityIn (keys : List PrefixKey) (z : PrefixKey) : Nat :=
  (keys.filter fun w => decide (w = z)).length

def bucketMultiplicities (keys : List PrefixKey) (bucket : Nat) :
    List KeyMultiplicity :=
  let bucketKeys := keys.filter fun z => keyBucket z == bucket
  bucketKeys.eraseDups.map fun z =>
    { key := z, multiplicity := multiplicityIn bucketKeys z }

def allMultiplicities (keys : List PrefixKey) : List KeyMultiplicity :=
  (List.range bucketCount).flatMap fun bucket =>
    bucketMultiplicities keys bucket

def fullKeyList : List PrefixKey := fullSupports.map prefixKey
def residualKeyList : List PrefixKey := residualSupports.map prefixKey

def maxNat : List Nat → Nat
  | [] => 0
  | x :: xs => Nat.max x (maxNat xs)

def sumNat (xs : List Nat) : Nat := xs.foldl (· + ·) 0

structure FiberCensus where
  mass : Nat
  imageCard : Nat
  maxFiber : Nat
  singletonKeys : Nat
  doubleKeys : Nat
  sixKeys : Nat
  otherKeys : Nat
  deriving Repr, BEq, DecidableEq

def fiberCensus (multiplicities : List KeyMultiplicity) : FiberCensus :=
  let counts := multiplicities.map KeyMultiplicity.multiplicity
  { mass := sumNat counts
  , imageCard := counts.length
  , maxFiber := maxNat counts
  , singletonKeys := (counts.filter fun n => n == 1).length
  , doubleKeys := (counts.filter fun n => n == 2).length
  , sixKeys := (counts.filter fun n => n == 6).length
  , otherKeys :=
      (counts.filter fun n => !(n == 1 || n == 2 || n == 6)).length }

/-- Four complete `T_4` support masks. -/
def t4BlockMasks : List Support := [15, 240, 3840, 61440]

def fullSixKey : PrefixKey := { p1 := 0, p2 := 4, p3 := 0 }

def fullSixMasks : List Support :=
  [255, 3855, 4080, 61455, 61680, 65280]

/-- First residual collision in ascending support-mask order. -/
def growthKey : PrefixKey :=
  { p1 := 826664565, p2 := 1588616718, p3 := 1026140363 }

def growthLeft : Support := 5903
def growthRight : Support := 6128
def growthRemainder : Support := 5888

def firstRepeatedKeyAux (seen : List PrefixKey) : List PrefixKey → Option PrefixKey
  | [] => none
  | z :: zs =>
      if seen.contains z then some z else firstRepeatedKeyAux (z :: seen) zs

def firstRepeatedResidualKey : Option PrefixKey :=
  firstRepeatedKeyAux [] residualKeyList

def disjointMasks (a b : Support) : Bool :=
  (List.range 16).all fun i =>
    !(Nat.testBit a i && Nat.testBit b i)

/-- The six unordered pairs of complete `T_4` blocks. -/
def t4BlockPairs : List (Support × Support) :=
  [(15, 240), (15, 3840), (15, 61440),
   (240, 3840), (240, 61440), (3840, 61440)]

structure BlockSwapRecord where
  leftBlock : Support
  rightBlock : Support
  remainder : Support
  leftSupport : Support
  rightSupport : Support
  key : PrefixKey
  deriving Repr, BEq, DecidableEq

def blockSwapRecords : List BlockSwapRecord :=
  t4BlockPairs.flatMap fun pair =>
    (weightFourMasks.filter fun remainder =>
      disjointMasks remainder (pair.1 + pair.2) &&
      !c1Owned (pair.1 + remainder) &&
      !c1Owned (pair.2 + remainder)).map fun remainder =>
        { leftBlock := pair.1
        , rightBlock := pair.2
        , remainder := remainder
        , leftSupport := pair.1 + remainder
        , rightSupport := pair.2 + remainder
        , key := prefixKey (pair.1 + remainder) }

def blockSwapRecordValid (record : BlockSwapRecord) : Bool :=
  maskWeight record.remainder == 4 &&
  maskWeight record.leftSupport == 8 &&
  maskWeight record.rightSupport == 8 &&
  residualSupports.contains record.leftSupport &&
  residualSupports.contains record.rightSupport &&
  record.leftSupport != record.rightSupport &&
  prefixKey record.leftSupport == record.key &&
  prefixKey record.rightSupport == record.key

def sameKeySet (xs ys : List PrefixKey) : Bool :=
  xs.all ys.contains && ys.all xs.contains

def ceilDiv (a b : Nat) : Nat := (a + b - 1) / b

def compilerLoss : Nat := 1
def naturalScale : Nat := 2

structure ScaleStepSummary where
  fullSupportCount : Nat
  fullCensus : FiberCensus
  c1OwnedSupportCount : Nat
  residualSupportCount : Nat
  residualCensus : FiberCensus
  fullSixFiberExact : Bool
  fullSixFiberDeleted : Bool
  firstRepeatedExact : Bool
  growthFiberExact : Bool
  growthBlockSwapExact : Bool
  blockSwapRecordCount : Nat
  blockSwapRecordsValid : Bool
  residualDoubleKeyCount : Nat
  residualDoubleKeysNodup : Bool
  blockSwapKeysNodup : Bool
  doubleKeysExactlyBlockSwaps : Bool
  fullNaturalScaleExact : Bool
  residualNaturalScaleExact : Bool
  integralLossOneBound : Bool
  imageNormalizedLossOneFails : Bool
  imageNormalizedLossTwoHolds : Bool
  deriving Repr, BEq, DecidableEq

def scaleStepSummary : ScaleStepSummary :=
  let fullMultiplicities := allMultiplicities fullKeyList
  let residualMultiplicities := allMultiplicities residualKeyList
  let fullStats := fiberCensus fullMultiplicities
  let residualStats := fiberCensus residualMultiplicities
  let residualDoubleKeys :=
    (residualMultiplicities.filter fun entry => entry.multiplicity == 2).map
      KeyMultiplicity.key
  let swapKeys := blockSwapRecords.map BlockSwapRecord.key
  { fullSupportCount := fullSupports.length
  , fullCensus := fullStats
  , c1OwnedSupportCount := c1OwnedSupports.length
  , residualSupportCount := residualSupports.length
  , residualCensus := residualStats
  , fullSixFiberExact := fullPrefixFiber fullSixKey == fullSixMasks
  , fullSixFiberDeleted := residualPrefixFiber fullSixKey == []
  , firstRepeatedExact := firstRepeatedResidualKey == some growthKey
  , growthFiberExact :=
      residualPrefixFiber growthKey == [growthLeft, growthRight]
  , growthBlockSwapExact :=
      growthLeft == 15 + growthRemainder &&
      growthRight == 240 + growthRemainder
  , blockSwapRecordCount := blockSwapRecords.length
  , blockSwapRecordsValid := blockSwapRecords.all blockSwapRecordValid
  , residualDoubleKeyCount := residualDoubleKeys.length
  , residualDoubleKeysNodup := noDuplicates residualDoubleKeys
  , blockSwapKeysNodup := noDuplicates swapKeys
  , doubleKeysExactlyBlockSwaps := sameKeySet residualDoubleKeys swapKeys
  , fullNaturalScaleExact :=
      ceilDiv fullStats.mass fullStats.imageCard == naturalScale
  , residualNaturalScaleExact :=
      ceilDiv residualStats.mass residualStats.imageCard == naturalScale
  , integralLossOneBound :=
      decide (residualStats.maxFiber ≤ compilerLoss * naturalScale)
  , imageNormalizedLossOneFails :=
      decide (residualStats.mass <
        residualStats.maxFiber * residualStats.imageCard)
  , imageNormalizedLossTwoHolds :=
      decide (residualStats.maxFiber * residualStats.imageCard ≤
        2 * residualStats.mass) }

def expectedFullCensus : FiberCensus :=
  { mass := 12870
  , imageCard := 12457
  , maxFiber := 6
  , singletonKeys := 12048
  , doubleKeys := 408
  , sixKeys := 1
  , otherKeys := 0 }

def expectedResidualCensus : FiberCensus :=
  { mass := 12800
  , imageCard := 12416
  , maxFiber := 2
  , singletonKeys := 12032
  , doubleKeys := 384
  , sixKeys := 0
  , otherKeys := 0 }

def expectedScaleStepSummary : ScaleStepSummary :=
  { fullSupportCount := 12870
  , fullCensus := expectedFullCensus
  , c1OwnedSupportCount := 70
  , residualSupportCount := 12800
  , residualCensus := expectedResidualCensus
  , fullSixFiberExact := true
  , fullSixFiberDeleted := true
  , firstRepeatedExact := true
  , growthFiberExact := true
  , growthBlockSwapExact := true
  , blockSwapRecordCount := 384
  , blockSwapRecordsValid := true
  , residualDoubleKeyCount := 384
  , residualDoubleKeysNodup := true
  , blockSwapKeysNodup := true
  , doubleKeysExactlyBlockSwaps := true
  , fullNaturalScaleExact := true
  , residualNaturalScaleExact := true
  , integralLossOneBound := true
  , imageNormalizedLossOneFails := true
  , imageNormalizedLossTwoHolds := true }

/-- Exact finite census, obstruction classification, and scale comparison. -/
theorem scale_step_summary_exact :
    scaleStepSummary = expectedScaleStepSummary := by decide

theorem residual_max_fiber_exact :
    scaleStepSummary.residualCensus.maxFiber = 2 := by
  rw [scale_step_summary_exact]
  rfl

theorem residual_doubled_key_count_exact :
    scaleStepSummary.residualCensus.doubleKeys = 384 := by
  rw [scale_step_summary_exact]
  rfl

theorem residual_image_normalized_loss_two_exact :
    scaleStepSummary.imageNormalizedLossOneFails = true ∧
    scaleStepSummary.imageNormalizedLossTwoHolds = true := by
  rw [scale_step_summary_exact]
  decide

theorem integral_loss_one_at_scale_two :
    scaleStepSummary.integralLossOneBound = true := by
  rw [scale_step_summary_exact]
  rfl

/-- Domain derivation and deployed-root checks, all in the kernel. -/
theorem generator_norm_one :
    fp2Mul normOneGenerator (fp2Conj normOneGenerator) = fp2One := by decide

theorem generator_half_order :
    fp2PowTwo 30 normOneGenerator =
      ({ re := fieldPrime - 1, im := 0 } : Fp2) := by decide

theorem generator_full_order :
    fp2PowTwo 31 normOneGenerator = fp2One := by decide

theorem domain_derived_from_generator : derivedDomain = domain := by decide

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
    (domain.take 4).all
        (fun x => chebyshevPowTwo 2 x == 1884637334) = true ∧
    ((domain.drop 4).take 4).all
        (fun x => chebyshevPowTwo 2 x == 51044589) = true ∧
    ((domain.drop 8).take 4).all
        (fun x => chebyshevPowTwo 2 x == 1916935773) = true ∧
    (domain.drop 12).all
        (fun x => chebyshevPowTwo 2 x == 116752674) = true := by decide

theorem t4_prefix_keys_equal :
    t4BlockMasks.map prefixKey =
      [ { p1 := 0, p2 := 2, p3 := 0 }
      , { p1 := 0, p2 := 2, p3 := 0 }
      , { p1 := 0, p2 := 2, p3 := 0 }
      , { p1 := 0, p2 := 2, p3 := 0 } ] := by decide

theorem deployed_dimensions :
    deployedPrefixDepth = 67447 ∧
    deployedComplementWeight = 981129 ∧
    fixedOutsideWeight = 981121 ∧
    outsideAvailable = 2097136 ∧
    fixedOutsideWeight ≤ outsideAvailable ∧
    3 ≤ deployedPrefixDepth := by decide

theorem local_charge_fits_deployed_budget :
    compilerLoss * naturalScale ≤ deployedBudget := by decide

#print axioms residual_exact
#print axioms scoped_residual_exact
#print axioms scale_step_summary_exact
#print axioms residual_max_fiber_exact
#print axioms residual_doubled_key_count_exact
#print axioms residual_image_normalized_loss_two_exact
#print axioms integral_loss_one_at_scale_two
#print axioms generator_norm_one
#print axioms generator_half_order
#print axioms generator_full_order
#print axioms domain_derived_from_generator
#print axioms domain_points_are_deployed_roots
#print axioms antipodal_pairs_exact
#print axioms t4_fibers_exact
#print axioms t4_prefix_keys_equal
#print axioms deployed_dimensions
#print axioms local_charge_fits_deployed_budget

end SidonEffectiveImage.M31C9ScaleStep
