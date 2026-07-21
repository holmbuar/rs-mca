# Audit of the M31 padded rank-two coloop elimination

```yaml
workboard_item: M1
row: Mersenne-31 list analytic stress row
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: >-
  Every intrinsic padded three-row frame attached to a marked rank-46 source
  key has a full-support locator dependence with nonzero distinguished
  coefficient, so the distinguished column is not a coloop and
  UNPAID_RANK2_COLOOP is empty.
architecture: M31_CANONICAL_PADDED_RANK46
partition_digest: >-
  ZERO_SYNDROME -> NEAR_RATIONAL_SINGLETON -> NAMED_EXISTING_OWNER ->
  CANONICAL_MASKED_SPLIT_PENCIL -> PADDED_FRAME ->
  {COMMON_CORE_ADD_BACK, RANK2_COLOOP}
atom_or_cell: UNPAID_RANK2_COLOOP
quantifier: every marked rank-46 source key and every intrinsic padded frame satisfying the source relation
projection_and_unit: padded syzygy-column matroid; exact route exclusion
claimed_bound: zero surviving rank-two coloop configurations
status: PROVED
impact: ROUTE_CUT
falsifier: zero distinguished locator coefficient or failure of the common padded syzygy relation
replay: >-
  python3 experimental/scripts/verify_m31_rank2_coloop_elimination.py --check;
  python3 -O experimental/scripts/verify_m31_rank2_coloop_elimination.py --check;
  python3 experimental/scripts/verify_m31_rank2_coloop_elimination.py --tamper-selftest
```

## 1. Verdict

```text
FIXED
```

Acceptance gate criterion **3** is met: the precisely named terminal
`UNPAID_RANK2_COLOOP` is empty on every padded frame supplied to a marked
rank-46 source key.  The proof is the full-support padded-locator dependence,
not a proxy-family count, interface adapter, or numerical union bound.

## 2. Source pins and imported-API audit

Base branch and source state:

| Item | SHA |
|---|---|
| Fork `holmbuar/rs-mca:main` base | `4e5f0b77c98f075ea7c8822cd4859847a232bc2a` |
| Upstream `przchojecki/rs-mca:main` included by the fork base | `a3017697ad1594521d2779fe1d83bccd45d4c06e` |
| Integrated rank-46 compiler blob on fork main | `11a1882d88ff8a3f725e61c0ce427cdaaa716fe9` |
| Same compiler blob on upstream main | `11a1882d88ff8a3f725e61c0ce427cdaaa716fe9` |
| Padding-bridge audit head / blob | `c7cbcf1cff1180b4aac0862ae3c3e665f6b29b21` / `85ec62a4594e292456e6e7acf26394c73e2af34c` |
| Masked-saturation audit head / blob | `626c61a95b0836e84655762ef4c90ca002da986b` / `cbb63ec62af7931b3fdb868f8d3745c8822edb09` |

The new Lean module has this complete imported integrated-API table:

| Imported integrated API | Fork-main blob | Upstream-main blob | Result |
|---|---:|---:|---|
| `AsymptoticSpine.*` | — | — | **No import** |
| `M31QRootedShell.*` | — | — | **No import** |

The module imports only `Std`.  Therefore the set of imported repository APIs is
empty and byte-identity is vacuous; no open-PR module, including
`M31C9RowSharp` or `HalfSliceFalsifier`, is in the dependency graph.  The
package `lakefile.lean` has no `require`; its checked empty `lake-manifest.json`
is present only because the pinned fork `lean-action` requires a manifest during
configuration, before any build command runs.

## 3. Exact source-label map

