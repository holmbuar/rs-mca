# Audit: Case-B support-universe correction and collision-aware lower bound

## Status

`COUNTEREXAMPLE / PROVED EXPONENTIAL-FIELD LOWER / OPEN FIXED-EPSILON CONSTANT FRACTION`

This packet audits the polynomial-base-field feasibility claim in
`experimental/notes/thresholds/caseb_equidistribution.md` and its verifier at
upstream base `6f4e918f27a11995d3951f4ebe7546d4add0f345`.

The source claim is directionally right—counting alone does not eliminate every
exponential-field Case-B corner—but its displayed prize-regime witness is
wrong.  It replaces the support universe
\[
        \binom{|D|}{m}
\]
by a surrogate of size
\[
        \binom{|\mathbb B|}{m},
\]
even though the source setup has \(D\subseteq\mathbb B\) with
\(n=|D|\).  On the three printed \(m=2e\) rows this is not a harmless
approximation: the entire \(m\)-support layer is already much smaller than
\(2^{-128}|\mathbb F|\).  No prefix fiber, however atypical, can be
prize-relevant there.

The broad open corner survives after a fixed-density repair such as
\(m=\lfloor n/2\rfloor\).  That is also the regime required by the active
ledger-admissibility condition \(m_N/N\in[\alpha,1-\alpha]\).  The packet
checks this twice: first as a generic arithmetic calibration with
\(q_0=n^C\), and then on literal smooth multiplicative domains
\(D=\mathbb F_p^\times\).

There is a further consequence missed by the source discussion.  Once the
corrected pigeonhole list has size at least the ambient field, the paper's
existing collision-aware simple-pole theorem already produces
\(\Omega(|\mathbb F|/k)\) distinct bad slopes.  All six corrected finite rows
therefore cross the \(2^{-128}\) target without any constant-fraction
equidistribution theorem.  The same composition gives an infinite
smooth-multiplicative sequence with \(|\mathbb F|/e^{o(n)}\) bad slopes, so it
also settles the exponential-resolution lower/falsification corner.

## 1. Exact objects and the two counting gates

Let

\[
 |D|=n,\qquad |\mathbb B|=q_0,\qquad
 [\mathbb F:\mathbb B]=e,\qquad |\mathbb F|=q_0^e.
\]

Let \(G_z\subseteq\binom Dm\) be a depth-\(w\) prefix fiber, and let

\[
 \delta_z
 =\left|\{Q_S(\alpha):S\in G_z\}\right|
\]

be its Case-B slope image after the fiber-common shift is removed.  Always

\[
 \delta_z\le |G_z|\le \binom nm.                         \tag{1}
\]

For target \(\varepsilon=2^{-\tau}\), (1) gives the exact universal
necessary condition

\[
 \boxed{\binom nm\,2^\tau>q_0^e.}                    \tag{N}
\]

If the depth-\(w\) prefix map takes values in \(\mathbb B^w\), pigeonhole
supplies some fiber with

\[
 |G_z|\ge \binom nm q_0^{-w}.
\]

Thus the exact condition for pigeonhole to supply a field-sized fiber is

\[
 \boxed{
 \left\lceil\binom nm q_0^{-w}\right\rceil\ge q_0^e
 \iff
 \binom nm>q_0^w(q_0^e-1).}                           \tag{S}
\]

Condition (S) is sufficient only for a large support fiber; it does not prove
that its slope image is large.  Condition (N), by contrast, is necessary for
every fiber and therefore can conclusively remove a parameter regime.

## 2. Counterexample to the printed \(m=2e\) calibration

The integrated verifier chooses \(q_0=n^C\), takes
\(e\log_2q_0\approx n/2\), sets \(m=2e\), and estimates the support count as

\[
 \binom{q_0}m\approx q_0^m/m!.
\]

That is the wrong universe.  The actual supports lie in \(D\), so the ceiling is
\(\binom nm\).

The exact integer replay is:

| \(n\) | \(C\) | \(e\) | \(m=2e\) | \(\log_2|\mathbb F|\) | \(\lfloor\log_2\binom nm\rfloor\) | deficit below \(2^{-128}|\mathbb F|\) |
|---:|---:|---:|---:|---:|---:|---:|
| $2^{14}$ | 2 | 292 | 584 | 8176 | 3630 | 4418 |
| $2^{16}$ | 3 | 682 | 1364 | 32736 | 9560 | 23048 |
| $2^{18}$ | 2 | 3640 | 7280 | 131040 | 47987 | 82925 |

Every deficit is positive by thousands of bits.  More explicitly,

