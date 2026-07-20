import AsymptoticSpine.PrefixAtlas
import AsymptoticSpine.UniformClosedLedger

namespace AsymptoticSpine

/-!
# High-redundancy simple-pole C9 direct-slope producer

For one actual post-C1--C8 simple-pole boundary profile, choose one rooted
support/polynomial witness for every distinct surviving slope.  Exact
prefix-list uniqueness makes the representative supports distinct.  Their
incidence vectors lie in one weighted-Vandermonde syndrome fibre, so the MDS
kernel distance gives the source-side ordered-pair inequality

`|Gamma| * (2 * R + 2 - N) <= 2 * (R + 1)`.

This module begins at that proved direct-slope inequality.  It does not replace
slopes by the size of the entire support fibre: `rawSlopes` is the actual slope
image of the rooted witness catalogue, and the inequality is stated directly
for that duplicate-free image.  Earlier C1--C8 slope owners are deleted before
payment.  When `2 * R + 2 > N`, the surviving slope count is at most the
polynomial loss `2 * (R + 1)`, hence is paid by the additive unit term of its
natural profile scale through `ProfilePayment.ofDirect`.

The sharp source theorem is

`|Gamma| <= floor (2 * (R + 1) / (2 * R + 2 - N))`.

The finite adapter deliberately keeps the denominator-cleared inequality and
uses the coarser polynomial loss, avoiding any hidden division convention.  No
row-complete atlas, survivor nonemptiness, general C9 Sidon/MI--MA theorem, or
row-wide `(UNIF)` is asserted.
-/

/-- Rooted source boundary for one high-redundancy simple-pole C9 profile.

`witnesses` enumerate actual support/polynomial witness states in one boundary
fibre; `slope` is their final MCA slope.  `directSlopePairCount` is the direct
MDS two-symbol pair count applied to one representative for each distinct raw
slope.  It is not a max-fibre or support-count hypothesis. -/
structure C9HighRedundancySimplePoleClass where
  witnesses : List Nat
  witnesses_nodup : witnesses.Nodup
  slope : Nat -> Nat
  N : Nat
  R : Nat
  R_le_N : R <= N
  gap_pos : 0 < 2 * R + 2 - N
  directSlopePairCount :
    (realizedKeys witnesses slope).length * (2 * R + 2 - N) <=
      2 * (R + 1)

namespace C9HighRedundancySimplePoleClass

/-- Distinct raw slopes realized by the rooted witness catalogue. -/
def rawSlopes (data : C9HighRedundancySimplePoleClass) : List Nat :=
  realizedKeys data.witnesses data.slope

/-- Positive high-redundancy gap in the pair-count theorem. -/
def gap (data : C9HighRedundancySimplePoleClass) : Nat :=
  2 * data.R + 2 - data.N

/-- Subexponential finite compiler loss used by the direct adapter. -/
def paymentLoss (data : C9HighRedundancySimplePoleClass) : Nat :=
  2 * (data.R + 1)

/-- The raw slope image is duplicate-free by construction. -/
theorem rawSlopes_nodup (data : C9HighRedundancySimplePoleClass) :
    data.rawSlopes.Nodup := by
  exact realizedKeys_nodup data.slope data.witnesses

/-- The constructed list is exactly the slope image of the rooted witnesses. -/
theorem mem_rawSlopes_iff_mem_witnessSlopeImage
    (data : C9HighRedundancySimplePoleClass) (gamma : Nat) :
    gamma ∈ data.rawSlopes <-> gamma ∈ data.witnesses.map data.slope := by
  exact mem_realizedKeys_iff data.witnesses data.slope gamma

/-- Actual C9 first-match slopes after deleting the aggregate C1--C8 slope
image on this received line. -/
def assignedSlopes (data : C9HighRedundancySimplePoleClass)
    (earlier : List Nat) : List Nat :=
  data.rawSlopes.filter fun gamma => decide (gamma ∉ earlier)

@[simp] theorem mem_assignedSlopes
    (data : C9HighRedundancySimplePoleClass) (earlier : List Nat)
    (gamma : Nat) :
    gamma ∈ data.assignedSlopes earlier <->
      gamma ∈ data.rawSlopes /\ gamma ∉ earlier := by
  simp [assignedSlopes]

