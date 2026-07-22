---
workboard_item: T
row: FAMILY-LEVEL RS TRACE-LINEAR PHASE OBSTRUCTION
object: OTHER
target_epsilon: NOT_INSTANTIATED
agreement: NOT_INSTANTIATED
B_star: NOT_INSTANTIATED
direct_statement: A degree-one RS trace-phase family has an attained singleton target and one complete balanced cyclotomic phase histogram with coherent signed Fourier mass. Any proof that assigns a separate nonnegative budget to each phase histogram has an exponential image-compensated loss at fixed odd phase order and a super-exponential raw loss at fixed density parameter and growing phase order.
architecture: DIRECT
partition_digest: NOT_APPLICABLE_DIRECT
atom_or_cell: RS_PHASE_STRUCTURED_SIDON_PAYMENT
quantifier: Every odd prime p and integer r>=1 in the declared family; exact complete-histogram falsifier p=3,r=5.
projection_and_unit: effective-character coherent Fourier histogram mass; not slopes, rays, codewords, or a row atom
claimed_bound: A_hist>=A_split and A_split/A_eff >= p*2^(2r)/((pr+1)^(2(p-1))*(2r+1)); at p=3,r=5, A_hist=155428415166024>6*A_eff.
status: COUNTEREXAMPLE
impact: ROUTE_CUT
falsifier: A histogram-local MI+MA replacement using nonnegative per-histogram budgets must pay the complete balanced histogram below. Exact Fourier inversion then forces a negative signed contribution from other histograms.
replay: python3 experimental/scripts/verify_sidon_effective_image_cyclotomic_phase_floor.py --check; python3 -O experimental/scripts/verify_sidon_effective_image_cyclotomic_phase_floor.py --check
---

# Trace-linear cyclotomic phase floor

## Result and exact route cut

This packet proves `COUNTEREXAMPLE_NEW_FLOOR`, acceptance criterion **4**, for
one precisely scoped proof interface:

```text
route cut: PHASE_HISTOGRAM_LOCAL_MI_MA
successor: ACTUAL_LEAF_CROSS_HISTOGRAM_CANCELLATION_OR_DIRECT_SIDON
```

The family uses the genuine degree-one Reed--Solomon/Vandermonde phase
`g(t)=t`; its characters are `p`-th roots produced by the field trace, not
arbitrarily assigned signs. A complete globally balanced phase histogram has
one identical positive fixed-weight Fourier coefficient on every character.
Consequently, cancellation **inside that histogram** is exactly zero.

The conclusion is deliberately narrower than “all cancellation-sensitive phase
methods fail.” It cuts only methods that assign a separate nonnegative budget
to each phase histogram. A surviving method may still couple different
histograms through their signed target factors, or bypass MI+MA with a direct
image-normalized Sidon/max-fiber theorem on a genuine post-C1--C8 residual.

## Construction

Fix an odd prime `p` and `r>=1`. Put `N=2pr`, `m=pr`, and
`K=F_(p^(N-2))`. Choose an `F_p`-basis `e_1,...,e_(N-2)` of `K` and set

```text
u = -(e_1+...+e_(m-1)),
T = {0,e_1,...,e_(N-2),u},
S_* = {e_1,...,e_(m-1),u},
Psi(S) = sum_(t in S) t,  S in binom(T,m).
```

Because `p` is odd and `m-1>=2`, the basis expansion of `u` has at least two
nonzero coefficients. Hence `u` is neither zero nor a basis vector, so `T`
contains exactly `N` distinct field elements. This is the first power-sum
coordinate of `eq:exact-power-sum-map`.

Characters are the actual trace-linear phases

```text
chi_a(t)=zeta_p^Tr_(K/F_p)(a t).
```

The differences from `0` contain a basis and therefore span `K`; thus
`A_eff=p^(N-2)`.

### Injectivity and the attained zero target

Suppose two `m`-supports collide. Let their incidence difference at `u` be the
integer `c in {-1,0,1}`. Comparing basis coefficients in `K` forces incidence
difference `c` on `e_1,...,e_(m-1)` and zero on all remaining basis elements.
Equal support cardinalities then force the incidence difference at `0` to be
`-cm`. Since that difference lies in `{-1,0,1}` and `m>=3`, one must have
`c=0`; all differences vanish. Hence `Psi` is injective on the slice.
Moreover `sum_(t in S_*) t=0`, so

```text
M = L = binom(N,m),
Psi^(-1)(0) = {S_*}.                                  (1)
```

The nondegenerate trace pairing parametrizes phase words by arbitrary values on
the basis, with

```text
y_0=0,
y_u=-(y_1+...+y_(m-1)).                              (2)
```

## A certified split-balanced subblock

Let every residue of `F_p` occur exactly `r` times on `S_*` and exactly `r`
times on its complement. Put

```text
H_(p,r)=(pr)!/(r!)^p.
```

Every balanced word on `S_*` satisfies (2), because
`r(0+...+(p-1))=0` in `F_p`; there are `H_(p,r)` choices. On the complement,
the distinguished coordinate `0` already has phase zero, leaving exactly
`H_(p,r)/p` choices. Therefore the certified split-balanced subblock has

```text
B_split(p,r) = H_(p,r)^2/p.                            (3)
```

Every one of these characters has `2r` copies of every phase. For odd `p`,

```text
prod_(j=0)^(p-1)(1+zeta_p^j z) = 1+z^p,
```

so the common fixed-weight coefficient is

```text
c_(p,r) = [z^(pr)](1+z^p)^(2r) = binom(2r,r)>0.       (4)
```

At target zero all target character factors are one. Thus the signed subblock
sum is coherent, not an absolute-value relaxation:

```text
A_split(p,r) = (H_(p,r)^2/p) binom(2r,r).              (5)
```

