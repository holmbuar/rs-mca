import cs25_cap_v12.Fiber

/-!
# `lem_phi_fiber_ii` repair certificate

The pre-repair Lean skeleton for Paper D's `lem:phi-fiber`(ii) did not tie the
polynomial `φ` to the base subfield `B`.  This module supplies two independent
kernel certificates:

* `lem_phi_fiber_ii_pre_repair_false` negates the exact old universal signature
  over a symbolic `GF(16)/GF(4)` counterexample; and
* `lem_phi_fiber_ii_of_basePolynomial` derives the repaired value-level
  hypothesis from the paper's coefficient-level premise `φ ∈ B[X]`.

The counterexample is symbolic.  It does not enumerate either finite field.
-/

noncomputable section

namespace RSCap.PhiFiberRepair

open Classical Polynomial

/-! ## The concrete field tower -/

abbrev K4 := GaloisField 2 2
abbrev F16 := GaloisField 2 4

/-- A chosen `GF(2)`-algebra embedding `GF(4) → GF(16)`. -/
noncomputable def emb : K4 →ₐ[ZMod 2] F16 :=
  (FiniteField.nonempty_algHom_of_finrank_dvd (F := ZMod 2)
    (K := K4) (L := F16) (by
      rw [GaloisField.finrank 2 (by decide), GaloisField.finrank 2 (by decide)]
      decide)).some

/-- The embedded copy of `GF(4)` inside `GF(16)`. -/
def B4 : Subfield F16 := emb.toRingHom.fieldRange

instance : Fintype K4 := Fintype.ofFinite K4
instance : Fintype F16 := Fintype.ofFinite F16

/-- The embedding, restricted to an equivalence with its field range. -/
noncomputable def equivK4B4 : K4 ≃ B4 := by
  change K4 ≃ Set.range emb
  exact Equiv.ofInjective emb emb.injective

instance : Fintype B4 := Fintype.ofEquiv K4 equivK4B4

/-- Field-cardinality support for the pre-repair `RSCap.lem_phi_fiber_ii`
declaration in `experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean`
at `c4856fa6`. -/
theorem card_K4 : Fintype.card K4 = 4 := by
  rw [Fintype.card_eq_nat_card, GaloisField.card 2 (n := 2) (by decide)]
  norm_num

/-- Field-cardinality support for the pre-repair `RSCap.lem_phi_fiber_ii`
declaration in `experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean`
at `c4856fa6`. -/
theorem card_F16 : Fintype.card F16 = 16 := by
  rw [Fintype.card_eq_nat_card, GaloisField.card 2 (n := 4) (by decide)]
  norm_num

/-- Field-cardinality support for the pre-repair `RSCap.lem_phi_fiber_ii`
declaration in `experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean`
at `c4856fa6`. -/
theorem card_B4 : Fintype.card B4 = 4 := by
  calc
    Fintype.card B4 = Fintype.card K4 := (Fintype.card_congr equivK4B4).symm
    _ = 4 := card_K4

/-- Proper-subfield support for the pre-repair `RSCap.lem_phi_fiber_ii`
declaration in `experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean`
at `c4856fa6`. -/
theorem exists_not_mem_B4 : ∃ t : F16, t ∉ B4 := by
  by_contra h
  push_neg at h
  have hle : Fintype.card F16 ≤ Fintype.card B4 :=
    Fintype.card_le_of_injective (fun x : F16 => (⟨x, h x⟩ : B4))
      (fun _ _ hxy => congrArg Subtype.val hxy)
  rw [card_F16, card_B4] at hle
  omega

/-- A fixed element of `GF(16)` outside the embedded `GF(4)`, supporting the
pre-repair `RSCap.lem_phi_fiber_ii` counterexample from
`experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean` at `c4856fa6`. -/
noncomputable def t : F16 := Classical.choose exists_not_mem_B4

