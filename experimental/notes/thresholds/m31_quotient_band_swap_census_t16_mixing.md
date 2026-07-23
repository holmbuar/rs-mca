---
workboard_item: M1
row: Mersenne-31 list at 2^-100
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: "On the pinned c=2048, (u,v)=(0,1) fixed-template quotient profile, an exact 3432-support T64 family has rooted shell counts 49, 441, and 1225 at deficiencies 64, 128, and 192. Hence every coefficient-four uniform band intercept satisfies b>=1225. A separate exact T16 mixing pair at deficiency 96 shares 47 nonleading locator coefficients, refuting full-T64 classification and zero off-lattice rigidity."
architecture: DIRECT_PINNED_C2048_U0_V1_QUOTIENT_PROFILE
partition_digest: "N/A; fixed local support profile, no row atom banked"
atom_or_cell: Q / fixed-template quotient-prefix family
quantifier: "Existential targets and anchors in the pinned punctured 1022-label quotient domain; the claimed shell lower bounds are exact finite support witnesses."
projection_and_unit: "479-subsets per first-32 quotient-locator coefficient target; no received-word, codeword, ray, or slope projection."
claimed_bound: "d_64(A)>=49, d_128(A)>=441, d_192(A)>=1225 for one anchor; another anchor has d_96(A)>=1 with a non-T64 exchange. Therefore 1225<=b<=5191 is the remaining arithmetic window for any coefficient-four uniform band theorem."
status: COUNTEREXAMPLE_NEW_FLOOR / ROUTE_CUT / OPEN_GAP
impact: COUNTEREXAMPLE_NEW_FLOOR / A1_CLASSIFICATION_FALSE / A4_ZERO_RIGIDITY_FALSE
falsifier: "A duplicate or punctured quotient label, a support of size other than 479, an incorrect shell census, a mismatch in any certified prefix, failure of 4H_192<p^32, or failure of the independent T16 power-sum relation."
replay: "Stdlib-only Lean package experimental/lean/m31_quotient_band_mixing; auxiliary Python --check and --tamper-selftest."
---

# M31 quotient band: a 1225 shell floor and off-lattice `T_16` mixing

## Status

```text
NEW UNIFORM-INTERCEPT FLOOR       b >= 1225
ARITHMETICALLY VIABLE WINDOW      1225 <= b <= 5191
A1 full-T64 classification        FALSE
A4 zero off-lattice rigidity      FALSE
A2 full-band uniform cap          OPEN
A3 uniform prefix cap             OPEN
B1 non-full e=64 mixing           NOT REACHED
B2 d_e >= 5192 route kill         NOT REACHED
row ledger movement               0
```

This is the round-3 stop packet for the pinned Mersenne-31 LIST stress-row
quotient profile. It supplies two exact support-level witnesses:

1. a `3,432`-support family whose rooted shell at `e=192` has `1,225`
   certified neighbors from every chosen anchor in that family; and
2. a genuinely off-lattice `e=96` exchange built from twelve intact
   `T_16` quotient fibers.

The first witness raises the necessary coefficient-four uniform intercept from
the round-2 floor `6` to `1,225`. The second witness proves that the tempting
full-`T_64` classification and the zero form of off-lattice rigidity are false.
Neither witness proves a uniform upper bound, a seventh non-full neighbor at
`e=64`, or a `5,192`-neighbor route kill.

The active source labels are `def:primitive-q`, `def:q-row-atom`,
`prop:q-exact-target`, and `lem:newton-equivalence` in
`experimental/grande_finale.tex`. The depth-32 quotient-jet bridge is
Corollary 3.2 of
`m31_c2048_fixed_template_interleaved_quotient_route_cut.md`, and the shell
compiler is `(RS)` in `m31_q_rooted_shell_envelope.md`.

## 1. Pinned quotient domain

