import M31QRootedShell.SemanticResidualFilter
import M31QRootedShell.DeployedOwnerProfiles

/-!
# A genuine semantic `F_241` owner/profile regression

The support-only packet from PR #1005 is lifted to one explicit received line.
Eleven exact explanation states carry explaining polynomials, normalized
codeword rays, distinct slopes, and parity certificates excluding a common
explanation of the received-line direction.

Two shell neighbors form an executable earlier common-GCD/pencil owner with an
exact two-slope line-local profile.  Its literal `classify = none` residual has
eight neighbors and satisfies the natural-scale `3+7` inequality with margin
`18,295`.

This is a finite semantic regression, not a deployed Mersenne-31 C1--C8 atlas.
-/

namespace M31QRootedShell.SemanticOwner.F241SemanticLine

open M31QRootedShell
open M31QRootedShell.MultiplicativeCounterexample

abbrev Explanation := Fin 11
abbrev Witness := Explanation
abbrev Support := List Nat
abbrev Prefix := Nat × Nat

structure ReceivedLine where
  u0 : Nat → Nat
  u1 : Nat → Nat

structure CodewordRay where
  coordinates : List Nat
  slope : Nat
  deriving Repr, DecidableEq

structure ExplainingCodeword where
  coefficients : List Nat
  scale : Nat
  ray : CodewordRay
  deriving Repr, DecidableEq

/-- First component of the explicit received line, indexed by the 20-point domain. -/
def actualU0 : Nat → Nat
  | 0 => 108
  | 1 => 150
  | 2 => 68
  | 3 => 65
  | 4 => 34
  | 5 => 129
  | 6 => 22
  | 7 => 52
  | 8 => 33
  | 9 => 226
  | 10 => 174
  | _ => 0

/-- Second component of the explicit received line. -/
def actualU1 : Nat → Nat
  | 0 => 5
  | 1 => 28
  | 2 => 224
  | 3 => 117
  | 4 => 204
  | 5 => 112
  | 6 => 224
  | 7 => 189
  | 8 => 230
  | 9 => 72
  | 10 => 55
  | _ => 0

def actualLine : ReceivedLine := ⟨actualU0, actualU1⟩

/-- The ten shell neighbors followed by the anchor explanation. -/
def supportTable : List Support :=
  [ [0, 1, 2, 4, 6, 7, 12, 15, 17, 19]
  , [0, 1, 3, 4, 6, 8, 13, 15, 18, 19]
  , [0, 1, 3, 5, 8, 10, 13, 15, 16, 18]
  , [0, 1, 4, 5, 9, 10, 14, 15, 16, 19]
  , [0, 1, 4, 7, 8, 9, 11, 17, 18, 19]
  , [0, 2, 3, 4, 5, 6, 12, 13, 15, 16]
  , [0, 2, 4, 5, 7, 9, 11, 12, 16, 17]
  , [0, 3, 4, 5, 8, 9, 11, 13, 16, 18]
  , [1, 2, 3, 7, 8, 12, 13, 16, 17, 18]
  , [1, 2, 4, 7, 9, 12, 14, 16, 17, 19]
  , [2, 5, 6, 10, 11, 13, 14, 17, 18, 19]
  ]

/-- Degree-`<8` explaining-polynomial coefficients, constant term first. -/
def coefficientTable : List (List Nat) :=
  [ [171, 176, 191, 210, 94, 14, 115, 194]
  , [140, 201, 133, 161, 175, 152, 122, 208]
  , [37, 130, 27, 158, 108, 217, 147, 117]
  , [41, 230, 170, 54, 57, 142, 7, 72]
  , [102, 124, 184, 203, 150, 123, 162, 210]
  , [22, 120, 143, 5, 219, 42, 154, 126]
  , [175, 213, 233, 115, 82, 137, 119, 127]
  , [1, 64, 94, 180, 21, 62, 176, 45]
  , [120, 53, 101, 117, 179, 171, 101, 131]
  , [86, 93, 79, 56, 134, 84, 102, 221]
  , [113, 237, 177, 78, 216, 69, 11, 189]
  ]

/-- Nonzero scalars used to normalize the codeword rays. -/
def scaleTable : List Nat :=
  [194, 208, 117, 72, 210, 126, 127, 45, 131, 221, 189]

