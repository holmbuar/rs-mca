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

The finite census is certified by a fixed-width stable radix sort of the
complete 12,870-row `(mask,key)` table.  Kernel checks recompute every key from
its mask, verify adjacent key order, radix-sort the mask column back to the
weight-eight slice of `List.range 65536`, and read every fiber from one
adjacent-equality run scan.  All passes are linear in the table size for the
fixed 16/31-bit widths; no deduplication or membership search is used in the
census.

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

/-- Duplicate-free executable predicate used only for the sixteen-point domain. -/
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

/-! ## Fixed-width radix table and linear certificate scans -/

structure TableRow where
  mask : Support
  p1 : Nat
  p2 : Nat
  p3 : Nat
  deriving Repr, BEq, DecidableEq

def TableRow.key (row : TableRow) : PrefixKey :=
  { p1 := row.p1, p2 := row.p2, p3 := row.p3 }

def tableRowOfMask (mask : Support) : TableRow :=
  let key := prefixKey mask
  ⟨mask, key.p1, key.p2, key.p3⟩

def unsortedTable : List TableRow :=
  fullSupports.map tableRowOfMask

/-- Stable one-bit partition.  Both filters are linear and no search is nested
inside either pass. -/
def stableBitPass {α : Type}
    (value : α → Nat) (bit : Nat) (rows : List α) : List α :=
  rows.filter (fun row => !Nat.testBit (value row) bit) ++
    rows.filter (fun row => Nat.testBit (value row) bit)

/-- Fixed-width least-significant-bit radix sort. -/
def radixSortNat {α : Type}
    (value : α → Nat) (bits : Nat) (rows : List α) : List α :=
  (List.range bits).foldl
    (fun current bit => stableBitPass value bit current) rows

/-- Lexicographic `(p1,p2,p3,mask)` order, obtained by stable LSD passes. -/
def sortedTable : List TableRow :=
  let byMask := radixSortNat TableRow.mask 16 unsortedTable
  let byP3 := radixSortNat (fun row => row.p3) 31 byMask
  let byP2 := radixSortNat (fun row => row.p2) 31 byP3
  radixSortNat (fun row => row.p1) 31 byP2

def rowKeyRecomputes (row : TableRow) : Bool :=
  prefixKey row.mask == row.key

def prefixKeyLT (a b : PrefixKey) : Bool :=
  if a.p1 < b.p1 then true
  else if b.p1 < a.p1 then false
  else if a.p2 < b.p2 then true
  else if b.p2 < a.p2 then false
  else decide (a.p3 < b.p3)

def tableRowLE (a b : TableRow) : Bool :=
  if a.key == b.key then decide (a.mask ≤ b.mask)
  else prefixKeyLT a.key b.key

def adjacentAllAux {α : Type}
    (p : α → α → Bool) (previous : α) : List α → Bool
  | [] => true
  | next :: rest => p previous next && adjacentAllAux p next rest

def adjacentAll {α : Type} (p : α → α → Bool) : List α → Bool
  | [] => true
  | first :: rest => adjacentAllAux p first rest

structure FiberCensus where
  mass : Nat
  imageCard : Nat
  maxFiber : Nat
  singletonKeys : Nat
  doubleKeys : Nat
  sixKeys : Nat
  otherKeys : Nat
  deriving Repr, BEq, DecidableEq

def emptyFiberCensus : FiberCensus :=
  { mass := 0
  , imageCard := 0
  , maxFiber := 0
  , singletonKeys := 0
  , doubleKeys := 0
  , sixKeys := 0
  , otherKeys := 0 }

def addRunToCensus (census : FiberCensus) (runSize : Nat) : FiberCensus :=
  { mass := census.mass + runSize
  , imageCard := census.imageCard + 1
  , maxFiber := Nat.max census.maxFiber runSize
  , singletonKeys :=
      census.singletonKeys + (if runSize == 1 then 1 else 0)
  , doubleKeys :=
      census.doubleKeys + (if runSize == 2 then 1 else 0)
  , sixKeys :=
      census.sixKeys + (if runSize == 6 then 1 else 0)
  , otherKeys :=
      census.otherKeys +
        (if runSize == 1 || runSize == 2 || runSize == 6 then 0 else 1) }

/-- Four complete `T_4` support masks. -/
def t4BlockMasks : List Support := [15, 240, 3840, 61440]

/-- The six unordered pairs of complete `T_4` blocks. -/
def t4BlockPairs : List (Support × Support) :=
  [(15, 240), (15, 3840), (15, 61440),
   (240, 3840), (240, 61440), (3840, 61440)]

