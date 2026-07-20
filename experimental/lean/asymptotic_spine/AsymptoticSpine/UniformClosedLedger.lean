import AsymptoticSpine.FirstMatch
import AsymptoticSpine.AddBack

namespace AsymptoticSpine

/-!
# Minimal closed-ledger / UNIF interface

This module formalizes the finite arithmetic compiler boundary used by the
profile-envelope proof.  It deliberately begins after the geometric work:
semantic first match has produced disjoint assigned slope lists, every profile
has been paid through its own residual/Sidon/ray chain, and the remaining
row-level input is the line-local uniform estimate

`sup_line sum_profile naturalScale(line, profile) <= envelope`.

The compiler preserves that order.  It never replaces `sup_line sum_profile`
by `sum_profile sup_line`; `sup_sum_interchange_falsifier` is an executable
regression showing that the latter may be strictly larger.

No C1--C9 classifier, field theorem, image-normalized Sidon theorem,
balanced-core ray theorem, asymptotic profile-count theorem, or target
comparison is proved here.  Those obligations are exposed as typed fields.
-/

/-- The semantic owner attached to a paid first-match profile.  Constructors
are labels only: creating a value does not classify a concrete RS witness. -/
inductive LedgerOwner where
  | c1 | c2 | c3 | c4 | c5 | c6 | c7 | c8 | c9 | primitive
  deriving DecidableEq, Repr

/-- One post-deletion semantic profile on one received line.

The numerical chain is deliberately typed in the order used by the proof:

`assigned slopes -> ray budget -> image-normalized Sidon budget
                  -> residual budget -> natural profile scale`.

`rayBudget` is the actual line/profile distinct-slope budget `U(r, lambda)`.
The three loss factors are separately printed and must fit inside the one
row/compiler loss.  A cell with an independently proved direct distinct-slope
bound can use `ofDirect`; otherwise its residual, image-normalized Sidon, and
ray interfaces must be supplied honestly. -/
structure ProfilePayment (compilerLoss : Nat) where
  owner : LedgerOwner
  assignedSlopes : List Nat
  assignedSlopes_nodup : assignedSlopes.Nodup
  naturalScale : Nat
  residualBudget : Nat
  sidonBudget : Nat
  rayBudget : Nat
  residualLoss : Nat
  sidonLoss : Nat
  rayLoss : Nat
  residualToFull : residualBudget ≤ residualLoss * naturalScale
  imageNormalizedSidon : sidonBudget ≤ sidonLoss * residualBudget
  rayCompiler : rayBudget ≤ rayLoss * sidonBudget
  distinctSlopePayment : assignedSlopes.length ≤ rayBudget
  compilerLossDominates : rayLoss * sidonLoss * residualLoss ≤ compilerLoss

namespace ProfilePayment

/-- The complete per-profile chain pays the actual first-match distinct-slope
image at the profile's own natural scale. -/
theorem paidAtNaturalScale {compilerLoss : Nat}
    (profile : ProfilePayment compilerLoss) :
    profile.rayBudget ≤ compilerLoss * profile.naturalScale := by
  calc
    profile.rayBudget ≤ profile.rayLoss * profile.sidonBudget :=
      profile.rayCompiler
    _ ≤ profile.rayLoss * (profile.sidonLoss * profile.residualBudget) :=
      Nat.mul_le_mul_left profile.rayLoss profile.imageNormalizedSidon
    _ = (profile.rayLoss * profile.sidonLoss) * profile.residualBudget := by
      rw [Nat.mul_assoc]
    _ ≤ (profile.rayLoss * profile.sidonLoss) *
          (profile.residualLoss * profile.naturalScale) :=
      Nat.mul_le_mul_left (profile.rayLoss * profile.sidonLoss)
        profile.residualToFull
    _ = (profile.rayLoss * profile.sidonLoss * profile.residualLoss) *
          profile.naturalScale := by
      simp only [Nat.mul_assoc]
    _ ≤ compilerLoss * profile.naturalScale :=
      Nat.mul_le_mul_right profile.naturalScale profile.compilerLossDominates

