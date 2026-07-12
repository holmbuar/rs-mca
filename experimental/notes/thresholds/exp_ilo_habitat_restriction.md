# The habitat-restricted (Bohr -> GAP) wall: #663's three bridges stay dead inside the #701 two-band habitat

## Status

`HARD INPUT 2 SERVED: image-scale MI+MA / direct Sidon payment (AGENTS.md's five).
Its wall is the per-instance EXPONENTIAL inverse-Littlewood-Offord = the
(Bohr -> GAP) step at exponential concentration = Diophantine control of the
dominant resonance denominator q.

TARGET: the residual wall RESTRICTED to the Theorem-5 HABITAT of open PR #701
(intermediate max-fiber density theta in (0.1740,0.8260) AND intermediate source
fiber energy -log2 Delta(F)/b in (0.1383,0.4779)).  #663 killed the three cheap
Bohr->GAP bridges for GENERAL spread blocks; the habitat is strictly smaller -- does
restriction REOPEN any route?  VERDICT: NO (DECIDED-NEGATIVE) / STEP 1 (PROVED):
the residual wall restated inside the habitat, carrying EVERY hypothesis (wall floor
phi>1/3, both #701 bands, #661 Thm A/Lemma2/ThmB trap, #663 Prop 5 / #700 T1'
common-q horn) / STEP 2 -- Theorem H (PROVED): both habitat coordinates
(theta = m*/b, Delta = E(F)/f^3) are AFFINE-INVARIANT while q is not (q -> q/gcd(q,a^2)
under v->av+c), and Delta = INT|Fhat|^4 integrates over the full source b-torus on
which the resonance is a Lebesgue-null 3-subtorus -- so habitat membership imposes
ZERO constraint on q.  Route-by-route: R1a large-sieve STILL-DEAD (INT|S|^4=2b^2-b
UNIVERSAL, unchanged in habitat); R1b Weyl STILL-DEAD (no interval; a Diophantine
in-habitat resonance exhibited); R2b volume->multiplicity STILL-DEAD (threshold uses
detG, which scales a^6 and is decoupled from the affine-invariant bands); R2c
elimination STILL-DEAD (mod-1 failure is frequency-universal); the closing horn is
NOT forced (champ18 is IN the habitat bands with a spread, no-small-q resonance) /
STEP 3 (DECIDED-NEGATIVE): the energy band + #661's sublevel volume do NOT force any
sub-exponential denominator control -- energy is decoupled (P3) and the exponentially
small volume vol(T_kappa)>=2^{-eta b}/2 can be Diophantine-centered / STEP 4 positive
residue (PROVED sharpening): the wall's SOLE remaining content inside the habitat is
image-denominator control, and the entire (theta,Delta) habitat box is provably
useless for supplying it; "the smaller habitat might help" is converted into the
theorem "it is smaller only along source axes -- the wall is exactly as open inside
the habitat as outside" / verifier PASS 47/47 + tamper 5/5, ~3.5 s`.

This packet restricts the image-face wall stack to the habitat that open PR **#701**
(`fenced_energy_pincer.md`, Theorem 5) proved every wall block inhabits, and asks
whether the strictly smaller region reopens any of the three Bohr->GAP bridges that
**#663** (`bohr_gap_volume.md`) killed for general spread blocks.

Shared notation (`#655/#657/#661/#663/#682/#691/#696/#701`): a **block** `V` is `b`
distinct integers, normalized `min V = 0`, `gcd = 1`, diameter `D = max V`; the
degree-2 signature is `Phi(S) = (|S|, sum_S x, sum_S x^2)`; `f` = max fiber size,
`L` = image size; `phi = log2 f/b`, `lambda = log2 L/b`, `eta = 1-phi`;
`X = (fL)^{1/b} = 2^{phi+lambda}`, and **the wall is `X > 2^{4/3}`**. The max fiber
`F subseteq {0,1}^b` is a set of Boolean masks at one weight `m*`; its **source**
additive energy is `E(F) = #{(a,b,c,d) in F^4 : a+b = c+d in Z^b}`,
`Delta(F) = E(F)/f^3 in [1/f,1]`, `theta = m*/b`. Moment-curve columns
`u_i = (1, v_i, v_i^2)`, `psi_i(theta) = <theta, u_i>`,
`|Xhat(theta)| = prod_i |cos(pi psi_i)|`; the quadratic Weyl sum on the **image** is
`S(t1,t2) = sum_i e(t1 v_i + t2 v_i^2)`; the **dominant resonance denominator** `q`
is the denominator of the `theta_2` at which the `|Xhat|`-marginal
`M(theta_2) = INT_{[0,1)^2} |Xhat| dtheta_0 dtheta_1` concentrates.
`T_kappa = { theta in [0,1)^3 : sum_i ||psi_i(theta)||^2 <= kappa b }`.

