import AsymptoticSpine.PrefixAtlas
import AsymptoticSpine.C7BasePoleProducer

namespace AsymptoticSpine

/-!
# Rooted witness adapter for the C7 base-pole class

`C7BasePoleProducer` begins at the proved source-side distinct-slope list.  This
module records the preceding, source-specific finite interface for the
constant-coefficient partition from
`experimental/notes/thresholds/aperiodic_one_ray_saturation.md`.

For one received base-pole line, every raw witness has a locator constant
coefficient `d`, and the source theorem identifies its final slope as the
injective image `slopeOfCoeff d` (mathematically `-d`).  The realized
constant-coefficient fibres therefore form a witness-exhaustive atlas whose raw
slope image is duplicate-free.  Deleting the aggregate C1--C6 slope image gives
the actual C7 first-match owner.  The surviving slopes are then handed to the
unit-scale direct producer already formalized in `C7BasePoleProducer`.

The finite structure below is not a new generic atlas.  It is the exact typed
boundary supplied by the base-pole theorem: witness catalogue, constant
coefficient, final slope law, injectivity of `d |-> -d`, and the `q - 1`
realized-coefficient census.  No survivor nonemptiness, global atlas, row-wide
`(UNIF)`, or target comparison is asserted.
-/

/-- Source-facing data for one real base-pole constant-coefficient witness
class on one received line. -/
structure BasePoleC7WitnessClass where
  witnesses : List Nat
  witnesses_nodup : witnesses.Nodup
  constantCoeff : Nat -> Nat
  slopeOfCoeff : Nat -> Nat
  slope : Nat -> Nat
  slope_from_coeff :
    forall w, w ∈ witnesses -> slope w = slopeOfCoeff (constantCoeff w)
  slopeOfCoeff_injective : Function.Injective slopeOfCoeff
  qMinusOne : Nat
  realizedCoeffCount :
    (realizedKeys witnesses constantCoeff).length <= qMinusOne

namespace BasePoleC7WitnessClass

/-- Constant coefficients actually realized by raw witnesses. -/
def realizedCoeffs (data : BasePoleC7WitnessClass) : List Nat :=
  realizedKeys data.witnesses data.constantCoeff

/-- Canonical witness fibres indexed by the realized constant coefficients. -/
def rawWitnessCells (data : BasePoleC7WitnessClass) : List (List Nat) :=
  totalFibreAtlas data.witnesses data.constantCoeff

/-- The raw distinct-slope image supplied by the base-pole theorem. -/
def rawSlopes (data : BasePoleC7WitnessClass) : List Nat :=
  data.realizedCoeffs.map data.slopeOfCoeff

/-- The raw constant-coefficient census is bounded by the source-side
`q - 1` count. -/
theorem realizedCoeffs_length_le_qMinusOne
    (data : BasePoleC7WitnessClass) :
    data.realizedCoeffs.length <= data.qMinusOne := by
  simpa [realizedCoeffs] using data.realizedCoeffCount

/-- Injectivity of `d |-> slope(d)` turns the realized coefficient list into a
duplicate-free raw slope image. -/
theorem rawSlopes_nodup (data : BasePoleC7WitnessClass) :
    data.rawSlopes.Nodup := by
  exact nodup_map_of_injective data.slopeOfCoeff_injective
    (realizedKeys_nodup data.constantCoeff data.witnesses)

/-- The raw distinct-slope image has at most `q - 1` elements. -/
theorem rawSlopes_length_le_qMinusOne
    (data : BasePoleC7WitnessClass) :
    data.rawSlopes.length <= data.qMinusOne := by
  simpa [rawSlopes, realizedCoeffs] using data.realizedCoeffCount

/-- The realized constant-coefficient fibres are a duplicate-free,
witness-exhaustive raw atlas, and their number is bounded by `q - 1`. -/
theorem rawWitnessCells_total (data : BasePoleC7WitnessClass) :
    data.rawWitnessCells.flatten.Nodup
      /\ (forall w, w ∈ data.rawWitnessCells.flatten <-> w ∈ data.witnesses)
      /\ (forall w,
        w ∈ (firstMatchLeaves [] data.rawWitnessCells).flatten <->
          w ∈ data.witnesses)
      /\ data.rawWitnessCells.length <= data.qMinusOne := by
  simpa [rawWitnessCells] using
    prefixFibreAtlas_total data.witnesses data.constantCoeff data.qMinusOne
      data.witnesses_nodup data.realizedCoeffCount

/-- One raw constant-coefficient fibre. -/
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

/-- The constructed raw slope list is exactly the slope image of the raw
witness catalogue, at the membership level. -/
theorem mem_rawSlopes_iff_mem_witnessSlopeImage
    (data : BasePoleC7WitnessClass) (gamma : Nat) :
    gamma ∈ data.rawSlopes <-> gamma ∈ data.witnesses.map data.slope := by
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

/-- Actual C7 first-match slopes after deleting the aggregate C1--C6 slope
image on this received line. -/
def assignedSlopes (data : BasePoleC7WitnessClass)
    (earlier : List Nat) : List Nat :=
  basePoleC7AssignedSlopes earlier data.rawSlopes

