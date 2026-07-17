/-!
# PROP-TAIL reduction: statement-level kernel checks

Statement-level Lean layer for the (PROP-TAIL) discharge: the claim that the
realized cross-child spread `rho_prop@i<17(j) <= 1.02560749` persists for all
`j > 60` (equivalently, the measured monotone decay of the operative-window
sibling ratio spread continues past the certified base). This module is the
DECIDABLE/ELEMENTARY skeleton (stdlib-only, no mathlib, no `sorry`, no
analytic content): it kernel-checks the exact/finite arithmetic that the
discharge leans on, and states plainly what it does NOT certify.

Five independent items, each `PropTail`-prefixed:

1. `poly_identity_coeffs` — the ring identity
   `75*(1-x^2) - (6+3x)^2 = -3*(2x-1)*(14x+13)`, checked as an equality of
   little-endian `Int` coefficient lists via `decide`.
2. `sign_factor_nonneg` / `window_ineq_cleared` — the sign corollary: on the
   domain `1/2 <= x <= 1` (denominator-cleared, `x = p/q`), the factor
   `(2x-1)(14x+13) >= 0`, hence `75*(1-x^2) <= (6+3x)^2`.
3. `window_factor_le_bound` — the window constant `289/256 <= 57/50`,
   denominator-cleared to `289*50 <= 57*256`.
4. `gateRows` / `gateRows_below_target` / `gateRows_strict_decreasing` — the
   deep-grid `rho_prop@i<17(j)` table, transcribed to exact rationals at
   printed precision, with a kernel-checked threshold + strict-monotonicity
   predicate.
5. `rho_prop_endpoint_48_below_target` / `rho_prop_endpoint_60_below_target` /
   `v17_above_before_62` / `v17_below_from_62` — the named `j=48,60`
   endpoints and the `V_17` vs. `tau*` crossover-at-`n=62` table check.

**What is certified:** exact integer/rational arithmetic, kernel-checked by
`decide` (no `native_decide` needed — every check here is small). Every
`List`-valued table is a literal transcription of numbers already printed by
the project's numeric verifier / lab scripts; the theorems below check the
transcribed table's INTERNAL consistency (thresholds, monotonicity), not the
correctness of the floating-point computation that produced the printed
decimals.

**What stays informal (analytic, out of scope):** the trigonometric
reduction `theta~(t) = sqrt3 sin(2 pi t/3) / (6+3 cos(2 pi t/3))`, the
substitution `x = cos(2 pi t/3)`, the squaring step turning
`theta~(t) <= 1/5` into the polynomial inequality of item 2, the value of
`tau* = 3*log(1.02560749...)` (transcendental), and every contraction-rate /
Birkhoff / CLT argument in the source note. None of that is proved or
assumed here — only the downstream exact/finite arithmetic is.

Note:     `experimental/notes/thresholds/dense_shell_inv_tail_closure.md` S7.
Verifier: `experimental/scripts/verify_dense_shell_inv_tail_closure.py`, gate V13.
Predecessor package (same conventions, template for this one):
          `experimental/lean/inv_tail_closure/`.
-/

namespace PropTail

/- ------------------------------------------------------------------ -/
/- 1. Coefficient-list polynomial machinery (little-endian, `Int`)     -/
/-
   Redeclared here (rather than imported) to keep this package
   dependency-free, following the same convention as the predecessor
   package `inv_tail_closure` (`padd`/`pscale`/`pmul`/`ptrim` on
   little-endian `List Int` coefficient lists: index `i` = coefficient of
   `x^i`; `ptrim` drops trailing zeros for canonical comparison).
-/

def padd : List Int → List Int → List Int
  | [], q => q
  | p, [] => p
  | a :: p, b :: q => (a + b) :: padd p q

def pscale (c : Int) (p : List Int) : List Int := p.map (c * ·)

def pmul : List Int → List Int → List Int
  | [], _ => []
  | a :: p, q => padd (pscale a q) (0 :: pmul p q)

def ptrim (p : List Int) : List Int :=
  (p.reverse.dropWhile (· == 0)).reverse

/-- The indeterminate `x`, as a coefficient list (`0 + 1*x`). -/
def xPoly : List Int := [0, 1]