**One-line verdict.** **DECIDED-NEGATIVE.** The habitat is cut out by two
**affine-invariant, source-side** coordinates `(theta, Delta)`; every one of #663's
three route-killers is either **universal** (the moment-curve energy identity
`INT|S|^4 = 2b^2-b`), a property of the **image frequencies** (Weyl-no-interval; the
mod-1 elimination failure), or a **spread/`det G` threshold** — none of which is
constrained by an affine-invariant source band. So restriction to the habitat gives
**zero traction** on the denominator axis the wall lives on: all three routes stay
dead inside it, and the closing rational-resonance horn is **not** forced (a
Diophantine-resonance block sits inside the habitat bands). The one genuinely new
thing the habitat buys — proved here — is a **sharpening**: the wall's sole
remaining content is image-denominator control, and the entire habitat box is
provably useless for it, so any future closing argument must supply `q`-control from
the image moment-Fourier data alone.

Every number is recomputed by
`experimental/scripts/verify_exp_ilo_habitat.py` (stdlib-only, deterministic,
`--check` prints `RESULT: PASS (47/47)`, `--tamper-selftest` catches `5/5`
mutations, ~3.5 s / <60 MB under `ulimit -v 2097152`; the habitat band edges are
re-derived exactly, `champ18`/`unionAP16` carried with exact `(f,L,m*,E)` and
certified in-habitat, affine-invariance of `(theta,Delta)` shown byte-for-byte
against the moving denominator `{3,6,27}`, the resonance subtorus rank certified
`= 3`, the moment-curve energy identity re-checked on five families, and each route
survival exhibited; a small JSON certificate is written to
`experimental/data/certificates/exp-ilo-habitat/certificate.json`).

Label key: **PROVED** (complete re-derivable proof, every external theorem quoted
within its printed hypotheses and used only in scope), **COUNTEREXAMPLE** (a
proposed statement refuted with a witness), **MEASURED** (exact finite objects, or
`|Xhat|` by fixed midpoint quadrature used only to read concentration), **AUDIT**
(cross-reference), **OPEN**. House labels in parentheses: **DECIDED-NEGATIVE**,
**STILL-DEAD**, **REOPENED**.

