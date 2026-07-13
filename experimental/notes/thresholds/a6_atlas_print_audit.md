# The witness-exhaustive atlas (hard input 1): print-audit against the A6 chart-payment wave

## Status

`PRINT-AUDIT (AUDIT) of hard input 1 (agents.md L46, "witness-exhaustive
first-match atlas") in experimental/asymptotic_rs_mca_frontiers.tex against
the newly integrated A6 chart-payment wave (PRs #659, #671, #676, #681
(three packets), #687, #697) / EVERY tex anchor verbatim-checked at ea4eb07
(tex byte-identical to 36de5bf, only commit 4e3c4ee ever touched it) /
RESULT: NO PRINT CHANGE FORCED -- 42 atlas-specific tex anchors across 9
routes verified current, 0 forced edits / the wave pays a field-independent,
selector-independent poly(r) distinct-slope bound for ONE named completed-
witness chart on ONE fixed received line and ONE active weighted-RS chart; it
is not a consumer of condition (A2) / def:first-match / lem:first-match-bound,
whose "uniformly in every received line" quantifier is untouched and remains
the sharpest honest form.`

This note performs the hard-input-1 analogue of the image-face print-audit
`#684` (`image_face_print_audit.md`) and the lower-reserve coverage audit
`#693` (`lower_reserve_unsafe_side_coverage_audit.md`, see its S5 for the
print-determination pattern followed here). Hard input 1 is structurally
different from both: its objects -- the **first-match atlas**, the **cell
catalogue** `C1`-`C9`, condition **(A2)** -- are the paper's own foundational
vocabulary, printed in over thirty locations from the abstract to the
finite-row interface. The central fact this audit turns on, established
pre-A6 by **holmbuar's #536** (`atlas_missing_witness.md`): **witness
exhaustiveness (mere covering) is nearly free; the hard content of (A2) is a
*paid* exhaustive atlas** -- every cell separately bounded, `e^{o(n)}` total
profiles, uniformly over every received line. The newly integrated A6 wave
is a genuine, unconditional advance in *payment* for one named chart, but --
by its own unanimous, sevenfold self-assessment -- it is not a payment
toward (A2)'s coverage-uniformity obligation, so **no printed atlas
statement is forced to change.**

