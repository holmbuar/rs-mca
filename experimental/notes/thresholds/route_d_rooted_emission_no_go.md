# Route-D rooted-emission no-go theorem

STATUS: COUNTEREXAMPLE

## Outcome

The integrated `DEEP_MCA_RANK_DROP` owner cannot by itself pay marked
Route-D support mass. Two exact examples prove separate interface failures:

1. rank-drop eligibility is not determined by the displayed marked co-support
   datum when the received line and error amplitudes are omitted;
2. even for one fixed received line and one primitive target, one actual
   rank-drop slope can carry more than `p` marked top-seam witnesses.

These are counterexamples to unrooted or selector-free support emission. They
are not counterexamples to the distinct-slope owner, the deployed
`t * p` support bound, or a future injection proved after every exact
first-match deletion.

## Governing owner contract

The rank-drop packet of Scott Hughes fixes one received line `f+gamma*g` and
counts distinct finite MCA-bad slopes for that line. An eligible slope must
come from an actual noncontained incidence and must satisfy the field-native
Hankel rank predicate. The checked contract states:

```text
requires_actual_bad_incidence = true
raw_algebraic_rank_drop_paid  = false
slope_set_is_support_independent = true
per_support_charge            = false
per_pivot_charge              = false
scope                         = FIRST_MATCH_GLOBAL_ONCE.
```

For an actual error support `E`, the weighted Vandermonde factorization gives

```text
rank_F M_A(gamma) = min(t, |E|).
```

The owner therefore pays a set of slopes. It stores neither the chosen
co-support `T` nor the common-core mark `G`.

The marked top-seam packet of Vadim Avdeev has the opposite unit: it records
support data such as `(r,c,U0,G,H,M_plus,M_minus)`. The examples below make
the missing rooting and multiplicity data explicit.

## Exact toy parameters

Work on `D=F_17^*` with the Reed--Solomon code of degree below `k=5`.
Set

```text
n = 16
A = 8
j = n-A = 8
t = A-k = 3
3(t-1) = 6 <= 11 = n-k.
```

Thus the example lies inside the numerical deep-owner gate. On `F_17^*`,
the standard dual weights are `lambda_x=-x`, so the owner matrix for an
error with unit amplitudes is

```text
M_E[a,b] = -sum_(x in E) x^(a+b+1),
0 <= a < 3, 0 <= b < 9.
```

Use the locator-prefix target `z=(1,9)`. It has trivial multiplicative
stabilizer, and its fiber contains exactly `49` eight-supports.

## Theorem 1: displayed support data do not determine rank eligibility

Fix the top-seam reference and chosen co-support

```text
B = (1,8,10,11,12,13,14,15)
T = (1,3,5,9,10,11,13,15)
G = B intersect T = (1,10,11,13,15).
```

Both `B` and `T` have target `z=(1,9)`, their one-sided distance is
`r=3`, and their side locators differ by the nonzero constant cell `c=2`.
Thus `(B,T,G,c)` is one fixed displayed marked top-seam datum. It is not the
complete Route-D weighted packet key.

Let the common line direction be `g(x)=x^5`. Compare two source lines whose
base words are the indicators of

```text
E_2 = (1,3)
E_3 = (1,3,5).
```

Both error supports lie in the same chosen co-support `T`. At `gamma=0`,
the zero codeword explains each base word on the exact agreement support
`S=D minus T`. The line is noncontained on `S`: if `x^5` agreed with a
polynomial of degree below five on the eight points of `S`, their nonzero
degree-five difference would have eight roots.

The exact dual-weighted owner matrices are:

```text
M_E2 =
13  7  6  3 11  1  5  0  2
 7  6  3 11  1  5  0  2  8
 6  3 11  1  5  0  2  8  9

M_E3 =
 8 16  0  7 14 16 12  1  7
16  0  7 14 16 12  1  7 16
 0  7 14 16 12  1  7 16 15.
```

Every maximal minor of `M_E2` vanishes and a `2 x 2` minor is `12`, so
its rank is exactly two. The leading `3 x 3` determinant of `M_E3` is
`2`, so its rank is three.

