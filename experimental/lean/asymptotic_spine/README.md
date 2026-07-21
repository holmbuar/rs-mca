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
does not construct the semantic atlas, C7/C8/C9 payments, residual/full
comparison, image-normalized Sidon input, ray compiler, subexponential profile
count, the actual asymptotic/window-uniform estimate, or profile-envelope
comparison; those remain explicit producer obligations. Its finite `lines`
list is supplied by the caller and is not itself a completeness proof over all
received RS lines, nor does it enforce one global profile atlas fixed before
the received line. `naturalTotal` contains only the profile sum, so the
universal terms in the literal frontiers envelope must be absorbed by the
supplied `envelope`.

## Actual C8 chart exhaustion at the spine calibration

`AsymptoticSpine.C8ChartExhaustion` constructs four raw chart projections and
applies the integrated first-match deletion operation.  The exact assigned
slope cells are

```text
[[5], [7,9], [11,13], [17]].
```

They correspond, in order, to:

```text
C1-owned earlier chart,
the supplied shallow closure chart,
a paid one-parameter moving-root chart,
DEEP_HIGHER_DIMENSIONAL_BALANCED_CORE_AFTER_C1_C7_SHALLOW_AND_ONE_PENCIL_DELETION.
```

The supplied shallow input is field-for-field the existing spine fixture used
by the C8 producer boundary: `affineToyBridge`, syndrome key `1`,
`highKappaToySE2`, its chart inclusion, `highKappaToyBounds`, and kernel label
`1000000`.  Its post-deletion slopes are exactly `[7,9]` and the integrated
shallow closure theorem proves their direct finite payment.  The bounded chart
carries the actual slope list `[11,13]` and a KoalaBear moving-root certificate,
which gives exact cap two.

The module proves both chart-key uniqueness and slope-level duplicate freedom
across the four buckets.  It does **not** pay the named deep residual, construct
a deployed RS semantic owner function, prove a common-core shortening
certificate, import open PR #1011/#1020, establish `UNIF`, or close a deployed
row.  Exact statement correspondence and nonclaims are in
`experimental/notes/audits/c8_chart_exhaustion_preflight.md`.

The replay packet is checked with

```sh
python3 experimental/scripts/verify_c8_chart_exhaustion.py --check
python3 -O experimental/scripts/verify_c8_chart_exhaustion.py --check
python3 experimental/scripts/verify_c8_chart_exhaustion.py --tamper-selftest
```

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
