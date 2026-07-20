# Root-free modular-locator C8 direct-slope producer in the positive Plotkin-gap regime

## Status

`PROVED LOCAL / NONDEPLOYED HIGH-RIGIDITY SUBREGIME / DIRECT DISTINCT-SLOPE PAYMENT / CONDITIONAL GLOBAL USE`

**Terminal verdict:** `FIXED` when the constant-weight Plotkin gap is positive;
`OPEN GAP` for the active deployed first-interior modular-locator fibres.

**Lean modules:**

- `AsymptoticSpine.C8ModularHighRigidityDirectSlope`
- `AsymptoticSpine.C8ModularHighRigidityLineExtension`

**Source inputs:**

- `experimental/notes/thresholds/bc_first_interior_general_line_modular_fibers.md`;
- `experimental/notes/thresholds/bc_first_interior_modular_subset_product.md`,
  especially the root-free mixed subset-product normal form and exchange
  lower bound;
- exact prefix-list uniqueness for the simple-pole support/polynomial witness;
- the `UniformClosedLedger` interface supplied by stacked PR #987.

## Source class

Fix one actual first-interior fixed-multiplier chart with

```text
m = K+w,
gcd(W1,Lambda_D)=1,
gcd(B,W1)=1,
0 != B, deg B <= 1.
```

The exact normal-form theorem identifies its support set as one fibre of

```text
Psi_(W1,h) : binom(D,m) -> U_h x (F[X]/W1)^x,
```

where

```text
d = deg W1,
h = max(0,w+deg B-d).
```

The modular collision-rigidity theorem proves that distinct supports in one
fibre exchange at least

```text
L = h+d+1
```

roots on each side:

```text
|T \ T'| = |T' \ T| >= L.                               (MR)
```

This is stronger than the ordinary Q prefix rigidity because equality modulo
`W1` contributes the additional degree-`d` divisibility.

## From support rigidity to a direct slope theorem

Let `Gamma` be the distinct final slope image of the rooted witnesses in this
one semantic profile. Choose one support/polynomial witness `(T_gamma,P_gamma)`
for each `gamma in Gamma`.

The representative supports are distinct. If two slopes used the same support,
exact prefix-list uniqueness would give the same listed polynomial; evaluating
that polynomial at the pole would give the same slope, contradicting the
choice of two distinct elements of `Gamma`.

Thus `(MR)` applies to every pair of slope representatives.

Write

```text
J = |Gamma|,
a_x = number of representative supports containing x,
N = |D|.
```

The total Hamming distance over unordered pairs is

```text
sum_x a_x (J-a_x).
```

Every pair has Hamming distance at least `2L`, so

```text
J(J-1)L <= sum_x a_x(J-a_x).                             (1)
```

All representatives have size `m`, hence

```text
sum_x a_x = mJ.
```

By Cauchy,

```text
sum_x a_x^2 >= (mJ)^2/N.
```

Therefore

```text
sum_x a_x(J-a_x)
  = mJ^2 - sum_x a_x^2
  <= m(N-m)J^2/N.                                        (2)
```

Combining (1)--(2) and multiplying by `N` gives, for `J>0`,

```text
N L (J-1) <= m(N-m)J.
```

Equivalently,

```text
J * (N L - m(N-m)) <= N L.                              (C8-P)
```

For `J=0`, `(C8-P)` is immediate.  Hence it holds for the actual distinct-slope
image, not merely for the complete support fibre.

## Positive-gap payment

Assume

```text
Delta := N L - m(N-m) > 0.                              (PG)
```

Then

```text
|Gamma| <= floor(NL/Delta) <= NL <= N^2.
```

After deleting the aggregate C1--C7 assigned-slope image on the same received
line, the survivor set `Gamma_C8^o` is a subset of `Gamma`, so `(C8-P)` and the
same polynomial payment survive.

The Lean adapter uses

```lean
ProfilePayment.ofDirect .c8 assignedSlopes 1 (N*L)
```

and installs no profile if the post-deletion image is empty.  This is the
additive unit of one realized modular-locator profile, multiplied by a
polynomial compiler loss.

The source pair count is used only to prove the direct inequality on one
representative per distinct slope.  The ledger never substitutes the raw
support-fibre size, a collision moment, a max-fibre bound, or an unrelated
fixed-chart count for the MCA numerator.

## Rooted chain

