import AsymptoticSpine.C8OnePencilLineExtension

namespace AsymptoticSpine

/-!
# Exact F97 C8 two-cell first-match producer

The source certificate
`experimental/notes/thresholds/bc_first_interior_f97_two_cell_certificate.md`
constructs one literal received line over `F_97 / mu_16`.  Its retained
first-interior incidence has four rooted line-ray witnesses:

* `z0` at slope `0`;
* `z1` at slope `1`;
* `z2a` and `z2b` at the common slope `2`.

Two distinct common-GCD projective-plane cells cover the witnesses:

`A = {z0,z1,z2a}` and `B = {z0,z1,z2b}`.

Both raw cells project to the same slope image `{0,1,2}`.  Therefore summing
raw per-chart slope counts gives `3+3=6`, while slope-level first match assigns
all three slopes to `A` and leaves `B` empty.  This module records that exact
rooted chain and installs the correctly deleted slope image as one direct C8
payment at unit natural scale with loss `3`.

The finite-field locator identities and the exhaustive projective-plane
censuses are owned by the source certificate.  The Lean module formalizes their
exact witness/cell/slope interface consequence.  No arbitrary-line atlas,
deployed-row theorem, higher-dimensional chart exhaustion, or row-wide `(UNIF)`
is asserted.
-/

/-- Rooted witness identifiers: `0=z0`, `1=z1`, `2=z2a`, `3=z2b`. -/
def f97C8Witnesses : List Nat := [0, 1, 2, 3]

/-- Final slope map of the exact source fixture. -/
def f97C8Slope : Nat -> Nat
  | 0 => 0
  | 1 => 1
  | 2 => 2
  | 3 => 2
  | w => w

/-- First common-GCD projective-plane cell. -/
def f97C8CellA : List Nat := [0, 1, 2]

/-- Second common-GCD projective-plane cell. -/
def f97C8CellB : List Nat := [0, 1, 3]

/-- Ordered source cells. -/
def f97C8WitnessCells : List (List Nat) := [f97C8CellA, f97C8CellB]

/-- Raw distinct-slope image of each source cell. -/
def f97C8CellSlopeImages : List (List Nat) :=
  f97C8WitnessCells.map fun cell => realizedKeys cell f97C8Slope

/-- The two source cells cover all four rooted witnesses. -/
theorem f97C8WitnessCells_cover :
    forall w, w ∈ f97C8WitnessCells.flatten <-> w ∈ f97C8Witnesses := by
  intro w
  by_cases h0 : w = 0 <;>
    by_cases h1 : w = 1 <;>
    by_cases h2 : w = 2 <;>
    by_cases h3 : w = 3 <;>
    simp [f97C8WitnessCells, f97C8CellA, f97C8CellB,
      f97C8Witnesses, h0, h1, h2, h3]

/-- Each source cell has the same three-slope raw projection. -/
theorem f97C8CellSlopeImages_exact :
    f97C8CellSlopeImages = [[0, 1, 2], [0, 1, 2]] := by
  decide

/-- The complete rooted witness catalogue has exactly three distinct slopes. -/
theorem f97C8WitnessSlopeImage_exact :
    realizedKeys f97C8Witnesses f97C8Slope = [0, 1, 2] := by
  decide

/-- Ordered slope-level first match assigns all slopes to cell `A` and leaves
cell `B` empty. -/
theorem f97C8FirstMatchSlopeLeaves :
    firstMatchLeaves [] f97C8CellSlopeImages = [[0, 1, 2], []] := by
  decide

/-- Raw per-chart summation overpays the exact line by a factor two. -/
theorem f97C8RawChartSlopeTotal :
    listSum (f97C8CellSlopeImages.map List.length) = 6 := by
  decide

/-- The correct first-match slope total is three. -/
theorem f97C8FirstMatchSlopeTotal :
    listSum ((firstMatchLeaves [] f97C8CellSlopeImages).map List.length) = 3 := by
  decide

