# C7 raw-collapse payment, first-match ownership, and deletion-aware base-pole producer

**Status:** `COUNTEREXAMPLE / FORMALIZATION PACKET / LOCAL PRODUCER ADAPTER / OPEN GLOBAL GAP`
**Base interface:** `UniformClosedLedger` at commit
`335b9634074fe3a1650749be5985b15e7c8b36ed`
**Upstream base:** `9908454995f3f195cfe748f35a1135211609d066`

## Verdict

A raw C7-style one-slope payment is not, by itself, a semantic C7 owner.  The
integrated affine-Steiner quotient-owner family is an actual Reed--Solomon
regression showing that the implication

```text
local C7-style collapse + one-slope direct payment
  => nonempty C7 first-match owner
```

is false.  In that family, many support witnesses project to one slope, but the
supports are complete fibres of `x -> x^p - gamma*x`; C1 therefore owns and
deletes the slope before C7.

The correction is not to demand that every raw C7 slope always survive.  The
right first-match object is the post-deletion assigned image:

```text
Z_C7_assigned(r, lambda) = Z_C7_raw(r, lambda) \ Z_<7(r),
```

where `Z_<7(r)` is the aggregate C1--C6 slope image on the same received line.
The local producer may pay this assigned subset directly.  Nonemptiness is a
separate semantic fact, not a requirement of the payment adapter.

## Candidate that was tested

`aperiodic_one_ray_saturation.md` proves, on the base-field pole line, that the
refined prefix fibre can be partitioned by the locator constant coefficient:

```text
C_d = {S in Fib_w(z) : c_m(S) = d}.
```

Every nonempty `C_d` has final slope image exactly `{-d}`; there are at most
`q-1` such cells; and they cover every exact-`m` witness of that pole line.  Thus
for each constant coefficient the raw rooted chain is

```text
raw witness
  -> raw distinct-slope cell {-d}
  -> natural direct scale 1
  -> ray budget 1.
```

What the raw theorem alone does not prove is whether `-d` survives the fixed
earlier owner order.  Multiplicative aperiodicity rules out one narrow periodic
quotient mechanism; it does not exclude every C1 quotient map or the C2--C6
owners.

## Exact deletion-aware owner

For the base-pole constant-coefficient class, define

```text
A_d(r) = {-d} \ Z_<7(r).
```

Because the raw cell is a singleton, `A_d(r)` is either `{-d}` or empty.  The
payment is uniform:

```text
|A_d(r)| <= 1.
```

If `A_d(r) = {-d}`, C7 genuinely owns that slope.  If `A_d(r) = empty`, an
earlier C1--C6 owner has already charged the slope and C7 contributes zero.  The
line-local C7 contribution is therefore

```text
sum_d |A_d(r)| <= #{d : C_d nonempty} <= q - 1.
```

This preserves the required order: deletion and summation happen inside the
received line before any outer supremum is taken.

## Actual RS falsifier to the untrimmed implication

The affine-Steiner equality family supplies the required falsifier to the
untrimmed raw-owner implication:

```text
pi_gamma(x) = x^p - gamma*x,
```

with affine `F_p`-lines as complete fibres.  For each quotient profile there are
`q/p` support witnesses and one realized slope `gamma`.  This has the local
C7-style collapse signature, but C1 precedes C7 and owns every witness and
slope.  Hence the full-survival statement fails:

```text
gamma in Z_C1(r) intersect Z_C7_raw(r).
```

The post-C1 C7 assigned slope cell is empty.  This refutes charging the
untrimmed raw C7 profile; it does not refute charging the post-deletion subset.

## Lean interface regression

`AsymptoticSpine.C7OwnerRegression` models the exact first-match consequence
with one finite slope identifier:

```text
raw slope cells:       C1 [7], C7_raw [7]
first-match leaves:    C1 [7], C7 []
```

The module proves all of the following.

