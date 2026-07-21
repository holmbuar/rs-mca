import M31QRootedShell.Deployed
import Std

/-!
# M31 fixed-remainder dyadic block route cut

This stdlib-only module certifies the exact deployed arithmetic in
`experimental/notes/thresholds/m31_fixed_remainder_dyadic_route_cut.md`.

The attacked family fixes a remainder `R` and varies complete fibers of the
dyadic Chebyshev folding `T_(2^s)` on the deployed `T_(2^21)` root domain.

* For exponents `1 <= s <= 17`, the Euclidean remainder satisfies `r <= w`
  and at least one complete fiber is present.  These are the exact
  quotient/remainder profiles routed to the earlier C1 owner.
* For `18 <= s <= 21`, the remainder is prefix-shallow (`w < r < 2^s`).
  Even before any deletion, a fixed nonempty remainder leaves at most
  `choose (N-1) q`, namely `35, 3, 1, 1`, complete-fiber choices.

The module checks only this finite deployed ledger.  The source note supplies
the Chebyshev complete-fiber argument and the mapping to
`thm:exact-quotient-remainder-normal-form`.
-/

namespace SidonEffectiveImage.M31DyadicBlockRouteCut

abbrev deployedPrime : Nat := M31QRootedShell.Deployed.pM31
abbrev deployedBudget : Nat := M31QRootedShell.Deployed.Bstar
abbrev prefixDepth : Nat := M31QRootedShell.Deployed.w
abbrev supportSize : Nat := M31QRootedShell.Deployed.listM

def domainSize : Nat := 2097152
def fullSliceAverageCeiling : Nat := 1993678

structure ScaleRow where
  exponent : Nat
  fiberSize : Nat
  quotientFibers : Nat
  completeFibers : Nat
  remainder : Nat
  /-- Zero means that the whole named profile is removed by C1.  On the late
  rows this is the exact worst fixed-remainder pre-deletion cap. -/
  postC1Cap : Nat
deriving Repr, BEq, DecidableEq

def scaleRows : List ScaleRow :=
  [
    { exponent := 1, fiberSize := 2, quotientFibers := 1048576, completeFibers := 490564, remainder := 1, postC1Cap := 0 },
    { exponent := 2, fiberSize := 4, quotientFibers := 524288, completeFibers := 245282, remainder := 1, postC1Cap := 0 },
    { exponent := 3, fiberSize := 8, quotientFibers := 262144, completeFibers := 122641, remainder := 1, postC1Cap := 0 },
    { exponent := 4, fiberSize := 16, quotientFibers := 131072, completeFibers := 61320, remainder := 9, postC1Cap := 0 },
    { exponent := 5, fiberSize := 32, quotientFibers := 65536, completeFibers := 30660, remainder := 9, postC1Cap := 0 },
    { exponent := 6, fiberSize := 64, quotientFibers := 32768, completeFibers := 15330, remainder := 9, postC1Cap := 0 },
    { exponent := 7, fiberSize := 128, quotientFibers := 16384, completeFibers := 7665, remainder := 9, postC1Cap := 0 },
    { exponent := 8, fiberSize := 256, quotientFibers := 8192, completeFibers := 3832, remainder := 137, postC1Cap := 0 },
    { exponent := 9, fiberSize := 512, quotientFibers := 4096, completeFibers := 1916, remainder := 137, postC1Cap := 0 },
    { exponent := 10, fiberSize := 1024, quotientFibers := 2048, completeFibers := 958, remainder := 137, postC1Cap := 0 },
    { exponent := 11, fiberSize := 2048, quotientFibers := 1024, completeFibers := 479, remainder := 137, postC1Cap := 0 },
    { exponent := 12, fiberSize := 4096, quotientFibers := 512, completeFibers := 239, remainder := 2185, postC1Cap := 0 },
    { exponent := 13, fiberSize := 8192, quotientFibers := 256, completeFibers := 119, remainder := 6281, postC1Cap := 0 },
    { exponent := 14, fiberSize := 16384, quotientFibers := 128, completeFibers := 59, remainder := 14473, postC1Cap := 0 },
    { exponent := 15, fiberSize := 32768, quotientFibers := 64, completeFibers := 29, remainder := 30857, postC1Cap := 0 },
    { exponent := 16, fiberSize := 65536, quotientFibers := 32, completeFibers := 14, remainder := 63625, postC1Cap := 0 },
    { exponent := 17, fiberSize := 131072, quotientFibers := 16, completeFibers := 7, remainder := 63625, postC1Cap := 0 },
    { exponent := 18, fiberSize := 262144, quotientFibers := 8, completeFibers := 3, remainder := 194697, postC1Cap := 35 },
    { exponent := 19, fiberSize := 524288, quotientFibers := 4, completeFibers := 1, remainder := 456841, postC1Cap := 3 },
    { exponent := 20, fiberSize := 1048576, quotientFibers := 2, completeFibers := 0, remainder := 981129, postC1Cap := 1 },
    { exponent := 21, fiberSize := 2097152, quotientFibers := 1, completeFibers := 0, remainder := 981129, postC1Cap := 1 }
  ]

