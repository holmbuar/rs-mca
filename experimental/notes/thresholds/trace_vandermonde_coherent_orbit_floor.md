---
workboard_item: T
row: binary trace-Vandermonde RS family q=2^s, s an odd prime at least 3
object: OTHER
target_epsilon: NOT_INSTANTIATED
agreement: fixed-weight source m=q/4; this is not an MCA agreement
B_star: NOT_INSTANTIATED
direct_statement: the canonical weight-q/2 trace-character orbit has image-compensated coherent Fourier aggregate at least 2^(q/4+1)/((q+1)(q/4+1))
architecture: DIRECT
partition_digest: NOT_INSTANTIATED
atom_or_cell: RS_PHASE_STRUCTURED_SIDON_PAYMENT
quantifier: every odd prime s>=3 under the integrated binary-kernel theorem for h_t=(t,t^2,...,t^(q/2-1))
projection_and_unit: coherent effective-character aggregate after exact L/A_eff compensation; not supports, rays, slopes, or codewords
claimed_bound: exp((log 2)N/4-O(log N))
status: COUNTEREXAMPLE
impact: ROUTE_CUT
falsifier: q=8, N=7, R=3, m=2, M=L=21, A_eff=64, 35 genuine trace-Vandermonde characters each have coefficient -3, coherent magnitude 105
replay: python3 experimental/scripts/verify_trace_vandermonde_coherent_orbit_floor.py --check; python3 -O experimental/scripts/verify_trace_vandermonde_coherent_orbit_floor.py --check; repeat both modes with --tamper-selftest
---

# Trace--Vandermonde coherent phase-orbit floor

**Verdict:** `COUNTEREXAMPLE_NEW_FLOOR`  
**Acceptance gate:** criterion 4, a statement-changing obstruction floor  
**Named floor:** `RS_TRACE_VANDERMONDE_COHERENT_ORBIT_FLOOR`  
**Named successor residual:** `POST_C1_C8_RS_ORBIT_DECORRELATION_OR_DIRECT_SIDON`

## 1. Result in one sentence

Actual Reed--Solomon trace--Vandermonde phases do not by themselves make a
cancellation-sensitive effective-character payment subexponential: on an
explicit infinite RS family, a canonical orbit of effective characters is
perfectly phase-aligned, and even after summing the orbit first, taking only one
absolute value, and applying the exact realized-image factor `L/A_eff`, the loss
is

\[
 \exp\!\left(\frac{\log 2}{4}N-O(\log N)\right).
\]

This extends the abstract half-slice obstruction into a genuine RS phase
regime.  It does **not** say that every possible cross-orbit cancellation
scheme fails.

## 2. Source and import pins

The lane was branched from fork `main` at

```text
4e5f0b77c98f075ea7c8822cd4859847a232bc2a
```

with upstream `main` at

```text
a3017697ad1594521d2779fe1d83bccd45d4c06e
```

at lane start.  The fork was ahead of, and not behind, upstream.

### Integrated source blob parity

| source | fork-main blob | upstream-main blob | parity |
|---|---|---|---|
| `experimental/grande_finale.tex` | `8a5d9791900ca9eed773feba146b92ad296704ce` | `8a5d9791900ca9eed773feba146b92ad296704ce` | byte-identical |
| `experimental/rs_mca_thresholds.tex` | `01302a797c502a05ed0b11ba949b8756e0aa2b22` | `01302a797c502a05ed0b11ba949b8756e0aa2b22` | byte-identical |
| `experimental/notes/thresholds/minimal_phase_supplement.md` | `6b1482b86e5eaad2046a41c5a122b86514a78a10` | `6b1482b86e5eaad2046a41c5a122b86514a78a10` | byte-identical |

### Imported Lean API parity

| imported integrated API | fork-main blob | upstream-main blob | parity |
|---|---:|---:|---|
| `AsymptoticSpine.*` | not imported | not imported | vacuous |
| `M31QRootedShell.*` | not imported | not imported | vacuous |
| any open-PR module | not imported | not imported | vacuous |

The new module imports only `Std`.  Every finite-field, fixed-weight, syndrome,
and phase definition used by the regression is restated locally.  In
particular, it does not import `M31C9RowSharp`, `HalfSliceFalsifier`, or any
other open-PR file.