/-- Direct adapter for any cell with an independently proved distinct-slope
payment.  The direct theorem is installed as the ray budget; the Sidon and
residual stages are identities, so no primitive analytic claim is manufactured. -/
def ofDirect (owner : LedgerOwner) (assignedSlopes : List Nat)
    (naturalScale compilerLoss : Nat)
    (hNodup : assignedSlopes.Nodup)
    (hPaid : assignedSlopes.length ≤ compilerLoss * naturalScale) :
    ProfilePayment compilerLoss where
  owner := owner
  assignedSlopes := assignedSlopes
  assignedSlopes_nodup := hNodup
  naturalScale := naturalScale
  residualBudget := compilerLoss * naturalScale
  sidonBudget := compilerLoss * naturalScale
  rayBudget := compilerLoss * naturalScale
  residualLoss := compilerLoss
  sidonLoss := 1
  rayLoss := 1
  residualToFull := by simp
  imageNormalizedSidon := by simp
  rayCompiler := by simp
  distinctSlopePayment := hPaid
  compilerLossDominates := by simp

end ProfilePayment

/-- Pull a constant multiplier through the stdlib-only list sum. -/
theorem listSum_map_const_mul {alpha : Type} (c : Nat) (f : alpha → Nat) :
    ∀ xs : List alpha,
      listSum (xs.map (fun x => c * f x)) = c * listSum (xs.map f) := by
  intro xs
  induction xs with
  | nil => simp
  | cons x xs ih =>
      simp only [List.map_cons, listSum_cons, ih, Nat.mul_add]

/-- The line-local output of the semantic first-match classifier.

* `firstMatchOwnership` records post-deletion disjointness of the assigned
  slope classes;
* `atlasExhaustive` is the numerical consequence of raw witness coverage that
  the producer must establish for the actual bad-slope numerator;
* `profileCountControl` prints the realized profile-count cap instead of
  hiding it in a later union bound.
-/
structure ClosedLineLedger (compilerLoss profileCap : Nat) where
  badCount : Nat
  profiles : List (ProfilePayment compilerLoss)
  firstMatchOwnership :
    (profiles.map (fun profile => profile.assignedSlopes)).flatten.Nodup
  atlasExhaustive :
    badCount ≤ (profiles.map (fun profile => profile.assignedSlopes)).flatten.length
  profileCountControl : profiles.length ≤ profileCap

namespace ClosedLineLedger

/-- Sum of the actual line/profile distinct-slope budgets `U(r, lambda)`. -/
def budgetTotal {compilerLoss profileCap : Nat}
    (line : ClosedLineLedger compilerLoss profileCap) : Nat :=
  listSum (line.profiles.map (fun profile => profile.rayBudget))

/-- Sum of the profiles' own natural scales on this received line. -/
def naturalTotal {compilerLoss profileCap : Nat}
    (line : ClosedLineLedger compilerLoss profileCap) : Nat :=
  listSum (line.profiles.map (fun profile => profile.naturalScale))

/-- Atlas exhaustiveness plus rooted distinct-slope projection bounds the line's
bad-slope numerator by the sum of its actual profile budgets. -/
theorem bad_le_budgetTotal {compilerLoss profileCap : Nat}
    (line : ClosedLineLedger compilerLoss profileCap) :
    line.badCount ≤ line.budgetTotal := by
  calc
    line.badCount ≤
        (line.profiles.map (fun profile => profile.assignedSlopes)).flatten.length :=
      line.atlasExhaustive
    _ = listSum (line.profiles.map
          (fun profile => profile.assignedSlopes.length)) := by
      rw [length_flatten]
      simp only [List.map_map, Function.comp_def]
    _ ≤ listSum (line.profiles.map (fun profile => profile.rayBudget)) := by
      exact listSum_map_le
        (fun profile : ProfilePayment compilerLoss =>
          profile.assignedSlopes.length)
        (fun profile => profile.rayBudget) line.profiles
        (fun profile _ => profile.distinctSlopePayment)
    _ = line.budgetTotal := rfl

