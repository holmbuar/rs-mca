import AsymptoticSpine.C7BasePoleWitnessLedgerBridge

namespace AsymptoticSpine

namespace ProfilePayment

/-!
The integrated closed-ledger structure indexes each profile by a single global
compiler loss.  The C7 adapter is proved at loss `1`; this loss-lifting map lets
its unit payment be appended to an earlier line using any larger loss without
changing the local slope, natural-scale, residual, Sidon, or ray data.
-/

/-- Weaken only the global compiler-loss bound.  Every local payment field is
preserved definitionally. -/
def liftLoss {small large : Nat} (profile : ProfilePayment small)
    (hLoss : small ≤ large) : ProfilePayment large where
  owner := profile.owner
  assignedSlopes := profile.assignedSlopes
  assignedSlopes_nodup := profile.assignedSlopes_nodup
  naturalScale := profile.naturalScale
  residualBudget := profile.residualBudget
  sidonBudget := profile.sidonBudget
  rayBudget := profile.rayBudget
  residualLoss := profile.residualLoss
  sidonLoss := profile.sidonLoss
  rayLoss := profile.rayLoss
  residualToFull := profile.residualToFull
  imageNormalizedSidon := profile.imageNormalizedSidon
  rayCompiler := profile.rayCompiler
  distinctSlopePayment := profile.distinctSlopePayment
  compilerLossDominates :=
    Nat.le_trans profile.compilerLossDominates hLoss

@[simp] theorem liftLoss_owner {small large : Nat}
    (profile : ProfilePayment small) (hLoss : small ≤ large) :
    (profile.liftLoss hLoss).owner = profile.owner := rfl

@[simp] theorem liftLoss_assignedSlopes {small large : Nat}
    (profile : ProfilePayment small) (hLoss : small ≤ large) :
    (profile.liftLoss hLoss).assignedSlopes = profile.assignedSlopes := rfl

@[simp] theorem liftLoss_naturalScale {small large : Nat}
    (profile : ProfilePayment small) (hLoss : small ≤ large) :
    (profile.liftLoss hLoss).naturalScale = profile.naturalScale := rfl

@[simp] theorem liftLoss_residualBudget {small large : Nat}
    (profile : ProfilePayment small) (hLoss : small ≤ large) :
    (profile.liftLoss hLoss).residualBudget = profile.residualBudget := rfl

@[simp] theorem liftLoss_sidonBudget {small large : Nat}
    (profile : ProfilePayment small) (hLoss : small ≤ large) :
    (profile.liftLoss hLoss).sidonBudget = profile.sidonBudget := rfl

@[simp] theorem liftLoss_rayBudget {small large : Nat}
    (profile : ProfilePayment small) (hLoss : small ≤ large) :
    (profile.liftLoss hLoss).rayBudget = profile.rayBudget := rfl

end ProfilePayment

namespace BasePoleC7WitnessClass

/-!
# Append the conditional C7 base-pole adapter to an earlier closed line

The input line already contains paid earlier profiles on one supplied received
line.  Its flattened assigned-slope list is used as the literal deletion set.
Given the explicit fields of `BasePoleC7WitnessClass`, the C7 adapter appends one
unit profile for every surviving constant-coefficient slope.

The result preserves duplicate-free numeric ownership and proves the exact
line-local telescopes

`combined budget = prior budget + C7 survivors`,

`combined natural sum = prior natural sum + C7 survivors`.

The C7 profiles are proved at compiler loss `1` and lifted to any supplied
`compilerLoss ≥ 1` without changing their unit ray budget.  The added cost is at
most the assumed source-side `q - 1` census.

This module does not formalize the finite-field source theorem, select an active
semantic atlas, prove line completeness, establish row-wide `(UNIF)`, assert
survivor nonemptiness, or compare with a target.
-/

/-- Assigned slope list already carried by a supplied closed line. -/
def lineAssignedSlopes {compilerLoss profileCap : Nat}
    (line : ClosedLineLedger compilerLoss profileCap) : List Nat :=
  (line.profiles.map (fun profile => profile.assignedSlopes)).flatten

/-- The earlier line's assigned slopes are duplicate-free by its supplied
ownership field. -/
theorem lineAssignedSlopes_nodup {compilerLoss profileCap : Nat}
    (line : ClosedLineLedger compilerLoss profileCap) :
    (lineAssignedSlopes line).Nodup :=
  line.firstMatchOwnership

