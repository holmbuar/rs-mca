import AsymptoticSpine.PrefixAtlas
import AsymptoticSpine.HighKappaCoverage

namespace AsymptoticSpine

/-!
# Actual first-match C8 charts at the finite spine calibration

This stdlib-only module constructs the finite C8 chart atlas used by the
asymptotic-spine calibration.  It imports only integrated APIs.  In particular,
it does not import the open C8 shallow producer or the open high-kappa owner
compiler.

The calibration begins from four raw chart slope projections.  Applying the
integrated `firstMatchLeaves` construction produces the exact post-deletion
slope cells.  A fixed semantic classifier then places every realized chart in
exactly one of four buckets:

1. an earlier C1--C7 semantic owner;
2. the supplied shallow closure input, field-for-field identical to the input
   shape consumed by the C8 producer;
3. a genuine one-parameter chart carrying a moving-root incidence certificate;
4. one explicitly named deep higher-dimensional residual.

The flattened post-deletion slope cells are proved duplicate-free.  The deep
class is named and enumerated but never paid.  No MI/MA, primitive Q/SP, curve
compiler, or direct higher-dimensional ray theorem is inserted implicitly.
-/

/-- Semantic owners preceding C8 in the first-match chronology. -/
inductive C8EarlierOwner where
  | c1 | c2 | c3 | c4 | c5 | c6 | c7
  deriving DecidableEq, Repr

/-- The four mutually exclusive C8 route-cut terminals. -/
inductive C8ChartBucket where
  | earlier
  | shallow
  | boundedPencil
  | deepResidual
  deriving DecidableEq, Repr

/-- Fixed bucket order. -/
def c8ChartBuckets : List C8ChartBucket :=
  [.earlier, .shallow, .boundedPencil, .deepResidual]

/-- The fixed bucket order is duplicate-free. -/
theorem c8ChartBuckets_nodup : c8ChartBuckets.Nodup := by
  decide

/-- Every bucket constructor occurs in the fixed order. -/
theorem mem_c8ChartBuckets (bucket : C8ChartBucket) :
    bucket ∈ c8ChartBuckets := by
  cases bucket <;> decide

/-! ## Field-for-field restatement of the supplied shallow producer input -/

/-- One supplied post-C1--C7 C8 residual chart in the shallow-prefix closure
regime.  The fields deliberately match the open producer's `ProfileData` input:
reindexed prefix-fibre bridge, effective key, `(SE2)` certificate, chart
inclusion, shallow closure bounds, and a kernel-dimension label. -/
structure C8ShallowClosureInput (Support Eff Raw : Type)
    [DecidableEq Eff] [DecidableEq Raw] where
  bridge : PrefixFiberBridge Support Eff Raw
  syndromeKey : Eff
  slopeCell : SE2Certificate Support Nat
  chartInclusion : List.Sublist slopeCell.supports
    (bridge.depthPrefixChart (bridge.toPrefix syndromeKey))
  bounds : ShallowPrefixClosureBounds bridge.fullSlice.length
  kernelDim : Nat

namespace C8ShallowClosureInput

/-- Exact finite loss furnished by the shallow effective-span bound. -/
def compilerLoss
    {Support Eff Raw : Type} [DecidableEq Eff] [DecidableEq Raw]
    (data : C8ShallowClosureInput Support Eff Raw) : Nat :=
  data.bounds.baseSize ^ data.bounds.prefixDepth

/-- Natural scale of the supplied shallow chart. -/
def naturalScale
    {Support Eff Raw : Type} [DecidableEq Eff] [DecidableEq Raw]
    (data : C8ShallowClosureInput Support Eff Raw) : Nat :=
  1 + data.bounds.average

