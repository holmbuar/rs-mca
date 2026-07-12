# Post-sweep reconciliation: the image-face bracket and the evening ships

## Status

`AUDIT (reconciliation).  Bookkeeping note in the #673 pattern: after the
whole-board integration at ea4eb07 and the same-evening PR wave #699-#706,
this note records the current unconditional image-face bracket, the exact
supersession map for every printed bracket number in the integrated corpus,
and a four-line attribution-wording normalization in #682's integrated files.
No new mathematics; every claim below cites its proof by PR number or
integrated file.`

## 1. The bracket

The unconditional image-face bracket after this wave is

```text
rho*  in  [0.160847, 0.405465]
```

- **Lower end** `0.160847`: the b=24 stacked-trade champion of **#694**
  (`comb_trade_champion.md`, integrated at `ea4eb07`), which superseded the
  b=18 champion `0.158411` (#655, carried by #673).
- **Upper end** `0.405465 = ln(3/2)`: the canonical-transversal VC compression
  chain (#668, validated and consumed by **#673**,
  `ilo_moment_closed_consumer.md`, integrated at `ea4eb07`).  Unchanged
  by this wave.
- **NEW — the lower end is a family ceiling at k<=5 (#705).**  The
  memory-bounded census of **#705** decides #694's residuals 1 and 3: the
  k=5 flat comb gives `rho_inf = 0.156900 < 0.160847` (two independent
  algorithms), and the non-uniform-weight search returns the b=24 champion
  itself as the unique maximum (AP weights, up to affine).  Within the
  same-block stacked-trade comb family at `k <= 5`, `0.160847` is final;
  movement now requires `k >= 6`, a different gadget, or a different family
  (see #705 Nonclaims for the exact searched window).

## 2. Supersession map (integrated corpus)

| printed statement (integrated file) | status after this wave |
|---|---|
| `[0.158411, 0.405465]` in `ilo_moment_closed_consumer.md` (#673) | lower end superseded by #694 (its note declares the move); upper end current |
| b=19-26 census null in `championship_census_b19_26.md` (#683) | coexists with #694: the null is for #683's searched class; #694's champion lives in the designed stacked-trade class the census did not cover |
| bracket rows of `image_face_print_audit.md` (#684) | point at the current values above; determination unchanged |
| `fenced_resonance_window.md` (#691) Theorem T1 as printed | superseded by **#700** T1' (exact multiplicity `M(a,a';q)`; the printed "only if q <= 1/(2w)" and the `0.84932 sqrt(b)` ceiling reading are refuted); T3 empty-window headline and its `b_0` table survive unchanged |
| `bohr_gap_volume.md` (#663) Prop 5 | hypothesis set unchanged and now carried explicitly by #700/#701 imports |

## 3. The evening wave (weave, one line each)

| PR | face | result |
|---|---|---|
| #699 | hard input 5 | O5c PAID (quotient, Euclidean-remainder, Chebyshev); deep-remainder wall localized; no profile-list reaches O7 |
| #700 | image-face wall | #691 T1 repaired (refuted-as-printed; corrected T1'); headline survives |
| #701 | hard input 2 wall | #696's energy is denominator-blind — no pincer; Theorem 5 two-band habitat shrink |
| #705 | image-face bracket | stacked-trade family ceiling at k<=5 (this note, section 1) |
| #706 | hard input 1 | atlas prints verified current, NO PRINT CHANGE; residuals (CAT)/(UNIF) named |
| #702, #703 | L2 (external) | DannyExperiments: all-arity shell compression; affine rank <= 14 exclusion |
| #704 | hard input 3 (external) | DannyExperiments: transverse all-parameter extension of #697, same one-line/one-chart scope (its Nonclaims); atlas gap unchanged (#706 addendum) |

## 4. Attribution-wording normalization (#682 files)

The integrated `corridor_diameter_map.md` and
`scripts/verify_corridor_diameter_map.py` credited the `F_13` modular
calibration with a stray two-word phrase (not a repository artifact) sitting
between the team name and the date.  This packet normalizes the four
occurrences (two per file) to "Codex team calibration, 2026-07-12".  No
number, statement, or check changes; the credit and the date are unchanged.

## Nonclaims

No new mathematics.  This note does not re-derive any cited result; each row
of sections 1-3 is proved in its cited PR or integrated file.  It does not
claim the bracket lower end is final outside the #705 searched window, and
it does not touch `experimental/asymptotic_rs_mca_frontiers.tex`.

## Files

- Note: `experimental/notes/thresholds/post_sweep_bracket_reconciliation.md` (this).
- Verifier: `experimental/scripts/verify_post_sweep_reconciliation.py`
  (`--check`: recomputes `ln(3/2)`, asserts every ordering in section 1,
  anchor-checks every quoted number against its integrated source file,
  asserts the section-2/3 row counts, and asserts the section-4
  normalization left zero stray occurrences repo-wide with the normalized
  credit dates in place; `--tamper-selftest`, 3 mutations).
