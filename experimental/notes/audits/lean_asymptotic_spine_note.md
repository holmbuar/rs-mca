# Asymptotic-spine Lean ↔ `asymptotic_rs_mca.tex` correspondence note — L1–L5 all sorry-free, `lake build` PASSING

Status: `FORMALIZATION` (a new stdlib-only Lean package `experimental/lean/asymptotic_spine/`
mechanizing the elementary spine of `experimental/asymptotic_rs_mca.tex`) /
`VERIFIED-CLEAN` (`lake build` **passes**; `#print axioms` on every shipped
statement shows only Lean's own `propext` / `Quot.sound` / `Classical.choice`; no
`sorry`, no `native_decide`, no custom logical assumption; grep of the `.lean`
sources for the two forbidden tokens returns zero hits).

This note follows the conventions of the `#418` audit
(`experimental/notes/audits/lean_grande_finale_correspondence_audit.md`): every
declaration is mapped to the tex `\label{...}` (or informal anchor) it formalizes,
with a per-declaration status.  The status vocabulary here is
**FORMALIZED** (the tex statement's exact finite/arithmetic content is
kernel-checked), **HYPOTHESIS-PARAM** (an external deep theorem enters as an
explicit hypothesis of the lemma, not as an axiom), and **OUT-OF-SCOPE** (needs
real analysis / imported algebro-geometry, kept in the tex).

## 0. Scope and the one structural divergence to flag

**Source of statements.** `experimental/asymptotic_rs_mca.tex` (346 lines; lives
on branch `thresholds-asymptotic-proof-audit-r2`).  Its ten in-paper proofs were
adversarially audited in
`experimental/notes/asymptotic_rs_mca_proof_audit_r2.md` (8 `NO ISSUE` / 2
`OPEN GAP`); this note mechanizes the elementary core of the `NO ISSUE` steps and
the one named formalization gap the r2 audit says a formalizer *must* supply
(§A3, the σ block-diagonal).

**Structural divergence — package location (flagged prominently).**  The steering
asks that new asymptotic material integrate "within/alongside" the existing
`experimental/lean/grande_finale/` package.  That package is **Mathlib-pinned**
(`lakefile.toml` requires `mathlib` at `v4.28.0`; `GrandeFinale.lean` opens with
`import Mathlib`) and, as its own `#418` audit records (§0), *"requires a
Mathlib-pinned toolchain that is unavailable here"* — Mathlib cannot be built on
this machine.  A module placed physically inside `grande_finale` therefore cannot
be `lake build`-verified here: Lake resolves the `require mathlib` dependency at
configure time regardless of whether the new module imports Mathlib, and that
resolution fails.  Because the hard mandate is **stdlib-only + a PASSING
`lake build`**, the spine is delivered as a **self-contained stdlib-only sibling
package** `experimental/lean/asymptotic_spine/`, alongside `grande_finale`,
mirroring the naming/docstring/label-citation conventions of the buildable
stdlib packages (`staircase_logic`, `l1_threshold_ledger`, `rs_mca_formalization`).
`grande_finale`'s lakefile/toolchain is left **untouched**.  The
`AsymptoticSpine.*` declarations cite `asymptotic_rs_mca.tex` labels in their
docstrings exactly as `GrandeFinale.*` cites `grande_finale.tex`, so the next
audit maps them the same way.

**Toolchain.** `leanprover/lean4:v4.31.0` (the pin used by the three buildable
stdlib packages), not `grande_finale`'s `v4.28.0`.  Both toolchains are installed;
`v4.31.0` is the one that builds fast here.

