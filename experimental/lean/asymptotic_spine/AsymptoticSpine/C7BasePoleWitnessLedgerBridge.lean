import AsymptoticSpine.C7BasePoleWitnessProducer
import AsymptoticSpine.C7BasePoleLedgerBridge

namespace AsymptoticSpine
namespace BasePoleC7WitnessClass

/-!
# Conditional witness-data hand-off into the C7 closed ledger

The integrated `C7BasePoleWitnessProducer` packages a witness list together with
explicit source-facing fields for its coefficient map, slope map, exact slope
law, injectivity, and `q - 1` census.  Those fields are hypotheses of the Lean
structure; this package does not formalize the finite field, support locators,
received pole line, or the proof of `d ↦ -d`.

This module hands that stable conditional interface to
`C7BasePoleLedgerBridge`.  The new line and one-line ledger use exactly the
integrated deletion-aware `directBudget`.  No source algebra, actual semantic
classification, completeness over received lines, global atlas, survivor
nonemptiness, row-wide `(UNIF)`, or target comparison is asserted.
-/

/-- Closed-ledger numeric residual produced from the integrated conditional
witness-data structure. -/
def c7Line (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    ClosedLineLedger 1 data.rawSlopes.length :=
  basePoleC7Line earlier data.rawSlopes data.rawSlopes_nodup

/-- The line's assigned numeric slope image is exactly the structure's
post-earlier slope list. -/
theorem c7Line_flatten_assignedSlopes
    (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    (((data.c7Line earlier).profiles.map
      (fun profile => profile.assignedSlopes)).flatten) =
        data.assignedSlopes earlier := by
  change
    ((basePoleC7Profiles earlier data.rawSlopes).map
      (fun profile => profile.assignedSlopes)).flatten =
        basePoleC7AssignedSlopes earlier data.rawSlopes
  exact basePoleC7Profiles_flatten_assignedSlopes earlier data.rawSlopes

/-- The line-local budget is definitionally tied to the already-integrated
narrow `directBudget`, rather than a second producer implementation. -/
theorem c7Line_budgetTotal_eq_directBudget
    (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    (data.c7Line earlier).budgetTotal = data.directBudget earlier := by
  change
    (basePoleC7Line earlier data.rawSlopes data.rawSlopes_nodup).budgetTotal =
      basePoleC7DirectBudget earlier data.rawSlopes
  exact basePoleC7Line_budgetTotal_eq_directBudget
    earlier data.rawSlopes data.rawSlopes_nodup

/-- The line-local natural sum equals the same integrated direct budget. -/
theorem c7Line_naturalTotal_eq_directBudget
    (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    (data.c7Line earlier).naturalTotal = data.directBudget earlier := by
  change
    (basePoleC7Line earlier data.rawSlopes data.rawSlopes_nodup).naturalTotal =
      basePoleC7DirectBudget earlier data.rawSlopes
  exact basePoleC7Line_naturalTotal_eq_directBudget
    earlier data.rawSlopes data.rawSlopes_nodup

/-- The conditional line-local C7 ray budget is bounded by the structure's
assumed `q - 1` census. -/
theorem c7Line_budgetTotal_le_qMinusOne
    (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    (data.c7Line earlier).budgetTotal ≤ data.qMinusOne := by
  rw [data.c7Line_budgetTotal_eq_directBudget earlier]
  exact data.directBudget_le_qMinusOne earlier

/-- The conditional line-local natural-profile sum obeys the same bound. -/
theorem c7Line_naturalTotal_le_qMinusOne
    (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    (data.c7Line earlier).naturalTotal ≤ data.qMinusOne := by
  rw [data.c7Line_naturalTotal_eq_directBudget earlier]
  exact data.directBudget_le_qMinusOne earlier

/-- One-line numeric wrapper.  Its envelope is the supplied `q - 1` census,
while the line contains only post-deletion profiles. -/
def c7Ledger (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    UniformClosedLedger 1 data.rawSlopes.length data.qMinusOne where
  lines := [data.c7Line earlier]
  windowUniformity := by
    intro line hline
    rcases List.mem_cons.mp hline with hEq | hNil
    · subst line
      exact data.c7Line_naturalTotal_le_qMinusOne earlier
    · simp at hNil

/-- Conditional finite adapter theorem: given all fields of
`BasePoleC7WitnessClass` and a supplied earlier numeric slope image, the
surviving singleton profiles are paid at unit natural scale and the one-line
profile sum is at most the supplied `q - 1` value. -/
theorem c7Ledger_compiles
    (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    (data.c7Ledger earlier).rowBad ≤ data.qMinusOne := by
  simpa using (data.c7Ledger earlier).compile

/-- Executable natural-number fixture: the supplied earlier list removes values
`100` and `102`, and the resulting one-line numeric ledger compiles under `4`.
The fixture is not a finite-field or RS instantiation. -/
theorem rootedFixture_compiles :
    (rootedFixture.c7Ledger [100, 102]).rowBad ≤ 4 :=
  rootedFixture.c7Ledger_compiles [100, 102]

#print axioms c7Line_flatten_assignedSlopes
#print axioms c7Line_budgetTotal_eq_directBudget
#print axioms c7Line_naturalTotal_eq_directBudget
#print axioms c7Line_budgetTotal_le_qMinusOne
#print axioms c7Line_naturalTotal_le_qMinusOne
#print axioms c7Ledger_compiles
#print axioms rootedFixture_compiles

end BasePoleC7WitnessClass
end AsymptoticSpine
