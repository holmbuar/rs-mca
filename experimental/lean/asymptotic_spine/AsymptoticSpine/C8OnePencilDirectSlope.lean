import AsymptoticSpine.PrefixAtlas
import AsymptoticSpine.UniformClosedLedger

namespace AsymptoticSpine

/-!
# Primitive one-parameter split-pencil C8 direct-slope producer

The source theorem `cor:bc-one-pencil` applies after tangent, common-support,
quotient, extension, degree-drop, and common-GCD branches have been removed.
Every residual bad slope injects into one projective locator parameter, and
every counted degree-`omega` split member has `omega - g` moving roots outside
the fixed `D`-part of degree `g`.  Since each moving domain point belongs to at
most one pencil parameter, the actual distinct-slope image satisfies

`|Gamma| * (omega - g) <= N - g`.

This module begins at that proved rooted slope-to-pencil incidence boundary.
It deletes the aggregate C1--C7 assigned-slope image, pays the surviving C8
slope list directly at unit natural profile scale with polynomial loss `N-g`,
and exposes the correct line-local profile sum through `UniformClosedLedger`.

The sharp source theorem is

`|Gamma| <= floor ((N - g) / (omega - g))`.

The finite adapter keeps the denominator-cleared inequality and uses the coarser
polynomial loss `N-g`.  No higher-dimensional chart exhaustion, survivor
nonemptiness, row-complete atlas, actual row-wide `(UNIF)`, or target comparison
is asserted.
-/

/-- Rooted source boundary for one actual C8 one-parameter split-pencil chart.

`witnesses` enumerate actual residual locator/explanation states in the chart;
`slope` is their final MCA slope; `parameterOfSlope` records the projective
pencil parameter selected by that slope.  The injection field is required only
on the realized raw slope image.  `directMovingRootIncidence` is the source
moving-root theorem stated directly for that distinct-slope image. -/
structure C8OnePencilClass where
  witnesses : List Nat
  witnesses_nodup : witnesses.Nodup
  slope : Nat -> Nat
  parameterOfSlope : Nat -> Nat
  parameterOfSlope_injective_on_raw :
    forall gamma1, gamma1 ∈ realizedKeys witnesses slope ->
      forall gamma2, gamma2 ∈ realizedKeys witnesses slope ->
        parameterOfSlope gamma1 = parameterOfSlope gamma2 -> gamma1 = gamma2
  N : Nat
  g : Nat
  omega : Nat
  omega_le_N : omega <= N
  g_lt_omega : g < omega
  directMovingRootIncidence :
    (realizedKeys witnesses slope).length * (omega - g) <= N - g

namespace C8OnePencilClass

/-- Distinct raw slopes realized by the rooted chart witnesses. -/
def rawSlopes (data : C8OnePencilClass) : List Nat :=
  realizedKeys data.witnesses data.slope

/-- Number of roots that move with the projective pencil parameter. -/
def movingRoots (data : C8OnePencilClass) : Nat :=
  data.omega - data.g

/-- Number of domain points available outside the fixed `D`-part. -/
def availableRoots (data : C8OnePencilClass) : Nat :=
  data.N - data.g

/-- Polynomial finite compiler loss used by the direct adapter. -/
def paymentLoss (data : C8OnePencilClass) : Nat :=
  data.availableRoots

/-- The raw slope image is duplicate-free by construction. -/
theorem rawSlopes_nodup (data : C8OnePencilClass) :
    data.rawSlopes.Nodup := by
  exact realizedKeys_nodup data.slope data.witnesses

/-- The constructed raw list is exactly the witness slope image. -/
theorem mem_rawSlopes_iff_mem_witnessSlopeImage
    (data : C8OnePencilClass) (gamma : Nat) :
    gamma ∈ data.rawSlopes <-> gamma ∈ data.witnesses.map data.slope := by
  exact mem_realizedKeys_iff data.witnesses data.slope gamma

/-- The source slope-to-pencil map is injective on the realized slope image. -/
theorem parameterOfSlope_injective_on_rawSlopes
    (data : C8OnePencilClass)
    (gamma1 : Nat) (hgamma1 : gamma1 ∈ data.rawSlopes)
    (gamma2 : Nat) (hgamma2 : gamma2 ∈ data.rawSlopes)
    (hparameter : data.parameterOfSlope gamma1 =
      data.parameterOfSlope gamma2) :
    gamma1 = gamma2 := by
  exact data.parameterOfSlope_injective_on_raw gamma1 hgamma1
    gamma2 hgamma2 hparameter

