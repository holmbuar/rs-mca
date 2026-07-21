import AsymptoticSpine.PrefixAtlas

namespace AsymptoticSpine

/-!
# Exact finite C8 chart construction and four-bucket exhaustion

This stdlib-only module formalizes the finite route-cut layer of the C8 chart
exhaustion problem.  It does not import the open C8 producer or high-kappa
modules.  Its only imported proof interfaces are the integrated prefix-fibre
atlas and first-match disjointization APIs.

A packet contains a duplicate-free list of realized C8 chart keys, an explicit
C1--C7 owner function, one supplied shallow key, and optional one-parameter
moving-root certificates.  The classifier is fixed before enumeration and uses
this strict order:

1. an earlier C1--C7 owner;
2. the one supplied shallow chart;
3. a certified one-parameter moving-root chart;
4. one named deep higher-dimensional residual class.

The resulting four cells are proved duplicate-free and exhaustive, with exact
membership characterizations.  The deep class is not paid.  The moving-root
certificate is only the finite incidence interface; proving that a concrete RS
chart supplies it remains external.
-/

/-- Semantic owners that precede C8 in the first-match chronology. -/
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

/-- Fixed bucket order used by the finite first-match atlas. -/
def c8ChartBuckets : List C8ChartBucket :=
  [.earlier, .shallow, .boundedPencil, .deepResidual]

/-- The four bucket labels are duplicate-free. -/
theorem c8ChartBuckets_nodup : c8ChartBuckets.Nodup := by
  decide

/-- Every bucket label occurs in the fixed bucket order. -/
theorem mem_c8ChartBuckets (bucket : C8ChartBucket) :
    bucket ∈ c8ChartBuckets := by
  cases bucket <;> decide

/-- Exact finite moving-root incidence data for one projective locator pencil.

`movingPoints` is the number of available nonfixed domain points,
`movingRootsPerSlope` is the certified number of moving roots contributed by
one counted slope, and `slopeCount` is the actual distinct-slope numerator of
the chart.  The cross-multiplied incidence inequality is the division-free form
of the moving-root payment. -/
structure C8MovingRootCertificate where
  movingPoints : Nat
  movingRootsPerSlope : Nat
  slopeCount : Nat
  movingRoots_pos : 0 < movingRootsPerSlope
  incidenceBound : slopeCount * movingRootsPerSlope ≤ movingPoints

namespace C8MovingRootCertificate

/-- If three slopes would already require more moving-root incidences than are
available, the certified chart has at most two distinct slopes. -/
theorem slopeCount_le_two_of_three_mul_gt
    (certificate : C8MovingRootCertificate)
    (hthree : certificate.movingPoints <
      3 * certificate.movingRootsPerSlope) :
    certificate.slopeCount ≤ 2 := by
  by_contra hle
  have hcount : 3 ≤ certificate.slopeCount := by
    omega
  have hmul : 3 * certificate.movingRootsPerSlope ≤
      certificate.slopeCount * certificate.movingRootsPerSlope :=
    Nat.mul_le_mul_right certificate.movingRootsPerSlope hcount
  have hbound : 3 * certificate.movingRootsPerSlope ≤
      certificate.movingPoints :=
    Nat.le_trans hmul certificate.incidenceBound
  exact (Nat.not_lt_of_ge hbound) hthree

/-- Active Mersenne-31 MCA calibration: a genuine one-pencil certificate with
`n=2^21` and `981128` moving roots per slope has at most two slopes. -/
theorem m31Mca_slopeCount_le_two
    (certificate : C8MovingRootCertificate)
    (hpoints : certificate.movingPoints = 2_097_152)
    (hroots : certificate.movingRootsPerSlope = 981_128) :
    certificate.slopeCount ≤ 2 := by
  apply certificate.slopeCount_le_two_of_three_mul_gt
  omega

/-- Active KoalaBear MCA calibration: a genuine one-pencil certificate with
`n=2^21` and `981104` moving roots per slope has at most two slopes. -/
theorem koalaBearMca_slopeCount_le_two
    (certificate : C8MovingRootCertificate)
    (hpoints : certificate.movingPoints = 2_097_152)
    (hroots : certificate.movingRootsPerSlope = 981_104) :
    certificate.slopeCount ≤ 2 := by
  apply certificate.slopeCount_le_two_of_three_mul_gt
  omega

end C8MovingRootCertificate

