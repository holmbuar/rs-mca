# M31 row-sharp Q: full-image Chebyshev toy refutes a uniform fold-primitive signed-`e_m` triangle certificate

**Status:** `PROVED FINITE COUNTEREXAMPLE / AUDIT / OPEN DEPLOYED Q`

**Target:** `experimental/grande_finale.tex`, `def:q-row-atom` and
`prob:row-sharp-q`; corrective follow-up to
`experimental/notes/thresholds/cap25_v13_m31_signed_em_inverse.md`.

**Replay:**

```text
python3 experimental/scripts/verify_m31_chebyshev_fold_primitive_star_counterexample.py --write
python3 experimental/scripts/verify_m31_chebyshev_fold_primitive_star_counterexample.py --check
python3 experimental/scripts/verify_m31_chebyshev_fold_primitive_star_counterexample.py --tamper-selftest
```

The verifier is standard-library-only.  It carries two independent exact prefix
censuses, rational enclosures for `pi` and every required cosine, source-bound
hashes, and nine tamper tests.  Its certificate is

```text
experimental/data/certificates/
  m31-chebyshev-fold-primitive-star-counterexample/
  m31_chebyshev_fold_primitive_star_counterexample.json
```

## 1. Result

The binding deployed Mersenne-31 list calibration is

```text
B*       = 16,777,215,
avg_ceil = 1,993,678,
K        = B*/avg_ceil = 8.4152079724...,
K - 1    = 7.4152079724....
```

The raw signed-`e_m` triangle route would prove a normalized max-fiber bound at
this calibration from

```text
(STAR_K)  sum_{t != 0} |E(t)| <= (K-1) C,
```

where `C` is the support-slice size and `E(t)` is the Fourier coefficient of
the prefix census.  The M31-domain note reduces `E(t)` to the signed elementary
symmetric coefficient `e_m(v_t)` and proposes controlling the primitive part
of this sum after Chebyshev-fold directions are removed.

The following exact finite example shows that **full image, average greater
than one, removal of every `T_2`-fold direction, and even the desired max-fiber
bound do not imply `(STAR_K)` for the remaining directions.**

Take

```text
p = 127,       n = 32,       m = 5,       w = 2,
C = binom(32,5) = 201,376.
```

Let `U(F_p)` be the norm-one torus in `F_p[i]`, let `H` be its subgroup of
order `32`, let `g` be the first power of the canonical order-`128` generator,
and let `D` be the `x`-projection of the twin coset

```text
gH union g^(-1)H.
```

The verifier reconstructs the domain rather than trusting a stored list.  It
checks that the lift has `64` points, the projection is exactly two-to-one,
`|D|=32`, `T_2` is exactly two-to-one on `D`, and `D` is not multiplicatively
closed.  Thus this is a faithful Mersenne/Chebyshev-domain toy, not a disguised
multiplicative subgroup.

Define

```text
Phi(S) = (sum_{x in S} x, sum_{x in S} x^2) in F_127^2
```

on the five-subsets of `D`.  Then the exact census gives

```text
|im Phi|       = 127^2 = 16,129                    (full image),
average fiber  = 201,376 / 16,129 = 12.4853...,
maximum fiber  = 26,
R_Q            = 26*127^2 / 201,376
               = 209,677 / 100,688
               = 2.08244... < K.
```

So the toy's literal max-fiber Q analogue passes the binding deployed
calibration with wide room.  Effective-image collapse is absent.

Nevertheless, after deleting all Chebyshev `T_2`-fold Fourier directions, the
remaining signed-`e_m` triangle sum violates `(STAR_K)`.  The verifier proves
the rational lower bound

```text
sum_{t_1 != 0} |E(t_1,t_2)|
  >= 1,598,306,180,642,586,439,652,124,191,350 / 10^24
   = 1,598,306.1806425864...,
```

while

```text
(K-1) C
  = 2,977,049,546,912 / 1,993,678
  = 1,493,244.920650175... .
```

The comparison is decided by the exact positive cross-multiplied margin

```text
209,458,322,699,150,447,832,767,653,562,285,300 > 0.
```

Equivalently, the certified fold-primitive triangle mass is at least

```text
7.9369248601... * C > (K-1) * C,
```

although the actual normalized max fiber is only `2.08244... < K`.

## 2. Exact meaning of “fold primitive”

This packet uses **Chebyshev-fold primitive**, not semantic first-match
primitive.

For a direction `t=(t_1,t_2)`, put

```text
f_t(x) = t_1 x + t_2 x^2.
```

The `T_2` fibers on this domain are the pairs `{x,-x}`.  Hence

```text
f_t(x) = f_t(-x) for every x in D
  iff 2 t_1 x = 0 for every x in D
  iff t_1 = 0.
```

The verifier also checks this implication exhaustively over all `127^2`
directions and all actual `T_2` fibers.  Therefore

