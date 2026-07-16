import GrandeFinale.DirectionDistanceAllPairs

/-!
# Fixed-slope kernel-Johnson multiplicity

This module records the remaining fixed-slope Johnson statement as an explicitly
labelled target and proves the arithmetic specialization used by the canonical
A6 parameters.

For a fixed slope, two error words differ by a word in the kernel.  A kernel
distance lower bound therefore limits the intersection of their agreement
supports.  The target below packages the resulting Johnson double count; its
combinatorial proof is intentionally not asserted here.
-/

open scoped BigOperators Classical
noncomputable section

namespace GrandeFinale
namespace FixedSlopeKernelJohnsonMultiplicity

open DirectionDistanceAllPairs

set_option autoImplicit false

variable {D F W : Type*}
variable [Fintype D] [DecidableEq D]
variable [Field F] [DecidableEq F]
variable [AddCommGroup W] [Module F W]

/-- The pairs in P whose first coordinate is the prescribed slope. -/
def fixedSlopeFiber
    (P : Finset (SlopeErrorPair D F)) (gamma : F) :
    Finset (SlopeErrorPair D F) :=
  P.filter fun p => p.1 = gamma

/-- The denominator in the fixed-slope kernel-Johnson double count. -/
def kernelJohnsonDenominator (N t kappa : Nat) : Nat :=
  (N - t) ^ 2 - N * (kappa - 1)

/-- The numerator in the fixed-slope kernel-Johnson double count. -/
def kernelJohnsonNumerator (N t kappa : Nat) : Nat :=
  N * ((N - t) - (kappa - 1))

/-- Positivity of the fixed-slope kernel-Johnson denominator. -/
def KernelJohnsonPositive (N t kappa : Nat) : Prop :=
  N * (kappa - 1) < (N - t) ^ 2

/-- The multiplicative and quotient forms of the Johnson conclusion. -/
def FixedSlopeKernelJohnsonConclusion
    (P : Finset (SlopeErrorPair D F)) (gamma : F)
    (t kappa : Nat) : Prop :=
  let N := Fintype.card D
  let denominator := kernelJohnsonDenominator N t kappa
  let numerator := kernelJohnsonNumerator N t kappa
  (fixedSlopeFiber P gamma).card * denominator ≤ numerator ∧
    (fixedSlopeFiber P gamma).card ≤ numerator / denominator

/--
**UNPROVED STATEMENT TARGET.**  The fixed-slope kernel-Johnson multiplicity
lemma.  The intended proof applies the Johnson support-intersection double
count after observing that two errors with the same slope differ by a kernel
word.  This definition only records the exact proposition to be proved.
-/
def fixedSlopeKernelJohnsonMultiplicityTarget
    (H : (D → F) →ₗ[F] W) (y₀ y₁ : W)
    (P : Finset (SlopeErrorPair D F)) (gamma : F)
    (t kappa : Nat) : Prop :=
  let N := Fintype.card D
  BasicPairHypotheses H y₀ y₁ P t →
    KernelDistanceAtLeast H (N - kappa + 1) →
    0 < kappa →
    kappa ≤ N →
    t ≤ N →
    KernelJohnsonPositive N t kappa →
    FixedSlopeKernelJohnsonConclusion P gamma t kappa

/-! ## Canonical A6 arithmetic -/

def canonicalA6Length (r : Nat) : Nat := 500 * r

def canonicalA6KernelDimension (r : Nat) : Nat := 225 * r

def canonicalA6Radius (r : Nat) : Nat := 150 * r

def canonicalA6Agreement (r : Nat) : Nat :=
  canonicalA6Length r - canonicalA6Radius r

def canonicalA6Denominator (r : Nat) : Nat :=
  kernelJohnsonDenominator
    (canonicalA6Length r) (canonicalA6Radius r)
    (canonicalA6KernelDimension r)

def canonicalA6Numerator (r : Nat) : Nat :=
  kernelJohnsonNumerator
    (canonicalA6Length r) (canonicalA6Radius r)
    (canonicalA6KernelDimension r)

def canonicalA6KernelCap (r : Nat) : Nat :=
  canonicalA6Numerator r / canonicalA6Denominator r

theorem canonicalA6_agreement (r : Nat) :
    canonicalA6Agreement r = 350 * r := by
  simp [canonicalA6Agreement, canonicalA6Length, canonicalA6Radius]
  omega

