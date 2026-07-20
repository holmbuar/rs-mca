import AsymptoticSpine.ClosedLedgerExtension
import AsymptoticSpine.HighKappaCoverage

namespace AsymptoticSpine
namespace C8ShallowClosure

/-!
# Shallow-prefix C8 residual producer

This module turns the existing kernel-dimension-independent shallow-prefix
closure theorem into one honest C8 `ProfilePayment` and then appends that
post-deletion profile to an earlier closed line.

The source object is an actual supplied residual chart: its support projection
is a sublist of the reindexed ambient prefix chart, and its distinct slopes are
carried by an `(SE2)` certificate.  The existing closure theorem gives

`number of assigned slopes ≤ |B|^w * (1 + average)`

for every printed residual-kernel label.  That is a direct C8 slope payment, so
this adapter uses `ProfilePayment.ofDirect`; it does not manufacture a Sidon
claim.

The module does not prove that a received line has such a chart, that the
first-match C8 atlas is exhaustive, that the prefix is asymptotically shallow,
or that deep-prefix `(MI)`/`(MA)`, row-wide `(UNIF)`, target comparison, or row
closure holds.
-/

/-- One supplied post-earlier-owner C8 residual chart in the shallow-prefix
closure regime. -/
structure ProfileData (Support Eff Raw : Type)
    [DecidableEq Eff] [DecidableEq Raw] where
  bridge : PrefixFiberBridge Support Eff Raw
  syndromeKey : Eff
  slopeCell : SE2Certificate Support Nat
  chartInclusion : List.Sublist slopeCell.supports
    (bridge.depthPrefixChart (bridge.toPrefix syndromeKey))
  bounds : ShallowPrefixClosureBounds bridge.fullSlice.length
  kernelDim : Nat

/-- Finite loss furnished by the shallow effective-span bound. -/
def ProfileData.compilerLoss
    {Support Eff Raw : Type} [DecidableEq Eff] [DecidableEq Raw]
    (data : ProfileData Support Eff Raw) : Nat :=
  data.bounds.baseSize ^ data.bounds.prefixDepth

/-- Natural profile scale used by the direct `(RC)` conclusion. -/
def ProfileData.naturalScale
    {Support Eff Raw : Type} [DecidableEq Eff] [DecidableEq Raw]
    (data : ProfileData Support Eff Raw) : Nat :=
  1 + data.bounds.average

/-- The existing shallow-prefix closure theorem pays the actual supplied slope
list, independently of the printed kernel-dimension label. -/
theorem ProfileData.slopes_paid
    {Support Eff Raw : Type} [DecidableEq Eff] [DecidableEq Raw]
    (data : ProfileData Support Eff Raw) :
    data.slopeCell.slopes.length ≤ data.compilerLoss * data.naturalScale := by
  have h := balancedCoreShallowClosure_to_directRC data.bridge data.syndromeKey
    data.slopeCell data.chartInclusion data.bounds data.kernelDim
  simpa [ProfileData.compilerLoss, ProfileData.naturalScale,
    KernelIndependentDirectRC, DirectRC] using h

/-- Install the supplied C8 chart as a directly paid semantic profile. -/
def ProfileData.payment
    {Support Eff Raw : Type} [DecidableEq Eff] [DecidableEq Raw]
    (data : ProfileData Support Eff Raw) :
    ProfilePayment data.compilerLoss :=
  ProfilePayment.ofDirect .c8 data.slopeCell.slopes data.naturalScale
    data.compilerLoss data.slopeCell.slopes_nodup data.slopes_paid

@[simp] theorem ProfileData.payment_owner
    {Support Eff Raw : Type} [DecidableEq Eff] [DecidableEq Raw]
    (data : ProfileData Support Eff Raw) :
    data.payment.owner = .c8 := rfl

@[simp] theorem ProfileData.payment_assignedSlopes
    {Support Eff Raw : Type} [DecidableEq Eff] [DecidableEq Raw]
    (data : ProfileData Support Eff Raw) :
    data.payment.assignedSlopes = data.slopeCell.slopes := rfl