/-- Chosen-witness support for the pre-repair `RSCap.lem_phi_fiber_ii`
declaration in `experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean`
at `c4856fa6`. -/
theorem t_not_mem_B4 : t ∉ B4 := Classical.choose_spec exists_not_mem_B4

/-! ## Symbolic cubic obstruction -/

/-- A monic cubic with three distinct roots in a subfield has its quadratic
coefficient in that subfield.  This is counterexample support for the
pre-repair `RSCap.lem_phi_fiber_ii` declaration in
`experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean` at `c4856fa6`. -/
theorem cubic_coeff_two_mem_of_three_roots_in_base
    {I F : Type*} [Field F] (B : Subfield F)
    (root : I → F) (hroot_inj : Function.Injective root)
    (hrootB : ∀ x, root x ∈ B)
    (d : Polynomial F) (hdmonic : d.Monic) (hddeg : d.natDegree = 3)
    (S : Finset I) (hScard : S.card = 3)
    (hroot : ∀ x ∈ S, d.eval (root x) = 0) :
    d.coeff 2 ∈ B := by
  classical
  let locator : Polynomial F := ∏ x ∈ S, (X - C (root x))
  have hlocmonic : locator.Monic := by
    exact monic_prod_of_monic _ _ fun x _ => monic_X_sub_C (root x)
  have hlocdeg : locator.natDegree = 3 := by
    dsimp [locator]
    rw [natDegree_prod_of_monic _ _ fun x _ => monic_X_sub_C (root x),
      Finset.sum_const_nat fun x _ => natDegree_X_sub_C (root x), mul_one, hScard]
  have hlocdvd : locator ∣ d := by
    dsimp [locator]
    refine Finset.prod_dvd_of_coprime (fun x hx y hy hxy => ?_) (fun x hx => ?_)
    · exact Polynomial.pairwise_coprime_X_sub_C hroot_inj hxy
    · rw [Polynomial.dvd_iff_isRoot, Polynomial.IsRoot.def]
      exact hroot x hx
  have heq : d = locator := by
    have h := Polynomial.eq_leadingCoeff_mul_of_monic_of_dvd_of_natDegree_le
      hlocmonic hlocdvd (by rw [hddeg, hlocdeg])
    simpa [hdmonic.leadingCoeff] using h
  have hcoeff : locator.coeff 2 = -∑ x ∈ S, root x := by
    dsimp [locator]
    simpa [hScard] using
      (Polynomial.prod_X_sub_C_coeff_card_pred S root (by omega))
  rw [heq, hcoeff]
  exact B.neg_mem (B.sum_mem fun x _ => hrootB x)

