import AsymptoticSpine.PrimitiveBoolean
import M31QRootedShell.Deployed

/-!
# Deployed M31 C1--C8 owner coverage and all-key C9 loss-one census

This stdlib-only module restates the eight-point deployed Chebyshev profile from
the predecessor packet without importing any open-PR module.  It defines the
actual local C1--C8 raw predicates, applies the printed first-match order, and
checks every one of the seventy weight-four supports.

The raw C2 complete-`T_4` and C7 effective-image-collapse predicates both detect
the two complete `T_4` blocks, but C1 owns them first because they are complete
unions of antipodal `x ↦ x^2` fibers.  C3--C6 and C8 have empty local raw
catalogues on this frozen profile.  Hence C1 owns six supports and the exact
post-C1--C8 residual has sixty-four supports.

The first-three-power-sum key is injective on that residual.  More strongly,
for every residual support its key has a singleton fiber already in the full
seventy-support slice.  Thus every surviving key satisfies the loss-one
full-prefix field used by the C9 producer, with no counterexample key.

This is a finite profile-local theorem.  It does not pay fixed-outside profile
multiplicity, construct a received-line `(SE2)` certificate, prove residual
add-back or UNIF, or close an adjacent deployed row.
-/

namespace SidonEffectiveImage.M31C9OwnerCoverage

open AsymptoticSpine

set_option maxRecDepth 1000000
set_option maxHeartbeats 0

abbrev Support := Vector Bool 8

/-- Three power-sum prefix coordinates, represented by canonical residues. -/
structure PrefixKey where
  p1 : Nat
  p2 : Nat
  p3 : Nat
  deriving Repr, BEq, DecidableEq

/-- Literal earlier-owner order.  C9 is the residual and is not an earlier owner. -/
inductive EarlierOwner where
  | c1 | c2 | c3 | c4 | c5 | c6 | c7 | c8
  deriving Repr, BEq, DecidableEq

def firstMatchOrder : List EarlierOwner :=
  [.c1, .c2, .c3, .c4, .c5, .c6, .c7, .c8]

/-- Exact deployed Mersenne-31 list-row constants used by the profile. -/
def fieldPrime : Nat := M31QRootedShell.Deployed.pM31
def deployedPrefixDepth : Nat := M31QRootedShell.Deployed.w
def deployedBudget : Nat := M31QRootedShell.Deployed.Bstar
def deployedLength : Nat := 2 ^ 21
def deployedComplementWeight : Nat := M31QRootedShell.Deployed.listM
def fixedOutsideWeight : Nat := deployedComplementWeight - 4
def outsideAvailable : Nat := deployedLength - 8
def activeExtensionDegree : Nat := 1

/-- Eight actual M31 roots of `T_(2^21)`.  The two blocks of four are complete
`T_4` fibers. -/
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

/-- Complete list of the seventy weight-four masks and supports. -/
def fullMasks : List Nat :=
  (List.range 256).filter fun mask =>
    decide (boolWeight (supportVector mask) = 4)

def fullPoints : List Support :=
  fullMasks.map supportVector

/-- Sum the selected domain values to the `e`-th power modulo the row prime. -/
def sumPowerMod (e : Nat) (x : Support) : Nat :=
  (x.toList.zip domain).foldl
    (fun acc pair =>
      if pair.1 then (acc + pair.2 ^ e % fieldPrime) % fieldPrime else acc)
    0

/-- Active first-three-power-sum prefix key. -/
def prefixKey (x : Support) : PrefixKey :=
  { p1 := sumPowerMod 1 x
  , p2 := sumPowerMod 2 x
  , p3 := sumPowerMod 3 x }

/-- Selected active field values, in domain order. -/
def selectedValues (x : Support) : List Nat :=
  (x.toList.zip domain).filterMap fun pair =>
    if pair.1 then some pair.2 else none

/-- Exact C1 complete-fiber supports: choose two of the four antipodal pairs. -/
def c1PairUnionSupports : List Support :=
  [ supportVector 15, supportVector 85, supportVector 165
  , supportVector 90, supportVector 170, supportVector 240 ]

def c1Trigger (x : Support) : Bool :=
  c1PairUnionSupports.contains x

/-- Local C2 trigger: a weight-four support is one complete `T_4` fiber. -/
def sameT4Fiber (values : List Nat) : Bool :=
  match values with
  | [] => false
  | x :: xs =>
      decide (values.length = 4) &&
        xs.all (fun y => chebyshevPowTwo 2 y == chebyshevPowTwo 2 x)

def c2Trigger (x : Support) : Bool :=
  sameT4Fiber (selectedValues x)

