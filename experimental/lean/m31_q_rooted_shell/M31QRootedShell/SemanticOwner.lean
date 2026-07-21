import M31QRootedShell.Envelope
import M31QRootedShell.MultiplicativeCounterexample

/-!
# Semantic C1--C8 owner-or-shell interface

This stdlib-only module states the semantic successor to PR #1005 without
repeating its rooted-shell summation compiler or its support-only
counterexamples.

The owner function is executable and fixed before a received line is chosen.
A certified owner carries the complete typed chain

`received line -> explanation state -> witness -> codeword -> ray -> distinct slope`,

together with a deduplicated line-local slope image, its exact slope numerator
and denominator, and the natural prefix-profile scale.  Support symmetry or an
empty common core cannot construct this certificate by itself.
-/

namespace M31QRootedShell.SemanticOwner

/-- Ordered earlier owners.  C9 is the residual, not an earlier owner. -/
inductive OwnerId where
  | c1
  | c2
  | c3
  | c4
  | c5
  | c6
  | c7
  | c8
  deriving Repr, DecidableEq

/--
One executable owner function fixed before any received line is selected.
The triggers may inspect the complete semantic explanation state, including its
line, but their definitions and C1--C8 order are fixed globally.
-/
structure FixedOwnerFunction (Explanation : Type) where
  c1 : Explanation → Bool
  c2 : Explanation → Bool
  c3 : Explanation → Bool
  c4 : Explanation → Bool
  c5 : Explanation → Bool
  c6 : Explanation → Bool
  c7 : Explanation → Bool
  c8 : Explanation → Bool

/-- Literal fixed-before-line C1--C8 first-match projector. -/
def FixedOwnerFunction.classify {Explanation : Type}
    (f : FixedOwnerFunction Explanation) (x : Explanation) : Option OwnerId :=
  if f.c1 x then some OwnerId.c1
  else if f.c2 x then some OwnerId.c2
  else if f.c3 x then some OwnerId.c3
  else if f.c4 x then some OwnerId.c4
  else if f.c5 x then some OwnerId.c5
  else if f.c6 x then some OwnerId.c6
  else if f.c7 x then some OwnerId.c7
  else if f.c8 x then some OwnerId.c8
  else none

/-- The deliberately owner-free adapter used by the mandatory regression. -/
def allResidualOwnerFunction {Explanation : Type} : FixedOwnerFunction Explanation where
  c1 := fun _ => false
  c2 := fun _ => false
  c3 := fun _ => false
  c4 := fun _ => false
  c5 := fun _ => false
  c6 := fun _ => false
  c7 := fun _ => false
  c8 := fun _ => false

@[simp] theorem allResidualOwnerFunction_classify
    {Explanation : Type} (x : Explanation) :
    (allResidualOwnerFunction : FixedOwnerFunction Explanation).classify x = none := by
  rfl

/--
The semantic data that an owner must preserve.  `valid` is the application-side
predicate asserting that the explanation is a genuine state for the received
line and code under study; the compatibility fields then expose every arrow in
the required chain.
-/
structure SemanticChain
    (Line Explanation Witness Support Codeword Ray Slope Prefix : Type) where
  valid : Explanation → Prop
  lineOf : Explanation → Line
  witnessOf : Explanation → Witness
  supportOfWitness : Witness → Support
  codewordOfWitness : Witness → Codeword
  rayOfCodeword : Codeword → Ray
  slopeOfRay : Ray → Slope
  supportOf : Explanation → Support
  codewordOf : Explanation → Codeword
  rayOf : Explanation → Ray
  slopeOf : Explanation → Slope
  prefixOf : Support → Prefix
  distance : Support → Support → Nat
  support_compatible : ∀ x, valid x →
    supportOf x = supportOfWitness (witnessOf x)
  codeword_compatible : ∀ x, valid x →
    codewordOf x = codewordOfWitness (witnessOf x)
  ray_compatible : ∀ x, valid x →
    rayOf x = rayOfCodeword (codewordOf x)
  slope_compatible : ∀ x, valid x →
    slopeOf x = slopeOfRay (rayOf x)

