import Std

/-!
# Branch-sensitive rooted-shell compiler

A stdlib-only formalization of the finite summation compiler used by the
KoalaBear tangent-pruned boundary-prefix Q packet.

Each shell row is `(rootedDegree, ambientShellSize)`.  The local hypothesis is

`Q * (rootedDegree - b) <= c * ambientShellSize`.

Natural subtraction is exactly `max(rootedDegree-b,0)`.  The anchored compiler
models the column-far branch, where one selected Q slope is the root.  The
anchor-free compiler models the non-column-far sparse branch after tangent
deletion puts every survivor into a positive-distance source shell.
-/

set_option autoImplicit false

namespace KbUqBoundaryPrefix

abbrev ShellRow := Nat × Nat

/-- Sum the rooted degrees in a shell table. -/
def degreeSum : List ShellRow → Nat
  | [] => 0
  | row :: rows => row.1 + degreeSum rows

/-- Sum the ambient shell sizes in a shell table. -/
def shellSum : List ShellRow → Nat
  | [] => 0
  | row :: rows => row.2 + shellSum rows

/-- Sum the rooted excess above the additive intercept `b`. -/
def excessSum (b : Nat) : List ShellRow → Nat
  | [] => 0
  | row :: rows => (row.1 - b) + excessSum b rows

/-- Pointwise rooted-shell hypothesis. -/
def LocalEnvelope (Q b c : Nat) : List ShellRow → Prop
  | [] => True
  | row :: rows =>
      Q * (row.1 - b) ≤ c * row.2 ∧ LocalEnvelope Q b c rows

@[simp] theorem degreeSum_nil : degreeSum [] = 0 := rfl
@[simp] theorem degreeSum_cons (row : ShellRow) (rows : List ShellRow) :
    degreeSum (row :: rows) = row.1 + degreeSum rows := rfl

@[simp] theorem shellSum_nil : shellSum [] = 0 := rfl
@[simp] theorem shellSum_cons (row : ShellRow) (rows : List ShellRow) :
    shellSum (row :: rows) = row.2 + shellSum rows := rfl

@[simp] theorem excessSum_nil (b : Nat) : excessSum b [] = 0 := rfl
@[simp] theorem excessSum_cons (b : Nat) (row : ShellRow) (rows : List ShellRow) :
    excessSum b (row :: rows) = (row.1 - b) + excessSum b rows := rfl

