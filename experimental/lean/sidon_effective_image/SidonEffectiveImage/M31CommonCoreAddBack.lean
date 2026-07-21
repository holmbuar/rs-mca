import AsymptoticSpine.FirstMatch
import M31QRootedShell.Deployed

/-!
# M31 common-core loss-one add-back

Local, field-for-field restatement of the open #1025 padded-frame interface,
without importing any open-PR module.  The companion note proves the actual
Reed--Solomon puncturing theorem.  This module checks its ordered-selector and
finite-ledger compiler at the exact deployed constants.
-/

namespace SidonEffectiveImage.M31CommonCoreAddBack

def length : Nat := 2097152
def dimension : Nat := 1048576
def agreement : Nat := 1116023
def radius : Nat := 981129
def cutoff : Nat := 67447

def paddedFirstCap : Nat := 20765
def paddedFirstTwoCap : Nat := 41530
def paddedFirstThreeCap : Nat := 62295

def markedSourceKeyFloor : Nat := 259881
def signedOccupancyAllowance : Nat := 259880
def signedOccupancyBaseline : Nat := 16517335
def forbiddenListSize : Nat := 16777216

structure RootMask where
  actual : List Nat
  padding : List Nat

structure SourceMetadata where
  sourceKeyId : Nat
  receivedCenter : List Nat
  codewords : List (List Nat)
  exactWeight : Nat
  orderedDomain : List Nat
  orderedAnchors : List Nat
  distinguishedExtra : Nat
  firstAgreementSelector : List (List Nat)
  rootStatusMasks : List RootMask
  semanticOwner : Option Nat
  refunds : List Int
  signedOccupancyCredits : List Int

structure SaturatedRank46Key where
  metadata : SourceMetadata
  paddedFirst : Nat
  paddedSecond : Nat
  paddedThird : Nat
  paddedLast : Nat
  maskedFirst : Nat
  maskedSecond : Nat
  maskedThird : Nat
  padded_last_floor : cutoff + 1 ≤ paddedLast
  padded_first_bound : paddedFirst ≤ paddedFirstCap
  padded_first_two_bound : paddedFirst + paddedSecond ≤ paddedFirstTwoCap
  padded_first_three_bound :
    paddedFirst + paddedSecond + paddedThird ≤ paddedFirstThreeCap
  masked_first_three_bound :
    maskedFirst + maskedSecond + maskedThird ≤
      paddedFirstThreeCap + 3 * (radius - metadata.exactWeight)

def selected {α : Type} (domain : List α) (agrees : α → Bool) (a : Nat) : List α :=
  (domain.filter agrees).take a

def deleteCore {α : Type} [DecidableEq α] (domain core : List α) : List α :=
  domain.filter fun x => decide (x ∉ core)

theorem filter_comm {α : Type} (p q : α → Bool) :
    ∀ xs : List α, (xs.filter p).filter q = (xs.filter q).filter p := by
  intro xs
  induction xs with
  | nil => rfl
  | cons x xs ih =>
      cases hp : p x <;> cases hq : q x <;> simp [hp, hq, ih]

theorem take_filter_eq_take_of_prefix_kept {α : Type} (keep : α → Bool) :
    ∀ (n : Nat) (xs : List α),
      (∀ x ∈ xs.take n, keep x = true) →
      (xs.filter keep).take n = xs.take n := by
  intro n
  induction n with
  | zero => intro xs _; simp
  | succ n ih =>
      intro xs h
      cases xs with
      | nil => simp
      | cons x xs =>
          have hx : keep x = true := h x (by simp)
          have ht : ∀ y ∈ xs.take n, keep y = true := by
            intro y hy
            exact h y (by simp [hy])
          simp [hx, ih xs ht]

theorem selected_deleteCore_eq {α : Type} [DecidableEq α]
    (domain core : List α) (agrees : α → Bool) (a : Nat)
    (hprefix : ∀ x ∈ selected domain agrees a, x ∉ core) :
    selected (deleteCore domain core) agrees a = selected domain agrees a := by
  unfold selected deleteCore
  rw [filter_comm (fun x => decide (x ∉ core)) agrees domain]
  apply take_filter_eq_take_of_prefix_kept (fun x => decide (x ∉ core)) a
  intro x hx
  simpa [hprefix x hx]

