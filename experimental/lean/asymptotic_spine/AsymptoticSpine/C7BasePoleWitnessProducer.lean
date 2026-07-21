import AsymptoticSpine.PrefixAtlas
import AsymptoticSpine.C7BasePoleProducer

namespace AsymptoticSpine

/-!
# Rooted witness adapter for the C7 base-pole class

`C7BasePoleProducer` begins at a raw distinct-slope list. This module records
the preceding finite interface supplied by the constant-coefficient partition
in `experimental/notes/thresholds/aperiodic_one_ray_saturation.md`.

For one received base-pole line, every raw witness has a locator constant
coefficient `d`, and its final slope is `slopeOfCoeff d` (mathematically `-d`).
Injectivity of `slopeOfCoeff` turns the realized coefficient list into a
duplicate-free raw slope list. Deleting a supplied earlier owner image gives
the literal C7 first-match image, and the singleton direct budget is at most the
source-side `q - 1` realized-coefficient census.

The structure below is an interface to the proved source theorem; it does not
reprove finite-field locator algebra. It also does not construct the earlier
semantic atlas, prove survivor nonemptiness, establish a fixed-before-line
global atlas, prove row-wide uniformity, or compare with a target.
-/

/-- Source-facing data for one base-pole constant-coefficient witness class on
one received line. -/
structure BasePoleC7WitnessClass where
  witnesses : List Nat
  witnesses_nodup : witnesses.Nodup
  constantCoeff : Nat → Nat
  slopeOfCoeff : Nat → Nat
  slope : Nat → Nat
  slope_from_coeff :
    ∀ w, w ∈ witnesses → slope w = slopeOfCoeff (constantCoeff w)
  slopeOfCoeff_injective : Function.Injective slopeOfCoeff
  qMinusOne : Nat
  realizedCoeffCount :
    (realizedKeys witnesses constantCoeff).length ≤ qMinusOne

namespace BasePoleC7WitnessClass

/-- Constant coefficients actually realized by raw witnesses. -/
def realizedCoeffs (data : BasePoleC7WitnessClass) : List Nat :=
  realizedKeys data.witnesses data.constantCoeff

/-- Canonical witness fibres indexed by realized constant coefficients. -/
def rawWitnessCells (data : BasePoleC7WitnessClass) : List (List Nat) :=
  totalFibreAtlas data.witnesses data.constantCoeff

/-- The raw distinct-slope image supplied by the base-pole source theorem. -/
def rawSlopes (data : BasePoleC7WitnessClass) : List Nat :=
  data.realizedCoeffs.map data.slopeOfCoeff

/-- The realized coefficient census is bounded by the source-side `q - 1`. -/
theorem realizedCoeffs_length_le_qMinusOne
    (data : BasePoleC7WitnessClass) :
    data.realizedCoeffs.length ≤ data.qMinusOne := by
  simpa [realizedCoeffs] using data.realizedCoeffCount

/-- Injectivity of the coefficient-to-slope law makes the raw slope image
collision-free. -/
theorem rawSlopes_nodup (data : BasePoleC7WitnessClass) :
    data.rawSlopes.Nodup := by
  exact nodup_map_of_injective data.slopeOfCoeff_injective
    (realizedKeys_nodup data.constantCoeff data.witnesses)

/-- The raw distinct-slope image has at most `q - 1` elements. -/
theorem rawSlopes_length_le_qMinusOne
    (data : BasePoleC7WitnessClass) :
    data.rawSlopes.length ≤ data.qMinusOne := by
  simpa [rawSlopes, realizedCoeffs] using data.realizedCoeffCount

/-- The realized constant-coefficient fibres are duplicate-free and
witness-exhaustive, and their number is at most `q - 1`. -/
theorem rawWitnessCells_total (data : BasePoleC7WitnessClass) :
    data.rawWitnessCells.flatten.Nodup
      ∧ (∀ w, w ∈ data.rawWitnessCells.flatten ↔ w ∈ data.witnesses)
      ∧ (∀ w,
        w ∈ (firstMatchLeaves [] data.rawWitnessCells).flatten ↔
          w ∈ data.witnesses)
      ∧ data.rawWitnessCells.length ≤ data.qMinusOne := by
  simpa [rawWitnessCells] using
    prefixFibreAtlas_total data.witnesses data.constantCoeff data.qMinusOne
      data.witnesses_nodup data.realizedCoeffCount

/-- One raw constant-coefficient witness fibre. -/
def constantCoeffCell (data : BasePoleC7WitnessClass) (d : Nat) : List Nat :=
  data.witnesses.filter fun w => decide (data.constantCoeff w = d)

/-- Every witness in the `d`-cell has the one final slope prescribed by `d`. -/
theorem slope_eq_of_mem_constantCoeffCell
    (data : BasePoleC7WitnessClass) (d w : Nat)
    (hw : w ∈ data.constantCoeffCell d) :
    data.slope w = data.slopeOfCoeff d := by
  have hwitness : w ∈ data.witnesses :=
    (List.mem_filter.mp hw).1
  have hcoeff : data.constantCoeff w = d :=
    of_decide_eq_true (List.mem_filter.mp hw).2
  calc
    data.slope w = data.slopeOfCoeff (data.constantCoeff w) :=
      data.slope_from_coeff w hwitness
    _ = data.slopeOfCoeff d := by rw [hcoeff]