theorem canonicalA6_denominator (r : Nat) (hr : 1 ≤ r) :
    canonicalA6Denominator r = 500 * r * (20 * r + 1) := by
  rw [canonicalA6Denominator, kernelJohnsonDenominator]
  change (500 * r - 150 * r) ^ 2 - 500 * r * (225 * r - 1) = _
  have hagree : 500 * r - 150 * r = 350 * r := by omega
  rw [hagree]
  have hsum : (225 * r - 1) + (20 * r + 1) = 245 * r := by omega
  have hid :
      (350 * r) ^ 2 =
        500 * r * (225 * r - 1) + 500 * r * (20 * r + 1) := by
    calc
      (350 * r) ^ 2 = 500 * r * (245 * r) := by ring
      _ = 500 * r * ((225 * r - 1) + (20 * r + 1)) := by rw [hsum]
      _ = 500 * r * (225 * r - 1) + 500 * r * (20 * r + 1) := by ring
  omega

theorem canonicalA6_numerator (r : Nat) (hr : 1 ≤ r) :
    canonicalA6Numerator r = 500 * r * (125 * r + 1) := by
  rw [canonicalA6Numerator, kernelJohnsonNumerator]
  change 500 * r * ((500 * r - 150 * r) - (225 * r - 1)) = _
  have hagree : 500 * r - 150 * r = 350 * r := by omega
  rw [hagree]
  have hinner : 350 * r - (225 * r - 1) = 125 * r + 1 := by omega
  rw [hinner]

theorem canonicalA6_denominator_pos (r : Nat) (hr : 1 ≤ r) :
    0 < canonicalA6Denominator r := by
  rw [canonicalA6_denominator r hr]
  positivity

theorem canonicalA6_kernel_cap (r : Nat) (hr : 1 ≤ r) :
    canonicalA6KernelCap r = 6 := by
  rw [canonicalA6KernelCap, canonicalA6_numerator r hr,
    canonicalA6_denominator r hr]
  have hden : 0 < 500 * r * (20 * r + 1) := by positivity
  have hlower :
      6 * (500 * r * (20 * r + 1)) ≤ 500 * r * (125 * r + 1) := by
    nlinarith
  have hupper :
      500 * r * (125 * r + 1) < 7 * (500 * r * (20 * r + 1)) := by
    nlinarith
  apply Nat.le_antisymm
  · have hlt :
        (500 * r * (125 * r + 1)) / (500 * r * (20 * r + 1)) < 7 :=
      (Nat.div_lt_iff_lt_mul hden).2 hupper
    omega
  · exact (Nat.le_div_iff_mul_le hden).2 hlower

theorem canonicalA6_multiplicity_le_six
    (r multiplicity : Nat) (hr : 1 ≤ r)
    (hcount : multiplicity * canonicalA6Denominator r ≤
      canonicalA6Numerator r) :
    multiplicity ≤ 6 := by
  have hden := canonicalA6_denominator_pos r hr
  have hdiv : multiplicity ≤ canonicalA6KernelCap r := by
    exact (Nat.le_div_iff_mul_le hden).2 hcount
  rwa [canonicalA6_kernel_cap r hr] at hdiv

/-! ## Composition with the fixed-direction slope bound -/

def fixedDirectionSlopeBound (D : Nat) : Nat :=
  1165 + 3744 * D ^ 6

def composedA6Bound (D : Nat) : Nat :=
  6 * fixedDirectionSlopeBound D

theorem composedA6Bound_eq (D : Nat) :
    composedA6Bound D = 6990 + 22464 * D ^ 6 := by
  simp [composedA6Bound, fixedDirectionSlopeBound]
  ring

theorem canonicalA6_compose_fixed_direction_bound
    (D slopeCount pairCount : Nat)
    (hslopes : slopeCount ≤ fixedDirectionSlopeBound D)
    (hpairs : pairCount ≤ 6 * slopeCount) :
    pairCount ≤ 6990 + 22464 * D ^ 6 := by
  calc
    pairCount ≤ 6 * slopeCount := hpairs
    _ ≤ 6 * fixedDirectionSlopeBound D := Nat.mul_le_mul_left 6 hslopes
    _ = composedA6Bound D := rfl
    _ = 6990 + 22464 * D ^ 6 := composedA6Bound_eq D

end FixedSlopeKernelJohnsonMultiplicity
end GrandeFinale