/-- In characteristic two, subtracting degree-`<2` data from
`(X+t)^3 + z(X+t)^2` leaves a monic cubic whose quadratic coefficient is
`t+z`.  This is counterexample support for the pre-repair
`RSCap.lem_phi_fiber_ii` declaration in
`experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean` at `c4856fa6`. -/
theorem shifted_cubic_sub_linear_data
    {F : Type*} [Field F] [CharP F 2]
    (t z : F) (Q : Polynomial F) (hQdeg : Q.degree < (2 : WithBot ℕ)) :
    let d := (X + C t) ^ 3 + C z * (X + C t) ^ 2 - Q
    d.Monic ∧ d.natDegree = 3 ∧ d.coeff 2 = t + z := by
  let d : Polynomial F := (X + C t) ^ 3 + C z * (X + C t) ^ 2 - Q
  have htwo : (2 : F) = 0 := CharP.cast_eq_zero F 2
  have htwoP : (2 : Polynomial F) = 0 := by
    change C (2 : F) = 0
    rw [htwo, C_0]
  have hthreeP : (3 : Polynomial F) = 1 := by
    calc
      (3 : Polynomial F) = 2 + 1 := by norm_num
      _ = 1 := by rw [htwoP, zero_add]
  have hexpand : d = X ^ 3 + (C (t + z) * X ^ 2 + C (t ^ 2) * X
      + C (t ^ 3 + z * t ^ 2) - Q) := by
    dsimp [d]
    ring_nf
    rw [htwoP, hthreeP]
    simp only [map_add, map_mul, map_pow]
    ring
  have hremdeg :
      (C (t + z) * X ^ 2 + C (t ^ 2) * X + C (t ^ 3 + z * t ^ 2) - Q).degree
        < (3 : WithBot ℕ) := by
    compute_degree
    exact max_lt (by norm_num) (lt_trans hQdeg (by norm_num))
  have hdmonic : d.Monic := by
    rw [hexpand]
    exact monic_X_pow_add hremdeg
  have hddeg : d.natDegree = 3 := by
    rw [hexpand]
    have h := natDegree_add_eq_left_of_degree_lt
      (p := (X : Polynomial F) ^ 3)
      (q := C (t + z) * X ^ 2 + C (t ^ 2) * X
        + C (t ^ 3 + z * t ^ 2) - Q)
      (by simpa using hremdeg)
    simpa using h
  have hQcoeff : Q.coeff 2 = 0 := coeff_eq_zero_of_degree_lt hQdeg
  have hdcoeff : d.coeff 2 = t + z := by
    rw [hexpand]
    have hx3 : (X ^ 3 : Polynomial F).coeff 2 = 0 := by simp
    have hquad : (C (t + z) * X ^ 2 : Polynomial F).coeff 2 = t + z := by
      rw [coeff_C_mul, coeff_X_pow, if_pos rfl]
      simp
    have hlinear : (C (t ^ 2) * X : Polynomial F).coeff 2 = 0 := by
      rw [coeff_C_mul, coeff_X]
      simp
    have hconstant :
        (C (t ^ 3 + z * t ^ 2) : Polynomial F).coeff 2 = 0 := by
      rw [coeff_C, if_neg (by decide)]
    rw [coeff_add, hx3, coeff_sub, coeff_add, coeff_add, hquad, hlinear,
      hconstant, hQcoeff]
    ring
  exact ⟨hdmonic, hddeg, hdcoeff⟩

/-- No degree-`<2` polynomial can agree with the shifted cubic on three
distinct embedded base-field points.  This is counterexample support for the
pre-repair `RSCap.lem_phi_fiber_ii` declaration in
`experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean` at `c4856fa6`. -/
theorem no_three_base_agreements
    {I F : Type*} [Field F] [CharP F 2]
    (B : Subfield F) (root : I → F) (hroot_inj : Function.Injective root)
    (hrootB : ∀ x, root x ∈ B)
    (t : F) (ht : t ∉ B) (z : F) (hz : z ∈ B)
    (Q : Polynomial F) (hQdeg : Q.degree < (2 : WithBot ℕ))
    (S : Finset I) (hScard : S.card = 3)
    (hagree : ∀ x ∈ S,
      Q.eval (root x) = (root x + t) ^ 3 + z * (root x + t) ^ 2) : False := by
  let d : Polynomial F := (X + C t) ^ 3 + C z * (X + C t) ^ 2 - Q
  have hdata := shifted_cubic_sub_linear_data t z Q hQdeg
  have hroot : ∀ x ∈ S, d.eval (root x) = 0 := by
    intro x hx
    dsimp [d]
    simp only [eval_sub, eval_add, eval_pow, eval_mul, eval_X, eval_C]
    rw [hagree x hx]
    ring
  have hcoeffB : d.coeff 2 ∈ B :=
    cubic_coeff_two_mem_of_three_roots_in_base B root hroot_inj hrootB d
      hdata.1 hdata.2.1 S hScard hroot
  have htz : t + z ∈ B := by
    rw [← hdata.2.2]
    exact hcoeffB
  exact ht (by simpa using B.sub_mem htz hz)

