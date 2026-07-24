# Audit: v4 synthesis bibliography and source pins

```yaml
workboard_item: n/a — synthesis-wide citation/source-pin audit (supports external submission prep; advances no K/L/M/T atom)
row: whole v4 catalogue (four Proth rows, F_{17^32}, corridor rows, deployed KoalaBear and Mersenne-31)
object: OTHER (bibliography, cite/bibitem integrity, blob pins, printed integers, status labels)
target_epsilon: n/a (row targets 2^-128 and 2^-100 carried through unchanged)
agreement: n/a (audit spans rows)
B_star: n/a (checked B* values include 274980728111395087 and 16777215)
direct_statement: on the checked scope every \cite resolves to a \bibitem, every printed integer and status label re-derives from its named source or from exact arithmetic, and all 18 pinned paths exist at both 5ecb9ab5 and f6a20fa; 0 integer defects and 0 status-inflation defects; 6 pre-circulation bibliography/label fixes (F1-F5, F7)
architecture: DIRECT (provenance audit; no partition)
partition_digest: n/a (DIRECT)
atom_or_cell: DIRECT
quantifier: exhaustive over the checked scope; the unchecked scope is enumerated explicitly
projection_and_unit: bibliography entries, cite/bibitem keys, blob-pin paths, exact integers, status labels
claimed_bound: 0 integer defects, 0 status-inflation defects on the checked scope; 6 pre-circulation fixes
status: AUDIT
impact: LOCAL_ONLY
falsifier: any checked integer that does not re-derive; any \cite without a \bibitem; any pinned path missing at either commit; any checked status label stronger than its source supports
replay: python3 experimental/scripts/verify_prize_results_v4_citation_audit.py --check   (45/45, < 1 s, stdlib-only; --tamper-selftest injects one defect and exits nonzero). Kernel-checked Lean is not applicable to a bibliography/pin audit; this verifier is the machine-checkable replay.
```

- **Status:** AUDIT / NO ISSUE on checked scope.
- **Date:** 2026-07-24.
- **Author:** Holm Buar.
- **Verifier:** `experimental/scripts/verify_prize_results_v4_citation_audit.py`
  (stdlib-only, < 1 s; `--check` exits 0 at 45/45, `--tamper-selftest` injects one
  defect and correctly exits nonzero).
- **Scope.** Bibliography, citation integrity, printed exact integers and status
  labels, and source pins of `experimental/proximity_prize_results_v4.tex` at
  `f6a20fa`, checked against the cited manuscripts and packets pinned at
  `5ecb9ab538a0a57dcb81018b17f32849049fb998`. Prompted by the maintainer's
  request to audit the v4 bibliography and source pins before external
  circulation. This note edits neither the manuscript nor any source;
  it records six pre-circulation fixes and the verified-clean inventory behind
  them.

## Verdict

**CLEAN ON CHECKED SCOPE: 0 integer defects, 0 status-inflation defects.** Every
exact integer and every status label re-derives from its named source or from
exact arithmetic; every `\cite` resolves; all eighteen pinned repository paths
exist at both the pin commit and the source commit. Six bibliography/label
items (F1-F5, F7) should be fixed before external circulation; none of them
changes a theorem, an exact value, or the truth of a status label. F6 records
seven descriptive citation brackets that are correct as printed.

## Findings

### F1 [SUBMISSION-CRITICAL] `ChoComp26` has no in-repo source and no ePrint number

`ChoComp26` carries load-bearing unconditional statements: the first Mersenne
primitive cell and Delsarte-barrier theorem `thm:m31-companion` (v4:453-475), the
`S+A+E` contract (v4:692-694), and the closing attribution (v4:476):

> "The cubic certificate, exact full Delsarte optimum, critical-core abundance,
> field descent, and owner concentration are in \cite{ChoComp26}." (v4:476)

The bibliography entry (v4:749-752) resolves to nothing checkable:

> "P. Chojecki, RS--MCA v4.4: ..., companion preprint included with the source
> release of the present paper, 2026." (v4:751-752)

It is the only bibliography key carrying **neither** an IACR ePrint report number
**nor** a pinned repository href. A grep at `f6a20fa` for the entry's identifying
integers and phrases (`16760701`, `16838532`, `critical core`, `owner
concentration`, `execution ledger`, and the paraphrase `Cubic closure`) returns
hits **only** inside `proximity_prize_results_v4.tex`, or none at all. There is no
in-repo file backing these theorems.

