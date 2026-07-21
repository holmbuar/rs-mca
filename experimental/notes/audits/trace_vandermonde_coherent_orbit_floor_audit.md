---
workboard_item: T
row: binary trace-Vandermonde RS family q=2^s, s an odd prime at least 3
object: OTHER
target_epsilon: NOT_INSTANTIATED
agreement: fixed-weight source m=q/4; this is not an MCA agreement
B_star: NOT_INSTANTIATED
direct_statement: image-compensated coherent weight-q/2 trace-character orbit has exponential loss on a genuine RS Vandermonde family
architecture: DIRECT
partition_digest: NOT_INSTANTIATED
atom_or_cell: RS_PHASE_STRUCTURED_SIDON_PAYMENT
quantifier: every odd prime s>=3 under the integrated binary-kernel theorem, plus an exact q=8 finite regression
projection_and_unit: effective-character coherent aggregate; not supports, rays, slopes, or codewords
claimed_bound: H/A_eff >= 2^(r+1)/((4r+1)(r+1))
status: COUNTEREXAMPLE
impact: ROUTE_CUT
falsifier: q=8 gives M=L=21, A_eff=64, H=105 from 35 same-phase genuine trace-Vandermonde characters
replay: python3 experimental/scripts/verify_trace_vandermonde_coherent_orbit_floor.py --check; python3 -O experimental/scripts/verify_trace_vandermonde_coherent_orbit_floor.py --check; repeat both modes with --tamper-selftest
---

# Audit: trace--Vandermonde coherent phase-orbit floor

**Audit verdict:** `COUNTEREXAMPLE_NEW_FLOOR`  
**Acceptance criterion:** 4  
**Lean validation state:** `AWAITING_FORK_CI`  
**Named floor:** `RS_TRACE_VANDERMONDE_COHERENT_ORBIT_FLOOR`  
**Remaining named input:** `POST_C1_C8_RS_ORBIT_DECORRELATION_OR_DIRECT_SIDON`

## 1. Scope audited

The packet attacks one precise successor statement to the absolute-dual-mass
half-slice obstruction:

> Genuine RS trace--Vandermonde phase origin, exact image normalization, and
> cancellation within each canonical phase-weight orbit suffice for a
> subexponential effective-character payment.

The threshold note gives an infinite family theorem and the exact `q=8`
falsifier.  The Lean module freezes the finite field arithmetic, actual RS
columns, syndrome injection, effective span, trace-character realization, and
coherent coefficient census.

The packet does not use an arbitrary sign assignment.  Every finite phase
pattern in the load-bearing orbit is accompanied by an explicit coefficient
vector `a=(a_1,a_2,a_3)` and checked against

\[
 t\longmapsto\operatorname{Tr}_{\mathbb F_8/\mathbb F_2}
 \left(a_1t+a_2t^2+a_3t^3\right).
\]

## 2. Branch and provenance

| item | frozen value |
|---|---|
| fork | `holmbuar/rs-mca` |
| base branch | `main` |
| base SHA | `4e5f0b77c98f075ea7c8822cd4859847a232bc2a` |
| upstream main at lane start | `a3017697ad1594521d2779fe1d83bccd45d4c06e` |
| branch | `gptpro/rs-phase-floor-hunt-normal-basis` |
| intended draft title | `CI: trace-Vandermonde coherent phase floor` |

The requested unsuffixed branch ref already existed at the current main SHA
with no commits and no pull request.  The packet therefore branched anew under
the suffixed descriptive name above rather than continuing an existing ref.

## 3. Imported API blob parity

The Lean module imports only `Std`; it imports no repository Lean API.
Consequently the required integrated-API parity table is vacuous rather than
silently omitted.

| imported integrated namespace | fork blob | upstream blob | result |
|---|---:|---:|---|
| `AsymptoticSpine.*` | not imported | not imported | vacuous parity |
| `M31QRootedShell.*` | not imported | not imported | vacuous parity |
| `M31C9RowSharp` | forbidden and not imported | forbidden and not imported | no dependency |
| `HalfSliceFalsifier` | forbidden and not imported | forbidden and not imported | no dependency |
| any open-PR module | not imported | not imported | no dependency |

The source documents used by the human proof are byte-identical on fork and
upstream main:

| source | fork blob | upstream blob |
|---|---|---|
| `experimental/grande_finale.tex` | `8a5d9791900ca9eed773feba146b92ad296704ce` | `8a5d9791900ca9eed773feba146b92ad296704ce` |
| `experimental/rs_mca_thresholds.tex` | `01302a797c502a05ed0b11ba949b8756e0aa2b22` | `01302a797c502a05ed0b11ba949b8756e0aa2b22` |
| `experimental/notes/thresholds/minimal_phase_supplement.md` | `6b1482b86e5eaad2046a41c5a122b86514a78a10` | `6b1482b86e5eaad2046a41c5a122b86514a78a10` |

No open pull request is a theorem or compilation dependency.

## 4. Exact PROVED-declaration table

### 4.1 General proof declarations

| ID | status | exact statement | hypotheses | proof location |
|---|---|---|---|---|
| G1 | PROVED | `Psi` is injective on the complete `m=r` slice, so `M=L=binom(4r-1,r)` and max fiber is one | `s` odd prime, `q=2^s`, `r=q/4`, integrated binary kernel is exactly `span{1_D}` | threshold note, Proposition 4.1 |
| G2 | PROVED | the effective difference span has dimension `N-1`, hence `A_eff=2^(4r-2)` | G1 family and `N=4r-1` odd | threshold note, Proposition 4.2 |
| G3 | PROVED | every even phase pattern, in particular every `|Y|=2r` pattern, is a trace-linear character of the actual RS columns | nondegenerate trace pairing and the exact binary kernel | threshold note, Section 5 |
| G4 | PROVED | every character in the orbit has coefficient `(-1)^(r/2) binom(2r-1,r/2)` | G1 family and `r` even | threshold note, equation (11) |
| G5 | PROVED | the coherent magnitude is `H=binom(4r-1,2r)binom(2r-1,r/2)` | G4; all orbit coefficients have the same real sign | threshold note, equation (12) |
| G6 | PROVED | the image-compensated coherent aggregate is at least `2^(r+1)/((4r+1)(r+1)) = exp((log 2)N/4-O(log N))` | G1--G5 | threshold note, equations (13)--(16) |
| G7 | PROVED route cut | orbitwise cancellation plus RS phase provenance does not universally imply subexponential payment | G1--G6 | threshold note, Theorem 8.1 |

### 4.2 Lean declarations for the exact `q=8` falsifier

| Lean declaration | exact certified statement | mathematical role |
|---|---|---|
| `field_arithmetic_exact` | the executable `F_8` trace/add/multiply range check is true | finite-field fixture |
| `source_mass_exact` | `M=21` | complete weight-two source |
| `syndrome_map_injective` | all 21 `(t,t^2,t^3)` support syndromes are distinct and fibers are singleton | actual RS image injection |
| `max_fiber_exact` | maximum realized fiber is 1 | exact Q |
| `image_normalized_q_exact` | `maxFiber * L = M` | exact image normalization |
| `effective_difference_span_exact` | six anchored RS differences generate 64 distinct vectors | effective span |
| `effective_target_size_exact` | `A_eff=64` | effective denominator |
| `all_effective_trace_patterns_realized` | the 64 explicit trace gauges give 64 distinct even phase patterns | genuine trace-character coverage |
| `coherent_orbit_size_exact` | the weight-four orbit has 35 classes | orbit count |
| `trace_phase_orbit_realized` | each orbit class equals the trace pattern of its paired explicit coefficient vector | RS phase correspondence |
| `anchor_translation_exact` | anchoring every phase at `t=1` leaves all weight-two coefficients unchanged | effective-difference-span correspondence |
| `coherent_orbit_coefficients_exact` | all 35 actual trace-phase coefficients equal `-3` | same-phase obstruction |
| `coherent_signed_sum_exact` | the one-block signed sum is `-105` | cancellation-sensitive aggregate |
| `coherent_magnitude_exact` | coherent magnitude is 105 | exact floor numerator |
| `source_normalized_coherent_exact` | `H=5M` | source-normalized loss |
| `image_compensated_coherent_strict` | `A_eff*M < L*H` | exact image-compensated failure at multiplier one |
| `coherent_multiplier_floor` | every natural multiplier paying the cleared aggregate is at least 2 | finite falsifier theorem |

All declarations carry their finite parameters definitionally in the module.
No theorem silently identifies this phase aggregate with an MCA slope count.

## 5. Executable certificate audit

Canonical certificate:

```text
experimental/data/certificates/trace-vandermonde-coherent-orbit-floor/
  trace_vandermonde_coherent_orbit_floor.json
```

Verifier:

```text
experimental/scripts/verify_trace_vandermonde_coherent_orbit_floor.py
```

Frozen SHA-256 values before fork CI:

| artifact | SHA-256 |
|---|---|
| certificate JSON | `7ec07b4200bcabef3c9531f7a75d6044723ac2eca5444b2b2fb546f674755677` |
| verifier | `435e05e441aac3d5c7f05275d96feeddc598b68577b1f36c2172ad5be66d7c88` |

The verifier uses explicit exceptions, not `assert`, and checks:

1. base/source provenance;
2. `F_8` multiplication and trace;
3. the primitive-element cycle;
4. all 21 weight-two supports and exact RS syndromes;
5. syndrome injectivity and max fiber one;
6. all 64 subsets of the six difference generators;
7. all 512 trace coefficient triples and the 64-pattern even-phase image;
8. all 35 orbit witnesses;
9. all 35 exact anchored coefficients `-3`;
10. coherent sum `-105`, magnitude 105, and the cleared compensation inequality;
11. the `r=2` specialization of the general formulas.

Local replay used for certificate verification only, not Lean validation:

```text
python3  experimental/scripts/verify_trace_vandermonde_coherent_orbit_floor.py --check
python3 -O experimental/scripts/verify_trace_vandermonde_coherent_orbit_floor.py --check
python3  experimental/scripts/verify_trace_vandermonde_coherent_orbit_floor.py --tamper-selftest
python3 -O experimental/scripts/verify_trace_vandermonde_coherent_orbit_floor.py --tamper-selftest
```

Result before branch publication:

```text
PASS: 21 supports, 512 trace coefficients, 35 coherent characters, 411 exact gates
PASS: 6/6 mutations rejected
```

Both lines passed in ordinary and optimized modes.

## 6. Lean census target

| item | required value |
|---|---:|
| Lean version | 4.31.0 |
| imports | `Std` only |
| Mathlib | 0 |
| `sorry` | 0 |
| `admit` | 0 |
| `sorryAx` | 0 |
| custom axioms | 0 |
| `native_decide` | 0 |
| unsafe declarations | 0 |
| project API imports | 0 |

The module ends with `#print axioms` for every load-bearing finite theorem.
The expected output is either `[]` or standard kernel principles only; the
final CI run and exact output will be recorded below before the branch is
declared ready.

## 7. Source-label map

| packet statement | source label or exact source boundary |
|---|---|
| effective difference span | `experimental/grande_finale.tex`: `eq:effective-fourier-span`, `lem:effective-span-fourier` |
| image compensation | `eq:image-ambient-scales`, `def:effective-fourier-payment` |
| minor/major interfaces being route-cut | `def:aggregate-minor-payment`, `def:major-arc-aggregate`, `prop:effective-mi-ma-flatness` |
| direct max-fiber/Sidon comparison | `def:primitive-q`, `def:sidon-heavy`, `def:sidon-paid-cell` |
| binary trace-Vandermonde kernel | `experimental/notes/thresholds/minimal_phase_supplement.md`, exact RS regression and equation `(C6)` |
| deployed row authority not instantiated | `tex/cs25_cap_v13_2.tex` and `experimental/rs_mca_thresholds.tex` |

## 8. Explicit nonclaims

1. The full fixed-weight slice is not proved to be a genuine post-C1--C8
   first-match survivor.
2. No received line, affine slope, ray, codeword numerator, or deployed row is
   constructed or bounded.
3. No row-sharp `U_Q`, `U_BC`, `U_new`, or adjacent certificate is banked.
4. No residual-to-full add-back or line-local `UNIF` theorem is proved.
5. Cross-orbit cancellation is not ruled out.
6. Odd characteristic is not treated.
7. The finite Lean theorem does not formalize the infinite-family rank theorem;
   that theorem is used from the byte-pinned integrated source.
8. Compilation will certify the finite module only; it will not certify the
   prose proof or semantic first-match survival.
9. The result does not refute a direct Sidon/max-fiber route.  On this family,
   direct Q is exact while the tested phase aggregate is large.

## 9. Validation record

To be completed only from the fork draft PR:

| field | value |
|---|---|
| draft PR | `AWAITING_FORK_CI` |
| validated head SHA | `AWAITING_FORK_CI` |
| workflow run | `AWAITING_FORK_CI` |
| package job | `AWAITING_FORK_CI` |
| build-log artifact | `AWAITING_FORK_CI` |
| Lean result | `AWAITING_FORK_CI` |
| `#print axioms` census | `AWAITING_FORK_CI` |
| manual statement/source comparison | completed before publication; repeat after final green head |

# COUNTEREXAMPLE_NEW_FLOOR