/-- Deletion makes the appended C7 survivor list disjoint from every earlier
assigned slope. -/
theorem earlier_append_assignedSlopes_nodup
    (data : BasePoleC7WitnessClass) (earlier : List Nat)
    (hearlier : earlier.Nodup) :
    (earlier ++ data.assignedSlopes earlier).Nodup := by
  apply List.nodup_append.mpr
  refine ⟨hearlier, ?_, ?_⟩
  · exact basePoleC7AssignedSlopes_nodup earlier data.rawSlopes
      data.rawSlopes_nodup
  · intro a ha b hb hab
    have hbdata := (mem_assignedSlopes data earlier b).1 hb
    exact hbdata.2 (hab ▸ ha)

/-- Local payment telescope for appending two natural-number budget lists. -/
theorem c7ListSum_append : ∀ xs ys : List Nat,
    listSum (xs ++ ys) = listSum xs + listSum ys := by
  intro xs
  induction xs with
  | nil =>
      intro ys
      simp
  | cons x xs ih =>
      intro ys
      simp [ih, Nat.add_assoc]

/-- Surviving unit C7 profiles lifted into an arbitrary larger compiler loss.
The lift preserves every local numerical field. -/
def basePoleC7ProfilesAtLoss {compilerLoss : Nat}
    (hLoss : 1 ≤ compilerLoss) (earlier raw : List Nat) :
    List (ProfilePayment compilerLoss) :=
  (basePoleC7Profiles earlier raw).map
    (fun profile => profile.liftLoss hLoss)

/-- Loss lifting does not change the flattened post-deletion slope image. -/
theorem basePoleC7ProfilesAtLoss_flatten_assignedSlopes
    {compilerLoss : Nat} (hLoss : 1 ≤ compilerLoss)
    (earlier raw : List Nat) :
    ((basePoleC7ProfilesAtLoss hLoss earlier raw).map
      (fun profile => profile.assignedSlopes)).flatten =
        basePoleC7AssignedSlopes earlier raw := by
  simpa [basePoleC7ProfilesAtLoss, List.map_map] using
    basePoleC7Profiles_flatten_assignedSlopes earlier raw

/-- Loss lifting preserves the exact unit C7 ray-budget sum. -/
theorem basePoleC7ProfilesAtLoss_budgetTotal
    {compilerLoss : Nat} (hLoss : 1 ≤ compilerLoss)
    (earlier raw : List Nat) :
    listSum ((basePoleC7ProfilesAtLoss hLoss earlier raw).map
      (fun profile => profile.rayBudget)) =
        (basePoleC7AssignedSlopes earlier raw).length := by
  simpa [basePoleC7ProfilesAtLoss, basePoleC7Profiles,
    List.map_map] using
      listSum_basePoleC7Profile_rayBudgets
        (basePoleC7AssignedSlopes earlier raw)

/-- Loss lifting also preserves the exact unit natural-scale sum. -/
theorem basePoleC7ProfilesAtLoss_naturalTotal
    {compilerLoss : Nat} (hLoss : 1 ≤ compilerLoss)
    (earlier raw : List Nat) :
    listSum ((basePoleC7ProfilesAtLoss hLoss earlier raw).map
      (fun profile => profile.naturalScale)) =
        (basePoleC7AssignedSlopes earlier raw).length := by
  simpa [basePoleC7ProfilesAtLoss, basePoleC7Profiles,
    List.map_map] using
      listSum_basePoleC7Profile_naturalScales
        (basePoleC7AssignedSlopes earlier raw)

/-- Append the post-earlier C7 singleton profiles to an already-closed numeric
line at any compiler loss at least one.  Deleted C7 cells are not installed. -/
def extendLine {compilerLoss profileCap : Nat}
    (hLoss : 1 ≤ compilerLoss)
    (data : BasePoleC7WitnessClass)
    (line : ClosedLineLedger compilerLoss profileCap) :
    ClosedLineLedger compilerLoss
      (profileCap + data.rawSlopes.length) where
  badCount := line.badCount +
    (data.assignedSlopes (lineAssignedSlopes line)).length
  profiles := line.profiles ++
    basePoleC7ProfilesAtLoss hLoss
      (lineAssignedSlopes line) data.rawSlopes
  firstMatchOwnership := by
    rw [List.map_append, List.flatten_append,
      basePoleC7ProfilesAtLoss_flatten_assignedSlopes]
    exact earlier_append_assignedSlopes_nodup data
      (lineAssignedSlopes line) line.firstMatchOwnership
  atlasExhaustive := by
    rw [List.map_append, List.flatten_append,
      basePoleC7ProfilesAtLoss_flatten_assignedSlopes,
      List.length_append]
    exact Nat.add_le_add_right line.atlasExhaustive _
  profileCountControl := by
    rw [List.length_append]
    have hc7 :
        (basePoleC7ProfilesAtLoss hLoss
          (lineAssignedSlopes line) data.rawSlopes).length ≤
            data.rawSlopes.length := by
      simpa [basePoleC7ProfilesAtLoss, basePoleC7Profiles] using
        basePoleC7AssignedSlopes_length_le_raw
          (lineAssignedSlopes line) data.rawSlopes
    exact Nat.add_le_add line.profileCountControl hc7

