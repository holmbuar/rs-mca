```yaml
workboard_item: M1
row: Mersenne-31 ordinary-list stress row at 2^-100
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: "At delta=981129/2097152, q*epsilon_CA(C,delta)<=16777214 implies |Lambda(C,delta)|<=16777215; the BCHKS25 conclusion |Lambda(C,delta)|<q is an exact route cut for this budget."
architecture: DIRECT
partition_digest: null
atom_or_cell: DIRECT
quantifier: "maximum number of ordinary C=RS_F(D,1048576) codewords in one closed Hamming ball around one received word"
projection_and_unit: codewords
claimed_bound: "conditional 16777215 via CS25; BCHKS25 route-cut upper 21267647892944572736998860269687930880"
status: PROVED / CONDITIONAL / AUDIT
impact: ROUTE_CUT
falsifier: "an eta making both CS25 gates hold at integer CA numerator 16777215, or a source convention invalidating the printed C/C^+ and radius assignments"
replay: "python3 experimental/scripts/verify_m31_postjohnson_conversion_contract.py --check; python3 experimental/scripts/verify_m31_postjohnson_conversion_contract.py --tamper-selftest"
```

# M31 post-Johnson ordinary-list conversion contract

## Claim and status

This packet freezes the deployed Mersenne-31 **ordinary-list** row and proves an
exact gate-C conversion contract.  It does not prove the row's unconditional list
upper bound and it does not construct a budget-crossing received word.

Let

\[
 p=2^{31}-1=2147483647,\qquad
 q=|\mathbb F|=p^4
 =21267647892944572736998860269687930881,
\]
\[
 n=2^{21}=2097152,\qquad k=2^{20}=1048576,
 \qquad C=\operatorname{RS}_{\mathbb F}(D,k),
\]
where \(D=\chi(\text{twin coset})\) is the full deployed evaluation domain.
The code convention is degree \(<k\), so the containing partner used by CS25 is

\[
 C^+=\operatorname{RS}_{\mathbb F}(D,k+1),\qquad C\subset C^+.
\]

At the row radius

\[
 a=1116023,\qquad
 \delta_{\rm row}=\frac{981129}{2097152},\qquad
 w=a-k=67447,
\]
put

\[
 B^*=\left\lfloor\frac q{2^{100}}\right\rfloor
 =16777215.
\]

The exact result is:

> **Conditional CS bridge.**  If the integer CA numerator for
> \(C=\operatorname{RS}_{\mathbb F}(D,k)\) at
> \(\delta_{\rm row}=981129/2097152\) satisfies
> \[
> q\,\epsilon_{\rm CA}(C,\delta_{\rm row})\le16777214,
> \]
> then
> \[
> |\Lambda(C^+,\delta_{\rm row})|\le16777215,
> \]
> and therefore, by \(C\subset C^+\),
> \[
> |\Lambda(C,\delta_{\rm row})|\le16777215.
> \]
> The input \(16777214=B^*-1\) is the largest possible integer input to
> this theorem at the target ceiling.  Input \(B^*\) is impossible for every
> admissible \(\eta\).

The bridge is non-vacuous: \(\eta=1/B^*\) certifies the endpoint
\(E=B^*-1\).  It does **not** follow from the adjacent M31 MCA-row statement at
agreement \(1116024\): that statement is at one smaller error radius and allows
one additional bad slope.

## Mandatory packet block

```text
row:                 (F_{p^4}, D=chi(twin coset), k=1048576, n=2097152, rho=1/2)
object:              ordinary LIST, not MCA
radius/agreement:    delta=981129/2097152 and integer agreement 1116023
Johnson comparison:  delta_Johnson=614241/2097152 and post-Johnson gap 366888
bound:               CONDITIONAL |Lambda(C,delta)|<=16777215 from q*epsilon_CA(C,delta)<=16777214; BCHKS route-cut upper q-1
route:               CS_CA_TO_LIST / BCHKS_CA_TO_LIST
CA_or_MCA_input:     q*epsilon_CA(C,delta)<=16777214 for CS; epsilon_CA(C,981131/n,1048575/n)<1/4194304 for BCHKS
code_shift:          C=RS(k); C^+=RS(k+1), with C subset C^+
status:              PROVED / CONDITIONAL / AUDIT
```

