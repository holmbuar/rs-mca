import AsymptoticSpine.PrimitiveBoolean
import AsymptoticSpine.EffectiveClosure
import AsymptoticSpine.UniformClosedLedger
import M31QRootedShell.Deployed

/-!
# One exact loss-one C9 prefix key at the deployed Mersenne-31 row

This stdlib-only module proves one scoped row-sharp field of the exact shape
consumed by the C9 semantic producer.  It uses eight actual roots of
`T_(2^21)` over `F_(2^31-1)`, arranged as two complete `T_4` fibers, and the
complete four-subset slice on those eight moving coordinates.

The first three power sums have one doubled key, occupied by the two complete
`T_4` blocks.  Removing the six complete fibers of the earlier antipodal C1
quotient leaves an injective residual prefix map.  One printed quotient-free key
already has a singleton full prefix fiber.  Therefore its full-prefix bound is
loss one, independently of any later owner deletion.  A genuine `SE2Certificate`
remains an explicit argument in the final slope-payment theorem; no synthetic
Sidon or slope claim is manufactured.

The module does not prove that this scoped profile occurs in an exhaustive
Mersenne-31 first-match atlas, pay the number of fixed-outside profiles, prove
residual add-back or UNIF, or close the deployed row.
-/

namespace SidonEffectiveImage.M31C9RowSharp

open AsymptoticSpine

abbrev Support := Vector Bool 8

/-- Three power-sum prefix coordinates, represented by canonical residues. -/
structure PrefixKey where
  p1 : Nat
  p2 : Nat
  p3 : Nat
  deriving Repr, BEq, DecidableEq

/-- Exact deployed Mersenne-31 list-row constants. -/
def fieldPrime : Nat := M31QRootedShell.Deployed.pM31
def deployedPrefixDepth : Nat := M31QRootedShell.Deployed.w
def deployedBudget : Nat := M31QRootedShell.Deployed.Bstar
def deployedLength : Nat := 2 ^ 21
def deployedComplementWeight : Nat := M31QRootedShell.Deployed.listM
def fixedOutsideWeight : Nat := deployedComplementWeight - 4
def outsideAvailable : Nat := deployedLength - 8

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

/-- Stereographic norm-one generator used to derive the printed domain. -/
def normOneGenerator : Fp2 :=
  { re := 1717986917, im := 1288490189 }

/-- Eight actual M31 Chebyshev-domain points.  The first and last four-point
blocks are complete `T_4` fibers. -/
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

/-- The two complete `T_4` blocks and one quotient-free singleton-key support. -/
def t4BlockA : Support := supportVector 15
def t4BlockB : Support := supportVector 240
def selectedSupport : Support := supportVector 51

/-- Exact C1 complete-fiber supports for the antipodal quotient `x ↦ x^2`:
choose two of the four antipodal pairs. -/
def c1OwnedSupports : List Support :=
  [ supportVector 15, supportVector 85, supportVector 165
  , supportVector 90, supportVector 170, supportVector 240 ]

def c1Owned (x : Support) : Bool :=
  c1OwnedSupports.contains x

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

/-- Scoped exact C1-complement leaf. -/
def leaf : PrimitiveBooleanLeaf PrefixKey where
  full := fullFamily
  full_complete := fullPoints_complete
  residual := residualPoints
  residual_sublist := List.filter_sublist
  prefixKey := prefixKey

/-- Local copy of the exact pre-C9 constructor grammar.  This module does not
import the open producer PR. -/
inductive ScopedPreC9Owner where
  | c1 | c2 | c3 | c4 | c5 | c6 | c7 | c8
  deriving Repr, BEq, DecidableEq

/-- Owner function with a generic C1 label.  It can be instantiated by the
integrated producer's `.c1` constructor after that producer is on main. -/
def earlierOwner {Owner : Type} (c1 : Owner) (x : Support) : Option Owner :=
  if c1Owned x then some c1 else none