/-- Normalized coefficient rays; every last coordinate is one. -/
def rayCoordinateTable : List (List Nat) :=
  [ [22, 227, 119, 175, 239, 92, 136, 1]
  , [98, 213, 69, 185, 2, 10, 230, 1]
  , [196, 135, 130, 127, 38, 179, 199, 1]
  , [24, 117, 76, 61, 51, 89, 57, 1]
  , [90, 237, 134, 9, 104, 66, 228, 1]
  , [4, 219, 26, 220, 237, 161, 28, 1]
  , [64, 144, 110, 166, 198, 225, 111, 1]
  , [75, 221, 61, 4, 129, 71, 186, 1]
  , [218, 28, 67, 80, 40, 154, 67, 1]
  , [68, 152, 225, 190, 162, 44, 19, 1]
  , [21, 204, 131, 119, 70, 96, 162, 1]
  ]

/-- Eleven distinct semantic slopes on the same received line. -/
def slopeTable : List Nat := [115, 44, 22, 133, 230, 0, 74, 107, 56, 9, 193]

/-- Dual parity weights on the eleven ten-point supports. -/
def parityTable : List (List Nat) :=
  [ [126, 49, 25, 199, 4, 139, 174, 112, 71, 65]
  , [124, 197, 153, 180, 21, 201, 21, 137, 2, 169]
  , [193, 29, 219, 11, 62, 60, 200, 218, 212, 1]
  , [68, 128, 109, 125, 229, 156, 82, 133, 113, 62]
  , [42, 33, 206, 62, 191, 9, 165, 62, 89, 105]
  , [9, 157, 93, 72, 154, 230, 219, 224, 206, 82]
  , [108, 29, 227, 182, 71, 40, 4, 150, 14, 139]
  , [3, 197, 60, 72, 7, 104, 21, 42, 194, 23]
  , [50, 108, 60, 85, 50, 116, 68, 191, 173, 63]
  , [229, 85, 41, 145, 179, 127, 22, 12, 125, 240]
  , [138, 46, 205, 127, 37, 196, 121, 2, 178, 155]
  ]

def supportOf (x : Explanation) : Support := supportTable.getD x.val []
def coefficientsOf (x : Explanation) : List Nat := coefficientTable.getD x.val []
def scaleOf (x : Explanation) : Nat := scaleTable.getD x.val 0
def rayCoordinatesOf (x : Explanation) : List Nat := rayCoordinateTable.getD x.val []
def slopeOf (x : Explanation) : Nat := slopeTable.getD x.val 0
def parityOf (x : Explanation) : List Nat := parityTable.getD x.val []

def codewordOf (x : Explanation) : ExplainingCodeword where
  coefficients := coefficientsOf x
  scale := scaleOf x
  ray := ⟨rayCoordinatesOf x, slopeOf x⟩

def rayOf (x : Explanation) : CodewordRay := (codewordOf x).ray

/-- Horner evaluation for low-to-high coefficient lists modulo `241`. -/
def evalCoefficients : List Nat → Nat → Nat
  | [], _ => 0
  | c :: cs, x => (c + x * evalCoefficients cs x) % p

/-- Coordinatewise scalar multiplication modulo `241`. -/
def scaleRay (scale : Nat) (coordinates : List Nat) : List Nat :=
  coordinates.map fun c => (scale * c) % p

/-- Weighted sum on one indexed support, modulo `241`. -/
def weightedSum : List Nat → List Nat → (Nat → Nat) → Nat
  | w :: ws, i :: is, f => (w * f i + weightedSum ws is f) % p
  | _, _, _ => 0

/-- Every support is a duplicate-free ten-subset of the displayed domain. -/
def supportShapeCheck (x : Explanation) : Bool :=
  let S := supportOf x
  S.length == 10 && noDuplicates S && S.all fun i => i < n

/-- Every state remains in the common depth-two prefix fibre `(92,135)`. -/
def prefixCheck (x : Explanation) : Bool :=
  prefix1 (supportOf x) == 92 && prefix2 (supportOf x) == 135

/-- The displayed polynomial explains `u0 + slope*u1` on the selected support. -/
def agreementCheck (x : Explanation) : Bool :=
  (supportOf x).all fun i =>
    evalCoefficients (coefficientsOf x) (domain i) ==
      (actualU0 i + slopeOf x * actualU1 i) % p