/-- The later witness `z2b` is removed because its slope `2` was already paid
by the first cell through `z2a`. -/
theorem f97C8LaterWitnessSlopeAlreadyPaid :
    f97C8Slope 3 ∈ (firstMatchLeaves [] f97C8CellSlopeImages).flatten := by
  decide

/-- Actual F97 slope image surviving arbitrary earlier C1--C7 owners. -/
def f97C8AssignedSlopes (earlier : List Nat) : List Nat :=
  [0, 1, 2].filter fun gamma => decide (gamma ∉ earlier)

@[simp] theorem mem_f97C8AssignedSlopes (earlier : List Nat) (gamma : Nat) :
    gamma ∈ f97C8AssignedSlopes earlier <->
      gamma ∈ [0, 1, 2] /\ gamma ∉ earlier := by
  simp [f97C8AssignedSlopes]

/-- First-match deletion preserves distinctness. -/
theorem f97C8AssignedSlopes_nodup (earlier : List Nat) :
    (f97C8AssignedSlopes earlier).Nodup := by
  exact List.filter_sublist.nodup (by decide)

/-- At most the three exact source slopes survive. -/
theorem f97C8AssignedSlopes_length_le_three (earlier : List Nat) :
    (f97C8AssignedSlopes earlier).length <= 3 := by
  simpa [f97C8AssignedSlopes] using
    List.length_filter_le (fun gamma => decide (gamma ∉ earlier)) [0, 1, 2]

/-- Every assigned slope remains rooted in one of the four actual source
witnesses. -/
theorem f97C8AssignedSlope_has_witness
    (earlier : List Nat) (gamma : Nat)
    (hgamma : gamma ∈ f97C8AssignedSlopes earlier) :
    exists w, w ∈ f97C8Witnesses /\ f97C8Slope w = gamma /\
      gamma ∉ earlier := by
  have hassigned := (mem_f97C8AssignedSlopes earlier gamma).mp hgamma
  rcases hassigned with ⟨hraw, hnot⟩
  simp at hraw
  rcases hraw with h0 | hrest
  · subst gamma
    exact ⟨0, by decide, rfl, hnot⟩
  · rcases hrest with h1 | h2
    · subst gamma
      exact ⟨1, by decide, rfl, hnot⟩
    · subst gamma
      exact ⟨2, by decide, rfl, hnot⟩

/-- One realized exact two-cell profile, paid directly on its post-deletion
slope image at natural scale one. -/
def f97C8Profile (earlier : List Nat) : ProfilePayment 3 :=
  ProfilePayment.ofDirect .c8 (f97C8AssignedSlopes earlier) 1 3
    (f97C8AssignedSlopes_nodup earlier)
    (by simpa using f97C8AssignedSlopes_length_le_three earlier)

@[simp] theorem f97C8Profile_assignedSlopes (earlier : List Nat) :
    (f97C8Profile earlier).assignedSlopes = f97C8AssignedSlopes earlier := rfl

/-- Empty post-deletion cells are not installed. -/
def f97C8Profiles (earlier : List Nat) : List (ProfilePayment 3) :=
  if f97C8AssignedSlopes earlier = [] then [] else [f97C8Profile earlier]

/-- The installed profile family has exactly the surviving source slopes. -/
theorem f97C8Profiles_flatten_assignedSlopes (earlier : List Nat) :
    ((f97C8Profiles earlier).map
      (fun profile => profile.assignedSlopes)).flatten =
        f97C8AssignedSlopes earlier := by
  unfold f97C8Profiles
  split <;> simp_all

/-- At most one exact two-cell semantic profile is realized. -/
theorem f97C8Profiles_length_le_one (earlier : List Nat) :
    (f97C8Profiles earlier).length <= 1 := by
  unfold f97C8Profiles
  split <;> simp