def disjointMasks (a b : Support) : Bool :=
  (List.range 16).all fun i =>
    !(Nat.testBit a i && Nat.testBit b i)

def blockIncluded (block mask : Support) : Bool :=
  (List.range 16).all fun i =>
    !Nat.testBit block i || Nat.testBit mask i

def orientedT4BlockSwap
    (left right : Support) (blocks : Support × Support) : Bool :=
  if blockIncluded blocks.1 left && blockIncluded blocks.2 right then
    let leftRemainder := left - blocks.1
    let rightRemainder := right - blocks.2
    leftRemainder == rightRemainder &&
      maskWeight leftRemainder == 4 &&
      disjointMasks leftRemainder (blocks.1 + blocks.2)
  else false

def isT4BlockSwap (left right : Support) : Bool :=
  t4BlockPairs.any fun blocks =>
    orientedT4BlockSwap left right blocks ||
      orientedT4BlockSwap right left blocks

structure RunAnalysis where
  census : FiberCensus
  blockSwapCount : Nat
  allDoubleBlockSwaps : Bool
  firstRepeatLaterMask : Nat
  firstRepeatKey : PrefixKey
  firstRepeatLeft : Support
  firstRepeatRight : Support
  deriving Repr, BEq, DecidableEq

def zeroPrefixKey : PrefixKey := { p1 := 0, p2 := 0, p3 := 0 }

def emptyRunAnalysis : RunAnalysis :=
  { census := emptyFiberCensus
  , blockSwapCount := 0
  , allDoubleBlockSwaps := true
  , firstRepeatLaterMask := 2 ^ 16
  , firstRepeatKey := zeroPrefixKey
  , firstRepeatLeft := 0
  , firstRepeatRight := 0 }

def finishRun
    (key : PrefixKey) (masksRev : List Support)
    (analysis : RunAnalysis) : RunAnalysis :=
  let masks := masksRev.reverse
  let runSize := masks.length
  let nextCensus := addRunToCensus analysis.census runSize
  if runSize == 2 then
    match masks with
    | [left, right] =>
        let isSwap := isT4BlockSwap left right
        let laterMask := Nat.max left right
        let isFirst := laterMask < analysis.firstRepeatLaterMask
        { census := nextCensus
        , blockSwapCount :=
            analysis.blockSwapCount + (if isSwap then 1 else 0)
        , allDoubleBlockSwaps := analysis.allDoubleBlockSwaps && isSwap
        , firstRepeatLaterMask :=
            if isFirst then laterMask else analysis.firstRepeatLaterMask
        , firstRepeatKey :=
            if isFirst then key else analysis.firstRepeatKey
        , firstRepeatLeft :=
            if isFirst then left else analysis.firstRepeatLeft
        , firstRepeatRight :=
            if isFirst then right else analysis.firstRepeatRight }
    | _ =>
        { census := nextCensus
        , blockSwapCount := analysis.blockSwapCount
        , allDoubleBlockSwaps := false
        , firstRepeatLaterMask := analysis.firstRepeatLaterMask
        , firstRepeatKey := analysis.firstRepeatKey
        , firstRepeatLeft := analysis.firstRepeatLeft
        , firstRepeatRight := analysis.firstRepeatRight }
  else
    { census := nextCensus
    , blockSwapCount := analysis.blockSwapCount
    , allDoubleBlockSwaps := analysis.allDoubleBlockSwaps
    , firstRepeatLaterMask := analysis.firstRepeatLaterMask
    , firstRepeatKey := analysis.firstRepeatKey
    , firstRepeatLeft := analysis.firstRepeatLeft
    , firstRepeatRight := analysis.firstRepeatRight }

def scanSortedRowsAux
    (currentKey : PrefixKey) (masksRev : List Support)
    (analysis : RunAnalysis) : List TableRow → RunAnalysis
  | [] => finishRun currentKey masksRev analysis
  | row :: rows =>
      if row.key == currentKey then
        scanSortedRowsAux currentKey (row.mask :: masksRev) analysis rows
      else
        scanSortedRowsAux row.key [row.mask]
          (finishRun currentKey masksRev analysis) rows

def analyzeSortedRows : List TableRow → RunAnalysis
  | [] => emptyRunAnalysis
  | row :: rows =>
      scanSortedRowsAux row.key [row.mask] emptyRunAnalysis rows

def tableFiber (rows : List TableRow) (z : PrefixKey) : List Support :=
  (rows.filter fun row => row.key == z).map TableRow.mask