/-- First-match deletion preserves duplicate-free slope ownership. -/
theorem assignedSlopes_nodup
    (data : C9HighRedundancySimplePoleClass) (earlier : List Nat) :
    (data.assignedSlopes earlier).Nodup := by
  exact List.filter_sublist.nodup data.rawSlopes_nodup

/-- Every surviving C9 slope remains rooted in an actual witness state and is
certified absent from the earlier C1--C8 slope image. -/
theorem assignedSlope_has_surviving_witness
    (data : C9HighRedundancySimplePoleClass) (earlier : List Nat)
    (gamma : Nat) (hgamma : gamma ∈ data.assignedSlopes earlier) :
    exists w, w ∈ data.witnesses /\ data.slope w = gamma /\
      gamma ∉ earlier := by
  have hassigned := (mem_assignedSlopes data earlier gamma).mp hgamma
  have hwimage :=
    (mem_rawSlopes_iff_mem_witnessSlopeImage data gamma).mp hassigned.1
  rw [List.mem_map] at hwimage
  rcases hwimage with ⟨w, hw, hslope⟩
  exact ⟨w, hw, hslope, hassigned.2⟩

/-- Deletion cannot increase the actual distinct-slope image. -/
theorem assignedSlopes_length_le_raw
    (data : C9HighRedundancySimplePoleClass) (earlier : List Nat) :
    (data.assignedSlopes earlier).length <= data.rawSlopes.length := by
  simpa [assignedSlopes] using
    List.length_filter_le (fun gamma => decide (gamma ∉ earlier)) data.rawSlopes

/-- The direct MDS pair-count inequality survives arbitrary earlier deletion. -/
theorem assignedSlopes_mul_gap_le_paymentLoss
    (data : C9HighRedundancySimplePoleClass) (earlier : List Nat) :
    (data.assignedSlopes earlier).length * data.gap <= data.paymentLoss := by
  calc
    (data.assignedSlopes earlier).length * data.gap <=
        data.rawSlopes.length * data.gap :=
      Nat.mul_le_mul_right data.gap
        (assignedSlopes_length_le_raw data earlier)
    _ <= data.paymentLoss := by
      simpa [rawSlopes, gap, paymentLoss] using data.directSlopePairCount

/-- Positive gap converts the denominator-cleared pair count into the direct
polynomial distinct-slope payment used by the finite compiler. -/
theorem assignedSlopes_length_le_paymentLoss
    (data : C9HighRedundancySimplePoleClass) (earlier : List Nat) :
    (data.assignedSlopes earlier).length <= data.paymentLoss := by
  have hgapOne : 1 <= data.gap := by
    exact data.gap_pos
  calc
    (data.assignedSlopes earlier).length =
        (data.assignedSlopes earlier).length * 1 := by simp
    _ <= (data.assignedSlopes earlier).length * data.gap :=
      Nat.mul_le_mul_left (data.assignedSlopes earlier).length hgapOne
    _ <= data.paymentLoss :=
      assignedSlopes_mul_gap_le_paymentLoss data earlier

/-- The loss is at most `2 * (N + 1)`, so it is polynomial in the active
coordinate count. -/
theorem paymentLoss_le_two_mul_N_succ
    (data : C9HighRedundancySimplePoleClass) :
    data.paymentLoss <= 2 * (data.N + 1) := by
  unfold paymentLoss
  exact Nat.mul_le_mul_left 2 (Nat.add_le_add_right data.R_le_N 1)

/-- One post-deletion C9 profile, paid directly on its actual assigned slope
list at unit natural scale. -/
def profile (data : C9HighRedundancySimplePoleClass)
    (earlier : List Nat) : ProfilePayment data.paymentLoss :=
  ProfilePayment.ofDirect .c9 (data.assignedSlopes earlier) 1 data.paymentLoss
    (data.assignedSlopes_nodup earlier)
    (by simpa using data.assignedSlopes_length_le_paymentLoss earlier)

@[simp] theorem profile_assignedSlopes
    (data : C9HighRedundancySimplePoleClass) (earlier : List Nat) :
    (data.profile earlier).assignedSlopes = data.assignedSlopes earlier := rfl

/-- Empty post-deletion cells are not installed as realized profiles. -/
def profiles (data : C9HighRedundancySimplePoleClass)
    (earlier : List Nat) : List (ProfilePayment data.paymentLoss) :=
  if data.assignedSlopes earlier = [] then [] else [data.profile earlier]

