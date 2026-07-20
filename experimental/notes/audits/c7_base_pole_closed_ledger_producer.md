# C7 base-pole constant-coefficient producer into the closed ledger

**Status:** `PROVED LOCAL ADAPTER / SOURCE-FACING FORMALIZATION / CONDITIONAL GLOBAL USE`

**Lean modules:**

- `AsymptoticSpine.C7OwnerRegression`
- `AsymptoticSpine.C7BasePoleProducer`
- `AsymptoticSpine.C7BasePoleWitnessProducer`
- `AsymptoticSpine.C7BasePoleLineExtension`

**Source theorem:**
`experimental/notes/thresholds/aperiodic_one_ray_saturation.md`

## Result

The base-pole constant-coefficient class now supplies a complete local producer
for the `UniformClosedLedger` interface.

For one received base-pole line and one fixed prefix value, the source theorem
partitions the actual exact-agreement witnesses by locator constant coefficient

```text
C_d = {S in Fib_w(z) : c_m(S) = d}.
```

Every nonempty `C_d` has final slope image exactly `{-d}`.  There are at most
`q - 1` realized nonzero constant coefficients.  The correct first-match C7
owner is not the untrimmed raw image.  Given the aggregate C1--C6 assigned slope
image `E_<7(r)` on the same received line, it is

```text
Z_C7^o(r) = {-d : C_d is nonempty} \ E_<7(r).
```

Each surviving slope is installed as a singleton direct payment at unit natural
scale.  If an earlier owner already paid the slope, that C7 cell is deleted and
is not installed as a realized profile.

The resulting line-local identities are

```text
C7 budgetTotal  = number of surviving C7 slopes,
C7 naturalTotal = number of surviving C7 slopes,
```

and therefore

```text
C7 budgetTotal <= number of raw constant-coefficient slopes <= q - 1.
```

When appended to an already-closed C1--C6 line, the formalization proves the
exact telescopes

```text
combined budgetTotal
  = earlier budgetTotal + number of surviving C7 slopes,

combined naturalTotal
  = earlier naturalTotal + number of surviving C7 slopes.
```

The flattened assigned-slope list remains duplicate-free, so the extension
preserves semantic first-match ownership.  The sum is formed inside the
received line; no `sum_profile sup_line` interchange occurs.

## Rooted chain

The source-facing structure `BasePoleC7WitnessClass` records precisely the data
proved by the base-pole theorem:

```text
raw witness identifier w
  -> constantCoeff(w) = d
  -> slope(w) = slopeOfCoeff(d)
  -> realized coefficient fibre C_d
  -> raw distinct slope slopeOfCoeff(d)
  -> delete aggregate C1--C6 slope image
  -> surviving singleton C7 ProfilePayment
  -> append to the earlier ClosedLineLedger.
```

For the mathematical source instance:

```text
constantCoeff(S) = c_m(S),
slopeOfCoeff(d)  = -d.
```

Negation is injective, so the realized coefficient list maps to a duplicate-free
raw slope list.  The source theorem supplies the `q - 1` realized-coefficient
bound.

## Lean statement map

### Raw witness atlas and slope law

`BasePoleC7WitnessClass.rawWitnessCells_total` proves that the canonical fibres
over realized constant coefficients are duplicate-free and witness-exhaustive,
with at most `qMinusOne` cells.

`BasePoleC7WitnessClass.slope_eq_of_mem_constantCoeffCell` proves that every
witness in one coefficient cell has its prescribed single slope.

`BasePoleC7WitnessClass.mem_rawSlopes_iff_mem_witnessSlopeImage` proves that the
constructed raw slope list is exactly the slope image of the raw witness
catalogue.

`BasePoleC7WitnessClass.assignedSlope_has_surviving_witness` roots every assigned
post-deletion C7 slope in an actual raw witness and records its exclusion from
the earlier slope image.

### Direct payment

`basePoleC7Profile` installs one surviving slope through

```lean
ProfilePayment.ofDirect .c7 [gamma] 1 1
```

so no residual/Sidon/ray theorem is fabricated.  The independent theorem being
used is the exact singleton final-slope image of `C_d`.  Unit natural scale is
the additive profile term in the image-normalized envelope.

`basePoleC7Line_budgetTotal` and `basePoleC7Line_naturalTotal` identify both
line-local sums with the survivor count.

`BasePoleC7WitnessClass.c7Line_budgetTotal_le_qMinusOne` and
`BasePoleC7WitnessClass.c7Line_naturalTotal_le_qMinusOne` apply the source-side
raw census.

### Composition after C1--C6

`BasePoleC7WitnessClass.extendLine` takes an existing
`ClosedLineLedger 1 profileCap`, uses its flattened assigned slopes as the exact
deletion set, and appends only the surviving C7 singleton profiles.

`earlier_append_assignedSlopes_nodup` proves disjointness from all earlier
assigned slopes.

`extendLine_budgetTotal` and `extendLine_naturalTotal` prove the exact line-local
payment telescopes.

`extendLine_budgetTotal_le_prior_add_qMinusOne` and
`extendLine_naturalTotal_le_prior_add_qMinusOne` bound the added C7 cost by the
source-side census.

The executable extension fixture starts with earlier C1/C2 slopes `100,102`,
raw C7 slopes `100,101,102,103`, and confirms that only `101,103` are appended;
the combined budget and natural total are both `4 = 2 + 2`.

## Correction to the earlier regression packet

The affine-Steiner regression remains valid and necessary:

```text
raw C7-style one-slope payment
  does not imply
nonempty C7 first-match ownership.
```

It forbids installing an untrimmed raw C7 cell after an earlier owner has already
paid the same slope.

However, full raw-cell survival

```text
Z_C7^o(r) = Z_C7_raw(r)
```

is stronger than necessary.  A correct producer may form and pay the literal
post-deletion subset

```text
Z_C7^o(r) = Z_C7_raw(r) \ E_<7(r).
```

For singleton constant-coefficient cells, each cell either survives as one paid
slope or disappears.  The negative regression and positive producer therefore
fit together: the former rejects double charging, while the latter performs the
required deletion before payment.

## Validation boundary

The stdlib-only package kernel-builds the finite producer, rooted witness
adapter, earlier-line extension, and executable fixtures.  Printed axiom reports
for these modules contain no `sorryAx` or custom axioms; the reported foundations
are the package's existing `propext` and `Quot.sound`.

The finite-field algebra is not reproved inside the stdlib-only package.  It
enters through the explicit fields of `BasePoleC7WitnessClass`, matched above to
the proved source theorem.  This is the same source/adapter separation used by
the rest of the asymptotic spine.

## Nonclaims

- No C7 survivor is asserted to exist on every received line.
- No completeness theorem over all received RS lines is proved.
- No single global C1--C9 atlas fixed before the line is constructed.
- No asymptotic semantic profile-count theorem is proved beyond the local
  `q - 1` census of this class.
- No row-wide `(UNIF)`, envelope-to-target comparison, or row closure is proved.
- No C8 ray compiler, C9 Sidon theorem, or residual-to-full theorem is claimed.
- The result does not replace distinct slopes by support counts, pair moments,
  max-fibre estimates, or fixed-chart bounds.

## Research consequence

This closes the requested local C7 producer interface for the established
base-pole constant-coefficient class.  The next research question is no longer
how to pay these cells: their exact post-deletion singleton slope image is paid.
The remaining global work is to place this class inside one row-complete
fixed-before-line semantic atlas and prove the honest

```text
sup_line sum_profile
```

comparison together with the other owners.