/-- Natural-number ceiling division. -/
def ceilDiv (N D : Nat) : Nat := (N + D - 1) / D

/--
Natural prefix-profile scale.  Its denominator is the coefficient-field scale
`q_prof^w`, not the slope-sampling denominator.
-/
structure NaturalProfileScale where
  profileFieldCard : Nat
  prefixDepth : Nat
  fullSupportMass : Nat
  loss : Nat
  profileFieldCard_pos : 0 < profileFieldCard

/-- Exact natural-profile denominator `q_prof^w`. -/
def NaturalProfileScale.denominator (s : NaturalProfileScale) : Nat :=
  s.profileFieldCard ^ s.prefixDepth

/-- Integral ceiling of the natural profile average. -/
def NaturalProfileScale.averageCeil (s : NaturalProfileScale) : Nat :=
  ceilDiv s.fullSupportMass s.denominator

/-- Finite paid-cell envelope `loss * (1 + ceil(M/q_prof^w))`. -/
def NaturalProfileScale.naturalNumerator (s : NaturalProfileScale) : Nat :=
  s.loss * (1 + s.averageCeil)

/--
Exact slope budget.  `slopeDenominator` is the sampler denominator and remains
separate from `NaturalProfileScale.denominator`.
-/
structure ExactSlopeBudget where
  numerator : Nat
  slopeDenominator : Nat
  slopeDenominator_pos : 0 < slopeDenominator
  numerator_le_denominator : numerator ≤ slopeDenominator

/-- Deduplicated line-local slope image with exact and natural-scale caps. -/
structure PaidSlopeProfile (Slope : Type) where
  naturalScale : NaturalProfileScale
  exactBudget : ExactSlopeBudget
  slopes : List Slope
  slopes_nodup : slopes.Nodup
  slopeCount_le_exact : slopes.length ≤ exactBudget.numerator
  exact_le_natural : exactBudget.numerator ≤ naturalScale.naturalNumerator

/--
Semantic owner ledger.  `ownerFn` is global; only the paid profile is line-local.
The soundness fields are exactly what support-only quotient/dihedral/core tests
do not supply.
-/
structure PaidOwnerLedger
    (Line Explanation Witness Support Codeword Ray Slope Prefix : Type)
    (chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix) where
  ownerFn : FixedOwnerFunction Explanation
  profile : OwnerId → Line → PaidSlopeProfile Slope
  classifies_valid : ∀ x owner, ownerFn.classify x = some owner → chain.valid x
  slope_mem_profile : ∀ x owner, ownerFn.classify x = some owner →
    chain.slopeOf x ∈ (profile owner (chain.lineOf x)).slopes

/-- A certified earlier first-match owner for one explanation state. -/
structure EarlierOwnerCertificate
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    (chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix)
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (x : Explanation) where
  owner : OwnerId
  classified : ledger.ownerFn.classify x = some owner

/-- Propositional packaging of one concrete owner certificate. -/
def HasEarlierOwner
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    (chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix)
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (x : Explanation) : Prop :=
  Nonempty (EarlierOwnerCertificate chain ledger x)

/-- A certified owner is a genuine semantic explanation state. -/
theorem EarlierOwnerCertificate.valid
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    {ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain}
    {x : Explanation} (c : EarlierOwnerCertificate chain ledger x) :
    chain.valid x :=
  ledger.classifies_valid x c.owner c.classified

/-- Every arrow in the received-line-to-slope chain is preserved. -/
theorem EarlierOwnerCertificate.preserves_chain
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    {ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain}
    {x : Explanation} (c : EarlierOwnerCertificate chain ledger x) :
    chain.supportOf x = chain.supportOfWitness (chain.witnessOf x) ∧
      chain.codewordOf x = chain.codewordOfWitness (chain.witnessOf x) ∧
      chain.rayOf x = chain.rayOfCodeword (chain.codewordOf x) ∧
      chain.slopeOf x = chain.slopeOfRay (chain.rayOf x) ∧
      chain.slopeOf x ∈
        (ledger.profile c.owner (chain.lineOf x)).slopes := by
  have hv : chain.valid x := c.valid
  exact ⟨chain.support_compatible x hv, chain.codeword_compatible x hv,
    chain.ray_compatible x hv, chain.slope_compatible x hv,
    ledger.slope_mem_profile x c.owner c.classified⟩

