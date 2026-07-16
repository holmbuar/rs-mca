import GrandeFinale.C0PeriodicF28DerivedOwner

/-!
# Periodic `q = 64`, `f = 28` target-indexed compiler

This module removes the separate deduplication and representative-selection
boundary from the derived residual owner.  Its input records the deployed
two-block and projective data directly on a finite target family.  Finite
choice selects one target for each distinct residual support, while the
designated target is always selected on the reference support.  Duplicate
targets therefore need no coherence hypothesis for the owner bound.

The resulting deduplicated family feeds the existing residual-pencil owner,
the 64 supplied scalar cells, and the exact PR #819 first-match wrapper.  The
deployed classification, per-target algebraic certificates, fixed-cell Hahn
cap, and first-match cover remain explicit inputs.  No complete `c = 0`
parent bound is claimed.
-/

open Polynomial

namespace GrandeFinale.C0PeriodicF28TargetCompiler

open C0PeriodicF28DerivedOwner
open C0PeriodicF29ResidualOwner

/-- Deployed two-block data indexed by target objects before equal residual
supports are deduplicated.  Requiring the designated reference only when the
target is nonempty preserves the empty-family branch. -/
structure TargetTwoBlockCertificate
    (α F : Type*) [DecidableEq α] [Field F] [DecidableEq F] where
  target : Finset α
  ambient : Finset F
  residualSupport : α → Finset F
  referenceTarget : α
  lowerBlock : α → F[X]
  upperBlock : α → F[X]
  quotient : α → F[X]
  rayScale : α → F
  reference_mem_of_nonempty : target.Nonempty → referenceTarget ∈ target
  ambient_card : ambient.card = 2097152
  ambient_ne_zero : ∀ z ∈ ambient, z ≠ 0
  residual_subset : ∀ x ∈ target, residualSupport x ⊆ ambient
  residual_card : ∀ x ∈ target, (residualSupport x).card = 63601
  decomposition : ∀ x ∈ target,
    supportLocator (residualSupport x) =
      deployedResidual (lowerBlock x) (upperBlock x)
  lower_degree_lt : ∀ x ∈ target, (lowerBlock x).natDegree < 32768
  upper_degree : ∀ x ∈ target, (upperBlock x).natDegree = 30833
  quotient_constant_ne_zero : ∀ x ∈ target, (quotient x).coeff 0 ≠ 0
  rayScale_ne_zero : ∀ x ∈ target, rayScale x ≠ 0
  projective : ∀ x ∈ target,
    residualSupport x ≠ residualSupport referenceTarget →
      DeployedProjective
        (lowerBlock x) (upperBlock x) (quotient x)
        (lowerBlock referenceTarget) (upperBlock referenceTarget)
        (quotient referenceTarget) (rayScale x)

/-- Distinct residual supports realized by the finite target family. -/
def TargetTwoBlockCertificate.residuals
    {α F : Type*} [DecidableEq α] [Field F] [DecidableEq F]
    (cert : TargetTwoBlockCertificate α F) : Finset (Finset F) :=
  cert.target.image cert.residualSupport

/-- An arbitrary target realizing a residual support, with the designated
reference as a harmless default outside the realized family. -/
noncomputable def TargetTwoBlockCertificate.representative
    {α F : Type*} [DecidableEq α] [Field F] [DecidableEq F]
    (cert : TargetTwoBlockCertificate α F) (R : Finset F) : α :=
  if hR : R ∈ cert.residuals then
    Classical.choose (Finset.mem_image.mp hR)
  else cert.referenceTarget

theorem TargetTwoBlockCertificate.representative_mem
    {α F : Type*} [DecidableEq α] [Field F] [DecidableEq F]
    (cert : TargetTwoBlockCertificate α F)
    {R : Finset F} (hR : R ∈ cert.residuals) :
    cert.representative R ∈ cert.target := by
  rw [TargetTwoBlockCertificate.representative, dif_pos hR]
  exact (Classical.choose_spec (Finset.mem_image.mp hR)).1

theorem TargetTwoBlockCertificate.representative_support
    {α F : Type*} [DecidableEq α] [Field F] [DecidableEq F]
    (cert : TargetTwoBlockCertificate α F)
    {R : Finset F} (hR : R ∈ cert.residuals) :
    cert.residualSupport (cert.representative R) = R := by
  rw [TargetTwoBlockCertificate.representative, dif_pos hR]
  exact (Classical.choose_spec (Finset.mem_image.mp hR)).2

/-- Select the fixed reference target on its support and an arbitrary realizing
target on every other support.  This removes any need for coherence axioms
between duplicate target objects. -/
noncomputable def TargetTwoBlockCertificate.selectedTarget
    {α F : Type*} [DecidableEq α] [Field F] [DecidableEq F]
    (cert : TargetTwoBlockCertificate α F) (R : Finset F) : α :=
  if R = cert.residualSupport cert.referenceTarget then
    cert.referenceTarget
  else cert.representative R