## R0 — row freeze and exact Johnson block

### Domain, code, radius, and budget

The full domain has \(n=2097152\) coordinates.  The value \(2097144=n-8\)
belongs to the punctured MCA working profile and is not used in any list-row
binomial or theorem in this packet.

The packet row is \(C=\operatorname{RS}_{\mathbb F}(D,k)\), dimension \(k\),
with degree \(<k\).  Its CS25 partner is
\(C^+=\operatorname{RS}_{\mathbb F}(D,k+1)\).  Their exact MDS distances are

\[
 d_{\min}(C)=\frac{1048577}{2097152},\qquad
 d_{\min}(C^+)=\frac{1048576}{2097152}=\frac12.
\]

The packet's capacity convention is

\[
 \delta_{\min}=1-\rho=\frac12.
\]

The floor/ceiling distinction is exact:

\[
 q=2^{100}\cdot16777215
   +1228036518998767348801905623041,
\]
hence

\[
 \left\lfloor q/2^{100}\right\rfloor=16777215,\qquad
 \left\lceil q/2^{100}\right\rceil=16777216.
\]

For the full support slice,

\[
 \left\lfloor\frac{\binom{2097152}{1116023}}{p^{67447}}\right\rfloor
 =1993677,\qquad
 \left\lceil\frac{\binom{2097152}{1116023}}{p^{67447}}\right\rceil
 =1993678,
\]
and

\[
 \left\lfloor
 \frac{B^*p^{67447}}{\binom{2097152}{1116023}}
 \right\rfloor=8.
\]

Thus the average ceiling is \(14783537\) below the budget, but the exact
full-budget multiplier has floor only \(8\).

### Johnson route A: exact finite-\(q\), finite-list inequality

The requested conservative comparison is for the containing code
\(C^+=\operatorname{RS}_{\mathbb F}(D,k+1)\), whose distinct codewords agree
on at most \(k=1048576\) coordinates.  Put \(\ell=B^*=16777215\).
After clearing the square root in the exact \(J_{q,\ell}\) formula from
`open-proximity.tex`, agreement \(A\) is Johnson-covered exactly when

\[
\begin{aligned}
M_{q,\ell}(A):={}&(\ell-1)(qA-n)^2\\
&-\left(n^2(q-1)^2(\ell-1)
 -n(q-1)q\ell(n-k)\right)\ge0.
\end{aligned}
\]

The two boundary evaluations are

\[
\begin{aligned}
M_{q,\ell}(1482910)
={}&-8016391725505050246066417496357516786153876577101023083937102496439633020969773596132104,\\
M_{q,\ell}(1482911)
={}&14489887525701682981712437636783439750805076991890876089727149238354095278314282946247294.
\end{aligned}
\]

Therefore the exact integer Johnson agreement is

\[
 a_J(C^+,\ell)=1482911,\qquad
 \delta_J=\frac{2097152-1482911}{2097152}
 =\frac{614241}{2097152}.
\]

### Johnson route B: direct quadratic agreement inequality

The independent MDS/Plotkin calculation uses

\[
 A^2>n k.
\]

At the same two integers,

\[
1482910^2-nk=-1187452,\qquad
1482911^2-nk=1778369.
\]

At \(A=1482911\), the exact quadratic list cap is

\[
 \left\lfloor
 \frac{n(A-k)}{A^2-nk}
 \right\rfloor
 =
 \left\lfloor\frac{910866513920}{1778369}\right\rfloor
 =512192
\]
with remainder \(139072\), so it is below \(B^*\).  The preceding integer has
a negative denominator.  This independently recovers the same integer
Johnson radius.