/- ------------------------------------------------------------------ -/
/- 2. THE POLYNOMIAL IDENTITY — the heart of `theta~ <= 1/5`.          -/

/-- `75*(1 - x^2) - (6 + 3x)^2`, built the same way the surface formula
reads: `75*(1 - x*x)` minus `(6+3x)*(6+3x)`. -/
def lhsPoly : List Int :=
  padd (pscale 75 (padd [1] (pscale (-1) (pmul xPoly xPoly))))
       (pscale (-1) (pmul (padd [6] (pscale 3 xPoly)) (padd [6] (pscale 3 xPoly))))

/-- `-3*(2x - 1)*(14x + 13)`. -/
def rhsPoly : List Int :=
  pscale (-3) (pmul (padd [-1] (pscale 2 xPoly)) (padd [13] (pscale 14 xPoly)))

/-- **The ring identity.** `75*(1-x^2) - (6+3x)^2 = -3*(2x-1)*(14x+13)` as
formal `Int`-coefficient polynomials in one indeterminate: both sides
normalize (`ptrim`) to the coefficient list `[39, -36, -84]`
(`39 - 36x - 84x^2`). Certified: the coefficient-level identity, by kernel
computation (`decide`) on the explicit list representation — not a claim
about any particular numeric `x`. This is `theta~(t) <= 1/5` post-squaring,
`x = cos(2 pi t/3)`; the trig substitution and the squaring step are
ANALYTIC and are not part of this statement. -/
theorem poly_identity_coeffs : ptrim lhsPoly = ptrim rhsPoly := by decide

/- ------------------------------------------------------------------ -/
/- 3. THE SIGN COROLLARY — denominator-cleared, `x = p / q`, `q > 0`.  -/
/-
   `hlo : q <= 2*p` and `hhi : p <= q` are the cleared forms of
   `1/2 <= x` and `x <= 1` (the domain `[1/2, cos(pi/9)]` is a subset of
   `[1/2, 1]`, so proving the corollary on the wider `[1/2,1]` covers it).
   `hhi` is not needed by the algebra below (`x >= 1/2` alone forces both
   factors nonneg) but is kept as a hypothesis to match the stated domain
   honestly; it is intentionally unused (`_hhi` downstream).
-/

/-- **The sign corollary, part (a).** With `x = p/q`, `q > 0`: on
`1/2 <= x` (`q <= 2p`), the factor `(2x-1)(14x+13)` is nonneg, cleared to
`(2p-q)(14p+13q) >= 0`. Elementary: `2p-q >= 0` directly from `hlo`; `p > 0`
follows from `hlo` and `q > 0`, so `14p+13q > 0`. Both factors nonneg, hence
the product is nonneg (`Int.mul_nonneg`). -/
theorem sign_factor_nonneg (p q : Int) (hq : 0 < q) (hlo : q <= 2 * p)
    (_hhi : p <= q) :
    0 <= (2 * p - q) * (14 * p + 13 * q) := by
  have h1 : 0 <= 2 * p - q := by omega
  have hp : 0 < p := by omega
  have h2 : 0 <= 14 * p + 13 * q := by omega
  exact Int.mul_nonneg h1 h2

