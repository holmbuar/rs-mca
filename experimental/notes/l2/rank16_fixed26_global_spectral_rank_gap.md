# Fixed-26 global spectral-rank gap and split-complement identity

**Status:** PROVED, conditional on the exact PR #862 head
`d2b11f1914dea4cb4a7670736cf00d1422c878de`. This note has zero finite
payment and leaves the official score at `0/2`.

## Dependency and source cell

This note is stacked on PR #862, whose parent is the `origin/main` commit
`7f278167e1e51f968896229ae438ea5a76398f90`. It imports exactly the fixed-26
source compiler and the global 64-step spectral collapse proved at that head.

Every quantifier below stays inside one and the same source cell:

- one canonical received word;
- one canonical first-match owner;
- one monic generator `g` of degree `a=67472`;
- one fixed nonzero projective residue ray represented by `xi`; and
- one fixed 26-label core with locator `G_C`.

Only the pair labels and the valid edges inside this cell may vary. In
particular, there is no sum, union, averaging, or owner aggregation across
generators, residue rays, cores, received words, or first-match source cells.
Calling an edge valid retains every splitting, footprint, nonpairing,
prior-owner, and canonical first-match filter of the source compiler.

Use the deployed constants

```text
p = 2130706433,       n = 2097152,
B = 32768,            Omega = mu_64,
a = 67472,            r = 63601,
delta = a-r = 3871.
```

Put

```text
A = F_p[X]/(g),       T = X^B in A,
W = xi (T^64-1)^(-1) in A.
```

PR #862 proves that the minimal polynomial `mu_g` of `T` has degree
`3 <= nu <= a`. In the global branch it also proves

```text
deg rem_g(T^j W) <= r,             0 <= j <= 63.          (1)
```

For an actual valid edge, the imported source conditions make `W` a unit.
No squarefreeness assumption on `g` is made or needed here.
In every polynomial identity below, `W` denotes its canonical representative;
the `j=0` case of (1) gives `deg W <=r`.

## Theorem

Inside the fixed source cell above, assume the global 64-step collapse (1)
and the existence of an actual valid edge. Then:

1. No valid edge can have spectral rank `18 <= nu <= 64`. Equivalently, the
   global branch is reduced to

   ```text
   nu in 3..17, or nu >=65.
   ```

2. For every actual valid edge `{y,z}`, put

   ```text
   F_y  = X^B-y,
   F_z  = X^B-z,
   H_yz = (X^n-1)/(F_y F_z),
   H_yz = R_yz L_yz,
   ```

   where `R_yz` is its monic degree-`r` valid split locator. If `q_yz` is
   the nonzero normalization scalar from PR #862, then there is a polynomial
   `A_yz in F_p[X]` such that

   ```text
   q_yz W L_yz = 1 + g A_yz,                              (2)
   deg L_yz = 1968015,
   deg A_yz <= 1964144.                                   (3)
   ```

   Consequently, for any two valid edges `e,f` in this same source cell,

   ```text
   g | q_e L_e - q_f L_f,                                 (4)
   ```

   and each valid edge obeys the exact resultant normalization

   ```text
   q_yz^67472 Res(g,W) Res(g,L_yz) = 1 in F_p.             (5)
   ```

## Proof of the spectral-rank exclusion

Assume first that `nu <=64`. Every class in `Fbar_p[T]` has a representative
of `T`-degree less than `nu`. Extending scalars in (1), linearity therefore
gives

```text
deg rem_g(W P(T)) <= r                                    (6)
```

for every `P in Fbar_p[Z]` of degree less than `nu`.

Factor over `Fbar_p`:

```text
mu_g(Z) = product_lambda (Z-lambda)^e_lambda,
nu = sum_lambda e_lambda.
```

Let `epsilon_lambda` be the CRT idempotent for the
`(Z-lambda)^e_lambda` primary factor. Reduce

```text
epsilon_lambda(Z) (Z-lambda)^(e_lambda-1)
```

modulo `mu_g` to a polynomial `J_lambda` of degree less than `nu`, and let

```text
f_lambda = rem_g(W J_lambda(T)).                          (7)
```

The element `J_lambda(T)` is a nonzero top primary layer. Since `W` is a
unit, `f_lambda` is nonzero; by (6), `deg f_lambda <=r`.

Write

```text
g(X) = product_beta (X-beta)^m_beta
```

over `Fbar_p`. Consider first `lambda !=0`. Because `p` does not divide `B`,
`X^B-lambda` has a simple zero at every `beta` with `beta^B=lambda`.
Consequently

```text
e_lambda = max_{beta^B=lambda} m_beta.
```

The polynomial `f_lambda` vanishes to full `g`-multiplicity on every other
primary component. On the `lambda` component it vanishes completely at roots
with `m_beta < e_lambda`, and to multiplicity exactly `e_lambda-1` at roots
with `m_beta=e_lambda`. If `N_lambda` is the number of those maximal roots,
then