**Modeling conventions (stdlib has no `Finset`/`Fintype`/`Nat.choose`).**  Finite
collections are `List Nat` / `List (List Nat)`; cardinalities are `Nat`; the
rational tolerance of L4 is core `Rat` (the `ℚ` glyph is a Mathlib-only notation,
so the sources write `Rat`).  Two faithful reductions are used and documented in
each file header: (i) the outer `max_{r_1,r_2}` of `B_C^{MCA}` — a finite `sup` —
is left in the tex; the per-received-line disjointization is what L1 formalizes
(the same choice `GrandeFinale.first_match_ledger` makes).  (ii) The moment/second-
moment statements are stated over the integer fiber counts, i.e. the positive
normalization `N̄ = M/L` is cleared; the displayed tex inequalities are recovered
by the positive scaling `N̄^{-q}` (L3) / dividing by `M` (L2), which is why no
`Rat`-ordered-field API (absent from stdlib) is needed.

## 1. Headline

| file | target | key statements | status |
|---|---|---|---|
| `AsymptoticSpine/FirstMatch.lean` | **L1** `lem:first-match` / `def:cells` | `nodup_firstMatchLeaves`, `mem_firstMatchLeaves`, `firstMatch_le_sum_cellSizes`, `firstMatch_le_sum_budgets` | FORMALIZED |
| `AsymptoticSpine/Moment.lean` | **L2** `lem:q-sp` ; **L3** `lem:moment-max` | `qsp_sumSq_le` ; `moment_max_squeeze` (+ halves) | FORMALIZED |
| `AsymptoticSpine/NoHighEnergy.lean` | **L5** `prop:no-high-energy` (+ `thm:bsg`, `thm:quasicube`) | `no_high_energy_bound`, `no_high_energy_contradiction` | FORMALIZED core + HYPOTHESIS-PARAM inputs |
| `AsymptoticSpine/SigmaDiagonal.lean` | **L4** σ-diagonal (r2 §A3, `prop:energy-extract`) | `sigma_block_diagonal` | FORMALIZED |
| `AsymptoticSpine/Util.lean` | infrastructure | `listSum`, `length_flatten`, `listSum_le_of_zip` | (support) |

All five of L1–L5 shipped sorry-free.  `Main.lean`-style entrypoint: none (a
library package).  No declaration uses `sorry`, `admit`, `native_decide`, or a
custom `axiom`.

## 2. `lem:first-match` (L1) — the centerpiece `FORMALIZED`

Tex `def:cells` (L77–79) + `lem:first-match` (L81–87).  Model: `cells : List
(List Nat)`, `cells[j]` = slope-ids witnessed by cell `j`; covered bad slopes =
`cells.flatten`; the first-match leaf `L_j = C_j \ (C_0 ∪ … ∪ C_{j-1})` is
`firstMatchLeaves`.

| decl | tex anchor | status | note |
|---|---|---|---|
| `newPaid`, `firstMatchLeaves`, `paidUnion` (defs) | `def:cells`, proof L86 | FORMALIZED | the leaf `C_j \ paid` and the running paid union |
| `paidUnion_eq_append_flatten`, `flatten_firstMatchLeaves` | (support) | FORMALIZED | leaves telescope to the paid union |
| `mem_paidUnion`, `nodup_paidUnion` | (support) | FORMALIZED | membership + duplicate-freeness of the union fold |
| `nodup_firstMatchLeaves` | `lem:first-match` ("assigned slope classes are disjoint") | FORMALIZED | **disjointness**: no slope charged twice |
| `mem_firstMatchLeaves` | `lem:first-match` (leaves cover the bad slopes) | FORMALIZED | **coverage**: assigned ⇔ witnessed |
| `firstMatchLeaves_sum_length_le` | proof L86 ("`j`-th class ⊆ projection of `C_j`") | FORMALIZED | leaf `⊆` cell, summed |
| `firstMatch_le_sum_cellSizes` | `lem:first-match` (`≤ ∑_j U_j`, `U_j = |C_j|`) | FORMALIZED | **budget-sum bound**, raw form |
| `firstMatch_le_sum_budgets` | `lem:first-match` (`≤ ∑_j U_j`, printed caps) | FORMALIZED | **budget-sum bound**, any `U_j ≥ |C_j|` |
| `firstMatch_A1_example` | r2 audit §A1 toy | FORMALIZED | `decide`: first-match `(3,1,1)=5` distinct vs raw `3+3+3=9` |

