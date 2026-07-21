import M31QRootedShell.PaddingBridgeAudit
import M31QRootedShell.Deployed

/-!
# Masked diagonal saturation at the deployed Mersenne-31 list row

This stdlib-only module is the finite arithmetic and metadata-preservation
certificate for the successor of the padding-bridge audit.

The polynomial-module input is kept explicit rather than reaxiomatized here:

* the diagonal map identifies padded syzygies with the coordinatewise
  `Q_i`-divisible submodule of the actual-error syzygy module and shifts every
  row degree by `d = R - j`;
* successive minima of a full-rank submodule cannot be smaller than those of
  the ambient module;
* the last actual-error Forney index is at least `K - j + 1`;
* the primitive padded locator row has total Forney degree at most `R`.

From those premises the kernel checks the deployed conclusion: the shifted
padded frame has the same first-three bounds `20765`, `41530`, and `62295` at
every interior weight.  It also checks that a list compiler can attach the new
frame to each marked source key without changing the ordered selector,
root-status masks, semantic owner, refunds, or signed occupancy credits.
-/

namespace M31QRootedShell.MaskedDiagonalSaturation

open M31QRootedShell.PaddingBridgeAudit

/-- Deployed Mersenne-31 code length. -/
def length : Nat := 2097152

/-- Deployed Reed--Solomon dimension. -/
def dimension : Nat := 1048576

/-- Adjacent list-row agreement. -/
def agreement : Nat := 1116023

/-- Canonical boundary radius. -/
def radius : Nat := 981129

/-- Shifted-locator cutoff `K - R`. -/
def cutoff : Nat := 67447

/-- Number of locator columns in one marked source packet. -/
def sourceColumns : Nat := 46

/-- Rank of the syzygy module of a primitive 46-column locator row. -/
def syzygyRank : Nat := 45

/-- Exact cap for the first 44 padded indices after the last-index floor. -/
def paddedPrefix44Cap : Nat := 913681

/-- Deployed rank-46 bounds inherited by the padded frame. -/
def paddedFirstCap : Nat := 20765
def paddedFirstTwoCap : Nat := 41530
def paddedFirstThreeCap : Nat := 62295

/-- Exact number of source keys forced by the signed occupancy ledger. -/
def markedSourceKeyFloor : Nat := 259881

/-- Exact signed allowance below the forbidden-list crossing. -/
def signedOccupancyAllowance : Nat := 259880

/-- Constant part of the signed occupancy identity. -/
def signedOccupancyBaseline : Nat := 16517335

/-- First forbidden list size `B* + 1`. -/
def forbiddenListSize : Nat := 16777216

/-- The deployed constants and the shifted-last-index identity agree exactly. -/
theorem deployed_parameter_identities :
    radius = length - agreement ∧
    cutoff = dimension - radius ∧
    paddedPrefix44Cap = radius - (cutoff + 1) ∧
    sourceColumns - 1 = syzygyRank := by
  decide

/-- Exact signed-occupancy crossing used by the rank-46 source theorem. -/
theorem signed_occupancy_crossing :
    signedOccupancyBaseline + markedSourceKeyFloor = forbiddenListSize ∧
    signedOccupancyAllowance + 1 = markedSourceKeyFloor ∧
    M31QRootedShell.Deployed.Bstar + 1 = forbiddenListSize := by
  decide

/--
The largest masked index cannot lie below the largest actual-error index, and
subtracting the exact common padding degree leaves the deployed padded
last-index floor `K - R + 1 = 67448`.
-/
theorem shifted_last_index_floor
    (j actualLast maskedLast paddedLast : Nat)
    (hj : j ≤ radius)
    (hactual : dimension - j + 1 ≤ actualLast)
    (hinclusion : actualLast ≤ maskedLast)
    (hshift : maskedLast = paddedLast + (radius - j)) :
    cutoff + 1 ≤ paddedLast := by
  simp only [dimension, radius, cutoff] at *
  omega

