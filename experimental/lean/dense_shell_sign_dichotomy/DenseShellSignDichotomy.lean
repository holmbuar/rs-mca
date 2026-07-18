/-!
# The dense-shell sign dichotomy: decidable arithmetic shadow

The companion note proves `sign(hatf) = (-1)^B` on the whole dense shell via
the alternating-cone
walk: outer roots preserve the cone entrywise, and each isolated inner
root composes with its EXACTLY-coupled predecessor into a nonnegative
2-step matrix.  The trig content (arcsine means, sine drifts) lives in
the note and Python verifier; this module is the DECIDABLE integer
skeleton (stdlib-only, no mathlib, no `sorry`):

* the inner-state coupling theorem in integer form: the bounds alone
  force the predecessor's opposite sign and the exact identity
  `|n_(k-1)| = 3^(k-1) - |n_k|` (both `d = +-1` branches);
* the parity impossibility `6 n = 3^k` (strictness of `delta < 1/12`);
* the alternating-word closed form `4 altN m = 1 -+ P3 m` by parity
  (the exact geometric approach to the T3 fixed point `u = +-1/4`);
* the exact all-integer S-expansion
  `x(3-4x)^2 = 16x^3-24x^2+9x`, plus the former 101-point census as a
  regression check;
* a `native_decide` census at B = 8: every inner state in every dense
  word is isolated, never first, and satisfies the coupling identity.

Powers of three enter as the self-contained recursion
`P3 0 = 1, P3 (k+1) = 3 * P3 k` (definitional, so `omega` can use it).

Note:     `experimental/notes/thresholds/dense_shell_sign_dichotomy.md`.
Verifier: `experimental/scripts/verify_dense_shell_sign_dichotomy.py`
          (23/23, tamper 7/7).
-/

namespace DenseShellSignDichotomy

/-- `P3 k = 3^k`, as a definitional recursion. -/
def P3 : Nat → Int
  | 0 => 1
  | k + 1 => 3 * P3 k

theorem P3_pos (k : Nat) : 0 < P3 k := by
  induction k with
  | zero => decide
  | succ k ih => simp only [P3]; omega

/-- Inner-state coupling, `d = +1` branch.  `P` stands for `3^(k-1)`
    (any positive integer works); the scan recursion is `n' = P + n`,
    the predecessor bound is `|2n| < P`, "inner" is `|4n'| < 3P`.
    The bounds alone force sign opposition and the exact identity. -/