/-- The integrated shallow closure theorem pays the actual post-deletion slope
list carried by the supplied `(SE2)` certificate. -/
theorem slopes_paid
    {Support Eff Raw : Type} [DecidableEq Eff] [DecidableEq Raw]
    (data : C8ShallowClosureInput Support Eff Raw) :
    data.slopeCell.slopes.length ≤ data.compilerLoss * data.naturalScale := by
  have h := balancedCoreShallowClosure_to_directRC data.bridge data.syndromeKey
    data.slopeCell data.chartInclusion data.bounds data.kernelDim
  simpa [compilerLoss, naturalScale, KernelIndependentDirectRC, DirectRC] using h

end C8ShallowClosureInput

/-! ## Exact finite moving-root payment interface -/

/-- A genuine one-parameter chart together with the division-free incidence
certificate used by `thm:bc-moving-root` / `cor:bc-one-pencil`.

The certificate stores the actual duplicate-free post-deletion slope list.  It
does not assert that an arbitrary chart is a pencil; that semantic fact is an
external construction obligation. -/
structure C8MovingRootCertificate where
  slopes : List Nat
  slopes_nodup : slopes.Nodup
  movingPoints : Nat
  movingRootsPerSlope : Nat
  movingRoots_pos : 0 < movingRootsPerSlope
  incidenceBound : slopes.length * movingRootsPerSlope ≤ movingPoints

namespace C8MovingRootCertificate

/-- If three counted slopes would require more moving-root incidences than are
available, the actual post-deletion chart has at most two slopes. -/
theorem slopes_length_le_two_of_three_mul_gt
    (certificate : C8MovingRootCertificate)
    (hthree : certificate.movingPoints <
      3 * certificate.movingRootsPerSlope) :
    certificate.slopes.length ≤ 2 := by
  by_cases hle : certificate.slopes.length ≤ 2
  · exact hle
  · have hcount : 3 ≤ certificate.slopes.length := by
      omega
    have hmul : 3 * certificate.movingRootsPerSlope ≤
        certificate.slopes.length * certificate.movingRootsPerSlope :=
      Nat.mul_le_mul_right certificate.movingRootsPerSlope hcount
    have hbound : 3 * certificate.movingRootsPerSlope ≤
        certificate.movingPoints :=
      Nat.le_trans hmul certificate.incidenceBound
    exact False.elim ((Nat.not_lt_of_ge hbound) hthree)

/-- Active KoalaBear MCA specialization of the one-pencil payment. -/
theorem koalaBearMca_slopes_length_le_two
    (certificate : C8MovingRootCertificate)
    (hpoints : certificate.movingPoints = 2_097_152)
    (hroots : certificate.movingRootsPerSlope = 981_104) :
    certificate.slopes.length ≤ 2 := by
  apply certificate.slopes_length_le_two_of_three_mul_gt
  omega

/-- Active Mersenne-31 MCA specialization of the same finite payment. -/
theorem m31Mca_slopes_length_le_two
    (certificate : C8MovingRootCertificate)
    (hpoints : certificate.movingPoints = 2_097_152)
    (hroots : certificate.movingRootsPerSlope = 981_128) :
    certificate.slopes.length ≤ 2 := by
  apply certificate.slopes_length_le_two_of_three_mul_gt
  omega

end C8MovingRootCertificate

/-! ## Generic first-match chart construction -/

/-- Finite chart-construction packet.  `rawSlopes key` is the raw projection of
one realized chart before the ordered chart leaves are taken. -/
structure C8ChartExhaustionPacket (Key : Type) [DecidableEq Key] where
  keys : List Key
  keys_nodup : keys.Nodup
  rawSlopes : Key → List Nat
  rawSlopes_nodup : ∀ key ∈ keys, (rawSlopes key).Nodup
  earlierOwner : Key → Option C8EarlierOwner
  suppliedShallowKey : Key
  onePencilCertificate : Key → Option C8MovingRootCertificate

namespace C8ChartExhaustionPacket

/-- Fixed-priority semantic classifier.  The last branch is the sole named deep
residual; it carries no payment. -/
def classify {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key) : C8ChartBucket :=
  match packet.earlierOwner key with
  | some _ => .earlier
  | none =>
      if key = packet.suppliedShallowKey then
        .shallow
      else
        match packet.onePencilCertificate key with
        | some _ => .boundedPencil
        | none => .deepResidual

