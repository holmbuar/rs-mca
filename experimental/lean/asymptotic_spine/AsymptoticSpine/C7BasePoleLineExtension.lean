import AsymptoticSpine.C7BasePoleWitnessLedgerBridge

namespace AsymptoticSpine
namespace BasePoleC7WitnessClass

/-!
# Append the rooted C7 base-pole producer to an earlier closed line

The input line already contains paid earlier profiles on one received line.  Its
flattened assigned-slope list is the literal first-match deletion set.  The
rooted C7 bridge appends one unit profile for every surviving
constant-coefficient slope.

The result preserves duplicate-free ownership and proves the exact line-local
telescopes

`combined budget = prior budget + C7 survivors`,

`combined natural sum = prior natural sum + C7 survivors`.

The added C7 cost is at most the source-side `q - 1` census.  No row-wide
`(UNIF)`, global atlas, survivor nonemptiness, or target comparison is claimed.
-/

/-- Assigned slope list already carried by a closed earlier line. -/
def lineAssignedSlopes {profileCap : Nat}
    (line : ClosedLineLedger 1 profileCap) : List Nat :=
  (line.profiles.map (fun profile => profile.assignedSlopes)).flatten

/-- The earlier line's assigned slopes are duplicate-free by its own ownership
field. -/
theorem lineAssignedSlopes_nodup {profileCap : Nat}
    (line : ClosedLineLedger 1 profileCap) :
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

/-- Append the actual post-earlier C7 singleton profiles to an already-closed
line.  Deleted C7 cells are not installed. -/
def extendLine {profileCap : Nat}
    (data : BasePoleC7WitnessClass)
    (line : ClosedLineLedger 1 profileCap) :
    ClosedLineLedger 1 (profileCap + data.rawSlopes.length) where
  badCount := line.badCount +
    (data.assignedSlopes (lineAssignedSlopes line)).length
  profiles := line.profiles ++
    basePoleC7Profiles (lineAssignedSlopes line) data.rawSlopes
  firstMatchOwnership := by
    rw [List.map_append, List.flatten_append,
      basePoleC7Profiles_flatten_assignedSlopes]
    exact earlier_append_assignedSlopes_nodup data
      (lineAssignedSlopes line) line.firstMatchOwnership
  atlasExhaustive := by
    rw [List.map_append, List.flatten_append,
      basePoleC7Profiles_flatten_assignedSlopes, List.length_append]
    exact Nat.add_le_add_right line.atlasExhaustive _
  profileCountControl := by
    rw [List.length_append]
    have hc7 :
        (basePoleC7Profiles (lineAssignedSlopes line)
          data.rawSlopes).length ≤ data.rawSlopes.length := by
      simpa [basePoleC7Profiles] using
        basePoleC7AssignedSlopes_length_le_raw
          (lineAssignedSlopes line) data.rawSlopes
    exact Nat.add_le_add line.profileCountControl hc7

/-- Appending C7 preserves the exact assigned-slope disjoint union: previous
first-match slopes first, followed by surviving base-pole slopes. -/
theorem extendLine_flatten_assignedSlopes {profileCap : Nat}
    (data : BasePoleC7WitnessClass)
    (line : ClosedLineLedger 1 profileCap) :
    (((data.extendLine line).profiles.map
      (fun profile => profile.assignedSlopes)).flatten) =
      lineAssignedSlopes line ++
        data.assignedSlopes (lineAssignedSlopes line) := by
  change
    (((line.profiles ++
      basePoleC7Profiles (lineAssignedSlopes line) data.rawSlopes).map
        (fun profile => profile.assignedSlopes)).flatten) =
      lineAssignedSlopes line ++
        basePoleC7AssignedSlopes (lineAssignedSlopes line) data.rawSlopes
  rw [List.map_append, List.flatten_append]
  exact congrArg (List.append (lineAssignedSlopes line))
    (basePoleC7Profiles_flatten_assignedSlopes
      (lineAssignedSlopes line) data.rawSlopes)

