import AsymptoticSpine.FirstMatch

namespace AsymptoticSpine

/-!
# True-R2 shell: gone by the end of C7, before C9

The complete true-`R = 2` shell in
`experimental/notes/audits/c9_true_r2_shell_realizability.md` is an exact
prefix fibre with exact MCA slopes.  It is not an eligible primitive C9 leaf.
Its full two-moment image has full effective span over the construction field,
while the realized image is exponentially smaller; the printed C7
effective-image-collapse trigger therefore fires before C9.

This module records two finite interface regressions at the exact `k = 6`
anchor from the source formulas.

1. After any C1--C6 deletion, the residual shell slopes occur in both the C7
   collapse projection and the later raw C9 projection.  Ordered first match
   removes all remaining shell slopes by the end of C7, so C9 is empty.
2. Residual self-normalization makes the single shell fibre look unit-paid, but
   the correct full-slice additive profile scale requires loss ten already at
   `k = 6`; loss nine fails.  This is the finite shadow of the proved asymptotic
   ratio `exp(k log(15/8) - O(log k))`.

The module does not prove the source asymptotics, the full-span field theorem,
or a paid C7 profile.  It formalizes their exact finite first-match and cleared
normalization consequences.  In particular, it does not turn the family into a
C9 producer or assert that C7, rather than C1--C6, is always the least owner.
-/

/-- The twenty exact central-shell slopes at the `k = 6` finite anchor are
represented by duplicate-free identifiers `0,...,19`. -/
def trueR2K6Slopes : List Nat := List.range 20

/-- C7 effective-image-collapse projection followed by the tempting later raw
C9 projection of the same shell slopes. -/
def trueR2C7ThenC9RawSlopeCells : List (List Nat) :=
  [trueR2K6Slopes, trueR2K6Slopes]

/-- With no C1--C6 deletion in the finite fixture, C7 receives the complete
shell image and C9 receives nothing. -/
theorem trueR2_c7Collapse_before_c9 :
    firstMatchLeaves [] trueR2C7ThenC9RawSlopeCells =
      [trueR2K6Slopes, []] := by
  decide

/-- More generally, after any aggregate C1--C6 deletion set `earlier`, the
remaining shell slopes are assigned no later than C7 and the C9 leaf is empty. -/
theorem trueR2_gone_by_end_of_c7 (earlier : List Nat) :
    firstMatchLeaves earlier trueR2C7ThenC9RawSlopeCells =
      [newPaid earlier trueR2K6Slopes, []] := by
  simp [trueR2C7ThenC9RawSlopeCells, firstMatchLeaves, newPaid]
  intro a ha hnot
  exact ⟨ha, hnot⟩

/-- Exact full fixed-weight slice mass `M_6 = binom(24,12)`. -/
def trueR2K6FullMass : Nat := 2704156

/-- Exact realized two-moment image size from
`[x^12](F(x)^6 + 6 x^2 F(x)^5)`. -/
def trueR2K6ImageSize : Nat := 2545055

/-- Exact central shell fibre and slope count `binom(6,3)`. -/
def trueR2K6SlopeCount : Nat := 20

/-- Clearing the realized-image denominator `L`, the additive natural profile
term `1 + M/L` has numerator `L + M`. -/
def trueR2K6FullProfileScaleN : Nat :=
  trueR2K6ImageSize + trueR2K6FullMass

/-- Clearing the same denominator, the direct distinct-slope charge is
`|Z| * L`. -/
def trueR2K6FullSlopeChargeN : Nat :=
  trueR2K6SlopeCount * trueR2K6ImageSize

/-- The stale residual-only normalization takes the residual mass to be the one
shell fibre and its residual image to have size one. -/
def trueR2K6ResidualSelfScaleN : Nat := trueR2K6SlopeCount + 1

def trueR2K6ResidualSelfChargeN : Nat := trueR2K6SlopeCount

/-- Residual self-normalization falsely makes the shell look paid with loss one:
`20 <= 1 * (20 + 1)`. -/
theorem trueR2K6_residual_self_normalization_passes :
    trueR2K6ResidualSelfChargeN ≤ trueR2K6ResidualSelfScaleN := by
  decide

/-- Correct full-slice normalization rejects loss nine:
`20 * 2545055 > 9 * (2545055 + 2704156)`. -/
theorem trueR2K6_full_slice_loss_nine_fails :
    ¬ (trueR2K6FullSlopeChargeN ≤
      9 * trueR2K6FullProfileScaleN) := by
  decide

/-- Loss ten is the first integer loss paying the exact `k = 6` cleared profile
term.  The asymptotic source theorem proves that the required loss then grows
exponentially, so this finite success is not a uniform C7 or C9 payment. -/
theorem trueR2K6_full_slice_loss_ten_passes :
    trueR2K6FullSlopeChargeN ≤
      10 * trueR2K6FullProfileScaleN := by
  decide

/-- Exact integer ceiling of the finite full-slice loss is ten. -/
theorem trueR2K6_required_loss_eq_ten :
    (trueR2K6FullSlopeChargeN + trueR2K6FullProfileScaleN - 1) /
      trueR2K6FullProfileScaleN = 10 := by
  decide

/-- The two normalization conventions really disagree at the same finite shell:
loss one passes residual self-normalization but fails the correct full-slice
scale. -/
theorem trueR2K6_normalization_regression :
    trueR2K6ResidualSelfChargeN ≤ trueR2K6ResidualSelfScaleN ∧
      ¬ (trueR2K6FullSlopeChargeN ≤ trueR2K6FullProfileScaleN) := by
  decide

#print axioms trueR2_c7Collapse_before_c9
#print axioms trueR2_gone_by_end_of_c7
#print axioms trueR2K6_residual_self_normalization_passes
#print axioms trueR2K6_full_slice_loss_nine_fails
#print axioms trueR2K6_full_slice_loss_ten_passes
#print axioms trueR2K6_required_loss_eq_ten
#print axioms trueR2K6_normalization_regression

end AsymptoticSpine
