# Full active-deletion theorem for at least 164 marked 15-fold points and at most 215 lines

## Theorem

Let `F` be a field of characteristic zero or characteristic greater than
`215`.  There is no projective line arrangement satisfying

```text
164 <= b <= d <= 215,
d distinct active lines,
b distinct marked points,
exactly 15 arrangement lines through every marked point,
at least one marked point on every arrangement line.                  (1)
```

Consequently, there is no arrangement of 215 lines, active or inactive, with
at least 164 marked 15-fold points: delete every line containing no marked
point and apply the theorem to the remaining degree `d`.

The argument is algebraic in the stated characteristic range.  We extend
scalars to an algebraic closure without changing incidence multiplicities or
Jacobian-syzygy dimensions.

## 1. Complete algebraic and incidence ledger

On an active line, distinct marked points use disjoint sets of fourteen other
lines.  If `k` is the number of marked points on that line, then

```text
1 <= k <= floor((d-1)/14) <= 15.
```

Counting marked incidences gives `15b=sum k_L<=15d`, which is exactly the
range in (1).  Put

```text
e_L=15-k_L,                     0<=e_L<=14.
```

For a residual, nonmarked intersection `R`, let `mu_R` be its multiplicity
and define

```text
E=sum_R C(mu_R-1,2).
```

Pair counting, marked incidence counting, and the ordinary multiple-point
Tjurina formula give

```text
tau=C(d,2)+91b+E,                                      (2)
sum_L e_L=15(d-b),                                     (3)
residual-neighbour degree on L=d-211+14e_L.            (4)
```

Every multiplicity is below the characteristic.  Thus the local Tjurina
formula and Euler conversion between logarithmic derivations and Jacobian
syzygies are valid.

