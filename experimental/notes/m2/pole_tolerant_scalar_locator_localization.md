# Pole-tolerant scalar-locator localization

Status: `PROVED_LOCAL_THEOREM / INDEPENDENT_AUDIT_ACCEPT_NARROWED`

This note isolates two source-compatible algebraic facts about the
scalar-locator certificates in `experimental/grande_finale.tex`.  The first
localizes overlaps without dividing by the denominator.  The second removes
common denominator poles when the locators are the exact monic support
locators used by the source.

The result is local.  It supplies no first-match adapter, no ledger payment,
and no official endpoint.

## Setup

Let `F` be a finite field, let `D` be a set of `n` distinct points of `F`, and
let

```text
1 <= k < m <= n.
```

Let `Gamma` be a set of slopes.  Fix received words `r0,r1 : D -> F` and put
`r_gamma = r0 + gamma r1`.

For a finite index set `I`, assume that each `i in I` has:

- a distinct slope `gamma_i in Gamma`;
- a support `S_i subset D` of size `m`;
- a polynomial `h_i` of degree less than `k` agreeing with
  `r0 + gamma_i r1` on `S_i`;
- support-wise MCA nontriviality on `S_i`: no two degree-`< k` polynomials
  simultaneously explain `r0` and `r1` on that support.

Let `Q,A,B` be polynomials with `Q != 0`, let `(c0,c1) != (0,0)`, and write
`c_i = c0 + c1 gamma_i`.  Let each locator `Lambda_i` vanish on `S_i`, and
assume the scalar-locator identities

```text
Q h_i + c_i Lambda_i = A + gamma_i B.                 (C)
```

No root-free assumption is made on `Q` over `D`.

Define the algebraic coincidence core

```text
G_Q = {x in D : A(x) = Q(x) r0(x) and B(x) = Q(x) r1(x)},
g   = |G_Q|.
```

For an evaluation set `E`, define `B^MCA_{F,E,k,Gamma}(a)` as the largest,
over received pairs on `E`, number of distinct slopes with a support of size
at least `a` on which a degree-`< k` combination agrees but the received pair
has no simultaneous degree-`< k` explanation.  This is a slope count, not a
support or codeword count.

## Theorem 1: exclusive localization without denominator division

Under the setup above:

1. For every `x in D \ G_Q`, at most one selected support contains `x`.
2. If `g < m`, then

   ```text
   |I| <= floor((n-g)/(m-g)) <= n-m+1.
   ```

3. If `g >= m`, then

   ```text
   |I| <= n-g + B^MCA_{F,G_Q,k,Gamma}(m).
   ```

4. At the exact boundary `g=m`,

   ```text
   B^MCA_{F,G_Q,k,Gamma}(m) <= 1,
   |I| <= n-m+1.
   ```

### Proof

Fix `i` and `x in S_i`.  Since `Lambda_i(x)=0`, evaluating (C) and using the
agreement of `h_i` on `S_i` gives

```text
(A(x)-Q(x)r0(x)) + gamma_i (B(x)-Q(x)r1(x)) = 0.      (1)
```

If `x` is outside `G_Q`, the two coefficients in (1) are not both zero.
Equation (1) is therefore a nonzero affine equation in `gamma_i` and has at
most one solution in the field.  The slopes are distinct, so `x` belongs to
at most one selected support.  This argument neither divides by `Q(x)` nor
uses `c_i != 0`.

If `g<m`, every support contains at least `m-g` points outside `G_Q`.  The
outside portions of distinct supports are disjoint, so

```text
|I|(m-g) <= n-g.
```

For integral `0 <= g <= m-1`,

```text
(n-m+1)(m-g) - (n-g) = (n-m)(m-1-g) >= 0,
```

which proves the endpoint bound.

Now suppose `g>=m`.  Split `I` into supports contained in `G_Q` and supports
meeting its complement.  Each crossing support consumes a nonempty outside
set, and those sets are pairwise disjoint, so there are at most `n-g`
crossing slopes.  Every contained support remains a support-wise MCA witness
for the restricted received pair on `G_Q`; a simultaneous explanation after
restriction would explain the same original support and contradict the
hypothesis.  This proves the punctured-core bound.  Since `g>=m>k`,
degree-`<k` evaluation on `G_Q` is injective, so the puncture is exactly a
dimension-`k` Reed-Solomon evaluation code.

If `g=m`, every size-at-least-`m` witness support is all of `G_Q`.  If two
distinct slopes `gamma,gamma'` had witnesses `h,h'`, then

