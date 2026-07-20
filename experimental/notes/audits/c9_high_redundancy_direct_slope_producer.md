# High-redundancy simple-pole C9 direct-slope producer

## Status

`PROVED LOCAL / DIRECT DISTINCT-SLOPE PAYMENT / SOURCE-FACING FORMALIZATION / CONDITIONAL GLOBAL USE`

**Terminal verdict:** `FIXED` for this high-redundancy local C9 class;
`OPEN GAP` for the row-complete C9/UNIF package.

**Lean modules:**

- `AsymptoticSpine.C9HighRedundancyDirectSlope`
- `AsymptoticSpine.C9HighRedundancyLineExtension`

**Source inputs:**

- `experimental/notes/audits/c9_literal_interface_counterexample_v1.md`,
  Section 4 (zero-error two-list recovery);
- the exact simple-pole prefix-list correspondence used there;
- the `UniformClosedLedger` interface supplied by stacked PR #987.

## Result

One actual post-C1--C8 simple-pole boundary profile is directly paid whenever
its active weighted-Vandermonde redundancy satisfies

```text
2 * R + 2 > N.
```

Let `Gamma` be the set of distinct final MCA slopes realized by the raw rooted
witnesses in that one boundary profile.  Choose one support/polynomial witness
for each slope.  The source argument proves the denominator-cleared direct
slope inequality

```text
|Gamma| * (2 * R + 2 - N) <= 2 * (R + 1).              (C9-HR)
```

Consequently

```text
|Gamma| <= floor(2 * (R + 1) / (2 * R + 2 - N))
        <= 2 * (R + 1)
        <= 2 * (N + 1).
```

The first-match C9 owner is the literal post-deletion image

```text
Gamma_C9^o(r) = Gamma_raw(r) \ Gamma_<9(r),
```

where `Gamma_<9(r)` is the aggregate C1--C8 assigned-slope image on the same
received line.  Deletion preserves `(C9-HR)`.  The surviving slope image is
therefore installed through a direct `.c9` payment at unit natural profile
scale with polynomial compiler loss `2 * (R + 1)`.

This is a direct final-slope payment.  It does not replace the MCA numerator by
the size of the complete support fibre, a pair moment, a max-fibre estimate, or
a fixed chart.

## Rooted chain

For the mathematical source instance, the chain is

```text
raw exact-agreement support/polynomial witness (S,P)
  -> final simple-pole slope gamma = P(alpha)
  -> choose one rooted witness for each distinct gamma
  -> distinct representative supports
  -> common weighted-Vandermonde boundary value
  -> MDS kernel-distance pair count on the representatives
  -> direct inequality (C9-HR) for the distinct slope set
  -> delete aggregate C1--C8 assigned slopes
  -> surviving C9 ProfilePayment at natural scale 1
  -> append to the earlier ClosedLineLedger
  -> line-local profile sum.
```

The representative choice does not overcount supports.  Exact prefix-list
uniqueness says that a support determines its listed polynomial.  Hence two
distinct slopes cannot use the same support: equal support would give equal
polynomial and therefore equal evaluation at the pole.

## Direct pair-count proof

Let `J = |Gamma|` and write `x_gamma in {0,1}^N` for the incidence vector of the
chosen representative support for slope `gamma`.

All representatives have the same boundary value, so for distinct slopes
`gamma != gamma'`,

```text
H (x_gamma - x_gamma') = 0.
```

The weighted-Vandermonde kernel is an `[N,N-R,R+1]` MDS code.  The difference
is nonzero because the representative supports are distinct.  Thus every pair
of representative incidence vectors differs in at least `R + 1` coordinates.
Summing Hamming distances over unordered pairs gives

```text
binom(J,2) * (R + 1)
  <= sum_t a_t * (J - a_t),
```

where `a_t` is the number of representatives containing coordinate `t`.
For every coordinate,

```text
4 * a_t * (J - a_t) <= J^2.
```

Therefore

```text
4 * binom(J,2) * (R + 1) <= N * J^2.
```

For `J = 0` the target is immediate.  For `J > 0`, cancel one factor of `J` and
rearrange:

```text
2 * (J - 1) * (R + 1) <= N * J,
J * (2 * R + 2 - N) <= 2 * (R + 1).
```

This proves `(C9-HR)` directly for the number of distinct slopes because the
counted family contains exactly one representative per slope.

## First-match deletion

The negative lesson from C7 applies unchanged: a valid raw payment does not
license double charging.  The producer therefore defines

```text
assignedSlopes = rawSlopes.filter (not previously assigned).
```