## 3. The genuine RS family

Let `s>=3` be an odd prime and put

\[
 q=2^s,\qquad r=q/4,\qquad
 D=\mathbb F_q^\times,\qquad N=q-1=4r-1,
\]
\[
 R=q/2-1=2r-1,\qquad m=r.
\]

For `t in D`, use the actual RS parity column

\[
 h_t=(t,t^2,\ldots,t^R)\in\mathbb F_q^R.
 \tag{1}
\]

The integrated exact RS regression in
`minimal_phase_supplement.md`, equation `(C6)` and its preceding binary-rank
argument, proves that the binary kernel of

\[
 \mathbb F_2^D\longrightarrow \mathbb F_q^R,\qquad
 (c_t)_t\longmapsto\sum_t c_t h_t
 \tag{2}
\]

is exactly the line spanned by the all-ones vector.

Let

\[
 \Omega_m=\{S\subseteq D:|S|=m\},\qquad
 \Psi(S)=\sum_{t\in S}h_t.
 \tag{3}
\]

All fields and scales in this note are now fixed:

| object | value |
|---|---|
| coefficient/generated field | `B=F_2` for the phase space |
| RS evaluation field | `F_q` |
| source mass | `M=binom(N,m)` |
| realized image size | `L=|Psi(Omega_m)|` |
| effective target | `A_eff=|V|`, with `V=Span_F2{h_t-h_t0}` |
| MCA line denominator | not instantiated |
| challenge/list denominator | not instantiated |

No field or denominator in the table is silently identified with another.

## 4. Exact image normalization and direct Q

### Proposition 4.1 -- the fixed-weight RS map is injective

\[
 M=L=\binom{4r-1}{r},\qquad \max_z|\Psi^{-1}(z)|=1.
 \tag{4}
\]

**Proof.**
If `Psi(S)=Psi(S')`, then the incidence vector of the symmetric difference
`S triangle S'` lies in the binary kernel (2).  It is therefore either zero or
the all-ones vector.  The first case gives `S=S'`.  The second gives
`S'=D\setminus S`, but

\[
 |D\setminus S|=(4r-1)-r=3r-1\ne r=|S'|,
\]

so the second case is impossible.  This proves (4).  In particular, the
image-normalized primitive max-fiber loss is exactly one and every nonempty
fiber is a singleton.  Consequently every fixed positive Sidon-heavy cutoff
has zero contribution on the full slice. ∎

### Proposition 4.2 -- the effective target has size `2^(N-1)`

For any anchor `t_0`,

\[
 V=\operatorname{Span}_{\mathbb F_2}\{h_t-h_{t_0}:t\in D\}
\]

has binary dimension `N-1`, and hence

\[
 A_{\rm eff}=2^{N-1}=2^{4r-2}.
 \tag{5}
\]

**Proof.**
The column span has rank `N-1` by (2).  Also
\(\sum_{t\in D}h_t=0\).  Because `N-1` is even in characteristic two,

\[
 h_{t_0}=\sum_{t\ne t_0}(h_t+h_{t_0}),
\]

so the difference span contains every column and equals the column span. ∎

## 5. Every middle trace phase is a genuine RS character

For \(a=(a_1,\ldots,a_R)\in\mathbb F_q^R\), define the trace phase

\[
 y_a(t)=\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}
          \left(\sum_{j=1}^R a_jt^j\right)\in\mathbb F_2.
 \tag{6}
\]

The trace pairing is nondegenerate.  Therefore the image of `a -> y_a` is the
orthogonal complement of the binary kernel (2), namely the even-parity
hyperplane

\[
 \left\{y\in\mathbb F_2^D:\sum_{t\in D}y(t)=0\right\}.
 \tag{7}
\]

Because `N` is odd, every effective character class modulo the constant phase
has exactly one even representative.  Thus (6) realizes all `A_eff=2^(N-1)`
effective characters.  Moreover `m=r` is even.  Replacing an even representative
`y` by `y+1` multiplies every weight-`m` term by `(-1)^m=1`, and passing from
`h_t` to the anchored difference `h_t-h_{t_0}` contributes the factor
`(-1)^{m y(t_0)}=1`.  The signed coefficient below is therefore an honest,
anchor-independent coefficient of the effective RS character, not merely an
unanchored sign convention.

