# Rank-15 `M=212` preserve-all deletion floor

Claim: in the deployed rank-15 two-flat source interval

```text
u = 1,043,592,...,1,043,916,
```

every literal source child has at least 118--123 distinct directions carrying
a saturated 15-point source line.  After projective duality these become
distinct multiplicity-15 marked points in the full 212-line arrangement.  Any
deletion that preserves all those points must retain 161--168 lines.  In
particular, it cannot produce the conditional 42-line arrangement object.

Status: **PROVED / SOURCE-INTERFACE ROUTE CUT.**

Verifier:

```text
python3 experimental/scripts/verify_rank15_m212_preserve_all_deletion_floor.py
python3 -O experimental/scripts/verify_rank15_m212_preserve_all_deletion_floor.py
python3 experimental/scripts/verify_rank15_m212_preserve_all_deletion_floor.py --tamper-selftest
```

Consumers: source/compiler boundary only.  The theorem removes no child and
no recurrence parent.

Risk-limits: this note does not prove that the 42-line arrangement interface
is unreachable by a lossy selector.  It proves only that a selector preserving
every saturated source point is impossible.

## Source statement

Use the deployed integers

```text
p = 2,130,706,433,
n = 2,097,152,
K = 1,048,576,
m = 1,116,047.
```

Let `H` be any `n`-point evaluation set over `F_p`, let `U:H -> F_p`, and let

```text
A = P_0 + span{V_1,V_2}
```

be an exact affine two-flat of polynomials of degree less than `K`.  Suppose
its actual universal agreement set has size exactly `u`, and select 212
members of `A` having at least `m` agreements with `U`.

Put

```text
N = n-u,
a = m-u,
lambda = K-1-u,
W = 212*a - 14*N.
```

Let `t` be the number of projective directions containing at least one affine
coordinate section with exactly 15 of the selected parameter points.  Then

```text
t >= ceil(W/lambda).                                    (1)
```

If `B` of the 212 projective-dual lines are retained and every saturated
source point remains incident with all of its 15 source lines, then

```text
15*ceil(W/lambda) <= B*floor((B-1)/14).                 (2)
```

The exact consequences are:

| `u` interval | rich-direction floor | preserve-all line floor | omitted or demoted by `B=42` |
|---|---:|---:|---:|
| `1,043,592..1,043,627` | 123 | 168 | at least 118 |
| `1,043,628..1,043,691` | 122 | 167 | at least 117 |
| `1,043,692..1,043,754` | 121 | 165 | at least 116 |
| `1,043,755..1,043,815` | 120 | 164 | at least 115 |
| `1,043,816..1,043,874` | 119 | 163 | at least 114 |
| `1,043,875..1,043,916` | 118 | 161 | at least 113 |

## Proof

### Proper sections contain at most 15 selected points

On any proper affine one-flat inside `A`, two distinct parameter values can
agree with `U` at the same non-universal coordinate only if their nonzero
direction polynomial vanishes there.  If the one-flat's actual universal set
has size `v`, the remaining agreement supports are disjoint.  Hence a section
containing `L` selected polynomials satisfies

```text
L(m-v) <= n-v.
```

The ratio on the right is increasing in `v`, and a nonzero direction
polynomial has at most `K-1` roots.  Therefore

```text
L <= floor((n-(K-1))/(m-(K-1)))
  = floor(1,048,577/67,472)
  = 15.
```

The exact remainder is `36,497`, so the cap is strict below 16.

### Saturation forces many directions

Factor the two directions after the universal locator as

```text
V_1 = L_Z G A,    V_2 = L_Z G B,    gcd(A,B)=1.
```

Let `r` be the number of roots of `G` in `H\Z`, and let
`d=max(deg A,deg B)`.  The degree ledger gives

```text
d <= lambda-r.                                          (3)
```

At an active coordinate `x`, let `h_x` be the number of selected parameter
points on its agreement line.  The proper-section cap gives `h_x<=15`, while
the 212 selected polynomials contribute at least `212a` active incidences.
There are `N-r` active coordinates.  If `C` is the number with `h_x=15`, the
deficit from 15 gives

```text
C >= 212a - 14N + 14r = W+14r.                         (4)
```

For a fixed projective direction `[alpha:beta]`, its active coordinates are
roots of the nonzero polynomial `beta*A-alpha*B`, so there are at most `d` of
them.  If the `C` saturated coordinates occupy `t` directions, then (3)--(4)
give

```text
t(lambda-r) >= td >= C >= W+14r,
```

and consequently `t*lambda >= W`.  This proves (1).

### Projective duality and preserve-all deletion

The 212 selected parameter points are distinct.  Standard projective duality
sends them to 212 distinct `F_p`-rational projective lines.  Every active
coordinate section with 15 selected points becomes a multiplicity-15 marked
point, and distinct affine sections become distinct dual points.  Thus the
full dual arrangement has at least the number of marked points in (1).

Now retain `B` lines and suppose every marked point is preserved with all 15
incident source lines.  On a retained line `L`, let `k_L` count preserved
marked points.  Each uses 14 other retained lines.  The sets of 14 are
disjoint for distinct marked points on `L`, because another projective line
cannot meet `L` twice.  Hence

```text
k_L <= floor((B-1)/14).
```

Summing incidences between retained lines and preserved marked points proves
(2).  Exact evaluation of (1)--(2) gives the table.

For `B=42`, a retained line contains at most two marked points and the whole
arrangement preserves at most `floor(42*2/15)=5`.  Therefore at least 113--118
source-rich points must be omitted or demoted.

## Exact impact and remaining wall

The repository's 42-line arrangement theorems remain valid as conditional
geometry.  This theorem changes their compiler boundary: projective duality
followed by a deletion that preserves all saturated source points cannot be
the missing source transport.

Any paying compiler must instead select 42 lines lossily and prove, for every
unresolved source child, the exact arrangement invariants, nonzero
denominators, and first-match owner.  Merely observing that the retained lines
are individually `F_p`-rational is insufficient.

The finite payment is zero.  No source child, recurrence parent, Grand List
row, Grand MCA input, or official score changes.

## Nonclaims

This note does not claim:

- existence of an `M=212` source child;
- `D_2(u)<=211` for any new state;
- impossibility of every nonlinear or lossy 42-line selector;
- the `q=14`, `U=E=0`, `R=211`, or minimal-syzygy invariants from source;
- invalidity of any conditional arrangement exclusion;
- a rank-16, all-rank, asymptotic, Grand List, or Grand MCA theorem;
- an official-score movement.