/-- Removing the last index leaves at most `913681` total degree. -/
theorem padded_prefix44_bound
    (first second third tail41 last : Nat)
    (htotal : first + second + third + tail41 + last ≤ radius)
    (hlast : cutoff + 1 ≤ last) :
    first + second + third + tail41 ≤ paddedPrefix44Cap := by
  simp only [radius, cutoff, paddedPrefix44Cap] at *
  omega

/--
Exact rank-46 arithmetic.  `tail41` is the sum of indices four through 44; its
lower bound records monotonicity of the ordered padded Forney indices.
-/
theorem padded_first_three_bounds
    (first second third tail41 last : Nat)
    (h12 : first ≤ second)
    (h23 : second ≤ third)
    (htail : 41 * third ≤ tail41)
    (htotal : first + second + third + tail41 + last ≤ radius)
    (hlast : cutoff + 1 ≤ last) :
    first ≤ paddedFirstCap ∧
      first + second ≤ paddedFirstTwoCap ∧
      first + second + third ≤ paddedFirstThreeCap := by
  have hprefix := padded_prefix44_bound first second third tail41 last htotal hlast
  simp only [paddedPrefix44Cap, paddedFirstCap, paddedFirstTwoCap,
    paddedFirstThreeCap] at hprefix ⊢
  constructor
  · omega
  constructor <;> omega

/-- The three exact contradiction thresholds used in the preceding proof. -/
theorem rank46_extremal_arithmetic :
    44 * 20766 = 913704 ∧
    41531 + 42 * 20766 = 913703 ∧
    62296 + 41 * 20766 = 913702 ∧
    paddedPrefix44Cap < 913702 := by
  decide

/-- Exact degree-shifted bound inside the diagonal-divisible submodule. -/
theorem masked_first_three_shifted_bound
    (j first second third maskedFirst maskedSecond maskedThird : Nat)
    (hj : j ≤ radius)
    (hfirst : first + second + third ≤ paddedFirstThreeCap)
    (hshift1 : maskedFirst = first + (radius - j))
    (hshift2 : maskedSecond = second + (radius - j))
    (hshift3 : maskedThird = third + (radius - j)) :
    maskedFirst + maskedSecond + maskedThird ≤
      paddedFirstThreeCap + 3 * (radius - j) := by
  omega

/-- The exact margin below the shifted-locator cutoff remains positive. -/
theorem padded_rank_three_margin :
    paddedFirstThreeCap < cutoff ∧
    cutoff - paddedFirstThreeCap = 5152 := by
  decide

/-- Both bands blocked for direct transport are covered by the uniform theorem. -/
theorem direct_transport_blocked_bands_are_covered :
    M31QRootedShell.PaddingBridgeAudit.m31FirstBlockedWeightMax ≤ radius ∧
    M31QRootedShell.PaddingBridgeAudit.m31ThreeBlockedWeightMax ≤ radius := by
  decide

/--
All source information that the compiler is required to retain.  The finite
lists stand for the exact evaluations and masks already attached to a marked
source key; no semantic owner is synthesized here.
-/
structure SourceMetadata where
  sourceKeyId : Nat
  receivedCenter : List Nat
  codewords : List (List Nat)
  exactWeight : Nat
  orderedDomain : List Nat
  orderedAnchors : List Nat
  distinguishedExtra : Nat
  firstAgreementSelector : List (List Nat)
  rootStatusMasks : List M31QRootedShell.PaddingBridgeAudit.RootMask
  semanticOwner : Option Nat
  refunds : List Int
  signedOccupancyCredits : List Int

/--
A marked rank-46 source key together with the exact arithmetic premises supplied
by the source theorem, the diagonal-saturation bridge, and padded primitivity.
-/
structure MarkedRank46Key where
  metadata : SourceMetadata
  actualLast : Nat
  maskedLast : Nat
  paddedFirst : Nat
  paddedSecond : Nat
  paddedThird : Nat
  paddedTail41 : Nat
  paddedLast : Nat
  maskedFirst : Nat
  maskedSecond : Nat
  maskedThird : Nat
  weight_le_radius : metadata.exactWeight ≤ radius
  actual_last_floor : dimension - metadata.exactWeight + 1 ≤ actualLast
  masked_last_mono : actualLast ≤ maskedLast
  last_shift : maskedLast = paddedLast + (radius - metadata.exactWeight)
  padded_sorted12 : paddedFirst ≤ paddedSecond
  padded_sorted23 : paddedSecond ≤ paddedThird
  padded_tail41_floor : 41 * paddedThird ≤ paddedTail41
  padded_total_degree :
    paddedFirst + paddedSecond + paddedThird + paddedTail41 + paddedLast ≤ radius
  first_shift : maskedFirst = paddedFirst + (radius - metadata.exactWeight)
  second_shift : maskedSecond = paddedSecond + (radius - metadata.exactWeight)
  third_shift : maskedThird = paddedThird + (radius - metadata.exactWeight)