In particular, every subset \(Y\subseteq D\) of size

\[
 |Y|=2r=q/2
 \tag{8}
\]

is the support of a genuine trace-linear character of the RS columns (1).
This is the point at which the present family differs from an arbitrary sign
pattern: the signs arise from actual trace evaluations of a Vandermonde
polynomial phase.

## 6. The coherent orbit and its exact phase

For an effective character with support `Y`, its fixed-weight Fourier
coefficient is

\[
 E_m(Y)
 =\sum_{\substack{S\subseteq D\\|S|=r}}(-1)^{|S\cap Y|}
 =[z^r](1-z)^{|Y|}(1+z)^{N-|Y|}.
 \tag{9}
\]

Take the canonical phase-weight orbit

\[
 \mathcal O_r=\{Y\subseteq D:|Y|=2r\}.
 \tag{10}
\]

For every `Y` in this orbit,

\[
\begin{aligned}
 E_m(Y)
  &=[z^r](1-z)^{2r}(1+z)^{2r-1}\\
  &=[z^r](1-z)(1-z^2)^{2r-1}\\
  &=(-1)^{r/2}\binom{2r-1}{r/2}.
\end{aligned}
\tag{11}
\]

Here `r=2^(s-2)` is even.  The would-be odd coefficient from the factor `-z`
vanishes.  Equation (11) is independent of `Y`: the entire orbit has the same
real sign.  Therefore summing before taking an absolute value produces no
cancellation:

\[
\begin{aligned}
 H_r
  &:=\left|\sum_{Y\in\mathcal O_r}E_m(Y)\right|\\
  &=\binom{4r-1}{2r}\binom{2r-1}{r/2}.
\end{aligned}
\tag{12}
\]

This is already cancellation-sensitive: there is one absolute value after the
whole phase orbit is summed, rather than one absolute value per character.

## 7. Image compensation does not remove the floor

Define the image-compensated coherent-orbit aggregate

\[
 \mathcal C_r
 :=\frac{L}{A_{\rm eff}}\frac{1}{M}
   \left|\sum_{Y\in\mathcal O_r}E_m(Y)\right|.
 \tag{13}
\]

Since `L=M`, equations (5) and (12) give

\[
 \mathcal C_r
 =\frac{\binom{4r-1}{2r}\binom{2r-1}{r/2}}{2^{4r-2}}.
 \tag{14}
\]

The elementary largest-binomial-coefficient bounds give

\[
 \binom{4r-1}{2r}\ge \frac{2^{4r-1}}{4r+1},
 \qquad
 \binom{2r-1}{r/2}\ge\binom r{r/2}
          \ge\frac{2^r}{r+1}.
 \tag{15}
\]

Hence

\[
 \boxed{
 \mathcal C_r
 \ge
 \frac{2^{r+1}}{(4r+1)(r+1)}
 =
 \exp\!\left(\frac{\log 2}{4}N-O(\log N)\right).
 }
 \tag{16}
\]

Thus even exact `L/A_eff` compensation leaves an exponential loss on this
genuine RS phase orbit.

## 8. The theorem and the route cut

### Theorem 8.1 -- `RS_TRACE_VANDERMONDE_COHERENT_ORBIT_FLOOR`

For every odd prime `s>=3`, the RS family (1)--(3) has all of the following
properties simultaneously:

1. exact realized-image normalization `M=L`;
2. exact max-fiber one and singleton residual fibers under arbitrary deletion;
3. effective target size `A_eff=2^(N-1)`;
4. every phase in the orbit (10) is a genuine trace--Vandermonde RS character;
5. the direct Sidon-heavy contribution is zero at every fixed positive cutoff;
6. the cancellation-sensitive, image-compensated coherent aggregate (13)
   satisfies the exponential lower bound (16).

Therefore the following proposed universal route is false:

```text
genuine trace-Vandermonde RS phase origin
+ exact image normalization
+ exact direct Q / singleton fibers
+ one signed sum per canonical phase-weight orbit
=> subexponential image-compensated phase aggregate.
```

