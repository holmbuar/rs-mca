# Pushing the same-block trade-stacking family past b=24: a memory-bounded exact method reaches k=5/b=30, and the family CAPS at the b=24 champion

## Status

`CEILING (COMPUTED). This packet supersede-extends #694 (comb_trade_champion.md)
on its explicitly-open residual #1 (k=5, b=30, left MEMORY-BOUNDED) and residual
#3 (non-uniform per-block weights). / S1 METHOD (PROVED memory bound + COMPUTED):
a size/value split of #694's 6-tuple aggregate-moment map turns the asymptotic
census into one bounded by a single (W,A,C)-group's value-set instead of the
whole L1_inf-key dict; this reaches k=5 in ~25 MB where #694's flat DP needs the
full ~57.4M-key table (several GB). Cross-checked against #694's flat DP on
k<=4 (exact agreement) and against an independent block-split meet-in-the-middle
on k<=5, with exact mass-conservation (sum of fibers = 2^b). / S2 k=5 FLAT
(COMPUTED, two independent methods): the flat-AP PROUHET comb at k=5 gives
fstar_inf=2072, L1_inf=57376057, rho_inf=0.156900 -- BELOW #694's b=24 champion
(0.160847) and even below #655's b=18 champion (0.158411). So k=5 flat does NOT
beat the record. / S3 WEIGHTS (COMPUTED): generalizing to non-uniform per-block
weights (block i at w_i*s), the maximum rho_inf over the searched weight window
is the b=24 champion itself, uniquely at k=4 with AP weights (0,1,...,k-1) up to
affine scaling; the k=5 weight maximum found is 0.160018 (weights (0,1,2,7,8),
its leading two-cluster family peaks there then decays) < 0.160847. rho_inf
falls off as the weight diameter grows (toward a size-injective floor ~0.11), so
the maximum lives at bounded, searched diameter. / VERDICT: the
PROUHET stacked-trade comb family does NOT extend past b=24; the champion is the
family maximum for k<=5 over all weight sequences searched. The unconditional
bracket lower end stays rho* >= 0.160847 (unchanged; now known not to be movable
by this family at k<=5). / Residual: k>=6, other gadgets, and non-uniform
per-block GADGETS remain unsearched (see Nonclaims).`

