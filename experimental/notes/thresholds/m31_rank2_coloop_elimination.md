# M31 padded rank-two coloop elimination

```yaml
workboard_item: M1
row: Mersenne-31 list analytic stress row
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: >-
  For every marked rank-46 source key carrying the intrinsic padded three-row
  syzygy frame of the masked-diagonal-saturation theorem, the distinguished
  extra column is not a coloop. Hence the terminal UNPAID_RANK2_COLOOP is empty.
architecture: M31_CANONICAL_PADDED_RANK46
partition_digest: >-
  ZERO_SYNDROME -> NEAR_RATIONAL_SINGLETON -> NAMED_EXISTING_OWNER ->
  CANONICAL_MASKED_SPLIT_PENCIL -> PADDED_FRAME ->
  {COMMON_CORE_ADD_BACK, RANK2_COLOOP}
atom_or_cell: UNPAID_RANK2_COLOOP
quantifier: every marked rank-46 source key and its intrinsic padded three-row frame
projection_and_unit: padded syzygy-column matroid; terminal exclusion, not a codeword payment
claimed_bound: exact empty terminal (zero surviving coloop configurations)
status: PROVED
impact: ROUTE_CUT
falsifier: >-
  a source frame whose distinguished padded locator is zero, or whose three
  rows are not syzygies of the same padded locator row; both violate the stated
  source hypotheses
replay: >-
  python3 experimental/scripts/verify_m31_rank2_coloop_elimination.py --check;
  python3 -O experimental/scripts/verify_m31_rank2_coloop_elimination.py --check;
  python3 experimental/scripts/verify_m31_rank2_coloop_elimination.py --tamper-selftest
```

## Status

**PROVED TERMINAL ELIMINATION / ACCEPTANCE GATE CRITERION 3 / MERSENNE-31
LIST ROW STILL OPEN / LEDGER MOVEMENT ZERO.**

The exact target is the sibling terminal left after the padded rank-three frame
in `experimental/notes/thresholds/m31_canonical_popov_rank46_compiler.md` and
the masked-diagonal-saturation successor packet:

```text
UNPAID_RANK2_COLOOP.
```

The source dichotomy distinguished one extra column in the first three padded
syzygy rows.  If deleting that column preserved rank three, the packet entered
the separate common-core branch.  If deletion lowered rank, the extra column
was called a coloop and the old 45 columns had rank at most two.  The second
alternative cannot occur, for a reason intrinsic to the padded syzygy frame.

## 1. Exact source object

Let `F` be the Mersenne-31 coefficient field and work, when taking column rank,
over the polynomial fraction field `K=F(X)`.  For one marked source key, the
masked-diagonal-saturation theorem supplies three independent padded syzygy
rows for a primitive padded locator row

```text
W'=(W'_1,...,W'_46).
```

Every `W'_i` is a nonzero polynomial.  Write the three syzygy rows as a
`3 x 46` matrix `A`, and write its `i`-th column as

```text
v_i=(A_(1,i),A_(2,i),A_(3,i)) in K^3.
```

The exact deployed bounds retained on this frame are

```text
lambda_1                         <= 20,765,
lambda_1+lambda_2                <= 41,530,
lambda_1+lambda_2+lambda_3       <= 62,295 < 67,447.
```

The no-coloop argument is stronger than these inequalities: it needs only that
the rows are syzygies of the same nonzero locator row.

## 2. Full-support dependence theorem

### Theorem 2.1 (padded locator dependence)

The columns of `A` satisfy

```text
sum_(i=1)^46 W'_i v_i = 0.                              (2.1)
```

Moreover, the coefficient of the distinguished extra column is nonzero.

**Proof.**  The `r`-th coordinate of the left side is

```text
sum_(i=1)^46 W'_i A_(r,i),
```

which is zero because row `r` is a syzygy of `W'`.  The distinguished
coefficient is its locator polynomial, hence is nonzero. `QED`

### Corollary 2.2 (the extra column is not a coloop)

In a vector matroid, a column is a coloop precisely when its coefficient is zero
in every linear dependence among the columns.  Equation (2.1) is a dependence
whose coefficient at the distinguished column is `W'_46 != 0`.  Therefore the
extra column is not a coloop.  Equivalently,

```text
v_46 = -(W'_46)^(-1) sum_(i=1)^45 W'_i v_i,
```

so it lies in the span of the old 45 columns and deleting it does not lower
column rank. `QED`

### Corollary 2.3 (terminal elimination)

No padded frame can simultaneously satisfy

```text
old 45 columns have rank at most two
and
the distinguished extra column is a coloop.
```

Thus `UNPAID_RANK2_COLOOP` has no surviving configuration.  This conclusion is
pointwise, so it applies to every one of the at least `259,881` marked rank-46
source keys without a union bound, enumeration of keys, or loss of signed
occupancy credits.

## 3. Compatibility with the `F_11` direct-transport counterpacket

The padding-bridge audit's `F_11` counterpacket remains a mandatory boundary
condition.  It proves that a named minimal **actual-error** syzygy row need not
be coordinatewise divisible by the padding locators and therefore need not
transport directly to the padded module.

The present theorem makes no such transport claim.  It starts only after the
masked-diagonal-saturation theorem has constructed an intrinsic **padded**
three-row frame.  Equation (2.1) is the defining syzygy relation of those padded
rows with their own padded locator row.  A failure of direct transport for an
old actual-error basis is fully compatible with the existence of this
full-support dependence in a different intrinsic padded basis.

## 4. Exact finite certificate

The canonical JSON certificate and independent stdlib verifier exhaust small
finite-field matrices.  For every enumerated matrix and every coefficient
vector whose distinguished coefficient is nonzero, the verifier checks:

```text
matrix * coefficients = 0
  ==> rank(all columns) = rank(old columns).
```

It also prints the load-bearing falsifier obtained by allowing the distinguished
coefficient to be zero: over `F_2`, the old zero column, extra unit column, and
coefficient vector `(1,0)` form a relation while deletion lowers rank.  This
shows that the nonzero padded-locator hypothesis is necessary and is not hidden
by the enumeration.

## 5. Lean boundary

The stdlib-only module

```text
experimental/lean/sidon_effective_image/
  SidonEffectiveImage/M31RankTwoColoop.lean
```

locally restates the padded three-row frame and proves:

```text
paddedLocatorGivesNonzeroExtraDependence
extraColumnIsNotColoop
rankTwoColoopTerminalIsEmpty
everyMarkedFrameExcludesRankTwoColoop.
```

The package imports no `AsymptoticSpine.*`, `M31QRootedShell.*`, or open-PR
module.  The root imports only this module.  The module ends with `#print axioms`
for every load-bearing theorem.

## 6. Nonclaims

- The Mersenne-31 list row remains open and no list upper-bound atom is banked.
- This packet does not pay or modify `UNPAID_COMMON_CORE_ADD_BACK`; that is the
  sibling Lane G terminal.
- It does not prove row-sharp Q, rooted-shell completion, list-interior coverage,
  a final add-back, or an adjacent-row certificate.
- It does not construct a forbidden received word or prove that one exists.
- It does not transport a named actual-error Forney basis through padding.
- It does not alter stable-paper TeX, a deployed radius, an official score, or a
  prize claim.

The acceptance gate is criterion **3**: a precisely named terminal is killed by
theorem.
