import M31QRootedShell.Envelope

/-!
# Faithful finite `2+7` route counterexample

A stdlib-only, decidable replay of the frozen `p=127`, `n=16`, `m=8`, `w=1`
Chebyshev/twin-coset control.  No finite-field library is required: all field
operations used by the certificate are evaluated as natural-number residues
modulo `127`.
-/

namespace M31QRootedShell.ToyCounterexample

open M31QRootedShell

/-- Domain indices. -/
def indices : List Nat := List.range 16

/-- A 16-point Chebyshev control domain in `Nat mod 127`. -/
def domain : Nat → Nat
  | 0 => 5
  | 1 => 39
  | 2 => 89
  | 3 => 42
  | 4 => 22
  | 5 => 125
  | 6 => 9
  | 7 => 53
  | 8 => 122
  | 9 => 88
  | 10 => 38
  | 11 => 85
  | 12 => 105
  | 13 => 2
  | 14 => 118
  | 15 => 74
  | _ => 0

/-- Negation partner on the control domain. -/
def partner : Nat → Nat
  | 0 => 8
  | 1 => 9
  | 2 => 10
  | 3 => 11
  | 4 => 12
  | 5 => 13
  | 6 => 14
  | 7 => 15
  | 8 => 0
  | 9 => 1
  | 10 => 2
  | 11 => 3
  | 12 => 4
  | 13 => 5
  | 14 => 6
  | 15 => 7
  | _ => 0

/-- `T₂(x)=2x²-1` represented without natural underflow. -/
def t2 (x : Nat) : Nat := (2 * x * x + 126) % 127

def anchor : List Nat := [0, 1, 3, 4, 7, 8, 13, 14]

def neighbors : List (List Nat) :=
  [ [0, 2, 5, 6, 10, 11, 12, 15]
  , [2, 3, 6, 9, 10, 11, 12, 15]
  , [2, 4, 5, 6, 9, 10, 11, 15]
  , [2, 5, 6, 9, 10, 11, 12, 14]
  , [2, 5, 6, 9, 10, 12, 13, 15]
  , [2, 5, 7, 9, 10, 11, 12, 15]
  ]

/-- Sum a natural-valued list. -/
def sumNat : List Nat → Nat
  | [] => 0
  | x :: xs => x + sumNat xs

/-- First power-sum prefix coordinate. -/
def prefix1 (S : List Nat) : Nat :=
  (sumNat (S.map domain)) % 127

/-- Intersection cardinality for duplicate-free supports. -/
def interCard (A B : List Nat) : Nat :=
  (A.filter fun x => B.contains x).length

/-- Constant-weight exchange distance. -/
def exchangeDistance (A B : List Nat) : Nat :=
  A.length - interCard A B

/-- Negation-closed supports are the toy quotient proxy removed before Q. -/
def negationClosed (S : List Nat) : Bool :=
  S.all fun i => S.contains (partner i)

/-- Literal common planted core of the displayed seven supports. -/
def commonCore : List Nat :=
  anchor.filter fun x => neighbors.all fun S => S.contains x

/-- Number of displayed neighbors at rooted exchange distance `e`. -/
def rootedDegree (e : Nat) : Nat :=
  (neighbors.filter fun S => exchangeDistance anchor S == e).length

def ambientShell7 : Nat := 64

/-- Duplicate-free list predicate, kept stdlib-only and executable. -/
def noDuplicates : List Nat → Bool
  | [] => true
  | x :: xs => !xs.contains x && noDuplicates xs

/-- Every displayed support is an eight-set with no duplicate indices. -/
def supportShapeCheck : Bool :=
  anchor.length == 8 && noDuplicates anchor &&
  neighbors.all fun S => S.length == 8 && noDuplicates S

/-- Every displayed support lies in the same first-prefix target. -/
def commonPrefixCheck : Bool :=
  neighbors.all fun S => prefix1 S == prefix1 anchor

/-- Every displayed neighbor has exchange distance seven from the anchor. -/
def distanceSevenCheck : Bool :=
  neighbors.all fun S => exchangeDistance anchor S == 7

/-- The displayed supports are outside the negation-closed quotient proxy. -/
def quotientPruningCheck : Bool :=
  !negationClosed anchor && neighbors.all fun S => !negationClosed S

/-- Partnering is exact field negation modulo 127. -/
def partnerNegationCheck : Bool :=
  indices.all fun i => (domain i + domain (partner i)) % 127 == 0

/-- The displayed pairs are exactly the fibers of `T₂`. -/
def t2FiberCheck : Bool :=
  indices.all fun i =>
    indices.all fun j =>
      (t2 (domain i) == t2 (domain j)) ==
        ((j == i) || (j == partner i))

/-- The control is not a multiplicative subgroup in disguise. -/
def notProductClosedCheck : Bool :=
  !(indices.any fun k =>
      domain k == (domain 0 * domain 1) % 127)

theorem support_shapes : supportShapeCheck = true := by decide

theorem common_prefix : commonPrefixCheck = true := by decide

theorem all_distances_seven : distanceSevenCheck = true := by decide

theorem quotient_proxy_removed : quotientPruningCheck = true := by decide

theorem partner_is_negation : partnerNegationCheck = true := by decide

theorem t2_fibers_exact : t2FiberCheck = true := by decide

theorem not_product_closed : notProductClosedCheck = true := by decide

theorem planted_common_core_empty : commonCore = [] := by decide

theorem rootedDegree_seven : rootedDegree 7 = 6 := by decide

/-- Exact failure of the stronger `2+7` local envelope. -/
theorem two_plus_seven_fails :
    7 * ambientShell7 < 127 * (rootedDegree 7 - 2) := by decide

/-- The same rooted configuration satisfies the neighboring `3+7` inequality. -/
theorem three_plus_seven_holds :
    127 * (rootedDegree 7 - 3) ≤ 7 * ambientShell7 := by decide

end M31QRootedShell.ToyCounterexample
