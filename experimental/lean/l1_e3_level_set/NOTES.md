# Notes on `E₃ ≤ ℓ − 2` (coset level-set inequality)

## What is in the project

The file `l1_e3_level_set/Main.lean` contains a formalization skeleton for the statement
and surrounding setup. The structural lemmas should be audited before promotion.

Definitions (namespace `CosetLevelSet`, field `𝔽_p = ZMod p`, `[Fact p.Prime]`):

* `cosetF p ℓ w` — the coset `{ x ≠ 0 : x^ℓ = w }` (a fiber of `x ↦ x^ℓ`).
* `levelMax p ℓ Γ w` — `μ(C) = max_λ #{ x ∈ C : Γ(x) = λ }` for the coset with power `w`.
* `powersF p ℓ` — the set of nonzero `ℓ`-th powers, indexing the cosets.
* `E3 p ℓ Γ = Σ_{w ∈ powersF} (levelMax w − 2)`; the truncated `ℕ`-subtraction is exactly
  the positive part `(·)₊`.

The main statement is
```
theorem E3_le (hℓ : ℓ.Prime) (hodd : Odd ℓ) (hdvd : ℓ ∣ p - 1)
    (Γ : (ZMod p)[X]) (hΓ : Γ ≠ 0) (hc0 : Γ.coeff 0 = 0) (hdeg : Γ.natDegree ≤ ℓ - 1) :
    E3 p ℓ Γ ≤ ℓ - 2
```

### Structural backbone, pending local Lean audit

* `levelMax_le_card`, `card_cosetF_le`, `levelMax_le_ell` — a level set has at most as many
  points as its coset, a coset has at most `ℓ` points, hence `μ(C) ≤ ℓ`.
* `card_cosetF_eq` — **every nonempty coset has exactly `ℓ` elements** (the fiber of `x ↦ x^ℓ`
  over a nonzero `ℓ`-th power; via the ℓ-torsion count `gcd(ℓ, p−1) = ℓ` in the cyclic unit
  group).
* `card_powersF` — **there are exactly `n = (p−1)/ℓ` cosets** (image of the `ℓ`-power map on
  the units has size `(p−1)/gcd(p−1, ℓ) = (p−1)/ℓ`).

Together these verify the partition claim of the problem: `𝔽_p^*` splits into `(p−1)/ℓ`
cosets, each of size exactly `ℓ`.

### Not proved (open crux)

The main inequality `E3_le` is left as a `sorry`. It reduces to a genuinely hard, and (per
the problem statement) open, crux — see below.

## Computational validation of the statement

The inequality was checked by exhaustive search (over `ZMod p`, all admissible `Γ ≠ 0`):

* `p = 7,  ℓ = 3`  (`n = 2` cosets): `max E₃ = 0 ≤ 1 = ℓ − 2`.
* `p = 11, ℓ = 5`  (`n = 2` cosets): `max E₃ = 2 ≤ 3 = ℓ − 2`.

(A subtlety that the formal statement must and does capture: `μ(C) = ℓ` would force `Γ` to be
constant on a whole coset, i.e. `Γ − λ` to have `ℓ` roots with `deg(Γ−λ) ≤ ℓ−1`, hence
`Γ` constant; combined with `Γ(0) = 0` this gives `Γ = 0`, which is excluded. Dropping
`Γ ≠ 0` makes the bound fail, e.g. `Γ = 0` gives `E₃ = n·(ℓ−2)`.)

## The reduction and the crux

For each *excess* coset (`μ_k := μ(C_k) ≥ 3`, `k = 1..K`) fix a maximal level set `F_k`
(size `μ_k`, common value `c_k`) and set
`g_k = ∏_{x∈F_k}(X−x)` (degree `μ_k`), `h_k = (X^ℓ − w_k)/g_k` (degree `ℓ−μ_k`), so
`g_k h_k = X^ℓ − w_k`. Let `V_k = h_k · 𝔽_p[X]_{≤ μ_k−2} ⊆ 𝔽_p[X]_{≤ ℓ−2}` (dimension
`μ_k − 1`). Then `Σ_k dim V_k = E₃ + K`, and with the functional
`L(A) = [X^{ℓ−1}](A·Γ)` one shows (elementary degree count) every `V_k ⊆ ker L`, whence
`dim(V_1+⋯+V_K) ≤ ℓ − 2` (**upper half**, elementary).

