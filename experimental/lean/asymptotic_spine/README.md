# Asymptotic Spine (stdlib-only Lean)

This Lean 4 package checks finite arithmetic and combinatorial lemmas used in
the asymptotic Reed–Solomon MCA analysis. It is deliberately stdlib-only and
builds with Lean `v4.31.0`.

## Build

```sh
cd experimental/lean/asymptotic_spine
lake build
```

## Exact adjacent identity scale

`AsymptoticSpine.StaircaseDeep` represents the literal identity-profile scale

```text
I(a) = binom(n,a) / |B|^w,   a = K+w,
```

as an exact natural-number numerator/denominator pair. The adjacent step is
proved without division:

```text
binom(n,a+1) (a+1) = binom(n,a) (n-a),
denominator(w+1) = denominator(w) |B|.
```

Combining these identities gives the cross-multiplied form of

```text
I(a+1) / I(a) = (n-a) / ((a+1)|B|).
```

The same module composes this equality with an adjacent unsafe/safe
certificate, proving that `a+1` is the first safe agreement.

| Lean declaration | Mathematical statement | Source label |
| --- | --- | --- |
| `staircaseBinom_succ_right_eq` | Exact adjacent binomial identity | `lem:exact-adjacent-identity-ratio` |
| `IdentityRawScale.next_numerator_step` | Numerator step from agreement `a` to `a+1` | `lem:exact-adjacent-identity-ratio` |
| `IdentityRawScale.adjacent_ratio_cross` | Cross-multiplied identity-scale ratio | `lem:exact-adjacent-identity-ratio`, equation (AR1) |
| `FrontiersStaircase.adjacent_isFirstSafe` | Adjacent unsafe/safe values pin the first safe agreement | `thm:unconditional-support-envelope-bracket`, adjacent case of (SB3) |
| `FrontiersStaircase.adjacent_identity_ratio_pins_threshold` | Exact ratio together with adjacent threshold pinning | (AR1) and the adjacent case of (SB3) |

## Scope

The exact rational ratio is represented by equality of cross products; the
logarithmic equality in (AR1) is not formalized here. The threshold corollary
assumes the unsafe and safe facts as inputs. Establishing those facts from the
literal lower and upper MCA budgets remains outside this theorem.

The package also contains modules for averaging, moment bounds, Boolean-fiber
arithmetic, profile envelopes, effective closure, rerouting, and the finite
root-incidence core of the deep-regime upper bound. `AsymptoticSpine.lean`
imports the complete package.


## Window-cell aggregation

`AsymptoticSpine.WindowCells` aggregates the generic window engine over
C1--C8 and formalizes slope-conserving activation handoff. The source-side
window-uniformity arithmetic can be checked from the repository root with

```sh
python3 experimental/scripts/verify_asymptotic_window_uniformity.py
python3 experimental/scripts/verify_asymptotic_window_uniformity.py --tamper-selftest
```

The package formalizes finite and denominator-cleared arithmetic. Analytic
entropy, Stirling, real-limit, and inverse-theorem inputs remain explicit
hypotheses or source-side assumptions. Individual module headers state their
precise proof boundaries.

## Minimal closed-ledger / UNIF compiler

`AsymptoticSpine.UniformClosedLedger` packages the post-deletion semantic
boundary needed by the profile-envelope proof. Each profile carries a C1--C9
or primitive owner, its assigned distinct-slope list, the residual/Sidon/ray
payment chain, and its own natural scale. Each received line also exposes its
realized-profile cap. The compiler proves

```text
sup_line bad(line)
  <= sup_line sum_profile U(line,profile)
  <= loss * sup_line sum_profile naturalScale(line,profile).
```

`UniformClosedLedger.compile` consumes the honest line-local `(UNIF)` bound and
produces the row-level numerator bound. The executable diagonal regression
`sup_sum_interchange_falsifier` proves that replacing `sup_line sum_profile` by
`sum_profile sup_line` changes and can loosen the required quantity. The module
does not construct the semantic
atlas, C7/C8/C9 payments, residual/full comparison, image-normalized Sidon
input, ray compiler, subexponential profile count, the actual asymptotic/window-
uniform estimate, or profile-envelope comparison; those remain explicit
producer obligations. Its finite `lines` list is supplied by the caller and is
not itself a completeness proof over all received RS lines, nor does it enforce
one global profile atlas fixed before the received line. `naturalTotal` contains
only the profile sum, so the universal terms in the literal frontiers envelope
must be absorbed by the supplied `envelope`.

## C7 first-match regression and rooted base-pole producer

`AsymptoticSpine.C7OwnerRegression` is the negative guardrail. It models the
established affine-Steiner family in which one slope occurs in both an earlier
C1 quotient projection and a later raw C7-style collapse projection. The raw C7
direct inequality is numerically valid, but installing the untrimmed raw cell
after C1 violates `ClosedLineLedger.firstMatchOwnership`. This rejects double
charging; it does not require a correct producer to retain every raw C7 slope.

`AsymptoticSpine.C7BasePoleProducer` is the deletion-aware slope-level adapter
for the real base-pole constant-coefficient class. Given the aggregate earlier
C1--C6 slope image on the same received line, it defines the assigned C7 image
as `raw \ earlier`, installs one direct unit-scale
`ProfilePayment.ofDirect .c7` for each survivor, and proves that the C7
line-local budget and natural sum both equal the survivor count and are bounded
by the raw `q - 1` census.

`AsymptoticSpine.C7BasePoleWitnessProducer` records the preceding rooted source
boundary. Its `BasePoleC7WitnessClass` contains the actual witness catalogue,
locator constant coefficient, exact slope law `slope(w) = slopeOfCoeff(d)`,
injectivity of the coefficient-to-slope map, and the realized-coefficient
census. It proves witness-exhaustive constant-coefficient fibres, exact equality
between the constructed raw slope list and the witness slope image, and a
surviving raw witness for every assigned C7 slope.

`AsymptoticSpine.C7BasePoleLineExtension` appends those surviving singleton
profiles to an already-closed C1--C6 line. It preserves duplicate-free
first-match ownership and proves the exact line-local telescopes

```text
combined budgetTotal
  = prior budgetTotal + number of C7 survivors,

combined naturalTotal
  = prior naturalTotal + number of C7 survivors.
```

The added cost is at most `q - 1`. The executable fixture deletes two earlier-
owned raw slopes and appends exactly the two survivors. These modules assert no
survivor nonemptiness on every line, global fixed-before-line atlas, actual
row-wide `(UNIF)`, target comparison, or row closure.

## Upgrade regression locks

`AsymptoticSpine.RegressionLocks` restates the current general interfaces for
the conditional profile-envelope frontier bracket, the deep-regime incidence
ledger, the prefix/residual effective-closure bridge, and first-match add-back
sufficiency. It also replays one exact finite fixture from each module.

These wrappers add no new source-paper claim: they make declaration drift,
lost imports, and broken computation visible in the default Lake build. A
green build certifies only the Lean statements and their explicit hypotheses.
It does not construct the finite-field incidence ledger, prove the residual
ray compiler, remove the profile compiler inputs, or upgrade a conditional
source theorem to an unconditional one. See `REGRESSION_LOCKS.md` for the
direct statement map.