/-- Pascal recursion used only on the late quotient sizes `8,4,2,1`. -/
def smallChoose : Nat → Nat → Nat
  | _, 0 => 1
  | 0, _ + 1 => 0
  | n + 1, k + 1 => smallChoose n k + smallChoose n (k + 1)

def exactShape (row : ScaleRow) : Bool :=
  row.fiberSize == 2 ^ row.exponent &&
  row.quotientFibers * row.fiberSize == domainSize &&
  row.completeFibers * row.fiberSize + row.remainder == supportSize &&
  decide (row.remainder < row.fiberSize)

def c1Visible (row : ScaleRow) : Bool :=
  decide (row.remainder ≤ prefixDepth ∧ 0 < row.completeFibers)

def expectedLateCap (row : ScaleRow) : Nat :=
  smallChoose (row.quotientFibers - 1) row.completeFibers

def routeCheck (row : ScaleRow) : Bool :=
  exactShape row &&
    (if c1Visible row then
      row.postC1Cap == 0
    else
      decide (prefixDepth < row.remainder) &&
      row.postC1Cap == expectedLateCap row &&
      decide (row.postC1Cap ≤ 35))

def postC1Caps : List Nat := scaleRows.map fun row => row.postC1Cap

def maxNat : List Nat → Nat
  | [] => 0
  | x :: xs => Nat.max x (maxNat xs)

def antipodalRow : ScaleRow :=
  { exponent := 1, fiberSize := 2, quotientFibers := 1048576,
    completeFibers := 490564, remainder := 1, postC1Cap := 0 }

def t4Row : ScaleRow :=
  { exponent := 2, fiberSize := 4, quotientFibers := 524288,
    completeFibers := 245282, remainder := 1, postC1Cap := 0 }

def lateRows : List ScaleRow :=
  scaleRows.filter fun row => !c1Visible row

theorem deployed_dimensions :
    deployedPrime = 2147483647 ∧
    deployedBudget = 16777215 ∧
    domainSize = 2097152 ∧
    supportSize = 981129 ∧
    prefixDepth = 67447 ∧
    fullSliceAverageCeiling = 1993678 := by
  decide

theorem all_scale_rows_checked :
    scaleRows.all routeCheck = true := by
  decide

theorem postC1_caps_exact :
    postC1Caps = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 35, 3, 1, 1] := by
  decide

theorem late_rows_exact :
    lateRows =
      [
    { exponent := 18, fiberSize := 262144, quotientFibers := 8, completeFibers := 3, remainder := 194697, postC1Cap := 35 },
    { exponent := 19, fiberSize := 524288, quotientFibers := 4, completeFibers := 1, remainder := 456841, postC1Cap := 3 },
    { exponent := 20, fiberSize := 1048576, quotientFibers := 2, completeFibers := 0, remainder := 981129, postC1Cap := 1 },
    { exponent := 21, fiberSize := 2097152, quotientFibers := 1, completeFibers := 0, remainder := 981129, postC1Cap := 1 }
      ] := by
  decide

theorem late_caps_exact :
    lateRows.map (fun row => row.postC1Cap) = [35, 3, 1, 1] := by
  decide

theorem postC1_cap_max :
    maxNat postC1Caps = 35 := by
  decide

theorem postC1_cap_below_average :
    maxNat postC1Caps < fullSliceAverageCeiling := by
  decide

theorem postC1_cap_below_budget :
    maxNat postC1Caps < deployedBudget := by
  decide

theorem deployed_margin_bracket :
    8 * fullSliceAverageCeiling ≤ deployedBudget ∧
    deployedBudget < 9 * fullSliceAverageCeiling := by
  decide

theorem antipodal_and_t4_are_c1_scales :
    scaleRows.contains antipodalRow = true ∧
    scaleRows.contains t4Row = true ∧
    c1Visible antipodalRow = true ∧
    c1Visible t4Row = true := by
  decide

/-- Exact finite arithmetic consumed by the source-level named route cut. -/
theorem named_route_cut_arithmetic :
    scaleRows.all routeCheck = true ∧
    maxNat postC1Caps = 35 ∧
    maxNat postC1Caps < fullSliceAverageCeiling ∧
    maxNat postC1Caps < deployedBudget := by
  decide

#print axioms deployed_dimensions
#print axioms all_scale_rows_checked
#print axioms postC1_caps_exact
#print axioms late_rows_exact
#print axioms late_caps_exact
#print axioms postC1_cap_max
#print axioms postC1_cap_below_average
#print axioms postC1_cap_below_budget
#print axioms deployed_margin_bracket
#print axioms antipodal_and_t4_are_c1_scales
#print axioms named_route_cut_arithmetic

end SidonEffectiveImage.M31DyadicBlockRouteCut
