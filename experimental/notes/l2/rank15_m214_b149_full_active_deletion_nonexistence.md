# Full active-deletion theorem for at least 149 marked 15-fold points and at most 214 lines

## Theorem

Let `F` be a field of characteristic zero or characteristic greater than
`214`.  There is no projective line arrangement satisfying

```text
149 <= b <= d <= 214,
d distinct active lines,
b distinct marked points,
exactly 15 arrangement lines through every marked point,
at least one marked point on every arrangement line.                  (1)
```

Consequently, there is no arrangement of 214 lines, active or inactive, with
at least 149 marked 15-fold points: delete every line containing no marked
point and apply the theorem to the retained degree `d`.

All geometric arguments below are algebraic in the stated characteristic
range.  We may extend scalars to an algebraic closure without changing
incidence multiplicities or Jacobian-syzygy dimensions.

## 1. Incidence, Tjurina, and du Plessis--Wall ledger

On an active line, distinct marked points use disjoint sets of fourteen other
lines.  If `k_L` is the number of marked points on a line `L`, then

```text
1 <= k_L <= floor((d-1)/14) <= 15.
```

Counting marked incidences gives `15b=sum_L k_L<=15d`, exactly the numerical
range in (1).  Put

```text
e_L=15-k_L,                         0<=e_L<=14.
```

For every residual, nonmarked intersection `R`, let `mu_R` be its
multiplicity and set

```text
E=sum_R C(mu_R-1,2).
```

Pair counting, marked-incidence counting, and the ordinary multiple-point
Tjurina formula give

```text
tau=C(d,2)+91b+E,                                      (2)
sum_L e_L=15(d-b),                                     (3)
residual-neighbour degree on L=d-211+14e_L.            (4)
```

Every multiplicity is less than the characteristic.  Locally, a reduced
ordinary `mu`-fold point is a product of `mu` distinct linear forms; Euler's
identity makes its Tjurina ideal the complete intersection of the two partial
derivatives, of length `(mu-1)^2`.  Thus (2) is field-uniform here.

Let `r=mdr(f)` for the reduced line product.  The algebraic
du Plessis--Wall inequalities are

```text
tau <= (d-1)^2-r(d-1-r),                               (5)
tau <= (d-1)^2-r(d-1-r)-C(2r-d+2,2),  if r>=d/2.       (6)
```

For completeness, a minimal degree-`r` section of the rank-two syzygy bundle
has quotient `I_Z(2r-d+1)` and

```text
length Z=(d-1)^2-tau-r(d-1-r)>=0.
```

This proves (5).  In the high branch, twist down once.  Minimality gives
`H^0(I_Z(2r-d))=0`, so `length Z>=C(2r-d+2,2)`, proving (6).  No comparison
with a complex arrangement is used.

## 2. Factoring bad lines

A minimal syzygy induces a nonzero section

```text
s in H^0(P^2,T_P2(r-1))
```

tangent to every arrangement line.  Call a line bad if `s` vanishes
identically on it.  Divide the product of the `B` bad-line equations.  The
quotient restricts nontrivially to each of the `G=d-B` good lines as a section
of

```text
O_P1(q),                         q=r+1-B.               (7)
```

In fact `B<=r`: the boundary `B=r+1` would leave a nonzero section of
`T_P2(-2)`, but its `H^0` vanishes by the Euler sequence.

Let

```text
E_g = sum of e_L over the good lines,
K   = number of marked incidences on bad lines,
C   = sum_marked C(j,2),
```

where `j` is the number of incident bad lines at a marked point.  Exact double
counting gives

```text
K=15B-15(d-b)+E_g,                                     (8)
X=BG-14K+2C,                                           (9)
```

where `X` is the number of residual bad-good pairs.  A marked quotient zero
can disappear only at type `j=14`; if `z` is the number of such exceptions,

```text
z<=min(floor(C/91),floor(K/14),15G-E_g).               (10)
```

The first exact scan enumerates every integer `149<=b<=d<=214`, every
DPW-admissible `r`, every `0<=B<=r+1`, and every allowed `E_g`.  It uses
(8)--(10) only permissively: `C`, residual bad-good pairs, and erased zeros
are independently maximized, and a negative relaxed good-good degree is
clamped to zero.  Every actual arrangement therefore remains in the relaxed
surviving set.

The sharp high branch (6) has no survivor.  The low scan leaves exactly

```text
84,460 coarse (b,d,r,B) rows, with B<=46.              (11)
```

## 3. Finite-linear-space and design cuts

Use the good lines as points and their good-good intersections as blocks.  No
coarse survivor has a full good-line pencil.  Indeed, the scan checks `G>15`.
A full pencil cannot be marked, so every marked point would contain at least
fourteen bad lines, forcing `91b<=C(B,2)`, which is false statewise.

