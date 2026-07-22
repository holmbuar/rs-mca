import AsymptoticSpine.EffectiveClosure
import AsymptoticSpine.UniformClosedLedger
import M31QRootedShell.Deployed
import Std

set_option maxRecDepth 1000000
set_option maxHeartbeats 0

/-!
# M31 C9 scale step: sixteen deployed roots and the first residual doubling

This stdlib-only module scales the exact finite calibration of upstream PR #1027
from eight roots in two complete `T_4` blocks to sixteen roots in four complete
`T_4` blocks.  The domain is re-derived from the same norm-one generator, the
complete weight-eight slice is enumerated, and the exact C1 antipodal-quotient
supports are deleted before the residual prefix fibers are counted.

The residual is no longer injective.  Its exact maximum fiber is two, attained
on 384 keys.  Every doubled residual key is a complete-`T_4` block swap, and the
first such key in ascending support-mask order is printed explicitly.  Thus the
minimal image-normalized residual loss grows from one in the eight-root packet
to two here, although the literal integral natural-scale inequality remains
`2 ≤ 1 * 2`.

PROOF BOUNDARY.  The exhaustive 12,870-support census, the key-sorted table,
and the exactness of the 384-fold block-swap classification are the authority
of the independent stdlib Python verifier and the hash-pinned JSON certificate
(replay commands in the threshold note).  This module kernel-certifies the
statement-level skeleton: the generator derivation of all sixteen deployed
roots, the antipodal and complete-`T_4` block structure, the six-fiber of the
two-block key `(0,4,0)` and its C1 ownership, the first residual doubled key
as an explicit complete-block swap surviving C1, every internal arithmetic
identity of the frozen census (binomial anchors, histogram sums, block-swap
counting), and the deployed budget and sharpness comparisons.  It does not
enumerate the weight-eight slice.

This is a finite Q-support certificate.  It does not construct received-line
witnesses, an `(SE2)` projection, a slope payment, a global first-match atlas,
profile multiplicity, add-back, `UNIF`, or a deployed row certificate.
-/

namespace SidonEffectiveImage.M31C9ScaleStep

open AsymptoticSpine

abbrev Support := Nat

/-- Three first power sums, represented by canonical Mersenne-prime residues. -/
structure PrefixKey where
  p1 : Nat
  p2 : Nat
  p3 : Nat
  deriving Repr, BEq, DecidableEq

/-- Exact deployed Mersenne-31 list-row calibration inherited from integrated
`M31QRootedShell.Deployed`. -/
def fieldPrime : Nat := M31QRootedShell.Deployed.pM31
def deployedPrefixDepth : Nat := M31QRootedShell.Deployed.w
def deployedBudget : Nat := M31QRootedShell.Deployed.Bstar
def deployedLength : Nat := 2 ^ 21
def deployedComplementWeight : Nat := M31QRootedShell.Deployed.listM
def fixedOutsideWeight : Nat := deployedComplementWeight - 8
def outsideAvailable : Nat := deployedLength - 16

/-- Quadratic extension arithmetic `a+b*i`, with `i^2=-1`, represented by
canonical natural residues. -/
structure Fp2 where
  re : Nat
  im : Nat
  deriving Repr, BEq, DecidableEq

def fp2One : Fp2 := { re := 1, im := 0 }

def fp2Mul (a b : Fp2) : Fp2 :=
  { re := ((a.re * b.re) % fieldPrime + fieldPrime -
      (a.im * b.im) % fieldPrime) % fieldPrime
  , im := ((a.re * b.im) % fieldPrime +
      (a.im * b.re) % fieldPrime) % fieldPrime }

def fp2Conj (a : Fp2) : Fp2 :=
  { re := a.re % fieldPrime
  , im := (fieldPrime - a.im % fieldPrime) % fieldPrime }

/-- Repeated squaring: `fp2PowTwo e u = u^(2^e)`. -/
def fp2PowTwo : Nat → Fp2 → Fp2
  | 0, u => u
  | e + 1, u => fp2PowTwo e (fp2Mul u u)

