# Rank-16 fixed-27 cubic reducibility and conductor budget

**Status:** PROVED LOCAL THEOREM / CONDITIONAL SOURCE PACKAGE / ZERO PAYMENT.

This note packages the theorem prose accepted from external ChatGPT Pro R28
Role 03. It is packaging and audit work, not a new theorem-generation pass.
The worker printed hashes for a verifier and expected transcript, but those
attachments were not returned. The repository verifier accompanying this note
is an independent stdlib-only reconstruction from the accepted proof and its
printed exact output. It is not represented as the unavailable worker file.

## Provenance and dependency pins

The repository base is exactly
`origin/main@7f278167e1e51f968896229ae438ea5a76398f90`.

The source chain is:

1. the integrated quotient-line obstruction formerly published as PR #826;
2. the integrated fixed-27 block-wedge theorem formerly published as PR #843;
3. the fixed-27 residual specialization curve at exact pending PR #863 head
   `55fa998275db505214347db296bdd8e38a3896e6`.

The first two source notes and their replay files are present at the pinned
base. PR #863 is a conditional dependency, not a theorem reclaimed here. Its
consumed statements are the literal fixed-27 source equation, quotient affine
rank two, the primitive syzygy, `e in {3,4}`, the coordinate formula, the
specialization curve, and the seven-label consequence `kappa_B(g)<=1`.

All source hashes, the Role 03 packet and return hashes, and the hashes claimed
for the missing worker attachments are recorded in
`experimental/data/certificates/rank16-fixed27-cubic-divisor-conductor/source_manifest.json`.
The reconstructed verifier pins that manifest, this theorem statement, and
every dependency file available at the base. If PR #863 changes, this package
must fail review until its statement and pins are refreshed.

## Literal source cell

Work at the deployed constants

```text
p = 2130706433 = 127*2^24+1,
H = mu_(2^21) in F_p^x,
n = 2097152,
B = 32768,
t = 981105,
a = 67472,
D = t-27B = 96369,
d = D-B = 63601,
w = D-a = 28897.
```

The auxiliary identities are

```text
3B-a = 30832,
B-w = a-d = 3871,
d-w = a-B = 34704,
a-2B = 1936.
```

Fix one and the same 27-label `q64` core, root-free monic generator `g` of
degree `a`, syndrome representative/projective ray, and normalized source
cell. Assume seven actual labels in the cubic rank-two branch

```text
e=3,                 kappa_B(g)<=1.
```

Every label `y_i` retains the complete source conditions and has

```text
A_i(X) = (T-y_i)R_i(X) = q_i h(X)+g(X)W_i(X),
T = X^B,
q_i != 0,
g(x) != 0 for every x in H,
deg R_i = d,
deg W_i <= w.
```

Each `R_i` remains monic, squarefree, and completely split over `H`, with
selected-fibre avoidance, no extra complete `q64` fibre, residual footprint
at least four, and the `q32` full-pair restriction. Put

```text
P_i = q_i^(-1)A_i = h+gV_i,
rho_i = q_i^(-1)R_i.
```

The consumed primitive rank-two syzygy supplies polynomials `a_0,a_1,a_2`
such that

```text
a_0(T)H_0+g(a_1(T)E_1+a_2(T)E_2)=0,
a_0(T)=g(X)s(X),
deg a_0=3,
gcd(a_0,a_1,a_2)=1,
a_0(y_i)!=0,
c_ij=a_j(y_i)/a_0(y_i).
```

Scale the primitive triple so that

```text
a_0(Z)=Z^3+c_2 Z^2+c_1 Z+c_0
```

is monic.

## Accepted theorem

Under exactly the source hypotheses above, the following five claims hold.

### 1. Divided-difference remainder

Define

```text
N(X,Y)=a_0(Y)H_0(X)+g(X)(a_1(Y)E_1(X)+a_2(Y)E_2(X)).
```

There is a unique polynomial `R(X,Y)` with

```text
N(X,Y)=(T-Y)R(X,Y),
deg_X R<=d,
deg_Y R<=2,
R(X,y_i)=a_0(y_i)rho_i(X).
```

Writing

```text
Q(T,Y)=(a_0(T)-a_0(Y))/(T-Y),
```

