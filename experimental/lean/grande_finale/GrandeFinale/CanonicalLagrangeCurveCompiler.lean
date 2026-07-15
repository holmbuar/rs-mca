import GrandeFinale.DirectionDistanceAllPairs

/-!
# Canonical-Lagrange curve compiler

This module contains **UNPROVED STATEMENT TARGETS**.  It records the exact
all-pair, moving-root, and positive-depth interfaces of the canonical
Lagrange chart.  It does not claim a Lean proof.
-/

open scoped Classical

noncomputable section

namespace GrandeFinale
namespace CanonicalLagrangeCurveCompiler

open DirectionDistanceAllPairs

set_option autoImplicit false

universe u v

variable {D : Type u} {F : Type v}
variable [Fintype D] [DecidableEq D]
variable [Field F] [DecidableEq F]

abbrev Pair (D : Type u) (F : Type v) := SlopeErrorPair D F

def canonicalIdentityDepth (R t : ℕ) : ℕ :=
  R - t - 1

def CanonicalLagrangePairConclusion
    (P : Finset (Pair D F)) (N t g : ℕ) : Prop :=
  (∀ p ∈ P, weight p.2 = t) ∧
    Set.InjOn (fun p : Pair D F => p.1) (↑P : Set (Pair D F)) ∧
    g ≤ t ∧
    P.card ≤ N - g ∧
    P.card ≤ N

/--
**UNPROVED STATEMENT TARGET (canonical-Lagrange all-pair compiler).**

The normalized first `2t` moments determine one exact-weight locator per
slope, and its formal common-root factor sharpens the complete pair bound
to `N-g`.
-/
def canonicalLagrangeAllPairTarget
    (P : Finset (Pair D F)) (N t g : ℕ) : Prop :=
  1 ≤ t →
    2 * t ≤ N →
    CanonicalLagrangePairConclusion P N t g

/--
**UNPROVED STATEMENT TARGET (residual curve arithmetic).**

The concrete proof supplies `delta ≤ h` and the moving-root incidence
`pairCount*h ≤ (N-g)*delta`, which should imply the `N-g` cap.
-/
def residualCurvePaymentTarget
    (N g h delta pairCount : ℕ) : Prop :=
  0 < h →
    delta ≤ h →
    pairCount * h ≤ (N - g) * delta →
    pairCount ≤ N - g

/--
**UNPROVED STATEMENT TARGET (positive-depth location).**
-/
def canonicalPositiveDepthTarget (R t : ℕ) : Prop :=
  2 * t ≤ R →
    t - 1 ≤ canonicalIdentityDepth R t

/--
**UNPROVED STATEMENT TARGET (constant-locator edge).**
-/
def constantLocatorTarget (pairCount N t : ℕ) : Prop :=
  2 * t ≤ N →
    pairCount ≤ 1 →
    pairCount ≤ N - t

end CanonicalLagrangeCurveCompiler
end GrandeFinale