**Credit.** The two-band **habitat** (`theta in (0.1740,0.8260)`,
`-log2 Delta(F)/b in (0.1383,0.4779)`) is **Theorem 5 of open PR #701**
(`fenced_energy_pincer.md`), together with its three decoupling pillars
(P1 affine-blindness, P2 equal-`(theta,Delta)` non-functionality of `q`, P3
measure-zero blindness), which this packet imports and re-verifies. The realized-image
energy lift `fL <= 2^{b g(theta)} Delta(F)` and the density/energy constants are
**DannyExperiments #696** (`realized_image_energy_lift.md`), consumed only through
#701. The atom bound `f <= 2^b INT|Xhat|` (Thm A), the sublevel-volume reduction
`vol(T_kappa) >= 2^{-eta b}/2` (Lemma 2), single-frequency quadratic-Bohr trapping at
width `w = sqrt(kappa/eps)`, `kappa = (ln2/2)(eta+1/b)` (Thm B), the affine action on
the resonance `theta_2 -> a^2 theta_2` (Prop 3), and the `det G` fiber-floor are
**our #661** (`exp_ilo_fourier.md`, integrated). The three dead bridges — the
structure-blind moment-curve energy `INT|S|^4 = 2b^2-b`, the Weyl-no-interval /
golden-Diophantine equidistribution, the per-branch Gaussian volume and the
volume-to-multiplicity threshold `log2 det G >= 2 eta b + O(log b)`, the mod-1
elimination obstruction, and the rational-resonance horn (Prop 5:
`theta_2 = a/q` AND `theta_1 = a'/q`, common `q`, `q = O(1)`, `w < 1/(2q)`) — are
**our #663** (`bohr_gap_volume.md`, integrated). The corrected common-`q`
resolution ceiling — class count `<= (2 floor(wq)+1) M(a,a';q)`, single class system
guaranteed only for `w < 1/(2q)`, horn-effective denominator ceiling **polynomial**
in `b` (`O(sqrt b)`) — is **open PR #700** (`fenced_resonance_window_repair.md`,
correcting #691 `fenced_resonance_window.md`). The `b=18` champion
`V = {2,3,4,...,34}` (`f=30, L=151275`) is **our #655** (`fiber_image_tradeoff.md`);
affine invariance is **our #643** (`pte_cluster_packing_frontier.md`, Lemma A) and
dilation invariance **our #685** (`corridor_interior_hunt.md`); the corrected
Step-B exception scale `O(eta b)` and the discipline of never importing a theorem
past its printed hypotheses are carried via #661/#700. The minimal degree-2 PTE
trade support `6` is **scottdhughes #564**
(`w_a_star_pte_lemma.md`). External inputs cited **only within printed hypotheses,
never re-derived**: Weyl's inequality (its interval hypothesis is exactly what a
spread block lacks); the large sieve / Halász method (shown structure-blind on the
moment curve); inverse-Littlewood-Offord (**Tao-Vu; Nguyen-Vu**) and its
exponential-regime analogue (**Ferber-Jain-Luh-Samotij**), named as the open
magnitude object. **Lane discipline:** image face only (`f, L, Phi, theta, Delta,
q`); no signed `mu_n`/`(LS)`/`(SV*)` object (#564) is entered. Open PRs #700/#701 are
flagged as such at every use; #661/#663 are integrated.

---

## R0 — the three inputs and the goal (AUDIT)

**The wall, verbatim (#661/#663).** #661 proved (unconditional): the atom bound
`f <= 2^b INT|Xhat|` (Thm A); `f >= 2^{(1-eta)b}` forces `vol(T_kappa) >=
2^{-eta b}/2` with `kappa = (ln2/2)(eta+1/b)` (Lemma 2); one `theta in T_kappa`
traps all but `eps b` of the `v_i` in one quadratic Bohr set `Q(theta; w)` of width
`w = sqrt(kappa/eps)` (Thm B). #663 proved the three cheap Bohr->GAP bridges
impossible for general spread blocks and localized the wall to **Diophantine control
of the dominant resonance denominator `q`**, the one horn that closes being the
**common-`q`** resonance (Prop 5): `theta_2 = a/q` **and** `theta_1 = a'/q`,
`q = O(1)`, `w < 1/(2q)`. Open PR #700 corrected the resolution ceiling to a class
count `<= (2 floor(wq)+1) M(a,a';q)` (single class system guaranteed only for
`w < 1/(2q)`), leaving the horn-effective denominator ceiling **polynomial** in `b`.

**The habitat (open PR #701, Theorem 5).** Composing #696's realized-image energy
lift with the wall, every wall block (`X > 2^{4/3}`) satisfies, in the
**affine-invariant source coordinates** `(theta, Delta)`:
```
    theta = m*/b in (0.173952, 0.826048)                         (density band, #696 (3))
    -log2 Delta(F)/b in (0.138346, 0.477945)                     (energy  band, #696 (4),(8))
```
so a wall block's max fiber has **intermediate weight** and **intermediate source
additive energy** (neither Sidon-like `Delta -> 1/f` nor coset-like `Delta -> 1`).
#701 also proved (P1--P3) that fiber energy is **denominator-blind**, so energy
**alone** cannot supply the Diophantine lever.

**The goal.** #663 killed the three bridges for *general* spread blocks. The habitat
is *strictly smaller*. Does the density band or the energy-deficit band invalidate
the counterexample/obstruction that killed each route? Ladder: (1) restate the
residual wall inside the habitat carrying every hypothesis; (2) re-examine each dead
route under the habitat constraints; (3) test whether energy + sublevel volume force
a Diophantine statement; (4) report the honest outcome.

---

## R1 — the residual wall, restated inside the habitat (STEP 1; PROVED restatement)

Carrying **every** hypothesis its proof uses (the standing lesson that an omitted
clause is a refutable print):

> **(Wall | Habitat) — residual form.** Suppose a normalized block `V` (`min = 0`,
> `gcd = 1`, `b` distinct integers) satisfies:
> - **[wall]** `X = (fL)^{1/b} > 2^{4/3}`, hence (from `lambda <= 1`) the fiber
>   floor `phi > 1/3`, hence `eta = 1 - phi < 2/3`;
> - **[habitat density — open PR #701 Thm 5 / #696 (3)]**
>   `theta = m*/b in (0.173952, 0.826048)`;
> - **[habitat energy — open PR #701 Thm 5 / #696 (4),(8)]**
>   `-log2 Delta(F)/b in (0.138346, 0.477945)`, `Delta(F) = E(F)/f^3`.
>
> Then **[#661 Thm A + Lemma 2 + Thm B]** `vol(T_kappa) >= 2^{-eta b}/2` with
> `kappa = (ln2/2)(eta + 1/b)`, and there is a `theta in T_kappa` trapping all but
> `eps b` of the `v_i` in one quadratic Bohr set `Q(theta; w)`, `w = sqrt(kappa/eps)`.
>
> The wall is defeated for `V` iff that Bohr trap upgrades to a proper GAP —
> equivalently **[#663 Prop 5 / open PR #700 T1']** iff the dominant resonance is a
> rational `theta_2 = a/q` with `theta_1 = a'/q` (**common** `q`) and `q` in the
> **horn-effective range** `q = O(sqrt b)`, so the trapped `v` occupy
> `<= (2 floor(wq) + 1) M(a,a';q) = O(1)` residue classes mod `q` (a single class
> system guaranteed when `w < 1/(2q)`), i.e. lie in a rank-1 GAP of `O(1)` APs of
> common difference `q`; #657 Thm 2/3 then gives `lambda <= o(1)`.
>
> **OPEN core (unchanged):** unconditional Diophantine control of `q` at exponential
> concentration = the per-instance exponential inverse-Littlewood-Offord.

This is #661/#663/#700's residual verbatim, now with the two `(theta, Delta)` band
clauses **added** as standing hypotheses. R2 asks whether those two new clauses do
any of the work the OPEN core needs.

---

## R2 — route by route inside the habitat (STEP 2): Theorem H, then three survivals

### 2.0 Theorem H — the habitat is affine-invariant and denominator-blind (PROVED, BLOCK 2/4)

> **Theorem H.** The two habitat coordinates are invariant under the integer affine
> action `v -> a v + c` (`a != 0`):
> ```
>     theta(aV+c) = theta(V),      Delta(aV+c) = Delta(V)          (affine-invariant)
> ```
> [open PR #701 P1; #643 Lemma A; #685], because the action is a bijection on
> signatures, preserving the max fiber `F` **as a set of masks** and hence
> `m*, f, E(F), Delta`. The dominant resonance denominator `q` is **not** invariant:
> the same action sends `theta_2 -> a^2 theta_2` [#661 Prop 3,
> `M = [[1,0,0],[c,a,0],[c^2,2ac,a^2]]`], i.e. `q -> q/gcd(q, a^2)`. Moreover
> `Delta(F) = E(F)/f^3` with `E(F) = INT_{[0,1)^b} |Fhat|^4`, and the resonance
> frequencies `{psi(theta) : theta in [0,1)^3}` form a **Lebesgue-null 3-subtorus**
> of the source `b`-torus (`rank[1, v, v^2] = 3 < b`), so `Delta(F)` is **exactly
> blind** to `theta_2` [open PR #701 P3]. Hence **habitat membership imposes no
> constraint on `q`.**

*Proof.* Affine-invariance of `(theta, Delta)`: `v -> av+c` induces the invertible
map `(m, s1, s2) -> (m, a s1 + c m, a^2 s2 + 2ac s1 + c^2 m)` on signatures, a
bijection, so each fiber — in particular the extremal one `F` — is preserved as a set
of masks; `E(F)` reads only those masks, so `m*, f, E, Delta` are unchanged
(BLOCK 2 shows this byte-for-byte: dilating `unionAP16` by `a = 1,2,3` leaves
`(f, m*, E, Delta, F) = (20, 8, 900, 0.11250, ·)` identical). The frequency
transformation and the resulting denominator orbit are #661 Prop 3; the raw
resonance `theta_2 = (2/3)/a^2` runs through denominators `{3, 6, 27}` at that one
fixed `Delta` (BLOCK 2). The subtorus rank is a Vandermonde fact (distinct `v_i`),
certified `= 3` for both witnesses (BLOCK 4). ∎

**Reading.** `(theta, Delta)` is a strictly coarser invariant than `q`: it factors
through the affine quotient, `q` does not. The habitat is therefore (a slice of) a
**union of affine orbits**, and within the geography that matters it does not — indeed
*cannot* — see the denominator. This is the single structural fact behind every
survival below.

### 2.1 Route 1 (V2, large-sieve / Weyl): STILL-DEAD inside the habitat

**R1a — the moment-curve energy is universal (PROVED, BLOCK 5).** #663's killer was
the identity `INT_{[0,1)^2} |S(t1,t2)|^4 = 2b^2 - b` for **every** `b`-block (the
2-dimensional Sidon rigidity of the moment curve: two points are determined by two
moments), which pins the additive energy that any large-sieve / energy-increment /
BSG argument would amplify at its **minimum**, structure-blind. The habitat
constrains `Delta(F)`, the **source** fiber energy on the `b`-torus; `INT|S|^4` is
the **image** moment-curve energy on the 2-torus, a *universal constant* in `b`.
These are different objects (BLOCK 4: the resonance/image data lives on a null
subtorus of the source integral), and a universal identity cannot be altered by a
nonempty constraint region — it holds **identically** inside the habitat (BLOCK 5
re-checks `INT|S|^4 = 2b^2-b` on five families including a champ18-core). The
large-sieve reach cap `eta >~ 2 log2(b)/b -> 0` is likewise untouched: the habitat's
only constraint on `eta` is the wall floor `eta < 2/3`, a **constant**, which clears
the vanishing corridor at every `b` (BLOCK 5). **Route 1a is unaffected by the
habitat: STILL-DEAD.**

**R1b — Weyl needs an interval; the habitat supplies none (MEASURED, BLOCK 6).**
#663's killer was that Weyl's inequality has no purchase on a spread set (nothing to
difference over), so "near-full Weyl sum" is *tautologically* the Bohr condition; the
witness was a golden-Diophantine `theta_2` whose Bohr set **equidistributes** (density
`~2w`, irregular gaps up to `65`) rather than forming a GAP. An affine-invariant band
constraint cannot manufacture an interval: BLOCK 6 reproduces the golden
equidistribution and, decisively, exhibits `champ18` — which **is in the habitat
bands** (BLOCK 1) — with a **spread, no-small-`q`** dominant resonance (small-`q`/global
marginal ratio `0.750 < 0.85`, global peak `0.679`, `0.0125` from every rational of
denominator `<= 5`). So a habitat block can carry exactly the Diophantine,
no-interval resonance that defeats Weyl. **Route 1b is unaffected by the habitat:
STILL-DEAD.**

### 2.2 Route 2 (V1, volume -> structure): STILL-DEAD inside the habitat

**R2b — the volume-to-multiplicity threshold is on the wrong axis (PROVED, BLOCK 7).**
#663's obstruction was the per-branch Gaussian volume `(4pi/3)(kappa b)^{3/2}/
sqrt(det G)`, whence Lemma 2's volume forces resonance multiplicity (`N_branch >= 2`)
**only** when `log2 det G >= 2 eta b + 3 log2(kappa b)` — a threshold in `det G` and
`eta`. But `det G` scales as `a^6` under `v -> a v` (BLOCK 7:
`det G(3V) = 3^6 det G(V)`), an **affine-variant spread** quantity, while the habitat
coordinates `(theta, Delta)` are **affine-invariant** and fixed under the *same*
dilation (BLOCK 7). So the habitat pins neither `det G` nor `eta` (beyond the wall
floor `eta < 2/3`); the multiplicity threshold is untouched. The residual it leaves —
**spread, large-fiber, not a union of few APs** — is exactly the AP-free block, of
which `champ18` (in-habitat) is the standing example. **Route 2b is unaffected by the
habitat: STILL-DEAD.**

**R2c — the mod-1 elimination failure is frequency-universal (PROVED, BLOCK 8).**
#663's obstruction was that eliminating `v^2` between two resonances is exact over
`R` but fails mod 1 (`||alpha x|| != |alpha| ||x||` for non-integer `alpha`), so two
quadratic Bohr conditions do not combine into a linear one. This is a property of
**any two real frequency vectors**, independent of the block; BLOCK 8 exhibits it on
genuine near-resonances (the eliminated linear form has `max_v ||mu v + c|| = 0.450`,
near the maximum `1/2`). Being frequency-universal, it holds for the frequencies of
habitat blocks verbatim. **Route 2c is unaffected by the habitat: STILL-DEAD.**

### 2.3 The closing horn is not forced by the habitat (MEASURED, BLOCK 3)

The one bridge that closes (#663 Prop 5 / #700 T1') needs a **rational, common-`q`,
bounded-`q`** dominant resonance. Theorem H says the habitat cannot deliver it, and
BLOCK 3 realizes the non-functionality on gcd=1 representatives: `champ18` and
`unionAP16` share `theta = 1/2` and `Delta` to within `4.6%` — **the same habitat
point** — yet `unionAP16` resonates **exactly at `2/3`** (`q = 3`, its embedded
difference-3 AP, marginal ratio `1.000`) while `champ18` is **spread** (ratio
`0.750`, Diophantine-like). So `(theta, Delta)` — the *entire* habitat datum — does
not determine `q`, and a habitat block may perfectly well carry a Diophantine
resonance for which the horn does not fire. **The habitat does not force
rationality.**

---

## R3 — energy band + sublevel volume do NOT force Diophantine control (STEP 3; DECIDED-NEGATIVE, BLOCK 9)

The most optimistic habitat hope is that the energy band, **combined** with #661's
sublevel volume, forces some — even weak — denominator control (any unconditional
sub-exponential bound on `q` would be new). It does not, for two independent reasons
already in hand:

1. **Energy is decoupled from the resonance (Theorem H / #701 P3).** `Delta(F)` is a
   source-Boolean invariant carried on the full `b`-torus; the resonance lives on a
   null 3-subtorus. No function of `Delta` can bound `q`.
2. **The sublevel volume can be Diophantine-centered.** `vol(T_kappa) >=
   2^{-eta b}/2` is **positive but exponentially small** (BLOCK 9:
   `-log2 vol >= eta b`). A positive set of exponentially small measure need not
   contain — or lie near — any low-denominator rational; it can concentrate at a badly
   approximable point (the golden `theta_2` of BLOCK 6, whose nearest denominator
   `<= 40` sits at distance `~1/q^2`). So the volume alone forces no bounded `q`, and
   the decoupled `Delta` cannot help it.

Hence **the natural pincer from both analytic sides — source energy and image
sublevel volume — still cannot cross below exponential.** This sharpens #701's
single-lever negative (energy alone is denominator-blind) to a **two-lever** negative
(energy *and* the sublevel volume, jointly, are). **Step 3 is DECIDED-NEGATIVE.**

---

## R4 — the positive residue: the wall's residual, sharpened (STEP 4; PROVED sharpening)

The composition is not sterile: it converts a *hope* into a *theorem* about where the
wall's remaining content can and cannot come from.

> **Theorem R (habitat-sharpened residual).** Inside the habitat, the wall's sole
> undecided content is **image-denominator control** — unconditional Diophantine
> control of the dominant resonance `theta_2` at exponential concentration — and the
> **entire** `(theta, Delta)` habitat box is provably useless for supplying it. More
> precisely, both habitat coordinates are affine-invariant source-side functions
> (Theorem H); the denominator `q` is an affine-variant image-side function decoupled
> from them (P1/P3); and each of #663's three bridges is killed by an obstruction
> that is either universal (R1a), image-frequency-based (R1b, R2c), or a `det G`
> threshold (R2b) — none constrained by the bands. Therefore any argument closing the
> wall **on a habitat block** must extract `q`-control from the **image moment-Fourier
> data alone**; it may assume the two bands for free, but they contribute nothing to
> the denominator.

This is the honest deliverable. It does **not** close the wall and does not shrink it
further as a region; it **decides a natural hope negatively and names the reason**:
"the habitat is strictly smaller, so maybe it excludes the killers" is false — the
habitat is smaller only along **source axes orthogonal to the denominator axis** on
which the wall lives, so the wall is **exactly as open inside the habitat as
outside**. Combined with #661 (spectral shortcuts impossible), #663 (three bridges
impossible for general blocks), and open PRs #700/#701 (polynomial horn ceiling; the
two-band habitat and its denominator-blindness), the residual is unchanged in kind —
the exponential-regime magnitude inverse-Littlewood-Offord — now with the additional
theorem that **no source-side band, and no combination of source energy with the
image sublevel volume, can be the missing lever.**

---

## R5 — verdict, and the wall named precisely

```
    TARGET: does restriction to the #701 two-band habitat reopen any of #663's
        three Bohr->GAP bridges, or force sub-exponential denominator control?

    STEP 1  (Wall | Habitat) restated, every hypothesis carried:  wall floor
        phi>1/3 (eta<2/3) + density band + energy band + #661 trap + #663/#700
        common-q horn;  OPEN core = Diophantine control of q  (PROVED restatement).

    STEP 2  Theorem H (PROVED):  theta=m*/b and Delta=E(F)/f^3 are AFFINE-INVARIANT;
        q -> q/gcd(q,a^2) is NOT;  Delta=INT|Fhat|^4 is null on the resonance
        3-subtorus.  => habitat imposes ZERO constraint on q.
      R1a  large-sieve   STILL-DEAD   INT|S|^4=2b^2-b UNIVERSAL, unchanged in habitat
      R1b  Weyl/major-arc STILL-DEAD  no interval; champ18 (in habitat) Diophantine
      R2b  volume->mult   STILL-DEAD  threshold in detG (a^6, affine-variant) & eta
      R2c  elimination    STILL-DEAD  mod-1 failure frequency-universal
      horn (Prop5/T1')   NOT FORCED   equal (theta,Delta), incompatible q (BLOCK 3)

    STEP 3  energy band + #661 sublevel volume  =>  NO sub-exp q-control
        (energy decoupled; volume Diophantine-centerable)             (DECIDED-NEGATIVE)

    STEP 4  Theorem R (PROVED sharpening):  the wall's sole residual inside the
        habitat is image-denominator control; the (theta,Delta) box is useless for
        it => "the smaller habitat might help" is FALSE; the wall is exactly as open
        inside the habitat as outside.

    VERDICT: DECIDED-NEGATIVE.  The habitat does not reopen the wall.  Verifier 47/47.
```

---

## Nonclaims

- **Not a wall closure, not a reopening.** No route reopens; the wall's OPEN core
  (exponential-regime inverse-Littlewood-Offord / Diophantine control of `q`) is
  unchanged. This packet decides the habitat-help question **negatively**.
- **No wall block is exhibited.** `champ18` and `unionAP16` are in the habitat
  **bands** but **off** the wall (`X = 2.343, 2.274 < 2^{4/3} = 2.520`, the standing
  small-`b` plateau of #646/#661). They witness that the bands are **compatible** with
  a spread, AP-free, Diophantine resonance — which is what kills the "habitat forces
  rationality" hope — not that a wall block exists. Whether the wall class is
  inhabited at all is untouched here.
- **The resonance readings are MEASURED.** `champ18` spread vs `unionAP16` at `2/3`
  are read from a fixed midpoint quadrature of the `|Xhat|`-marginal at `b <= 18`;
  the load-bearing pillars are the exact affine-invariance (Theorem H, P1) and the
  measure-zero decoupling (P3, rank `= 3`), which are `b`-uniform.
- **The energy band's lower edge is conditional.** `-log2 Delta/b > 0.138346` uses
  the wall floor `phi > 1/3` together with `E(F) <= f^{log2 6}` (open PR #701 /
  #696); it is quoted, and only the band's nonemptiness is used.
- **No signed object entered.** The magnitude inverse-LO would need the signed `mu_n`
  object of #564; it is recorded as transfer, not entry, and remains **OPEN**.
- **Open PRs.** #700 and #701 are **open PRs**; every use is flagged. #661 and #663
  are integrated. No internal process, board, or review artifact is referenced.
- **No `.tex`/`.pdf` touched.** No `Lxxxx` anchor introduced.

---

## Files, labels, PI re-derivation

- Note: `experimental/notes/thresholds/exp_ilo_habitat_restriction.md` (this).
- Verifier: `experimental/scripts/verify_exp_ilo_habitat.py`
  (`python3` stdlib only, deterministic; `--check` -> `RESULT: PASS (47/47)`,
  `--tamper-selftest` -> `5/5` caught, ~3.5 s / <60 MB). Writes
  `experimental/data/certificates/exp-ilo-habitat/certificate.json`.
- Read-only inputs (public-repo artifacts, by PR number): open PR **#701**
  `fenced_energy_pincer.md` (Theorem 5 habitat, P1/P2/P3); open PR **#700**
  `fenced_resonance_window_repair.md` (corrected common-`q` ceiling); **#696**
  `realized_image_energy_lift.md` (the energy lift, via #701); our **#661**
  `exp_ilo_fourier.md`, **#663** `bohr_gap_volume.md`, **#655**
  `fiber_image_tradeoff.md`, **#643** `pte_cluster_packing_frontier.md`, **#685**
  `corridor_interior_hunt.md`, **#691** `fenced_resonance_window.md`; hughes **#564**
  `w_a_star_pte_lemma.md`.

**Per-claim status.** The habitat restatement (R1), Theorem H (affine-invariance +
denominator-blindness, R2.0), the three route survivals R1a/R2b/R2c, the Step-3
negative (R3), and Theorem R (R4) = **PROVED** (elementary; the affine and
measure-zero facts are exact integer / linear-algebra computation). R1b's
no-interval survival and the closing-horn non-forcing (R2.3) rest on **MEASURED**
resonance readings (fixed quadrature) plus the PROVED pillars. The habitat bands
themselves = **AUDIT** (imported from open PR #701, its constants re-derived). The
unconditional Diophantine control of `q` = **OPEN** (unchanged).

**Flagged for PI (least-certain, 3 points).**
(a) **Theorem H is the load-bearing claim and is exact.** Affine-invariance of
`(theta, Delta)` (bijection on signatures) and the null-subtorus decoupling
(`rank = 3 < b`) are `b`-uniform integer/linear-algebra facts; the two witness
blocks only *illustrate* them. The verdict does not depend on the small-`b`
quadrature.
(b) **The witnesses are off-wall band residents.** `champ18`/`unionAP16` establish
that the habitat **bands** are compatible with a Diophantine resonance; they are not
wall blocks (none is known at small `b`). The claim is precisely "the habitat does
not force rationality," for which a band-resident Diophantine block suffices.
(c) **Step 3 is a negative about two named levers.** It proves the source energy and
the image sublevel volume, jointly, cannot force sub-exponential `q`-control; it does
**not** prove no other lever can. A genuinely new image-side idea (e.g. `INT|S|^6`
at growing order) remains open — but that is the exponential-regime inverse-LO itself.

**Exact vs heuristic.** All `f, L, m*, E, Delta, theta, det G`, the affine-invariance
byte-check, the moment-map rank, the moment-curve energy identity, and the habitat
band edges are exact integer / closed-form computation. Theorems H and R and the
route survivals are elementary closed-form proofs. The `|Xhat|`-marginal peak
locations are midpoint quadrature used only to read which denominator a peak occupies
(MEASURED). #700/#701/#696 and the exponential-regime inverse-LO are cited within
their (open / audited) scopes and never re-derived. No signed `mu_n` object entered.
No `.tex`/`.pdf` touched.