/-- Appending C7 preserves the exact assigned-slope disjoint union: previous
first-match slopes first, followed by surviving base-pole slopes. -/
theorem extendLine_flatten_assignedSlopes
    {compilerLoss profileCap : Nat}
    (hLoss : 1 ≤ compilerLoss)
    (data : BasePoleC7WitnessClass)
    (line : ClosedLineLedger compilerLoss profileCap) :
    (((extendLine hLoss data line).profiles.map
      (fun profile => profile.assignedSlopes)).flatten) =
      lineAssignedSlopes line ++
        data.assignedSlopes (lineAssignedSlopes line) := by
  change
    (((line.profiles ++ basePoleC7ProfilesAtLoss hLoss
      (lineAssignedSlopes line) data.rawSlopes).map
        (fun profile => profile.assignedSlopes)).flatten) =
      lineAssignedSlopes line ++
        basePoleC7AssignedSlopes (lineAssignedSlopes line) data.rawSlopes
  rw [List.map_append, List.flatten_append]
  exact congrArg (List.append (lineAssignedSlopes line))
    (basePoleC7ProfilesAtLoss_flatten_assignedSlopes hLoss
      (lineAssignedSlopes line) data.rawSlopes)

/-- The combined ray-budget sum is the previous line-local sum plus one unit for
every surviving C7 slope, independently of the larger compiler loss. -/
theorem extendLine_budgetTotal
    {compilerLoss profileCap : Nat}
    (hLoss : 1 ≤ compilerLoss)
    (data : BasePoleC7WitnessClass)
    (line : ClosedLineLedger compilerLoss profileCap) :
    (extendLine hLoss data line).budgetTotal = line.budgetTotal +
      (data.assignedSlopes (lineAssignedSlopes line)).length := by
  change
    listSum ((line.profiles ++ basePoleC7ProfilesAtLoss hLoss
      (lineAssignedSlopes line) data.rawSlopes).map
        (fun profile => profile.rayBudget)) =
      listSum (line.profiles.map (fun profile => profile.rayBudget)) +
        (basePoleC7AssignedSlopes (lineAssignedSlopes line)
          data.rawSlopes).length
  rw [List.map_append, c7ListSum_append,
    basePoleC7ProfilesAtLoss_budgetTotal]

/-- The combined natural-profile sum has the same exact line-local telescope. -/
theorem extendLine_naturalTotal
    {compilerLoss profileCap : Nat}
    (hLoss : 1 ≤ compilerLoss)
    (data : BasePoleC7WitnessClass)
    (line : ClosedLineLedger compilerLoss profileCap) :
    (extendLine hLoss data line).naturalTotal = line.naturalTotal +
      (data.assignedSlopes (lineAssignedSlopes line)).length := by
  change
    listSum ((line.profiles ++ basePoleC7ProfilesAtLoss hLoss
      (lineAssignedSlopes line) data.rawSlopes).map
        (fun profile => profile.naturalScale)) =
      listSum (line.profiles.map (fun profile => profile.naturalScale)) +
        (basePoleC7AssignedSlopes (lineAssignedSlopes line)
          data.rawSlopes).length
  rw [List.map_append, c7ListSum_append,
    basePoleC7ProfilesAtLoss_naturalTotal]

/-- The combined line's additional C7 ray cost is at most the assumed
source-side `q - 1` census. -/
theorem extendLine_budgetTotal_le_prior_add_qMinusOne
    {compilerLoss profileCap : Nat}
    (hLoss : 1 ≤ compilerLoss)
    (data : BasePoleC7WitnessClass)
    (line : ClosedLineLedger compilerLoss profileCap) :
    (extendLine hLoss data line).budgetTotal ≤
      line.budgetTotal + data.qMinusOne := by
  rw [extendLine_budgetTotal]
  apply Nat.add_le_add_left
  exact Nat.le_trans
    (basePoleC7AssignedSlopes_length_le_raw
      (lineAssignedSlopes line) data.rawSlopes)
    data.rawSlopes_length_le_qMinusOne

