# b2 giant-extras core ≡ L1 route-A E_3 core (fold-in, 2026-07-06)

- **Status:** UNIFICATION NOTE. Connects two lanes; no bound proved.
- **Claim:** the b2 `mod-p giant-extras` bound and the L1 route-A `E_3 ≤ ℓ−2` bound reduce, past the
  same `√p` Weil barrier, to the SAME additive-combinatorics inverse theorem — so one core lemma
  discharges both, and progress on either transfers.

## The two problems

| | **L1 route A** (`l1_e3_route_A_high_moment_scoping.md`) | **b2 prong 1** (`b2_modp_giant_extras_first_move.md`) |
|---|---|---|
| object | `M_r = Σ_x K(x)^{r-1}`, `K(x)=#{ζ∈μ_ℓ: Γ(ζx)=Γ(x)}` (r-fold coincidence count) | `extras_b = q^{-t} Σ_c S_b(c)`, `S_b(c)=[z^b]∏_{x∈μ_n}(1+z·e_q(f_c(x)))` |
| polynomial on a mult. subgroup | `Γ` (deg ≤ ℓ−1) on `μ_ℓ`-cosets | `f_c=Σ_r c_r x^r` (deg ≤ t) on `μ_n` |
| per-frequency / per-character Weil | INSUFFICIENT: char maxima `~3√p`, identical extremal vs random (`moment_charsum_test.sage`) | INSUFFICIENT: `p_r(c)` Weil-small `~√q`, but giant-b `|S_b(c)|` mean 2473/max 493394 vs count 32 (`b2_prong1_fixed_b.py`) |
| barrier | `√p` (CAP25 line 8144) | `√p` (CAP25 Rem 16.10) |
| surviving route | joint cancellation = BGK inverse theorem | joint cancellation = BGK inverse theorem |

**Both** are "bound a value-coincidence / high-moment character sum of a polynomial restricted to a
multiplicative subgroup, where per-frequency Weil hits `√p` and only joint (BGK-style) cancellation
survives." The reductions are independent (different lanes, papers, reviewers) yet land on one core.

## The shared core lemma (milestone-paper candidate)

> **CORE.** A bound on value-coincidence moments of a low-degree polynomial on a multiplicative
> subgroup `H ≤ 𝔽_q^*`, tight enough to beat the `√p` barrier, via the BGK / Bourgain–Glibichuk–Konyagin
> additive-combinatorics inverse theorem (large moment ⇒ quotient-stabilizer / block-structured support).

Discharging CORE gives `E_3 ≤ ℓ−2` (L1) **and** the giant-extras `≤ n^3` (b2). Per the multiyear-program
decomposition this is the right milestone: one lemma, two lanes. **b2 is the more tractable entry point**
— its 123-bit cushion (`2^100`-lossy OK) means CORE need only be crude for b2, whereas L1 needs it sharp.

> **CORRECTION (2026-07-06, after the D1 literature dive + D3 structure computation — see
> `b2_l1_lemma_draft.md`).** "One CORE lemma discharges both lanes" is an OVER-UNIFICATION. The two
> lanes share the `√p` barrier and the "inverse theorem" *framing*, but NOT one dischargeable lemma:
> - **b2** (large subgroup `|H|=2^41 ≥ q^{0.16}`, cushion): a crude BGK/Heath-Brown–Konyagin single-sum
>   bound is IN-REGIME and precise enough — essentially citeable.
> - **L1** (needs uniformity over all `ℓ|p−1` incl. tiny `ℓ`, and the EXACT `ℓ−2`): every subgroup
>   moment/energy method is out of regime and out of precision (only `p^{-ν}` / log savings; Carlitz–
>   McConnel collapses to linear over prime fields). The moment/BGK route — including the Step-3
>   monodromy handle — is a **DEAD END for L1's sharp bound**. L1's real route is the **rank statement
>   `dim Syz ≤ K`** (the lane's pre-existing crux), NOT an inverse theorem.
> So: refocus L1 on `dim Syz ≤ K`; take the BGK draft only for b2. The "shared core" is the barrier +
> the extremal-rigidity picture, not a common proof.

## Shared computable object: the pencil monodromy (structure detection)

Both moments are governed by the monodromy `G = Gal(pencil / 𝔽_p(t))` of `ψ: X ↦ X^ℓ/Γ(X)`
(`pencil_monodromy.sage`). If EXTREMAL `Γ` (large `E_3`) have SPECIAL/small `G` while random `Γ` give the
full symmetric group, monodromy DETECTS the structure geometrically (the inverse theorem's structured
case), and the bound follows from a monodromy classification. If both give the full group, monodromy is
BLIND to `E_3` (the decorrelation trap) and the BGK route is the only one. **Step 3 computes this**
(`b2_l1_pencil_monodromy_v2.sage`), correcting the stalled pass (base-point + symbolic transitivity).

## Step 3 RESULT (2026-07-06, Codex-GREEN): monodromy is BLIND to E_3 → BGK is the sole route

Corrected pencil monodromy `G = Gal(X^{ℓ-1} − t·γ / 𝔽_p(t))` (base point `X=0` stripped since `X | Γ`;
transitivity = symbolic irreducibility over `𝔽_p(t)`; group ID = **rigorous GAP transitive-subgroup
filter**, not just Chebotarev thresholds):

| Γ | `E_3` | `P[(ℓ−1)-cycle]` (S: `1/(ℓ−1)`) | `P[odd]` (S: `½`) | GAP survivors |
|---|---|---|---|---|
| **extremal** ℓ=11 | 9 | 0.088 (0.100) | 0.52 | **only `S_10` (10!)** |
| **extremal** ℓ=13 | 11 | 0.081 (0.083) | 0.55 | **only `S_12` (12!)** |
| random ℓ=11 | 0 | 0.10/0.08 | 0.48/0.46 | `S_10` |
| random ℓ=13 | 0 | 0.083/0.084 | 0.57 | `S_12` |

**Extremal `Γ` (E_3=ℓ−2) and random `Γ` (E_3=0) have the IDENTICAL full-symmetric-group monodromy** — the
GAP filter leaves only `S_{ℓ-1}` for the extremal cases. So the pencil monodromy is BLIND to `E_3`: the
geometric / Katz-equidistribution handle CANNOT see or bound the extremal structure (a concrete
confirmation of the decorrelation trap and the route-A Step-2 finding). **Therefore the BGK
additive-combinatorics inverse theorem is the SOLE surviving route for the shared core.** Route
eliminated, effort focused. Caveat: toy `ℓ=11,13`; the pencil `ψ=X^ℓ/Γ` is the natural monodromy object
(a more exotic refined monodromy is not ruled out, but the natural one is blind).

## Cross-refs
`b2_modp_giant_extras_first_move.md`, `l1_e3_route_A_high_moment_scoping.md`, `pencil_monodromy.sage`,
`l1_cyclotomic_directions_bridge.md` / `l1_e3_lacunary_directions_connection.md`. Memory:
[[project-rsmca-proximity-prize]], [[feedback-transport-decorrelation-trap]].