*Mitigant.* Every reconstructible integer in `thm:m31-companion` re-derives under
exact arithmetic (see the verifier): the Johnson-scheme Delsarte LP optimum
`1031427641435096867222903646984 / 61254010871010657240949 =
16838532.3143506... > 16777215`; the cubic-cell bound `16760701 < 2^24`; and the
owner concentration `ceil(63684220 * C(440837,8) / C(1053558,8)) = 59838`. The
one figure new in v4, "at least `1133314` projective minimum directions"
(v4:472), has no in-repo source and is **not** reconstructed here; it stays in
the unchecked list.

*Fix.* Give `ChoComp26` an IACR ePrint report number, or ship the companion in
the source-release bundle, before the paper circulates externally.

### F2 [DISCLOSURE-COVERAGE] the unpinned-field caveat omits the length-1024 rows

The corridor remark scopes its unpinned-prime disclaimer to the prize-scale rows
only:

> "The prize-scale corridor packet uses a pinned exact budget convention
> corresponding to a line field near $2^{255.9}$; it does not yet pin one literal
> prime in the paper." (v4:293-295)

The source packet flags **both** scales in its Non-claims section:

> "Row C's literal ~2^250 prime is unpinned (qa3 flag C1(b)); prize 2^255.9 is a
> convention." (`corridor-unconditional-safe-edges/README.md`, Non-claims)

The three length-1024 (Row C, `n = 2^10`) rows in `tab:corridor` (v4:283-285)
therefore rest on the same idealized, not-yet-pinned field, but the remark
mentions only the prize-scale (`n = 2^41`) rows. The values themselves are
digit-for-digit correct: the six safe radii `512, 663, 769, 1092724518963,
1415997755216, 1644686143216` match the packet's Haböck column and the
`tab:corridor` column exactly (verifier).

*Fix.* Extend the remark's unpinned-field caveat to the length-1024 rows.

### F3 [LABEL-IMPRECISE] `ChoThresholds26` citation bracket names a non-existent section

Corollary `cor:abf`(iii) points at a titled statement that does not exist:

> "...the explicit integer consequences stated in \cite[Line decoding and
> list-decoding consequences]{ChoThresholds26}." (v4:332)

At `f6a20fa`, `experimental/rs_mca_thresholds.tex` has **zero**
section/subsection/theorem headings containing "line decoding" or "list-decoding"
(0 heading hits). The only occurrence of "list-decoding" is prose (thresholds:
3795); the underlying list-size-consequence content is present but untitled. The
bracket text reproduces a section name from the retired v3 synthesis, not a
statement in `ChoThresholds26`.

*Fix.* Point the bracket at the actual list-consequence statement in
`rs_mca_thresholds.tex`, or drop the descriptive bracket.

### F4 [OBVIOUS-FIX] two orphan bibliography entries: `CS25`, `GG25`

`\bibitem[CS25]{CS25}` (v4:801) and `\bibitem[GG25]{GG25}` (v4:806) are defined
but never `\cite`d anywhere in the body (verifier orphan set `== {CS25, GG25}`).
`GG25`'s subject appears only as prose:

> "This is not the stronger Goyal--Guruswami notion of $(\delta,A,B)$
> line-decodability." (v4:320)

which is not a `\cite`. There is no dangling citation in the other direction:
every `\cite` key in the body resolves to a `\bibitem`.

*Fix.* Cite each entry where its result is used, or remove the two orphan
entries.

### F5 [MINOR] `ChoShort26` title drift against its own source file

The bibliography entry prints:

> "MDS paving bounds for Reed--Solomon MCA, version 9.2, IACR Cryptology ePrint
> Archive, Report 2026/1463, 2026." (v4:729-730)

The source file's own title line reads differently:

> "\title{Shortening Bounds for Reed--Solomon MCA}" (`RS_MCA_Paving_v9.2.tex`:130)

The ePrint number (2026/1463) and version (9.2) are correct; only the
human-readable title drifts. The cited "MDS paving bounds..." matches the
published ePrint and the repository index name, while the file's `\title` still
reads "Shortening Bounds...".

