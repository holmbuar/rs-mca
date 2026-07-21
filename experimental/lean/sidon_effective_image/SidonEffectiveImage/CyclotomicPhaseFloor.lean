import Std

/-!
# Trace-linear cyclotomic phase-floor arithmetic

This stdlib-only module checks the exact finite arithmetic for the
`p = 3`, `r = 5` affine-basis Reed--Solomon trace-phase falsifier in
`experimental/notes/thresholds/sidon_effective_image_cyclotomic_phase_floor.md`.
It also checks the exhaustively replayed `p = 3`, `r = 2` regression constants.

The mathematical note proves the field construction, injectivity, trace-pairing
phase-code parametrization, cyclotomic coefficient identity, and general-family
asymptotics.  This module deliberately certifies the finite integer boundary:
source/image mass, effective target size, coherent block census, payment floor,
and the exact signed cancellation debt.  It imports no repository module and no
open-PR declaration.
-/

namespace SidonEffectiveImage.CyclotomicPhaseFloor

set_option maxRecDepth 8192
set_option maxHeartbeats 0

/-- Closed factorial used only to evaluate the finite certificate constants. -/
def factorial : Nat → Nat
  | 0 => 1
  | n + 1 => (n + 1) * factorial n

/-- Closed binomial evaluator; all certificate calls satisfy `k ≤ n`. -/
def binomial (n k : Nat) : Nat :=
  factorial n / (factorial k * factorial (n - k))

/-- Exhaustive regression parameters: `p=3`, `r=2`, `N=12`, `m=6`. -/
def regressionPhaseCodeSize : Nat := 3 ^ 10

def regressionSourceMass : Nat := binomial 12 6

def regressionHalfBalancedCount : Nat :=
  binomial 6 2 * binomial 4 2

def regressionAnchoredComplementCount : Nat :=
  binomial 5 1 * binomial 4 2

def regressionCoherentBlockCount : Nat :=
  regressionHalfBalancedCount * regressionAnchoredComplementCount

def regressionCyclotomicCoefficient : Nat := binomial 4 2

def regressionCoherentBlockMass : Nat :=
  regressionCoherentBlockCount * regressionCyclotomicCoefficient

/-- The verifier exhausts exactly `3^10=59049` trace-linear phase words. -/
theorem regression_phase_code_size_exact :
    regressionPhaseCodeSize = 59049 := by decide

/-- The verifier exhausts exactly `binom(12,6)=924` supports. -/
theorem regression_source_mass_exact :
    regressionSourceMass = 924 := by decide

/-- Exact split-balanced coherent character count in the regression. -/
theorem regression_coherent_block_count_exact :
    regressionCoherentBlockCount = 2700 := by decide

/-- Every regression block character has coefficient six. -/
theorem regression_cyclotomic_coefficient_exact :
    regressionCyclotomicCoefficient = 6 := by decide

/-- Exact coherent block sum in the exhaustive regression. -/
theorem regression_coherent_block_mass_exact :
    regressionCoherentBlockMass = 16200 := by decide

/-- Exact `p=3`, `r=5` source mass `M=L=binom(30,15)`. -/
def sourceMass : Nat := binomial 30 15

/-- Exact effective target size `A_eff=3^28`. -/
def effectiveTargetSize : Nat := 3 ^ 28

/-- Balanced phase words on the attained zero-target half. -/
def halfBalancedCount : Nat :=
  binomial 15 5 * binomial 10 5

/-- Balanced phase words on the complementary half with the base phase fixed to zero. -/
def anchoredComplementBalancedCount : Nat :=
  binomial 14 4 * binomial 10 5

/-- Characters in the coherent split-balanced cyclotomic block. -/
def coherentBlockCount : Nat :=
  halfBalancedCount * anchoredComplementBalancedCount

/-- Common fixed-weight cyclotomic coefficient `[z^15](1+z^3)^10`. -/
def cyclotomicCoefficient : Nat := binomial 10 5

/-- Signed block contribution at the attained zero target; every summand is positive. -/
def coherentBlockMass : Nat :=
  coherentBlockCount * cyclotomicCoefficient

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

/-- Exact coherent phase-block census. -/
theorem coherent_block_count_exact :
    coherentBlockCount = 190893214512 := by decide

/-- Exact common cyclotomic coefficient. -/
theorem cyclotomic_coefficient_exact :
    cyclotomicCoefficient = 252 := by decide

/-- Exact coherent phase-block mass. -/
theorem coherent_block_mass_exact :
    coherentBlockMass = 48105090057024 := by decide

/-- The coherent block exceeds twice the effective target by an exact positive gap. -/
theorem coherent_block_double_gap_exact :
    coherentBlockMass = 2 * effectiveTargetSize + 2351505147102 := by decide

/-- Criterion-4 finite falsifier: exact image compensation still leaves a factor greater than two. -/
theorem coherent_block_exceeds_double_effective_target :
    2 * effectiveTargetSize < coherentBlockMass := by decide

/--
Any nonnegative source-normalized block payment
`coherentBlockMass <= (kappa-1)*sourceMass` needs `kappa >= 310122`.
-/
theorem source_payment_kappa_floor (kappa : Nat)
    (hpay : coherentBlockMass ≤ (kappa - 1) * sourceMass) :
    310122 ≤ kappa := by
  rw [coherent_block_mass_exact, source_mass_exact] at hpay
  omega

/--
After the trivial coefficient and coherent block are removed, exact Fourier
inversion at the unique zero target forces this signed complementary debt.
-/
theorem signed_complement_debt_exact :
    (effectiveTargetSize : Int) - (sourceMass : Int) - (coherentBlockMass : Int)
      = -(25228452719583 : Int) := by decide

/-- Exact integer Fourier balance including the negative cross-histogram debt. -/
theorem exact_fourier_balance :
    (sourceMass : Int) + (coherentBlockMass : Int) - (25228452719583 : Int)
      = (effectiveTargetSize : Int) := by decide

/-- No nonnegative blockwise remainder can satisfy the exact target balance. -/
theorem no_nonnegative_blockwise_balance (remainder : Nat)
    (hbalance : sourceMass + coherentBlockMass + remainder = effectiveTargetSize) :
    False := by
  rw [source_mass_exact, coherent_block_mass_exact, effective_target_size_exact] at hbalance
  omega

#print axioms regression_coherent_block_mass_exact
#print axioms coherent_block_mass_exact
#print axioms coherent_block_double_gap_exact
#print axioms coherent_block_exceeds_double_effective_target
#print axioms source_payment_kappa_floor
#print axioms signed_complement_debt_exact
#print axioms exact_fourier_balance
#print axioms no_nonnegative_blockwise_balance

end SidonEffectiveImage.CyclotomicPhaseFloor