/-- Bitwise exponentiation for exponents below `2^31`. -/
def fp2Pow31 (u : Fp2) (e : Nat) : Fp2 :=
  (List.range 31).foldl
    (fun acc i =>
      if Nat.testBit e i then fp2Mul acc (fp2PowTwo i u) else acc)
    fp2One

/-- Stereographic norm-one generator used in #1027. -/
def normOneGenerator : Fp2 :=
  { re := 1717986917, im := 1288490189 }

/-- Four odd base exponents; adjoining the four `2^29` translates gives four
complete `T_4` blocks. -/
def baseExponents : List Nat := [256, 768, 1280, 1792]

def domainExponents : List Nat :=
  baseExponents.flatMap fun base =>
    (List.range 4).map fun j => base + j * 2 ^ 29

def derivedDomain : List Nat :=
  domainExponents.map fun e => (fp2Pow31 normOneGenerator e).re

/-- Sixteen actual deployed `T_(2^21)` roots, ordered by four complete `T_4`
blocks. -/
def domain : List Nat :=
  [ 434373082, 614288294, 1713110565, 1533195353
  , 1984437538, 380812851, 163046109, 1766670796
  , 1244279234, 907334541, 903204413, 1240149106
  , 2066813671, 1590029158, 80669976, 557454489 ]

/-- Duplicate-free executable predicate used only for the sixteen-point domain. -/
def noDuplicates [BEq α] : List α → Bool
  | [] => true
  | x :: xs => xs.all (fun y => !(y == x)) && noDuplicates xs

/-- `T_(2n)(x)=2T_n(x)^2-1`, evaluated modulo the Mersenne prime. -/
def chebyshevDouble (x : Nat) : Nat :=
  (2 * (x % fieldPrime) * (x % fieldPrime) + (fieldPrime - 1)) % fieldPrime

/-- Evaluate `T_(2^e)` by repeated doubling. -/
def chebyshevPowTwo : Nat → Nat → Nat
  | 0, x => x % fieldPrime
  | e + 1, x => chebyshevPowTwo e (chebyshevDouble x)

/-- Hamming weight of the low sixteen bits of a support mask. -/
def maskWeight (mask : Support) : Nat :=
  (List.range 16).foldl
    (fun acc i => if Nat.testBit mask i then acc + 1 else acc) 0

def allMasks : List Support := List.range (2 ^ 16)

def fullSupports : List Support :=
  allMasks.filter fun mask => maskWeight mask == 8

/-- Sum selected domain values to the `e`-th power modulo the row prime. -/
def sumPowerMod (e : Nat) (mask : Support) : Nat :=
  ((List.range 16).zip domain).foldl
    (fun acc pair =>
      if Nat.testBit mask pair.1 then
        (acc + pair.2 ^ e % fieldPrime) % fieldPrime
      else acc)
    0

def prefixKey (mask : Support) : PrefixKey :=
  { p1 := sumPowerMod 1 mask
  , p2 := sumPowerMod 2 mask
  , p3 := sumPowerMod 3 mask }

/-- The eight antipodal pairs, two in each `T_4` block. -/
def antipodalPairs : List (Nat × Nat) :=
  [(0, 2), (1, 3), (4, 6), (5, 7),
   (8, 10), (9, 11), (12, 14), (13, 15)]

/-- C1 owns exactly the weight-eight unions of four complete antipodal pairs. -/
def c1Owned (mask : Support) : Bool :=
  antipodalPairs.all fun pair =>
    Nat.testBit mask pair.1 == Nat.testBit mask pair.2

def residualSupports : List Support :=
  fullSupports.filter fun mask => !c1Owned mask

/-- Local exact prefix fibers, definitionally using the integrated `mapFiber`. -/
def fullPrefixFiber (z : PrefixKey) : List Support :=
  mapFiber fullSupports prefixKey z

def residualPrefixFiber (z : PrefixKey) : List Support :=
  mapFiber residualSupports prefixKey z

/-- Local copy of the exact pre-C9 constructor grammar. -/
inductive ScopedPreC9Owner where
  | c1 | c2 | c3 | c4 | c5 | c6 | c7 | c8
  deriving Repr, BEq, DecidableEq