/-- The moving-root count is positive on a genuine moving pencil. -/
theorem movingRoots_pos (data : C8OnePencilClass) :
    0 < data.movingRoots := by
  exact Nat.sub_pos_of_lt data.g_lt_omega

/-- The polynomial payment loss is at most the domain size. -/
theorem paymentLoss_le_N (data : C8OnePencilClass) :
    data.paymentLoss <= data.N := by
  exact Nat.sub_le data.N data.g

/-- Actual C8 first-match slopes after deleting the aggregate C1--C7 slope
image on this received line. -/
def assignedSlopes (data : C8OnePencilClass)
    (earlier : List Nat) : List Nat :=
  data.rawSlopes.filter fun gamma => decide (gamma ∉ earlier)

@[simp] theorem mem_assignedSlopes
    (data : C8OnePencilClass) (earlier : List Nat) (gamma : Nat) :
    gamma ∈ data.assignedSlopes earlier <->
      gamma ∈ data.rawSlopes /\ gamma ∉ earlier := by
  simp [assignedSlopes]

/-- First-match deletion preserves duplicate-free slope ownership. -/
theorem assignedSlopes_nodup
    (data : C8OnePencilClass) (earlier : List Nat) :
    (data.assignedSlopes earlier).Nodup := by
  exact List.filter_sublist.nodup data.rawSlopes_nodup

/-- Every surviving C8 slope remains rooted in an actual chart witness and is
certified absent from the earlier C1--C7 slope image. -/
theorem assignedSlope_has_surviving_witness
    (data : C8OnePencilClass) (earlier : List Nat)
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
    (data : C8OnePencilClass) (earlier : List Nat) :
    (data.assignedSlopes earlier).length <= data.rawSlopes.length := by
  simpa [assignedSlopes] using
    List.length_filter_le (fun gamma => decide (gamma ∉ earlier)) data.rawSlopes

/-- The direct moving-root incidence inequality survives arbitrary earlier
deletion. -/
theorem assignedSlopes_mul_movingRoots_le_availableRoots
    (data : C8OnePencilClass) (earlier : List Nat) :
    (data.assignedSlopes earlier).length * data.movingRoots <=
      data.availableRoots := by
  calc
    (data.assignedSlopes earlier).length * data.movingRoots <=
        data.rawSlopes.length * data.movingRoots :=
      Nat.mul_le_mul_right data.movingRoots
        (assignedSlopes_length_le_raw data earlier)
    _ <= data.availableRoots := by
      simpa [rawSlopes, movingRoots, availableRoots] using
        data.directMovingRootIncidence

/-- Positive moving-root count converts the denominator-cleared incidence bound
into the direct polynomial distinct-slope payment. -/
theorem assignedSlopes_length_le_paymentLoss
    (data : C8OnePencilClass) (earlier : List Nat) :
    (data.assignedSlopes earlier).length <= data.paymentLoss := by
  have hmoveOne : 1 <= data.movingRoots := data.movingRoots_pos
  calc
    (data.assignedSlopes earlier).length =
        (data.assignedSlopes earlier).length * 1 := by simp
    _ <= (data.assignedSlopes earlier).length * data.movingRoots :=
      Nat.mul_le_mul_left (data.assignedSlopes earlier).length hmoveOne
    _ <= data.availableRoots :=
      assignedSlopes_mul_movingRoots_le_availableRoots data earlier
    _ = data.paymentLoss := rfl

/-- One post-deletion C8 profile, paid directly on the actual assigned slope
image at unit natural scale. -/
def profile (data : C8OnePencilClass)
    (earlier : List Nat) : ProfilePayment data.paymentLoss :=
  ProfilePayment.ofDirect .c8 (data.assignedSlopes earlier) 1 data.paymentLoss
    (data.assignedSlopes_nodup earlier)
    (by simpa using data.assignedSlopes_length_le_paymentLoss earlier)

@[simp] theorem profile_assignedSlopes
    (data : C8OnePencilClass) (earlier : List Nat) :
    (data.profile earlier).assignedSlopes = data.assignedSlopes earlier := rfl

