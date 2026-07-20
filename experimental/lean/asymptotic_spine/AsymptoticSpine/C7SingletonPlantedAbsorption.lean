import AsymptoticSpine.PrefixAtlas
import AsymptoticSpine.UniformClosedLedger

namespace AsymptoticSpine

/-!
# C7 singleton-planted absorption regression

The planted-cell grammar in
`experimental/asymptotic_rs_mca_frontiers.tex` permits a predetermined common
support divisor `P`; its planted-entropy lemma explicitly treats `|P| = o(n)`
as a subexponential profile factor.  Consequently the fixed atlas indexed by
evaluation points

`P_t(X) = X - t`,  `t in D`,

is a legitimate earlier C3 atlas unless an additional semantic restriction is
imposed: the `t`-profile contains every witness whose support contains `t`.
Every positive-agreement witness has nonempty support, so these profiles cover
all witnesses before C7.  On the base-pole family `q = n + 1 = exp(o(n))`; each
realized planted profile has at most `q` distinct slopes and is therefore paid
from the additive profile term with subexponential compiler loss.

This module formalizes the finite first-match interface consequence.  It does
not reprove the asymptotic field-size statement or finite-field locator algebra.
The fixture keeps the actual rooted object visible: witnesses carry a slope and
a nonempty support, singleton-root C3 cells overlap, slope-level first match
assigns every slope to C3, and the later raw C7 cell is empty.
-/

/-- Four finite witness records `(slope, support)`.  Each support is nonempty,
and the overlapping singleton-root profiles model the genuine divisors `X-t`. -/
def singletonPlantedWitnesses : List (Nat × List Nat) :=
  [(10, [0, 1]), (11, [1, 2]), (12, [2, 3]), (13, [3, 0])]

/-- Distinct slopes having a witness whose support contains the planted root
`t`. -/
def singletonPlantedSlopeCell (t : Nat) : List Nat :=
  realizedKeys
    (singletonPlantedWitnesses.filter fun witness => decide (t ∈ witness.2))
    (fun witness => witness.1)

/-- Fixed earlier C3 atlas, indexed before the received line by the four domain
points. -/
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
planted C3 profile; the later C7 assigned image is empty. -/
theorem singletonPlanted_absorbs_rawC7 :
    firstMatchLeaves [] singletonPlantedThenC7RawSlopeCells =
      [[10, 13], [11], [12], [], []] := by
  decide

/-- First earlier C3 payment.  Compiler loss `4` is the finite stand-in for the
source-side field-size factor `q = exp(o(n))`; natural scale is the additive
profile term `1`. -/
def singletonPlantedC3Payment0 : ProfilePayment 4 :=
  ProfilePayment.ofDirect .c3 [10, 13] 1 4 (by decide) (by decide)

/-- Second nonempty first-match C3 payment. -/
def singletonPlantedC3Payment1 : ProfilePayment 4 :=
  ProfilePayment.ofDirect .c3 [11] 1 4 (by decide) (by decide)

/-- Third nonempty first-match C3 payment. -/
def singletonPlantedC3Payment2 : ProfilePayment 4 :=
  ProfilePayment.ofDirect .c3 [12] 1 4 (by decide) (by decide)

/-- Correct closed line: every raw slope has already been assigned to C3, so no
C7 profile is installed. -/
def singletonPlantedC3Line : ClosedLineLedger 4 4 where
  badCount := 4
  profiles := [singletonPlantedC3Payment0,
    singletonPlantedC3Payment1, singletonPlantedC3Payment2]
  firstMatchOwnership := by decide
  atlasExhaustive := by decide
  profileCountControl := by decide

/-- The earlier C3 atlas has natural-profile sum `3` and compiler budget `12`;
this is the exact finite analogue of `q` loss times the additive profile sum. -/
theorem singletonPlantedC3Line_totals :
    singletonPlantedC3Line.naturalTotal = 3 ∧
      singletonPlantedC3Line.budgetTotal = 12 := by
  decide

/-- The tempting untrimmed C7 payment is numerically valid in isolation but has
no semantic assigned slope after the C3 atlas. -/
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

/-- A one-line compiler fixture for the paid earlier C3 atlas.  It is not a
row-wide `(UNIF)` theorem. -/
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
