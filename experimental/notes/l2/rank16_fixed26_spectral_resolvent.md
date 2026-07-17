# Rank-16 fixed-26 spectral resolvent and split-star constraints

**Status:** proved local structural theorem. This note makes no finite or
global-ledger payment.

## Claim

Work over the deployed field and subgroup

```text
p = 2130706433,       H = mu_2097152,
B = 32768,            Omega = mu_64,
a = 67472,            r = 63601,
d = 28897,            r-d = 34704.
```

Fix one literal fixed-26 source cell from the integrated divided-difference
compiler: one received word and canonical first-match owner, one monic
degree-`a` polynomial `g` with `gcd(g,X^2097152-1)=1`, one nonzero projective
residue ray, and one 26-label core. Put

```text
A = F_p[X]/(g),        T = X^B in A,
F_y = X^B-y,           xi = rem_g(G_C^(-1) eta).
```

For every `y in Omega`, define the algebraic extension of the source
resolvent

```text
V_y = rem_g(xi (T-y)^(-1)).
```

Only labels outside the fixed core can support compiled pair candidates.
Calling a pair *valid* always retains every splitting, footprint, nonpairing,
prior-owner, and canonical first-match filter from the divided-difference
compiler.

### Theorem 1 (minimal spectral resolvent)

There is a unique monic polynomial `mu_g in F_p[Z]` of least positive degree
`nu` such that

```text
mu_g(T) = 0 in A.
```

It satisfies

```text
3 <= nu <= a,
g(X) | mu_g(X^B),
mu_g(y) != 0 for every y in Omega.
```

Consequently

```text
mu_g(X^B) = g(X) J_g(X),       deg J_g = nu B-a.
```

Define

```text
q_Z(W) = (mu_g(W)-mu_g(Z))/(W-Z),
N(Z)   = -xi q_Z(T) in A[Z].
```

Then `deg_Z N <= nu-1` and the exact resolvent formula is

```text
V_y = N(y)/mu_g(y).                                      (1)
```

Let `pi: A -> A/L_r` be the quotient by the canonical representatives of
degree at most `r`. If `Y` is one collision class for the high tails
`pi(V_y)` and `lambda_Y` is their common value, then

```text
prod_{y in Y}(Z-y)
  | pi(N(Z))-mu_g(Z) lambda_Y.                            (2)
```

Thus a class of size at least `nu+1` forces the global zero-tail collapse

```text
pi(V_w)=0 for every w in Omega.                           (3)
```

If `lambda_Y=0`, size at least `nu` already forces (3). Away from (3), every
collision class has size at most `nu`, and a zero-tail class has size at most
`nu-1`.

### Theorem 2 (simultaneous Krylov collapse)

For a collision class `Y` of size `k>=2`, put

```text
phi_Y(Z) = prod_{y in Y}(Z-y),
U_Y      = rem_g(xi phi_Y(T)^(-1)).
```

If `I_Y(Z)` is the Lagrange interpolation polynomial with
`I_Y(y)=V_y`, then in `A[Z]`

```text
I_Y(Z) = U_Y (phi_Y(T)-phi_Y(Z))/(T-Z).                   (4)
```

Coefficient comparison gives the simultaneous low-degree conditions

```text
deg rem_g(T^m U_Y) <= r,          0 <= m <= k-2.          (5)
```

For distinct `y,z in Y`, let

```text
p_yz(Z) = phi_Y(Z)/((Z-y)(Z-z)).
```

The literal divided-difference pair candidate satisfies

```text
U_yz = rem_g(U_Y p_yz(T)).                                (6)
```

If the cell contains an actual valid edge, then `xi` and `U_Y` are units in
`A`. In a non-global class, `k<=nu`; hence

```text
U_Y, T U_Y, ..., T^(k-2) U_Y
```

are linearly independent. For any anchor `y0 in Y`, the `k-1` candidates
`U_y0z`, and therefore their nonzero scalar-normalized monic locators, are
linearly independent.

### Theorem 3 (global 64-step form)

Since `T^64-1=X^2097152-1` is a unit in `A`, put