/-- The exact two-agreement ceiling used to refute the pre-repair
`RSCap.lem_phi_fiber_ii` declaration in
`experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean` at `c4856fa6`. -/
theorem at_most_two_agreements
    (z : F16) (hz : z ∈ B4) (Q : Polynomial F16)
    (hQdeg : Q.degree < (2 : WithBot ℕ)) :
    (Finset.univ.filter fun x : K4 =>
      Q.eval (emb x) = (emb x + t) ^ 3 + z * (emb x + t) ^ 2).card ≤ 2 := by
  classical
  by_contra h
  have h3 : 3 ≤ (Finset.univ.filter fun x : K4 =>
      Q.eval (emb x) = (emb x + t) ^ 3 + z * (emb x + t) ^ 2).card := by omega
  obtain ⟨S, hSsub, hScard⟩ := Finset.exists_subset_card_eq h3
  apply no_three_base_agreements B4 emb emb.injective
      (fun x => show emb x ∈ emb.toRingHom.fieldRange from ⟨x, rfl⟩)
      t t_not_mem_B4 z hz Q hQdeg S hScard
  intro x hx
  exact (Finset.mem_filter.mp (hSsub hx)).2

/-! ## Concrete failure of the old conclusion -/

def phi : Polynomial F16 := X + C t

def received (z : F16) (x : K4) : F16 :=
  (emb x + t) ^ 3 + z * (emb x + t) ^ 2

/-- Degree-premise check for the pre-repair `RSCap.lem_phi_fiber_ii`
declaration in `experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean`
at `c4856fa6`. -/
theorem phi_natDegree : phi.natDegree = 1 := natDegree_X_add_C t

/-- Domain-containment check for the pre-repair `RSCap.lem_phi_fiber_ii`
declaration in `experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean`
at `c4856fa6`. -/
theorem dom_in_base (x : K4) : emb x ∈ B4 := ⟨x, rfl⟩

/-- The counterexample violates exactly the repaired value-level base-field
tie for `RSCap.lem_phi_fiber_ii` in
`experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean` at `3404d21`. -/
theorem phi_eval_not_mem_B4 (x : K4) : phi.eval (emb x) ∉ B4 := by
  intro h
  apply t_not_mem_B4
  have hsub := B4.sub_mem h (dom_in_base x)
  simpa [phi] using hsub

/-- Smoothness-premise check for the pre-repair `RSCap.lem_phi_fiber_ii`
declaration in `experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean`
at `c4856fa6`. -/
theorem phi_smooth : DomSmooth emb (fun x => phi.eval x) 1 := by
  classical
  intro i
  have hset : (Finset.univ.filter fun j : K4 =>
      phi.eval (emb j) = phi.eval (emb i)) = {i} := by
    ext j
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_singleton]
    simp only [phi, eval_add, eval_X, eval_C]
    constructor
    · intro h
      exact emb.injective (add_right_cancel h)
    · intro h
      subst j
      rfl
  rw [hset, Finset.card_singleton]

/-- All hypotheses of the pre-repair `RSCap.lem_phi_fiber_ii` declaration in
`experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean` at `c4856fa6` hold
at the chosen parameters. -/
theorem concrete_old_hypotheses :
    Function.Injective emb ∧
    (∀ x : K4, emb x ∈ B4) ∧
    0 < (1 : ℕ) ∧ phi.natDegree = 1 ∧
    1 * 4 = Fintype.card K4 ∧
    DomSmooth emb (fun x => phi.eval x) 1 ∧
    3 = 1 / 1 + 2 ∧ 3 ≤ 4 - 1 ∧ 3 = 1 * 3 := by
  refine ⟨emb.injective, dom_in_base, by decide, phi_natDegree, ?_, phi_smooth,
    by decide, by decide, by decide⟩
  norm_num [card_K4]

