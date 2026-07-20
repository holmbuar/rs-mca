import AsymptoticSpine.UniformClosedLedger

namespace AsymptoticSpine

/-!
# Deletion-aware C7 base-pole producer

The source theorem in
`experimental/notes/thresholds/aperiodic_one_ray_saturation.md` partitions one
actual base-pole prefix fibre by locator constant coefficient.  Every nonempty
raw cell has one final slope, and the raw cells realize at most `q - 1`
distinct slopes on that received line.

This module starts at that proved slope-image boundary.  `earlier` is the
aggregate C1--C6 slope image on the same received line and `raw` is the
duplicate-free list of slopes supplied by the constant-coefficient cells.
The C7 owner is the literal first-match residual `raw \ earlier`.  Each surviving
singleton is paid directly at unit profile scale, the additive `1` in the
image-normalized profile envelope.  The line-local profile sum is therefore the
number of surviving slopes and is bounded by the raw `q - 1` census.

No nonemptiness of the residual is asserted.  The module does not construct the
finite-field prefix fibre, a global fixed-before-line atlas, completeness over
all received lines, actual row-wide `(UNIF)`, or a target comparison.
-/

/-- Slopes of the real base-pole constant-coefficient class that remain after
all earlier C1--C6 slope images on the same received line have been deleted. -/
def basePoleC7AssignedSlopes (earlier raw : List Nat) : List Nat :=
  raw.filter fun gamma => decide (gamma ∉ earlier)

@[simp] theorem mem_basePoleC7AssignedSlopes
    (earlier raw : List Nat) (gamma : Nat) :
    gamma ∈ basePoleC7AssignedSlopes earlier raw ↔
      gamma ∈ raw ∧ gamma ∉ earlier := by
  simp [basePoleC7AssignedSlopes]

/-- Deletion preserves the duplicate-free raw distinct-slope census. -/
theorem basePoleC7AssignedSlopes_nodup
    (earlier raw : List Nat) (hraw : raw.Nodup) :
    (basePoleC7AssignedSlopes earlier raw).Nodup := by
  exact List.filter_sublist.nodup hraw

/-- Aggregating all earlier owners into one paid slope list gives exactly the
same second leaf as ordered first match: the C7 cell is the post-deletion
subset, not the untrimmed raw projection. -/
theorem basePoleC7_firstMatchLeaves (earlier raw : List Nat) :
    firstMatchLeaves [] [earlier, raw] =
      [earlier, basePoleC7AssignedSlopes earlier raw] := by
  simp [firstMatchLeaves, newPaid, basePoleC7AssignedSlopes]

/-- One surviving constant-coefficient cell is one assigned C7 slope and is
paid by the direct distinct-slope adapter at unit natural scale. -/
def basePoleC7Profile (gamma : Nat) : ProfilePayment 1 :=
  ProfilePayment.ofDirect .c7 [gamma] 1 1 (by simp) (by simp)

@[simp] theorem basePoleC7Profile_assignedSlopes (gamma : Nat) :
    (basePoleC7Profile gamma).assignedSlopes = [gamma] := rfl

@[simp] theorem basePoleC7Profile_rayBudget (gamma : Nat) :
    (basePoleC7Profile gamma).rayBudget = 1 := rfl

@[simp] theorem basePoleC7Profile_naturalScale (gamma : Nat) :
    (basePoleC7Profile gamma).naturalScale = 1 := rfl

/-- The realized nonempty C7 profiles on this received line.  Deleted singleton
cells are not installed as profiles. -/
def basePoleC7Profiles (earlier raw : List Nat) :
    List (ProfilePayment 1) :=
  (basePoleC7AssignedSlopes earlier raw).map basePoleC7Profile

/-- Singleton assigned-slope lists flatten back to the surviving slope list. -/
theorem flatten_basePoleC7ProfileSlopes :
    ∀ xs : List Nat,
      ((xs.map basePoleC7Profile).map
        (fun profile => profile.assignedSlopes)).flatten = xs := by
  intro xs
  induction xs with
  | nil => simp
  | cons gamma xs ih => simp [ih]

/-- The producer's assigned slope image is exactly the post-earlier residual. -/
theorem basePoleC7Profiles_flatten_assignedSlopes
    (earlier raw : List Nat) :
    ((basePoleC7Profiles earlier raw).map
      (fun profile => profile.assignedSlopes)).flatten =
        basePoleC7AssignedSlopes earlier raw := by
  simpa [basePoleC7Profiles] using
    flatten_basePoleC7ProfileSlopes (basePoleC7AssignedSlopes earlier raw)

/-- Unit ray budgets sum to the number of surviving singleton profiles. -/
theorem listSum_basePoleC7Profile_rayBudgets :
    ∀ xs : List Nat,
      listSum ((xs.map basePoleC7Profile).map
        (fun profile => profile.rayBudget)) = xs.length := by
  intro xs
  induction xs with
  | nil => simp
  | cons gamma xs ih => simp [ih]

/-- Unit natural scales sum to the same line-local survivor count. -/
theorem listSum_basePoleC7Profile_naturalScales :
    ∀ xs : List Nat,
      listSum ((xs.map basePoleC7Profile).map
        (fun profile => profile.naturalScale)) = xs.length := by
  intro xs
  induction xs with
  | nil => simp
  | cons gamma xs ih => simp [ih]