```text
raw modular-locator support/polynomial witness (T,P)
  -> final slope gamma=P(alpha)
  -> one rooted witness chosen for each distinct gamma
  -> distinct constant-weight representative supports
  -> modular exchange rigidity L=h+d+1
  -> direct slope inequality (C8-P)
  -> delete aggregate C1--C7 assigned slopes
  -> surviving C8 ProfilePayment at natural scale 1
  -> append to the earlier ClosedLineLedger
  -> line-local profile sum.
```

## Lean statement map

### Rooted image and direct payment

- `rawSlopes` is the duplicate-free realized witness slope image.
- `mem_rawSlopes_iff_mem_witnessSlopeImage` proves exact image membership.
- `plotkinGap` is `NL-m(N-m)`.
- `assignedSlopes` performs C1--C7 slope deletion.
- `assignedSlope_has_surviving_witness` roots every survivor.
- `assignedSlopes_mul_plotkinGap_le_paymentLoss` carries `(C8-P)` through
  deletion.
- `assignedSlopes_length_le_paymentLoss` uses `(PG)`.
- `paymentLoss_le_N_sq` records polynomial loss.
- `profile`, `line`, and `ledger` populate `UniformClosedLedger`.
- `ledger_compiles` proves the one-line numerator bound while preserving
  `sup_line sum_profile`.

### Composition after earlier owners

- `priorAssignedSlopes` extracts the exact C1--C7 assigned image.
- `extendLine` appends the modular profile only when its residual is nonempty.
- `extendLine_flatten_assignedSlopes` proves the exact disjoint union.
- `extendLine_budgetTotal` and `extendLine_naturalTotal` prove line-local
  telescopes.
- `extendLine_budgetTotal_le_prior_add_paymentLoss` bounds the added ray cost.
- `extendLine_naturalTotal_le_prior_add_one` bounds the added natural-profile
  cost by one.

The executable fixture has

```text
N=10, m=5, h=d=1, L=3, Delta=30-25=5.
```

Six raw slopes saturate `6*5=30`; two earlier-owned slopes are deleted in the
local fixture.

## Deployed-range audit

The positive-gap theorem is not a deployed-row closure.

For the active KoalaBear first-interior row,

```text
N=2097152,
m=1116048,
omega=N-m=981104,
w=67471,
L<=67474.
```

Even at the largest possible `L`,

```text
NL-m(N-m) = -953455922944 < 0.
```

For the active Mersenne-31 row,

```text
N=2097152,
m=1116024,
omega=981128,
w=67447,
L<=67450,
```

and

```text
NL-m(N-m) = -953509492672 < 0.
```

Thus the constant-weight Plotkin regime is far from the deployed parameters.
The deployed residual still requires mixed-character control, aggregate
occupancy/ray deduplication across multipliers, or another direct first-match
slope theorem.

This negative calibration is load-bearing: the new local theorem must not be
cited as a KoalaBear or Mersenne first-interior payment.

## Relation to current source obstructions

The source modular-fibre packet proves that rank alone does not pay separately
rounded fixed-multiplier slices.  In subunit-average cases, any nonempty slice
forces a large integer overhead.  It explicitly asks for one of:

1. aggregate fixed-word incidence across multipliers;
2. ray deduplication rather than raw modular coordinates; or
3. a direct first-match slope-image theorem along the received line.

The present result supplies item 3 only under `(PG)`. It neither estimates the
mixed character mass nor aggregates the deployed multiplier slices.

## Nonclaims

- No survivor is asserted to exist on every received line.
- No theorem covers the nonpositive Plotkin-gap range.
- No deployed first-interior row is paid.
- No root-bearing `W1`, common-GCD, quotient, extension, or field-transfer
  branch is included; those remain earlier owners.
- No aggregate multiplier theorem, mixed-character estimate, general residual
  ray compiler, or chart-count theorem is proved.
- No global fixed-before-line C1--C9 atlas, actual row-wide `(UNIF)`, target
  comparison, row closure, adjacent certificate, or score movement is claimed.

## Research consequence

The root-free modular-locator wall is now split honestly:

```text
positive Plotkin gap      -> direct polynomial C8 slope payment;
nonpositive Plotkin gap   -> mixed-character / aggregate slope residual.
```

Future work should not reopen the positive-gap subregime or treat exchange
rigidity alone as a deployed payment.
