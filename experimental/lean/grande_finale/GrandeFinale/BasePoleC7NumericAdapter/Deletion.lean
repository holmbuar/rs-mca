import GrandeFinale.BasePoleC7NumericAdapter.ProfilePayment

namespace GrandeFinale.BasePoleC7NumericAdapter

/-! ## Deletion-aware base-pole residual -/

/-- Literal deletion of every slope already present in the supplied earlier
assigned-slope image. -/
def basePoleSurvivors (earlier raw : List Nat) : List Nat :=
  raw.filter fun gamma => decide (gamma ∉ earlier)

@[simp] theorem mem_basePoleSurvivors (earlier raw : List Nat) (gamma : Nat) :
    gamma ∈ basePoleSurvivors earlier raw ↔ gamma ∈ raw ∧ gamma ∉ earlier := by
  simp [basePoleSurvivors]

/-- Deletion preserves the duplicate-free raw slope census. -/
theorem basePoleSurvivors_nodup (earlier raw : List Nat)
    (hraw : raw.Nodup) : (basePoleSurvivors earlier raw).Nodup :=
  List.filter_sublist.nodup hraw

/-- The survivor list cannot be longer than the supplied raw slope list. -/
theorem basePoleSurvivors_length_le_raw (earlier raw : List Nat) :
    (basePoleSurvivors earlier raw).length ≤ raw.length := by
  simpa [basePoleSurvivors] using
    List.length_filter_le (fun gamma => decide (gamma ∉ earlier)) raw

/-- Two-cell active first-match chart: `false` is the supplied earlier image and
`true` is the later raw base-pole image. -/
def twoCellSlopeSet (earlier raw : List Nat) : Bool → Finset Nat
  | false => earlier.toFinset
  | true => raw.toFinset

/-- The list deletion agrees exactly, after deduplication, with the active
`FirstMatchAddBack.firstMatchCell` construction for the later cell. -/
theorem basePoleSurvivors_toFinset_eq_firstMatchCell
    (earlier raw : List Nat) :
    (basePoleSurvivors earlier raw).toFinset =
      GrandeFinale.FirstMatchAddBack.firstMatchCell
        (Finset.univ : Finset Bool) (twoCellSlopeSet earlier raw) true := by
  ext gamma
  constructor
  · intro hgamma
    have hsurvivor : gamma ∈ basePoleSurvivors earlier raw := by
      simpa using hgamma
    have hdata := (mem_basePoleSurvivors earlier raw gamma).mp hsurvivor
    rw [GrandeFinale.FirstMatchAddBack.mem_firstMatchCell]
    refine ⟨?_, by simp, ?_⟩
    · simpa [twoCellSlopeSet] using hdata.1
    · intro j _hj hj
      cases j with
      | false =>
          have hearlier : gamma ∈ earlier := by
            simpa [twoCellSlopeSet] using hj
          exact (hdata.2 hearlier).elim
      | true => simp
  · intro hgamma
    rw [GrandeFinale.FirstMatchAddBack.mem_firstMatchCell] at hgamma
    have hraw : gamma ∈ raw := by
      simpa [twoCellSlopeSet] using hgamma.1
    have hearlier : gamma ∉ earlier := by
      intro hmem
      have hle := hgamma.2.2 false (by simp) (by
        simpa [twoCellSlopeSet] using hmem)
      simp at hle
    have hsurvivor : gamma ∈ basePoleSurvivors earlier raw :=
      (mem_basePoleSurvivors earlier raw gamma).mpr ⟨hraw, hearlier⟩
    simpa using hsurvivor

/-- Source theorem boundary consumed by this adapter.  Every field is assumed;
this structure does not derive the raw list from concrete RS data. -/
structure BasePoleSlopeSource where
  rawSlopes : List Nat
  rawSlopes_nodup : rawSlopes.Nodup
  qMinusOne : Nat
  rawCount_le_qMinusOne : rawSlopes.length ≤ qMinusOne

/-- One surviving slope receives one unit local direct payment. -/
def basePoleUnitProfile (gamma : Nat) : ProfilePayment 1 :=
  ProfilePayment.ofDirect [gamma] 1 1 (by simp) (by simp)

@[simp] theorem basePoleUnitProfile_assignedSlopes (gamma : Nat) :
    (basePoleUnitProfile gamma).assignedSlopes = [gamma] := rfl

@[simp] theorem basePoleUnitProfile_rayBudget (gamma : Nat) :
    (basePoleUnitProfile gamma).rayBudget = 1 := rfl

@[simp] theorem basePoleUnitProfile_naturalScale (gamma : Nat) :
    (basePoleUnitProfile gamma).naturalScale = 1 := rfl