one has the exact oriented identity

```text
Q(T,Y)=Y^2+(T+c_2)Y+(T^2+c_2 T+c_1),
R(X,Y)=-rem_g(h(X)Q(T,Y)).                              (1)
```

Thus the three `Y`-coefficients are respectively

```text
-h,
-rem_g((T+c_2)h),
-rem_g((T^2+c_2 T+c_1)h),
```

and each has `X`-degree at most `d`.

### 2. Primitive cubic reducibility

The primitive cubic `a_0` is reducible over `F_p`; equivalently, it has an
`F_p`-linear factor. The irreducible-cubic branch is empty.

### 3. Nested divisor-deficit budget

Over a common splitting field write

```text
a_0(Y)=product_alpha (Y-alpha)^m_alpha,
F_alpha(X)=X^B-alpha.
```

For every nonzero root, assign the factors of the `alpha` part of `g` to
nested monic layers

```text
G_(alpha,m_alpha) | ... | G_(alpha,2) | G_(alpha,1) | F_alpha.
```

If `alpha=0` and `v_X(g)=k`, use the canonical monomial layers

```text
G_(0,nu)=X^e_nu,
e_nu=min(B,max(k-(nu-1)B,0)).
```

For every layer put `S_(alpha,nu)=B-deg G_(alpha,nu)`. Then

```text
0<=S_(alpha,1)<=...<=S_(alpha,m_alpha)<=B,
sum_(alpha,nu) S_(alpha,nu)=3B-deg g=30832.             (2)
```

For each distinct root, the first-layer specialization gives a nonzero
polynomial `M_alpha` satisfying

```text
L_alpha=(F_alpha/G_(alpha,1))M_alpha,
R_alpha=(g/G_(alpha,1))M_alpha,
deg M_alpha<=w-S_(alpha,1).                              (3)
```

Consequently

```text
S_(alpha,1)<=w=28897,
deg G_(alpha,1)>=B-w=3871.                              (4)
```

Equations (2)-(4) include repeated-root and zero-root cases; no hidden
squarefreeness assumption on `g` is used.

### 4. Kummer conductor bounds

For a nonzero root `alpha`, let `K_alpha=F_p(alpha)` and define

```text
delta_alpha=ord([alpha]) in K_alpha^x/(K_alpha^x)^B.
```

For a zero root set `delta_0=1`. Every `delta_alpha` is a power of two
dividing `B`, every irreducible factor of `X^B-alpha` over `K_alpha` has
degree exactly `delta_alpha`, and

```text
delta_alpha | deg G_(alpha,nu),
delta_alpha | S_(alpha,nu).
```

Since `67472 == 16 (mod 32)`, some root block has

```text
delta_alpha<=16.                                        (5)
```

In the linear-times-irreducible-quadratic case, let `S_0,delta_0` denote the
linear block and `S_2,delta_2` the common quantities on the two conjugate
quadratic blocks. Then

```text
S_0+2S_2=30832,
968<=S_2<=15416,
delta_0<=16 or delta_2<=8.                              (6)
```

In particular, if `S_0=0`, then `S_2=15416=8*1927` and
`delta_2<=8`. The compatible factor-type arithmetic supports (5)-(6); it is
not a claim that any remaining factor type is excluded.

### 5. Squarefree resultant factorization

If `a_0` is squarefree, then over its splitting field

```text
Res_Y(a_0(Y),R(X,Y))
  = g(X)^2 M(X),
M(X)=product_(a_0(alpha)=0) M_alpha(X).                 (7)
```

The multiplier is Galois invariant and lies in `F_p[X]`. Its degree obeys

```text
deg M<=3w-30832=55859,
deg_X Res_Y(a_0,R)<=2a+55859=190803=3d.                 (8)
```

## Proof audit

Substitution `Y=T` gives `N(X,T)=0`, hence the polynomial remainder theorem
gives `(T-Y)|N`. Modulo `g`, one has `H_0==h` and

```text
a_0(Y)==-(T-Y)Q(T,Y).
```

Since `gcd(g(X),X^B-Y)=1` in `F_p(Y)[X]`, cancellation gives
`R==-hQ (mod g)`. The degree bound `deg_X R<deg g` selects the unique
remainder and proves (1), including its minus sign and coefficient order.