/-- Complete finite input for constructing the realized C8 chart atlas.

The list `keys` is the duplicate-free realized chart-key list after the chosen
raw chart construction.  `earlierOwner` is the explicit semantic owner function
for C1--C7.  `suppliedShallowKey` names the single shallow closure chart.
`onePencilCertificate` is `some` exactly on keys carrying a supplied moving-root
certificate. -/
structure C8ChartExhaustionPacket (Key : Type) [DecidableEq Key] where
  keys : List Key
  keys_nodup : keys.Nodup
  earlierOwner : Key → Option C8EarlierOwner
  suppliedShallowKey : Key
  onePencilCertificate : Key → Option C8MovingRootCertificate

namespace C8ChartExhaustionPacket

/-- Fixed-priority chart classifier.  The final branch is the sole named deep
residual class; no analytic or ray payment is inserted there. -/
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

/-- One exact bucket cell. -/
def bucketCell {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (bucket : C8ChartBucket) : List Key :=
  packet.keys.filter (fun key => decide (packet.classify key = bucket))

/-- The ordered four-cell atlas. -/
def bucketAtlas {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) : List (List Key) :=
  fibreAtlas packet.keys packet.classify c8ChartBuckets

/-- The atlas is definitionally the four bucket cells in the fixed order. -/
theorem bucketAtlas_eq_cells {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) :
    packet.bucketAtlas = c8ChartBuckets.map packet.bucketCell := by
  rfl

/-- Exact membership in one bucket cell. -/
theorem mem_bucketCell_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (bucket : C8ChartBucket) (key : Key) :
    key ∈ packet.bucketCell bucket ↔
      key ∈ packet.keys ∧ packet.classify key = bucket := by
  simp [bucketCell]

/-- Exact characterization of the earlier-owner bucket. -/
theorem classify_eq_earlier_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key) :
    packet.classify key = .earlier ↔
      ∃ owner, packet.earlierOwner key = some owner := by
  cases he : packet.earlierOwner key with
  | some owner =>
      simp [classify, he]
  | none =>
      by_cases hs : key = packet.suppliedShallowKey
      · simp [classify, he, hs]
      · cases hp : packet.onePencilCertificate key with
        | some certificate => simp [classify, he, hs, hp]
        | none => simp [classify, he, hs, hp]

/-- Exact characterization of the supplied shallow bucket. -/
theorem classify_eq_shallow_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key) :
    packet.classify key = .shallow ↔
      packet.earlierOwner key = none ∧
      key = packet.suppliedShallowKey := by
  cases he : packet.earlierOwner key with
  | some owner =>
      simp [classify, he]
  | none =>
      by_cases hs : key = packet.suppliedShallowKey
      · simp [classify, he, hs]
      · cases hp : packet.onePencilCertificate key with
        | some certificate => simp [classify, he, hs, hp]
        | none => simp [classify, he, hs, hp]

/-- Exact characterization of the bounded one-pencil bucket. -/
theorem classify_eq_boundedPencil_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key) :
    packet.classify key = .boundedPencil ↔
      packet.earlierOwner key = none ∧
      key ≠ packet.suppliedShallowKey ∧
      ∃ certificate,
        packet.onePencilCertificate key = some certificate := by
  cases he : packet.earlierOwner key with
  | some owner =>
      simp [classify, he]
  | none =>
      by_cases hs : key = packet.suppliedShallowKey
      · simp [classify, he, hs]
      · cases hp : packet.onePencilCertificate key with
        | some certificate => simp [classify, he, hs, hp]
        | none => simp [classify, he, hs, hp]

/-- Exact characterization of the sole named deep residual class. -/
theorem classify_eq_deepResidual_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key) :
    packet.classify key = .deepResidual ↔
      packet.earlierOwner key = none ∧
      key ≠ packet.suppliedShallowKey ∧
      packet.onePencilCertificate key = none := by
  cases he : packet.earlierOwner key with
  | some owner =>
      simp [classify, he]
  | none =>
      by_cases hs : key = packet.suppliedShallowKey
      · simp [classify, he, hs]
      · cases hp : packet.onePencilCertificate key with
        | some certificate => simp [classify, he, hs, hp]
        | none => simp [classify, he, hs, hp]

/-- Exact earlier-cell membership, including raw-key membership. -/
theorem mem_earlierCell_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key) :
    key ∈ packet.bucketCell .earlier ↔
      key ∈ packet.keys ∧
      ∃ owner, packet.earlierOwner key = some owner := by
  rw [packet.mem_bucketCell_iff, packet.classify_eq_earlier_iff]

