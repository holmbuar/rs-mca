import Std

/-!
# Trace--Vandermonde coherent phase-orbit floor

A stdlib-only exact regression over `F_8 = F_2[x]/(x^3+x+1)`.

The domain is `F_8^×`, the RS parity columns are `(t,t^2,t^3)`, and the
fixed-weight source is the complete weight-two slice.  The syndrome map is
injective.  Nevertheless, the 35 trace characters whose phase support has
weight four are all genuine RS trace--Vandermonde phases and all have the same
fixed-weight coefficient `-3`.  Their cancellation-sensitive coherent sum is
therefore `-105`, so the image-compensated coherent aggregate is `105/64 > 1`.

This module certifies only the exact finite arithmetic and correspondence.
The general `q = 2^s` family theorem is proved in the paired threshold note.
-/

set_option maxRecDepth 32768
set_option maxHeartbeats 0

namespace SidonEffectiveImage.TraceVandermondeCoherentFloor

/-- The `k`th binary digit of a natural number. -/
def bit (a k : Nat) : Nat :=
  (a / (2 ^ k)) % 2

/-- Addition in the polynomial basis of `F_8`. -/
def gfAdd (a b : Nat) : Nat :=
  let r0 := (bit a 0 + bit b 0) % 2
  let r1 := (bit a 1 + bit b 1) % 2
  let r2 := (bit a 2 + bit b 2) % 2
  r0 + 2 * r1 + 4 * r2

/--
Multiplication in `F_2[x]/(x^3+x+1)`.  The reductions are
`x^3 = x+1` and `x^4 = x^2+x`.
-/
def gfMul (a b : Nat) : Nat :=
  let a0 := bit a 0
  let a1 := bit a 1
  let a2 := bit a 2
  let b0 := bit b 0
  let b1 := bit b 1
  let b2 := bit b 2
  let c0 := a0 * b0
  let c1 := a0 * b1 + a1 * b0
  let c2 := a0 * b2 + a1 * b1 + a2 * b0
  let c3 := a1 * b2 + a2 * b1
  let c4 := a2 * b2
  let r0 := (c0 + c3) % 2
  let r1 := (c1 + c3 + c4) % 2
  let r2 := (c2 + c4) % 2
  r0 + 2 * r1 + 4 * r2

def gfSq (a : Nat) : Nat := gfMul a a
def gfCube (a : Nat) : Nat := gfMul (gfSq a) a
def gfFourth (a : Nat) : Nat := gfSq (gfSq a)

def gfPow (a : Nat) : Nat → Nat
  | 0 => 1
  | n + 1 => gfMul (gfPow a n) a

/-- Absolute trace `F_8 -> F_2`. -/
def gfTrace (a : Nat) : Nat :=
  gfAdd (gfAdd a (gfSq a)) (gfFourth a)

structure F8Vec where
  c1 : Nat
  c2 : Nat
  c3 : Nat
  deriving BEq, DecidableEq, Repr

def zeroVec : F8Vec := { c1 := 0, c2 := 0, c3 := 0 }

def vecAdd (u v : F8Vec) : F8Vec :=
  { c1 := gfAdd u.c1 v.c1,
    c2 := gfAdd u.c2 v.c2,
    c3 := gfAdd u.c3 v.c3 }

def vecSum : List F8Vec → F8Vec
  | [] => zeroVec
  | v :: vs => vecAdd v (vecSum vs)

/-- RS parity column `(t,t^2,t^3)`. -/
def column (t : Nat) : F8Vec :=
  { c1 := t, c2 := gfSq t, c3 := gfCube t }

def dot (a v : F8Vec) : Nat :=
  gfAdd (gfAdd (gfMul a.c1 v.c1) (gfMul a.c2 v.c2))
    (gfMul a.c3 v.c3)

/-- All `k`-subsets of a supplied list. -/
def chooseFrom {α : Type} : List α → Nat → List (List α)
  | _, 0 => [[]]
  | [], _ + 1 => []
  | x :: xs, k + 1 =>
      (chooseFrom xs k).map (fun s => x :: s) ++ chooseFrom xs (k + 1)

/-- Executable powerset. -/
def powerset {α : Type} : List α → List (List α)
  | [] => [[]]
  | x :: xs =>
      let tail := powerset xs
      tail ++ tail.map (fun s => x :: s)

def noDuplicates {α : Type} [BEq α] : List α → Bool
  | [] => true
  | x :: xs => !xs.contains x && noDuplicates xs

def sumInt : List Int → Int
  | [] => 0
  | z :: zs => z + sumInt zs

def maxNatList : List Nat → Nat
  | [] => 0
  | z :: zs => Nat.max z (maxNatList zs)

def pairAll {α β : Type} (p : α → β → Bool) : List α → List β → Bool
  | [], [] => true
  | x :: xs, y :: ys => p x y && pairAll p xs ys
  | _, _ => false

def domain : List Nat := [1, 2, 3, 4, 5, 6, 7]
def supports : List (List Nat) := chooseFrom domain 2
def orbitSupports : List (List Nat) := chooseFrom domain 4

