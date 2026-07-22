import AsymptoticSpine.PrefixAtlas
import AsymptoticSpine.SemanticAtlasOwnership

namespace AsymptoticSpine

/-!
# C7 singleton-planted atlas-order regression

The archived broad planted-cell grammar permitted a predetermined common support
divisor `P` and treated `|P| = o(n)` as a subexponential profile factor.  Under
that permissive historical reading, the fixed catalogue indexed by evaluation
points

`P_t(X) = X - t`,  `t in D`,

contains every positive-agreement witness before C7.  The later base-pole C7
first-match image can therefore be empty even though its raw payment is valid.

This module checks only the finite list consequence of supplying that atlas
order.  It exposes active-atlas noncanonicity and does not select a policy.
`SemanticAtlasOwnership` is merely a labeled numeric interface: its provenance
labels prove no row-derived factor theorem and do not authorize singleton-root
C3 owners in an actual Reed--Solomon atlas.

Possible source-level resolutions remain external: restrict C3, require a
proved row-derived factor, exclude singleton profiles, place C7 earlier, or
accept the earlier assignment.  No finite-field locator algebra, actual
semantic owner, global atlas, line completeness, row-wide `(UNIF)`, or target
comparison is proved here.
-/

/-- Four finite records `(numeric slope, support)`.  Each support is nonempty,
and the overlapping singleton-root cells model the historical divisors `X-t`.
They are not asserted to arise from an actual RS line. -/
def singletonPlantedWitnesses : List (Nat × List Nat) :=
  [(10, [0, 1]), (11, [1, 2]), (12, [2, 3]), (13, [3, 0])]

/-- Distinct numeric slopes whose supplied support contains the root `t`. -/
def singletonPlantedSlopeCell (t : Nat) : List Nat :=
  realizedKeys
    (singletonPlantedWitnesses.filter fun witness => decide (t ∈ witness.2))
    (fun witness => witness.1)

/-- Fixed earlier candidate order, indexed before any received-line semantics by
four finite domain points.  The list is a regression input, not an active-atlas
theorem. -/
def singletonPlantedRawSlopeCells : List (List Nat) :=
  (List.range 4).map singletonPlantedSlopeCell

/-- Exact overlapping raw numeric slope images of the four candidate cells. -/
theorem singletonPlantedRawSlopeCells_eq :
    singletonPlantedRawSlopeCells =
      [[10, 13], [10, 11], [11, 12], [12, 13]] := by
  decide

/-- Add the tempting later raw C7 cell containing all four numeric slopes. -/
def singletonPlantedThenC7RawSlopeCells : List (List Nat) :=
  singletonPlantedRawSlopeCells ++ [[10, 11, 12, 13]]

/-- Ordered list-level first match assigns every value to an earlier candidate
cell; the later C7 leaf is empty. -/
theorem singletonPlanted_absorbs_rawC7 :
    firstMatchLeaves [] singletonPlantedThenC7RawSlopeCells =
      [[10, 13], [11], [12], [], []] := by
  decide

/-- First earlier labeled C3 payment in the finite numeric fixture.  Compiler
loss `4` is only a chosen arithmetic constant. -/
def singletonPlantedC3Payment0 : ProfilePayment 4 :=
  ProfilePayment.ofDirect .c3 [10, 13] 1 4 (by decide) (by decide)

/-- Second nonempty first-match numeric payment. -/
def singletonPlantedC3Payment1 : ProfilePayment 4 :=
  ProfilePayment.ofDirect .c3 [11] 1 4 (by decide) (by decide)

/-- Third nonempty first-match numeric payment. -/
def singletonPlantedC3Payment2 : ProfilePayment 4 :=
  ProfilePayment.ofDirect .c3 [12] 1 4 (by decide) (by decide)

/-- Closed numeric line under the explicitly supplied earlier order: every raw
value is assigned before C7, so no C7 profile is installed. -/
def singletonPlantedC3Line : ClosedLineLedger 4 4 where
  badCount := 4
  profiles := [singletonPlantedC3Payment0,
    singletonPlantedC3Payment1, singletonPlantedC3Payment2]
  firstMatchOwnership := by decide
  atlasExhaustive := by decide
  profileCountControl := by decide

/-- The supplied earlier line has natural-profile sum `3` and direct budget
`12`. -/
theorem singletonPlantedC3Line_totals :
    singletonPlantedC3Line.naturalTotal = 3 ∧
      singletonPlantedC3Line.budgetTotal = 12 := by
  decide

/-- The untrimmed raw C7 payment is numerically valid in isolation but has no
assigned value after the supplied earlier order. -/
def singletonPlantedRawC7Payment : ProfilePayment 4 :=
  ProfilePayment.ofDirect .c7 [10, 11, 12, 13] 1 4
    (by decide) (by decide)

/-- Appending the untrimmed raw C7 profile would charge all four values twice
and violates the closed-ledger disjointness field. -/
theorem singletonPlantedRawC7_breaks_firstMatchOwnership :
    ¬ ((([singletonPlantedC3Payment0, singletonPlantedC3Payment1,
      singletonPlantedC3Payment2, singletonPlantedRawC7Payment].map
        (fun profile => profile.assignedSlopes)).flatten).Nodup) := by
  decide

/-- Therefore no closed numeric line can consist of the assigned earlier
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

/-- A one-line compiler fixture for the explicitly supplied earlier order.  It
is neither a complete received-line list nor row-wide `(UNIF)`. -/
def singletonPlantedC3Ledger : UniformClosedLedger 4 4 3 where
  lines := [singletonPlantedC3Line]
  windowUniformity := by
    intro line hline
    rcases List.mem_cons.mp hline with hEq | hNil
    · subst line
      decide
    · simp at hNil

/-- Replay the supplied numeric order through the existing line-local compiler. -/
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