**Credit.** The audited wave is **DannyExperiments'** `#659`
(`a6_full_support_zero_boundary.md`: full-support/zero-boundary payment),
`#671` (`completed_cramer_strict_strata.md`: completed-Cramer subexponential
strata), `#676` (`completed_zero_mask_two_block.md`: `Xi_e>=0` two-block
payment), `#687` (`a6_higher_order_completed_mask_rank_envelope.md`:
higher-order mask-rank exclusion), and `#697`
(`a6_all_witness_line_section_compiler.md`: the selector-free all-witness
line-section compiler, the wave's headline). **holmbuar's** `#681`
(`a6_actual_witness_core_rank_preflight.md`,
`a6_u2_five_slope_rank_preflight.md`, `a6_u2_source_rooted_conic_preflight.md`
-- three hypothesis-audited preflight packets) supplies the actual-core-rank
and `U(2,L)`/conic route cuts consumed by `#687`/`#697`. All six PR
numbers (`#659,#671,#676,#681,#687,#697`, spanning the seven consumed note
files) were confirmed against the upstream tracker (`gh api
repos/przchojecki/rs-mca/pulls/<n>`), matching each note's own internal
cross-references to its predecessors. The pre-A6 baseline is **holmbuar's**
`#536` (`atlas_missing_witness.md`), which named the printed cell catalogue
`C1`-`C9` (`sec:cell-catalogue`, L2366-2496) and proved that the *only*
unconditional exhaustiveness discharge in the paper is the trivial one-cell
atlas `thm:small-effective-dual-closure` (SE1/SE2, L3026-3060), paying only
at identity scale; `atlas_exhaustiveness_hunt.md` and
`exhaustiveness_proof.md` are cited by filename as earlier, narrower rung
scans on the same object. No `.tex`/`.pdf` is touched by this audit.

---

## Summary table

| classification | count | routes |
|----------------|-------|--------|
| SUPERSEDED-NEEDS-PRINT | **0** | -- |
| TIGHTENED | **0** | -- |
| CONTRADICTED | **0** | -- |
| STILL-OPEN (verified current, sharpest form) | 5 | U1, ATL, LNU, NEG, NCH |
| CURRENT-PROVED (arc does not bear) | 2 | POA, CNS |
| PARTIAL (named-chart payment; hypothesis undischarged) | 1 | FIN |
| AUDIT/DEFINITIONAL (verified current, not itself a claim) | 1 | DEF |
| **hard-input-1 tex statements audited** | **9 routes / 42 anchors** | -- |

**PRINT-LIST: EMPTY.** No forced edit.

---

## 1. The printed obligation, by route

Every quote below is byte-verified at its cited line (tolerance-window
search, `+/-2` lines) by
`experimental/scripts/verify_a6_atlas_print_audit.py`.

### Route U1 -- umbrella phrasing (abstract, recap, checklist, robustness)

- **Abstract, L160-161:** *"requires a witness-exhaustive atlas, image-scale
  MI and MA or a direct / Sidon payment, residual ray bounds, and comparison
  of the complete profile [envelope with the target and lower reserve]."*
- **Theorem-recap, L778-779:** *"still requires a witness-exhaustive
  first-match atlas, image-scale / effective Fourier payment or a direct
  Sidon payment, residual ray bounds [for the remaining higher-dimensional
  balanced cores]."*
- **Verification template, L7214-7215:** *"this requires an exhaustive /
  subexponential atlas with direct slope budgets, effective (MI) and"*
  [(MA)...].
- **prop:standard-admissible, L7105:** *"The atlas payments, (MA), image-scale
  conditions,"* [(RC), and full profile envelope remain separate checks].
- **sec:robustness, L7129:** *"does not close the Sidon, algebraic-projection,
  or higher-dimensional ray"* [branches for every smooth/circle row].

### Route DEF -- the defining vocabulary (audited, not itself a claim)

- **First naming, L433:** *"[An ordered] \emph{first-match atlas} is
  witness-exhaustive if its realized cells cover"* [every witness].
- **Glossary restatement, L1238:** *"ordered atlas is witness-exhaustive and
  uses actual first-match slope"* [projections].
- **def:first-match, L1463 (the formal definition):** *"The ordered family is
  a \emph{witness-exhaustive first-match atlas} if"* `W_a(r) = union_i C_i`.
- **def:paid-cell, L2307:** *"Fix a witness-exhaustive ordered atlas.  A
  scaled realized cell C_i"* [is paid at its profile scale when ...].
- **Cell catalogue framing, L2368-2369:** *"The catalogue below is a language
  for row-specific proofs, not a theorem / that every displayed locus is
  automatically paid."*
- **Balanced-core/split-pencil naming, L2458:** *"[A common core is a locator
  factor shared by every member of a] family.  A \emph{balanced core} is a
  pair of equal-degree monic residual"* [locators with a common depth-w
  prefix].

- **thm:small-effective-dual-closure (SE1/SE2), L3053, L3055 -- the paper's
  own trivial atlas:** *"[... all hold with subexponential loss.] Taking the
  [support-restricted incidence over Omega as one ordered cell is]
  exhaustive for that restricted incidence; it is exhaustive for the whole"*
  [exact-agreement incidence when `Omega=binom(D,a)`, or after an exhaustive
  partition into such slices].