This is a third obstruction floor after the ambient/effective normalization
floor and the absolute effective-dual `L^1` floor.  It changes the successor
statement: “use the RS phases” is not a sufficient hypothesis.

### Named successor residual

A positive successor must prove at least one of the following on the **actual**
post-C1--C8 residual:

- first-match deletion destroys the coherent orbit quantitatively;
- a cross-orbit decorrelation theorem cancels (12) against other phase weights
  without reintroducing an absolute-value loss;
- an odd-characteristic or restricted-rank hypothesis excludes this binary
  trace family; or
- a direct realized-image Sidon/max-fiber theorem bypasses the Fourier
  aggregate.

The residual is named

```text
POST_C1_C8_RS_ORBIT_DECORRELATION_OR_DIRECT_SIDON.
```

A theorem bounding only orbitwise coherent sums cannot be the missing
universal replacement.

## 9. Exact finite falsifier over `F_8`

Take

\[
 \mathbb F_8=\mathbb F_2[x]/(x^3+x+1),\quad
 D=\mathbb F_8^\times,\quad N=7,\quad R=3,\quad m=2.
\]

Use columns

\[
 h_t=(t,t^2,t^3).
\]

The certificate and Lean module check:

| quantity | exact value |
|---|---:|
| source supports `M` | 21 |
| realized syndromes `L` | 21 |
| maximum fiber | 1 |
| effective difference span `A_eff` | 64 |
| trace phase patterns | 64, exactly the even patterns |
| weight-four trace-character orbit | 35 |
| every orbit coefficient | `-3` |
| coherent signed sum | `-105` |
| coherent magnitude `H` | 105 |
| source-normalized aggregate `H/M` | 5 |
| image-compensated aggregate | `105/64 > 1` |

The JSON contains all 21 supports and syndromes and all 35 explicit
trace-linear coefficient witnesses.  The verifier independently recomputes
the field arithmetic, Vandermonde columns, fixed-weight image, difference
span, all 512 coefficient triples, every trace pattern, all orbit
coefficients, the anchor translation, and the coherent sum.

Frozen artifact hashes before fork CI:

```text
certificate SHA-256:
7ec07b4200bcabef3c9531f7a75d6044723ac2eca5444b2b2fb546f674755677

verifier SHA-256:
435e05e441aac3d5c7f05275d96feeddc598b68577b1f36c2172ad5be66d7c88
```

Replay completed in ordinary and optimized Python modes, and all six mutation
tests were rejected in both modes.

## 10. Nonclaims

- No theorem here proves that the full slice, or the coherent orbit, survives
  the repository's actual C1--C8 first-match chronology.
- This is not an MCA received-line counterexample and instantiates no affine
  slope, ray compiler, challenge denominator, list denominator, `B*`, or
  deployed adjacent row.
- The result does not rule out cancellation that deliberately mixes different
  phase-weight orbits.
- No odd-characteristic analogue is claimed.
- It does not refute the correctness of a theorem whose hypotheses already
  assume an adequate pointwise minor bound or a direct Sidon payment.
- Lean certifies the exact `q=8` arithmetic and correspondence.  The infinite
  family theorem is the proof in Sections 3--8.
- Green Lean CI proves compilation, not the general mathematical argument or
  post-C1--C8 survival.

## 11. Source-label map

| role | active source |
|---|---|
| effective span and image scales | `experimental/grande_finale.tex`, `eq:effective-fourier-span`, `lem:effective-span-fourier`, `eq:image-ambient-scales` |
| effective Fourier payment | `def:effective-fourier-payment`, `def:aggregate-minor-payment`, `def:major-arc-aggregate`, `prop:effective-mi-ma-flatness` |
| direct image-scale payment | `def:primitive-q`, `def:sidon-heavy`, `def:sidon-paid-cell` |
| actual RS binary-rank family | `experimental/notes/thresholds/minimal_phase_supplement.md`, equation `(C6)` and the exact RS regression immediately preceding it |
| deployed/foundation conventions not instantiated here | `experimental/rs_mca_thresholds.tex` and `tex/cs25_cap_v13_2.tex` |

# COUNTEREXAMPLE_NEW_FLOOR
