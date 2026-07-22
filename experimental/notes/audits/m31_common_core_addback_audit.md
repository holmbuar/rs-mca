# Audit: M31 common-core loss-one add-back

```yaml
workboard_item: M1
row: Mersenne-31 list, auxiliary analytic stress row at 2^-100
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: Every padded-frame common-core branch has exact factor-one puncturing/add-back, unchanged canonical selectors, and unchanged source-key/refund/signed-credit ledger.
architecture: GRANDE_FINALE_V4_EXACT_COMPLETION / M31_CANONICAL_RANK46_SOURCE_KEY_COMPILER
partition_digest: NOT_YET_ASSIGNED_TO_ACTIVE_GLOBAL_FIRST_MATCH_PARTITION
atom_or_cell: UNPAID_COMMON_CORE_ADD_BACK
quantifier: Every marked rank-46 source key and every declared common canonical locator core satisfying the exact theorem hypotheses.
projection_and_unit: Distinct RS codewords and distinct source-key ledger entries.
claimed_bound: c<=62295, n-c>=2034857, R-c>=918834, add_back_factor=1.
status: PROVED
impact: ARCHITECTURE_BRIDGE
falsifier: Selected/core intersection, c>62295, n-c<K, failure of source-key uniqueness, or any metadata-changing compiler.
replay: certificate verifier plus fork draft-PR Lean 4.31.0 build.
```

**Date:** 2026-07-21  
**Lane:** `gptpro/m31-common-core-addback`  
**Acceptance gate:** **criterion 3 — named terminal kill**  
**Terminal killed:** `UNPAID_COMMON_CORE_ADD_BACK`  
**Global row status:** open

## 1. Audit scope

This audit compares the theorem packet with the exact terminal grammar recovered
from:

- `experimental/notes/audits/m31_padding_bridge_audit.md` at upstream PR #1014;
- `experimental/notes/audits/m31_masked_diagonal_saturation.md` at upstream PR
  #1025; and
- the integrated source-key compiler
  `experimental/notes/thresholds/m31_canonical_popov_rank46_compiler.md`.

The packet is deliberately narrower than the open locator--numerator/owner
problem. It proves that common-core shortening and restoration have
multiplicity one at the exact deployed constants. It does not provide the
payment on the shortened component.

## 2. Base, source pins, and blob-SHA audit

The branch was created from the exact current fork head:

| repository object | SHA |
|---|---|
| `holmbuar/rs-mca:main` base | `4e5f0b77c98f075ea7c8822cd4859847a232bc2a` |
| integrated upstream `przchojecki/rs-mca:main` | `a3017697ad1594521d2779fe1d83bccd45d4c06e` |
| #1014 padding-audit head | `c7cbcf1cff1180b4aac0862ae3c3e665f6b29b21` |
| #1025 masked-saturation head | `626c61a95b0836e84655762ef4c90ca002da986b` |
| #1022 overlap-audit head, not imported or assumed | `0b39b40644e04a60e0953b7e8f6cfe2816a04b59` |

Every directly imported integrated Lean API is byte-identical on fork and
upstream main:

| imported API | fork blob | upstream blob | verdict |
|---|---|---|---|
| `experimental/lean/asymptotic_spine/AsymptoticSpine/FirstMatch.lean` | `44592371660c453c1f8522abb9c0f9364e4dd43d` | `44592371660c453c1f8522abb9c0f9364e4dd43d` | `BYTE_IDENTICAL` |
| `experimental/lean/m31_q_rooted_shell/M31QRootedShell/Deployed.lean` | `7e21ff098567d26aba7330fbb2722d5cb952fb09` | `7e21ff098567d26aba7330fbb2722d5cb952fb09` | `BYTE_IDENTICAL` |

Source-note blobs used to recover the terminal and padded-frame contract:

| source | blob SHA | role |
|---|---|---|
| integrated `m31_canonical_popov_rank46_compiler.md` | `11a1882d88ff8a3f725e61c0ce427cdaaa716fe9` | source-key ledger, Pluecker/common-core branch, terminal grammar |
| #1014 `m31_padding_bridge_audit.md` | `85ec62a4594e292456e6e7acf26394c73e2af34c` | exact padding bridge and successor separation |
| #1025 `m31_masked_diagonal_saturation.md` | `cbb63ec62af7931b3fdb868f8d3745c8822edb09` | padded frame `20765/41530/62295`, source metadata preservation |
| #1022 `m31_direct_padded_forney_frame_route_cut.md` | `4e2652b5486e1f8d06b239142951cc7a6610451c` | overlap boundary and sharper surviving owner/refund terminal only |