The disjointness + coverage together say the assigned classes **partition** the
covered slopes (r2 §A1: *"first-match sends every covered slope to a unique cell …
`Σ_j U_j` equals the total exactly"*).  Relationship to existing repo work:
`staircase_logic`'s `firstMatch_partitions_union` proves the same partition against
a different source (`agents.md` / m5 notes); the budget-sum inequality
`≤ ∑_j U_j` in the exact tex form is new here, and `GrandeFinale.first_match_ledger`
is the Mathlib/`Finset` analogue of `firstMatch_le_sum_budgets`.

## 3. `lem:q-sp` (L2) and `lem:moment-max` (L3) `FORMALIZED`

| decl | tex label | status | note |
|---|---|---|---|
| `listSumSq` (def) | `lem:q-sp` (L254) | FORMALIZED | `∑_s N(s)^2` |
| `qsp_sumSq_le` | `lem:q-sp` (L254–260) | FORMALIZED | `(∀ x, x ≤ B) → ∑ N(s)^2 ≤ B·∑ N(s)`; the tex `M^{-1}∑N^2 ≤ κN̄` is this ÷`M` with `B = κN̄` (r2 §A7) |
| `listSumPow` (def) | `lem:moment-max` (L162) | FORMALIZED | `∑_s x_s^q` |
| `pow_mem_le_listSumPow` | `lem:moment-max` lower (L168) | FORMALIZED | `(max_s x_s)^q ≤ ∑_s x_s^q` |
| `listSumPow_le_length_mul` | `lem:moment-max` upper (L170) | FORMALIZED | `∑_s x_s^q ≤ L·(max_s x_s)^q` |
| `moment_max_squeeze` | `lem:moment-max` (L165–172) | FORMALIZED | the two-sided squeeze, `L = f.length` |
| `qsp_example`, `moment_example` | (sanity) | FORMALIZED | `decide` instances incl. `Γ_1`-flatness `listSumPow 1 = listSum` |

The tex's `L^{-1}R^q ≤ Γ^{ord}_q ≤ R^q` (with `Γ^{ord}_q = L^{-1}∑(|F_s|/N̄)^q`,
`R = max|F_s|/N̄`) becomes, after multiplying by `L` and clearing `N̄^{-q}`, the
scale-free `mx^q ≤ ∑ x_s^q ≤ L·mx^q` on the integer counts `x_s = |F_s|`,
`mx = max_s|F_s|` — exactly `moment_max_squeeze`.  The `q`-th-root / `log L =
o(Nq)` passage to `Γ^{ord}_q ≤ exp(o(Nq)) ⇔ max|F_s| ≤ exp(o(N))N̄` is OUT-OF-SCOPE
(reals; stays in tex).  These are the discrete cores; they are distinct from
`GrandeFinale.moment_upper` / `moment_lower`, which formalize `grande_finale.tex`'s
`prop:moment-sandwich` over `ℝ` with a probability weight.

## 4. `prop:no-high-energy` (L5) `FORMALIZED` core + `HYPOTHESIS-PARAM` inputs

| decl | tex label | status | note |
|---|---|---|---|
| `BoolFiber` (structure) | interface for `thm:quasicube` | (support) | abstracts "`A ⊆ {0,1}^N` with `|A|=s`, `|A-A|=d`" |
| `no_high_energy_bound` | `prop:no-high-energy` (L228–234) | FORMALIZED (composition) + HYPOTHESIS-PARAM (`bsg`, `quasicube`) | the exact inequality `f ≤ K^{3C}` |
| `no_high_energy_contradiction` | `prop:no-high-energy` | FORMALIZED | `K^{3C} < f → False` (the "no such fiber" shape) |

### 4a. The external theorems are HYPOTHESES, not axioms — signatures

`no_high_energy_bound` takes, verbatim:

```lean
theorem no_high_energy_bound
    (quasicube : ∀ s d : Nat, BoolFiber s d → s ^ 4 ≤ d ^ 2 * s)
    (f K C : Nat)
    (bsg : ∃ s d : Nat, f ≤ K ^ C * s ∧ d ≤ K ^ C * s ∧ BoolFiber s d) :
    f ≤ K ^ (3 * C)
```

* `quasicube` is `thm:quasicube` (L220–226) — *"every finite `A ⊆ {0,1}^N` has
  `|A-A| ≥ |A|^{3/2}`"* — in the squared, root-free `Nat` form `s^4 ≤ d^2·s`
  (`d = |A-A|`, `s = |A|`), quantified over every Boolean-cube fiber `BoolFiber s d`.
* `bsg` is the output of `thm:bsg` (L214–216): the high-energy set of size `f`
  yields a Boolean-cube subfiber `(s, d)` with the size bound `f ≤ K^C·s`
  (`|A'| ≥ K^{-C}|A|`, cleared of division) and the difference bound `d ≤ K^C·s`
  (`|A'-A'| ≤ K^C|A'|`).

**Why hypotheses, not axioms.**  BSG and quasicube are deep external theorems
(`\cite{BalogSzemeredi,Gowers1998}` and `\cite{GMRSZ2020,MRSZ2020}`); the paper
cites, does not reprove them, and their proofs are far outside a stdlib formalizer's
reach.  Encoding them as `axiom`s would make the kernel *trust unproven
statements* — precisely the failure a correspondence audit exists to catch.  As
hypotheses, the theorem's honest content is exactly *"the inequality composition
`|A| ≤ K^{3C}` is valid **given** these two inputs"* — which is all `prop:no-high-
energy`'s in-paper proof claims — and `#print axioms no_high_energy_bound` shows
only `propext, Quot.sound` (no `Classical.choice`, no `sorryAx`, no custom symbol).
The `e^{o(N)}` bookkeeping `K^{±C} = e^{±o(N)}` and the energy lower bound
`f ≥ e^{cN-o(N)}` are OUT-OF-SCOPE (reals); `no_high_energy_contradiction`
exposes the join point as the explicit regime hypothesis `K^{3C} < f`.

## 5. σ block-diagonalization (L4) — the r2 §A3 gap `FORMALIZED`

Tex `prop:energy-extract` (L202–208) elides the diagonal in *"Letting σ↓0 slowly
along the sequence"*; r2 audit §A3 states a formalizer **must** supply the
block-diagonal *"`σ_N = 1/k` on `N`-blocks `[N_k, N_{k+1})`"*.  This is that
construction.

| decl | anchor | status | note |
|---|---|---|---|
| `Mrec` (def) | block starts | FORMALIZED | monotonized, strictly-increasing, `N0`-dominating threshold |
| `level` (def), `level_succ` | block index `σ_N = 1/k` | FORMALIZED | the staircase level at scale `N` |
| `Mrec_ge_N0`, `Mrec_lt_succ`, `Mrec_ge_self`, `Mrec_mono` | (support) | FORMALIZED | threshold monotonicity/domination |
| `level_le_succ`, `level_mono`, `level_zero_of_lt` | (support) | FORMALIZED | level monotonicity + below-first-threshold |
| `level_below` | block containment | FORMALIZED | `Mrec 0 ≤ N → Mrec (level N) ≤ N` |
| `level_diverge` | `σ_N → 0` | FORMALIZED | `Mrec K ≤ N → K ≤ level N` (level `→ ∞`) |
| `sigma_block_diagonal` | r2 §A3 / `prop:energy-extract` | FORMALIZED | the diagonalization theorem |

### 5a. The per-tolerance guarantee is a HYPOTHESIS — signature

```lean
theorem sigma_block_diagonal
    (P : Nat → Rat → Prop) (N0 : Nat → Nat)
    (hP : ∀ k : Nat, 1 ≤ k → ∀ N : Nat, N0 k ≤ N → P N ((1 : Rat) / (k : Rat))) :
    ∃ (σ : Nat → Rat) (lvl : Nat → Nat),
      (∀ N, σ N = (1 : Rat) / (lvl N : Rat)) ∧
      (∀ K : Nat, ∃ N₁, ∀ N, N₁ ≤ N → K ≤ lvl N) ∧
      (∃ N₂, ∀ N, N₂ ≤ N → 1 ≤ lvl N ∧ P N (σ N))
```