theorem TargetTwoBlockCertificate.target_nonempty_of_residual_mem
    {α F : Type*} [DecidableEq α] [Field F] [DecidableEq F]
    (cert : TargetTwoBlockCertificate α F)
    {R : Finset F} (hR : R ∈ cert.residuals) : cert.target.Nonempty := by
  rcases Finset.mem_image.mp hR with ⟨x, hx, _⟩
  exact ⟨x, hx⟩

theorem TargetTwoBlockCertificate.selectedTarget_mem
    {α F : Type*} [DecidableEq α] [Field F] [DecidableEq F]
    (cert : TargetTwoBlockCertificate α F)
    {R : Finset F} (hR : R ∈ cert.residuals) :
    cert.selectedTarget R ∈ cert.target := by
  by_cases href : R = cert.residualSupport cert.referenceTarget
  · rw [TargetTwoBlockCertificate.selectedTarget, if_pos href]
    exact cert.reference_mem_of_nonempty
      (cert.target_nonempty_of_residual_mem hR)
  · rw [TargetTwoBlockCertificate.selectedTarget, if_neg href]
    exact cert.representative_mem hR

theorem TargetTwoBlockCertificate.selectedTarget_support
    {α F : Type*} [DecidableEq α] [Field F] [DecidableEq F]
    (cert : TargetTwoBlockCertificate α F)
    {R : Finset F} (hR : R ∈ cert.residuals) :
    cert.residualSupport (cert.selectedTarget R) = R := by
  by_cases href : R = cert.residualSupport cert.referenceTarget
  · rw [TargetTwoBlockCertificate.selectedTarget, if_pos href, href]
  · rw [TargetTwoBlockCertificate.selectedTarget, if_neg href]
    exact cert.representative_support hR

theorem TargetTwoBlockCertificate.reference_mem_of_residual_nonempty
    {α F : Type*} [DecidableEq α] [Field F] [DecidableEq F]
    (cert : TargetTwoBlockCertificate α F)
    (hne : cert.residuals.Nonempty) :
    cert.residualSupport cert.referenceTarget ∈ cert.residuals := by
  rcases hne with ⟨R, hR⟩
  exact Finset.mem_image.mpr
    ⟨cert.referenceTarget,
      cert.reference_mem_of_nonempty
        (cert.target_nonempty_of_residual_mem hR), rfl⟩

/-- Finite choice deduplicates the target-indexed residual supports and feeds
the existing derived owner. -/
noncomputable def TargetTwoBlockCertificate.toTwoBlockFamilyCertificate
    {α F : Type*} [DecidableEq α] [Field F] [DecidableEq F]
    (cert : TargetTwoBlockCertificate α F) : TwoBlockFamilyCertificate F where
  ambient := cert.ambient
  residuals := cert.residuals
  reference := cert.residualSupport cert.referenceTarget
  lowerBlock := fun R ↦ cert.lowerBlock (cert.selectedTarget R)
  upperBlock := fun R ↦ cert.upperBlock (cert.selectedTarget R)
  quotient := fun R ↦ cert.quotient (cert.selectedTarget R)
  rayScale := fun R ↦ cert.rayScale (cert.selectedTarget R)
  ambient_card := cert.ambient_card
  ambient_ne_zero := cert.ambient_ne_zero
  residual_subset := by
    intro R hR
    have hx := cert.selectedTarget_mem hR
    simpa only [cert.selectedTarget_support hR] using
      cert.residual_subset (cert.selectedTarget R) hx
  residual_card := by
    intro R hR
    have hx := cert.selectedTarget_mem hR
    simpa only [cert.selectedTarget_support hR] using
      cert.residual_card (cert.selectedTarget R) hx
  decomposition := by
    intro R hR
    have hx := cert.selectedTarget_mem hR
    simpa only [cert.selectedTarget_support hR] using
      cert.decomposition (cert.selectedTarget R) hx
  lower_degree_lt := by
    intro R hR
    exact cert.lower_degree_lt (cert.selectedTarget R)
      (cert.selectedTarget_mem hR)
  upper_degree := by
    intro R hR
    exact cert.upper_degree (cert.selectedTarget R)
      (cert.selectedTarget_mem hR)
  quotient_constant_ne_zero := by
    intro R hR
    exact cert.quotient_constant_ne_zero (cert.selectedTarget R)
      (cert.selectedTarget_mem hR)
  rayScale_ne_zero := by
    intro R hR
    exact cert.rayScale_ne_zero (cert.selectedTarget R)
      (cert.selectedTarget_mem hR)
  reference_mem_of_two := by
    intro htwo
    apply cert.reference_mem_of_residual_nonempty
    exact Finset.card_pos.mp (by omega)
  projective := by
    intro R hR hRref
    have hx := cert.selectedTarget_mem hR
    have hsupp := cert.selectedTarget_support hR
    have hne : cert.residualSupport (cert.selectedTarget R) ≠
        cert.residualSupport cert.referenceTarget := by
      rw [hsupp]
      exact hRref
    have hproj := cert.projective (cert.selectedTarget R) hx hne
    simpa [TargetTwoBlockCertificate.selectedTarget] using hproj