@[simp] theorem mem_assignedSlopes
    (data : BasePoleC7WitnessClass) (earlier : List Nat) (gamma : Nat) :
    gamma ∈ data.assignedSlopes earlier <->
      gamma ∈ data.rawSlopes /\ gamma ∉ earlier := by
  simp [assignedSlopes]

/-- Every assigned C7 slope is rooted in an actual raw witness and is certified
not to have been owned by C1--C6. -/
theorem assignedSlope_has_surviving_witness
    (data : BasePoleC7WitnessClass) (earlier : List Nat) (gamma : Nat)
    (hgamma : gamma ∈ data.assignedSlopes earlier) :
    exists w, w ∈ data.witnesses /\ data.slope w = gamma /\ gamma ∉ earlier := by
  have hassigned := (mem_assignedSlopes data earlier gamma).mp hgamma
  have hwimage :=
    (mem_rawSlopes_iff_mem_witnessSlopeImage data gamma).mp hassigned.1
  rw [List.mem_map] at hwimage
  rcases hwimage with ⟨w, hw, hslope⟩
  exact ⟨w, hw, hslope, hassigned.2⟩

/-- Closed-ledger C7 residual produced from the rooted witness class. -/
def c7Line (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    ClosedLineLedger 1 data.rawSlopes.length :=
  basePoleC7Line earlier data.rawSlopes data.rawSlopes_nodup

/-- The line's assigned slope image is exactly the post-C1--C6 witness slope
image. -/
theorem c7Line_flatten_assignedSlopes
    (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    (((data.c7Line earlier).profiles.map
      (fun profile => profile.assignedSlopes)).flatten) =
        data.assignedSlopes earlier := by
  simpa [c7Line, assignedSlopes] using
    basePoleC7Profiles_flatten_assignedSlopes earlier data.rawSlopes

/-- The rooted line-local C7 ray budget is bounded by `q - 1`. -/
theorem c7Line_budgetTotal_le_qMinusOne
    (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    (data.c7Line earlier).budgetTotal <= data.qMinusOne := by
  exact basePoleC7Line_budgetTotal_le_qMinusOne
    earlier data.rawSlopes data.rawSlopes_nodup data.qMinusOne
      data.rawSlopes_length_le_qMinusOne

/-- The rooted line-local natural-profile sum is also bounded by `q - 1`. -/
theorem c7Line_naturalTotal_le_qMinusOne
    (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    (data.c7Line earlier).naturalTotal <= data.qMinusOne := by
  exact Nat.le_trans
    (basePoleC7Line_naturalTotal_le_raw
      earlier data.rawSlopes data.rawSlopes_nodup)
    data.rawSlopes_length_le_qMinusOne

/-- One-line source-facing wrapper.  Its envelope is the actual `q - 1` raw
constant-coefficient census, while the sum inside the line uses only surviving
profiles. -/
def c7Ledger (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    UniformClosedLedger 1 data.rawSlopes.length data.qMinusOne where
  lines := [data.c7Line earlier]
  windowUniformity := by
    intro line hline
    rcases List.mem_cons.mp hline with hEq | hNil
    · subst line
      exact data.c7Line_naturalTotal_le_qMinusOne earlier
    · simp at hNil

/-- Rooted C7 producer theorem: raw witnesses are partitioned by constant
coefficient, their exact slope image is deleted by earlier owners, every
surviving singleton is paid at unit natural scale, and the correct line-local
profile sum is at most `q - 1`. -/
theorem c7Ledger_compiles
    (data : BasePoleC7WitnessClass) (earlier : List Nat) :
    (data.c7Ledger earlier).rowBad <= data.qMinusOne := by
  simpa using (data.c7Ledger earlier).compile

/-- Executable rooted fixture: four witnesses realize four coefficient/slope
cells; earlier owners delete slopes `100` and `102`, leaving `101` and `103`. -/
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
    omega
  qMinusOne := 4
  realizedCoeffCount := by decide

 theorem rootedFixture_rawSlopes :
    rootedFixture.rawSlopes = [100, 101, 102, 103] := by
  decide

 theorem rootedFixture_assignedSlopes :
    rootedFixture.assignedSlopes [100, 102] = [101, 103] := by
  decide

 theorem rootedFixture_compiles :
    (rootedFixture.c7Ledger [100, 102]).rowBad <= 4 :=
  rootedFixture.c7Ledger_compiles [100, 102]

#print axioms rawWitnessCells_total
#print axioms slope_eq_of_mem_constantCoeffCell
#print axioms mem_rawSlopes_iff_mem_witnessSlopeImage
#print axioms assignedSlope_has_surviving_witness
#print axioms c7Line_budgetTotal_le_qMinusOne
#print axioms c7Line_naturalTotal_le_qMinusOne
#print axioms c7Ledger_compiles
#print axioms rootedFixture_compiles

end BasePoleC7WitnessClass

end AsymptoticSpine
