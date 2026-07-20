# Primitive one-parameter split-pencil C8 direct-slope producer

## Status

`PROVED LOCAL / DIRECT DISTINCT-SLOPE PAYMENT / SOURCE-FACING FORMALIZATION / CONDITIONAL GLOBAL USE`

**Terminal verdict:** `FIXED` for the actual primitive one-parameter C8 chart;
`OPEN GAP` for higher-dimensional chart exhaustion and row-wide `(UNIF)`.

**Lean modules:**

- `AsymptoticSpine.C8OnePencilDirectSlope`
- `AsymptoticSpine.C8OnePencilLineExtension`

**Source inputs:**

- `experimental/grande_finale.tex`, `thm:bc-moving-root` and
  `cor:bc-one-pencil`;
- the source first-match order removing tangent, common-support, quotient,
  extension, degree-drop, and common-GCD branches;
- the `UniformClosedLedger` interface supplied by stacked PR #987.

## Result

One actual post-C1--C7 balanced-core chart is directly paid once its residual
candidate locators have been reduced to a projective one-parameter pencil

```text
L_[s:t](X) = s A(X) + t B(X).
```

Let

```text
G = gcd(A,B,Lambda_D),
g = deg G,
omega = degree of every counted D-split residual locator,
N = |D|,
```

with `g < omega`.  Assume, exactly as in `cor:bc-one-pencil`, that the final MCA
slope injects into the projective pencil parameter and that each residual bad
slope supplies a degree-`omega` split locator with fixed `D`-part exactly `G`.
Then the actual distinct-slope image `Gamma` satisfies

```text
|Gamma| * (omega - g) <= N - g.                         (C8-MR)
```

Consequently

```text
|Gamma| <= floor((N - g) / (omega - g))
        <= N - g
        <= N.
```

The first-match C8 owner is

```text
Gamma_C8^o(r) = Gamma_raw(r) \ Gamma_<8(r),
```

where `Gamma_<8(r)` is the aggregate assigned-slope image of C1--C7 on the same
received line.  Deletion preserves `(C8-MR)`.  The surviving image is installed
through a direct `.c8` payment at unit natural profile scale with polynomial
compiler loss `N-g`.

This is a direct final-slope theorem.  No raw support census, support-pair
moment, max-fibre bound, or fixed-chart cardinality is substituted for the MCA
numerator.

## Rooted chain

```text
raw residual locator/explanation witness w
  -> final MCA slope gamma(w)
  -> projective pencil parameter lambda(gamma)
  -> injective slope-to-parameter map on the realized slope image
  -> omega-g moving roots outside the fixed D-part G
  -> moving-root incidence bound (C8-MR)
  -> delete aggregate C1--C7 assigned slopes
  -> surviving C8 ProfilePayment at natural scale 1
  -> append to the earlier ClosedLineLedger
  -> line-local profile sum.
```

The slope-to-parameter injection is essential.  Without it, several slopes
could be charged to one pencil parameter and the moving-root theorem would not
pay the final MCA image.  The source theorem prints this injection as a
hypothesis; the Lean structure exposes it explicitly on the realized raw slope
list.

## Moving-root proof

Count incidences

```text
I = {(lambda,x) : x in D \ Z(G), L_lambda(x)=0}.
```

For a moving point `x` outside the fixed part, `(A(x),B(x)) != (0,0)`.  The
homogeneous equation

```text
s A(x) + t B(x) = 0
```

therefore has exactly one projective solution `[s:t]`.  Hence each available
moving domain point contributes to at most one parameter and

```text
|I| <= N-g.
```

Every counted degree-`omega` split member has exactly `omega-g` moving roots, so

```text
|I| >= |parameters| * (omega-g).
```

The residual slope-to-parameter map is injective; therefore

```text
|Gamma| = |slope parameters|,
|Gamma| * (omega-g) <= N-g.
```

This already incorporates saturation at the MCA layer: one slope is counted
once even if several raw support representatives lie below the same line ray.

## First-match deletion

The producer never installs the untrimmed raw pencil image.  It defines

```text
assignedSlopes = rawSlopes.filter (not previously assigned).
```

Every survivor remains rooted in an actual chart witness, and the subset
inherits the direct moving-root inequality.  If all raw slopes were paid by an
earlier cell, no C8 profile is installed.

## Natural-scale direct payment

The one-pencil chart is one realized semantic profile.  Its image-normalized
profile term contains an additive unit.  The direct loss is