/-- One chart-key bucket. -/
def bucketCell {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (bucket : C8ChartBucket) : List Key :=
  packet.keys.filter (fun key => decide (packet.classify key = bucket))

/-- Ordered chart-key atlas. -/
def bucketAtlas {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) : List (List Key) :=
  fibreAtlas packet.keys packet.classify c8ChartBuckets

/-- Raw chart slope projections in the same order as the realized chart keys. -/
def rawSlopeCells {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) : List (List Nat) :=
  packet.keys.map packet.rawSlopes

/-- Actual post-deletion chart slope projections. -/
def postDeletionSlopeCells {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) : List (List Nat) :=
  firstMatchLeaves [] packet.rawSlopeCells

/-- Exact membership in one chart-key bucket. -/
theorem mem_bucketCell_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (bucket : C8ChartBucket) (key : Key) :
    key ∈ packet.bucketCell bucket ↔
      key ∈ packet.keys ∧ packet.classify key = bucket := by
  simp [bucketCell]

/-- Earlier bucket iff an explicit C1--C7 owner is present. -/
theorem classify_eq_earlier_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key) :
    packet.classify key = .earlier ↔
      ∃ owner, packet.earlierOwner key = some owner := by
  unfold classify
  cases howner : packet.earlierOwner key with
  | some owner =>
      simp [howner]
  | none =>
      by_cases hshallow : key = packet.suppliedShallowKey
      · simp [howner, hshallow]
      · cases hpencil : packet.onePencilCertificate key with
        | some certificate => simp [howner, hshallow, hpencil]
        | none => simp [howner, hshallow, hpencil]

/-- Shallow bucket iff all earlier owners are absent and the key is exactly the
one supplied shallow chart. -/
theorem classify_eq_shallow_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key) :
    packet.classify key = .shallow ↔
      packet.earlierOwner key = none ∧
      key = packet.suppliedShallowKey := by
  unfold classify
  cases howner : packet.earlierOwner key with
  | some owner =>
      simp [howner]
  | none =>
      by_cases hshallow : key = packet.suppliedShallowKey
      · simp [howner, hshallow]
      · cases hpencil : packet.onePencilCertificate key with
        | some certificate => simp [howner, hshallow, hpencil]
        | none => simp [howner, hshallow, hpencil]

/-- Bounded-pencil bucket iff the chart survives the first two tests and carries
an original moving-root certificate. -/
theorem classify_eq_boundedPencil_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key) :
    packet.classify key = .boundedPencil ↔
      packet.earlierOwner key = none ∧
      key ≠ packet.suppliedShallowKey ∧
      ∃ certificate,
        packet.onePencilCertificate key = some certificate := by
  unfold classify
  cases howner : packet.earlierOwner key with
  | some owner =>
      simp [howner]
  | none =>
      by_cases hshallow : key = packet.suppliedShallowKey
      · simp [howner, hshallow]
      · cases hpencil : packet.onePencilCertificate key with
        | some certificate => simp [howner, hshallow, hpencil]
        | none => simp [howner, hshallow, hpencil]

/-- Deep bucket iff the chart survives every paid/owned test. -/
theorem classify_eq_deepResidual_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key) :
    packet.classify key = .deepResidual ↔
      packet.earlierOwner key = none ∧
      key ≠ packet.suppliedShallowKey ∧
      packet.onePencilCertificate key = none := by
  unfold classify
  cases howner : packet.earlierOwner key with
  | some owner =>
      simp [howner]
  | none =>
      by_cases hshallow : key = packet.suppliedShallowKey
      · simp [howner, hshallow]
      · cases hpencil : packet.onePencilCertificate key with
        | some certificate => simp [howner, hshallow, hpencil]
        | none => simp [howner, hshallow, hpencil]

