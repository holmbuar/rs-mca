# Effective-image MI+MA: an absolute-dual-mass floor on the half slice

**Status:** `PROVED / COUNTEREXAMPLE_NEW_FLOOR / CONDITIONAL_ON_NAMED_INPUT`
**Hard input:** Grande Finale v3 Sidon/Fourier payment, or an equivalent effective-image MI+MA proof
**New floor:** `ABSOLUTE_EFFECTIVE_DUAL_L1_FLOOR`
**Named residual:** `RS_PHASE_STRUCTURED_SIDON_PAYMENT`

## Source pins

- fork base: `holmbuar/rs-mca` `main` at
  `b410c7ee14488bb751c5a89df10cb5b0323e3669`;
- `experimental/grande_finale.tex` blob
  `759678e30639972e4f64b438d3d6ba76ff3ddf8f`;
- `experimental/rs_mca_thresholds.tex` blob
  `01302a797c502a05ed0b11ba949b8756e0aa2b22`;
- `experimental/notes/audits/sidon_direct_payment.md` blob
  `34c7f2e1ea2be8106a700aca1a744af73f0b3784`.

No open PR is a theorem dependency of this packet.

## Claim attacked

The active v3 Fourier interface starts with a fixed-weight slice

\[
\Omega_{T,m}=\{x\in\{0,1\}^{T}:\sum_{t\in T}x_t=m\},
\qquad
\Psi(x)=\sum_{t\in T}x_tg(t),
\]

and performs Fourier inversion on the effective difference span

\[
V_g=\operatorname{Span}_{\mathbb F_p}
   \{g(t)-g(t_0):t\in T\},
\qquad A_{\rm eff}=|V_g|,
\]

as in `eq:effective-fourier-span` and `lem:effective-span-fourier` of
`experimental/grande_finale.tex`.  Put

\[
M=|\Omega_{T,m}|,\qquad
L=|\Psi(\Omega_{T,m})|,\qquad
\bar N^{\rm img}=M/L.
\]

The exact finite effective Fourier multiplier from
`def:effective-fourier-payment`, `prop:effective-mi-ma-flatness`, and
`cor:exact-finite-fourier-constants` is

\[
\kappa_{\rm abs}
 =1+\frac1M\sum_{1\ne\chi\in\widehat{V_g}}
 \left|e_m\bigl(\chi(g(t)-g(t_0)):t\in T\bigr)\right|.
\tag{1}
\]

Any partition into effective minor and major characters has

\[
C_{\rm min}+C_{\rm maj}=\kappa_{\rm abs}-1.
\tag{2}
\]

The proposed universal implication being tested is:

> correct effective-image normalization, together with a perfect or
> subexponential image-normalized Q/Sidon bound, should force a
> subexponential absolute-value MI+MA payment in (1).

That implication is false, even when the full-image certificate holds with only
polynomial loss.

## Relation to the existing direct-Sidon audit

`experimental/notes/audits/sidon_direct_payment.md` records the orthogonal
phenomenon: an explicit fixed-weight Boolean map whose literal
image-normalized Sidon-heavy moment is large.  The present packet does not
repeat that counterexample.  Here the direct Sidon-heavy moment is exactly zero,
while the absolute effective-dual Fourier mass is exponentially large.  Taken
together, the two packets separate three logically different statements:

1. correct ambient/effective/image normalization;
2. direct `def:sidon-paid-cell` control; and
3. absolute-value `(MI)+(MA)` control.

Neither of the last two is an equivalent reformulation of the other without
additional phase structure.

## Denominator and field ledger

This packet is an additive-boundary falsifier, not an MCA/list threshold row.
The ledgers are therefore printed rather than silently identified.

| object | value in this packet |
|---|---|
| coefficient/generated field | `q_gen = |B| = 2`, with `B = F_2` |
| ambient Fourier target | `A_amb = |B|^N = 2^N` |
| effective Fourier target | `A_eff = 2^(N-1)` |
| realized image target | `L = binom(N,N/2)` |
| image-normalized average | `barN_img = M/L = 1` |
| ambient average | `barN_amb = M/A_amb` |
| MCA line denominator | `q_line = NOT_INSTANTIATED` |
| verifier challenge denominator | `q_chal = NOT_INSTANTIATED` |
| list denominator | `q_list = NOT_INSTANTIATED` |
| Sidon moment order | `q_mom`; this is not a field-size denominator |