/-- Append the paid C8 chart after all earlier owners on one line.  The explicit
cross-disjointness proof is the remaining slope-level first-match obligation. -/
def ProfileData.extendLine
    {Support Eff Raw : Type} [DecidableEq Eff] [DecidableEq Raw]
    {profileCap : Nat} (data : ProfileData Support Eff Raw)
    (line : ClosedLineLedger data.compilerLoss profileCap)
    (hdisjoint : ∀ gamma ∈ line.assignedSlopeList,
      gamma ∉ data.slopeCell.slopes) :
    ClosedLineLedger data.compilerLoss (profileCap + 1) :=
  line.appendPayment data.payment hdisjoint

/-- The C8 extension has the exact line-local ray-budget telescope. -/
theorem ProfileData.extendLine_budgetTotal
    {Support Eff Raw : Type} [DecidableEq Eff] [DecidableEq Raw]
    {profileCap : Nat} (data : ProfileData Support Eff Raw)
    (line : ClosedLineLedger data.compilerLoss profileCap)
    (hdisjoint : ∀ gamma ∈ line.assignedSlopeList,
      gamma ∉ data.slopeCell.slopes) :
    (data.extendLine line hdisjoint).budgetTotal =
      line.budgetTotal + data.compilerLoss * data.naturalScale := by
  simpa [ProfileData.extendLine, ProfileData.payment] using
    (ClosedLineLedger.appendPayment_budgetTotal line data.payment hdisjoint)

/-- The C8 extension has the exact line-local natural-scale telescope. -/
theorem ProfileData.extendLine_naturalTotal
    {Support Eff Raw : Type} [DecidableEq Eff] [DecidableEq Raw]
    {profileCap : Nat} (data : ProfileData Support Eff Raw)
    (line : ClosedLineLedger data.compilerLoss profileCap)
    (hdisjoint : ∀ gamma ∈ line.assignedSlopeList,
      gamma ∉ data.slopeCell.slopes) :
    (data.extendLine line hdisjoint).naturalTotal =
      line.naturalTotal + data.naturalScale := by
  simpa [ProfileData.extendLine, ProfileData.payment] using
    (ClosedLineLedger.appendPayment_naturalTotal line data.payment hdisjoint)

/-! ## Exact large-label fixture -/

def fixture : ProfileData Nat Nat Nat where
  bridge := affineToyBridge
  syndromeKey := 1
  slopeCell := highKappaToySE2
  chartInclusion := by decide
  bounds := highKappaToyBounds
  kernelDim := 1000000

def fixtureEarlierProfile : ProfilePayment fixture.compilerLoss :=
  ProfilePayment.ofDirect .c1 [5] 1 fixture.compilerLoss
    (by decide) (by decide)

def fixtureEarlierLine : ClosedLineLedger fixture.compilerLoss 1 where
  badCount := 1
  profiles := [fixtureEarlierProfile]
  firstMatchOwnership := by decide
  atlasExhaustive := by decide
  profileCountControl := by decide

/-- The million-dimensional label is inert: the actual chart slopes `[7,9]`
are appended after the earlier C1 slope `5`. -/
theorem fixture_assignedSlopes :
    (fixture.extendLine fixtureEarlierLine (by decide)).assignedSlopeList =
      [5, 7, 9] := by
  decide

/-- Exact finite telescope: prior budget `4`, C8 budget `12`, natural sum
`1 + 3`, and three covered slopes. -/
theorem fixture_totals :
    (fixture.extendLine fixtureEarlierLine (by decide)).budgetTotal = 16 /\
    (fixture.extendLine fixtureEarlierLine (by decide)).naturalTotal = 4 /\
    (fixture.extendLine fixtureEarlierLine (by decide)).badCount = 3 := by
  decide

#print axioms ProfileData.slopes_paid
#print axioms ProfileData.extendLine_budgetTotal
#print axioms ProfileData.extendLine_naturalTotal
#print axioms fixture_assignedSlopes
#print axioms fixture_totals

end C8ShallowClosure
end AsymptoticSpine