/-- Every raw chart projection is duplicate-free. -/
theorem rawSlopeCells_nodup {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) :
    ∀ cell ∈ packet.rawSlopeCells, cell.Nodup := by
  intro cell hcell
  simp only [rawSlopeCells, List.mem_map] at hcell
  rcases hcell with ⟨key, hkey, rfl⟩
  exact packet.rawSlopes_nodup key hkey

/-- First-match deletion makes the flattened post-deletion slope projections
duplicate-free.  This is the bucket-level ownership disjointness theorem. -/
theorem postDeletionSlopeCells_nodup {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) :
    packet.postDeletionSlopeCells.flatten.Nodup := by
  unfold postDeletionSlopeCells
  exact nodup_firstMatchLeaves packet.rawSlopeCells packet.rawSlopeCells_nodup

/-- First-match deletion preserves exactly the raw covered slope union. -/
theorem mem_postDeletionSlopeCells_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (slope : Nat) :
    slope ∈ packet.postDeletionSlopeCells.flatten ↔
      slope ∈ packet.rawSlopeCells.flatten := by
  unfold postDeletionSlopeCells
  exact mem_firstMatchLeaves packet.rawSlopeCells slope

/-- The chart-key buckets themselves are duplicate-free. -/
theorem bucketAtlas_nodup {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) :
    packet.bucketAtlas.flatten.Nodup := by
  unfold bucketAtlas
  exact nodup_fibreAtlas_flatten packet.keys packet.classify c8ChartBuckets
    packet.keys_nodup c8ChartBuckets_nodup

/-- The four chart-key buckets cover exactly the realized chart keys. -/
theorem mem_bucketAtlas_flatten_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key) :
    key ∈ packet.bucketAtlas.flatten ↔ key ∈ packet.keys := by
  unfold bucketAtlas
  exact mem_fibreAtlas_flatten_iff packet.keys packet.classify c8ChartBuckets
    (fun current _ => mem_c8ChartBuckets (packet.classify current)) key

/-- Every realized chart key belongs to exactly one bucket. -/
theorem existsUnique_bucket {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key)
    (hkey : key ∈ packet.keys) :
    ∃ bucket,
      key ∈ packet.bucketCell bucket ∧
      ∀ other, key ∈ packet.bucketCell other → other = bucket := by
  refine ⟨packet.classify key, ?_, ?_⟩
  · exact (packet.mem_bucketCell_iff (packet.classify key) key).2 ⟨hkey, rfl⟩
  · intro other hmem
    have hclass := (packet.mem_bucketCell_iff other key).1 hmem
    exact hclass.2.symm

/-- Membership in the bounded-pencil bucket returns the original supplied
certificate; no ray certificate is synthesized by the route cut. -/
theorem onePencilCertificate_of_mem {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key)
    (hmem : key ∈ packet.bucketCell .boundedPencil) :
    ∃ certificate, packet.onePencilCertificate key = some certificate := by
  have hclass := (packet.mem_bucketCell_iff .boundedPencil key).1 hmem
  exact ((packet.classify_eq_boundedPencil_iff key).1 hclass.2).2.2

end C8ChartExhaustionPacket

/-- Exact sole residual name used by the source note and replay certificate. -/
def c8DeepResidualName : String :=
  "DEEP_HIGHER_DIMENSIONAL_BALANCED_CORE_AFTER_C1_C7_SHALLOW_AND_ONE_PENCIL_DELETION"

/-- Regression lock for the exact residual spelling. -/
theorem c8DeepResidualName_exact :
    c8DeepResidualName =
      "DEEP_HIGHER_DIMENSIONAL_BALANCED_CORE_AFTER_C1_C7_SHALLOW_AND_ONE_PENCIL_DELETION" :=
  rfl

/-! ## Actual finite spine calibration -/

/-- Four realized chart keys in first-match order. -/
inductive C8SpineChartKey where
  | earlierC1
  | suppliedShallow
  | movingPencil
  | deepHigherDimensional
  deriving DecidableEq, Repr

