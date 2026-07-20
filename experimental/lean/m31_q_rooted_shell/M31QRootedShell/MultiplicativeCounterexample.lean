import M31QRootedShell.Envelope

/-!
# Multiplicative-subgroup counterexample to support-only `3+7`

This stdlib-only module checks an explicit family in the order-twenty
multiplicative subgroup of `F_241`.  After deleting every support with a
nontrivial dihedral stabilizer, the retained same-prefix family has empty common
core but violates the local `(b,c)=(3,7)` rooted-shell envelope.

The claim is deliberately support-level.  No actual slope-level C1--C8 owner is
constructed, so this is a route counterexample rather than a counterexample to
the deployed Mersenne-31 exact residual.
-/

namespace M31QRootedShell.MultiplicativeCounterexample

open M31QRootedShell

abbrev Support := List Nat

/-- Packet parameters. -/
def p : Nat := 241
def n : Nat := 20
def m : Nat := 10
def w : Nat := 2
def generator : Nat := 235

def indices : List Nat := List.range n

/-- The order-twenty subgroup, indexed by powers of `235` modulo `241`. -/
def domain : Nat → Nat
  | 0 => 1
  | 1 => 235
  | 2 => 36
  | 3 => 25
  | 4 => 91
  | 5 => 177
  | 6 => 143
  | 7 => 106
  | 8 => 87
  | 9 => 201
  | 10 => 240
  | 11 => 6
  | 12 => 205
  | 13 => 216
  | 14 => 150
  | 15 => 64
  | 16 => 98
  | 17 => 135
  | 18 => 154
  | 19 => 40
  | _ => 0

/-- Small modular exponentiation used only for the frozen subgroup control. -/
def powMod (a : Nat) : Nat → Nat
  | 0 => 1
  | k + 1 => (powMod a k * a) % p

/-- Sum a natural-valued list. -/
def sumNat : List Nat → Nat
  | [] => 0
  | x :: xs => x + sumNat xs

/-- Sum all unordered pair products. -/
def pairSum : List Nat → Nat
  | [] => 0
  | x :: xs => x * sumNat xs + pairSum xs

/-- The first two elementary-symmetric prefix coordinates modulo `241`. -/
def prefix1 (S : Support) : Nat := (sumNat (S.map domain)) % p
def prefix2 (S : Support) : Nat := (pairSum (S.map domain)) % p

/-- Duplicate-free list predicate. -/
def noDuplicates : List Nat → Bool
  | [] => true
  | x :: xs => !xs.contains x && noDuplicates xs

/-- Duplicate-free catalogue predicate. -/
def noDuplicateSupports : List Support → Bool
  | [] => true
  | S :: families => !families.contains S && noDuplicateSupports families

/-- Extensional equality for supports inside the twenty-point domain. -/
def sameSupport (A B : Support) : Bool :=
  indices.all fun i => (A.contains i) == (B.contains i)

/-- Rotation is multiplication by a subgroup element. -/
def rotateSupport (shift : Nat) (S : Support) : Support :=
  S.map fun i => (i + shift) % n

/-- Reflection is multiplication by a subgroup element followed by inversion. -/
def reflectSupport (axis : Nat) (S : Support) : Support :=
  S.map fun i => (axis + n - i) % n

/-- Whether a rotation or reflection fixes a support. -/
def rotationFixes (S : Support) (shift : Nat) : Bool :=
  sameSupport S (rotateSupport shift S)

def reflectionFixes (S : Support) (axis : Nat) : Bool :=
  sameSupport S (reflectSupport axis S)

/-- The support has no nonidentity rotation and no reflection stabilizer. -/
def dihedralGeneric (S : Support) : Bool :=
  (List.range (n - 1)).all (fun k => !rotationFixes S (k + 1)) &&
  indices.all fun axis => !reflectionFixes S axis

/-- Whether two supports are related by some element of the dihedral action. -/
def sameDihedralOrbit (A B : Support) : Bool :=
  indices.any (fun shift => sameSupport (rotateSupport shift A) B) ||
  indices.any fun axis => sameSupport (reflectSupport axis A) B

/-- Intersection cardinality for duplicate-free supports. -/
def interCard (A B : Support) : Nat :=
  (A.filter fun x => B.contains x).length

/-- Constant-weight exchange distance. -/
def exchangeDistance (A B : Support) : Nat :=
  A.length - interCard A B