Every assigned slope remains rooted in an actual raw witness.  Since it is a
subset of `Gamma`, both the duplicate-free property and `(C9-HR)` survive.
If every raw slope was already owned by C1--C8, the C9 profile is empty and is
not installed.

## Natural-scale direct payment

This local C9 object is one realized boundary profile.  Its image-normalized
profile term contains the additive unit `1`; the direct polynomial loss is

```text
compilerLoss = 2 * (R + 1) <= 2 * (N + 1) = exp(o(N)).
```

The Lean adapter uses

```lean
ProfilePayment.ofDirect .c9 assignedSlopes 1 paymentLoss
```

with the proved distinct-slope inequality.  The Sidon, residual, and ray stages
inside `ofDirect` are identities; no primitive analytic theorem is fabricated.
This class is paid by its direct final-slope theorem, which is an allowed
alternative to image-normalized Sidon/MI--MA.

## Lean statement map

### Rooted slope image

- `rawSlopes` is the duplicate-free realized image of the witness-to-slope map.
- `mem_rawSlopes_iff_mem_witnessSlopeImage` proves exact image membership.
- `assignedSlopes` performs the C1--C8 deletion.
- `assignedSlope_has_surviving_witness` roots every survivor in an actual witness
  and records exclusion from the earlier image.

### Direct payment

- `assignedSlopes_mul_gap_le_paymentLoss` carries `(C9-HR)` through deletion.
- `assignedSlopes_length_le_paymentLoss` uses the positive high-redundancy gap.
- `paymentLoss_le_two_mul_N_succ` records polynomial loss.
- `profile`, `line`, and `ledger` populate the existing closed-ledger interface.
- `ledger_compiles` proves the local one-line numerator bound without changing
  the line-supremum/profile-sum order.

### Composition after C1--C8

- `priorAssignedSlopes` extracts the exact earlier assigned image.
- `extendLine` appends the C9 profile only when the post-deletion image is
  nonempty.
- `extendLine_flatten_assignedSlopes` proves the exact disjoint union.
- `extendLine_budgetTotal` and `extendLine_naturalTotal` prove the line-local
  telescopes.
- `extendLine_budgetTotal_le_prior_add_paymentLoss` bounds the added C9 ray cost.
- `extendLine_naturalTotal_le_prior_add_one` bounds the added natural-profile
  cost by one realized boundary profile.

The executable fixture has `N=10`, `R=6`, gap `4`, and three raw slopes.  One
slope is earlier-owned, leaving two C9 survivors.  Appending the C9 profile to
the earlier line gives three covered slopes and two realized profiles.

## Why this is C9 progress rather than another Q wrapper

The literal C9 interface audit proves that unrestricted image-normalized C9 is
false and that the phrase “surviving C1--C8” carries indispensable content.  It
also identifies high redundancy as a genuine positive range.  The present
packet turns that positive range into the missing producer shape:

1. actual rooted witnesses;
2. actual final slopes;
3. slope-level first-match deletion;
4. a direct bound on one representative per distinct slope;
5. natural-scale payment;
6. append-only line-local summation.

The support pair count is used only to prove the direct slope inequality after
selecting one representative per slope.  The quantity installed in the ledger
is the distinct slope set itself.

## Validation boundary

The stdlib-only package is required to kernel-build the two new modules and all
fixtures.  Every exported theorem prints its axiom set.  Promotion requires no
`sorryAx`, no custom axiom, and only the package's accepted foundations.

The finite-field/polynomial algebra is not reproved in the stdlib-only adapter.
It enters through the explicit rooted witness catalogue and the direct
slope-pair inequality `(C9-HR)`, whose source proof is printed above.

## Nonclaims

- No C9 survivor is asserted to exist on every received line.
- No theorem classifies all simple-pole profiles as post-C1--C8 survivors.
- No low-redundancy theorem is proved when `2 * R + 2 <= N`.
- No general primitive-Q, Sidon, MI--MA, or major-arc ownership theorem is
  proved.
- No completeness theorem over all received RS lines or global fixed-before-line
  C1--C9 atlas is constructed.
- No asymptotic profile-count theorem, actual row-wide `(UNIF)`, target
  comparison, row closure, or score movement is claimed.
- No support count, pair moment, max-fibre bound, or fixed-chart estimate is
  inserted in place of a distinct-slope payment.

## Research consequence

The high-redundancy simple-pole portion of C9 no longer requires a Sidon theorem:
it is paid directly at the actual post-deletion slope image.  The live C9 lane
is narrowed to low redundancy, plus the row-global tasks of semantic atlas
completion, major-arc ownership, and honest

```text
sup_line sum_profile
```

control.