Let `r=mdr(f)` for the reduced line product.  The algebraic
du Plessis--Wall bounds are

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
`H^0(I_Z(2r-d))=0`, hence `length Z>=C(2r-d+2,2)`, proving (6).  No complex
comparison is used.

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
O_P1(q),                    q=r+1-B.                    (7)
```

In fact `B<=r`: the boundary `B=r+1` would produce a nonzero section of
`T_P2(-2)`, but its `H^0` vanishes by the Euler sequence.

Let

```text
E_g = sum of e_L over the good lines,
K   = number of marked incidences on bad lines,
C   = sum_marked C(j,2),
```

where `j` is the number of incident bad lines.  Exact double counting gives

```text
K=15B-15(d-b)+E_g,                                     (8)
X=BG-14K+2C,                                           (9)
```

where `X` is the number of residual bad-good pairs.  A marked quotient zero
can disappear only at type `j=14`; if `z` is the number of such exceptions,

```text
z<=min(floor(C/91),floor(K/14),15G-E_g).               (10)
```

The first exact scan enumerates every integer `164<=b<=d<=215`, every
DPW-admissible `r`, every `0<=B<=r+1`, and every allowed `E_g`.  It uses (8)--
(10) only permissively: `C`, residual bad-good pairs, and erased zeros are
independently maximized, while a negative relaxed good-good degree is clamped
to zero.  Thus a strict positive gap is a valid elimination, and every real
configuration remains in the surviving set.

The high branch (6) has no survivor.  The low scan leaves exactly

```text
29,595 coarse (b,d,r,B) rows, with B<=35.               (11)
```

## 3. Finite-linear-space and design cuts

Use the good lines as points and their good-good intersections as blocks.
No surviving branch has a full good-line pencil.  Indeed, the scan checks
`G>15`.  A full pencil cannot be marked, so every marked point would contain
at least fourteen bad lines, forcing `91b<=C(B,2)`, which is false statewise.

Choose a good line outside any block.  Its intersections with the block lines
are distinct zeros of a nonzero `O_P1(q)` section.  Thus every block has size
at most `q`; every point lies on at most `q` blocks by (7).  Consequently

```text
G-1<=q(q-1),        hence       G<=q(q-1)+1.            (12)
```

This eliminates `8,541` rows from (11), leaving exactly

```text
21,054 structural rows =121 with B=0 +20,933 with B>0. (13)
```

If `q=15` and `G>=198`, every point lies on at least
`ceil((G-1)/14)=15` blocks and hence on exactly fifteen.  The intersection
space is a `(15,1)`-design.  Vanstone's embedding theorem, in the form
allowing singleton lines, embeds every such design with

```text
G>(15-1)^2-1=195
```

in a projective plane of order 14.  Bruck--Ryser forbids that plane because
`14=2 mod 4` is not a sum of two squares.  The exact embedding statement is
Theorem 1.1 of Joel Christopher Fowler, *Topics in Linear Spaces and
Projective Planes*, Caltech PhD thesis (1984), attributing it to Vanstone.

## 4. Exhaustive joint-`C` deletion scan

For `B>0`, delete the bad lines.  The quotient section gives a good-arrangement
syzygy of degree `r-B`.  It is minimal: a smaller deletion syzygy, multiplied
by the bad-line product, would contradict minimality of the parent syzygy.
Hence

```text
mdr(good)=r-B=q-1.                                     (14)
```

At a marked point with `j` bad lines, the deletion marked excess is
`C(14-j,2)`.  Since

```text
C(14-j,2)=91-13j+C(j,2)  for 0<=j<=14
```

and the expression overcounts by one at `j=15`, its total `A` satisfies

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

For an incidence with `a` other good lines in its block, give charge

```text
phi(a)=C(a,2)/(a+1).
```

The total charge of a block is its deletion excess.  Discrete convexity shows
that the smallest total charge for oriented degree `M_gg` in at most `S`
positive parts is the exact balanced-integer-partition value `P(M_gg,S)`.
This is compared with both valid upper bounds

```text
E_G <= (d-1)^2-r(d-1-r)-C(d,2)-91b,
E_G <= (G-1)^2-(q-1)(G-q)-C(G,2)-A.                   (19)
```

The verifier enumerates all `20,933` positive-`B` rows and exactly
`373,774,811` joint integer states `(E_g,K,C)`.  The minimum strictly positive
lower-minus-upper margin is `1/120`.  There are 404 numerical survivors:

| `q` | `G` | rows |
|---:|---:|---:|
| 15 | 207 | 8 |
| 15 | 208 | 74 |
| 15 | 209 | 137 |
| 15 | 210 | 181 |
| 16 | 214 | 4 |

The first 400 rows are eliminated by the design cut in Section 3.

The four remaining rows are all

```text
(d,r,B,q,G)=(215,16,1,16,214),   b=164,165,166,167.    (20)
```

Imposing the necessary integer condition
`ceil(P(M_gg,S))<=E_G` leaves exactly one aggregate state per row:

| `b` | `E_g,K,C` | pooled lower | parent upper | deletion upper |
|---:|---:|---:|---:|---:|
| 164 | 751,1,0 | `366355/78` | 4699 | 4697 |
| 165 | 736,1,0 | `179630/39` | 4608 | 4606 |
| 166 | 721,1,0 | `352165/78` | 4517 | 4515 |
| 167 | 706,1,0 | `172535/39` | 4426 | 4424 |

The lower ceiling equals the deletion upper.  Moreover `K=1,C=0` makes
(15) exact: the bad line contains exactly one marked point and is the only
bad line there.  Thus deletion leaves 214 good lines with

```text
mdr=15,
tau=213^2-15*198=42399,
at least b-1>=163 points of multiplicity 15,
one point of multiplicity 14.                           (21)
```

In particular the deletion arrangement attains equality in DPW and its
minimal tangent section is good on every remaining line.

## 5. The zero-bad residue

Of the 121 zero-bad rows, 106 have `q=15` and `G>=198` and are eliminated by
Section 3.  Exactly fifteen remain:

```text
d=214, r=15, B=0, b=164,165,166,167,
d=215, r=15, B=0, b=164,...,174.                        (22)
```

Their pooled lower-minus-DPW-upper margins are respectively

```text
(b-167)/26             for d=214,
(3b-523)/78            for d=215.                       (23)
```

Every margin lies in `(-1,0]`.  The residual excess is an integer, so its
lower and upper bounds force DPW equality in every row.  Together with (21),
all non-design residue reduces to the following terminal lemma.

## 6. Algebraic terminal lemma for `d=214,215`

Suppose

```text
d in {214,215},
mdr=15,
every arrangement line is good,
tau=(d-1)^2-15(d-16),                                  (24)
```

and there are at least 164 marked 15-fold points when `d=215`, or at least
163 such points when `d=214`.  No such arrangement exists.

### 6.1 Zero length and corrected moments

A minimal syzygy gives a section

```text
s in H^0(P^2,T_P2(14))
```

tangent to every line.  It has no divisorial zero.  If `s=h s'` with
`deg h>0`, no line equation divides `h` because every line is good.
Cancellation shows `s'` is still tangent to all lines.  Lift through the
Euler sequence and subtract the logarithmic cofactor divided by the
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
D=sum_L(16-n_L),        I=sum_L n_L=16d-D.
```

If `Q` is the number of singularities, (26) gives

```text
Q=241-D.                                               (27)
```

Every singularity has multiplicity at most 16.  A full pencil is impossible
in the presence of 15-fold points; choosing a line outside any other
singularity bounds its multiplicity by that line's at most sixteen distinct
intersections.

Set `epsilon_P=16-mu_P`.  Then

```text
sum epsilon_P   =3856-16d-15D,
sum epsilon_P^2 =d^2-497d+61696-225D.                  (28)
```

The exact values are

| `d` | unit entries | `sum epsilon` | `sum epsilon^2` |
|---:|---:|---:|---:|
| 215 | at least 164 | `416-15D` | `1066-225D` |
| 214 | at least 163 | `432-15D` | `1134-225D` |

The square sum first forces `D<=4`.  Remove the unit entries and apply Cauchy
to the remaining at most `Q-t` entries.  For `D=1,2,3,4`, the minimum
left-minus-right gaps are

| `d` | `D=1` | `D=2` | `D=3` | `D=4` |
|---:|---:|---:|---:|---:|
| 215 | 4717 | 15384 | 17689 | 14161 |
| 214 | 7074 | 17525 | 22201 | 18225 |

All are positive, so

```text
D=0,       Q=241,       n_L=16 on every line.          (29)
```

If a double point existed, remove its `epsilon=14` entry and the marked unit
entries, then apply Cauchy again.  The minimum contradiction gaps are `2988`
for `d=215` and `5350` for `d=214`.  Thus every singularity has multiplicity
at least three.

### 6.2 Algebraic invariant-line residue

The 241 distinct arrangement singularities are zeros of `s`, and (25) says
the whole zero scheme has length 241.  Hence every zero is simple.  At least
three invariant lines meet at every zero, so its invertible two-by-two
linearization has three invariant directions and is scalar:

```text
J_P=lambda_P I_2,       lambda_P !=0.                  (30)
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
applied relative to a rational section.  This proves (31) algebraically in
arbitrary characteristic and is unaffected by the twist.

