# Audit: M31 C9 full-prefix owner-refund floor

**Status:** `AUDIT / CONDITIONAL_ON_NAMED_INPUT`  
**Package:** `experimental/lean/sidon_effective_image/`  
**Validation head:** `PENDING_FINAL_HEAD`  
**Fork draft PR:** `holmbuar/rs-mca#73`

## 1. Scope

This audit checks one activity only: the exact owner-refund cost of using the
C9 producer's supplied **full-prefix** field after an earlier owner has already
consumed part of the Mersenne-31 list row budget.

It does not import the open-PR C9 module.  The stdlib-only Lean file restates the
load-bearing field literally,

```lean
fullPrefixFiber.length ≤ compilerLoss * naturalScale
```

and proves the owner-complement, genuine `(SE2)` projection, generic refund cut,
M31 arithmetic, and exact falsifier implication in a standalone namespace.

## 2. Result

The exact deployed arithmetic is:

```text
B*                         = 16,777,215
c=2048 earlier-owner floor =  6,796,405
remaining Q allocation     =  9,980,810
full-field residual cap     =  3,184,405
first falsifier residual    =  3,184,406
```

Therefore a key with at least `6,796,405` earlier-owned supports and at least
`3,184,406` exact residual supports falsifies the full-prefix field at the
remaining allocation `9,980,810`.

This is an exact implication, not an exhibited deployed RS key.  The semantic
co-location and residual lower bound remain the named input
`M31-C9-POST-C2048-COLOCATED-RESIDUAL-3184406`.

## 3. Exact PROVED declaration table

| Lean declaration | Exact statement audited | Status |
|---|---|---|
| `mem_residualOf_iff` | `x` is in the residual iff it is in the full prefix fiber and `earlierOwner x = none` | `PROVED` |
| `residual_owned_length` | canonical owner complement gives `|Residual|+|Owned|=|Full|` | `PROVED` |
| `se2_support_injection` | genuine selected-support sublist bounds distinct slopes | `PROVED` |
| `C9ProfileData.support_not_earlier` | every selected slope support has no earlier owner | `PROVED` |
| `C9ProfileData.slopes_paid` | `(SE2) -> residual -> full -> rowSharpMaxFiber` pays the slope list | `PROVED` |
| `residual_plus_ownerFloor_le_budget` | full bound plus an owned lower floor forces residual plus floor into the same budget | `PROVED` |
| `m31_arithmetic_check` | exact `q_gen`, `q_list`, row budget, imported `c=2048` floor value, residual cut, and falsifier arithmetic | `PROVED` |
| `m31_full_bound_fails_of_falsifier` | the two exact M31 cardinality hypotheses imply failure of `full.length <= 9,980,810` | `PROVED` |
| `toy_check` | executable exact owner-complement and genuine-SE2 regression | `PROVED` |

The finite M31 theorem proves only the implication from its two cardinality
hypotheses.  It does not prove those hypotheses for the deployed RS catalogue.

## 4. Source-label correspondence

| Source label/object | Packet declaration or section | Audit conclusion |
|---|---|---|
| `def:primitive-q` | normalization section in the threshold note | image average is `M_res/L_res`, not automatically `M_res/q_gen^w` |
| `lem:logmoment-q` | successor-route discussion | any moment route must imply the literal max-fiber target |
| `lem:image-ambient-moment-conversion` | normalization section | ambient/image conversion carries the exact image-collapse factor |
| `rem:flatness-certifies-image` | normalization guard | no full-image assumption is smuggled into MI/MA |
| `def:q-row-atom` | attacked inequality | v3 target is first-match residual `P_Q(z)` |
| `prop:q-exact-target` | M31 constants | `ceil(avg)=1,993,678`, `B*=16,777,215` |
| `prop:q-moment-order-floor` | nonclaim/normalization | residual mass must be carried explicitly |
| `eq:mca-final-ledger` | owner-refund cut | earlier cells and Q are summed, not each assigned the whole budget |
| `thm:exact-completion-certificate` | owner-refund cut | no one term may independently consume the row margin |
| `prob:row-sharp-q` | named remaining obligation | literal pruned row allocation remains open |
| `eq:intro-normalized-mca` | denominator table | MCA/challenge normalization is distinct from the support prefix denominator |
| `eq:intro-asymptotic-threshold` | row budget | exact integer target convention |

## 5. C9 statement correspondence

The open-PR source reference has blob
`5318f56130a98c8224b3baa977108e213127517f` and states:

```lean
rowSharpMaxFiber :
  (fullPrefixFiber leaf syndromeKey).length ≤
    compilerLoss * naturalScale
```

The standalone structure `SidonEffectiveImage.C9ProfileData` states the same
cardinality field:

```lean
rowSharpMaxFiber :
  fullPrefixFiber.length ≤ compilerLoss * naturalScale
```

The adapter chain is the same finite monotonicity chain:

```text
slopes <= selected supports <= residual prefix fiber
       <= full prefix fiber <= compilerLoss * naturalScale.
```