/-- **The sign corollary, part (b) — the certified inequality.** With
`x = p/q`, `q > 0`, on `1/2 <= x <= 1`: `75*(1-x^2) <= (6+3x)^2`, cleared
(scaled by `q^2 > 0`) to `75*(q^2-p^2) <= (6q+3p)^2`. Proved from part (a)
via the homogeneous identity
`(6q+3p)^2 - 75*(q^2-p^2) = 3*((2p-q)(14p+13q))` (an independent,
denominator-cleared restatement of `poly_identity_coeffs`, expanded
directly here by elementary `Int` rewriting rather than routed through the
coefficient-list form, to avoid an extra polynomial-evaluation bridge).
NOT certified: that `x = cos(2 pi t/3)` for the operative `t`, or that
squaring `theta~(t) <= 1/5` is valid (both analytic, both out of scope) —
only the resulting polynomial inequality on `x` is kernel-checked. -/
theorem window_ineq_cleared (p q : Int) (hq : 0 < q) (hlo : q <= 2 * p)
    (hhi : p <= q) :
    75 * (q * q - p * p) <= (6 * q + 3 * p) * (6 * q + 3 * p) := by
  have hsign := sign_factor_nonneg p q hq hlo hhi
  have hid : (6 * q + 3 * p) * (6 * q + 3 * p) - 75 * (q * q - p * p) =
      3 * ((2 * p - q) * (14 * p + 13 * q)) := by
    simp [Int.mul_add, Int.add_mul, Int.mul_sub, Int.sub_mul, Int.neg_mul,
      Int.mul_neg, Int.mul_assoc, Int.mul_comm, Int.mul_left_comm]
    have e1 : q * (q * (75 : Int)) = 75 * (q * q) := by
      rw [← Int.mul_assoc, Int.mul_comm (q * q) 75]
    have e2 : q * (q * (36 : Int)) = 36 * (q * q) := by
      rw [← Int.mul_assoc, Int.mul_comm (q * q) 36]
    have e3 : q * (q * (39 : Int)) = 39 * (q * q) := by
      rw [← Int.mul_assoc, Int.mul_comm (q * q) 39]
    have e4 : p * (p * (75 : Int)) = 75 * (p * p) := by
      rw [← Int.mul_assoc, Int.mul_comm (p * p) 75]
    have e5 : p * (p * (9 : Int)) = 9 * (p * p) := by
      rw [← Int.mul_assoc, Int.mul_comm (p * p) 9]
    have e6 : p * (p * (84 : Int)) = 84 * (p * p) := by
      rw [← Int.mul_assoc, Int.mul_comm (p * p) 84]
    have e7 : p * (q * (18 : Int)) = 18 * (p * q) := by
      rw [← Int.mul_assoc, Int.mul_comm (p * q) 18]
    have e8 : p * (q * (42 : Int)) = 42 * (p * q) := by
      rw [← Int.mul_assoc, Int.mul_comm (p * q) 42]
    have e9 : p * (q * (78 : Int)) = 78 * (p * q) := by
      rw [← Int.mul_assoc, Int.mul_comm (p * q) 78]
    rw [e1, e2, e3, e4, e5, e6, e7, e8, e9]
    generalize q * q = A
    generalize p * p = B
    generalize p * q = C
    omega
  omega

/- ------------------------------------------------------------------ -/
/- 4. THE WINDOW CONSTANT.                                             -/

/-- The child-window factor bound: `V_18/V_17 -> 289/256 = 1.1289` is
covered by the rational threshold `57/50 = 1.14`, denominator-cleared
(`289*50 <= 57*256`, i.e. `14450 <= 14592`). Certified: this single
rational-comparison fact, by `decide`. NOT certified: that `289/256` is
actually the limiting window ratio, or that `57/50` is a valid bound over
the full deep grid (both are modeling claims from the source note; this
theorem only certifies the arithmetic fact about the two named
constants). -/
theorem window_factor_le_bound : (289 * 50 : Nat) <= 57 * 256 := by decide

/- ------------------------------------------------------------------ -/
/- 5. THE GATE TABLE — deep-grid `rho_prop@i<17(j)`, exact rationals.   -/
/-
   Each row's value is the printed decimal `rho_prop@i<17(j)` (7 digits
   after the point) transcribed as an exact numerator over the common
   denominator `10^8` (matching the target's 8-digit precision): e.g.
   `1.0255905 -> rhoPropNum = 102559050` (`= 1.02559050 * 10^8`). COMPUTED
   float-derived values transcribed at printed precision — the theorems
   below check the TABLE's internal consistency (threshold + strict
   monotonicity), not the floating computation that produced the decimals.
-/

/-- One deep-grid row: level `j` and `rho_prop@i<17(j)` as a numerator
over the implicit denominator `10^8`. -/
structure GateRow where
  level : Nat
  rhoPropNum : Nat
  deriving DecidableEq, Repr