No declaration or file from `M31C9RowSharp`, `HalfSliceFalsifier`, #1014,
#1022, #1025, or any other open PR is imported. The #1025 structures are
restated locally with the same field order and definitions.

## 3. Source-label map

| packet object | proof/source node |
|---|---|
| marked source-key ledger and signed crossing | `m31_canonical_popov_rank46_compiler.md`, equations (5.4)--(5.8) |
| padded rank-three bound | `m31_masked_diagonal_saturation.md`, equations (5.3)--(5.4) |
| source metadata preservation | `m31_masked_diagonal_saturation.md`, Section 6 |
| old separated terminal | `m31_masked_diagonal_saturation.md`, Section 9, `UNPAID_COMMON_CORE_ADD_BACK` |
| diagonal padding semantics | `m31_padding_bridge_audit.md`, Theorem 2.1 and successor contract |
| common core divides an old-anchor minor | `m31_canonical_popov_rank46_compiler.md`, Lemma 6.1 / Corollary 6.2 |
| selector-stability theorem | companion threshold note, Lemma 3.1 |
| exact RS list bijection | companion threshold note, Theorem 4.1 |
| no-double-counting compiler | integrated `AsymptoticSpine.FirstMatch.firstMatch_le_sum_cellSizes` |
| exact row constants | integrated `M31QRootedShell.Deployed` and the four-row compiler M31-list row |
| sharper surviving terminal | #1022 overlap note, equation (5.10), not a dependency |

## 4. Exact source theorem audit

The threshold theorem states every load-bearing hypothesis:

1. an ordered distinct evaluation domain;
2. a common canonical locator core `C`;
3. disjointness of `C` from every selected first-`a` agreement set in the
   component;
4. `|D\C|>=K`; and
5. the padded-frame bound `|C|<=62,295` for the deployed specialization.

The proof has two directions:

- full to shortened uses the unchanged first-`a` selector;
- shortened to full uses monotonicity of agreements under adding coordinates.

It then invokes only the elementary RS injectivity fact that a nonzero
polynomial of degree `<K` cannot vanish on `K` distinct retained points.
Therefore the theorem proves exact equality of polynomial lists and exact
bijection of evaluation codewords. It does not assume a bound on the
shortened list and does not smuggle in an owner/refund.

## 5. Exact PROVED declaration table

Namespace: `SidonEffectiveImage.M31CommonCoreAddBack`.

| declaration | exact statement/role |
|---|---|
| `filter_comm` | two Boolean list filters commute |
| `take_filter_eq_take_of_prefix_kept` | deleting only entries outside a prefix leaves that prefix unchanged |
| `selected_deleteCore_eq` | first-`a` selector is unchanged when the core avoids it |
| `map_eq_of_pointwise` | pointwise equality compiles to ordered selector-vector equality |
| `core_degree_le_cap` | core degree is at most `62,295` from the local frame premise |
| `selector_preserved` | one column's canonical selector is unchanged |
| `selector_vector_preserved` | the complete ordered selector vector is unchanged |
| `RestrictionEquiv.injective` | the proved RS restriction equivalence is injective |
| `shortenedComponent_nodup` | distinct full codewords remain distinct after restriction |
| `mem_shortenedComponent_iff` | shortened membership is exactly membership after add-back |
| `shortenedComponent_length_exact` | component cardinality is unchanged exactly |
| `integrated_constant_alignment` | imported `listM`, `w`, and `Bstar` equal `981129`, `67447`, and `16777215` |
| `deployed_parameter_identities` | exact `n,K,a,R,w`, margin, and worst-case shortened constants |
| `signed_occupancy_crossing` | `16517335+259881=16777216=B*+1` |
| `shortened_length_floor` | every allowed core leaves length at least `2,034,857` |
| `shortened_dimension_gate` | every retained domain has at least `K` points |
| `shortened_agreement_gate` | agreement `a` remains feasible |
| `shortened_radius_exact` | shortened radius is exactly `981129-|C|` |
| `shortened_radius_floor` | every shortened radius is at least `918,834` |
| `common_core_addback_exact` | source metadata is pointwise identical after the compiler |
| `source_key_ids_nodup_preserved` | duplicate-free source IDs remain duplicate-free |
| `marked_source_key_floor_preserved` | the `259,881` key floor is unchanged |
| `signed_credit_sum_preserved` | aggregate signed occupancy credits are unchanged |
| `sourceIdCells_sum_length` | singleton source-ID cells have exact total size equal to the source-key list length |
| `firstMatch_addback_le_source_keys` | singleton source-key cells cannot charge more than the source-key list length |
| `maximal_core_regression` | exact worst-case finite gate at core degree `62,295` |