Put
\[
 p=2^{31}-1=2,147,483,647,\qquad Q=p^{32}.
\]
Use the round-2 quotient labels
\[
 q_r=2^{-2047}\operatorname{Re}(g^{r2^{19}})\pmod p
 \quad (r=1,3,\ldots,2047),
\]
with \(g=(1717986917,1288490189)\). The `1,024` labels are distinct. The
pinned profile removes \(q_1\) and \(q_3\), so
\[
 Q'=Q_{\rm labels}\setminus\{q_1,q_3\},\qquad |Q'|=1022.
\]

For odd \(a\in\{1,3,\ldots,31\}\), let
\[
 {\cal C}_a=\{q_r:r\equiv a\ \hbox{or}\ -a\pmod{64}\}.
\]
Each class has `64` points before puncturing. The classes `1` and `3` are
punctured once; the fourteen classes
\[
 {\cal I}=\{5,7,9,11,13,15,17,19,21,23,25,27,29,31\}
\]
are intact.

Let
\[
 F_{64}(Y)=2^{-127}T_{64}(2Y),\qquad
 \lambda_a=2^{-127}\tau_a.
\]
The monic locator of \({\cal C}_a\) is
\[
 P_a(Y)=F_{64}(Y)-\lambda_a.
\tag{1.1}
\]
Thus all intact block locators differ only in their constant coefficient.

## 2. The `3,432`-support family

Take the following exact `31`-point core from the punctured class
\({\cal C}_1\setminus\{q_1\}\):
```text
63, 65, 127, 129, 191, 193, 255, 257
319, 321, 383, 385, 447, 449, 511, 513
575, 577, 639, 641, 703, 705, 767, 769
831, 833, 895, 897, 959, 961, 1023
```