Because `dim(ΣV_k) = (E₃ + K) − dim Syz` where
`Syz = { (q_k) : Σ_k h_k q_k = 0, deg q_k ≤ μ_k − 2 }`, the inequality `E₃ ≤ ℓ − 2` is
**equivalent** to the crux
```
dim(V_1 + ⋯ + V_K) ≥ E₃     ⟺     dim Syz ≤ K .
```

## Flagged hypothesis: the crux is NOT a statement about coprime polynomials alone

The crux is true only because all the `F_k` are level sets of a **single** polynomial `Γ`
of degree `≤ ℓ − 1`. The purely formal statement

> "for pairwise-coprime `h_1,…,h_K` with `deg h_k = d_k` and bounds `b_k = N − d_k`
> (`N = ℓ − 2`), the degree-bounded syzygy module `Syz` has `dim Syz ≤ K`"

**is false.** Counterexample (rank–nullity): take `N = 4`, `K = 3` and pairwise-coprime
`h_1 = X−1, h_2 = X−2, h_3 = X²−X−1` with `d = (1,1,2)`, `b = (3,3,2)`. The domain
`⊕_k 𝔽[X]_{≤ b_k}` has dimension `Σ(b_k+1) = 4+4+3 = 11`, while the sum map lands in
`𝔽[X]_{≤ 4}` of dimension `5`, so `dim Syz ≥ 11 − 5 = 6 > 3 = K`. Hence coprimality plus the
degree bookkeeping is insufficient; the global "single `Γ`" structure is essential. This is
exactly the "it is FALSE for arbitrary configurations of fibers" remark in the problem, and
it is the additional hypothesis a correct proof of the crux must exploit.

The `K = 2` case is elementary (the two `h_k` are coprime and the degree bounds force
`q_1 = q_2 = 0`), but for general `K` a complete argument requires more than the tools set up
here, and is left open.

## A lead toward the crux (uses the single-`Γ` structure)

Write `s_k := (Γ − c_k)/g_k` (a polynomial, since `g_k ∣ Γ − c_k`), so `deg s_k ≤ ℓ−1−μ_k`
and `g_k s_k = Γ − c_k`, `g_k h_k = X^ℓ − w_k`. Then for **every** degree-bounded syzygy
`(q_k)` (i.e. `Σ_k h_k q_k = 0`, `deg q_k ≤ μ_k − 2`):

* Multiplying the syzygy by `Γ` and using `h_k(Γ − c_k) = h_k g_k s_k = (X^ℓ − w_k) s_k`,
  ```
  0 = Γ·Σ_k h_k q_k = Σ_k q_k h_k (Γ − c_k) + Σ_k c_k q_k h_k
    = Σ_k q_k (X^ℓ − w_k) s_k + Σ_k c_k q_k h_k
    = X^ℓ · (Σ_k q_k s_k) − Σ_k w_k q_k s_k + Σ_k c_k q_k h_k .
  ```
* The last two sums have degree `≤ ℓ−2`, while `X^ℓ·(Σ_k q_k s_k)` occupies degrees `≥ ℓ`
  (as `deg(Σ q_k s_k) ≤ ℓ−3`). Since there is no overlap, the top part must vanish, giving
  the **new relation** `Σ_k s_k q_k = 0`, together with `Σ_k w_k q_k s_k = Σ_k c_k q_k h_k`.

So every degree-bounded syzygy of the `h_k` is *also* a syzygy of the `s_k`. This is a
genuine consequence of all `F_k` being level sets of the same `Γ` (it is exactly the extra
structure the false coprime-only version lacks). It cuts down `Syz`, but by itself does not
yet yield `dim Syz ≤ K`; completing the crux from here is left open.
