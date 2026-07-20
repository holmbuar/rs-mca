import GrandeFinale.BasePoleC7NumericAdapter.Deletion

namespace GrandeFinale.BasePoleC7NumericAdapter

/-! ## Generic line-local extension -/

/-- Append the surviving unit profiles to an arbitrary prior numeric profile
list with compiler loss at least one. -/
def extendProfiles {compilerLoss : Nat} (hLoss : 1 ≤ compilerLoss)
    (source : BasePoleSlopeSource)
    (prior : List (ProfilePayment compilerLoss)) :
    List (ProfilePayment compilerLoss) :=
  prior ++ basePoleProfiles hLoss (assignedSlopeImage prior) source

/-- Deletion makes the appended survivor image disjoint from every earlier
assigned slope. -/
theorem earlier_append_basePoleSurvivors_nodup
    (earlier raw : List Nat) (hearlier : earlier.Nodup) (hraw : raw.Nodup) :
    (earlier ++ basePoleSurvivors earlier raw).Nodup := by
  apply List.nodup_append.mpr
  refine ⟨hearlier, basePoleSurvivors_nodup earlier raw hraw, ?_⟩
  intro a ha b hb hab
  have hbdata := (mem_basePoleSurvivors earlier raw b).mp hb
  exact hbdata.2 (hab ▸ ha)

/-- Exact assigned-slope telescope for the extension. -/
theorem assignedSlopeImage_extendProfiles {compilerLoss : Nat}
    (hLoss : 1 ≤ compilerLoss) (source : BasePoleSlopeSource)
    (prior : List (ProfilePayment compilerLoss)) :
    assignedSlopeImage (extendProfiles hLoss source prior) =
      assignedSlopeImage prior ++
        basePoleSurvivors (assignedSlopeImage prior) source.rawSlopes := by
  simp [extendProfiles]

/-- A duplicate-free prior image remains duplicate-free after extension. -/
theorem assignedSlopeImage_extendProfiles_nodup {compilerLoss : Nat}
    (hLoss : 1 ≤ compilerLoss) (source : BasePoleSlopeSource)
    (prior : List (ProfilePayment compilerLoss))
    (hprior : (assignedSlopeImage prior).Nodup) :
    (assignedSlopeImage (extendProfiles hLoss source prior)).Nodup := by
  rw [assignedSlopeImage_extendProfiles]
  exact earlier_append_basePoleSurvivors_nodup
    (assignedSlopeImage prior) source.rawSlopes hprior source.rawSlopes_nodup

/-- Exact line-local direct-budget telescope. -/
theorem budgetTotal_extendProfiles {compilerLoss : Nat}
    (hLoss : 1 ≤ compilerLoss) (source : BasePoleSlopeSource)
    (prior : List (ProfilePayment compilerLoss)) :
    budgetTotal (extendProfiles hLoss source prior) =
      budgetTotal prior +
        (basePoleSurvivors (assignedSlopeImage prior) source.rawSlopes).length := by
  simp [extendProfiles]

/-- Exact line-local natural-scale telescope. -/
theorem naturalTotal_extendProfiles {compilerLoss : Nat}
    (hLoss : 1 ≤ compilerLoss) (source : BasePoleSlopeSource)
    (prior : List (ProfilePayment compilerLoss)) :
    naturalTotal (extendProfiles hLoss source prior) =
      naturalTotal prior +
        (basePoleSurvivors (assignedSlopeImage prior) source.rawSlopes).length := by
  simp [extendProfiles]

/-- The combined direct budget grows by at most the supplied `q - 1` census. -/
theorem budgetTotal_extendProfiles_le_prior_add_qMinusOne
    {compilerLoss : Nat} (hLoss : 1 ≤ compilerLoss)
    (source : BasePoleSlopeSource)
    (prior : List (ProfilePayment compilerLoss)) :
    budgetTotal (extendProfiles hLoss source prior) ≤
      budgetTotal prior + source.qMinusOne := by
  rw [budgetTotal_extendProfiles]
  exact Nat.add_le_add_left
    ((basePoleSurvivors_length_le_raw
      (assignedSlopeImage prior) source.rawSlopes).trans
        source.rawCount_le_qMinusOne) _

