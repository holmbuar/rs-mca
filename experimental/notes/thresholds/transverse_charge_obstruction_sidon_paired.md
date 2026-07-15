# Transverse pieces cannot carry the failure charge and no fiber can pay it: the semantic-or-signed decomposition is unrealizable on the Sidon-paired class at q=2, so the sixth (packet-scale) alternative is forced

## Status

```text
Status: PROVED (Prop 1, chart-free) that on EVERY colliding chart (M >= L), for
        EVERY band failure at q=2, the total charge assignable to
        bounded-multiplicity ("transverse") pieces is <= e^{-eta N + o(N)}
        Omega_+ -- compatibility itself caps a transverse piece's charge at
        ||P_A b||_2, and Cauchy-Schwarz over e^{o(N)} pieces cannot reach
        Omega_+.  The (NFB) transverse branch (#760 Sec 7) is CLOSED NEGATIVE:
        transverse partitions exist and are clause-honest, but they are
        charge-trivial; Prop 6.1's semantic obligation is partition-invariant.
      + PROVED (Thm 2, Sidon-paired) the fiber-rooted semantic cap: at the
        canonical q=2 rooting of ANY failing band A, every owner weight obeys
        omega(sigma) <= sqrt(delta_A), so a semantic piece rooted in one fiber
        carries charge <= f_max sqrt(delta_A), and e^{o(N)} of them carry
        <= e^{-(eta + kappa)N + o(N)} Omega_+ with kappa = ln(2/sqrt 3)/2 > 0
        per N-unit.  Uniform over ALL failing bands.
      + PROVED (Thm 3, assembly) that NO charge-preserving decomposition into
        e^{o(N)} pieces, each five-precursor-semantic (hypothesis (FR): the
        grammar's precursors are fiber-rooted) or signed-clause-compliant,
        attains sum c_i = Omega_+ on the Sidon-paired class at q=2:
        signed side <= e^{-eta N} Omega_+ (the clause), semantic side
        <= e^{-(eta+kappa)N} Omega_+ (Thm 2).  The five-precursor dichotomy is
        UNREALIZABLE on this class; avdeevvadim's OWN proposed sixth
        alternative (#716 Sec 7.1) is upgraded from optional to FORCED, and it
        must be packet-scale (non-fiber-rooted).
      + PROVED (Thm 4) the direct branch of (NFB) fails too: the packet's band
        excess obeys R_q(f) >= L^{1/2}||h restricted to the image||_2 / M for
        EVERY q >= 2 (occupied-support transfer, base-free), which is
        e^{eta N} with eta -> (1/4) ln(9/8) per N-unit; the moderately-unpaired
        slice s in [B/4, 3B/4] has the same exponential excess.  Exact
        rationals to B = 32, both bases.  No direct PO4/signed payment exists
        at ANY moment order, not only q <= q_+ = 4.199.
      + PROVED the payment-gap window: every fiber lies in [2M/L, M/sqrt L):
        heavy enough that point-mass band failures exist (#739 / #716
        Cor 1.2), too light for any single fiber to carry a q=2 failure's
        charge -- f_max sqrt(L) / M = (sqrt 3 / 2)^B -> 0.  "Heavy enough to
        fail, too light to pay" is the class mechanism in one line.
      + EXPERIMENTAL (Sec 6, structure of the survivor) with a PROVED identity:
        hat f(j) = [z^B] prod_i (1 + z^2 + 2 z cos(2 pi j A_i / c)) (exact
        per-pair factorization), and the exact antipodal congruence
        (c-1)/2 * A_i == (c - A_i)/2 (mod c), so the half-frequency
        j* = (c-1)/2 aligns every factor toward (1-z)^2 and resonates at
        |hat f(j*)| >= 0.70 M (base 3, finite-verified through B = 64;
        0.61 M base 5 at B = 6).  The resonant spectrum is the digit-sparse
        frequencies; census #{|hat f| >= M/10} = 42 (B=6), 58 (B=8) on base 3.
        Any sixth-alternative conversion must consume exactly these
        correlations (#716 Sec 5.6's Bohr wall, now with a minimal explicit
        instance).
LANE: hard input 2 ("image-scale MI + MA, or a direct Sidon payment",
        agents.md L47) -- the (NFB) object (quoted verbatim in Sec 0 below;
        stated in the companion packet PR #760, OPEN, not yet integrated),
        BOTH branches now decided negative on the Sidon-paired class.  Input-2 residual after
        this packet: (i) a packet-scale (non-fiber-rooted) semantic conversion
        -- the forced sixth alternative -- with Sec 6's resonant spectrum as
        its first mandatory instance; or (ii) exclusion of the class from the
        first-match atlas (atlas-totality lane, Codex-owned); plus (iii) the
        unchanged large-q Sidon residual of #729 Sec 3.3.  Fence (N1)
        (thm:aperiodic-one-ray-saturation) respected throughout: nothing here
        pays or claims lower reserve via emission.
```