For completeness, the packet code \(C=\operatorname{RS}_{\mathbb F}(D,k)\)
itself has pairwise agreement at most \(k-1\), so its own Johnson boundary is
one agreement earlier:

\[
 a_J(C,\ell)=1482910,\qquad
 \delta_J(C)=\frac{614242}{2097152},
\]
with quadratic denominator \(909700\) and cap \(1001282\).  The mandatory
comparison above uses \(C^+\), as required by the conversion convention.

The stress row therefore lies exactly

\[
 \delta_{\min}-\delta_{\rm row}
 =\frac{67447}{2097152}
\]
below capacity, and exactly

\[
 \delta_{\rm row}-\delta_J
 =\frac{366888}{2097152}
 =\frac{45861}{262144}
\]
beyond the conservative \(C^+\) Johnson radius.  The locator degree identity

\[
 n-a=981129
\]
matches the live M31 locator degree, but it does not identify the packet list
code with \(C^+\).

## R1 — two direct-list attacks

### Attack 1: classical Johnson/Plotkin at the stress row

For the packet code \(C=\operatorname{RS}_{\mathbb F}(D,k)\),

\[
 a^2-n(k-1)=-953513821871.
\]

For its containing partner \(C^+\),

\[
 a^2-nk=-953515919023.
\]

Both denominators are negative, so neither classical Johnson theorem gives any
upper certificate at agreement \(1116023\).

### Attack 2: support-averaging shortening followed by Johnson

Shorten \(C\) on \(s\) common agreement coordinates.  The shortened quadratic
denominator is

\[
\begin{aligned}
D(s)
&=(a-s)^2-(n-s)(k-s-1)\\
&=-953513821871+913681s.
\end{aligned}
\]

It first becomes positive at

\[
 s_J=1043596,
\]
because

\[
 D(1043595)=-898676,\qquad D(1043596)=15005.
\]

At activation,

\[
 n'=1053556,\qquad k'=4980,\qquad a'=72427,
\]
and the shortened Johnson cap is

\[
 \left\lfloor
 \frac{1053556(72427-4979)}{15005}
 \right\rfloor
 =4735771
\]
with remainder \(1233\).

The standard support-averaging loss is already larger than the entire row
budget after only \(27\) shortened coordinates:

\[
 \left\lfloor
 \frac{\binom{2097152}{27}}{\binom{1116023}{27}}
 \right\rfloor
 =24940004
 =B^*+8162789.
\]

The ratio is increasing in \(s\), while \(s_J\gg27\).  Consequently, even a
hypothetical shortened cap of \(1\) would pull back above \(B^*\) by the time
Johnson activates.  This is an exact route cut for the standard
shortening-plus-Johnson composition, not a general impossibility theorem for
all shortening arguments.

No direct theorem moving \(U_{\rm list,int}\) is obtained.

## R2 — two independent witness searches, plus a structured control

### Identity-prefix family

The exact pigeonhole family gives one received word with at least

\[
 \left\lceil\binom n a/p^w\right\rceil=1993678
\]
ordinary \(C\)-codewords.  This is a valid list lower bound but remains

\[
 16777215-1993678=14783537
\]
below the target.

### Round-robin coset family from the #169 route cut

The proved \(t=3\) round-robin-coset reconstruction theorem collapses every
interior stratum to exactly \(0\) or \(1\) distinct listed codeword.  It cannot
cross the deployed budget.  The measured \(t\ge5\) polynomial counts in that
note are experimental and are not promoted to a deployed witness.

### Fixed-remainder dyadic/Chebyshev family

For the deployed M31 domain, the proved fixed-remainder family is post-C1 empty
at scales \(2^1,\ldots,2^{17}\); at the four remaining scales its raw support
fiber has size at most \(35\).  This is only a support-family route cut:
it is not relabeled as a list upper bound.  It supplies no ordinary-codeword
witness above \(B^*\).

No mechanized budget-crossing received word was found, so gate B is not
claimed.

## R3(i) — CS25 exact conversion contract

**Code roles.**
Here and only here,