/-- The combined natural-scale sum obeys the same exact census bound. -/
theorem naturalTotal_extendProfiles_le_prior_add_qMinusOne
    {compilerLoss : Nat} (hLoss : 1 ≤ compilerLoss)
    (source : BasePoleSlopeSource)
    (prior : List (ProfilePayment compilerLoss)) :
    naturalTotal (extendProfiles hLoss source prior) ≤
      naturalTotal prior + source.qMinusOne := by
  rw [naturalTotal_extendProfiles]
  exact Nat.add_le_add_left
    ((basePoleSurvivors_length_le_raw
      (assignedSlopeImage prior) source.rawSlopes).trans
        source.rawCount_le_qMinusOne) _

/-- The extension adds no more realized profiles than raw supplied slopes. -/
theorem length_extendProfiles_le_prior_add_raw {compilerLoss : Nat}
    (hLoss : 1 ≤ compilerLoss) (source : BasePoleSlopeSource)
    (prior : List (ProfilePayment compilerLoss)) :
    (extendProfiles hLoss source prior).length ≤
      prior.length + source.rawSlopes.length := by
  rw [extendProfiles, List.length_append]
  exact Nat.add_le_add_left (by
    simpa [basePoleProfiles, unitProfiles] using
      basePoleSurvivors_length_le_raw
        (assignedSlopeImage prior) source.rawSlopes) _

/-! ## Executable finite regressions -/

/-- An untrimmed later payment double charges a slope already assigned earlier;
the deletion-aware residual is empty. -/
theorem affineSteiner_doubleCharge_regression :
    basePoleSurvivors [7] [7] = [] ∧ ¬ ([7] ++ [7]).Nodup := by
  decide

/-- A broad earlier singleton-root atlas can erase the later residual, whereas
an empty earlier image leaves it intact.  This is atlas-order noncanonicity, not
a theorem selecting either policy. -/
theorem singletonPlanted_atlasOrder_regression :
    basePoleSurvivors [10, 13, 11, 12] [10, 11, 12, 13] = [] ∧
      basePoleSurvivors [] [10, 11, 12, 13] = [10, 11, 12, 13] := by
  decide

/-- Basic deletion fixture. -/
theorem basePole_deletion_fixture :
    basePoleSurvivors [2, 4, 9] [1, 2, 3, 4] = [1, 3] := by
  decide

/-- A unit direct payment lifted from loss one to loss three; every local budget
remains one. -/
def liftedUnitFixture : ProfilePayment 3 :=
  (basePoleUnitProfile 9).liftLoss (by decide)

theorem liftedUnitFixture_preservesLocalBudgets :
    liftedUnitFixture.residualBudget = 1 ∧
      liftedUnitFixture.sidonBudget = 1 ∧
      liftedUnitFixture.rayBudget = 1 ∧
      liftedUnitFixture.naturalScale = 1 := by
  decide

/-- Prior line-local payment used by the extension fixture. -/
def extensionFixturePriorProfile : ProfilePayment 3 :=
  (ProfilePayment.ofDirect [100, 102] 2 1 (by decide) (by decide)).liftLoss
    (by decide)

/-- Supplied source boundary for the extension fixture. -/
def extensionFixtureSource : BasePoleSlopeSource where
  rawSlopes := [100, 101, 102, 103]
  rawSlopes_nodup := by decide
  qMinusOne := 4
  rawCount_le_qMinusOne := by decide

/-- The generic-loss extension deletes earlier slopes, preserves unit local C7
budgets, and gives the exact `2 + 2` telescopes. -/
theorem extensionFixture_exact :
    assignedSlopeImage
        (extendProfiles (by decide) extensionFixtureSource
          [extensionFixturePriorProfile]) = [100, 102, 101, 103] ∧
      budgetTotal
        (extendProfiles (by decide) extensionFixtureSource
          [extensionFixturePriorProfile]) = 4 ∧
      naturalTotal
        (extendProfiles (by decide) extensionFixtureSource
          [extensionFixturePriorProfile]) = 4 := by
  decide

#print axioms ProfilePayment.paidAtNaturalScale
#print axioms ProfilePayment.liftLoss
#print axioms ProfilePayment.toPrimitiveCellBudget
#print axioms assignedSlopeImage_length_le_loss_mul_naturalTotal
#print axioms basePoleSurvivors_toFinset_eq_firstMatchCell
#print axioms assignedSlopeImage_extendProfiles_nodup
#print axioms budgetTotal_extendProfiles
#print axioms naturalTotal_extendProfiles
#print axioms budgetTotal_extendProfiles_le_prior_add_qMinusOne
#print axioms affineSteiner_doubleCharge_regression
#print axioms singletonPlanted_atlasOrder_regression
#print axioms extensionFixture_exact


end GrandeFinale.BasePoleC7NumericAdapter
