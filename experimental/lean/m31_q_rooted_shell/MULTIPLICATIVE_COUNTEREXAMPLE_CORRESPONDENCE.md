# Multiplicative `3+7` counterexample: source/Lean correspondence

## Authority and status

The source-facing research note is
`experimental/notes/thresholds/m31_q_three_plus_seven_multiplicative_counterexample.md`.
The formal declarations are in
`M31QRootedShell/MultiplicativeCounterexample.lean`.

Status:

```text
COUNTEREXAMPLE_TO_SUPPORT_ONLY_3PLUS7
```

This is not a counterexample to the deployed Mersenne-31 exact residual.  The
formal packet contains no received line, explanation state, ray, or certified
slope-level C1--C8 owner.

## Parameter and object map

| Research-note object | Lean declaration | Audit |
|---|---|---|
| prefix field `F_241` | `p = 241`, arithmetic reduced modulo `p` | Exact for the frozen finite packet; no abstract finite-field API is claimed. |
| order-twenty subgroup `<235>` | `generator`, `domain`, `powMod` | `domain_is_order_twenty_control` checks the power table, exact order, and distinctness. |
| support universe: ten-subsets of twenty indices | `Support`, `rawCatalog` | `raw_catalog_support_shapes` checks cardinality, duplicate freedom, index range, and catalogue duplicate freedom. |
| depth-two elementary prefix `(92,135)` | `prefix1`, `prefix2` | `raw_catalog_has_common_prefix` checks all seventeen displayed supports. Completeness of this target fibre in `choose(20,10)` is auxiliary replay, not a Lean claim. |
| multiplicative scaling and scale-inversion support action | `rotateSupport`, `reflectSupport` | Exact index action on the cyclic subgroup. |
| support-level C1/C2 proxy deletion | `dihedralGeneric`, `residual`, `deleted` | `residual_is_exact_dihedral_filter` and `deleted_is_exact_dihedral_filter` prove the displayed split; `residual_supports_are_dihedral_generic` proves every retained support has trivial stabilizer. |
| literal planted-core proxy | `residualCommonCore`, `starCommonCore` | Both are proved empty. This is not a row-dependent C3 resultant or common-GCD owner theorem. |
| anchor and exchange shell | `anchor`, `exchangeDistance`, `neighborsAt`, `rootedDegree` | `anchor_distance_histogram` proves the exact `1,10,3` distribution on shells `5,6,7`; `anchor_neighbors_not_dihedrally_related` rejects orbit coincidence. |
| `Q = 241^2` | `q` | `q_eq` proves `58,081`. |
| `H_6 = C(10,6)^2` | stdlib-recursive `choose`, `ambientShell6` | `ambientShell6_eq` proves `44,100`; no Mathlib dependency is introduced. |
| failure of support-only `(3+7)` | `three_plus_seven_fails` | Exact inequality `7 H_6 < Q(d_6-3)`. |
| failure of `(4+7)` and survival of `(5+7)` | `four_plus_seven_fails`, `five_plus_seven_holds` | Exact neighboring calibration. |
| exact margin and coefficient | `three_plus_seven_margin`, `least_integer_coefficient_at_b3` | Margin `97,867`; least integer coefficient at intercept three is `10`. |
| direct failure of the existing compiler premise | `counterexampleRows`, `localEnvelope_three_seven_fails` | Instantiates and negates `M31QRootedShell.LocalEnvelope q 3 7` on the explicit row. |

## Validation boundary

GitHub Actions must build the package root
`M31QRootedShell.lean`, which imports the multiplicative counterexample module.
A green build certifies compilation of every declaration above.  It does not
certify the auxiliary Python enumeration or the mathematical nonclaims.

The auxiliary verifier and JSON certificate establish by independent exact
replay that:

- the displayed seventeen supports are the complete target fibre;
- the displayed fifteen supports are the complete support-level residual under
  the stated dihedral and planted-core filters;
- the full `choose(20,10)` census has exactly twenty violations forming one
  multiplicative orbit; and
- twelve hostile certificate mutations are rejected.

Python remains replay and certificate generation only; it is not proof
validation.

## Required successor theorem

Any result consuming this packet must preserve the typed distinction between
support structure and semantic ownership.  The next acceptable statement has
the form

```text
p^w max(d_e(A)-3,0) <= 7 H_e
or
an excess neighbor carries a certified earlier paid slope owner.
```

The owner branch must include received-line and explanation descent, the
first-match projector, projection type, natural profile scale, and exact slope
budget.  A support stabilizer or empty common core alone cannot discharge that
branch.