def syndrome (S : List Nat) : F8Vec :=
  vecSum (S.map column)

def sourceMass : Nat := supports.length
def realizedImageSize : Nat := supports.length

def fiberSize (target : F8Vec) : Nat :=
  (supports.filter fun S => syndrome S == target).length

def maxFiber : Nat :=
  maxNatList ((supports.map syndrome).map fiberSize)

def singletonFiberCheck : Bool :=
  supports.all fun S => fiberSize (syndrome S) == 1

def syndromeInjectiveCheck : Bool :=
  supports.length == 21 &&
  noDuplicates (supports.map syndrome) &&
  singletonFiberCheck

def differenceGenerators : List F8Vec :=
  (domain.drop 1).map fun t => vecAdd (column t) (column 1)

def differenceSpan : List F8Vec :=
  (powerset differenceGenerators).map vecSum

def differenceSpanCheck : Bool :=
  differenceGenerators.length == 6 &&
  differenceSpan.length == 64 &&
  noDuplicates differenceSpan

def effectiveTargetSize : Nat := differenceSpan.length

def tracePhase (a : F8Vec) (t : Nat) : Nat :=
  gfTrace (dot a (column t))

def phasePattern (a : F8Vec) : List Nat :=
  domain.map (tracePhase a)

def incidencePattern (Y : List Nat) : List Nat :=
  domain.map fun t => if Y.contains t then 1 else 0

/--
A 64-element gauge for all effective trace characters.  In this finite row the
coefficients of `t^2` and `t^3` already realize every even phase pattern.
-/
def traceGaugeCoefficients : List F8Vec :=
  (List.range 8).flatMap fun a2 =>
    (List.range 8).map fun a3 => { c1 := 0, c2 := a2, c3 := a3 }

def tracePatterns : List (List Nat) :=
  traceGaugeCoefficients.map phasePattern

def evenPattern (pattern : List Nat) : Bool :=
  pattern.foldl (fun parity value => (parity + value) % 2) 0 == 0

def traceImageCheck : Bool :=
  traceGaugeCoefficients.length == 64 &&
  tracePatterns.length == 64 &&
  noDuplicates tracePatterns &&
  tracePatterns.all evenPattern

/--
Explicit trace-linear coefficient witnesses for the 35 weight-four effective
characters, in the same order as `orbitSupports`.
-/
def orbitWitnesses : List F8Vec := [
  { c1 := 0, c2 := 7, c3 := 2 },
  { c1 := 0, c2 := 0, c3 := 3 },
  { c1 := 0, c2 := 1, c3 := 4 },
  { c1 := 0, c2 := 2, c3 := 5 },
  { c1 := 0, c2 := 1, c3 := 6 },
  { c1 := 0, c2 := 0, c3 := 1 },
  { c1 := 0, c2 := 3, c3 := 0 },
  { c1 := 0, c2 := 7, c3 := 0 },
  { c1 := 0, c2 := 4, c3 := 1 },
  { c1 := 0, c2 := 5, c3 := 6 },
  { c1 := 0, c2 := 4, c3 := 7 },
  { c1 := 0, c2 := 5, c3 := 0 },
  { c1 := 0, c2 := 6, c3 := 1 },
  { c1 := 0, c2 := 2, c3 := 1 },
  { c1 := 0, c2 := 1, c3 := 0 },
  { c1 := 0, c2 := 0, c3 := 7 },
  { c1 := 0, c2 := 3, c3 := 4 },
  { c1 := 0, c2 := 0, c3 := 5 },
  { c1 := 0, c2 := 1, c3 := 2 },
  { c1 := 0, c2 := 6, c3 := 3 },
  { c1 := 0, c2 := 2, c3 := 0 },
  { c1 := 0, c2 := 3, c3 := 7 },
  { c1 := 0, c2 := 0, c3 := 6 },
  { c1 := 0, c2 := 4, c3 := 6 },
  { c1 := 0, c2 := 7, c3 := 7 },
  { c1 := 0, c2 := 6, c3 := 0 },
  { c1 := 0, c2 := 5, c3 := 3 },
  { c1 := 0, c2 := 6, c3 := 2 },
  { c1 := 0, c2 := 7, c3 := 5 },
  { c1 := 0, c2 := 0, c3 := 4 },
  { c1 := 0, c2 := 0, c3 := 2 },
  { c1 := 0, c2 := 3, c3 := 3 },
  { c1 := 0, c2 := 2, c3 := 4 },
  { c1 := 0, c2 := 5, c3 := 5 },
  { c1 := 0, c2 := 4, c3 := 0 }
]

def phaseOrbitRealizationCheck : Bool :=
  orbitSupports.length == 35 &&
  orbitWitnesses.length == 35 &&
  pairAll (fun Y a => phasePattern a == incidencePattern Y)
    orbitSupports orbitWitnesses

def phaseParityOnSupport (a : F8Vec) (S : List Nat) : Nat :=
  S.foldl (fun parity t => (parity + tracePhase a t) % 2) 0