```text
fold directions             = {(0,t_2): t_2 != 0},  count 126,
Chebyshev-fold-primitive     = {(t_1,t_2): t_1 != 0}, count 16,002.
```

Any higher `T_{2^j}` fold is already constant on `T_2` fibers, so no additional
quadratic direction is lost by this classification.

This does **not** prove that all `16,002` directions survive every earlier
semantic first-match owner.  The result is a route cut for a uniform raw or
fold-pruned Fourier triangle theorem, not a closed C1--C9 ownership statement.

## 3. Rigorous signed-`e_m` lower certificate

For each prefix target `z=(z_1,z_2)`, let `N(z)` be its exact fiber size.  For
a Fourier direction `t`,

```text
E(t) = sum_z N(z) exp(2*pi*i*(t dot z)/127).
```

By the standard support expansion, this is the signed elementary-symmetric
coefficient `e_m(v_t)` used in the M31 inverse packet.

Every direction with `t_1 != 0` has a unique representation

```text
t = c(1,u),        c in F_127^*, u in F_127.
```

For fixed `u`, define the exact phase histogram

```text
h_u(s) = sum_{z_1+u z_2=s} N(z).
```

Choose the least mode `s_u` of maximum multiplicity.  For each scalar `c`, the
support-functional inequality

```text
|E(c,cu)| >= Re(exp(-2*pi*i*a/127) E(c,cu))
```

holds for every residue `a`.  The verifier deterministically tries the nine
alignments

```text
a in {c s_u-4, ..., c s_u+4}
```

and retains the strongest certified lower support functional.

No floating-point trigonometry enters this proof.  The program encloses `pi`
using Machin's identity

```text
pi = 16 arctan(1/5) - 4 arctan(1/239)
```

with alternating-series rational remainders, then encloses every
`cos(2*pi*r/127)` by rational Taylor bounds.  After scaling by `10^24`, every
cosine interval has width at most one integer.  Summing the resulting integer
lower bounds over all `16,002` directions gives the displayed rational lower
bound.  The certificate records hashes of all selected alignments and all
projective-orbit lower totals.

The prefix fibers are independently recomputed in two ways:

1. direct enumeration of all `201,376` five-subsets; and
2. a weight-indexed dynamic program over `F_127^2`.

The two complete histograms must agree byte-for-byte before any Fourier claim
is evaluated.

## 4. Research consequence

The older M31 signed-`e_m` audit reported that above-calibration triangle
spikes appeared only in an `average << 1` regime and extrapolated that no such
spike was seen in its faithful `average >> 1` toys.  The present example has

```text
average = 12.4853... > 1,
full image,
R_Q = 2.08244... < 8.41521...,
```

but its fold-primitive triangle sum exceeds the deployed `(K-1)` allowance.
Thus the extrapolation is not a valid uniform theorem or proof interface.

The important distinction is:

```text
Q is true on the toy,
triangle/absolute-value STAR_K is false on the toy.
```

Accordingly, a viable M31 row-sharp Q proof must use at least one input absent
from this finite implication, for example:

- a quantitative deployed-scale or very-large-average hypothesis;
- the actual semantic first-match residual rather than all fold-primitive
  directions;
- cancellation between Fourier directions instead of the global triangle
  inequality;
- a mask-aware/falling-factorial estimate on the residual family; or
- a direct max-fiber inverse theorem that bypasses signed-`e_m` `L^1`.

The packet does not choose among those routes.  It removes one overbroad route
and supplies an exact regression that every replacement theorem should pass.

## 5. Nonclaims

- This is **not** a counterexample to deployed Mersenne-31 row-sharp Q.
- It is **not** a counterexample to a theorem with a quantitative
  large-average, deployed-scale, or row-specific hypothesis.
- “Fold primitive” is not the same as surviving all earlier semantic atlas
  cells.
- The packet does not prove a list or MCA upper ledger, an adjacent safe row,
  a ray compiler, or a balanced-core payment.
- The finite example does not address three-or-more-shell residuals.

## 6. Frozen replay identifiers

The generated JSON freezes the full domain, prefix histogram, and proof-choice
identifiers.  At the source head used for the packet:

```text
domain SHA-256:
  fcb72d14a05048d72351e54fd23993b14afb2e143fe92cb9731ac1a21546ac7c
prefix census SHA-256:
  fbb3b35918aa7e4c3374a553cd4f77baef48fa86532c280471085c78f77a19a0
fiber histogram SHA-256:
  101f518ac85c2b5e318e2828f68491d3722aa6a192aa50f440f8b4e2ed91ad4d
alignment SHA-256:
  a341e08f852affb797d099f6b19f5329e3fdc358e2caa6ea2d6a7ff1c826c919
projective-orbit lower SHA-256:
  548fa974d4f0abd7fb3711b529c42327a4fe0f26a2668c8e5ba50f10d46cdddb
```

A changed hash is a changed mathematical packet and requires a new audit.
