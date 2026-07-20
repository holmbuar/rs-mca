# Exact F97 C8 two-cell closed-ledger producer

## Status

`PROVED-SPECIAL / EXACT FINITE FIRST-MATCH PRODUCER / FORMALIZATION / AUDIT`

**Terminal verdict:** `FIXED` for the pinned `F_97 / mu_16` first-interior
subincidence; `OPEN GAP` for arbitrary first-interior modular-locator fibres and
row-wide `(UNIF)`.

**Lean module:**

- `AsymptoticSpine.C8F97TwoCellFirstMatch`

**Source certificate:**

- `experimental/notes/thresholds/bc_first_interior_f97_two_cell_certificate.md`

**General residual context:**

- `experimental/notes/thresholds/bc_first_interior_general_line_modular_fibers.md`
- `experimental/notes/thresholds/bc_first_interior_modular_subset_product.md`

## Exact source object

The pinned received line is over

```text
F = F_97,          D = mu_16,
(K,m,w,d1,omega) = (5,7,2,4,9).
```

After the source certificate performs exact support enumeration, line-ray
deduplication, common-support exclusion, and cyclic-periodicity exclusion, the
retained first-interior incidence has four rooted witnesses:

```text
z0   slope 0,
z1   slope 1,
z2a  slope 2,
z2b  slope 2.
```

Two fixed-domain-root common-GCD cells cover all four witnesses:

```text
A = {z0,z1,z2a},       G_A = X-D_15,
B = {z0,z1,z2b},       G_B = (X-D_10)(X-D_13).
```

After division by the common GCD, each cell spans a projective plane.  The
source verifier enumerates all `9507` projective points of each plane and,
independently, every split divisor on the residual domain.  Each plane contains
exactly the three stated locators.

The witness cover is therefore literal, not inferred from selected generators.

## Slope-level first match

Both cells have the same raw slope projection:

```text
pi(A) = {0,1,2},
pi(B) = {0,1,2}.
```

Thus raw per-chart summation gives

```text
|pi(A)| + |pi(B)| = 3 + 3 = 6.
```

This is not the MCA contribution.  Ordering `A` before `B` gives

```text
Z_A^o = {0,1,2},
Z_B^o = pi(B) \ Z_A^o = empty,
|Z_A^o| + |Z_B^o| = 3.
```

The later witness `z2b` is not lost: its slope `2` was already paid by the first
cell through `z2a`, and first-match excision removes all later witnesses above
that slope.

This exact line is therefore a concrete regression against either of the
following invalid compilers:

```text
sum raw chart slope images,
sum per-chart caps without slope-level deletion.
```

The failure is inside one received line, before any outer line supremum.  The
correct quantity remains

```text
sup_line sum_profile assignedSlopeBudget(line,profile).
```

## Rooted chain

```text
raw line-ray witness z0,z1,z2a,z2b
  -> exact common-GCD cell A or B
  -> complete residual projective-plane split-locator census
  -> raw cell slope image {0,1,2}
  -> ordered slope-level first match
  -> assigned images {0,1,2}, empty
  -> arbitrary earlier C1--C7 slope deletion
  -> one nonempty C8 ProfilePayment at natural scale 1
  -> append to the earlier ClosedLineLedger
  -> exact line-local budget and natural-scale telescopes.
```

No support count, pair moment, max-fibre bound, or unrelated fixed-chart
estimate is inserted as the final payment.  The source has already computed the
actual distinct-slope image of the witness-exhaustive cells; the Lean adapter
installs that image.

## Natural-scale direct payment

After all earlier owners have been deleted, the assigned F97 image is a subset
of `{0,1,2}`.  Hence

```text
|assigned slopes| <= 3.
```

The exact retained incidence is one realized semantic profile at this source
scale.  The adapter uses

```lean
ProfilePayment.ofDirect .c8 assignedSlopes 1 3
```

and installs no profile if the assigned image is empty.  Thus

```text
naturalTotal <= 1,
budgetTotal <= 3.
```

The direct adapter's residual, Sidon, and ray stages are identities.  No generic
balanced-core ray theorem is fabricated.

## Lean statement map

### Source witness and chart interface

- `f97C8Witnesses` names the four rooted source witnesses.
- `f97C8Slope` records the exact final slopes.
- `f97C8WitnessCells_cover` proves witness-exhaustive two-cell coverage.
- `f97C8CellSlopeImages_exact` proves both raw chart images are `[0,1,2]`.
- `f97C8WitnessSlopeImage_exact` proves the complete witness slope image is
  `[0,1,2]`.

### First-match regression

- `f97C8FirstMatchSlopeLeaves` proves the assigned images are
  `[[0,1,2],[]]`.
- `f97C8RawChartSlopeTotal` proves the invalid raw chart sum is `6`.
- `f97C8FirstMatchSlopeTotal` proves the correct sum is `3`.
- `f97C8LaterWitnessSlopeAlreadyPaid` records the later slope-2 witness as
  already covered.

### Closed-ledger producer

- `f97C8AssignedSlopes` performs arbitrary earlier C1--C7 deletion.
- `f97C8AssignedSlope_has_witness` roots every survivor in the exact source
  catalogue.
- `f97C8Profile`, `f97C8Line`, and `f97C8Ledger` populate
  `UniformClosedLedger`.
- `f97C8Ledger_compiles` gives the three-slope local numerator bound.
- `f97C8ExtendLine` appends the exact source profile to an earlier closed line.
- `f97C8ExtendLine_badCount`, `f97C8ExtendLine_budgetTotal`, and
  `f97C8ExtendLine_naturalTotal` prove exact line-local telescopes.

The extension fixture lets an earlier C1 cell own slope `0`; only slopes `1,2`
are appended.  The combined line has three covered slopes, two realized
profiles, budget total six, and natural total two.

## Relation to the general first-interior residual

The general first-interior chart has the exact modular-locator normal form

```text
MLFib_B(W1,N1,W2,N2,gamma,Lambda_D,K,m).
```

On root-free nonconstant-`W1` charts this is a mixed fixed-cardinality subset
product in

```text
U_h x (F[X]/W1)^x,
```

not ordinary Q.  Current source results give exact ranks, Fourier reduction,
and exchange rigidity but no row-sharp mixed-character theorem or aggregate
first-match slope compiler.

The F97 line does not solve that general residual.  It proves that one explicit
rank-two pre-first-match candidate is absorbed by two common-GCD cells and that
those cells must be combined by slope-level first match rather than independent
chart summation.

## Nonclaims

- No arbitrary-line first-interior atlas is constructed.
- No theorem says every rank-two or modular-locator candidate has a common
  `D`-root decomposition.
- No tangent, quotient, extension, or complete common-GCD classifier is proved.
- No deployed-row bound, row-sharp mixed-character estimate, chart-count
  theorem, or higher-dimensional ray compiler is supplied.
- No global fixed-before-line C1--C9 atlas, actual row-wide `(UNIF)`, target
  comparison, row closure, adjacent certificate, or score movement is claimed.
- The stdlib-only adapter does not reprove the finite-field projective-plane
  enumerations; it formalizes the exact source witness/cell/slope boundary.

## Research consequence

The pinned F97 first-interior line is fully paid and should remain closed.  It
also fixes the correct interface for future deficiency-two work:

```text
cover rooted witnesses by actual cells,
project every cell to slopes,
perform slope-level first match inside the line,
then sum the assigned budgets.
```

The next open C8 target is the root-free nonconstant-`W1` modular-locator
residual on arbitrary lines, not another raw projective-plane census.