\[
 \binom nm\,2^{128}<q_0^e
\]

on all three rows.  Hence no depth-\(w\) fiber can furnish the target number of
distinct slopes—even if the slope map were injective.

The wrong-universe count passes even when replayed as the exact integer
\(\binom{q_0}{m}\), not merely through the source's Stirling-style surrogate.
The integrated verifier therefore certifies the substitution
\(n\mapsto q_0\), not the stated RS support problem.

There is a second incompatibility.  Here

\[
 \frac mn
 =\frac{2e}n
 \sim\frac1{C\log_2 n}
 \longrightarrow0,
\]

whereas the active admissibility interface requires the primitive active-slice
density to stay in a fixed interval
\([\alpha,1-\alpha]\).  The printed \(m=2e\) sequence is not a
fixed-density asymptotic leaf.

## 3. Corrected fixed-density calibrations

### 3.1 Generic arithmetic repair

Keep the same \(q_0=n^C\), the same extension degree
\(e\log_2q_0\approx n/2\), and \(w=4\), but take

\[
        m=\left\lfloor\frac n2\right\rfloor.
\]

Then \(e\le k=m-w-1\), so this remains Case B, and the exact average fiber is
larger than the ambient field:

| \(n\) | \(C\) | \(e\) | \(m=n/2\) | \(\log_2|\mathbb F|\) | \(\lfloor\log_2\binom nm\rfloor\) | surplus after \(w\) prefix coordinates |
|---:|---:|---:|---:|---:|---:|---:|
| $2^{14}$ | 2 | 292 | 8192 | 8176 | 16376 | 8088 |
| $2^{16}$ | 3 | 682 | 32768 | 32736 | 65527 | 32599 |
| $2^{18}$ | 2 | 3640 | 131072 | 131040 | 262134 | 130950 |

Here the last column is

\[
 \left\lfloor\log_2\binom nm\right\rfloor
 -(e+w)\log_2q_0.
\]

These rows prove the arithmetic feasibility of the repaired parameter regime,
but they do not by themselves assert that an \(n\)-point multiplicative
subgroup exists inside a field of cardinality \(n^C\).

### 3.2 Literal smooth multiplicative repair

To remove that modeling caveat, take the full multiplicative domain

\[
        \mathbb B=\mathbb F_p,\qquad
        D=\mathbb F_p^\times,\qquad n=p-1,
\]

with \(p\in\{1009,4099,16411\}\), \(m=n/2\), and \(w=4\).  Choose
\(e\) to be the largest integer satisfying

\[
        p^{2e}\le 2^n;
\]

this is an exact integer version of the ambient rate
\(e\log_2p/n\le1/2\).  The resulting rows are:

| \(p\) | \(n=p-1\) | \(e\) | \(m=n/2\) | \(\lfloor\log_2 p^e\rfloor\) | \(\lfloor\log_2\binom nm\rfloor\) | surplus over \(p^{e+w}\) |
|---:|---:|---:|---:|---:|---:|---:|
| 1009 | 1008 | 50 | 504 | 498 | 1002 | 463 |
| 4099 | 4098 | 170 | 2049 | 2040 | 4091 | 2003 |
| 16411 | 16410 | 585 | 8205 | 8191 | 16402 | 8155 |

The verifier proves primality, the maximality of each displayed \(e\), the
Case-B inequality \(e\le m-w-1\), and the exact comparison

\[
        \binom{p-1}{(p-1)/2}\ge p^{e+w}.
\]

The last column is the exact integer
\[
 \left\lfloor
   \log_2\!\left(\binom{p-1}{(p-1)/2}/p^{e+w}\right)
 \right\rfloor.
\]

Thus the broad corner genuinely survives counting on explicit smooth
multiplicative rows at fixed density.  Pigeonhole supplies a depth-\(w\)
support fiber at least as large as \(|\mathbb F|=p^e\); whether the slope
image covers a positive fraction of \(\mathbb F\) remains the actual
equidistribution question.

## 4. Collision-aware consequence

Put

\[
 Q=q_0^e,\qquad
 L_0=\left\lceil\binom nm q_0^{-w}\right\rceil,\qquad
 k=m-w-1.
\]

The exact prefix-list bijection supplies \(L_0\) distinct codewords of the
dimension-\((k+1)\) code.  The paper's collision-aware simple-pole conversion
then gives one line for the dimension-\(k\) code with at least

\[
 M(L_0)=
 \left\lceil
   \frac{L_0(Q-n)}{Q-n+k(L_0-1)}
 \right\rceil                                                   \tag{2}
\]