\[
 C=\operatorname{RS}_{\mathbb F}(D,k),\qquad
 C^+=\operatorname{RS}_{\mathbb F}(D,k+1).
\]

**Radius.**
Both the CA input and the list output use exactly

\[
 \delta=\delta_{\rm row}=\frac{981129}{2097152}.
\]

**Field denominator.**
All CA probabilities have denominator

\[
 q=21267647892944572736998860269687930881.
\]

Let

\[
 E=q\,\epsilon_{\rm CA}(C,\delta)\in\mathbb Z_{\ge0}.
\]

The CS25 premise and the target ceiling are respectively

\[
 E\le\eta\frac{q-n}{k},
 \qquad
 \left\lceil\frac{E}{1-\eta}\right\rceil\le B^*.
\]

For an integer \(E\), the exact feasible window is therefore

\[
 \boxed{\quad
 \frac{kE}{q-n}\le\eta\le\frac{B^*-E}{B^*}
 \quad}
\]
with \(0\le\eta<1\).  Equivalently, in \((\epsilon,\eta)\)-coordinates,

\[
 0\le\epsilon\le
 \min\left\{
 \eta\frac{q-n}{kq},\,
 \frac{B^*(1-\eta)}q
 \right\}.
\]

The two boundaries balance at

\[
 \eta_*=
 \frac{B^*k}{q-n+B^*k}
 =
 \frac{17592184995840}
 {21267647892944572736998877861870829569}
\]
and

\[
 E_*=
 \frac{B^*(q-n)}{q-n+B^*k}
 =
 \frac{
 356811901244228079891768333499477214925684735
 }{
 21267647892944572736998877861870829569
 }.
\]

Exact division gives

\[
 \lfloor E_*\rfloor=16777214,
\]
with remainder

\[
 21267647892944572441851007866889043969.
\]

Hence \(B^*-1\) is the maximal integer input.  The endpoint is genuinely
attained: take

\[
 E=B^*-1=16777214,\qquad \eta=\frac1{B^*}=\frac1{16777215}.
\]

The premise margin is

\[
 (q-n)-B^*(B^*-1)k
 =
 21267647892944572441851007866889043969>0,
\]
and the output is exactly

\[
 \left\lceil
 \frac{B^*-1}{1-1/B^*}
 \right\rceil=B^*.
\]

At \(E=B^*\), the output condition forces \(\eta=0\), while the premise then
forces \(E=0\).  Thus the ceiling costs exactly one bad slope.

### Is the packet list row the literal CS image of the MCA row?

No.

1. The packet list row is \(C=\operatorname{RS}_{\mathbb F}(D,k)\), while
   CS25 outputs a bound for the containing \(C^+\).  This mismatch is harmless
   for an upper bound because \(C\subset C^+\), but the row is not literally
   \(C^+\).
2. The live adjacent MCA row is for the same base code \(C\) at agreement
   \(1116024\), namely error radius \(981128/2097152\).  CS25 needs CA at the
   larger radius \(981129/2097152\).  Monotonicity goes in the wrong direction
   for transferring the smaller-radius upper bound.
3. Even at the correct radius, a numerator bound \(B^*\) is one count too weak;
   the exact CS input is \(B^*-1\).

The corrected non-vacuous bridge is therefore:

\[
\boxed{
 B_{\rm CA}^C(1116023)\le16777214
 \Longrightarrow
 |\Lambda(C^+,981129/2097152)|\le16777215
 \Longrightarrow
 |\Lambda(C,981129/2097152)|\le16777215.
}
\]

Since \(B_{\rm CA}\le B_{\rm MCA}\), the same conclusion follows from an MCA
numerator at most \(16777214\) **at agreement \(1116023\)**.  It does not
follow from the candidate MCA closure at agreement \(1116024\).

## R3(ii) — BCHKS25 exact two-radius route cut

**Code role.**
BCHKS25 is applied directly to
\(C=\operatorname{RS}_{\mathbb F}(D,k)\); there is no \(C^+\) shift.

