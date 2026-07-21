import Std

/-!
# Interior padding-bridge audit

A stdlib-only finite certificate for the audit of the Mersenne-31 list-row
`UNPAID_PADDING_BRIDGE` terminal.

The module checks one genuine Reed--Solomon instance over `F_11`.  The two
listed degree-`< 4` codewords and the received word are fixed.  Only the order
used by the canonical first-`a` selector changes.  The actual error-locator row
is unchanged, while the discarded-agreement padding changes whether the
minimal actual-error pair syzygy satisfies the coordinatewise divisibility
needed to become a syzygy of the canonical padded locators.

The polynomial-module diagonal-saturation identity is proved in the companion
research note.  Here Lean checks its exact finite root-mask premises, the pair
index arithmetic, and the deployed M31 degree barriers.
-/

namespace M31QRootedShell.PaddingBridgeAudit

/-- The control field order. -/
def prime : Nat := 11

/-- The nine evaluation points, in the first canonical order. -/
def naturalOrder : List Nat := List.range 9

/-- The same nine points, with a common agreement moved behind both pivots. -/
def commonPaddingOrder : List Nat := [0, 1, 3, 4, 5, 6, 7, 8, 2]

/-- Duplicate-free list predicate, kept executable and stdlib-only. -/
def noDuplicates : List Nat → Bool
  | [] => true
  | x :: xs => !xs.contains x && noDuplicates xs

/-- A valid ordered copy of the nine-point subset of `F_11`. -/
def validOrder (order : List Nat) : Bool :=
  order.length == 9 && noDuplicates order &&
    order.all fun x => decide (x < prime)

/-- Horner evaluation of a coefficient list modulo `11`. -/
def evalMod11 : List Nat → Nat → Nat
  | [], _ => 0
  | a :: coeffs, x => (a + x * evalMod11 coeffs x) % prime

/-- The zero codeword. -/
def zeroCodeword (_ : Nat) : Nat := 0

/-- The codeword `X(X-1)(X-2)`, with coefficients `[0,2,8,1]` modulo `11`. -/
def cubicCodeword (x : Nat) : Nat := evalMod11 [0, 2, 8, 1] x

/-- One received word on the common underlying nine-point domain. -/
def received : Nat → Nat
  | 0 => 0
  | 1 => 0
  | 2 => 0
  | 3 => 0
  | 4 => 0
  | 5 => 0
  | 6 => 10
  | 7 => 1
  | 8 => 6
  | _ => 0

/-- Agreement threshold `a=5`; the RS dimension is `K=4`. -/
def agreementThreshold : Nat := 5

/-- Canonical boundary radius `R=9-a=4`. -/
def radius : Nat := 4

/-- Ordered exact agreement set of a codeword. -/
def agreements (order : List Nat) (c : Nat → Nat) : List Nat :=
  order.filter fun x => received x == c x

/-- Ordered exact error set of a codeword. -/
def errors (order : List Nat) (c : Nat → Nat) : List Nat :=
  order.filter fun x => !(received x == c x)

/-- The first `a` agreements selected by the canonical selector. -/
def selected (order : List Nat) (c : Nat → Nat) : List Nat :=
  (agreements order c).take agreementThreshold

/-- Agreements discarded after the canonical first-`a` selection. -/
def padding (order : List Nat) (c : Nat → Nat) : List Nat :=
  (agreements order c).drop agreementThreshold

/-- Roots of the canonical boundary locator: the complement of `selected`. -/
def paddedRoots (order : List Nat) (c : Nat → Nat) : List Nat :=
  order.filter fun x => !(selected order c).contains x

/-- Ordered intersection for the duplicate-free certificate lists. -/
def inter (xs ys : List Nat) : List Nat := xs.filter fun x => ys.contains x

/-- Common roots of the two actual-error locators. -/
def actualCommonRoots (order : List Nat) : List Nat :=
  inter (errors order zeroCodeword) (errors order cubicCodeword)

/-- Common roots of the two canonical padded locators. -/
def paddedCommonRoots (order : List Nat) : List Nat :=
  inter (paddedRoots order zeroCodeword) (paddedRoots order cubicCodeword)

/-- Root-count formula for the primitive actual-error pair-syzygy degree. -/
def actualPairIndex (order : List Nat) : Nat :=
  (errors order zeroCodeword).length - (actualCommonRoots order).length

/-- Root-count formula for the primitive padded-locator pair-syzygy degree. -/
def paddedPairIndex (order : List Nat) : Nat :=
  (paddedRoots order zeroCodeword).length - (paddedCommonRoots order).length