```text
W = xi (T^64-1)^(-1).
```

Then

```text
V_y = W (T^64-1)/(T-y)
    = W sum_{j=0}^{63} y^j T^(63-j).                      (7)
```

The global zero-tail collapse (3) is equivalent to

```text
deg rem_g(T^j W) <= r,            0 <= j <= 63.           (8)
```

For every pair, the corresponding pair candidate is

```text
U_yz = rem_g(W (T^64-1)/((T-y)(T-z))).                    (9)
```

The numerator/denominator orientation in (9) is load-bearing. It follows
directly from `W=xi/(T^64-1)` and
`U_yz=xi/((T-y)(T-z))`.

### Theorem 4 (valid split-star constraints)

Let `{y,z}` and `{y,w}` be two actual valid edges with `z!=w`. Their monic
degree-`r` locators satisfy

```text
deg gcd(R_yz,R_yw) <= d = 28897.                          (10)
```

The proof uses the literal prohibition on a twenty-ninth complete `q64`
fiber; it is not a degree-only statement.

If all three edges on distinct labels `y,z,w` are valid, write `c_y` for the
boundary coefficient inherited from the fixed-26 compiler. Then

```text
(c_y-c_z)R_yz + (c_z-c_w)R_zw + (c_w-c_y)R_wy = 0.       (11)
```

The three pairwise gcds are one common monic polynomial `G_yzw`. After
cancelling it, the three quotients are monic, pairwise coprime, squarefree,
completely `H`-split, have common degree at least

```text
r-d = 63601-28897 = 34704,                                (12)
```

and obey the nondegenerate split S-unit equation obtained from (11).

For a valid edge put

```text
rho_y = Res(g,F_y),        kappa = Res(g,xi).
```

Both are nonzero, and the exact resultant normalization is

```text
Res(g,R_yz) = q_yz^a kappa/(rho_y rho_z).                 (13)
```

For every valid four-cycle with edges
`{a,b},{c,d},{a,c},{b,d}`, cancellation in (13) gives

```text
Res(g,R_ac) Res(g,R_bd)
------------------------ = (q_ac q_bd/(q_ab q_cd))^a.     (14)
Res(g,R_ab) Res(g,R_cd)
```

Because `p-1=2^24*127`, `a=16*4217`, and `gcd(a,p-1)=16`, the left side of
(14) is a sixteenth power in `F_p^*`.

Finally, complete simple splitting over `H`, odd `r`, and `-1 in H` give
`R_yz(0) in H`. Since

```text
V_y-V_z = (c_y-c_z)R_yz,
```

every valid edge satisfies

```text
(V_y(0)-V_z(0))/(c_y-c_z) in H,                           (15)
```

equivalently the `n`th powers of numerator and denominator agree.

## Proof

Multiplication by `T` is an endomorphism of the `a`-dimensional vector space
`A`, giving the unique minimal polynomial and `nu<=a`. The identity
`mu_g(T)=0` is exactly `g(X)|mu_g(X^B)`. Since `a>2B`, it forces `nu>=3`.
If `mu_g(y)=0` for `y in Omega`, then `T-y` times a lower-degree polynomial
annihilates `T`. The factor `T-y` is a unit because `g` is root-free on `H`,
contradicting minimality. This proves Theorem 1's first assertions.

The divided difference obeys

```text
(T-y) q_y(T) = mu_g(T)-mu_g(y) = -mu_g(y),
```

which proves (1). Equation (2) follows by evaluating its vector polynomial at
each label of the collision class. Its degree is at most `nu`, and its leading
coefficient is `-lambda_Y`; the stated root counts therefore give (3) and the
two collapse thresholds.

Both sides of (4) have `Z`-degree at most `k-1` and agree at every label in
`Y`. Vandermonde uniqueness over `A` proves (4). Successive coefficient
comparison proves (5), while cancellation of `phi_Y(T)` proves (6). A valid
edge makes `xi` a unit: every factor in the source congruence is a unit in
`A`. Multiplying a relation among the Krylov vectors by `U_Y^(-1)` would give
an annihilating polynomial of degree below `nu`, proving independence.