/-- The parity row annihilates every monomial of degree below eight. -/
def parityMomentCheck (x : Explanation) : Bool :=
  (List.range 8).all fun t =>
    weightedSum (parityOf x) (supportOf x)
      (fun i => domain i ^ t % p) == 0

/-- The same parity row does not annihilate the received-line direction. -/
def parityDirectionCheck (x : Explanation) : Bool :=
  weightedSum (parityOf x) (supportOf x) actualU1 != 0

/-- The stored codeword and normalized projective ray agree exactly. -/
def rayCheck (x : Explanation) : Bool :=
  let cw := codewordOf x
  cw.coefficients.length == 8 &&
    cw.ray.coordinates.length == 8 &&
    cw.scale != 0 &&
    cw.ray.coordinates.getD 7 0 == 1 &&
    cw.coefficients == scaleRay cw.scale cw.ray.coordinates

/-- Executable semantic validity of one exact explanation state. -/
def semanticValid (x : Explanation) : Bool :=
  supportShapeCheck x && prefixCheck x && agreementCheck x &&
    parityMomentCheck x && parityDirectionCheck x && rayCheck x

/-- All eleven records pass the full semantic certificate. -/
theorem all_explanations_semantically_valid :
    ∀ x : Explanation, semanticValid x = true := by
  native_decide

/-- The line-agreement checks themselves are exact. -/
theorem all_explanations_agree_on_their_supports :
    ∀ x : Explanation, agreementCheck x = true := by
  native_decide

/-- Every parity certificate has the required annihilation/nonannihilation pair. -/
theorem all_parity_certificates_valid :
    ∀ x : Explanation,
      parityMomentCheck x = true ∧ parityDirectionCheck x = true := by
  native_decide

/-- The displayed codeword rays are normalized correctly. -/
theorem all_ray_certificates_valid :
    ∀ x : Explanation, rayCheck x = true := by
  native_decide

/-- No two semantic states use the same slope. -/
theorem semantic_slopes_nodup : slopeTable.Nodup := by
  native_decide

/-- No two semantic states use the same normalized codeword ray. -/
theorem semantic_rays_nodup : rayCoordinateTable.Nodup := by
  native_decide

/-- The complete typed chain on the explicit received line. -/
def chain : SemanticChain
    ReceivedLine Explanation Witness Support ExplainingCodeword CodewordRay Nat Prefix where
  valid := fun x => semanticValid x = true
  lineOf := fun _ => actualLine
  witnessOf := fun x => x
  supportOfWitness := supportOf
  codewordOfWitness := codewordOf
  rayOfCodeword := fun c => c.ray
  slopeOfRay := fun r => r.slope
  supportOf := supportOf
  codewordOf := codewordOf
  rayOf := rayOf
  slopeOf := slopeOf
  prefixOf := fun S => (prefix1 S, prefix2 S)
  distance := exchangeDistance
  support_compatible := by intro _ _; rfl
  codeword_compatible := by intro _ _; rfl
  ray_compatible := by intro _ _; rfl
  slope_compatible := by intro _ _; rfl

/-- The two semantic states selected by the earlier common-GCD/pencil owner. -/
def ownerA : Explanation := 0
def ownerB : Explanation := 2

/-- Their two degree-ten support locators, constant coefficient first. -/
def locatorA : List Nat := [25, 68, 25, 95, 0, 89, 90, 46, 135, 149, 1]
def locatorB : List Nat := [201, 179, 205, 0, 146, 154, 35, 0, 135, 149, 1]

def commonCore : List Nat := [0, 1, 15]
def outsideCore : List Nat := indices.filter fun i => !commonCore.contains i

/-- Finite pencil parameter `lambda`; the sentinel `241` denotes infinity. -/
def pencilCoefficients (param : Nat) : List Nat :=
  if param < p then
    List.zipWith (fun a b => (a + param * b) % p) locatorA locatorB
  else locatorB

/-- Moving roots outside the certified common core. -/
def pencilMovingRootCount (param : Nat) : Nat :=
  (outsideCore.filter fun i =>
    evalCoefficients (pencilCoefficients param) (domain i) == 0).length

/-- Parameters with enough moving roots to be a split degree-seven quotient. -/
def splitPencilParameters : List Nat :=
  (List.range (p + 1)).filter fun param =>
    decide (7 ≤ pencilMovingRootCount param)

