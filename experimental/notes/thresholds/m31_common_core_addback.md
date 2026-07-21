# M31 canonical common-core add-back: exact loss-one puncturing under the padded frame

```yaml
workboard_item: M1
row: Mersenne-31 list, auxiliary analytic stress row at 2^-100
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: For every marked rank-46 common-core branch satisfying the canonical padded-frame hypotheses, puncturing the common canonical locator core induces an exact bijection between the full radius-981129 RS list component and the shortened radius-(981129-|C|) component, with add-back multiplicity one and unchanged source-key/refund/signed-credit data.
architecture: GRANDE_FINALE_V3_EXACT_COMPLETION / M31_CANONICAL_RANK46_SOURCE_KEY_COMPILER
partition_digest: NOT_YET_ASSIGNED_TO_ACTIVE_GLOBAL_FIRST_MATCH_PARTITION
atom_or_cell: UNPAID_COMMON_CORE_ADD_BACK
quantifier: Every marked rank-46 source key, every old-anchor rank-three common-core branch, every received word, and every common canonical locator core satisfying the printed hypotheses.
projection_and_unit: Distinct RS codewords and distinct source-key ledger entries; exact cardinality, not supports, rays, or MCA slopes.
claimed_bound: core_degree <= 62295; shortened_length >= 2034857; shortened_radius >= 918834; add_back_factor = 1.
status: PROVED
impact: ARCHITECTURE_BRIDGE
falsifier: A core point in a selected first-a agreement set, core degree above 62295, retained domain shorter than K, or a duplicated source-key map invalidates the theorem application.
replay: python3 experimental/scripts/verify_m31_common_core_addback.py --check; python3 -O experimental/scripts/verify_m31_common_core_addback.py --check; python3 experimental/scripts/verify_m31_common_core_addback.py --tamper-selftest; fork draft-PR Lean 4.31.0 build.
```

## 1. Result and acceptance gate

This packet satisfies **acceptance criterion 3: kill a precisely named terminal**.
It discharges

```text
UNPAID_COMMON_CORE_ADD_BACK
```

on the common-core branch produced after the padded rank-three frame. The
result is an exact, factor-one shortening/add-back theorem. It is not a new
owner, charge, or row bound.

The deployed constants are

```text
p       = 2^31-1          = 2,147,483,647,
n       = 2^21            = 2,097,152,
K       = 2^20            = 1,048,576,
a       = 1,116,023,
w       = a-K             = 67,447,
R       = n-a             = 981,129,
B*      = 16,777,215.
```

Upstream #1025 supplies, pointwise on every marked rank-46 source key, a
canonical padded rank-three frame with

```text
lambda_1                  <= 20,765,
lambda_1+lambda_2         <= 41,530,
lambda_1+lambda_2+lambda_3<= 62,295 < 67,447.
```

On the noncoloop/common-core branch of the integrated source theorem, a
complementary canonical common core `C` divides one nonzero old-anchor
three-by-three minor. Hence

```text
c=|C| <= 62,295.                                             (1.1)
```

The theorem below proves that deleting this `C` and then adding it back costs
exactly one, not a factor depending on `c`, the number of columns, or the number
of source keys.

## 2. Canonical list notation

Let `F` be a field, let

```text
D=(x_1,...,x_n)
```

be an ordered list of distinct elements of `F`, and let `RS_F(D,K)` denote the
evaluations of polynomials of degree `<K`. Fix a received word `y` on `D`.
For a polynomial `f` of degree `<K`, write

```text
A_D(f)={x in D:y(x)=f(x)}
```

with the inherited order, and let `T_D(f)` be the first `a` entries of `A_D(f)`.
The canonical closed radius-`R=n-a` list is equivalently

```text
L_D(y,a)={f in F[X]_<K: |A_D(f)|>=a}.                         (2.1)
```

Its canonical boundary locator is

```text
W_f=Lambda_(D\T_D(f)).                                       (2.2)
```

A **canonical common locator core** for a component `L_0 subset L_D(y,a)` is a
set `C subset D` such that

```text
C subset Z(W_f)=D\T_D(f)       for every f in L_0.            (2.3)
```

Thus every core point is either an actual error or an agreement discarded after
the first `a` selections; no core point lies in a selected set `T_D(f)`.

Let

```text
D'=D\C,       y'=y|D',       n'=n-c,       R'=R-c.            (2.4)
```

The order on `D'` is inherited from `D`.

## 3. Selector stability

### Lemma 3.1 (first-`a` selector survives common-core puncturing)

If `C cap T_D(f)=emptyset`, then

```text
T_D'(f)=T_D(f).                                               (3.1)
```

**Proof.** Delete the elements of `C` from the ordered agreement list
`A_D(f)`. Every deleted error was absent already. Every deleted agreement is
outside the first `a` entries by the hypothesis. Filtering an ordered list
away from its first `a` entries does not change its first `a` entries. This is
exactly (3.1). `QED`

The Lean declarations `take_filter_eq_take_of_prefix_kept`,
`selected_deleteCore_eq`, `selector_preserved`, and
`selector_vector_preserved` kernel-check the finite ordered-list content.

## 4. Exact common-core shortening/add-back theorem

### Theorem 4.1 (canonical common-core loss-one add-back)

Assume:

1. `D` has `n` distinct points;
2. `C subset D` has size `c`;
3. `n-c>=K`;
4. for every `f in L_D(y,a)`, the canonical selected set satisfies
   `C cap T_D(f)=emptyset`.

Then, as sets of degree-`<K` polynomials,