Equation (7) is the geometric-series identity for `y^64=1`. Fourier
inversion over the 64 distinct labels proves the equivalence with (8), and
the two definitions of `W` and `U_yz` give the correctly oriented (9).

For two edges through `y`, the fixed-27 equations from the inherited compiler
give

```text
q_yw F_z R_yz - q_yz F_w R_yw
  = g q_yz q_yw (Q_yz-Q_yw).
```

The common gcd of the locators is coprime to `g`, so it divides the quotient
difference. That difference cannot vanish: otherwise unique factorization
would force the extra complete fiber `F_w` to divide `R_yz`, violating the
validity filter. Its degree is at most `d`, proving (10).

Summing the three exact normalized differences gives (11). A root common to
two triangle locators is common to the third, so squarefree complete splitting
makes all three pairwise gcds equal. Cancelling that gcd proves (12) and the
split S-unit statement.

Taking resultants of

```text
F_y F_z R_yz = q_yz xi (mod g)
```

gives

```text
rho_y rho_z Res(g,R_yz)=q_yz^a kappa,
```

which is (13). Four copies cancel to (14). The image of the `a`th-power map
on the cyclic group `F_p^*` is its subgroup of sixteenth powers. The
constant-term assertion and (15) follow from complete `H`-splitting.

## Exact use of the inherited graph reduction

This note consumes, and does not reclaim, the integrated fixed-26 compiler's
38 interpolants, 703 pairs, collision criterion, graph reduction, and
monomial-generator cap 37. Its graph reduction says that a putative 117-edge
cell has either:

1. a collision class of size at least 9; or
2. an 8-label collision class with at least 25 valid edges.

In the second branch, the complement has at most three edges. Hence there are
at least two universal vertices, at least `56-3*6=38` valid triangles, and at
least `210-3*30=120` valid four-cycles. The present theorem upgrades each
available anchor, triangle, and four-cycle only to the local structural
constraints above.

After the separately owned rank-two classification, a non-global seven-star
is reduced only to spectral ranks at least 3. No rank-at-least-3 exclusion is
proved here.

## Ownership, consumers, and risk limits

Inherited and not reclaimed:

- the fixed-26 compiler's 38 interpolants, 703 pairs, collision criterion,
  graph reduction, and monomial cap 37;
- the fixed-27 affine-line obstruction;
- the rank-two cubic/quartic classification;
- every global first-match owner and ledger count.

Potential consumers are a future proof of `G64-CAP`, a future exclusion of
the non-global rank-at-least-3 split-star object, and a future independently
proved global aggregator. None is available in this note.

Risk limits and nonclaims:

- no local cap 116;
- no exclusion of 117 valid edges;
- no all-core cap;
- no multiplication over generators, rays, cores, or source cells;
- no global-ledger or first-match payment;
- no rank-16 parent closure;
- no finite or asymptotic Grand List theorem;
- no Grand MCA theorem;
- no official score movement.

## Exact remaining wall

The global local-cell wall is **G64-CAP**: prove that the prescribed family

```text
rem_g(W (T^64-1)/((T-y)(T-z)))
```

contains at most 116 valid pairs among the 703 label pairs outside the fixed
core, uniformly over the literal source data.

The non-global wall is the rank-at-least-3 seven-star object: seven linearly
independent, completely `H`-split, pairwise-gcd-bounded locators in one
source-fixed Krylov system, with all triangle, resultant, cycle, and
constant-term constraints retained.

Even either local result would still require a separate, source-valid global
aggregation across generators, projective rays, cores, and first-match source
cells. This note makes zero progress by ledger arithmetic alone.

## Reproducibility

The standard-library verifier is
`experimental/scripts/verify_rank16_fixed26_spectral_resolvent.py`. It pins
the inherited compiler artifacts, checks the deployed constants and graph
counts, independently replays the minimal-polynomial, resolvent, collapse,
Krylov, and resultant identities in a finite quotient algebra, and rejects
semantic mutations that reverse (9) or (13) or promote any forbidden scope.