Choose a good line outside a block.  Its intersections with the block lines
are distinct zeros of a nonzero `O_P1(q)` section.  Hence every block has size
at most `q`; every point lies on at most `q` blocks.  Since every pair of good
lines has a unique intersection block,

```text
G-1<=q(q-1),             hence G<=q(q-1)+1.            (12)
```

This eliminates `23,635` rows from (11), leaving

```text
60,825 structural rows =211 with B=0 +60,614 with B>0. (13)
```

If `q=15` and `G>=198`, every point lies on at least
`ceil((G-1)/14)=15` blocks and hence on exactly fifteen.  The intersection
space is a `(15,1)`-design.  Vanstone's embedding theorem, in the form
allowing singleton lines, embeds such a design with

```text
G>(15-1)^2-1=195
```

in a projective plane of order 14.  Bruck--Ryser forbids that plane because
`14=2 mod 4` is not a sum of two squares.  This cuts `659` positive-`B` rows
and `175` zero-`B` rows after the later joint scan.

We shall also use the equality case of (12).

### Embedded equality-plane lemma

If a finite linear space is realized by points and lines in `P^2(F)`, every
block and every replication number is at most `q`, and it has

```text
v=q(q-1)+1
```

points, then it is an embedded projective plane of order `q-1`.  Indeed, for
every point `P`,

```text
v-1=sum_(blocks L through P)(|L|-1)<=q(q-1).
```

Equality forces exactly `q` blocks of size `q` through every point.  The
resulting symmetric linear space is a projective plane of order `q-1`.

If this order is finite and equal to `n`, then `F` has a subfield with `n`
elements.  Here is a self-contained coordinatization argument.  Choose a
quadrangle in the embedded subplane and projectively send it to the standard
affine frame

```text
O=(0,0), U=(1,0), V=(0,1), I=(1,1),
```

with the standard line at infinity.  Let

```text
S={a in F : (a,0) is a point of the subplane}.
```

The subplane's `x`-axis has `n+1` points, one at infinity, so `|S|=n` and
`0,1 in S`.  Joins and intersections inside the subplane give explicit field
operations:

* the direction of the line `UV` has slope `-1`; using a parallel of that
  direction transfers `(a,0)` to `(0,a)`;
* from `(a,0)` and `(0,b)`, take their vertical/horizontal intersection
  `(a,b)` and then the slope-`-1` parallel back to the `x`-axis, obtaining
  `(a+b,0)`;
* the line through `(1,0)` and `(0,b)` has direction `(1,-b,0)`; its parallel
  through `(a,0)` meets the `y`-axis at `(0,ab)`, which transfers back to
  `(ab,0)`;
* for `a!=0`, the line through `(a,0)` and `(0,1)` has direction
  `(a,-1,0)`; its parallel through `(1,0)` meets the `y`-axis at `(0,a^-1)`,
  which again transfers back to the `x`-axis.

The slope-`1` direction similarly gives additive inverses.  Thus `S` is a
finite subfield of `F` of order `n`.

In particular, an embedded projective plane of order 13 forces a 13-element
subfield and therefore characteristic 13.  It cannot occur in characteristic
zero or characteristic greater than 214.

## 4. Exhaustive joint-`C` deletion scan

For `B>0`, delete the bad lines.  The quotient section gives a good-arrangement
syzygy of degree `r-B`.  It is minimal: a smaller deletion syzygy multiplied
by the bad-line product would contradict minimality of the parent.  Therefore

```text
mdr(good)=r-B=q-1.                                     (14)
```

At a marked point with `j` bad lines, its deletion marked excess is
`C(14-j,2)`.  Since

```text
C(14-j,2)=91-13j+C(j,2),       0<=j<=14,
```

and the expression overcounts by one only at `j=15`, its total `A` satisfies

```text
A>=91b-13K+C-floor(C/105).                             (15)
```

The same integer `C` is used simultaneously in (9), (10), and (15), over the
complete relaxed interval

```text
max(0,ceil((14K-BG)/2)) <= C <= min(C(B,2),7K).        (16)
```

After subtracting exact residual bad-good pairs, the oriented good-good
residual degree is at least

```text
M_gg=max(0,G(d-211)+14E_g-X).                          (17)
```

The residual block-incidence capacity is at most

```text
S=Gq-(15G-E_g)+z.                                     (18)
```

For an incidence with `a` other good lines in its block, assign charge

```text
phi(a)=C(a,2)/(a+1).
```