/-- The compiled masked diagonal-saturation certificate on one source key. -/
structure SaturatedRank46Key where
  metadata : SourceMetadata
  paddedFirst : Nat
  paddedSecond : Nat
  paddedThird : Nat
  paddedLast : Nat
  maskedFirst : Nat
  maskedSecond : Nat
  maskedThird : Nat
  padded_last_floor : cutoff + 1 ≤ paddedLast
  padded_first_bound : paddedFirst ≤ paddedFirstCap
  padded_first_two_bound : paddedFirst + paddedSecond ≤ paddedFirstTwoCap
  padded_first_three_bound :
    paddedFirst + paddedSecond + paddedThird ≤ paddedFirstThreeCap
  masked_first_three_bound :
    maskedFirst + maskedSecond + maskedThird ≤
      paddedFirstThreeCap + 3 * (radius - metadata.exactWeight)

private theorem key_last_floor (key : MarkedRank46Key) :
    cutoff + 1 ≤ key.paddedLast :=
  shifted_last_index_floor key.metadata.exactWeight key.actualLast key.maskedLast
    key.paddedLast key.weight_le_radius key.actual_last_floor key.masked_last_mono
    key.last_shift

private theorem key_first_three_bounds (key : MarkedRank46Key) :
    key.paddedFirst ≤ paddedFirstCap ∧
      key.paddedFirst + key.paddedSecond ≤ paddedFirstTwoCap ∧
      key.paddedFirst + key.paddedSecond + key.paddedThird ≤
        paddedFirstThreeCap :=
  padded_first_three_bounds key.paddedFirst key.paddedSecond key.paddedThird
    key.paddedTail41 key.paddedLast key.padded_sorted12 key.padded_sorted23
    key.padded_tail41_floor key.padded_total_degree (key_last_floor key)

private theorem key_masked_first_three_bound (key : MarkedRank46Key) :
    key.maskedFirst + key.maskedSecond + key.maskedThird ≤
      paddedFirstThreeCap + 3 * (radius - key.metadata.exactWeight) :=
  masked_first_three_shifted_bound key.metadata.exactWeight key.paddedFirst
    key.paddedSecond key.paddedThird key.maskedFirst key.maskedSecond
    key.maskedThird key.weight_le_radius (key_first_three_bounds key).2.2
    key.first_shift key.second_shift key.third_shift

/-- Compile one source key, changing only its attached algebraic certificate. -/
def compileKey (key : MarkedRank46Key) : SaturatedRank46Key where
  metadata := key.metadata
  paddedFirst := key.paddedFirst
  paddedSecond := key.paddedSecond
  paddedThird := key.paddedThird
  paddedLast := key.paddedLast
  maskedFirst := key.maskedFirst
  maskedSecond := key.maskedSecond
  maskedThird := key.maskedThird
  padded_last_floor := key_last_floor key
  padded_first_bound := (key_first_three_bounds key).1
  padded_first_two_bound := (key_first_three_bounds key).2.1
  padded_first_three_bound := (key_first_three_bounds key).2.2
  masked_first_three_bound := key_masked_first_three_bound key

@[simp] theorem compileKey_metadata (key : MarkedRank46Key) :
    (compileKey key).metadata = key.metadata := rfl

@[simp] theorem compileKey_selector (key : MarkedRank46Key) :
    (compileKey key).metadata.firstAgreementSelector =
      key.metadata.firstAgreementSelector := rfl