/-- At those parameters, the exact conclusion of the pre-repair
`RSCap.lem_phi_fiber_ii` declaration in
`experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean` at `c4856fa6` is
false. -/
theorem old_phi_fiber_conclusion_false :
    ¬ ∃ (z : F16) (_ : z ∈ B4) (L : ℕ),
      (Nat.choose 4 3 : ℝ) / (Fintype.card B4 : ℝ) ≤ (L : ℝ) ∧
      HasList (RSpoly emb 2) (1 - (3 : ℝ) / Fintype.card K4)
        (fun i => (phi.eval (emb i)) ^ 3 + z * (phi.eval (emb i)) ^ (3 - 1)) L := by
  classical
  rintro ⟨z, hz, L, hL, hlist⟩
  have hlist' : HasList (RSpoly emb 2) (1 - (3 : ℝ) / Fintype.card K4)
      (received z) L := by
    simpa [received, phi] using hlist
  obtain ⟨P, hPmem, _hPinj, hPclose⟩ := hlist'
  have hLpos : 0 < L := by
    rw [card_B4] at hL
    norm_num [Nat.choose] at hL
    exact_mod_cast hL
  let i0 : Fin L := ⟨0, hLpos⟩
  obtain ⟨Q, hQdeg, hQeval⟩ := hPmem i0
  have hclose := hPclose i0
  have hdiff : numDiff (received z) (P i0) ≤ 1 := by
    rw [relDist, card_K4] at hclose
    have hdiffR : (numDiff (received z) (P i0) : ℝ) ≤ 1 := by linarith
    exact_mod_cast hdiffR
  have hsum := Finset.card_filter_add_card_filter_not
    (s := (Finset.univ : Finset K4)) (p := fun x => received z x = P i0 x)
  have hnotcard :
      (Finset.univ.filter fun x : K4 => ¬ received z x = P i0 x).card
        = numDiff (received z) (P i0) := by
    rfl
  rw [hnotcard, Finset.card_univ, card_K4] at hsum
  have hagree3 : 3 ≤
      (Finset.univ.filter fun x : K4 =>
        Q.eval (emb x) = (emb x + t) ^ 3 + z * (emb x + t) ^ 2).card := by
    have hcard : 3 ≤
        (Finset.univ.filter fun x : K4 => received z x = P i0 x).card := by omega
    have hfilters :
        (Finset.univ.filter fun x : K4 =>
          Q.eval (emb x) = (emb x + t) ^ 3 + z * (emb x + t) ^ 2) =
        (Finset.univ.filter fun x : K4 => received z x = P i0 x) := by
      ext x
      simp only [Finset.mem_filter, Finset.mem_univ, true_and]
      rw [hQeval x]
      simp [received, eq_comm]
    rw [hfilters]
    exact hcard
  have hle := at_most_two_agreements z hz Q hQdeg
  omega

end RSCap.PhiFiberRepair

namespace RSCap

open Classical Polynomial
open PhiFiberRepair

universe u v

/-! ## Exact falsity certificate and repaired paper wrapper -/

set_option linter.unusedVariables false in
/-- The pre-repair `RSCap.lem_phi_fiber_ii` statement from
`experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean` at `c4856fa6`,
preserving its binders, hypotheses, and conclusion and omitting exactly the
later-added `hQB`. -/
def LemPhiFiberIIPreRepair : Prop :=
  ∀ {ι : Type u} {F : Type v} [Fintype ι] [Field F] [Fintype F],
    ∀ (dom : ι → F) (hdom : Function.Injective dom)
      (B : Subfield F) [Fintype B] (hdomB : ∀ i, dom i ∈ B)
      (φ : Polynomial F) {a N k ℓ₂ A₂ : ℕ}
      (ha : 0 < a) (hφdeg : φ.natDegree = a)
      (haN : a * N = Fintype.card ι)
      (hsmooth : DomSmooth dom (fun x => φ.eval x) a)
      (hℓ₂ : ℓ₂ = k / a + 2) (hℓ₂N : ℓ₂ ≤ N - 1)
      (hA₂ : A₂ = a * ℓ₂),
    ∃ (z : F) (_ : z ∈ B) (L : ℕ),
      (Nat.choose N ℓ₂ : ℝ) / (Fintype.card B : ℝ) ≤ (L : ℝ) ∧
      HasList (RSpoly dom (k + 1))
        (1 - (A₂ : ℝ) / Fintype.card ι)
        (fun i => (φ.eval (dom i)) ^ ℓ₂ +
          z * (φ.eval (dom i)) ^ (ℓ₂ - 1)) L

