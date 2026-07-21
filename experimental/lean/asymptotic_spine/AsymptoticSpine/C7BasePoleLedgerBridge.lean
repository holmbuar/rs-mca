import AsymptoticSpine.C7BasePoleProducer
import AsymptoticSpine.UniformClosedLedger

namespace AsymptoticSpine

/-!
# Closed-ledger bridge for the narrow C7 base-pole producer

`C7BasePoleProducer` is the integrated deletion-aware producer.  It exposes the
literal post-earlier slope image and its `directBudget`, without depending on
the closed-ledger compiler.  This module adds the deferred payment layer on top
of that stable narrow interface.

Each surviving slope is installed as one direct `ProfilePayment` at unit natural
scale.  The resulting line and one-line ledger preserve the line-local
`sum_profile` order and have budget and natural totals equal to the number of
survivors.  The added cost is bounded by the raw slope census and hence by any
source-side `q - 1` bound.

No earlier semantic atlas is constructed here.  No survivor nonemptiness,
row-wide `(UNIF)`, global atlas, target comparison, or row closure is claimed.
-/

/-- One surviving constant-coefficient cell is one assigned C7 slope, paid by
the direct distinct-slope adapter at unit natural scale. -/
def basePoleC7Profile (gamma : Nat) : ProfilePayment 1 :=
  ProfilePayment.ofDirect .c7 [gamma] 1 1 (by simp) (by simp)

@[simp] theorem basePoleC7Profile_assignedSlopes (gamma : Nat) :
    (basePoleC7Profile gamma).assignedSlopes = [gamma] := rfl

@[simp] theorem basePoleC7Profile_rayBudget (gamma : Nat) :
    (basePoleC7Profile gamma).rayBudget = 1 := rfl

@[simp] theorem basePoleC7Profile_naturalScale (gamma : Nat) :
    (basePoleC7Profile gamma).naturalScale = 1 := rfl

/-- Realized nonempty C7 profiles on one received line.  Deleted singleton cells
are not installed as profiles. -/
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
  | cons gamma xs ih =>
      simp only [List.map_cons, List.flatten_cons,
        basePoleC7Profile_assignedSlopes, List.singleton_append]
      exact congrArg (List.cons gamma) ih

/-- The bridge's assigned slope image is exactly the narrow producer's
post-earlier residual. -/
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
  | cons gamma xs ih =>
      simp only [List.map_cons, basePoleC7Profile_rayBudget,
        listSum_cons, List.length_cons]
      rw [ih]
      omega

/-- Unit natural scales sum to the same line-local survivor count. -/
theorem listSum_basePoleC7Profile_naturalScales :
    ∀ xs : List Nat,
      listSum ((xs.map basePoleC7Profile).map
        (fun profile => profile.naturalScale)) = xs.length := by
  intro xs
  induction xs with
  | nil => simp
  | cons gamma xs ih =>
      simp only [List.map_cons, basePoleC7Profile_naturalScale,
        listSum_cons, List.length_cons]
      rw [ih]
      omega

/-- Closed-ledger line for the C7 residual of one raw base-pole slope class.
`badCount` is only this post-earlier C7 contribution. -/
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

/-- The line-local C7 budget is exactly the integrated narrow producer's direct
budget. -/
theorem basePoleC7Line_budgetTotal_eq_directBudget
    (earlier raw : List Nat) (hraw : raw.Nodup) :
    (basePoleC7Line earlier raw hraw).budgetTotal =
      basePoleC7DirectBudget earlier raw := by
  rw [basePoleC7Line_budgetTotal, basePoleC7DirectBudget_eq]

/-- The line-local natural sum is also the integrated narrow producer's direct
budget. -/
theorem basePoleC7Line_naturalTotal_eq_directBudget
    (earlier raw : List Nat) (hraw : raw.Nodup) :
    (basePoleC7Line earlier raw hraw).naturalTotal =
      basePoleC7DirectBudget earlier raw := by
  rw [basePoleC7Line_naturalTotal, basePoleC7DirectBudget_eq]

/-- The correct line-local C7 budget is bounded by the raw slope census. -/
theorem basePoleC7Line_budgetTotal_le_raw
    (earlier raw : List Nat) (hraw : raw.Nodup) :
    (basePoleC7Line earlier raw hraw).budgetTotal ≤ raw.length := by
  rw [basePoleC7Line_budgetTotal_eq_directBudget]
  exact basePoleC7DirectBudget_le_raw earlier raw

/-- The correct line-local C7 natural sum is bounded by the raw slope census. -/
theorem basePoleC7Line_naturalTotal_le_raw
    (earlier raw : List Nat) (hraw : raw.Nodup) :
    (basePoleC7Line earlier raw hraw).naturalTotal ≤ raw.length := by
  rw [basePoleC7Line_naturalTotal_eq_directBudget]
  exact basePoleC7DirectBudget_le_raw earlier raw

/-- Source-facing `q - 1` budget payment. -/
theorem basePoleC7Line_budgetTotal_le_qMinusOne
    (earlier raw : List Nat) (hraw : raw.Nodup) (qMinusOne : Nat)
    (hrawBound : raw.length ≤ qMinusOne) :
    (basePoleC7Line earlier raw hraw).budgetTotal ≤ qMinusOne :=
  Nat.le_trans (basePoleC7Line_budgetTotal_le_raw earlier raw hraw) hrawBound

/-- Source-facing `q - 1` natural-scale bound. -/
theorem basePoleC7Line_naturalTotal_le_qMinusOne
    (earlier raw : List Nat) (hraw : raw.Nodup) (qMinusOne : Nat)
    (hrawBound : raw.length ≤ qMinusOne) :
    (basePoleC7Line earlier raw hraw).naturalTotal ≤ qMinusOne :=
  Nat.le_trans (basePoleC7Line_naturalTotal_le_raw earlier raw hraw) hrawBound

/-- One-line wrapper exposing the correct line-local profile sum.  This is a
local C7 residual ledger, not row-wide `(UNIF)`. -/
def basePoleC7Ledger (earlier raw : List Nat) (hraw : raw.Nodup) :
    UniformClosedLedger 1 raw.length raw.length where
  lines := [basePoleC7Line earlier raw hraw]
  windowUniformity := by
    intro line hline
    rcases List.mem_cons.mp hline with hEq | hNil
    · subst line
      exact basePoleC7Line_naturalTotal_le_raw earlier raw hraw
    · simp at hNil

/-- Replay the deletion-aware bridge through the closed-ledger compiler without
interchanging the line supremum and profile sum. -/
theorem basePoleC7Ledger_compiles
    (earlier raw : List Nat) (hraw : raw.Nodup) :
    (basePoleC7Ledger earlier raw hraw).rowBad ≤ raw.length := by
  simpa using (basePoleC7Ledger earlier raw hraw).compile

#print axioms basePoleC7Profiles_flatten_assignedSlopes
#print axioms basePoleC7Line_budgetTotal
#print axioms basePoleC7Line_naturalTotal
#print axioms basePoleC7Line_budgetTotal_eq_directBudget
#print axioms basePoleC7Line_naturalTotal_eq_directBudget
#print axioms basePoleC7Line_budgetTotal_le_qMinusOne
#print axioms basePoleC7Line_naturalTotal_le_qMinusOne
#print axioms basePoleC7Ledger_compiles

end AsymptoticSpine