/-- Intersection of all supports in the complete active slice.  This is the
only possible active planted block fixed throughout this local profile. -/
def commonActiveCore : Support :=
  Vector.ofFn fun i => fullPoints.all (fun x => x.get i)

/-- Local C3 trigger: a nonempty active block is planted throughout the profile. -/
def c3Trigger (_x : Support) : Bool :=
  decide (0 < boolWeight commonActiveCore)

/-- Local C4 trigger: the active locator has a repeated selected root. -/
def c4Trigger (x : Support) : Bool :=
  !noDuplicates (selectedValues x)

/-- Local C5 trigger: the frozen active profile uses a nontrivial extension. -/
def c5Trigger (_x : Support) : Bool :=
  decide (1 < activeExtensionDegree)

/-- Canonical modular subtraction. -/
def modSub (a b : Nat) : Nat :=
  (a % fieldPrime + fieldPrime - b % fieldPrime) % fieldPrime

/-- One `3×3` Jacobian minor of the first-three-power-sum map.
For selected values `a,b,c`, it is `6(b-a)(c-a)(c-b)`. -/
def powerSumJacobianMinor : List Nat → Nat
  | a :: b :: c :: _ =>
      (6 * modSub b a * modSub c a * modSub c b) % fieldPrime
  | _ => 0

/-- Local C6 trigger: rank drop of the active first-three-power-sum map. -/
def c6Trigger (x : Support) : Bool :=
  powerSumJacobianMinor (selectedValues x) == 0

/-- Full prefix fiber before any owner deletion. -/
def fullKeyFiber (z : PrefixKey) : List Support :=
  mapFiber fullPoints prefixKey z

/-- Local C7 trigger: effective-image collapse at the active prefix key. -/
def c7Trigger (x : Support) : Bool :=
  decide (1 < (fullKeyFiber (prefixKey x)).length)

/-- First-match classifier through C7, used to define the actual C8 residual. -/
def firstSevenOwner (x : Support) : Option EarlierOwner :=
  if c1Trigger x then some .c1
  else if c2Trigger x then some .c2
  else if c3Trigger x then some .c3
  else if c4Trigger x then some .c4
  else if c5Trigger x then some .c5
  else if c6Trigger x then some .c6
  else if c7Trigger x then some .c7
  else none

def postC1C7Points : List Support :=
  fullPoints.filter fun x => decide (firstSevenOwner x = none)

/-- Local C8 trigger: after C1--C7 deletion, a distinct same-prefix mate remains. -/
def c8Trigger (x : Support) : Bool :=
  decide (1 <
    (mapFiber postC1C7Points prefixKey (prefixKey x)).length)

/-- All raw local predicates, before first-match deletion. -/
def rawTrigger : EarlierOwner → Support → Bool
  | .c1 => c1Trigger
  | .c2 => c2Trigger
  | .c3 => c3Trigger
  | .c4 => c4Trigger
  | .c5 => c5Trigger
  | .c6 => c6Trigger
  | .c7 => c7Trigger
  | .c8 => c8Trigger

/-- Actual deployed local C1--C8 first-match owner function. -/
def earlierOwner (x : Support) : Option EarlierOwner :=
  if c1Trigger x then some .c1
  else if c2Trigger x then some .c2
  else if c3Trigger x then some .c3
  else if c4Trigger x then some .c4
  else if c5Trigger x then some .c5
  else if c6Trigger x then some .c6
  else if c7Trigger x then some .c7
  else if c8Trigger x then some .c8
  else none

/-- Exact post-C1--C8 residual. -/
def residualPoints : List Support :=
  fullPoints.filter fun x => decide (earlierOwner x = none)

theorem fullPoints_complete :
    ∀ x : Support, boolWeight x = 4 ↔ x ∈ fullPoints := by decide

theorem fullPoints_nodup : fullPoints.Nodup := by decide

/-- Complete fixed-weight family on the eight active coordinates. -/
def fullFamily : BoolFamily where
  dimension := 8
  weight := 4
  points := fullPoints
  points_nodup := fullPoints_nodup
  points_fixed := fun x hx => (fullPoints_complete x).mpr hx

/-- Exact local post-C1--C8 primitive leaf. -/
def leaf : PrimitiveBooleanLeaf PrefixKey where
  full := fullFamily
  full_complete := fullPoints_complete
  residual := residualPoints
  residual_sublist := List.filter_sublist
  prefixKey := prefixKey

/-- Literal exact owner-complement condition used by the C9 producer boundary. -/
def IsExactOwnerComplement : Prop :=
  ∀ x : Support,
    x ∈ leaf.residual ↔ x ∈ leaf.full.points ∧ earlierOwner x = none