/-- Exact supplied-shallow-cell membership. -/
theorem mem_shallowCell_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key) :
    key ∈ packet.bucketCell .shallow ↔
      key ∈ packet.keys ∧
      packet.earlierOwner key = none ∧
      key = packet.suppliedShallowKey := by
  rw [packet.mem_bucketCell_iff, packet.classify_eq_shallow_iff]
  tauto

/-- Exact bounded-pencil-cell membership. -/
theorem mem_boundedPencilCell_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key) :
    key ∈ packet.bucketCell .boundedPencil ↔
      key ∈ packet.keys ∧
      packet.earlierOwner key = none ∧
      key ≠ packet.suppliedShallowKey ∧
      ∃ certificate,
        packet.onePencilCertificate key = some certificate := by
  rw [packet.mem_bucketCell_iff, packet.classify_eq_boundedPencil_iff]
  tauto

/-- Exact named-deep-cell membership.  This is the route-cut remainder and is
not paid by this module. -/
theorem mem_deepResidualCell_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key) :
    key ∈ packet.bucketCell .deepResidual ↔
      key ∈ packet.keys ∧
      packet.earlierOwner key = none ∧
      key ≠ packet.suppliedShallowKey ∧
      packet.onePencilCertificate key = none := by
  rw [packet.mem_bucketCell_iff, packet.classify_eq_deepResidual_iff]
  tauto

/-- The flattened four-cell atlas is duplicate-free: no chart key is assigned
to two buckets. -/
theorem bucketAtlas_nodup {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) :
    packet.bucketAtlas.flatten.Nodup := by
  unfold bucketAtlas
  exact nodup_fibreAtlas_flatten packet.keys packet.classify c8ChartBuckets
    packet.keys_nodup c8ChartBuckets_nodup

/-- Exhaustion: the four bucket cells cover exactly the realized chart keys. -/
theorem mem_bucketAtlas_flatten_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key) :
    key ∈ packet.bucketAtlas.flatten ↔ key ∈ packet.keys := by
  unfold bucketAtlas
  exact mem_fibreAtlas_flatten_iff packet.keys packet.classify c8ChartBuckets
    (fun current _ => mem_c8ChartBuckets (packet.classify current)) key

/-- The same exact coverage survives the generic first-match leaf operation. -/
theorem mem_firstMatch_bucketAtlas_iff {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key) :
    key ∈ (firstMatchLeaves [] packet.bucketAtlas).flatten ↔
      key ∈ packet.keys :=
  (mem_firstMatchLeaves packet.bucketAtlas key).trans
    (packet.mem_bucketAtlas_flatten_iff key)

/-- Every realized chart key belongs to exactly one of the four bucket cells. -/
theorem existsUnique_bucket {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key)
    (hkey : key ∈ packet.keys) :
    ∃! bucket, key ∈ packet.bucketCell bucket := by
  refine ⟨packet.classify key, ?_, ?_⟩
  · exact (packet.mem_bucketCell_iff (packet.classify key) key).2 ⟨hkey, rfl⟩
  · intro bucket hmem
    have hclass := (packet.mem_bucketCell_iff bucket key).1 hmem
    exact hclass.2.symm

/-- A bounded-pencil key exposes the exact moving-root certificate used to pay
it; no synthetic certificate is manufactured by the classifier. -/
theorem onePencilCertificate_of_mem {Key : Type} [DecidableEq Key]
    (packet : C8ChartExhaustionPacket Key) (key : Key)
    (hmem : key ∈ packet.bucketCell .boundedPencil) :
    ∃ certificate, packet.onePencilCertificate key = some certificate :=
  ((packet.mem_boundedPencilCell_iff key).1 hmem).2.2.2

end C8ChartExhaustionPacket

/-- The exact sole residual-class name used by the source and certificate
packet. -/
def c8DeepResidualName : String :=
  "DEEP_HIGHER_DIMENSIONAL_BALANCED_CORE_AFTER_C1_C7_SHALLOW_AND_ONE_PENCIL_DELETION"

/-- Regression lock for the exact residual spelling. -/
theorem c8DeepResidualName_exact :
    c8DeepResidualName =
      "DEEP_HIGHER_DIMENSIONAL_BALANCED_CORE_AFTER_C1_C7_SHALLOW_AND_ONE_PENCIL_DELETION" :=
  rfl