theorem inner_coupling_pos (P n n' : Int) (_hP : 0 < P)
    (hrec : n' = P + n) (hb₁ : 2 * n < P) (hb₂ : -P < 2 * n)
    (hi₁ : 4 * n' < 3 * P) (_hi₂ : -(3 * P) < 4 * n') :
    n < 0 ∧ 0 < n' ∧ -n = P - n' := by
  omega

/-- Inner-state coupling, `d = -1` branch (mirror). -/
theorem inner_coupling_neg (P n n' : Int) (_hP : 0 < P)
    (hrec : n' = -P + n) (hb₁ : 2 * n < P) (hb₂ : -P < 2 * n)
    (_hi₁ : 4 * n' < 3 * P) (hi₂ : -(3 * P) < 4 * n') :
    0 < n ∧ n' < 0 ∧ n = P + n' := by
  omega

/-- `P3 k` is odd. -/
theorem P3_odd (k : Nat) : P3 k % 2 = 1 := by
  induction k with
  | zero => decide
  | succ k ih => simp only [P3]; omega

/-- `6 n = 3^k` is impossible: the boundary `delta = 1/12`
    (equivalently `|u| = 1/6`) is never attained on finite words. -/
theorem no_sixth (n : Int) (k : Nat) : 6 * n ≠ P3 k := by
  intro h
  have h2 := P3_odd k
  omega

/-- Alternating word: digits `d_i = (-1)^i`, states
    `altN (m+1) = d_m * 3^m + altN m`. -/
def altSign (m : Nat) : Int := if m % 2 = 0 then 1 else -1

def altN : Nat → Int
  | 0 => 0
  | m + 1 => altSign m * P3 m + altN m

/-- Closed form by parity: `4 altN m = 1 - 3^m` (even m),
    `= 1 + 3^m` (odd m); so `|4 u_m| = 1 -+ 3^(-m)` exactly. -/
theorem alt_closed (m : Nat) :
    (m % 2 = 0 → 4 * altN m = 1 - P3 m) ∧
    (m % 2 = 1 → 4 * altN m = 1 + P3 m) := by
  induction m with
  | zero => exact ⟨fun _ => rfl, fun h => by omega⟩
  | succ m ih =>
      have hp : P3 (m + 1) = 3 * P3 m := rfl
      rcases Nat.mod_two_eq_zero_or_one m with hm | hm
      · have hs : altSign m = 1 := by simp [altSign, hm]
        have h4 := ih.1 hm
        refine ⟨fun h => by omega, fun _ => ?_⟩
        show 4 * (altSign m * P3 m + altN m) = 1 + P3 (m + 1)
        rw [hs, hp]
        omega
      · have hs : altSign m = -1 := by simp [altSign, hm]
        have h4 := ih.2 hm
        refine ⟨fun _ => ?_, fun h => by omega⟩
        show 4 * (altSign m * P3 m + altN m) = 1 - P3 (m + 1)
        rw [hs, hp]
        omega

/-- Exact S-expansion over every integer.  The ambient type is intentionally
    `Int`: the analogous surface syntax over `Nat` is false because subtraction
    truncates. -/
theorem s_expand (x : Int) :
    x * (3 - 4 * x) * (3 - 4 * x) =
      16 * x * x * x - 24 * x * x + 9 * x := by
  have h44 : (4 * x) * (4 * x) = 16 * (x * x) := by
    calc
      (4 * x) * (4 * x) = (4 * 4) * (x * x) := by ac_rfl
      _ = 16 * (x * x) := by rfl
  have hsq :
      (3 - 4 * x) * (3 - 4 * x) =
        9 - 24 * x + 16 * (x * x) := by
    rw [Int.sub_mul, Int.mul_sub, Int.mul_sub, h44]
    omega
  have h9 : x * 9 = 9 * x := Int.mul_comm x 9
  have h24 : x * (24 * x) = 24 * x * x := by ac_rfl
  have h16 : x * (16 * (x * x)) = 16 * x * x * x := by ac_rfl
  rw [Int.mul_assoc, hsq, Int.mul_add, Int.mul_sub, h9, h24, h16]
  omega

/-- Finite regression for the S-expansion on `x in [-50, 50]`.  The universal
    theorem above supplies the mathematical statement; this Boolean census is
    retained unchanged for API and source compatibility. -/
def sExpandOK : Bool :=
  (List.range 101).all fun i =>
    let x : Int := Int.ofNat i - 50
    x * (3 - 4 * x) * (3 - 4 * x) == 16 * x * x * x - 24 * x * x + 9 * x

theorem s_expand_census : sExpandOK = true := by native_decide

/-- Scan states of a word as `(n_k, 3^k)` pairs, k = 1..B. -/
def scan (w : List Int) : List (Int × Int) :=
  (w.foldl
    (fun (st : Int × Int × List (Int × Int)) d =>
      let n := d * st.2.1 + st.1
      (n, 3 * st.2.1, st.2.2 ++ [(n, 3 * st.2.1)]))
    (0, 1, [])).2.2

/-- Inner at `(n, 3^k)`: `4 |n| < 3^k`. -/
def isInner (s : Int × Int) : Bool := 4 * s.1.natAbs < s.2.natAbs

/-- All length-B words with digits in {+1, -1}. -/
def words : Nat → List (List Int)
  | 0 => [[]]
  | n + 1 => (words n).flatMap fun w => [(1 : Int) :: w, (-1 : Int) :: w]

/-- Census predicate: every inner state is isolated, never first, and
    satisfies `|n_(k-1)| = 3^(k-1) - |n_k|` with opposite signs. -/
def couplingOK (w : List Int) : Bool :=
  let ss := scan w
  (List.range ss.length).all fun k =>
    match ss[k]? with
    | none => true
    | some s =>
        if isInner s then
          (k != 0) &&
          (match ss[k - 1]? with
           | none => false
           | some p =>
               !(isInner p) &&
               (p.1.natAbs == s.2.natAbs / 3 - s.1.natAbs) &&
               ((decide (p.1 < 0) && decide (0 < s.1)) ||
                (decide (0 < p.1) && decide (s.1 < 0))))
        else true

theorem census_B8 : ((words 8).all couplingOK) = true := by
  native_decide

end DenseShellSignDichotomy
