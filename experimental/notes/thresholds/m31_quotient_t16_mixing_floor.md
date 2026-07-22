---
workboard_item: M1
row: Mersenne-31 list at 2^-100
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: On the pinned c=2048, (u,v)=(0,1) quotient profile, one explicit 479-subset anchor has 1233 distinct same-depth-32-prefix neighbors at deficiency 192. Exactly 1225 certified neighbors are triple exchanges among seven full T_64 classes on each side, while eight further certified neighbors exchange twelve full T_16 fibers and are not full-T_64-class exchanges. Since floor(4 H_192/p^32)=0, every coefficient-four uniform shell intercept must satisfy b>=1233. The A1 full-T_64 classification is false; the coefficient-four route remains arithmetically viable for 1233<=b<=5191.
architecture: M31_C2048_U0_V1_QUOTIENT_T16_MIXING_FLOOR_V1
partition_digest: SUPPORT-LEVEL PINNED QUOTIENT PROFILE; no first-match ledger atom assigned
atom_or_cell: Q / PINNED_QUOTIENT_PREFIX_FIBER
quantifier: Existential depth-32 quotient target and anchor on the pinned eight-root (u,v)=(0,1) profile; all 1233 displayed/generated neighbors are exact support witnesses.
projection_and_unit: 479-subsets of the 1022-label punctured quotient domain, depth-32 monic quotient-locator prefixes, and rooted deficiency-192 neighbor count. No codeword, explanation, ray, or slope projection.
claimed_bound: d_192(A)>=1233; eight certified neighbors are outside the full-T_64 swap family; floor(4 H_192/p^32)=0; coefficient-four intercept floor b>=1233; compiler value 15007628 and reserve 1769587 at b=1233.
status: COUNTEREXAMPLE / COUNTEREXAMPLE_NEW_FLOOR / SUPPORT-LEVEL ONLY
impact: A1 CLASSIFICATION FALSE / UNIFORM-INTERCEPT FLOOR 1233 / COEFFICIENT-FOUR ROUTE STILL OPEN
falsifier: Any duplicate among the 1233 generated supports; any support leaving Q' or having size other than 479; deficiency other than 192; failure of one depth-32 prefix equality; one mixed exchange being a union of three full T_64 classes; 4 H_192>=p^32; or a compiler arithmetic mismatch.
replay: Stdlib verifier --check and --tamper-selftest; stdlib-only Lean package experimental/lean/m31_quotient_t16_mixing_floor/ through fork draft-PR CI. Python is replay only; Lean is the proof validator.
artifact_state: UNPINNED_LOCAL_DRAFT
intended_branch: gptpro/m31-quotient-t16-mixing-floor
parent_head: 5b8bbc2083583460dd3d9b23b8d8fca6701f7ae6
---

# M31 quotient `T_16` mixing floor

## Status

```text
artifact state                                = UNPINNED LOCAL DRAFT
intended branch                               = gptpro/m31-quotient-t16-mixing-floor
parent head                                   = 5b8bbc2083583460dd3d9b23b8d8fca6701f7ae6
COUNTEREXAMPLE_NEW_FLOOR
A1 full-T_64 classification                  = false
certified deficiency-192 class-swap neighbors = 1225
certified deficiency-192 mixed neighbors      = 8
certified rooted degree d_192(A)               >= 1233
uniform coefficient-four intercept             >= 1233
coefficient-four route                          still arithmetically viable
B1 non-class neighbor at e=64                  not proved
B2 degree at least 5192                        not proved
row ledger movement                            = 0
M31 LIST row closed                            = false
```

This is the round-3 successor to
`m31_quotient_prefix_flatness_t64_witness.md`.  That predecessor is read-only
precedent.  The present packet uses a new anchor, a new `T_16` mixing
mechanism, a new certificate, and a new Lean package.

The active proof labels are `def:primitive-q`, `def:q-row-atom`,
`prop:q-exact-target`, and `lem:newton-equivalence` in
`experimental/grande_finale.tex`.  The depth-32 quotient-jet reduction is
Corollary 3.2 of
`m31_c2048_fixed_template_interleaved_quotient_route_cut.md`.  The shell
compiler is theorem `(RS)` in `m31_q_rooted_shell_envelope.md`.

