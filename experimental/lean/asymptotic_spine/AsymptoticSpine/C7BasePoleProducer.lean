import AsymptoticSpine.FirstMatch

namespace AsymptoticSpine

/-!
# Deletion-aware C7 base-pole slope producer

The source theorem in
`experimental/notes/thresholds/aperiodic_one_ray_saturation.md` partitions one
base-pole prefix fibre by locator constant coefficient. Every nonempty raw cell
has one final slope, and the raw cells realize at most `q - 1` distinct slopes
on that received line.

This module begins at that proved slope-image boundary. `earlier` is a supplied
list of slopes already owned by earlier semantic cells on the same received
line, while `raw` is the duplicate-free raw slope image of the
constant-coefficient cells. The C7 first-match image is exactly `raw \ earlier`.
Each surviving slope is represented by one singleton cell, so its direct
line-local budget is the number of survivors and is bounded by the raw census.

No theorem here constructs the earlier semantic atlas, proves that the C7
residual is nonempty, establishes row-wide uniformity, or compares the local
budget with an asymptotic target.
-/

/-- Slopes of the raw base-pole constant-coefficient class that remain after
all supplied earlier owner slopes on the same received line are deleted. -/
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

/-- Aggregating all earlier owner slopes into one list gives the same second
leaf as ordered first match: the C7 leaf is post-deletion, not the raw image. -/
theorem basePoleC7_firstMatchLeaves (earlier raw : List Nat) :
    firstMatchLeaves [] [earlier, raw] =
      [earlier, basePoleC7AssignedSlopes earlier raw] := by
  simp [firstMatchLeaves, newPaid, basePoleC7AssignedSlopes]

/-- One direct unit-budget cell for one surviving final slope. -/
def basePoleC7SingletonCell (gamma : Nat) : List Nat := [gamma]

/-- The realized nonempty C7 cells after deletion. Deleted raw cells are not
installed. -/
def basePoleC7SingletonCells (earlier raw : List Nat) : List (List Nat) :=
  (basePoleC7AssignedSlopes earlier raw).map basePoleC7SingletonCell

/-- Flattening singleton cells returns their slope list exactly. -/
theorem flatten_basePoleC7SingletonCells :
    ∀ xs : List Nat,
      (xs.map basePoleC7SingletonCell).flatten = xs := by
  intro xs
  induction xs with
  | nil => simp
  | cons gamma xs ih =>
      simp [basePoleC7SingletonCell, ih]

/-- The producer's cell image is exactly the post-earlier residual. -/
theorem basePoleC7SingletonCells_flatten
    (earlier raw : List Nat) :
    (basePoleC7SingletonCells earlier raw).flatten =
      basePoleC7AssignedSlopes earlier raw := by
  simpa [basePoleC7SingletonCells] using
    flatten_basePoleC7SingletonCells (basePoleC7AssignedSlopes earlier raw)

/-- Direct local payment obtained by summing one slope per surviving singleton
cell. -/
def basePoleC7DirectBudget (earlier raw : List Nat) : Nat :=
  listSum ((basePoleC7SingletonCells earlier raw).map List.length)

/-- Singleton cell sizes sum to the number of singleton cells. -/
theorem listSum_basePoleC7SingletonCell_lengths :
    ∀ xs : List Nat,
      listSum ((xs.map basePoleC7SingletonCell).map List.length) =
        xs.length := by
  intro xs
  induction xs with
  | nil => simp
  | cons gamma xs ih =>
      change 1 + listSum ((xs.map basePoleC7SingletonCell).map List.length) =
        xs.length + 1
      omega

/-- The direct line-local budget is exactly the number of surviving slopes. -/
theorem basePoleC7DirectBudget_eq
    (earlier raw : List Nat) :
    basePoleC7DirectBudget earlier raw =
      (basePoleC7AssignedSlopes earlier raw).length := by
  simpa [basePoleC7DirectBudget, basePoleC7SingletonCells] using
    listSum_basePoleC7SingletonCell_lengths
      (basePoleC7AssignedSlopes earlier raw)

/-- The surviving slope count is bounded by the raw slope census. -/
theorem basePoleC7AssignedSlopes_length_le_raw
    (earlier raw : List Nat) :
    (basePoleC7AssignedSlopes earlier raw).length ≤ raw.length := by
  simpa [basePoleC7AssignedSlopes] using
    List.length_filter_le (fun gamma => decide (gamma ∉ earlier)) raw

/-- The direct line-local C7 budget is bounded by the raw slope census. -/
theorem basePoleC7DirectBudget_le_raw
    (earlier raw : List Nat) :
    basePoleC7DirectBudget earlier raw ≤ raw.length := by
  rw [basePoleC7DirectBudget_eq]
  exact basePoleC7AssignedSlopes_length_le_raw earlier raw

/-- Source-facing `q - 1` payment. Once the source theorem supplies
`raw.length ≤ qMinusOne`, the post-deletion singleton budget has the same
bound. -/
theorem basePoleC7DirectBudget_le_qMinusOne
    (earlier raw : List Nat) (qMinusOne : Nat)
    (hrawBound : raw.length ≤ qMinusOne) :
    basePoleC7DirectBudget earlier raw ≤ qMinusOne :=
  Nat.le_trans (basePoleC7DirectBudget_le_raw earlier raw) hrawBound

/-- Executable deletion fixture: earlier owners remove slopes `2` and `4`. -/
theorem basePoleC7_deletion_fixture :
    basePoleC7AssignedSlopes [2, 4, 9] [1, 2, 3, 4] = [1, 3] := by
  decide

/-- Executable ownership-boundary fixture: a raw slope already owned earlier
leaves no C7 first-match slope. -/
theorem basePoleC7_absorbed_fixture :
    basePoleC7AssignedSlopes [7] [7] = [] := by
  decide

#print axioms mem_basePoleC7AssignedSlopes
#print axioms basePoleC7AssignedSlopes_nodup
#print axioms basePoleC7_firstMatchLeaves
#print axioms flatten_basePoleC7SingletonCells
#print axioms basePoleC7SingletonCells_flatten
#print axioms basePoleC7DirectBudget_eq
#print axioms basePoleC7DirectBudget_le_qMinusOne
#print axioms basePoleC7_deletion_fixture
#print axioms basePoleC7_absorbed_fixture

end AsymptoticSpine
