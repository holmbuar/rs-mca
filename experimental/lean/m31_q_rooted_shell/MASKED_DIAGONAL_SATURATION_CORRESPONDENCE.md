# Masked diagonal saturation: source/Lean correspondence

## Packet

- Predecessor audit:
  `experimental/notes/audits/m31_padding_bridge_audit.md`
- Successor proof note:
  `experimental/notes/audits/m31_masked_diagonal_saturation.md`
- Lean module:
  `M31QRootedShell/MaskedDiagonalSaturation.lean`
- Target package:
  `experimental/lean/m31_q_rooted_shell`
- Lean version: `v4.31.0`
- Dependency policy: stdlib only
- Terminal: `PROVED_MASKED_DIAGONAL_SATURATION`

The packet is the successor to upstream PR #1014.  It retains that packet's
`F_11` counterexample to direct transport of a named actual-error minimal row.
The new theorem compares intrinsic successive minima and constructs a new
padded frame; it does not identify the old actual-error basis with the padded
basis.

## Source theorem boundary

The proof note establishes the following polynomial-module statements.

1. **Successive-minimum monotonicity.**  If `N subset M subset F[X]^t` are free
   modules of the same rank and their ordered minimal-basis degrees are
   `beta_i` and `alpha_i`, then `beta_i >= alpha_i` for every `i`.
2. **Application to the #1014 bridge.**  For

   ```text
   N=DSat_Q(Syz(P)) subset Syz(P)=M,
   ```

   the diagonal isomorphism gives `nu_i=lambda_i+d`, while monotonicity gives
   `nu_i>=mu_i`.
3. **Uniform deployed last-index floor.**  The source non-surjectivity bound
   `mu_45>=K-j+1` and `d=R-j` imply

   ```text
   lambda_45>=K-R+1=67,448.
   ```
4. **Primitive padded sum.**  Dividing any additional padded common gcd changes
   no syzygy module and leaves an equal-degree primitive 46-column row of degree
   at most `R`; hence `sum_i lambda_i<=R`.
5. **Rank-46 conclusion.**  The first 44 indices total at most `913,681`, so

   ```text
   lambda_1<=20,765,
   lambda_1+lambda_2<=41,530,
   lambda_1+lambda_2+lambda_3<=62,295.
   ```

These polynomial statements are proved in the note rather than represented by
custom Lean axioms.

## Lean declaration map

| Lean declaration | Source statement checked |
|---|---|
| `deployed_parameter_identities` | `R=n-a`, `w=K-R`, `913681=R-(w+1)`, and rank `45=46-1`. |
| `signed_occupancy_crossing` | `16517335+259881=16777216=B*+1` and allowance plus one equals the marked-key floor. |
| `shifted_last_index_floor` | From `mu_45>=K-j+1`, `mu_45<=nu_45`, and `nu_45=lambda_45+(R-j)`, infer `lambda_45>=67448`. |
| `padded_prefix44_bound` | Total padded Forney degree at most `R` and the last-index floor leave prefix cap `913681`. |
| `padded_first_three_bounds` | Ordered rank-46 arithmetic gives the exact caps `20765`, `41530`, and `62295`. |
| `rank46_extremal_arithmetic` | Exact hostile thresholds `913704`, `913703`, and `913702`, all above the prefix cap. |
| `masked_first_three_shifted_bound` | Exact shifted masked sum `nu_1+nu_2+nu_3<=62295+3(R-j)`. |
| `padded_rank_three_margin` | `62295<67447` with exact margin `5152`. |
| `direct_transport_blocked_bands_are_covered` | Both predecessor blocked maxima lie below `R`; the new theorem is weight-uniform. |
| `MarkedRank46Key` | Typed finite interface carrying source metadata and every arithmetic premise consumed by the compiler. |
| `compileKey` | Attaches the derived padded/masked bounds without changing source metadata. |
| `marked_source_key_floor_preserved` | The compiler preserves the exact `259881` source-key floor. |
| `source_key_ids_preserved` | No source key is deleted, duplicated, or merged. |
| `selectors_preserved` | Ordered first-agreement selectors are unchanged. |
| `root_status_masks_preserved` | Actual-error/padding root masks are unchanged. |
| `semantic_owners_preserved` | Existing semantic ownership data are unchanged; no owner is synthesized. |
| `refunds_preserved`, `refund_sum_preserved` | Refund vectors and their exact aggregate are unchanged. |
| `signed_occupancy_credit_vectors_preserved`, `signed_occupancy_credit_sum_preserved` | Signed credit vectors and their exact aggregate are unchanged. |

## Statement audit

The Lean arithmetic interface intentionally prints all hypotheses that come
from polynomial theory:

```text
weight <= R,
K-weight+1 <= actualLast,
actualLast <= maskedLast,
maskedLast = paddedLast+(R-weight),
ordered first three padded indices,
41*paddedThird <= paddedTail41,
padded total degree <= R,
masked_i = padded_i+(R-weight) for i=1,2,3.
```

No hypothesis is hidden inside an opaque declaration.  The compiler's metadata
contains the received center, codewords, exact weight, ordered domain, ordered
anchors, distinguished extra support, first-agreement selectors, root masks,
semantic owner, refunds, and signed occupancy credits.  Every preservation
theorem is definitional or follows by list-map simplification.

The general polynomial proof remains in the source note because this stdlib-only
package has no polynomial-ring, row-reduced-basis, or Forney-index library.  The
kernel certificate therefore validates the complete deployed arithmetic and
typed preservation boundary, not a generic implementation of minimal
polynomial bases.

## Sorry and axiom census

```text
sorry              0
custom axioms       0
Mathlib imports     0
```

The module imports only existing stdlib-only modules in the same package and
uses `omega`, decidable exact arithmetic, structures, and lists.  Green fork CI
proves compilation only; this correspondence separately audits the match to the
source theorem.

## Explicit noncorrespondence

The packet does **not** formalize or prove:

- a polynomial-ring implementation of successive minima or predictable degree;
- existence of a forbidden M31 center;
- common-core add-back after the padded rank-three frame;
- the rank-two coloop terminal;
- an exhaustive semantic owner or a new owner charge;
- row-sharp `U_Q`, list-interior coverage, or an adjacent safe row;
- identification of the global rank-two Popov basis with a local actual-error or
  padded rank-46 basis.

The algebraic padding terminal is discharged, but every downstream payment and
row-closure obligation remains separately conditional.
