import AsymptoticSpine.UniformClosedLedger

namespace AsymptoticSpine

/-!
# Labeled atlas-order numeric interface

This file retains the historical module name because it is the audit boundary
for the C7 ownership regressions.  It does **not** formalize a semantic
classifier.  `ClosedLineLedger` is a numeric compiler interface: its owner tags,
assigned slope lists, disjointness, exhaustiveness inequality, and line list are
all supplied by a caller.

The labels below record provenance metadata for a proposed C3 payment; the
labels prove no semantic classification.  They do not prove a gcd, resultant,
ramification, quotient, locator, witness theorem, or least-applicable owner
predicate.  A concrete Reed--Solomon use must separately
prove those source-facing facts and the completeness of its received-line list.

The purpose of this module is narrower: once a caller has supplied labeled C3
payments followed by later payments, together with the exact numeric ownership
and exhaustiveness fields, the existing `sup_line sum_profile` compiler applies
without changing summation order.  No active-atlas policy is selected here.
-/

/-- Provenance metadata for a proposed planted payment.  Constructors are labels
only and carry no semantic soundness theorem. -/
inductive C3ProvenanceLabel where
  | gcd
  | resultant
  | ramification
  | quotient
  | other
  deriving DecidableEq, Repr

/-- A labeled direct C3 payment.  `labelId` and `labelKind` are metadata; the
slope list, natural scale, and payment inequality are explicit numeric inputs. -/
structure LabeledC3Payment (compilerLoss : Nat) where
  labelId : Nat
  labelKind : C3ProvenanceLabel
  assignedSlopes : List Nat
  assignedSlopes_nodup : assignedSlopes.Nodup
  naturalScale : Nat
  paid : assignedSlopes.length ≤ compilerLoss * naturalScale

namespace LabeledC3Payment

/-- Forget the provenance metadata and install the supplied numeric payment in
the existing closed-ledger type. -/
def payment {compilerLoss : Nat} (profile : LabeledC3Payment compilerLoss) :
    ProfilePayment compilerLoss :=
  ProfilePayment.ofDirect .c3 profile.assignedSlopes profile.naturalScale
    compilerLoss profile.assignedSlopes_nodup profile.paid

@[simp] theorem payment_owner {compilerLoss : Nat}
    (profile : LabeledC3Payment compilerLoss) :
    profile.payment.owner = .c3 := rfl

@[simp] theorem payment_assignedSlopes {compilerLoss : Nat}
    (profile : LabeledC3Payment compilerLoss) :
    profile.payment.assignedSlopes = profile.assignedSlopes := rfl

end LabeledC3Payment

/-- Witness-local metadata used by the singleton-planted regression.  The
structure intentionally has no field or constructor producing a ledger owner. -/
structure WitnessLocalRefinement where
  witnessId : Nat
  factorId : Nat

/-- One supplied atlas-order numeric slice: labeled C3 payments first, followed
by later payments.  `ownership` and `exhaustive` are explicit caller-supplied
facts; this structure does not prove that the slopes are actual RS bad slopes or
that C3 is their semantic least owner. -/
structure LabeledC3ThenLater
    (compilerLoss c3Cap laterCap : Nat) where
  badCount : Nat
  c3Profiles : List (LabeledC3Payment compilerLoss)
  laterProfiles : List (ProfilePayment compilerLoss)
  c3CountControl : c3Profiles.length ≤ c3Cap
  laterCountControl : laterProfiles.length ≤ laterCap
  ownership :
    ((c3Profiles.map (fun p => p.assignedSlopes)) ++
      (laterProfiles.map (fun p => p.assignedSlopes))).flatten.Nodup
  exhaustive :
    badCount ≤
      (((c3Profiles.map (fun p => p.assignedSlopes)) ++
        (laterProfiles.map (fun p => p.assignedSlopes))).flatten).length

namespace LabeledC3ThenLater

/-- Forget labels and concatenate the supplied payment lists in the stated
atlas order. -/
def profiles {compilerLoss c3Cap laterCap : Nat}
    (atlas : LabeledC3ThenLater compilerLoss c3Cap laterCap) :
    List (ProfilePayment compilerLoss) :=
  atlas.c3Profiles.map LabeledC3Payment.payment ++ atlas.laterProfiles

