import AsymptoticSpine.HighKappaCoverage

namespace AsymptoticSpine

/-!
# C8 common-core shortening and high-kappa owner-or-payment compilation

This module formalizes the exact finite compiler boundary isolated by
`experimental/notes/thresholds/common_core_cover_obstruction.md` and the
factor-aware correction in
`experimental/notes/audits/balanced_core_factored_rank_audit.md`.

A fixed common-core shortening is represented by an explicit certificate that
keeps the same duplicate-free slope list and commutes with the chosen
support-for-slope map.  Consequently every support budget, direct `(RC)` bound,
or shallow-prefix closure proved on the shortened chart transfers to the
original chart with no slope add-back loss.

The kernel ledger keeps the factored core and any residual common core
separate.  Only after the maximal common core has been removed may one identify
`kappa` with the shortened dimension `k - |K|`.  The resulting exact arithmetic
turns a high-kappa premise into the equivalent small-core premise and compiles
an earlier-owner theorem on that branch with a shortened-chart payment on the
complementary branch.

The module does not construct an RS shortening certificate, an actual semantic
C1--C8 owner, a deep-prefix MI/MA or Sidon payment, or a deployed row bound.
Those are explicit inputs to the compiler.
-/

/-- Exact finite interface for a fixed-core shortening of one first-match C8
cell.  The same slopes are retained, the displayed support projection is the
image of the original one, and the chosen support for every slope commutes with
shortening. -/
structure SlopePreservingShortening
    (Support ResidualSupport Slope : Type) where
  original : SE2Certificate Support Slope
  shortened : SE2Certificate ResidualSupport Slope
  shortenSupport : Support → ResidualSupport
  slopes_eq : shortened.slopes = original.slopes
  supports_eq : shortened.supports = original.supports.map shortenSupport
  supportOf_commutes :
    ∀ gamma, shortened.supportOf gamma = shortenSupport (original.supportOf gamma)

namespace SlopePreservingShortening

@[simp] theorem slopes_length_eq
    {Support ResidualSupport Slope : Type}
    (s : SlopePreservingShortening Support ResidualSupport Slope) :
    s.shortened.slopes.length = s.original.slopes.length :=
  congrArg List.length s.slopes_eq

@[simp] theorem supports_length_eq
    {Support ResidualSupport Slope : Type}
    (s : SlopePreservingShortening Support ResidualSupport Slope) :
    s.shortened.supports.length = s.original.supports.length := by
  rw [s.supports_eq, List.length_map]

@[simp] theorem supportOf_shortened
    {Support ResidualSupport Slope : Type}
    (s : SlopePreservingShortening Support ResidualSupport Slope)
    (gamma : Slope) :
    s.shortened.supportOf gamma = s.shortenSupport (s.original.supportOf gamma) :=
  s.supportOf_commutes gamma

/-- A support budget on the shortened chart pays the original distinct-slope
cell with no add-back factor. -/
theorem supportBudget_addBack
    {Support ResidualSupport Slope : Type}
    (s : SlopePreservingShortening Support ResidualSupport Slope)
    (budget : Nat)
    (hbudget : s.shortened.supports.length ≤ budget) :
    s.original.slopes.length ≤ budget := by
  rw [← s.slopes_eq]
  exact se2_to_paidBudget s.shortened budget hbudget

/-- A direct ray-compiler inequality on the shortened slope list is literally
the same inequality on the original slope list. -/
theorem directRC_addBack
    {Support ResidualSupport Slope : Type}
    (s : SlopePreservingShortening Support ResidualSupport Slope)
    (loss average : Nat)
    (h : DirectRC s.shortened.slopes.length loss average) :
    DirectRC s.original.slopes.length loss average := by
  rw [← s.slopes_eq]
  exact h

/-- The kernel-labelled shallow-prefix direct `(RC)` proposition also transfers
without changing the kernel label, loss, or average. -/
theorem kernelIndependentDirectRC_addBack
    {Support ResidualSupport Slope : Type}
    (s : SlopePreservingShortening Support ResidualSupport Slope)
    (kernelDim loss average : Nat)
    (h : KernelIndependentDirectRC kernelDim s.shortened.slopes.length loss average) :
    KernelIndependentDirectRC kernelDim s.original.slopes.length loss average := by
  rw [← s.slopes_eq]
  exact h

/-- End-to-end shallow-prefix C8 payment after common-core shortening.  The
ambient prefix bridge is stated for the shortened support type, while the
conclusion pays the original slope cell. -/
theorem shallowClosure_addBack
    {Support ResidualSupport Slope Eff Raw : Type}
    [DecidableEq Eff] [DecidableEq Raw]
    (s : SlopePreservingShortening Support ResidualSupport Slope)
    (b : PrefixFiberBridge ResidualSupport Eff Raw) (z : Eff)
    (hchart :
      List.Sublist s.shortened.supports (b.depthPrefixChart (b.toPrefix z)))
    (bounds : ShallowPrefixClosureBounds b.fullSlice.length)
    (kernelDim : Nat) :
    KernelIndependentDirectRC kernelDim s.original.slopes.length
      (bounds.baseSize ^ bounds.prefixDepth) bounds.average := by
  rw [← s.slopes_eq]
  exact balancedCoreShallowClosure_to_directRC
    b z s.shortened hchart bounds kernelDim

