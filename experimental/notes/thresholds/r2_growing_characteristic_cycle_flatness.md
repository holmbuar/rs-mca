# R=2 growing-characteristic cycle flatness

## Claim

Let \(B_\nu\) be finite fields of odd characteristic \(p_\nu\), with
\(|B_\nu|=Q_\nu\).  Let

```text
D_nu = theta_nu H_nu subset B_nu^x,
T_nu = D_nu \ P_nu,
N_nu = |T_nu| -> infinity,
```

where \(P_\nu\) is an allowed planted exceptional set.  Fix
\(0<\alpha<1/2\), take

```text
alpha <= m_nu/N_nu <= 1-alpha,
```

and define on \(\Omega_\nu=\binom{T_\nu}{m_\nu}\)

\[
 \Phi_\nu(S)=\left(\sum_{t\in S}t,\sum_{t\in S}t^2\right)\in B_\nu^2,
 \qquad M_\nu=\binom{N_\nu}{m_\nu}.
\]

Let \(C_0\) be the absolute constant in
`prop:weighted-weil-minor-arcs`, and put

\[
 C_W=3C_0,
 \qquad
 \Lambda_\nu=C_W\sqrt{Q_\nu}+|P_\nu|.
\]

Assume that a fixed \(\lambda<1/2\) satisfies
\(\Lambda_\nu/N_\nu\le\lambda\) eventually.  Define, for natural-log binary
entropy \(h\),

\[
 \delta_{\alpha,\lambda}
 =\min_{\alpha\le x\le1/2}
 \left\{
 h(x)-(x+\lambda)h\!\left(\frac{x}{x+\lambda}\right)
 \right\}>0.                                             \tag{1}
\]

If

\[
 \limsup_{\nu\to\infty}
 \left(
   \frac{2\log Q_\nu}{N_\nu}
   +\frac{3\log2}{2p_\nu}
 \right)
 <\delta_{\alpha,\lambda},                              \tag{2}
\]

then there is \(c>0\) such that, uniformly in \(z\in B_\nu^2\),

\[
 \left|
  |\Phi_\nu^{-1}(z)|-\frac{M_\nu}{Q_\nu^2}
 \right|
 \le e^{-cN_\nu}\frac{M_\nu}{Q_\nu^2}.                \tag{3}
\]

Consequently the realized image is exactly \(B_\nu^2\) for all sufficiently
large rows, and every first-match residual
\(\Omega_\nu^\circ\subseteq\Omega_\nu\) satisfies

\[
 \max_z|\Omega_\nu^\circ\cap\Phi_\nu^{-1}(z)|
 \le (1+e^{-cN_\nu})\frac{M_\nu}{Q_\nu^2}.              \tag{4}
\]

In particular, the simpler hypotheses

\[
 p_\nu\longrightarrow\infty,
 \qquad \log Q_\nu=o(N_\nu),
 \qquad \Lambda_\nu/N_\nu\le\lambda<1/2               \tag{5}
\]

suffice.  Thus the bounded-\(N_\nu/p_\nu\) assumption in
`r2_constant_weil_cycle_flatness.md` is unnecessary: it can be replaced by
growing characteristic, or more generally by the explicit gate (2).

## Status

**PROVED**, conditional only on the same classical mixed Weil estimate used by
the integrated `prop:weighted-weil-minor-arcs`.  The coefficient compression,
quantitative gate, and strict source family below are **PROVED**.  This is a
special-class payment toward maintainer hard input 2, not a closure of that
hard input for every primitive leaf.

## Parameters

- Field tower: \(B_\nu\), with \(Q_\nu=|B_\nu|\) and odd characteristic
  \(p_\nu\).
- Domain: an unweighted multiplicative coset with an allowed planted deletion,
  \(T_\nu=\theta_\nu H_\nu\setminus P_\nu\).
- Slice: \(N_\nu=|T_\nu|\), fixed-density
  \(\alpha\le m_\nu/N_\nu\le1-\alpha\).
- Boundary map: the \(R=2\) power-sum map into \(B_\nu^2\).
- Weil parameter: \(\Lambda_\nu=3C_0\sqrt{Q_\nu}+|P_\nu|\), with
  \(\Lambda_\nu/N_\nu\le\lambda<1/2\).
- Image scale: \(A_{\rm eff}=Q_\nu^2\), proved here to be the realized full
  image; the source-prescribed random-fiber scale is \(M_\nu/Q_\nu^2\).
- No \(q_{\rm gen}\), \(q_{\rm line}\), code rate \(\rho\), agreement radius,
  or list/interleaving arity is changed or inferred by this packet.

## Existing paper dependency