/-- The supplied shallow chart is exactly the integrated spine fixture consumed
field-for-field by the C8 shallow producer: `affineToyBridge`, syndrome key `1`,
`highKappaToySE2`, its chart inclusion, `highKappaToyBounds`, and kernel label
`1000000`. -/
def c8SpineShallowInput : C8ShallowClosureInput Nat Nat Nat where
  bridge := affineToyBridge
  syndromeKey := 1
  slopeCell := highKappaToySE2
  chartInclusion := by decide
  bounds := highKappaToyBounds
  kernelDim := 1_000_000

/-- Genuine one-parameter calibration chart, paid at the active KoalaBear
moving-root cap. -/
def c8SpineMovingPencil : C8MovingRootCertificate where
  slopes := [11, 13]
  slopes_nodup := by decide
  movingPoints := 2_097_152
  movingRootsPerSlope := 981_104
  movingRoots_pos := by decide
  incidenceBound := by decide

/-- The sole unexhausted post-deletion calibration slope list. -/
def c8SpineDeepResidualSlopes : List Nat := [17]

/-- Raw chart projections before first-match deletion.

The overlaps are intentional and certify the deletion order:
`5` is already C1-owned; `9` is first paid by the supplied shallow chart; and
`13` is first paid by the one-pencil chart. -/
def c8SpineRawSlopes : C8SpineChartKey → List Nat
  | .earlierC1 => [5]
  | .suppliedShallow => [5, 7, 9]
  | .movingPencil => [9, 11, 13]
  | .deepHigherDimensional => [13, 17]

/-- Exact C1--C7 semantic owner at the calibration. -/
def c8SpineEarlierOwner : C8SpineChartKey → Option C8EarlierOwner
  | .earlierC1 => some .c1
  | _ => none

/-- Exact one-pencil certificate lookup at the calibration. -/
def c8SpineOnePencilCertificate :
    C8SpineChartKey → Option C8MovingRootCertificate
  | .movingPencil => some c8SpineMovingPencil
  | _ => none

/-- Complete actual finite calibration packet. -/
def c8SpineCalibrationPacket : C8ChartExhaustionPacket C8SpineChartKey where
  keys := [.earlierC1, .suppliedShallow, .movingPencil, .deepHigherDimensional]
  keys_nodup := by decide
  rawSlopes := c8SpineRawSlopes
  rawSlopes_nodup := by
    intro key hkey
    cases key <;> decide
  earlierOwner := c8SpineEarlierOwner
  suppliedShallowKey := .suppliedShallow
  onePencilCertificate := c8SpineOnePencilCertificate

/-- Exact first-match deletion.  The second leaf is literally the `(SE2)` slope
list supplied to the shallow producer, the third is literally the moving-root
certificate's slope list, and the fourth is the named deep residual. -/
theorem c8Spine_postDeletionSlopeCells_exact :
    c8SpineCalibrationPacket.postDeletionSlopeCells =
      [[5], c8SpineShallowInput.slopeCell.slopes,
        c8SpineMovingPencil.slopes, c8SpineDeepResidualSlopes] := by
  decide

/-- The flattened assigned slopes are exact and duplicate-free across all four
buckets. -/
theorem c8Spine_postDeletionSlopeFlatten_exact :
    c8SpineCalibrationPacket.postDeletionSlopeCells.flatten =
      [5, 7, 9, 11, 13, 17] := by
  decide

/-- First-match disjointness for the actual calibration. -/
theorem c8Spine_firstMatchOwnership_nodup :
    c8SpineCalibrationPacket.postDeletionSlopeCells.flatten.Nodup :=
  c8SpineCalibrationPacket.postDeletionSlopeCells_nodup

/-- The supplied shallow leaf is exactly the producer input `[7,9]`. -/
theorem c8Spine_shallowSlopes_exact :
    c8SpineShallowInput.slopeCell.slopes = [7, 9] := by
  rfl

