# Rank-16 global `c=0` residual payment

Claim: For the deployed base-field row and one arbitrary normalized received
word, after the integrated first-match owners `D`, `Q110`, and `M`, three
deterministic owners `Q41`, `X175`, and `J48` are first-match disjoint. Their
new cap charge is `178244340267914072`; the paid subtotal becomes
`274847747040605072`, leaving residual allowance `6363455582520` across
exactly 1,641 truncated profiles.
Status: PROVED finite source-valid ledger theorem and exact certificate. No
rank-16 parent, Grand List theorem, Grand MCA theorem, or official score
change is claimed.
Verifier: `experimental/scripts/verify_rank16_global_c0_residual_payment.py`
independently reconstructs the 64-leaf dyadic census, the integrated `#838`
residual CSV, all new owner rows, the six fixed-`(A,F)` Johnson constants,
the exact frontiers, and two reviewable ledgers using only the Python standard
library.
Consumers: The deployed rank-16 degree-saturated `c=0` compiler may charge
these owners once, globally for one received word, before any generator,
syndrome, or projective-ray partition.
Risk-limits: The theorem is tied to the exact deployed row. It does not prove
a uniform cap on any remaining profile or justify multiplying a local result
by generators or rays.

## Deployed source and integrated baseline

Work over `F_p` with

```text
p = 2130706433, n = 2097152, K = 1048576,
m = 1116047, t = n-m = 981105.
```

Let `H <= F_p^x` be the order-`n` evaluation subgroup. For one arbitrary
normalized received word `U : H -> F_p`, let

```text
L(U) = {P in F_p[X] : deg(P)<K and |Agr(U,P)|>=m}.
```

Fix a total order on `H`. For each `P in L(U)`, let `S_P` be its first exactly
`m` agreement points and let `E_P=H\S_P`. This canonical selection makes every
`S_P` and `E_P` a fixed-size source object.

The integrated theorem `rank16_global_c0_first_match_ledger.md` supplies the
literal first-match order

```text
D -> Q110 -> M
```

with paid subtotal

```text
96603406772691000
```

against target

```text
T = 274854110496187592.
```

Its residual allowance is `178250703723496592`. It leaves 1,682 nested
dyadic profiles, and its canonical CSV has exactly 22,614 bytes. Removing the
24-byte header gives a 22,590-byte row stream. The verifier regenerates both:

```text
row stream SHA-256:
7dfa0fba111addf8ef4568821e2ce451de094c1ccef5de3468e80bd7e0373cfe

complete CSV SHA-256:
83413c33cbea4f7d3cf7d6aeeb8b7a034317b443e80c1617323a94fdd13220e2
```

It also compares the regenerated CSV byte-for-byte with the integrated `#838`
certificate rather than accepting either digest as an input.

## Exact new owners

Write a residual agreement profile as

```text
pi = (e15,e16,e17,e18,e19,e20),
```

where `e15` counts complete 32,768-point agreement blocks and the remaining
entries count their complete dyadic parents.

### The complete-profile owner `Q41`

Among the 56 unpaid `e15=32` profiles, order profiles by exact 32-of-64
dyadic pattern count, breaking ties lexicographically by `pi`. Let `Q41` be
the first 41 complete residual profile buckets. Then

```text
|Q41| <= 165153328111550464.
```

The next profile is `(32,10,0,0,0,0)`, with cap
`21719537074307072`. The sum through 42 profiles is
`186872865185857536`, already `8622161462360944` above the original `#838`
allowance. Thus 41 is the maximal prefix for this complete-profile payment.

### The nonpaired top-cell owner `X175`

Outside `Q41`, order nonpaired exact-`f64=28` cells by their exact cap,
breaking ties lexicographically by `pi`. Let `X175` be the first 175 cells.
Their raw cap sum is

```text
x = 13253558241240832.
```

Let

```text
C  = binom(64,28),
P0 = binom(32,14),
F(x) = P0+x+floor((C-P0-x)/29).
```

The exact joint mixed-shadow charge is

```text
F(x) = 51374825411730344,
F(x)-F(0) = 12796538991542872.
```

The next cell has profile `(31,13,6,2,1,0)`, raw cap
`423894739968000`, and incremental shadow charge `409277679969103`.
Adding it after `Q41` would exceed the available allowance by
`108441059565847`.

### The lower-cell owner `J48`

Outside `Q41`, order all exact-`f64<=27` cells for which the fixed-`(A,F)`
second-moment denominator is positive by exact cap, breaking ties by `pi` and
then `f64`. There are 1,696 such cells. Let `J48` be the first 48. It contains
38 `f64=27` cells and 10 `f64=26` cells, and

```text
|J48| <= 294473164820736.
```

The next cell is `pi=(30,15,5,2,1,0), f64=27`. Its local multiplicity cap is
5 and its total cap is `19087738306560`, larger than the final residual.

## Proof

### 1. Exact dyadic pattern count and `Q41`

The 64 level-15 blocks are the leaves of a fixed binary tree. Starting with
one empty and one full leaf, join ordered left/right states six times. A join
adds leaf weights and all existing complete-node counts and appends one when
the joined node is full. This counts every leaf subset exactly once and
reconstructs all 1,792 admissible residual profiles.

For a fixed `e15=32` profile, map each list polynomial to its set of 32
complete level-15 agreement blocks. The map is injective: if distinct
`P,Q` had the same 32 blocks, then `P-Q` would vanish on

