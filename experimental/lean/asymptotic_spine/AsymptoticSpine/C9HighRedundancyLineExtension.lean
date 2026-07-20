import AsymptoticSpine.C9HighRedundancyDirectSlope

namespace AsymptoticSpine
namespace C9HighRedundancySimplePoleClass

/-!
# Append the high-redundancy C9 producer to an earlier closed line

The input line already contains the paid C1--C8 profiles on one received line,
using the same polynomial compiler loss as the C9 direct-slope profile.  Its
flattened assigned-slope image is the literal first-match deletion set.  The
C9 profile is appended only when some raw slope survives.

The result preserves duplicate-free first-match ownership and the required
line-local order.  It proves exact telescopes for the combined budget and
natural-profile sums, together with the added-cost bounds

`added C9 budget <= paymentLoss`,

`added C9 natural sum <= 1`.

No row-wide `(UNIF)`, global atlas, survivor nonemptiness, or target comparison
is claimed.
-/

/-- Assigned slope image already carried by a closed C1--C8 line. -/
def priorAssignedSlopes {compilerLoss profileCap : Nat}
    (line : ClosedLineLedger compilerLoss profileCap) : List Nat :=
  (line.profiles.map (fun profile => profile.assignedSlopes)).flatten

/-- The prior assigned image is duplicate-free by the line's ownership field. -/
theorem priorAssignedSlopes_nodup {compilerLoss profileCap : Nat}
    (line : ClosedLineLedger compilerLoss profileCap) :
    (priorAssignedSlopes line).Nodup :=
  line.firstMatchOwnership

/-- First-match deletion makes the appended C9 image disjoint from all prior
assigned slopes. -/
theorem prior_append_assignedSlopes_nodup
    (data : C9HighRedundancySimplePoleClass) (prior : List Nat)
    (hprior : prior.Nodup) :
    (prior ++ data.assignedSlopes prior).Nodup := by
  apply List.nodup_append.mpr
  refine ⟨hprior, data.assignedSlopes_nodup prior, ?_⟩
  intro a ha b hb hab
  have hbdata := (mem_assignedSlopes data prior b).mp hb
  exact hbdata.2 (hab ▸ ha)

/-- Local sum telescope for appended natural-number lists. -/
theorem c9ListSum_append : forall xs ys : List Nat,
    listSum (xs ++ ys) = listSum xs + listSum ys := by
  intro xs
  induction xs with
  | nil =>
      intro ys
      simp
  | cons x xs ih =>
      intro ys
      simp [ih, Nat.add_assoc]

/-- Append the actual post-C1--C8 C9 profile to an already-closed line.  The
empty residual installs no profile. -/
def extendLine {profileCap : Nat}
    (data : C9HighRedundancySimplePoleClass)
    (line : ClosedLineLedger data.paymentLoss profileCap) :
    ClosedLineLedger data.paymentLoss (profileCap + 1) where
  badCount := line.badCount +
    (data.assignedSlopes (priorAssignedSlopes line)).length
  profiles := line.profiles ++ data.profiles (priorAssignedSlopes line)
  firstMatchOwnership := by
    rw [List.map_append, List.flatten_append,
      profiles_flatten_assignedSlopes]
    exact prior_append_assignedSlopes_nodup data
      (priorAssignedSlopes line) line.firstMatchOwnership
  atlasExhaustive := by
    rw [List.map_append, List.flatten_append,
      profiles_flatten_assignedSlopes, List.length_append]
    exact Nat.add_le_add_right line.atlasExhaustive _
  profileCountControl := by
    rw [List.length_append]
    exact Nat.add_le_add line.profileCountControl
      (data.profiles_length_le_one (priorAssignedSlopes line))

/-- The combined assigned-slope image is the prior image followed by the
surviving C9 image. -/
theorem extendLine_flatten_assignedSlopes {profileCap : Nat}
    (data : C9HighRedundancySimplePoleClass)
    (line : ClosedLineLedger data.paymentLoss profileCap) :
    (((data.extendLine line).profiles.map
      (fun profile => profile.assignedSlopes)).flatten) =
      priorAssignedSlopes line ++
        data.assignedSlopes (priorAssignedSlopes line) := by
  change
    (((line.profiles ++ data.profiles (priorAssignedSlopes line)).map
      (fun profile => profile.assignedSlopes)).flatten) =
      priorAssignedSlopes line ++
        data.assignedSlopes (priorAssignedSlopes line)
  rw [List.map_append, List.flatten_append]
  exact congrArg (List.append (priorAssignedSlopes line))
    (data.profiles_flatten_assignedSlopes (priorAssignedSlopes line))

/-- Exact combined bad-slope numerator telescope. -/
theorem extendLine_badCount {profileCap : Nat}
    (data : C9HighRedundancySimplePoleClass)
    (line : ClosedLineLedger data.paymentLoss profileCap) :
    (data.extendLine line).badCount = line.badCount +
      (data.assignedSlopes (priorAssignedSlopes line)).length := rfl