/-- Empty post-deletion charts are not installed as realized profiles. -/
def profiles (data : C8OnePencilClass)
    (earlier : List Nat) : List (ProfilePayment data.paymentLoss) :=
  if data.assignedSlopes earlier = [] then [] else [data.profile earlier]

/-- The installed profile family has exactly the assigned C8 slope image. -/
theorem profiles_flatten_assignedSlopes
    (data : C8OnePencilClass) (earlier : List Nat) :
    ((data.profiles earlier).map
      (fun p => p.assignedSlopes)).flatten = data.assignedSlopes earlier := by
  unfold profiles
  split <;> simp_all

/-- At most one pencil profile is realized in this local producer. -/
theorem profiles_length_le_one
    (data : C8OnePencilClass) (earlier : List Nat) :
    (data.profiles earlier).length <= 1 := by
  unfold profiles
  split <;> simp

/-- Closed line-local C8 producer. `badCount` is only this post-C1--C7 residual
slope contribution. -/
def line (data : C8OnePencilClass) (earlier : List Nat) :
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
    (data : C8OnePencilClass) (earlier : List Nat) :
    (data.line earlier).naturalTotal <= 1 := by
  unfold line profiles ClosedLineLedger.naturalTotal
  split <;> simp [profile, ProfilePayment.ofDirect]

/-- The local ray budget is bounded by the direct moving-root loss. -/
theorem line_budgetTotal_le_paymentLoss
    (data : C8OnePencilClass) (earlier : List Nat) :
    (data.line earlier).budgetTotal <= data.paymentLoss := by
  unfold line profiles ClosedLineLedger.budgetTotal
  split <;> simp [profile, ProfilePayment.ofDirect]

/-- One-line wrapper preserving the required sum-inside-line order. -/
def ledger (data : C8OnePencilClass) (earlier : List Nat) :
    UniformClosedLedger data.paymentLoss 1 1 where
  lines := [data.line earlier]
  windowUniformity := by
    intro current hcurrent
    rcases List.mem_cons.mp hcurrent with hEq | hNil
    · subst current
      exact data.line_naturalTotal_le_one earlier
    · simp at hNil

/-- Rooted primitive one-pencil C8 producer theorem. -/
theorem ledger_compiles
    (data : C8OnePencilClass) (earlier : List Nat) :
    (data.ledger earlier).rowBad <= data.paymentLoss := by
  simpa using (data.ledger earlier).compile

/-- Executable moving-root fixture: `N=10`, fixed part `g=2`, locator degree
`omega=6`, hence four moving roots and eight available points. Two raw slopes
saturate the incidence bound; one earlier-owned slope is deleted. -/
def fixture : C8OnePencilClass where
  witnesses := [0, 1]
  witnesses_nodup := by decide
  slope := fun w => w + 100
  parameterOfSlope := fun gamma => gamma + 1000
  parameterOfSlope_injective_on_raw := by
    intro gamma1 _hgamma1 gamma2 _hgamma2 h
    exact Nat.add_right_cancel h
  N := 10
  g := 2
  omega := 6
  omega_le_N := by decide
  g_lt_omega := by decide
  directMovingRootIncidence := by decide

 theorem fixture_rawSlopes : fixture.rawSlopes = [100, 101] := by
  decide

 theorem fixture_assignedSlopes :
    fixture.assignedSlopes [100] = [101] := by
  decide

 theorem fixture_compiles :
    (fixture.ledger [100]).rowBad <= fixture.paymentLoss :=
  fixture.ledger_compiles [100]

#print axioms rawSlopes_nodup
#print axioms mem_rawSlopes_iff_mem_witnessSlopeImage
#print axioms parameterOfSlope_injective_on_rawSlopes
#print axioms movingRoots_pos
#print axioms paymentLoss_le_N
#print axioms assignedSlope_has_surviving_witness
#print axioms assignedSlopes_mul_movingRoots_le_availableRoots
#print axioms assignedSlopes_length_le_paymentLoss
#print axioms profiles_flatten_assignedSlopes
#print axioms line_naturalTotal_le_one
#print axioms line_budgetTotal_le_paymentLoss
#print axioms ledger_compiles
#print axioms fixture_compiles

end C8OnePencilClass
end AsymptoticSpine
