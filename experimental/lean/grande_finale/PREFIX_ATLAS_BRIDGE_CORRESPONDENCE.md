# Locator-Prefix Atlas Bridge Correspondence

Status: **PROVED** for concrete locator-prefix support coverage, exact
support-family and Reed--Solomon MCA bad-slope unions, typed cellwise-budget
summation, and the exact fixed-row outer-line lift to the full
Reed--Solomon `B_MCA` numerator.

Sources:

- `experimental/lean/asymptotic_spine/AsymptoticSpine/PrefixAtlas.lean`, the
  generic total-key first-match partition;
- `experimental/lean/grande_finale/GrandeFinale/PrefixPigeonhole.lean`, the
  finite-field locator coefficient key and its fibres;
- `experimental/lean/grande_finale/GrandeFinale/SyndromeLine.lean`, the actual
  support-family MCA/syndrome-line bad-slope set; and
- `experimental/lean/grande_finale/GrandeFinale/RSExactSupportUpper.lean`, the
  exact-support reduction for injectively evaluated Reed--Solomon codes.

## Statement map

| Interface statement | Lean declaration |
| --- | --- |
| Locator coefficient-prefix key of a supplied support | `GrandeFinale.PrefixAtlasBridge.supportPrefixKey` |
| Concrete prefix cell inside a supplied support family | `GrandeFinale.PrefixAtlasBridge.supportPrefixCell` |
| Membership in a concrete prefix cell | `GrandeFinale.PrefixAtlasBridge.mem_supportPrefixCell_iff` |
| Concrete prefix cells cover exactly the supplied support family | `GrandeFinale.PrefixAtlasBridge.supportPrefixCells_cover` |
| Ambient key-space cardinality is `|F|^(m-K)` | `GrandeFinale.PrefixAtlasBridge.supportPrefixKey_space_card` |
| Coefficient fibres cover all `m`-subsets of the evaluation set | `GrandeFinale.PrefixAtlasBridge.coefficientFiber_biUnion_eq_powersetCard` |
| Bad slopes of all `m`-subsets equal the union of concrete coefficient-fibre cells | `GrandeFinale.PrefixAtlasBridge.badSlopeSetOnPowersetCard_eq_prefixCells_biUnion` |
| Corresponding unconditional union bound | `GrandeFinale.PrefixAtlasBridge.badSlopeSetOnPowersetCard_card_le_sum_prefixCells` |
| Bad slopes of an arbitrary supplied support family equal the union over its prefix cells | `GrandeFinale.PrefixAtlasBridge.badSlopeSetOnSupportFamily_eq_prefixCells_biUnion` |
| Corresponding unconditional union bound | `GrandeFinale.PrefixAtlasBridge.badSlopeSetOnSupportFamily_card_le_sum_prefixCells` |
| Explicit cellwise budgets `U(z)` sum to a whole-family budget | `GrandeFinale.PrefixAtlasBridge.badSlopeSetOnSupportFamily_card_le_sum_prefixBudgets` |
| Locator-prefix cell for the exact-`a` Reed--Solomon support family | `GrandeFinale.PrefixAtlasBridge.rsPrefixBadSlopeCell` |
| Fixed-line threshold-`a` RS bad slopes equal the union of locator-prefix cells | `GrandeFinale.PrefixAtlasBridge.rsMcaBadSlopes_eq_prefixCells_biUnion` |
| Corresponding fixed-line unconditional union bound | `GrandeFinale.PrefixAtlasBridge.rsMcaBadSlopes_card_le_sum_prefixCells` |
| Fixed-line cellwise budgets sum to an RS bad-slope budget | `GrandeFinale.PrefixAtlasBridge.rsMcaBadSlopes_card_le_sum_prefixBudgets` |
| Line-dependent cell budgets with a uniform per-line total bound the full RS numerator | `GrandeFinale.PrefixAtlasBridge.B_MCA_rsEval_le_of_linewise_prefixBudgets` |
| A single line-independent family `U(z)` also bounds the full RS numerator | `GrandeFinale.PrefixAtlasBridge.B_MCA_rsEval_le_sum_prefixBudgets` |