Label key (agents.md dialect): **PROVED** / **CONDITIONAL** / **CONJECTURAL** /
**EXPERIMENTAL** / **AUDIT** / **COUNTEREXAMPLE**.  Every combinatorial and
rational claim below is recomputed exactly (`int`/`Fraction`) by
`experimental/scripts/verify_transverse_charge_obstruction.py` (stdlib only,
deterministic, `RESULT: PASS (281/281)`, `--tamper-selftest` catches `4/4`,
~1.3 s); the resonance section uses floats guarded by an exact Parseval
identity (machine sum matches the exact `M2` to relative `1e-6`).
Machine-readable certificate:
`experimental/data/certificates/transverse-charge-obstruction/transverse_charge_obstruction.json`.
Lean statement stub (decidable `native_decide` facts, no `sorry`, no mathlib):
`experimental/lean/transverse_charge_obstruction/` (`lake build` succeeds).
No `.tex`/`.pdf` is edited.

## Interfaces

Paper labels (`experimental/rs_mca_thresholds.tex`,
`experimental/asymptotic_rs_mca_frontiers.tex`, base commit `c35a6da`; read,
none edited):
- **`prop:partial-occupancy-fourier` (PO3/PO4)** and **`rem` PO5**: the
  character-sum object and the realized-image normalization.  Theorem 4 decides
  the PO4 flatness question negatively for this class at every moment order;
  Sec 6's product formula is the PO3 coefficient-extraction specialized to the
  Sidon-paired chart.
- **`thm:aperiodic-one-ray-saturation` (SAT1)**: fence (N1); no rung here
  converts emission into reserve.
- The three proved barriers (`prop:pairwise-overlap-limit`,
  `drc:prop-recurrence-nonadditive`, `prop:no-growing-prime-density`): none
  re-attempted.

Integrated in-tree packets (consumed and credited, not reproved):
- **avdeevvadim's #716**
  (`experimental/notes/audits/primitive_signed_payment_barrier_v1.md`): the
  entire target frame is his -- the charge-preserving semantic-or-signed
  dichotomy (Sec 6), its four charge conditions, Prop 6.1, the point-mass
  reduction (Secs 1-2) that this packet's hypothesis (FR) formalizes, the
  Bohr-route warning (Sec 5.6) that Sec 6 here instantiates, and -- explicitly
  -- the **Sec 7.1 anticipation that a "sixth signed Sidon/minor alternative"
  might be needed**.  This packet proves that anticipation NECESSARY on an
  explicit class.  Nothing here contradicts #716; it decides which of his two
  offered forms survives.
- **Companion packet #760 (OPEN PR, `nonfiber_decomposition_realized_scale.md`
  on its own branch -- NOT yet integrated; every use here is self-contained or
  CONDITIONAL-on-open-PR):** it states the (NFB) open object this packet
  closes; that statement is quoted verbatim in Sec 0 so this note stands alone
  at main.  The one fact this packet's taxonomy leans on from its rung (c) --
  the coset homogeneity census (zero single-unpaired-level mass below
  `3^{B-2}` classes) -- is REPRODUCED inside this packet's own verifier (V7),
  so no result here depends on #760's integration; the framing link ("closes
  #760 Sec 7") is the only conditional part.
- **#739** (`staircase_concentration_sidon_paired.md`): the class itself, with
  **DannyExperiments' #749-corrected hypotheses** (2-superincreasing hence
  B[+-2]-dissociated `P`, center bound `c > 2 sum P`) -- this packet consumes
  only the corrected statements; the exact staircase (fiber `C(B-s,(B-s)/2)`,
  `C(B,s) 2^s` syndromes, `L = (3^B+1)/2`, `M = C(2B,B)`) is Theorem 1 there
  and is re-verified by brute force here (V1).
