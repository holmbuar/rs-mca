# Rooted order-two Fourier-band reduction

**Status:** PROVED finite reduction / AUDIT / ROUTE CUT.

This packet closes the order-two rooting step in the mask-aware band program.
Vadim Avdeev's PR #677 introduces complete dyadic character bands, the
multilinear band restriction target (MBR), and a band-to-cell inverse target
(BCI). Its exact dual witness must be general at top moment order. At order two
no arbitrary dual witness is needed: orthogonal projection roots every failure
in the actual residual support-pair statistic.

The result is deliberately narrower than BCI. It proves that an order-two band
failure produces a heavy realized boundary fiber and actual same-boundary
residual supports. It does not turn that pair into a previously paid quotient,
planted, field, rank, or saturation owner. That semantic pair-to-owner map is
exactly what remains if order two is to advance A4 rather than restate Q/SP.

Target manuscript: experimental/asymptotic_rs_mca_frontiers.tex, especially
def:primitive-first-match-residual and def:q-sp. No manuscript file is edited.

Verifier: experimental/scripts/verify_rooted_order_two_band_reduction.py
(stdlib only, deterministic, no files written):

    abstract_cases=29
    source_cases=45
    strict_emission_cases=1
    RESULT: PASS (639 checks)

## 1. Exact setup

Let \(\Omega^0\) be a finite full profile slice, let
\(\Phi:\Omega^0\to G\) map into a finite abelian group of order \(H\), and
write

\[
 M=|\Omega^0|,\qquad L=|\Phi(\Omega^0)|,\qquad \bar N=M/L.
\]

Let \(\Omega^\circ\subseteq\Omega^0\) be the actual primitive first-match
residual, with mass \(W=|\Omega^\circ|\), and put

\[
 f(s)=|\Omega^\circ\cap\Phi^{-1}(s)|,\qquad
 Q=\max_s f(s),\qquad {\rm SP}=\sum_s f(s)^2.
\]

Thus \(W\le M\), \(L\le M\), and

\[
 {\rm SP}\le WQ.                                           \tag{1}
\]

Partition the nonzero effective dual into pairwise disjoint symmetric bands

\[
 \widehat G\setminus\{0\}=\coprod_{k\in\mathcal I}A_k,
 \qquad -A_k=A_k.
\]

The dyadic \(|\tau|\)-bands of PR #677 have these properties. With
unnormalized Fourier transform, define

\[
 P_kf(s)=\frac1H\sum_{\gamma\in A_k}
 \widehat f(\gamma)\gamma(s),\qquad
 \mathcal C_{2,k}=\frac{L}{M^2}\sum_s|P_kf(s)|^2.          \tag{2}
\]

This is the order-two specialization of the complete-pattern normalization in
PR #677.

## 2. The order-two theorem

### Theorem 2.1 (diagonal pattern and rooted pair identity)

For the setup above:

1. every mixed order-two pattern \((k,\ell)\), \(k\ne\ell\), is empty;
2. for each band,
   \[
   \sum_s|P_kf(s)|^2
   =\frac1H\sum_{\gamma\in A_k}|\widehat f(\gamma)|^2
   =\frac1H\sum_{x,y\in\Omega^\circ}
      K_k(\Phi(y)-\Phi(x)),                              \tag{3}
   \]
   where \(K_k(u)=\sum_{\gamma\in A_k}\gamma(u)\);
3. the exact inequalities
   \[
   \sum_s|P_kf(s)|^2\le {\rm SP}\le WQ                  \tag{4}
   \]
   hold; and
4. summing all nonzero bands gives
   \[
   \sum_k\sum_s|P_kf(s)|^2
     ={\rm SP}-\frac{W^2}{H}.                           \tag{5}
   \]

#### Proof

If \(\gamma_1\in A_k\), \(\gamma_2\in A_\ell\), and
\(\gamma_1+\gamma_2=0\), then \(\gamma_2=-\gamma_1\in A_k\).
Disjointness forces \(k=\ell\), proving the first assertion.