```text
g / product_{m_beta=e_lambda, beta^B=lambda} (X-beta)
```

divides `f_lambda`. Hence

```text
a-N_lambda <= deg f_lambda <= r,
N_lambda >= a-r = delta.                                 (8)
```

The `lambda` primary component therefore contributes at least
`delta e_lambda` to `deg g`.

The zero eigenvalue needs a separate argument, and this is why no hidden
squarefree hypothesis is permissible. If `X^m_0` exactly divides `g`, then

```text
e_0 = ceil(m_0/B),
N_0 = m_0-B(e_0-1).
```

The top zero-primary layer in (7) has exact `X`-adic order `B(e_0-1)`.
Thus the same degree argument gives `N_0 >=delta`. Since `B>=delta`,

```text
m_0 = B(e_0-1)+N_0 >= delta e_0.                          (9)
```

Summing (8) and (9) over all primary factors gives

```text
a >= delta sum_lambda e_lambda = delta nu.                (10)
```

At the deployed values,

```text
17 delta = 65807 <= 67472,
18 delta = 69678 > 67472.
```

Therefore `nu <=17` whenever `nu <=64`. This excludes all 47 integral ranks
`18,19,...,64`. Combining the exclusion with the imported lower bound
`nu>=3` proves the stated dichotomy.

## Proof of the split-complement identity

For a valid edge, PR #862 gives

```text
U_yz = rem_g(W H_yz),        R_yz = q_yz U_yz.            (11)
```

Since `H_yz=R_yz L_yz`, (11) implies

```text
g | R_yz(q_yz W L_yz-1).
```

Validity gives `gcd(g,R_yz)=1`, so cancellation in `F_p[X]` yields (2).
The `j=0` case of (1) gives `deg W <=r`, while

```text
deg H_yz = n-2B = 2031616,
deg L_yz = n-2B-r = 1968015.
```

It follows from (2) that

```text
deg A_yz <= r+(n-2B-r)-a = n-2B-a = 1964144,
```

which proves (3). Subtracting two copies of (2) and cancelling the unit `W`
modulo `g` proves (4). Taking resultants of (2), using that `g` is monic,
gives

```text
q_yz^a Res(g,W) Res(g,L_yz)
  = Res(g,1+g A_yz)
  = 1,
```

which is (5), including when `g` is not squarefree.

The word *complement* is literal. If the complete locator is

```text
E_yz = G_C F_y F_z R_yz
```

and `C_yz=(X^n-1)/E_yz`, then direct cancellation gives

```text
L_yz = G_C C_yz.                                         (12)
```

## Ownership, overlap, and nonclaims

PR #862 owns the source resolvent, minimal polynomial, global 64-step
collapse, pair-candidate orientation, gcd/S-unit constraints, and its
resultant/cycle identities. This note consumes those statements at the exact
head above. Its narrow new claim is the primary-layer inequality
`a>=3871 nu`, the resulting rank exclusion `18..64`, and the explicit
split-complement consequence (2)-(5). It contains no Role 06 collision
theorem and makes no seven-star closure claim.

Open PR #872 is a nonclaim here: its conditional arithmetic reaching `T-3`
does not prove that the outside population is at most three, and it does not
turn this fixed-cell theorem into a payment. Open PR #873 is also a nonclaim:
its exclusion of fixed-26/fixed-27 multiplicity-one global owners forbids
multiplying or aggregating this local theorem into a global owner count.

Accordingly this note records zero finite payment: parent `0`, Grand List
`0`, Grand MCA `0`, and official score remains `0/2`. It does not prove
`G64-CAP`, cap 116, a rank-16 parent theorem, either Grand theorem, or a
global aggregation. The exact remaining global spectral branches are
`3..17` and `>=65`.

## Attachment and replay requirements

This note, its verifier, its expected transcript, and the corresponding
`experimental/agents-log.md` entry must travel as one patch stacked on the
exact PR #862 head. If #862 is rebased or changed, refresh and review every
source hash before replay; do not detach this theorem from its dependency.

Replay with a stdlib Python interpreter:

```bash
python3 experimental/scripts/verify_rank16_fixed26_divided_difference_source_compiler.py
python3 experimental/scripts/verify_rank16_fixed26_spectral_resolvent.py
python3 experimental/scripts/verify_rank16_fixed26_global_spectral_rank_gap.py
python3 -O experimental/scripts/verify_rank16_fixed26_global_spectral_rank_gap.py
python3 experimental/scripts/verify_rank16_fixed26_global_spectral_rank_gap.py --tamper-selftest
python3 -O experimental/scripts/verify_rank16_fixed26_global_spectral_rank_gap.py --tamper-selftest
python3 -m py_compile experimental/scripts/verify_rank16_fixed26_global_spectral_rank_gap.py
git diff --check
```

The normal and `-O` transcripts must be byte-identical to each other and to
`experimental/scripts/verify_rank16_fixed26_global_spectral_rank_gap.expected.txt`.