theorem map_eq_of_pointwise {α β : Type} (f g : α → β) :
    ∀ xs : List α, (∀ x ∈ xs, f x = g x) → xs.map f = xs.map g := by
  intro xs
  induction xs with
  | nil => intro _; rfl
  | cons x xs ih =>
      intro h
      have hx := h x List.mem_cons_self
      have ht : ∀ y ∈ xs, f y = g y := by
        intro y hy
        exact h y (List.mem_cons_of_mem x hy)
      simp [hx, ih ht]

structure CanonicalCommonCoreShortening where
  frame : SaturatedRank46Key
  core : List Nat
  agreementPredicates : List (Nat → Bool)
  selectors_match :
    frame.metadata.firstAgreementSelector =
      agreementPredicates.map
        (fun agrees => selected frame.metadata.orderedDomain agrees agreement)
  selected_avoids_core :
    ∀ agrees ∈ agreementPredicates,
      ∀ x ∈ selected frame.metadata.orderedDomain agrees agreement, x ∉ core
  core_nodup : core.Nodup
  domain_nodup : frame.metadata.orderedDomain.Nodup
  core_subdomain : ∀ x ∈ core, x ∈ frame.metadata.orderedDomain
  core_degree_bound :
    core.length ≤ frame.paddedFirst + frame.paddedSecond + frame.paddedThird
  shortened_length_exact :
    (deleteCore frame.metadata.orderedDomain core).length = length - core.length

theorem core_degree_le_cap (cert : CanonicalCommonCoreShortening) :
    cert.core.length ≤ paddedFirstThreeCap :=
  Nat.le_trans cert.core_degree_bound cert.frame.padded_first_three_bound

theorem selector_preserved (cert : CanonicalCommonCoreShortening)
    (agrees : Nat → Bool) (h : agrees ∈ cert.agreementPredicates) :
    selected (deleteCore cert.frame.metadata.orderedDomain cert.core)
        agrees agreement =
      selected cert.frame.metadata.orderedDomain agrees agreement :=
  selected_deleteCore_eq cert.frame.metadata.orderedDomain cert.core agrees agreement
    (cert.selected_avoids_core agrees h)

theorem selector_vector_preserved (cert : CanonicalCommonCoreShortening) :
    cert.agreementPredicates.map
        (fun agrees => selected
          (deleteCore cert.frame.metadata.orderedDomain cert.core) agrees agreement) =
      cert.frame.metadata.firstAgreementSelector := by
  calc
    _ = cert.agreementPredicates.map
          (fun agrees => selected cert.frame.metadata.orderedDomain agrees agreement) := by
            apply map_eq_of_pointwise
            intro agrees h
            exact selector_preserved cert agrees h
    _ = _ := cert.selectors_match.symm

structure RestrictionEquiv (Full Short : Type) where
  toShort : Full → Short
  toFull : Short → Full
  toFull_toShort : ∀ x, toFull (toShort x) = x
  toShort_toFull : ∀ y, toShort (toFull y) = y

theorem RestrictionEquiv.injective {Full Short : Type}
    (e : RestrictionEquiv Full Short) : Function.Injective e.toShort := by
  intro x y h
  calc
    x = e.toFull (e.toShort x) := (e.toFull_toShort x).symm
    _ = e.toFull (e.toShort y) := congrArg e.toFull h
    _ = y := e.toFull_toShort y

def shortenedComponent {Full Short : Type}
    (e : RestrictionEquiv Full Short) (full : List Full) : List Short :=
  full.map e.toShort

theorem shortenedComponent_nodup {Full Short : Type}
    (e : RestrictionEquiv Full Short) (full : List Full) (h : full.Nodup) :
    (shortenedComponent e full).Nodup := by
  exact h.map e.injective