def earlierOwner {Owner : Type} (c1 : Owner) (mask : Support) : Option Owner :=
  if c1Owned mask then some c1 else none

def scopedEarlierOwner : Support → Option ScopedPreC9Owner :=
  earlierOwner .c1

def IsExactOwnerComplement {Owner : Type} [DecidableEq Owner]
    (owner : Support → Option Owner) : Prop :=
  ∀ mask : Support,
    mask ∈ residualSupports ↔ mask ∈ fullSupports ∧ owner mask = none

theorem residual_exact {Owner : Type} [DecidableEq Owner] (c1 : Owner) :
    IsExactOwnerComplement (earlierOwner c1) := by
  intro mask
  unfold residualSupports earlierOwner
  simp only [List.mem_filter]
  cases h : c1Owned mask <;> simp [h]

theorem scoped_residual_exact :
    IsExactOwnerComplement scopedEarlierOwner := by
  unfold scopedEarlierOwner
  exact residual_exact ScopedPreC9Owner.c1

/-- Two-block key and its six full-slice supports (pairs of complete blocks). -/
def fullSixKey : PrefixKey := { p1 := 0, p2 := 4, p3 := 0 }

def fullSixMasks : List Support :=
  [255, 3855, 4080, 61455, 61680, 65280]

/-- First residual collision in ascending support-mask order. -/
def growthKey : PrefixKey :=
  { p1 := 826664565, p2 := 1588616718, p3 := 1026140363 }

def growthLeft : Support := 5903
def growthRight : Support := 6128
def growthRemainder : Support := 5888

def compilerLoss : Nat := 1
def naturalScale : Nat := 2

/-- The four complete `T_4` block masks. -/
def blockMasks : List Support := [15, 240, 3840, 61440]

/-- Frozen census constants; authority = verifier + certificate digests. -/
def fullMass : Nat := 12870
def fullImageCard : Nat := 12457
def fullSingletons : Nat := 12048
def fullDoubles : Nat := 408
def fullSixes : Nat := 1
def c1OwnedCount : Nat := 70
def residualMass : Nat := 12800
def residualImageCard : Nat := 12416
def residualSingletons : Nat := 12032
def residualDoubles : Nat := 384
def residualMaxFiber : Nat := 2

/-- Executable binomial coefficient, used only for the two anchors. -/
def binomial : Nat → Nat → Nat
  | _, 0 => 1
  | 0, _ + 1 => 0
  | n + 1, k + 1 => binomial n k + binomial n (k + 1)

theorem generator_norm_one :
    fp2Mul normOneGenerator (fp2Conj normOneGenerator) = fp2One := by decide

theorem generator_half_order :
    fp2PowTwo 30 normOneGenerator =
      ({ re := fieldPrime - 1, im := 0 } : Fp2) := by decide

theorem generator_full_order :
    fp2PowTwo 31 normOneGenerator = fp2One := by decide

theorem domain_derived_from_generator : derivedDomain = domain := by decide

theorem domain_nodup : noDuplicates domain = true := by decide

theorem domain_points_are_deployed_roots :
    domain.all (fun x => chebyshevPowTwo 21 x == 0) = true := by decide

theorem antipodal_pairs_exact :
    antipodalPairs.all (fun pair =>
      ((domain.getD pair.1 0 + domain.getD pair.2 0) % fieldPrime == 0)) =
      true := by decide

/-- The four printed `T_4` block values, one per complete block. -/
theorem t4_blocks_exact :
    ((domain.take 4).all (fun x => chebyshevPowTwo 2 x == 1884637334) &&
     ((domain.drop 4).take 4).all (fun x => chebyshevPowTwo 2 x == 51044589) &&
     ((domain.drop 8).take 4).all (fun x => chebyshevPowTwo 2 x == 1916935773) &&
     (domain.drop 12).all (fun x => chebyshevPowTwo 2 x == 116752674)) =
      true := by decide