If `a_0` were irreducible cubic and `r(X)` were any irreducible factor of
`a_0(X^B)`, then for a root `xi` of `r`, the element `alpha=xi^B` has degree
three over `F_p`. The tower law gives `3|deg r`. Since `g|a_0(X^B)`, every
irreducible-factor degree contributing to `deg g` is divisible by three, but

```text
67472 == 2 (mod 3),
```

a contradiction. This proves primitive cubic reducibility.

Factoring `a_0(T)` over the splitting field and assigning a factor to layer
`nu` exactly when its exponent in `g` is at least `nu` gives (2). For a zero
root the displayed monomial layers give the same identity directly. At a
root `alpha`, specialization gives

```text
F_alpha R_alpha=g L_alpha.
```

After cancelling the first layer, the complementary factors are coprime;
Euclid's lemma gives (3). Since `deg L_alpha<=w`, equations (3)-(4) follow.

Because `B|p-1`, all `B`th roots of unity lie in every `K_alpha`. Standard
Kummer theory can be read directly: if `xi^B=alpha`, the Galois image embeds
in `mu_B`; its order is both `[K_alpha(xi):K_alpha]` and the order of
`[alpha]` modulo `B`th powers. Thus every factor degree is exactly
`delta_alpha`. If no zero block existed and every conductor were at least
32, every deficit in (2) would be divisible by 32, contrary to
`30832 == 16 (mod 32)`. This proves (5). In the quadratic case, simultaneous
`delta_0>=32` and `delta_2>=16` would make both `S_0` and `2S_2` divisible by
32, again contradicting (6); because the conductors are powers of two, the
stated alternative follows.

For squarefree `a_0`, its three first layers multiply to `g`. Multiplying the
three identities `R_alpha=(g/G_(alpha,1))M_alpha` therefore contributes each
first layer twice, giving exactly `g^2`. Summing the three bounds in (3) and
using (2) gives (8).

## Exact nonclaims and ledger impact

This theorem does **not** prove nonexistence of the seven-label
`e=3, kappa_B(g)<=1` family. It does not construct such a family, exclude all
reducible cubic factor types, turn the small-conductor block into an
`H`-splitting contradiction, or turn (8) into a contradiction. It makes no
fixed-27 cap-six claim and no seven-label closure.

It supplies no reverse source construction, first-match owner, or disjoint
aggregation over generators, syndromes, projective rays, cores, or profiles.
It makes zero finite payment, zero asymptotic payment, zero recurrence-parent
payment, no rank-16 closure, no Grand List or Grand MCA claim, and no official
score movement. The official score remains `0/2`.

## Reconstructed replay

The unavailable worker attachments were claimed as

```text
R28_ROLE03_CUBIC_DIVISOR_CONDUCTOR_REPLAY.py
sha256 ad0ef2f27eb234d19d0c5a7a30fc3745921a48ac99d62201c4a72ce014f55524

R28_ROLE03_CUBIC_DIVISOR_CONDUCTOR_REPLAY.expected.txt
sha256 ee774950f25653a898673062c1416ee8e677f33c323e124f3a7c895e9d03de55
```

The reconstructed repository verifier checks the pinned statement and source
manifest, deployed constants, exact cubic divided difference, irreducible
degree obstruction, repeated/zero divisor layers, all 110,196 compatible
linear-quadratic conductor cases, squarefree resultant exponents and degree
arithmetic, expected transcript, and fail-closed semantic mutations.

Replay with a stdlib Python interpreter:

```bash
python3 experimental/scripts/verify_rank16_fixed27_cubic_divisor_conductor.py
python3 -O experimental/scripts/verify_rank16_fixed27_cubic_divisor_conductor.py
python3 experimental/scripts/verify_rank16_fixed27_cubic_divisor_conductor.py --tamper-selftest
python3 -O experimental/scripts/verify_rank16_fixed27_cubic_divisor_conductor.py --tamper-selftest
python3 -m py_compile experimental/scripts/verify_rank16_fixed27_cubic_divisor_conductor.py
git diff --check
```

Normal and optimized output must be byte-identical to each other and to
`experimental/scripts/verify_rank16_fixed27_cubic_divisor_conductor.expected.txt`.