**Reading.** `def:first-match`'s ONLY requirement for "witness-exhaustive" is
the covering equality `W_a(r) = union_i C_i` -- nothing about payment. This is
precisely `#536`'s finding: covering is nearly free (any total partition,
e.g. `thm:small-effective-dual-closure`'s one giant cell taking `Omega=
binom(D,a)`, or the depth-`w` prefix-fibre partition, is trivially
exhaustive, and SE1/SE2 pay it -- but only at identity scale
`|Z|<=M=binom(D,a)`, i.e. no gain over the trivial bound). The catalogue
framing (L2368-2369) says so explicitly: it is "a language for row-specific
proofs," not a completeness theorem. So DEF is audited as **verified
current, definitional** -- not itself open or closed.

### Route ATL -- condition (A2), the formal hard input

- **def:admissible-sequence preamble, L897-899:** *"A sequence (C_n,a_n) ...
  is ledger-admissible if the following conditions hold uniformly in every
  received line."*
- **(A2) itself, L905, L907:** *"A first-match atlas covers every bad-slope
  witness and has [e^{o(n)} profiles.] ... [The total distinct-slope
  contribution] of its algebraic cells is at most e^{o(n)} E_n(a_n)."*
- **def:closed-asymptotic-ledger (L1), L1103-1104:** *"[its exact-agreement
  witness incidence ...] has a witness-exhaustive / first-match atlas in the
  sense of def:first-match, with"* [e^{o(n)} realized profiles].
- **Finite-row cross-reference, L6514:** *"and is required by (A2) or
  (RC)."*

**This is hard input 1's precise printed form:** exhaustive covering **+**
`e^{o(n)}` total profiles **+** per-cell payment summing to `e^{o(n)}
E_n(a_n)`, **uniformly in every received line** (the def:admissible-sequence
preamble). STILL-OPEN in general.

### Route LNU -- the "every received line" / row-sequence quantifier

- **lem:first-match-bound, L1527:** *"If every received line admits a
  witness-exhaustive first-match atlas and a"* [certified upper ledger with
  sum U_i <= U, then B_C^MCA(a) <= U].
- **def:asymptotic-row, L2256:** *"and, for every received line, a
  witness-exhaustive first-match atlas of"* [realized profiles with their
  fields, full slices, boundary maps, and actual slope projections
  recorded].

**This is the row-sequence quantifier a general solution must clear.** It is
untouched by any fixed-parameter instance.

### Route POA -- thm:canonical-partial-occupancy-atlas (proved, orthogonal)

- **L3749:** *"[order these cells] arbitrarily.  Then they form a
  witness-exhaustive first-match atlas and,"* [with `Z_lambda^o` its
  first-match slope projections, ...].

**CURRENT-PROVED, in-paper, unconditional** -- for the partial-occupancy
support cells (`Omega_{t,m,p,r}` slices), one received line. A genuinely
closed sub-atlas for **one structural cell type**, disjoint from the A6
completed-witness two-block chart (a different cell type; see Route FIN).

### Route NEG / NCH -- explicit negative statements

- **thm:aperiodic-package, L7160, L7163-7164:** *"If an exhaustive atlas has
  separately identified all quotient, planted,"* [tangent, extension,
  rank-defect, saturation, and pencil loci, its fully primitive residual has
  the negated properties by definition.] *"Smoothness alone does not prove /
  that these loci form such an exhaustive subexponential atlas."*
- **sec:no-closed-hypothesis, L7543-7544:** *"[does not] prove the
  enumerative statements that drive the upper bound: exhaustion of / the
  corresponding boundary-map and algebraic slope projections,"* [the
  primitive effective minor/major aggregates, and the higher-dimensional
  transverse-secant bound].

**STILL-OPEN, verified current.** These are the manuscript's own explicit
admissions that atlas exhaustiveness-with-payment does not follow from
smooth/circle geometry alone.

### Route CNS -- conditional consumers (proved implications, hypothesis undischarged)

- **prop:first-match-atlas-finite, L6517:** *"Suppose a smooth or circle
  sequence admits a witness-exhaustive"* [atlas ... Then the atlas has
  e^{o(n)} profiles and satisfies the census part of (A2)].
- **prop:first-match-sum-detail, L6695:** *"Suppose a witness-exhaustive
  ordered ledger has e^{o(n)} profiles and their"* [distinct-slope budgets
  sum to e^{o(n)} E_n(a) ...].
- **prop:cell-budget-theorem, L7417:** *"Suppose an exhaustive atlas has
  e^{o(n)} profiles and each profile"* [satisfies a direct distinct-slope
  estimate ...].
- **prop:smooth-domain-algebraic-closure, L7463:** *"If a multiplicative
  smooth row verifies the exhaustive atlas, invariant"* [quotient-descent/lift
  counts, planted and determinantal projection criteria, ...].
- **cor:smooth-domain-full-ledger, L7487:** *"A multiplicative smooth row
  satisfying the algebraic hypotheses above,"* [effective (MI) plus (MA) or a
  direct Sidon payment, the primitive-Q conditions, and (RC) has a closed
  asymptotic ledger].
- **prop:circle-domain-full-ledger, L7525:** *"A circle twin-coset row with a
  proved exhaustive subexponential atlas and"* [complete profile envelope,
  satisfying the circle analogues ...].

**CURRENT-PROVED as implications; arc does not bear.** Each is a genuine
proved theorem of the form "IF an exhaustive/paid atlas exists, THEN ...".
None discharges the hypothesis; the A6 wave does not either.

### Route FIN -- the finite-row interface (where the A6 wave actually lands)

- **sec:finite-interface, L6711:** *"[A finite row supplies a number B*, the
  desired bad-slope ceiling. A] certificate consists of a witness-exhaustive
  ordered atlas"* [C_i, exact supersets E_i >= Z_i^o of its actual first-match
  projections, and integer budgets |E_i| <= U_i with sum U_i <= B*].
- **prop:finite-specialization-principle, L6723:** *"Let a finite smooth or
  circle row admit a witness-exhaustive first-match atlas,"* [exact
  distinct-slope budgets for its algebraic profiles, an exact Sidon moment
  estimate yielding Q, and an exact (RC) or direct ray bound].
- **thm:exact-finite-profile-compiler, L6739:** *"[Fix a finite row, an
  agreement a, and a received line. Let an ordered] witness-exhaustive
  first-match atlas have algebraic or direct cells with"* [exact integer
  budgets D_i, and primitive cells indexed by lambda].

**CURRENT-PROVED as scaffold; PARTIAL as instantiation.** This is the exact
object type the A6 wave's headline result produces a candidate for: a
per-cell integer budget `U_i` (or `E_i`) for ONE chart, on one fixed row. See
Section 3.

---

## 2. What the A6 wave actually pays (per note, with route)

| PR | note | author | pays | route touched | own atlas disclaimer (verbatim) |
|----|------|--------|------|----------------|----------------------------------|
| #659 | `a6_full_support_zero_boundary.md` | DannyExperiments | full-support + `J_e=0`-stratum payment for one completed-witness chart | FIN (candidate cell payment) | "No A2 witness-exhaustive atlas, A4 image-normalized payment, A7 envelope comparison ... is proved." |
| #671 | `completed_cramer_strict_strata.md` | DannyExperiments | completed-Cramer count for strict `W1-`/`W2-` strata, all `e=o(n/log n)` | FIN (candidate cell payment) | does not name A2 explicitly, but: "the displayed count can be exponential. Terminal-mask rigidity and Cramer reconstruction alone therefore do not close the strict interior." (admits non-uniform scope) |
| #676 | `completed_zero_mask_two_block.md` | DannyExperiments | `Xi_e>=0` two-block zero-mask payment | FIN (candidate cell payment) | "a witness-exhaustive A2 atlas or a bound on the number of profiles" [is not proved] |
| #681 | `a6_actual_witness_core_rank_preflight.md` | holmbuar | actual selected-witness core-rank charge, set-pair/determinant route cut | FIN (localizes what FIN still needs) | "A2 atlas or selector exhaustiveness and the number of profiles" [is still open and not claimed] |
| #681 | `a6_u2_five_slope_rank_preflight.md` | holmbuar | `U(2,L)` five-slope rank packet, value-sensitive route test | FIN | "no primitive-rank theorem, atlas exhaustion, A2, RC, full A6, A7, deployed-row result, prize closure, or TeX change" |
| #681 | `a6_u2_source_rooted_conic_preflight.md` | holmbuar | conic/simple-pole vs collision-determinant branch separation | FIN | "no primitive atlas, quotient classification, planted-profile census, ray-occupancy theorem, full A6/A7 theorem, deployed-row result, or prize closure" |
| #687 | `a6_higher_order_completed_mask_rank_envelope.md` | DannyExperiments | forced-overlap (HCM) theorem, high-rank exclusion | FIN | "no full A6 theorem, witness-exhaustive atlas, image-scale MI/MA or Sidon payment, profile-envelope target comparison, deployed adjacent [result]" |
| #697 | `a6_all_witness_line_section_compiler.md` | DannyExperiments | selector-free \|Z\| <= 1960+3744(1400r+5)^6 on ONE fixed line/chart, all retained slopes | FIN (headline payment) | "a witness-exhaustive atlas or a bound across different received lines, active charts, or realized profiles" |

**Unanimity.** All seven notes -- six different PRs, two different
authors -- independently disclaim the atlas in their own Nonclaims/scope
section. This is a strong, self-consistent signal, not an audit inference.

---

## 3. The central quantifier gap: #697 vs the general atlas

`#697` is the wave's cleanest statement and the best case for a possible
atlas payment, so it is the one worked through in full.

