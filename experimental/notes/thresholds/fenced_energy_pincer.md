# The fenced energy pincer: why #696's realized-image energy lift does not close the resonance-denominator wall (source/image face mismatch)

## Status

`TARGET: compose DannyExperiments PR #696 (realized-image Boolean-slice energy
lift: fL <= K(N,m) Delta(F), a per-instance bound by the max fiber's OWN additive
energy) with our #691 (bounded-denominator window EMPTY on the fenced class, as corrected)
and our #692 (fiber-denominator resolution tension confined off the wall), against the
image-face wall #661/#663 localized as Diophantine control of the dominant
resonance denominator q -- does the composition force q into controlled range on
any nonempty window? / STEP 1 -- #696 RESTATED + VERIFIED (AUDIT): #696 proves, for
a realized additive image on a fixed-weight Boolean slice, fL <= B(N,m) Delta(F)
and fL <= 2^{N g(theta)} Delta(F) with Delta(F)=E(F)/f^3 the fiber's source
additive energy; its cardinality-augmented form is EXACTLY the program's degree-2
signature, so on the wall X=(fL)^{1/b}>2^{4/3} it forces (i) density
h2(theta)>2/3 (theta in (0.1740,0.8260)) and (ii) the two-sided ENERGY BAND
2^{-0.4779 b} < Delta(F) < 2^{-0.1383 b}. Its verifier PASSES (76,231 checks) /
STEP 2 -- COMPOSITION (PROVED negative): #696's band lives in coordinates
(theta, Delta) that are ORTHOGONAL to the denominator coordinate q that #691/#692
control; the intersection #696 ∩ #691 ∩ #692 is a nonempty PRODUCT with q free, so
no window forces q / OBSTRUCTION (PROVED, three pillars): (P1, EXACT) Delta(F) is
AFFINE-INVARIANT -- dilating a block leaves (f,L,fiber,E,Delta) byte-identical
while the resonance denominator runs through {3,6,27}; (P2, MEASURED) even after
gcd=1 normalization, champ18 and unionAP16 share theta=1/2 and Delta within 4.6%
yet have incompatible resonances (champ spread at theta_2~0.679, no small rational
within 0.012; union exactly at 2/3, q=3); (P3, EXACT) the resonance frequencies
{psi(theta): theta in [0,1)^3} form a 3-dim (Lebesgue-null) subtorus of the source
b-torus over which E(F)=INT|Fhat|^4 integrates, so Delta carries ZERO resonance
information / POSITIVE RESIDUE (PROVED): #696 nonetheless CONFINES the wall to a
new two-band region -- density theta in (0.1740,0.8260) AND energy
-log2 Delta(F)/b in (0.1383,0.4779) -- a genuine habitat-shrink orthogonal to the
denominator geography of #682/#691 / VERDICT: DECIDED-NEGATIVE for closing the
denominator wall; the obstruction is a SOURCE-energy / IMAGE-denominator face
mismatch (a per-instance energy bound that is uniform-denominator-blind), pinned
exactly in the style of #692; #696's real contribution is a new energy+density
localization of the wall's habitat, not a bridge`.