/-- Closed line-local producer for the exact retained F97 incidence. -/
def f97C8Line (earlier : List Nat) : ClosedLineLedger 3 1 where
  badCount := (f97C8AssignedSlopes earlier).length
  profiles := f97C8Profiles earlier
  firstMatchOwnership := by
    rw [f97C8Profiles_flatten_assignedSlopes]
    exact f97C8AssignedSlopes_nodup earlier
  atlasExhaustive := by
    rw [f97C8Profiles_flatten_assignedSlopes]
    exact Nat.le_refl _
  profileCountControl := f97C8Profiles_length_le_one earlier

/-- The exact F97 line contributes at most one natural profile. -/
theorem f97C8Line_naturalTotal_le_one (earlier : List Nat) :
    (f97C8Line earlier).naturalTotal <= 1 := by
  unfold f97C8Line f97C8Profiles ClosedLineLedger.naturalTotal
  split <;> simp [f97C8Profile, ProfilePayment.ofDirect]

/-- The exact F97 line contributes ray budget at most three. -/
theorem f97C8Line_budgetTotal_le_three (earlier : List Nat) :
    (f97C8Line earlier).budgetTotal <= 3 := by
  unfold f97C8Line f97C8Profiles ClosedLineLedger.budgetTotal
  split <;> simp [f97C8Profile, ProfilePayment.ofDirect]

/-- One-line wrapper preserving the correct line-local profile sum. -/
def f97C8Ledger (earlier : List Nat) : UniformClosedLedger 3 1 1 where
  lines := [f97C8Line earlier]
  windowUniformity := by
    intro line hline
    rcases List.mem_cons.mp hline with hEq | hNil
    · subst line
      exact f97C8Line_naturalTotal_le_one earlier
    · simp at hNil

/-- Exact F97 two-cell producer theorem. -/
theorem f97C8Ledger_compiles (earlier : List Nat) :
    (f97C8Ledger earlier).rowBad <= 3 := by
  simpa using (f97C8Ledger earlier).compile

/-- Assigned slope image already carried by an earlier closed line. -/
def f97PriorAssignedSlopes {compilerLoss profileCap : Nat}
    (line : ClosedLineLedger compilerLoss profileCap) : List Nat :=
  (line.profiles.map (fun profile => profile.assignedSlopes)).flatten

/-- First-match deletion makes the exact F97 survivor image disjoint from the
prior line. -/
theorem f97Prior_append_assignedSlopes_nodup
    (prior : List Nat) (hprior : prior.Nodup) :
    (prior ++ f97C8AssignedSlopes prior).Nodup := by
  apply List.nodup_append.mpr
  refine ⟨hprior, f97C8AssignedSlopes_nodup prior, ?_⟩
  intro a ha b hb hab
  have hbdata := (mem_f97C8AssignedSlopes prior b).mp hb
  exact hbdata.2 (hab ▸ ha)

/-- Local sum telescope. -/
theorem f97C8ListSum_append : forall xs ys : List Nat,
    listSum (xs ++ ys) = listSum xs + listSum ys := by
  intro xs
  induction xs with
  | nil =>
      intro ys
      simp
  | cons x xs ih =>
      intro ys
      simp [ih, Nat.add_assoc]

/-- Append the exact F97 C8 cell after an earlier closed C1--C7 line. -/
def f97C8ExtendLine {profileCap : Nat}
    (line : ClosedLineLedger 3 profileCap) :
    ClosedLineLedger 3 (profileCap + 1) where
  badCount := line.badCount +
    (f97C8AssignedSlopes (f97PriorAssignedSlopes line)).length
  profiles := line.profiles ++ f97C8Profiles (f97PriorAssignedSlopes line)
  firstMatchOwnership := by
    rw [List.map_append, List.flatten_append,
      f97C8Profiles_flatten_assignedSlopes]
    exact f97Prior_append_assignedSlopes_nodup
      (f97PriorAssignedSlopes line) line.firstMatchOwnership
  atlasExhaustive := by
    rw [List.map_append, List.flatten_append,
      f97C8Profiles_flatten_assignedSlopes, List.length_append]
    exact Nat.add_le_add_right line.atlasExhaustive _
  profileCountControl := by
    rw [List.length_append]
    exact Nat.add_le_add line.profileCountControl
      (f97C8Profiles_length_le_one (f97PriorAssignedSlopes line))