def scopedEarlierOwner : Support → Option ScopedPreC9Owner :=
  earlierOwner .c1

/-- Standalone exact owner-complement condition required by the C9 producer. -/
def IsExactOwnerComplement {Owner : Type} [DecidableEq Owner]
    (owner : Support → Option Owner) : Prop :=
  ∀ x : Support,
    x ∈ leaf.residual ↔ x ∈ leaf.full.points ∧ owner x = none

/-- The displayed residual is definitionally the complement of the explicit C1
owner inside the complete fixed-weight slice. -/
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

/-- Concrete scoped C1--C8 owner-complement witness.  Only C1 is nonempty in
this local profile. -/
theorem scoped_residual_exact :
    IsExactOwnerComplement scopedEarlierOwner := by
  unfold scopedEarlierOwner
  exact residual_exact ScopedPreC9Owner.c1

/-- Exact selected and collision keys. -/
def collisionKey : PrefixKey := { p1 := 0, p2 := 2, p3 := 0 }
def selectedKey : PrefixKey :=
  { p1 := 1266428118, p2 := 2, p3 := 458186840 }

/-- Full and residual realized-key lists. -/
def fullKeyList : List PrefixKey := fullPoints.map prefixKey
def fullImage : List PrefixKey := fullKeyList.eraseDups
def residualKeyList : List PrefixKey := residualPoints.map prefixKey

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem generator_norm_one :
    fp2Mul normOneGenerator (fp2Conj normOneGenerator) = fp2One := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem generator_half_order :
    fp2PowTwo 30 normOneGenerator =
      ({ re := fieldPrime - 1, im := 0 } : Fp2) := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem generator_full_order :
    fp2PowTwo 31 normOneGenerator = fp2One := by decide

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
theorem c1_owned_supports_valid :
    c1OwnedSupports.Nodup ∧
    c1OwnedSupports.all (fun x => decide (boolWeight x = 4)) = true := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem residual_slice_card : residualPoints.length = 64 := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem residual_prefix_injective : residualKeyList.Nodup := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem collision_full_fiber_exact :
    fullPrefixFiber leaf collisionKey = [t4BlockA, t4BlockB] := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem collision_residual_fiber_empty :
    residualPrefixFiber leaf collisionKey = [] := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem selected_key_exact : prefixKey selectedSupport = selectedKey := by decide

theorem selected_not_c1Owned : c1Owned selectedSupport = false := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem selected_survives : selectedSupport ∈ leaf.residual := by decide

theorem selected_not_earlier : scopedEarlierOwner selectedSupport = none := by
  exact ((scoped_residual_exact selectedSupport).mp selected_survives).2

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem selected_full_prefix_singleton :
    fullPrefixFiber leaf selectedKey = [selectedSupport] := by decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 0 in
theorem selected_residual_prefix_singleton :
    residualPrefixFiber leaf selectedKey = [selectedSupport] := by decide

/-- Exact loss and integral natural scale used by the future producer adapter. -/
def compilerLoss : Nat := 1
def naturalScale : Nat := 2

/-- Definitionally the exact field required by
`C9ResidualMaxFiber.ProfileData.rowSharpMaxFiber`. -/
theorem fullPrefixFiber_rowSharp :
    (fullPrefixFiber leaf selectedKey).length ≤ compilerLoss * naturalScale := by
  rw [selected_full_prefix_singleton]
  decide

/-- The singleton key is also loss one at the exact realized-image scale,
cleared of division: `1 * 69 <= 70`. -/
theorem imageNormalized_rowSharp :
    (fullPrefixFiber leaf selectedKey).length * fullImage.length ≤
      fullPoints.length := by decide