The theorem strengthens
`experimental/notes/thresholds/r2_constant_weil_cycle_flatness.md`, introduced
at commit `6588d8d6c393df81642dafafc82c70f565d009cf` and integrated by
`7d66bfa9b2f3c3cf557f1a4e898fe6cbc26a4ce3`.  That note proves the same
conclusion under \(N/p\le K\) and explicitly leaves unbounded \(N/p\) open.

The only analytic input retained here is the non-characteristic-divisible
quadratic phase estimate from `prop:weighted-weil-minor-arcs`.  The exact cycle
factor is the one named in `rem:small-characteristic-cycles`.  Relative to the
frontiers paper, (3) is a direct effective Fourier payment on the full
\(R=2\) image: every nonzero effective character is paid in aggregate and no
major-character remainder is needed.

This does not conflict with the unrestricted separated-Prouhet construction in
`c9_r2_near_sidon_razor.md`: that source is not a multiplicative coset and does
not satisfy this packet's constant-Weil-ratio and field-size hypotheses.

## Proof idea or experiment

Suppress \(\nu\).  Fix a nonzero dual parameter \(u=(a,b)\in B^2\), a
nontrivial additive character \(\psi\), and put

\[
 x_t=\psi(at+bt^2),
 \qquad
 P_j(u)=\sum_{t\in T}x_t^j.
\]

If \(p\nmid j\), the phase \(j(aX+bX^2)\) is nonconstant and not of
Artin--Schreier form, so the named mixed Weil input gives
\(|P_j(u)|\le\Lambda\).  If \(p\mid j\), additive-character values have
\(p\)-torsion and \(P_j(u)=N\) exactly.  Newton's generating identity and
coefficientwise absolute majorization therefore give, for any \(r\le N/2\),

\[
 |e_r(x_t:t\in T)|\le B_r,
 \qquad
 B_r=[v^r](1-v)^{-\Lambda}
                (1-v^p)^{-(N-\Lambda)/p}.                \tag{6}
\]

Set

\[
 \beta=\frac{N-\Lambda}{p}>0,
 \qquad L=\left\lfloor\frac rp\right\rfloor.
\]

Expanding (6), using that
\(\binom{\Lambda+s-1}{s}\) is nondecreasing in the integer \(s\) once
\(\Lambda\ge1\), and then applying the generalized hockey-stick identity
gives the new coefficient bound

\[
\begin{aligned}
 B_r
 &=\sum_{\ell=0}^{L}
   \binom{\beta+\ell-1}{\ell}
   \binom{\Lambda+r-p\ell-1}{r-p\ell}\\
 &\le
   \binom{\Lambda+r-1}{r}
   \sum_{\ell=0}^{L}\binom{\beta+\ell-1}{\ell}\\
 &=\binom{\Lambda+r-1}{r}
   \binom{\beta+L}{L}.                                  \tag{7}
\end{aligned}
\]

This replaces the old row-independent constant \(C_K\) by an exact factor.
Because generalized binomial coefficients increase in their upper parameter,

\[
 \binom{\beta+L}{L}
 \le\binom{\lceil\beta\rceil+L}{L}
 \le2^{\lceil\beta\rceil+L}
 \le2^{1+3N/(2p)}.                                      \tag{8}
\]

The last inequality uses \(\beta\le N/p\) and
\(L\le r/p\le N/(2p)\).

For a finite row with \(1\le\Lambda<N\), put \(r=\min(m,N-m)\),
\(M=\binom Nm\), and define

\[
 \epsilon_*
 =\frac{Q^2-1}{\binom Nr}
   \binom{\Lambda+r-1}{r}
   \binom{\beta+\lfloor r/p\rfloor}{\lfloor r/p\rfloor}.
                                                               \tag{9}
\]

Fourier inversion and complementation give the exact implication

\[
 \left||\Phi^{-1}(z)|-M/Q^2\right|
 \le\epsilon_*M/Q^2.                                    \tag{10}
\]

Hence \(\epsilon_*<1\) certifies the full image and the residual bound
\((1+\epsilon_*)M/Q^2\) without any asymptotic argument.

For \(x=r/N\in[\alpha,1/2]\), uniform Stirling comparison in (9) yields

\[
 \frac1N\log\epsilon_*
 \le
 -\left[
   h(x)-(x+\lambda)h\!\left(\frac{x}{x+\lambda}\right)
  \right]
 +\frac{2\log Q}{N}
 +\frac{3\log2}{2p}
 +o(1).                                                  \tag{11}
\]

The bracket is positive on the compact interval because its zeros are
\(0\) and \(1-\lambda\), while
\([\alpha,1/2]\subset(0,1-\lambda)\).  Equations (1)--(2) now imply (3).

