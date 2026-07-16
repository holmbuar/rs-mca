# Balanced-core factored-rank audit

**Status:** PROVED / AUDIT / COUNTEREXAMPLE.
**Lane:** adversarial proof audit, hard input 3 (balanced-core residuals).
**Scope:** correct two experimental notes and add an exact checked certificate.
No TeX, Lean, README, HTML, deployment, or theorem-row file is changed.

## 1. Claim under audit

The raw-family identity used in
experimental/notes/thresholds/balanced_core_kappa_growth.md is correct. The
defect occurs when that note factors a common agreement core, declares the
residual core empty, and continues to use the original RS dimension **k**.
Common-core factorization shortens the row, so the dimension changes too.

The audited conclusions are:

- **PROVED:** for a raw family,
  **kappa=max(0,k-|intersection S_gamma|)**.
- **COUNTEREXAMPLE:** after factoring a core **K** with **|K|<=k**, an empty
  residual intersection does not imply **kappa=k** for the original row.
- **PROVED:** in that range, the correct conclusion is
  **kappa=k'=k-|K|** when the full core is factored. If the full raw core has
  size greater than **k**, equation (2.1) already gives zero nullity; no
  negative-dimensional shortened row is asserted.
- **OPEN GAP:** residuality alone does not show that **k'=Theta(n)**.
- **NO ISSUE:** thm:fixed-core-determinacy-ray in
  experimental/rs_mca_thresholds.tex already uses the shortened dimension
  **k-c**.

## 2. Rank types and shortening law

Let

\[
 C=\operatorname{RS}_{\mathbb F}(D,k),\qquad |D|=n,\qquad R=n-k,
\]

and let \(\mathcal F=\{S_\gamma\}\) be a nonempty family of agreement supports.
Put

\[
 C_{\rm raw}=\bigcap_\gamma S_\gamma,\qquad
 U_{\rm raw}=\bigcup_\gamma(D\setminus S_\gamma)
            =D\setminus C_{\rm raw}.
\]

The MDS/Vandermonde rank identity gives

\[
 \kappa_{\rm raw}
 =\dim\ker H_{U_{\rm raw}}
 =\max\{0,|U_{\rm raw}|-R\}
 =\max\{0,k-|C_{\rm raw}|\}.                 \tag{2.1}
\]

Now factor a fixed common core \(K\subseteq C_{\rm raw}\), with
\(c=|K|\leq k\).
The shortened row is

\[
 D'=D\setminus K,\qquad n'=n-c,\qquad
 k'=k-c,\qquad R'=n'-k'=R.                  \tag{2.2}
\]

