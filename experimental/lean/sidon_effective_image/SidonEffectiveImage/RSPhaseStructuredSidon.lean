import Std

/-!
# Phase-structured cancellation on one genuine M31 RS primitive leaf

This stdlib-only module restates one deployed-calibration Reed--Solomon leaf
locally.  The moving coordinates are eight actual roots of `T_(2^21)` over the
Mersenne prime.  The earlier C1 owner deletes the six supports made from two
complete antipodal pairs.  The remaining 64 weight-four supports are therefore
an explicit owner complement.

For a support `S`, the monic locator has constant term
`Q_S(0) = ∏_{x ∈ S} x` (the weight is even).  We attach its quadratic phase
`χ(Q_S(0))`.  On the realized second-power-sum image, a fixed-point-free
antipodal swap preserves the second moment and flips this phase because
`p = 3 (mod 4)`.  The 32 printed pairs exhaust the post-C1 residual, so every
realized phase coefficient vanishes.  Hence both the phase-aware L1 aggregate
and its signed collision moment are exactly zero, whereas the unsigned
collision moment is 576.

This is a scoped phase-payment theorem on an actual post-owner RS leaf.  It is
not a full three-coordinate C9 payment, a slope/codeword projection, an
exhaustive first-match atlas, residual add-back, UNIF, or an adjacent-row
certificate.
-/

set_option maxRecDepth 1000000
set_option maxHeartbeats 0

namespace SidonEffectiveImage.RSPhaseStructuredSidon

/-- Deployed Mersenne prime and row constants. -/
def fieldPrime : Nat := 2 ^ 31 - 1
def deployedLength : Nat := 2 ^ 21
def deployedAgreement : Nat := 1116023
def deployedComplementWeight : Nat := 981129
def deployedPrefixDepth : Nat := 67447
def deployedBudget : Nat := 2 ^ 24 - 1
def fixedOutsideWeight : Nat := deployedComplementWeight - 4
def outsideAvailable : Nat := deployedLength - 8

/-- Eight actual M31 Chebyshev-domain points, grouped into four antipodal pairs. -/
def domain : List Nat :=
  [ 434373082, 614288294, 1713110565, 1533195353
  , 1984437538, 380812851, 163046109, 1766670796 ]

/-- Masks of the four antipodal pairs. -/
def antipodalPairMasks : List Nat := [5, 10, 80, 160]

/-- C1 complete-fiber supports: choose two of the four antipodal pairs. -/
def c1OwnedMasks : List Nat := [15, 85, 165, 90, 170, 240]

/-- Sum a natural list. -/
def sumNat : List Nat → Nat
  | [] => 0
  | x :: xs => x + sumNat xs

/-- Sum an integer list. -/
def sumInt : List Int → Int
  | [] => 0
  | x :: xs => x + sumInt xs

/-- Maximum of a natural list, with zero on the empty list. -/
def maxNat : List Nat → Nat
  | [] => 0
  | x :: xs => Nat.max x (maxNat xs)

/-- Executable duplicate-freeness. -/
def noDuplicates [BEq α] : List α → Bool
  | [] => true
  | x :: xs => !xs.contains x && noDuplicates xs

/-- Boolean set equality for duplicate-free finite lists. -/
def sameElements [BEq α] (xs ys : List α) : Bool :=
  xs.all (fun x => ys.contains x) && ys.all (fun y => xs.contains y)

/-- Hamming weight of the low eight bits. -/
def maskWeight (mask : Nat) : Nat :=
  (List.range 8).foldl
    (fun acc i => if Nat.testBit mask i then acc + 1 else acc) 0

/-- Complete weight-four slice on the eight moving coordinates. -/
def fullMasks : List Nat :=
  (List.range 256).filter (fun mask => decide (maskWeight mask = 4))

/-- Explicit post-C1 owner complement. -/
def c1Owned (mask : Nat) : Bool := c1OwnedMasks.contains mask

def residualMasks : List Nat :=
  fullMasks.filter (fun mask => !c1Owned mask)

/-- Fixed-fuel repeated squaring.  Fuel 64 is enough for every exponent used. -/
def powModBits : Nat → Nat → Nat → Nat → Nat → Nat
  | 0, _, _, _, acc => acc
  | fuel + 1, modulus, base, exponent, acc =>
      powModBits fuel modulus ((base * base) % modulus) (exponent / 2)
        (if exponent % 2 = 1 then (acc * base) % modulus else acc)

def powMod (base exponent modulus : Nat) : Nat :=
  powModBits 64 modulus (base % modulus) exponent (1 % modulus)

/-- `T_(2n)(x)=2T_n(x)^2-1`, modulo the Mersenne prime. -/
def chebyshevDouble (x : Nat) : Nat :=
  (2 * (x % fieldPrime) * (x % fieldPrime) + (fieldPrime - 1)) % fieldPrime

/-- Evaluate `T_(2^e)` by repeated doubling. -/
def chebyshevPowTwo : Nat → Nat → Nat
  | 0, x => x % fieldPrime
  | e + 1, x => chebyshevPowTwo e (chebyshevDouble x)