theorem mem_shortenedComponent_iff {Full Short : Type}
    (e : RestrictionEquiv Full Short) (full : List Full) (y : Short) :
    y ∈ shortenedComponent e full ↔ e.toFull y ∈ full := by
  constructor
  · intro hy
    rw [shortenedComponent, List.mem_map] at hy
    obtain ⟨x, hx, hxy⟩ := hy
    rw [← hxy, e.toFull_toShort]
    exact hx
  · intro hy
    rw [shortenedComponent, List.mem_map]
    exact ⟨e.toFull y, hy, e.toShort_toFull y⟩

theorem shortenedComponent_length_exact {Full Short : Type}
    (e : RestrictionEquiv Full Short) (full : List Full) :
    (shortenedComponent e full).length = full.length := by
  simp [shortenedComponent]

theorem integrated_constant_alignment :
    M31QRootedShell.Deployed.listM = radius ∧
    M31QRootedShell.Deployed.w = cutoff ∧
    M31QRootedShell.Deployed.Bstar = 16777215 := by
  decide

theorem deployed_parameter_identities :
    radius = length - agreement ∧
    cutoff = agreement - dimension ∧
    paddedFirstThreeCap < cutoff ∧
    cutoff - paddedFirstThreeCap = 5152 ∧
    length - paddedFirstThreeCap = 2034857 ∧
    radius - paddedFirstThreeCap = 918834 ∧
    (length - paddedFirstThreeCap) - dimension = 986281 := by
  decide

theorem signed_occupancy_crossing :
    signedOccupancyBaseline + markedSourceKeyFloor = forbiddenListSize ∧
    signedOccupancyAllowance + 1 = markedSourceKeyFloor ∧
    M31QRootedShell.Deployed.Bstar + 1 = forbiddenListSize := by
  decide

def shortenedLength (cert : CanonicalCommonCoreShortening) : Nat :=
  (deleteCore cert.frame.metadata.orderedDomain cert.core).length

def shortenedRadius (cert : CanonicalCommonCoreShortening) : Nat :=
  shortenedLength cert - agreement

theorem shortened_length_floor (cert : CanonicalCommonCoreShortening) :
    2034857 ≤ shortenedLength cert := by
  unfold shortenedLength
  rw [cert.shortened_length_exact]
  have hc := core_degree_le_cap cert
  simp only [length, paddedFirstThreeCap] at *
  omega

theorem shortened_dimension_gate (cert : CanonicalCommonCoreShortening) :
    dimension ≤ shortenedLength cert := by
  have h := shortened_length_floor cert
  simp only [dimension] at *
  omega

theorem shortened_agreement_gate (cert : CanonicalCommonCoreShortening) :
    agreement ≤ shortenedLength cert := by
  have h := shortened_length_floor cert
  simp only [agreement] at *
  omega

theorem shortened_radius_exact (cert : CanonicalCommonCoreShortening) :
    shortenedRadius cert = radius - cert.core.length := by
  unfold shortenedRadius shortenedLength
  rw [cert.shortened_length_exact]
  have hc := core_degree_le_cap cert
  simp only [length, agreement, radius, paddedFirstThreeCap] at *
  omega

theorem shortened_radius_floor (cert : CanonicalCommonCoreShortening) :
    918834 ≤ shortenedRadius cert := by
  rw [shortened_radius_exact]
  have hc := core_degree_le_cap cert
  simp only [radius, paddedFirstThreeCap] at *
  omega

structure ShortenedRank46Key where
  metadata : SourceMetadata
  coreDegree : Nat
  shortLength : Nat
  shortRadius : Nat
  core_degree_le : coreDegree ≤ paddedFirstThreeCap
  short_length_eq : shortLength = length - coreDegree
  short_radius_eq : shortRadius = radius - coreDegree
  dimension_gate : dimension ≤ shortLength
  agreement_gate : agreement ≤ shortLength

def shortenKey (cert : CanonicalCommonCoreShortening) : ShortenedRank46Key where
  metadata := cert.frame.metadata
  coreDegree := cert.core.length
  shortLength := shortenedLength cert
  shortRadius := shortenedRadius cert
  core_degree_le := core_degree_le_cap cert
  short_length_eq := cert.shortened_length_exact
  short_radius_eq := shortened_radius_exact cert
  dimension_gate := shortened_dimension_gate cert
  agreement_gate := shortened_agreement_gate cert

