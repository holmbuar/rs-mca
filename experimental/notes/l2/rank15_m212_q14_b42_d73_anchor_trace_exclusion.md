# Rank-15 `D=73` anchor-trace exclusion

Claim: No set of 27 points in an affine plane contains a 10-point line and
eight distinct 6-point lines.  Therefore the exact `D=73` affine-direction
object left open by the integrated `D=69..72` arrangement theorem does not
exist.

Status: **PROVED / CONDITIONAL ARRANGEMENT INTERFACE / FIELD-INDEPENDENT
LEMMA / FIELD-SPECIFIC CONSUMER.**

Verifier: `experimental/scripts/verify_rank15_m212_q14_b42_d73_anchor_trace_exclusion.py`
pins the integrated `OPEN_D73` source record and checks the exact spectrum and
the `29>28` arithmetic.  The geometric proof is the argument below.

Consumers: This extends the conditional arrangement exclusion from
`D=69..72` to `D=69..73`.  It does not construct the arrangement from a
Reed--Solomon child.

Risk-limits: No source transport, first-match ownership, child payment,
recurrence-parent payment, Grand List theorem, Grand MCA theorem, or official
score movement is claimed.  The immediate conditional geometry wall is
`D=74`; the independent source interval remains unpaid.

## Anchor-trace packing theorem

Let `U` be a finite set of `N` points in an affine plane.  Suppose a line `L`
contains exactly `a<N` points of `U`, and let `M_1,...,M_b` be pairwise
distinct lines, all different from `L`.  Let `s_1,...,s_b` be positive
integers with

```text
|M_i intersect U| >= s_i.
```

Put

```text
v = N-a,
I = sum_i (s_i-1),
I = qv+r,  0 <= r < v.
```

Then necessarily

```text
(v-r) C(q,2) + r C(q+1,2) <= C(b,2).                 (1)
```

### Proof

Let `V=U\L`.  Since `M_i` and `L` are distinct affine lines, they meet in at
most one point.  Hence `(M_i intersect U)\L` has at least `s_i-1` points.
Choose a subset `E_i` of exactly that size.

For `x in V`, let `d_x` be the number of selected sets `E_i` containing `x`.
Then

```text
sum_(x in V) d_x = I.                                  (2)
```

Two distinct affine lines meet in at most one point, so

```text
sum_(x in V) C(d_x,2)
  = sum_(i<j) |E_i intersect E_j|
  <= C(b,2).                                            (3)
```

For a fixed sum in (2), the left side of (3) is minimized when the `v`
degrees differ by at most one: if `d_x >= d_y+2`, replacing them by
`d_x-1,d_y+1` decreases the sum by `d_y-d_x+1<0`.  Thus the minimum is
attained by `v-r` entries equal to `q` and `r` entries equal to `q+1`.
Substitution in (3) proves (1).

## The exact `D=73` object

The integrated arrangement theorem leaves one `D=73` profile.  After its
proved projective duality step, the remaining object is a 27-point affine set
with block spectrum

```text
10^1, 6^11, 5^1, 4^1, 3^1, 2^122, 1^73.
```

The integrated source packet checks

```text
number of occupied lines = 210 = 15*14,
point-line incidences     = 405 = 15*27,
determined pairs          = 351 = C(27,2),
```

and marks this exact profile `OPEN_D73`.

Take the 10-point line as `L`, and select any eight of the eleven distinct
6-point lines.  The anchor-trace theorem has

```text
N=27, a=10, v=17, b=8, I=8*(6-1)=40=2*17+6.
```

Its left side is therefore

```text
11*C(2,2) + 6*C(3,2) = 11+18 = 29,
```

while its right side is `C(8,2)=28`.  This would require `29<=28`, a
contradiction.  Thus the exact `D=73` object does not exist.

Using all eleven 6-point lines gives the redundant check

```text
I=55=3*17+4,
13*C(3,2)+4*C(4,2)=63 > C(11,2)=55.
```

## Exact impact and remaining wall

Combining this theorem with the integrated arrangement packet gives the
conditional geometry statement

```text
D not in {69,70,71,72,73}.
```

Only `D=73` is new here; `D=69..72`, the terminal `D=73` profile, and its
affine dual spectrum are inherited from the packet integrated from PR #848 in
commit `168e9ba0`.  The convex pair-capacity kernel is also an
anchor-localized form of the repository's earlier subset-pair argument.  The
nonduplicative theorem layer is the restriction to the 17 off-anchor points
and its `29>28` exclusion of the formerly open `D=73` object.

The word *conditional* is load-bearing.  The repository still has no theorem
that maps every child in the motivating rank-15 source interval to the
42-line arrangement with the required first-match owner.  Consequently this
packet pays zero source children and zero recurrence parents.

The immediate conditional geometry wall is `D=74`.  Separately, the literal
Reed--Solomon source compiler and consumer remain required across
`u=1,043,592..1,043,916` (325 states) before any of the arrangement exclusions
can be charged to the finite ledger.

## Nonclaims

This note does not claim:

- exclusion or realization of any `D>=74` profile;
- a Reed--Solomon received-word, syndrome, or arrangement compiler;
- first-match ownership;
- `D_2(u)<=211` for a new child;
- a recurrence-parent payment;
- an all-rank or capacity-adjacent theorem;
- Grand List, Grand MCA, or official score movement.