**What #697 proves.** Fix `r>=1` and the canonical source parameters
`N=500r, kappa=225r, t=150r, d=250r`. Over **any** field containing the `N`
evaluation points, fix **one** received line and **one** active weighted-RS
chart. Let `Z` be the set of slopes retaining at least one actual completed
witness of weight `<=t`. Then
```
|Z| <= 1960 + 3744(1400r+5)^6                                    (1)
```
-- field-independent, selector-independent, first-match-order-independent.
`|Z| = poly(r) = exp(o(N))`. This is a genuine unconditional theorem
(conditional only on citing Kaltofen's characteristic-free Noether-form
degree bound), and it pays the entire fixed-line canonical stress instance,
including the previously open central band `50r < e < 100r` (per the note's
own "why this moves the board" section, and the audit-correction record
fixing an earlier worker's unsupported quartic bound to the sixth-power
Noether degree).

**What route FIN (`sec:finite-interface`, L6710-6720) demands of a finite
certificate:** *"a witness-exhaustive ordered atlas C_i, exact supersets E_i
>= Z_i^o ... and integer budgets |E_i| <= U_i with sum_i U_i <= B*."* #697's
bound (1) is exactly a candidate `U_i` for ONE such `C_i`.

**What route ATL/LNU demand for the asymptotic hard input:** the SAME
inequality (1) supplied for **every** cell of a full first-match atlas,
**uniformly in every received line**, for a genuine ledger-admissible row
sequence `(C_n,a_n)` (not one scaled family), with the total profile count
staying `e^{o(n)}`.