/-- The same exact add-back feeds the direct branch of condition `(A6)`. -/
theorem shallowClosure_to_A6_addBack
    {Support ResidualSupport Slope Eff Raw : Type}
    [DecidableEq Eff] [DecidableEq Raw]
    (s : SlopePreservingShortening Support ResidualSupport Slope)
    (b : PrefixFiberBridge ResidualSupport Eff Raw) (z : Eff)
    (hchart :
      List.Sublist s.shortened.supports (b.depthPrefixChart (b.toPrefix z)))
    (bounds : ShallowPrefixClosureBounds b.fullSlice.length)
    (kernelDim : Nat) (directProfileBound : Prop) :
    A6RayCondition
      (KernelIndependentDirectRC kernelDim s.original.slopes.length
        (bounds.baseSize ^ bounds.prefixDepth) bounds.average)
      directProfileBound :=
  Or.inl (shallowClosure_addBack s b z hchart bounds kernelDim)

end SlopePreservingShortening

/-- Factor-aware C8 kernel bookkeeping.  `factoredCoreSize` is the core removed
from the original row.  `residualCoreSize` is any common core still present in
the shortened chart.  The exact MDS rank law is

`kernelDim = shortenedDimension - residualCoreSize`.

Only the special case `residualCoreSize = 0` represents removal of the maximal
common core. -/
structure FactoredKernelLedger where
  originalDimension : Nat
  factoredCoreSize : Nat
  shortenedDimension : Nat
  residualCoreSize : Nat
  kernelDim : Nat
  factoredCore_le : factoredCoreSize ≤ originalDimension
  residualCore_le : residualCoreSize ≤ shortenedDimension
  shortened_eq : shortenedDimension = originalDimension - factoredCoreSize
  kernel_eq : kernelDim = shortenedDimension - residualCoreSize

namespace FactoredKernelLedger

/-- The post-factor kernel never exceeds the shortened code dimension. -/
theorem kernel_le_shortened (ledger : FactoredKernelLedger) :
    ledger.kernelDim ≤ ledger.shortenedDimension := by
  rw [ledger.kernel_eq]
  exact Nat.sub_le _ _

/-- Predicate recording that the factored core was the full common core. -/
def MaximalCoreRemoved (ledger : FactoredKernelLedger) : Prop :=
  ledger.residualCoreSize = 0

/-- After the maximal common core is removed, the residual kernel equals the
shortened dimension. -/
theorem kernel_eq_shortened_of_maximal
    (ledger : FactoredKernelLedger)
    (hmax : ledger.MaximalCoreRemoved) :
    ledger.kernelDim = ledger.shortenedDimension := by
  rw [ledger.kernel_eq, hmax, Nat.sub_zero]

/-- Factor-aware correction: after maximal-core removal,
`kappa = k - |K|`, not the original `k`. -/
theorem kernel_eq_sub_core_of_maximal
    (ledger : FactoredKernelLedger)
    (hmax : ledger.MaximalCoreRemoved) :
    ledger.kernelDim = ledger.originalDimension - ledger.factoredCoreSize := by
  calc
    ledger.kernelDim = ledger.shortenedDimension :=
      ledger.kernel_eq_shortened_of_maximal hmax
    _ = ledger.originalDimension - ledger.factoredCoreSize := ledger.shortened_eq

/-- Exact finite high-kappa/small-core equivalence.  With the maximal common
core removed and a cutoff inside the original dimension,

`cutoff < kappa` iff `|K| < k - cutoff`.
-/
theorem highKernel_iff_smallCore
    (ledger : FactoredKernelLedger) (cutoff : Nat)
    (hmax : ledger.MaximalCoreRemoved)
    (hcutoff : cutoff ≤ ledger.originalDimension) :
    cutoff < ledger.kernelDim ↔
      ledger.factoredCoreSize < ledger.originalDimension - cutoff := by
  rw [ledger.kernel_eq_sub_core_of_maximal hmax]
  omega

end FactoredKernelLedger

/-- Exact C8 terminal: either the cell has an earlier certified semantic owner,
or its original distinct-slope numerator fits the displayed budget. -/
def C8OwnerOrPayment (earlierOwner : Prop) (slopeCount budget : Nat) : Prop :=
  earlierOwner ∨ slopeCount ≤ budget

/-- Kernel dichotomy compiler.  A theorem assigning every high-kappa shortened
cell to an earlier owner, together with a support payment on every small-kappa
shortened cell, pays the original cell. -/
theorem ownerOrPayment_of_kernelDichotomy
    {Support ResidualSupport Slope : Type}
    (s : SlopePreservingShortening Support ResidualSupport Slope)
    (ledger : FactoredKernelLedger)
    (earlierOwner : Prop) (cutoff budget : Nat)
    (highKernelOwner : cutoff < ledger.kernelDim → earlierOwner)
    (smallKernelPayment :
      ledger.kernelDim ≤ cutoff → s.shortened.supports.length ≤ budget) :
    C8OwnerOrPayment earlierOwner s.original.slopes.length budget := by
  by_cases hsmall : ledger.kernelDim ≤ cutoff
  · exact Or.inr (s.supportBudget_addBack budget (smallKernelPayment hsmall))
  · exact Or.inl (highKernelOwner (by omega))