Neither `A_amb`, `A_eff`, nor `L` is an MCA, challenge, or list denominator.
No claim about `eq:intro-normalized-mca` or the finite budget in
`eq:intro-asymptotic-threshold` of `experimental/rs_mca_thresholds.tex` is made.

## The half-slice family

Fix an integer `r >= 1` and put

\[
N=4r,\qquad T=\{1,\dots,N\},\qquad m=2r=N/2.
\]

Let `W = F_2^N`, let `e_t` be the standard basis vector, and set

\[
g(t)=e_t,
\qquad
\Psi(S)=\sum_{t\in S}e_t=\mathbf 1_S.
\]

The full slice is the middle Hamming sphere.

### Claim 1 — effective span and image normalization

**Status:** `PROVED`.
**Normalization in this claim:** `M=L=binom(N,N/2)`, `barN_img=M/L=1`, `A_eff=2^(N-1)`, `A_amb=2^N`; `q_line`, `q_chal`, and `q_list` are not instantiated.

For any anchor `t_0`,

\[
V_g=\{v\in\mathbb F_2^N:\sum_i v_i=0\},
\qquad A_{\rm eff}=2^{N-1}.
\tag{3}
\]

The map `S -> 1_S` is injective, so

\[
M=L=\binom{N}{N/2},
\qquad \bar N^{\rm img}=1.
\tag{4}
\]

Every full-slice fiber, and hence every residual fiber obtained by deletion, has
size at most one.  Thus `def:primitive-q` holds with exact loss one on the full
slice.

Moreover, because the largest binomial coefficient is at least the average of
the `N+1` binomial coefficients,

\[
L=\binom N{N/2}\ge \frac{2^N}{N+1}.
\tag{5}
\]

Consequently

\[
\frac{A_{\rm amb}}L\le N+1,
\qquad
\frac{A_{\rm eff}}L\le\frac{N+1}{2}.
\tag{6}
\]

The `eq:full-image-certificate` gap is therefore only `O(log N)` in the
logarithm.  This example is not an exponential effective-image collapse.

**Proof.**  The vectors `e_t+e_{t_0}` span the even-parity hyperplane, proving
(3).  Equation (4) is injectivity of incidence vectors.  Equations (5)--(6) are
the elementary averaging bound on the binomial expansion of `2^N`.  ∎

### Claim 2 — exact direct Sidon payment

**Status:** `PROVED`.
**Normalization in this claim:** every moment uses the full-slice realized-image average `barN_img=M/L=1`; `q_mom` is a moment order, while `q_line`, `q_chal`, and `q_list` remain uninstantiated.

For every attained target `s`, the full-slice fiber `F_s` is a singleton.
Hence

\[
f_s=1,\qquad E(F_s)=1,\qquad \Delta_s=E(F_s)/f_s^3=1.
\]

For every fixed `sigma > 0`, one has `exp(-sigma N) < 1`, so no nonempty
full-slice fiber lies in the Sidon-heavy cut.  After arbitrary first-match
deletion, every surviving nonempty fiber is still a singleton; deleted fibers
have `f_s=0` and contribute zero to the moment.  Therefore the
image-normalized Sidon-heavy moment of `def:sidon-heavy` is

\[
\Gamma^{\rm sid}_{q_{\rm mom},\sigma}=0
\tag{7}
\]

for every admissible positive moment order `q_mom`, on the full slice and on every residual subset.
In particular `def:sidon-paid-cell` holds exactly, not merely up to
`exp(o(N q_mom))`.

### Claim 3 — exponential absolute effective-dual mass

**Status:** `PROVED / COUNTEREXAMPLE_NEW_FLOOR`.
**Normalization in this claim:** the absolute character mass is divided by the source mass `M` exactly as in `(EF6)`/`def:effective-fourier-payment`, and the dual is `widehat(V_g)` with size `A_eff`; neither `A_amb`, `L`, `q_line`, `q_chal`, nor `q_list` is substituted for that denominator.

