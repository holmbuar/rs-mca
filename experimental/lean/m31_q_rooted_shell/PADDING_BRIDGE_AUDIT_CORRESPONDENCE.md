# Padding-bridge audit: source/Lean correspondence

## Packet

- Research note:
  `experimental/notes/audits/m31_padding_bridge_audit.md`
- Lean module:
  `M31QRootedShell/PaddingBridgeAudit.lean`
- Target package:
  `experimental/lean/m31_q_rooted_shell`
- Lean version: `v4.31.0`
- Dependency policy: stdlib only
- Audit terminal: `COUNTEREXAMPLE_NEW_FLOOR`

The packet audits the Mersenne-31 list-row terminal
`UNPAID_PADDING_BRIDGE`.  It does not repeat the canonical whole-list injection,
the occupancy-sensitive rank-46 source theorem, or the actual-error Forney
bounds already proved in
`experimental/notes/thresholds/m31_canonical_popov_rank46_compiler.md`.

## Source boundary

The source note proves the general polynomial identity

```text
Syz((P_i Q_i)_i)
  ~= {A in Syz((P_i)_i) : Q_i divides A_i for every i},
```

with row-degree shift `d` when all `deg Q_i=d`.  It also proves the exact
split-squarefree pair formula

```text
mu_padded = mu_error + d - mixedCommonExcess.
```

The Lean module does not introduce a polynomial-ring or Forney-index library.
Instead it kernel-checks the complete finite Reed--Solomon counterpacket and the
integer consequences that falsify an unmasked bridge.  The source theorem and
the finite certificate are intentionally kept distinct.

## Declaration map

| Lean declaration | Source statement checked |
|---|---|
| `natural_order_valid` | `O_cross` is a duplicate-free ordered nine-point subset of `F_11`. |
| `common_padding_order_valid` | `O_common` is the same underlying nine-point subset with a different fixed order. |
| `cubic_values` | Evaluation table of `c_1=X(X-1)(X-2)` from coefficients `[0,2,8,1]`. |
| `received_values` | Exact received word used by the counterpacket. |
| `natural_zero_agreements`, `natural_cubic_agreements` | Exact agreement sets `A_0,A_1`. |
| `natural_zero_errors`, `natural_cubic_errors` | Exact actual error sets `E_0,E_1`. |
| `both_codewords_are_interior_listed` | Both codewords have six agreements at `a=5` and weight three below radius four. |
| `actual_error_frame_is_identical` | Reordering changes neither actual error locator. |
| `cross_zero_selected`, `cross_cubic_selected` | Canonical first-five selections in `O_cross`. |
| `cross_zero_padding`, `cross_cubic_padding` | Cross-error padding roots `{5}` and `{8}`. |
| `cross_zero_padded_roots`, `cross_cubic_padded_roots` | Canonical padded root sets in `O_cross`. |
| `cross_actual_common_empty`, `cross_padded_common_mixed` | Empty actual common core but mixed padded common roots `{5,8}`. |
| `cross_minimal_pair_transports` | Root-set form of coordinatewise divisibility for the minimal actual pair generator. |
| `cross_pair_indices` | Exact pair-index change `3 -> 2`. |
| `common_zero_selected`, `common_cubic_selected` | Canonical first-five selections in `O_common`. |
| `common_zero_padding`, `common_cubic_padding` | Both columns discard the common agreement `2`. |
| `common_zero_padded_roots`, `common_cubic_padded_roots` | Canonical padded root sets in `O_common`. |
| `common_actual_common_empty`, `common_padded_common_is_discarded_agreement` | Empty actual common core but padded gcd root `{2}`. |
| `common_minimal_pair_does_not_transport` | Minimal actual pair generator fails coordinatewise divisibility. |
| `common_pair_indices` | Actual pair index three and padded pair index three. |
| `same_actual_frame_different_padding_bridge` | Same actual-error frame, different transportability and padded index. |
| `actualCommon_implies_paddedCommon` | Typed inclusion of actual common-error roots into padded common roots. |
| `no_direct_degree_transport_of_lt` | Necessary degree floor `mu>=d` for direct diagonal transport. |
| `m31_first_blocked_padding_degree` | `j<=960363` gives padding degree at least `20766`. |
| `m31_three_blocked_padding_degree` | `j<=918833` gives padding degree at least `62296`. |
| `m31_first_row_direct_transport_blocked` | The certified first M31 actual-error row cannot directly transport in the first band. |
| `m31_first_three_direct_transport_blocked` | None of the first three certified rows can directly transport in the second band. |
| `arithmetic_extremizer_blocked_positions` | The current arithmetic extremizer has `197585` weight positions in the three-row blocked band. |

## Statement audit

The finite instance is an actual Reed--Solomon instance:

```text
F       = F_11,
D       = {0,...,8},
K       = 4,
a       = 5,
R       = 4,
c_0     = 0,
c_1     = X(X-1)(X-2),
wt(y-c_0)=wt(y-c_1)=3.
```

The module evaluates field operations as natural-number residues modulo `11`,
as in the existing stdlib-only toy certificates in this package.  Every listed
support, error support, canonical selection, and padding mask is computed from
the received word and codeword evaluations; no support list is accepted as an
untyped premise.

The M31 declarations formalize only necessary degree arithmetic.  Their source
premise is the exact diagonal map: a padded syzygy of degree `lambda` maps to an
actual-error syzygy of degree `lambda+(R-j)`.  They do not claim that the current
M31 source packets occur in any particular weight layer.

## Sorry and axiom census

```text
sorry              0
custom axioms       0
Mathlib imports     0
```

The module imports `Std`, uses decidable finite evaluation and `omega`, and
contains no opaque proof placeholder.  Green CI proves compilation of these
finite statements only.

## Explicit noncorrespondence

The Lean module does **not** formalize or prove:

- the general `F[X]` diagonal-saturation module isomorphism;
- a general theory of minimal polynomial bases or Forney indices;
- existence of a forbidden M31 center;
- source-key distribution among M31 error-weight layers;
- a semantic first-match owner, refund, or occupancy-credit transport;
- common-core add-back, the rank-two coloop terminal, row-sharp Q, or row
  closure.

Those boundaries match the research note's nonclaims.  The next theorem must
construct or bound the diagonal-saturation indices on the actual marked
rank-46 source keys while carrying the canonical selector and root-status masks.
