# Balanced-core kappa growth: raw versus factored rank

**Lane:** residual (1) of PR #528 (`thresholds-ray-compiler-balanced-core`) ---
the kernel-growth question for the balanced core, not the atlas-count question.
**Target:** `experimental/asymptotic_rs_mca_frontiers.tex`; no TeX or PDF is
edited here.

**Correction notice.** The first version of this note mixed two different RS
rows. Its raw-family identity was correct, but its post-factor inference kept
the original dimension `k` after shortening by a common agreement core. The
factor-aware audit in
`experimental/notes/audits/balanced_core_factored_rank_audit.md` gives an exact
actual-line counterexample to that inference.

**Corrected verdict:**

- `PROVED`: the raw-family identity
  `kappa = max(0, k - |intersection S_gamma|)`.
- `COMPUTED`: raw empty-core prefix families, including the PTM family and the
  finite census below, can have `kappa = k = Theta(n)`.
- `COUNTEREXAMPLE`: after a common core `K` with `|K|<=k` is factored, an empty
  residual core implies `kappa = k' = k - |K|`, not the original `k`; a larger
  raw core already has zero nullity.
- `OPEN GAP`: prove `k - |K| = Theta(n)` for a positive-rate actual first-match
  balanced-core residual, or pay the shortened row by another certified route.
- `NO ISSUE`: the governing TeX already uses the shortened dimension in
  `thm:fixed-core-determinacy-ray`.

Credit remains with PR #528 for the field-independent per-chart bound
`|Z| <= C(R+kappa,kappa+1)` and for isolating kernel growth as an open wall.
This correction narrows what the experiments establish; it does not change
that theorem.

---

## 1. Two rows, two dimension parameters

Let `C = RS_F(D,k)`, `|D|=n`, and `R=n-k`. For a nonempty raw family of
agreement supports `{S_gamma}`, put

```
    C_raw = intersection_gamma S_gamma,
    U_raw = union_gamma (D \ S_gamma) = D \ C_raw.
```

For an RS Vandermonde parity check,

```
    rank H_U = min(|U|,R),
    kappa_raw = dim ker H_U
              = max(0, |U_raw|-R)
              = max(0, k-|C_raw|).                         (K-raw)
```

This set/rank identity is exact. The existing
`experimental/scripts/verify_kappa_growth.py` checks it over every enumerated
raw prefix class.

Now fix a common core `K subseteq C_raw`, `c=|K|<=k`, and divide the locator
and received-word data by `Q_K`. This is shortening, so the new row is

```
    D' = D \ K,      n' = n-c,
    k' = k-c,        R' = n'-k' = R.                       (S)
```

For `S'_gamma=S_gamma\K` and
`C'=intersection_gamma S'_gamma=C_raw\K`, the residual rank law is

```
    kappa' = max(0, k'-|C'|).                              (K-short)
```

If the full common core is factored in this range, then `C'=empty` and

```
    kappa' = k' = k-|K|,                                  (F)
```

not the original `k`. Numerically, full-core shortening preserves the correctly
computed raw nullity `k-|C_raw|`; it changes the row dimension against which an
empty residual core is interpreted. This is also the law in
`experimental/notes/thresholds/common_core_cover_obstruction.md`, equations
(2.5)--(2.6).
If `|C_raw|>k`, `(K-raw)` already gives `kappa_raw=0`; no negative-dimensional
shortened row is formed.

The moving-coefficient projective dimension `d_proj` is a separate parameter.
It selects the pencil/curve/balanced-core tool, whereas `kappa` measures the
error-union kernel. Neither parameter determines the other.

---

## 2. Exact factor-aware counterexample

Over `F_11`, take

```
    D={1,...,7}, n=7, k=2, R=5, a=4, w=1,
    S0={1,2,3,7}, S1={1,2,4,6}, S2={1,3,4,5}.
```

The monic locator coefficient vectors are

```
    [1,9,9,5,9], [1,9,1,7,4], [1,9,4,3,5].
```

They share the depth-one prefix `[1,9]` and have full common core `K={1}`.
After factoring `X-1`, the residual supports are

```
    {2,3,7}, {2,4,6}, {3,4,5},
```

with empty intersection and projective deep-coefficient dimension `2`. The
shortened row has