The first equality in (3) is Parseval. Expanding
\(|\widehat f(\gamma)|^2\) over the actual residual supports gives

\[
 \overline{\gamma(\Phi(x))}\gamma(\Phi(y))
 =\gamma(\Phi(y)-\Phi(x)),
\]

which proves the second equality. Since \(P_k\) is an orthogonal projection
on \(\ell^2(G)\),

\[
 \|P_kf\|_2^2\le\|f\|_2^2={\rm SP}.
\]

The second inequality in (4) is (1). Finally, the bands are disjoint and
exhaust the nonzero dual, so Parseval after deleting the trivial character
gives (5). \(\square\)

### Corollary 2.2 (quantitative rooted emission)

Let \(C\ge1\). If one band violates the order-two restriction scale,

\[
 \sum_s|P_kf(s)|^2>C\frac{M^2}{L},
 \qquad\text{equivalently}\qquad
 \mathcal C_{2,k}>C,                                   \tag{6}
\]

then

\[
 Q>C\bar N                                             \tag{7}
\]

and the number of ordered distinct same-boundary residual pairs satisfies

\[
 {\rm SP}-W>C\frac{M^2}{L}-W\ge0.                      \tag{8}
\]

In particular, there are distinct
\(x,y\in\Omega^\circ\) with \(\Phi(x)=\Phi(y)\): an actual residual
shift pair, not an ambient or mask-blind witness.

#### Proof

By (4) and \(W\le M\),

\[
 WQ\ge{\rm SP}\ge\|P_kf\|_2^2
   >C\frac{M^2}{L},
\]

so \(Q>C M^2/(LW)\ge C M/L=C\bar N\). Also
\({\rm SP}>C M^2/L\); subtract \(W\), and use
\(C M^2/L\ge M\ge W\), to obtain (8). \(\square\)

### Corollary 2.3 (Q pays the entire order-two sector)

If \(Q\le K\bar N\), then

\[
 \sum_k\mathcal C_{2,k}\le K.                          \tag{9}
\]

If the residual boundary map is injective, every band is paid with constant
one. Indeed, (5), (1), and \(W\le M\) give

\[
 \sum_k\mathcal C_{2,k}
 \le\frac{L}{M^2}WQ\le K.
\]

For an injective residual \(Q\le1\), and directly
\(\mathcal C_{2,k}\le LW/M^2\le L/M\le1\).

### Corollary 2.4 (literal first-match source root)

Fix an actual received line \(r\), a primitive profile \(\lambda\), its full
profile slice \(\Omega^0_\lambda\), and the supports
\(\Omega^\circ_\lambda(r)\) that survive the canonical first-match deletion.
Let

\[
 \Phi_\lambda:\Omega^0_\lambda\longrightarrow G_\lambda,
 \qquad
 L_\lambda=\left|\Phi_\lambda(\Omega^0_\lambda)\right|,
\]

be the effective boundary map and its realized image size.  For \(C\ge1\), if
a complete symmetric band \(A_{\lambda,k}\) satisfies, for the pushed-forward
residual count

\[
 f_{\lambda,r}(s)
 =\left|\Omega^\circ_\lambda(r)\cap\Phi_\lambda^{-1}(s)\right|,
\]

the bound

\[
 \left\|P_{\lambda,k}f_{\lambda,r}\right\|_2^2
 > C\frac{|\Omega^0_\lambda|^2}{L_\lambda},
\]

then its actual residual max fiber exceeds
\(C|\Omega^0_\lambda|/L_\lambda\), and there are distinct
\(S,T\in\Omega^\circ_\lambda(r)\) with
\(\Phi_\lambda(S)=\Phi_\lambda(T)\).  Thus the emitted pair is attached to
the literal source root \((r,\lambda)\) and survives every earlier cell.  The
corollary does not assign that pair to a paid owner cell.