| Source | Label or exact location | Use in this packet |
|---|---|---|
| `experimental/notes/thresholds/m31_canonical_popov_rank46_compiler.md` | Section 6, Lemma 6.1, Corollary 6.2, terminals (6.7) | Defines the three-row column matroid and the `UNPAID_RANK2_COLOOP` alternative. |
| Same source | (6.5) | Supplies the exact `20,765`, `41,530`, `62,295 < 67,447` padded-frame constants after the successor theorem. |
| `experimental/notes/audits/m31_padding_bridge_audit.md` | Theorem 2.1 and Sections 4, 6, 8 | Supplies the diagonal-saturation boundary and the `F_11` direct-transport counterpacket that must remain valid. |
| `experimental/notes/audits/m31_masked_diagonal_saturation.md` | (2.1), (5.3), (5.4), Sections 6--9 | Supplies an intrinsic padded rank-three frame pointwise on every marked key while retaining selectors, masks, owners, refunds, and signed credits. |
| `experimental/notes/thresholds/m31_rank2_coloop_elimination.md` | Theorem 2.1 and Corollaries 2.2--2.3 | Proves the full-support dependence, no-coloop theorem, and exact terminal elimination. |

## 4. Exact PROVED-declaration table

All declarations are in
`SidonEffectiveImage.M31RankTwoColoop`.

| Lean declaration | Exact proved statement | Source match | Axiom target |
|---|---|---|---|
| `deployedConstantsExact` | The marked-key floor and padded-frame bounds are exactly `259881`, `20765`, `41530`, `62295`, with `62295 < 67447`. | Source (5.8), (6.5), and masked-saturation (5.3). | none |
| `paddedLocatorGivesNonzeroExtraDependence` | Every stated padded frame admits the locator-coefficient column dependence and its distinguished coefficient is nonzero. | Threshold Theorem 2.1 / row-by-row syzygy identity. | none |
| `extraColumnIsNotColoop` | The dependence-characterized extra-column coloop predicate is false. | Threshold Corollary 2.2. | none |
| `rankTwoColoopTerminalIsEmpty` | The conjunction “old columns rank at most two and extra column is a coloop” is false. | Threshold Corollary 2.3; kills source terminal (6.7). | none |
| `everyMarkedFrameExcludesRankTwoColoop` | The same exclusion holds pointwise for every frame in any supplied marked-frame list. | Pointwise transfer to all source keys; no union loss. | none |

The Lean theorem deliberately proves a stronger statement than required:
`extraColumnIsNotColoop` does not use the old-rank-at-most-two hypothesis or the
numerical degree bounds.  It uses only the exact common syzygy relation and the
nonzero distinguished locator coefficient.  The unused source bounds remain in
the frame structure so the formal object is definitionally the deployed padded
frame rather than a weakened proxy.

## 5. Mathematical audit

For the three-row matrix `A`, the `r`-th syzygy equation is

```text
sum_i W'_i A_(r,i)=0.
```

Collecting the three equations by columns gives

```text
sum_i W'_i v_i=0.
```

The distinguished coefficient is the nonzero locator polynomial `W'_46`.
Hence the distinguished column appears with nonzero coefficient in a dependence
and is not a coloop.  Solving for it shows directly that it lies in the span of
the old columns, so deletion preserves rank.  There is no local-to-global jump:
the masked-saturation source supplies exactly this padded locator and these
padded syzygy rows to each marked key.

### `F_11` boundary condition

No statement contradicts the direct-transport counterpacket.  That packet says
a named low actual-error basis row may fail the coordinatewise divisibility
needed to transport through padding.  This packet neither names nor transports
that row.  It uses the intrinsic padded basis furnished after masked saturation
and its defining padded syzygy equation.  Direct transport can fail while the
intrinsic padded column relation above still holds.

### Load-bearing hypothesis

The nonzero distinguished coefficient is essential.  The certificate includes
the exact `F_2` falsifier obtained when it is dropped: old column `0`, extra
column `1`, and coefficient vector `(1,0)`.  This is a dependence with zero
extra coefficient, yet deleting the extra column lowers rank.  The source
locators are monic nonzero polynomials, so the falsifier is outside the theorem.

