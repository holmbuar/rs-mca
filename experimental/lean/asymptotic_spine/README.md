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

`AsymptoticSpine.UniformClosedLedger` packages a finite numeric compiler
boundary used after a separately proved first-match classification. Each
profile carries a C1--C9 or primitive label, an assigned slope list, the
residual/Sidon/ray payment chain, and its own natural scale. The labels and
lists are caller-supplied data; the structure does not prove that they describe
actual RS bad slopes or least semantic owners. Each supplied line also exposes
its realized-profile cap. The compiler proves

```text
sup_line bad(line)
  <= sup_line sum_profile U(line,profile)
  <= loss * sup_line sum_profile naturalScale(line,profile).
```

`UniformClosedLedger.compile` consumes the supplied line-local bound and
produces the finite row-list numerator bound. The executable diagonal regression
`sup_sum_interchange_falsifier` proves that replacing `sup_line sum_profile` by
`sum_profile sup_line` changes and can loosen the required quantity. The module
does not construct the semantic atlas, prove line completeness, construct
C7/C8/C9 payments, establish residual/full comparison or image-normalized Sidon,
prove a ray compiler or subexponential profile count, supply actual asymptotic
`(UNIF)`, or compare the profile envelope with a target. `naturalTotal` contains
only the profile sum, so any universal terms must be absorbed by the supplied
`envelope`.

## Conditional C7 ledger adapter and atlas-order regressions

The integrated narrow modules `C7BasePoleProducer` and
`C7BasePoleWitnessProducer` remain independent of `UniformClosedLedger` and are
unchanged by this packet. `C7BasePoleLedgerBridge` and
`C7BasePoleWitnessLedgerBridge` add the deferred `ProfilePayment`,
`ClosedLineLedger`, and one-line hand-off on top of their existing
`directBudget` interface. The bridge proves that both line-local totals equal
the deletion-aware `directBudget`, and bounds them by the raw census and the
supplied `q - 1` value.

`BasePoleC7WitnessClass` assumes its source-facing witness, coefficient, exact
slope-law, injectivity, and census fields. The new modules do not formalize the
finite field, locator algebra, received pole line, or `d ↦ -d`; they are
conditional finite adapters. `C7BasePoleLineExtension` lifts the unit C7
payments to any compiler loss at least one, appends them to an earlier numeric
line, preserves disjointness, and proves exact budget and natural-scale
telescopes without inflating the local C7 ray budget.

The historical filename `SemanticAtlasOwnership` now contains only a labeled
C3 numeric interface. Its provenance labels prove no semantic classification
and select no active-atlas policy. `C7OwnerRegression` rejects an untrimmed C7
payment after an earlier duplicate assignment.
`C7SingletonPlantedAbsorption` shows that a broader supplied singleton-root
order can leave the later C7 residual empty; it records atlas noncanonicity, not
a theorem choosing singleton C3 owners.

These asymptotic-spine modules are interface/provenance formalizations, not the
active theorem authority. They do not construct a fixed-before-line C1--C9
atlas, prove a concrete RS semantic C7 owner or survivor, establish completeness
over received lines or actual row-wide `(UNIF)`, compare an envelope with a
target, prove an adjacent safe row, or close an RS--MCA row. See
`experimental/notes/audits/c7_base_pole_closed_ledger_producer.md` for the exact
statement map and proof boundary.

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
