import GrandeFinale.DirectionDistanceAllPairs

/-!
# Depth-zero identity owner for complete LineRay pairs

This module contains **UNPROVED STATEMENT TARGETS**.  It records the exact
support injection and identity-profile arithmetic at agreement `a = k + 1`.
It does not claim a Lean proof.
-/

open scoped Classical

noncomputable section

namespace GrandeFinale
namespace DepthZeroIdentityLineRayOwner

open DirectionDistanceAllPairs

set_option autoImplicit false

universe u v w

variable {D : Type u} {F : Type v} {W : Type w}
variable [Fintype D] [DecidableEq D]
variable [Field F] [DecidableEq F]
variable [AddCommGroup W] [Module F W]

abbrev Pair (D : Type u) (F : Type v) := SlopeErrorPair D F

def VanishesOn (A : Finset D) (e : D → F) : Prop :=
  ∀ x ∈ A, e x = 0

def SupportedOutside (A : Finset D) (e : D → F) : Prop :=
  ∀ x ∈ A, e x = 0

def CommonOn (H : (D → F) →ₗ[F] W) (y₀ y₁ : W)
    (A : Finset D) : Prop :=
  ∃ e₀ e₁ : D → F,
    SupportedOutside A e₀ ∧ SupportedOutside A e₁ ∧
      H e₀ = y₀ ∧ H e₁ = y₁

def DepthZeroSupportSelector (H : (D → F) →ₗ[F] W)
    (y₀ y₁ : W) (P : Finset (Pair D F))
    (support : Pair D F → Finset D) (a : ℕ) : Prop :=
  ∀ p ∈ P,
    (support p).card = a ∧ VanishesOn (support p) p.2 ∧
      ¬ CommonOn H y₀ y₁ (support p)

def identityPrefixDepth (a k : ℕ) : ℕ :=
  a - k - 1

def identityProfileScale (N a : ℕ) : ℕ :=
  Nat.choose N a

/--
**UNPROVED STATEMENT TARGET (noncommon exact-support reduction).**

At `N = t + k + 1`, the RS kernel distance `t + 2` makes local common
explanations on adjacent `(k+1)`-subsets glue.  Hence a set that is globally
noncommon contains a noncommon `(k+1)`-subset.
-/
def noncommonSubsetExistsTarget
    (H : (D → F) →ₗ[F] W) (y₀ y₁ : W) (S : Finset D)
    (k t : ℕ) : Prop :=
  let a := k + 1
  Fintype.card D = t + a →
    KernelDistanceAtLeast H (t + 2) →
    a ≤ S.card →
    ¬ CommonOn H y₀ y₁ S →
    ∃ A : Finset D,
      A ⊆ S ∧ A.card = a ∧ ¬ CommonOn H y₀ y₁ A

/--
**UNPROVED STATEMENT TARGET (depth-zero support injection).**

The target counts every retained `(slope,error)` pair.  `support p` is an
actual noncommon agreement support, not an arbitrary subset of the zero set.
-/
def depthZeroSupportInjectionTarget
    (H : (D → F) →ₗ[F] W) (y₀ y₁ : W)
    (P : Finset (Pair D F)) (support : Pair D F → Finset D)
    (k t : ℕ) : Prop :=
  let a := k + 1
  BasicPairHypotheses H y₀ y₁ P t →
    KernelDistanceAtLeast H (t + 1) →
    Fintype.card D = t + a →
    DepthZeroSupportSelector H y₀ y₁ P support a →
    Set.InjOn support (↑P : Set (Pair D F)) ∧
      P.card ≤ identityProfileScale (Fintype.card D) a

/-- **UNPROVED STATEMENT TARGET (depth-zero identity arithmetic).** -/
def depthZeroIdentityArithmeticTarget (N k t : ℕ) : Prop :=
  N = t + (k + 1) →
    identityPrefixDepth (k + 1) k = 0 ∧
      identityProfileScale N (k + 1) = Nat.choose N t

/--
**UNPROVED STATEMENT TARGET (canonical route-cut ownership).**

This is the finite cardinality interface: the canonical `R=t+1` family has
one pair per `t`-set and is paid exactly by the depth-zero identity scale.
-/
def canonicalRouteCutOwnershipTarget (N k t pairCount : ℕ) : Prop :=
  N = t + (k + 1) → pairCount = Nat.choose N t →
    pairCount = identityProfileScale N (k + 1)

end DepthZeroIdentityLineRayOwner
end GrandeFinale
