# Rank-16 fixed-core global-owner counterexample

**Claim:** A literal same-word source construction defeats any total map from
the post-#861 residual to valid fixed-27 or fixed-26 cells selected from a
candidate's actual complete-error labels. On the top witness, the natural
core incidence projections have exact degrees 28 and 378.

**Status:** Counterexample to one proposed globalization mechanism. Finite
ledger delta `0`; no local fixed-core cap or rank-16 parent is refuted.

**Verifier:**
`experimental/scripts/verify_rank16_fixed_core_global_owner_counterexample.py`
reconstructs the integrated #838 baseline and pending #861 ledger, checks the
field and subgroup orders, exact fiber counts, intersections, cell survival,
source degrees, and incidence multiplicities.

**Consumers:** Audits that attempt to globalize the fixed-27/fixed-26 local
packets #826/#843/#846/#862/#863.

**Risk limits:** The theorem concerns one deployed finite row, audited PR #861
head `bc04696d8ebbc4103463a41c3d7a68b4cc202c5a`, and one proposed owner. It
does not disprove a marked-incidence aggregation, occupied-source-key cap,
local algebraic theorem, Grand List, or Grand MCA.

## Literal construction

Use

```text
p=2,130,706,433, n=2^21, K=2^20, m=1,116,047,
t=n-m=981,105, a=m-K+1=67,472, B=32,768.
```

Let `omega=3^1016` in `F_p`. It has order `n`; `zeta=omega^B` has order 64.
Write the 64 complete `q64` fibers as

```text
H_j = {omega^(j+64k) : 0<=k<B}.
```

Define a top error complement `E_1` by taking initial segments in the fibers
with counts

```text
28 copies of 32,768; 25 copies of 1,767; 11 copies of 1,766.
```

Define a lower error complement `E_0` by counts

```text
20 copies of 30,358; 8 copies of 30,359;
8 copies of 3,642; 17 copies of 3,641; 11 copies of 3,640.
```

Both have size `t`. Every lower fiber is nonempty and nonfull. The top
complement has exactly the complete labels `0,...,27`, with residual degree
63,601 touching all other 36 fibers. Coordinatewise minima give

```text
|E_0 intersect E_1| = 913,633.
```

For `S_i=H minus E_i`, this implies

```text
|S_0|=|S_1|=m,
|S_0 intersect S_1|=1,048,575=K-1,
|E_i minus E_(1-i)|=67,472=a.
```

Put `A=S_0 intersect S_1`, `P_0=0`, and

```text
P_1(X)=product_{x in A}(X-x).
```

Then `P_1` is monic of degree `K-1<K` and has no roots in `H minus A`.
Partition `H` into `A`, `S_0 minus S_1`, `S_1 minus S_0`, and
`E_0 intersect E_1`. Define `U` to equal zero on `S_0`, `P_1` on
`S_1 minus S_0`, and on the common-error part choose 1 unless `P_1(x)=1`,
in which case choose 2. Therefore

```text
Agr(U,P_0)=S_0,  Agr(U,P_1)=S_1
```

exactly. Since each agreement set has exactly `m` points, these are the
canonical first-`m` sets under any fixed total order.

## Survival after pending PR #861

Every error fiber is touched for both candidates, so neither agreement set
contains a complete `q64` block; both have profile `(0,0,0,0,0,0)`. This
profile is outside `D`, `Q110`, and `Q41` and has nonpaired-`f64=28` X-rank
501, outside `X175`.

The lower witness has `f64=0`; its Johnson denominator is nonpositive, so it
is outside `J48`. The top labels `0,...,27` contain no pair under
`j -> j+32`, hence the top witness is outside the paired owner `M`; `J48`
uses only exact `f64=26,27`. Both candidates therefore survive the #861
first-match order.

The lower witness has no actual 26- or 27-label complete-error core. Thus no
total source-preserving function can map every residual candidate into a
valid fixed-26/fixed-27 cell selected from its actual complete-error labels.

## Exact top-layer incidence

Let `L_1=G_F R` be the top error locator, where

```text
F={zeta^j:0<=j<=27},
G_F=product_{y in F}(X^B-y),
deg R=63,601.
```

The residual `R` is monic, squarefree, split over `H`, has no root in the 28
full fibers, has no additional complete `q64` fiber, and has footprint 36.
Take

```text
g=X^a, eta=L_1 mod g.
```

The generator is monic and root-free on `H`. Since all roots of `L_1` are
nonzero, its constant term is nonzero, so `eta` is a nonzero residue ray.

For every 27-subset `C` of `F`, cancel `G_C` and put

```text
h_C = (G_C^(-1) eta) mod g.
```

If `F minus C={y}`, then

```text
(X^B-y)R = h_C + gW_C,
deg((X^B-y)R)=96,369,
deg W_C<=28,897.
```

This is the literal fixed-27 post-core equation. There are exactly
`binom(28,27)=28` such core incidences.

For every 26-subset `C`, write `F minus C={y,z}`. Cancelling `G_C` and the
two remaining fiber factors modulo `g` recovers `R` itself, because
`deg R=63,601<a`. This is the fixed-26 compiler with all the same source data
and exactly `binom(28,26)=378` core incidences.

The generator and projective ray are the same across all cores; the reduced
representatives indexed by the cores are allowed to vary. Thus the correct
top-layer object is a marked incidence relation whose projection degree is
28 or 378, not a multiplicity-one owner function.

## Consequence and nonclaims

The result contributes no payment. It forbids two shortcuts:

1. mapping the entire residual into top fixed-core cells, because the lower
   witness has no such core;
2. treating all core incidences as multiplicity one on the top lane.

A paying globalization must first split off the lower-`f64` lane and then
bound the marked top incidence relation through a canonical source-key or
occupied-cell theorem. The result does not refute local caps six or 116,
G64-CAP, seven-star exclusion, another global owner, an asymptotic theorem,
or either official prize question.