```
    D'={2,...,7}, n'=6, k'=1, R'=5,
    rank H_{D'}=5, kappa'=6-5=1=k' != k=2.
```

The audit certificate also realizes these three supports on one transverse RS
syndrome line, so this is not merely a locator proxy. The exact verifier checks
the line equations, transversality, factorization, rank, and a complete census
of all `1,140` triples of four-supports containing `1`.

---

## 3. What the original experiments still prove

### 3.1 Raw PTM family

`disjoint_equal_prefix_pair` uses a tiled Prouhet--Thue--Morse split to produce
disjoint equal-prefix supports. Here `C_raw=empty`, so no shortening occurs and
`k'=k`; the following exact raw examples remain valid:

| n | a | k | R | raw kappa | log2 C(R+kappa,kappa+1) | / n |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 8 | 5 | 11 | 5 | 13.0 | 0.81 |
| 32 | 16 | 13 | 19 | 13 | 28.8 | 0.90 |
| 64 | 32 | 29 | 35 | 29 | 60.5 | 0.945 |
| 128 | 64 | 61 | 67 | 61 | 124.1 | 0.969 |

These are raw empty-core shift-pair examples. They show that high kernel is
possible; they do not prove that a positive-rate balanced-core residual with
that kernel survives the full first-match atlas.

### 3.2 Raw depth-two census

The existing verifier exhaustively groups all `a`-subsets by their depth-two
locator prefix and recomputes `(K-raw)` in two ways:

| p | n | k | classes | raw higher-dimensional classes | largest raw class (size, d_proj, kappa, core) | frac(kappa=k) |
|---:|---:|---:|---:|---:|:---|---:|
| 13 | 12 | 5 | 169 | 97 | (5, 4, 5, 0) | 0.26 |
| 17 | 14 | 6 | 289 | 288 | (11, 7, 6, 0) | 0.84 |
| 17 | 16 | 7 | 289 | 289 | (32, 8, 7, 0) | 1.00 |
| 19 | 18 | 8 | 361 | 361 | (95, 9, 8, 0) | 1.00 |

This is an exact census of raw prefix-support families. Class size is not the
number of realized slopes, and a largest raw class is not automatically a
largest actual first-match ray cell. Consequently the table does not establish
that high `kappa` is generic or dominant among actual rays. That projection is
part of hard input 3.

---

## 4. Corrected wall

The PR #528 secant bound is subexponential when the **actual shortened** kernel
satisfies `kappa'=o(n/log n)`. It is exponential on the displayed raw
empty-core constant-rate families, but residuality alone does not force that
regime. A post-factor conclusion requires control of the shortened dimension

```
    k' = k-|K|.
```

The missing input is therefore one of:

1. prove that actual first-match balanced-core cells have
   `k-|K|=o(n/log n)` and use the secant compiler;
2. prove that any large-mass residual has `k-|K|=Theta(n)` and pay it through a
   certified atlas or Sidon/Fourier route; or
3. obtain a structure-sensitive per-chart estimate not captured by the current
   uniform binomial bound.

Sharpness of `C(R+kappa,kappa+1)` for `kappa<=2` does not rule out a different
large-kernel, structure-sensitive estimate. Profile complexity still controls
the number of realized profiles, not the kernel within one profile.

---

## 5. Verification and status

- `experimental/scripts/verify_kappa_growth.py`: validates the raw PTM and raw
  prefix-census statements. It does **not** verify the old factor step.
- `experimental/scripts/verify_balanced_core_factored_rank.py`: validates the
  shortened-row law and the exact `F_11` transverse counterexample, including
  optimized-mode and tamper-rejection gates.
- `experimental/data/certificates/balanced-core-factored-rank/`: deterministic
  checked certificate for the counterexample and census.

**Per-claim status:** `(K-raw)` and `(K-short)` are `PROVED`; the PTM and raw
census are `COMPUTED`; retaining original `k` after factorization is
`COUNTEREXAMPLE`; positive-rate shortened balanced-core growth is `OPEN GAP`.
No theorem row, asymptotic closure, or TeX statement is promoted by this note.

**Next action:** control `|K|` and realized slope mass in the actual first-match
atlas. Re-derive the factor/shortening boundary before using any raw prefix
census as evidence about residual rank.