**Radii.**
The exact two-radius input is

\[
 \delta_{\rm fld}
 =\delta_{\rm row}+\frac2n
 =\frac{981131}{2097152},
\]
\[
 \delta_{\rm intr}
 =1-\rho-\frac1n
 =\frac{1048575}{2097152},
\]
with exact window

\[
 \delta_{\rm intr}-\delta_{\rm fld}
 =\frac{67444}{2097152}
 =\frac{16861}{524288}.
\]

**Field denominator and premise.**
The theorem asks for

\[
 \epsilon_{\rm CA}(C,\delta_{\rm fld},\delta_{\rm intr})
 <\frac1{2n}=\frac1{4194304}.
\]

Writing its integer numerator as \(E_{\rm BCHKS}\), the exact congruence is

\[
 q=4194304\cdot
 5070602391468184646844592158720+1.
\]

Thus the largest integer numerator satisfying the strict premise is

\[
 E_{\rm BCHKS}=5070602391468184646844592158720;
\]
the lower and upper strictness margins are exactly \(1\) and \(4194303\).

The conclusion is only

\[
 |\Lambda(C,\delta_{\rm row})|<q,
\]
hence the integer upper bound

\[
 q-1=21267647892944572736998860269687930880.
\]

Its exact division by the row budget is

\[
 q-1=
 16777215\cdot
 1267650673424914250487870619151
 +8486415.
\]

The quotient exceeds \(2^{100}\) by

\[
 73196684848991167413775,
\]
and

\[
 (q-1)-2^{100}B^*
 =1228036518998767348801905623040>0.
\]

Therefore BCHKS25, even assuming its two-radius premise, lands more than
\(2^{100}\) times above the row budget.  This is a proved exact route cut.

## R3(iii) — GCXK25 reverse conversion, literal-source audit

**Code role.**
This subsection starts from a hypothetical list closure for the packet code

\[
 C=\operatorname{RS}_{\mathbb F}(D,k):
 \qquad |\Lambda(C,\delta_{\rm row})|\le B^*.
\]

**Field denominator.**
The MCA probability is divided by the same exact \(q\).

The literal formula printed in `open-proximity.tex` gives, for
\(0<\eta<1\),

\[
 \epsilon_{\rm MCA}\left(
 C,\,
 1-\sqrt{1-\delta_{\rm row}}+\eta
 \right)
 \le
 \frac{(B^*)^2\delta_{\rm row}n+1/\eta}{q}.
\]

Here

\[
 (B^*)^2\delta_{\rm row}n
 =(16777215)^2\cdot981129
 =276163229503923878025.
\]

Thus the exact rational trade-off in the repository transcription is

\[
 q\,\epsilon_{\rm MCA}
 \le276163229503923878025+\frac1\eta.
\]

In particular, \(\eta=1/t\) gives the integer numerator bound

\[
 B_{\rm MCA}\le276163229503923878025+t.
\]

To make the printed radius equal the adjacent MCA-row radius
\(981128/2097152\), one must take

\[
 \eta_0=
 \sqrt{\frac{1116023}{2097152}}
 -\frac{1116024}{2097152}.
\]

Two exact squared comparisons give

\[
 \frac16<\eta_0<\frac15:
\]
\[
 36\cdot1116023\cdot2097152
 -(6\cdot1116024+2097152)^2
 =6934860650240>0,
\]
\[
 (5\cdot1116024+2097152)^2
 -25\cdot1116023\cdot2097152
 =428758699584>0.
\]

Hence \(5<1/\eta_0<6\), and integrality yields

\[
 B_{\rm MCA}(1116024)
 \le276163229503923878030.
\]

This is

\[
 16777215\cdot16460612175735+5,
\]
so even the hypothetical list closure would buy only an MCA numerator more
than \(16\) trillion row budgets under this formula.

### Source-sign guard