Apply (31) to any arrangement line.  It contains exactly sixteen simple
zeros by (29); every transverse/tangent eigenvalue ratio is 1 by (30); and
`N_(L/P^2)=O_L(1)`.  Thus

```text
16=1 in F,
```

impossible in characteristic zero or characteristic greater than 215.  The
terminal lemma, the fifteen zero-bad rows, and the four deletion rows are all
eliminated.  This proves the theorem. QED.

## 7. Frozen sources, verification, and nonclaims

Run

```text
ruby --disable-gems research/verify_m215_b164_full_active_deletion_nonexistence.rb
```

The verifier source-pins the frozen arithmetic primitives and checks every
integer and rational comparison in the full range, including all
`373,774,811` joint-`C` states, the exact survivor stratification, the four
exceptional integer states, all fifteen zero-bad terminals, and the terminal
moment inequalities.

Frozen terminal source:

```text
581e3cdebf0d800611dad22972b4b811a6d6280f21cd23a0f1ad4110cfce6feb
  research/M215_B164_DUAL_ARRANGEMENT_NONEXISTENCE.md
```

Frozen arithmetic support:

```text
6260d6f7f44391227c23b5469ce74a2ca1bdd2745a69a94758c8f3fb02b5c3f6
  research/verify_m217_b195_dual_arrangement_nonexistence.rb
```

Full verifier SHA-256:

```text
cc47b2a1c7e79d003d5d5a5b2898b8f714b9aae2479a5ed5a5f8df57a5effe9b
  research/verify_m215_b164_full_active_deletion_nonexistence.rb
```

The verifier SHA-pins and compares its canonical stdout byte-for-byte with

```text
014381b3b29e5edddc9c64423ea8e0f1e43fe5985865f62c7db5eabc134c4594
  research/verify_m215_b164_full_active_deletion_nonexistence.expected.txt
```

The sorted 404-row positive-`B` survivor ledger has SHA-256

```text
d4f0798b89f133791e2e79d90851eb51937cbee4bb816ee5634c64d7f0f67dc6
```

This is an arrangement theorem.  A consumer must separately establish the
marked-point lower bound, exact multiplicity 15, source interval, and
recurrence transport.  No affine-rank-at-least-16 or official-score claim is
made here.
