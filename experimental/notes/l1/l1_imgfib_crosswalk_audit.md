# L1 imgfib crosswalk — adversarial audit

Status: AUDIT
Scope: gates the roadmap-promotion decision the maintainer flagged
("Audit the L1 crosswalk against in-repo proof artifacts before promoting
roadmap language").

Audits the claim (imgfib, PROVED 2026-07-13) crosswalked in
`experimental/notes/l1/l1_official_rows_crosswalk_20260713.md`: that the
official-row instances of the upstream assumption **ass:locator**
("Field-aware locator local limit", `archived/snarks_v4.tex` lines
368-382) are theorem-backed at all four official prize rows by the imgfib
chain (`petal_growth + conj_f + l1_program_frontier +
dyadic_profile_evaluation + payment_completeness`).

External proof trail audited at the collaborator's DAG
(github.com/AllenGrahamHart/rs-mca-prize-dag; node `imgfib` and its five
wired children under `critical/nodes/`). Upstream pin as in the crosswalk:
rs-mca snarks_v4.tex, `ass:locator`; target `towards-prize.md` §"L1.
Generated-Field Locator Local Limit" (lines 816-825).

Every number reported below is recomputed by
`experimental/scripts/verify_l1_imgfib_crosswalk_audit.py`
(stdlib, deterministic, `RESULT: PASS (41/41)`, `--tamper-selftest`
catches every corrupted constant).

---

## 1. Anchor check — quote fidelity and the three hypotheses

**Integration fidelity — NO ISSUE.** The integrated note
`l1_official_rows_crosswalk_20260713.md` is **byte-identical** to the
collaborator's source `critical/nodes/imgfib/notes/l1_upstream_crosswalk_20260713.md`
(diff empty). The maintainer withheld only the roadmap-promotion text, as
recorded.

**ass:locator quoted faithfully — NO ISSUE.** The upstream assumption
(snarks_v4.tex, lines 368-382) attaches **three** hypotheses to the
conclusion `|ImgFib_U(k_n+σ_n)| ≤ n^{B_L}`:

- (H-scale) `σ_n ≥ C_{ρ,B_L,ε}·n/log₂ n`,
- (H-entropy) `σ_n log₂ q_n ≥ (1+ε) log₂ C(n, k_n+σ_n)`,
- (H-qprof) all active quotient-core profiles satisfy eq:qprofile-list-budget
  (`Qprof_H(a,k) ≤ B_L log₂ n + Γ_Q`, lines 359-362).

All three appear in the crosswalk (as clauses 4, 3, 5 respectively) — **no
dropped hypothesis**. The consequence clause 9 quotes lem:fiber-list
(`|Λ(C,1−a/n,U)| = |ImgFib_U(a)|`, snarks_v4.tex lines 197-208), which is
upstream-proved; TRANSFERS is correct.

## 2. Per-clause verdicts

| # | Crosswalk verdict | Audit verdict | Evidence |
|---|---|---|---|
| 1 | MATCH (ours stronger) | **NO ISSUE** | "for every received word U" faithful; clause-(P) atlas word-independence independently confirmed (§4, `cp_verify.py` P-v) |
| 2 | MATCH at rows | **NO ISSUE** | honest: single uniform `B_L` across the family explicitly not claimed |
| 3 | MATCH | **NO ISSUE** | (H-entropy) is the verbatim imgfib hypothesis |
| 4 | SUBSUMED in scope | **FIXED** | verdict survives via *hypothesis non-consumption*, but the stated reason ("clause 3 forces σ = Ω(n), far stronger") is refuted at all four rows (§3) |
| 5 | MATCH at rows (exact) | **NO ISSUE** | `dyadic_profile_evaluation` Q_M reproduced exactly: 99.8063 / 66.1465 / 82.9664 (§4); node `verify.py` reruns PASS |
| 6 | MATCH | **OPEN GAP** | mixed-petal / diffuse-partial-petal amplification is CONJECTURAL and out of the petal nodes' scope (§5) |
| 7 | MATCH at rows | **NO ISSUE** (minor convention note §6) | generated-field 2-power rows; `q ≡ 1 mod n` |
| 8 | N/A (freedom unused) | **NO ISSUE** | `k = 2^40` fixed; O(1) freedom is upstream flexibility |
| 9 | TRANSFERS | **NO ISSUE** | lem:fiber-list upstream-proved; `|Λ| = |ImgFib|` |

## 3. Clause 4 (SUBSUMED) — re-derivation: verdict stands, reason is wrong

**Attack.** The crosswalk argues (H-scale) is redundant because "at the
official rows (q < 2^256, log₂ C(n,·) = Θ(n)) clause 3 forces σ = Ω(n),
far stronger". Re-derive the entropy threshold exactly.

Solving (H-entropy) for the smallest admissible slack gives
`σ_min ≈ (1+ε)·H(ρ)·n / log₂ q`. At the official rows `q ≡ 1 mod n`, so
`log₂ q ≥ log₂ n`, hence `σ_min ≤ (1+ε)·H(ρ)·n/log₂ n = O(n/log n)` — the
**same order** as (H-scale), **not** `Ω(n)`. `Ω(n)` would require `log₂ q`
bounded as `n→∞`, which fails since `q ≥ n+1`.

The verifier computes `σ_min` exactly (binary search on the entropy
inequality, `lgamma` binomials) at all four rows for every admissible
`log₂ q ∈ {smallest prime > n, 64, 128, 256}`:

```
                    σ_min/(n/log₂ n)          σ_min/n
row     rho    smallest-q … 2^256      smallest-q … 2^256
2^41    1/2     0.975 … 0.160          0.0238 … 0.0039
2^42    1/4     0.821 … 0.134          0.0195 … 0.0032
2^43    1/8     0.566 … 0.092          0.0132 … 0.0022
2^44    1/16    0.360 … 0.059          0.0082 … 0.0013
```

`σ_min/(n/log₂ n) < 1` at **every** row and every admissible `q`, and
`σ_min/n → 0`. So (H-entropy) does **not** imply (H-scale) at the official
rows — if anything the scale line (with `C=1`) is the weakly binding one.
Algebraically, entropy ⟹ scale iff `C ≲ (1+ε)H(ρ)·(log₂ n)/(log₂ q)`,
which at `ρ=1/16, n=2^44, q=2^256` is `C ≲ 0.058` — a constant-sensitive
condition, not the unconditional "far stronger".

**Why the SUBSUMED verdict nonetheless holds (route: hypothesis
non-consumption).** Clause (P) is proved at `σ = 1` (`ell = σ+1 = 2`; see
`cp_statement.md` §0). Contributors at any `σ ≥ 1` are a *subset* of the
`σ = 1` contributors (`|S| ≥ k+σ`), so the `σ=1` census bounds every
larger reserve — the imgfib chain **does not consume (H-scale) at all**.
Dropping a hypothesis makes the imgfib conclusion strictly stronger than
ass:locator's, so the official-row instances are covered *regardless* of
whether entropy implies scale. **FIXED:** the correct one-liner is "the
scale clause is not consumed by the chain (clause (P) works at σ=1),
hence dropped, not subsumed-by-entropy"; the "forces σ = Ω(n)" sentence
should be struck before promotion (it is false at the rows).

## 4. Clause (P) mathematics — independently reproduced, no defect

The last open branch (Thm 21 / B11 full-petal frontier, `l1_program_frontier`)
is closed for the **top band** by clause (P) = `petal_g1_layer_maps`. This
is the strongest piece of the packet and it checks out end to end.

**Support-rigidity (Lemma B) — NO ISSUE.** Re-derived from the packet
definitions (`cp_statement.md` §0). With `|S| = j + 2m + s_r` (full-petal:
2 points per touched petal), `s_r ≤ b0 ≤ 1`, and floor band `d ≥ 2(t_ch−2)`
i.e. `j ≤ J = k+3−2t_ch`:
`2m ≥ (k+1) − j − s_r ≥ 2t_ch − 2 − s_r ⟹ m ≥ t_ch − 1`, and `m ≤ t_ch`
trivially, so `m ∈ {t_ch−1, t_ch}`; the corner `(j=J, m=t_ch−1)` sits at
`|S|=k+1` (identity `J + 2(t_ch−1) = k+1`) and `m=t_ch−2` forces `|S| ≤ k`
(impossible). An independent enumeration of all floor-band full-petal
supports at `(16,8)` finds **0 rigidity violations** over 491 supports,
`max j = 3 = J`, `m ∈ {3,4}`.

**Emptiness at rates ≤ 1/4 — NO ISSUE.** `J = 2k+3−n < 0` for `ρ < 1/2`;
verified `(16,4): J = −5`, band empty. Independently reproduces (P-i).

**Census / budget — NO ISSUE.** `N_max = 2^{b0}(t_ch+1)·S_J(k−1) ~ n^4/96`
at rate 1/2 (`J = 3` constant). At the binding official row `n = 2^41`:
`log₂ N_max = 157.4150`, `log₂((121/128)n^6) = 245.9189`, margin
`88.5038` bits `= 90.75·n^2`. All reproduced to the last quoted digit.

**Reruns (stdlib, capped) — reproduced:** `cp_verify.py` **62 PASS / 0**,
`cpa_checks.py` **37 PASS / 0**, `dyadic_profile_evaluation/verify.py`
**ALL PASS**, `spi_exceptional_class/notes/verify_writeup.py` **PASS**
(2500 pencils / 1600 tangent fibres), Modal replay **135 PASS / 0**
(`experiments/prize_resolution/modal_verifier_replay.json`, `complete:true`).

## 5. Clause 6 — the open gap: mixed-petal / diffuse-partial-petal amplification

**Attack.** Clause 6 asserts the full `#ImgFib_U(k+σ)` count is theorem-
backed for all words via "the periodic branch … census gate; the aperiodic
top band … clause (P); **mixed/below-top by petal_growth's off-band
induction + the P1-floor band split**". The count decomposes as
periodic + primitive + full-petal (top-band, below-top) + **mixed/partial-
petal**. Trace the last bucket.

1. **Full-petal is closed; mixed-petal is not.** `petal_growth` proves the
   *full-petal* top band (clause (P) atlas). "Off-band" = full-petal
   *below* top defect, closed by the top-coefficient-rank lemmas
   (`l1_full_list_quotient_proof_program.md` Lemma 13 "Full-Petal High Rank
   Below Top Defect", Lemma 15/16 "Cofactor-Budgeted Full-Petal Layers",
   both PROVED). These are **full-petal** results; they do not bound
   mixed/partial-petal codewords.

2. **The petal nodes place mixed-petal explicitly out of scope.** Three
   independent files say so:
   - `petal_growth/proof.md`: "Mixed-petal and below-top are SEPARATE
     obligations … untouched by this promotion";
   - `petal_growth/conditional.md` §Scope: "Top band only. Mixed-petal and
     below-top contributions are separate obligations, untouched by this
     packet";
   - `petal_g1_layer_maps/proof.md` §Scope: "Mixed-petal and below-top are
     petal_growth's separate obligations … explicitly out of scope"
     (mixed-petal floor mass "4x full-petal at the smallest cell — catch
     #176").

3. **The program note itself marks it CONJECTURAL.** Its Development Ledger
   (`l1_full_list_quotient_proof_program.md`, final lines):
   "**Mixed-petal sunflower amplification: CONJECTURAL. Next focused bound
   to prove or refute in the large-defect regime.**" Theorem B11 (PROVED)
   reduces to the residual frontier "d−ell → ∞, or … G_2(P)→∞, G_R(P)→∞"
   — the growing-excess full-petal case (clause (P)) **plus** the diffuse
   partial-petal case, which is the second of the two "genuinely hard
   cases" the note leaves open (the first is closed by clause (P)).

4. **The cited induction is retracted, not proved.** The
   mixed-amplification induction (`petal_excess_induction`,
   `petal_mixed_amplification_step`) was cut in the 2026-07-05 retraction
   after "repeated falsifications-as-stated"
   (`petal_growth/RETRACTION_MANIFEST.md`); its own attack note reports the
   obstruction fired ("if the residue-line count grows with c, that growth
   IS the obstruction"; petal_growth stress evidence: "dim K grows with c …
   induction not revivable"). So "off-band induction" does not cover
   mixed-petal.

5. **`payment_completeness` does not close the count.** Its own honest
   boundary (`payment_completeness/proof.md` §3): the taxonomy is
   exhaustive but "the generic row-full horizontal scroll … is the separate,
   still-open quantitative node `spi_point_counting` (the R2 lane) … a
   counting gap, not a taxonomy gap." Taxonomy exhaustiveness ≠ a
   polynomial count of the mixed/core bucket.

**Smallest witness.** `cpa_checks.py` (which passes 37/0) prints, at the
smallest audited cell `(16,8,97)`:
`A4 (16,8,97) mixed-petal floor-band contributors (outside clause (P)
scope, petal_growth's separate bucket): 43` — versus 10 full-petal floor
classes. Mixed-petal contributors are real, present at an official rate
(1/2), and 4× the full-petal mass at that cell; no PROVED node bounds
their large-defect amplification.

**Verdict — OPEN GAP (route-scoped).** *There is no theorem-backed
polynomial bound on `#ImgFib_U(k+σ)` at the official rows via the imgfib
chain for the mixed-petal / diffuse-partial-petal (large-defect) bucket*:
that bucket is CONJECTURAL in the program note's own ledger and out of
scope in `petal_growth`, `petal_g1_layer_maps`, and the clause-(P) packet.
The chain **does** theorem-back the full-petal top band (clause (P)),
full-petal below-top (Lemmas 13/15/16), the periodic branch (census gate),
and the primitive branch (K4). The crosswalk's top-line "every instance …
is theorem-backed" and clause 6's "mixed/below-top by … off-band
induction" over-state relative to these node scopes; the standing caveat
names only the "#171 wide-minus-floor lift mass" (a below-top *full-petal*
item), not the mixed-petal bucket.

## 6. Minor items

- **Verification-trail citation — FIXED.** The crosswalk cites "Modal
  execution re-pin 124/124" and "harness 124 scripts"; the current DAG
  state is **135/135** (manifest refreshed via `--refresh-manifest`; HEAD
  "Modal execution re-pin … 135/135 PASS"). Stale, not wrong-in-spirit;
  update the count if promoted.
- **Official-row convention — NO ISSUE (note).** `dyadic_profile_evaluation`
  fixes `n = 2^41` and varies `k`; clause (P) fixes `k = 2^40` and varies
  `n = 2^41..2^44`. Both are generated-field 2-power rows at the four
  rates, immaterial to every quantity checked here, but the crosswalk
  should pin one convention for the four rows to avoid ambiguity.

## 7. Promotion decision

**HOLD** on any roadmap language that reads as "the L1 hard input
(ass:locator) is theorem-backed / discharged at all four official rows for
all received words." That statement is not supported: the mixed-petal /
diffuse-partial-petal amplification bucket is CONJECTURAL (§5).

**PROMOTE-WITH-CAVEATS** the narrower, accurate claim the artifacts do
support, namely:

> At the four official prize rows, the **full-petal** locator-image-fiber
> contribution is theorem-backed and independently verified: the growing-
> excess top band by clause (P) (`petal_g1_layer_maps`; empty at rates ≤ 1/4,
> census ~ n^4/96 with an 88.5-bit margin at n = 2^41), the below-top band
> by the full-petal rank/cofactor lemmas (Lemmas 13/15/16), the periodic
> branch by the census gate, and the primitive branch by K4. The full
> `#ImgFib_U` bound additionally requires the mixed-petal amplification
> bound, which is open.

Caveat lines that must sit next to any promoted L1 language (each names its
own conditional dependency inline):

1. **Row-scoped, not asymptotic.** Exponents are row-explicit; no single
   uniform `B_L` across the family `n = 2^m` is claimed (crosswalk clause 2).
2. **P1 floor-band tripwire.** Proved for the layout-anchored floor band
   `d ≥ M(t−2)` (catch #168); a re-resolution of the band constant re-opens
   clause (P) (re-surgery criterion 4 / tripwire (P)-3).
3. **Mixed-petal bucket open (new — required).** The discharge covers the
   full-petal, periodic, and primitive buckets only; the mixed-petal /
   diffuse-partial-petal (large-defect) amplification bound is CONJECTURAL
   (`l1_full_list_quotient_proof_program.md` Development Ledger; Theorem B11
   residual frontier) and is not covered by any wired node.
4. **Clause-4 wording.** State "(H-scale) is not consumed by the chain
   (clause (P) works at σ=1), hence dropped"; drop "forces σ = Ω(n), far
   stronger" (false at the official rows, §3).

## 8. Nonclaims (honest boundary of this audit)

- This audit does **not** refute imgfib. Clause (P), the full-petal
  below-top lemmas, the dyadic profile, the periodic census gate, and the
  spi taxonomy route are sound as far as re-derived/rerun here; the gap is
  a *missing* mixed-petal bound, not a counterexample. No
  COUNTEREXAMPLE_NEW_FLOOR is claimed.
- It does **not** independently re-run the full 124/135-script Modal
  harness; it reruns the stdlib verifiers that decide the load-bearing
  clauses (cp/cpa/dyadic/spi) and reads the replay manifest's recorded
  counts.
- It does **not** evaluate the asymptotic family form of ass:locator, nor
  op:locator (the polynomial-field open problem, snarks_v4.tex lines
  775-777); the crosswalk already disclaims those.
- It does **not** re-audit `conj_f`'s `f_primitive_case` internals beyond
  confirming it is wired PROVED; that node is not on the mixed-petal gap
  path.
- "No mixed-petal bound" is scoped to the **imgfib chain's five wired
  nodes**; a future `petal` amplification lemma (the collaborator's flagged
  next target) would close it and lift caveat 3.

## Credit

The clause-(P) support-rigidity theorem and its word-free layout-anchored
census are a clean, independently reproducible result; the emptiness law at
rates ≤ 1/4 and the 88.5-bit rate-1/2 margin are exactly as stated. The
verifier batteries (`cp_verify.py`, `cpa_checks.py`) are honest — indeed
`cpa_checks.py` is what surfaces the out-of-scope mixed-petal count that
this audit turns into caveat 3.