- **#729** (`general_pruned_signed_bound.md`): Theorem I / Theorem D and the
  layer-cake give the general-q corollary of Prop 1; its Sec 3.3 fixes q=2 as
  the dichotomy's natural operating point (the scope of Thm 2/3); its Sec 3.2
  "third kind" obligation is decided UNMEETABLE within (FR) on this class; its
  large-q Sidon residual is untouched.
- **#732** (`charge_preserving_split_decomposition.md`): Theorem A
  (partition-agnostic freeness of the charge conditions) is why the obstruction
  proved here is NOT about the charge conditions -- it is about carrying
  capacity under compatibility, a different inequality.
- **#735** (`heavy_fiber_planted_emission.md`): the five-precursor grammar
  whose fiber-rootedness is hypothesis (FR); its corrected Thm 2a central fiber
  is the `s=0` cell realizing the max root-cell charge (V3).
- **#728** (`first_match_signed_gain.md`): its unpruned-growth threshold
  `q = 2.709` reappears here exactly as the moment order where the single
  top-fiber term alone turns exponential (V2, point-mass rate sign flip) -- an
  independent cross-check of both packets' constants.
- **#717** (`heavy_fiber_admissibility_transfer.md`): the complete-band count
  `K_N = 2 + ceil(log2 N)` (used only to note that band pigeonholes cost
  polynomial factors, absorbed in `e^{o(N)}`).
- **Codex atlas-totality lane** (in progress, theirs): if the first-match atlas
  is proved to contain no admissible chart beyond the locator-prefix family,
  the "exclude the class" escape (residual route ii) closes and only the sixth
  alternative remains.  CONDITIONAL interface; no result of that lane is
  assumed here.

---

## 0. Setup and conventions

**The object being closed** (verbatim from the companion packet's Sec 7, so
this note is self-contained at main):

> **(NFB)** Whether the moderately-unpaired fibers (`s = Theta(B)`) of the
> Sidon-paired chart can be discharged by a partition **transverse to every
> prefix-quotient fiber** (a non-`q_H o Phi` split), or paid **without any
> semantic decomposition** by the #729 signed clause / `prop:partial-occupancy-
> fourier` (PO4) nontrivial-character bound at `q <= q_+ = 4.199`.

Prop 1 + Theorems 2-3 decide the first branch negatively (transverse pieces
cannot carry the charge, and nothing else can either); Theorem 4 decides the
second (the excess is exponential at every moment order, slice included).

Fix the Sidon-paired class in the #749-corrected form: `P = {A_1, ..., A_B}`
2-superincreasing (`A_i > 2 sum_{j<i} A_j`, hence B[+-2]-dissociated),
`c = 2 sum P + 1 > 2 sum P`, `T = P u (c - P)`, `|T| = N = 2B`, `a = B`,
`Phi(S) = sum_{t in S} t`.  The `(k, D) <-> eps` bijection (#739 Sec 1) makes
the over-`Z` chart and the mod-`c` chart the same set partition, so we work on
`G = Z_c` (the PO5 realized-image group; `H = |G| = c`).  Scalars:

```text
L = (3^B + 1)/2,   M = C(2B, B),   f_max = C(B, B/2),
M2 = sum_{s == B (2)} C(B,s) 2^s C(B-s, (B-s)/2)^2
   = [z^B w^B] (2zw + (1+z^2)(1+w^2))^B          (V1, exact; ~ 6^B / poly).
```

`f(sigma) = |Phi^{-1}(sigma)|` is the packet's count mask.  For a symmetric
band `A subseteq hat G \ {0}` write `h = h_A = P_A f` (real), `delta_A = |A|/c`.
The **canonical q=2 rooting** of a failing band (#716 Sec 2 at `q = 2`, where
the norming dual `g = h/||h||_2` is itself `A`-band-limited, so `P_A g = g`)
assigns owner weights

```text
omega(S) = omega(Phi(S)) = h(Phi(S))_+ / ||h||_2,        (syndrome function)
Omega_+  = sum_S omega(S) = sum_sigma f(sigma) h(sigma)_+ / ||h||_2
        >= <f, h> / ||h||_2 = ||h||_2 ,