*Fix.* Reconcile the two: update the file's `\title` to the published title, or
match the bibliography to the file's `\title`.

### F7 [LABEL-IMPRECISE] the Acknowledgements misname the attribution mechanism

The Acknowledgements state where contributor credit lives:

> "Contributor-specific results are attributed in theorem headings and
> bibliography entries." (v4:708)

In v4 the theorem headings carry no contributor names at all. Across every
`theorem`, `proposition`, `lemma`, `corollary`, and `conjecture` heading in the
manuscript, the count of occurrences of any acknowledged contributor's name is
zero; the headings are uniformly descriptive, e.g. `[Source-coordinate tangent
atom]` and `[KoalaBear rank-nine moving-root boundary cut]`.

Per-result attribution in v4 lives instead in the 33 `\source{...}` lines, which
do name contributors explicitly:

> "\source{Holm Buar, \cite{BuarKBTangent26}. ...}" (v4:496)
>
> "\source{Danny, \cite{DannyCoordinateSpan26}. ...}" (v4:509)
>
> "\source{Scott Hughes, \cite{HughesKBM126}. ...}" (v4:544)

The sentence is inherited rather than newly wrong. Its v3 ancestor read "The
theorem headings and bibliography identify the source of each collaborative
result" (`proximity_prize_results_v3.tex` at `5ecb9ab5`), and that was accurate
for v3: v3 carried twelve name-bearing headings — `[Buar: source-coordinate
tangent atom]`, `[Danny: pole-tolerant scalar-locator localization]`, `[Hughes:
fixed-$G$ universal embedding]`, and nine more — and zero `\source` lines. The
v3->v4 rewrite inverted the mechanism (12 named headings -> 0; 0 `\source` lines
-> 33) and reworded the sentence, but kept "theorem headings".

The "bibliography entries" half remains correct, including for the two
contributors who appear in no `\source` name position: Latif and Hart are
credited through the packets cited at v4:292 and v4:207, whose `\bibitem`
entries carry their names.

*Fix.* Reword to name the mechanism v4 actually uses, e.g. "Contributor-specific
results are attributed in the per-result source lines and bibliography entries."
No theorem, exact value, or status label is affected.

## F6 [NO ISSUE] descriptive citation brackets that paraphrase source titles

Seven `\cite[...]` brackets restate the cited source's own section/theorem title
rather than quoting it verbatim. The cited result exists in each case, so these
are acceptable as printed and are listed only for completeness:

- v4 `[Quadratic staircase]` -> source title "Exact quadratic staircase".
- v4 `[Exact target compiler]` -> source "self-contained / almost-half-distance
  target compiler".
- v4 `[Four certified smooth rows]` -> `ChoThresholds26` "Certified
  Proximity-Prize rows at all four rates".
- v4 `[Binary additive-domain rows]` -> source "exact binary additive-domain
  examples".
- v4 `[Large scalar-extension exponent]` -> `ChoGF26` "unconditional
  shallow-prefix RS--MCA exponent".
- v4 `[Universal field-size cap]` -> `ChoCap26` "...for the challenge envelope".
- v4 `[Corrected deployed identity-prefix floors]` -> `ChoCap26` "deployed MCA
  frontier floors".

## Verified clean (independently re-derived)

The positive content behind the verdict. All items re-run in the verifier at
`f6a20fa`.

1. **Four Proth rows (`thm:proth`, tab v4:185-188).** Each explicit prime `p` is
   prime under deterministic Miller-Rabin, `n | p-1`, and `B = floor(p/2^128)` is
   exact for all four rows: `(2^41, 389500552609)`, `(2^42, 1210584858040)`,
   `(2^43, 2879806199253)`, `(2^44, 6233898019554)`.
2. **Exact `F_{17^32}` threshold (`thm:f17`).** `floor(17^32/2^128) = 6`, hence the
   printed complete safe set `[0, 6/512)`.
3. **Corridor table vs packet, digit-for-digit.** The six safe integer radii in
   `tab:corridor` equal the Haböck column of the `Corridor26` packet README and
   the hardcoded expected six, all three identical. "The Haböck bound is the
   stronger of the two in all six rows" (v4:271) matches the packet; the packet's
   "delta <= 0.2045 < 1/4" line is the deployed-KoalaBear row, **not** a corridor
   row, so there is no status inflation. `GKL24` is cited as version 3.