The total charge of a block is its deletion excess.  Discrete convexity shows
that the smallest total charge for oriented degree `M_gg` in at most `S`
positive parts is the exact balanced-integer-partition value `P(M_gg,S)`.
It is compared with both valid upper bounds

```text
E_G <= (d-1)^2-r(d-1-r)-C(d,2)-91b,
E_G <= (G-1)^2-(q-1)(G-q)-C(G,2)-A.                   (19)
```

The verifier enumerates all `60,614` positive-`B` structural rows and exactly

```text
2,411,034,031
```

joint integer states `(E_g,K,C)`.  The least strictly positive
lower-minus-upper margin is `1/120`.  There are `685` numerical survivors:
`659` are the `q=15,G>=198` designs already excluded in Section 3.  The other
26 rows are exactly

| parent `(d,r,B)` | `b` | `(q,G)` | rows | integer states |
|---|---:|---:|---:|---:|
| `(213,16,1)` | `149..154` | `(16,212)` | 6 | 6 |
| `(214,16,1)` | `149..160` | `(16,213)` | 12 | 12 |
| `(214,17,2)` | `149..154` | `(16,212)` | 6 | 12 |
| `(214,18,3)` | `149` | `(16,211)` | 1 | 1 |
| `(214,44,31)` | `149` | `(14,183)` | 1 | 3 |

The exact integer condition `ceil(P(M_gg,S))<=E_G` leaves 34 states.  In the
first two families they have `(K,C)=(1,0)`.  In the third family each row has
the two possibilities `(K,C)=(2,0),(2,1)`.  The fourth has `(K,C)=(3,0)`.
The last, exotic row has

```text
(K,C)=(101,455),(101,456),(101,457).                  (20)
```

But its `q=14,G=183=14*13+1` already attains equality in (12).  The equality-
plane lemma makes its good-line intersection space an embedded projective
plane of order 13, which is impossible in the advertised characteristic.
Thus all three states in (20) are eliminated at once.

## 5. All remaining rows reduce to DPW-equality terminals

Consider one of the other 31 integer states.  In every case

```text
q=16,             mdr(good)=15,
ceil(P(M_gg,S))=the deletion upper bound.              (21)
```

Moreover `K<=3`, so no type-15 marked point occurs and (15) is exact.  The
integer squeeze in (21) therefore forces equality in DPW for the deletion
arrangement.  Its lines are all good by construction.  The marked points that
remain 15-fold are counted exactly as follows:

| `(K,C)` | deleted marked pattern | surviving 15-fold points |
|---:|---|---:|
| `(1,0)` | one type `j=1` | `b-1` |
| `(2,0)` | two type `j=1` | `b-2` |
| `(2,1)` | one type `j=2` | `b-1` |
| `(3,0)` | three type `j=1` | `b-3` |

For each resulting degree `G in {211,212,213}`, this number is at least

```text
G-65.                                                     (22)
```

For `B=0`, the design cut eliminates 175 of the 211 rows.  Exactly 36 remain:

```text
d=212, r=15, b=149..153,       5 rows,
d=213, r=15, b=149..160,      12 rows,
d=214, r=15, b=149..167,      19 rows.                  (23)
```

In every row, the rational lower-minus-DPW-upper margin lies in `(-1,0]`.
The residual excess is an integer, so the lower and upper bounds squeeze it
to DPW equality.  Every row in (23) also has at least `d-65` marked 15-fold
points.  Hence all non-design residue, including the deletion states above,
is reduced to the following terminal lemma.

## 6. Uniform algebraic terminal lemma for degrees 211 through 214

Suppose

```text
211<=d<=214,
mdr=15,
every arrangement line is good,
tau=(d-1)^2-15(d-16),
there are at least d-65 marked 15-fold points.          (24)
```

No such arrangement exists.

### 6.1 Zero length and exact moments

A minimal syzygy gives a section

```text
s in H^0(P^2,T_P2(14))
```

tangent to every line.  It has no divisorial zero.  Indeed, if `s=h s'` with
`deg h>0`, no arrangement-line equation divides `h` because every line is
good.  Cancellation shows `s'` remains tangent to every line.  Lift through
the Euler sequence and subtract the logarithmic cofactor divided by the
invertible degree `d` times the Euler derivation.  This produces a Jacobian
syzygy below degree 15, contradicting minimality.

Therefore

```text
length Z(s)=c_2(T_P2(14))=241.                          (25)
```

DPW equality and pair counting give

```text
sum_P(mu_P-1)=d(d-1)-tau=16d-241.                      (26)
```

Let `n_L` be the number of distinct singularities on a line.  Restriction of
the good section is a nonzero section of `O_L(16)`, so `n_L<=16`.  Put

```text
D=sum_L(16-n_L),          I=sum_L n_L=16d-D.
```

