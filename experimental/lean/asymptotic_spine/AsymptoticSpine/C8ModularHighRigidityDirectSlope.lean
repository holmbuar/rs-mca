import AsymptoticSpine.PrefixAtlas
import AsymptoticSpine.UniformClosedLedger

namespace AsymptoticSpine

/-!
# Root-free modular-locator C8 producer in the positive Plotkin-gap regime

The source theorem
`bc_first_interior_modular_subset_product.md` identifies one root-free,
fixed-multiplier first-interior modular-locator fibre and proves that two
distinct supports in it exchange at least

`L = h + d + 1`

roots, where `d = deg W1` and `h` is the truncated-locator depth.  Choose one
rooted support/polynomial witness for every distinct final slope.  Exact
support-to-polynomial uniqueness makes the representative supports distinct.
The constant-weight Plotkin count then gives the direct slope inequality

`J * (N * L - m * (N - m)) <= N * L`,

where `J` is the number of distinct slopes, all supports have size `m`, and the
active domain has size `N`.

This module starts at that proved denominator-cleared slope inequality.  In the
positive-gap regime

`N * L > m * (N - m)`,

the actual post-C1--C7 slope image is paid directly at unit natural scale with
polynomial loss `N * L <= N^2`.  This is a direct distinct-slope theorem after
one representative per slope has been selected; the ledger does not install a
support-fibre size, pair moment, max-fibre estimate, or arbitrary fixed-chart
count.

The active deployed first-interior rows do not satisfy the positive Plotkin-gap
condition.  Their mixed-character/aggregate slope problem remains open.  No
row-wide `(UNIF)`, survivor nonemptiness, or target comparison is asserted.
-/

/-- Rooted source boundary for one actual root-free fixed-multiplier
modular-locator profile. -/
structure C8ModularHighRigidityClass where
  witnesses : List Nat
  witnesses_nodup : witnesses.Nodup
  slope : Nat -> Nat
  N : Nat
  m : Nat
  h : Nat
  d : Nat
  m_le_N : m <= N
  exchangeDepth_le_N : h + d + 1 <= N
  plotkinGap_pos :
    0 < N * (h + d + 1) - m * (N - m)
  directSlopePlotkin :
    (realizedKeys witnesses slope).length *
        (N * (h + d + 1) - m * (N - m)) <=
      N * (h + d + 1)

namespace C8ModularHighRigidityClass

/-- Distinct raw final slopes realized by the rooted modular witnesses. -/
def rawSlopes (data : C8ModularHighRigidityClass) : List Nat :=
  realizedKeys data.witnesses data.slope

/-- Exchange depth supplied by modular collision rigidity. -/
def exchangeDepth (data : C8ModularHighRigidityClass) : Nat :=
  data.h + data.d + 1

/-- Positive constant-weight Plotkin denominator. -/
def plotkinGap (data : C8ModularHighRigidityClass) : Nat :=
  data.N * data.exchangeDepth - data.m * (data.N - data.m)

/-- Polynomial direct-payment loss. -/
def paymentLoss (data : C8ModularHighRigidityClass) : Nat :=
  data.N * data.exchangeDepth

/-- The raw slope image is duplicate-free by construction. -/
theorem rawSlopes_nodup (data : C8ModularHighRigidityClass) :
    data.rawSlopes.Nodup := by
  exact realizedKeys_nodup data.slope data.witnesses

/-- The constructed raw list is exactly the rooted witness slope image. -/
theorem mem_rawSlopes_iff_mem_witnessSlopeImage
    (data : C8ModularHighRigidityClass) (gamma : Nat) :
    gamma ∈ data.rawSlopes <-> gamma ∈ data.witnesses.map data.slope := by
  exact mem_realizedKeys_iff data.witnesses data.slope gamma

/-- The source Plotkin gap is positive. -/
theorem plotkinGap_positive (data : C8ModularHighRigidityClass) :
    0 < data.plotkinGap := by
  simpa [plotkinGap, exchangeDepth] using data.plotkinGap_pos

/-- The direct loss is at most the quadratic active-domain scale. -/
theorem paymentLoss_le_N_sq (data : C8ModularHighRigidityClass) :
    data.paymentLoss <= data.N * data.N := by
  unfold paymentLoss exchangeDepth
  exact Nat.mul_le_mul_left data.N data.exchangeDepth_le_N