The gap has three independent axes, each alone sufficient to block
discharge:

1. **One line vs. every line.** (1) is proved for one fixed received pair;
   nothing shows it uniform as the line varies, let alone across `n ->
   infinity` (Route LNU, L1527/L2256).
2. **One chart vs. the full catalogue.** (1) pays one named completed-witness
   two-block chart. The tex's own cell catalogue (`sec:cell-catalogue`,
   L2366-2496, per `#536`'s extraction: quotient/periodic `C1`, dihedral
   `C2`, planted-block `C3`, tangent/deep `C4`, extension `C5`,
   differential-locator `C6`, saturation `C7`, balanced-core/split-pencil
   `C8`, Fourier/Sidon `C9`) names eight *other* structural types that a
   general row's witnesses can realize; none is closed by (1). The A6
   two-block object is itself only a **candidate** instance of `C8`
   (balanced core: "a pair of equal-degree monic residual locators with a
   common depth-w prefix," L2458-2459) -- and `#681`'s own preflight packet
   is explicit that its companion rank invariant `r` "is not automatically
   ... a C8 certificate" (`a6_actual_witness_core_rank_preflight.md` L954),
   i.e. the corpus itself declines to claim the C8 identification is
   established, only that it is the natural target.
3. **One scaled canonical family vs. a general row.** `N,kappa,t,d` are
   locked to one stress ratio (`kappa=0.45N, t=0.3N, d=0.5N`) scaled by `r`,
   not an arbitrary structured row with `k_n/n -> rho`.

This is why the wave's own Nonclaims (Section 2 above) all converge on the
same sentence in different words: a payment for one chart on one line is not
"a bound across different received lines, active charts, or realized
profiles" (#697's own phrase).

**A note on hard-input numbering.** `#697`'s own Lane line self-labels
*"asymptotic A6 / hard input 3"* (the residual ray compiler), and the
sibling notes' Track lines say *"asymptotic hard input C / condition A6."*
Condition **(A6)** in `def:admissible-sequence` (L942-945) is *"Every
residual shift-pair and balanced-core chart satisfies the ray compiler (RC)
... or has a direct distinct-slope bound"* -- i.e. hard input 3, not hard
input 1 (which is condition (A2)). This audit's finding is not that the
A6 wave *mis*-labels itself: (1) is a **direct distinct-slope bound**, and
`def:paid-cell` (L2306-2313) and condition (A6) (RC) cash out in the *same*
currency (a distinct-slope bound at profile scale), so the identical
theorem is simultaneously a candidate (A6)/ray-compiler payment and a
candidate (A2)/atlas cell-payment for whichever chart it is assigned to.
The wave's own Nonclaims correctly track this: they disclaim (A2) and (RC)
side by side (e.g. `a6_u2_five_slope_rank_preflight.md`: *"atlas exhaustion,
A2, RC"*). Hard input 1 and hard input 3 are logically distinct printed
obligations that happen to share a payment currency; #697 contributes to
neither's *general* discharge, only to the shared currency's balance for
one named chart.

---

## 4. Residual handles

Following the `#693` convention (`O5c`/`O7`), the remaining atlas gap
decomposes into two coupled, independently named residuals:

- **(CAT) -- the catalogue-completion residual.** A first-match atlas for a
  general ledger-admissible row whose cells jointly cover the *entire*
  catalogue realizable by the row's witnesses (`C1`-`C9` plus, if `#697`'s
  chart is confirmed a genuinely new type, a `C8`-adjacent completed-witness
  entry), with **every** cell separately paid and the **total** profile
  count `e^{o(n)}`. This is condition (A2) stated in full; it is what
  `thm:aperiodic-package` (Route NEG) says smoothness alone does not supply.
- **(UNIF) -- the line-uniformity residual.** The same paid catalogue, but
  holding **uniformly in every received line** of a genuine asymptotic row
  sequence `(C_n,a_n)` as `n -> infinity` (Route LNU), not one scaled fixed
  family `N=500r,...`.

**(CAT) and (UNIF) are coupled the same way `#693`'s `O5c`/`O7` are: a
construction that supplies one without the other is not a discharge.** A
`C8`-style payment proved only for the canonical two-block family (as `#697`
does) advances (CAT) for one candidate cell without touching (UNIF); a
uniformity argument that ignored the `C1`-`C9` split would leave (CAT) open.
Closing hard input 1 needs both at once, exactly as printed.

---

## 5. Print determination

**The printed umbrella phrasing is the sharpest honest form; no printed
statement is forced to change.**

- Routes U1, ATL, LNU, NEG, NCH state the atlas requirement as open, and
  the A6 wave -- by its own sevenfold, unanimous Nonclaims -- does not close
  it. Narrowing any of these to "closed for the canonical A6 two-block
  family" would misstate a broad printed hypothesis as discharged by a
  fixed-parameter instance, the same overclaim-in-disguise error the `#684`
  audit identified and declined to make for the image-scale input.
- Route POA (`thm:canonical-partial-occupancy-atlas`) and Route CNS (the six
  conditional consumers) are verified current and untouched by the wave --
  different cell type (POA) or unexercised hypothesis (CNS).
- Route DEF is verified current; the wave does not redefine
  witness-exhaustiveness or the catalogue.
- Route FIN is the one place the wave's headline result (#697) is
  structurally the *right kind* of object (a per-cell integer budget for a
  finite-row certificate). It is not yet a discharge: no note claims
  uniformity over lines, charts, or the rest of the catalogue, and none
  proposes a TeX edit. The scaffold (L6710-6720) remains correctly
  conditional.

No row is SUPERSEDED-NEEDS-PRINT, TIGHTENED, or CONTRADICTED.

**Optional, non-forced adjacency (maintainer's discretion only; not
counted in the print-list).** A single sentence could be added after
`sec:cell-catalogue`'s balanced-core paragraph (L2456-2466) noting that a
selector-free, field-independent poly(r) distinct-slope bound is now
available for the canonical A6 two-block stress family on one line/chart
(citing `#697`), pending confirmation that the family is a `C8` instance and
extension across lines/charts/profiles. This would be new exposition
crediting the wave, not a correction of any stale or overclaiming
statement, and nothing printed is wrong without it.

---

## 6. Per-claim verdict ledger

| # | claim | verdict | basis |
|---|-------|---------|-------|
| A | 42 hard-input-1 tex anchors byte-current at `ea4eb07` (= `36de5bf`), tolerance-window verified, negative-tested | **AUDIT** | verifier BLOCK A |
| B | Routes U1, ATL, LNU, NEG, NCH open, sharpest honest form | **STILL-OPEN** | Sections 1, 5 |
| C | Routes POA, CNS proved, wave does not bear | **CURRENT-PROVED** | Section 1 |
| D | Route DEF verified current, not itself a claim | **AUDIT/DEFINITIONAL** | Section 1 |
| E | Route FIN: scaffold proved conditional; #697 supplies a candidate per-cell payment, not a discharge | **PARTIAL** | Sections 1, 3 |
| F | #697's arithmetic (`C=520`, `U(r)=260050r+1022`, surplus `50r+1022>0`, `\|E\|<=364+3744(1400r+5)^6`, `\|Z\\E\|<=1596`, final bound `1960+3744(1400r+5)^6`) recomputed independently | **COMPUTED** | verifier BLOCK B |
| G | All seven A6-wave notes independently disclaim A2/atlas discharge in their own text | **AUDIT** | verifier BLOCK C; Section 2 |
| H | `#697`'s own Lane line and sibling Track lines self-label hard input 3 / condition (A6), not hard input 1 | **AUDIT** | Section 3, verifier BLOCK C |
| I | (CAT) and (UNIF) named as the coupled residuals | **OPEN** (named, not proved) | Section 4 |
| -- | any deployed finite-row, Grand MCA, Grand List, or prize-threshold claim | NOT CLAIMED | this is a hard-input-1 coverage map only |

---

## 7. Replay

```bash
python3 experimental/scripts/verify_a6_atlas_print_audit.py --check
# -> RESULT: PASS (n/n)
python3 experimental/scripts/verify_a6_atlas_print_audit.py --tamper-selftest
# -> confirms a corrupted anchor is detected, then RESULT: PASS (n/n)
```

The verifier (stdlib-only, deterministic) checks: (BLOCK A) every quoted tex
anchor against `asymptotic_rs_mca_frontiers.tex` at its stated line with a
`+/-2`-line tolerance-window search, plus a negative test that a corrupted
anchor is absent both at its line and file-wide; (BLOCK B) `#697`'s
arithmetic recomputed from the raw summation formulas (not copied from the
note's closed forms) at multiple values of `r`, confirming the polynomial
identities exactly with Python's arbitrary-precision integers; (BLOCK C)
that each of the seven A6-wave notes' own text contains its cited atlas
disclaimer and that `#697`'s own text contains its "hard input 3" self-label;
(BLOCK D) the route/classification counts in the Summary table.

## Post-baseline addendum (PR #704; updated at its globalized head)

PR #704 (DannyExperiments, opened after this audit's `ea4eb07` baseline)
extends the #697 compiler along the transverse all-parameter line-section
frontier.  At its ORIGINAL head it stayed on one fixed received line and one
active chart, and its Nonclaims re-disclaimed the atlas.  Its GLOBALIZED head
(three later commits, "globalize the section-positive one-cell atlas") goes
materially further: on the strict section-positive locus `J = a^2 - n(k-1) >
0` the exact-witness incidence collapses to ONE compact algebraic profile
cell with a uniform `|Z_a(r)| < 10000 n^27` bound — catalogue exhaustivity
AND line-uniformity ON THAT LOCUS.  If integrated, this pays the `(CAT)` and
`(UNIF)` residuals restricted to `J > 0`; the residual handles then live on
the complementary locus `J <= 0` (which #704 explicitly does not touch) plus
the summation cells of the catalogue ledger.  The determination above is a
statement about the INTEGRATED corpus at `ea4eb07` and is unchanged; the
residual handles `(CAT)`/`(UNIF)` remain open as stated there, now with the
sharper post-#704 form: open exactly on `J <= 0` once #704 integrates.
