import M31QuotientBandMixing.Witnesses

/-!
# M31 quotient-band mixing packet

The public module re-exports the finite witness theorems used by
`m31_quotient_band_swap_census_t16_mixing.md`.
-/

namespace M31QuotientBandMixing

open Witnesses

theorem packet_floor_and_window :
    (familyClassSelections.filter fun cs => classDeficiency cs == 192).length = 1225 ∧
    (4 * H192) / Q32 = 0 ∧
    1 + 1225 * 447 + 14456476 = 15004052 ∧
    15004052 ≤ 16777215 := by
  exact ⟨rooted_shell_census.2.2.1, shell_192_floor_zero,
    intercept_1225_compiler_arithmetic.1,
    intercept_1225_compiler_arithmetic.2.1⟩

theorem packet_off_lattice_witness :
    supportValid mixingAnchor = true ∧
    supportValid mixingNeighbor = true ∧
    deficiency mixingAnchor mixingNeighbor = 96 ∧
    locatorPrefix 47 mixingAnchor = locatorPrefix 47 mixingNeighbor ∧
    96 % 64 = 32 := by
  exact ⟨mixing_supports_exact.2.2.1,
    mixing_supports_exact.2.2.2.1,
    mixing_supports_exact.2.2.2.2,
    mixing_prefix_exact.1,
    mixing_is_off_lattice.2⟩

#print axioms packet_floor_and_window
#print axioms packet_off_lattice_witness

end M31QuotientBandMixing
