import Std

/-!
# Trace-linear cyclotomic phase-floor arithmetic

This stdlib-only module checks the exact finite arithmetic for the
`p = 3`, `r = 5` affine-basis Reed--Solomon trace-phase falsifier in
`experimental/notes/thresholds/sidon_effective_image_cyclotomic_phase_floor.md`.
It also checks the exhaustively replayed `p = 3`, `r = 2` regression constants.

The mathematical note proves the field construction, domain distinctness,
injectivity, trace-pairing phase-code parametrization, cyclotomic coefficient
identity, complete balanced-histogram formula, and general-family asymptotics.
This module deliberately certifies the finite integer boundary. It imports no
repository module and no open-PR declaration.
-/

namespace SidonEffectiveImage.CyclotomicPhaseFloor

set_option autoImplicit false
set_option maxRecDepth 8192
set_option maxHeartbeats 0

/-- Exhaustive regression parameters: `p=3`, `r=2`, `N=12`, `m=6`. -/
def regressionPhaseCodeSize : Nat := 3 ^ 10

def regressionSourceMass : Nat := Nat.choose 12 6

def regressionHalfBalancedCount : Nat :=
  Nat.choose 6 2 * Nat.choose 4 2

def regressionAnchoredComplementCount : Nat :=
  Nat.choose 5 1 * Nat.choose 4 2

def regressionSplitBalancedBlockCount : Nat :=
  regressionHalfBalancedCount * regressionAnchoredComplementCount

def regressionCyclotomicCoefficient : Nat := Nat.choose 4 2

def regressionSplitBalancedBlockMass : Nat :=
  regressionSplitBalancedBlockCount * regressionCyclotomicCoefficient

/-- The verifier exhausts exactly `3^10=59049` trace-linear phase words. -/
theorem regression_phase_code_size_exact :
    regressionPhaseCodeSize = 59049 := by decide

/-- The verifier exhausts exactly `binom(12,6)=924` supports. -/
theorem regression_source_mass_exact :
    regressionSourceMass = 924 := by decide

/-- Exact split-balanced coherent character count in the regression. -/
theorem regression_split_balanced_block_count_exact :
    regressionSplitBalancedBlockCount = 2700 := by decide

/-- Every globally balanced regression character has coefficient six. -/
theorem regression_cyclotomic_coefficient_exact :
    regressionCyclotomicCoefficient = 6 := by decide

/-- Exact split-balanced coherent sum in the exhaustive regression. -/
theorem regression_split_balanced_block_mass_exact :
    regressionSplitBalancedBlockMass = 16200 := by decide

/-- Exact `p=3`, `r=5` source mass `M=L=binom(30,15)`. -/
def sourceMass : Nat := Nat.choose 30 15

/-- Exact effective target size `A_eff=3^28`. -/
def effectiveTargetSize : Nat := 3 ^ 28

/-- Balanced phase words on the attained zero-target half. -/
def halfBalancedCount : Nat :=
  Nat.choose 15 5 * Nat.choose 10 5

/-- Balanced phase words on the complementary half with the base phase fixed to zero. -/
def anchoredComplementBalancedCount : Nat :=
  Nat.choose 14 4 * Nat.choose 10 5

/-- Characters in the certified split-balanced cyclotomic subblock. -/
def splitBalancedBlockCount : Nat :=
  halfBalancedCount * anchoredComplementBalancedCount

/-- Common fixed-weight cyclotomic coefficient `[z^15](1+z^3)^10`. -/
def cyclotomicCoefficient : Nat := Nat.choose 10 5

/-- Signed split-balanced subblock contribution; every summand is positive. -/
def splitBalancedBlockMass : Nat :=
  splitBalancedBlockCount * cyclotomicCoefficient

/-- Three phase counts on the attained support. -/
abbrev PhaseCountTriple := Nat × Nat × Nat

/--
All count triples for the attained support in the `p=3,r=5` globally balanced
histogram. The verifier independently checks this list against the congruence
and range conditions.
-/
def balancedHistogramTriples : List PhaseCountTriple :=
  [ (0, 6, 9), (0, 9, 6),
    (1, 4, 10), (1, 7, 7), (1, 10, 4),
    (2, 5, 8), (2, 8, 5),
    (3, 3, 9), (3, 6, 6), (3, 9, 3),
    (4, 1, 10), (4, 4, 7), (4, 7, 4), (4, 10, 1),
    (5, 2, 8), (5, 5, 5), (5, 8, 2),
    (6, 0, 9), (6, 3, 6), (6, 6, 3), (6, 9, 0),
    (7, 1, 7), (7, 4, 4), (7, 7, 1),
    (8, 2, 5), (8, 5, 2),
    (9, 0, 6), (9, 3, 3), (9, 6, 0) ]

/-- Three-part multinomial coefficient. -/
def multinomial3 (n a b c : Nat) : Nat :=
  Nat.factorial n /
    (Nat.factorial a * Nat.factorial b * Nat.factorial c)

/--
Number of characters for one attained-support count triple. Globally there are
ten copies of each phase; the distinguished base coordinate already consumes
one zero on the complement.
-/
def balancedHistogramTerm : PhaseCountTriple → Nat
  | (a0, a1, a2) =>
      multinomial3 15 a0 a1 a2 *
        (Nat.factorial 14 /
          (Nat.factorial (9 - a0) *
            Nat.factorial (10 - a1) * Nat.factorial (10 - a2)))

/-- Exact complete globally balanced histogram count at `p=3,r=5`. -/
def balancedHistogramCount : Nat :=
  (balancedHistogramTriples.map balancedHistogramTerm).sum