/-- The complete displayed target catalogue.  Exhaustiveness in the whole
`choose(20,10)` universe is auxiliary replay; the explicit family is the Lean
counterexample. -/
def rawCatalog : List Support :=
  [ [0, 1, 2, 3, 4, 6, 7, 9, 15, 18]
  , [0, 1, 2, 4, 6, 7, 12, 15, 17, 19]
  , [0, 1, 2, 5, 7, 10, 12, 15, 16, 17]
  , [0, 1, 3, 4, 6, 8, 13, 15, 18, 19]
  , [0, 1, 3, 5, 8, 10, 13, 15, 16, 18]
  , [0, 1, 3, 6, 7, 8, 12, 14, 15, 19]
  , [0, 1, 4, 5, 9, 10, 14, 15, 16, 19]
  , [0, 1, 4, 7, 8, 9, 11, 17, 18, 19]
  , [0, 2, 3, 4, 5, 6, 12, 13, 15, 16]
  , [0, 2, 4, 5, 7, 9, 11, 12, 16, 17]
  , [0, 3, 4, 5, 8, 9, 11, 13, 16, 18]
  , [0, 3, 5, 7, 8, 9, 11, 12, 14, 16]
  , [0, 4, 5, 8, 11, 12, 13, 16, 17, 19]
  , [1, 2, 3, 7, 8, 12, 13, 16, 17, 18]
  , [1, 2, 4, 7, 9, 12, 14, 16, 17, 19]
  , [1, 3, 4, 8, 9, 13, 14, 16, 18, 19]
  , [2, 5, 6, 10, 11, 13, 14, 17, 18, 19]
  ]

/-- The two reflection-fixed supports removed by the support-level C2 proxy. -/
def deletedExpected : List Support :=
  [ [0, 1, 2, 5, 7, 10, 12, 15, 16, 17]
  , [1, 3, 4, 8, 9, 13, 14, 16, 18, 19]
  ]

/-- The exact retained subcatalogue. -/
def residualExpected : List Support :=
  [ [0, 1, 2, 3, 4, 6, 7, 9, 15, 18]
  , [0, 1, 2, 4, 6, 7, 12, 15, 17, 19]
  , [0, 1, 3, 4, 6, 8, 13, 15, 18, 19]
  , [0, 1, 3, 5, 8, 10, 13, 15, 16, 18]
  , [0, 1, 3, 6, 7, 8, 12, 14, 15, 19]
  , [0, 1, 4, 5, 9, 10, 14, 15, 16, 19]
  , [0, 1, 4, 7, 8, 9, 11, 17, 18, 19]
  , [0, 2, 3, 4, 5, 6, 12, 13, 15, 16]
  , [0, 2, 4, 5, 7, 9, 11, 12, 16, 17]
  , [0, 3, 4, 5, 8, 9, 11, 13, 16, 18]
  , [0, 3, 5, 7, 8, 9, 11, 12, 14, 16]
  , [0, 4, 5, 8, 11, 12, 13, 16, 17, 19]
  , [1, 2, 3, 7, 8, 12, 13, 16, 17, 18]
  , [1, 2, 4, 7, 9, 12, 14, 16, 17, 19]
  , [2, 5, 6, 10, 11, 13, 14, 17, 18, 19]
  ]

/-- Executable support-level pruning. -/
def residual : List Support := rawCatalog.filter dihedralGeneric
def deleted : List Support := rawCatalog.filter fun S => !dihedralGeneric S

/-- The violating anchor. -/
def anchor : Support := [2, 5, 6, 10, 11, 13, 14, 17, 18, 19]

/-- Retained neighbors in one rooted exchange shell. -/
def neighborsAt (e : Nat) : List Support :=
  residualExpected.filter fun S =>
    !sameSupport S anchor && exchangeDistance anchor S == e

/-- Rooted shell degree in the retained family. -/
def rootedDegree (e : Nat) : Nat := (neighborsAt e).length

/-- Literal common core of the retained target. -/
def residualCommonCore : List Nat :=
  anchor.filter fun x => residualExpected.all fun S => S.contains x

/-- Literal common core of the violating rooted star. -/
def starCommonCore : List Nat :=
  anchor.filter fun x => (neighborsAt 6).all fun S => S.contains x

/-- Packet checks. -/
def domainPowerCheck : Bool :=
  indices.all fun i => domain i == powMod generator i

def generatorExactOrderCheck : Bool :=
  powMod generator n == 1 &&
  (List.range (n - 1)).all fun k => powMod generator (k + 1) != 1

def domainDistinctCheck : Bool := noDuplicates (indices.map domain)

def supportShapeCheck : Bool :=
  noDuplicateSupports rawCatalog &&
  rawCatalog.all fun S =>
    S.length == m && noDuplicates S && S.all fun i => i < n