/-- Every rooted degree is at most the intercept plus its truncated excess. -/
theorem degreeSum_le_intercept_add_excess (b : Nat) :
    ∀ rows : List ShellRow,
      degreeSum rows ≤ b * rows.length + excessSum b rows := by
  intro rows
  induction rows with
  | nil => simp
  | cons row rows ih =>
      cases row with
      | mk d h =>
          have hd : d ≤ b + (d - b) := by omega
          have hadd := Nat.add_le_add hd ih
          simpa [Nat.mul_succ, Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using hadd

/-- Pointwise local shell bounds sum after exact cross multiplication. -/
theorem localEnvelope_mul_le (Q b c : Nat) :
    ∀ rows : List ShellRow,
      LocalEnvelope Q b c rows →
        Q * excessSum b rows ≤ c * shellSum rows := by
  intro rows
  induction rows with
  | nil => intro _; simp
  | cons row rows ih =>
      cases row with
      | mk d h =>
          intro hlocal
          have hhead : Q * (d - b) ≤ c * h := hlocal.1
          have htail : LocalEnvelope Q b c rows := hlocal.2
          have hrest := ih htail
          simpa [Nat.mul_add] using Nat.add_le_add hhead hrest

/-- Convert a strict cross-multiplied packet bracket into a floor bound. -/
theorem excessSum_le_scaledFloor
    (rows : List ShellRow) (Q b c totalShell scaledFloor : Nat)
    (hlocal : LocalEnvelope Q b c rows)
    (htotal : shellSum rows ≤ totalShell)
    (hfloor : c * totalShell < Q * (scaledFloor + 1)) :
    excessSum b rows ≤ scaledFloor := by
  have hlocalMul : Q * excessSum b rows ≤ c * shellSum rows :=
    localEnvelope_mul_le Q b c rows hlocal
  have htotalMul : c * shellSum rows ≤ c * totalShell :=
    Nat.mul_le_mul_left c htotal
  have hmul : Q * excessSum b rows ≤ c * totalShell :=
    Nat.le_trans hlocalMul htotalMul
  have hlt : Q * excessSum b rows < Q * (scaledFloor + 1) :=
    Nat.lt_of_le_of_lt hmul hfloor
  have hQ : 0 < Q := by
    cases Q with
    | zero => simp at hfloor
    | succ q => exact Nat.succ_pos q
  have hexcessLt : excessSum b rows < scaledFloor + 1 :=
    (Nat.mul_lt_mul_left hQ).mp hlt
  omega

/--
Anchored rooted-shell envelope.  The leading `1` is the selected column-far
anchor slope.
-/
theorem rootedShellEnvelopeAnchored
    (rows : List ShellRow)
    (familyCard shellCount Q b c totalShell scaledFloor : Nat)
    (hfamily : familyCard ≤ 1 + degreeSum rows)
    (hshellCount : rows.length ≤ shellCount)
    (hlocal : LocalEnvelope Q b c rows)
    (htotal : shellSum rows ≤ totalShell)
    (hfloor : c * totalShell < Q * (scaledFloor + 1)) :
    familyCard ≤ 1 + b * shellCount + scaledFloor := by
  have hdegree := degreeSum_le_intercept_add_excess b rows
  have hexcess := excessSum_le_scaledFloor rows Q b c totalShell scaledFloor
    hlocal htotal hfloor
  have hcount : b * rows.length ≤ b * shellCount :=
    Nat.mul_le_mul_left b hshellCount
  calc
    familyCard ≤ 1 + degreeSum rows := hfamily
    _ ≤ 1 + (b * rows.length + excessSum b rows) :=
      Nat.add_le_add_left hdegree 1
    _ ≤ 1 + (b * shellCount + scaledFloor) :=
      Nat.add_le_add_left (Nat.add_le_add hcount hexcess) 1
    _ = 1 + b * shellCount + scaledFloor := by
      simp [Nat.add_assoc]

/--
Anchor-free rooted-shell envelope.  This is the sparse branch after tangent
deletion proves that every survivor lies in a positive-distance source shell.
-/
theorem rootedShellEnvelopePruned
    (rows : List ShellRow)
    (familyCard shellCount Q b c totalShell scaledFloor : Nat)
    (hfamily : familyCard ≤ degreeSum rows)
    (hshellCount : rows.length ≤ shellCount)
    (hlocal : LocalEnvelope Q b c rows)
    (htotal : shellSum rows ≤ totalShell)
    (hfloor : c * totalShell < Q * (scaledFloor + 1)) :
    familyCard ≤ b * shellCount + scaledFloor := by
  have hdegree := degreeSum_le_intercept_add_excess b rows
  have hexcess := excessSum_le_scaledFloor rows Q b c totalShell scaledFloor
    hlocal htotal hfloor
  have hcount : b * rows.length ≤ b * shellCount :=
    Nat.mul_le_mul_left b hshellCount
  calc
    familyCard ≤ degreeSum rows := hfamily
    _ ≤ b * rows.length + excessSum b rows := hdegree
    _ ≤ b * shellCount + scaledFloor := Nat.add_le_add hcount hexcess

/-- A family above the anchored packet bound violates a local shell inequality. -/
theorem localEnvelope_fails_of_large_anchored_family
    (rows : List ShellRow)
    (familyCard shellCount Q b c totalShell scaledFloor : Nat)
    (hfamily : familyCard ≤ 1 + degreeSum rows)
    (hshellCount : rows.length ≤ shellCount)
    (htotal : shellSum rows ≤ totalShell)
    (hfloor : c * totalShell < Q * (scaledFloor + 1))
    (hlarge : 1 + b * shellCount + scaledFloor < familyCard) :
    ¬ LocalEnvelope Q b c rows := by
  intro hlocal
  have hbound := rootedShellEnvelopeAnchored rows familyCard shellCount Q b c
    totalShell scaledFloor hfamily hshellCount hlocal htotal hfloor
  exact (Nat.not_lt_of_ge hbound) hlarge

/-- A family above the pruned packet bound violates a local shell inequality. -/
theorem localEnvelope_fails_of_large_pruned_family
    (rows : List ShellRow)
    (familyCard shellCount Q b c totalShell scaledFloor : Nat)
    (hfamily : familyCard ≤ degreeSum rows)
    (hshellCount : rows.length ≤ shellCount)
    (htotal : shellSum rows ≤ totalShell)
    (hfloor : c * totalShell < Q * (scaledFloor + 1))
    (hlarge : b * shellCount + scaledFloor < familyCard) :
    ¬ LocalEnvelope Q b c rows := by
  intro hlocal
  have hbound := rootedShellEnvelopePruned rows familyCard shellCount Q b c
    totalShell scaledFloor hfamily hshellCount hlocal htotal hfloor
  exact (Nat.not_lt_of_ge hbound) hlarge

#print axioms degreeSum_le_intercept_add_excess
#print axioms localEnvelope_mul_le
#print axioms excessSum_le_scaledFloor
#print axioms rootedShellEnvelopeAnchored
#print axioms rootedShellEnvelopePruned
#print axioms localEnvelope_fails_of_large_anchored_family
#print axioms localEnvelope_fails_of_large_pruned_family

end KbUqBoundaryPrefix
