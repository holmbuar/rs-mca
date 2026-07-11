# Aperiodic prefix fibers can be one-ray saturated

- **Status:** PROVED route cut.
- **Track:** asymptotic lower reserve / primitive first-match routing.
- **Verifier:**
  `python3 experimental/scripts/verify_aperiodic_one_ray_saturation.py`.

## Theorem

For an integer `r>=5`, put

```text
q=2^r,        D=F_q^x,       n=q-1,
m=2^(r-1)-1, w=floor(n/r^2), k=m-w-1, K=k+1.
```

For an `m`-set `S subset D`, write its locator as

```text
ell_S(X)=X^m+c_1(S)X^(m-1)+...+c_m(S)
```

and refine the usual prefix map by its constant coefficient:

```text
Psi_r(S)=(c_1(S),...,c_w(S),c_m(S)).                    (1)
```

There are `z in F_q^w` and `c in F_q^x` such that the fiber

```text
G_r={S: Psi_r(S)=(z,c)}
```

satisfies

```text
|G_r| >= ceil(binom(n,m)/q^(w+1))
       = exp((log(2)-o(1))n).                            (2)
```

Every support in `G_r` is multiplicatively aperiodic.  Nevertheless, the
entire fiber gives only one bad slope on the base-field pole line for
`RS_(F_q)(D,k)`.

More precisely, define

```text
U_z(X)=X^m+sum_(i=1)^w z_i X^(m-i),
P_S(X)=U_z(X)-ell_S(X).
```

Then `deg(P_S)<K`, the `P_S` are distinct codewords of
`RS_(F_q)(D,K)`, and every one agrees with `U_z` on exactly `S`.  At the
only base-field pole outside `D`, namely `alpha=0`,

```text
P_S(0)=-c                                                   (3)
```

for every `S in G_r`.  Thus all `|G_r|` explanation states project to the
single MCA-bad slope `-c`.

The stronger complete-incidence statement also holds.  In the full prefix
fiber `Fib_w(z)`, define

```text
C_d={S in Fib_w(z): c_m(S)=d},       d in F_q^x.          (4)
```

On the pole line, every `C_d` has final slope image exactly `{-d}`.  The at
most `q-1` nonempty cells in (4) cover every exact-`m` witness of that line.
Consequently an explicit first-match atlas that places these direct
constant-coefficient saturation cells first has empty later residual.
Since

```text
q-1=exp(o(n)),                                             (5)
```

this is a subexponential algebraic routing of an exponentially large,
fully aperiodic prefix profile.

## Proof

The map in (1) has at most `q^(w+1)` values, so pigeonholing the
`binom(n,m)` supports gives (2).  The central-binomial estimate gives

```text
log binom(n,m)=n log(2)-O(log n),
```

while `log q=r log(2)` and

```text
(w+1)log q <= (n/r+ r)log(2)=o(n).
```

This proves the asserted exponential size.

Next,

```text
gcd(m,n)=gcd(2^(r-1)-1,2^r-1)=2^gcd(r-1,r)-1=1.         (6)
```

If an `m`-support were invariant under a nontrivial multiplicative subgroup
of order `d`, it would be a union of `d`-element orbits.  Then `d` would
divide both `m` and `n`, contradicting (6).  Hence every `m`-support, not
only those in `G_r`, is aperiodic.

Fix the first `w` coefficients to `z`.  The leading term and those `w`
coefficients cancel in `P_S`, so

```text
deg(P_S) <= m-w-1=k < K.
```

Also `U_z-P_S=ell_S`, whose roots in `D` are exactly `S`; this proves the
exact list statement and distinctness.  Because `D=F_q^x`, the only
base-field pole is zero.  Here `U_z(0)=0`, while
`ell_S(0)=c_m(S)=c`, proving (3).

Apply the proved pole-line transport proposition at `alpha=0`.  It says
that every exact-`m` witness comes from a unique member of `Fib_w(z)` and
that its slope is

```text
U_z(0)-ell_S(0)=-c_m(S).
```

Partitioning by `c_m(S)` therefore gives (4), with one slope per cell and
complete witness coverage.  There are at most `q-1` cells because a locator
of a subset of `F_q^x` has nonzero constant coefficient.  Finally
`log(q-1)=O(log n)=o(n)`, proving (5).

## Ledger effect

This is the opposite projection extreme from the existing aperiodic
distinct-ray obstruction.  Aperiodicity removes quotient stabilizers, but it
does not force a large slope image or a nonempty primitive residual.  Even an
exponential refined prefix fiber may be completely paid by a subexponential
family of one-slope saturation cells.

Therefore an unsafe-side compiler cannot infer primitive lower reserve from
positive profile entropy plus aperiodicity alone.  It must prove either a
distinct-ray theorem or a quantitative bound on overlap with the earlier
first-match saturation cells.

## Nonclaims

- No canonical pre-atlas is claimed to contain the cells (4) in this order.
- No lower bound for an actual post-algebraic primitive residual is proved.
- No global hard-input-E, hard-input-A, or hard-input-B closure is claimed.
- No finite M31 or KoalaBear survivor count changes.
- No deployed adjacent inequality is proved.
- No paper TeX is changed.