Characters of the even-parity space in (3) are represented by vectors
`y in F_2^N` modulo `y ~ y + 1`.  Let `Y` be the support of a representative.
Translation by `g(t_0)` changes the fixed-weight Fourier coefficient only by a
unit phase, so its magnitude is

\[
\left|K_m(|Y|)\right|,
\qquad
K_m(j)=[z^m](1-z)^j(1+z)^{N-j}.
\tag{8}
\]

Take `|Y|=N/2=2r`.  Then

\[
K_{2r}(2r)
 =[z^{2r}](1-z)^{2r}(1+z)^{2r}
 =[z^{2r}](1-z^2)^{2r}
 =(-1)^r\binom{2r}{r}.
\tag{9}
\]

There are exactly

\[
\frac12\binom{4r}{2r}=\frac M2
\tag{10}
\]

such nontrivial effective characters, because complementation pairs the
middle-weight representatives.  Hence

\[
\sum_{1\ne\chi\in\widehat{V_g}}|E_m(\chi)|
 \ge \frac M2\binom{2r}{r}.
\tag{11}
\]

Every constant `kappa` satisfying the effective Fourier payment `(EFP)` must
therefore obey

\[
\boxed{
\kappa\ge 1+\frac12\binom{2r}{r}
}
\tag{12}
\]

and the elementary central-binomial averaging bound gives

\[
\kappa
 \ge 1+\frac{2^{2r-1}}{2r+1}
 =\exp\!\left(\frac{\log 2}{2}N-O(\log N)\right).
\tag{13}
\]

For every effective minor/major partition, nonnegativity and (11) give

\[
\boxed{
\max\{C_{\rm min},C_{\rm maj}\}
 \ge \frac14\binom{2r}{r}
}
\tag{14}
\]

for the source-normalized constants in `(MI)` and `(MA)`.  At least one side
therefore has the same exponential-rate floor.  The two absolute-value
payments cannot both have subexponential loss on this family.

### Theorem — the universal absolute-MI+MA equivalence is false

**Status:** `COUNTEREXAMPLE_NEW_FLOOR`.
**Normalization in this theorem:** Q and Sidon use `barN_img=M/L=1`; the Fourier loss is the `(EF6)` source-normalized absolute mass over `widehat(V_g)`; all MCA/list denominators are absent.

There is a fixed-density sequence of additive boundary maps for which:

1. the realized-image normalization is exact: `barN_img = 1`;
2. primitive Q holds with exact loss one;
3. the Sidon-heavy moment is identically zero at every fixed `sigma > 0` and
   every moment order;
4. the full-image certificate holds with polynomial, hence subexponential,
   loss; but
5. every absolute-value effective MI+MA payment has multiplier at least the
   exponential quantity in (12)--(13).

Therefore an absolute sum over the entire nontrivial effective dual is a
strictly stronger demand than the v3 Sidon moment payment.  Correcting the
ambient/effective/image denominator does not remove this separate
`ABSOLUTE_EFFECTIVE_DUAL_L1_FLOOR`.

Equivalently, the following universal implication is falsified by the displayed
family:

```text
(eq:full-image-certificate)
+ exact (def:primitive-q)
+ exact (def:sidon-paid-cell)
=> subexponential (def:aggregate-minor-payment)
 + subexponential (def:major-arc-aggregate).
```

The falsifier is explicit for every `N=4r`: `B=F_2`, `g(t)=e_t`, and the
weight-`N/2` slice, with all scales printed in the denominator ledger above.

## Exact finite regression: `N=8`

**Status:** `PROVED` as a consequence of Claim 3; the Lean executable certificate is `AWAITING_FORK_CI`.
**Normalization:** `M=L=70`, `barN_img=1`, `A_eff=128`, `A_amb=256`; `q_line`, `q_chal`, and `q_list` are not instantiated.

Take `r=2`, so `N=8` and `m=4`.  Then

\[
M=L=\binom84=70,
\qquad A_{\rm eff}=128,
\qquad A_{\rm amb}=256.
\]

There are `35` middle-weight effective character classes.  Every one has
Fourier magnitude

\[
\binom42=6,
\]