/-- Selected power sum on one support mask. -/
def sumPowerMod (e mask : Nat) : Nat :=
  ((List.range 8).zip domain).foldl
    (fun acc pair =>
      if Nat.testBit mask pair.1 then
        (acc + powMod pair.2 e fieldPrime) % fieldPrime
      else acc)
    0

/-- Realized coarse phase-payment key: the second power sum. -/
def p2Key (mask : Nat) : Nat := sumPowerMod 2 mask

/-- Constant term of the even-weight monic locator. -/
def locatorConstant (mask : Nat) : Nat :=
  ((List.range 8).zip domain).foldl
    (fun acc pair =>
      if Nat.testBit mask pair.1 then (acc * pair.2) % fieldPrime else acc)
    1

/-- Quadratic phase of the locator constant, certified nonzero on the residual. -/
def quadraticPhase (mask : Nat) : Int :=
  if powMod (locatorConstant mask) ((fieldPrime - 1) / 2) fieldPrime = 1
  then 1
  else -1

/-- Realized image only: no ambient `q^R` target is used. -/
def realizedImage : List Nat :=
  (residualMasks.map p2Key).eraseDups

/-- One realized fiber and its unsigned size. -/
def phaseFiber (key : Nat) : List Nat :=
  residualMasks.filter (fun mask => p2Key mask == key)

def phaseFiberSize (key : Nat) : Nat := (phaseFiber key).length

/-- Signed locator-phase coefficient on one realized key. -/
def phaseCoefficient (key : Nat) : Int :=
  sumInt ((phaseFiber key).map quadraticPhase)

/-- Corrected realized-image parameters. -/
def sourceMass : Nat := residualMasks.length
def realizedImageSize : Nat := realizedImage.length
def naturalScale : Nat :=
  (sourceMass + realizedImageSize - 1) / realizedImageSize

/-- Cancellation-sensitive aggregate and signed collision moment. -/
def phaseAwareL1 : Nat :=
  sumNat (realizedImage.map (fun key => (phaseCoefficient key).natAbs))

def phaseCollisionMoment : Nat :=
  sumNat (realizedImage.map (fun key =>
    (phaseCoefficient key * phaseCoefficient key).natAbs))

/-- Unsigned comparison statistics on the same realized image. -/
def unsignedCollisionMoment : Nat :=
  sumNat (realizedImage.map (fun key =>
    phaseFiberSize key * phaseFiberSize key))

def maxUnsignedFiber : Nat :=
  maxNat (realizedImage.map phaseFiberSize)

/-- Canonical first-split-antipodal-pair matching of the 64 residual supports. -/
def cancellationPairs : List (Nat × Nat) :=
  [ (23, 29), (27, 30), (39, 45), (43, 46)
  , (51, 54), (53, 101), (57, 60), (58, 106)
  , (71, 77), (75, 78), (83, 86), (89, 92)
  , (99, 102), (105, 108), (113, 116), (114, 120)
  , (135, 141), (139, 142), (147, 150), (149, 197)
  , (153, 156), (154, 202), (163, 166), (169, 172)
  , (177, 180), (178, 184), (195, 198), (201, 204)
  , (209, 212), (210, 216), (225, 228), (226, 232) ]

/-- Flatten the pairing table. -/
def pairedMasks : List Nat :=
  cancellationPairs.flatMap (fun pair => [pair.1, pair.2])

/-- Each printed pair lies in the residual, preserves `p2`, and flips phase. -/
def cancellationPairCheck (pair : Nat × Nat) : Bool :=
  residualMasks.contains pair.1 &&
  residualMasks.contains pair.2 &&
  (p2Key pair.1 == p2Key pair.2) &&
  (quadraticPhase pair.1 + quadraticPhase pair.2 == 0)

/-- Exact owner-complement predicate over the full eight-bit universe. -/
def ownerComplementCheck : Bool :=
  (List.range 256).all (fun mask =>
    decide (residualMasks.contains mask =
      (fullMasks.contains mask && !c1Owned mask)))

/-- Number of complete antipodal pairs selected by one mask. -/
def completeAntipodalPairCount (mask : Nat) : Nat :=
  (if Nat.testBit mask 0 && Nat.testBit mask 2 then 1 else 0) +
  (if Nat.testBit mask 1 && Nat.testBit mask 3 then 1 else 0) +
  (if Nat.testBit mask 4 && Nat.testBit mask 6 then 1 else 0) +
  (if Nat.testBit mask 5 && Nat.testBit mask 7 then 1 else 0)

/-- All weight-four supports made from exactly two complete antipodal pairs. -/
def completePairOwners : List Nat :=
  fullMasks.filter (fun mask => decide (completeAntipodalPairCount mask = 2))

/-- The six C1 owners are exactly the six unions of two complete antipodal pairs. -/
def c1AntipodalOwnerCheck : Bool :=
  c1OwnedMasks.length == 6 &&
  noDuplicates c1OwnedMasks &&
  c1OwnedMasks.all (fun mask => decide (maskWeight mask = 4)) &&
  c1OwnedMasks.all (fun mask => decide (completeAntipodalPairCount mask = 2)) &&
  sameElements c1OwnedMasks completePairOwners

