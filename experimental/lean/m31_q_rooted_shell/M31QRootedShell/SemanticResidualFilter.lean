import M31QRootedShell.SemanticNaturalScale

/-!
# Executable post-C1--C8 residual filter

The semantic owner function is fixed before the line.  This module applies that
literal function to a rooted shell, constructs its actual `none`-fiber residual,
and proves the owner-or-envelope target from a bound on that executable
residual.  The mandatory `F_241` packet yields a sharper regression: its
post-deletion residual can contain at most eight of the ten displayed
neighbors, so at least two neighbors must have genuine earlier-owner
certificates.
-/

namespace M31QRootedShell.SemanticOwner

/-- Keep exactly the explanations classified into the C9 residual. -/
def residualOf {Explanation : Type}
    (ownerFn : FixedOwnerFunction Explanation) (xs : List Explanation) :
    List Explanation :=
  xs.filter fun x => decide (ownerFn.classify x = none)

/-- Keep exactly the explanations assigned to an earlier C1--C8 owner. -/
def ownedOf {Explanation : Type}
    (ownerFn : FixedOwnerFunction Explanation) (xs : List Explanation) :
    List Explanation :=
  xs.filter fun x => decide (ownerFn.classify x ≠ none)

@[simp] theorem mem_residualOf
    {Explanation : Type} (ownerFn : FixedOwnerFunction Explanation)
    (xs : List Explanation) (x : Explanation) :
    x ∈ residualOf ownerFn xs ↔
      x ∈ xs ∧ ownerFn.classify x = none := by
  simp [residualOf]

@[simp] theorem mem_ownedOf
    {Explanation : Type} (ownerFn : FixedOwnerFunction Explanation)
    (xs : List Explanation) (x : Explanation) :
    x ∈ ownedOf ownerFn xs ↔
      x ∈ xs ∧ ownerFn.classify x ≠ none := by
  simp [ownedOf]

/-- The executable residual and owned filters partition the input list. -/
theorem residualOf_length_add_ownedOf_length
    {Explanation : Type} (ownerFn : FixedOwnerFunction Explanation) :
    ∀ xs : List Explanation,
      (residualOf ownerFn xs).length + (ownedOf ownerFn xs).length = xs.length := by
  intro xs
  induction xs with
  | nil => simp [residualOf, ownedOf]
  | cons x xs ih =>
      by_cases h : ownerFn.classify x = none
      · simp [residualOf, ownedOf, h] at ih ⊢
        omega
      · simp [residualOf, ownedOf, h] at ih ⊢
        omega

/-- Line-local executable C9 residual neighbors. -/
def residualNeighbors
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain) : List Explanation :=
  residualOf ledger.ownerFn s.neighbors

/-- Line-local neighbors assigned to one of the fixed earlier owners. -/
def ownedNeighbors
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain) : List Explanation :=
  ownedOf ledger.ownerFn s.neighbors

/-- The two executable neighbor lists have exact complementary cardinalities. -/
theorem residual_owned_length_eq
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain) :
    (residualNeighbors ledger s).length +
        (ownedNeighbors ledger s).length = s.neighbors.length := by
  simpa [residualNeighbors, ownedNeighbors] using
    residualOf_length_add_ownedOf_length ledger.ownerFn s.neighbors

/-- The actual post-C1--C8 rooted shell produced by the executable owner. -/
def residualShell
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain) : RootedShell chain where
  line := s.line
  prefixTarget := s.prefixTarget
  anchor := s.anchor
  shell := s.shell
  neighbors := residualNeighbors ledger s
  neighbors_valid := by
    intro x hx
    exact s.neighbors_valid x (mem_residualOf ledger.ownerFn s.neighbors x |>.mp hx).1
  neighbors_on_line := by
    intro x hx
    exact s.neighbors_on_line x (mem_residualOf ledger.ownerFn s.neighbors x |>.mp hx).1
  neighbors_same_prefix := by
    intro x hx
    exact s.neighbors_same_prefix x
      (mem_residualOf ledger.ownerFn s.neighbors x |>.mp hx).1
  neighbors_in_shell := by
    intro x hx
    exact s.neighbors_in_shell x (mem_residualOf ledger.ownerFn s.neighbors x |>.mp hx).1
  neighborSupports_nodup := by
    have hsub : List.Sublist (residualNeighbors ledger s) s.neighbors := by
      unfold residualNeighbors residualOf
      exact List.filter_sublist
    have hmap : List.Sublist
        ((residualNeighbors ledger s).map chain.supportOf)
        (s.neighbors.map chain.supportOf) :=
      hsub.map chain.supportOf
    exact hmap.nodup s.neighborSupports_nodup