@[simp] theorem compileKey_rootStatusMasks (key : MarkedRank46Key) :
    (compileKey key).metadata.rootStatusMasks = key.metadata.rootStatusMasks := rfl

@[simp] theorem compileKey_semanticOwner (key : MarkedRank46Key) :
    (compileKey key).metadata.semanticOwner = key.metadata.semanticOwner := rfl

@[simp] theorem compileKey_refunds (key : MarkedRank46Key) :
    (compileKey key).metadata.refunds = key.metadata.refunds := rfl

@[simp] theorem compileKey_signedOccupancyCredits (key : MarkedRank46Key) :
    (compileKey key).metadata.signedOccupancyCredits =
      key.metadata.signedOccupancyCredits := rfl

/-- Compile every marked source key without selecting, deleting, or duplicating it. -/
def compileAll (keys : List MarkedRank46Key) : List SaturatedRank46Key :=
  keys.map compileKey

@[simp] theorem compileAll_length (keys : List MarkedRank46Key) :
    (compileAll keys).length = keys.length := by
  simp [compileAll]

/-- The exact `259881` source-key floor survives the compiler. -/
theorem marked_source_key_floor_preserved
    (keys : List MarkedRank46Key)
    (hfloor : markedSourceKeyFloor ≤ keys.length) :
    markedSourceKeyFloor ≤ (compileAll keys).length := by
  simpa using hfloor

/-- Source-key identities are unchanged, so no cross-key deduplication occurs. -/
theorem source_key_ids_preserved (keys : List MarkedRank46Key) :
    (compileAll keys).map (fun key => key.metadata.sourceKeyId) =
      keys.map (fun key => key.metadata.sourceKeyId) := by
  simp [compileAll, compileKey]

/-- Ordered first-agreement selectors are unchanged key by key. -/
theorem selectors_preserved (keys : List MarkedRank46Key) :
    (compileAll keys).map (fun key => key.metadata.firstAgreementSelector) =
      keys.map (fun key => key.metadata.firstAgreementSelector) := by
  simp [compileAll, compileKey]

/-- Root-status masks are unchanged key by key. -/
theorem root_status_masks_preserved (keys : List MarkedRank46Key) :
    (compileAll keys).map (fun key => key.metadata.rootStatusMasks) =
      keys.map (fun key => key.metadata.rootStatusMasks) := by
  simp [compileAll, compileKey]

/-- Semantic owners are neither synthesized nor reassigned. -/
theorem semantic_owners_preserved (keys : List MarkedRank46Key) :
    (compileAll keys).map (fun key => key.metadata.semanticOwner) =
      keys.map (fun key => key.metadata.semanticOwner) := by
  simp [compileAll, compileKey]

/-- Refund vectors are unchanged. -/
theorem refunds_preserved (keys : List MarkedRank46Key) :
    (compileAll keys).map (fun key => key.metadata.refunds) =
      keys.map (fun key => key.metadata.refunds) := by
  simp [compileAll, compileKey]

/-- Signed occupancy-credit vectors are unchanged. -/
theorem signed_occupancy_credit_vectors_preserved (keys : List MarkedRank46Key) :
    (compileAll keys).map (fun key => key.metadata.signedOccupancyCredits) =
      keys.map (fun key => key.metadata.signedOccupancyCredits) := by
  simp [compileAll, compileKey]

/-- The aggregate signed occupancy credit is unchanged exactly. -/
theorem signed_occupancy_credit_sum_preserved (keys : List MarkedRank46Key) :
    ((compileAll keys).map
      (fun key => key.metadata.signedOccupancyCredits.sum)).sum =
      (keys.map (fun key => key.metadata.signedOccupancyCredits.sum)).sum := by
  simp [compileAll, compileKey]

/-- The aggregate refund is unchanged exactly. -/
theorem refund_sum_preserved (keys : List MarkedRank46Key) :
    ((compileAll keys).map (fun key => key.metadata.refunds.sum)).sum =
      (keys.map (fun key => key.metadata.refunds.sum)).sum := by
  simp [compileAll, compileKey]

end M31QRootedShell.MaskedDiagonalSaturation