No open-PR module is imported.  Once that producer integrates, the arithmetic
owner-refund theorem can be applied outside the producer to any concrete
`ProfileData` after exposing the earlier-owned count at the selected key.

## 6. Blob-SHA audit

The Lean package imports only `Std`; it imports no repository module.  The
following source/API files were read from both current fork `main`
`b410c7ee14488bb751c5a89df10cb5b0323e3669` and upstream `main`
`18cfc199d4612f5dfc01bf6c0155a65a1eaa3832`.  Matching blob SHAs prove byte
identity at the audit anchors.

| Path | Fork-main blob | Upstream-main blob | Result |
|---|---|---|---|
| `experimental/grande_finale.tex` | `759678e30639972e4f64b438d3d6ba76ff3ddf8f` | `759678e30639972e4f64b438d3d6ba76ff3ddf8f` | identical |
| `experimental/rs_mca_thresholds.tex` | `01302a797c502a05ed0b11ba949b8756e0aa2b22` | `01302a797c502a05ed0b11ba949b8756e0aa2b22` | identical |
| `experimental/lean/asymptotic_spine/AsymptoticSpine/PrimitiveBoolean.lean` | `777273e4377c31c815062769803622c6226988d3` | `777273e4377c31c815062769803622c6226988d3` | identical |
| `experimental/lean/asymptotic_spine/AsymptoticSpine/EffectiveClosure.lean` | `9fb097e23d00e2f3ee3afeda021b86ba4192d2a4` | `9fb097e23d00e2f3ee3afeda021b86ba4192d2a4` | identical |
| `experimental/lean/asymptotic_spine/AsymptoticSpine/UniformClosedLedger.lean` | `deda34063f4629e245c37ba03e3cb3ab70502570` | `deda34063f4629e245c37ba03e3cb3ab70502570` | identical |
| `experimental/notes/thresholds/20260709_m31_chebyshev_fixed_remainder_floor/cap25_v13_m31_chebyshev_fixed_remainder_floor.md` | `f25d9f5b7c6638ab5c7ef36a887b670de1f846c6` | `f25d9f5b7c6638ab5c7ef36a887b670de1f846c6` | identical |

The open-PR C9 blob is a **statement reference only** and is excluded from the
byte-identical imported-API table because it is not on upstream main and is not
an import dependency.

## 7. Certificate and replay audit

Certificate:

```text
experimental/data/certificates/m31-c9-full-prefix-owner-refund-floor/
  m31_c9_full_prefix_owner_refund_floor.json
```

Replay:

```text
python experimental/scripts/verify_m31_c9_full_prefix_owner_refund_floor.py
python experimental/scripts/verify_m31_c9_full_prefix_owner_refund_floor.py \
  --tamper-selftest
```

The verifier recomputes the quartic row budget and the exact
`ceil(binomial(1023,544)/q_gen^32)` floor with Python's standard library.  The
million-bit full-slice average `1,993,678` is treated as a source value from
`prop:q-exact-target`; it is not rederived by this compact replay.  Python is
not the proof authority.

## 8. Lean build and axiom census

Build contract:

```text
Lean toolchain: v4.31.0
imports: Std only
Mathlib imports: 0
external packages: 0
sorry: 0
admit: 0
sorryAx: 0
custom axiom declarations: 0
unsafe declarations: 0
native_decide: 0
```

Final fork-CI result:

```text
PENDING_FINAL_CI_RESULT
```

Printed axiom dependencies from the final build log:

```text
PENDING_FINAL_AXIOM_OUTPUT
```

Green compilation will certify the Lean declarations only.  The source audit
above separately limits what those declarations mean.

## 9. Explicit nonclaims

This packet does not prove:

- an actual deployed M31 prefix key satisfying the falsifier;
- the final C1--C8 `earlierOwner` semantics or co-location theorem;
- the #1020 row-sharp full-prefix field at any deployed key;
- the residual bound `|P_Q(z)| <= 3,184,405` or `<= 9,980,810`;
- `def:q-row-atom`, `prop:q-exact-target`, or `prob:row-sharp-q` as upper theorems;
- any Sidon, Fourier, MI, MA, RC, add-back, `UNIF`, target comparison, or adjacent-row closure;
- equality or substitution among `q_gen`, `q_line`, `q_chal`, and `q_list`.

## 10. Files in the packet

- `experimental/notes/thresholds/m31_c9_full_prefix_owner_refund_floor.md`
- `experimental/notes/audits/m31_c9_full_prefix_owner_refund_audit.md`
- `experimental/data/certificates/m31-c9-full-prefix-owner-refund-floor/m31_c9_full_prefix_owner_refund_floor.json`
- `experimental/scripts/verify_m31_c9_full_prefix_owner_refund_floor.py`
- `experimental/lean/sidon_effective_image/SidonEffectiveImage.lean`
- `experimental/lean/sidon_effective_image/SOURCE_CORRESPONDENCE.md`
- `experimental/agents-log-entry-gptpro-sidon-effective-image-mi-ma.md`