/-- **The exact pre-repair `lem_phi_fiber_ii` signature is false.**  The
refuted declaration is in
`experimental/lean/cs25_cap_v12/cs25_cap_v12/Fiber.lean` at `c4856fa6`.

Its universe-zero instance has a `GF(16)/GF(4)` counterexample, which refutes
the original universe-polymorphic declaration.  The counterexample satisfies
the degree premise; only the missing base-field tie fails. -/
theorem lem_phi_fiber_ii_pre_repair_false :
    ¬ LemPhiFiberIIPreRepair.{0, 0} := by
  intro h
  have hbad := h (dom := emb) emb.injective B4 dom_in_base phi
    (a := 1) (N := 4) (k := 1) (ℓ₂ := 3) (A₂ := 3)
    (by decide) phi_natDegree (by norm_num [card_K4]) phi_smooth
    (by decide) (by decide) (by decide)
  exact old_phi_fiber_conclusion_false hbad

/-- Paper-faithful coefficient-level wrapper for the repaired theorem,
formalizing `def:map-smooth` and `lem:phi-fiber` in
`tex/cs25_cap_v13_2.tex` at `4bea7abb`.

Paper D assumes `φ ∈ B[X]`.  Representing that polynomial as `φB : B[X]`
automatically supplies the repaired value-level hypothesis after mapping its
coefficients into `F`. -/
theorem lem_phi_fiber_ii_of_basePolynomial
    {ι F : Type*} [Fintype ι] [Field F]
    (dom : ι → F) (hdom : Function.Injective dom)
    (B : Subfield F) [Fintype B] (hdomB : ∀ i, dom i ∈ B)
    (φB : Polynomial B) {a N k ℓ₂ A₂ : ℕ}
    (ha : 0 < a) (hφdeg : φB.natDegree = a)
    (haN : a * N = Fintype.card ι)
    (hsmooth : DomSmooth dom (fun x => (φB.map B.subtype).eval x) a)
    (hℓ₂ : ℓ₂ = k / a + 2) (hℓ₂N : ℓ₂ ≤ N - 1)
    (hA₂ : A₂ = a * ℓ₂) :
    ∃ (z : F) (_ : z ∈ B) (L : ℕ),
      (Nat.choose N ℓ₂ : ℝ) / (Fintype.card B : ℝ) ≤ (L : ℝ) ∧
      HasList (RSpoly dom (k + 1))
        (1 - (A₂ : ℝ) / Fintype.card ι)
        (fun i => ((φB.map B.subtype).eval (dom i)) ^ ℓ₂ +
          z * ((φB.map B.subtype).eval (dom i)) ^ (ℓ₂ - 1)) L := by
  have hφdegF : (φB.map B.subtype).natDegree = a := by
    rw [Polynomial.natDegree_map]
    exact hφdeg
  have hQB : ∀ i, (φB.map B.subtype).eval (dom i) ∈ B := by
    intro i
    let x : B := ⟨dom i, hdomB i⟩
    have heval : (φB.map B.subtype).eval (dom i) =
        B.subtype (φB.eval x) := by
      change (φB.map B.subtype).eval (B.subtype x) = B.subtype (φB.eval x)
      exact Polynomial.eval_map_apply (p := φB) B.subtype x
    rw [heval]
    exact (φB.eval x).property
  exact lem_phi_fiber_ii dom hdom B hdomB (φB.map B.subtype)
    ha hφdegF hQB haN hsmooth hℓ₂ hℓ₂N hA₂

#print axioms RSCap.lem_phi_fiber_ii_pre_repair_false
#print axioms RSCap.lem_phi_fiber_ii_of_basePolynomial

end RSCap