/-- The per-profile residual/Sidon/ray chains are summed inside the received
line, before any outer supremum is taken. -/
theorem budgetTotal_le_loss_mul_naturalTotal
    {compilerLoss profileCap : Nat}
    (line : ClosedLineLedger compilerLoss profileCap) :
    line.budgetTotal ≤ compilerLoss * line.naturalTotal := by
  calc
    line.budgetTotal =
        listSum (line.profiles.map (fun profile => profile.rayBudget)) := rfl
    _ ≤ listSum (line.profiles.map
          (fun profile => compilerLoss * profile.naturalScale)) := by
      exact listSum_map_le
        (fun profile : ProfilePayment compilerLoss => profile.rayBudget)
        (fun profile => compilerLoss * profile.naturalScale) line.profiles
        (fun profile _ => profile.paidAtNaturalScale)
    _ = compilerLoss * line.naturalTotal := by
      simpa [naturalTotal] using
        (listSum_map_const_mul compilerLoss
          (fun profile : ProfilePayment compilerLoss => profile.naturalScale)
          line.profiles)

/-- Complete line-local compiler: semantic coverage, first-match ownership,
rooted slope payment, natural-scale payment, and profile-count visibility. -/
theorem bad_le_loss_mul_naturalTotal {compilerLoss profileCap : Nat}
    (line : ClosedLineLedger compilerLoss profileCap) :
    line.badCount ≤ compilerLoss * line.naturalTotal :=
  Nat.le_trans line.bad_le_budgetTotal
    line.budgetTotal_le_loss_mul_naturalTotal

end ClosedLineLedger

/-- Minimal finite row package.  The finite list models only the received lines
supplied by the producer; an RS application must separately prove that this
list is complete.  `windowUniformity` is the honest line-local `(UNIF)` input.
The profile-count cap remains available on every line through
`ClosedLineLedger.profileCountControl`. -/
structure UniformClosedLedger (compilerLoss profileCap envelope : Nat) where
  lines : List (ClosedLineLedger compilerLoss profileCap)
  windowUniformity : ∀ line ∈ lines, line.naturalTotal ≤ envelope

namespace UniformClosedLedger

/-- Finite supremum of bad-slope numerators over the supplied ledger lines. -/
def rowBad {compilerLoss profileCap envelope : Nat}
    (ledger : UniformClosedLedger compilerLoss profileCap envelope) : Nat :=
  listMax (ledger.lines.map (fun line => line.badCount))

/-- Correct `(UNIF)` quantity: each line is summed over profiles first. -/
def rowBudgetSup {compilerLoss profileCap envelope : Nat}
    (ledger : UniformClosedLedger compilerLoss profileCap envelope) : Nat :=
  listMax (ledger.lines.map (fun line => line.budgetTotal))

/-- Supremum of the line-local natural-scale sums. -/
def rowNaturalSup {compilerLoss profileCap envelope : Nat}
    (ledger : UniformClosedLedger compilerLoss profileCap envelope) : Nat :=
  listMax (ledger.lines.map (fun line => line.naturalTotal))

/-- Supremum of the realized semantic profile count. -/
def rowProfileCountSup {compilerLoss profileCap envelope : Nat}
    (ledger : UniformClosedLedger compilerLoss profileCap envelope) : Nat :=
  listMax (ledger.lines.map (fun line => line.profiles.length))

/-- `sup_line bad(line) <= sup_line sum_profile U(line, profile)`. -/
theorem rowBad_le_rowBudgetSup {compilerLoss profileCap envelope : Nat}
    (ledger : UniformClosedLedger compilerLoss profileCap envelope) :
    ledger.rowBad ≤ ledger.rowBudgetSup := by
  unfold rowBad
  apply listMax_le
  intro x hx
  rcases List.mem_map.mp hx with ⟨line, hline, rfl⟩
  have hmem : line.budgetTotal ∈
      ledger.lines.map (fun current => current.budgetTotal) :=
    List.mem_map.mpr ⟨line, hline, rfl⟩
  exact Nat.le_trans line.bad_le_budgetTotal (by
    unfold rowBudgetSup
    exact le_listMax_of_mem hmem)