/-- Maximal-core form of the compiler.  The high-kappa owner hypothesis can be
stated equivalently as an owner theorem for cells whose maximal common core is
too small to reduce the shortened dimension below `cutoff`. -/
theorem ownerOrPayment_of_maximalCoreThreshold
    {Support ResidualSupport Slope : Type}
    (s : SlopePreservingShortening Support ResidualSupport Slope)
    (ledger : FactoredKernelLedger)
    (earlierOwner : Prop) (cutoff budget : Nat)
    (hmax : ledger.MaximalCoreRemoved)
    (hcutoff : cutoff ≤ ledger.originalDimension)
    (smallCoreOwner :
      ledger.factoredCoreSize < ledger.originalDimension - cutoff → earlierOwner)
    (smallKernelPayment :
      ledger.kernelDim ≤ cutoff → s.shortened.supports.length ≤ budget) :
    C8OwnerOrPayment earlierOwner s.original.slopes.length budget := by
  apply ownerOrPayment_of_kernelDichotomy
    s ledger earlierOwner cutoff budget
  · intro hhigh
    exact smallCoreOwner ((ledger.highKernel_iff_smallCore cutoff hmax hcutoff).mp hhigh)
  · exact smallKernelPayment

/-! ## Exact finite fixtures -/

def c8ToyShortening : SlopePreservingShortening Nat Nat Nat where
  original := highKappaToySE2
  shortened := highKappaToySE2
  shortenSupport := id
  slopes_eq := rfl
  supports_eq := by simp
  supportOf_commutes := by intro gamma; rfl

def c8ToySmallKernelLedger : FactoredKernelLedger where
  originalDimension := 9
  factoredCoreSize := 5
  shortenedDimension := 4
  residualCoreSize := 0
  kernelDim := 4
  factoredCore_le := by decide
  residualCore_le := by decide
  shortened_eq := by decide
  kernel_eq := by decide

def c8ToyHighKernelLedger : FactoredKernelLedger where
  originalDimension := 9
  factoredCoreSize := 3
  shortenedDimension := 6
  residualCoreSize := 0
  kernelDim := 6
  factoredCore_le := by decide
  residualCore_le := by decide
  shortened_eq := by decide
  kernel_eq := by decide

/-- The small-kernel branch closes by the shortened support budget. -/
theorem c8Toy_smallKernel_payment :
    C8OwnerOrPayment False c8ToyShortening.original.slopes.length 2 := by
  exact ownerOrPayment_of_kernelDichotomy
    c8ToyShortening c8ToySmallKernelLedger False 4 2
    (by intro h; simp [c8ToySmallKernelLedger] at h)
    (by intro h; decide)

/-- The high-kernel branch is routed to the supplied earlier owner. -/
theorem c8Toy_highKernel_owner :
    C8OwnerOrPayment True c8ToyShortening.original.slopes.length 0 := by
  exact ownerOrPayment_of_kernelDichotomy
    c8ToyShortening c8ToyHighKernelLedger True 4 0
    (by intro h; trivial)
    (by intro h; simp [c8ToyHighKernelLedger] at h)

/-- The finite fixture also checks the high-kappa/small-core equivalence. -/
theorem c8Toy_highKernel_iff_smallCore :
    4 < c8ToyHighKernelLedger.kernelDim ↔
      c8ToyHighKernelLedger.factoredCoreSize <
        c8ToyHighKernelLedger.originalDimension - 4 := by
  exact c8ToyHighKernelLedger.highKernel_iff_smallCore 4 rfl (by decide)

#print axioms SlopePreservingShortening.slopes_length_eq
#print axioms SlopePreservingShortening.supports_length_eq
#print axioms SlopePreservingShortening.supportBudget_addBack
#print axioms SlopePreservingShortening.directRC_addBack
#print axioms SlopePreservingShortening.kernelIndependentDirectRC_addBack
#print axioms SlopePreservingShortening.shallowClosure_addBack
#print axioms SlopePreservingShortening.shallowClosure_to_A6_addBack
#print axioms FactoredKernelLedger.kernel_le_shortened
#print axioms FactoredKernelLedger.kernel_eq_shortened_of_maximal
#print axioms FactoredKernelLedger.kernel_eq_sub_core_of_maximal
#print axioms FactoredKernelLedger.highKernel_iff_smallCore
#print axioms ownerOrPayment_of_kernelDichotomy
#print axioms ownerOrPayment_of_maximalCoreThreshold
#print axioms c8Toy_smallKernel_payment
#print axioms c8Toy_highKernel_owner
#print axioms c8Toy_highKernel_iff_smallCore

end AsymptoticSpine