/--
The minimal actual-error pair generator transports directly through the
coordinatewise padding map exactly when each column's padding roots are errors
of the other column.
-/
def minimalPairTransportable (order : List Nat) : Bool :=
  ((padding order zeroCodeword).all fun x =>
      (errors order cubicCodeword).contains x) &&
  ((padding order cubicCodeword).all fun x =>
      (errors order zeroCodeword).contains x)

/-- A typed root mask separating actual errors from discarded agreements. -/
structure RootMask where
  actual : List Nat
  padding : List Nat

/-- A root is common to the actual-error locators in every column. -/
def InActualCommon (columns : List RootMask) (x : Nat) : Prop :=
  ∀ column, column ∈ columns → x ∈ column.actual

/-- A root is common to every padded locator, with its status retained. -/
def InPaddedCommon (columns : List RootMask) (x : Nat) : Prop :=
  ∀ column, column ∈ columns → x ∈ column.actual ∨ x ∈ column.padding

/-- Actual common-error roots are always padded common roots. -/
theorem actualCommon_implies_paddedCommon
    {columns : List RootMask} {x : Nat}
    (h : InActualCommon columns x) : InPaddedCommon columns x := by
  intro column hcolumn
  exact Or.inl (h column hcolumn)

/-- Necessary degree equation for direct diagonal transport by degree-`d` paddings. -/
def DirectDegreeTransport (actualDegree paddingDegree : Nat) : Prop :=
  ∃ paddedDegree, actualDegree = paddedDegree + paddingDegree

/-- No nonzero row of degree below the padding degree can transport directly. -/
theorem no_direct_degree_transport_of_lt
    {actualDegree paddingDegree : Nat}
    (h : actualDegree < paddingDegree) :
    ¬ DirectDegreeTransport actualDegree paddingDegree := by
  intro htransport
  obtain ⟨paddedDegree, hdegree⟩ := htransport
  omega

-- Exact Reed--Solomon fixture -------------------------------------------------

theorem natural_order_valid : validOrder naturalOrder = true := by decide

theorem common_padding_order_valid : validOrder commonPaddingOrder = true := by decide

theorem cubic_values :
    naturalOrder.map cubicCodeword = [0, 0, 0, 6, 2, 5, 10, 1, 6] := by decide

theorem received_values :
    naturalOrder.map received = [0, 0, 0, 0, 0, 0, 10, 1, 6] := by decide

theorem natural_zero_agreements :
    agreements naturalOrder zeroCodeword = [0, 1, 2, 3, 4, 5] := by decide

theorem natural_cubic_agreements :
    agreements naturalOrder cubicCodeword = [0, 1, 2, 6, 7, 8] := by decide

theorem natural_zero_errors :
    errors naturalOrder zeroCodeword = [6, 7, 8] := by decide

theorem natural_cubic_errors :
    errors naturalOrder cubicCodeword = [3, 4, 5] := by decide

theorem both_codewords_are_interior_listed :
    agreementThreshold < (agreements naturalOrder zeroCodeword).length ∧
    agreementThreshold < (agreements naturalOrder cubicCodeword).length ∧
    (errors naturalOrder zeroCodeword).length < radius ∧
    (errors naturalOrder cubicCodeword).length < radius := by decide

/-- Reordering changes no received value, codeword, or actual-error locator. -/
theorem actual_error_frame_is_identical :
    errors naturalOrder zeroCodeword =
      errors commonPaddingOrder zeroCodeword ∧
    errors naturalOrder cubicCodeword =
      errors commonPaddingOrder cubicCodeword := by decide

-- Cross-error padding: the minimal actual pair row transports directly.

theorem cross_zero_selected :
    selected naturalOrder zeroCodeword = [0, 1, 2, 3, 4] := by decide

theorem cross_cubic_selected :
    selected naturalOrder cubicCodeword = [0, 1, 2, 6, 7] := by decide

theorem cross_zero_padding :
    padding naturalOrder zeroCodeword = [5] := by decide

theorem cross_cubic_padding :
    padding naturalOrder cubicCodeword = [8] := by decide

theorem cross_zero_padded_roots :
    paddedRoots naturalOrder zeroCodeword = [5, 6, 7, 8] := by decide

theorem cross_cubic_padded_roots :
    paddedRoots naturalOrder cubicCodeword = [3, 4, 5, 8] := by decide

theorem cross_actual_common_empty : actualCommonRoots naturalOrder = [] := by decide

theorem cross_padded_common_mixed :
    paddedCommonRoots naturalOrder = [5, 8] := by decide

theorem cross_minimal_pair_transports :
    minimalPairTransportable naturalOrder = true := by decide

