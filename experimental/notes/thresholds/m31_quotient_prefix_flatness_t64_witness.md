---
workboard_item: M1
row: Mersenne-31 list at 2^-100
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: On the pinned c=2048, (u,v)=(0,1) fixed-template quotient family there is an explicit target eta and anchor A with six deficiency-64 same-prefix neighbors. Since floor(4 H_64/p^32)=0, this gives p^32(d_64(A)-3)_+>4H_64 and refutes (Q-3+4).
architecture: DIRECT_PINNED_C2048_U0_V1_QUOTIENT_PROFILE
partition_digest: N/A; fixed local profile, no row atom banked
atom_or_cell: Q / fixed-template quotient-prefix family
quantifier: Existential target eta and anchor A in the pinned punctured quotient domain, with six explicitly listed same-prefix neighbors.
projection_and_unit: 479-subsets per first-32 quotient-locator coefficient target; no codeword, ray, or slope projection.
claimed_bound: d_64(A)>=6 and floor(4 H_64/p^32)=0; hence the coefficient-four rooted-shell hypothesis with intercepts 3, 4, or 5 fails.
status: COUNTEREXAMPLE
impact: COUNTEREXAMPLE_NEW_FLOOR / ROUTE_CUT
falsifier: Any duplicate quotient label, wrong puncture, support outside Q', support size not 479, deficiency not 64, mismatch among the first 32 coefficients, or failure of 4H_64<p^32.
replay: Fork Lean CI for experimental/lean/m31_quotient_prefix_flatness; auxiliary Python normal/optimized replay and mutation test.
---

# M31 quotient prefix-flatness: an explicit `T_64` block-swap violation

## Status

```text
SIDE (B) REACHED — FULL WITNESS RESULT

target                          = explicit eta in F_p^32
anchor                          = explicit 479-subset A of Q'
deficiency                      = e=64
certified same-prefix neighbors = 6
floor(4 H_64 / p^32)            = 0
required witness threshold      = 4
conclusion                      = (Q-3+4) is false as posed
row ledger movement             = 0
```

This packet **falsifies** the proposed pointwise shell input on the exact pinned
eight-root `(u,v)=(0,1)` profile. It does not extrapolate to another profile.
The obstruction is not statistical: fourteen intact `T_64` fibers remain in
the punctured quotient domain, and complete-block swaps preserve the first
sixty-three nonleading quotient-locator coefficients.

The active proof labels are `def:primitive-q`, `def:q-row-atom`,
`prop:q-exact-target`, and `lem:newton-equivalence` in
`experimental/grande_finale.tex`; the depth-32 quotient-jet bridge is
Corollary 3.2 of
`m31_c2048_fixed_template_interleaved_quotient_route_cut.md`; and the
rooted-shell compiler is the theorem `(RS)` in
`m31_q_rooted_shell_envelope.md`.

## 1. Exact pinned quotient domain

Put
\[
 p=2^{31}-1=2147483647.
\]
In \(\mathbb F_p[i]\), \(i^2=-1\), use the norm-one generator
\[
 g=(1717986917,1288490189),
 \qquad g^{2^{30}}=-1,\qquad g^{2^{31}}=1.
\]
For odd \(r\), \(1\le r\le2047\), define
\[
 q_r=2^{-2047}\operatorname{Re}\!\left(g^{r2^{19}}\right)
      \pmod p,
 \qquad 2^{-2047}\equiv1073741824\pmod p.
\tag{1.1}
\]
The 1,024 values \(q_r\) are pairwise distinct and form the complete
quotient-label set \(Q\) of the monic deployed `T_2048` fold.

The pinned active eight roots are
```text
434373082,  614288294, 1713110565, 1533195353,
1984437538, 380812851,  163046109, 1766670796.
```
The first four have monic fold label
\[
 q_1=778433895,
\]
and the last four have label
\[
 q_3=173262001.
\]
The pinned active four-subset is indices `{0,1,4,5}`, with two selected
points in each of those partial fibers. Therefore the moving complete-fiber
labels range over exactly
\[
 Q'=Q\setminus\{q_1,q_3\},\qquad |Q'|=1022.
\tag{1.2}
\]

The certificate freezes the exact parameterization, the two punctures, a
SHA-256 digest of all 1,024 ordered labels, and exact support digests:
`experimental/data/certificates/m31-quotient-prefix-flatness-t64-witness/m31_quotient_prefix_flatness_t64_witness.json`.

## 2. Sixteen quotient `T_64` fibers