```text
L_D(y,a)=L_D'(y',a).                                         (4.1)
```

Consequently restriction induces a bijection of distinct Reed--Solomon
codewords and

```text
|L_D(y,a)|=|L_D'(y',a)|.                                     (4.2)
```

The full-radius and shortened-radius forms are therefore

```text
|L_R^D(y)|=|L_(R-c)^(D')(y')|.                               (4.3)
```

**Proof.**

*Full to shortened.* Let `f in L_D(y,a)`. Its first `a` agreements are
`T_D(f)`. By hypothesis they avoid `C`, and Lemma 3.1 gives
`T_D'(f)=T_D(f)`. Hence `f` still has at least `a` agreements on `D'`, so it
lies in `L_D'(y',a)`.

*Shortened to full.* If `f` has at least `a` agreements on `D'`, the same
agreements occur on `D`. Thus `f in L_D(y,a)`. This direction needs no
common-core hypothesis.

This proves (4.1) on polynomial parameters. Since `n-c>=K`, two degree-`<K`
polynomials agreeing on all `n-c` retained distinct points are equal: their
difference has at least `K` roots but degree `<K`. Therefore the restriction
map is injective on codewords, and (4.2)--(4.3) follow. `QED`

The hypothesis `n-c>=K` is load-bearing only for interpreting polynomial
parameters as distinct shortened evaluation codewords. It is not an extension,
quotient, or field-transfer assumption.

## 5. Exact deployed specialization

From (1.1), every allowed core degree satisfies `0<=c<=62,295`. Therefore

```text
n' = 2,097,152-c >= 2,034,857,
R' =   981,129-c >=   918,834,
n'-K                >=   986,281,
a-K                 =     67,447,
(n'-K+1)-R'          =     67,448.                            (5.1)
```

In particular

```text
n' >= a > K,
```

so the same agreement threshold is feasible and the shortened RS evaluation
map is injective. The exact padding-frame margin is

```text
67,447-62,295=5,152.                                         (5.2)
```

The certificate verifier exhausts all `62,296` integer core degrees
`c=0,...,62,295` and checks every identity and gate in (5.1)--(5.2).

## 6. Source-key ledger and no double counting

The rank-46 compiler's marked key is

```text
(j, ordered 45-anchor tuple, distinguished extra codeword).  (6.1)
```

The common-core operation is pointwise:

```text
same marked key and metadata
  -> same key plus (core degree, shortened length, shortened radius). (6.2)
```

It does not select, split, merge, or duplicate a source key. The compiler
retains literally:

1. source-key ID and exact-weight layer;
2. received center and codewords;
3. ordered domain, anchors, and distinguished extra;
4. first-`a` selector vector;
5. actual-error/padding root-status masks;
6. semantic owner, if already supplied;
7. refund vector; and
8. signed occupancy-credit vector.

The Lean theorem `common_core_addback_exact` proves pointwise metadata equality;
`compileAll_length`, `source_key_ids_preserved`, and
`source_key_ids_nodup_preserved` prove that the source-key list is unchanged;
`signed_credit_sum_preserved` proves the signed aggregate is unchanged. The
integrated first-match theorem then gives

```text
firstMatchCount(singleton source-ID cells) <= number of keys, (6.3)
```

so hostile duplicate IDs can only reduce the charged count. There is no
common-core multiplicity in the add-back.

The exact source crossing remains

```text
16,517,335+259,881=16,777,216=B*+1,                           (6.4)
```

with allowance `259,880`; this packet does not discard or recompute the signed
credits.

## 7. What terminal is removed, and what remains

The old branch sequence was

```text
PROVED_MASKED_DIAGONAL_SATURATION
  -> UNPAID_COMMON_CORE_ADD_BACK
  -> UNPAID_RANK2_COLOOP.
```

Theorem 4.1 and the deployed specialization remove the middle terminal:

```text
PROVED_COMMON_CORE_LOSS_ONE_ADDBACK.                          (7.1)
```

This does **not** turn a shortened component into a paid owner. In the sharper
post-#1022 vocabulary, the still-open successor is

```text
UNPAID_CANONICAL_LOCATOR_NUMERATOR_ESCAPE_OWNER_REFUND.       (7.2)
```

That theorem must use the simultaneous locator--numerator data, one-point
escapes, or an exact typed semantic owner/refund. The present result says only
that once such a shortened-component payment is proved, restoring its common
canonical locator core costs factor one and cannot double count the source
ledger.

## 8. Explicit nonclaims

- No Mersenne-31 list upper bound or row closure is proved.
- No `U_Q` or exhaustive list-interior atom is supplied.
- No row-sharp Q, list-interior coverage, or adjacent-row closure is claimed.
- No first-match owner, locator--numerator escape theorem, refund value, or
  shortened-component upper payment is constructed.
- The rank-two/coloop branch is not used or discharged here.
- No common root is declared a semantic deletion merely because it divides a
  locator.
- No MCA slope/ray statement is inferred from a list-codeword theorem.
- No extension-field, quotient, or full-row partition bridge is asserted.
- No stable-paper theorem, deployed radius, official score, or prize claim
  changes.

## 9. Replay

```bash
python3 experimental/scripts/verify_m31_common_core_addback.py --check
python3 -O experimental/scripts/verify_m31_common_core_addback.py --check
python3 experimental/scripts/verify_m31_common_core_addback.py --tamper-selftest
python3 -O experimental/scripts/verify_m31_common_core_addback.py --tamper-selftest
```

Lean validation is only through the fork draft PR on Lean `v4.31.0`; no local
Lean build is part of this packet.
