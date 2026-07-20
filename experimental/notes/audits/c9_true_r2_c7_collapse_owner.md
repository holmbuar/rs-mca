# The complete true-R2 shell is C7 image collapse, not a primitive C9 leaf

## Claim

The complete true-`R=2` shell family from
`experimental/notes/audits/c9_true_r2_shell_realizability.md` cannot populate
the primitive C9 interface.

Its full fixed-weight two-moment image has full two-dimensional effective span
over the construction field, but exponentially fewer realized values than that
span.  Hence the printed C7 effective-image-collapse trigger fires before C9.
For the central shell, the exact distinct-slope image is nevertheless
exponentially larger than its full-slice natural profile scale, so the
unrefined C7 collapse cell is not paid either.

Thus the family is a precise routing obstruction:

```text
exact true-R2 prefix fibre with exact MCA slopes
  -> full effective target F_p^2
  -> exponential realized-image collapse
  -> C7 first-match owner
  -> natural-scale payment still exponential
  -> no primitive C9 profile.
```

## Status

`COUNTEREXAMPLE / PROVED C7 ROUTING / UNPAID EXPONENTIAL-FIELD COLLAPSE / AUDIT`

The effective-span and collapse estimates below are exact elementary
consequences of the source construction.  The finite first-match and
normalization regressions are kernel-checked in
`AsymptoticSpine.C9TrueR2CollapseRegression`.

## Parameters

Let the block count be `k`, with `k` divisible by six for the central asymptotic
shell.  The source construction uses

```text
b = 16,
d0 = least positive odd integer with b^d0 > 14k,
di = d0 + 2i,
ai = b^di,
Ti = {ai, ai+1, ai+2, ai+3},
Dk = disjoint union_i Ti,
N = |Dk| = 4k,
m = 2k.
```

Choose a prime

```text
p_k > sum_{t in Dk} t^3.
```

The line field and generated field are both `F_{p_k}`.  The RS code in the exact
locator-line realization has dimension

```text
k_RS = 2k - 3,
```

and agreement `a=2k`.

The full-slice boundary map is

```text
Phi_2(S) = (sum_{t in S} t, sum_{t in S} t^2)
```

on the `2k`-of-`4k` slice.

## Existing paper dependency

The result uses only named existing interfaces.

- `c9_true_r2_shell_realizability.md` proves the complete fibres, exact image
  formula, central-shell energy and normalized rate, and exact MCA line.
- The frontiers cell catalogue defines C7 effective-image collapse as a boundary
  map realizing exponentially fewer values than its effective/ambient target.
- C7 precedes C9 in the first-match order.
- The primitive C9 profile uses the full fixed-weight slice mass `M`, realized
  image size `L`, and natural average `M/L`; residual self-normalization is not
  permitted.

No C8 chart theorem, MI/MA estimate, Sidon theorem, or support-count substitute
is used.

## Proof idea

### 1. The effective two-moment span is full

Fix all blocks except one, and in that block write `a=a_i`.  Consider the three
weight-two choices

```text
A = {a, a+3},
B = {a+1, a+2},
C = {a, a+2}.
```

Their local moment pairs are

```text
Phi(A) = (2a+3, 2a^2+6a+9),
Phi(B) = (2a+3, 2a^2+6a+5),
Phi(C) = (2a+2, 2a^2+4a+4).
```

Hence

```text
Phi(B)-Phi(A) = (0,-4),
Phi(C)-Phi(A) = (-1,-2a-5).
```

Their determinant is `-4`, nonzero in `F_{p_k}` because `p_k>4`.  These are two
independent directions in the image of the full fixed-weight slice.  Therefore
the effective affine target has dimension two and

```text
A_eff = p_k^2.
```

This removes the possible escape that the small realized image merely reflects
a smaller effective span.

### 2. The realized image is exponentially collapsed

The source proves

```text
M_k = binom(4k,2k),
L_k = [x^(2k)] (F(x)^k + k x^2 F(x)^(k-1)),
F(x)=1+4x+5x^2+4x^3+x^4,
F(1)=15.
```

Coefficient positivity gives the explicit upper bound

```text
L_k <= 15^k + k 15^(k-1) <= (k+1)15^k.
```

Also

```text
p_k > sum_{t in Dk} t^3 > a_(k-1)^3
    = 16^(3(d0+2k-2)).
```

Since `d0>=1`,

```text
A_eff / L_k
  = p_k^2 / L_k
  > 16^(12k-6) / ((k+1)15^k).
```

Thus

```text
log(A_eff/L_k)
  >= k(12 log16 - log15) - O(log k)
  = Omega(N).
```