## Statement comparison

`AsymptoticSpine.PrefixAtlas.prefixFibreAtlas_total` proves the abstract
coverage fact: the fibres of a total key map give duplicate-free first-match
coverage of every supplied witness. `PrefixAtlasBridge` replaces the abstract
key by

```text
S |-> coefficientPrefix K m (locator (image point S))
```

and replaces an abstract witness list by a finite family of agreement supports.
On the full evaluation-set chart it uses
`PrefixPigeonhole.coefficientFiber A K m z`; on an arbitrary supplied family it
filters by the same key. The consumer is not an abstract cell count but
`SyndromeLine.badSlopeSetOnSupportFamily`, which deduplicates slopes witnessed
by multiple supports.

The exact union theorem is therefore the concrete bridge:

```text
badSlopeSet(supports)
  = union_z badSlopeSet(prefixCell(supports, z)).
```

The generic support-family theorem carries payment as an explicit hypothesis:

```text
(forall z, card (badSlopeSet (prefixCell z)) <= U z)
  -> card (badSlopeSet supports) <= sum_z U z.
```

This is the prefix-cell counting interface, not a construction of the budgets
or a semantic first-match classification.

The direct Reed--Solomon specialization first invokes
`RSExactSupportUpper.mcaBadSlopes_eq_exactSupportFamily`. For injective
evaluation, `k + R = |D|`, and `k + 1 <= a`, it identifies a fixed received
line's threshold-`a` MCA-bad slopes with the exact-`a` support family and
then partitions that family by locator prefixes. Taking `K := k + 1` gives
the source depth `a - k - 1`.

The exact full-numerator theorem allows line-dependent budgets
`U(u0,u1,z)`. It assumes each cell bound on each line and only requires a
uniform bound `B` on the resulting per-line sum. Its conclusion is
`B_MCA <= B`, with the quantifier order `sup_line sum_z U(line,z) <= B`.

The line-independent theorem is a valid stronger sufficient condition,
effectively bounding `sum_z sup_line cell(line,z)`. This can overpay
exponentially when different lines activate different cells. The
certificate checks the diagonal family with `2^b` lines and cells: every
per-line sum is one, while the sum of cellwise line maxima is `2^b`.

The linewise theorem is the exact fixed-row outer-line `B_MCA` interface. Neither
theorem constructs a cell budget or a catalogue classification, and neither
establishes one paid semantic catalogue uniformly along an asymptotic row;
that stronger ledger `(UNIF)` obligation remains open.

## Scope boundaries

The module proves support coverage, bad-slope union identities, and their
finite union bounds. It does not prove a semantic C1--C9 classification, a
subexponential count of realized profiles, any numerical `U(z)`, primitive
survival after C1--C8, or a Sidon payment. In particular, totality does not
turn the four residual cells C3/C7/C8/C9 into paid cells.

The arbitrary-domain definition accepts a map `point : D -> F`; injectivity
is not needed for its coverage/union statements because cells are cut out on
the original support family. The full `m`-subset theorem is stated directly
over `A : Finset F`, matching `PrefixPigeonhole.coefficientFiber`. The direct
RS specialization requires injective evaluation and `k + R = |D|` only to
invoke the exact-support reduction. Its full-numerator theorem additionally
requires a uniform bound on the line-dependent budget sum.
The parameter `K` remains generic and `a - K` is truncated natural-number
subtraction. In the intended specialization `K := k + 1`, `hka` ensures
`K <= a`; for `K > a` the theorem remains true but degenerates to the
single empty-function key and one global cell.

## Module placement

This is a leaf module. It imports `GrandeFinale.SyndromeLine`, and
`SyndromeLine.lean` imports the root module `GrandeFinale`. Consequently the
root `GrandeFinale.lean` cannot import `PrefixAtlasBridge` without creating an
import cycle. The bridge remains available through its fully qualified module
name and is checked directly.

## Verification

From `experimental/lean/grande_finale`:

```text
lake build GrandeFinale.PrefixAtlasBridge
```

The module prints the axioms of its exported coverage, union, fixed-line
budget, and full-numerator theorems. No proof placeholder or added axiom is
used.