The module ends with `#print axioms` for every load-bearing declaration in this
table.

## 6. Enumeration and certificate audit

The canonical JSON certificate enumerates every integer core degree

```text
c=0,1,...,62,295
```

and checks:

- `n'=n-c` and `R'=R-c`;
- `n'>=a>K`;
- `n'>=K` and retained evaluation injectivity gate;
- `a-K=67,447` unchanged;
- `(n'-K+1)-R'=67,448` unchanged;
- worst-case `n'=2,034,857`, `R'=918,834`;
- padded-frame margin `5,152`;
- exact signed crossing and allowance; and
- imported/source blob pins and forbidden-import/static-source guards.

The verifier is stdlib-only, integer-only, and has hostile mutation tests. No
floating point decides a gate.

## 7. Lean/source proof boundary

The companion note proves the field/polynomial theorem. Lean checks:

- the ordered selector lemma without a field axiom;
- the two-sided finite add-back compiler from the proved restriction equivalence;
- all deployed integer gates;
- metadata/source-key/refund/signed-credit preservation; and
- integrated first-match no-double-counting.

Lean deliberately does not introduce a polynomial-ring library or restate an
unproved global row theorem. The explicit `RestrictionEquiv` value at an
application is supplied by Theorem 4.1, not by a custom axiom.

## 8. Validation record

```text
Lean toolchain: v4.31.0
stdlib only: yes
local Lean build: NOT RUN
fork draft PR: holmbuar/rs-mca#93
validated Lean-source head: 5ac70dd54d034554e50649a5d33c5a2a78d33d9f
workflow: Lean build — PR #93, run 29855624079 (run number 197)
package job: 88719127466, experimental/lean/sidon_effective_image
build-log artifact: 8505156641, lean-build-log-0
compilation result: SUCCESS, 10 jobs
```

The build executed both

```text
lake build SidonEffectiveImage SidonEffectiveImage.M31CommonCoreAddBack
lake build
```

and completed successfully. The only diagnostic was the nonfatal linter
suggestion to replace one `simpa` with `simp`; there were no elaboration or
kernel errors.

Final static and kernel census:

```text
sorry: 0
admit: 0
sorryAx: 0
custom axiom declarations: 0
unsafe declarations: 0
native_decide: 0
Mathlib imports: 0
```

The printed declarations use only standard Lean principles:

- `propext` on list/filter and proposition-normalization proofs;
- `Quot.sound` where the integrated equality/list machinery uses quotient
  soundness; and
- no axioms at all for `RestrictionEquiv.injective`,
  `integrated_constant_alignment`, `deployed_parameter_identities`,
  `signed_occupancy_crossing`, and `maximal_core_regression`.

No declaration depends on `sorryAx`, `Classical.choice`, or a custom axiom. The
audit-record successor changes no Lean source; its fork-PR rerun is the final
branch-readiness gate.

## 9. Acceptance criterion and impact

**Criterion 3 is met.** The theorem removes the named add-back terminal with
an exact factor-one statement. It does not move a deployed numerical atom, so
criterion 1 is not claimed.

The exact terminal transition is

```text
UNPAID_COMMON_CORE_ADD_BACK
  -> PROVED_COMMON_CORE_LOSS_ONE_ADDBACK.
```

The sharper current residual remains

```text
UNPAID_CANONICAL_LOCATOR_NUMERATOR_ESCAPE_OWNER_REFUND.
```

## 10. Explicit nonclaims

- No row-sharp Q.
- No list-interior coverage.
- No adjacent-row closure.
- No M31 list upper bound, safe endpoint, or ledger atom.
- No rank-two/coloop theorem.
- No shortened-component payment or semantic owner/refund.
- No claim that locator-only empty core or a low minor pays the row.
- No common-root deletion from received-line/numerator semantics.
- No MCA slope or ray compiler.
- No active global partition digest or row-wide first-match coverage.
- No stable-paper theorem, official score, or prize claim.

FIXED