/-- Compile the supplied numeric slice to one closed line.  The result inherits
no semantic content beyond the fields already present in `atlas`. -/
def line {compilerLoss c3Cap laterCap : Nat}
    (atlas : LabeledC3ThenLater compilerLoss c3Cap laterCap) :
    ClosedLineLedger compilerLoss (c3Cap + laterCap) where
  badCount := atlas.badCount
  profiles := atlas.profiles
  firstMatchOwnership := by
    unfold profiles
    rw [List.map_append, List.map_map]
    exact atlas.ownership
  atlasExhaustive := by
    unfold profiles
    rw [List.map_append, List.map_map]
    exact atlas.exhaustive
  profileCountControl := by
    unfold profiles
    rw [List.length_append, List.length_map]
    exact Nat.add_le_add atlas.c3CountControl atlas.laterCountControl

/-- Once the numeric inputs are supplied, the existing line compiler applies. -/
theorem bad_le_loss_mul_naturalTotal
    {compilerLoss c3Cap laterCap : Nat}
    (atlas : LabeledC3ThenLater compilerLoss c3Cap laterCap) :
    atlas.badCount ≤ compilerLoss * atlas.line.naturalTotal :=
  atlas.line.bad_le_loss_mul_naturalTotal

/-- Finite row wrapper preserving `sup_line sum_profile`.  The caller still owes
completeness of `atlases` over received lines and the actual uniform estimate. -/
def ledger {compilerLoss c3Cap laterCap envelope : Nat}
    (atlases : List (LabeledC3ThenLater compilerLoss c3Cap laterCap))
    (hUnif : ∀ atlas ∈ atlases, atlas.line.naturalTotal ≤ envelope) :
    UniformClosedLedger compilerLoss (c3Cap + laterCap) envelope where
  lines := atlases.map line
  windowUniformity := by
    intro current hcurrent
    rcases List.mem_map.mp hcurrent with ⟨atlas, hatlas, rfl⟩
    exact hUnif atlas hatlas

/-- Numeric compiler theorem for the supplied finite line list.  This is not an
actual semantic atlas, actual `(UNIF)`, or an RS row theorem. -/
theorem ledger_compiles
    {compilerLoss c3Cap laterCap envelope : Nat}
    (atlases : List (LabeledC3ThenLater compilerLoss c3Cap laterCap))
    (hUnif : ∀ atlas ∈ atlases, atlas.line.naturalTotal ≤ envelope) :
    (ledger atlases hUnif).rowBad ≤ compilerLoss * envelope :=
  (ledger atlases hUnif).compile

end LabeledC3ThenLater

/-- Executable numeric fixture: one labeled C3 slope is followed by two C7
slopes.  The provenance label is not a proof that any actual row has this
classification. -/
def labeledOwnershipFixtureC3 : LabeledC3Payment 3 where
  labelId := 7
  labelKind := .resultant
  assignedSlopes := [10]
  assignedSlopes_nodup := by decide
  naturalScale := 1
  paid := by decide

def labeledOwnershipFixtureC7 : ProfilePayment 3 :=
  ProfilePayment.ofDirect .c7 [11, 12] 1 3 (by decide) (by decide)

def labeledOwnershipFixture : LabeledC3ThenLater 3 1 1 where
  badCount := 3
  c3Profiles := [labeledOwnershipFixtureC3]
  laterProfiles := [labeledOwnershipFixtureC7]
  c3CountControl := by decide
  laterCountControl := by decide
  ownership := by decide
  exhaustive := by decide

example : labeledOwnershipFixture.line.badCount ≤
    3 * labeledOwnershipFixture.line.naturalTotal := by
  exact labeledOwnershipFixture.bad_le_loss_mul_naturalTotal

#print axioms LabeledC3ThenLater.bad_le_loss_mul_naturalTotal
#print axioms LabeledC3ThenLater.ledger_compiles

end AsymptoticSpine