## The complete balanced phase histogram

Let `H_bal(p,r)` be the set of **all** effective characters whose phase word on
`T` contains exactly `2r` copies of each residue. Every character in this
complete histogram has the same positive coefficient (4), and the certified
split-balanced subblock is contained in it. Writing `A_hist(p,r)` for its signed
mass gives

```text
A_hist(p,r) >= A_split(p,r),                            (6)
```

with equality not asserted. Equation (6) is enough for the general family
floor. It also fixes an ambiguity in the predecessor packet: subtracting only
the split subblock gives an exact signed sum outside that subblock, but not an
exact cross-histogram sum, because further characters of the same global
histogram may remain. The finite falsifier below counts the complete histogram
and obtains the true cross-histogram debt.

## General family theorem

The balanced multinomial is maximal: if two counts differ by at least two,
transferring one item from the larger count to the smaller increases the
multinomial coefficient, so the maximum at total `pr` is the balanced type.
There are at most `(pr+1)^(p-1)` types. The central binomial coefficient is
maximal among the `2r+1` coefficients of `(1+z)^(2r)`. Hence

```text
H_(p,r) >= p^(pr)/(pr+1)^(p-1),
binom(2r,r) >= 2^(2r)/(2r+1).                          (7)
```

Since `L=M`, exact image compensation and (6) give

```text
(L/A_eff)(A_hist/M) >= A_split/A_eff
 >= p*2^(2r)/((pr+1)^(2(p-1))*(2r+1))                 (8)
 = exp((log 2)N/p - O_p(log N)).
```

Thus every fixed odd `p` leaves an exponential compensated histogram-local
floor. Also `M<=2^N`, so

```text
A_hist/M >= A_split/M
 >= p^(-1)(p/2)^N/(pr+1)^(2(p-1)).                    (9)
```

For fixed `r>=2` and odd primes `p->infinity`, (9) is
`exp(Omega_r(N log N))`: the raw histogram-local cost is super-exponential.

## Exact complete-histogram falsifier: `p=3`, `r=5`

The certified split subblock has

```text
N=30, m=15, K=F_(3^28),
M=L=binom(30,15)=155117520,
A_eff=3^28=22876792454961,
H_(3,5)=756756,
H_(3,5)/3=252252,
B_split=190893214512,
c_(3,5)=binom(10,5)=252,
A_split=48105090057024
       =2*A_eff+2351505147102.                         (10)
```

To count the complete globally balanced histogram, let
`a=(a_0,a_1,a_2)` be the phase counts on `S_*`. Its exact admissible set is

```text
a_0+a_1+a_2=15,
0<=a_j<=10,
a_0<=9,
a_1+2a_2=0 mod 3.
```

The complement has counts `(10-a_0,10-a_1,10-a_2)` and its distinguished zero
coordinate has already consumed one zero phase. Therefore

```text
C_bal = sum_a 15!/(a_0!a_1!a_2!)
                *14!/((9-a_0)!(10-a_1)!(10-a_2)!)
      = 616779425262.                                  (11)
```

The verifier checks all admissibility conditions and all summands in (11); the
Lean module checks the same frozen 29-term integer formula. Since every
character in the histogram has coefficient `252`,

```text
A_hist = C_bal*252
       = 155428415166024
       = 6*A_eff+18167660436258.                       (12)
```

A separate nonnegative source-normalized payment
`A_hist <= (kappa-1)M` therefore forces

```text
kappa >= 1002006.                                      (13)
```

For comparison, the certified split subblock alone forces `kappa>=310122`.

Let `A_other` be the signed sum over every nontrivial effective character
outside the complete balanced histogram. Exact Fourier inversion at the unique
zero target, using (1), gives

```text
M + A_hist + A_other = A_eff,
A_other = -132551777828583.                            (14)
```

Equation (14) is the exact cross-histogram cancellation debt. Any proof that
pays the balanced histogram by a separate nonnegative budget must obtain an
even larger negative signed contribution from other histograms; it cannot close
by summing nonnegative histogram-local charges.

## Replay and source map

The stdlib verifier exhausts all `3^10=59049` trace-linear phase words and all
`binom(12,6)=924` supports at `p=3,r=2`. It checks domain distinctness,
singleton fibers, the unique zero target, the 2700-character split subblock, the
complete 3900-character balanced histogram, exact coefficient `6`, the full
character sum, the `p=3,r=5` 29-term histogram formula, both finite payment
floors, general lower-bound instances, and eight rejected mutations.
Cyclotomic arithmetic is exact in `Z[zeta_3]`; no floating point enters a gate.

| Packet statement | Source label |
|---|---|
| degree-one RS map | `eq:exact-power-sum-map` |
| effective target/Fourier denominator | `eq:effective-fourier-span`, `lem:effective-span-fourier` |
| separately paid nonnegative aggregate | `def:effective-fourier-payment` |
| phase-aware major aggregation | `def:major-arc-aggregate` |
| source/image scales | `eq:image-ambient-scales`, `def:primitive-q` |
| small-characteristic boundary | `rem:small-characteristic-cycles` |
| positive shallow theorem boundary | `thm:unconditional-shallow-mi-ma` |

All labels are in `experimental/grande_finale.tex`.

## Nonclaims

This family is not claimed to survive the deployed C1--C8 atlas. It does not
instantiate a Mersenne-31 or KoalaBear leaf, move `U_Q` or another ledger atom,
prove a ray/slope compiler, or close an adjacent row. It does not refute a
global target-coupled method that combines different histogram signs before
assigning any nonnegative charge. It proves no lower bound for the true MCA or
list numerator. The field `K`, prime phase field `F_p`, effective target, and
deployed row fields remain distinct; no extension-field payment is transferred
to a live row.