This is Corollary 2.2 with the displayed source data substituted for
\((\Omega^0,\Omega^\circ,\Phi,L)\).

## 3. What this resolves in the BCI program

For order two, the following chain is exact:

    order-two band-restriction failure
      => physical SP failure
      => image-normalized Q failure
      => actual same-boundary residual support pair.

Thus order-two Fourier analysis has no unrooted dual-witness gap. The root is
an actual pair surviving first-match deletion.

This is also a route cut. A proposed order-two BCI whose conclusion is only
"there is a heavy fiber" or "there is a shift pair" is circular: (6)--(8)
already give that conclusion from the failed estimate, and the manuscript
treats Q/SP as unproved counting interfaces rather than paid slope cells. To
advance A4, the source-specific theorem must take the emitted pair and produce
a previously paid semantic owner certificate with its own enumerative bound.
Naming the pair is not that payment.

At higher orders, a sharp Fourier projection need not be contractive on
\(\ell^j\). This reduction therefore does not replace the dense top-order
restriction or the full BCI target of PR #677.

## 4. Rank-one prime-field source specialization

Take

\[
 G=\mathbb F_p^+,\qquad T=\mathbb F_p^\times,\qquad
 \Phi(x)=\sum_{t\in T}x_t t
\]

on a fixed-weight slice. This is the rank-one power-sum boundary map. For every
nontrivial additive character,

\[
 \tau(\gamma)=\sum_{t\in\mathbb F_p^\times}\gamma(t)=-1.
\]

Hence all nontrivial characters form one exact band. Its kernel is

\[
 K(u)=
 \begin{cases}
 p-1,&u=0,\\
 -1,&u\ne0,
 \end{cases}
\]

and (3) becomes

\[
 \|P_{\ne0}f\|_2^2={\rm SP}-\frac{W^2}{p}.            \tag{10}
\]

The verifier exhausts support sums for
\(p\in\{5,7,11,13\}\), all weights through four that occur in the script,
and three deterministic residual masks. This is a rank-one/shallow
calibration, not a positive-depth-ratio A4 theorem.

## 5. Independent exact replay

The verifier uses two independent finite models.

1. On elementary \(2\)-groups it computes every band projection directly,
   by Parseval, and through the pair kernel in (3), all in exact rational
   arithmetic. It checks mixed-band orthogonality, the centered-SP sum,
   contraction, the injective case, and a deliberately heavy map that
   exercises strict emission.
2. On the prime-field source specialization it enumerates fixed-weight
   supports and checks (10) through the independent kernel formula
   \(K(0)=p-1\), \(K(u)=-1\).

The run covers 29 abstract residual maps and 45 source rows. Exactly one
deliberately heavy abstract case crosses the strict normalized threshold; it
emits the predicted heavy fiber and same-boundary pair. All 639 checks pass.

## 6. Claim ledger

| Claim | Status |
|---|---|
| Mixed order-two patterns vanish | **PROVED** |
| Projection, Parseval, and actual residual-pair routes agree | **PROVED** |
| Every order-two band is bounded by SP and \(WQ\) | **PROVED** |
| Band failure emits \(Q>C\bar N\) and an actual residual shift pair | **PROVED** |
| Q pays the complete nonzero order-two band sector | **PROVED** |
| A source failure emits a pair tied to the actual \((r,\lambda)\) first-match root | **PROVED** |
| Rank-one \(\mathbb F_p^\times\) specialization has one flat nonzero band | **PROVED** |
| Emitted pair has a previously paid algebraic owner | **OPEN** |
| Dense top-order restriction | **OPEN** |
| Full A4, primitive Q, RC, or the asymptotic frontier | **NOT CLAIMED** |

## 7. Reproduction

From the repository root:

    python3 experimental/scripts/verify_rooted_order_two_band_reduction.py

Expected summary:

    abstract_cases=29
    source_cases=45
    strict_emission_cases=1
    RESULT: PASS (639 checks)
