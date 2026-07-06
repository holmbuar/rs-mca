# L1 E3 Level-Set Lean Skeleton

This experimental Lean package records a formalization skeleton for the L1
coset level-set inequality. It was imported from PR #360 after renaming the
placeholder package to `l1_e3_level_set`; it was not Lake-built locally during
integration.

The file `l1_e3_level_set/Main.lean` defines the cosets of nonzero
`ell`-th powers in `ZMod p`, the level maximum on each coset, and the excess
quantity `E3`. The target theorem is

```lean
E3 p ell Gamma <= ell - 2
```

under the exact hypotheses used in the L1 notes: `ell` odd prime, `ell ∣ p-1`,
`Gamma ≠ 0`, no constant term, and `Gamma.natDegree <= ell - 1`.

The surrounding partition lemmas are intended to formalize that the nonzero
field elements split into `(p-1)/ell` cosets of size `ell`, with each coset
level set bounded by `ell`. The main inequality remains an annotated `sorry`;
do not cite this package as a formal proof of the L1 ceiling.

The accompanying `NOTES.md` records the mathematical reduction to the open
rank/syzygy crux `dim Syz <= K`, the counterexample showing that coprime
co-fiber locators alone are insufficient, and the syzygy lead used by the
experimental scripts.
