# C9 full-prefix owner-refund floor: source correspondence

## Scope

This independent stdlib-only package checks the finite cardinality boundary in
`experimental/notes/thresholds/m31_c9_full_prefix_owner_refund_floor.md`.
It mirrors the exact owner-complement and `(SE2)` shapes used by the C9 producer,
then proves the generic owner-refund cut and the deployed Mersenne-31 ledger
arithmetic.

It does not import the open-PR C9 module or any repository module. It does not
enumerate the deployed RS support slice, construct the final C1--C8 owner
function, prove co-location of the `c=2048` floor, prove a deployed residual
lower bound, or prove row-sharp Q.

## Statement map

| Lean declaration | Source-level role | Exact status |
|---|---|---|
| `mem_residualOf_iff` | standalone post-C1--C8 residual condition: full-slice/fiber membership plus `earlierOwner = none` | `PROVED` |
| `residual_owned_length` | exact owner-complement partition `|Residual|+|Owned|=|Full|` | `PROVED` |
| `SE2Certificate` | genuine selected-support projection for distinct slopes | finite interface |
| `se2_support_injection` | distinct slopes are bounded by selected noncommon supports | `PROVED` |
| `C9ProfileData.rowSharpMaxFiber` | literal supplied C9 field `fullPrefixFiber.length <= compilerLoss * naturalScale` | hypothesis, not proved |
| `C9ProfileData.support_not_earlier` | every selected slope support survives the earlier-owner deletion | `PROVED` |
| `C9ProfileData.slopes_paid` | exact chain `(SE2) -> residual -> full -> supplied field` | `PROVED` |
| `residual_plus_ownerFloor_le_budget` | an owned lower floor inside a full prefix fiber must be refunded from the full-prefix budget | `PROVED` |
| `m31_arithmetic_check` | exact downstream arithmetic from the integrated `6,796,405` fixed-remainder floor | `PROVED` |
| `m31_full_bound_fails_of_falsifier` | `Owned>=6,796,405` and `Residual>=3,184,406` imply `Full>9,980,810` | `PROVED` implication |
| `toy_check` | executable owner-complement plus genuine-`SE2` regression | `PROVED` |

The integrated fixed-remainder source supplies

```text
ceil(binomial(1023,544) / (2^31-1)^32) = 6,796,405.
```

The companion Python-stdlib verifier independently replays that ceiling. Lean
treats the integrated floor value as the certified input and kernel-checks the
subsequent row-budget, refund, and falsifier arithmetic.

## v3 source labels

| Source label | Correspondence |
|---|---|
| `def:primitive-q` | image-normalized primitive max-fiber target |
| `lem:logmoment-q` | any moment route must imply the literal max-fiber target |
| `lem:image-ambient-moment-conversion` | exact ambient/image normalization loss |
| `rem:flatness-certifies-image` | full-image guard before replacing the realized image |
| `def:q-row-atom` | first-match residual `P_Q(z)`, not the unpruned full prefix fiber |
| `prop:q-exact-target` | M31-list `B*=16,777,215`, average ceiling `1,993,678` |
| `prop:q-moment-order-floor` | residual mass must be carried in a finite moment proof |
| `eq:mca-final-ledger` | earlier-owner and Q payments are summed |
| `thm:exact-completion-certificate` | no one cell may independently consume the row budget |
| `prob:row-sharp-q` | remaining literal pruned-row obligation |

The exact integer denominator conventions are those of
`experimental/rs_mca_thresholds.tex`, labels `eq:intro-normalized-mca` and
`eq:intro-asymptotic-threshold`. The packet keeps `q_gen`, `q_line`, `q_chal`,
and `q_list` separate.

## Build contract

The package is rooted at `experimental/lean/sidon_effective_image/` and imports
only the Lean `Std` root. The fork draft-PR workflow on Lean `v4.31.0` is the
authoritative build; no local Lean build is claimed.

```text
sorry declarations: 0
admit declarations: 0
custom axiom declarations: 0
native-evaluation proof steps: 0
Mathlib imports: 0
external packages: 0
```

Every theorem-facing declaration ends in the module's `#print axioms` census.
Green compilation certifies only the finite Lean statements above; the audit
note separately records the semantic hypotheses and nonclaims.