/-- Actual C8 first-match slopes after deleting the aggregate C1--C7 slope
image on the same received line. -/
def assignedSlopes (data : C8ModularHighRigidityClass)
    (earlier : List Nat) : List Nat :=
  data.rawSlopes.filter fun gamma => decide (gamma ∉ earlier)

@[simp] theorem mem_assignedSlopes
    (data : C8ModularHighRigidityClass) (earlier : List Nat)
    (gamma : Nat) :
    gamma ∈ data.assignedSlopes earlier <->
      gamma ∈ data.rawSlopes /\ gamma ∉ earlier := by
  simp [assignedSlopes]

/-- First-match deletion preserves duplicate-free slope ownership. -/
theorem assignedSlopes_nodup
    (data : C8ModularHighRigidityClass) (earlier : List Nat) :
    (data.assignedSlopes earlier).Nodup := by
  exact List.filter_sublist.nodup data.rawSlopes_nodup

/-- Every assigned slope remains rooted in an actual modular-locator witness. -/
theorem assignedSlope_has_surviving_witness
    (data : C8ModularHighRigidityClass) (earlier : List Nat)
    (gamma : Nat) (hgamma : gamma ∈ data.assignedSlopes earlier) :
    exists w, w ∈ data.witnesses /\ data.slope w = gamma /\
      gamma ∉ earlier := by
  have hassigned := (mem_assignedSlopes data earlier gamma).mp hgamma
  have hwimage :=
    (mem_rawSlopes_iff_mem_witnessSlopeImage data gamma).mp hassigned.1
  rw [List.mem_map] at hwimage
  rcases hwimage with ⟨w, hw, hslope⟩
  exact ⟨w, hw, hslope, hassigned.2⟩

/-- Deletion cannot enlarge the actual distinct-slope image. -/
theorem assignedSlopes_length_le_raw
    (data : C8ModularHighRigidityClass) (earlier : List Nat) :
    (data.assignedSlopes earlier).length <= data.rawSlopes.length := by
  simpa [assignedSlopes] using
    List.length_filter_le (fun gamma => decide (gamma ∉ earlier)) data.rawSlopes

/-- The denominator-cleared direct slope inequality survives arbitrary earlier
deletion. -/
theorem assignedSlopes_mul_plotkinGap_le_paymentLoss
    (data : C8ModularHighRigidityClass) (earlier : List Nat) :
    (data.assignedSlopes earlier).length * data.plotkinGap <=
      data.paymentLoss := by
  calc
    (data.assignedSlopes earlier).length * data.plotkinGap <=
        data.rawSlopes.length * data.plotkinGap :=
      Nat.mul_le_mul_right data.plotkinGap
        (assignedSlopes_length_le_raw data earlier)
    _ <= data.paymentLoss := by
      simpa [rawSlopes, plotkinGap, paymentLoss, exchangeDepth] using
        data.directSlopePlotkin

/-- Positive Plotkin gap converts the direct inequality into a polynomial slope
payment. -/
theorem assignedSlopes_length_le_paymentLoss
    (data : C8ModularHighRigidityClass) (earlier : List Nat) :
    (data.assignedSlopes earlier).length <= data.paymentLoss := by
  have hgapOne : 1 <= data.plotkinGap := data.plotkinGap_positive
  calc
    (data.assignedSlopes earlier).length =
        (data.assignedSlopes earlier).length * 1 := by simp
    _ <= (data.assignedSlopes earlier).length * data.plotkinGap :=
      Nat.mul_le_mul_left (data.assignedSlopes earlier).length hgapOne
    _ <= data.paymentLoss :=
      assignedSlopes_mul_plotkinGap_le_paymentLoss data earlier

/-- One post-deletion modular C8 profile paid directly on its actual assigned
slope image at unit natural scale. -/
def profile (data : C8ModularHighRigidityClass)
    (earlier : List Nat) : ProfilePayment data.paymentLoss :=
  ProfilePayment.ofDirect .c8 (data.assignedSlopes earlier) 1 data.paymentLoss
    (data.assignedSlopes_nodup earlier)
    (by simpa using data.assignedSlopes_length_le_paymentLoss earlier)

@[simp] theorem profile_assignedSlopes
    (data : C8ModularHighRigidityClass) (earlier : List Nat) :
    (data.profile earlier).assignedSlopes = data.assignedSlopes earlier := rfl