/-- The surviving slope count is bounded by the raw constant-coefficient slope
census. -/
theorem basePoleC7AssignedSlopes_length_le_raw
    (earlier raw : List Nat) :
    (basePoleC7AssignedSlopes earlier raw).length ≤ raw.length := by
  simpa [basePoleC7AssignedSlopes] using
    List.length_filter_le (fun gamma => decide (gamma ∉ earlier)) raw

/-- Closed-ledger producer for the C7 residual of one real base-pole prefix
class.  `badCount` is only this post-C1--C6 C7 residual contribution. -/
def basePoleC7Line (earlier raw : List Nat) (hraw : raw.Nodup) :
    ClosedLineLedger 1 raw.length where
  badCount := (basePoleC7AssignedSlopes earlier raw).length
  profiles := basePoleC7Profiles earlier raw
  firstMatchOwnership := by
    rw [basePoleC7Profiles_flatten_assignedSlopes]
    exact basePoleC7AssignedSlopes_nodup earlier raw hraw
  atlasExhaustive := by
    rw [basePoleC7Profiles_flatten_assignedSlopes]
  profileCountControl := by
    simpa [basePoleC7Profiles] using
      basePoleC7AssignedSlopes_length_le_raw earlier raw

/-- The line-local C7 ray-budget sum is exactly the number of surviving slopes. -/
theorem basePoleC7Line_budgetTotal
    (earlier raw : List Nat) (hraw : raw.Nodup) :
    (basePoleC7Line earlier raw hraw).budgetTotal =
      (basePoleC7AssignedSlopes earlier raw).length := by
  simpa [basePoleC7Line, ClosedLineLedger.budgetTotal, basePoleC7Profiles] using
    listSum_basePoleC7Profile_rayBudgets
      (basePoleC7AssignedSlopes earlier raw)

/-- The line-local natural-profile sum is the same survivor count. -/
theorem basePoleC7Line_naturalTotal
    (earlier raw : List Nat) (hraw : raw.Nodup) :
    (basePoleC7Line earlier raw hraw).naturalTotal =
      (basePoleC7AssignedSlopes earlier raw).length := by
  simpa [basePoleC7Line, ClosedLineLedger.naturalTotal, basePoleC7Profiles] using
    listSum_basePoleC7Profile_naturalScales
      (basePoleC7AssignedSlopes earlier raw)

/-- The correct line-local C7 budget is bounded by the raw slope census. -/
theorem basePoleC7Line_budgetTotal_le_raw
    (earlier raw : List Nat) (hraw : raw.Nodup) :
    (basePoleC7Line earlier raw hraw).budgetTotal ≤ raw.length := by
  rw [basePoleC7Line_budgetTotal]
  exact basePoleC7AssignedSlopes_length_le_raw earlier raw

/-- The correct line-local C7 natural sum is bounded by the raw slope census. -/
theorem basePoleC7Line_naturalTotal_le_raw
    (earlier raw : List Nat) (hraw : raw.Nodup) :
    (basePoleC7Line earlier raw hraw).naturalTotal ≤ raw.length := by
  rw [basePoleC7Line_naturalTotal]
  exact basePoleC7AssignedSlopes_length_le_raw earlier raw

/-- Source-facing `q - 1` payment: once the raw theorem supplies at most
`qMinusOne` constant-coefficient slopes, the actual post-deletion profile sum
has the same bound. -/
theorem basePoleC7Line_budgetTotal_le_qMinusOne
    (earlier raw : List Nat) (hraw : raw.Nodup) (qMinusOne : Nat)
    (hrawBound : raw.length ≤ qMinusOne) :
    (basePoleC7Line earlier raw hraw).budgetTotal ≤ qMinusOne :=
  Nat.le_trans (basePoleC7Line_budgetTotal_le_raw earlier raw hraw) hrawBound

/-- One-line wrapper exposing the correct `sum_profile` quantity to the existing
closed-ledger compiler.  This is a local C7 residual ledger, not row-wide
`(UNIF)`. -/
def basePoleC7Ledger (earlier raw : List Nat) (hraw : raw.Nodup) :
    UniformClosedLedger 1 raw.length raw.length where
  lines := [basePoleC7Line earlier raw hraw]
  windowUniformity := by
    intro line hline
    rcases List.mem_cons.mp hline with hEq | hNil
    · subst line
      exact basePoleC7Line_naturalTotal_le_raw earlier raw hraw
    · simp at hNil

/-- Replay the deletion-aware producer through the existing compiler without
interchanging the line supremum and profile sum. -/
theorem basePoleC7Ledger_compiles
    (earlier raw : List Nat) (hraw : raw.Nodup) :
    (basePoleC7Ledger earlier raw hraw).rowBad ≤ raw.length := by
  simpa using (basePoleC7Ledger earlier raw hraw).compile

/-- Executable finite regression: two raw singleton slopes are removed by the
earlier owner image and the two survivors contribute budget `2`, not `4`. -/
theorem basePoleC7_deletion_fixture :
    basePoleC7AssignedSlopes [2, 4, 9] [1, 2, 3, 4] = [1, 3] := by
  decide

#print axioms mem_basePoleC7AssignedSlopes
#print axioms basePoleC7AssignedSlopes_nodup
#print axioms basePoleC7_firstMatchLeaves
#print axioms flatten_basePoleC7ProfileSlopes
#print axioms basePoleC7Profiles_flatten_assignedSlopes
#print axioms basePoleC7Line_budgetTotal
#print axioms basePoleC7Line_naturalTotal
#print axioms basePoleC7Line_budgetTotal_le_qMinusOne
#print axioms basePoleC7Ledger_compiles
#print axioms basePoleC7_deletion_fixture

end AsymptoticSpine
