# Lower reserve O5c: quotient / Chebyshev / remainder certified profile-lists

**Status:** `PARTIAL`.  Per-class honest labels for the "any larger ... list"
clause of `prop:simple-pole-lower` (L6196--6198):

| profile class | label |
|---|---|
| **quotient** (complete-fiber; complete-square flagship) | **PROVED** |
| **remainder**, Euclidean / fixed-`R` (`w >= r`) | **PROVED** (same lemma) |
| **Chebyshev** (Dickson twin-coset fold) | **PROVED-via-quotient** (instance; domain hypothesis stated) |
| **remainder**, deep (`w < r`, i.e. `|R| >= c`) | **WALL localised** (`OPEN`) |

**Verdict:** **O5c is PAID for the quotient class** (route O5c of audit **#693**),
and with it the Euclidean-remainder and Chebyshev instances.  The payment is a
composition of two theorems already in `asymptotic_rs_mca_frontiers.tex`: the
complete-fiber quotient profile-list of `thm:smooth-quotient-obstruction`
(eq 6.4/6.8) and the exact normal form `thm:exact-quotient-remainder-normal-form`
(QR2), routed through the collision-aware pole + challenge average of
`prop:simple-pole-lower` (4.2 + L6201--6208) **instead of** the separating-pole
route it currently uses.  The remaining deep-remainder regime is localised to a
single missing input (a partial-occupancy atlas at the degree-`c` interlace).
Route **O7** stays `OPEN`, exactly as **#693** marks it; the coupling lemma
(section 7) proves no profile-list can reach it.

Target: `experimental/asymptotic_rs_mca_frontiers.tex` (read at `36de5bf`).
Attacks route **O5c** of hard input 5, scoped by the coverage audit **#693**
(`lower_reserve_unsafe_side_coverage_audit.md`, sections 3--4).

**Consumes (never attacks or extends):**
- **#693** — lower-reserve / unsafe-side route audit; supplies the O5c/O7
  decomposition and the open statement discharged here.
- **#524** — `simple_pole_realizability.md` (integrated): the two-regime reserve
  `B^MCA >= max{P, E}`, the min-distance rigidity `(star)`, and the
  collision-aware realizability surface (H1)--(H2) reused verbatim below.
Also consumes the in-paper theorems `prop:simple-pole-lower` (L6180),
`thm:collision-aware-pole` (L1997), `prop:exact-prefix-list` (L1965),
`thm:exact-quotient-remainder-normal-form` (L3456),
`thm:smooth-quotient-obstruction` (L3985),
`prop:identity-quotient-comparison` (L3896), and
`prop:complete-support-factorization` (L3577).

**Verifier:** `experimental/scripts/verify_lower_reserve_o5c.py`
-> `RESULT: PASS 49/49` (`--check`), `RESULT: PASS 7/7` (`--tamper-selftest`),
~0.04 s, python3 stdlib only.  It builds the quotient list and runs the genuine
simple-pole conversion over `F_25`, the field-drop QR2 pigeonhole over
`F_169`, and recomputes every number printed below.

---

## 1. The obligation O5c, with every quantifier (anchors L6180--6199, L980--986)

`prop:simple-pole-lower` ("Exact unsafe test", L6180) proves: for a
ledger-admissible row `C_n = RS_{F_n}(D_n, k_n)` with `D_n subseteq B_n subseteq
F_n`, `q_n = |F_n| > n`, challenge set `emptyset != Gamma_n subseteq F_n`, target
`B_n^* = floor(eps |Gamma_n|)`, and agreement `k_n + 1 <= a_n <= n`, writing
`w = a_n - k_n - 1` and

```text
  L_n  = ceil( binom(n, a_n) |B_n|^{-w} )                         (identity list floor)
  M(L) = ceil( L (q_n - n) / (q_n - n + k_n (L - 1)) )            (4.2, L2003)
```

if `ceil( (|Gamma_n|/q_n) M(L_n) ) > B_n^*` then agreement `a_n` is **unsafe**.
Its last sentence (L6196--6198) is the open content:

> "The same statement holds with `L_n` replaced by **any larger identity,
> quotient, Chebyshev, or remainder-profile list proved for the dimension-`k_n+1`
> code.**"

**Reading, exactly.** A *list* for a received word `U in B_n^{D_n}` is
`Lcal_a(U) = { c in C_n^+ : |{x in D_n : c(x) = U(x)}| >= a_n }`, the set of
distinct codewords of the dimension-`(k_n+1)` code `C_n^+ = RS_{F_n}(D_n, k_n+1)`
agreeing with `U` on at least `a_n` coordinates.  "Larger" means
`|Lcal_a(U)| >= L_n`.  "Proved for the ... profile" means the members are
exhibited through that profile's structured supports:

- **identity** profile — supports = arbitrary `a_n`-subsets, locators
  `U_z = X^{a_n} + sum z_i X^{a_n - i}`; list = one depth-`w` prefix fiber
  (`prop:exact-prefix-list`).  This is **O5a**, already paid.
- **quotient** profile — supports = unions of complete fibers `phi^{-1}(E)` of a
  `c`-fold folding `phi: D_n -> Q` (`def:structured-folding`, L2606).
- **Chebyshev** profile — quotient profile for the Dickson fold `phi = T_c` on a
  twin-coset domain (`def:circle-domain-code`, L2635; cells L2385--2395).
- **remainder** profile — complete-fiber-plus-remainder supports
  `S = phi^{-1}(E) sqcup R`, `|R| = r < c`
  (`def:quotient-remainder-profile`, L3384).

For each such list, the transported conclusion is: **some received line for
`C_n` has at least `ceil( (|Gamma_n|/q_n) M(|Lcal_a(U)|) )` MCA-bad slopes lying
in `Gamma_n`** (this is the *challenge-intersection* estimate); hence
`> B_n^*` certifies `a_n` unsafe.  The definitional source (L980--986) states the
same obligation as data: a certified profile-list needs "the pole and
challenge-intersection estimates that prove its bad-slope count exceeds the
target."

**What was open (per #693 section 4).** Only the identity list (O5a) and the
value-set list (O5b) carried the challenge-intersection lower bound.  The
quotient / Chebyshev / remainder lists were "an input, not a theorem."  O5c asks
to produce, for at least one of these profiles, the list *of proven size*
together with `M` and the challenge average.

---

## 2. The two half-theorems O5c composes

The unsafe test factors as **list size** `x` **conversion**, and both halves are
already in the paper; only their composition on a non-identity profile is new.

**(A) Conversion is list-agnostic.**  `thm:collision-aware-pole` (4.2, L1997)
takes *any* `L` distinct `C^+`-codewords agreeing on `>= m >= k+1` points and
delivers a received line for `C` with `>= M(L)` distinct MCA-bad slopes,
for every `q > n`.  The proof of `prop:simple-pole-lower` (L6201--6208) then
shifts the line `(r_0, r_1) -> (r_0 + delta r_1, r_1)`, translating the bad-slope
set `Z` (`|Z| >= M(L)`) by `-delta`; averaging over `delta in F_n` some translate
carries `>= |Z| |Gamma_n| / q_n >= M(L) |Gamma_n| / q_n` bad slopes inside
`Gamma_n`.  **Neither step inspects how the list arose** — the "profile variants
use the same conversion after their list sizes have been established"
(L6208).  Both `M(.)` and the outer average are nondecreasing in `L`, so a
*larger* list gives an at-least-as-strong test.  [verifier G1, G4]

**(B) The quotient profile already supplies a proved list.**
`thm:exact-quotient-remainder-normal-form` (QR2, L3486--3503) gives the exact
depth-`w` prefix fiber of complete-fiber-plus-remainder locators
`L_{E,R} = P_R(X) V_E(phi(X))`: for `w >= r`, `d = floor(w/c)`, it equals one
depth-`d` *quotient*-prefix fiber `{ E in binom(Q\phi(R), m) : pref_d(V_E) =
eta_z }` after the unique recovery of `R`.  Pigeonholing over the scaled
quotient coefficient field `B_phi` (`def:quotient-remainder-profile`, L3405)
proves a fiber of size

```text
  L_quot = ceil( binom(N - |phi(R)|, m) |B_phi|^{-d} ),   N = |Q| = n/c,  m = (a - r)/c.   (QR6)
```

`thm:smooth-quotient-obstruction` (eq 6.4, L4016) is the flagship instance:
the complete-*square* fold (`c = 2`, `B = F_{p^2}`, `B_phi = F_p`) gives
`L_quot >= binom(n/2, a/2) p^{-w/2} = exp((h(alpha)/4 + o(1)) n)`.

---

## 3. The quotient payment (PROVED)

**Lemma O5c-Q (quotient challenge-intersection lower bound).**
Let `phi: D_n -> Q` be a `c`-fold complete-fiber folding
(`def:structured-folding`) with `N = |Q| = n/c` and scaled quotient coefficient
field `B_phi subseteq B_n`.  Fix a remainder size `0 <= r < c`, an agreement
`a_n = c m + r` with `w = a_n - k_n - 1 >= r`, and put `d = floor(w/c)`.  Then
for every `q_n = |F_n| > n` and `emptyset != Gamma_n subseteq F_n` there is a
received line for `C_n = RS_{F_n}(D_n, k_n)` carrying at least

```text
  P_quot(a_n) = ceil( (|Gamma_n|/q_n) M(L_quot) )      distinct MCA-bad slopes in Gamma_n,
```

with `L_quot` as in (QR6) and `M` as in (4.2).  Consequently
`P_quot(a_n) > B_n^*` certifies `a_n` unsafe.

*Proof.*  By QR2 (case `w >= r`) the depth-`w` prefix fiber of the complete-fiber
locators, at its heaviest prefix value `z`, is one quotient-prefix fiber of size
`>= L_quot`; by `prop:exact-prefix-list` its members `U_z - Q_{S}` are distinct
`C^+`-codewords agreeing with `U_z|_{D_n}` on exactly `a_n >= k_n+1` points.
Feed this list to half-theorem (A): `M(L_quot)` distinct bad slopes on one line,
then `ceil((|Gamma_n|/q_n) M(L_quot))` after the challenge average.  `QED`

This is precisely the "`L_n` replaced by a larger quotient-profile list" clause,
now with its pole (`M`) and challenge-intersection (`|Gamma|/q`) estimates
proved.  **O5c is paid for the quotient class.**

**Why the quotient class is closest to reach** (task ladder, step 2).  Of the
three non-identity profiles, the quotient list is the only one whose size *and*
its exponential dominance over the identity list are already theorems
(`thm:smooth-quotient-obstruction` eq 6.4; `prop:identity-quotient-comparison`
QR8/QR9).  The single missing step was the *conversion route*: eq 6.8 realises
its bad slopes through the separating-pole `thm:prefix-to-line-hardness`, which
needs a huge extension `|F| - n > k binom(|Fcal_z|, 2)`.  Lemma O5c-Q instead
uses the collision-aware pole, valid for every `q > n`, and carries the
challenge intersection the separating-pole route drops.

**Concrete faithful witness** (verifier G1, over `F_25`).  `D` an order-8
multiplicative coset, square fold, `a = 2`, `k = 1`, `q = 25`, `n = 8`.  The
quotient list is the four complete-square supports; its codewords are the four
constants `y in D^2`.  Building the genuine simple-pole line `(U(x)/(x-alpha),
-1/(x-alpha))` and counting support-wise MCA-bad slopes (per L187--201) at every
admissible pole gives `max = 4 = M(4)` distinct bad slopes, all landing in
`Gamma = F_25^*`.  With `eps = 1/8`, `B^* = 3`: `P_quot = ceil(24/25 * 4) = 4 >
3`, so `a = 2` is **unsafe** by the quotient list.  Window is shallow
(`a = 2 < (n+k)/2 = 4.5`).

---

## 4. Genuine strengthening: the quotient list beats the identity list

O5c-Q is non-vacuous exactly when `L_quot >= L_n`, i.e. when the quotient list is
*larger*.  `prop:identity-quotient-comparison` (QR9, L3920) gives the exponent

```text
  (1/n) log Nbar_{c,r} = (h(alpha)/c)(1 - lambda_c) + o(1),      lambda_c = log|B_c| / log|B|,
```

strictly positive under a **positive-rate field drop** (`lambda_c < 1`) and `0`
without one (`lambda_c = 1`).  At `c = 2`, `lambda_2 = 1/2` this is `h(alpha)/4`,
matching the eq 6.4 exponent — the quotient list is exponentially larger than
the identity scale in the smooth-quotient tower. [verifier G6]

**Faithful field-drop witness** (verifier G2/G3, over `F_169 = F_13[t]/(t^2-2)`,
`B_phi = F_13`, `lambda_2 = 1/2`).  `theta` a generator of `F_169^*`,
`H = <theta^7>` of order 24, `D = theta H`, so the square fold is 2-to-1 onto
`D^2 = theta^2 F_13^*` (the field drop, verified `theta^{-2} D^2 subset F_13`).
Take `a = 8`, `k = 5`, `c = 2`, `N = 12`, `m = 4`, `w = 2`, `d = 1`, `q = 169`,
`Gamma = F_169^*` (`|Gamma| = 168`).  Bucketing the `binom(12,4) = 495`
complete-square supports by their depth-2 locator prefix gives `<= 13` buckets
(the lacunary gap-1 coefficient vanishes; the gap-2 coefficient is `-e_1(E) in
theta^2 F_13`), heaviest `>= 39`.  Then:

```text
  L_quot = ceil(495 / 13)        = 39   >   L_id = ceil(binom(24,8) / 169^2) = 26
  M(39)  = 17                    >   M(26) = 14
  P_quot = ceil(168/169 * 17)=17 >   P_id  = ceil(168/169 * 14) = 14
```

**Headline.**  At target `B^* = 15` (`eps = 15/168 ~ 0.089`) the quotient
profile-list certifies `a = 8` **unsafe** (`P_quot = 17 > 15`) while the identity
list does **not** (`P_id = 14 <= 15`).  The quotient list pays O5c strictly
beyond the identity floor `P`.  The window is shallow: `a = 8 < (n+k)/2 = 14.5 <
a_deep = 18`.

---

## 5. Remainder profile: Euclidean case PAID, deep case WALL

QR2 splits on `w` vs `r` (`thm:exact-quotient-remainder-normal-form`).

**Euclidean / fixed-`R` case `w >= r` — PROVED.**  Here the first `r` prefix
coefficients recover `R` uniquely (QR2 (i), L3546--3552), and the fiber is one
quotient-prefix fiber; Lemma O5c-Q applies verbatim with the floor
`ceil(binom(N - |phi(R)|, m) |B_phi|^{-d})`.  So the remainder profile in its
Euclidean regime is paid by the same composition. [verifier G7, first check]

**Deep case `w < r` (equivalently `|R| >= c`) — WALL localised, `OPEN`.**  QR2
(ii) (QR4, L3513--3520) gives the fiber count as a **sum**

```text
  #{(E,R) : pref_w(L_{E,R}) = z} = sum_{R : pref_w(P_R) = T^{-1}(z)} binom(N - |phi(R)|, m),
```

not a single pigeonhole floor: distinct admissible `R` contribute different
summands `binom(N - |phi(R)|, m)` (verifier G7 exhibits three distinct values),
so there is no clean `L_quot` to feed the conversion.  The precise clause of
L6197 that fails is **"proved for the dimension-`(k+1)` code"**: the list is no
longer one prefix fiber.  The obstruction is the degree-`c` interlace of
`prop:complete-support-factorization` (L3591--3594) — once `|R| >= c`, the
remainder coefficient `p_c(R)` and the quotient coefficient `v_1(E)` collide at
degree `c`, so the triangular separation is lost.  The missing input is exactly
a **partial-occupancy atlas** on the remainder-prefix problem (named at
L3594 and L6325--6328); this note does not supply it.

---

## 6. Chebyshev profile: reduces to the quotient lemma

The Chebyshev / twin-coset structure (`def:circle-domain-code`, L2635; dihedral
and Chebyshev cells L2385--2395) is a quotient by the Dickson fold: on a
Chebyshev twin-coset domain `D` smooth at scale `c`, the map `phi = T_c`
(Dickson, `T_c((u + u^{-1})/2) = (u^c + u^{-c})/2`) is a `c`-fold complete-fiber
folding (`def:structured-folding`), so **Lemma O5c-Q applies with `phi = T_c`**.
The list floor is `ceil(binom(N, m) |B_phi|^{-d})` with `N = |T_c(D)|` and
`B_phi` the descended coefficient field.  Hence the Chebyshev class is **PROVED
as an instance** of the quotient payment, under the stated domain hypothesis (a
twin-coset domain complete-fibered at scale `c`); a genuine strengthening over
the identity list again requires a positive-rate field drop.  The finite
Mersenne-31 Chebyshev fixed-remainder floor (`m31_chebyshev_fixed_remainder_floor`)
is the deployed-row shadow of the same `phi = T_c` fold at `c = 2^j` and is
consistent with this reduction; it is not consumed as an asymptotic input.

---

## 7. Coupling lemma (deliverable 4): what a paid O5c list needs to also supply O7

O7 (`#693` route) asks for an unsafe `a_{-,n}` within `o(n)` of the interior
entropy crossing `g_{T,n}` in the band `(n+k_n)/2 < a_{-,n} < a_deep`,
`a_deep = ceil((2n+k_n)/3)`.

**Coupling lemma.**  A certified profile-list at agreement `a` — identity,
value-set, quotient, Chebyshev, or remainder — has size `>= 2` **only if**
`a <= (n + k)/2`.

*Proof.*  Two distinct `C^+`-codewords agreeing with one word on `>= a` points
agree with each other on `>= 2a - n` points; their difference is a nonzero
degree-`<= k` polynomial, hence has `<= k` roots, so `2a - n <= k`, i.e.
`a <= (n+k)/2`.  This is the min-distance rigidity `(star)` of `#524`
(`prop:prefix-rigidity-full`, L2044), and is **independent of the profile**. `QED`

**Consequence (the additional property, stated as mathematics).**  For a paid
O5c list to *also* supply O7 it would have to be a size-`>= 2` list at an
agreement `a_{-,n} > (n+k_n)/2` (inside the O7 band).  The coupling lemma says
**no such list exists**: above `(n+k)/2` every profile-list collapses to size
`<= 1`, so `M(1) = 1` and the challenge-intersection floor is
`ceil(|Gamma|/q) = 1`, which cannot exceed any target `B^* >= 1`.  Because
`a_deep > (n+k)/2` exactly when `n > k` (always), the entire O7 band lies in the
list-`<= 1` zone.  [verifier G5]

So the coupling of `#693` section 4 — "a profile-list construction that reaches
the interior crossing supplies both O5c and O7" — is a **true but vacuous**
implication on the list side: its hypothesis is unsatisfiable.  The sharp form
is: **O5c is a shallow-window (`a <= (n+k)/2`) problem, fully payable by lists;
O7 is a list-*inaccessible* band and must be paid by the non-list tangent floor**
`E(a) = min{|Gamma|, n - a + 1}` (`prop:universal-tangent-floor`, L1833), whose
crossing-sharpness — not any list — is the open content.  Any O7 argument must
therefore come from the tangent floor, not from a profile-list construction.

---

## 8. O7 remark (OPEN)

Route O7 (crossing sharpness in the intermediate identity-dominant window,
L6280--6281 / L6683--6684) remains `OPEN`, exactly as `#693` marks it.  By
section 7 it is not a profile-list question; discharging it requires showing the
two-regime reserve `max{P(a), E(a)}` (with `P(a) = 1` collapsed and `E` a valid
but not-proved-exact floor in the band) crosses `B_n^*` within `o(n)` of
`g_{T,n}`.  No construction toward it is attempted here.

---

## 9. Per-class labels

| # | claim | verdict | basis |
|---|---|---|---|
| Q1 | quotient challenge-intersection floor `P_quot(a) = ceil((|Gamma|/q) M(L_quot))` is a valid lower bound; `> B^*` certifies unsafe | **PROVED** | Lemma O5c-Q: QR2 + `thm:collision-aware-pole` + challenge average; G1 faithful `F_25` MCA count |
| Q2 | quotient list is a genuine *larger* list (`L_quot > L_id`) under a positive-rate field drop | **PROVED** | `prop:identity-quotient-comparison` QR9; G3 faithful `F_169` (`39 > 26`) |
| Q3 | headline: quotient certifies `a` unsafe at `B^*` where identity fails | **COMPUTED** | G3 (`P_quot=17 > 15 >= 14=P_id`) |
| R1 | remainder Euclidean case `w >= r` paid by the same lemma | **PROVED** | QR2 (i); G7 single-pigeonhole floor |
| R2 | remainder deep case `w < r` (`|R| >= c`) is a remainder-prefix sum, not one floor | **WALL / OPEN** | QR4; `prop:complete-support-factorization` degree-`c` interlace (L3591--3594) |
| C1 | Chebyshev class paid as the `phi = T_c` (Dickson) instance | **PROVED (instance)** | section 6; domain hypothesis: twin-coset, complete-fibered at scale `c` |
| K1 | coupling: no profile-list has size `>= 2` above `(n+k)/2`; O7 is list-inaccessible | **PROVED** | min-distance `(star)`; G5 (0 counterexamples, `n <= 89`) |
| K2 | collision saturation `M(L) -> floor((q-n)/k)`: exponential lists give bounded challenge floors for fixed `q` | **PROVED** | G4 (`M(10^7)=29=(q-n)/k`) |
| -- | O7 crossing sharpness; any safe-side / envelope-domination / prize-threshold claim | **OPEN / NOT CLAIMED** | section 8; this is a lower-side O5c payment only |

---

## 10. Nonclaims

This note does **not** claim:

- an **exponential** challenge-restricted floor.  `M(L)` saturates at
  `floor((q-n)/k)` (verifier G4), so an exponentially large quotient list does
  **not** yield an exponential `B^MCA_{C,Gamma}` for fixed `q`; that needs the
  separating-pole route (`thm:prefix-to-line-hardness`, large extension), a
  different mechanism.  The quotient list strengthens the *challenge* floor over
  the identity floor precisely on the field-drop regime where `M(L_id) <
  M(L_quot)` (section 4).
- any payment of **O7** (section 8) or of the interior crossing; section 7
  proves lists cannot reach it.
- a **general** field-drop for the quotient/Chebyshev profile.  Absent a
  positive-rate drop the quotient list is *dominated* by the identity list on the
  exponential scale (`log L_quot ~ (1/c) log L_id`, QR9 with `lambda_c = 1`);
  Lemma O5c-Q is still valid but not a strengthening there.
- the deep-remainder floor (R2): the partial-occupancy atlas at the degree-`c`
  interlace is an input, not supplied here.
- any general-linear-code statement beyond the RS rows of `prop:simple-pole-lower`;
  the finite witnesses are RS toy scales (`F_25`, `F_169`).

---

## 11. Replay

```bash
python3 experimental/scripts/verify_lower_reserve_o5c.py --check
# -> RESULT: PASS 49/49            (~0.04 s, stdlib only)
python3 experimental/scripts/verify_lower_reserve_o5c.py --tamper-selftest
# -> RESULT: PASS 7/7
```
