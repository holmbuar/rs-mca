import AsymptoticSpine.BooleanFiber

namespace AsymptoticSpine

/-!
# (L5) No large high-energy Boolean fiber — `prop:no-high-energy` skeleton

Stdlib-only (no mathlib) formalization of the **inequality composition** behind
`prop:no-high-energy` (L228–234) of `experimental/asymptotic_rs_mca.tex`, with the
two external additive-combinatorics inputs entering as **hypotheses**, never
baked into the logic (they are deep theorems whose proofs are out of scope; the
paper cites them, and a faithful skeleton must not silently assume them):

* `thm:bsg` Balog–Szemerédi–Gowers (L214–216): from a high-energy set one extracts
  a subset `A'` with `|A'| ≥ K^{-C}|A|` and `|A'-A'| ≤ K^C|A'|`.
* `thm:quasicube` (L220–226): every finite `A ⊆ {0,1}^N` has `|A-A| ≥ |A|^{3/2}`.
  To stay over `Nat` and avoid square roots, the squared form `|A|^4 ≤ |A-A|^2·|A|`
  is used (equivalent to `|A-A| ≥ |A|^{3/2}`).

Paper proof (L232–234): BSG gives `A' ⊆ A` with `|A'| ≥ e^{cN-o(N)}` and
`|A'-A'| ≤ e^{o(N)}|A'|`; quasicube gives `|A'-A'| ≥ |A'|^{3/2}`, so
`|A'|^{1/2} ≤ e^{o(N)}`, contradicting `|A'| ≥ e^{cN-o(N)}`.

The `e^{o(N)}` bookkeeping (`K^{±C} = e^{±o(N)}`) is the reals part and stays in
the tex.  The scale-free content is the **exact inequality composition**:
combining the BSG size/difference bounds with the (squared) quasicube bound forces

    `|A| ≤ K^{3C}`,

and hence, whenever the energy regime makes `K^{3C} < |A|` (the tex's
`|A| ≥ e^{cN-o(N)}` beating the subexponential `K^{3C} = e^{o(N)}`), a
contradiction.  Cardinalities are modelled directly as `Nat`; the Boolean-cube
membership needed to invoke quasicube is carried by the concrete semantic
predicate `BoolFiber` from `BooleanFiber.lean`, so the quasicube hypothesis
reads exactly as "every realized Boolean-cube fiber obeys the squared
quasicube bound".

Kernel-checked, stdlib-only, no mathlib.
-/

/-- **(L5) `prop:no-high-energy`, exact-inequality skeleton.**  Given

* `quasicube` — the quasicube theorem, as a hypothesis: every Boolean-cube fiber
  `(s, d)` satisfies the squared growth bound `s^4 ≤ d^2 · s`
  (i.e. `|A-A| ≥ |A|^{3/2}`);
* `bsg` — the BSG output, as a hypothesis: the high-energy set of size `f` yields a
  Boolean-cube subfiber `(s, d)` with `f ≤ K^C · s` (size bound, `|A'| ≥ K^{-C}|A|`)
  and `d ≤ K^C · s` (difference bound, `|A'-A'| ≤ K^C|A'|`),

the composition forces `f ≤ K^{3C}`. -/
theorem no_high_energy_bound
    (quasicube : ∀ s d : Nat, BoolFiber s d → s ^ 4 ≤ d ^ 2 * s)
    (f K C : Nat)
    (bsg : ∃ s d : Nat, f ≤ K ^ C * s ∧ d ≤ K ^ C * s ∧ BoolFiber s d) :
    f ≤ K ^ (3 * C) := by
  obtain ⟨s, d, hsize, hdiff, hfib⟩ := bsg
  -- quasicube (squared) on the extracted fiber: s^4 ≤ d^2·s
  have hq : s ^ 4 ≤ d ^ 2 * s := quasicube s d hfib
  -- square the BSG difference bound: d^2 ≤ (K^C·s)^2 = (K^C)^2·s^2
  have hd2 : d ^ 2 ≤ (K ^ C) ^ 2 * s ^ 2 := by
    have h := Nat.pow_le_pow_left hdiff 2
    rwa [Nat.mul_pow] at h
  -- combine: s^4 ≤ d^2·s ≤ ((K^C)^2·s^2)·s = (K^C)^2·s^3
  have hss : s ^ 2 * s = s ^ 3 := by rw [← Nat.pow_succ]
  have hstep : d ^ 2 * s ≤ (K ^ C) ^ 2 * s ^ 2 * s := Nat.mul_le_mul hd2 (Nat.le_refl s)
  have heq2 : (K ^ C) ^ 2 * s ^ 2 * s = (K ^ C) ^ 2 * s ^ 3 := by
    rw [Nat.mul_assoc, hss]
  have hcube : s ^ 4 ≤ (K ^ C) ^ 2 * s ^ 3 := by
    have := Nat.le_trans hq hstep
    rwa [heq2] at this
  -- cancel s^3: either s = 0 (then f = 0) or s ≤ (K^C)^2
  rcases Nat.eq_zero_or_pos s with hs | hs
  · subst hs
    have hf0 : f ≤ 0 := by simpa using hsize
    exact Nat.le_trans hf0 (Nat.zero_le _)
  · have hs3 : 0 < s ^ 3 := Nat.pow_pos hs
    have hs4 : s ^ 3 * s = s ^ 4 := by rw [← Nat.pow_succ]
    have key : s ^ 3 * s ≤ s ^ 3 * (K ^ C) ^ 2 := by
      rw [hs4, Nat.mul_comm (s ^ 3) ((K ^ C) ^ 2)]; exact hcube
    have hs_le : s ≤ (K ^ C) ^ 2 := Nat.le_of_mul_le_mul_left key hs3
    have hfin : K ^ C * (K ^ C) ^ 2 = K ^ (3 * C) := by
      rw [← Nat.pow_mul, ← Nat.pow_add]; congr 1; omega
    calc f ≤ K ^ C * s := hsize
      _ ≤ K ^ C * (K ^ C) ^ 2 := Nat.mul_le_mul (Nat.le_refl (K ^ C)) hs_le
      _ = K ^ (3 * C) := hfin

/-- **(L5) `prop:no-high-energy`, contradiction form.**  In the tex's energy
regime the extracted fiber size `f` exceeds the subexponential ledger overhead
`K^{3C}`; combined with `no_high_energy_bound` this is a contradiction, i.e. no
such large high-energy Boolean fiber exists. -/
theorem no_high_energy_contradiction
    (quasicube : ∀ s d : Nat, BoolFiber s d → s ^ 4 ≤ d ^ 2 * s)
    (f K C : Nat)
    (bsg : ∃ s d : Nat, f ≤ K ^ C * s ∧ d ≤ K ^ C * s ∧ BoolFiber s d)
    (hregime : K ^ (3 * C) < f) : False := by
  have hb := no_high_energy_bound quasicube f K C bsg
  omega

end AsymptoticSpine