4. **Deployed unsafe floors (`thm:deployed-unsafe`).** The four unsafe agreements
   `1116047` / `1116023` (MCA) and `1116046` / `1116022` (list) match
   `tex/cs25_cap_v13_2.tex`; the four radius fractions `981105/2097152`,
   `490553/1048576`, `981129/2097152`, `490565/1048576` reduce consistently from
   `(n - a_0)/n` at `n = 2^21`; the Mersenne-31 target is correctly `2^-100`, not
   `2^-128`.
5. **Universal-cap terminal edges (`tab:threshold-map`).** `383/512`, `447/512`,
   `959/1024` equal `1 - rho - 2^-9` (rho in {1/2,1/4,1/8}) and `1 - rho - 2^-10`
   (rho = 1/16) exactly.
6. **KoalaBear tangent reserve (`thm:kb-tangent`).** With `p_KB = 2^31-2^24+1 =
   2130706433` read back from `Conjectures_and_Barriers_RS_MCA_v4_1.tex`:1072,
   `floor(p_KB^6/2^128) = 274980728111395087` (the deployed `B*`) and the printed
   reserve `274980728111395087 - 981104 = 274980728110413983`.
7. **Pin integrity, 18/18 at both commits.** Every one of the eighteen `blob`
   hrefs pinned at `5ecb9ab5` resolves via `git cat-file -e` at both
   `5ecb9ab5` (pin) and `f6a20fa` (source); no pin broke in the v3->v4 move, and
   the short form `5ecb9ab5` at v4:77 is a correct prefix.
8. **No dangling citations, including the deliberately dropped keys.** Every
   `\cite` resolves; the dropped `RepoLog26` (coordination log, not proof
   authority, v4:77) and the dropped `BuarKBQ26` / `Bua26b` (conditional cut)
   leave no dangling `\cite` — all three keys are fully absent from the body.

## Unchecked (with reasons)

- **`ChoComp26` entirely (F1).** No in-repo source; the reconstructible integers
  re-derive under exact arithmetic, but the underlying theorems and the new-in-v4
  `1133314` figure are not verifiable against any in-repo file.
- **Eleven pull-request-linked citations** (`#1048`, `#1055`, `#1056`, `#1057`,
  `#993`, `#1058`, `#1060`, `#1061`, `#1015`-`#1018`). These resolve to remote
  pull-request URLs, not offline-checkable here; all fall inside the reviewed
  integration waves recorded in the repository coordination log.
- **`thm:active-payments` exact values.** The `b_0` thresholds `70230` / `108962`,
  the certified maxima `274974976450914526`, `274975238687487221`, `16776934`,
  `16776950`, and the paving-basis `J_{B*}` tables are source-bound to `ChoGF26`
  and were not recomputed.
- **`thm:high-ledger` interior.** The coding-ledger identity `N_coding = l + sum
  d_i(r+1)` and items (i)-(iii): the pinned packet exists but was not
  deep-checked.
- **External ePrint theorem numbers.** `ABF26` Thms 5.2 / 5.3 / 4.21, the
  `BCHKS25` two-radius theorem, `GKL24` Thm 3, `Hab25` Thm 2: the ePrints were
  not opened.

## Routes killed

None. This is an audit packet; it claims and kills no proof route, and it moves
no ledger term.

## Replay

```bash
python3 experimental/scripts/verify_prize_results_v4_citation_audit.py            # verbose, 45/45
python3 experimental/scripts/verify_prize_results_v4_citation_audit.py --check    # exit 0, gate mode
python3 experimental/scripts/verify_prize_results_v4_citation_audit.py --tamper-selftest  # must exit nonzero
```

Source commit `f6a20fa39f8b3ebbf98056726c69133c82309e51`; pin commit
`5ecb9ab538a0a57dcb81018b17f32849049fb998`. Kernel-checked Lean is not applicable
to a bibliography/pin audit; the verifier above is the machine-checkable replay.

**Audit verdict: NO ISSUE (checked scope).** Six pre-circulation
bibliography/label fixes are recorded (F1-F5, F7); the strongest, F1, gates
external circulation of the `ChoComp26` companion. Credit to Latif for the `Corridor26`
packet cross-checked in F2/clean-item 3 and to Hart for the `F17Audit26` note
pinned in clean-item 7.