theorem cross_pair_indices :
    actualPairIndex naturalOrder = 3 ∧ paddedPairIndex naturalOrder = 2 := by decide

-- Common-agreement padding: the same minimal actual pair row does not transport.

theorem common_zero_selected :
    selected commonPaddingOrder zeroCodeword = [0, 1, 3, 4, 5] := by decide

theorem common_cubic_selected :
    selected commonPaddingOrder cubicCodeword = [0, 1, 6, 7, 8] := by decide

theorem common_zero_padding :
    padding commonPaddingOrder zeroCodeword = [2] := by decide

theorem common_cubic_padding :
    padding commonPaddingOrder cubicCodeword = [2] := by decide

theorem common_zero_padded_roots :
    paddedRoots commonPaddingOrder zeroCodeword = [6, 7, 8, 2] := by decide

theorem common_cubic_padded_roots :
    paddedRoots commonPaddingOrder cubicCodeword = [3, 4, 5, 2] := by decide

theorem common_actual_common_empty :
    actualCommonRoots commonPaddingOrder = [] := by decide

theorem common_padded_common_is_discarded_agreement :
    paddedCommonRoots commonPaddingOrder = [2] := by decide

theorem common_minimal_pair_does_not_transport :
    minimalPairTransportable commonPaddingOrder = false := by decide

theorem common_pair_indices :
    actualPairIndex commonPaddingOrder = 3 ∧
    paddedPairIndex commonPaddingOrder = 3 := by decide

/--
The actual-error frame is identical, but the canonical padding bridge and the
padded pair index are not determined by it.
-/
theorem same_actual_frame_different_padding_bridge :
    actualPairIndex naturalOrder = actualPairIndex commonPaddingOrder ∧
    minimalPairTransportable naturalOrder = true ∧
    minimalPairTransportable commonPaddingOrder = false ∧
    paddedPairIndex naturalOrder ≠ paddedPairIndex commonPaddingOrder := by decide

-- Deployed M31 degree barriers -----------------------------------------------

/-- M31 list-row canonical boundary radius. -/
def m31Radius : Nat := 981129

/-- Uniform cap for the first certified actual-error Forney row. -/
def m31FirstIndexCap : Nat := 20765

/-- Uniform cap for each of the first three rows, from their total `62295`. -/
def m31ThreeIndexCap : Nat := 62295

/-- At or below this weight, padding degree is at least `20766`. -/
def m31FirstBlockedWeightMax : Nat := 960363

/-- At or below this weight, padding degree is at least `62296`. -/
def m31ThreeBlockedWeightMax : Nat := 918833

theorem m31_first_blocked_padding_degree (j : Nat)
    (hj : j ≤ m31FirstBlockedWeightMax) :
    20766 ≤ m31Radius - j := by
  simp only [m31FirstBlockedWeightMax, m31Radius] at hj ⊢
  omega

theorem m31_three_blocked_padding_degree (j : Nat)
    (hj : j ≤ m31ThreeBlockedWeightMax) :
    62296 ≤ m31Radius - j := by
  simp only [m31ThreeBlockedWeightMax, m31Radius] at hj ⊢
  omega

/-- The certified first actual-error row cannot directly transport in this band. -/
theorem m31_first_row_direct_transport_blocked
    (j actualDegree : Nat)
    (hj : j ≤ m31FirstBlockedWeightMax)
    (hdegree : actualDegree ≤ m31FirstIndexCap) :
    ¬ DirectDegreeTransport actualDegree (m31Radius - j) := by
  apply no_direct_degree_transport_of_lt
  have hpadding := m31_first_blocked_padding_degree j hj
  have hcap : actualDegree ≤ 20765 := by
    simpa only [m31FirstIndexCap] using hdegree
  omega

/-- None of the first three certified rows can directly transport in this band. -/
theorem m31_first_three_direct_transport_blocked
    (j actualDegree : Nat)
    (hj : j ≤ m31ThreeBlockedWeightMax)
    (hdegree : actualDegree ≤ m31ThreeIndexCap) :
    ¬ DirectDegreeTransport actualDegree (m31Radius - j) := by
  apply no_direct_degree_transport_of_lt
  have hpadding := m31_three_blocked_padding_degree j hj
  have hcap : actualDegree ≤ 62295 := by
    simpa only [m31ThreeIndexCap] using hdegree
  omega

/-- Blocked weight positions inside the current sharp arithmetic extremizer. -/
theorem arithmetic_extremizer_blocked_positions :
    m31ThreeBlockedWeightMax - 721249 + 1 = 197585 := by decide

end M31QRootedShell.PaddingBridgeAudit