/-- The raw slope list is exactly the slope image of the raw witness catalogue,
at the membership level. -/
theorem mem_rawSlopes_iff_mem_witnessSlopeImage
    (data : BasePoleC7WitnessClass) (gamma : Nat) :
    gamma ∈ data.rawSlopes ↔ gamma ∈ data.witnesses.map data.slope := by
  constructor
  · intro hgamma
    rw [rawSlopes, realizedCoeffs, List.mem_map] at hgamma
    rcases hgamma with ⟨d, hd, hgamma⟩
    have hdmap : d ∈ data.witnesses.map data.constantCoeff :=
      (mem_realizedKeys_iff data.witnesses data.constantCoeff d).mp hd
    rw [List.mem_map] at hdmap
    rcases hdmap with ⟨w, hw, hcoeff⟩
    apply List.mem_map.mpr
    refine ⟨w, hw, ?_⟩
    calc
      data.slope w = data.slopeOfCoeff (data.constantCoeff w) :=
        data.slope_from_coeff w hw
      _ = data.slopeOfCoeff d := by rw [hcoeff]
      _ = gamma := hgamma
  · intro hgamma
    rw [List.mem_map] at hgamma
    rcases hgamma with ⟨w, hw, hslope⟩
    rw [rawSlopes, realizedCoeffs]
    apply List.mem_map.mpr
    refine ⟨data.constantCoeff w, ?_, ?_⟩
    · rw [mem_realizedKeys_iff]
      exact List.mem_map.mpr ⟨w, hw, rfl⟩
    · calc
        data.slopeOfCoeff (data.constantCoeff w) = data.slope w :=
          (data.slope_from_coeff w hw).symm
        _ = gamma := hslope

/-- Actual C7 first-match slopes after deleting the supplied earlier owner
slope image on this received line. -/
def assignedSlopes (data : BasePoleC7WitnessClass)
    (earlier : List Nat) : List Nat :=
  basePoleC7AssignedSlopes earlier data.rawSlopes

@[simp] theorem mem_assignedSlopes
    (data : BasePoleC7WitnessClass) (earlier : List Nat) (gamma : Nat) :
    gamma ∈ data.assignedSlopes earlier ↔
      gamma ∈ data.rawSlopes ∧ gamma ∉ earlier := by
  simp [assignedSlopes]

/-- Every assigned C7 slope is rooted in an actual raw witness and is certified
not to be in the supplied earlier slope image. -/
theorem assignedSlope_has_surviving_witness
    (data : BasePoleC7WitnessClass) (earlier : List Nat) (gamma : Nat)
    (hgamma : gamma ∈ data.assignedSlopes earlier) :
    ∃ w, w ∈ data.witnesses ∧ data.slope w = gamma ∧ gamma ∉ earlier := by
  have hassigned := (mem_assignedSlopes data earlier gamma).mp hgamma
  have hwimage :=
    (mem_rawSlopes_iff_mem_witnessSlopeImage data gamma).mp hassigned.1
  rw [List.mem_map] at hwimage
  rcases hwimage with ⟨w, hw, hslope⟩
  exact ⟨w, hw, hslope, hassigned.2⟩

/-- Direct singleton budget for the post-deletion rooted C7 image. -/
def directBudget (data : BasePoleC7WitnessClass) (earlier : List Nat) : Nat :=
  basePoleC7DirectBudget earlier data.rawSlopes

/-- Rooted local payment: the direct post-deletion C7 slope budget is at most
the source-side `q - 1` census. -/
theorem directBudget_le_qMinusOne
    (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    data.directBudget earlier ≤ data.qMinusOne := by
  exact basePoleC7DirectBudget_le_qMinusOne
    earlier data.rawSlopes data.qMinusOne data.rawSlopes_length_le_qMinusOne

/-- Executable rooted fixture: four witnesses realize four coefficient/slope
cells; earlier owners delete `100` and `102`, leaving `101` and `103`. -/
def rootedFixture : BasePoleC7WitnessClass where
  witnesses := [0, 1, 2, 3]
  witnesses_nodup := by decide
  constantCoeff := fun w => w
  slopeOfCoeff := fun d => d + 100
  slope := fun w => w + 100
  slope_from_coeff := by
    intro w _hw
    rfl
  slopeOfCoeff_injective := by
    intro a b h
    exact Nat.add_right_cancel h
  qMinusOne := 4
  realizedCoeffCount := by decide

theorem rootedFixture_rawSlopes :
    rootedFixture.rawSlopes = [100, 101, 102, 103] := by
  decide

theorem rootedFixture_assignedSlopes :
    rootedFixture.assignedSlopes [100, 102] = [101, 103] := by
  decide

theorem rootedFixture_directBudget :
    rootedFixture.directBudget [100, 102] = 2 := by
  decide

#print axioms rawWitnessCells_total
#print axioms slope_eq_of_mem_constantCoeffCell
#print axioms mem_rawSlopes_iff_mem_witnessSlopeImage
#print axioms assignedSlope_has_surviving_witness
#print axioms directBudget_le_qMinusOne
#print axioms rootedFixture_directBudget

end BasePoleC7WitnessClass

end AsymptoticSpine