def compileAll (certs : List CanonicalCommonCoreShortening) : List ShortenedRank46Key :=
  certs.map shortenKey

@[simp] theorem compileAll_length (certs : List CanonicalCommonCoreShortening) :
    (compileAll certs).length = certs.length := by simp [compileAll]

theorem common_core_addback_exact (certs : List CanonicalCommonCoreShortening) :
    (compileAll certs).map ShortenedRank46Key.metadata =
      certs.map (fun cert => cert.frame.metadata) := by
  simp [compileAll, shortenKey]

theorem source_key_ids_preserved (certs : List CanonicalCommonCoreShortening) :
    (compileAll certs).map (fun key => key.metadata.sourceKeyId) =
      certs.map (fun cert => cert.frame.metadata.sourceKeyId) := by
  simp [compileAll, shortenKey]

theorem source_key_ids_nodup_preserved
    (certs : List CanonicalCommonCoreShortening)
    (h : (certs.map (fun cert => cert.frame.metadata.sourceKeyId)).Nodup) :
    ((compileAll certs).map (fun key => key.metadata.sourceKeyId)).Nodup := by
  rw [source_key_ids_preserved]
  exact h

theorem marked_source_key_floor_preserved
    (certs : List CanonicalCommonCoreShortening)
    (h : markedSourceKeyFloor ≤ certs.length) :
    markedSourceKeyFloor ≤ (compileAll certs).length := by
  simpa using h

theorem signed_credit_sum_preserved
    (certs : List CanonicalCommonCoreShortening) :
    ((compileAll certs).map
      (fun key => key.metadata.signedOccupancyCredits.sum)).sum =
      (certs.map (fun cert => cert.frame.metadata.signedOccupancyCredits.sum)).sum := by
  simp [compileAll, shortenKey, Function.comp_def]

def sourceIdCells (keys : List ShortenedRank46Key) : List (List Nat) :=
  keys.map (fun key => [key.metadata.sourceKeyId])

theorem firstMatch_addback_le_source_keys
    (certs : List CanonicalCommonCoreShortening) :
    AsymptoticSpine.firstMatchCount (sourceIdCells (compileAll certs)) ≤ certs.length := by
  have h := AsymptoticSpine.firstMatch_le_sum_cellSizes
    (sourceIdCells (compileAll certs))
  simpa [sourceIdCells, compileAll] using h

theorem maximal_core_regression :
    length - paddedFirstThreeCap = 2034857 ∧
    radius - paddedFirstThreeCap = 918834 ∧
    dimension ≤ length - paddedFirstThreeCap ∧
    agreement ≤ length - paddedFirstThreeCap ∧
    paddedFirstThreeCap < cutoff := by
  decide

#print axioms filter_comm
#print axioms take_filter_eq_take_of_prefix_kept
#print axioms selected_deleteCore_eq
#print axioms map_eq_of_pointwise
#print axioms core_degree_le_cap
#print axioms selector_preserved
#print axioms selector_vector_preserved
#print axioms RestrictionEquiv.injective
#print axioms shortenedComponent_nodup
#print axioms mem_shortenedComponent_iff
#print axioms shortenedComponent_length_exact
#print axioms integrated_constant_alignment
#print axioms deployed_parameter_identities
#print axioms signed_occupancy_crossing
#print axioms shortened_length_floor
#print axioms shortened_dimension_gate
#print axioms shortened_agreement_gate
#print axioms shortened_radius_exact
#print axioms shortened_radius_floor
#print axioms common_core_addback_exact
#print axioms source_key_ids_nodup_preserved
#print axioms marked_source_key_floor_preserved
#print axioms signed_credit_sum_preserved
#print axioms firstMatch_addback_le_source_keys
#print axioms maximal_core_regression

end SidonEffectiveImage.M31CommonCoreAddBack
