/-!
# M31 post-Johnson conversion arithmetic

Kernel-checked, stdlib-only arithmetic shadow of
`experimental/notes/thresholds/m31_postjohnson_conversion_contract.md`.

The module certifies the frozen row constants, exact Johnson boundary,
shortening route cut, CS25 integer window, BCHKS25 route-cut margins, and the
literal-source GCXK25 integer instantiation.  It does not formalize the cited
coding-theory implications themselves.

No `sorry`. No Mathlib.
-/

namespace LPostJohnsonContract

def p : Nat := 2147483647
def q : Nat := 21267647892944572736998860269687930881
def n : Nat := 2097152
def k : Nat := 1048576
def agreement : Nat := 1116023
def errors : Nat := 981129
def adjacentAgreement : Nat := 1116024
def adjacentErrors : Nat := 981128
def BStar : Nat := 16777215
def securityDenominator : Nat := 2 ^ 100

/-! ## Frozen row and budget -/

theorem q_value : p ^ 4 = q := by native_decide

theorem full_domain_value : n = 2 ^ 21 := by native_decide

theorem dimension_value : k = 2 ^ 20 := by native_decide

theorem agreement_error_partition : agreement + errors = n := by native_decide

theorem adjacent_error_partition :
    adjacentAgreement + adjacentErrors = n := by native_decide

theorem adjacent_agreement_shift :
    adjacentAgreement = agreement + 1 := by native_decide

theorem adjacent_error_shift : errors = adjacentErrors + 1 := by native_decide

theorem locator_degree_value : n - agreement = 981129 := by native_decide

theorem budget_floor : q / securityDenominator = BStar := by native_decide

theorem budget_floor_remainder :
    q % securityDenominator =
      1228036518998767348801905623041 := by native_decide

theorem budget_ceiling :
    (q + securityDenominator - 1) / securityDenominator = BStar + 1 := by
  native_decide

/-! ## Exact finite-q Johnson boundary for C+ = RS(k+1) -/

def finiteJohnsonLhs (a : Nat) : Nat :=
  (BStar - 1) * (q * a - n) ^ 2

def finiteJohnsonRhs (a : Nat) : Nat :=
  n ^ 2 * (q - 1) ^ 2 * (BStar - 1)
    - n * (q - 1) * q * BStar * (n - k)

theorem finite_johnson_previous_deficit :
    finiteJohnsonRhs 1482910 - finiteJohnsonLhs 1482910 =
      8016391725505050246066417496357516786153876577101023083937102496439633020969773596132104 := by
  native_decide

theorem finite_johnson_boundary_margin :
    finiteJohnsonLhs 1482911 - finiteJohnsonRhs 1482911 =
      14489887525701682981712437636783439750805076991890876089727149238354095278314282946247294 := by
  native_decide

theorem quadratic_previous_deficit :
    n * k - 1482910 ^ 2 = 1187452 := by native_decide

theorem quadratic_boundary_margin :
    1482911 ^ 2 - n * k = 1778369 := by native_decide

theorem johnson_integer_radius :
    n - 1482911 = 614241 := by native_decide

theorem post_johnson_agreement_gap :
    1482911 - agreement = 366888 := by native_decide

theorem post_johnson_fraction_reduction :
    366888 * 262144 = 45861 * n := by native_decide

theorem capacity_headroom :
    n / 2 - errors = 67447 := by native_decide

theorem johnson_cap :
    (n * (1482911 - k)) / (1482911 ^ 2 - n * k) = 512192 := by
  native_decide

theorem johnson_cap_remainder :
    (n * (1482911 - k)) % (1482911 ^ 2 - n * k) = 139072 := by
  native_decide

/-! ## Packet code C = RS(k): one-step convention audit -/

theorem row_code_quadratic_previous_deficit :
    n * (k - 1) - 1482909 ^ 2 = 2056119 := by native_decide

theorem row_code_quadratic_boundary_margin :
    1482910 ^ 2 - n * (k - 1) = 909700 := by native_decide

theorem row_code_johnson_integer_radius :
    n - 1482910 = 614242 := by native_decide

theorem row_code_johnson_cap :
    (n * (1482910 - (k - 1))) /
      (1482910 ^ 2 - n * (k - 1)) = 1001282 := by
  native_decide

theorem row_code_johnson_cap_remainder :
    (n * (1482910 - (k - 1))) %
      (1482910 ^ 2 - n * (k - 1)) = 278520 := by
  native_decide

/-! ## R1 route cuts -/

theorem row_stress_quadratic_deficit :
    n * (k - 1) - agreement ^ 2 = 953513821871 := by native_decide

theorem partner_stress_quadratic_deficit :
    n * k - agreement ^ 2 = 953515919023 := by native_decide

def shortenedLhs (s : Nat) : Nat := (agreement - s) ^ 2

def shortenedRhs (s : Nat) : Nat :=
  (n - s) * (k - s - 1)