distinct MCA-bad slopes.

If the corrected counting gate (S) holds, then \(L_0\ge Q\).  Direct algebra
in (2) gives

\[
 \frac{L_0(Q-n)}{Q-n+k(L_0-1)}
 \ge \frac{Q-n}{k+1},
\]

because the inequality after cancellation is
\(L_0\ge Q-n-k\), which follows from \(L_0\ge Q\).  Therefore

\[
 \boxed{
 B_C^{\mathrm{MCA}}(m)
 \ge M(L_0)
 \ge \left\lceil\frac{Q-n}{k+1}\right\rceil.}             \tag{CA}
\]

This has two distinct readings.

1. **Finite \(2^{-128}\) target.**  Every corrected row satisfies
   \[
      M(L_0)>\left\lfloor Q/2^{128}\right\rfloor.
   \]
   Hence these are not merely candidate fibers; the already-proved theorem
   produces target-relevant bad lines.
2. **Asymptotic exponential scale.**  At fixed density \(k=\Theta(n)\), (CA)
   gives \(Q/e^{o(n)}\) slopes.  Thus no additional equidistribution theorem is
   needed to preserve the ambient-field exponent.  A uniform positive constant
   fraction of \(Q\), however, is not supplied because the normalized guarantee
   is only about \(1/(k+1)\).

For the explicit smooth multiplicative rows:

| \(p\) | \(k\) | \(\lfloor\log_2 Q\rfloor\) | \(\lfloor\log_2 M(L_0)\rfloor\) | target headroom above \(2^{-128}Q\) |
|---:|---:|---:|---:|---:|
| 1009 | 499 | 498 | 489 | 119 bits |
| 4099 | 2044 | 2040 | 2029 | 117 bits |
| 16411 | 8200 | 8191 | 8178 | 114 bits |

The headroom column is the exact floor of
\(\log_2(2^{128}M(L_0)/Q)\).  The generic \(q_0=n^C\) repaired rows have
headrooms \(115\), \(113\), and \(111\) bits respectively.

This is a lower/unsafe construction.  It does not prove that these slopes form
a surviving C7 primitive cell; first-match may assign them to earlier owners.
That semantic question is irrelevant to the validity of the MCA lower bound
but remains relevant to any proposed upper ledger.

### 4.1 Infinite smooth-multiplicative obstruction

The preceding finite rows are samples of an elementary infinite family.  Let
\(p\to\infty\) through primes and put

\[
 n=p-1,\qquad D=\mathbb F_p^\times,\qquad
 m=n/2,\qquad w=4,\qquad k=m-5.
\]

Let \(e=e_p\) be maximal with \(p^{2e}\le2^n\), and take
\(\mathbb F=\mathbb F_{p^e}\).  Then

\[
 \frac{2^{n/2}}p < Q=p^e\le2^{n/2},
 \qquad \log_2Q=\frac n2-O(\log n).                     \tag{3}
\]

The central binomial coefficient is the largest coefficient of
\((1+X)^n\), hence

\[
 \binom n{n/2}\ge\frac{2^n}{n+1}=\frac{2^n}{p}.         \tag{4}
\]

For every \(p\ge61\),

\[
 2^{n/2}=2^{(p-1)/2}\ge p^5.
\]

The base case is \(2^{30}\ge61^5\).  For odd \(p\ge61\), the ratio
\(2^{(p-1)/2}/p^5\) increases when \(p\) is replaced by \(p+2\), since

\[
 2\left(\frac p{p+2}\right)^5
 \ge 2\left(\frac{61}{63}\right)^5>1.
\]

Combining (3)--(4) gives

\[
 L_0
 \ge \frac{\binom n{n/2}}{p^4}
 \ge \frac{2^n}{p^5}
 \ge 2^{n/2}
 \ge Q.
\]

Therefore (CA) applies for every sufficiently large prime and yields

\[
 B_C^{\mathrm{MCA}}(m)
 \ge \left\lceil\frac{Q-n}{k+1}\right\rceil
 =\frac{Q}{\exp(o(n))}
 =2^{n/2-o(n)}.                                         \tag{5}
\]

Consequently, every target \(T_n=\exp(o(n))\) is crossed eventually.  This is
a theorem-level exponential-field obstruction obtained solely by composing
the paper's exact prefix floor and collision-aware pole conversion.  No
growing-dimensional character sum or constant-fraction equidistribution input
is needed.