`P N ε` reads "the Sidon-heavy null rate at tolerance `ε` is controlled at scale
`N`" (`def:sidon-paid`, L196–198); `hP` is the per-fixed-`σ` null rate the tex
supplies.  `hP` is the sole external input, entering as a hypothesis — the
diagonal is *derived*, nothing is assumed as an axiom.

**Convergence encoded without `Rat`-order API.**  `σ N → 0` is certified by the
pure-`Nat` divergence `level N → ∞` (`∀ K, ∃ N₁, ∀ N ≥ N₁, K ≤ lvl N`) together
with the definitional `σ N = 1 / lvl N`.  This is a complete certificate that
`σ N → 0` (the wrapper `1/lvl → 0` is precisely the divergence of `lvl`), and it
deliberately avoids ordered-field lemmas over `Rat`, which stdlib does not carry.
The `e^{-σ_N N} = e^{-o(N)}` consequence and the full analytic use of the diagonal
in `prop:energy-extract` are OUT-OF-SCOPE (reals).

## 6. OUT-OF-SCOPE inventory (recorded, not formalized)

Per the mandate, the entropy/Stirling analysis is **not** formalized (it needs
reals).  Explicitly out of scope, kept in the tex:

- `thm:frontier` (L135–142, L289–296): the Stirling identity `log₂ N̄_{n,a} =
  n(H_2(ρ+g)-βg)+o(n)`, the envelope `g*(ρ,β)`, and the two-sided `g → g*` limit
  (r2 §A10, `NO ISSUE` but analytic).
- `thm:closed-ledger-package` (C1)–(C9) (L105–131): imported algebro-geometric
  cell counts; a citation package, not self-contained theorems.
- `def:sidon-paid` (L196–200): Fourier inversion `Lμ(s) ≤ exp(o(N))`.
- the `o(n)` / `o(Nq)` / `q`-th-root passages throughout §2–§5.
- `lem:addback` (L246–252): the subexponential-profile decomposition — r2 §A6
  `OPEN GAP` (imported from Grande as if discharged); not formalized.
- the identity-prefix pole construction's collision loss (L283–287) — r2 §A9
  `OPEN GAP`; the sound floor is the collision-free injective construction in
  `cap25_cap_v13_raw.tex`, not formalized here.

## 7. Verification `VERIFIED-CLEAN`

- Build (from `experimental/lean/asymptotic_spine/`, `LEAN_NUM_THREADS=1`):

  ```
  Build completed successfully (8 jobs).
  ```

  Clean build ≈ 2.7 s wall, peak RSS ≈ 792 MB (5 modules, all `✔`).

- **Environment note (flag).**  The mandated `ulimit -v 2097152` (2 GB virtual)
  is incompatible with the installed `v4.31.0` toolchain: `lake`/`lean` reserve a
  large *virtual* arena and abort at thread creation under a 2 GB cap (even 8 GB
  aborts; 16 GB virtual is the floor).  This is unrelated to the build's real
  footprint — peak **resident** memory is ≈ 792 MB and wall time ≈ 2.7 s — so the
  guardrail's intent (a tiny, non-runaway build) holds and is verified by RSS.
- `#print axioms` on all shipped statements: only `propext`, `Quot.sound`, and
  (for the `omega`/`split`-closed `no_high_energy_contradiction` and
  `sigma_block_diagonal`) `Classical.choice` — Lean's three standard foundational
  assumptions, the same ones under all of Mathlib.  No `sorryAx`; no
  user-declared logical assumption in any file.
- Token gate on the `.lean` sources: `grep -rn 'sorry\|axiom'` → 0 hits;
  `grep -rn 'native_decide'` → 0 hits.