/-- Lift unit local profiles to an arbitrary allowed compiler loss.  The local
ray budget remains one. -/
def unitProfiles {compilerLoss : Nat} (hLoss : 1 ≤ compilerLoss)
    (slopes : List Nat) : List (ProfilePayment compilerLoss) :=
  slopes.map fun gamma => (basePoleUnitProfile gamma).liftLoss hLoss

@[simp] theorem assignedSlopeImage_unitProfiles {compilerLoss : Nat}
    (hLoss : 1 ≤ compilerLoss) : ∀ slopes : List Nat,
    assignedSlopeImage (unitProfiles hLoss slopes) = slopes
  | [] => by simp [assignedSlopeImage, unitProfiles]
  | gamma :: slopes => by
      simp [assignedSlopeImage, unitProfiles,
        assignedSlopeImage_unitProfiles hLoss slopes]

@[simp] theorem budgetTotal_unitProfiles {compilerLoss : Nat}
    (hLoss : 1 ≤ compilerLoss) : ∀ slopes : List Nat,
    budgetTotal (unitProfiles hLoss slopes) = slopes.length
  | [] => by simp [budgetTotal, unitProfiles]
  | gamma :: slopes => by
      simp [budgetTotal, unitProfiles,
        budgetTotal_unitProfiles hLoss slopes]

@[simp] theorem naturalTotal_unitProfiles {compilerLoss : Nat}
    (hLoss : 1 ≤ compilerLoss) : ∀ slopes : List Nat,
    naturalTotal (unitProfiles hLoss slopes) = slopes.length
  | [] => by simp [naturalTotal, unitProfiles]
  | gamma :: slopes => by
      simp [naturalTotal, unitProfiles,
        naturalTotal_unitProfiles hLoss slopes]

/-- Surviving base-pole profiles after deleting the supplied earlier assigned
slope image. -/
def basePoleProfiles {compilerLoss : Nat} (hLoss : 1 ≤ compilerLoss)
    (earlier : List Nat) (source : BasePoleSlopeSource) :
    List (ProfilePayment compilerLoss) :=
  unitProfiles hLoss (basePoleSurvivors earlier source.rawSlopes)

@[simp] theorem assignedSlopeImage_basePoleProfiles {compilerLoss : Nat}
    (hLoss : 1 ≤ compilerLoss) (earlier : List Nat)
    (source : BasePoleSlopeSource) :
    assignedSlopeImage (basePoleProfiles hLoss earlier source) =
      basePoleSurvivors earlier source.rawSlopes := by
  simp [basePoleProfiles]

@[simp] theorem budgetTotal_basePoleProfiles {compilerLoss : Nat}
    (hLoss : 1 ≤ compilerLoss) (earlier : List Nat)
    (source : BasePoleSlopeSource) :
    budgetTotal (basePoleProfiles hLoss earlier source) =
      (basePoleSurvivors earlier source.rawSlopes).length := by
  simp [basePoleProfiles]

@[simp] theorem naturalTotal_basePoleProfiles {compilerLoss : Nat}
    (hLoss : 1 ≤ compilerLoss) (earlier : List Nat)
    (source : BasePoleSlopeSource) :
    naturalTotal (basePoleProfiles hLoss earlier source) =
      (basePoleSurvivors earlier source.rawSlopes).length := by
  simp [basePoleProfiles]

/-- The added direct payment is bounded by the supplied `q - 1` census. -/
theorem budgetTotal_basePoleProfiles_le_qMinusOne {compilerLoss : Nat}
    (hLoss : 1 ≤ compilerLoss) (earlier : List Nat)
    (source : BasePoleSlopeSource) :
    budgetTotal (basePoleProfiles hLoss earlier source) ≤ source.qMinusOne := by
  rw [budgetTotal_basePoleProfiles]
  exact (basePoleSurvivors_length_le_raw earlier source.rawSlopes).trans
    source.rawCount_le_qMinusOne

/-- The same census controls the added natural-scale sum. -/
theorem naturalTotal_basePoleProfiles_le_qMinusOne {compilerLoss : Nat}
    (hLoss : 1 ≤ compilerLoss) (earlier : List Nat)
    (source : BasePoleSlopeSource) :
    naturalTotal (basePoleProfiles hLoss earlier source) ≤ source.qMinusOne := by
  rw [naturalTotal_basePoleProfiles]
  exact (basePoleSurvivors_length_le_raw earlier source.rawSlopes).trans
    source.rawCount_le_qMinusOne


end GrandeFinale.BasePoleC7NumericAdapter