This packet works the third artifact into the image-face wall stack. Our **#691**
(`fenced_resonance_window.md`, imported here **as corrected** -- see Credit) proved
the cheap bounded-denominator horn (**#663** R3) **empty** on the fenced class; our
**#692** (`fiber_denominator_tension.md`)
made the resolution half of the fiber-denominator tension a theorem and showed its
mechanism **disjoint** from the wall regime. DannyExperiments' **#696**
(`realized_image_energy_lift.md`) supplies a genuinely new inequality -- an
**energy-boosted atom bound** `fL <= K(N,m) Delta(F)` controlling the fiber-image
product by the fiber's **own** additive energy. We ask whether #696 ∩ #691 ∩ #692
forces the dominant resonance denominator into range on any window, and decide it
**negative**, with the exact obstruction pinned.

Shared notation (`#661/#663/#682/#685/#691/#692/#696`): a **block** `V` is `b`
distinct integers, normalized `min V = 0`, `gcd = 1`, diameter `D = max V`; the
degree-2 signature is `Phi(S) = (|S|, sum_S x, sum_S x^2)`; `f` = max fiber,
`L` = image size; `phi = log2 f/b`, `lambda = log2 L/b`, `eta = 1-phi`,
`delta = log2 D/b`, `alpha = d/b` (`d` = dissociation dimension, **#668**),
`X = 2^{phi+lambda} = (fL)^{1/b}`. The wall is `X > 2^{4/3}`. The moment-curve
columns are `u_i = (1, v_i, v_i^2)`, `psi_i(theta) = <theta, u_i>`,
`|Xhat(theta)| = prod_i |cos(pi psi_i)|`; the **dominant resonance denominator**
`q` is the denominator of the `theta_2` at which the marginal `M(theta_2) =
INT_{[0,1)^2} |Xhat| dtheta_0 dtheta_1` concentrates. In #696's slice notation
(here `N = b`), for the max fiber `F`: `E(F) = |{(a,b,c,d) in F^4 : a+b=c+d in
Z^b}|` is the **source** additive energy, `Delta(F) = E(F)/f^3 in [1/f, 1]`,
`theta = m*/b` the density of the max-fiber cardinality `m*`.

**One-line verdict.** **DECIDED-NEGATIVE.** #696 constrains the **source**
additive energy `Delta(F)` of the max fiber -- a Boolean-cube invariant -- while
the wall (#663) and its two proven levers (#691 Bohr-trap denominators, #692
embedded-AP Vandermondes) constrain the **image** moment-Fourier support
`theta_2`. These live in **orthogonal coordinates**: `(theta, Delta)`
[source-density/energy] versus `(delta, alpha, eta, q)` [image-diameter/
dissociation/fiber/denominator]. #696's wall band does not touch `q`, so the
composed region is a nonempty **product** with the denominator free -- there is no
pincer. The obstruction is **exact and threefold**: (P1) `Delta(F)` is
affine-invariant, but the affine action moves the resonance denominator, so a
whole orbit of denominators shares one `Delta`; (P2) even on gcd=1 representatives,
equal `(theta, Delta)` is realized by both a small-denominator (embedded-AP) block
and a spread large-denominator block; (P3) the resonance frequencies form a
measure-zero subtorus over which the energy integral is blind. What #696 **does**
buy is a genuine **habitat-shrink**: every wall block now has density
`theta in (0.1740, 0.8260)` and normalized energy deficit
`-log2 Delta(F)/b in (0.1383, 0.4779)` -- a two-band localization orthogonal to,
and hence composable with, the denominator geography of #682/#691, but not a route
that pays the denominator wall itself. This sharpens #691/#692's "leaning negative"
into a decided face-mismatch, with the exact reason (source energy is null on the
image resonance) in hand.

Every number is recomputed by
`experimental/scripts/verify_fenced_energy_pincer.py` (stdlib-only,
`RESULT: PASS 82/82`, ~3.5 s / <60 MB under `ulimit -v 2097152`; #696's band and
density constants re-derived, its four inequalities re-checked on four exact
blocks, the affine-blindness exhibited byte-for-byte, the equal-`(theta,Delta)`
non-functionality of `q` measured, the resonance subtorus rank certified `= 3`, and
the `(theta,Delta)`-independence of #691/#692's endpoints confirmed; a
`--tamper-selftest` mutates four witnesses and confirms 4/4 detection).

Label key: **PROVED** (complete re-derivable proof, every external theorem quoted
within its printed hypotheses and used only in scope), **COMPUTED** (exact
enumeration), **MEASURED** (exact finite objects, trend read off; `|Xhat|` by
midpoint quadrature used only to read concentration), **REFUTED** (a route proved
unable to close, obstruction exhibited), **AUDIT** (cross-reference), **OPEN**.

**Credit.** The realized-image energy lift `fL <= B(N,m) Delta(F)`, its entropy
refinement `fL <= 2^{N g(theta)} Delta(F)`, the coefficient extractors
`A(N,m) = [z^{2m}](1+z+z^2)^N`, `B(N,m) = [z^{3m}](1+z+z^2+z^3)^N`, the
cardinality-augmented map `x -> (|x|, Phi(x))`, and the fenced-wall consequence
`h2(theta) > 2/3`, `-log Delta(F)/N < g(1/2) - 4/3` are **DannyExperiments #696**
(`realized_image_energy_lift.md`); its verifier
`verify_realized_image_energy_lift.py` passes (76,231 checks) and is the input this
packet builds on. The fiber bound `f <= 2^{b-d}` and `fL <= 3^b` are
**DannyExperiments #668** (`canonical_transversal_vc_compression.md`). The atom
bound `f <= 2^b INT|Xhat|` (Thm A), the sublevel-volume reduction (Lemma 2), and
single-frequency quadratic-Bohr trapping at width `w = sqrt(kappa/eps)`,
`kappa = (ln2/2)(eta+1/b)` (Thm B), are **our #661** (`exp_ilo_fourier.md`). The
rational-resonance horn (`theta_2 = a/q => <= 2^omega(q)` residue classes, R3), the
golden-Diophantine equidistributing set, and `INT|S|^4 = 2b^2-b` are **our #663**
(`bohr_gap_volume.md`). The `(alpha, delta)` diameter map, `alpha_0`, and residual
line are **our #682** (`corridor_diameter_map.md`). The dilation invariance
`f(sV)=f(V)` and the non-dilation fence are **our #685**
(`corridor_interior_hunt.md`), a special case of **#643**'s affine invariance
Lemma A (`pte_cluster_packing_frontier.md`) and #661 Prop 3 (affine action on
`theta`). The **T2/T3 empty window** is **our #691** (`fenced_resonance_window.md`),
imported here **as corrected**: #691's printed T1 resolution ceiling (the "only if
`q <= 1/(2w)` resolves" form) is superseded -- under the common-`q` hypothesis
(`theta_2 = a/q`, `theta_1 = a'/q`, #663 Prop 5) a width-`w` trap admits up to
`(2*floor(wq)+1) * M(a,a';q)` (`M` = quadratic-congruence multiplicity; `= 2^omega(q)` for odd squarefree `q`, #700) congruence-class systems (a single system guaranteed only for
`w < 1/(2q)`), which leaves the **horn-effective** ceiling polynomial in `b`
(`O(sqrt(b))` up to `q^{o(1)}`) and preserves T3's headline (empty window, Bohr
face = box face) with corrected constants. #691's correction is **PR #700**; this note uses only the corrected qualitative
ceiling and never T1's superseded constant. **Lemma V,
Theorem AP (embedded-AP denominator bound), and the regime-disjointness
`eta <= 0.033`** are **our #692** (`fiber_denominator_tension.md`), whose P5
correction (concentration tracks embedded-run structure, not fiber magnitude) is
the seed of this packet's obstruction. The `b=18` champion
`V = {2,3,4,6,13,14,15,16,17,19,20,21,22,23,30,32,33,34}` (`f=30, L=151275`) is
**our #655** (`fiber_image_tradeoff.md`). The minimal degree-2 PTE trade support
`6` is **scottdhughes #564** (`w_a_star_pte_lemma.md`). External inputs cited
**only within printed hypotheses, never re-derived**: additive energy /
`E = INT|.|^4` (classical); inverse-Littlewood-Offord (**Tao-Vu; Nguyen-Vu**) and
its exponential-regime analogue (**Ferber-Jain-Luh-Samotij**) named as the open
magnitude object. **Lane discipline:** this packet stays entirely on the **image
face** (`f, L, Phi, theta, Delta`); it does **not** enter the signed
`(LS)/(SV*)/mu_n` object (#564). Where the *magnitude* inverse question would need
signed cancellation we record it as **transfer, not entry** (R3, R5).

---

## R0 -- the three artifacts and the composition target (AUDIT)

**The wall, verbatim (#661/#663).** #661 proved (unconditional): the atom bound
`f <= 2^b INT|Xhat|` (Thm A); `f >= 2^{(1-eta)b}` forces `vol(T_kappa) >=
2^{-eta b}/2` (Lemma 2); one `theta in T_kappa` traps all but `eps b` of the `v_i`
in one quadratic Bohr set of width `w = sqrt(kappa/eps)` (Thm B). #663 proved the
three cheap Bohr->GAP bridges impossible and localized the wall to **Diophantine
control of the dominant resonance denominator `q`**, the one horn (#663 R3/Prop 5)
that closes being the **common-`q` resonance** `theta_2 = a/q` **and**
`theta_1 = a'/q` at bounded `q`.

**Our two prior packets.** #691 proved the bounded-denominator horn **empty** on
the fenced class (**as corrected** -- see Credit): under the common-`q` hypothesis
(`theta_2 = a/q` **and** `theta_1 = a'/q`, #663 Prop 5) a width-`w` trap confines
the trapped `v` to at most `(2*floor(wq)+1) * M(a,a';q)` (`M` = quadratic-congruence multiplicity; `= 2^omega(q)` for odd squarefree `q`, #700) congruence-class systems, a single
system being guaranteed only for `w < 1/(2q)`; since #663 R3's horn needs `O(1)`
classes, the **horn-effective** denominator ceiling is polynomial in `b`
(`O(sqrt(b))` up to `q^{o(1)}` factors), while a corridor-closing residue host
needs `q >= q_cross = 2^{beta b}` (T2, exponential) -- so the horn-effective window
is empty (T3), its crossover on #682's residual line. #692 converted the
resolution half of the fiber-denominator tension into Lemma V (the 3-point
Vandermonde identity) and Theorem AP (an embedded AP of difference `t` pins
`theta_2` to the **bounded** denominator `2t^2`), then showed the mechanism bites
only for `eta <= 0.033`, where #668's envelope already gives `phi+lambda <= 1.18
< 4/3` -- **disjoint** from the wall regime.

**The third artifact (#696).** #696 proves a **per-instance energy-boosted atom
bound**: for a realized image on a fixed-weight Boolean slice, `fL` is controlled
by the max fiber's **own** additive energy `Delta(F)`. This is orthogonal to the
atom bound `f <= 2^b INT|Xhat|` that #691/#692 use, and it is an **upper** bound on
`fL` in terms of `Delta`, so on the wall it produces a **lower** bound on
`Delta(F)`. The composition target: does a high-energy lower bound, intersected
with the two dead denominator levers, force `q` into range?

**The quantifier caution.** The known failure mode on this face is a
quantifier-order mismatch (per-instance vs uniform, #661 R5 / #692 PI note (b)).
#696's `Delta` bound is **per-instance** (the specific max fiber's energy); #691's
window emptiness and #692's regime-disjointness are **uniform** over the fenced
class. We work the quantifiers explicitly in R2--R3.

---

## R1 -- #696's theorem, stated precisely (goal-ladder step 1; AUDIT, verifier PASS)

We restate #696 in the program's coordinates (`N = b`), quoting only within its
printed hypotheses.

> **Theorem (#696, realized-image energy lift).** Let `Omega_m = {x in {0,1}^b :
> |x| = m}`, `Phi : Z^b -> G` a homomorphism to a finite abelian group, `S_m =
> Phi(Omega_m)`, `L = |S_m|`. Fix `s in S_m` and `F subseteq Omega_m ∩
> Phi^{-1}(s)`, `f = |F| > 0`; write `E(F) = |{(a,b,c,d) in F^4 : a+b = c+d in
> Z^b}|`, `Delta(F) = E(F)/f^3 in [1/f, 1]`, `theta = m/b`. With
> `A(N,m) = [z^{2m}](1+z+z^2)^N`, `B(N,m) = [z^{3m}](1+z+z^2+z^3)^N`,
> `a(theta) = 1 + h2(theta)/2`, and `g(theta) = H_2((1-theta)^2/2, (1-theta^2)/2,
> theta(2-theta)/2, theta^2/2)`:
> ```
>     fL <= A(N,m),                 fL <= B(N,m) Delta(F),
>     fL <= 2^{b a(theta)},         fL <= 2^{b g(theta)} Delta(F).      (1)-(4)
> ```
> The entropy bounds (3)-(4) hold with `L` the full image of the
> **cardinality-augmented map** `x -> (|x|, Phi(x))`, `F` one augmented fiber.

**Identification with the program (PROVED).** Take `Phi(x) = (sum_i x_i v_i, sum_i
x_i v_i^2)`. Then the cardinality-augmented map `x -> (|x|, Phi(x))` is **exactly**
the degree-2 signature `Phi(S) = (|S|, sum_S v, sum_S v^2)`, so `#696`'s
augmented image size is the program's `L` and one augmented fiber at the extremal
cardinality is the program's max fiber, `f = f*`. Thus (3)-(4) read, for the wall
quantity `X = (fL)^{1/b}`:
```
    X <= 2^{a(theta)},      X <= 2^{g(theta)} Delta(F)^{1/b}.
```

**Fenced-wall consequence (PROVED, #696 (6)-(8); verifier BLOCK 0/1).** If the wall
holds, `X > 2^{4/3}`, then (3) forces `a(theta) > 4/3`, i.e. `h2(theta) > 2/3`, so
```
    theta in (0.173952331409, 0.826048...).                              (density band)
```
And (4) forces `Delta(F) > 2^{-b(g(theta)-4/3)}`; since `g` is maximized at
`g(1/2) = 3 - (3/4) log2 3 = 1.811278124459`,
```
    -log2 Delta(F)/b  <  g(1/2) - 4/3  =  0.477944791126        (= 0.331286084432 in ln).
```
The complementary lower edge uses the sharp Boolean-cube energy bound
`E(F) <= f^{log2 6}` (so `Delta(F) <= f^{-(3-log2 6)}`), `L <= 2^b`, and the wall
floor `phi > 1/3`: since `(3 - log2 6) ln2 = ln(4/3)` exactly,
```
    -log2 Delta(F)/b  >  ln(4/3)/(3 ln2)  =  0.138345833093        (= ln(4/3)/3 in ln).
```
Hence, **conditional on the wall**, the fiber energy sits in the two-sided band
```
    2^{-0.4779 b}  <  Delta(F)  <  2^{-0.1383 b}.                        (energy band)
```
The band is **nonempty** (`0.1383 < 0.4779`): #696 alone does **not** contradict
the wall -- it constrains it. Verifier BLOCK 0 recomputes every constant (including
the exact identity `(3 - log2 6) ln2 = ln(4/3)` and the density thresholds
`h2^{-1}(2/3) = 0.173952`, `g^{-1}(4/3) = 0.078609`); BLOCK 1 confirms (1)-(4) hold
on four exact blocks and pins the enumerations `champ18 (f,L,m*,E) =
(30,151275,9,2898)`, `unionAP16 = (20,25619,8,900)`.

**#696's verifier (AUDIT).** `verify_realized_image_energy_lift.py` (stdlib-only)
runs `76,231` exact theorem checks over exhaustive small cyclic syndrome maps plus
the constants and a strengthened-`Delta` tamper, and **passes** -- confirmed before
building on it.

---

## R2 -- the composition, quantified: #696 adds orthogonal coordinates (PROVED)

#696 contributes two **new** constraints on a wall block: a **density** window on
`theta = m*/b` and an **energy** window on `Delta(F)`. Neither is a constraint on
the resonance denominator `q`, and neither moves #691/#692's window.

> **Proposition 1 (orthogonality).** #696's wall constraints live in the
> coordinates `(theta, Delta)`; #691's empty window and #692's regime boundary live
> in `(b, eta, delta, alpha, q)`. The two coordinate sets are disjoint, and
> #691/#692's endpoints are **independent of `(theta, Delta)`**:
> ```
>     Q_horn = O(sqrt(b)) up to q^{o(1)}    (horn-effective ceiling, #691 corrected),
>     q_cross = 2^{beta b},   beta = delta - alpha/3 - 1/9,
>     #692 biting threshold   eta <= 0.033,
> ```
> all functions of `(b, eta, delta, alpha)` only. Hence `#696 ∩ #691 ∩ #692` is the
> **product** `{theta in density band} × {Delta in energy band} × {(delta, alpha,
> eta) fenced} × {q free}`.

*Proof.* The horn-effective ceiling comes from the corrected common-`q` class count
`(2*floor(wq)+1) * M(a,a';q)` (`M` = quadratic-congruence multiplicity; `= 2^omega(q)` for odd squarefree `q`, #700) with trap width `w = sqrt(kappa/eps)`, `kappa =
(ln2/2)(eta+1/b)` (#691 as corrected): `O(1)` classes force `q = O(1/w) =
O(sqrt(b))` up to `q^{o(1)}` -- a function of `(b, eta, eps)` only, with no `theta`
or `Delta`. `q_cross = 2^{beta b}`, `beta = delta-alpha/3-1/9` (#691 T2) -- no
`theta` or `Delta`. #692's biting threshold solves `4 b sqrt(kappa)/(b-2) < 1/2` at
`b = 100`, giving `eta <= 0.033` -- no `theta` or `Delta`. #696's band constrains
only `theta` and `Delta`. The constraint sets therefore cut disjoint coordinates;
their intersection is the Cartesian product, and the `q`-fiber over any point of it
is the entire admissible `q`-range left open by #691/#692. ∎ (Verifier BLOCK 5
recomputes the class-count ceiling and confirms every endpoint carries no
`(theta, Delta)` dependence.)

**What closure would require.** To turn the product into a pincer we would need a
**bridge** `Delta(F) in energy band => q controlled`. The only proven `q`-controls
are #663 R3/Prop 5 (which *assumes* the common-`q` resonance `theta_2 = a/q`,
`theta_1 = a'/q` at bounded `q`) and #692 Theorem AP (`embedded AP of difference
t => q | 2t^2`). So the bridge would have to read: *high fiber energy `Delta(F)`
forces a positive-density embedded AP in `V`* (which supplies both the bounded `q`
and the common-`q` alignment). R3 shows this bridge is **false**.

---

## R3 -- the obstruction: source-energy / image-denominator face mismatch (PROVED)

The bridge fails because `Delta(F)` and `q` are computed from **disjoint data**:
`Delta(F) = E(F)/f^3` reads only the max fiber `F subseteq {0,1}^b` as a set of
Boolean vectors (the count of `a+b=c+d` in `Z^b`), with no reference to the values
`v_i`; the denominator `q` reads only the moment values `u_i = (1, v_i, v_i^2)`,
with the fiber entering only through its size `f`. Three pillars make this exact.

### P1 -- Delta is affine-invariant; the denominator is not (EXACT, BLOCK 2)

> **Lemma 2 (affine-blindness).** The integer affine action `v -> a v + c`
> (`a != 0`) fixes the fiber partition, hence `F` (as a set of masks), `E(F)`, `f`,
> and `Delta(F)` **exactly**; but it acts on the resonance frequency by
> `theta_2 -> a^2 theta_2` (#661 Prop 3, `M = [[1,0,0],[c,a,0],[c^2,2ac,a^2]]`),
> sending a resonance of denominator `q` to one of denominator `q/gcd(q, a^2)`.
> Therefore one value of `Delta(F)` corresponds to a whole affine **orbit** of
> denominators: `Delta` cannot determine `q`.

*Proof.* Under `v -> av+c` the signature `(|S|, s1, s2)` transforms by the
invertible affine map `(m, s1, s2) -> (m, a s1 + cm, a^2 s2 + 2ac s1 + c^2 m)`, a
bijection on signatures, so every fiber -- in particular the max fiber `F` -- is
preserved as a **set of masks** (#643 Lemma A, #685). `E(F) = |{a+b=c+d in Z^b}|`
depends only on those masks, so `E, f, Delta` are unchanged. The frequency claim is
#661 Prop 3. ∎ Verifier BLOCK 2 dilates `unionAP16` by `a = 1, 2, 3` **without
renormalizing**: the max-fiber mask set, `E = 900`, `f = 20`, and `Delta = 0.11250`
are byte-identical across all three, while the raw resonance
`theta_2 = (2/3)/a^2` reduces to denominators `{3, 6, 27}` -- three distinct `q`
at one fixed `Delta`.

(Normalization to `gcd = 1` gauge-fixes the *dilation* subgroup, but Lemma 2 is the
structural statement that `Delta` factors through the affine quotient while `q`
does not -- `Delta` is a strictly coarser invariant. P2 confirms the
non-functionality survives on gauge-fixed representatives.)

### P2 -- equal (theta, Delta), incompatible q, on normalized blocks (MEASURED, BLOCK 3)

> **Proposition 3 (non-functionality).** There are gcd=1 blocks with identical
> `theta` and `Delta` agreeing to `4.6%` whose dominant resonances sit at
> incompatible denominators.

Verifier BLOCK 3 exhibits the pair (exact `f, L, E`; `|Xhat|`-marginal by fixed
midpoint quadrature, MEASURED):
```
    block       b   f      L     m*  theta  Delta    dominant resonance
    unionAP16  16  20   25619    8   0.500  0.1125   theta_2 = 2/3   (q = 3, small)
    champ18    18  30  151275    9   0.500  0.1073   theta_2 ~ 0.679 (no small q)
```
Both share `theta = 1/2`; `|Delta_champ - Delta_union|/Delta = 0.046`. Yet:
`unionAP16` (two APs of difference `3`, embedded AP length `8`) has its dominant
non-parity peak **exactly** at `2/3` -- the bounded denominator `q = 3` forced by
its own AP (#692 Theorem AP, `2t^2 = 18`, and `2/3 = 12/18`); its small-`q`-to-
global peak ratio is `1.00`. `champ18` (a #655 PTE-trade block, AP-free) has its
dominant peak at `theta_2 ~ 0.679`, **more than `0.012` from every rational of
denominator `<= 5`**, and its small-`q` peaks reach only `0.75` of the global peak.
So `(theta, Delta)` -- #696's entire wall data -- does **not** determine `q`; the
denominator tracks the block's embedded-run **structure** (#692's corrected P5),
which `Delta` does not see.

### P3 -- the resonance subtorus is Lebesgue-null in the energy integral (EXACT, BLOCK 4)

> **Proposition 4 (measure-zero blindness).** `Delta(F) = E(F)/f^3` with
> `E(F) = INT_{[0,1)^b} |Fhat(xi)|^4 dxi` (source `b`-torus). The resonance
> frequencies where #663's denominator wall lives are
> `{psi(theta) : theta in [0,1)^3}`, the image of the homomorphism
> `theta -> (theta_0 + theta_1 v_i + theta_2 v_i^2)_i`, a `3`-dimensional subtorus
> of `[0,1)^b`. For `b > 3` with distinct `v_i` this subtorus is **Lebesgue-null**,
> so it contributes **zero** to `E(F)`. Hence `Delta(F)` carries no information
> about the resonance denominator.

*Proof.* `E(F) = INT |Fhat|^4` is the standard additive-energy identity. The map
`theta -> psi(theta)` is linear with matrix `[1, v_i, v_i^2]_{i,col}` of rank `3`
(Vandermonde, distinct `v_i`), so its image is a `3`-torus, of measure `0` in
`[0,1)^b` when `b > 3`. ∎ Verifier BLOCK 4 certifies rank `= 3 < b` for all four
blocks. This is the **why** behind P1--P2: the energy integral and the resonance
support are carried on complementary-dimension pieces of Fourier space; no
per-instance energy bound can transmit force to the denominator.

**Reading.** #696's `Delta` bound is a genuine, sharp fact about the **source**
Boolean fiber. The resonance denominator is an **image** moment-Fourier datum. The
two are not merely "different" -- they are provably decoupled (P3), affinely
decoupled (P1), and empirically decoupled on normalized blocks (P2). The pincer
does not close; the obstruction is a **source/image face mismatch**, the
per-instance-vs-uniform failure mode named in advance, here made exact.

---

## R4 -- what DOES compose: the two-band wall localization (PROVED, the positive residue)

The composition is not sterile. #696 legitimately **shrinks the wall's habitat**,
in coordinates that compose cleanly with #682/#691's denominator geography because
they are orthogonal to it.

> **Theorem 5 (energy+density localization).** Every wall block (`X > 2^{4/3}`)
> satisfies, simultaneously and independently of its `(delta, alpha)` position:
> ```
>     theta = m*/b in (0.1740, 0.8260)                        (density, #696 (3))
>     -log2 Delta(F)/b in (0.1383, 0.4779)                    (energy,  #696 (4),(8))
> ```
> in addition to the fenced-class facts `delta > alpha/3 + 1/9` (#682 Cor 2), the
> horn-effective denominator window empty (#691 T3, as corrected), and the
> resolution mechanism confined to `eta <= 0.033` (#692). The wall's habitat is
> thus pinned to a **bounded box in
> `(theta, -log2 Delta/b)`** cross the fenced `(alpha, delta)` wedge cross a free
> denominator coordinate.

This is the honest deliverable: #696 does not pay the denominator wall, but it
**localizes** the wall to intermediate density and a definite energy band -- a
constraint no prior packet supplied, and one that any future closing argument may
assume for free. In particular a wall block is **neither Sidon-like**
(`Delta -> 1/f`, excluded by the lower edge) **nor a full coset/subgroup**
(`Delta -> 1`, excluded by the upper edge): its fiber has **intermediate** additive
energy. Locating a large fiber of exactly this intermediate energy, at intermediate
density, that is **AP-free at moderate `eta`** (so that #692 Theorem AP does not
pin it into #663 R3's closable horn) is the residual -- unchanged in substance from
#663/#691/#692, now with the energy band attached.

---

## R5 -- verdict, and the wall named precisely

```
    TARGET: force the dominant resonance denominator q into range on some window,
        via #696 (energy) ∩ #691 (empty denom window) ∩ #692 (AP-resolution).

    STEP 1  #696 RESTATED + VERIFIED (AUDIT):  fL <= 2^{b g(theta)} Delta(F);
        wall => theta in (0.174,0.826) AND 2^{-0.4779 b} < Delta(F) < 2^{-0.1383 b}.
        #696 verifier PASS (76,231 checks).
    STEP 2  COMPOSITION (PROVED negative):  #696's band is in (theta, Delta),
        orthogonal to (delta, alpha, eta, q); intersection is a PRODUCT, q free.
    OBSTRUCTION (PROVED, 3 pillars):
        P1 (EXACT)    Delta affine-invariant; dilation moves q through {3,6,27}.
        P2 (MEASURED) equal (theta,Delta): champ18 (spread, no small q) vs
                      unionAP16 (q=3) -- Delta does not determine q.
        P3 (EXACT)    resonance subtorus is 3-dim, Lebesgue-null in E(F)=INT|Fhat|^4.
    POSITIVE RESIDUE (PROVED):  Theorem 5 -- wall confined to density (0.174,0.826)
        and energy deficit (0.1383,0.4779): a new two-band habitat-shrink.
    VERDICT: DECIDED-NEGATIVE for the denominator wall; obstruction = source-energy
        / image-denominator FACE MISMATCH (per-instance bound, denominator-blind).
```

**The wall, after this packet.** #663 left the wall as "Diophantine control of
`q`." #691 killed the bounded-`q` horn on the fence; #692 confined the
resolution-tension mechanism off the wall. #696 adds a per-instance **energy**
constraint -- and we prove it **cannot** be the missing denominator control,
because energy is a source-Boolean invariant blind (P1--P3) to the image resonance.
What #696 **does** contribute is a genuine localization (Theorem 5): the wall lives
at intermediate density and intermediate fiber energy. Combined with #661
(spectral shortcuts impossible), #663 (three bridges impossible), #682/#685
(geography, dilation excluded), #691 (bounded-`q` window empty), and #692
(resolution tension off-wall), the residual is unchanged in kind -- the
exponential-regime magnitude inverse-Littlewood-Offord -- but now boxed into an
explicit energy+density region, and one more candidate lever (per-instance fiber
energy) is proved denominator-blind with the exact reason recorded.

---

## Nonclaims

- **Not a wall closure.** #696 ∩ #691 ∩ #692 does **not** force `q` into range on
  any window; no pincer closes. The result is decided-**negative** for that goal.
- **Not a proof the wall class is empty.** #696's band is nonempty and
  self-consistent; nothing here contradicts the existence of a wall block. Theorem
  5 localizes, it does not exclude.
- **No wall block exhibited.** All four blocks are **off** the wall
  (`X in [2.0, 2.343] < 2^{4/3}`, the standing small-`b` plateau of #646/#661);
  the composition is analyzed structurally, not witnessed at a wall instance. The
  `|Xhat|` marginals (P2) are midpoint quadrature at `b <= 18`, used only to read
  which denominator a peak sits at (MEASURED); the `b -> inf` behaviour where the
  wall lives is beyond enumeration.
- **P2 is measured, not proved.** The equal-`(theta,Delta)` non-functionality of
  `q` is exact in `(f, L, E, Delta)` and read off the fixed-grid quadrature for the
  peak locations; it corroborates the exact pillars P1, P3, which carry the
  obstruction.
- **The lower energy edge is conditional.** `-log2 Delta/b > 0.1383` uses the wall
  floor `phi > 1/3` (from `lambda <= 1` on the wall) together with `E(F) <=
  f^{log2 6}`; off the wall it may fail (e.g. `holes14` has `0.122 < 0.1383`), as
  it should.
- **No signed object entered.** The magnitude inverse-LO / "large fiber of
  intermediate energy without an embedded AP at moderate `eta`" is recorded as
  transfer, not entry (it would need the signed `mu_n` object of #564). It remains
  **OPEN**.
- **No `.tex`/`.pdf` touched.** No `Lxxxx` anchor is introduced; the frontiers
  manuscript is unchanged. All content is self-contained in this note and its
  verifier.

---

## Files, labels, PI re-derivation

- Note: `experimental/notes/thresholds/fenced_energy_pincer.md` (this).
- Verifier: `experimental/scripts/verify_fenced_energy_pincer.py`
  (`RESULT: PASS 82/82`, ~3.5 s / <60 MB; recomputes #696's band and density
  constants, its four inequalities on four exact blocks, the affine-blindness
  byte-for-byte, the equal-`(theta,Delta)` non-functionality of `q`, the
  resonance-subtorus rank `= 3`, and the `(theta,Delta)`-independence of #691/#692's
  endpoints; `--tamper-selftest` mutates four witnesses, 4/4 detected).
- Read-only inputs: **DannyExperiments #696** `realized_image_energy_lift.md` and
  its verifier; **DannyExperiments #668** `canonical_transversal_vc_compression.md`;
  our **#661** `exp_ilo_fourier.md`, **#663** `bohr_gap_volume.md`, **#682**
  `corridor_diameter_map.md`, **#685** `corridor_interior_hunt.md`, **#691**
  `fenced_resonance_window.md`, **#692** `fiber_denominator_tension.md`, **#655**
  `fiber_image_tradeoff.md`, **#643** `pte_cluster_packing_frontier.md`; hughes
  **#564** `w_a_star_pte_lemma.md`.

**Per-claim status.** #696's restatement + fenced-wall band = **AUDIT** (quoted
within its printed hypotheses; its verifier re-run, PASS). Proposition 1
(orthogonality), Lemma 2 (affine-blindness), Proposition 4 (measure-zero
blindness), and Theorem 5 (energy+density localization) = **PROVED** (elementary;
P1/P4 exact integer/linear-algebra facts). Proposition 3 (equal-`(theta,Delta)`
non-functionality) = **MEASURED** (exact `f,L,E`; peak location by fixed midpoint
quadrature). The composed-pincer denominator control = **REFUTED** as a closing
route (the source/image face mismatch, obstruction exhibited). The
exponential-regime magnitude inverse-LO / intermediate-energy AP-free wall block =
**OPEN**.

**Flagged for PI (least-certain, 4 points).**
(0) **#691 is imported as corrected.** This packet uses only the *qualitative*
horn-effective ceiling (polynomial in `b`, `(theta,Delta)`-free) under the
common-`q` hypothesis, never #691's superseded printed T1 constant; Proposition 1
(the only place #691 enters) is robust to the exact ceiling value. #691's
correction is **PR #700** (all "#691 as corrected" citations point there).
(a) **P2's peak locations are `b <= 18` quadrature.** The *pair's* equal
`(theta, Delta)` and the small-`b` peak denominators (`q = 3` vs spread) are exact
and deterministic, but the small-`b` plateau (#646/#661) means the champion's
resonance is not yet in its asymptotic regime; the load of the obstruction rests on
the exact pillars P1 (affine) and P3 (measure-zero), which are `b`-uniform.
(b) **The lower energy edge uses `E(F) <= f^{log2 6}` and `phi > 1/3`.** The upper
edge `0.4779` is #696's direct `g(1/2)-4/3`; the lower edge `0.1383` inherits
#696's use of the sharp Boolean-cube energy bound and the wall floor. Both are
quoted, not re-derived; the band's *nonemptiness* (the only thing R4 needs) is
robust to the exact edges.
(c) **Theorem 5 is a localization, not an exclusion.** It shrinks the wall's
habitat but does not prove the habitat empty; a future closing argument may assume
the two bands for free, but must still supply the intermediate-energy AP-free wall
block or its impossibility.

**Exact vs heuristic.** All `f, L, m*, E, Delta, theta`, the affine-blindness, the
subtorus rank, #696's four inequalities, and every band/density constant are exact
integer / closed-form computation. Proposition 1's endpoint independence and the
band nonemptiness are closed-form. The `|Xhat|` peak locations (P2) are midpoint
quadrature used only to read which denominator a peak occupies. #696 and the
exponential-regime inverse-LO are cited within their (audited / open) scope and
never re-derived. No signed `mu_n` object entered. No `.tex`/`.pdf` touched.