For odd \(a\in\{1,3,\ldots,31\}\), put
\[
 \mathcal C_a
   =\{q_r:r\equiv a\ \text{or}\ -a\pmod{64}\}.
\tag{2.1}
\]
Every \(\mathcal C_a\) has exactly 64 elements. If
\[
 \tau_a=T_{64}(2q_a),
\]
then
\[
 P_a(Y):=\prod_{q\in\mathcal C_a}(Y-q)
   =2^{-127}\bigl(T_{64}(2Y)-\tau_a\bigr).
\tag{2.2}
\]
Thus every \(P_a\) is monic of degree 64, and for all \(a,b\)
\[
 P_a-P_b=2^{-127}(\tau_b-\tau_a)
\tag{2.3}
\]
is constant. The exact fiber values are:

| class `a` | `tau_a` | status in `Q'` |
|---:|---:|:---|
| `1` | `26164677` | punctured |
| `3` | `1580223790` | punctured |
| `5` | `280947147` | intact |
| `7` | `456695729` | intact |
| `9` | `579625837` | intact |
| `11` | `1013961365` | intact |
| `13` | `194696271` | intact |
| `15` | `505542828` | intact |
| `17` | `1641940819` | intact |
| `19` | `1952787376` | intact |
| `21` | `1133522282` | intact |
| `23` | `1567857810` | intact |
| `25` | `1690787918` | intact |
| `27` | `1866536500` | intact |
| `29` | `567259857` | intact |
| `31` | `2121318970` | intact |

Only classes 1 and 3 are punctured. In particular the fourteen classes
`5,7,...,31` remain intact.

## 3. Explicit anchor and six neighbors