### Strict family newly admitted by the theorem

Fix an integer \(d>2C_W=6C_0\).  Dirichlet's theorem supplies infinitely many
odd primes \(p\equiv1\pmod d\); along those primes, take

\[
 B=\mathbb F_{p^4},
 \qquad Q=p^4,
 \qquad |H|=N=d(p^2+1),
 \qquad T=\theta H,
 \qquad P=\varnothing.                                  \tag{12}
\]

The subgroup exists because
\(d(p^2+1)\mid(p^2-1)(p^2+1)=p^4-1\).  Moreover,

\[
 \frac Np\sim dp\longrightarrow\infty,
 \qquad
 \frac\Lambda N\longrightarrow\frac{C_W}{d}<\frac12,
 \qquad
 \log Q=o(N),                                           \tag{13}
\]

whereas

\[
 \frac{2\sqrt Q}{N}\longrightarrow\frac2d>0.           \tag{14}
\]

Thus (12) is excluded both by the bounded-\(N/p\) theorem and by the shallow
condition \(2\sqrt Q=o(N)\), but it is covered by (5).  It is also not a
disguised proper-subfield row: every proper subfield of \(\mathbb F_{p^4}\)
has multiplicative group of order at most \(p^2-1<N\).

## Ledger impact

- **Hard input 2:** pays image-scale Fourier flatness and the direct max-fiber
  bound for the stated unweighted \(R=2\) multiplicative-coset class.
- **C9:** rules out positive exponential max-fiber excess on this class before
  any Sidon-energy split; deleting supports in a primitive first-match residual
  cannot enlarge a full-slice fiber.
- **Major/minor ledger:** all \(Q^2-1\) nontrivial characters are paid by the
  aggregate in (9); the realized image is proved rather than replaced by the
  ambient codomain.
- No first-match exhaustion, higher-dimensional balanced-core ray compiler,
  profile-envelope comparison, or lower-reserve claim is supplied.

The bounded-block Prouhet product from `c9_r2_near_sidon_razor.md` can instead
be recognized as a higher-dimensional balanced-core architecture when its
product decomposition is source-certified.  That observation routes a
counterexample family toward C8/hard input 3; it is deliberately not bundled
into this direct hard-input-2 payment.

## Constants

- \(C_W=3C_0\) is exactly the predecessor note's quadratic-coset Weil
  constant.
- \(\delta_{\alpha,\lambda}\) is explicit in (1).  Any positive constant
  smaller than
  \[
    \delta_{\alpha,\lambda}
    -\limsup\left(2\log Q/N+3\log2/(2p)\right)
  \]
  is an admissible exponential decay constant in (3), after reducing it once
  to absorb the uniform Stirling remainder.
- \(\epsilon_*\) in (9) is the exact finite certificate exposed by this
  packet.  It is sharper than replacing \(Q^2-1\) by \(Q^2\) and sharper than
  the asymptotic power-of-two estimate (8).

## Reproducibility

```bash
python3 experimental/scripts/verify_r2_growing_characteristic_cycle_flatness.py --check
python3 experimental/scripts/verify_r2_growing_characteristic_cycle_flatness.py --tamper-selftest
```

The verifier uses exact `Fraction` arithmetic to check the expansion (6), the
generalized hockey-stick identity, (7), (8), and the finite bound (9) over a
grid that includes \(p\nmid N\).  For (12)--(14), it checks only the sampled
prime congruences, subgroup divisibility, proper-subfield exclusion, increasing
\(N/p\), and nonzero shallow ratio recorded in the machine-readable certificate
`experimental/data/certificates/r2-growing-characteristic-cycle-flatness/r2_growing_characteristic_cycle_flatness.json`.
The essential margin \(d>2C_W\) remains the theorem's explicit symbolic
hypothesis; the sample values of \(d\) are arithmetic checks, not certified
instances of the unspecified absolute Weil constant.

## Nonclaims

- No theorem for weighted rational charts is claimed.
- The same coefficient compression is available if a circle chart supplies
  the required non-characteristic-divisible cycle estimate, with the doubled
  circle Weil constant.  The currently printed weighted-Weil proposition is
  formally stated in the \(m<p\) range, so this packet does **not** promote a
  circle corollary.
- Fixed characteristic is not covered automatically.  Such a row is covered
  only if it satisfies the quantitative gate (2) or the exact finite predicate
  \(\epsilon_*<1\).
- No deployed finite leaf, Proximity Prize power-of-two row, adjacent
  inequality, MCA threshold, list-size statement, or paper-TeX edit is claimed.