The repository transcription uses a \(+\eta\) radius, which is monotonicity-
suspicious because increasing \(\eta\) simultaneously enlarges the radius and
improves the displayed bound.  The cited GCXK25 abstract is worded with a
different smaller-radius expression.  This packet does not reconcile those
forms.  Consequently this subsection is an exact algebraic audit of the
repository source only, not a bankable external-theorem consequence.  No
result in the CS or BCHKS subsections depends on this guarded formula.

## R4 — adversarial epilogue

The strongest surviving claim is the CS endpoint
\(E_{\max}=B^*-1\).  The adversarial pass attacked it in five ways.  First,
allowing real \(\epsilon_{\rm CA}\) does not help because \(q\epsilon_{\rm CA}\)
is an integer bad-slope count.  Second, \(\eta=0\) cannot admit \(E=B^*\):
the CS premise then forces \(E=0\).  Third, every \(\eta>0\) makes
\(E/(1-\eta)>B^*\) when \(E=B^*\).  Fourth, passing from \(C^+\) back to
\(C\) by inclusion removes the code mismatch but not the ceiling loss.
Fifth, the adjacent MCA row is at the smaller radius and monotonicity cannot
move its upper bound to the list radius.  All five attacks fail to enlarge the
endpoint.  The separate GCXK sign attack succeeds only in limiting that
subsection's status to a guarded source audit; it does not affect the CS
contract.

## Independent-integer replay ledger

Every verdict-bearing integer is computed twice by the verifier.

| Block | Route 1 | Route 2 |
|---|---|---|
| \(q=p^4\) | repeated exponentiation | binomial expansion of \((2^{31}-1)^4\) |
| full-slice average | `math.comb` | Legendre prime-exponent factorization |
| Johnson boundary | exact finite-\(q,\ell\) cleared inequality | direct MDS quadratic inequality |
| Johnson caps | exact integer division | neighboring-sign boundary checks |
| shortening activation | expanded affine formula for \(D(s)\) | direct substituted quadratic |
| shortening loss | binomial ratio | falling-product ratio |
| CS endpoint | exact rational floor of \(E_*\) | explicit \(\eta=1/B^*\) cross-multiplication |
| BCHKS strict input | quotient/remainder by \(2n\) | two neighboring strict margins |
| GCXK adjacent \(\eta\) | lower squared comparison | upper squared comparison |

The JSON stores no raw two-million-bit binomial.  It stores its bit length and
the derived floor/ceiling only; the verifier recomputes the full integer by both
routes.

## Source pins and proof authority

The verifier checks Git blob hashes for the exact source files used:

- `agents.md` — `30d8b9f1b4caa3c7504fe3d24fc7ce8da84de434`;
- `open-proximity.tex` — `f8ccfcc11bbfcd5f1a00595ef4d81325128ff58a`;
- `tex/cs25_cap_v13_2.tex` — `5ceff5dbc4b1ac4cef53eae7eada32046e4bafeb`;
- `RS_MCA_Paving_v9.2.tex` — `3381e130c691561974f645d4d832173784db2108`;
- four-row compiler JSON — `357cf4865a04f3db78eda39c983a2d1ef79451e1`;
- M31 list packet JSON — `ae8927f38e27c5de40a176c364135d3604cd2a86`;
- aperiodic prefix-collision note — `be91876079ba2b9a0332dedfa78f0fe36eccd0af`;
- #169 coset-collapse note — `7c7586d1caf3cf561b2f602612128ce5e5f596ba`;
- fixed-remainder dyadic route cut — `e08705282f7f5a0f15d52d51b3bb97ce834041ff`.

The source commit is
`c49e45eed71af9c24e3599c2fca3b76e02692be9`.

## Nonclaims

- No unconditional upper bound for the row is proved.
- No received word with more than \(16777215\) listed codewords is constructed.
- No MCA bad-slope numerator is used as a list bound.
- No implication from the adjacent agreement-\(1116024\) MCA row is claimed.
- No KoalaBear closure or transfer is claimed.
- No external GCXK theorem is claimed until the source-sign discrepancy is
  reconciled.

# OPEN GAP