The result is deliberately local and support-level.  It falsifies the proposed
A1 classification and raises the pointwise intercept floor.  It does not prove
or disprove a uniform band cap with `1233 <= b <= 5191`, and it does not claim
that this quotient-prefix fiber survives any first-match deletion or projects
to codewords or slopes.

---

## 1. Pinned quotient domain

Put

\[
 p=2^{31}-1=2147483647.
\]

In \(\mathbb F_p[i]\), with \(i^2=-1\), use

\[
 g=(1717986917,1288490189),
 \qquad g^{2^{30}}=-1,
 \qquad g^{2^{31}}=1.
\]

For odd \(r\), \(1\le r\le2047\), define

\[
 q_r=2^{-2047}\operatorname{Re}(g^{r2^{19}})\pmod p,
 \qquad 2^{-2047}=1073741824\pmod p.
\tag{1.1}
\]

The 1,024 values are pairwise distinct.  The pinned eight-root profile removes
`q_1` and `q_3`, leaving

\[
 Q'=\{q_r:r\text{ odd},1\le r\le2047, r\notin\{1,3\}\},
 \qquad |Q'|=1022.
\tag{1.2}
\]

For a 479-subset \(E\subset Q'\), write

\[
 V_E(Y)=\prod_{q\in E}(Y-q),
 \qquad
 \operatorname{pref}_{32}(V_E)
  =(v_1,\ldots,v_{32}),
\tag{1.3}
\]

where \(v_j\) is the coefficient of \(Y^{479-j}\).

---

## 2. Nested full fibers

### 2.1 The sixteen `T_64` classes

For odd \(a\in\{1,3,\ldots,31\}\), put

\[
 \mathcal C_a
 =\{q_r:r\equiv a\text{ or }-a\pmod {64}\}.
\tag{2.1}
\]

Every \(\mathcal C_a\) has 64 elements.  With
\(\tau_a=T_{64}(2q_a)\),

\[
 P_a(Y):=\prod_{q\in\mathcal C_a}(Y-q)
 =2^{-127}\bigl(T_{64}(2Y)-\tau_a\bigr).
\tag{2.2}
\]

Thus all \(P_a\) are monic degree-64 polynomials with a common nonconstant
part.  Products of three such factors have the same leading term as a
polynomial in the common monic degree-64 core; the difference of any two
triple products has degree at most 128.

Only \(\mathcal C_1\) and \(\mathcal C_3\) are punctured in \(Q'\).  The other
fourteen classes are intact.

### 2.2 The sixty-four `T_16` classes

For odd \(a\in\{1,3,\ldots,127\}\), put

\[
 \mathcal D_a
 =\{q_r:r\equiv a\text{ or }-a\pmod {256}\}.
\tag{2.3}
\]

Every \(\mathcal D_a\) has 16 elements, and each intact \(\mathcal C_b\) is the
disjoint union of four such classes.  With
\(\rho_a=T_{16}(2q_a)\),

\[
 R_a(Y):=\prod_{q\in\mathcal D_a}(Y-q)
 =2^{-31}\bigl(T_{16}(2Y)-\rho_a\bigr).
\tag{2.4}
\]

Set \(H(Y)=2^{-31}T_{16}(2Y)\) and
\(\lambda_a=2^{-31}\rho_a\).  Then

\[
 R_a(Y)=H(Y)-\lambda_a.
\tag{2.5}
\]

For twelve indices \(X\),

\[
 \prod_{a\in X}R_a
 =H^{12}-e_1(\lambda_X)H^{11}
       +e_2(\lambda_X)H^{10}+\cdots.
\tag{2.6}
\]

Hence equal first and second power sums of the \(\rho_a\)'s imply equal
\(e_1,e_2\), and the difference of the two degree-192 exchange locators has
degree at most

\[
 9\cdot16=144.
\tag{2.7}
\]

This is the mixing mechanism absent from round 2.

---

## 3. The anchor

Partition the fourteen intact `T_64` classes as

```text
inside  I = {7, 9, 13, 19, 21, 23, 27},
outside O = {5, 11, 15, 17, 25, 29, 31}.
```

Let \(R\) be the first 31 representatives, in increasing order, of
\(\mathcal C_1\setminus\{q_1\}\):

```text
63, 65, 127, 129, 191, 193, 255, 257,
319, 321, 383, 385, 447, 449, 511, 513,
575, 577, 639, 641, 703, 705, 767, 769,
831, 833, 895, 897, 959, 961, 1023.
```

Define

\[
 A=R\sqcup\bigsqcup_{a\in I}\mathcal C_a.
\tag{3.1}
\]

Then

\[
 |A|=31+7\cdot64=479.
\tag{3.2}
\]

The exact depth-32 target is

```text
1034127669,   50736831,  297947808, 2001416587,
 582486197, 1119161472, 2092060217,  691570973,
 351942517, 1850514162,  230010785, 1719889839,
1235349562,  568398669, 1689825028,  515651434,
  18957312,  672550470, 1519314673,  322573603,
 116542290, 1792409170,  753121918,  223352466,
1193775763,  493795963,  257600683, 1893789609,
1766068826,  431705051, 1355303332,  141998040.
```

Call this vector \(\eta\).

---

## 4. The 1,225 full-class neighbors

Choose any three classes from \(I\), remove their 192 labels, and add any three
classes from \(O\).  The number of resulting supports is

\[
 \binom73\binom73=35^2=1225.
\tag{4.1}
\]

Every support has size 479 and deficiency 192 from \(A\).  The exchanged
triple locators differ in degree at most 128.  Their common support has degree

\[
 479-192=287,
\]

so the full locator difference has degree at most

\[
 287+128=415=479-64.
\tag{4.2}
\]

Therefore all 1,225 supports share the first 63 nonleading locator
coefficients with \(A\), in particular the target \(\eta\).

The verifier constructs all 1,225 supports twice: once from the closed form and
once from the full Cartesian product of the two triple-combination lists.  It
checks canonical support distinctness and every depth-32 prefix directly.

---

## 5. Eight `T_16`-mixed neighbors

The following table gives eight exchanges.  An entry lists twelve removed
`T_16` class indices \(X\subset I\) and twelve added indices
\(Y\subset O\).  Each class contributes 16 quotient labels, so every exchange
has deficiency 192.

| # | removed `T_16` indices | added `T_16` indices | common \(\sum\rho\) | common \(\sum\rho^2\) |
|---:|---|---|---:|---:|
| 1 | `7 9 27 37 55 71 73 77 83 109 115 119` | `5 11 17 25 39 47 53 69 79 93 99 113` | 752337374 | 6 |
| 2 | `7 21 27 37 43 71 77 83 85 107 109 115` | `5 11 17 25 39 47 53 69 79 93 99 113` | 752337374 | 6 |
| 3 | `7 23 27 37 41 71 77 83 87 105 109 115` | `5 11 17 25 39 47 53 69 79 93 99 113` | 752337374 | 6 |
| 4 | `9 37 41 51 55 83 85 101 105 107 109 115` | `5 25 31 33 47 69 75 89 93 99 111 117` | 1029303379 | 6 |
| 5 | `13 19 21 23 27 43 45 73 77 87 91 119` | `11 17 29 35 39 53 59 81 95 97 103 123` | 1118180268 | 6 |
| 6 | `9 13 19 45 51 55 57 73 91 101 119 121` | `15 29 35 49 59 75 81 89 103 111 117 123` | 1395146273 | 6 |
| 7 | `13 19 21 43 45 51 57 85 91 101 107 121` | `15 29 35 49 59 75 81 89 103 111 117 123` | 1395146273 | 6 |
| 8 | `13 19 23 41 45 51 57 87 91 101 105 121` | `15 29 35 49 59 75 81 89 103 111 117 123` | 1395146273 | 6 |

For every row, exact field arithmetic gives

\[
 \sum_{a\in X}\rho_a=\sum_{a\in Y}\rho_a,
 \qquad
 \sum_{a\in X}\rho_a^2=\sum_{a\in Y}\rho_a^2=6.
\tag{5.1}
\]

Equation (2.7) applies.  After multiplication by the degree-287 common-core
locator, each full locator difference has degree exactly 431.  Thus every mixed
neighbor shares exactly the first

\[
 479-431-1=47
\]

nonleading coefficients with \(A\), and differs at coefficient 48.  In
particular all eight lie in \(F_\eta\).

No removed twelve-class set in the table is a union of three complete
`T_64` classes, and the direct occupancy check shows none of the eight
supports belongs to the 1,225-member class-swap family.  The eight supports
are pairwise distinct.

This proves that A1 classification is false: same-prefix band pairs need not
arise from full-`T_64` exchanges.

### 5.1 Independent `T_32` pair

The independent six-fiber `T_32` exchange used in the rung audit is

```text
removed T_32 indices = 5, 21, 27, 29, 31, 39
added T_32 indices   = 13, 19, 33, 37, 43, 63
common sum rho       = 1122577494
```

Neither side is a union of complete `T_64` classes.  With the certificate's
287-label common core, the resulting 479-subsets have deficiency 192, share
the first 63 nonleading locator coefficients, and differ at coefficient 64.
This pair is a secondary A1 falsifier and is not included in the rooted degree
`1233` for the anchor in Section 3.

---

## 6. New rooted-shell floor

Combining Sections 4 and 5 gives

\[
 \boxed{d_{192}(A)\ge1225+8=1233.}
\tag{6.1}
\]

The exact shell size is

\[
 H_{192}=\binom{479}{192}\binom{543}{192}.
\tag{6.2}
\]

Two independent integer routes in the verifier and the Lean package certify

\[
 4H_{192}<p^{32},
 \qquad
 \left\lfloor\frac{4H_{192}}{p^{32}}\right\rfloor=0.
\tag{6.3}
\]

Therefore any coefficient-four pointwise condition

\[
 p^{32}\max(d_e(A)-b,0)\le4H_e
\tag{6.4}
\]

fails at \(e=192\) for every \(b\le1232\).  Any uniform intercept on the band
must satisfy

\[
 \boxed{b\ge1233.}
\tag{6.5}
\]

The new floor does not kill coefficient four.  At \(b=1233\),

```text
1233 * 447                              =   551151
1 + 1233*447 + floor(4M/p^32)           = 15007628
16777215 - 15007628                     =  1769587
```

while the previously certified upper edge remains

```text
b=5191: 1 + 5191*447 + 14456476 = 16776854 <= 16777215,
b=5192: 1 + 5192*447 + 14456476 = 16777301 >  16777215.
```

Hence the surviving arithmetic window is exactly

\[
 \boxed{1233\le b\le5191.}
\tag{6.6}
\]

No cap in this window is proved here.

---

## 7. Rung-ladder audit

Every requested rung was attacked from at least two distinct angles before the
packet was written.  Only the certified falsifier and floor above are banked.

| Rung | First angle | Second angle | Outcome |
|---|---|---|---|
| A1 classification | Full-`T_64` product analysis and exact triple-swap census. | Nested `T_16` symmetric-function search, followed independently by a `T_32` six-fiber equal-sum search. | **Falsified.** The eight displayed `T_16` exchanges are decisive; a separate `T_32` non-class identity confirms the mechanism is not an indexing accident. |
| A2 uniform `b<=5191` | Product-Johnson sphere packing from Newton distance 33. | Degree pruning by fixing `e-32` roots and solving the remaining monic degree-32 factor. | Both bounds are many orders of magnitude above 5191. No uniform cap follows. |
| A3 prefix through at least 128 | Exact nested-fiber scans through the double-swap shell. | Newton isolation of small corrections to a full-class exchange. | Strong local evidence and a local isolation lemma, but no all-anchor theorem. |
| A4 off-lattice rigidity | Symmetric augmentation/truncation of a class swap by at most 32 points. | Direct full-`T_16` scans at off-lattice multiples on the certified anchor. | The local perturbation route is impossible and the scanned subclass is empty off lattice; arbitrary off-lattice exchanges remain open. |
| B1 non-class `e=64` | Exact `T_16` four-fiber and `T_32` two-fiber collision classification. | Small-transposition/corrected-tail attack, plus a finer paired-`T_8` signed-moment search. | No seventh non-class `e=64` neighbor was found. Any correction of a class swap must move more than 32 additional points. |
| B2 degree at least 5192 | Maximize pure full-class production over fourteen intact classes. | Introduce `T_16` mixing and exhaust balanced seven-block splits at the relevant moment key. | Pure production reaches 1225; certified mixing reaches 1233, still below 5192. |

### Local Newton isolation lemma

Let \((X_0,Y_0)\) be a same-prefix full-class exchange.  Suppose another
same-prefix exchange is obtained by adding or deleting at most 32 points on
each side, with both sides still separated by the anchor partition.  Subtract
the two moment identities.  After cancellation one obtains two disjoint,
equal-cardinality sets of at most 32 points with the same first 32 power sums.
`lem:newton-equivalence` forces the two sets to coincide; anchor-side separation
then forces them to be empty.  Thus no nontrivial correction of this size
exists.

This lemma blocks the suggested small-transposition-with-corrected-tail attack,
but it is not a global `e=64` classification.

---

## 8. Mandatory adversarial epilogue

The strongest self-attack was that the eight apparent mixed supports might be
full-class swaps in a finer notation, or that equal `T_16` power sums might fail
to imply the claimed locator-prefix equality after the monic normalization and
common-core multiplication.

The attack fails for four independent reasons.

1. **Occupancy:** every mixed removed set cuts several `T_64` classes, so none is
a union of three complete classes.
2. **Full polynomial replay:** direct multiplication of the 479 linear factors
shows all eight locators agree with the anchor through coefficient 47 and
break at coefficient 48.  This does not rely on the compressed moment proof.
3. **Duplicate audit:** the 1,225 class supports and eight mixed supports are
canonicalized on the 1,022 ordered representatives; all 1,233 are distinct.
4. **Puncture audit:** every support avoids representatives 1 and 3, has exactly
479 labels, and has rooted deficiency exactly 192.

A separate adversarial pass recomputed the shell integer by both library
binomials and multiplicative recurrences, and recomputed the compiler charge by
multiplication and repeated addition.  No asserted integer depends on a single
route.

---

## 9. Exact remaining theorem

The band theorem remains:

\[
 d_e(A)\le b
 \quad\text{for every target, every anchor, and }33\le e\le213,
\tag{9.1}
\]

for one explicit

\[
 1233\le b\le5191.
\tag{9.2}
\]

For the post-crossover shells, the exact coefficient-four requirement is

\[
 d_e(A)\le b+
 \left\lfloor\frac{4H_e}{p^{32}}\right\rfloor,
 \qquad 214\le e\le479.
\tag{9.3}
\]

Nothing in this packet proves (9.1) or (9.3).  B1 remains open at deficiency
64, and B2 remains open at threshold 5,192.

---

## 10. Validation boundary and replay

This rescue packet is an **unpinned local draft** intended for branch
`gptpro/m31-quotient-t16-mixing-floor` from parent
`5b8bbc2083583460dd3d9b23b8d8fca6701f7ae6`.  No Lean build has been run for
this archive.  The intended authoritative formal validator is the stdlib-only
package

```text
experimental/lean/m31_quotient_t16_mixing_floor/
```

through the fork draft-PR Lean action.  Its witness module is designed to check
the field/domain construction, anchor and support generators, the
1,225-plus-eight census, prefix equalities, non-class separation, shell
inequality, and compiler arithmetic.  The Python verifier is local replay and
certificate integrity only.

```text
python3 experimental/scripts/verify_m31_quotient_t16_mixing_floor.py --check
python3 -O experimental/scripts/verify_m31_quotient_t16_mixing_floor.py --check
python3 experimental/scripts/verify_m31_quotient_t16_mixing_floor.py --tamper-selftest
```

The certificate is

```text
experimental/data/certificates/m31-quotient-t16-mixing-floor/
  m31_quotient_t16_mixing_floor.json
```

It records the intended parent head, all construction parameters, the complete
parametric support listing, direct support digests, integer gates, and SHA-256
hashes of every included proof artifact.  Repository predecessor/source blob
pins are deliberately absent in this local rescue handoff and must be applied
at pickup.  Any edit requires regeneration of every artifact hash and a
complete replay.

# COUNTEREXAMPLE_NEW_FLOOR
