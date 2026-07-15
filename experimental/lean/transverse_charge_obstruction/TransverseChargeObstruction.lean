/-!
# Transverse/charge obstruction on the Sidon-paired class (statement stub)

Maps to **hard input 2**: closes BOTH branches of the (NFB) object (#760 Sec 7)
on the Sidon-paired class -- (i) a partition transverse to every prefix-quotient
fiber cannot carry a q=2 failure's charge (chart-free Prop 1), and (ii) no
direct PO4/signed payment of the packet or of its moderately-unpaired slice
exists at ANY moment order (Theorem 4).  With the fiber-rooted semantic cap
(Theorem 2) this makes the five-precursor form of avdeevvadim's #716 Sec-6
semantic-or-signed decomposition UNREALIZABLE on the class at the canonical
q=2 rooting; #716 Sec 7.1's sixth (packet-scale) alternative is FORCED.  The
surviving structure is the resonant spectrum: the half-frequency j* = (c-1)/2
satisfies the exact antipodal congruence and |hat f(j*)| >= 0.70 M.

Note:     `experimental/notes/thresholds/transverse_charge_obstruction_sidon_paired.md`.
Verifier: `experimental/scripts/verify_transverse_charge_obstruction.py`
          (281/281, tamper 4/4).

Class (#739, DannyExperiments-#749-corrected hypotheses): `P = {base^i : i<B}`
2-superincreasing (hence B[+-2]-dissociated), `c = 2 sum P + 1`,
`T = P u (c-P)`, `a = B`, `Phi = subset sum`; `L = (3^B+1)/2`, `M = C(2B,B)`,
`f_max = C(B,B/2)`, `M2 = sum_s C(B,s) 2^s C(B-s,(B-s)/2)^2`.

Analytic results (PROVED in note + Python verifier; NOT in Lean):
  Prop 1   (chart-free)  transverse pieces: sum c_i <= sqrt(K W M)
           <= e^{-eta N} Omega_+ under compatibility -- charge-trivial.
  Thm 2    (Sidon-paired, any failing band, q=2)  fiber-rooted semantic
           pieces: c_i <= f_max sqrt(delta_A); total semantic
           <= e^{-(eta+kappa)N} Omega_+, kappa = ln(2/sqrt 3)/2 per N.
  Thm 3    assembly: NO (FR)-decomposition attains sum c_i = Omega_+.
  Thm 4    direct branch: R_q(f) >= (L^{1/2}/M) ||h_occ||_2 for every q >= 2
           (occupied-support transfer), = e^{eta N}; same for the slice.

This module is the DECIDABLE arithmetic shadow (stdlib-only `native_decide`,
no mathlib, no `sorry`) of the integer/combinatorial parts.
-/

namespace TransverseChargeObstruction

/-! ## 0. Exact combinatorial scalars. -/

/-- `binom n k = C(n,k)` via the running product `prod_{i<k} (n-i)/(i+1)`. -/
def binom (n k : Nat) : Nat :=
  (List.range k).foldl (fun acc i => acc * (n - i) / (i + 1)) 1

/-- Realized image `L = (3^B+1)/2` (B even; intrinsic, base-independent). -/
def realizedImage (B : Nat) : Nat := (3 ^ B + 1) / 2

/-- Full slice `M = C(2B,B)`. -/
def slice (B : Nat) : Nat := binom (2 * B) B

/-- Central (heaviest) fiber `f_max = C(B,B/2)`. -/
def maxFiber (B : Nat) : Nat := binom B (B / 2)

/-- Ambient modulus `c = 2*sum_{i<B} base^i + 1`; for base 3 this is `3^B`. -/
def ambientMod (base B : Nat) : Nat := 2 * ((base ^ B - 1) / (base - 1)) + 1

/-- Collision count `M2 = sum_{s == B mod 2} C(B,s) 2^s C(B-s,(B-s)/2)^2`
    (the exact `l^2` mass of the fiber profile; `~ 6^B/poly`). -/
def collisionMass (B : Nat) : Nat :=
  (List.range (B + 1)).foldl
    (fun acc s =>
      if s % 2 == B % 2 then
        acc + binom B s * 2 ^ s * (binom (B - s) ((B - s) / 2)) ^ 2
      else acc) 0

theorem ambient_base3_is_pow : ambientMod 3 8 = 3 ^ 8 := by native_decide

/-! ## 1. The staircase identities (V1's closed forms, pinned). -/

/-- `sum_s C(B,s) 2^s C(B-s,(B-s)/2) = C(2B,B)` at `B = 6, 8` (mass identity). -/
theorem staircase_mass_B6 :
    (List.range 7).foldl
      (fun acc s => if s % 2 == 0 then
        acc + binom 6 s * 2 ^ s * binom (6 - s) ((6 - s) / 2) else acc) 0
    = slice 6 := by native_decide

theorem staircase_mass_B8 :
    (List.range 9).foldl
      (fun acc s => if s % 2 == 0 then
        acc + binom 8 s * 2 ^ s * binom (8 - s) ((8 - s) / 2) else acc) 0
    = slice 8 := by native_decide

/-- Pinned collision masses (match the Python verifier and the JSON cert). -/
theorem collision_pinned : collisionMass 6 = 3584 ∧ collisionMass 8 = 97444 := by
  native_decide

/-! ## 2. The payment-gap window: heavy enough to fail, too light to pay.
    `f_max * L >= 2M` (heavy fibers exist, #739's point-mass failures) AND
    `f_max^2 * L < M^2` (no fiber reaches the q=2 carrying scale `M/sqrt L`). -/

theorem window_B8 :
    maxFiber 8 * realizedImage 8 ≥ 2 * slice 8 ∧
    (maxFiber 8) ^ 2 * realizedImage 8 < (slice 8) ^ 2 := by native_decide

theorem window_B16 :
    maxFiber 16 * realizedImage 16 ≥ 2 * slice 16 ∧
    (maxFiber 16) ^ 2 * realizedImage 16 < (slice 16) ^ 2 := by native_decide

theorem window_B32 :
    maxFiber 32 * realizedImage 32 ≥ 2 * slice 32 ∧
    (maxFiber 32) ^ 2 * realizedImage 32 < (slice 32) ^ 2 := by native_decide

/-- The gap RATE: `f_max sqrt(L)/M` decays at least like `(7/8)^{B/2}`
    (integer cross-multiplied form at `B = 16`). -/
theorem window_rate_B16 :
    8 ^ 16 * (maxFiber 16) ^ 2 * realizedImage 16
      < 7 ^ 16 * (slice 16) ^ 2 := by native_decide

/-! ## 3. The q=2 band excess is exponential (Theorem 4's finite shadow):
    `R_2^2 = L (M2 - M^2/c)/M^2 > 1`, cross-multiplied over `Z`
    (base 3, `c = 3^B`): `L * (M2 * c - M^2) > M^2 * c`. -/

theorem excess_B6 :
    realizedImage 6 * (collisionMass 6 * 3 ^ 6 - (slice 6) ^ 2)
      > (slice 6) ^ 2 * 3 ^ 6 := by native_decide

theorem excess_B8 :
    realizedImage 8 * (collisionMass 8 * 3 ^ 8 - (slice 8) ^ 2)
      > (slice 8) ^ 2 * 3 ^ 8 := by native_decide

/-- The point-mass term's moment-order sign flip (#728's `q = 2.709` constant,
    recovered): at `B = 16`, `L f_max^2 < M^2` (q=2) yet `L^3 f_max^4 > M^4`
    (q=4) -- between them the single top fiber turns exponential. -/
theorem pointmass_sign_flip_B16 :
    realizedImage 16 * (maxFiber 16) ^ 2 < (slice 16) ^ 2 ∧
    (realizedImage 16) ^ 3 * (maxFiber 16) ^ 4 > (slice 16) ^ 4 := by
  native_decide

/-! ## 4. The antipodal congruence behind the half-frequency resonance:
    `j* * A_i mod c = (c - A_i)/2` for `j* = (c-1)/2`, i.e.
    `2 * (j* * 3^i % c) + 3^i = c`, for ALL `i < B` (base 3, `B = 8`;
    the same congruence holds for every base -- V4 checks base 5). -/

theorem antipodal_congruence_B8 :
    (List.range 8).all
      (fun i => 2 * ((3280 * 3 ^ i) % 6561) + 3 ^ i == 6561) = true := by
  native_decide

/-- `j* = (c-1)/2` for `c = 3^8` is `3280` (digits `11111111` in base 3). -/
theorem jstar_B8 : (3 ^ 8 - 1) / 2 = 3280 := by native_decide

end TransverseChargeObstruction
