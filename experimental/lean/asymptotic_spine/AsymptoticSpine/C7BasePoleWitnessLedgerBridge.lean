import AsymptoticSpine.C7BasePoleWitnessProducer
import AsymptoticSpine.C7BasePoleLedgerBridge

namespace AsymptoticSpine
namespace BasePoleC7WitnessClass

/-!
# Rooted witness hand-off into the C7 closed ledger

The integrated `C7BasePoleWitnessProducer` ends at the exact raw witness slope
image and its deletion-aware `directBudget`.  This module hands that stable
interface to `C7BasePoleLedgerBridge`.

The new line and one-line ledger are rooted in the existing witness catalogue,
use exactly the integrated direct budget, and inherit the source-side `q - 1`
census.  No finite-field algebra is reproved here, and no global semantic atlas,
survivor nonemptiness, row-wide `(UNIF)`, or target comparison is asserted.
-/

/-- Closed-ledger C7 residual produced from the integrated rooted witness class. -/
def c7Line (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    ClosedLineLedger 1 data.rawSlopes.length :=
  basePoleC7Line earlier data.rawSlopes data.rawSlopes_nodup

/-- The line's assigned slope image is exactly the post-earlier witness slope
image. -/
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

/-- The rooted line-local budget is definitionally tied to the already-integrated
narrow `directBudget`, rather than a second producer implementation. -/
theorem c7Line_budgetTotal_eq_directBudget
    (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    (data.c7Line earlier).budgetTotal = data.directBudget earlier := by
  change
    (basePoleC7Line earlier data.rawSlopes data.rawSlopes_nodup).budgetTotal =
      basePoleC7DirectBudget earlier data.rawSlopes
  exact basePoleC7Line_budgetTotal_eq_directBudget
    earlier data.rawSlopes data.rawSlopes_nodup

/-- The rooted line-local natural sum equals the same integrated direct budget. -/
theorem c7Line_naturalTotal_eq_directBudget
    (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    (data.c7Line earlier).naturalTotal = data.directBudget earlier := by
  change
    (basePoleC7Line earlier data.rawSlopes data.rawSlopes_nodup).naturalTotal =
      basePoleC7DirectBudget earlier data.rawSlopes
  exact basePoleC7Line_naturalTotal_eq_directBudget
    earlier data.rawSlopes data.rawSlopes_nodup

/-- The rooted line-local C7 ray budget is bounded by `q - 1`. -/
theorem c7Line_budgetTotal_le_qMinusOne
    (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    (data.c7Line earlier).budgetTotal ≤ data.qMinusOne := by
  rw [data.c7Line_budgetTotal_eq_directBudget earlier]
  exact data.directBudget_le_qMinusOne earlier

/-- The rooted line-local natural-profile sum is also bounded by `q - 1`. -/
theorem c7Line_naturalTotal_le_qMinusOne
    (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    (data.c7Line earlier).naturalTotal ≤ data.qMinusOne := by
  rw [data.c7Line_naturalTotal_eq_directBudget earlier]
  exact data.directBudget_le_qMinusOne earlier

/-- One-line source-facing wrapper.  Its envelope is the source-side `q - 1`
census, while the line contains only surviving profiles. -/
def c7Ledger (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    UniformClosedLedger 1 data.rawSlopes.length data.qMinusOne where
  lines := [data.c7Line earlier]
  windowUniformity := by
    intro line hline
    rcases List.mem_cons.mp hline with hEq | hNil
    · subst line
      exact data.c7Line_naturalTotal_le_qMinusOne earlier
    · simp at hNil

/-- Rooted C7 bridge theorem: raw witnesses are partitioned by constant
coefficient, the exact slope image is deleted by earlier owners, the surviving
singleton profiles are paid at unit natural scale, and the correct line-local
profile sum is at most `q - 1`. -/
theorem c7Ledger_compiles
    (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    (data.c7Ledger earlier).rowBad ≤ data.qMinusOne := by
  simpa using (data.c7Ledger earlier).compile

/-- Executable rooted fixture: earlier owners delete slopes `100` and `102`, and
the resulting one-line ledger compiles under the source census `4`. -/
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
