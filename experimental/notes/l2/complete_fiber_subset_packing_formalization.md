# Complete-fiber subset-packing Lean formalization

## Status

PROVED

The formalized result is the fixed-size subset-packing compiler used for
equation (2) of
`experimental/notes/l2/dyadic_complete_fiber_slicing_route_cut.md`:

```text
#{P : |E_c(P)| = e}
  <= floor(choose(N_c, h_c + 1) / choose(e, h_c + 1)).
```

The source-facing Lean declaration is
`CompleteFiberSubsetPacking.completeFiberSubsetPacking`; it is built from the
generic compiler
`CompleteFiberSubsetPacking.subsetPacking_finite_and_ncard_le` in the package
`experimental/lean/complete_fiber_subset_packing/`.

## Exact theorem

For arbitrary types `alpha` and `beta`, the theorem takes:

- a finite ground set `ground : Finset alpha`;
- an arbitrary set `objects : Set beta`;
- a block map `block : beta -> Finset alpha`;
- natural numbers `e,h`;
- containment of every object block in `ground`;
- exact block size `e`;
- intersection size at most `h` for distinct objects; and
- `h+1 <= e`.

It concludes both that `objects` is finite and that

```text
objects.ncard <= choose(ground.card, h+1) / choose(e, h+1).
```

Thus the theorem does not presuppose finiteness of the source polynomial
family.  It derives it from the same intersection hypothesis used in the
double count.  The printed public signature has no `DecidableEq alpha` or
`DecidableEq beta` parameter; the local classical instance only elaborates
finite-set intersections and powersets.

## Source connector

`fixedFiberPolynomialSet H K m c e U` is exactly the set of polynomials that
belong to the received list and whose canonical complete-fiber set has
cardinality `e`.  The source theorem imports the already proved
`DyadicCompleteFiberSlicing.completeFiberIntersection`, takes

```text
ground = powerImage H c,
block P = completeFiberSet H c (canonicalSupport H m U P),
h = floor((K-1)/c),
```

and proves every generic premise directly.  Its exported wrapper retains the
arbitrary field, finite ordered multiplicative subgroup of cardinality `n`,
`1 <= K <= m <= n`, divisor `c | n`, arbitrary received word, and fixed
`e >= floor((K-1)/c)+1` hypotheses.  The numerator
`(powerImage H c).card` is exactly the source definition `N_c = |Q_c|`.

## Proof map

1. If two objects have the same block, that block intersects itself in `e`
   points.  The distinct-object hypothesis would give at most `h`, contrary
   to `h+1 <= e`; hence the block map is injective on `objects`.
2. Every block lies in `ground.powersetCard e`.  The finite image and the
   injectivity just proved imply `objects.Finite`.
3. For each realized block, take its family of `(h+1)`-subsets.  Two distinct
   block families are disjoint: a shared member would give `h+1` points in
   their intersection.
4. Their disjoint union lies in `ground.powersetCard (h+1)`.  Mathlib's
   `Finset.card_biUnion` and `Finset.card_powersetCard` therefore give

   ```text
   #objects * choose(e,h+1) <= choose(#ground,h+1).
   ```

5. `Nat.choose_pos` makes the denominator positive from `h+1 <= e`, and
   `Nat.le_div_iff_mul_le` yields the exact floored quotient.

## Replay and axioms

The package pins Lean 4.28.0 and Mathlib commit
`8f9d9cff6bd728b17a24e163c9402775d9e6a365`.

```text
lake build
Build completed successfully (8029 jobs).

#print axioms CompleteFiberSubsetPacking.subsetPacking_finite_and_ncard_le
[propext, Classical.choice, Quot.sound]
```

The Lean file contains no `sorry`, `admit`, `sorryAx`, custom `axiom`, custom
`opaque`, or `native_decide`.  The companion fail-closed verifier pins the
source reference, exact declaration, proof anchors, package root, toolchain,
Mathlib revision, README, and this note, and includes a mutation self-test.

## Boundary

This package proves both the complete combinatorial compiler and the
source-specific equation-(2) wrapper.  It does not separately formalize the
group-cardinality rewrite `(powerImage H c).card = n/c`; the theorem retains
the exact source definition `N_c = |Q_c|` instead.

No Johnson-ball packing theorem (equation (3)), deployed integer certificate,
residual `1792`-profile cap, uniform residual sublist cap, GRS/syndrome
transport, Grand List, Grand MCA, extension-field list result, or
exact-threshold conclusion is formalized here.