## 6. Certificate and enumeration audit

Files:

```text
experimental/data/certificates/m31-rank2-coloop-elimination/
  m31_rank2_coloop_elimination.json
experimental/scripts/verify_m31_rank2_coloop_elimination.py
```

The independent verifier:

1. checks the pinned base and source blob table;
2. checks the package has exactly one module, imports only `Std`, has no
   `require`, carries the canonical empty Lake manifest, and contains no
   `sorry`, `axiom`, `native_decide`, Mathlib, or
   forbidden open-PR import;
3. checks the source markers and exact constants;
4. exhausts the printed small finite-field matrix suites;
5. verifies every relation with nonzero distinguished coefficient preserves
   rank after deleting the extra column; and
6. rejects certificate/source mutations and confirms the zero-extra-coefficient
   falsifier.

The enumeration is a regression for the formal theorem, not the proof of the
deployed result.  The general proof is Theorem 2.1 and the Lean kernel theorem.

## 7. Validation record

The authoritative proof build ran on fork draft PR `#88` against
`holmbuar/rs-mca:main` at proof head
`0c11da80beacfbcb4d5ae0f6538c84c21df92307`.

| Validation item | Recorded result |
|---|---|
| Workflow run | `29853452863` (`Lean build — PR #88`, run number `178`) |
| Package job | `88711871996`, `experimental/lean/sidon_effective_image` |
| Lean toolchain | `leanprover/lean4:v4.31.0` |
| Explicit targets | `lake build SidonEffectiveImage SidonEffectiveImage.M31RankTwoColoop` |
| Explicit-target result | success |
| Default package target | success |
| Build-log artifact | `8504306481`, digest `sha256:beb6c73493d03dac9c5f32e29ab93ad9e54018686dc9e2fc262153bdb9eeb2ca` |
| Workflow conclusion | success |

The first setup attempt, run `29852581050`, exited before compilation because
the pinned `lean-action` requires `lake-manifest.json` even when the lakefile has
no dependencies.  The byte-identical canonical empty manifest from the already
green sibling package repaired that workflow precondition.  The next
source-bearing build exposed only stdlib portability errors (`Field` and unopened
big-sum notation); the final module restates zero/add/mul and the 45-term fold
explicitly and imports only `Std`.

### Printed axiom census

The successful artifact prints the following kernel results twice, once for the
explicit targets and once for the default package target:

| Declaration | `#print axioms` result |
|---|---|
| `paddedLocatorGivesNonzeroExtraDependence` | does not depend on any axioms |
| `extraColumnIsNotColoop` | does not depend on any axioms |
| `rankTwoColoopTerminalIsEmpty` | does not depend on any axioms |
| `everyMarkedFrameExcludesRankTwoColoop` | does not depend on any axioms |
| `deployedConstantsExact` | does not depend on any axioms |

Census: **zero `sorry`, zero custom axioms, zero reported theorem axioms, zero
`native_decide`**.  The independent verifier also passes under ordinary and
optimized Python, with 15 exhaustive suites, 26,294 matrices, 20,012
nonzero-extra relation checks, zero violations, and all four tamper mutations
rejected.

This audit-stamp update does not alter the Lean module, root, manifest,
certificate, or theorem statement.  The final PR head must replay the same
package check successfully before branch-ready status is declared.

## 8. Explicit nonclaims

- No `U_Q`, `U_list_int`, boundary, whole-ball, or completion atom is banked.
- The Mersenne-31 list inequality `B^list_C(1116023) <= 16777215` remains open.
- `UNPAID_COMMON_CORE_ADD_BACK` is not touched, weakened, or imported.
- No row-sharp Q, rooted-shell closure, list-interior coverage, residual add-back,
  or adjacent-row theorem is claimed.
- No forbidden center or surviving M31 configuration is constructed.
- No named actual-error basis is transported through padding.
- No stable-paper TeX, deployed radius, official score, or prize claim changes.
