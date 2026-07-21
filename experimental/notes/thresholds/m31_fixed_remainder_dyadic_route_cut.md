```yaml
workboard_item: M1
row: Mersenne-31 list at 2^-100
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: "For every fixed-remainder dyadic Chebyshev complete-fiber family on the deployed domain, the post-C1 residual is empty at scales 2^1 through 2^17, while every remaining fixed-R prefix fiber has size at most 35."
architecture: GRANDE_FINALE_V3_EXACT_COMPLETION
partition_digest: null
atom_or_cell: C1_QUOTIENT_REMAINDER / M31_FIXED_REMAINDER_DYADIC_FOLD
quantifier: "for every 1<=s<=21 and every admissible fixed remainder R"
projection_and_unit: support fibers; no codeword projection claimed
claimed_bound: "0 after C1 for s<=17; at most 35 even pre-deletion for s>=18"
status: PROVED
impact: ROUTE_CUT
falsifier: "a fixed-R support at one enumerated dyadic scale that survives C1 and has more than the certified cap"
replay: "python3 experimental/scripts/verify_m31_fixed_remainder_dyadic_route_cut.py --check"
```

# M31 fixed-remainder dyadic fold route cut

## Status

```text
PROVED_EXACT_NAMED_ROUTE_CUT
route_cut = M31_FIXED_REMAINDER_DYADIC_FOLD_ROUTE_CUT
criterion_4_deployed_witness = NOT_FOUND
ledger_movement = 0
```

The Lane-F search did not produce a post-first-match configuration exceeding
the deployed Mersenne-31 list margin. It does remove one complete structured
attack class at all dyadic Chebyshev scales and also collapses global
multiplicative-domain symmetries to the already earlier antipodal owner.

The surviving named problem is

```text
M31_VARIABLE_REMAINDER_ORIENTATION_RESIDUAL
```

in which the remainder varies with the complete-fiber choice, or the support is
an antipodal transversal / isolated local coset rather than a fixed-remainder
complete-fiber profile.

## 1. Exact deployed target

The row is the auxiliary Mersenne-31 list stress test, not a `2^-128` Prize row:

\[
 p=2^{31}-1,\qquad
 n=2^{21}=2097152,\qquad
 k=2^{20}=1048576,
\]
\[
 a=1116023,\qquad
 M=n-a=981129,\qquad
 w=a-k=67447,
\]
\[
 B^*=2^{24}-1=16777215.
\]

The full-slice prefix average is

\[
 \overline F=\binom nM p^{-w}
 =1993677.11347033375755678821551\ldots,
\]
so

\[
 \lfloor\overline F\rfloor=1993677,\qquad
 \lceil\overline F\rceil=1993678,
\]
and

\[
 \frac{B^*}{\overline F}
 =8.41521171439662399020173440541\ldots.
\]

This is the binding few-bit calibration from workboard item M1.

## 2. Attacked family

Let \(D\subseteq\mathbb F_p\) be the deployed set of all roots of
\(T_{2^{21}}\). For \(1\le s\le21\), put

\[
 c_s=2^s,\qquad \phi_s=T_{c_s}\big|_D.
\]

Chebyshev composition gives

\[
 T_{2^{21}}=T_{2^{21-s}}\circ T_{2^s}.
\]

Using the norm-one parametrization of the deployed domain, multiplication of
the exponent by \(2^s\) has exactly \(2^s\) preimages after the inversion
identification. Thus \(\phi_s:D\to Q_s\) is a \(c_s\)-fold complete-fiber
folding map, with

\[
 N_s=|Q_s|=n/c_s.
\]

Fix a remainder set \(R\subseteq D\). The attacked family is

\[
 \mathcal F_{s,R}
 =
 \left\{
   \phi_s^{-1}(E)\sqcup R:
   E\in\binom{Q_s\setminus\phi_s(R)}{q_s}
 \right\},
\]
where

\[
 q_s=\left\lfloor\frac{M}{c_s}\right\rfloor,
 \qquad
 r_s=|R|=M\bmod c_s.
\]

The remainder is fixed across the family. This is exactly the
complete-fiber-plus-remainder object of
`def:quotient-remainder-profile`. No arbitrary varying-remainder family is
included.

## 3. Exact 21-scale census