/-- Any genuine `(SE2)` cell supported on this exact residual key inherits the
same loss-one slope payment. -/
theorem slopes_paid
    (slopeCell : SE2Certificate Support Nat)
    (supportsInResidual : List.Sublist slopeCell.supports
      (residualPrefixFiber leaf selectedKey)) :
    slopeCell.slopes.length ≤ compilerLoss * naturalScale := by
  calc
    slopeCell.slopes.length ≤ slopeCell.supports.length :=
      se2_support_injection slopeCell
    _ ≤ (residualPrefixFiber leaf selectedKey).length :=
      supportsInResidual.length_le
    _ ≤ (fullPrefixFiber leaf selectedKey).length :=
      residualPrefixFiber_length_le_fullPrefixFiber leaf selectedKey
    _ ≤ compilerLoss * naturalScale := fullPrefixFiber_rowSharp

/-- Direct C9 payment after a genuine slope projection; no Sidon stage is
invented. -/
def payment
    (slopeCell : SE2Certificate Support Nat)
    (supportsInResidual : List.Sublist slopeCell.supports
      (residualPrefixFiber leaf selectedKey)) :
    ProfilePayment compilerLoss :=
  ProfilePayment.ofDirect .c9 slopeCell.slopes naturalScale compilerLoss
    slopeCell.slopes_nodup (slopes_paid slopeCell supportsInResidual)

@[simp] theorem payment_owner
    (slopeCell : SE2Certificate Support Nat)
    (supportsInResidual : List.Sublist slopeCell.supports
      (residualPrefixFiber leaf selectedKey)) :
    (payment slopeCell supportsInResidual).owner = .c9 := rfl

@[simp] theorem payment_assignedSlopes
    (slopeCell : SE2Certificate Support Nat)
    (supportsInResidual : List.Sublist slopeCell.supports
      (residualPrefixFiber leaf selectedKey)) :
    (payment slopeCell supportsInResidual).assignedSlopes = slopeCell.slopes := rfl

@[simp] theorem payment_naturalScale
    (slopeCell : SE2Certificate Support Nat)
    (supportsInResidual : List.Sublist slopeCell.supports
      (residualPrefixFiber leaf selectedKey)) :
    (payment slopeCell supportsInResidual).naturalScale = 2 := rfl

@[simp] theorem payment_rayBudget
    (slopeCell : SE2Certificate Support Nat)
    (supportsInResidual : List.Sublist slopeCell.supports
      (residualPrefixFiber leaf selectedKey)) :
    (payment slopeCell supportsInResidual).rayBudget = 2 := rfl

/-- Exact deployed-row arithmetic attached to this local profile. -/
theorem deployed_dimensions :
    deployedPrefixDepth = 67447 ∧
    deployedComplementWeight = 981129 ∧
    fixedOutsideWeight = 981125 ∧
    outsideAvailable = 2097144 ∧
    fixedOutsideWeight ≤ outsideAvailable ∧
    3 ≤ deployedPrefixDepth := by decide

/-- Loss-one local charge fits the literal M31 list-row integer budget. -/
theorem loss_one_fits_deployed_budget :
    compilerLoss * naturalScale ≤ deployedBudget := by decide

#print axioms residual_exact
#print axioms scoped_residual_exact
#print axioms selected_not_c1Owned
#print axioms selected_not_earlier
#print axioms generator_norm_one
#print axioms generator_half_order
#print axioms generator_full_order
#print axioms domain_points_are_deployed_roots
#print axioms antipodal_pairs_exact
#print axioms t4_fibers_exact
#print axioms c1_owned_support_card
#print axioms c1_owned_supports_valid
#print axioms residual_prefix_injective
#print axioms selected_full_prefix_singleton
#print axioms fullPrefixFiber_rowSharp
#print axioms imageNormalized_rowSharp
#print axioms slopes_paid
#print axioms payment_owner
#print axioms payment_assignedSlopes
#print axioms payment_naturalScale
#print axioms payment_rayBudget
#print axioms deployed_dimensions
#print axioms loss_one_fits_deployed_budget

end SidonEffectiveImage.M31C9RowSharp
