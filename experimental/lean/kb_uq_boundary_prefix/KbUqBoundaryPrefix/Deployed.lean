import Std

/-!
# KoalaBear deployed arithmetic for tangent-pruned boundary-prefix Q

This module freezes the row constants and the small exact deductions used by
the source-bound proof.  The enormous binomial quotient is intentionally kept
in the independent integer certificate; Lean checks its compiled packet value
and all downstream row arithmetic.
-/

set_option autoImplicit false

namespace KbUqBoundaryPrefix


def basePrime : Nat := 2130706433
def extensionDegree : Nat := 6
def domainSize : Nat := 2097152
def codeDimension : Nat := 1048576
def agreement : Nat := 1116048
def mismatchSize : Nat := 981104
def prefixDimension : Nat := 1048577
def prefixDepth : Nat := 67471
def tangentCharge : Nat := 981104
def budget : Nat := 274980728111395087
def reserveAfterTangent : Nat := 274980728110413983

def firstBoundaryExchange : Nat := 67472
def firstSparseSurvivorExchange : Nat := 67473
def columnFarShellCount : Nat := 913633
def sparseShellCount : Nat := 913632

def tailScaledFloor : Nat := 57198030365
def conditionalQCap : Nat := 57198030366
def sparseConditionalCap : Nat := 57198030365
def certifiedQLowerFloor : Nat := 57198030366
def reserveAfterConditionalQ : Nat := 274980670912383617

def fullBudgetMultiplierFloor : Nat := 4807520
def lastFullMultiplierIntercept : Nat := 58194
def firstExcludedFullMultiplierIntercept : Nat := 58195
def lastFullMultiplierCap : Nat := 274980728109989882
def firstExcludedFullMultiplierCap : Nat := 274980728110903515

def lastFullMultiplierMargin : Nat := 424101
def firstExcludedFullMultiplierExcess : Nat := 489532

def separationLeftSide : Nat := 1715268316138129359421571072
def extensionFieldCardinality : Nat := 93571093019388561295270373781649880353786165192103559169
def separationMargin : Nat := 93571093019388561295270373779934612037648035832681988097

/-- The source-intersection arithmetic behind deletion of the first sparse shell. -/
theorem sourceIntersectionLower
    (sourceHits outsideHits : Nat)
    (hagreement : agreement ≤ sourceHits + outsideHits)
    (hroot : outsideHits ≤ codeDimension - 1) :
    firstSparseSurvivorExchange ≤ sourceHits := by
  change 67473 ≤ sourceHits
  change 1116048 ≤ sourceHits + outsideHits at hagreement
  change outsideHits ≤ 1048575 at hroot
  omega

/-- The deployed source lower is exactly `w+2`. -/
theorem sparseSurvivorExchange_eq_prefixDepth_add_two :
    firstSparseSurvivorExchange = prefixDepth + 2 := by
  decide

/-- The ordinary boundary-prefix seam is `w+1`. -/
theorem firstBoundaryExchange_eq_prefixDepth_add_one :
    firstBoundaryExchange = prefixDepth + 1 := by
  decide

/-- Exact row and branch arithmetic. -/
theorem deployedConstantsExact :
    domainSize - agreement = mismatchSize ∧
    prefixDimension = codeDimension + 1 ∧
    agreement - prefixDimension = prefixDepth ∧
    agreement - (codeDimension - 1) = firstSparseSurvivorExchange ∧
    mismatchSize - prefixDepth = columnFarShellCount ∧
    mismatchSize - prefixDepth - 1 = sparseShellCount ∧
    budget - tangentCharge = reserveAfterTangent := by
  decide

/-- `(b,c)=(0,1)` gives the anchored and pruned packet values. -/
theorem normalizedConditionalCapsExact :
    1 + tailScaledFloor = conditionalQCap ∧
    tailScaledFloor = sparseConditionalCap ∧
    max conditionalQCap sparseConditionalCap = conditionalQCap ∧
    conditionalQCap = certifiedQLowerFloor := by
  decide

/-- The conditional Q charge leaves the printed reserve. -/
theorem conditionalReserveExact :
    reserveAfterTangent - conditionalQCap = reserveAfterConditionalQ ∧
    conditionalQCap ≤ reserveAfterTangent := by
  decide

/-- Exact full-budget-multiplier boundary slice. -/
theorem fullMultiplierBoundaryExact :
    lastFullMultiplierCap + lastFullMultiplierMargin = reserveAfterTangent ∧
    reserveAfterTangent + firstExcludedFullMultiplierExcess =
      firstExcludedFullMultiplierCap ∧
    lastFullMultiplierIntercept + 1 = firstExcludedFullMultiplierIntercept := by
  decide

/-- The extension-pole separation inequality has the printed exact margin. -/
theorem scalarExtensionSeparationExact :
    separationLeftSide + separationMargin = extensionFieldCardinality ∧
    separationLeftSide < extensionFieldCardinality := by
  decide

#print axioms sourceIntersectionLower
#print axioms sparseSurvivorExchange_eq_prefixDepth_add_two
#print axioms firstBoundaryExchange_eq_prefixDepth_add_one
#print axioms deployedConstantsExact
#print axioms normalizedConditionalCapsExact
#print axioms conditionalReserveExact
#print axioms fullMultiplierBoundaryExact
#print axioms scalarExtensionSeparationExact

end KbUqBoundaryPrefix
