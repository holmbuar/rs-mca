# C7 raw-collapse payment does not imply post-prefix ownership

**Status:** `COUNTEREXAMPLE / FORMALIZATION PACKET / OPEN GAP`
**Base interface:** `UniformClosedLedger` at commit
`335b9634074fe3a1650749be5985b15e7c8b36ed`
**Upstream base:** `9908454995f3f195cfe748f35a1135211609d066`

## Verdict

The currently established one-ray/base-pole C7 packet cannot yet be installed
as a nonempty `UniformClosedLedger` producer.  Its direct distinct-slope payment
is real, but its survival under the earlier C1--C6 cells is not proved.

This is not merely a missing bookkeeping lemma.  The integrated
`affine_steiner_quotient_owner.md` family is an actual Reed--Solomon regression
showing that the implication

```text
local C7-style collapse + one-slope direct payment
  => nonempty C7 first-match owner
```

is false.  In that family, many support witnesses project to one slope, but the
supports are complete fibres of `x -> x^p - gamma*x`; C1 therefore owns and
deletes the slope before C7.

The useful deliverable is option (2) from the task: a precise counterexample to
the proposed owner/payment interface.  No genuine C7 producer is claimed.

## Candidate that was tested

`aperiodic_one_ray_saturation.md` proves, on the base-field pole line, that the
refined prefix fibre can be partitioned by the locator constant coefficient:

```text
C_d = {S in Fib_w(z) : c_m(S) = d}.
```

Every nonempty `C_d` has final slope image exactly `{-d}`; there are at most
`q-1` such cells; and they cover every exact-`m` witness of that pole line.
Thus the raw projection and direct payment are strong enough for

```text
raw witness
  -> raw distinct-slope cell {-d}
  -> natural direct scale 1
  -> ray budget 1.
```

What the packet explicitly does not prove is that this raw cell survives the
fixed earlier owner order.  Multiplicative aperiodicity rules out one narrow
periodic quotient mechanism; it does not exclude every C1 quotient map or the
C2--C6 owners.

## Exact missing theorem

For a proposed raw C7 slope cell `Z_C7(r,lambda)`, the adapter needs the
line-local survival statement

```text
(C7-SURV)
forall gamma in Z_C7(r,lambda),
  forall earlier owner i in {C1,...,C6},
    gamma notin Z_i(r).
```

Equivalently, after the already-fixed ordered atlas,

```text
firstMatchSlopeCell(C7, r, lambda) = Z_C7(r,lambda).
```

Only after `(C7-SURV)` may the raw one-slope estimate be used as the assigned
C7 payment.  A support predicate, aperiodicity, or a raw slope-image theorem is
not a substitute.

## Actual RS falsifier to the proposed implication

The affine-Steiner equality family supplies the required falsifier:

```text
pi_gamma(x) = x^p - gamma*x,
```

with affine `F_p`-lines as complete fibres.  For each quotient profile there
are `q/p` support witnesses and one realized slope `gamma`.  This has the local
C7-style collapse signature, but C1 precedes C7 and owns every witness and
slope.  Hence `(C7-SURV)` fails:

```text
gamma in Z_C1(r) intersect Z_C7_raw(r).
```

The post-C1 C7 assigned slope cell is empty.

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

## Ledger consequence

In the finite one-slope interface model, the invalid sum is

```text
U_C1(r) + U_C7_raw(r) = 1 + 1,
```

because it charges the same slope twice.  The correct first-match line-local
sum is

```text
U_C1(r) + U_C7_assigned(r) = 1 + 0 = 1.
```

The outer supremum is taken only after this line-local deletion and sum.  No
`sum_profile sup_line` interchange is introduced.

## What would convert this negative result into a producer

A successor C7 packet must prove `(C7-SURV)` for a real post-prefix class, then
supply one of:

```text
assigned C7 slope image <= natural profile scale,
```

or a typed residual/full -> ray chain ending in that inequality.  For the
base-pole constant-coefficient cells, the direct one-slope payment is already
available; only the actual earlier-owner exclusion is missing.

## Nonclaims

- This is not a counterexample to every possible C7 survivor theorem.
- It does not show that the base-pole constant-coefficient cells are always
  earlier-owned; it shows that their current theorem does not establish
  survival and that the proposed inference is false in an actual RS family.
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
lake build
python3 ../../scripts/verify_c7_first_match_owner_regression.py
```

The original PR #987 claims remain unchanged: this packet is a separate
negative producer test layered on top of its interface.
