# Rank-16 integer-subcore residual owner

**Claim:** Conditional on the first-match ledger in pending PR #861, an
append-only integer-subcore owner has cap `6,363,455,582,517`, raising the
deployed rank-16 `c=0` paid subtotal to `274,854,110,496,187,589 = T-3`.

**Status:** Proved as a finite conditional owner theorem. This does not bound
the population outside the expanded owner by three and does not close the
rank-16 parent.

**Verifier:**
`experimental/scripts/verify_rank16_integer_subcore_owner.py` reconstructs
the integrated #838 baseline and pending #861 ledger, then checks every new
integer, cell rank, canonical subcell rank, and first-match exclusion.

**Consumers:** The deployed base-field rank-16 `c=0` finite ledger after
pending PR #861.

**Risk limits:** The theorem is tied to the printed finite row and to audited
PR #861 head `bc04696d8ebbc4103463a41c3d7a68b4cc202c5a`; it removes no whole
profile and proves neither an asymptotic statement nor either official prize
question.

## Setup

Use the deployed constants

```text
p = 2,130,706,433        n = 2,097,152
K = 1,048,576            m = 1,116,047
B = 32,768               T = 274,854,110,496,187,592.
```

For one arbitrary normalized received word `U`, fix a total order on the
evaluation subgroup. For each list polynomial `P`, let `S_P` be its first
exactly `m` agreement points and `E_P` its complement. Let `B_0,...,B_63`
be the fixed level-15 blocks and define

```text
A(P) = {i : B_i is contained in S_P},
F(P) = {i : B_i is contained in E_P}.
```

This note concerns the exact `|A(P)|=31` cells left after pending PR #861.
The first-match order inherited from that PR is

```text
D -> Q110 -> M -> Q41 -> X175 -> J48.
```

The pending paid subtotal is `274,847,747,040,605,072`; its exact remaining
allowance is `6,363,455,582,520` across 1,641 profile labels.

## Fixed lower-subcore lemma

Fix an exact 31-block agreement set `A` and a disjoint set `G` of complete
error blocks. Then

```text
|G| = 25:  #{P : A(P)=A and G subset F(P)} <= 11,
|G| = 26:  #{P : A(P)=A and G subset F(P)} <= 5,
|G| = 27:  #{P : A(P)=A and G subset F(P)} <= 2.
```

Indeed, after deleting the fixed agreement blocks, every residual agreement
set has size

```text
a = m - 31B = 100,239
```

and two such sets intersect in at most

```text
h = K - 1 - 31B = 32,767.
```

For `r` residual sets in an `N`-point universe, write `d_x` for the number
containing `x`. If `ra=qN+rho`, integer convexity gives

```text
sum_x binom(d_x,2) >= N*binom(q,2) + rho*q,
sum_x binom(d_x,2) <= binom(r,2)*h.
```

The first forbidden values give strict contradictions:

| `|G|` | `N` | forbidden `r` | integer lower | pair upper | margin |
|---:|---:|---:|---:|---:|---:|
| 25 | 262,144 | 12 | 2,190,032 | 2,162,622 | 27,410 |
| 26 | 229,376 | 6 | 514,740 | 491,505 | 23,235 |
| 27 | 196,608 | 3 | 104,109 | 98,301 | 5,808 |

## Coupled fixed-`A` caps

Fix `A` and put `V=[64] minus A`, so `|V|=33`. For exact `f64=27`, write
`C=V minus F(P)`, so `|C|=6`, and let `x_C` be the population with that
exact complement. For every 8-subset `D` of `V`, the 25-core lemma gives

```text
sum_{C subset D, |C|=6} x_C <= 11.
```

Let `delta_D` be the nonnegative integer deficit. For every 10-subset `W`,

```text
sum_{D subset W, |D|=8} delta_D
  = 11*binom(10,8) - binom(4,2)*sum_{C subset W} x_C
  = 495 - 6X_W >= 3.
```

Every 8-set lies in 300 such 10-sets. Hence

```text
Delta := sum_D delta_D >= ceil(3*binom(33,10)/300) = 925,611.
```

Every 6-set lies in 351 8-sets, so

```text
351*sum_C x_C = 11*binom(33,8) - Delta,
sum_C x_C <= 432,478.
```

For exact `f64=26`, the complement has size seven. Summing the same 8-set
deficits over a 9-set gives the nonnegative odd integer `99-2X_W`, hence at
least one. Each 8-set lies in 25 9-sets, so

```text
Delta >= ceil(binom(33,9)/25) = 1,542,684,
26*sum_C x_C = 11*binom(33,8) - Delta,
sum_C x_C <= 5,814,732.
```

These are coupled caps over all lower cores for one fixed exact `A`; no
generator, ray, or isolated-core multiplicity is multiplied.

## Canonical append-only owner

The verifier reconstructs the exact dyadic pattern counts and the #861
Johnson-cell order. The following cells are outside `D` because `e15=31` and
`e16<=15`, outside `Q110/Q41` because those owners use `e15=32`, outside
`M/X175` because those owners use `f64=29/28`, and outside `J48` because their
Johnson ranks are 51, 53, and 50 respectively.

Own the two whole cells

```text
(31,14,7,0,0,0), f64=27:
  6,684,672 * 432,478 = 2,890,973,577,216,

(31,15,6,2,1,0), f64=27:
  7,833,600 * 432,478 = 3,387,859,660,800.
```

Their combined charge is `6,278,833,238,016`.

The next cell is `(31,15,6,3,1,0), f64=26`. It has 783,360 exact agreement
patterns and whole-cell cap `4,555,028,459,520`. Order its patterns by the
recursive ordered state-pair order implemented by the verifier. Own its first
14,553 exact `A` patterns, charging

```text
14,553 * 5,814,732 = 84,621,794,796.
```

For the next pattern `A*`, order the 26-subsets of its 33-label complement
lexicographically and own the first 109,941 fixed-`F` buckets. The fixed
26-core cap charges `109,941*5=549,705`.

The total append-only charge is therefore

```text
6,278,833,238,016 + 84,621,794,796 + 549,705
  = 6,363,455,582,517.
```

Adding it to #861 gives `T-3`. Exact `A` buckets are disjoint, and fixed `F`
buckets inside one exact `A` are disjoint, so no candidate is charged twice.

The first unpaid bucket is

```text
profile=(31,15,6,3,1,0), f64=26,
A-rank=14,554,
A*={6,7,22,23,32,33,34,35,36,37,38,39,40,41,42,43,
    44,45,46,47,48,49,50,51,52,53,54,55,56,57,62},
F-rank=109,942,
F*={0,1,2,3,4,5,8,9,10,11,12,13,16,17,19,20,
    24,26,28,29,30,58,59,60,61,63}.
```

## Exact remaining wall

The expanded owner has an allowance of three, but this theorem does **not**
prove that at most three candidates remain outside it. A consumer still needs
a source-valid cap on the complement of the expanded owner, beginning with
the printed `(A*,F*)` bucket. No rank-16 parent, Grand List theorem, Grand MCA
theorem, or official score change follows.
