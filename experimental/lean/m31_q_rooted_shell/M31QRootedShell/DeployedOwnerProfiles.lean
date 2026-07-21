import M31QRootedShell.SemanticNaturalScale

/-!
# Deployed Mersenne-31 line-local owner profiles

This module instantiates the natural-scale payment interface on two theorem-level
branches of the active Mersenne-31 list row.  It keeps the profile denominator
`q_prof ^ w` separate from the slope-sampling denominator `q_slope`.

The source-facing inputs are the active near-rational line cap and the primitive
one-pencil moving-root cap after common-GCD deletion.  The module does not claim
that these branches exhaust C1--C8 or that every residual shell satisfies the
open `3+7` inequality.
-/

namespace M31QRootedShell.SemanticOwner

/-- Active Mersenne-31 list-row constants. -/
def m31ListPrime : Nat := 2147483647
def m31ListDomainSize : Nat := 2097152
def m31ListAgreement : Nat := 1116023
def m31ListComplementSize : Nat := 981129
def m31ListPrefixDepth : Nat := 67447
def m31ListAverageCeil : Nat := 1993678

/-- The primitive one-pencil moving-root cap is exactly `floor(n / omega) = 2`. -/
theorem m31List_onePencilCap_eq_two :
    m31ListDomainSize / m31ListComplementSize = 2 := by
  native_decide

/--
Calibration of a natural profile scale to the active Mersenne-31 list row.
The enormous full support mass remains an explicit source-side field, while the
kernel consumes its already audited ceiling average.
-/
structure M31ListNaturalScaleCalibration (scale : NaturalProfileScale) : Prop where
  profileFieldCard_eq : scale.profileFieldCard = m31ListPrime
  prefixDepth_eq : scale.prefixDepth = m31ListPrefixDepth
  averageCeil_eq : scale.averageCeil = m31ListAverageCeil
  loss_eq : scale.loss = 1

/-- The calibrated natural denominator is literally `q_prof ^ w`. -/
theorem M31ListNaturalScaleCalibration.denominator_eq
    {scale : NaturalProfileScale}
    (h : M31ListNaturalScaleCalibration scale) :
    scale.denominator = m31ListPrime ^ m31ListPrefixDepth := by
  unfold NaturalProfileScale.denominator
  rw [h.profileFieldCard_eq, h.prefixDepth_eq]

/-- The loss-one Mersenne-31 natural numerator is `1 + 1,993,678`. -/
theorem M31ListNaturalScaleCalibration.naturalNumerator_eq
    {scale : NaturalProfileScale}
    (h : M31ListNaturalScaleCalibration scale) :
    scale.naturalNumerator = 1993679 := by
  unfold NaturalProfileScale.naturalNumerator
  rw [h.loss_eq, h.averageCeil_eq]
  native_decide

/-- A line-local certificate for the paid near-rational finite-slope branch. -/
structure M31NearRationalCertificate (Slope : Type) where
  slopes : List Slope
  slopes_nodup : slopes.Nodup
  slopes_length_le : slopes.length ≤ 1

/-- A line-local certificate for a primitive projective locator pencil. -/
structure M31PrimitiveOnePencilCertificate (Slope : Type) where
  slopes : List Slope
  slopes_nodup : slopes.Nodup
  slopes_length_le :
    slopes.length ≤ m31ListDomainSize / m31ListComplementSize

/-- Paid line-local near-rational profile: exact numerator one, `q_slope = p`. -/
def m31NearRationalProfile
    {Slope : Type} (scale : NaturalProfileScale)
    (hscale : M31ListNaturalScaleCalibration scale)
    (cert : M31NearRationalCertificate Slope) : PaidSlopeProfile Slope where
  naturalScale := scale
  exactBudget := {
    numerator := 1
    slopeDenominator := m31ListPrime
    slopeDenominator_pos := by native_decide
    numerator_le_denominator := by native_decide
  }
  slopes := cert.slopes
  slopes_nodup := cert.slopes_nodup
  slopeCount_le_exact := cert.slopes_length_le
  exact_le_natural := by
    rw [hscale.naturalNumerator_eq]
    native_decide

/--
Paid primitive C8 one-pencil profile: exact numerator two from
`floor(n / omega)`, with `q_slope = p`.
-/
def m31PrimitiveOnePencilProfile
    {Slope : Type} (scale : NaturalProfileScale)
    (hscale : M31ListNaturalScaleCalibration scale)
    (cert : M31PrimitiveOnePencilCertificate Slope) : PaidSlopeProfile Slope where
  naturalScale := scale
  exactBudget := {
    numerator := 2
    slopeDenominator := m31ListPrime
    slopeDenominator_pos := by native_decide
    numerator_le_denominator := by native_decide
  }
  slopes := cert.slopes
  slopes_nodup := cert.slopes_nodup
  slopeCount_le_exact := by
    simpa [m31List_onePencilCap_eq_two] using cert.slopes_length_le
  exact_le_natural := by
    rw [hscale.naturalNumerator_eq]
    native_decide

/-- The primitive one-pencil profile prints the two distinct denominators. -/
theorem m31PrimitiveOnePencilProfile_denominators
    {Slope : Type} (scale : NaturalProfileScale)
    (hscale : M31ListNaturalScaleCalibration scale)
    (cert : M31PrimitiveOnePencilCertificate Slope) :
    (m31PrimitiveOnePencilProfile scale hscale cert).naturalScale.denominator =
        m31ListPrime ^ m31ListPrefixDepth ∧
      (m31PrimitiveOnePencilProfile scale hscale cert).exactBudget.slopeDenominator =
        m31ListPrime := by
  constructor
  · simpa [m31PrimitiveOnePencilProfile] using hscale.denominator_eq
  · rfl

/-- Exact paid-profile chain for the deployed primitive one-pencil branch. -/
theorem m31PrimitiveOnePencilProfile_budget
    {Slope : Type} (scale : NaturalProfileScale)
    (hscale : M31ListNaturalScaleCalibration scale)
    (cert : M31PrimitiveOnePencilCertificate Slope) :
    (m31PrimitiveOnePencilProfile scale hscale cert).slopes.length ≤ 2 ∧
      (m31PrimitiveOnePencilProfile scale hscale cert).exactBudget.numerator = 2 ∧
      (m31PrimitiveOnePencilProfile scale hscale cert).exactBudget.numerator ≤
        (m31PrimitiveOnePencilProfile scale hscale cert).exactBudget.slopeDenominator ∧
      (m31PrimitiveOnePencilProfile scale hscale cert).exactBudget.numerator ≤
        (m31PrimitiveOnePencilProfile scale hscale cert).naturalScale.naturalNumerator := by
  exact ⟨(m31PrimitiveOnePencilProfile scale hscale cert).slopeCount_le_exact,
    rfl,
    (m31PrimitiveOnePencilProfile scale hscale cert).exactBudget.numerator_le_denominator,
    (m31PrimitiveOnePencilProfile scale hscale cert).exact_le_natural⟩

#print axioms m31List_onePencilCap_eq_two
#print axioms M31ListNaturalScaleCalibration.denominator_eq
#print axioms M31ListNaturalScaleCalibration.naturalNumerator_eq
#print axioms m31PrimitiveOnePencilProfile_denominators
#print axioms m31PrimitiveOnePencilProfile_budget

end M31QRootedShell.SemanticOwner