The exact 31-point partial piece of \(\mathcal C_{27}\) is
```text
R27 = [
  27, 37, 91, 101, 155, 165, 219, 229,
  283, 293, 347, 357, 411, 421, 475, 485,
  539, 549, 603, 613, 667, 677, 731, 741,
  795, 805, 859, 869, 923, 933, 987
].
```
Here an integer `r` denotes the quotient label \(q_r\) from (1.1). Define
\[
 \mathcal C
 =\mathcal C_{15}\sqcup\mathcal C_{17}\sqcup
  \mathcal C_{19}\sqcup\mathcal C_{21}\sqcup
  \mathcal C_{23}\sqcup\mathcal C_{25}
  \sqcup\{q_r:r\in R27\}.
\tag{3.1}
\]
Then \(|\mathcal C|=6\cdot64+31=415\), and \(\mathcal C\subset Q'\).

The seven complete supports are
\[
\begin{array}{c|c}
\text{name}&\text{support}\\ \hline
A   &\mathcal C\sqcup\mathcal C_5\\
B_1 &\mathcal C\sqcup\mathcal C_7\\
B_2 &\mathcal C\sqcup\mathcal C_9\\
B_3 &\mathcal C\sqcup\mathcal C_{11}\\
B_4 &\mathcal C\sqcup\mathcal C_{13}\\
B_5 &\mathcal C\sqcup\mathcal C_{29}\\
B_6 &\mathcal C\sqcup\mathcal C_{31}.
\end{array}
\tag{3.2}
\]
This is an exact support listing: each full block is the congruence class
(2.1), and the only partial block is the printed list `R27`. The JSON
certificate records SHA-256 digests of each support's ordered odd
representatives and canonical field residues. The exact supports themselves
are already listed by (2.1), the printed `R27`, and (3.2); the Lean module
recomputes every representative and residue directly.

All seven supports lie in \(\binom{Q'}{479}\). For every \(1\le i\le6\),
\[
 A\cap B_i=\mathcal C,\qquad |A\setminus B_i|=64.
\tag{3.3}
\]

## 4. Exact common target

For \(E\in\binom{Q'}{479}\), write
\[
 V_E(Y)=\prod_{q\in E}(Y-q)
       =Y^{479}+\eta_1Y^{478}+\cdots+\eta_{32}Y^{447}+\cdots.
\tag{4.1}
\]
The target, in the order \((\eta_1,\ldots,\eta_{32})\), is
```text
[
  2144970186, 693846040, 254084710, 1501952290,
  1904231690, 558873387, 1400618348, 1749425225,
  2110682204, 1763030673, 102589073, 1770388691,
  971529856, 948975681, 774218929, 1490251835,
  2095038705, 838625156, 774891784, 644995098,
  888552471, 1685238706, 1330006363, 1053276022,
  1544945819, 100722017, 1420529349, 1803184017,
  1196844108, 324775767, 591689729, 1982980281
]
```

For a neighbor using moving class \(a\),
\[
 V_A-V_{B_i}
   =V_{\mathcal C}(P_5-P_a).
\tag{4.2}
\]
By (2.3), the right side has degree at most \(415\). Therefore the
coefficients of degrees \(478,477,\ldots,416\)—the first 63 nonleading
locator coefficients—are identical. In particular
\[
 \operatorname{pref}_{32}(V_A)
 =\operatorname{pref}_{32}(V_{B_i})
 =\eta
 \qquad(1\le i\le6).
\tag{4.3}
\]
Hence \(A,B_1,\ldots,B_6\in\mathcal F_\eta\) and
\[
 d_{64}(A)\ge6.
\tag{4.4}
\]

The Lean module also computes the seven locators directly and checks the
printed 32-tuple, rather than taking (4.2) as an unchecked correspondence
claim.

## 5. Exact violation of `(Q-3+4)`

At \(e=64\),
\[
 H_{64}=\binom{479}{64}\binom{543}{64}
\]
is exactly
```text
586374616784432967317447344396311850952251481404090129066339701269086144611744331859382537679275957595113162682732279972248681107329260801825759429939073953027297000
```
and
```text
4 H_64 =
2345498467137731869269789377585247403809005925616360516265358805076344578446977327437530150717103830380452650730929119888994724429317043207303037719756295812109188000
```
whereas
```text
p^32 =
41855804344513474996659235398101492226513356497450298740932889847998693318143069882098996132602011303952349637025722282585533160693229396196872386718816372844518146497415885223313922264348563527038409009746582412510577609691239404142296725925022012935690228019787759005225367255740944911962461962241
```
Thus
\[
 4H_{64}<p^{32},
 \qquad \left\lfloor\frac{4H_{64}}{p^{32}}\right\rfloor=0.
\tag{5.1}
\]
The Side-(B) threshold is therefore \(4\), while (4.4) gives six witnesses.
More directly,
\[
 p^{32}(d_{64}(A)-3)_+
 \ge 3p^{32}>4H_{64}.
\tag{5.2}
\]
This is a certified violation of `(Q-3+4)` within the stated sub-crossover
band \(33\le64\le213\).

## 6. Recalibrated coefficient window

Because \(4H_{64}<p^{32}\) and \(d_{64}(A)\ge6\), the same witness
refutes coefficient four with additive intercept \(b=3,4,\) or \(5\).
Any unchanged coefficient-four route must therefore do at least one of:

1. delete these intact `T_64` swaps by a proved earlier owner on this exact
   pinned profile;
2. raise the additive intercept to at least six; or
3. replace the pointwise shell hypothesis.

The arithmetic compiler would still fit **conditionally** at `(b,c)=(6,4)`:
\[
 1+6\cdot447+14,456,476
 =14,459,159
 \le16,777,215,
\tag{6.1}
\]
leaving `2,318,056`. This is not a proof of `(6+4)`: the actual value of
\(d_{64}(A)\) may exceed the six listed neighbors, and all other anchors and
shells remain unproved.

## 7. Validation boundary

The stdlib-only Lean package
`experimental/lean/m31_quotient_prefix_flatness/` kernel-checks:

- the norm-one generator identities;
- all 1,024 quotient labels, duplicate-freeness, and the two pinned punctures;
- the sixteen 64-point quotient fibers and their exact `T_64` values;
- the common core and all seven 479-element supports;
- membership in `Q'`, duplicate-freeness, and deficiency 64;
- equality of all seven printed depth-32 locator prefixes;
- six distinct neighbors;
- the exact fast-binomial value of \(H_{64}\);
- \(4H_{64}<p^{32}\) and the strict rooted-shell violation.

The Python verifier independently regenerates the canonical JSON, checks
source Git-blob pins, replays normal and optimized modes, and rejects a
mutated target. Python is replay only; green fork Lean CI is the proof
validation gate.

## 8. Explicit nonclaims

- No row-global `U_Q` integer is banked.
- No received word or exact-boundary codeword family is constructed.
- No first-match survival after a possible `T_64` quotient owner is claimed.
- No codeword, ray, or slope projection is claimed.
- No rigidity extension is proved at any deficiency.
- No replacement `(6+4)` theorem is proved.
- No adjacent-row closure, safe agreement, stable-paper change, or score claim
  is made.

# COUNTEREXAMPLE_NEW_FLOOR