/-- Exact complete globally balanced histogram mass. -/
def balancedHistogramMass : Nat :=
  balancedHistogramCount * cyclotomicCoefficient

/-- Exact source and realized-image size. -/
theorem source_mass_exact : sourceMass = 155117520 := by decide

/-- Exact effective target size. -/
theorem effective_target_size_exact :
    effectiveTargetSize = 22876792454961 := by decide

/-- Exact first-half balanced census. -/
theorem half_balanced_count_exact :
    halfBalancedCount = 756756 := by decide

/-- Exact anchored complementary-half balanced census. -/
theorem anchored_complement_balanced_count_exact :
    anchoredComplementBalancedCount = 252252 := by decide

/-- Exact certified split-balanced phase-subblock census. -/
theorem split_balanced_block_count_exact :
    splitBalancedBlockCount = 190893214512 := by decide

/-- Exact common cyclotomic coefficient. -/
theorem cyclotomic_coefficient_exact :
    cyclotomicCoefficient = 252 := by decide

/-- Exact certified split-balanced phase-subblock mass. -/
theorem split_balanced_block_mass_exact :
    splitBalancedBlockMass = 48105090057024 := by decide

/-- The split-balanced subblock exceeds twice the effective target by this gap. -/
theorem split_balanced_double_gap_exact :
    splitBalancedBlockMass = 2 * effectiveTargetSize + 2351505147102 := by decide

/-- Exact complete balanced-histogram character count. -/
theorem balanced_histogram_count_exact :
    balancedHistogramCount = 616779425262 := by decide

/-- Exact complete balanced-histogram signed mass. -/
theorem balanced_histogram_mass_exact :
    balancedHistogramMass = 155428415166024 := by decide

/-- The complete balanced histogram exceeds six effective targets by this gap. -/
theorem balanced_histogram_six_gap_exact :
    balancedHistogramMass = 6 * effectiveTargetSize + 18167660436258 := by decide

/-- Criterion-4 finite subblock floor after exact image compensation. -/
theorem split_balanced_block_exceeds_double_effective_target :
    2 * effectiveTargetSize < splitBalancedBlockMass := by decide

/-- Criterion-4 finite histogram floor after exact image compensation. -/
theorem balanced_histogram_exceeds_six_effective_targets :
    6 * effectiveTargetSize < balancedHistogramMass := by decide

/--
Any nonnegative source-normalized payment for the certified split subblock,
`splitBalancedBlockMass <= (kappa-1)*sourceMass`, needs `kappa >= 310122`.
-/
theorem split_source_payment_kappa_floor (kappa : Nat)
    (hpay : splitBalancedBlockMass ≤ (kappa - 1) * sourceMass) :
    310122 ≤ kappa := by
  rw [split_balanced_block_mass_exact, source_mass_exact] at hpay
  omega

/--
Any nonnegative source-normalized payment for the complete balanced histogram
needs `kappa >= 1002006`.
-/
theorem histogram_source_payment_kappa_floor (kappa : Nat)
    (hpay : balancedHistogramMass ≤ (kappa - 1) * sourceMass) :
    1002006 ≤ kappa := by
  rw [balanced_histogram_mass_exact, source_mass_exact] at hpay
  omega

/-- Exact signed sum outside only the certified split-balanced subblock. -/
theorem outside_split_subblock_signed_sum_exact :
    (effectiveTargetSize : Int) - (sourceMass : Int) -
        (splitBalancedBlockMass : Int)
      = -(25228452719583 : Int) := by decide

/-- Exact signed debt carried by all other phase histograms. -/
theorem other_histogram_signed_debt_exact :
    (effectiveTargetSize : Int) - (sourceMass : Int) -
        (balancedHistogramMass : Int)
      = -(132551777828583 : Int) := by decide

/-- Exact Fourier balance after isolating the complete balanced histogram. -/
theorem exact_histogram_fourier_balance :
    (sourceMass : Int) + (balancedHistogramMass : Int) -
        (132551777828583 : Int)
      = (effectiveTargetSize : Int) := by decide

/-- No nonnegative other-histogram remainder can satisfy the exact balance. -/
theorem no_nonnegative_histogram_balance (remainder : Nat)
    (hbalance : sourceMass + balancedHistogramMass + remainder = effectiveTargetSize) :
    False := by
  rw [source_mass_exact, balanced_histogram_mass_exact,
    effective_target_size_exact] at hbalance
  omega

#print axioms regression_phase_code_size_exact
#print axioms regression_source_mass_exact
#print axioms regression_split_balanced_block_count_exact
#print axioms regression_cyclotomic_coefficient_exact
#print axioms regression_split_balanced_block_mass_exact
#print axioms source_mass_exact
#print axioms effective_target_size_exact
#print axioms half_balanced_count_exact
#print axioms anchored_complement_balanced_count_exact
#print axioms split_balanced_block_count_exact
#print axioms cyclotomic_coefficient_exact
#print axioms split_balanced_block_mass_exact
#print axioms split_balanced_double_gap_exact
#print axioms balanced_histogram_count_exact
#print axioms balanced_histogram_mass_exact
#print axioms balanced_histogram_six_gap_exact
#print axioms split_balanced_block_exceeds_double_effective_target
#print axioms balanced_histogram_exceeds_six_effective_targets
#print axioms split_source_payment_kappa_floor
#print axioms histogram_source_payment_kappa_floor
#print axioms outside_split_subblock_signed_sum_exact
#print axioms other_histogram_signed_debt_exact
#print axioms exact_histogram_fourier_balance
#print axioms no_nonnegative_histogram_balance

end SidonEffectiveImage.CyclotomicPhaseFloor