| s | c=2^s | N=n/c | q=floor(M/c) | r=M mod c | exact route/cap |
|---:|---:|---:|---:|---:|---|
| 1 | 2 | 1048576 | 490564 | 1 | C1 quotient/remainder; post-C1 residual 0 |
| 2 | 4 | 524288 | 245282 | 1 | C1 quotient/remainder; post-C1 residual 0 |
| 3 | 8 | 262144 | 122641 | 1 | C1 quotient/remainder; post-C1 residual 0 |
| 4 | 16 | 131072 | 61320 | 9 | C1 quotient/remainder; post-C1 residual 0 |
| 5 | 32 | 65536 | 30660 | 9 | C1 quotient/remainder; post-C1 residual 0 |
| 6 | 64 | 32768 | 15330 | 9 | C1 quotient/remainder; post-C1 residual 0 |
| 7 | 128 | 16384 | 7665 | 9 | C1 quotient/remainder; post-C1 residual 0 |
| 8 | 256 | 8192 | 3832 | 137 | C1 quotient/remainder; post-C1 residual 0 |
| 9 | 512 | 4096 | 1916 | 137 | C1 quotient/remainder; post-C1 residual 0 |
| 10 | 1024 | 2048 | 958 | 137 | C1 quotient/remainder; post-C1 residual 0 |
| 11 | 2048 | 1024 | 479 | 137 | C1 quotient/remainder; post-C1 residual 0 |
| 12 | 4096 | 512 | 239 | 2185 | C1 quotient/remainder; post-C1 residual 0 |
| 13 | 8192 | 256 | 119 | 6281 | C1 quotient/remainder; post-C1 residual 0 |
| 14 | 16384 | 128 | 59 | 14473 | C1 quotient/remainder; post-C1 residual 0 |
| 15 | 32768 | 64 | 29 | 30857 | C1 quotient/remainder; post-C1 residual 0 |
| 16 | 65536 | 32 | 14 | 63625 | C1 quotient/remainder; post-C1 residual 0 |
| 17 | 131072 | 16 | 7 | 63625 | C1 quotient/remainder; post-C1 residual 0 |
| 18 | 262144 | 8 | 3 | 194697 | fixed-R cap 35 |
| 19 | 524288 | 4 | 1 | 456841 | fixed-R cap 3 |
| 20 | 1048576 | 2 | 0 | 981129 | fixed-R cap 1 |
| 21 | 2097152 | 1 | 0 | 981129 | fixed-R cap 1 |

The arithmetic has two exhaustive regimes.

### 3.1 Visible-remainder scales: \(1\le s\le17\)

Here

\[
 r_s\le w,\qquad q_s>0.
\]

By `thm:exact-quotient-remainder-normal-form` (QR2), every nonempty depth-\(w\)
prefix fiber determines \(R\) uniquely and is exactly one quotient-prefix
fiber after \(R\) is divided out. Under the active first-match convention that
assigns the declared quotient/remainder profile to C1, the post-C1 residual of
\(\mathcal F_{s,R}\) is empty.

This range includes:

- \(s=1\): antipodal complete fibers;
- \(s=2\): complete \(T_4\) blocks;
- every larger dyadic block scale through \(c=2^{17}\).

The conclusion is classification, not a numerical Q payment: any large raw
prefix fiber in these rows belongs to the earlier quotient owner and is not a
primitive M31 row-sharp survivor.

### 3.2 Prefix-shallow remainder scales: \(18\le s\le21\)

Here

\[
 w<r_s<c_s.
\]

By QR3--QR4 of `thm:exact-quotient-remainder-normal-form`, the first \(w\)
locator coefficients depend only on \(R\); the complete-fiber set \(E\) is
invisible. Consequently the fixed-\(R\) family occupies one prefix fiber and
has exact cardinality

\[
 \binom{N_s-|\phi_s(R)|}{q_s}.
\]

Since \(r_s>0\), one has \(|\phi_s(R)|\ge1\), hence

\[
 |\mathcal F_{s,R}|
 \le \binom{N_s-1}{q_s}.
\]

The four exact caps are

\[
 \binom73=35,\qquad
 \binom31=3,\qquad
 \binom10=1,\qquad
 \binom00=1.
\]

Therefore

\[
 \max_{18\le s\le21}\max_R |\mathcal F_{s,R}|=35
 <1993678
 <16777215.
\]

The late dyadic block mechanism misses even one full-slice average, before any
other owner consumes reserve.

## 4. Main route-cut theorem