/-- Exact numerator/denominator and natural-scale payment carried by an owner. -/
theorem EarlierOwnerCertificate.budget_chain
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    {ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain}
    {x : Explanation} (c : EarlierOwnerCertificate chain ledger x) :
    (ledger.profile c.owner (chain.lineOf x)).slopes.length ≤
        (ledger.profile c.owner (chain.lineOf x)).exactBudget.numerator ∧
      (ledger.profile c.owner (chain.lineOf x)).exactBudget.numerator ≤
        (ledger.profile c.owner (chain.lineOf x)).exactBudget.slopeDenominator ∧
      (ledger.profile c.owner (chain.lineOf x)).exactBudget.numerator ≤
        (ledger.profile c.owner (chain.lineOf x)).naturalScale.naturalNumerator :=
  ⟨(ledger.profile c.owner (chain.lineOf x)).slopeCount_le_exact,
    (ledger.profile c.owner (chain.lineOf x)).exactBudget.numerator_le_denominator,
    (ledger.profile c.owner (chain.lineOf x)).exact_le_natural⟩

/--
A rooted same-prefix shell on one received line.  The neighbor list consists of
semantic explanation states, not bare supports.  Duplicate support projections
are forbidden, so its length is the rooted support degree.
-/
structure RootedShell
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    (chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix) where
  line : Line
  prefixTarget : Prefix
  anchor : Support
  shell : Nat
  neighbors : List Explanation
  neighbors_valid : ∀ x ∈ neighbors, chain.valid x
  neighbors_on_line : ∀ x ∈ neighbors, chain.lineOf x = line
  neighbors_same_prefix : ∀ x ∈ neighbors,
    chain.prefixOf (chain.supportOf x) = prefixTarget
  neighbors_in_shell : ∀ x ∈ neighbors,
    chain.distance anchor (chain.supportOf x) = shell
  neighborSupports_nodup : (neighbors.map chain.supportOf).Nodup

/-- The literal local rooted-shell inequality at intercept `b` and coefficient `c`. -/
def LocalEnvelopeAt
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (s : RootedShell chain) (Q b c ambientShell : Nat) : Prop :=
  Q * (s.neighbors.length - b) ≤ c * ambientShell

/-- The shell is the actual post-C1--C8 residual for the fixed owner function. -/
def IsActualPostC1C8Residual
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain) : Prop :=
  ∀ x ∈ s.neighbors, ledger.ownerFn.classify x = none

/--
The exact semantic theorem target: local envelope, or an explanation in the
violating shell carries a certified earlier paid slope owner.
-/
def SemanticEnvelopeOrOwner
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain) (Q b c ambientShell : Nat) : Prop :=
  LocalEnvelopeAt s Q b c ambientShell ∨
    ∃ x ∈ s.neighbors, HasEarlierOwner chain ledger x

/-- On the exact residual, the owner branch is impossible. -/
theorem actualResidual_has_no_certified_owner
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain) (hactual : IsActualPostC1C8Residual ledger s) :
    ¬ ∃ x ∈ s.neighbors, HasEarlierOwner chain ledger x := by
  intro howner
  obtain ⟨x, hx, hcert⟩ := howner
  obtain ⟨cert⟩ := hcert
  have hnone := hactual x hx
  have hsome : ledger.ownerFn.classify x = some cert.owner := cert.classified
  rw [hnone] at hsome
  cases hsome