/-- Euler-criterion outputs are nonzero phases on every residual support. -/
def residualPhaseCheck : Bool :=
  residualMasks.all (fun mask =>
    let e := powMod (locatorConstant mask) ((fieldPrime - 1) / 2) fieldPrime
    (e == 1) || (e == fieldPrime - 1))

/-- Every realized phase coefficient is zero. -/
def phaseCoefficientCheck : Bool :=
  realizedImage.all (fun key => phaseCoefficient key == 0)

/-- Exact finite leaf and domain checks. -/
theorem field_prime_exact : fieldPrime = 2147483647 := by decide

theorem full_slice_card : fullMasks.length = 70 := by decide

theorem c1_owned_card : c1OwnedMasks.length = 6 := by decide

theorem residual_slice_card : residualMasks.length = 64 := by decide

theorem owner_complement_exact : ownerComplementCheck = true := by decide

theorem antipodal_pairs_exact :
    (434373082 + 1713110565) % fieldPrime = 0 ∧
    (614288294 + 1533195353) % fieldPrime = 0 ∧
    (1984437538 + 163046109) % fieldPrime = 0 ∧
    (380812851 + 1766670796) % fieldPrime = 0 := by decide

theorem c1_antipodal_owner_exact : c1AntipodalOwnerCheck = true := by decide

theorem domain_nodup : noDuplicates domain = true := by decide

theorem domain_points_are_deployed_roots :
    domain.all (fun x => chebyshevPowTwo 21 x == 0) = true := by decide

theorem quadratic_phase_defined_on_residual : residualPhaseCheck = true := by decide

/-- The printed involution is a fixed-point-free exhaustive matching. -/
theorem cancellation_pair_count : cancellationPairs.length = 32 := by decide

theorem paired_masks_nodup : noDuplicates pairedMasks = true := by decide

theorem pairing_exhausts_residual :
    sameElements pairedMasks residualMasks = true := by decide

theorem pairing_cancels_p2_phase :
    cancellationPairs.all cancellationPairCheck = true := by decide

/-- Correct realized-image normalization and exact cancellation. -/
theorem realized_image_card : realizedImageSize = 9 := by decide

theorem realized_fiber_sizes :
    realizedImage.map phaseFiberSize = [8, 8, 8, 8, 16, 4, 4, 4, 4] := by decide

theorem phase_coefficients_zero : phaseCoefficientCheck = true := by decide

theorem phase_aware_l1_exact : phaseAwareL1 = 0 := by decide

theorem phase_collision_moment_exact : phaseCollisionMoment = 0 := by decide

theorem unsigned_collision_moment_exact : unsignedCollisionMoment = 576 := by decide

theorem max_unsigned_fiber_exact : maxUnsignedFiber = 16 := by decide

theorem natural_scale_exact : naturalScale = 8 := by decide

/-- The phase-aware aggregate has exact multiplier one at the realized image. -/
def phaseMultiplier : Nat := 1

theorem phase_multiplier_one_payment :
    phaseAwareL1 ≤ (phaseMultiplier - 1) * sourceMass := by decide

/-- The same exact payment in image-compensated form, with `A_eff=L=9`. -/
theorem image_compensated_phase_payment :
    realizedImageSize * phaseAwareL1 ≤
      realizedImageSize * (phaseMultiplier - 1) * sourceMass := by decide

/-- Arithmetic embedding into the deployed M31 list calibration. -/
theorem deployed_dimensions :
    deployedLength = 2097152 ∧
    deployedAgreement = 1116023 ∧
    deployedComplementWeight = 981129 ∧
    fixedOutsideWeight = 981125 ∧
    outsideAvailable = 2097144 ∧
    fixedOutsideWeight ≤ outsideAvailable ∧
    deployedPrefixDepth = 67447 ∧
    deployedBudget = 16777215 := by decide

theorem phase_scale_fits_deployed_budget : naturalScale ≤ deployedBudget := by decide

#print axioms field_prime_exact
#print axioms owner_complement_exact
#print axioms antipodal_pairs_exact
#print axioms c1_antipodal_owner_exact
#print axioms domain_points_are_deployed_roots
#print axioms quadratic_phase_defined_on_residual
#print axioms pairing_exhausts_residual
#print axioms pairing_cancels_p2_phase
#print axioms realized_image_card
#print axioms realized_fiber_sizes
#print axioms phase_coefficients_zero
#print axioms phase_aware_l1_exact
#print axioms phase_collision_moment_exact
#print axioms unsigned_collision_moment_exact
#print axioms natural_scale_exact
#print axioms phase_multiplier_one_payment
#print axioms image_compensated_phase_payment
#print axioms deployed_dimensions
#print axioms phase_scale_fits_deployed_budget

end SidonEffectiveImage.RSPhaseStructuredSidon
