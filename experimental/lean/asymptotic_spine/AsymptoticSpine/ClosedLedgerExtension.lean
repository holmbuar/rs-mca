import AsymptoticSpine.UniformClosedLedger

namespace AsymptoticSpine
namespace ClosedLineLedger

/-!
# One-profile extension of a closed line ledger

This module isolates the finite bookkeeping shared by later semantic producers.
A new profile may be appended only after its assigned slope list has been proved
disjoint from every earlier assigned slope.  The construction preserves the
line-local order of summation and gives exact budget and natural-scale
telescopes.

The module proves no semantic owner, residual estimate, Sidon payment, ray
compiler, profile census, or `(UNIF)` estimate.  Those remain inputs carried by
the appended `ProfilePayment` and by the surrounding row producer.
-/

/-- Flattened first-match slope image already owned on a closed line. -/
def assignedSlopeList {compilerLoss profileCap : Nat}
    (line : ClosedLineLedger compilerLoss profileCap) : List Nat :=
  (line.profiles.map (fun profile => profile.assignedSlopes)).flatten

/-- The earlier assigned slope image is duplicate-free. -/
theorem assignedSlopeList_nodup {compilerLoss profileCap : Nat}
    (line : ClosedLineLedger compilerLoss profileCap) :
    line.assignedSlopeList.Nodup :=
  line.firstMatchOwnership

/-- Local append identity for the package's stdlib-only natural-number sum. -/
theorem listSum_append_extension : ∀ xs ys : List Nat,
    listSum (xs ++ ys) = listSum xs + listSum ys := by
  intro xs
  induction xs with
  | nil =>
      intro ys
      simp
  | cons x xs ih =>
      intro ys
      simp [ih, Nat.add_assoc]

/-- Append one paid post-deletion profile to an already closed line.

`hdisjoint` is the exact cross-owner first-match obligation.  The output counts
all slopes assigned by the new profile in addition to the earlier line's
numerator; a concrete RS producer must prove that this numerical sum is the
intended bad-slope count for its covered line slice. -/
def appendPayment {compilerLoss profileCap : Nat}
    (line : ClosedLineLedger compilerLoss profileCap)
    (profile : ProfilePayment compilerLoss)
    (hdisjoint : ∀ gamma ∈ line.assignedSlopeList,
      gamma ∉ profile.assignedSlopes) :
    ClosedLineLedger compilerLoss (profileCap + 1) where
  badCount := line.badCount + profile.assignedSlopes.length
  profiles := line.profiles ++ [profile]
  firstMatchOwnership := by
    simp only [List.map_append, List.map_cons, List.map_nil,
      List.flatten_append, List.flatten_cons, List.flatten_nil, List.append_nil]
    change (line.assignedSlopeList ++ profile.assignedSlopes).Nodup
    apply List.nodup_append.mpr
    refine ⟨line.firstMatchOwnership, profile.assignedSlopes_nodup, ?_⟩
    intro a ha b hb hab
    subst b
    exact hdisjoint a ha hb
  atlasExhaustive := by
    simp only [List.map_append, List.map_cons, List.map_nil,
      List.flatten_append, List.flatten_cons, List.flatten_nil, List.append_nil,
      List.length_append]
    change line.badCount + profile.assignedSlopes.length ≤
      line.assignedSlopeList.length + profile.assignedSlopes.length
    exact Nat.add_le_add_right line.atlasExhaustive _
  profileCountControl := by
    simp only [List.length_append, List.length_cons, List.length_nil,
      Nat.add_zero]
    exact Nat.add_le_add_right line.profileCountControl 1

/-- Exact assigned-slope concatenation after appending one profile. -/
theorem assignedSlopeList_appendPayment
    {compilerLoss profileCap : Nat}
    (line : ClosedLineLedger compilerLoss profileCap)
    (profile : ProfilePayment compilerLoss)
    (hdisjoint : ∀ gamma ∈ line.assignedSlopeList,
      gamma ∉ profile.assignedSlopes) :
    (line.appendPayment profile hdisjoint).assignedSlopeList =
      line.assignedSlopeList ++ profile.assignedSlopes := by
  simp [appendPayment, assignedSlopeList]

/-- Exact line-local ray-budget telescope. -/
theorem appendPayment_budgetTotal
    {compilerLoss profileCap : Nat}
    (line : ClosedLineLedger compilerLoss profileCap)
    (profile : ProfilePayment compilerLoss)
    (hdisjoint : ∀ gamma ∈ line.assignedSlopeList,
      gamma ∉ profile.assignedSlopes) :
    (line.appendPayment profile hdisjoint).budgetTotal =
      line.budgetTotal + profile.rayBudget := by
  change listSum ((line.profiles ++ [profile]).map
      (fun current => current.rayBudget)) =
    listSum (line.profiles.map (fun current => current.rayBudget)) +
      profile.rayBudget
  rw [List.map_append, listSum_append_extension]
  simp

/-- Exact line-local natural-scale telescope. -/
theorem appendPayment_naturalTotal
    {compilerLoss profileCap : Nat}
    (line : ClosedLineLedger compilerLoss profileCap)
    (profile : ProfilePayment compilerLoss)
    (hdisjoint : ∀ gamma ∈ line.assignedSlopeList,
      gamma ∉ profile.assignedSlopes) :
    (line.appendPayment profile hdisjoint).naturalTotal =
      line.naturalTotal + profile.naturalScale := by
  change listSum ((line.profiles ++ [profile]).map
      (fun current => current.naturalScale)) =
    listSum (line.profiles.map (fun current => current.naturalScale)) +
      profile.naturalScale
  rw [List.map_append, listSum_append_extension]
  simp

/-! ## Executable regression -/

def extensionToyEarlierProfile : ProfilePayment 2 :=
  ProfilePayment.ofDirect .c1 [4] 1 2 (by decide) (by decide)

def extensionToyEarlierLine : ClosedLineLedger 2 1 where
  badCount := 1
  profiles := [extensionToyEarlierProfile]
  firstMatchOwnership := by decide
  atlasExhaustive := by decide
  profileCountControl := by decide

def extensionToyLaterProfile : ProfilePayment 2 :=
  ProfilePayment.ofDirect .c8 [7, 9] 1 2 (by decide) (by decide)

/-- The extension keeps the earlier slope first and appends the later cell. -/
theorem extensionToy_assignedSlopes :
    (extensionToyEarlierLine.appendPayment extensionToyLaterProfile
      (by decide)).assignedSlopeList = [4, 7, 9] := by
  decide

/-- The exact telescopes are visible in the finite fixture. -/
theorem extensionToy_totals :
    (extensionToyEarlierLine.appendPayment extensionToyLaterProfile
      (by decide)).budgetTotal = 4 /\
    (extensionToyEarlierLine.appendPayment extensionToyLaterProfile
      (by decide)).naturalTotal = 2 := by
  decide

#print axioms assignedSlopeList_nodup
#print axioms listSum_append_extension
#print axioms assignedSlopeList_appendPayment
#print axioms appendPayment_budgetTotal
#print axioms appendPayment_naturalTotal
#print axioms extensionToy_assignedSlopes
#print axioms extensionToy_totals

end ClosedLineLedger
end AsymptoticSpine
