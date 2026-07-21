import AsymptoticSpine.PrefixAtlas
import AsymptoticSpine.SemanticAtlasOwnership

namespace AsymptoticSpine

/-!
# C7 singleton-planted absorption regression

The archived broad planted-cell grammar permitted a predetermined common support
divisor `P` and treated `|P| = o(n)` as a subexponential profile factor.  Under
that permissive historical reading, the fixed atlas indexed by evaluation points

`P_t(X) = X - t`,  `t in D`,

contains every positive-agreement witness before C7.  The later base-pole C7
first-match image can therefore be empty even though its raw payment is valid.

This module kernel-checks the finite ownership consequence.  The active semantic
repair is `SemanticAtlasOwnership`: witness-local factors are refinements only,
and an earlier C3 owner must be supplied as a certified row-derived profile.
Thus this is a regression against silently promoting local support factors, not
a claim that the active atlas must contain singleton-root C3 owners.

No asymptotic field-size estimate, finite-field locator algebra, global atlas,
row-wide `(UNIF)`, or target comparison is proved here.
-/

/-- Four finite witness records `(slope, support)`.  Each support is nonempty,
and the overlapping singleton-root profiles model the divisors `X-t`. -/
def singletonPlantedWitnesses : List (Nat × List Nat) :=
  [(10, [0, 1]), (11, [1, 2]), (12, [2, 3]), (13, [3, 0])]

/-- Distinct slopes having a witness whose support contains the planted root
`t`. -/
def singletonPlantedSlopeCell (t : Nat) : List Nat :=
  realizedKeys
    (singletonPlantedWitnesses.filter fun witness => decide (t ∈ witness.2))
    (fun witness => witness.1)

/-- Fixed earlier C3 candidate atlas, indexed before the received line by four
domain points.  Semantic use requires the certified interface described above. -/
def singletonPlantedRawSlopeCells : List (List Nat) :=
  (List.range 4).map singletonPlantedSlopeCell

/-- The actual overlapping raw slope images of the four singleton-root cells. -/
theorem singletonPlantedRawSlopeCells_eq :
    singletonPlantedRawSlopeCells =
      [[10, 13], [10, 11], [11, 12], [12, 13]] := by
  decide

/-- Add the tempting later raw C7 cell containing all four base-pole slopes. -/
def singletonPlantedThenC7RawSlopeCells : List (List Nat) :=
  singletonPlantedRawSlopeCells ++ [[10, 11, 12, 13]]

/-- Ordered slope-level first match assigns every slope to an earlier singleton
candidate profile; the later C7 assigned image is empty. -/
theorem singletonPlanted_absorbs_rawC7 :
    firstMatchLeaves [] singletonPlantedThenC7RawSlopeCells =
      [[10, 13], [11], [12], [], []] := by
  decide

/-- First earlier C3 payment.  Compiler loss `4` is the finite stand-in for a
field-size factor; natural scale is the additive profile term `1`. -/
def singletonPlantedC3Payment0 : ProfilePayment 4 :=
  ProfilePayment.ofDirect .c3 [10, 13] 1 4 (by decide) (by decide)

/-- Second nonempty first-match C3 payment. -/
def singletonPlantedC3Payment1 : ProfilePayment 4 :=
  ProfilePayment.ofDirect .c3 [11] 1 4 (by decide) (by decide)

/-- Third nonempty first-match C3 payment. -/
def singletonPlantedC3Payment2 : ProfilePayment 4 :=
  ProfilePayment.ofDirect .c3 [12] 1 4 (by decide) (by decide)

/-- Correct finite line under the explicitly supplied earlier C3 candidate
order: every raw slope is assigned before C7, so no C7 profile is installed. -/
def singletonPlantedC3Line : ClosedLineLedger 4 4 where
  badCount := 4
  profiles := [singletonPlantedC3Payment0,
    singletonPlantedC3Payment1, singletonPlantedC3Payment2]
  firstMatchOwnership := by decide
  atlasExhaustive := by decide
  profileCountControl := by decide

/-- The earlier C3 candidate atlas has natural-profile sum `3` and compiler
budget `12`. -/
theorem singletonPlantedC3Line_totals :
    singletonPlantedC3Line.naturalTotal = 3 ∧
      singletonPlantedC3Line.budgetTotal = 12 := by
  decide

/-- The tempting untrimmed C7 payment is numerically valid in isolation but has
no semantic assigned slope after the supplied earlier C3 order. -/
def singletonPlantedRawC7Payment : ProfilePayment 4 :=
  ProfilePayment.ofDirect .c7 [10, 11, 12, 13] 1 4
    (by decide) (by decide)

/-- Appending the untrimmed raw C7 profile would charge all four slopes twice
and violates the closed-ledger ownership field. -/
theorem singletonPlantedRawC7_breaks_firstMatchOwnership :
    ¬ ((([singletonPlantedC3Payment0, singletonPlantedC3Payment1,
      singletonPlantedC3Payment2, singletonPlantedRawC7Payment].map
        (fun profile => profile.assignedSlopes)).flatten).Nodup) := by
  decide

/-- Therefore no closed line ledger can consist of the correctly assigned C3
profiles followed by the untrimmed raw C7 payment. -/
theorem noClosedLineLedger_with_singletonPlanted_then_rawC7 :
    ¬ ∃ line : ClosedLineLedger 4 4,
      line.profiles = [singletonPlantedC3Payment0,
        singletonPlantedC3Payment1, singletonPlantedC3Payment2,
        singletonPlantedRawC7Payment] := by
  intro hline
  rcases hline with ⟨line, hprofiles⟩
  have howned := line.firstMatchOwnership
  rw [hprofiles] at howned
  exact singletonPlantedRawC7_breaks_firstMatchOwnership howned

/-- A one-line compiler fixture for the explicitly supplied earlier C3 order.
It is not a row-wide `(UNIF)` theorem. -/
def singletonPlantedC3Ledger : UniformClosedLedger 4 4 3 where
  lines := [singletonPlantedC3Line]
  windowUniformity := by
    intro line hline
    rcases List.mem_cons.mp hline with hEq | hNil
    · subst line
      decide
    · simp at hNil

/-- Replay the earlier-owner absorption through the existing line-local
compiler. -/
theorem singletonPlantedC3Ledger_compiles :
    singletonPlantedC3Ledger.rowBad ≤ 4 * 3 :=
  singletonPlantedC3Ledger.compile

#print axioms singletonPlantedRawSlopeCells_eq
#print axioms singletonPlanted_absorbs_rawC7
#print axioms singletonPlantedC3Line_totals
#print axioms singletonPlantedRawC7_breaks_firstMatchOwnership
#print axioms noClosedLineLedger_with_singletonPlanted_then_rawC7
#print axioms singletonPlantedC3Ledger_compiles

end AsymptoticSpine