/-- The deep-grid table, `j = 48` through `300`; shipped gate V13 covers
`{48,50,55,60}`, this extends the same measurement to the deeper grid. -/
def gateRows : List GateRow :=
  [ { level := 48,  rhoPropNum := 102559050 }
  , { level := 50,  rhoPropNum := 102352050 }
  , { level := 55,  rhoPropNum := 101932970 }
  , { level := 60,  rhoPropNum := 101617140 }
  , { level := 70,  rhoPropNum := 101180630 }
  , { level := 80,  rhoPropNum := 100900050 }
  , { level := 100, rhoPropNum := 100572970 }
  , { level := 128, rhoPropNum := 100348300 }
  , { level := 160, rhoPropNum := 100222350 }
  , { level := 200, rhoPropNum := 100142050 }
  , { level := 240, rhoPropNum := 100098530 }
  , { level := 300, rhoPropNum := 100063000 } ]

/-- The (PROP-TAIL) target `1.02560749`, as a numerator over `10^8`. -/
def gateTarget : Nat := 102560749

/-- Every transcribed deep-grid value is `<= 1.02560749` (the tightest
margin is at `j=48`, matching the shipped V13 gate's own value). -/
theorem gateRows_below_target : ∀ row ∈ gateRows, row.rhoPropNum <= gateTarget := by
  decide

/-- Strict pairwise decrease of a `Nat` list (adjacent-pair recursion). -/
def strictlyDecreasing : List Nat → Bool
  | [] => true
  | [_] => true
  | a :: b :: t => a > b && strictlyDecreasing (b :: t)

/-- The deep-grid table is strictly decreasing in `j` (no plateau, no
uptick, over the transcribed rows). -/
theorem gateRows_strict_decreasing :
    strictlyDecreasing (gateRows.map GateRow.rhoPropNum) = true := by decide

/- ------------------------------------------------------------------ -/
/- 6. THE CROSSOVER ARITHMETIC.                                        -/
/-
   Same transcription discipline and caveat as section 5. `V_17(n)` values
   (6 digits after the point) and `tau* = 3*log(1.02560749...) ~ 0.0758553`
   (7 digits) are both transcribed as numerators over the common
   denominator `10^7`. `tau*` itself involves `log` (transcendental,
   informal, out of scope) — only the printed-decimal comparison is
   kernel-checked here, exactly as with the gate table.
-/

/-- The two named `rho_prop@i<17` endpoints quoted in the source note
(`1.02559 @ j=48 -> 1.01617 @ j=60`), against the target — corollaries of
`gateRows_below_target`, restated standalone for direct traceability. -/
theorem rho_prop_endpoint_48_below_target : (102559050 : Nat) <= gateTarget := by
  decide

theorem rho_prop_endpoint_60_below_target : (101617140 : Nat) <= gateTarget := by
  decide

/-- One `V_17(n)` row: level `n` and `V_17(n)` as a numerator over the
implicit denominator `10^7`. -/
structure V17Row where
  level : Nat
  v17Num : Nat
  deriving DecidableEq, Repr

/-- `V_17(n)` at the endpoints and around the claimed crossover. -/
def v17Rows : List V17Row :=
  [ { level := 48, v17Num := 1235790 }
  , { level := 50, v17Num := 1137820 }
  , { level := 55, v17Num := 938410 }
  , { level := 60, v17Num := 787190 }
  , { level := 61, v17Num := 761360 }
  , { level := 62, v17Num := 736780 } ]

/-- `tau* = 3*log(1.02560749...) ~= 0.0758553`, as a numerator over `10^7`. -/
def tauStarNum : Nat := 758553

/-- Claim-shape check, part 1: for every transcribed row at `n <= 61`,
`V_17(n)` is still (strictly) above `tau*` — no crossing yet. -/
theorem v17_above_before_62 :
    ∀ row ∈ v17Rows, row.level <= 61 → tauStarNum < row.v17Num := by decide

/-- Claim-shape check, part 2: at `n = 62` (the only transcribed row with
`n >= 62`), `V_17(n)` has dropped to at or below `tau*` — the first
crossing, matching the source note's independent full-integer-scan
finding. Together with part 1 this certifies the TABLE's crossover shape
at the transcribed rows; it is not an independent recomputation of
`V_17` or `tau*`. -/
theorem v17_below_from_62 :
    ∀ row ∈ v17Rows, 62 <= row.level → row.v17Num <= tauStarNum := by decide

end PropTail