For \(S'_\gamma=S_\gamma\setminus K\) and
\(C'=\bigcap_\gamma S'_\gamma=C_{\rm raw}\setminus K\),

\[
 \kappa'
 =\max\{0,k'-|C'|\}.                         \tag{2.3}
\]

If \(K=C_{\rm raw}\) (and hence \(|C_{\rm raw}|\leq k\)), then
\(C'=\varnothing\), but (2.3) reads

\[
 \kappa'=k'=k-|K|,                           \tag{2.4}
\]

not the original \(k\). Equations (2.2)--(2.3) agree with the shortening
bijection and kernel calculation in
experimental/notes/thresholds/common_core_cover_obstruction.md, equations
(2.5)--(2.6), and with thm:fixed-core-determinacy-ray.

There is no paradox in (2.1) and (2.4): in the stated range, full-core
shortening preserves the correctly computed nullity \(k-|C_{\rm raw}|\), while
changing the row dimension against which an empty residual intersection is
interpreted. When \(|C_{\rm raw}|>k\), (2.1) gives \(\kappa_{\rm raw}=0\) and
the factor-aware high-kernel question is already vacuous.

## 3. Exact transverse witness over F_11

Take

\[
 p=11,\quad D=\{1,\ldots,7\},\quad n=7,\quad k=2,\quad R=5,
 \quad a=4,\quad w=1,
\]

and the agreement supports

\[
\begin{aligned}
 S_0&=\{1,2,3,7\},\\
 S_1&=\{1,2,4,6\},\\
 S_2&=\{1,3,4,5\}.
\end{aligned}
\]

Their monic locator polynomials, written in descending coefficient order
modulo 11, are

\[
 [1,9,9,5,9],\qquad [1,9,1,7,4],\qquad [1,9,4,3,5].
\]

Thus all three share the depth-one prefix \([1,9]\). Their full common
agreement core is \(K=\{1\}\).

### 3.1 Factorization and moving dimension

After division by \(X-1\), the residual supports are

\[
 \{2,3,7\},\qquad \{2,4,6\},\qquad \{3,4,5\},
\]

and the residual locator coefficient vectors are

\[
 [1,10,8,2],\qquad [1,10,0,7],\qquad [1,10,3,6].
\]

The residual intersection is empty. The two deep-coefficient differences have
determinant

\[
 \det\begin{pmatrix}3&5\\6&4\end{pmatrix}=4\pmod {11},
\]

so the affine/projective moving dimension is exactly two. This remains a
genuinely higher-dimensional residual locator family after factorization.

### 3.2 Rank

The shortened row has

\[
 D'=\{2,\ldots,7\},\qquad n'=6,\qquad k'=1,\qquad R'=5.
\]

The exact Vandermonde calculation gives

\[
 \operatorname{rank}H_{D'}=5,\qquad
 \kappa'=|D'|-5=1=k'\ne k=2.                 \tag{3.1}
\]

Equation (3.1) is the finite counterexample to retaining the original \(k\).

### 3.3 Actual syndrome line and transversality

Let \(H_x=(1,x,x^2,x^3,x^4)^T\) over \(\mathbb F_{11}\). The error supports,
which are the complements of the three agreement supports in \(D\), are

\[
 E_0=\{4,5,6\},\qquad E_1=\{3,5,7\},\qquad E_2=\{2,6,7\}.
\]

Use the nonzero error coefficients

\[
\begin{aligned}
 c_0&=\{4:10,5:3,6:4\},\\
 c_1&=\{3:8,5:1,7:1\},\\
 c_2&=\{2:1,6:1,7:1\}.
\end{aligned}
\]

For

\[
 y_0=(6,2,5,9,5),\qquad y_1=(4,1,9,4,6),
\]

the verifier checks exactly that

\[
 Hc_\gamma=y_0+\gamma y_1,\qquad \gamma=0,1,2.
\]

For every \(E_\gamma\),

\[
 \operatorname{rank}H_{E_\gamma}=3,\qquad
 \operatorname{rank}[H_{E_\gamma}\mid y_0\mid y_1]=4.
\]

Hence the syndrome line meets each support image in the certified slope but is
not contained in that image. The witness therefore consists of exact,
noncommon, transverse realized slopes rather than formal locator parameters.

## 4. Exhaustive finite census

There are 20 four-subsets of \(D\) that contain \(1\), hence

\[
 {20\choose3}=1{,}140
\]

unordered triples. Exact exhaustion gives:

- 480 triples have full common core exactly \(\{1\}\);
- four of those triples have a common depth-one locator prefix;
- after factoring \(X-1\), all four have empty residual core and moving
  dimension two.

The four prefix triples are

\[
\begin{aligned}
&(\{1,2,3,7\},\{1,2,4,6\},\{1,3,4,5\}),\\
&(\{1,2,4,7\},\{1,2,5,6\},\{1,3,4,6\}),\\
&(\{1,2,5,7\},\{1,3,4,7\},\{1,3,5,6\}),\\
&(\{1,2,6,7\},\{1,3,5,7\},\{1,4,5,6\}).
\end{aligned}
\]

This census establishes the finite rank/type boundary. It is not an
asymptotic slope-mass theorem.

## 5. Impact and preserved results

The correction is deliberately narrow.

Preserved:

- the raw rank identity (2.1);
- the raw empty-core PTM examples;
- the exact raw prefix-support census in verify_kappa_growth.py;
- the kernel-independent shallow-prefix closure routing in the A4 note; and
- the governing conditional TeX statements.

Retracted or narrowed:

- “factoring the core leaves k unchanged”;
- “residual implies original kappa=k=Theta(n)”;
- “most raw prefix members” as a proxy for “most realized slopes”; and
- any claim that small-kappa sharpness rules out a different
  structure-sensitive estimate at large kernel.

Hard input 3 remains open: control the factored size \(|K|\), the shortened
rate \(k'/n'\), and the projection to actual first-match distinct slopes.

## 6. Reproduction and tamper gates

Run from the repository root:

~~~bash
python3 experimental/scripts/verify_balanced_core_factored_rank.py
python3 -O experimental/scripts/verify_balanced_core_factored_rank.py
python3 experimental/scripts/verify_balanced_core_factored_rank.py --tamper-selftest
python3 -O experimental/scripts/verify_balanced_core_factored_rank.py --tamper-selftest
python3 experimental/scripts/verify_balanced_core_factored_rank.py \
  --emit-certificate /tmp/balanced_core_factored_rank.json
cmp -s \
  experimental/data/certificates/balanced-core-factored-rank/balanced_core_factored_rank.json \
  /tmp/balanced_core_factored_rank.json
~~~

The normal and optimized runs exhaust all 1,140 triples. The tamper self-test
rejects 5/5 mutations: locator coefficient, use of the unfactored \(k\),
syndrome line, exact-core census, and projective dimension. The checked
certificate SHA-256 is

~~~
b53d34728090219f9fd3e5a88e28d9af7858c5b8cf40a397fe2bfd58f73bbd33
~~~

The certificate is checked data, not trusted input: the verifier recomputes the
witness and census before comparing them with the JSON.

## 7. Next action

Either prove that every large actual first-match balanced-core residual has
\(k-|K|=\Theta(n)\), or certify a small-shortened-dimension/A4/direct-payment
dichotomy. Any future census must keep raw support families, shortened rows,
and realized distinct slopes as separate types.