/-- The two locators vanish on exactly the two selected supports. -/
theorem locatorA_roots_exact :
    (indices.filter fun i => evalCoefficients locatorA (domain i) == 0) = supportOf ownerA := by
  native_decide

theorem locatorB_roots_exact :
    (indices.filter fun i => evalCoefficients locatorB (domain i) == 0) = supportOf ownerB := by
  native_decide

/-- The common support roots are exactly the three displayed core points. -/
theorem owner_pair_common_core_exact :
    (supportOf ownerA).filter (fun i => (supportOf ownerB).contains i) = commonCore := by
  native_decide

/-- Only the two projective endpoints have the seven required moving roots. -/
theorem splitPencilParameters_exact : splitPencilParameters = [0, 241] := by
  native_decide

/-- Executable earlier trigger for this exact semantic common-GCD chart. -/
def c3Trigger (x : Explanation) : Bool :=
  decide (x = ownerA ∨ x = ownerB)

/-- Fixed-before-line owner function: only the certified C3 chart fires. -/
def ownerFn : FixedOwnerFunction Explanation where
  c1 := fun _ => false
  c2 := fun _ => false
  c3 := c3Trigger
  c4 := fun _ => false
  c5 := fun _ => false
  c6 := fun _ => false
  c7 := fun _ => false
  c8 := fun _ => false

/-- Exact characterization of the executable classification. -/
theorem classify_eq_some_iff (x : Explanation) (owner : OwnerId) :
    ownerFn.classify x = some owner ↔
      (x = ownerA ∨ x = ownerB) ∧ owner = OwnerId.c3 := by
  by_cases hx : x = ownerA ∨ x = ownerB
  · constructor
    · intro hclass
      have hsome : (some OwnerId.c3 : Option OwnerId) = some owner := by
        simpa [ownerFn, c3Trigger, FixedOwnerFunction.classify, hx] using hclass
      cases hsome
      exact ⟨hx, rfl⟩
    · rintro ⟨_, rfl⟩
      simp [ownerFn, c3Trigger, FixedOwnerFunction.classify, hx]
  · constructor
    · intro hclass
      have hnone : (none : Option OwnerId) = some owner := by
        simpa [ownerFn, c3Trigger, FixedOwnerFunction.classify, hx] using hclass
      cases hnone
    · rintro ⟨h, _⟩
      exact (hx h).elim

/-- Exact natural numerator of the finite regression profile. -/
theorem f241NaturalScale_naturalNumerator : f241NaturalScale.naturalNumerator = 5 := by
  native_decide

/-- Empty paid profile for owner identifiers not used by the fixture. -/
def emptyProfile : PaidSlopeProfile Nat where
  naturalScale := f241NaturalScale
  exactBudget := {
    numerator := 0
    slopeDenominator := p
    slopeDenominator_pos := by native_decide
    numerator_le_denominator := by native_decide
  }
  slopes := []
  slopes_nodup := by simp
  slopeCount_le_exact := by simp
  exact_le_natural := by simp

/-- Exact two-slope line-local profile of the certified C3 pencil. -/
def c3Profile : PaidSlopeProfile Nat where
  naturalScale := f241NaturalScale
  exactBudget := {
    numerator := 2
    slopeDenominator := p
    slopeDenominator_pos := by native_decide
    numerator_le_denominator := by native_decide
  }
  slopes := [115, 22]
  slopes_nodup := by native_decide
  slopeCount_le_exact := by native_decide
  exact_le_natural := by
    rw [f241NaturalScale_naturalNumerator]
    native_decide

/-- Line-local paid profiles; only C3 is nonempty in this exact fixture. -/
def profile : OwnerId → ReceivedLine → PaidSlopeProfile Nat
  | OwnerId.c3, _ => c3Profile
  | _, _ => emptyProfile

/-- Fully instantiated semantic ledger for the explicit received line. -/
def ledger : PaidOwnerLedger
    ReceivedLine Explanation Witness Support ExplainingCodeword CodewordRay Nat Prefix chain where
  ownerFn := ownerFn
  profile := profile
  classifies_valid := by
    intro x _ _
    exact all_explanations_semantically_valid x
  slope_mem_profile := by
    intro x owner hclass
    rcases (classify_eq_some_iff x owner).mp hclass with ⟨hx, rfl⟩
    rcases hx with rfl | rfl <;> native_decide