If `Q` is the number of singularities, (26) gives

```text
Q=241-D.                                               (27)
```

Every singularity has multiplicity at most 16.  A full pencil is impossible
because (24) supplies marked 15-fold points while `d>15`; choosing a line
outside any singularity bounds its multiplicity by that line's at most sixteen
distinct intersections.

Set `epsilon_P=16-mu_P`.  Then

```text
sum epsilon_P   =3856-16d-15D,
sum epsilon_P^2 =d^2-497d+61696-225D.                  (28)
```

Remove `t` unit entries, where `t>=d-65`, and apply Cauchy to the remaining
entries.  The verifier minimizes over every integer `t` in its full allowed
interval; merely checking the endpoint `t=d-65` would not be sufficient.  The
minimum Cauchy gaps for positive `D` are

| `d` | admissible `D` | minimum gaps in increasing `D` |
|---:|---:|---|
| 211 | `1..5` | `9735,22294,34853,33489,28561` |
| 212 | `1..5` | `7132,19901,32670,27889,23409` |
| 213 | `1..4` | `4773,17754,27225,22801` |
| 214 | `1..4` | `2664,15859,22201,18225` |

All are positive.  Larger `D` is already impossible from the square sum and
the unit entries.  Therefore

```text
D=0,              Q=241,             n_L=16 for every L. (29)
```

If a double point existed, remove its `epsilon=14` entry and the unit entries,
then apply Cauchy again.  The minimum contradiction gaps for
`d=211,212,213,214` are respectively

```text
7648, 5040, 2676, 562.
```

Thus every singularity has multiplicity at least three.

### 6.2 Algebraic invariant-line residue

The 241 distinct arrangement singularities are zeros of `s`, and (25) says
that they exhaust the zero scheme with total length 241.  Hence every zero is
simple.  At least three invariant lines meet at each zero, so its invertible
two-by-two linearization has three invariant directions and is scalar:

```text
J_P=lambda_P I_2,               lambda_P!=0.            (30)
```

Let `C` be a smooth proper invariant curve of a possibly twisted vector field
on a smooth surface.  In parameters `(x,y)` with `C=(y=0)`, write

```text
v=a(x,y) partial_x+y c(x,y) partial_y.
```

At a simple zero put `lambda=partial_x a` and `nu=c`.  The algebraic
normal-bundle residue identity is

```text
sum_(zeros on C) nu/lambda=deg N_(C/X).                (31)
```

Indeed, the Bott partial connection on the normal bundle, divided by the
nonzero tangent field, has connection form `-(c/a)dx` and residue
`-nu/lambda`.  A meromorphic connection on a line bundle `N` over a smooth
proper curve has total residue `-deg N`, by the ordinary residue theorem
relative to a rational section.  This proves (31) algebraically in arbitrary
characteristic and is unaffected by the twist.

Apply (31) to an arrangement line.  It contains exactly sixteen simple zeros
by (29); every transverse/tangent eigenvalue ratio is 1 by (30); and
`N_(L/P^2)=O_L(1)`.  Thus

```text
16=1 in F,
```

so `15=0`, impossible in characteristic zero or characteristic greater than
214.  This proves the terminal lemma, eliminates (21)--(23), and completes the
theorem. QED.

## 7. Verification and exact nonclaims

Run

```text
/Users/danielcabezas/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node \
  experimental/data/certificates/rank15-m214-b149-active-deletion/verify_m214_b149_full_active_deletion_nonexistence.js
```

The verifier source-pins the independently implemented M215 hostile-audit
arithmetic engine, mechanically changes only the theorem domain and frozen
row counts, and then checks the complete M214 survivor, integer-state,
equality-plane, deletion, terminal-moment, and characteristic ledgers.  It
compares its canonical output byte for byte with the adjacent expected-output
artifact.

This is an arrangement theorem only.  A consumer must separately prove the
marked-point lower bound, exact multiplicity 15, source interval, recurrence
transport, and any claimed compiler consequence.  No affine-rank-at-least-16
or official-score claim is made here.

## 8. Audited consumer, not part of the theorem

The current unpublished rank-15 recurrence uses this theorem only after a
separate source transport proves that the relevant original-`K` two-flat
states have at least 149 marked directions.  An independent replay at shifted
row `c=57` gives the conditional consumer values

```text
raw parent interval:       1042057..1043516 (1460 parents)
cap-213 source cells:      698
unsafe parents after cap:  0
maximum:                   273549681441821776
target:                    274854110496187592
slack:                     1304429054365816
```

These numbers identify the theorem's exact intended consumer.  They are not
promoted here as an integrated recurrence theorem: the recurrence and its
source transport retain separate proof and publication ownership.