/-- Empty post-deletion modular cells are not installed. -/
def profiles (data : C8ModularHighRigidityClass)
    (earlier : List Nat) : List (ProfilePayment data.paymentLoss) :=
  if data.assignedSlopes earlier = [] then [] else [data.profile earlier]

/-- The installed profile family has exactly the assigned C8 slope image. -/
theorem profiles_flatten_assignedSlopes
    (data : C8ModularHighRigidityClass) (earlier : List Nat) :
    ((data.profiles earlier).map
      (fun p => p.assignedSlopes)).flatten = data.assignedSlopes earlier := by
  unfold profiles
  split <;> simp_all

/-- At most one fixed-multiplier modular profile is realized. -/
theorem profiles_length_le_one
    (data : C8ModularHighRigidityClass) (earlier : List Nat) :
    (data.profiles earlier).length <= 1 := by
  unfold profiles
  split <;> simp

/-- Closed line-local producer for the high-rigidity modular C8 class. -/
def line (data : C8ModularHighRigidityClass) (earlier : List Nat) :
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

/-- The local natural-profile sum is at most one. -/
theorem line_naturalTotal_le_one
    (data : C8ModularHighRigidityClass) (earlier : List Nat) :
    (data.line earlier).naturalTotal <= 1 := by
  unfold line profiles ClosedLineLedger.naturalTotal
  split <;> simp [profile, ProfilePayment.ofDirect]

/-- The local ray budget is bounded by the direct Plotkin loss. -/
theorem line_budgetTotal_le_paymentLoss
    (data : C8ModularHighRigidityClass) (earlier : List Nat) :
    (data.line earlier).budgetTotal <= data.paymentLoss := by
  unfold line profiles ClosedLineLedger.budgetTotal
  split <;> simp [profile, ProfilePayment.ofDirect]

/-- One-line wrapper preserving the required sum-inside-line order. -/
def ledger (data : C8ModularHighRigidityClass) (earlier : List Nat) :
    UniformClosedLedger data.paymentLoss 1 1 where
  lines := [data.line earlier]
  windowUniformity := by
    intro current hcurrent
    rcases List.mem_cons.mp hcurrent with hEq | hNil
    · subst current
      exact data.line_naturalTotal_le_one earlier
    · simp at hNil

/-- Rooted high-rigidity modular C8 producer theorem. -/
theorem ledger_compiles
    (data : C8ModularHighRigidityClass) (earlier : List Nat) :
    (data.ledger earlier).rowBad <= data.paymentLoss := by
  simpa using (data.ledger earlier).compile

/-- Executable mixed modular fixture: `N=10`, `m=5`, `h=d=1`, exchange depth
three, Plotkin gap five, and six distinct raw slopes saturating the direct
inequality `6*5 <= 30`. -/
def fixture : C8ModularHighRigidityClass where
  witnesses := [0, 1, 2, 3, 4, 5]
  witnesses_nodup := by decide
  slope := fun w => w + 100
  N := 10
  m := 5
  h := 1
  d := 1
  m_le_N := by decide
  exchangeDepth_le_N := by decide
  plotkinGap_pos := by decide
  directSlopePlotkin := by decide

 theorem fixture_rawSlopes :
    fixture.rawSlopes = [100, 101, 102, 103, 104, 105] := by
  decide

 theorem fixture_assignedSlopes :
    fixture.assignedSlopes [100, 103] = [101, 102, 104, 105] := by
  decide

 theorem fixture_compiles :
    (fixture.ledger [100, 103]).rowBad <= fixture.paymentLoss :=
  fixture.ledger_compiles [100, 103]

#print axioms rawSlopes_nodup
#print axioms mem_rawSlopes_iff_mem_witnessSlopeImage
#print axioms plotkinGap_positive
#print axioms paymentLoss_le_N_sq
#print axioms assignedSlope_has_surviving_witness
#print axioms assignedSlopes_mul_plotkinGap_le_paymentLoss
#print axioms assignedSlopes_length_le_paymentLoss
#print axioms profiles_flatten_assignedSlopes
#print axioms line_naturalTotal_le_one
#print axioms line_budgetTotal_le_paymentLoss
#print axioms ledger_compiles
#print axioms fixture_compiles

end C8ModularHighRigidityClass
end AsymptoticSpine
