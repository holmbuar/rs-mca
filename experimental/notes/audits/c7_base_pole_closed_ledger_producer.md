# C7 base-pole constant-coefficient adapter into the closed ledger

**Status:** `PROVED LOCAL ADAPTER / SOURCE-FACING FORMALIZATION / SEMANTIC OWNER AMBIGUITY / CONDITIONAL GLOBAL USE`

**Lean modules:**

- `AsymptoticSpine.C7OwnerRegression`
- `AsymptoticSpine.C7BasePoleProducer`
- `AsymptoticSpine.C7BasePoleWitnessProducer`
- `AsymptoticSpine.C7BasePoleLineExtension`
- `AsymptoticSpine.C7SingletonPlantedAbsorption`

**Source theorem:**
`experimental/notes/thresholds/aperiodic_one_ray_saturation.md`

## Result

The base-pole constant-coefficient class supplies a complete local
deletion-aware adapter for the `UniformClosedLedger` interface.  It does not by
itself establish an atlas-independent nonempty C7 semantic owner.

For one received base-pole line and one fixed prefix value, the source theorem
partitions the actual exact-agreement witnesses by locator constant coefficient

```text
C_d = {S in Fib_w(z) : c_m(S) = d}.
```

Every nonempty `C_d` has final slope image exactly `{-d}`.  There are at most
`q - 1` realized nonzero constant coefficients.  Given an already-fixed earlier
C1--C6 assigned slope image `E_<7(r)` on the same received line, the correct C7
adapter uses

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
preserves first-match ownership.  The sum is formed inside the received line;
no `sum_profile sup_line` interchange occurs.

## Rooted chain

The source-facing structure `BasePoleC7WitnessClass` records precisely the data
used from the base-pole theorem:

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
the supplied earlier slope image.

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

## Correction to the earlier affine-Steiner regression packet

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

is stronger than necessary.  A correct adapter may form and pay the literal
post-deletion subset

```text
Z_C7^o(r) = Z_C7_raw(r) \ E_<7(r).
```

For singleton constant-coefficient cells, each cell either survives as one paid
slope or disappears.  The negative regression and deletion-aware adapter fit
together: the former rejects double charging, while the latter performs the
required deletion before payment.

## Singleton-planted absorption of C7

A second, stronger semantic regression is
`experimental/notes/audits/c7_singleton_planted_absorption.md`.

The broad planted-cell grammar in the frontiers draft admits the fixed profiles

```text
P_t(X)=X-t,  t in D,
```

unless a stricter semantic rule is imposed.  The `t`-profile consists of all
witnesses whose support contains `t`; every positive-agreement witness has
nonempty support, so these C3 profiles cover every witness before C7.

On the base-pole family there are `n=q-1=exp(o(n))` profiles, and each realized
profile has at most `q=exp(o(n))` distinct slopes.  The direct field-cardinality
bound therefore pays them from the additive profile term with subexponential
loss.  Ordered first match leaves

```text
Z_C7^o(r)=empty.
```

`AsymptoticSpine.C7SingletonPlantedAbsorption` kernel-checks the finite interface
regression: four overlapping singleton-root C3 cells assign all four raw slopes,
and the later raw C7 list is empty.  Thus the base-pole adapter can be populated
only relative to a named earlier atlas; it is not a proof that C7 is nonempty
under every atlas admitted by the current grammar.

A nonempty semantic C7 theorem must therefore do at least one of the following:

1. restrict C3 to positive-density planted blocks;
2. require planted factors to arise from a named row-dependent common-factor or
   resultant mechanism;
3. fix a canonical atlas that excludes singleton-root profiles;
4. place the direct constant-coefficient saturation profiles before them; or
5. accept C3 as the semantic owner and C7 as empty.

## Validation boundary

The stdlib-only package kernel-builds the finite adapter, rooted witness module,
earlier-line extension, both ownership regressions, and executable fixtures.
The full package build passes in 33 jobs.  Printed axiom reports for the C7
modules contain no `sorryAx` or custom axioms; the reported foundations are the
package's existing `propext` and `Quot.sound`.

The finite-field algebra is not reproved inside the stdlib-only package.  It
enters through the explicit fields of `BasePoleC7WitnessClass`, matched above to
the proved source theorem.  The singleton-planted asymptotic payment is recorded
in the audit note; the Lean module formalizes its finite first-match consequence.

## Nonclaims

- No C7 survivor is asserted to exist on every received line or under every
  admissible atlas.
- No completeness theorem over all received RS lines is proved.
- No single global C1--C9 atlas fixed before the line is constructed.
- No asymptotic semantic profile-count theorem is proved beyond the stated
  local `q - 1` and singleton-profile censuses.
- No row-wide `(UNIF)`, envelope-to-target comparison, or row closure is proved.
- No C8 ray compiler, C9 Sidon theorem, or residual-to-full theorem is claimed.
- The result does not replace distinct slopes by support counts, pair moments,
  max-fibre estimates, or fixed-chart bounds.

## Research consequence

The natural-scale payment problem for the base-pole constant-coefficient image
is solved: after an earlier slope image is supplied, its literal survivor subset
is paid and composes with the earlier line.

The semantic-owner problem is not solved by the raw theorem.  Under the broad
frontiers C3 grammar, a paid fixed singleton-root atlas absorbs the entire class.
The next C7 decision is therefore a definition/theorem choice about the global
atlas, not another slope estimate:

```text
restrict C3 / choose canonical order / accept C3 ownership.
```

Only after that choice can a nonempty C7 survival theorem be meaningfully
formulated.  Any global use must still preserve the honest

```text
sup_line sum_profile
```

comparison together with the other owners.