def rawPrefixCheck : Bool :=
  rawCatalog.all fun S => prefix1 S == 92 && prefix2 S == 135

def residualGenericCheck : Bool := residualExpected.all dihedralGeneric

def deletedReflectionCheck : Bool :=
  deletedExpected.all fun S => reflectionFixes S 17

def anchorNeighborOrbitCheck : Bool :=
  (neighborsAt 6).all fun S => !sameDihedralOrbit anchor S

def distanceHistogramCheck : Bool :=
  rootedDegree 5 == 1 && rootedDegree 6 == 10 && rootedDegree 7 == 3 &&
  rootedDegree 5 + rootedDegree 6 + rootedDegree 7 == residualExpected.length - 1

/-- Shell and inequality constants. -/
def q : Nat := p ^ w
/-- Pascal recursion for the small binomial coefficient used by this packet. -/
def choose : Nat → Nat → Nat
  | _, 0 => 1
  | 0, _ + 1 => 0
  | n + 1, k + 1 => choose n k + choose n (k + 1)

def ambientShell6 : Nat := choose m 6 * choose (n - m) 6
def counterexampleRows : List ShellRow := [(rootedDegree 6, ambientShell6)]

/-- The displayed domain really is the order-twenty multiplicative control. -/
theorem domain_is_order_twenty_control :
    domainPowerCheck = true ∧ generatorExactOrderCheck = true ∧
      domainDistinctCheck = true := by decide

/-- Every displayed raw support is a duplicate-free ten-subset. -/
theorem raw_catalog_support_shapes : supportShapeCheck = true := by decide

/-- All seventeen displayed supports have prefix target `(92,135)`. -/
theorem raw_catalog_has_common_prefix : rawPrefixCheck = true := by decide

/-- Filtering by the executable dihedral proxy retains exactly fifteen supports. -/
theorem residual_is_exact_dihedral_filter : residual = residualExpected := by decide

/-- The complementary filter removes exactly the two reflection-fixed supports. -/
theorem deleted_is_exact_dihedral_filter : deleted = deletedExpected := by decide

theorem deleted_supports_are_reflection_fixed :
    deletedReflectionCheck = true := by decide

/-- No retained support has a nontrivial rotation or reflection stabilizer. -/
theorem residual_supports_are_dihedral_generic :
    residualGenericCheck = true := by decide

/-- The support-level planted-core proxy is absent. -/
theorem residual_common_core_empty : residualCommonCore = [] := by decide

/-- The violating rooted star itself has no common planted point. -/
theorem star_common_core_empty : starCommonCore = [] := by decide

/-- No violating neighbor is a rotation or scale-inversion image of the anchor. -/
theorem anchor_neighbors_not_dihedrally_related :
    anchorNeighborOrbitCheck = true := by decide

/-- Exact rooted distance distribution `1,10,3` on shells `5,6,7`. -/
theorem anchor_distance_histogram : distanceHistogramCheck = true := by decide

theorem rootedDegree_six : rootedDegree 6 = 10 := by decide

theorem ambientShell6_eq : ambientShell6 = 44100 := by decide

theorem q_eq : q = 58081 := by decide

/-- Exact failure of the proposed support-only `(3+7)` local envelope. -/
theorem three_plus_seven_fails :
    7 * ambientShell6 < q * (rootedDegree 6 - 3) := by decide

/-- Increasing the additive intercept only to four still fails. -/
theorem four_plus_seven_fails :
    7 * ambientShell6 < q * (rootedDegree 6 - 4) := by decide

/-- Intercept five is the first of `3,4,5` that survives this packet. -/
theorem five_plus_seven_holds :
    q * (rootedDegree 6 - 5) ≤ 7 * ambientShell6 := by decide

theorem three_plus_seven_margin :
    q * (rootedDegree 6 - 3) - 7 * ambientShell6 = 97867 := by decide

theorem least_integer_coefficient_at_b3 :
    (q * (rootedDegree 6 - 3) + ambientShell6 - 1) / ambientShell6 = 10 := by decide

/-- Direct connection to the generic compiler predicate from `Envelope.lean`. -/
theorem localEnvelope_three_seven_fails :
    ¬ LocalEnvelope q 3 7 counterexampleRows := by
  intro hlocal
  have hle : q * (rootedDegree 6 - 3) ≤ 7 * ambientShell6 := by
    simpa [counterexampleRows, LocalEnvelope] using hlocal
  exact (Nat.not_lt_of_ge hle) three_plus_seven_fails

end M31QRootedShell.MultiplicativeCounterexample