Equation (5) gives only a \(1/\Theta(n)\) normalized fraction of \(Q\).  Thus a
fixed positive target \(\varepsilon Q\) on an exponential ambient field still
asks for a stronger constant-fraction theorem.  That question is now optional
for the current subexponential-target asymptotic frontier rather than a missing
C7 lower input.

## 5. Correct asymptotic boundary

Assume

\[
 \frac mn\to\beta\in(0,1),\qquad
 \frac{e\log_2q_0}n\to c,\qquad
 \frac{w\log_2q_0}n\to\lambda\ge0.
\]

Stirling gives

\[
 \log_2\binom nm=nH_2(\beta)+o(n),
 \qquad
 \log_2(L_0/Q)
 =n\bigl(\max\{H_2(\beta)-\lambda,0\}-c\bigr)+o(n).
\]

Consequently:

- if \(c>H_2(\beta)\), condition (N) fails exponentially and no
  fixed-target Case-B fiber exists even before the prefix cost;
- if \(c+\lambda<H_2(\beta)\), condition (S) holds with exponential room,
  and (CA) upgrades the pigeonhole support fiber to
  \[
       B_C^{\mathrm{MCA}}(m)\ge Q/\exp(o(n));
  \]
  in particular every target \(T_n=\exp(o(n))\) is crossed;
- at \(c+\lambda=H_2(\beta)\), finite constants and the exact prefix cost
  decide whether the collision-aware lower enters;
- the strip \(H_2(\beta)-\lambda<c\le H_2(\beta)\) is support-possible but
  not certified by the average-fiber route; an atypically heavy fiber or a
  different lower construction would be required there.

This is the corrected counting-and-conversion boundary.  What fails in the
source is its \(m=2e\) instantiation.  Since \(m=O(e)\) and
\(e\log q_0=\Theta(n)\) with \(\log q_0=\Theta(\log n)\) imply
\(m/n\to0\), such a sequence has \(H_2(m/n)=o(1)\) and cannot support a
positive ambient-field rate \(c\).

## 6. Research consequence

The remaining C7 corner must be posed on a fixed-density support layer:

\[
 m=\beta n+o(n),\qquad
 e=\Theta\!\left(\frac n{\log q_0}\right),\qquad
 e=o(m),
\]

not on the minimal \(m\asymp e\) slice.  This matters for the next analytic
step:

1. the fixed-\(e\) theorem remains valid on its stated bounded-degree slice;
2. its \(m=e+1\) degradation is not a calibration of the prize-admissible
   corner;
3. the corrected rows already have a theorem-level
   \(Q/e^{o(n)}\) bad-slope lower bound through collision-aware conversion;
4. first-match survival is unnecessary for that lower bound, but is still
   required before calling the family a surviving C7 primitive cell;
5. finite full-line censuses remain evidence only and do not transfer
   automatically to general sparse smooth/circle domains;
6. the C7 lower/falsification corner is closed for every
   \(T_n=\exp(o(n))\) by the infinite family above;
7. the remaining optional question is a **fixed-\(\varepsilon\) uniform
   constant-fraction** growing-\(e\) subset-product theorem, or a structural
   route for failures of such a theorem.

## 7. Verification

Run:

```bash
python3 experimental/scripts/verify_caseb_counting_domain_size_correction.py --check
python3 -O experimental/scripts/verify_caseb_counting_domain_size_correction.py --check
python3 experimental/scripts/verify_caseb_counting_domain_size_correction.py --check --tamper-selftest
python3 -O experimental/scripts/verify_caseb_counting_domain_size_correction.py --check --tamper-selftest
```

The verifier uses exact integers for every acceptance-critical comparison.  It
replays the three bad calibrations, proves the universal target impossibility,
checks both corrected fixed-density families, proves the primality and exact
half-rate degree of the multiplicative rows, composes the exact prefix floor
with theorem (4.2), checks all six target crossings, gates the elementary
\(p\ge61\) asymptotic family, checks the two exact counting gates, pins the
three source files, and rejects nine semantic mutations.  Every true-domain
binomial is independently reconstructed from Legendre prime exponents; every
wrong-universe binomial is independently replayed by the multiplicative
recurrence.

## 8. Scope and nonclaims

This packet does not prove a uniform constant-fraction growing-\(e\)
subset-product theorem, semantic C7 survival, removal of `(FI-field')`, a
deployed adjacent-row inequality, or any official prize claim.  It does prove
the corrected finite target crossings and an ambient-exponent lower bound.
Its status is:

\[
 \boxed{\texttt{COUNTEREXAMPLE / PROVED TARGET LOWER /
 OPEN CONSTANT-FRACTION EQUIDISTRIBUTION}}.
\]