**Theorem (M31 fixed-remainder dyadic fold route cut).**
Assume the deployed domain and row constants above, the complete-fiber
Chebyshev maps \(\phi_s\), and the active first-match rule assigning declared
quotient/remainder profiles to C1. For every \(1\le s\le21\) and every
admissible fixed remainder \(R\):

1. if \(s\le17\), the post-C1 residual of \(\mathcal F_{s,R}\) is empty;
2. if \(s\ge18\), every depth-\(w\) fixed-\(R\) prefix fiber has at most \(35\)
   supports, even without deleting any earlier owner.

Hence no family \(\mathcal F_{s,R}\) can produce a post-first-match max-fiber
ratio exceeding the deployed M31 list allowance.

**Proof.**
The exact table proves the split \(r_s\le w\) for \(s\le17\) and
\(w<r_s<c_s\) for \(s\ge18\). Apply QR2 in the first range and the active C1
owner order. Apply QR4 in the second range and use
\(|\phi_s(R)|\ge1\). The four binomial evaluations are exact integers.
\(\square\)

## 5. Global multiplicative-domain symmetry also collapses to C1

This is a separate source-level lemma supporting the same route cut.

Let \(P_n=2^{1-n}T_n\) be the monic deployed root polynomial. Its next
coefficient is

\[
 [X^{n-2}]P_n=-n/4\ne0\quad\text{in }\mathbb F_p.
\]

Indeed, for the unnormalized Chebyshev polynomial the leading and next
coefficients reduce modulo \(p\) to

\[
 2^{n-1}=2,\qquad
 -n2^{n-3}=p-2^{20}=2146435071,
\]
so the normalized coefficient is
\(2146959359\ne0\).

Suppose \(\lambda\in\mathbb F_p^\times\) globally permutes the deployed domain:
\(\lambda D=D\). The monic polynomials with that root set satisfy

\[
 P_n(\lambda X)=\lambda^nP_n(X).
\]

Comparing the nonzero \(X^{n-2}\) coefficients gives

\[
 \lambda^{n-2}=\lambda^n,
 \qquad\text{hence}\qquad
 \lambda^2=1.
\]

Since \(\mathbb F_p\) is a field of odd characteristic,
\(\lambda=\pm1\). The nontrivial case is precisely the antipodal
\(c=2\) folding already in the first row of the route-cut table.

Thus a multiplicative-coset construction coming from a scalar action on the
whole deployed domain supplies no new post-C1 family. This does **not**
classify isolated multiplicative cosets contained only in a proper subset of
\(D\).

## 6. Why this is a route cut rather than a row theorem

The result removes the full fixed-remainder dyadic block family, including
antipodal and \(T_4\)-block combinations. It does not bound the actual full
post-C1 residual. In particular, it leaves open:

- remainders that vary with \(E\);
- partial-occupancy profiles with \(|R|\ge c\);
- antipodal transversals choosing one point from many pairs;
- isolated local multiplicative cosets;
- arbitrary list-interior codeword multiplicity;
- the support-to-codeword and received-word realization needed for a direct
  list-row counterexample;
- every other owner, add-back, and row-summation obligation.

Accordingly the packet records no \(U_Q\), no \(U_{\rm list,int}\), no ledger
movement, and no adjacent-row closure.

## 7. Formal and computational certificates

The stdlib-only Lean module is

```text
experimental/lean/sidon_effective_image/
  SidonEffectiveImage/M31DyadicBlockRouteCut.lean
```

It checks all 21 division rows, the C1-visible split, the exact late caps
`35,3,1,1`, the margin bracket, and the antipodal/T4 entries. It imports only
the integrated `M31QRootedShell.Deployed` API and does not import any open-PR
module.

Replay:

```text
python3 experimental/scripts/verify_m31_fixed_remainder_dyadic_route_cut.py --check
python3 -O experimental/scripts/verify_m31_fixed_remainder_dyadic_route_cut.py --check
python3 experimental/scripts/verify_m31_fixed_remainder_dyadic_route_cut.py --tamper-selftest
```

The JSON certificate is

```text
experimental/data/certificates/m31-fixed-remainder-dyadic-route-cut/
  m31_fixed_remainder_dyadic_route_cut.json
```

It recomputes the exact binomial average, every dyadic division row, every late
binomial cap, the deployed Chebyshev coefficient residues, and the imported API
blob identities.

# ROUTE CUT