```

and a **failure** at `A` means `R_A(f) = (L^{1/2}/M) ||h||_2 >= e^{eta N}`,
i.e. `||h||_2 >= e^{eta N} M / L^{1/2}`.  A decomposition piece is
`(B_i, U_i, c_i)` with the #716 Sec-6 conditions; its mask is
`b_{U_i}(sigma) = sum_{S in U_i, Phi(S) = sigma} omega(S)`; its per-syndrome
support multiplicity is `W_i(sigma) = #{S in U_i : Phi(S) = sigma}`.

Two elementary facts used repeatedly (both from Cauchy-Schwarz + Parseval,
proved inline below): for any symmetric band `A` and any `sigma`,

```text
(CS-K)   |h_A(sigma)| <= sqrt(delta_A) ||h_A||_2 ,
(CS-P)   c_i <= ||P_{B_i} b_{U_i}||_2 <= ||b_{U_i}||_2          (compatibility
         + orthogonal projection),
```

(CS-K): `h_A(sigma) = (1/c) sum_{xi in A} hat f(xi) xi(sigma)`, so
`|h_A(sigma)|^2 <= (|A|/c) * (1/c) sum_{xi in A} |hat f(xi)|^2
= delta_A ||h_A||_2^2`.

---

## 1. Proposition 1 (chart-free): transverse pieces are charge-trivial

> **Proposition 1.** Let `Phi` be ANY chart with `M` supports and image size
> `L <= M`, let `A` be any symmetric failing band at `q = 2`
> (`||h||_2 >= e^{eta N} M/L^{1/2}`, `eta > 0`) with its canonical rooting, and
> let `{U_i}_{i <= K}` be disjoint pieces whose multiplicities satisfy
> `W_i(sigma) <= W` for all `i, sigma`.  Then every compatible charge
> assignment obeys
> ```text
> sum_i c_i  <=  sqrt(K W M)  <=  e^{-eta N + o(N)} Omega_+
> whenever K, W = e^{o(N)}.
> ```

**Proof.** `omega <= sqrt(delta_A) <= 1` pointwise by (CS-K) (with
`||h||_2` cancelling), so `b_{U_i}(sigma) <= W_i(sigma)` and
`||b_{U_i}||_2^2 <= sum_sigma W_i(sigma)^2 <= W sum_sigma W_i(sigma)
= W |U_i|`.  By (CS-P) and Cauchy-Schwarz over the pieces,
`sum_i c_i <= sum_i ||b_{U_i}||_2 <= sqrt(K sum_i ||b_{U_i}||_2^2)
<= sqrt(K W M)` since `sum_i |U_i| <= M`.  Meanwhile
`Omega_+ >= ||h||_2 >= e^{eta N} M / L^{1/2} >= e^{eta N} sqrt(M)` because
`M >= L`.  Divide. `square`

Three remarks.  (i) The bound is an UNSATISFIABILITY statement: for an
all-transverse partition, charge preservation `sum c_i = Omega_+` and
compatibility cannot hold together -- verified exactly (V5) on explicit
round-robin partitions of the `B = 6` base-3 packet (`K in {4, 16}`,
`W = ceil(f_max/K)`): `K * sum_i ||P b_i||_2^2 < Omega_+^2` as exact rationals.
(ii) The pieces are NOT required to come from a partition of the whole packet,
only to be disjoint; and the bound is uniform over which supports they take
from which fibers -- this is what "transverse to every prefix-quotient fiber"
buys you: nothing.  (iii) At general `q in [2, q_+)` the same conclusion holds
with `sqrt(KWM)` replaced by `K W L^{1/2}` via #729's layer-cake + Theorem I
(each layer is a pruned signed mask), and the density criterion makes
`K W L^{3/2 - 1/q} <= e^{o(N)} M` again exponentially below
`e^{eta N} M / L^{1-1/q}`.  So the transverse branch of (NFB) is dead on the
whole moment window, chart-free.

