# Lean correspondence: primitive Boolean fibers and energy split

## Status

PROVED for the concrete finite Boolean-family semantics, exact difference and
closure definitions, residual-prefix construction, and low/high moment
partition.  CONDITIONAL for the final high-energy and low-energy payments:
Balog--Szemerédi--Gowers extraction, quasicube growth, and the Sidon/low-energy
moment estimate remain explicit inputs.

## Source

The source is `experimental/asymptotic_rs_mca_frontiers.tex`, especially the
primitive Boolean slice and Sidon/energy split surrounding
`prop:no-high-energy`.  The Lean modules are:

- `experimental/lean/asymptotic_spine/AsymptoticSpine/BooleanFiber.lean`;
- `experimental/lean/asymptotic_spine/AsymptoticSpine/NoHighEnergy.lean`;
- `experimental/lean/asymptotic_spine/AsymptoticSpine/PrimitiveBoolean.lean`.

## Statement-to-declaration map

| Finite step | Lean declaration | Status |
| --- | --- | --- |
| A duplicate-free fixed-weight family in `{0,1}^n` | `BoolFamily` | PROVED concrete representation |
| Integer embedding and exact ordered-pair difference set | `bitEmbed`, `bitDifference`, `BoolFamily.differenceSet` | PROVED definitions |
| A realized pair `(s,d)` has an actual Boolean family witness | `BoolFiber` | PROVED semantic predicate |
| Nonempty families have nonempty difference sets; in particular `(2,0)` is impossible | `differenceSet_length_pos_of_points_ne_nil`, `not_boolFiber_two_zero` | PROVED |
| `a-b=d-c` iff the forced fourth point satisfies `d=a-b+c` in the integer embedding | `bitDifference_eq_iff_embed_eq_closure` | PROVED |
| Each ordered triple admits at most one closing fourth point | `closureCandidates_length_le_one` | PROVED |
| Exact closure/repeated-difference energy and `E(F)<=|F|^3` | `additiveEnergy`, `additiveEnergy_le_card_cubed` | PROVED |
| The complete fixed-weight slice, routed residual, and prefix key | `PrimitiveBooleanLeaf` | EXPLICIT FINITE DATA; fullness is certified by `full_complete` |
| A residual prefix class is a sublist of the full prefix class | `residualPrefixFiber_sublist_fullPrefixFiber` | PROVED; specializes existing residual filtering |
| Full and residual prefix classes are semantic Boolean fibers | `fullFiberFamily_isBoolFiber`, `residualFiberFamily_isBoolFiber` | PROVED |
| Closure energy is exactly the standard `a-b=c-d` witness count | `additiveEnergy_eq_repeatedDifferenceWitnesses`, `mem_repeatedDifferenceWitnesses_iff` | PROVED |
| Low/high energy tests partition the ordinary finite moment exactly | `ordinaryFiberMoment_eq_low_add_high` | PROVED |
| Moment excess forces a large high-energy member | `exists_large_highEnergyFiber_of_moment_excess` | PROVED exact finite contrapositive |
| BSG plus quasicube caps every high-energy member by `K^(3C)` | `booleanFiberStat_count_le_of_bsg_quasicube` | CONDITIONAL on both named inputs; reuses `no_high_energy_bound` |
| The ordinary moment is paid by the low-energy term plus the high-energy cap | `primitiveBooleanMomentUpper` | CONDITIONAL on BSG and quasicube |
| A supplied low-energy/Sidon budget closes the finite compiler | `primitiveBooleanMomentUpper_of_lowEnergyPayment` | CONDITIONAL on all three named inputs |

## Scope guard

All Boolean operations are performed after the coordinatewise embedding into
`Vector Int n`; no characteristic-two cancellation is used.  The energy is the
finite count of ordered quadruples satisfying a repeated-difference equation,
represented through its equivalent forced-closure form.  Duplicate-free point
lists ensure that a fixed ordered triple contributes at most one fourth point.

`PrimitiveBooleanLeaf.full_complete` is a certificate that its list is the
entire fixed-weight slice.  The routed residual is allowed to delete points,
but it must be a displayed sublist.  Filtering by a prefix key therefore gives
a concrete residual `BoolFamily`; it does not assert that the residual remains
the whole prefix class.

The module deliberately reuses the existing exact finite APIs in `Moment.lean`,
`EffectiveClosure.lean`, and `NoHighEnergy.lean`.  It does not prove BSG,
quasicube growth, the low-energy/Sidon payment, a large-fiber-to-high-energy
implication, max-fiber control, C9, an asymptotic `o(n)` estimate, a character
frame theorem, or profile-atlas exhaustiveness.

## Build and trust audit

From `experimental/lean/asymptotic_spine/`:

```text
lake build
```

The package is stdlib-only on Lean 4.31.0.  The selected `#print axioms` checks
report only Lean's standard `propext`, `Quot.sound`, and `Classical.choice`.
There is no `sorryAx`, `sorry`, `admit`, `native_decide`, or added axiom.