For every seven-subset \(S\in\binom{{\cal I}}{7}\), define
\[
 E_S=R\sqcup\bigsqcup_{a\in S}{\cal C}_a.
\tag{2.1}
\]
Every \(E_S\) is a `479`-subset of \(Q'\), and
\[
 |\{E_S:S\in\binom{{\cal I}}{7}\}|
 =\binom{14}{7}=3432.
\tag{2.2}
\]

### Proposition 2.1 — common depth-63 prefix

All `3,432` locators \(V_{E_S}\) have the same first `63` nonleading
coefficients.

**Proof.** Put
\[
 R_S(Z)=\prod_{a\in S}(Z-\lambda_a).
\]
For two seven-subsets \(S,T\), the monic degree-seven polynomials \(R_S,R_T\)
have difference of degree at most six. By (1.1),
\[
 V_{E_S}-V_{E_T}
 =V_R\bigl(R_S(F_{64})-R_T(F_{64})\bigr),
\]
so
\[
 \deg(V_{E_S}-V_{E_T})
 \le 31+6\cdot64=415.
\tag{2.3}
\]
Both locators have degree `479`; hence their coefficients of degrees
`478,477,...,416`, exactly the first `63` nonleading coefficients, agree.
In particular every member has one common depth-32 target. \(\square\)

The certificate records the canonical family digests

```text
family_sha256 = 58c024f478c956b7c8280c782d41244f6f9b4d8ddbcf0b3613d1279d694fee35
selection_sha256 = 42561e9d287e1f4cb72dffac67163739afb52f85193147db662371012410aab7
```

### Proposition 2.2 — exact class-swap shell census

Fix
\[
 S_0=\{5,7,9,11,13,15,17\},\qquad A=E_{S_0}.
\]
For \(t=1,2,3\), replacing \(t\) classes of \(S_0\) by \(t\) classes of
\({\cal I}\setminus S_0\) gives
\[
 \binom{7}{t}\binom{7}{t}
\]
distinct members at deficiency \(64t\). Therefore
\[
 d_{64}(A)\ge49,\qquad
 d_{128}(A)\ge441,\qquad
 d_{192}(A)\ge1225.
\tag{2.4}
\]
Inside the `3,432`-support family these three shell counts are exact. Direct
enumeration gives the full restricted shell polynomial
```text
e=64: 49, e=128: 441, e=192: 1225,
e=256: 1225, e=320: 441, e=384: 49, e=448: 1.
```

The count `1,225` is obtained independently as
\(\binom73^2=35^2\) and by enumerating all \(3,432\) seven-class selections.

### Round-2 six-neighbor list was not complete

The round-2 anchor contains seven full intact classes
```text
5, 15, 17, 19, 21, 23, 25
```
and leaves six full intact classes disjoint:
```text
7, 9, 11, 13, 29, 31.
```
Its complete **full-class-swap** census is therefore
\[
 \binom71\binom61=42,\qquad
 \binom72\binom62=315,\qquad
 \binom73\binom63=700
\tag{2.5}
\]
at deficiencies `64`, `128`, and `192`. Thus the six neighbors printed in
round 2 were certified examples, not the complete list even within the
full-class-swap subclass. The new punctured-class core in (2.1) leaves seven
intact classes on each side and raises the three counts to
`49`, `441`, and `1,225`.

## 3. Consequence for the coefficient-four band

At \(e=192\),
\[
 H_{192}=\binom{479}{192}\binom{543}{192}
\]
is exactly
```text
250306657071379809146712330966428990686412627706880861569476097211926513715638118988008071592368035074016933687250963576376001122774381719478502944898782144806538717279733256653844747778197374722693408393198745533043396789913740659616431432884514095828053347551969743776494179678510074205400
```
and
\[
 4H_{192}<p^{32},\qquad
 \left\lfloor\frac{4H_{192}}{p^{32}}\right\rfloor=0.
\tag{3.1}
\]
Consequently every uniform pointwise theorem
\[
 d_e(A)\le b+\left\lfloor\frac{4H_e}{p^{32}}\right\rfloor
 \quad(33\le e\le213)
\tag{3.2}
\]
must have
\[
 \boxed{b\ge1225}.
\tag{3.3}
\]

The coefficient-four rooted-shell arithmetic remains viable:
\[
 1+1225\cdot447+\left\lfloor\frac{4\binom{1022}{479}}{p^{32}}\right\rfloor
 =1+547575+14456476
 =15004052
 \le16777215,
\tag{3.4}
\]
with reserve `1,773,163`. Thus this packet narrows, but does not close or
kill, the arithmetic window:
\[
 \boxed{1225\le b\le5191}.
\tag{3.5}
\]

For \(e\ge214\), the still-unproved pointwise requirement is exactly
\[
 d_e(A)\le b+\left\lfloor\frac{4H_e}{p^{32}}\right\rfloor.
\tag{3.6}
\]
The ambient allowance first becomes \(b+1\) at \(e=214\). No claim about any
shell in `[214,479]` is made here.

## 4. An exact off-lattice `e=96` exchange

Let
\[
 F_{16}(Y)=2^{-31}T_{16}(2Y).
\]
For a raw fiber value \(\sigma=T_{16}(2q)\), its monic 16-point locator is
\[
 L_\sigma(Y)=F_{16}(Y)-2^{-31}\sigma.
\tag{4.1}
\]

The two sides below use twelve pairwise disjoint intact `T_16` fibers. A
representative `r` denotes the quotient label \(q_r\).

| side | minimum representative | raw `sigma` | all 16 representatives |
|:---:|---:|---:|:---|
| `X` | `29` | `583555490` | `29, 227, 285, 483, 541, 739, 797, 995, 1053, 1251, 1309, 1507, 1565, 1763, 1821, 2019` |
| `X` | `15` | `812986380` | `15, 241, 271, 497, 527, 753, 783, 1009, 1039, 1265, 1295, 1521, 1551, 1777, 1807, 2033` |
| `X` | `93` | `849605071` | `93, 163, 349, 419, 605, 675, 861, 931, 1117, 1187, 1373, 1443, 1629, 1699, 1885, 1955` |
| `X` | `21` | `1093071961` | `21, 235, 277, 491, 533, 747, 789, 1003, 1045, 1259, 1301, 1515, 1557, 1771, 1813, 2027` |
| `X` | `119` | `1362440376` | `119, 137, 375, 393, 631, 649, 887, 905, 1143, 1161, 1399, 1417, 1655, 1673, 1911, 1929` |
| `X` | `95` | `2022380190` | `95, 161, 351, 417, 607, 673, 863, 929, 1119, 1185, 1375, 1441, 1631, 1697, 1887, 1953` |
| `Y` | `33` | `125103457` | `33, 223, 289, 479, 545, 735, 801, 991, 1057, 1247, 1313, 1503, 1569, 1759, 1825, 2015` |
| `Y` | `71` | `197700101` | `71, 185, 327, 441, 583, 697, 839, 953, 1095, 1209, 1351, 1465, 1607, 1721, 1863, 1977` |
| `Y` | `9` | `785043271` | `9, 247, 265, 503, 521, 759, 777, 1015, 1033, 1271, 1289, 1527, 1545, 1783, 1801, 2039` |
| `Y` | `107` | `1054411686` | `107, 149, 363, 405, 619, 661, 875, 917, 1131, 1173, 1387, 1429, 1643, 1685, 1899, 1941` |
| `Y` | `7` | `1079800039` | `7, 249, 263, 505, 519, 761, 775, 1017, 1031, 1273, 1287, 1529, 1543, 1785, 1799, 2041` |
| `Y` | `113` | `1334497267` | `113, 143, 369, 399, 625, 655, 881, 911, 1137, 1167, 1393, 1423, 1649, 1679, 1905, 1935` |

The six raw values on each side satisfy, independently,
\[
 \sum_{\sigma\in X}\sigma
 =\sum_{\sigma\in Y}\sigma
 =281588527\pmod p,
\tag{4.2}
\]
\[
 \sum_{\sigma\in X}\sigma^2
 =\sum_{\sigma\in Y}\sigma^2
 =1888686693\pmod p,
\tag{4.3}
\]
and hence
\[
 e_2(X)=e_2(Y)=1950190555\pmod p.
\tag{4.4}
\]
The two monic degree-six block-label polynomials differ by the exact cubic
whose ascending coefficients are
```text
1030524974, 16043166, 1710076578, 1294116245.
```

Let \(X_q,Y_q\subset Q'\) be the unions of the six fibers on the two sides.
They are disjoint and have size `96`. Let \(C\) be the first `383` odd
representatives, in increasing order, from
\(Q'\setminus(X_q\cup Y_q)\). Define
\[
 A_{96}=C\sqcup X_q,\qquad B_{96}=C\sqcup Y_q.
\tag{4.5}
\]
Both are `479`-subsets, with deficiency `96`.

By (4.2)--(4.4), the two degree-six block-label polynomials have equal first
two nonleading coefficients, so their difference has degree at most three.
Using (4.1), the two 96-point exchange locators differ in degree at most
\(3\cdot16=48\). Multiplication by the `383`-point common core gives
\[
 \deg(V_{A_{96}}-V_{B_{96}})\le383+48=431.
\tag{4.6}
\]
Therefore the first `47` nonleading locator coefficients agree. Direct
locator multiplication gives common prefix digest
```text
prefix47_sha256 = e552d0b2c0617cb48cb2b19261959a9a3e1d361a53ec7126c20f2ac76af6b146
```
and confirms that the forty-eighth coefficient differs.

Since \(96\not\equiv0\pmod{64}\), this pair is not a full-`T_64` class
exchange. It proves:

```text
A1 full-class classification: false.
A4 statement d_e=0 off the 64-lattice: false.
```

It does **not** refute an off-lattice cap such as `d_e <= 1225`, and it does
not meet B1 because its deficiency is `96`, not `64`.

## 5. A proved obstruction to the simplest B1 perturbation

Let \(P,Q\) be distinct intact `T_64` block locators, so \(P-Q\) is a
nonzero constant. Suppose \(U\) is a `t`-subset of the roots of \(P\) and
\(V\) is a `t`-subset of the roots of \(Q\), with
\(33\le t\le63\). Write
\[
 P=P_UC,\qquad Q=P_VD,
\]
where \(C,D\) are monic of degree \(64-t\). If the first 32 coefficients of
\(P_U,P_V\) agreed, then \(R=P_U-P_V\) would have degree at most \(t-33\).
But
\[
 P-Q=P_U(C-D)+RD.
\tag{5.1}
\]
If \(C-D\ne0\), the first term has degree at least \(t\ge33\), while
\(\deg(RD)\le31\), so their sum cannot be constant. If \(C=D\), then the
nonzero constant \(P-Q=RD\) is impossible because \(\deg D\ge1\).
Therefore:

> No non-full same-prefix exchange of size `33` through `63` can be confined
> to two intact `T_64` classes.

In particular, any B1 witness must mix at least three `T_64` classes or use
the punctured classes in an essential way. This is a route cut, not a proof
that B1 is impossible.

## 6. Rung-by-rung stop ledger

Every requested rung was attacked from two distinct directions before this
stop verdict.

| rung | first attack | second attack | outcome |
|:---|:---|:---|:---|
| A1 | exact full-class swap census for every anchor in the seven-class family, with restricted maximum `1225` | explicit `T_16` composition witness and direct locator multiplication at `e=96` | **false** |
| A2 | fixed-anchor exchange equations as low-degree RS/Padé agreement lists | Chebyshev divisor-difference and block-hierarchy analysis | no all-anchor cap `<=5191` proved |
| A3 | exact `T_64/T_32/T_16` block scans through the double-swap range | perturbation and shortening analysis around the `e=96` relation | no all-anchor prefix cap proved |
| A4 | closed-form `T_16` power-sum relation | independent 479-root locator multiplication | zero-rigidity **false**; capped form open |
| B1 | proved two-class partial-swap impossibility | exhaustive auxiliary searches in the full-`T_16`, `T_8`, and `T_4` subdivisions and in the certified relation span | no non-full `e=64` witness found |
| B2 | exact `49/441/1225` class-swap mass production | auxiliary optimization over the `T_32/T_16` block relation systems | no shell degree `>=5192` found |

The auxiliary searches are direction evidence only. They do not classify
arbitrary point exchanges and are not promoted as upper theorems.

## 7. Mandatory adversarial epilogue

The strongest attack on Proposition 2.1 was that multiplying several
constant-shift block locators might leak their constants into the first 32
coefficients. It fails for a sharp degree reason: using one block constant
drops `64` degrees, so after multiplying the degree-31 core every
constant-dependent term has degree at most `415`. An independent truncated
product over all `3,432` class selections gives one common 63-prefix, and
direct full-locator multiplication agrees.

The strongest attack on the `e=96` witness was that equality of raw
`T_16(2q)` sums might not transfer through monic normalization. It fails
because (4.1) uses one common nonzero scale, and equality of the first two
elementary coefficients is scale-invariant. Direct multiplication of both
479-root locators independently gives exactly `47` common nonleading
coefficients. Replacing one quotient point destroys the depth-32 match.

The arithmetic was computed twice: binomials by `math.comb` and by an exact
multiplicative recurrence; shell counts by closed form and direct selection
enumeration; quotient labels by exponentiation and by the order-1024
recurrence. All routes agree.

## 8. Validation and nonclaims

The stdlib-only Lean package
`experimental/lean/m31_quotient_band_mixing/` certifies the finite quotient
domain, block structure, class-selection shell census, exact `H_192` floor,
coefficient-four arithmetic, the `T_16` relation, both 479-supports, their
deficiency, and their direct common locator prefix. The Python verifier
regenerates the canonical certificate and supports both `--check` and
`--tamper-selftest`; Python remains replay, not proof validation.

Explicit nonclaims:

- no uniform cap on all anchors or targets;
- no B1 non-full neighbor at `e=64`;
- no B2 degree `5,192` witness;
- no statement that `1,225` is the true optimal intercept;
- no received word, first-match survival, codeword, ray, or slope projection;
- no row-global `U_Q`, adjacent-row closure, endpoint movement, or paper claim;
- no extrapolation beyond the pinned `(u,v)=(0,1)` profile.

# COUNTEREXAMPLE_NEW_FLOOR