/-- Block masks are the complete weight-four `T_4` blocks in mask form. -/
theorem block_masks_exact :
    blockMasks = [15, 240, 3840, 61440] ∧
    blockMasks.all (fun b => maskWeight b == 4) = true := by
  exact ⟨rfl, by decide⟩

/-- The six two-block unions all realize the key `(0,4,0)` and are C1-owned. -/
theorem six_fiber_two_block_c1 :
    fullSixMasks.all (fun mask =>
      (maskWeight mask == 8) &&
      (prefixKey mask == fullSixKey) &&
      c1Owned mask) = true := by decide

theorem six_fiber_nodup : noDuplicates fullSixMasks = true := by decide

/-- The first residual doubled key: an explicit complete-block swap that
survives C1.  `growthLeft` and `growthRight` share the fixed remainder and
differ by swapping block one for block two. -/
theorem growth_pair_block_swap :
    growthLeft = 15 ||| growthRemainder ∧
    growthRight = 240 ||| growthRemainder ∧
    (15 &&& growthRemainder) = 0 ∧
    (240 &&& growthRemainder) = 0 := by decide

theorem growth_pair_distinct_weight_eight :
    (growthLeft != growthRight) &&
    (maskWeight growthLeft == 8) &&
    (maskWeight growthRight == 8) = true := by decide

theorem growth_pair_survives_c1 :
    (!c1Owned growthLeft && !c1Owned growthRight) = true := by decide

theorem growth_pair_collides :
    (prefixKey growthLeft == growthKey) &&
    (prefixKey growthRight == growthKey) = true := by decide

/-- Every complete block has first-three-power-sum key `(0,2,0)`. -/
theorem t4_prefix_keys_equal :
    blockMasks.all (fun b =>
      prefixKey b == ({ p1 := 0, p2 := 2, p3 := 0 } : PrefixKey)) = true := by
  decide

/-- Binomial anchors for the frozen census masses. -/
theorem binomial_anchors :
    binomial 16 8 = fullMass ∧ binomial 8 4 = c1OwnedCount ∧
    binomial 4 2 = 6 := by decide

/-- Internal arithmetic coherence of the frozen census. -/
theorem census_coherence :
    fullMass = residualMass + c1OwnedCount ∧
    fullSingletons + 2 * fullDoubles + 6 * fullSixes = fullMass ∧
    fullSingletons + fullDoubles + fullSixes = fullImageCard ∧
    residualSingletons + 2 * residualDoubles = residualMass ∧
    residualSingletons + residualDoubles = residualImageCard ∧
    6 * 68 = fullDoubles ∧
    fullDoubles - 6 * 4 = residualDoubles := by decide

/-- Sharpness: image-normalized loss one fails, loss two holds exactly, and
the literal integral field is unchanged. -/
theorem sharpness_bracket :
    residualMass < residualMaxFiber * residualImageCard ∧
    residualMaxFiber * residualImageCard ≤ 2 * residualMass ∧
    residualMaxFiber ≤ compilerLoss * naturalScale := by decide

theorem deployed_dimensions :
    fieldPrime = 2147483647 ∧
    deployedPrefixDepth = 67447 ∧
    deployedBudget = 16777215 ∧
    deployedComplementWeight = 981129 ∧
    fixedOutsideWeight = 981121 ∧
    outsideAvailable = 2097136 ∧
    fixedOutsideWeight ≤ outsideAvailable ∧
    residualMaxFiber ≤ deployedBudget := by decide

#print axioms generator_norm_one
#print axioms generator_full_order
#print axioms domain_derived_from_generator
#print axioms domain_nodup
#print axioms domain_points_are_deployed_roots
#print axioms antipodal_pairs_exact
#print axioms t4_blocks_exact
#print axioms scoped_residual_exact
#print axioms six_fiber_two_block_c1
#print axioms growth_pair_block_swap
#print axioms growth_pair_survives_c1
#print axioms growth_pair_collides
#print axioms t4_prefix_keys_equal
#print axioms binomial_anchors
#print axioms census_coherence
#print axioms sharpness_bracket
#print axioms deployed_dimensions

end SidonEffectiveImage.M31C9ScaleStep