def fullSixKey : PrefixKey := { p1 := 0, p2 := 4, p3 := 0 }

def fullSixMasks : List Support :=
  [255, 3855, 4080, 61455, 61680, 65280]

/-- First residual collision in ascending support-mask order. -/
def growthKey : PrefixKey :=
  { p1 := 826664565, p2 := 1588616718, p3 := 1026140363 }

def growthLeft : Support := 5903
def growthRight : Support := 6128
def growthRemainder : Support := 5888

def ceilDiv (a b : Nat) : Nat := (a + b - 1) / b

def compilerLoss : Nat := 1
def naturalScale : Nat := 2

structure ScaleStepSummary where
  tableKeyRecomputation : Bool
  tableSorted : Bool
  maskColumnComplete : Bool
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
  let rows := sortedTable
  let keyCheck := rows.all rowKeyRecomputes
  let sortedCheck := adjacentAll tableRowLE rows
  let maskSorted := radixSortNat TableRow.mask 16 rows
  let maskCheck := maskSorted.map TableRow.mask == fullSupports
  let fullAnalysis := analyzeSortedRows rows
  let residualRows := rows.filter fun row => !c1Owned row.mask
  let residualAnalysis := analyzeSortedRows residualRows
  { tableKeyRecomputation := keyCheck
  , tableSorted := sortedCheck
  , maskColumnComplete := maskCheck
  , fullSupportCount := rows.length
  , fullCensus := fullAnalysis.census
  , c1OwnedSupportCount := rows.length - residualRows.length
  , residualSupportCount := residualRows.length
  , residualCensus := residualAnalysis.census
  , fullSixFiberExact :=
      tableFiber rows fullSixKey == fullSixMasks
  , fullSixFiberDeleted :=
      tableFiber residualRows fullSixKey == []
  , firstRepeatedExact :=
      residualAnalysis.firstRepeatLaterMask == growthRight &&
      residualAnalysis.firstRepeatKey == growthKey &&
      residualAnalysis.firstRepeatLeft == growthLeft &&
      residualAnalysis.firstRepeatRight == growthRight
  , growthFiberExact :=
      tableFiber residualRows growthKey == [growthLeft, growthRight]
  , growthBlockSwapExact :=
      growthLeft == 15 + growthRemainder &&
      growthRight == 240 + growthRemainder &&
      isT4BlockSwap growthLeft growthRight
  , blockSwapRecordCount := residualAnalysis.blockSwapCount
  , blockSwapRecordsValid := residualAnalysis.allDoubleBlockSwaps
  , residualDoubleKeyCount := residualAnalysis.census.doubleKeys
  , residualDoubleKeysNodup := sortedCheck
  , blockSwapKeysNodup :=
      sortedCheck && residualAnalysis.allDoubleBlockSwaps
  , doubleKeysExactlyBlockSwaps :=
      residualAnalysis.allDoubleBlockSwaps &&
        residualAnalysis.blockSwapCount == residualAnalysis.census.doubleKeys
  , fullNaturalScaleExact :=
      ceilDiv fullAnalysis.census.mass fullAnalysis.census.imageCard ==
        naturalScale
  , residualNaturalScaleExact :=
      ceilDiv residualAnalysis.census.mass residualAnalysis.census.imageCard ==
        naturalScale
  , integralLossOneBound :=
      decide
        (residualAnalysis.census.maxFiber ≤ compilerLoss * naturalScale)
  , imageNormalizedLossOneFails :=
      decide
        (residualAnalysis.census.mass <
          residualAnalysis.census.maxFiber *
            residualAnalysis.census.imageCard)
  , imageNormalizedLossTwoHolds :=
      decide
        (residualAnalysis.census.maxFiber *
            residualAnalysis.census.imageCard ≤
          2 * residualAnalysis.census.mass) }

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
  { tableKeyRecomputation := true
  , tableSorted := true
  , maskColumnComplete := true
  , fullSupportCount := 12870
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

theorem sorted_table_key_recomputation :
    scaleStepSummary.tableKeyRecomputation = true := by
  rw [scale_step_summary_exact]
  rfl

theorem sorted_table_order_exact :
    scaleStepSummary.tableSorted = true := by
  rw [scale_step_summary_exact]
  rfl

theorem sorted_table_mask_column_complete :
    scaleStepSummary.maskColumnComplete = true := by
  rw [scale_step_summary_exact]
  rfl

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

/-! ## Domain derivation and deployed arithmetic -/

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
#print axioms sorted_table_key_recomputation
#print axioms sorted_table_order_exact
#print axioms sorted_table_mask_column_complete
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