```text
compilerLoss = N-g <= N = exp(o(N)).
```

The Lean adapter uses

```lean
ProfilePayment.ofDirect .c8 assignedSlopes 1 paymentLoss
```

with `(C8-MR)`.  The residual, Sidon, and ray fields inside the direct adapter
are identities; no C9 analytic input or generic residual ray compiler is
manufactured.

The sharp source count remains available externally.  In the primitive case
`g=0`, it is `floor(N/omega)`.  At the active deployed MCA adjacent rows, the
corrected complements are `omega=981104` and `omega=981128`, so the sharp count
is two.  The stdlib-only compiler deliberately uses the coarser polynomial loss
because asymptotic natural-scale payment, not deployed constant closure, is the
claim here.

## Lean statement map

### Rooted slope and pencil parameter

- `rawSlopes` is the duplicate-free realized witness slope image.
- `mem_rawSlopes_iff_mem_witnessSlopeImage` proves exact image membership.
- `parameterOfSlope_injective_on_rawSlopes` exposes the source injection.
- `movingRoots_pos` records that the chart is genuinely moving rather than a
  common-GCD cell.

### First match and direct payment

- `assignedSlopes` performs C1--C7 slope deletion.
- `assignedSlope_has_surviving_witness` roots every survivor.
- `assignedSlopes_mul_movingRoots_le_availableRoots` carries `(C8-MR)` through
  deletion.
- `assignedSlopes_length_le_paymentLoss` gives the polynomial direct payment.
- `profile`, `line`, and `ledger` populate `UniformClosedLedger`.
- `ledger_compiles` proves the one-line numerator bound while preserving
  `sup_line sum_profile`.

### Composition after earlier owners

- `priorAssignedSlopes` extracts the exact C1--C7 assigned image.
- `extendLine` appends the C8 profile only when its residual is nonempty.
- `extendLine_flatten_assignedSlopes` proves the exact disjoint union.
- `extendLine_budgetTotal` and `extendLine_naturalTotal` prove line-local
  telescopes.
- `extendLine_budgetTotal_le_prior_add_paymentLoss` bounds the added C8 ray cost.
- `extendLine_naturalTotal_le_prior_add_one` bounds the added natural-profile
  cost by one realized pencil.

The executable fixture has `N=10`, `g=2`, and `omega=6`.  Two raw slopes
saturate `2*(6-2)=10-2`; one is earlier-owned and the other is appended as the
C8 survivor.

## Why this closes a real C8 class

The source audit already states that `thm:bc-moving-root` and
`cor:bc-one-pencil` settle the enumerative part for the original primitive
one-parameter split-locator object.  The remaining issue was composition with
the semantic first-match and closed-ledger interface.  This packet supplies
that composition:

1. actual rooted residual witnesses;
2. actual final slopes;
3. explicit slope-to-pencil injection;
4. direct moving-root payment of the slope image;
5. deletion under C1--C7;
6. natural-scale profile installation;
7. append-only line-local summation.

The local one-pencil class should therefore remain closed in future audits.

## Validation boundary

The stdlib-only package must kernel-build both new modules and their executable
fixtures.  Every exported theorem prints its axiom set.  Promotion requires no
`sorryAx`, no custom axiom, and only the package's accepted foundations.

The finite-field locator algebra and the projective moving-root theorem are not
reproved in the stdlib-only adapter.  They enter through the explicit rooted
slope-to-parameter interface and `(C8-MR)`, whose source proof is printed above.

## Nonclaims

- No C8 survivor is asserted to exist on every received line.
- No theorem proves that every post-common-core residual chart is
  one-dimensional.
- No higher-dimensional chart exhaustion, chart-count theorem, or off-chart
  exclusion is proved.
- No general residual ray compiler for unbounded shortened-kernel dimension is
  supplied.
- No row-complete fixed-before-line C1--C9 atlas, actual row-wide `(UNIF)`,
  target comparison, row closure, deployed adjacent certificate, or score
  movement is claimed.
- No support count, pair moment, max-fibre bound, or fixed-chart estimate is
  inserted in place of a distinct-slope payment.

## Research consequence

The primitive one-parameter C8 pencil is no longer an open enumerative or
interface input.  The live C8 lane is now exactly the structural remainder:
prove that every actual higher-dimensional post-common-core chart splits into
paid one-parameter pencils, routes to an earlier owner, or belongs to one
sharply named residual class, with a row-uniform chart count.