/-- The integrated shallow closure theorem pays the exact supplied leaf. -/
theorem c8Spine_shallow_paid :
    c8SpineShallowInput.slopeCell.slopes.length ≤
      c8SpineShallowInput.compilerLoss * c8SpineShallowInput.naturalScale :=
  c8SpineShallowInput.slopes_paid

/-- The one-parameter leaf is paid at exact slope cap two. -/
theorem c8Spine_movingPencil_paid :
    c8SpineMovingPencil.slopes.length ≤ 2 := by
  exact C8MovingRootCertificate.koalaBearMca_slopes_length_le_two
    c8SpineMovingPencil rfl rfl

/-- The classifier reaches the four required terminals in exact order. -/
theorem c8Spine_classification_exact :
    c8SpineCalibrationPacket.classify .earlierC1 = .earlier ∧
    c8SpineCalibrationPacket.classify .suppliedShallow = .shallow ∧
    c8SpineCalibrationPacket.classify .movingPencil = .boundedPencil ∧
    c8SpineCalibrationPacket.classify .deepHigherDimensional = .deepResidual := by
  decide

/-- The actual chart-key atlas is one chart in each required bucket. -/
theorem c8Spine_bucketAtlas_exact :
    c8SpineCalibrationPacket.bucketAtlas =
      [[.earlierC1], [.suppliedShallow], [.movingPencil],
        [.deepHigherDimensional]] := by
  decide

/-- Exactly one calibration chart remains in the named deep residual. -/
theorem c8Spine_deepResidual_exact :
    c8SpineCalibrationPacket.bucketCell .deepResidual =
      [.deepHigherDimensional] ∧
    c8SpineDeepResidualSlopes = [17] := by
  decide

/-- Every realized calibration chart belongs to exactly one of the four buckets. -/
theorem c8Spine_everyChart_exactlyOneBucket :
    ∀ key ∈ c8SpineCalibrationPacket.keys,
      ∃ bucket,
        key ∈ c8SpineCalibrationPacket.bucketCell bucket ∧
        ∀ other,
          key ∈ c8SpineCalibrationPacket.bucketCell other → other = bucket := by
  intro key hkey
  exact c8SpineCalibrationPacket.existsUnique_bucket key hkey

#print axioms C8ShallowClosureInput.slopes_paid
#print axioms C8MovingRootCertificate.slopes_length_le_two_of_three_mul_gt
#print axioms C8MovingRootCertificate.koalaBearMca_slopes_length_le_two
#print axioms C8MovingRootCertificate.m31Mca_slopes_length_le_two
#print axioms C8ChartExhaustionPacket.classify_eq_earlier_iff
#print axioms C8ChartExhaustionPacket.classify_eq_shallow_iff
#print axioms C8ChartExhaustionPacket.classify_eq_boundedPencil_iff
#print axioms C8ChartExhaustionPacket.classify_eq_deepResidual_iff
#print axioms C8ChartExhaustionPacket.postDeletionSlopeCells_nodup
#print axioms C8ChartExhaustionPacket.mem_postDeletionSlopeCells_iff
#print axioms C8ChartExhaustionPacket.bucketAtlas_nodup
#print axioms C8ChartExhaustionPacket.mem_bucketAtlas_flatten_iff
#print axioms C8ChartExhaustionPacket.existsUnique_bucket
#print axioms C8ChartExhaustionPacket.onePencilCertificate_of_mem
#print axioms c8DeepResidualName_exact
#print axioms c8Spine_postDeletionSlopeCells_exact
#print axioms c8Spine_postDeletionSlopeFlatten_exact
#print axioms c8Spine_firstMatchOwnership_nodup
#print axioms c8Spine_shallowSlopes_exact
#print axioms c8Spine_shallow_paid
#print axioms c8Spine_movingPencil_paid
#print axioms c8Spine_classification_exact
#print axioms c8Spine_bucketAtlas_exact
#print axioms c8Spine_deepResidual_exact
#print axioms c8Spine_everyChart_exactlyOneBucket

end AsymptoticSpine