/-- Exact combined bad-slope numerator telescope. -/
theorem f97C8ExtendLine_badCount {profileCap : Nat}
    (line : ClosedLineLedger 3 profileCap) :
    (f97C8ExtendLine line).badCount = line.badCount +
      (f97C8AssignedSlopes (f97PriorAssignedSlopes line)).length := rfl

/-- Exact line-local ray-budget telescope. -/
theorem f97C8ExtendLine_budgetTotal {profileCap : Nat}
    (line : ClosedLineLedger 3 profileCap) :
    (f97C8ExtendLine line).budgetTotal = line.budgetTotal +
      (f97C8Line (f97PriorAssignedSlopes line)).budgetTotal := by
  change
    listSum ((line.profiles ++ f97C8Profiles (f97PriorAssignedSlopes line)).map
      (fun profile => profile.rayBudget)) =
      listSum (line.profiles.map (fun profile => profile.rayBudget)) +
      listSum ((f97C8Profiles (f97PriorAssignedSlopes line)).map
        (fun profile => profile.rayBudget))
  rw [List.map_append, f97C8ListSum_append]

/-- Exact line-local natural-profile telescope. -/
theorem f97C8ExtendLine_naturalTotal {profileCap : Nat}
    (line : ClosedLineLedger 3 profileCap) :
    (f97C8ExtendLine line).naturalTotal = line.naturalTotal +
      (f97C8Line (f97PriorAssignedSlopes line)).naturalTotal := by
  change
    listSum ((line.profiles ++ f97C8Profiles (f97PriorAssignedSlopes line)).map
      (fun profile => profile.naturalScale)) =
      listSum (line.profiles.map (fun profile => profile.naturalScale)) +
      listSum ((f97C8Profiles (f97PriorAssignedSlopes line)).map
        (fun profile => profile.naturalScale))
  rw [List.map_append, f97C8ListSum_append]

/-- Earlier fixture paying slope `0`. -/
def f97ExtensionEarlierProfile : ProfilePayment 3 :=
  ProfilePayment.ofDirect .c1 [0] 1 3 (by decide) (by decide)

/-- Earlier closed line for the deletion fixture. -/
def f97ExtensionEarlierLine : ClosedLineLedger 3 1 where
  badCount := 1
  profiles := [f97ExtensionEarlierProfile]
  firstMatchOwnership := by decide
  atlasExhaustive := by decide
  profileCountControl := by decide

/-- The exact F97 extension deletes slope `0` and appends `1,2`. -/
theorem f97Extension_assignedSlopes :
    f97PriorAssignedSlopes (f97C8ExtendLine f97ExtensionEarlierLine) =
      [0, 1, 2] := by
  decide

/-- The combined fixture has three covered slopes, two realized profiles,
ray-budget total six, and natural total two. -/
theorem f97Extension_totals :
    (f97C8ExtendLine f97ExtensionEarlierLine).badCount = 3 /\
    (f97C8ExtendLine f97ExtensionEarlierLine).profiles.length = 2 /\
    (f97C8ExtendLine f97ExtensionEarlierLine).budgetTotal = 6 /\
    (f97C8ExtendLine f97ExtensionEarlierLine).naturalTotal = 2 := by
  decide

#print axioms f97C8WitnessCells_cover
#print axioms f97C8CellSlopeImages_exact
#print axioms f97C8FirstMatchSlopeLeaves
#print axioms f97C8RawChartSlopeTotal
#print axioms f97C8FirstMatchSlopeTotal
#print axioms f97C8AssignedSlope_has_witness
#print axioms f97C8Profiles_flatten_assignedSlopes
#print axioms f97C8Line_budgetTotal_le_three
#print axioms f97C8Ledger_compiles
#print axioms f97C8ExtendLine_badCount
#print axioms f97C8ExtendLine_budgetTotal
#print axioms f97C8ExtendLine_naturalTotal
#print axioms f97Extension_totals

end AsymptoticSpine