**Prop 1 does not contradict Theorem D (#729)**: transverse pieces DO satisfy
the signed clause -- they are honest signed pieces.  What they cannot do is
carry the failure's charge.  Prop 6.1's conclusion (semantic pieces must carry
`(1 - o(1)) Omega_+`) is therefore invariant under re-partitioning: the charge
always re-concentrates on pieces with exponential multiplicity somewhere.

---

## 2. Theorem 2 (Sidon-paired): the fiber-rooted semantic cap

Hypothesis **(FR)** (fiber-rooted grammar): each semantic piece's support lies
in a single `Phi`-fiber, or in at most `e^{o(N)}` of them.  This is the letter
of the grammar: #716's point-mass reduction takes
`F subseteq Phi^{-1}(s_0)` (one syndrome; Secs 1-2), each of #735's five
precursors roots "at one of its actual positive owners", finer (deeper) charts
only shrink fibers, and every COARSER admissible chart is a quotient chart,
whose classes below an exponential piece count are heterogeneous unions
carrying zero of the five precursors -- the coset homogeneity census, first
run in the companion packet's rung (c) and REPRODUCED self-containedly here
(V7: zero single-level mass below `3^{B-2}` classes, first mass exactly at
`3^{B-2}`, full resolution at `3^{B-1}`; `B in {6, 8}`).  (FR) is exactly
what the forced sixth alternative will have to break -- see Sec 6.

> **Theorem 2.** On the Sidon-paired class, at the canonical q=2 rooting of ANY
> failing band `A` (`||h||_2 >= e^{eta N} M/L^{1/2}`), every semantic piece
> under (FR) has
> ```text
> c_i <= sum_{S in U_i} omega(S) <= f(sigma_i) * omega(sigma_i)
>     <= f_max sqrt(delta_A) <= f_max ,
> ```
> so `e^{o(N)}` semantic pieces carry at most
> ```text
> e^{o(N)} f_max  <=  e^{o(N)} * (f_max L^{1/2} / M) * e^{-eta N} * Omega_+
>                  =  e^{-(eta + kappa) N + o(N)} Omega_+ ,
> ```
> with `kappa = ln(2/sqrt 3)/2 = 0.0719...` per `N`-unit, since
> `f_max L^{1/2} / M = (sqrt 3 / 2)^{B + o(B)}`.

**Proof.** The charge condition gives `c_i <= sum_{U_i} omega(S)`; `omega` is a
syndrome function, so a single-fiber piece has
`sum_{U_i} omega <= f(sigma_i) omega(sigma_i)`; (CS-K) bounds
`omega(sigma) = h(sigma)_+ / ||h||_2 <= sqrt(delta_A)`; and
`f(sigma_i) <= f_max`.  An `e^{o(N)}`-fiber piece costs another `e^{o(N)}`.
For the fraction: `Omega_+ >= ||h||_2 >= e^{eta N} M / L^{1/2}`, so
`f_max / Omega_+ <= f_max L^{1/2} M^{-1} e^{-eta N}`, and
`f_max L^{1/2}/M = C(B, B/2) sqrt((3^B+1)/2) / C(2B, B) = (sqrt 3/2)^B` up to
`poly(B)` (V2/V6 verify the exact integer form `f_max^2 L < M^2` for all
`4 <= B <= 64` and the rate `8^B f_max^2 L < 7^B M^2` from `B = 8`). `square`

The cap is **uniform over the failing band** -- the adversarially resonant
bands of Sec 6 included: a band concentrated on the resonant characters has
`delta_A` so small that (CS-K) crushes `omega`, while a band wide enough to
fail exponentially is too wide for its kernel to localize on any one fiber.
That trade-off is the whole theorem.

---

## 3. Theorem 3 (assembly): no realization at q=2 -- the sixth alternative is forced

> **Theorem 3.** On the Sidon-paired class, at the canonical q=2 rooting of any
> failing band, NO decomposition into `e^{o(N)}` pieces, each either
> (FR)-semantic or signed-clause-compliant, satisfies the #716 Sec-6 charge
> conditions: the signed side carries `<= e^{o(N)} M/L^{1/2}
> <= e^{-eta N + o(N)} Omega_+` (the clause bound, summed -- Prop 6.1's own
> step), the semantic side carries `<= e^{-(eta+kappa) N + o(N)} Omega_+`
> (Theorem 2), and their sum is exponentially below the required
> `sum_i c_i = Omega_+`.  In particular the five-precursor form of the
> dichotomy is FALSE on this class, and #716 Sec 7.1's sixth alternative is
> NECESSARY; by Theorem 2 it cannot be fiber-rooted.

Exact instantiation (V3, both bases, `B in {4, 6}`): with unnormalized weights
`h_+ = (f - M/c)_+`, the maximal root-cell charge is exactly the central cell
`f_max (f_max - M/c)`, and its ratio to `Omega~_+ = sum f h_+` is below
`(3/4)^{B/2}` already at these sizes.  Every piece type is covered: transverse
pieces are signed (Prop 1 / Theorem D), fiber-rooted pieces are capped
(Theorem 2), multi-fiber pieces with exponential multiplicity are heterogeneous
quotient-style unions emitting none of the five precursors (#760 Sec 6), hence
signed, hence clause-capped despite their large norms -- which is precisely the
capacity they lack.

**Honest q > 2 residual.** For `q > 2` the norming dual
`g = |h|^{q-2} h / ||h||_q^{q-1}` is no longer band-limited, `P_A g != g`, and
the pointwise cap on `omega = Re conj(P_A g)` needs `||P_A g||_inf` -- a signed
character-sum (Sidon-type) input, the same species as #729 Sec 3.3's `q >= q_+`
residual.  Theorem 3 is therefore stated at `q = 2` (the operating point #729
Sec 3.3 names, and the only `q` needed by the downstream consumers of the
dichotomy); a `q`-uniform version of Theorem 2 is exactly one more Sidon
estimate away.  Nothing is claimed for `q > 2` roots.

---

## 4. Theorem 4: the direct branch fails at every moment order

> **Theorem 4.** On the Sidon-paired class (both bases; any base with the class
> hypotheses), for EVERY `q >= 2`,
> ```text
> R_q(f) >= (L^{1/2}/M) ||h * 1_{image}||_2 = e^{eta_B N},
> eta_B -> (1/4) ln(9/8) = 0.0294... per N-unit,
> ```
> and the moderately-unpaired slice `s in [B/4, 3B/4]` (the (NFB) object)
> satisfies the same bound with its own mask.  So no direct PO4/signed payment
> of the packet -- or of the moderate slice -- exists at ANY moment order; the
> `q <= q_+ = 4.199` window offered by #760 Sec 7 is empty for this purpose.

**Proof.** Occupied-support transfer: `h_occ = h * 1_{Phi(Omega^0)}` has
support exactly `L`, so the power-mean inequality gives
`||h||_q >= ||h_occ||_q >= ||h_occ||_2 L^{1/q - 1/2}`, hence
`R_q(f) = (L^{1-1/q}/M) ||h||_q >= (L^{1/2}/M) ||h_occ||_2` -- the `q` and the
ambient size `c` both cancel (this is what makes the statement ASYMPTOTICALLY
base-free despite base 5's exponential image collapse `L/c = (3/5)^B`: the
finite `||h_occ||_2` is base-dependent, the `(9/8)^B` exponent is not).  Then
`||h_occ||_2^2 = M2 - 2(M/c)M + (M/c)^2 L >= M2 - 2M^2/c`, and
`L * M2 / M^2 = (9/8)^{B - o(B)}` (V2: exact `R_2^2 > 1` from `B = 6`
(base 3) / `B = 4` (base 5), exact Fractions through `B = 32`, pinned value at
`B = 6`; slice version from `B = 8`). `square`

Cross-check of constants (V2): the single top-fiber term
`L^{q-1} f_max^q / M^q` alone flips from exponentially small to exponentially
large exactly at `(1 - 1/q) ln 3 = ln 2 - ln ... `, i.e. `q = 2.709` -- #728's
unpruned-growth threshold, recovered here as the sign flip of
`L^{q-1} f_max^q - M^q` between `q = 2` and `q = 4` at `B = 16`.  Below
`2.709` the excess is carried by the bulk (`M2`); above, already by the central
fiber.  There is no `q` where neither carries it.

---

## 5. The payment-gap window: heavy enough to fail, too light to pay

Exact integers, all even `4 <= B <= 64` (V6):

```text
f_max * L >= 2 M          (heavy fibers exist: point-mass failures per #739
                           and #716 Cor 1.2, at every such B), and
f_max^2 * L < M^2         (no fiber reaches the q=2 carrying scale M/sqrt L),
with  f_max^2 L * 8^B < M^2 * 7^B  from B = 8   (gap rate (7/8)^B, i.e.
                           f_max sqrt(L)/M <= (sqrt(7)/sqrt(8))^{B/...} -- the
                           clean asymptotic rate is (sqrt 3/2)^B = (3/4)^{B/2}).
```

Every fiber of the class lies in the half-open window `[2M/L, M/sqrt L)`
(sizes `2^{B-s}` against thresholds `~(4/3)^B` and `~2.31^B`): each one is
individually admissible as a #739-heavy point mass, none is individually
capable of carrying a failure's charge, and (Theorem 3) no way of grouping,
slicing, or re-cutting them changes the totals.  This window statement is the
one-line summary of why the class defeats every decomposition.

---

## 6. EXPERIMENTAL: the survivor's structure -- the resonant spectrum

What the failure charge actually correlates with is explicit.  Per-pair
factorization (pair `i` contributes `1` (absent), `z^2 e_c(j c) = z^2` (both),
`z e_c(j A_i)`, or `z e_c(-j A_i)`) gives the PROVED identity

```text
hat f(j) = sum_S e_c(-j Phi(S)) = [z^B] prod_{i=1}^B (1 + z^2 + 2 z cos(2 pi j A_i / c)),
```

verified against brute-force DFT at `B = 4` and against Parseval
(`sum_j |hat f(j)|^2 = c * M2`, machine-exact to `1e-6` relative) at
`B in {6, 8}` base 3 and `B = 6` base 5 (V4).  Consequences:

- **Half-frequency resonance (exact congruence + finite verification).**  For
  `j* = (c-1)/2`: `j* A_i mod c = (c - A_i)/2` EXACTLY (one line: `A_i` is odd
  and `(c-1) A_i / 2 = c (A_i - 1)/2 + (c - A_i)/2`), verified for all `i`,
  both bases (V4).  So the phases sit at `pi (1 - A_i/c)`: all but the top
  `O(1)` factors approach `(1 - z)^2` geometrically fast in `B - i` (the top
  pair sits at `2 pi / 3` for base 3), and `[z^B] (1-z)^{2B} = (-1)^B C(2B, B)
  = +-M` -- which is why the half-frequency is near-extremal with the constant
  settling at `0.707...` rather than `1`.  Finite verification: `|hat f(j*)| >= 0.70 M` for
  `B in {6, 8, 16, 32, 64}` (base 3; the constant converges to `0.7071...`),
  `>= 0.61 M` at `B = 6` base 5 (where the top shell has 12 frequencies of the
  same magnitude, all digit-sparse).
- **Census.**  Base 3: `#{j != 0 : |hat f(j)| >= rho M}` = 2, 2, 42 at
  `rho = 1/2, 1/4, 1/10` for `B = 6` and 2, 2, 58 for `B = 8` (V4, pinned) --
  the top shell is just `{j*, j*+1}` (digit patterns `11...1`, `11...12`), and
  the `rho = 1/10` shell is the 3-adically sparse frequencies (pure powers
  `10...0`, `20...0` resonate at `~0.18-0.20 M`), growing like `O(B)`, i.e.
  `O(log L)` -- polynomially few characters carry `Theta(1)`-of-`M`
  correlations.  (The census counts and `j*` values are verifier-pinned; the
  shell-membership descriptions and the `O(B)` growth reading are
  observational, from the two scanned sizes.)
- **What this means for the sixth alternative.**  The packet-scale structure
  that survives all of Theorems 1-4 is exactly this Bohr/resonant correlation
  -- the object #716 Sec 5.6 warned "does not by itself produce" a semantic
  output.  A sixth alternative must be a conversion theorem: input, a
  `Theta(1)`-correlation with `e^{o(N)}`-many explicit (digit-sparse)
  characters of the realized image; output, a paid structure at the compiler
  interface.  The instance above (explicit `j*`, exact congruence, exact
  product formula, census) is the minimal test any such theorem must pass, and
  the natural first target for it.  This is where the Pisot/Erdos non-decay
  mechanism (integer-base Bernoulli convolutions have non-vanishing Fourier
  transforms) enters RS-MCA: the class's self-similar image measure is
  non-Rajchman, and that -- not fiber concentration alone -- is the invariant
  content of its resistance.

## Nonclaims

- **NOT a refutation of #716's dichotomy as a conjecture-with-sixth-
  alternative.**  Proved: the FIVE-precursor, fiber-rooted form is unrealizable
  on this class at the q=2 rooting.  His Sec 7.1 already offered the sixth
  alternative; this packet converts "or" into "must".
- **NOT a proof of the sixth alternative**, of any Bohr-to-semantic conversion,
  of atlas totality (Codex's lane; only an interface here), or of the
  large-q(`>= q_+`) Sidon estimate (#729 Sec 3.3, untouched).
- **NOT a reserve payment**: fence (N1) respected; emission and resonance are
  never converted into lower reserve here.
- **q > 2 roots are an honest residual** (Sec 3): Theorem 2's pointwise cap is
  proved at q=2 only, where the norming dual is band-limited.
- **(FR) is a hypothesis**, argued from the grammar's letter (#716 Secs 1-2,
  #735, #760 Sec 6), not a theorem about all conceivable grammars -- on
  purpose: its negation IS the forced sixth alternative.
- Resonance constants (`0.70`, `0.61`, the census) are finite-verified
  (through `B = 64` for `j*`), not asymptotically proved; the antipodal
  congruence and the product formula are exact/proved.
- Floats appear ONLY in Sec 6/V4 (+ a CS sanity check in V3), always guarded by
  the exact Parseval identity; every other number is exact `int`/`Fraction`.

## Consumers

- **#716** (`primitive_signed_payment_barrier_v1.md`): Sec 6's decomposition
  step is DECIDED on the Sidon-paired class -- unrealizable in five-precursor
  form at q=2; Sec 7.1's sixth alternative is now load-bearing, with Sec 8's
  "signed minor-arc payment" disjunct pointed at the explicit resonant
  spectrum.
- **companion packet #760 (OPEN PR)**: its Sec 7 (NFB) is CLOSED, both
  branches (transverse: Prop 1 + Thms 2-3; direct `q <= 4.199`: Theorem 4);
  the object is quoted in Sec 0 here, so the closure reads at main.  Input-2
  residual re-pointed as in LANE above.
- **#739** (`staircase_concentration_sidon_paired.md`): its Sec 5 open branch
  ("route the moderately-unpaired fibers through the signed clause") is closed
  negative (Theorem 4, slice form); its heaviness and this packet's payment gap
  are the two walls of the same window (Sec 5).
- **#729** (`general_pruned_signed_bound.md`): the Sec 3.2 decomposition
  obligation is UNMEETABLE within (FR) on this class; Theorem D and the
  layer-cake are confirmed sharp (transverse pieces are exactly
  clause-compliant and exactly charge-trivial).
- **#732 / #735**: Theorem A survives untouched (the obstruction is capacity,
  not the charge conditions); the five-precursor grammar acquires its exact
  boundary.
- `rs_mca_thresholds.tex` / `asymptotic_rs_mca_frontiers.tex`: paste-ready as
  (i) a proposition after the PO4/PO5 material -- "on the Sidon-paired class no
  fiber-rooted semantic-or-signed decomposition pays, and no direct
  character-sum payment exists at any moment order" -- and (ii) a remark naming
  the packet-scale resonant conversion as the surviving open input, with the
  half-frequency instance as its test case.  Visible hypotheses: #749-corrected
  class, q=2 rooting, (FR).
- Lean statement stub: `experimental/lean/transverse_charge_obstruction/`
  (exact-integer facts: staircase/M/M2 identities, the payment-gap window and
  its rate, the `R_2^2 > 1` cross-multiplied inequality, the antipodal
  congruence; statements only, `lake build` succeeds, no `sorry`).

## Reproducibility

```bash
python3 experimental/scripts/verify_transverse_charge_obstruction.py
# -> RESULT: PASS (281/281)
python3 experimental/scripts/verify_transverse_charge_obstruction.py --tamper-selftest
# -> tamper-selftest: caught 4/4 ; then RESULT: PASS (281/281)
cd experimental/lean/transverse_charge_obstruction && lake build
# -> Build completed successfully
```