```text
32*32768 = 1048576 = K
```

points despite having degree at most `K-1`. Hence a fixed profile contains at
most its exact leaf-pattern count. The integrated `Q110` criterion removes
exactly 110 profiles first; sorting the 56 remaining counts proves the `Q41`
cap and frontier.

### 2. Profile-sensitive nonpaired `f64=28` cap

Fix one exact agreement pattern `A` with profile `pi` and put `e=e15`. An
error label set `F` of size 28 must be disjoint from `A`, giving
`binom(64-e,28)` choices. Among the 32 natural level-16 pairs, exactly
`e-e16` pairs meet `A`; therefore `32-e+e16` pairs are untouched. The exact
number of nonpaired choices is

```text
d_pi = binom(64-e,28)-binom(32-e+e16,14).
```

Distinct candidates cannot have the same 28 complete error blocks. Indeed,
their canonical complements satisfy

```text
|E_P intersect E_Q| <= n-2m+K-1 = 913633,
```

whereas 28 common blocks contain `28*32768=917504` points. Thus a profile
with `a_pi` exact agreement patterns has nonpaired `f64=28` population at
most `a_pi*d_pi`. Sorting these caps gives `X175` and its frontier.

### 3. Joint `M union X175` shadow payment

Every `f64=29` candidate owns 29 distinct 28-shadows. A paired `f64=28`
candidate owns one of the `P0` paired shadows, and an `X175` candidate owns
one nonpaired shadow. The same intersection calculation makes all these
28-shadows unique across distinct candidates. Therefore, for `|X|=z`,

```text
29*N29 + N28_paired + z <= C,
N28_paired <= P0.
```

The maximum of `N29+N28_paired+z` is `F(z)`. Since `F` is nondecreasing and
`|X175|<=x`, the joint owner has cap `F(x)`. This is one joint charge, not
separate overlapping payments for `M` and `X175`.

### 4. Fixed-`(A,F)` second moment and `J48`

Fix a complete agreement-label set `A` of size `e` and a disjoint complete
error-label set `F` of size `f`. Remove the `e` complete agreement blocks
from each canonical agreement set. The remaining sets have size

```text
a = m-eB
```

inside a universe of size

```text
N_e,f = (64-e-f)B,
```

and any two intersect in at most

```text
h = K-1-eB.
```

For `r` such sets, let `d_x` count sets containing point `x`. Then

```text
sum_x d_x = r*a,
sum_x d_x(d_x-1) <= r(r-1)h,
sum_x d_x^2 >= r^2*a^2/N_e,f.
```

If `D_e,f=a^2-N_e,f*h>0`, rearrangement gives

```text
r <= J_e,f
  := floor(N_e,f*(a-h)/(a^2-N_e,f*h)).
```

For a fixed agreement pattern there are `binom(64-e,f)` disjoint choices of
`F`, so an exact profile cell has cap

```text
a_pi*binom(64-e,f)*J_e,f.
```

The selected cells use exactly these six local rows:

```text
 e  f      a       N       h          D       J
28 27 198543  294912  131071   764912097     26
29 27 165775  262144   98303  1711808993     10
30 27 133007  229376   65535  2658705889      5
31 27 100239  196608   32767  3605602785      3
30 26 133007  262144   65535   511255009     34
31 26 100239  229376   32767  2531893729      6
```

The deterministic lower-cell sort proves the `J48` cap and frontier.

### 5. First-match disjointness

The literal owner order is

```text
D -> Q110 -> M -> Q41 -> X175 -> J48.
```

`Q41` takes whole residual profile buckets after `M`. `X175` uses only
nonpaired exact-`f64=28` cells outside `Q41`. `J48` uses only exact
`f64=27` or 26 cells outside `Q41`. Different profiles and different exact
`f64` values are disjoint. The `M union X175` quantity is the single joint
shadow bound proved above. Hence no candidate is charged twice.

## Exact ledger impact

```text
Existing owner D                 57121027290597096
Existing owner Q110               904093061906432
Joint owner M union X175         51374825411730344
New owner Q41                   165153328111550464
New owner J48                      294473164820736
                                  ------------------
Paid subtotal                   274847747040605072
Target                          274854110496187592
Residual allowance                 6363455582520
```

Only `Q41` removes whole profiles, so 1,641 truncated profiles remain, and

```text
6363455582520 = 1641*3877791336 + 144.
```

A uniform cap `3877791336` on each remaining truncated profile would close
this ledger; a list of size `T+1` forces one bucket to contain at least
`3877791337` candidates.

## Nonclaims and exact remaining wall

This theorem does not prove a rank-16 parent closure, a uniform cap on all
remaining profiles, emptiness of any profile, the fixed-27 cap 6, the
fixed-26 cap 116, any generator/ray multiplication, an asymptotic theorem,
Grand List, Grand MCA, or an official score change. It makes no claim about
the unavailable worker executable hashes; all repository artifacts and
hashes are newly generated.

The exact remaining global obligation is

```text
sum of all unpaid profile/cell populations <= 6363455582520.
```

The ordinary pattern-count and fixed-`(A,F)` second-moment prefixes are
exhausted: their next cells already exceed the available residual. Further
movement requires a simultaneous source constraint across many error-label
sets, such as an exact global dual coupling 28-shadow capacities, agreement
profiles, fixed-syndrome or locator-prefix equations, and lower-`f64` cells.