/-- The combined ray-budget sum is the previous line-local sum plus one unit for
every surviving C7 slope. -/
theorem extendLine_budgetTotal {profileCap : Nat}
    (data : BasePoleC7WitnessClass)
    (line : ClosedLineLedger 1 profileCap) :
    (data.extendLine line).budgetTotal = line.budgetTotal +
      (data.assignedSlopes (lineAssignedSlopes line)).length := by
  change
    listSum ((line.profiles ++
      (basePoleC7AssignedSlopes (lineAssignedSlopes line)
        data.rawSlopes).map basePoleC7Profile).map
          (fun profile => profile.rayBudget)) =
      listSum (line.profiles.map (fun profile => profile.rayBudget)) +
        (basePoleC7AssignedSlopes (lineAssignedSlopes line)
          data.rawSlopes).length
  rw [List.map_append, c7ListSum_append,
    listSum_basePoleC7Profile_rayBudgets]

/-- The combined natural-profile sum has the same exact line-local telescope. -/
theorem extendLine_naturalTotal {profileCap : Nat}
    (data : BasePoleC7WitnessClass)
    (line : ClosedLineLedger 1 profileCap) :
    (data.extendLine line).naturalTotal = line.naturalTotal +
      (data.assignedSlopes (lineAssignedSlopes line)).length := by
  change
    listSum ((line.profiles ++
      (basePoleC7AssignedSlopes (lineAssignedSlopes line)
        data.rawSlopes).map basePoleC7Profile).map
          (fun profile => profile.naturalScale)) =
      listSum (line.profiles.map (fun profile => profile.naturalScale)) +
        (basePoleC7AssignedSlopes (lineAssignedSlopes line)
          data.rawSlopes).length
  rw [List.map_append, c7ListSum_append,
    listSum_basePoleC7Profile_naturalScales]

/-- The combined line's additional C7 ray cost is at most the source-side
`q - 1` census. -/
theorem extendLine_budgetTotal_le_prior_add_qMinusOne {profileCap : Nat}
    (data : BasePoleC7WitnessClass)
    (line : ClosedLineLedger 1 profileCap) :
    (data.extendLine line).budgetTotal ≤
      line.budgetTotal + data.qMinusOne := by
  rw [extendLine_budgetTotal]
  apply Nat.add_le_add_left
  exact Nat.le_trans
    (basePoleC7AssignedSlopes_length_le_raw
      (lineAssignedSlopes line) data.rawSlopes)
    data.rawSlopes_length_le_qMinusOne

/-- The combined line's additional C7 natural-scale cost obeys the same bound. -/
theorem extendLine_naturalTotal_le_prior_add_qMinusOne {profileCap : Nat}
    (data : BasePoleC7WitnessClass)
    (line : ClosedLineLedger 1 profileCap) :
    (data.extendLine line).naturalTotal ≤
      line.naturalTotal + data.qMinusOne := by
  rw [extendLine_naturalTotal]
  apply Nat.add_le_add_left
  exact Nat.le_trans
    (basePoleC7AssignedSlopes_length_le_raw
      (lineAssignedSlopes line) data.rawSlopes)
    data.rawSlopes_length_le_qMinusOne

/-- A concrete earlier line paying slopes `100` and `102`. -/
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
    lineAssignedSlopes (rootedFixture.extendLine extensionFixtureEarlierLine) =
      [100, 102, 101, 103] := by
  decide

/-- The combined fixture has line-local budget and natural sum `4 = 2 + 2`. -/
theorem extensionFixture_totals :
    (rootedFixture.extendLine extensionFixtureEarlierLine).budgetTotal = 4 ∧
      (rootedFixture.extendLine extensionFixtureEarlierLine).naturalTotal = 4 := by
  decide

#print axioms lineAssignedSlopes_nodup
#print axioms earlier_append_assignedSlopes_nodup
#print axioms c7ListSum_append
#print axioms extendLine_flatten_assignedSlopes
#print axioms extendLine_budgetTotal
#print axioms extendLine_naturalTotal
#print axioms extendLine_budgetTotal_le_prior_add_qMinusOne
#print axioms extendLine_naturalTotal_le_prior_add_qMinusOne
#print axioms extensionFixture_assignedSlopes
#print axioms extensionFixture_totals

end BasePoleC7WitnessClass
end AsymptoticSpine
