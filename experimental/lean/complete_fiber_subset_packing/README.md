# Complete-fiber subset-packing formalization map

Build the standalone package with its pinned Lean 4.28 / Mathlib environment:

```bash
lake build
```

## Source correspondence

Source note:
`experimental/notes/l2/dyadic_complete_fiber_slicing_route_cut.md`.

| Source statement | Lean declaration | Status |
|---|---|---|
| Equation (2), fixed-size subset-packing kernel | `CompleteFiberSubsetPacking.subsetPacking_finite_and_ncard_le` | PROVED |
| Equation (2), arbitrary-field complete-fiber wrapper | `CompleteFiberSubsetPacking.completeFiberSubsetPacking` | PROVED |

Instantiate `ground` with `Q_c`, `objects` with the fixed-`e` polynomial
family, and `block P` with `E_c(P)`.  Given the equation-(1) intersection
bound and `h_c + 1 <= e`, the theorem first proves that the object set is
finite and then proves exactly

```text
#objects <= floor(choose(#ground, h_c + 1) / choose(e, h_c + 1)).
```

The arbitrary object type is not assumed finite.  Equal blocks for two
distinct objects would have intersection size `e > h_c`, so the block map is
injective; its image lies in the finite family of `e`-subsets of `ground`.
The local classical decidable-equality instance is proof infrastructure and
does not appear in the exported theorem signature.

The source-facing wrapper imports
`DyadicCompleteFiberSlicing.completeFiberIntersection`, defines the fixed-`e`
set of received-list polynomials, and discharges containment, exact block
size, and pairwise intersection before applying the generic compiler.  Its
numerator uses `(powerImage H c).card`, which is definitionally the source's
`N_c = |Q_c|`.

The declarations report only `[propext, Classical.choice, Quot.sound]` and no
`sorryAx` or custom axiom.

## Boundary

This package formalizes both the combinatorial implication and its full
source-specific equation-(2) instantiation.  It does not separately prove the
normalization `(powerImage H c).card = n / c`; the theorem keeps the exact
source quantity `N_c = |Q_c|` in cardinality form.  Equation (3), deployed
arithmetic, the residual `1792`-profile cap, Grand List, Grand MCA, and
exact-threshold closure are not claimed.
