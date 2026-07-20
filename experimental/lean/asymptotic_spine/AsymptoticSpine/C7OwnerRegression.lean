import AsymptoticSpine.UniformClosedLedger

namespace AsymptoticSpine

/-!
# C7 raw-payment / first-match-owner regression

The algebraic source
`experimental/notes/thresholds/affine_steiner_quotient_owner.md` proves an
actual Reed--Solomon family with a local C7-style collapse: many support
witnesses project to one slope.  The same theorem proves that the supports are
complete fibres of a nontrivial quotient map, so the printed owner is C1, which
precedes C7.

This module formalizes only the finite first-match consequence at the
`UniformClosedLedger` boundary.  It does not reprove the finite-field algebra.
All values below form a one-slope interface model; the ledger fixture does not
assert completeness for an actual RS line, actual `(UNIF)`, or row closure.
Its purpose is to reject the invalid implication

`raw C7-style collapse + direct slope payment => nonempty C7 first-match owner`.

A direct payment can be numerically correct and still fail to populate a
closed line ledger when the same slope was already assigned to an earlier
cell.  The correct line-local sum retains the C1 payment and gives C7 no
assigned slope.
-/

/-- One slope appears in both the earlier C1 projection and the proposed raw
C7-style projection.  The natural number is only a finite slope identifier. -/
def affineSteinerC1C7RawSlopeCells : List (List Nat) := [[7], [7]]

/-- Ordered first match assigns the shared slope to C1 and leaves the proposed
C7 residual empty. -/
theorem affineSteinerC1C7_firstMatch :
    firstMatchLeaves [] affineSteinerC1C7RawSlopeCells = [[7], []] := by
  decide

/-- The finite-model earlier-owner payment.  No source-level natural-scale C1
payment is claimed. -/
def affineSteinerC1Payment : ProfilePayment 1 :=
  ProfilePayment.ofDirect .c1 [7] 1 1 (by decide) (by decide)

/-- The tempting raw C7 payment.  It is numerically valid in isolation, but it
uses the pre-deletion slope image rather than the assigned first-match cell. -/
def affineSteinerRawC7Payment : ProfilePayment 1 :=
  ProfilePayment.ofDirect .c7 [7] 1 1 (by decide) (by decide)

/-- The raw C7 payment really does satisfy the direct natural-scale inequality;
the obstruction below is ownership, not numerical payment. -/
theorem affineSteinerRawC7_numericallyPaid :
    affineSteinerRawC7Payment.rayBudget ≤
      1 * affineSteinerRawC7Payment.naturalScale :=
  affineSteinerRawC7Payment.paidAtNaturalScale

/-- Installing both raw projections as assigned profiles violates the exact
`ClosedLineLedger.firstMatchOwnership` field: the shared slope would be charged
twice. -/
theorem affineSteinerRawC7_breaks_firstMatchOwnership :
    ¬ (([affineSteinerC1Payment, affineSteinerRawC7Payment].map
      (fun profile => profile.assignedSlopes)).flatten.Nodup) := by
  decide

/-- Consequently there is no closed line ledger whose assigned profile list is
the earlier C1 payment followed by the untrimmed raw C7 payment. -/
theorem noClosedLineLedger_with_affineSteinerRawC7 :
    ¬ ∃ line : ClosedLineLedger 1 2,
      line.profiles =
        [affineSteinerC1Payment, affineSteinerRawC7Payment] := by
  intro hline
  rcases hline with ⟨line, hprofiles⟩
  have howned := line.firstMatchOwnership
  rw [hprofiles] at howned
  exact affineSteinerRawC7_breaks_firstMatchOwnership howned

/-- The correctly disjointized one-slope model contains only the C1 profile;
the post-C1 C7 residual is empty and is not inserted as a realized profile. -/
def affineSteinerCorrectLine : ClosedLineLedger 1 1 where
  badCount := 1
  profiles := [affineSteinerC1Payment]
  firstMatchOwnership := by decide
  atlasExhaustive := by decide
  profileCountControl := by decide

/-- A one-line interface fixture retaining the required line-local profile
sum.  It is not an actual RS row or an actual `(UNIF)` theorem. -/
def affineSteinerCorrectLedger : UniformClosedLedger 1 1 1 where
  lines := [affineSteinerCorrectLine]
  windowUniformity := by
    intro line hline
    rcases List.mem_cons.mp hline with hEq | hNil
    · subst line
      decide
    · simp at hNil

/-- In the finite model, the line-local distinct-slope budget and natural-scale
sum are both one; no raw C7 term is added after the C1 owner has paid the
slope. -/
theorem affineSteinerCorrectLine_totals :
    affineSteinerCorrectLine.budgetTotal = 1 ∧
      affineSteinerCorrectLine.naturalTotal = 1 := by
  decide

/-- Replay the finite-model owner assignment through the general compiler.
This is not actual `(UNIF)` or row closure. -/
theorem affineSteinerCorrectLedger_compiles :
    affineSteinerCorrectLedger.rowBad ≤ 1 * 1 :=
  affineSteinerCorrectLedger.compile

#print axioms affineSteinerC1C7_firstMatch
#print axioms affineSteinerRawC7_numericallyPaid
#print axioms affineSteinerRawC7_breaks_firstMatchOwnership
#print axioms noClosedLineLedger_with_affineSteinerRawC7
#print axioms affineSteinerCorrectLine_totals
#print axioms affineSteinerCorrectLedger_compiles

end AsymptoticSpine