/-- The profile-count field is really row-uniform and remains separately
visible from the payment estimate. -/
theorem rowProfileCountSup_le_profileCap
    {compilerLoss profileCap envelope : Nat}
    (ledger : UniformClosedLedger compilerLoss profileCap envelope) :
    ledger.rowProfileCountSup ≤ profileCap := by
  unfold rowProfileCountSup
  apply listMax_le
  intro x hx
  rcases List.mem_map.mp hx with ⟨line, hline, rfl⟩
  exact line.profileCountControl

/-- Pointwise line-local natural-scale control bounds the correct outer
supremum. -/
theorem rowNaturalSup_le_envelope
    {compilerLoss profileCap envelope : Nat}
    (ledger : UniformClosedLedger compilerLoss profileCap envelope) :
    ledger.rowNaturalSup ≤ envelope := by
  unfold rowNaturalSup
  apply listMax_le
  intro x hx
  rcases List.mem_map.mp hx with ⟨line, hline, rfl⟩
  exact ledger.windowUniformity line hline

/-- `sup_line sum_profile U(line, profile)` is bounded without interchanging
the line supremum and profile sum. -/
theorem rowBudgetSup_le_loss_mul_rowNaturalSup
    {compilerLoss profileCap envelope : Nat}
    (ledger : UniformClosedLedger compilerLoss profileCap envelope) :
    ledger.rowBudgetSup ≤ compilerLoss * ledger.rowNaturalSup := by
  unfold rowBudgetSup
  apply listMax_le
  intro x hx
  rcases List.mem_map.mp hx with ⟨line, hline, rfl⟩
  have hmem : line.naturalTotal ∈
      ledger.lines.map (fun current => current.naturalTotal) :=
    List.mem_map.mpr ⟨line, hline, rfl⟩
  have hscale : line.naturalTotal ≤ ledger.rowNaturalSup := by
    unfold rowNaturalSup
    exact le_listMax_of_mem hmem
  exact Nat.le_trans line.budgetTotal_le_loss_mul_naturalTotal
    (Nat.mul_le_mul_left compilerLoss hscale)

/-- `sup_line bad(line) <= loss * sup_line sum_profile scale(line, profile)`. -/
theorem rowBad_le_loss_mul_rowNaturalSup
    {compilerLoss profileCap envelope : Nat}
    (ledger : UniformClosedLedger compilerLoss profileCap envelope) :
    ledger.rowBad ≤ compilerLoss * ledger.rowNaturalSup :=
  Nat.le_trans ledger.rowBad_le_rowBudgetSup
    ledger.rowBudgetSup_le_loss_mul_rowNaturalSup

/-- Minimal closed-ledger / `(UNIF)` compiler theorem.  The proof deliberately
passes through `sup_line sum_profile U(line, profile)`. -/
theorem compile {compilerLoss profileCap envelope : Nat}
    (ledger : UniformClosedLedger compilerLoss profileCap envelope) :
    ledger.rowBad ≤ compilerLoss * envelope := by
  calc
    ledger.rowBad ≤ ledger.rowBudgetSup := ledger.rowBad_le_rowBudgetSup
    _ ≤ compilerLoss * ledger.rowNaturalSup :=
      ledger.rowBudgetSup_le_loss_mul_rowNaturalSup
    _ ≤ compilerLoss * envelope :=
      Nat.mul_le_mul_left compilerLoss ledger.rowNaturalSup_le_envelope