The full two-moment profile is therefore an actual C7 effective-image-collapse
profile, not a primitive C9 leaf.

### 3. C7 first match empties the proposed C9 cell

For the central shell `h=k/2`, the source exact line has

```text
|Z_shell| = binom(k,k/2)
```

distinct slopes.  The same witness family lies in the C7 collapse projection
and in the tempting raw C9 shell projection.  Because C7 precedes C9, ordered
first match assigns those slopes to C7 and gives

```text
Z_C9^o = empty.
```

`C9TrueR2CollapseRegression.trueR2_c7Collapse_before_c9` kernel-checks this
finite interface consequence on the exact `k=6` twenty-slope anchor.

### 4. The unrefined C7 collapse profile is not naturally paid

The source gives

```text
log M_k = k log16 + O(log k),
log L_k = k log15 + O(log k),
Nbar_k = M_k/L_k = exp(k log(16/15)+O(log k)).
```

For the central shell,

```text
|Z_shell| = binom(k,k/2) = exp(k log2-O(log k)).
```

Therefore

```text
|Z_shell| / (1+Nbar_k)
  = exp(k log(15/8)-O(log k)).
```

Since `N=4k`, this is `exp(Omega(N))`, not `exp(o(N))`.  The direct
natural-profile payment required by the closed ledger fails exponentially.

The family is consequently an unpaid C7 collapse unless a further named
refinement or earlier paid owner is proved.  Calling it C9 cannot repair the
payment because the C7 trigger already fired.

## Exact finite normalization regression

At `k=6`, the exact source formulas give

```text
M_6 = binom(24,12) = 2704156,
L_6 = 2545055,
|Z_shell| = binom(6,3) = 20.
```

Clearing the image denominator, the additive full-slice profile term is

```text
L_6 + M_6 = 5249211,
```

while the distinct-slope charge is

```text
20 L_6 = 50901100.
```

Hence loss nine fails and loss ten is the first integer loss:

```text
50901100 > 9 * 5249211,
50901100 <= 10 * 5249211.
```

By contrast, stale residual self-normalization takes residual mass `20` and
residual image size `1`, making the same fibre appear unit-paid:

```text
20 <= 20+1.
```

`C9TrueR2CollapseRegression` kernel-checks all these exact statements.  The
source asymptotic ratio proves that the required loss then grows exponentially;
the finite factor ten is not a uniform payment.

## Ledger impact

- **C9 / hard input 2:** this true-`R=2` shell is not a primitive C9 survivor and
  cannot be used as a Sidon counterexample at that interface.
- **C7 / hard input 1:** the family has an explicit C7 effective-image-collapse
  owner before C9.
- **C7 payment:** the unrefined collapse profile remains unpaid in this
  exponential-field construction; the exact slope/natural-scale ratio has
  positive exponential rate.
- **C8 / hard input 3:** the product locator architecture may still admit a
  further balanced-core refinement, but no such refinement or ray payment is
  asserted here.
- **UNIF:** no row-uniform profile sum or target comparison follows.

The line-local order is unchanged:

```text
first-match deletion inside the received line
  -> sum_profile
  -> outer sup_line.
```

## Constants

```text
N = 4k,
m = 2k,
k_RS = 2k-3,
A_eff = p_k^2,
L_k <= (k+1)15^k,
A_eff/L_k > 16^(12k-6)/((k+1)15^k),
|Z_shell|/(1+M_k/L_k)
  = exp(k log(15/8)-O(log k)).
```

Finite `k=6` anchor:

```text
M=2704156,
L=2545055,
Z=20,
required cleared loss=10.
```

## Reproducibility

Source verifier:

```text
PYTHONDONTWRITEBYTECODE=1 \
  python3 experimental/scripts/verify_c9_true_r2_shell_realizability.py
PYTHONDONTWRITEBYTECODE=1 \
  python3 experimental/scripts/verify_c9_true_r2_shell_realizability.py --json
PYTHONDONTWRITEBYTECODE=1 \
  python3 experimental/scripts/verify_c9_true_r2_shell_realizability.py --tamper-selftest
```

Lean:

```text
cd experimental/lean/asymptotic_spine
lake build AsymptoticSpine.C9TrueR2CollapseRegression
lake build
```

## Nonclaims

- The separated block domains are not smooth multiplicative or circle domains.
- No general C9 survivor theorem is refuted on intended rows.
- No paid C7 refinement, C8 balanced-core chart, RC, MI/MA, Sidon theorem, FI
  theorem, target comparison, or deployed threshold is proved.
- The result does not replace slopes by support energy; it uses the exact MCA
  slope count from the source line.
- No main-paper TeX is changed.
