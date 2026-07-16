# Does (A4) cover high-kappa balanced cores? Factor-aware routing

**Lane:** the wall named by PR #534
(`thresholds-balanced-core-kappa-growth`): determine whether the
prefix-flatness/Sidon route `(A4)` reaches balanced-core charts on which the
transverse-secant `(RC)` estimate is too large. This is a coverage/routing
question, not a proof of `(MI)` or `(MA)`.

**Target:** `experimental/asymptotic_rs_mca_frontiers.tex`; no TeX or PDF is
edited here. **Verifier:** `experimental/scripts/verify_a4_coverage.py`
(stdlib-only, exact finite arithmetic).

**Factor-aware correction.** PR #534's raw identity and raw empty-core
experiments are valid. Its statement that factoring a common core leaves the
original dimension `k` was not. After shortening by `K` with `|K|<=k`, the row
dimension is `k'=k-|K|`, and an empty residual core gives `kappa=k'`, not the
original `k`. A larger raw common core already has zero nullity. See
`experimental/notes/audits/balanced_core_factored_rank_audit.md`.

**Corrected verdict:**

- `PROVED` (routing, shallow prefix): the small-effective-dual closure and
  residual-monotonicity criteria do not depend on either the raw or shortened
  kernel dimension.
- `COMPUTED` (raw families): the #534 census and PTM examples contain raw
  empty-core families with `kappa=k`; they are not a census of actual slopes.
- `WALL` (deep prefix): the remaining payment is the ambient-slice
  character-sum `(MI)`/`(MA)` problem.
- `OPEN GAP`: determine the factor size and realized slope mass of actual
  first-match balanced-core residuals.
- `NO COUNTEREXAMPLE`: high kernel by itself does not obstruct `(A4)` coverage.

Credit: PR #528 supplies `(RC)`, PR #534 supplies the raw prefix/kernel
experiments, LegaSage #531 isolates the residual Sidon input, and the
scottdhughes program supplies the `(MI)`/`(MA)` and inverse-theorem inputs. This
note only audits how those ingredients are routed.

---

## 1. What `(A4)` requires

On every primitive prefix leaf, `(A4)` asks for:

1. normalized Fourier inversion on the effective span
   `V_g=span{g(t)-g(t_0):t in T}`, with `A_eff=|V_g|`;
2. a certified effective major/minor partition; and
3. `(MI)` plus `(MA)`, or a separately proved image-normalized Sidon/Fourier
   moment payment.

The relevant payment axes are:

- **prefix-span entropy:** `log A_eff`, bounded by the prefix depth and field;
- **additive energy:** `Delta_s` of a support fiber; and
- **character sums:** the `(MI)`/`(MA)` phases on the ambient slice.

None of these definitions contains the error-union nullity. The raw identity

```
    kappa_raw = max(0,k-|C_raw|)
```

and the shortened identity

```
    0 <= |K| <= k,
    k'=k-|K|,
    kappa_short = max(0,k'-|C_short|)
```

(For `|C_raw|>k`, the raw max-formula gives zero nullity.)

must nevertheless be kept separate when deciding whether `(RC)`, rather than
`(A4)`, is useful.

---

## 2. Shallow-prefix routing

`thm:small-effective-dual-closure` states that if
`log A_eff=o(|T|)`, then effective `(MI)`, effective `(MA)`, the
image-normalized fiber bound, and the direct alternative used by `(RC)/(A6)`
hold with subexponential loss. A concrete sufficient condition is

```
    (a-k-1) log|B| = o(n).
```

This is a property of the ambient prefix slice. It does not ask whether the
cell's kernel is small, large, raw, or shortened. The set-inclusion statement
in `lem:residual-monotonicity` transfers a full-slice max-fiber bound to every
first-match residual.

Consequently, in the shallow-prefix regime, the closure payment reaches every
residual subfamily independently of `kappa`. This is the sense in which `(A4)`
coverage is kernel-independent. It does **not** assert that every raw prefix
member is a distinct realized slope, nor does it determine the shortened
kernel of an actual balanced-core cell.

Balanced-core charts are initially governed by `(A6)`: use `(RC)` when its
actual shortened kernel is small, or use a direct distinct-slope payment. The
closure theorem supplies the latter alternative in the shallow-prefix regime.
The rank correction changes which `(RC)` estimate applies; it does not insert a
kernel hypothesis into the closure theorem.

---

## 3. Raw PTM stress test

The Prouhet--Thue--Morse construction in PR #534 has fixed prefix depth `w=2`
and disjoint agreement supports. Its raw common core is empty, so there is no
factor to remove and `kappa_raw=k`. The exact finite data remain:

| n | a | k | raw kappa | closure exp `w log p/n` | `log2 C(R+kappa,kappa+1)/n` | pair energy |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 8 | 5 | 5 | 0.392 | 0.810 | 0.750 |
| 32 | 16 | 13 | 13 | 0.235 | 0.900 | 0.750 |
| 64 | 32 | 29 | 29 | 0.137 | 0.945 | 0.750 |
| 128 | 64 | 61 | 61 | 0.077 | 0.969 | 0.750 |

Thus the uniform secant constant is large while the shallow-prefix closure
criterion strengthens. This is a useful separation of mechanisms, but it is a
raw support-family stress test, not proof that the PTM pair is a surviving
balanced-core cell in the complete first-match slope atlas.

---

## 4. Raw prefix census

The verifier exhaustively measures the joint distribution of `A_eff`, raw
prefix-family size, raw `kappa`, and additive energy:

| p | n | k | slice `A_eff` | `log A_eff/|T|` | raw kappa range | largest raw fiber (size, kappa, Delta) |
|---:|---:|---:|:---:|---:|:---:|:---|
| 13 | 12 | 5 | p^2 | 0.427 | [0..5] | 5, 5, 0.360 |
| 17 | 14 | 6 | p^2 | 0.405 | [2..6] | 11, 6, 0.174 |
| 17 | 16 | 7 | p^2 | 0.354 | [7..7] | 32, 7, 0.062 |
| 19 | 18 | 8 | p^2 | 0.327 | [8..8] | 95, 8, 0.024 |

Exact conclusions:

- `A_eff` is fixed by the ambient slice while raw kernel and family size vary.
- The largest enumerated raw prefix fibers have empty core and decreasing
  measured energy.
- High raw kernel is compatible with a shallow-prefix closure certificate.

The table does **not** identify family size with realized distinct-slope count,
does not include the first-match removal pipeline, and does not prove that the
largest raw fiber is the largest actual ray cell. Those are precisely the
slope-projection and shortened-row parts of hard input 3.

---

## 5. The remaining wall

When `log A_eff=Theta(n)`, the trivial closure multiplier may be exponential.
Payment then reduces to genuine `(MI)`/`(MA)` cancellation, or a separate
Sidon/Fourier moment bound, on the ambient full slice. This obstruction is
still a character-sum/additive-energy condition rather than a kernel condition.

What remains unknown is how the actual balanced-core residual is distributed
after all earlier first-match owners and common factors are removed. The next
useful theorem must connect at least three quantities:

1. realized distinct-slope mass;
2. the factored size `|K|`, hence shortened dimension `k'=k-|K|`; and
3. either a small `(RC)` kernel or a valid `(A4)`/direct payment.

Sharpness of the existing binomial secant constant at `kappa<=2` does not
exclude a different structure-sensitive large-kernel estimate.

---

## 6. Proposed ledger wording

### L-A4-1 (kernel-independent shallow-prefix routing)

- **Status:** `PROVED` (routing) / `WALL` (deep-prefix) / `AUDIT`.
- **Paper impact:** cross-reference `(A6)` to the direct alternative supplied by
  `thm:small-effective-dual-closure` plus `lem:residual-monotonicity`. State
  that this coverage is independent of the **actual shortened** kernel.
- **Nonclaim:** do not cite the raw #534 census as proof that actual residuals
  retain the original `k` or that raw support-family mass equals slope mass.

### L-A4-2 (disambiguate the two kappas)

The effective-Fourier payment multiplier and the transverse-secant kernel
parameter are both written `kappa` in nearby parts of the draft. Rename or
footnote one of them; they are unrelated.

---

## 7. Verification and status

- `experimental/scripts/verify_a4_coverage.py` checks the raw PTM/census,
  effective-span, energy, and set-inclusion computations. It does not certify
  the old factor step or an actual first-match slope projection.
- `experimental/scripts/verify_balanced_core_factored_rank.py` checks the
  shortened-row law on an exact transverse `F_11` syndrome-line witness.

**Per-claim status:** shallow-prefix routing is `PROVED` from the cited draft
theorems; raw tables are `COMPUTED`; deep-prefix payment and actual-slope
projection are `WALL`; retaining original `k` after factorization is
`COUNTEREXAMPLE` in the companion audit. No main theorem or asymptotic closure
is claimed here.

**Next action:** audit the actual first-match slope atlas, recording `K`, `k'`,
and the payment owner for every surviving balanced-core cell.