/-- The constructed residual is definitionally the `none` fiber. -/
theorem residualShell_is_actual
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain) :
    IsActualPostC1C8Residual ledger (residualShell ledger s) := by
  intro x hx
  change x ∈ residualNeighbors ledger s at hx
  exact (mem_residualOf ledger.ownerFn s.neighbors x).mp hx |>.2

/-- Every explanation in the executable owned filter has a concrete certificate. -/
theorem ownedNeighbor_has_certificate
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain) {x : Explanation}
    (hx : x ∈ ownedNeighbors ledger s) :
    HasEarlierOwner chain ledger x := by
  have hne : ledger.ownerFn.classify x ≠ none :=
    (mem_ownedOf ledger.ownerFn s.neighbors x).mp hx |>.2
  cases hclass : ledger.ownerFn.classify x with
  | none => exact (hne hclass).elim
  | some owner => exact ⟨{ owner := owner, classified := hclass }⟩

/--
A natural-scale bound on the executable post-C1--C8 residual proves the desired
owner-or-envelope statement on the original shell.
-/
theorem semanticNaturalEnvelopeOrOwner_of_residualShell
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain) (scale : NaturalProfileScale)
    (b c ambientShell : Nat)
    (hresidual : LocalNaturalEnvelopeAt (residualShell ledger s) scale
      b c ambientShell) :
    SemanticNaturalEnvelopeOrOwner ledger s scale b c ambientShell := by
  unfold SemanticNaturalEnvelopeOrOwner
  by_cases howned : ownedNeighbors ledger s = []
  · left
    unfold LocalEnvelopeAt
    unfold LocalNaturalEnvelopeAt at hresidual
    have hpartition := residual_owned_length_eq ledger s
    have hlength : (residualNeighbors ledger s).length = s.neighbors.length := by
      simpa [howned] using hpartition
    simpa [residualShell, hlength] using hresidual
  · right
    cases hlist : ownedNeighbors ledger s with
    | nil => exact (howned hlist).elim
    | cons x xs =>
        have hxOwned : x ∈ ownedNeighbors ledger s := by
          rw [hlist]
          simp
        exact ⟨x, (mem_ownedOf ledger.ownerFn s.neighbors x).mp hxOwned |>.1,
          ownedNeighbor_has_certificate ledger s hxOwned⟩

/-- The exact `F_241` residual `3+7` bound permits at most eight neighbors. -/
theorem f241_residualShell_degree_le_eight
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain)
    (hresidual : LocalNaturalEnvelopeAt (residualShell ledger s)
      f241NaturalScale 3 7 MultiplicativeCounterexample.ambientShell6) :
    (residualNeighbors ledger s).length ≤ 8 := by
  unfold LocalNaturalEnvelopeAt at hresidual
  simp only [residualShell] at hresidual
  rw [f241NaturalScale_denominator, MultiplicativeCounterexample.q_eq,
    MultiplicativeCounterexample.ambientShell6_eq] at hresidual
  omega

/--
Mandatory strengthened regression: a semantic `3+7` residual bound on the
full ten-neighbor `F_241` shell requires at least two distinct earlier-owned
neighbors.
-/
theorem f241_residualShell_bound_forces_two_owned_neighbors
    {Line Explanation Witness Support Codeword Ray Slope Prefix : Type}
    {chain : SemanticChain Line Explanation Witness Support Codeword Ray Slope Prefix}
    (ledger : PaidOwnerLedger Line Explanation Witness Support Codeword Ray Slope Prefix chain)
    (s : RootedShell chain)
    (hdegree : s.neighbors.length =
      MultiplicativeCounterexample.rootedDegree 6)
    (hresidual : LocalNaturalEnvelopeAt (residualShell ledger s)
      f241NaturalScale 3 7 MultiplicativeCounterexample.ambientShell6) :
    2 ≤ (ownedNeighbors ledger s).length := by
  have hresidualDegree := f241_residualShell_degree_le_eight ledger s hresidual
  have hpartition := residual_owned_length_eq ledger s
  have hfull : s.neighbors.length = 10 := by
    calc
      s.neighbors.length = MultiplicativeCounterexample.rootedDegree 6 := hdegree
      _ = 10 := MultiplicativeCounterexample.rootedDegree_six
  omega

end M31QRootedShell.SemanticOwner
