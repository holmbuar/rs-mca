import Std.Tactic.NativeDecide

/-!
# Finite effective-image normalization regression

This stdlib-only module checks the `p=11`, `T=F_11^x`, `m=5`, `R=3`
power-sum prefix fixture from
`experimental/notes/audits/sidon_effective_image_mi_ma_normalization_floor.md`.

The module is deliberately finite.  It checks the support catalogue, realized
image, max fiber, one double target, and an explicit inverse proving that three
moment-column differences span all of `F_11^3`.  It does not formalize Fourier
analysis, asymptotics, semantic first-match survival, or a ray compiler.
-/

namespace SidonEffectiveImage

abbrev Support := List Nat

structure Vec3 where
  x : Nat
  y : Nat
  z : Nat
deriving Repr, BEq, DecidableEq

/-- Finite fixture parameters. -/
def p : Nat := 11
def n : Nat := 10
def m : Nat := 5
def r : Nat := 3

/-- The nonzero elements of `F_11`, represented by natural residues. -/
def domain : List Nat := (List.range n).map (fun i => i + 1)

/-- All `k`-subsets of a duplicate-free input list. -/
def choose {alpha : Type} : Nat -> List alpha -> List (List alpha)
  | 0, _ => [[]]
  | _ + 1, [] => []
  | k + 1, x :: xs =>
      (choose k xs).map (fun ys => x :: ys) ++ choose (k + 1) xs

/-- The complete fixed-weight support slice. -/
def supports : List Support := choose m domain

/-- Modular power sum. -/
def sumPowerMod (e : Nat) (S : Support) : Nat :=
  S.foldl (fun acc t => (acc + (t ^ e) % p) % p) 0

/-- The first three power sums modulo `11`. -/
def syndrome (S : Support) : Vec3 :=
  { x := sumPowerMod 1 S
  , y := sumPowerMod 2 S
  , z := sumPowerMod 3 S }

/-- Duplicate-free list predicate, kept executable and stdlib-only. -/
def noDuplicates [BEq alpha] : List alpha -> Bool
  | [] => true
  | x :: xs => !xs.contains x && noDuplicates xs

/-- Retain one copy of each value. -/
def dedup [BEq alpha] : List alpha -> List alpha
  | [] => []
  | x :: xs =>
      let ys := dedup xs
      if ys.contains x then ys else x :: ys

/-- Realized full-slice image. -/
def syndromeList : List Vec3 := supports.map syndrome
def image : List Vec3 := dedup syndromeList

/-- Exact full-slice fiber cardinality. -/
def fiberCount (v : Vec3) : Nat :=
  (syndromeList.filter fun w => w == v).length

/-- Maximum of a natural list. -/
def maxNat : List Nat -> Nat
  | [] => 0
  | x :: xs => Nat.max x (maxNat xs)

/-- Exact maximum fiber over the realized image. -/
def maxFiber : Nat := maxNat (image.map fiberCount)

/-- The unique doubled target in the fixture. -/
def zeroSyndrome : Vec3 := { x := 0, y := 0, z := 0 }
def doubleTargets : List Vec3 := image.filter fun v => fiberCount v == 2

def collisionA : Support := [1, 3, 4, 5, 9]
def collisionB : Support := [2, 6, 7, 8, 10]

/-- Coordinatewise modular vector operations. -/
def addVec (a b : Vec3) : Vec3 :=
  { x := (a.x + b.x) % p
  , y := (a.y + b.y) % p
  , z := (a.z + b.z) % p }

def subMod (a b : Nat) : Nat := (a + p - (b % p)) % p

def subVec (a b : Vec3) : Vec3 :=
  { x := subMod a.x b.x
  , y := subMod a.y b.y
  , z := subMod a.z b.z }

def scaleVec (c : Nat) (a : Vec3) : Vec3 :=
  { x := (c * a.x) % p
  , y := (c * a.y) % p
  , z := (c * a.z) % p }

/-- Moment column `g(t)=(t,t^2,t^3)`. -/
def momentColumn (t : Nat) : Vec3 :=
  { x := t % p
  , y := (t ^ 2) % p
  , z := (t ^ 3) % p }

/-- Three differences from the base column `g(1)`. -/
def basis1 : Vec3 := subVec (momentColumn 2) (momentColumn 1)
def basis2 : Vec3 := subVec (momentColumn 3) (momentColumn 1)
def basis3 : Vec3 := subVec (momentColumn 4) (momentColumn 1)

/-- Linear combination of the three displayed difference columns. -/
def linComb (c : Vec3) : Vec3 :=
  addVec (scaleVec c.x basis1)
    (addVec (scaleVec c.y basis2) (scaleVec c.z basis3))

/-- Explicit inverse to the difference-column matrix modulo `11`. -/
def inverseCoeffs (v : Vec3) : Vec3 :=
  { x := (4 * v.x + 7 * v.y + 6 * v.z) % p
  , y := (4 * v.x + 9 * v.y + 5 * v.z) % p
  , z := (10 * v.y + 2 * v.z) % p }

/-- All vectors in the ambient `F_11^3`, represented by residues. -/
def residues : List Nat := List.range p
def allVec3 : List Vec3 :=
  residues.flatMap fun a =>
    residues.flatMap fun b =>
      residues.map fun c => { x := a, y := b, z := c }

/-- Executable full-span certificate. -/
def fullSpanCheck : Bool :=
  allVec3.all fun v => linComb (inverseCoeffs v) == v

/-- The generated support slice is exactly `binom(10,5)`. -/
theorem support_count : supports.length = 252 := by native_decide

/-- Every generated support has the intended shape. -/
theorem support_shapes :
    supports.all (fun S => S.length == m && noDuplicates S) = true := by
  native_decide

/-- The realized image has 251 targets. -/
theorem realized_image_count : image.length = 251 := by native_decide

/-- The image representation itself has no duplicate target. -/
theorem realized_image_is_duplicate_free : noDuplicates image = true := by
  native_decide

/-- The exact full-slice maximum fiber is two. -/
theorem max_fiber_eq_two : maxFiber = 2 := by native_decide

/-- Exactly one realized target has two preimages. -/
theorem unique_double_target : doubleTargets = [zeroSyndrome] := by
  native_decide

/-- The two displayed supports are the double zero-syndrome fiber. -/
theorem displayed_collision :
    collisionA != collisionB &&
      syndrome collisionA == zeroSyndrome &&
      syndrome collisionB == zeroSyndrome := by
  native_decide

/-- Cleared-denominator image-normalized Q loss is strictly below two. -/
theorem image_normalized_q_loss_below_two :
    maxFiber * image.length < 2 * supports.length := by
  native_decide

/-- The general two-free-coefficient census is valid on the toy row. -/
theorem two_coefficient_census_bound : maxFiber <= p ^ 2 := by
  native_decide

/-- The displayed generator differences have the intended residue values. -/
theorem basis_values :
    basis1 = { x := 1, y := 3, z := 7 } &&
      basis2 = { x := 2, y := 8, z := 4 } &&
      basis3 = { x := 3, y := 4, z := 8 } := by
  native_decide

/-- The explicit inverse represents every ambient vector. -/
theorem effective_span_is_full : fullSpanCheck = true := by native_decide

/-- The effective ambient group has `11^3=1331` elements. -/
theorem effective_ambient_count : allVec3.length = 1331 := by native_decide

/-- The effective span is already more than five times the realized image. -/
theorem effective_span_over_image_gt_five :
    5 * image.length < allVec3.length := by
  native_decide

end SidonEffectiveImage