/-- The installed profile family has exactly the assigned C9 slope image. -/
theorem profiles_flatten_assignedSlopes
    (data : C9HighRedundancySimplePoleClass) (earlier : List Nat) :
    ((data.profiles earlier).map
      (fun p => p.assignedSlopes)).flatten = data.assignedSlopes earlier := by
  unfold profiles
  split <;> simp_all

/-- At most one boundary profile is realized in this local producer. -/
theorem profiles_length_le_one
    (data : C9HighRedundancySimplePoleClass) (earlier : List Nat) :
    (data.profiles earlier).length <= 1 := by
  unfold profiles
  split <;> simp

/-- Closed line-local C9 producer.  `badCount` is only this post-C1--C8
assigned-slope contribution. -/
def line (data : C9HighRedundancySimplePoleClass) (earlier : List Nat) :
    ClosedLineLedger data.paymentLoss 1 where
  badCount := (data.assignedSlopes earlier).length
  profiles := data.profiles earlier
  firstMatchOwnership := by
    rw [profiles_flatten_assignedSlopes]
    exact data.assignedSlopes_nodup earlier
  atlasExhaustive := by
    rw [profiles_flatten_assignedSlopes]
    exact Nat.le_refl _
  profileCountControl := data.profiles_length_le_one earlier

/-- The local natural-profile sum is zero after total deletion and one
otherwise. -/
theorem line_naturalTotal_le_one
    (data : C9HighRedundancySimplePoleClass) (earlier : List Nat) :
    (data.line earlier).naturalTotal <= 1 := by
  unfold line profiles ClosedLineLedger.naturalTotal
  split <;> simp [profile, ProfilePayment.ofDirect]

/-- The local ray budget is bounded by the direct polynomial loss. -/
theorem line_budgetTotal_le_paymentLoss
    (data : C9HighRedundancySimplePoleClass) (earlier : List Nat) :
    (data.line earlier).budgetTotal <= data.paymentLoss := by
  unfold line profiles ClosedLineLedger.budgetTotal
  split <;> simp [profile, ProfilePayment.ofDirect]

/-- One-line wrapper preserving the required sum-inside-line order. -/
def ledger (data : C9HighRedundancySimplePoleClass) (earlier : List Nat) :
    UniformClosedLedger data.paymentLoss 1 1 where
  lines := [data.line earlier]
  windowUniformity := by
    intro current hcurrent
    rcases List.mem_cons.mp hcurrent with hEq | hNil
    · subst current
      exact data.line_naturalTotal_le_one earlier
    · simp at hNil

/-- Rooted direct-slope C9 producer theorem. -/
theorem ledger_compiles
    (data : C9HighRedundancySimplePoleClass) (earlier : List Nat) :
    (data.ledger earlier).rowBad <= data.paymentLoss := by
  simpa using (data.ledger earlier).compile

/-- Executable high-redundancy fixture: `N=10`, `R=6`, gap `4`; three raw
slopes satisfy `3*4 <= 14`, and one earlier-owned slope is deleted. -/
def fixture : C9HighRedundancySimplePoleClass where
  witnesses := [0, 1, 2]
  witnesses_nodup := by decide
  slope := fun w => w + 100
  N := 10
  R := 6
  R_le_N := by decide
  gap_pos := by decide
  directSlopePairCount := by decide

 theorem fixture_rawSlopes : fixture.rawSlopes = [100, 101, 102] := by
  decide

 theorem fixture_assignedSlopes :
    fixture.assignedSlopes [100] = [101, 102] := by
  decide

 theorem fixture_compiles :
    (fixture.ledger [100]).rowBad <= fixture.paymentLoss :=
  fixture.ledger_compiles [100]

#print axioms rawSlopes_nodup
#print axioms mem_rawSlopes_iff_mem_witnessSlopeImage
#print axioms assignedSlope_has_surviving_witness
#print axioms assignedSlopes_mul_gap_le_paymentLoss
#print axioms assignedSlopes_length_le_paymentLoss
#print axioms paymentLoss_le_two_mul_N_succ
#print axioms profiles_flatten_assignedSlopes
#print axioms line_naturalTotal_le_one
#print axioms line_budgetTotal_le_paymentLoss
#print axioms ledger_compiles
#print axioms fixture_compiles

end C9HighRedundancySimplePoleClass
end AsymptoticSpine