theorem shortening_previous_deficit :
    shortenedRhs 1043595 - shortenedLhs 1043595 = 898676 := by
  native_decide

theorem shortening_activation_margin :
    shortenedLhs 1043596 - shortenedRhs 1043596 = 15005 := by
  native_decide

theorem shortened_row_values :
    n - 1043596 = 1053556 ∧
    k - 1043596 = 4980 ∧
    agreement - 1043596 = 72427 := by
  native_decide

theorem shortened_johnson_cap :
    (1053556 * (72427 - 4979)) / 15005 = 4735771 := by
  native_decide

theorem shortened_johnson_cap_remainder :
    (1053556 * (72427 - 4979)) % 15005 = 1233 := by
  native_decide

def falling (x count : Nat) : Nat :=
  (List.range count).foldl (fun acc i => acc * (x - i)) 1

theorem shortening_averaging_floor_27 :
    falling n 27 / falling agreement 27 = 24940004 := by
  native_decide

theorem shortening_averaging_exceeds_budget :
    falling n 27 > BStar * falling agreement 27 := by
  native_decide

theorem shortening_averaging_gap :
    24940004 - BStar = 8162789 := by native_decide

/-! ## R2 lower-route calibration -/

theorem identity_prefix_gap :
    BStar - 1993678 = 14783537 := by native_decide

theorem coset_t3_gap :
    BStar - 1 = 16777214 := by native_decide

theorem fixed_remainder_support_gap :
    BStar - 35 = 16777180 := by native_decide

/-! ## R3(i): CS25 exact integer window -/

def qMinusN : Nat := q - n
def csDenominator : Nat := qMinusN + BStar * k
def csNumerator : Nat := BStar * qMinusN

theorem q_minus_n_value :
    qMinusN = 21267647892944572736998860269685833729 := by
  native_decide

theorem cs_denominator_value :
    csDenominator =
      21267647892944572736998877861870829569 := by
  native_decide

theorem cs_numerator_value :
    csNumerator =
      356811901244228079891768333499477214925684735 := by
  native_decide

theorem cs_max_integer_input :
    csNumerator / csDenominator = BStar - 1 := by
  native_decide

theorem cs_floor_remainder :
    csNumerator % csDenominator =
      21267647892944572441851007866889043969 := by
  native_decide

theorem cs_explicit_eta_premise_margin :
    qMinusN - BStar * (BStar - 1) * k =
      21267647892944572441851007866889043969 := by
  native_decide

theorem cs_explicit_eta_output :
    ((BStar - 1) * BStar) / (BStar - 1) = BStar := by
  native_decide

theorem cs_candidate_budget_is_one_too_large :
    BStar > csNumerator / csDenominator := by
  native_decide

/-! ## R3(ii): BCHKS25 exact route cut -/

def twoN : Nat := 2 * n
def bchksMaxInput : Nat := 5070602391468184646844592158720
def bchksConclusion : Nat := q - 1
def bchksBudgetFactor : Nat :=
  1267650673424914250487870619151

theorem bchks_q_congruence :
    q = twoN * bchksMaxInput + 1 := by native_decide

theorem bchks_strict_lower_margin :
    q - twoN * bchksMaxInput = 1 := by native_decide

theorem bchks_strict_upper_margin :
    twoN * (bchksMaxInput + 1) - q = 4194303 := by
  native_decide

theorem bchks_two_radius_gap :
    1048575 - 981131 = 67444 := by native_decide

theorem bchks_budget_division :
    bchksConclusion = BStar * bchksBudgetFactor + 8486415 := by
  native_decide

theorem bchks_factor_exceeds_two_pow_100 :
    bchksBudgetFactor - 2 ^ 100 =
      73196684848991167413775 := by
  native_decide

theorem bchks_conclusion_excess :
    bchksConclusion - (2 ^ 100) * BStar =
      1228036518998767348801905623040 := by
  native_decide

/-! ## R3(iii): literal-source GCXK25 arithmetic -/

def gcxkBaseNumerator : Nat := BStar ^ 2 * errors
def gcxkAdjacentNumerator : Nat := gcxkBaseNumerator + 5
def gcxkBudgetFactor : Nat := 16460612175735

theorem gcxk_base_numerator_value :
    gcxkBaseNumerator = 276163229503923878025 := by
  native_decide

theorem gcxk_eta_lower_squared_margin :
    36 * agreement * n -
      (6 * adjacentAgreement + n) ^ 2 = 6934860650240 := by
  native_decide

theorem gcxk_eta_upper_squared_margin :
    (5 * adjacentAgreement + n) ^ 2 -
      25 * agreement * n = 428758699584 := by
  native_decide

theorem gcxk_adjacent_budget_division :
    gcxkAdjacentNumerator = BStar * gcxkBudgetFactor + 5 := by
  native_decide

theorem gcxk_budget_factor_value :
    BStar * errors = gcxkBudgetFactor := by
  native_decide

end LPostJohnsonContract