/-- Target-facing finite wrapper.  The target comparison is explicit and is
not manufactured by the compiler. -/
theorem compile_to_target {compilerLoss profileCap envelope target : Nat}
    (ledger : UniformClosedLedger compilerLoss profileCap envelope)
    (hTarget : compilerLoss * envelope ≤ target) :
    ledger.rowBad ≤ target :=
  Nat.le_trans ledger.compile hTarget

end UniformClosedLedger

/-! ## Supremum/sum order regression -/

/-- Total budget on each received line, followed by the finite supremum. -/
def linewiseSupSum (matrix : List (List Nat)) : Nat :=
  listMax (matrix.map listSum)

/-- Read a column entry, padding a short row by zero. -/
def getOrZero : List Nat → Nat → Nat
  | [], _ => 0
  | x :: _, 0 => x
  | _ :: xs, Nat.succ j => getOrZero xs j

/-- Supremum over lines for one fixed profile column. -/
def profileSup (matrix : List (List Nat)) (j : Nat) : Nat :=
  listMax (matrix.map (fun row => getOrZero row j))

/-- Sum of independently maximized profile columns.  This is generally the
wrong quantity for `(UNIF)`. -/
def profilewiseSumSup (matrix : List (List Nat)) (profiles : List Nat) : Nat :=
  listSum (profiles.map (profileSup matrix))

/-- Smallest diagonal countermodel: two lines activate disjoint profiles.  The
required quantity is `sup_line sum_profile = 1`, while the lossy interchange
gives `sum_profile sup_line = 2`. -/
theorem sup_sum_interchange_falsifier :
    linewiseSupSum [[1, 0], [0, 1]] = 1 ∧
    profilewiseSumSup [[1, 0], [0, 1]] [0, 1] = 2 ∧
    linewiseSupSum [[1, 0], [0, 1]] <
      profilewiseSumSup [[1, 0], [0, 1]] [0, 1] := by
  decide

/-! ## Positive compiler fixture -/

/-- One already-paid C7 first-match profile, installed through the direct
adapter without pretending that it passed through a primitive Sidon theorem. -/
def fixtureProfile : ProfilePayment 1 :=
  ProfilePayment.ofDirect .c7 [3, 5] 2 1 (by decide) (by decide)

/-- One received line whose two bad slopes are exactly the assigned profile. -/
def fixtureLine : ClosedLineLedger 1 1 where
  badCount := 2
  profiles := [fixtureProfile]
  firstMatchOwnership := by decide
  atlasExhaustive := by decide
  profileCountControl := by decide

/-- The fixture's line-local envelope is `2`. -/
def fixtureLedger : UniformClosedLedger 1 1 2 where
  lines := [fixtureLine]
  windowUniformity := by
    intro line hline
    rcases List.mem_cons.mp hline with hEq | hNil
    · subst line
      decide
    · simp at hNil

/-- Replay the fixture through the general compiler rather than direct
computation. -/
theorem uniform_closed_ledger_fixture :
    fixtureLedger.rowBad ≤ 1 * 2 :=
  fixtureLedger.compile

#print axioms ProfilePayment.paidAtNaturalScale
#print axioms ProfilePayment.ofDirect
#print axioms listSum_map_const_mul
#print axioms ClosedLineLedger.bad_le_budgetTotal
#print axioms ClosedLineLedger.budgetTotal_le_loss_mul_naturalTotal
#print axioms ClosedLineLedger.bad_le_loss_mul_naturalTotal
#print axioms UniformClosedLedger.rowBad_le_rowBudgetSup
#print axioms UniformClosedLedger.rowProfileCountSup_le_profileCap
#print axioms UniformClosedLedger.rowNaturalSup_le_envelope
#print axioms UniformClosedLedger.rowBudgetSup_le_loss_mul_rowNaturalSup
#print axioms UniformClosedLedger.rowBad_le_loss_mul_rowNaturalSup
#print axioms UniformClosedLedger.compile
#print axioms UniformClosedLedger.compile_to_target
#print axioms sup_sum_interchange_falsifier
#print axioms uniform_closed_ledger_fixture

end AsymptoticSpine