1. `affineSteinerC1C7_firstMatch`: the ordered first-match leaves are
   `[[7], []]`.
2. `affineSteinerRawC7_numericallyPaid`: the raw C7 direct payment satisfies its
   natural-scale inequality in isolation.
3. `affineSteinerRawC7_breaks_firstMatchOwnership`: installing both raw
   projections as assigned profiles violates the duplicate-free
   `ClosedLineLedger.firstMatchOwnership` field.
4. `noClosedLineLedger_with_affineSteinerRawC7`: no closed line ledger can have
   the earlier C1 payment followed by the untrimmed raw C7 payment.
5. `affineSteinerCorrectLine_totals`: after correct deletion, the line-local ray
   budget and natural-scale sum are both one.
6. `affineSteinerCorrectLedger_compiles`: the corrected line replays through
   `UniformClosedLedger.compile`.

Thus the failure is precisely semantic ownership.  It is not a failure of the
one-slope payment, not a support-count argument, and not a change to the
`sup_line sum_profile` order.

## Lean producer adapter

`AsymptoticSpine.C7BasePoleProducer` formalizes the deletion-aware local
producer at the same interface boundary.  It starts from two finite slope lists:

```text
earlier : aggregate C1--C6 slope image on the received line
raw     : duplicate-free base-pole constant-coefficient C7 raw slope image
```

and defines

```text
basePoleC7AssignedSlopes earlier raw = raw \ earlier.
```

It then maps each survivor `gamma` to a singleton direct payment

```text
ProfilePayment.ofDirect .c7 [gamma] 1 1 ...
```

and proves that the flattened assigned C7 slope image is exactly the survivor
list, the budget total and natural-scale total both equal the survivor count,
and the survivor count is bounded by the raw constant-coefficient census.  The
source-facing wrapper is

```text
basePoleC7Line_budgetTotal_le_qMinusOne
```

which consumes only the raw theorem's `raw.length <= qMinusOne` bound.

## Ledger consequence

The invalid untrimmed sum is

```text
U_C1(r) + U_C7_raw(r) = 1 + 1,
```

when both terms charge the same slope.  The correct first-match line-local sum
is

```text
U_C1(r) + U_C7_assigned(r) = 1 + 0 = 1
```

in the affine-Steiner deletion regression, and more generally

```text
sum_d U_C7_assigned(r,d) = #{surviving constant-coefficient slopes} <= q - 1.
```

The outer supremum is taken only after this line-local deletion and sum.  No
`sum_profile sup_line` interchange is introduced.

## What remains open

The local producer does not prove that a survivor exists, and it does not prove
that every proposed base-pole slope avoids C1--C6.  It only shows how to populate
the closed-ledger interface after the required first-match deletion has been
performed.

A successor source theorem could strengthen the result by proving nonempty
survival for a specific constant coefficient, or by classifying every deleted
coefficient under a named earlier owner.  Neither strengthening is required for
the local direct-payment adapter.

## Nonclaims

- This is not a counterexample to every possible C7 survivor theorem.
- It does not show that the base-pole constant-coefficient cells are always
  earlier-owned; it shows that untrimmed raw ownership is invalid and that the
  assigned subset is the correct producer object.
- It does not prove completeness over all received lines, a global atlas fixed
  before the line, profile-count asymptotics, actual UNIF, row closure, or a
  target comparison.
- It does not replace slope payment by support counts, moments, max fibres, or
  chart estimates.

## Replay

After applying the patch on top of commit `335b9634074fe3a1650749be5985b15e7c8b36ed`:

```text
cd experimental/lean/asymptotic_spine
lake build AsymptoticSpine.C7OwnerRegression
lake build AsymptoticSpine.C7BasePoleProducer
lake build
python3 ../../scripts/verify_c7_first_match_owner_regression.py
```

The original PR #987 claims remain unchanged: this packet is a separate C7
consumer/producers test layered on top of its interface.
