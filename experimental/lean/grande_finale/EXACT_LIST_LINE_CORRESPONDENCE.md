# Exact List--Line Correspondence

Status: **PROVED** for the same-field, fixed-pole list--line bijection and
agreement-set preservation in `thm:exact-list-line-bijection`.

Source: `experimental/asymptotic_rs_mca_frontiers.tex`, especially
`thm:exact-list-line-bijection`.

## Statement map

| Frontiers argument | Lean declaration |
| --- | --- |
| Polynomial agreement support | `GrandeFinale.ExactListLine.polynomialAgreementSet` |
| Quotient explaining polynomial | `GrandeFinale.ExactListLine.explainingPolynomial` |
| Quotient factorization and degree bound | `GrandeFinale.ExactListLine.explainingPolynomial_spec`, `GrandeFinale.ExactListLine.explainingPolynomial_degree_lt` |
| Pointwise equivalence of line and polynomial agreement | `GrandeFinale.ExactListLine.explainingPolynomial_agrees_iff` |
| Exact agreement-set preservation | `GrandeFinale.ExactListLine.lineAgreementSet_eq_polynomialAgreementSet` |
| Finite MCA-bad slope set | `GrandeFinale.ExactListLine.badSlopeSet` |
| Complete list maps onto the bad-slope set | `GrandeFinale.ExactListLine.image_eval_eq_badSlopeSet` |
| Separating evaluation gives equal cardinalities | `GrandeFinale.ExactListLine.badSlopeSet_card_eq` |

## Statement comparison

For a field `F`, an injective evaluation map `ev : D -> F`, a received word
`U`, and a pole `alpha` outside the evaluation image, Lean defines

`h_P = (P - C (P.eval alpha)) / (X - C alpha)`

through the divisibility theorem for `X - C alpha`.  It proves that `h_P` has
degree less than `k` whenever `P` has degree at most `k`, and that agreement of
`h_P` with the pole line at slope `P.eval alpha` is pointwise equivalent to
agreement of `P` with `U`.

The finite list theorem takes a `Finset F[X]` together with both directions of
its completeness specification: every member has degree at most `k` and at
least `m` agreements, and every polynomial satisfying those conditions is a
member.  Its evaluation image is proved equal to the full finite MCA-bad slope
set.  If evaluation at the pole is injective on the list, cardinality of the
bad-slope set is exactly the list cardinality.

## Scope boundaries

This module proves the fixed-pole core over one ambient field.  In the source,
the received word and complete list may first be defined over a subfield and
then viewed in an extension.  The Vandermonde descent showing that an
ambient-field polynomial agreeing with the base-valued word has base-field
coefficients is not part of this module; completeness over the ambient field
is an explicit hypothesis instead.  Existence of a separating pole from the
finite-extension size bound in equation (4.6), and the direct specialization
to the locator prefix fiber in `cor:exact-prefix-ray-realization`, also remain
separate.

The assumption `k + 1 <= m` is used through the existing
`CollisionAwarePole.eval_slope_mcaBad` theorem to rule out simultaneous pair
explanation.  No stronger list-decoding or asymptotic claim is made.

## Verification

```text
lake env lean GrandeFinale/ExactListLine.lean
```

The module prints the axioms of its principal results. The audit reports only
Lean's standard `propext`, `Classical.choice`, and `Quot.sound`; no proof
placeholder or added axiom occurs.