/-! ## Executable four-chart spine calibration -/

inductive C8CalibrationKey where
  | earlierC4
  | suppliedShallow
  | movingPencil
  | deepHigherDimensional
  deriving DecidableEq, Repr

/-- Exact active-row one-pencil certificate used by the finite calibration. -/
def c8CalibrationM31Pencil : C8MovingRootCertificate where
  movingPoints := 2_097_152
  movingRootsPerSlope := 981_128
  slopeCount := 2
  movingRoots_pos := by decide
  incidenceBound := by decide

/-- Four realized keys, one in each route-cut bucket. -/
def c8CalibrationPacket : C8ChartExhaustionPacket C8CalibrationKey where
  keys := [.earlierC4, .suppliedShallow, .movingPencil, .deepHigherDimensional]
  keys_nodup := by decide
  earlierOwner := fun
    | .earlierC4 => some .c4
    | _ => none
  suppliedShallowKey := .suppliedShallow
  onePencilCertificate := fun
    | .movingPencil => some c8CalibrationM31Pencil
    | _ => none

/-- The classifier reaches all four terminals in the intended order. -/
theorem c8Calibration_classification :
    c8CalibrationPacket.classify .earlierC4 = .earlier ∧
    c8CalibrationPacket.classify .suppliedShallow = .shallow ∧
    c8CalibrationPacket.classify .movingPencil = .boundedPencil ∧
    c8CalibrationPacket.classify .deepHigherDimensional = .deepResidual := by
  decide

/-- Enumeration certificate: the four-cell atlas is literally one key per
bucket, in the fixed first-match order. -/
theorem c8Calibration_bucketAtlas_exact :
    c8CalibrationPacket.bucketAtlas =
      [[.earlierC4], [.suppliedShallow], [.movingPencil],
        [.deepHigherDimensional]] := by
  decide

/-- The only unexhausted calibration key is the explicitly named deep class. -/
theorem c8Calibration_deepResidual_exact :
    c8CalibrationPacket.bucketCell .deepResidual =
      [.deepHigherDimensional] := by
  decide

/-- The calibration atlas is duplicate-free and exhaustive. -/
theorem c8Calibration_exhaustive :
    c8CalibrationPacket.bucketAtlas.flatten.Nodup ∧
    ∀ key,
      key ∈ c8CalibrationPacket.bucketAtlas.flatten ↔
        key ∈ c8CalibrationPacket.keys := by
  constructor
  · exact c8CalibrationPacket.bucketAtlas_nodup
  · intro key
    exact c8CalibrationPacket.mem_bucketAtlas_flatten_iff key

/-- The active M31 one-pencil calibration is paid by the moving-root interface
at exact cap two. -/
theorem c8Calibration_m31Pencil_paid :
    c8CalibrationM31Pencil.slopeCount ≤ 2 := by
  exact C8MovingRootCertificate.m31Mca_slopeCount_le_two
    c8CalibrationM31Pencil rfl rfl

#print axioms C8MovingRootCertificate.slopeCount_le_two_of_three_mul_gt
#print axioms C8MovingRootCertificate.m31Mca_slopeCount_le_two
#print axioms C8MovingRootCertificate.koalaBearMca_slopeCount_le_two
#print axioms C8ChartExhaustionPacket.classify_eq_earlier_iff
#print axioms C8ChartExhaustionPacket.classify_eq_shallow_iff
#print axioms C8ChartExhaustionPacket.classify_eq_boundedPencil_iff
#print axioms C8ChartExhaustionPacket.classify_eq_deepResidual_iff
#print axioms C8ChartExhaustionPacket.bucketAtlas_nodup
#print axioms C8ChartExhaustionPacket.mem_bucketAtlas_flatten_iff
#print axioms C8ChartExhaustionPacket.mem_firstMatch_bucketAtlas_iff
#print axioms C8ChartExhaustionPacket.existsUnique_bucket
#print axioms C8ChartExhaustionPacket.onePencilCertificate_of_mem
#print axioms c8DeepResidualName_exact
#print axioms c8Calibration_classification
#print axioms c8Calibration_bucketAtlas_exact
#print axioms c8Calibration_deepResidual_exact
#print axioms c8Calibration_exhaustive
#print axioms c8Calibration_m31Pencil_paid

end AsymptoticSpine