/-- Exact line-local ray-budget telescope. -/
theorem extendLine_budgetTotal {profileCap : Nat}
    (data : C9HighRedundancySimplePoleClass)
    (line : ClosedLineLedger data.paymentLoss profileCap) :
    (data.extendLine line).budgetTotal = line.budgetTotal +
      (data.line (priorAssignedSlopes line)).budgetTotal := by
  change
    listSum ((line.profiles ++ data.profiles (priorAssignedSlopes line)).map
      (fun profile => profile.rayBudget)) =
      listSum (line.profiles.map (fun profile => profile.rayBudget)) +
      listSum ((data.profiles (priorAssignedSlopes line)).map
        (fun profile => profile.rayBudget))
  rw [List.map_append, c9ListSum_append]

/-- Exact line-local natural-profile telescope. -/
theorem extendLine_naturalTotal {profileCap : Nat}
    (data : C9HighRedundancySimplePoleClass)
    (line : ClosedLineLedger data.paymentLoss profileCap) :
    (data.extendLine line).naturalTotal = line.naturalTotal +
      (data.line (priorAssignedSlopes line)).naturalTotal := by
  change
    listSum ((line.profiles ++ data.profiles (priorAssignedSlopes line)).map
      (fun profile => profile.naturalScale)) =
      listSum (line.profiles.map (fun profile => profile.naturalScale)) +
      listSum ((data.profiles (priorAssignedSlopes line)).map
        (fun profile => profile.naturalScale))
  rw [List.map_append, c9ListSum_append]

/-- The appended C9 ray cost is at most the polynomial direct-slope loss. -/
theorem extendLine_budgetTotal_le_prior_add_paymentLoss {profileCap : Nat}
    (data : C9HighRedundancySimplePoleClass)
    (line : ClosedLineLedger data.paymentLoss profileCap) :
    (data.extendLine line).budgetTotal <=
      line.budgetTotal + data.paymentLoss := by
  rw [extendLine_budgetTotal]
  exact Nat.add_le_add_left
    (data.line_budgetTotal_le_paymentLoss (priorAssignedSlopes line)) _

/-- The appended C9 natural-profile cost is at most one realized boundary
profile. -/
theorem extendLine_naturalTotal_le_prior_add_one {profileCap : Nat}
    (data : C9HighRedundancySimplePoleClass)
    (line : ClosedLineLedger data.paymentLoss profileCap) :
    (data.extendLine line).naturalTotal <= line.naturalTotal + 1 := by
  rw [extendLine_naturalTotal]
  exact Nat.add_le_add_left
    (data.line_naturalTotal_le_one (priorAssignedSlopes line)) _

/-- Earlier C1 fixture paying raw slope `100` at the same compiler loss. -/
def extensionFixtureEarlierProfile : ProfilePayment fixture.paymentLoss :=
  ProfilePayment.ofDirect .c1 [100] 1 fixture.paymentLoss
    (by decide) (by decide)

/-- One already-closed earlier line. -/
def extensionFixtureEarlierLine : ClosedLineLedger fixture.paymentLoss 1 where
  badCount := 1
  profiles := [extensionFixtureEarlierProfile]
  firstMatchOwnership := by decide
  atlasExhaustive := by decide
  profileCountControl := by decide

/-- The C9 extension deletes raw slope `100` and appends `101,102`. -/
theorem extensionFixture_assignedSlopes :
    priorAssignedSlopes (fixture.extendLine extensionFixtureEarlierLine) =
      [100, 101, 102] := by
  decide

/-- The combined fixture has three covered slopes, two realized profiles,
ray-budget total `28 = 14 + 14`, and natural total `2 = 1 + 1`. -/
theorem extensionFixture_totals :
    (fixture.extendLine extensionFixtureEarlierLine).badCount = 3 /\
    (fixture.extendLine extensionFixtureEarlierLine).profiles.length = 2 /\
    (fixture.extendLine extensionFixtureEarlierLine).budgetTotal = 28 /\
    (fixture.extendLine extensionFixtureEarlierLine).naturalTotal = 2 := by
  decide

#print axioms priorAssignedSlopes_nodup
#print axioms prior_append_assignedSlopes_nodup
#print axioms c9ListSum_append
#print axioms extendLine_flatten_assignedSlopes
#print axioms extendLine_badCount
#print axioms extendLine_budgetTotal
#print axioms extendLine_naturalTotal
#print axioms extendLine_budgetTotal_le_prior_add_paymentLoss
#print axioms extendLine_naturalTotal_le_prior_add_one
#print axioms extensionFixture_assignedSlopes
#print axioms extensionFixture_totals

end C9HighRedundancySimplePoleClass
end AsymptoticSpine