```text
p1 = (h-h')/(gamma-gamma'),
p0 = h - gamma p1
```

would simultaneously explain the restricted received pair on all of `G_Q`.
Thus at most one bad slope exists, and the displayed boundary follows.

## Theorem 2: exact-locator common-pole cancellation

Strengthen the locator hypothesis to the source-normalized condition

```text
Lambda_i(X) = product_{x in S_i} (X-x).                (L)
```

Let

```text
I_x = {i in I : c_i != 0},
P   = {x in D : Q(x)=A(x)=B(x)=0},
R(X)= product_{x in P} (X-x).
```

Here `P` equals the set of denominator roots lying in `G_Q`.  Then:

1. At most one index is deleted from `I` to form `I_x`.
2. Every `S_i` with `i in I_x` contains `P`.
3. `R` divides `Q,A,B` and every exact locator `Lambda_i`, `i in I_x`.
4. On

   ```text
   D'        = D \ P,
   S_i'      = S_i \ P,
   Q',A',B'  = Q/R, A/R, B/R,
   Lambda_i' = Lambda_i/R,
   ```

   the exact divided identities hold:

   ```text
   Lambda_i'(X) = product_{x in S_i'} (X-x),
   Q' h_i + c_i Lambda_i' = A' + gamma_i B'.          (C')
   ```

5. The reduced coincidence core is exactly `G_Q \ P`, and `Q'` has no root
   on that reduced core.
6. If the source degree profile is

   ```text
   deg Q = s <= m-k,  deg A,deg B <= m,
   ```

   and `t=|P|`, then

   ```text
   deg Q' = s-t <= (m-t)-k,
   deg A',deg B' <= m-t,
   |S_i'| = m-t.
   ```

### Proof

The affine scalar `c0+c1 gamma` is either a nonzero constant or has exactly
one field root.  Hence at most one slope is deleted.

For `x in P` and `i in I_x`, evaluating (C) gives

```text
c_i Lambda_i(x)=0.
```

Since `c_i != 0`, the exact locator vanishes at `x`, and (L) implies
`x in S_i`.  Therefore every polynomial in `Q,A,B,Lambda_i` vanishes on all
distinct points of `P`, so `R` divides each.  Dividing (C) gives (C'), and
exact monic squarefree normalization gives the reduced locator formula.

For `x in D'`, `R(x) != 0`, so the two coincidence equations before and after
division are equivalent.  This proves the reduced-core identity.  A root of
`Q'` on the reduced core would force `Q,A,B` all to vanish at that point,
putting it back in `P`, a contradiction.  The degree statements follow from
exact division by the degree-`t` polynomial `R`.

The theorem does not assert that support-wise MCA nontriviality survives the
puncture.  It is an algebraic normalization, not a ledger payment.

## Source compiler

The source defines exact monic locators and scalar-locator certificates in
`experimental/grande_finale.tex`, definition `def:certificate`.  Its rational
atom branch explicitly permits denominator roots on `D` and retains them for
a separate first-match branch.  The two theorems above consume exactly that
certificate.  They do not claim that every source atom is paid: an
active-architecture selector still has to show which coherent certificate is
owned, preserve first-match order, and account for any reduction of
support-wise nontriviality after cancellation.

## Audit and replay

The same-author repair archive has SHA-256
`12389f7fbe6064e1e6f964597212f2603cc081808995a4192958be637e476c20`.
The independent hostile-proof audit returned `ACCEPT_NARROWED`; its frozen
public text has SHA-256
`6e0ea5e0cabdca117aee894dbbc2264f1c2d82e0b2b7da48cc8158e0906e1f8f`.

`experimental/scripts/verify_pole_tolerant_scalar_locator_localization.py`
checks the source pin, exact deployed constants, finite-field examples of both
theorems, the zero-scalar deletion, the extra-root failure mode, the exact
`g=m` slope bound, and hostile mutations.  It is corroboration of the finite
seams; the universal proof is the argument above.

## Nonclaims and remaining wall

- No active-v4 first-match adapter is supplied.
- No source cell, owner, refund, reserve, or ledger value is paid.
- No imported CA/CAP25 premise is asserted.
- No Mersenne-31 or KoalaBear endpoint is closed.
- No official score changes; it remains `0/2`.

The exact remaining wall is a source compiler: for every denominator-root
rational atom selected by the active architecture, either preserve
support-wise MCA nontriviality through the cancellation or route the reduced
object to a disjoint existing owner, with chronology-correct add-backs.  The
local algebra here proves what happens inside one coherent certificate; it
does not prove exhaustive ownership of all exceptions.