theorem residual_exact : IsExactOwnerComplement := by
  intro x
  show x ∈ residualPoints ↔ x ∈ fullPoints ∧ earlierOwner x = none
  unfold residualPoints
  simp only [List.mem_filter, decide_eq_true_eq]

/-- Executable row printed for each support in the complete slice. -/
structure OwnerDecision where
  mask : Nat
  key : PrefixKey
  rawC1 : Bool
  rawC2 : Bool
  rawC3 : Bool
  rawC4 : Bool
  rawC5 : Bool
  rawC6 : Bool
  rawC7 : Bool
  rawC8 : Bool
  owner : Option EarlierOwner
  deriving Repr, BEq, DecidableEq

def ownerDecision (mask : Nat) : OwnerDecision :=
  let x := supportVector mask
  { mask := mask
  , key := prefixKey x
  , rawC1 := c1Trigger x
  , rawC2 := c2Trigger x
  , rawC3 := c3Trigger x
  , rawC4 := c4Trigger x
  , rawC5 := c5Trigger x
  , rawC6 := c6Trigger x
  , rawC7 := c7Trigger x
  , rawC8 := c8Trigger x
  , owner := earlierOwner x }

def ownerTable : List OwnerDecision :=
  fullMasks.map ownerDecision

def rawCount (owner : EarlierOwner) : Nat :=
  (fullPoints.filter (rawTrigger owner)).length

def firstMatchCount (owner : EarlierOwner) : Nat :=
  (fullPoints.filter fun x => decide (earlierOwner x = some owner)).length

/-- Residual mask list used by the machine-readable key certificate. -/
def residualMasks : List Nat :=
  fullMasks.filter fun mask =>
    decide (earlierOwner (supportVector mask) = none)

def fullMaskFiber (z : PrefixKey) : List Nat :=
  fullMasks.filter fun mask =>
    decide (prefixKey (supportVector mask) = z)

def residualMaskFiber (z : PrefixKey) : List Nat :=
  residualMasks.filter fun mask =>
    decide (prefixKey (supportVector mask) = z)

/-- Executable certificate row for every surviving key. -/
structure ResidualKeyDecision where
  mask : Nat
  key : PrefixKey
  fullFiberMasks : List Nat
  residualFiberMasks : List Nat
  deriving Repr, BEq, DecidableEq

def residualKeyDecision (mask : Nat) : ResidualKeyDecision :=
  let z := prefixKey (supportVector mask)
  { mask := mask
  , key := z
  , fullFiberMasks := fullMaskFiber z
  , residualFiberMasks := residualMaskFiber z }

def residualKeyTable : List ResidualKeyDecision :=
  residualMasks.map residualKeyDecision

def fullKeyList : List PrefixKey :=
  fullPoints.map prefixKey

def fullImage : List PrefixKey :=
  fullKeyList.eraseDups

def residualKeyList : List PrefixKey :=
  residualPoints.map prefixKey

def collisionKey : PrefixKey :=
  { p1 := 0, p2 := 2, p3 := 0 }

/-- Exact compiler loss and integral local image scale `ceil(70/69)`. -/
def compilerLoss : Nat := 1
def naturalScale : Nat := 2

/-- Every certificate row is an exact singleton in both the full and residual
fibers.  Together with `residualKeyList.Nodup`, this checks every surviving key
once and leaves no counterexample key. -/
def allResidualKeyRowsLossOne : Bool :=
  residualKeyTable.all fun row =>
    row.fullFiberMasks == [row.mask] &&
      row.residualFiberMasks == [row.mask]

def counterexampleMasks : List Nat :=
  residualKeyTable.filterMap fun row =>
    if row.fullFiberMasks == [row.mask] then none else some row.mask

/-- Every residual support also satisfies the literal producer inequality. -/
def allResidualRowsRowSharp : Bool :=
  residualKeyTable.all fun row =>
    decide (row.fullFiberMasks.length ≤ compilerLoss * naturalScale)

/-- Cleared image-normalized inequality on every surviving key. -/
def allResidualRowsImageNormalized : Bool :=
  residualKeyTable.all fun row =>
    decide (row.fullFiberMasks.length * fullImage.length ≤ fullPoints.length)

/-! ## Exact finite checks -/

theorem firstMatchOrder_exact :
    firstMatchOrder = [.c1, .c2, .c3, .c4, .c5, .c6, .c7, .c8] := rfl

theorem deployed_dimensions :
    fieldPrime = 2147483647 ∧
    deployedPrefixDepth = 67447 ∧
    deployedComplementWeight = 981129 ∧
    fixedOutsideWeight = 981125 ∧
    outsideAvailable = 2097144 ∧
    fixedOutsideWeight ≤ outsideAvailable ∧
    3 ≤ deployedPrefixDepth := by decide