/-- The combined line's additional C7 natural-scale cost obeys the same bound. -/
theorem extendLine_naturalTotal_le_prior_add_qMinusOne
    {compilerLoss profileCap : Nat}
    (hLoss : 1 ≤ compilerLoss)
    (data : BasePoleC7WitnessClass)
    (line : ClosedLineLedger compilerLoss profileCap) :
    (extendLine hLoss data line).naturalTotal ≤
      line.naturalTotal + data.qMinusOne := by
  rw [extendLine_naturalTotal]
  apply Nat.add_le_add_left
  exact Nat.le_trans
    (basePoleC7AssignedSlopes_length_le_raw
      (lineAssignedSlopes line) data.rawSlopes)
    data.rawSlopes_length_le_qMinusOne

/-- A concrete loss-one earlier line paying slopes `100` and `102`. -/
def extensionFixtureEarlierProfile100 : ProfilePayment 1 :=
  ProfilePayment.ofDirect .c1 [100] 1 1 (by decide) (by decide)

def extensionFixtureEarlierProfile102 : ProfilePayment 1 :=
  ProfilePayment.ofDirect .c2 [102] 1 1 (by decide) (by decide)

def extensionFixtureEarlierLine : ClosedLineLedger 1 2 where
  badCount := 2
  profiles := [extensionFixtureEarlierProfile100,
    extensionFixtureEarlierProfile102]
  firstMatchOwnership := by decide
  atlasExhaustive := by decide
  profileCountControl := by decide

/-- The rooted fixture appends only slopes `101` and `103`; the earlier-owned
`100` and `102` cells are deleted. -/
theorem extensionFixture_assignedSlopes :
    lineAssignedSlopes
      (extendLine (by decide) rootedFixture extensionFixtureEarlierLine) =
        [100, 102, 101, 103] := by
  decide

/-- The loss-one fixture has budget and natural sum `4 = 2 + 2`. -/
theorem extensionFixture_totals :
    (extendLine (by decide) rootedFixture
      extensionFixtureEarlierLine).budgetTotal = 4 ∧
    (extendLine (by decide) rootedFixture
      extensionFixtureEarlierLine).naturalTotal = 4 := by
  decide

/-- A larger-loss earlier line.  Its two direct earlier profiles have ray budget
`3` each; the lifted C7 profiles retain ray budget `1` each. -/
def extensionFixtureEarlierProfile100Loss3 : ProfilePayment 3 :=
  ProfilePayment.ofDirect .c1 [100] 1 3 (by decide) (by decide)

def extensionFixtureEarlierProfile102Loss3 : ProfilePayment 3 :=
  ProfilePayment.ofDirect .c2 [102] 1 3 (by decide) (by decide)

def extensionFixtureEarlierLineLoss3 : ClosedLineLedger 3 2 where
  badCount := 2
  profiles := [extensionFixtureEarlierProfile100Loss3,
    extensionFixtureEarlierProfile102Loss3]
  firstMatchOwnership := by decide
  atlasExhaustive := by decide
  profileCountControl := by decide

/-- Generic loss lifting preserves the unit local C7 budget: the combined budget
is `6 + 2 = 8`, while the natural sum is `2 + 2 = 4`. -/
theorem extensionFixture_loss3_totals :
    (extendLine (by decide) rootedFixture
      extensionFixtureEarlierLineLoss3).budgetTotal = 8 ∧
    (extendLine (by decide) rootedFixture
      extensionFixtureEarlierLineLoss3).naturalTotal = 4 := by
  decide

#print axioms ProfilePayment.liftLoss
#print axioms lineAssignedSlopes_nodup
#print axioms earlier_append_assignedSlopes_nodup
#print axioms c7ListSum_append
#print axioms basePoleC7ProfilesAtLoss_flatten_assignedSlopes
#print axioms basePoleC7ProfilesAtLoss_budgetTotal
#print axioms basePoleC7ProfilesAtLoss_naturalTotal
#print axioms extendLine_flatten_assignedSlopes
#print axioms extendLine_budgetTotal
#print axioms extendLine_naturalTotal
#print axioms extendLine_budgetTotal_le_prior_add_qMinusOne
#print axioms extendLine_naturalTotal_le_prior_add_qMinusOne
#print axioms extensionFixture_assignedSlopes
#print axioms extensionFixture_totals
#print axioms extensionFixture_loss3_totals

end BasePoleC7WitnessClass
end AsymptoticSpine