def rsPhaseTerm (a : F8Vec) (S : List Nat) : Int :=
  if phaseParityOnSupport a S = 0 then 1 else -1

def rsCoefficient (a : F8Vec) : Int :=
  sumInt (supports.map (rsPhaseTerm a))

/--
The effective Fourier span is anchored at `t=1`.  Weight two is even, so the
anchor phase occurs twice and cancels exactly.
-/
def anchoredTracePhase (a : F8Vec) (t : Nat) : Nat :=
  (tracePhase a t + tracePhase a 1) % 2

def anchoredPhaseParityOnSupport (a : F8Vec) (S : List Nat) : Nat :=
  S.foldl (fun parity t => (parity + anchoredTracePhase a t) % 2) 0

def anchoredRsPhaseTerm (a : F8Vec) (S : List Nat) : Int :=
  if anchoredPhaseParityOnSupport a S = 0 then 1 else -1

def anchoredRsCoefficient (a : F8Vec) : Int :=
  sumInt (supports.map (anchoredRsPhaseTerm a))

def anchorTranslationCheck : Bool :=
  orbitWitnesses.all fun a => anchoredRsCoefficient a == rsCoefficient a

def orbitCoefficientCheck : Bool :=
  orbitWitnesses.all fun a => anchoredRsCoefficient a == (-3 : Int)

def coherentSignedSum : Int :=
  sumInt (orbitWitnesses.map anchoredRsCoefficient)

def coherentMagnitude : Nat :=
  Int.natAbs coherentSignedSum

def fieldArithmeticCheck : Bool :=
  (List.range 8).all fun a =>
    decide (gfTrace a < 2) &&
    (List.range 8).all fun b =>
      decide (gfAdd a b < 8) && decide (gfMul a b < 8)

def primitiveCycle : List Nat :=
  (List.range 7).map (gfPow 2)

def primitiveCycleCheck : Bool :=
  primitiveCycle == [1, 2, 4, 3, 6, 7, 5] &&
  gfPow 2 7 == 1 &&
  noDuplicates primitiveCycle

theorem field_arithmetic_exact : fieldArithmeticCheck = true := by decide

theorem primitive_cycle_shape : primitiveCycleCheck = true := by decide

theorem source_mass_exact : sourceMass = 21 := by decide

theorem syndrome_map_injective : syndromeInjectiveCheck = true := by decide

theorem singleton_fibers : singletonFiberCheck = true := by decide

theorem max_fiber_exact : maxFiber = 1 := by decide

theorem realized_image_size_exact : realizedImageSize = 21 := by decide

/-- Exact image-normalized Q equality: `maxFiber = M/L = 1`. -/
theorem image_normalized_q_exact :
    maxFiber * realizedImageSize = sourceMass := by decide

theorem effective_difference_span_exact : differenceSpanCheck = true := by decide

theorem effective_target_size_exact : effectiveTargetSize = 64 := by decide

theorem all_effective_trace_patterns_realized : traceImageCheck = true := by decide

theorem coherent_orbit_size_exact : orbitSupports.length = 35 := by decide

theorem trace_phase_orbit_realized : phaseOrbitRealizationCheck = true := by decide

theorem anchor_translation_exact : anchorTranslationCheck = true := by decide

theorem coherent_orbit_coefficients_exact : orbitCoefficientCheck = true := by decide

theorem coherent_signed_sum_exact : coherentSignedSum = -105 := by decide

theorem coherent_magnitude_exact : coherentMagnitude = 105 := by decide

/-- The source-normalized coherent aggregate is exactly `105/21 = 5`. -/
theorem source_normalized_coherent_exact :
    coherentMagnitude = 5 * sourceMass := by decide

/--
After exact image compensation, the coherent aggregate remains greater than
one: `L*H > A_eff*M`.
-/
theorem image_compensated_coherent_strict :
    effectiveTargetSize * sourceMass <
      realizedImageSize * coherentMagnitude := by decide

/--
Any integer multiplier paying the image-compensated coherent-orbit aggregate
must be at least two in the exact `q=8` falsifier.
-/
theorem coherent_multiplier_floor
    (kappa : Nat)
    (h : realizedImageSize * coherentMagnitude ≤
      kappa * effectiveTargetSize * sourceMass) :
    2 ≤ kappa := by
  rw [realized_image_size_exact, coherent_magnitude_exact,
    effective_target_size_exact, source_mass_exact] at h
  omega

#print axioms syndrome_map_injective
#print axioms image_normalized_q_exact
#print axioms effective_difference_span_exact
#print axioms all_effective_trace_patterns_realized
#print axioms trace_phase_orbit_realized
#print axioms anchor_translation_exact
#print axioms coherent_orbit_coefficients_exact
#print axioms coherent_signed_sum_exact
#print axioms image_compensated_coherent_strict
#print axioms coherent_multiplier_floor

end SidonEffectiveImage.TraceVandermondeCoherentFloor