theorem domain_nodup : noDuplicates domain = true := by decide

theorem domain_points_are_deployed_roots :
    domain.all (fun x => chebyshevPowTwo 21 x == 0) = true := by decide

theorem antipodal_pairs_exact :
    (434373082 + 1713110565) % fieldPrime = 0 ∧
    (614288294 + 1533195353) % fieldPrime = 0 ∧
    (1984437538 + 163046109) % fieldPrime = 0 ∧
    (380812851 + 1766670796) % fieldPrime = 0 := by decide

theorem t4_fibers_exact :
    (domain.take 4).all (fun x => chebyshevPowTwo 2 x == 1884637334) = true ∧
    (domain.drop 4).all (fun x => chebyshevPowTwo 2 x == 51044589) = true := by
  decide

theorem full_slice_card : fullPoints.length = 70 := by decide

theorem full_image_card : fullImage.length = 69 := by decide

theorem common_active_core_empty : boolWeight commonActiveCore = 0 := by decide

theorem active_extension_is_base_field : activeExtensionDegree = 1 := rfl

theorem raw_trigger_counts :
    rawCount .c1 = 6 ∧
    rawCount .c2 = 2 ∧
    rawCount .c3 = 0 ∧
    rawCount .c4 = 0 ∧
    rawCount .c5 = 0 ∧
    rawCount .c6 = 0 ∧
    rawCount .c7 = 2 ∧
    rawCount .c8 = 0 := by decide

/-- Both raw C2 hits are already exact C1 quotient supports. -/
theorem c2_raw_hits_preempted :
    fullPoints.all (fun x => !c2Trigger x || c1Trigger x) = true := by decide

/-- Both raw C7 hits are already exact C1 quotient supports. -/
theorem c7_raw_hits_preempted :
    fullPoints.all (fun x => !c7Trigger x || c1Trigger x) = true := by decide

/-- Actual first-match ownership on all seventy supports. -/
theorem first_match_owner_counts :
    firstMatchCount .c1 = 6 ∧
    firstMatchCount .c2 = 0 ∧
    firstMatchCount .c3 = 0 ∧
    firstMatchCount .c4 = 0 ∧
    firstMatchCount .c5 = 0 ∧
    firstMatchCount .c6 = 0 ∧
    firstMatchCount .c7 = 0 ∧
    firstMatchCount .c8 = 0 ∧
    residualPoints.length = 64 := by decide

theorem owner_table_card : ownerTable.length = 70 := by decide

theorem residual_masks_card : residualMasks.length = 64 := by decide

theorem residual_points_match_masks :
    residualPoints = residualMasks.map supportVector := by decide

theorem residual_key_table_card : residualKeyTable.length = 64 := by decide

theorem residual_prefix_injective : residualKeyList.Nodup := by decide

theorem collision_full_fiber_exact :
    fullPrefixFiber leaf collisionKey =
      [supportVector 15, supportVector 240] := by decide

theorem collision_removed_by_first_match :
    residualPrefixFiber leaf collisionKey = [] := by decide

/-- Criterion 2: every post-C1--C8 key is singleton already in the full slice. -/
theorem all_residual_key_rows_loss_one :
    allResidualKeyRowsLossOne = true := by decide

theorem no_counterexample_key : counterexampleMasks = [] := by decide

theorem all_residual_rows_rowSharp :
    allResidualRowsRowSharp = true := by decide

theorem all_residual_rows_imageNormalized :
    allResidualRowsImageNormalized = true := by decide

/-- Exact local charge fits the literal deployed M31 list-row budget. -/
theorem loss_one_fits_deployed_budget :
    compilerLoss * naturalScale ≤ deployedBudget := by decide

#print axioms residual_exact
#print axioms firstMatchOrder_exact
#print axioms deployed_dimensions
#print axioms domain_points_are_deployed_roots
#print axioms antipodal_pairs_exact
#print axioms t4_fibers_exact
#print axioms common_active_core_empty
#print axioms raw_trigger_counts
#print axioms c2_raw_hits_preempted
#print axioms c7_raw_hits_preempted
#print axioms first_match_owner_counts
#print axioms residual_points_match_masks
#print axioms residual_prefix_injective
#print axioms collision_full_fiber_exact
#print axioms collision_removed_by_first_match
#print axioms all_residual_key_rows_loss_one
#print axioms no_counterexample_key
#print axioms all_residual_rows_rowSharp
#print axioms all_residual_rows_imageNormalized
#print axioms loss_one_fits_deployed_budget

end SidonEffectiveImage.M31C9OwnerCoverage
