# REPAIR: the resonance-denominator window — T1 refuted as printed, corrected, and the empty-window headline re-derived

## Status

`T1-AS-PRINTED REFUTED: the "resolves q only if q <= Q_res = 1/(2w)" NECESSITY and
its constant 0.84932 sqrt(b) read as a *resolution ceiling* are FALSE -- a width-w
trap resolves denominators ABOVE 1/(2w) (explicit witness q=7, w=0.10 => a SINGLE
residue class, though 1/(2w)=5); verifier BLOCK 2's headline lines "a width-w trap
NEVER resolves q>..." assert the false form.  ALSO: T1 dropped a hypothesis -- its
proof uses {theta_2 r^2 + theta_1 r + theta_0} in (1/q)Z + theta_0, which needs BOTH
theta_2 = a/q AND theta_1 = a'/q with COMMON q (#663 Prop 5), a clause #691 omitted
everywhere T1 is stated or used / CORRECTED T1'-T3' PROVED: under the common-q
hypothesis a width-w trap confines the trapped residues to <= (2 floor(wq)+1) *
M(a,a';q) classes mod q (M = max quadratic-congruence multiplicity; = 2^omega(q) for
odd squarefree q, #663 Prop 5); a single class SYSTEM is GUARANTEED when w < 1/(2q)
(sufficient, NOT necessary); the horn (O(1) classes feeding #657 Thm 2/3) forces the
target count 2 floor(wq)+1 = O(1), i.e. q = O(1/w), POLYNOMIAL in b since
w >= sqrt(ln2/(2b)) / T3 EMPTY-WINDOW HEADLINE SURVIVES: exponential q_cross =
2^{beta b} vs polynomial horn ceiling O(sqrt b); interval empty for b > b_0(beta);
the b_0 table (411/53/19/2 at beta=.01/.05/.10/>=.193) is UNCHANGED -- the numeric
constant 0.84932=1/sqrt(2 ln2) SURVIVES, its ROLE reinterpreted from necessary
ceiling (refuted) to sufficient guaranteed-single-class threshold; emptiness is
robust to any polynomial relaxation of the ceiling / T2 (host-smallness threshold),
the "Bohr face = box face" corollary (beta=0 == #682 residual line, a T2-side fact),
and R4/P4 (decoupling) SURVIVE UNTOUCHED.  This is a REPAIR note; it does NOT edit
the integrated fenced_resonance_window.md (#691) or its verifier.`

Every number below is recomputed and **asserted** (not printed) by
`experimental/scripts/verify_fenced_resonance_window_repair.py`
(`python3` stdlib only, deterministic, `--check` and `--tamper-selftest`;
`RESULT: PASS`). The refutation witness `q=7, w=0.10` is carried as an explicit
**negative control against the old form** on the assertion grid.

**Credit.** The `q=7` counterexample to the printed T1 and the dropped
common-denominator hypothesis were found by a **Codex team read-only audit**. The
underlying results are **our #661** (`exp_ilo_fourier.md`: Theorem B quadratic-Bohr
trapping at width `w = sqrt(kappa/eps)`, `kappa = (ln2/2)(eta+1/b)`), **our #663**
(`bohr_gap_volume.md`: R3 / **Proposition 5**, the rational-resonance horn and its
full four-part hypothesis), **our #657** (`ilo_moment_structured.md`: Theorem 2/3,
the rank-1 GAP consumer the horn feeds), and the fencing packets **#682/#685**
carried by #691. External inputs (three-distance / quadratic congruences; #657's box
bound) are cited within their printed hypotheses and never re-derived.

Label key: **REFUTED** (a printed claim shown false, witness exhibited), **PROVED**
(complete re-derivation within quoted hypotheses), **SURVIVES** (a #691 claim
re-checked intact), **COMPUTED** (exact enumeration), **OPEN**.

---

## 1 — What is refuted, and why (REFUTED, verifier BLOCK A/C)

