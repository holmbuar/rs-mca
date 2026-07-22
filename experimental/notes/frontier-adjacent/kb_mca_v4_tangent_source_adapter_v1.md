---
workboard_item: K1
row: KoalaBear MCA at 2^-128
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: Every received line has a source-coordinate tangent first-match cell of at most 981104 distinct bad finite slopes; the following Q, balanced-core, and final residual cells are iterated exact set differences and exhaust all remaining bad slopes.
architecture: GRANDE_FINALE_V4_KB_MCA_TANGENT_SOURCE_ADAPTER_V1
partition_digest: 4fade91abc408264989babcff6f8f9bbd80bcec52545a5db15ac376bf17d88fc
atom_or_cell: U_paid=SOURCE_COORDINATE_TANGENT_IMAGE
quantifier: Uniform over every admissible received line over F_(p^6)
projection_and_unit: Distinct bad finite slopes per received line
claimed_bound: U_paid'=981104
status: PROVED
impact: BANKABLE_ATOM
falsifier: Failure of translation invariance, the 981104 support cap, or exact four-cell disjoint exhaustion.
replay: python3 experimental/scripts/verify_kb_mca_v4_tangent_source_adapter_v1.py --check; lake build in experimental/lean/kb_m1_source_bound_bridge
---

# KoalaBear v4 source-coordinate tangent owner re-proof

**GATE (B) RE-PROOF / PROVED BANKABLE ATOM / ROW OPEN.**

This packet does not transport the legacy M1 ledger. It re-proves one useful
local payment directly in a source-bound Grande Finale v4 first-match
partition:

\[
U_{\rm paid}'=981{,}104.
\]

The legacy value \(422{,}354{,}730{,}332\) is provenance only.

## Frozen contract

The companion manifest fixes

\[
p=2{,}130{,}706{,}433,\quad \F=\mathbf F_{p^6},\quad
n=2{,}097{,}152,\quad k=1{,}048{,}576,
\]
\[
a=1{,}116{,}048,\quad n-a=981{,}104,\quad
B^*=274{,}980{,}728{,}111{,}395{,}087.
\]

The unit is distinct bad finite slopes per received line. All four atoms use
architecture
`GRANDE_FINALE_V4_KB_MCA_TANGENT_SOURCE_ADAPTER_V1` and partition digest
`4fade91abc408264989babcff6f8f9bbd80bcec52545a5db15ac376bf17d88fc`.

## Source-bound translation

Use `thm:exact-sparsification` and challenge-restricted (SP3) in
`experimental/rs_mca_thresholds.tex`. For a column-far pair the tangent image
is empty. Otherwise fix public total orders and choose the first common
explaining triple \((c_0,c_1,S)\). Put \(e_i=r_i-c_i\) and
\(\Sigma=\operatorname{supp}(e_0)\cup\operatorname{supp}(e_1)\).

The source theorem gives

\[
|\Sigma|\le n-a=981{,}104
\]

and preserves the complete MCA-bad slope set pointwise under this one
pair-global translation. The pointwise equivalence is formalized by
`RsMcaThresholds.ExactSparsification.mcaBad_sub_mem_iff`. Unions over
alternative translations are forbidden.

Define

\[
\mathcal T(r)=
\left\{-e_0(x)/e_1(x):x\in\Sigma,\ e_1(x)\ne0\right\}.
\]

This is a set image, so \(|\mathcal T(r)|\le|\Sigma|\le981{,}104\).

## Active four-cell chronology

Let \(Z\) be the complete bad-slope set. Let \(Q\) and \(BC\) be the
source-bound active-v4 certificate sets. Define

\[
Z_{\rm paid}=Z\cap\mathcal T,\quad R_1=Z\setminus\mathcal T,
\]
\[
Z_Q=R_1\cap Q,\quad R_2=R_1\setminus Q,
\]
\[
Z_{\rm BC}=R_2\cap BC,\quad Z_{\rm new}=R_2\setminus BC.
\]

The owner order is

```text
SOURCE_COORDINATE_TANGENT_IMAGE
ACTIVE_V4_BOUNDARY_PREFIX_Q
ACTIVE_V4_BALANCED_CORE
UNPAID_V4_COMPLEMENT
```

The cells are pairwise disjoint and their union is exactly \(Z\). Therefore the
scope is uniform and exhaustive. The first cell satisfies

\[
|Z_{\rm paid}|\le981{,}104.
\]

No witness, support, pair, coordinate, or selector multiplicity is charged.

## Exact ledger

The only value banked here is

\[
U_{\rm paid}'=981{,}104.
\]

The exact numerical reserve is

\[
B^*-U_{\rm paid}'
=274{,}980{,}728{,}110{,}413{,}983.
\]

This is reserve, not an allocation. The active values \(U_Q\), \(U_{\rm BC}\),
and \(U_{\rm new}\) remain open.

## Proof and nonclaims

`KbM1SourceBoundBridge.lean` is stdlib-only and proves the image bound, exact
four-cell partition, pairwise disjointness, and deployed integer arithmetic.
The existing semantic translation theorem is source-bound in
`CORRESPONDENCE.md`; it is not replaced by an axiom. The Python replay is
structural only.

This packet does not import any other legacy owner, pay Q or balanced-core
residuals, bound the final complement, close the row, or move the endpoint.
It contains no `sorry`, `axiom`, `admit`, or Mathlib dependency.

Thus the open row ledger is exactly

\[
U_{\rm total}=981{,}104+U_Q+U_{\rm BC}+U_{\rm new}.
\]

# PROVED