/--
A proof of the semantic disjunction immediately gives `3+7` on the actual
post-C1--C8 residual.
-/
theorem semantic_three_plus_seven_on_actual_residual
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain) (Q ambientShell : Nat)
    (hactual : IsActualPostC1C8Residual ledger s)
    (hsemantic : SemanticEnvelopeOrOwner ledger s Q 3 7 ambientShell) :
    LocalEnvelopeAt s Q 3 7 ambientShell := by
  cases hsemantic with
  | inl h => exact h
  | inr h => exact (actualResidual_has_no_certified_owner ledger s hactual h).elim

/-- Any violation of the semantic theorem's envelope branch forces an owner. -/
theorem violation_forces_certified_earlier_owner
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain) (Q b c ambientShell : Nat)
    (hsemantic : SemanticEnvelopeOrOwner ledger s Q b c ambientShell)
    (hviol : c * ambientShell < Q * (s.neighbors.length - b)) :
    ∃ x ∈ s.neighbors, HasEarlierOwner chain ledger x := by
  cases hsemantic with
  | inl h => exact ((Nat.not_lt_of_ge h) hviol).elim
  | inr h => exact h

/-- The imported PR #1005 arithmetic makes the `F_241` full envelope false. -/
theorem f241_localEnvelope_fails
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (s : RootedShell chain)
    (hdegree : s.neighbors.length =
      MultiplicativeCounterexample.rootedDegree 6) :
    ¬ LocalEnvelopeAt s MultiplicativeCounterexample.q 3 7
      MultiplicativeCounterexample.ambientShell6 := by
  intro h
  unfold LocalEnvelopeAt at h
  rw [hdegree] at h
  exact (Nat.not_lt_of_ge h) MultiplicativeCounterexample.three_plus_seven_fails

/--
Mandatory `F_241` regression: any claimed semantic theorem on the ten-neighbor
packet must return a certified earlier paid slope owner.  The support census and
arithmetic are imported from PR #1005 rather than repeated.
-/
theorem f241_semantic_target_forces_certified_owner
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain)
    (hdegree : s.neighbors.length =
      MultiplicativeCounterexample.rootedDegree 6)
    (hsemantic : SemanticEnvelopeOrOwner ledger s
      MultiplicativeCounterexample.q 3 7
      MultiplicativeCounterexample.ambientShell6) :
    ∃ x ∈ s.neighbors, HasEarlierOwner chain ledger x := by
  exact violation_forces_certified_earlier_owner ledger s
    MultiplicativeCounterexample.q 3 7
    MultiplicativeCounterexample.ambientShell6 hsemantic (by
      simpa [hdegree] using MultiplicativeCounterexample.three_plus_seven_fails)

/--
An all-residual/support-only adapter cannot pass the mandatory regression.  In
particular, quotient/dihedral support symmetry and empty planted-core tests do
not count as semantic ownership without the received-line-to-slope certificate.
-/
theorem f241_all_residual_rejects_semantic_target
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain)
    (hdegree : s.neighbors.length =
      MultiplicativeCounterexample.rootedDegree 6)
    (hallResidual : IsActualPostC1C8Residual ledger s) :
    ¬ SemanticEnvelopeOrOwner ledger s MultiplicativeCounterexample.q 3 7
      MultiplicativeCounterexample.ambientShell6 := by
  intro hsemantic
  have hlocal := semantic_three_plus_seven_on_actual_residual ledger s
    MultiplicativeCounterexample.q
    MultiplicativeCounterexample.ambientShell6 hallResidual hsemantic
  exact f241_localEnvelope_fails s hdegree hlocal

/-- Explicit rejection of the owner-free fixed-before-line function. -/
theorem f241_owner_free_function_rejects_semantic_target
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain)
    (howner : ledger.ownerFn =
      (allResidualOwnerFunction : FixedOwnerFunction Explanation))
    (hdegree : s.neighbors.length =
      MultiplicativeCounterexample.rootedDegree 6) :
    ¬ SemanticEnvelopeOrOwner ledger s MultiplicativeCounterexample.q 3 7
      MultiplicativeCounterexample.ambientShell6 := by
  apply f241_all_residual_rejects_semantic_target ledger s hdegree
  intro x hx
  rw [howner]
  exact allResidualOwnerFunction_classify x

end M31QRootedShell.SemanticOwner