theorem TargetTwoBlockCertificate.distinct_residuals_card_le
    {α F : Type*} [DecidableEq α] [Field F] [DecidableEq F]
    (cert : TargetTwoBlockCertificate α F) : cert.residuals.card ≤ 63 :=
  cert.toTwoBlockFamilyCertificate.residuals_card_le

/-- The same target-indexed input feeds the already-proved 64 scalar-cell
wrapper; membership in the deduplicated residual image is automatic. -/
noncomputable def TargetTwoBlockCertificate.toTwoBlockProjectiveRayCertificate
    {α F : Type*} [DecidableEq α] [Field F] [DecidableEq F]
    (cert : TargetTwoBlockCertificate α F)
    (scalarClass : α → Fin 64)
    (fixedResidualScalarCap : ∀ R ∈ cert.residuals, ∀ s : Fin 64,
      (cert.target.filter fun x ↦
        cert.residualSupport x = R ∧ scalarClass x = s).card ≤ 20826085) :
    TwoBlockProjectiveRayCertificate α F where
  target := cert.target
  owner := cert.toTwoBlockFamilyCertificate
  residualSupport := cert.residualSupport
  scalarClass := scalarClass
  residual_member := by
    intro x hx
    exact Finset.mem_image.mpr ⟨x, hx, rfl⟩
  fixedResidualScalarCap := fixedResidualScalarCap

/-- Exact deployed q64, `f = 28` target cap directly from target-indexed
two-block certificates and the supplied fixed cells. -/
theorem TargetTwoBlockCertificate.target_card_le
    {α F : Type*} [DecidableEq α] [Field F] [DecidableEq F]
    (cert : TargetTwoBlockCertificate α F)
    (scalarClass : α → Fin 64)
    (fixedResidualScalarCap : ∀ R ∈ cert.residuals, ∀ s : Fin 64,
      (cert.target.filter fun x ↦
        cert.residualSupport x = R ∧ scalarClass x = s).card ≤ 20826085) :
    cert.target.card ≤ 83970774720 :=
  (cert.toTwoBlockProjectiveRayCertificate
    scalarClass fixedResidualScalarCap).target_card_le

/-- PR #819's first-match payment with q64, `f = 28` data indexed directly
by the deployed targets. -/
theorem c0_periodic_first_match_payment_of_target_certificate
    {α F : Type*} [DecidableEq α] [Field F] [DecidableEq F]
    {ambient : Finset F}
    (bad : Finset α)
    (cert28 : TargetTwoBlockCertificate α F)
    (scalarClass : α → Fin 64)
    (fixedResidualScalarCap : ∀ R ∈ cert28.residuals, ∀ s : Fin 64,
      (cert28.target.filter fun x ↦
        cert28.residualSupport x = R ∧ scalarClass x = s).card ≤ 20826085)
    (cert29 : F29ProjectiveRayCertificate α F)
    (cert5 : C0PeriodicSingletonCertificate.Q128OccupancyCertificate
      α F ambient 5 14641173)
    (cert7 : C0PeriodicSingletonCertificate.Q128OccupancyCertificate
      α F ambient 7 10193410)
    (hthree : (3 : F) ≠ 0) (hambient : ambient.card = 128)
    (hcover : bad ⊆
      cert29.target ∪ cert28.target ∪ cert5.target ∪ cert7.target) :
    bad.card ≤ 16501904760592192 :=
  c0_periodic_first_match_payment_of_twoBlock_certificate
    bad
    (cert28.toTwoBlockProjectiveRayCertificate
      scalarClass fixedResidualScalarCap)
    cert29 cert5 cert7 hthree hambient hcover

#print axioms TargetTwoBlockCertificate.toTwoBlockFamilyCertificate
#print axioms TargetTwoBlockCertificate.distinct_residuals_card_le
#print axioms TargetTwoBlockCertificate.toTwoBlockProjectiveRayCertificate
#print axioms TargetTwoBlockCertificate.target_card_le
#print axioms c0_periodic_first_match_payment_of_target_certificate

end GrandeFinale.C0PeriodicF28TargetCompiler
