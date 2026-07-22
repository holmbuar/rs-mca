import Std

/-!
# KoalaBear boundary-prefix Q shell compiler

This stdlib-only module formalizes the finite summation compiler used by
`kb_uq_boundary_prefix_tangent_rooted_shell_v1.md` and kernel-checks the
reported 18-digit ledger arithmetic.  It does not assume or prove the deployed
shell hypothesis, calculate the gigantic binomial quotient, identify the
semantic Q cell, or close the KoalaBear row.
-/

set_option autoImplicit false

namespace KbUqBoundaryPrefix

abbrev ShellRow := Nat × Nat

/-- Sum selected-support degrees/populations over a canonical shell table. -/
def degreeSum : List ShellRow → Nat
  | [] => 0
  | row :: rows => row.1 + degreeSum rows

/-- Sum ambient shell sizes. -/
def shellSum : List ShellRow → Nat
  | [] => 0
  | row :: rows => row.2 + shellSum rows

/-- Sum truncated excess above the additive intercept `b`. -/
def excessSum (b : Nat) : List ShellRow → Nat
  | [] => 0
  | row :: rows => (row.1 - b) + excessSum b rows

/-- Pointwise cross-multiplied shell hypothesis. -/
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

/-- Every shell population is bounded by its intercept plus truncated excess. -/
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
          simpa [Nat.mul_succ, Nat.add_assoc, Nat.add_comm,
            Nat.add_left_comm] using hadd

/-- Pointwise exact shell inequalities sum after cross multiplication. -/
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

/-- Convert a strict cross-multiplied packet bracket to a floor bound. -/
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

/-- Compiler for the tangent-zero-anchor branch, whose root is not selected. -/
theorem shellCompilerNoRoot
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

/-- Compiler for the column-far branch, with one selected support as root. -/
theorem shellCompilerWithRoot
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
    _ = 1 + b * shellCount + scaledFloor := by omega

-- Frozen row constants and packet arithmetic.
def basePrime : Nat := 2130706433
def domainSize : Nat := 2097152
def codeDimension : Nat := 1048576
def agreement : Nat := 1116048
def radius : Nat := 981104
def prefixDepth : Nat := 67471
def tangentMinimumExchange : Nat := 67473
def sparseShellCount : Nat := 913632
def budget : Nat := 274980728111395087
def paid : Nat := 981104
def reserve : Nat := 274980728110413983
def scaledFloorSeven : Nat := 400386212557
def sparseCap : Nat := 400388953453
def uniformCap : Nat := 400389155870
def remainingReserve : Nat := 274980327721258113

 theorem deployed_radius : domainSize - agreement = radius := by native_decide
 theorem deployed_prefix_depth : agreement - (codeDimension + 1) = prefixDepth := by
  native_decide
 theorem deployed_tangent_minimum : agreement - codeDimension + 1 =
    tangentMinimumExchange := by native_decide
 theorem deployed_sparse_shell_count :
    radius - tangentMinimumExchange + 1 = sparseShellCount := by native_decide
 theorem deployed_reserve : budget - paid = reserve := by native_decide
 theorem deployed_sparse_cap :
    3 * sparseShellCount + scaledFloorSeven = sparseCap := by native_decide
 theorem deployed_uniform_cap :
    1 + 3 * radius + scaledFloorSeven = uniformCap := by native_decide
 theorem deployed_pruning_dividend : uniformCap - sparseCap = 202417 := by
  native_decide
 theorem deployed_partial_total : paid + uniformCap = 400390136974 := by
  native_decide
 theorem deployed_remaining_reserve : reserve - uniformCap = remainingReserve := by
  native_decide
 theorem deployed_cap_fits : uniformCap ≤ reserve := by native_decide

-- Exact viable-window boundary checks from the independently replayed quotient.
def cMax : Nat := 4807520
def bAtCMax : Nat := 54192
def cMaxFloor : Nat := 274980674942031079

theorem deployed_window_corner :
    1 + bAtCMax * radius + cMaxFloor = 274980728110019048 := by
  native_decide

theorem deployed_window_corner_remaining :
    reserve - (1 + bAtCMax * radius + cMaxFloor) = 394935 := by
  native_decide

theorem deployed_next_b_fails :
    reserve < 1 + 54193 * radius + cMaxFloor := by native_decide

theorem deployed_next_b_excess :
    (1 + 54193 * radius + cMaxFloor) - reserve = 586169 := by
  native_decide

theorem deployed_next_c_fails :
    reserve < 274980732140061446 := by native_decide

theorem deployed_next_c_excess :
    274980732140061446 - reserve = 4029647463 := by native_decide

#print axioms shellCompilerNoRoot
#print axioms shellCompilerWithRoot
#print axioms deployed_uniform_cap
#print axioms deployed_window_corner

end KbUqBoundaryPrefix