so those characters alone contribute absolute mass `35*6=210` and force
`kappa >= 4`.  The full effective dual has 128 character classes, represented
uniquely by binary vectors with coordinate zero fixed to zero.  Excluding the
trivial class, the exact magnitude census by representative weight is

| weight | class count | coefficient magnitude | mass |
|---:|---:|---:|---:|
| 1 | 7 | 0 | 0 |
| 2 | 21 | 10 | 210 |
| 3 | 35 | 0 | 0 |
| 4 | 35 | 6 | 210 |
| 5 | 21 | 0 | 0 |
| 6 | 7 | 10 | 70 |
| 7 | 1 | 0 | 0 |

Thus the complete nontrivial absolute mass is `490`, and

\[
\kappa_{\rm abs}=1+\frac{490}{70}=8
\tag{15}
\]

exactly.  At the same time every image fiber is a singleton and the direct
Sidon-heavy moment is zero.  The stdlib-only package
`experimental/lean/sidon_effective_image/` checks `M=L=70`, the 35 middle
coefficients of magnitude 6, all 128 effective representatives, full mass 490,
singleton fibers, the lower implications `kappa >= 4` and `kappa >= 8`, the
exact failure at `kappa=7`, and the balance at `kappa=8`.

## Ledger impact

The negative result does not refute `prop:effective-mi-ma-flatness`: that
proposition is a correct sufficient implication once `(MI)` and `(MA)` are
supplied.  It refutes the broader proof strategy that treats their
absolute-value hypotheses as an equivalent reformulation of
`def:sidon-paid-cell` after effective-image normalization.

The hard input is narrowed as follows.

### Named residual

**Status:** `CONDITIONAL_ON_NAMED_INPUT`.

`RS_PHASE_STRUCTURED_SIDON_PAYMENT` is one of the following, on every actual
post-C1--C8 primitive RS first-match leaf:

1. a direct proof of `def:sidon-paid-cell` at the realized-image scale; or
2. a phase-structured, cancellation-sensitive replacement for `(MI)+(MA)`
   that avoids the absolute effective-dual `L^1` floor above.

A theorem using the existing absolute `(MI)+(MA)` interface must additionally
prove, from the genuine weighted Vandermonde/rational phase structure of that
RS chart, that the half-slice mechanism cannot occur.  Image normalization
alone is not that theorem.

### Explicit falsifier for the named residual

A falsifier is a sequence of genuine post-C1--C8 primitive RS leaves, with the
weighted map required by `sec:primitive-leaf`, and fixed constants
`sigma,c > 0`, together with logarithmic orders `q_N`, such that

\[
\Gamma^{\rm sid}_{q_N,\sigma}
 \ge \exp(cNq_N)
\]

at the realized-image normalization.  The abstract half-slice family above is
not itself such an RS falsifier.

## Nonclaims

- This is not a Reed--Solomon received-line counterexample.
- The explicit family uses `B=F_2`.  An odd-characteristic theorem restricted
  to genuine weighted Vandermonde/rational RS phases may evade the floor, but
  it must use that phase structure rather than image normalization alone.
- It does not prove that the half-slice characters survive a C1--C8 semantic
  first-match atlas.
- It does not refute the shallow theorem `thm:sidon-resolved-payment`, whose
  pointwise phase hypotheses exclude this example.
- It does not provide a ray compiler or a distinct-slope payment.
- It does not instantiate `q_line`, `q_chal`, `q_list`, a finite `B*`, or an
  adjacent deployed row.
- The Lean regression certifies only the finite `N=8` arithmetic and executable
  census; the general proof is the argument printed above.

## Source correspondence

The exact active v3 nodes used or attacked are:

- `eq:effective-fourier-span`;
- `lem:effective-span-fourier`;
- `def:effective-major-minor`;
- `def:effective-fourier-payment`;
- `def:major-arc-aggregate`;
- `def:aggregate-minor-payment`;
- `prop:effective-mi-ma-flatness`;
- `cor:exact-finite-fourier-constants`;
- `eq:image-ambient-scales`;
- `eq:full-image-certificate`;
- `lem:image-ambient-moment-conversion`;
- `def:primitive-q`;
- `def:sidon-heavy`;
- `def:sidon-paid-cell`;
- `thm:sidon-resolved-payment`.
