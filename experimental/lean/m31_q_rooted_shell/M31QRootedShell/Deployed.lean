import M31QRootedShell.Envelope

/-!
# Exact deployed packet arithmetic

Stdlib-only checks of the Mersenne-31 list and MCA deductions from the pinned
scaled-floor packet integers.  The gigantic binomial quotient values are
explicit inputs; this module proves the resulting bounds, reserves, and the
intercept calibration in the Lean kernel.
-/

namespace M31QRootedShell.Deployed

/-- Mersenne-31 base prime. -/
def pM31 : Nat := 2147483647

/-- Official auxiliary-row integer budget. -/
def Bstar : Nat := 16777215

/-- Shared deployed prefix depth. -/
def w : Nat := 67447

/-- Mersenne-31 list-row complement size and admissible shell count. -/
def listM : Nat := 981129
def listShellCount : Nat := 913682

/-- Pinned packet value `floor (7 * choose n m / p^w)`. -/
def listScaledFloor : Nat := 13955739

/-- The resulting `3+7` rooted-shell upper bound. -/
def listBound : Nat := 1 + 3 * listShellCount + listScaledFloor

/-- Mersenne-31 MCA-row complement size and admissible shell count. -/
def mcaM : Nat := 981128
def mcaShellCount : Nat := 913681

/-- Pinned packet value `floor (7 * choose n m / p^w)`. -/
def mcaScaledFloor : Nat := 12268894

def mcaBound : Nat := 1 + 3 * mcaShellCount + mcaScaledFloor

/-- The official budget formula evaluates to `2^24 - 1`. -/
theorem Bstar_formula : pM31 ^ 4 / 2 ^ 100 = Bstar := by decide

theorem listShellCount_eq : listShellCount = listM - w := by decide

theorem listBound_eq : listBound = 16696786 := by decide

theorem listBound_le_budget : listBound ≤ Bstar := by decide

theorem listReserve_eq : Bstar - listBound = 80429 := by decide

/-- Intercept two fits the numerical row budget, but the faithful toy refutes
its local shell premise. -/
theorem list_two_plus_seven_fits :
    1 + 2 * listShellCount + listScaledFloor ≤ Bstar := by decide

/-- Intercept four is already too expensive at the binding list row. -/
theorem list_four_plus_seven_exceeds :
    Bstar < 1 + 4 * listShellCount + listScaledFloor := by decide

theorem mcaShellCount_eq : mcaShellCount = mcaM - w := by decide

theorem mcaBound_eq : mcaBound = 15009938 := by decide

theorem mcaBound_le_budget : mcaBound ≤ Bstar := by decide

theorem mcaReserve_eq : Bstar - mcaBound = 1767277 := by decide

end M31QRootedShell.Deployed