/-- The ten-neighbor rooted shell on the semantic line. -/
def shellNeighbors : List Explanation := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def shell : RootedShell chain where
  line := actualLine
  prefixTarget := (92, 135)
  anchor := supportOf 10
  shell := 6
  neighbors := shellNeighbors
  neighbors_valid := by
    intro x _
    exact all_explanations_semantically_valid x
  neighbors_on_line := by intro _ _; rfl
  neighbors_same_prefix := by native_decide
  neighbors_in_shell := by native_decide
  neighborSupports_nodup := by native_decide

/-- The executable owned filter contains exactly the two certified states. -/
theorem ownedNeighbors_exact : ownedNeighbors ledger shell = [ownerA, ownerB] := by
  native_decide

/-- The literal `classify = none` residual contains the other eight states. -/
theorem residualNeighbors_exact :
    residualNeighbors ledger shell = [1, 3, 4, 5, 6, 7, 8, 9] := by
  native_decide

/-- Both earlier-owned states carry genuine semantic certificates. -/
theorem ownerA_has_certificate : HasEarlierOwner chain ledger ownerA := by
  apply ownedNeighbor_has_certificate ledger shell
  native_decide

theorem ownerB_has_certificate : HasEarlierOwner chain ledger ownerB := by
  apply ownedNeighbor_has_certificate ledger shell
  native_decide

/-- The exact two-slope owner budget keeps `q_slope=241` separate from `q_prof^w`. -/
theorem c3Profile_budget_chain :
    c3Profile.slopes.length = 2 ∧
      c3Profile.exactBudget.numerator = 2 ∧
      c3Profile.exactBudget.slopeDenominator = 241 ∧
      c3Profile.naturalScale.denominator = 58081 ∧
      c3Profile.naturalScale.naturalNumerator = 5 := by
  native_decide

/-- The executable residual has exact degree eight. -/
theorem residualShell_degree_exact :
    (residualShell ledger shell).neighbors.length = 8 := by
  native_decide

/-- Exact residual arithmetic: `58081*(8-3) <= 7*44100`, margin `18,295`. -/
theorem residualShell_three_plus_seven :
    LocalNaturalEnvelopeAt (residualShell ledger shell) f241NaturalScale
      3 7 ambientShell6 := by
  unfold LocalNaturalEnvelopeAt
  rw [residualShell_degree_exact, f241NaturalScale_denominator,
    MultiplicativeCounterexample.q_eq,
    MultiplicativeCounterexample.ambientShell6_eq]
  omega

/-- The executable residual is definitionally the actual C9 `none` fibre. -/
theorem residualShell_actual :
    IsActualPostC1C8Residual ledger (residualShell ledger shell) :=
  residualShell_is_actual ledger shell

/-- The concrete residual proof compiles to the semantic owner-or-envelope target. -/
theorem semantic_owner_or_shell :
    SemanticNaturalEnvelopeOrOwner ledger shell f241NaturalScale
      3 7 ambientShell6 :=
  semanticNaturalEnvelopeOrOwner_of_residualShell ledger shell f241NaturalScale
    3 7 ambientShell6 residualShell_three_plus_seven

/-- The exact regression has two, not merely one, earlier-owned neighbors. -/
theorem exactly_two_owned_neighbors :
    (ownedNeighbors ledger shell).length = 2 := by
  native_decide

/-- The inherited generic lower bound is attained by this semantic fixture. -/
theorem generic_two_owner_regression_is_sharp :
    2 ≤ (ownedNeighbors ledger shell).length :=
  f241_residualShell_bound_forces_two_owned_neighbors ledger shell (by native_decide)
    residualShell_three_plus_seven

#print axioms all_explanations_semantically_valid
#print axioms all_parity_certificates_valid
#print axioms semantic_slopes_nodup
#print axioms splitPencilParameters_exact
#print axioms ownerA_has_certificate
#print axioms ownerB_has_certificate
#print axioms residualShell_three_plus_seven
#print axioms semantic_owner_or_shell
#print axioms exactly_two_owned_neighbors

end M31QRootedShell.SemanticOwner.F241SemanticLine
