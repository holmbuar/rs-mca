import M31QRootedShell.SemanticOwner

/-!
# Natural-scale specialization of the semantic owner-or-shell interface

This module removes the remaining free normalization symbol from the semantic
successor to PR #1005.  The local shell coefficient is literally the natural
prefix denominator `q_prof ^ w`; the MCA slope denominator remains a separate
field of every paid owner profile.
-/

namespace M31QRootedShell.SemanticOwner

/-- The local rooted-shell inequality at the literal natural profile scale. -/
def LocalNaturalEnvelopeAt
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (s : RootedShell chain) (scale : NaturalProfileScale)
    (b c ambientShell : Nat) : Prop :=
  scale.denominator * (s.neighbors.length - b) ≤ c * ambientShell

/-- The printed formula is exactly `q_prof^w * max(d-b,0) <= c H`. -/
theorem localNaturalEnvelopeAt_iff
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (s : RootedShell chain) (scale : NaturalProfileScale)
    (b c ambientShell : Nat) :
    LocalNaturalEnvelopeAt s scale b c ambientShell ↔
      scale.profileFieldCard ^ scale.prefixDepth *
          (s.neighbors.length - b) ≤ c * ambientShell := by
  rfl

/--
Natural-scale semantic target: the literal profile inequality, or a concrete
neighbor carries a certified earlier paid slope owner.
-/
def SemanticNaturalEnvelopeOrOwner
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain) (scale : NaturalProfileScale)
    (b c ambientShell : Nat) : Prop :=
  SemanticEnvelopeOrOwner ledger s scale.denominator b c ambientShell

/-- The natural-scale target yields literal `3+7` on the actual residual. -/
theorem semantic_natural_three_plus_seven_on_actual_residual
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain) (scale : NaturalProfileScale)
    (ambientShell : Nat)
    (hactual : IsActualPostC1C8Residual ledger s)
    (hsemantic : SemanticNaturalEnvelopeOrOwner ledger s scale 3 7 ambientShell) :
    LocalNaturalEnvelopeAt s scale 3 7 ambientShell := by
  exact semantic_three_plus_seven_on_actual_residual ledger s
    scale.denominator ambientShell hactual hsemantic

/-- A strict violation at the natural scale forces a concrete owner. -/
theorem natural_violation_forces_certified_earlier_owner
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain) (scale : NaturalProfileScale)
    (b c ambientShell : Nat)
    (hsemantic : SemanticNaturalEnvelopeOrOwner ledger s scale b c ambientShell)
    (hviol : c * ambientShell <
      scale.profileFieldCard ^ scale.prefixDepth *
        (s.neighbors.length - b)) :
    ∃ x ∈ s.neighbors, HasEarlierOwner chain ledger x := by
  exact violation_forces_certified_earlier_owner ledger s scale.denominator
    b c ambientShell hsemantic hviol

/-- Exact natural prefix scale of the mandatory `F_241` packet. -/
def f241NaturalScale : NaturalProfileScale where
  profileFieldCard := MultiplicativeCounterexample.p
  prefixDepth := MultiplicativeCounterexample.w
  fullSupportMass := MultiplicativeCounterexample.choose
    MultiplicativeCounterexample.n MultiplicativeCounterexample.m
  loss := 1
  profileFieldCard_pos := by decide

/-- Its denominator is exactly the imported `241^2 = 58,081` constant. -/
theorem f241NaturalScale_denominator :
    f241NaturalScale.denominator = MultiplicativeCounterexample.q := by
  rfl

/-- Mandatory natural-scale `F_241` regression. -/
theorem f241_semantic_natural_target_forces_certified_owner
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain)
    (hdegree : s.neighbors.length =
      MultiplicativeCounterexample.rootedDegree 6)
    (hsemantic : SemanticNaturalEnvelopeOrOwner ledger s f241NaturalScale
      3 7 MultiplicativeCounterexample.ambientShell6) :
    ∃ x ∈ s.neighbors, HasEarlierOwner chain ledger x := by
  apply f241_semantic_target_forces_certified_owner ledger s hdegree
  change SemanticEnvelopeOrOwner ledger s f241NaturalScale.denominator
    3 7 MultiplicativeCounterexample.ambientShell6 at hsemantic
  rw [f241NaturalScale_denominator] at hsemantic
  exact hsemantic

/-- The natural-scale target also rejects an actual-residual declaration. -/
theorem f241_all_residual_rejects_semantic_natural_target
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain)
    (hdegree : s.neighbors.length =
      MultiplicativeCounterexample.rootedDegree 6)
    (hallResidual : IsActualPostC1C8Residual ledger s) :
    ¬ SemanticNaturalEnvelopeOrOwner ledger s f241NaturalScale
      3 7 MultiplicativeCounterexample.ambientShell6 := by
  intro hsemantic
  apply f241_all_residual_rejects_semantic_target ledger s hdegree hallResidual
  change SemanticEnvelopeOrOwner ledger s f241NaturalScale.denominator
    3 7 MultiplicativeCounterexample.ambientShell6 at hsemantic
  rw [f241NaturalScale_denominator] at hsemantic
  exact hsemantic

end M31QRootedShell.SemanticOwner