The integrated note `fenced_resonance_window.md` (#691) states, as its Theorem 1:

> *(T1, as printed)* "Let `V` be trapped ... in `Q(theta; w)` with `theta_2 = a/q`
> rational. The trap **resolves** `q` ... **only if** `q <= Q_res := 1/(2w)`." ...
> "`Q_res = 1/(2w) <= 0.84932 sqrt(b)`."

and its proof carries the step

> "if `w >= 1/(2q)` the trap straddles adjacent residues and **no `mod q` structure
> is forced**."

Two independent defects.

### 1a. The "only if" is FALSE; confinement degrades gradually (BLOCK A)

Write `theta_2 = a/q`, `theta_1 = a'/q` (common `q`), `s(v) := (a v^2 + a' v) mod q
in Z/q`; then `theta_2 v^2 + theta_1 v ≡ s(v)/q (mod 1)`, so `v` is trapped iff
`s(v)` lands in the arc `W(theta_0) = { s in Z/q : ||s/q + theta_0|| <= w }`. The arc
has length `2w` on the `(1/q)`-lattice, hence
```
    |W(theta_0)|  =  2 floor(wq) + 1   (theta_0 lattice-centered)   <=  2wq + 1 .
```
The number of admissible target residues **grows continuously like `~2wq+1`**; it
does **not** drop to zero at `w = 1/(2q)`. The claimed vanishing ("no `mod q`
structure is forced" for `w >= 1/(2q)`) is the error. The trap's *own* verifier,
BLOCK 2, computes the transition and exhibits the counterexample:
```
    theta_1 = 0,  w = 0.10  (so 1/(2w) = 5) :
       q =   7 :  # trapped residues = 1     <-- SINGLE-CLASS RESOLUTION, yet q = 7 > 5
       q =  20 :  # trapped residues = 6     (~ 2wq+1 = 5)
       q = 100 :  # trapped residues = 26    (~ 2wq+1 = 21)
       q = 600 :  # trapped residues = 146   (~ 2wq+1 = 121)
```
The `q = 7` row is a **resolution above the printed ceiling** `Q_res = 5`: the trap
confines every trapped `v` to the single class `v ≡ 0 (mod 7)`. So T1's "only if"
(equivalently the print "a width-`w` trap **NEVER** resolves `q > 1/(2w)`") is
**refuted**. The verifier passes only because BLOCK 2 tests each row against a
*count* bound (`cnt >= 0.5·2wq` in the equidistributed branch) and **never
cross-asserts the transition rows against the ceiling** — so the false headline is
never exercised.

*Why `q = 7` slips through.* Single-target resolution with `theta_0` lattice-centered
holds whenever `wq < 1` (i.e. `w < 1/q`), which is **weaker** than the
`theta_0`-uniform guarantee `w < 1/(2q)`. Here `1/(2q) = 0.0714 < 0.10 < 0.1428 =
1/q`: outside the guaranteed regime, but a favorable `theta_0 = 0` still yields one
class. These accidental single-class resolutions populate the whole strip
`1/(2q) <= w < 1/q` and beyond, which is exactly what "only if" forbids.

### 1b. Dropped hypothesis: T1 needs `theta_1 = a'/q` too (BLOCK C)

The proof's key line — "the values `{theta_2 r^2 + theta_1 r + theta_0}` lie in
`(1/q)Z + theta_0`" — is true **only if `theta_1` is also a rational with
denominator `q`**: `theta_2 r^2 + theta_1 r = (a r^2 + a' r)/q in (1/q)Z` needs
`theta_1 = a'/q`. #691's T1 hypothesizes only "`theta_2 = a/q` rational" and uses the
`(1/q)Z` step regardless. This is precisely the hypothesis of **#663 Proposition 5**
(`bohr_gap_volume.md` R3): `theta_2 = a/q`, `theta_1 = a'/q` with **common** `q`,
`q = O(1)`, `w < 1/(2q)`. #691 dropped the `theta_1 = a'/q` clause (and the `q=O(1)`
bound) everywhere T1 is stated or used.

The dropped clause is **not cosmetic** — it is the whole content of #663's R2.4
mod-1 elimination obstruction and its golden counterexample. The verifier exhibits
it directly at `theta_2 = 1/7`:
```
    theta_1 = 0/7      (common q) :  admissible residues mod 7 = {0}                (1 class)
    theta_1 = 3/7      (common q) :  admissible residues mod 7 = {0,4}              (2 classes)
    theta_1 = golden   (NOT a'/q) :  admissible residues mod 7 = {0,1,2,3,4,5,6}    (ALL 7 -- no structure)
```
With `theta_1` off the `(1/q)`-lattice the trap forces **no** `mod q` structure at
all — the resolution mechanism collapses. So even the *corrected-ceiling* form of T1
is false without the common-`q` hypothesis.

---

## 2 — T1' (corrected resolution / class-count bound) (PROVED, BLOCK A/B/D)

> **Theorem 1' (class count under a common-denominator resonance).** Let `V` be
> trapped off `eps b` exceptions in `Q(theta; w)` with **`theta_2 = a/q` and
> `theta_1 = a'/q`, common `q`, `gcd(a,q) = 1`** (the #663 Prop 5 hypothesis).
> Writing `s(v) = (a v^2 + a' v) mod q`, the trapped `v` occupy at most
> ```
>     N(q, w)  <=  (2 floor(wq) + 1) · M(a,a';q)   <=   (2wq + 1) · M(a,a';q)
> ```
> residue classes `mod q`, where `M(a,a';q) = max_t #{ r in Z/q : a r^2 + a' r ≡ t }`
> is the maximal fiber of the quadratic residue map. For **odd squarefree `q`** with
> `gcd(2a,q)=1`, `M = 2^omega(q)` (`<= 2` per prime, CRT — #663 Prop 5); in general
> `M <= 2^omega(q)` up to the prime-power slack #663 flagged (`M <= sqrt(q)` in the
> worst degenerate target `t` with `disc ≡ 0`, and `M = 2^omega(q) = q^{o(1)}`
> generically).
>
> **(Sufficient single-class regime — the surviving correct core.)** If
> `w < 1/(2q)` then `2 floor(wq)+1 = 1` **uniformly in `theta_0`** (a single target
> `s = r_0`), so `N <= M = 2^omega(q)` — a rank-1 GAP, exactly #663 Prop 5. This is
> **sufficient, not necessary**: the `q = 7`, `w = 0.10` witness resolves to a single
> class with `w > 1/(2q)`.
>
> **(Horn-effective ceiling.)** The horn feeds #657 Theorem 2/3, which needs
> `O(1)` residue classes (a rank-1 GAP of `O(1)` APs of common difference `q`). For
> `N = O(1)` the target count must be `O(1)`: `2 floor(wq)+1 = O(1)`, i.e.
> `q = O(1/w)`. For a #661-Theorem-B trap of a `phi >= 1-eta` block,
> ```
>     w = sqrt( (ln2/2)(eta + 1/b)/eps )  >=  sqrt( ln2/(2b) )  =: w_min ,
> ```
> so the horn-usable denominators satisfy `q = O(1/w) = O(sqrt(b))`, **polynomial in
> `b`, uniformly in `eta in (0,1)`, `eps in (0,1]`**. The `theta_0`-uniform
> guaranteed-single-class ceiling is `q < 1/(2 w_min) = sqrt(b/(2 ln2)) = 0.84932
> sqrt(b)`.

*Proof.* Under the hypothesis `theta_2 v^2 + theta_1 v ≡ s(v)/q (mod 1)` with
`s(v) in Z/q`; `v` trapped `<=> s(v) in W(theta_0)`, `|W| = 2 floor(wq)+1 <= 2wq+1`
(integers of the `(1/q)`-lattice inside an arc of length `2w`; `= 1` for all
`theta_0` iff `2wq < 1`). The trapped `v` lie in `union_{s in W} {v : a v^2+a'v ≡ s}`,
a union of `|W|` quadratic-congruence fibers, each of size `<= M`. Hence
`N <= |W|·M <= (2wq+1)M`. The single-class regime and the multiplicity bounds are the
standard quadratic-congruence counts (`gcd(2a,q)=1`: complete the square,
`(2av+a')^2 ≡ a'^2 + 4a s (mod q)`, `<= 2^omega(q)` square roots for `q` odd
squarefree; `<= sqrt(q)` in the degenerate `disc ≡ 0` target). The width bound is
#661 Theorem B minimized at `eps = 1`, `eta -> 0`. The `O(1/w)` ceiling follows since
`2 floor(wq)+1 <= K` forces `q < K/(2w)`, and `M >= 1` only tightens it. ∎

**Verifier (BLOCK B).** `N(q,w) <= (2 floor(wq)+1)·M(a,a';q)` is asserted on a
`13 x 4` grid of `(q, w)` (`q` up to 600, including `q=7, w=0.10`); all rows hold.
The naive `(2wq+1)·2^omega(q)` form is **not** universally valid (it fails at
`q = 81, a' = 0` where the degenerate `t=0` fiber has `M = 9 > 2^omega = 2`), which
is why T1' carries `M` explicitly; `M = 2^omega(q)` is verified on the odd-squarefree
sub-grid.

**Moral (corrected).** A large-fiber Bohr trap resolves rationality only at
**polynomial** denominators `q = O(sqrt(b))` — but this is a statement about the
**horn-usable** range (`O(1)` classes), *not* a hard ceiling on where any single
class can appear. The load-bearing fact for T3 is the polynomial growth, which
survives; the false part was reading `0.84932 sqrt(b)` as a *necessary* ceiling.

---

## 3 — T2' (host-smallness threshold, common-q carried) (PROVED/SURVIVES, BLOCK E)

T2 is untouched by the T1 defect except that its input "resolved rational resonance"
must now name the full hypothesis. Restated:

> **Theorem 2' (host-smallness threshold).** Let `V subseteq [0,D]`, `D = 2^{delta
> b}`, be trapped by a resonance with **`theta_2 = a/q`, `theta_1 = a'/q` (common
> `q`)** into `N(q) = q^{o(1)}` residue classes `mod q` (T1'). The residue-class host
> `P = R + q[0, D/q)` has `log2|P|/b = delta - log2(q)/b + o(1)`, and the corridor
> bound `lambda <= alpha + 1/3` (#657 box bound, rank `<= 2`) follows from
> `V subseteq P` **only if**
> ```
>     log2(q)/b  >=  beta := delta - (alpha+1/3)/3 = delta - alpha/3 - 1/9 ,
>     i.e.  q  >=  q_cross := 2^{beta b} .
> ```
> On the fenced class `beta > 0` (#682 Cor 2), so `q_cross` is **exponential**.

*Proof.* Verbatim #691 T2: `|P| = N(q)·(D/q+O(1)) = D·q^{-1+o(1)}`; dividing out the
common difference is the affine map `v -> (v-r)/q`, which preserves `(f,L)` exactly
and cuts `delta` by exactly `log2(q)/b` (#643/#685 affine invariance). A rank-1 host
gives `lambda <= 3(delta - log2 q/b) + o(1) <= alpha + 1/3` iff `log2 q/b >= beta`.
The common-`q` clause enters only through T1' (it is what makes `N(q) = q^{o(1)}`
meaningful); the box-bound arithmetic is unchanged. ∎

**Corollary (box bound already useless, SURVIVES).** On the fence `delta > alpha/3 +
1/9`, so `3 delta > alpha + 1/3`: the trivial diameter box bound `lambda <= 3 delta`
exceeds the corridor target, so the horn must genuinely **cut `delta`**, needing
`q >= 2^{beta b}`. (Verifier BLOCK E: dilation by `q` raises `delta` by exactly
`log2(q)/b` with `(f,L)` fixed; `3 delta_fenced > alpha+1/3` at
`alpha in {alpha_0, 0.4, 2/3}`.)

---

## 4 — T3' (empty window, re-derived with the corrected ceiling) (PROVED/SURVIVES, BLOCK F)

Combine T1' and T2'. The horn (#663 Prop 5 / R3) needs a `q` that is simultaneously
**host-shrinking** (`q >= q_cross = 2^{beta b}`, T2') and **horn-usable** (resolves
into `O(1)` classes, T1'). By T1' the horn-usable range is **polynomial**,
`q = O(sqrt(b))`; the `theta_0`-uniform guaranteed-single-class ceiling is `Q_res :=
1/(2 w_min) = 0.84932 sqrt(b)` (the *same* constant as #691, now correctly a
**sufficient** threshold).

> **Theorem 3' (empty denominator window / main result — SURVIVES).** On the fenced
> class the rational-resonance horn requires `q` in the interval `[q_cross, Q_res] =
> [2^{beta b}, 0.84932 sqrt(b)]`. Since `beta > 0`, `2^{beta b} > 0.84932 sqrt(b)`
> for every `b > b_0(beta)`, so **the interval is empty and the horn is vacuous**:
> ```
>     beta      0.0100   0.0500   0.1000   0.1928   0.2222   0.3000
>     b_0       411      53       19       2        2        2      (verifier BLOCK F, UNCHANGED)
> ```
> and the gap `q_cross / Q_res` only widens for `b > b_0`. The `b_0` table and the
> constant `0.84932 = 1/sqrt(2 ln2)` are **unchanged from #691** — the correction
> reinterprets the constant's *role* (a sufficient horn-usability threshold, not a
> necessary resolution ceiling) and adds the common-`q` hypothesis, but leaves the
> emptiness arithmetic identical (`2^{beta b}` exponential vs `sqrt(b)` polynomial).

*Proof.* A `q in [q_cross, Q_res]` exists iff `2^{beta b} <= 0.84932 sqrt(b)`, false
for `b > b_0(beta)` (BLOCK F recomputes `b_0` from the inequality and checks the gap
widens at `4 b_0`). The horn cannot instead exploit an accidental single-class
resolution at exponential `q`: for `q >> 1/w` the trapped count is `N ~ 2wq`
(equidistribution of `s(v)`), which is **exponential** at `q = 2^{beta b}` — no
`O(1)`-class resolution exists there (BLOCK F asserts `N(q,w) >= ` a growing
fraction of `2wq` on a large-`q` grid). Thus the polynomial ceiling is not merely a
sufficient-condition artifact: the horn-usable set is genuinely `O(sqrt b)`. ∎

> **Corollary (Bohr face = box face — SURVIVES UNTOUCHED, a T2-side fact).** The
> `delta` at which the window closes is `beta = 0`, i.e. `delta = alpha/3 + 1/9 =
> (alpha+1/3)/3` — **exactly #682's residual line** `delta_res(alpha)`. This identity
> is a property of `beta` (defined on the T2 / host side and #682's residual line);
> it does **not** reference T1's resolution ceiling and so is untouched by the
> refutation. Verifier BLOCK F checks `alpha/3 + 1/9 = (alpha+1/3)/3` at
> `alpha in {alpha_0, 0.4, 2/3}`.

**Negative control (BLOCK F, SURVIVES).** Emptiness *hinges* on the ceiling being
polynomial. The verifier re-checks the counterfactual: a hypothetical exponential
ceiling `~ 2^{b/4}` would open a window for `beta < 1/4`. So T3' is carried by the
`O(sqrt b)` ceiling of T1', which is its genuine content — unchanged in substance
from #691, now on a correct footing.

---

## 5 — Supersession: what is refuted, corrected, and what survives

| #691 claim | verdict | replacement / note |
|---|---|---|
| T1 "resolves `q` **only if** `q <= 1/(2w)`" (necessity) | **REFUTED** | T1' class-count bound; `q=7,w=0.10` witness |
| T1 `0.84932 sqrt(b)` read as a *resolution ceiling* | **REFUTED** as a ceiling | survives as the **sufficient** guaranteed-single-class threshold |
| T1 proof "no `mod q` structure forced for `w >= 1/(2q)`" | **REFUTED** | count grows `~2wq+1`, does not vanish |
| T1 hypothesis "`theta_2 = a/q` rational" (only) | **UNDER-HYPOTHESIZED** | needs `theta_1 = a'/q`, common `q` (#663 Prop 5) |
| verifier BLOCK 2 "a width-`w` trap NEVER resolves `q > ...`" | **REFUTED** (false headline, never cross-asserted) | corrected grid asserts `N <= (2floor(wq)+1)M` |
| T2 host-smallness threshold `q_cross = 2^{beta b}` | **SURVIVES** | T2' (common-`q` named; arithmetic identical) |
| T2 box-uselessness corollary (`3 delta > alpha+1/3`) | **SURVIVES** | unchanged |
| T3 empty-window headline + `b_0` table (411/53/19/2) | **SURVIVES** | T3' (corrected ceiling role + common-`q`; table unchanged) |
| T3 "Bohr face = box face" (`beta=0 ==` residual line) | **SURVIVES UNTOUCHED** | T2-side fact, independent of the T1 error |
| R4 / P4 (fiber-trapping decoupling: generic Bohr subset is Sidon) | **SURVIVES UNTOUCHED** | metric/additive decoupling; no `(1/q)Z` step used (BLOCK G) |
| P5 tension, P6 descent | **SURVIVES** | affine-invariance / measured mass; do not invoke the refuted ceiling |

The one-line verdict of #691 ("MIXED, leaning negative — the fenced class is
Diophantine-blind to the bounded-denominator horn, empty window, crossover =
residual line") **stands**, now on a corrected T1.

---

## 6 — Nonclaims

- We do **not** claim `0.84932 sqrt(b)` is a bound on where *any* single-class
  resolution can occur — it is the `theta_0`-uniform **sufficient** threshold and the
  horn-usable ceiling; accidental single classes occur above it (`q=7`).
- We do **not** prove `M(a,a';q) = 2^omega(q)` for all `q` — it can reach `~ sqrt(q)`
  at degenerate targets; T1' carries `M` explicitly and only uses `M = q^{o(1)}`
  generically and the target-count factor `2 floor(wq)+1` for the ceiling.
- We do **not** edit `fenced_resonance_window.md` (#691) or its verifier; this is a
  standalone repair note. The integrated file's other blocks (T2, R4/P4, P5, P6) are
  re-checked here as surviving but not modified.
- We do **not** re-open the unconditional `Bohr -> GAP` step; it remains **OPEN**
  (multi-class exponential inverse-Littlewood-Offord), unchanged from #663/#673.
- No signed `mu_n` / max-fiber object is entered (hughes #564 lane). Image face only
  (`f, L, Phi`). No `.tex`/`.pdf` touched.

---

## 7 — Files, credit, PI re-derivation

- Repair note: `experimental/notes/thresholds/fenced_resonance_window_repair.md` (this).
- Repair verifier: `experimental/scripts/verify_fenced_resonance_window_repair.py`
  (`python3` stdlib only, deterministic; `--check` asserts the corrected ceiling and
  class-count bound on the `(q,w)` grid with `q=7,w=0.10` as the explicit negative
  control, the dropped-hypothesis control, the guaranteed-single-class threshold, the
  `b_0` table, the Bohr=box-face identity, and the P4 decoupling survival;
  `--tamper-selftest` confirms the harness catches a reinstated false ceiling;
  `RESULT: PASS`).
- Read-only inputs (public repo artifacts, by PR number): the integrated
  **#691** `fenced_resonance_window.md` (the note under repair); **#663**
  `bohr_gap_volume.md` (**Proposition 5**, R3, the full common-`q` hypothesis and
  the golden counterexample R2.4); **#661** `exp_ilo_fourier.md` (Theorem B trapping
  width); **#657** `ilo_moment_structured.md` (Theorem 2/3, the rank-1 GAP consumer);
  and, via #691, **#682/#685** (`delta` coordinate, residual line, dilation
  invariance).

**Credit (mandatory).** The `q = 7` counterexample to the printed T1 and the dropped
common-denominator hypothesis were found by a **Codex team read-only audit**, and
verified firsthand. No other process references — public repo artifacts and PR
numbers only.

**Per-claim status.** T1 as printed = **REFUTED** (the "only if", the ceiling
reading, the "no structure forced" step) and **UNDER-HYPOTHESIZED** (dropped
`theta_1 = a'/q`). T1' (class-count bound + guaranteed-single-class sufficient
threshold + polynomial horn ceiling), T2' (host threshold), T3' (empty window) =
**PROVED**. T3's empty-window headline, its `b_0` table, the constant `0.84932`, the
Bohr=box-face corollary, and R4/P4 = **SURVIVE**. The unconditional `Bohr -> GAP`
= **OPEN** (unchanged).

**Exact vs heuristic.** All residue counts `N(q,w)`, the maximal fibers `M`, the
`b_0(beta)` table, the invariances, and the dropped-hypothesis controls are exact
integer computation. Theorems 1'-3' are elementary closed-form. No signed `mu_n`
object entered.