Therefore the same displayed marked support datum is owner-eligible for one
received line and full-row-rank for the other. No predicate of that displayed
datum alone can decide the field-native rank-drop condition. An adapter must
attach the received line and actual error witness.

This does not refute a future canonical construction that derives a received
line from the complete weighted packet or richer residual data. It proves only
that the displayed support datum does not already contain the required
information.

## Theorem 2: one slope can carry more than p marked witnesses

Keep the same reference `B`. Inside the primitive target fiber there are
exactly `19` supports `T_i` at one-sided distance three from `B`. Their
common-core marks

```text
G_i = T_i intersect B
```

are pairwise distinct. Every side-locator difference is a nonzero constant.
The cell histogram is:

```text
{1:2, 2:1, 3:2, 4:1, 5:1, 6:2, 7:2,
 11:2, 14:2, 15:2, 16:2}.
```

Now fix one received line:

```text
f = 0
g(x) = x^5.
```

For every mate `T_i`, take the exact agreement support
`S_i=D minus T_i`. At `gamma=0`, the zero codeword explains the received
word and the actual error is empty, so the owner matrix is zero and has rank
below three. Noncontainment again follows from the degree-five root bound.

Moreover `gamma=0` is the only finite MCA-bad slope for this line. If
`gamma` were nonzero and `gamma*x^5` agreed with a degree-below-five
polynomial on eight points, a nonzero degree-five polynomial would have eight
roots.

Hence the exact bad-slope set is `{0}`, while the same primitive target has
`19` distinct marked top-seam witnesses above that slope. Since
`19 > 17=p`, there is no injection from all these raw marked witnesses into

```text
{0} times F_17.
```

This does not contradict the owner: it correctly deduplicates the slope and
charges it once. The `19` witnesses are padded exact-agreement witnesses for
the full-agreement error `E=empty`; a canonical exact-support selector may
retain only one. They may also be removed by an earlier full-agreement or
other first-match branch. The example refutes only selector-free emission of
all marked witnesses to the slope owner.

## Minimal viable rooted-emission lemma

For each deployed primitive target `z`, a support payment through the
rank-drop owner needs the following new theorem.

1. Fix one received line `(f_z,g_z)`.
2. Define the marked residual set `V_z` only after executable exact
   first-match deletion.
3. For every packet in `V_z`, construct an actual finite slope, exact
   agreement support, explaining codeword, and actual error support.
4. Prove noncontainment and `rank M_A(gamma)<t`.
5. Construct an injection

```text
V_z -> Z_rankdrop(f_z,g_z) times F_p.
```

6. Recover the complete marked key, including `G`, from the full pair
   `(owner label, F_p label)`, not from the slope alone.

The existing owner then gives

```text
|V_z| <= |Z_rankdrop(f_z,g_z)| * p <= t * p.
```

If such an injection is false, the surplus fibers require an independent
support-multiplicity owner. Membership in the rank-drop slope set alone is not
a support payment.

## Nonclaims

- The `19` packets are not claimed to survive the deployed first-match
  deletion order.
- No equality between a Route-D RIM pivot and the field-native owner Hankel
  predicate is asserted.
- No deployed target exceeds `67472 * 2130706433`.
- The examples concern finite slopes only.
- The distinct-slope theorem `DEEP_MCA_RANK_DROP` is not refuted.
- No submission-facing theorem is changed.

## Reproduction

```bash
python3 experimental/scripts/verify_route_d_rooted_emission_no_go.py --check --self-test
cd experimental/lean/kb_rowsharp_route_d_rooted_emission_no_go
lake build
```

The Python verifier recomputes the target fiber, the `19` marked top-seam
mates, cell histogram, exact owner matrices and ranks, deep-gate arithmetic,
unique bad slope, owner-contract fields, and fail-closed mutations. The Lean
companion kernel-checks the finite arithmetic and matrix-minor certificates.
Its rooted-emission theorem is an explicit bookkeeping target, not a
formalization of actual MCA incidence.