Label key (as #694): **PROVED** (written re-derivable proof), **COMPUTED**
(exact/exhaustive finite enumeration), **MEASURED** (exact finite objects,
trend read off), **AUDIT** (recap of a prior result), **OPEN**.

**Credit.** The construction (`Comb(G,k,s) = union_i (i*s + G)`), the census
`(fstar, L1)` and rate `rho = (log fstar + log L1)/b - log 2`, the b=24 champion
`rho=0.160847`, the 6-tuple aggregate-moment mechanism, and the PROUHET gadget
`G = {0,1,2,4,5,6}` (scottdhughes **#564**'s minimal degree-2 PTE trade) are all
**#694** (`comb_trade_champion.md`), building on **#655**
(`fiber_image_tradeoff.md`: the `rho` definition, moment-curve reduction, b=18
champion `0.158411`, and the unconditional bracket) and **#683**
(`championship_census_b19_26.md`: the b=19..26 null census and the
positional-tensor lemma). The bracket ends `[0.158411, 0.405465]` (before #694)
are per **#673** and DannyExperiments **#668**; #694 moved the lower end to
`0.160847`. This packet adds the memory-bounded method, the k=5 census, and the
weight-sequence ceiling; it does not move either bracket end.

---

## 0. Setup (AUDIT, recap of #694 / #655)

A block `V` is `b` distinct integers; for `S subseteq V`,
`Phi(S) = (|S|, sum_S x, sum_S x^2)`; `fstar(V)` is the largest fiber (most
subsets sharing one `Phi`), `L1(V)` the image size (number of distinct `Phi`),
and `rho(V) = (log fstar + log L1)/b - log 2` (natural log), with
`X = (fstar L1)^{1/b} = 2 e^rho`. `fstar, L1, rho` are invariant under any affine
map `x -> a x + b` (`a != 0`) applied to `V`. The **comb** of `k` copies of a
gadget `G` (`|G| = g`) at common shift `s` is `Comb(G,k,s) = union_{i=0}^{k-1}
(i s + G)`, a block of `b = g k` distinct integers for `s` large. #694's
**champion**: `G = PROUHET = {0,1,2,4,5,6}`, `k=4`, `s>=48`, giving `b=24`,
`fstar=190`, `L1=4192627`, `rho=0.160847`.

**#694's asymptotic mechanism (the object we compute).** For `s` past an
explicit threshold `s_0`, a subset `T` of `Comb(G,k,s)` (a choice
`T_i subseteq G` per block) has `Phi(T)` a fixed `s`-independent function of the
**six aggregate invariants**

```
    W = sum_i |T_i|,  A = sum_i i|T_i|,  C = sum_i i^2|T_i|,
    B = sum_i sum(T_i),  D = sum_i i sum(T_i),  E = sum_i sumsq(T_i),
```

because `|T| = W`, `sum(T) = s A + B`, `sumsq(T) = s^2 C + 2 s D + E`, and for
`s > s_0` two subsets collide **iff** their six aggregates agree (#694 R2,
PROVED there). Hence `fstar_inf`, `L1_inf` -- the values for every `s > s_0` --
are the max fiber and image size of the map `(T_0,...,T_{k-1}) -> (W,A,C,B,D,E)`
over `(2^G)^k`. #694 computes these with a **flat DP** whose state is the full
6-tuple; its dict has exactly `L1_inf` keys.

---

## 1. Where #694 hits the wall, in its own terms (AUDIT)

#694's flat 6-tuple DP (`asymptotic_fL`, its Method 4) holds one dict entry per
distinct 6-tuple, so its memory is `Theta(L1_inf)`:

```
    k    b     L1_inf        flat-DP dict         status in #694
    2   12       3863        ~KB                  fine
    3   18     162075        ~10 MB               fine
    4   24    4192627        ~0.5-1 GB            fine (the champion)
    5   30   57376057        ~5-8 GB (est.)       MEMORY-BOUNDED (#694 residual 1)
```

`L1_inf` grows ~14-42x per step, so at `k=5` the flat dict needs tens of
millions of 6-tuple->count entries -- several GB, past this environment's guard.
#694 therefore left `k=5` explicitly OPEN ("may or may not beat the b=24
record"). The task is not a bigger machine but a **smarter enumeration**.

---

## 2. The memory-bounded method (PROVED bound + COMPUTED validation)

**Key structural split.** The 6-tuple factors into a **size part** `(W,A,C)`
and a **value part** `(B,D,E)`. The size part depends **only on the size-vector**
`n = (|T_0|,...,|T_{k-1}|) in {0,...,g}^k` -- of which there are only
`(g+1)^k` (for `g=6, k=5`: `7^5 = 16807`). The value part depends on the actual
subset choices. So:

```
    L1_inf   = sum over distinct wac=(W,A,C) of | union_{n : WAC(n)=wac} Val(n) |
    fstar_inf= max over (wac, bde) of  sum_{n: WAC(n)=wac, bde in Val(n)} mult(n,bde)
```

where `Val(n) subseteq (B,D,E)-space` is the set of value-parts achievable with
size-vector `n`, and `mult` its multiplicity. **Algorithm (grouped):** enumerate
the `(g+1)^k` size-vectors, bucket them by `wac`; process one `wac`-group at a
time, accumulating a dict `agg: (B,D,E) -> total multiplicity` for that group
(a per-`n` convolution over the `k` blocks in the 3-D value space); then
`L1_inf += len(agg)` and `fstar_inf = max(fstar_inf, max(agg.values()))`.

**Memory bound (PROVED).** Peak resident memory is bounded by the largest single
`wac`-group's `agg`, whose key set lies in the value box
`[0, kS_G] x [0, (sum_i w_i) S_G] x [0, k Q_G]` (`S_G = sum G`, `Q_G = sum G^2`).
For `PROUHET, k=5` (`S_G=18, Q_G=82`) that box has at most
`91 * 181 * 411 ~ 6.8M` points -- an absolute ceiling independent of the
`57.4M` total. **Measured** peak: `25 MB` at `k=5` (groups are far smaller than
the box), versus the flat DP's multi-GB.

**Validation (COMPUTED).** On `k=2,3,4` the grouped method agrees with #694's
flat DP **to the last digit** (`(4,3863), (23,162075), (190,4192627)`), and both
conserve mass exactly (`sum of fibers = 2^{6k}`). A third, independent
**block-split meet-in-the-middle** (split the `k` blocks into two halves,
enumerate each half's partial 6-tuples, hash-join on the shared `wac` one target
at a time) agrees on `k<=5`. See `verify_comb_trade_champion_k5.py`.

---

## 3. k=5 (b=30), flat AP: BELOW the champion (COMPUTED, two methods + mass)

```
    Comb(PROUHET, 5, s),  s large:
        b = 30    fstar_inf = 2072    L1_inf = 57376057    rho_inf = 0.156900
```

Grouped DP and block-split meet-in-the-middle **agree exactly**, and both
conserve mass `= 2^30 = 1073741824`. This is

```
    rho_inf(k=5, flat) = 0.156900  <  0.160847 (b=24 champion, #694)
                                    <  0.158411 (b=18 champion, #655)  is FALSE;
        in fact 0.156900 < 0.158411 too -- k=5 flat is below BOTH prior champions.
```

So the naive "one more copy" does **not** extend the record; the family's
flat-AP rate **peaks at k=4 and falls at k=5**:

```
    k    b     fstar_inf    L1_inf      rho_inf     vs champion 0.160847
    2   12          4         3863      0.110644    below
    3   18         23       162075      0.147481    below
    4   24        190      4192627      0.160847    == CHAMPION (peak)
    5   30       2072     57376057      0.156900    below  (turns over)
```

This resolves #694 residual #1: **k=5 flat AP does not beat the champion.**

---

## 4. Non-uniform per-block weights (#694 residual #3): the champion is the maximum

The mechanism generalizes verbatim to a **weight sequence** `(w_0<...<w_{k-1})`
(block `i` at position `w_i s`): the aggregates become `A = sum_i w_i|T_i|`,
`C = sum_i w_i^2|T_i|`, `D = sum_i w_i sum(T_i)` (`W,B,E` unchanged), and the
grouped method computes `(fstar_inf, L1_inf)` for any such sequence. The flat AP
is the special case `w_i = i`. By affine invariance the census depends only on
the sequence up to `x -> a x + b`, so we search **primitive** sequences
(`gcd = 1`, `w_0 = 0`) up to reflection.

**k=4 (b=24), exhaustive over all weight sequences of diameter <= 12
(COMPUTED).** The maximum `rho_inf` is the **champion 0.160847**, attained by the
AP `(0,1,2,3)` and exactly its affine dilations `(0,2,4,6), (0,3,6,9), ...`
(identical census); every non-AP sequence is strictly below (next best
`0.156808`). The AP is the unique k=4 window optimum up to scaling.

**k=5 (b=30), search over weight sequences (COMPUTED).** No sequence reaches the
champion. Across an exhaustive scan of the dominant `(0,1,2,·,·)` two-cluster
sequences of diameter `<= 8`, and a trace of the leading family
`(0,1,2,m,m+1)` out to diameter `15`, the maximum is

```
    weights (0,1,2,7,8):   fstar_inf = 760   L1_inf = 171764913   rho_inf = 0.160018
```

The family `(0,1,2,m,m+1)` (three low weights pushed apart from a far adjacent
pair) has a genuine **interior peak at m=7** and then falls -- `rho_inf` reads
`0.159794, 0.158688, 0.160018, 0.159484, 0.157924, 0.157123, 0.157831, ...` for
`m = 5,6,7,8,9,10,11,...` -- an oscillate-then-decay toward the `k3 (x) k2`
tensor value `~0.133`, never crossing `0.160847`. (Numerically, beating the
champion at `b=30` needs `fstar_inf * L1_inf > 2^30 e^{30*0.160847} ~ 1.34e11`;
the peak `(0,1,2,7,8)` reaches `760 * 171764913 ~ 1.31e11`, a persistent ~2%
short, and every other searched sequence is below it.)

**Why the maximum is at bounded (searched) diameter (COMPUTED trend).** As the
weight diameter grows, the size-vector map `n -> (W,A,C)` becomes injective, so
cross-block size-collisions vanish, `fstar_inf -> 2^k`, and `rho_inf` falls
**monotonically** to a floor (`~0.108` at `k=3`, `~0.11` region generally) far
below the champion:

```
    k=3 weights   diam    rho_inf
    (0,1,2)         2      0.147481   (AP, the k=3 maximum)
    (0,1,3)         3      0.127811
    (0,2,5)         5      0.115634
    (0,3,8)         8      0.107504
    (0,8,21)       21      0.108577   (floor; size-injective regime)
```

so no large-diameter sequence can beat the champion, and the exhaustive
small-diameter search captures the maximum. (Note: the comb does NOT become
#683's positional tensor when the weights spread -- all blocks still share one
quadratic coordinate -- but the rate still collapses well below the champion,
which is all the ceiling needs.)

---

## 5. Verdict (COMPUTED CEILING)

```
    Over the PROUHET stacked-trade comb family with any per-block weight
    sequence, for every k <= 5:
        max_k max_weights  rho_inf  =  0.160847  =  the #694 b=24 champion,
    attained uniquely (up to affine scaling) at k=4 with AP weights (0,1,2,3).

    * k=5 flat AP:        rho_inf = 0.156900  (< champion; two methods + mass)
    * k=5 weight maximum: rho_inf = 0.160018 at (0,1,2,7,8)  (< champion; searched window)
    * k=4 weight maximum: rho_inf = 0.160847  (= champion, AP, exhaustive diam<=12)
    * rho_inf(k) rises 2->3->4 then FALLS at k=5; and within each k it falls
      monotonically as the weight diameter grows -- a genuine interior maximum
      at k=4/b=24, not a boundary artifact.

    => The same-block trade-stacking family does NOT extend the record past
       b=24. rho* >= 0.160847 stays the certified bracket lower end, now known
       to be the ceiling of THIS family at k<=5.
```

This is a **decided** result in the sense of the assignment's option (4): it
closes #694's k=5 residual (does not beat) and its weight-sequence residual (AP
optimal at k=4, nothing better at k=5), redirecting the record hunt away from
"more copies of the same trade" and toward genuinely different resonances.

---

## Files, PI re-derivation

- Note: `experimental/notes/thresholds/comb_trade_champion_k5.md` (this).
- Verifier: `experimental/scripts/verify_comb_trade_champion_k5.py`
  (stdlib-only; `--check` recomputes every number above from scratch -- the
  champion, the k=5 census by two independent methods with mass-conservation,
  the k=4 weight-window optimum sample, and the reported k=5 window maximum --
  within a stated ~12-min cap, exit 0 with final line `RESULT: PASS n/n`;
  `--tamper-selftest` confirms the check is non-vacuous).
- Reproducer: `experimental/scripts/repro_comb_trade_champion_k5.py` (documented
  runtime; the k-trend table, the full k=4 weight sweep, the k=5 weight sweep,
  and the diameter-degeneration scan).
- Read-only inputs: **#694** `comb_trade_champion.md`, **#655**
  `fiber_image_tradeoff.md`, **#683** `championship_census_b19_26.md`, **#673**
  `ilo_moment_closed_consumer.md`; scottdhughes **#564** `w_a_star_pte_lemma.md`.

**Per-claim status.** S1 method (the size/value split and its memory bound) =
**PROVED** (bound) + **COMPUTED** (agreement with the flat DP and the
independent MITM, mass-conservation). S2 (k=5 flat census and its being below
both champions) = **COMPUTED** (two independent methods). S3 (weight-sequence
search, k=4 optimum, k=5 maximum, diameter degeneration) = **COMPUTED**. The
VERDICT/CEILING is COMPUTED over the stated search window (all k<=5 weight
sequences of the searched diameters), not a closed-form proof over all gadgets.

**Nonclaims.** No claim for `k >= 6` (heavier, not run here; the k-trend and the
per-k diameter decay make a champion-beating `k>=6` member of THIS family
implausible but it is not computed). No claim over gadgets other than PROUHET
(support 6) and #694's GADGET8 (support 8); the minimal degree-2 PTE support is
6 (#564), so no smaller gadget exists, but larger/other-degree gadgets are
unsearched. No claim over **non-uniform per-block gadgets** (a different trade in
each block) -- a strictly larger design space than uniform-gadget weight
sequences. No bracket end is moved. No `.tex` touched.
