# M31 interior padding bridge: diagonal saturation and a masked-root counterpacket

## Status

**COUNTEREXAMPLE_NEW_FLOOR / AUDIT / MERSENNE-31 LIST ROW OPEN / LEDGER MOVEMENT ZERO.**

This packet audits exactly one deployed row and one terminal: the Mersenne-31
adjacent list row and `UNPAID_PADDING_BRIDGE` in
`experimental/notes/thresholds/m31_canonical_popov_rank46_compiler.md`.

The audit has a precise negative conclusion.  The canonical padded locator row
and the actual-error locator row do not have canonically identical syzygy
modules at an interior weight.  The exact bridge is a **coordinatewise
diagonal-saturation submodule**, and the current rank-46 Forney bounds control
the full actual-error syzygy module rather than that submodule.  A genuine
`RS[F_11,D,4]` counterpacket shows that the actual-error frame can be held fixed
while the canonical first-agreement ordering changes both direct
transportability and the padded pair index.

The terminal is therefore narrowed from an unspecified algebraic interface to

```text
UNPAID_MASKED_DIAGONAL_SATURATION
```

followed, separately, by the already named common-core add-back and rank-two
coloop terminals.  No list upper bound, completion atom, or adjacent-row claim
moves.

## 1. Source objects and deployed parameters

The canonical whole-list compiler fixes an ordered domain and, for each listed
codeword `c`, selects the first `a` agreement points.  Its degree-`R` boundary
locator is

```text
W_c = Lambda_(E_c) Q_c,
```

where `E_c` is the actual error support and `Q_c` is the locator of agreements
discarded after the first-`a` selection.  At an interior error weight `j<R`,

```text
deg Q_c = d = R-j > 0.
```

The roots of `Q_c` are agreements, not errors, and carry no one-point escapes.
This is equation (3.3) and terminal (3.4) of the canonical Popov/rank-46 note.
The same note proves that a hypothetical forbidden M31 list forces at least
`259,881` marked rank-46 actual-error packets and gives, after the actual common
error core is divided out,

```text
mu_1 <= 20,765,
mu_1 + mu_2 + mu_3 <= 62,295 < w=67,447.
```

The deployed constants are

```text
p  = 2^31-1,
n  = 2^21,
K  = 2^20,
a  = 1,116,023,
w  = 67,447,
R  = 981,129,
B* = 16,777,215.
```

Grande Finale v3's `thm:exact-completion-certificate` requires an exhaustive
first-match upper ledger with every atom literally defined and bounded.  It
does not permit an actual-error Forney bound to be inserted into the canonical
Popov cell without the bridge audited here.

## 2. Exact diagonal-saturation identity

Let `F` be a field.  After the common actual-error locator has been divided
out, let

```text
P = (P_1,...,P_t)
```

be the primitive actual-error locator row.  Let `Q_i` be the discarded-agreement
padding locator in column `i`, and put

```text
W_i = P_i Q_i.
```

Write

```text
Syz(P) = {A=(A_i) : sum_i P_i A_i = 0}
```

and define the diagonal-divisibility submodule

```text
DSat_Q(Syz(P))
  = {A in Syz(P) : Q_i divides A_i for every i}.
```

### Theorem 2.1 (diagonal-saturation bridge)

The map

```text
Delta_Q : Syz(W) -> DSat_Q(Syz(P)),
Delta_Q(B_1,...,B_t) = (Q_1 B_1,...,Q_t B_t)
```

is an `F[X]`-module isomorphism.  If every `Q_i` has the same degree `d`, it
shifts every nonzero row degree by exactly `d`:

```text
deg Delta_Q(B) = deg B + d.
```

**Proof.**  If `B in Syz(W)`, then

```text
sum_i P_i(Q_i B_i) = sum_i W_i B_i = 0,
```

and every coordinate is divisible by its `Q_i`.  Conversely, if
`A in DSat_Q(Syz(P))`, write `A_i=Q_i B_i`; then
`sum_i W_i B_i=0`.  These constructions are inverse.  Equal padding degrees
give the displayed degree shift because at least one coordinate is nonzero.
`QED`

Consequently, if

```text
mu_1 <= ... <= mu_(t-1)
```

are the Forney indices of the full actual-error module `Syz(P)`, while

```text
nu_1 <= ... <= nu_(t-1)
```

are the minimal indices of `DSat_Q(Syz(P))`, then the canonical padded row is
governed by

```text
lambda_i = nu_i-d,
```

not by `mu_i`.  The current rank-46 theorem bounds the `mu_i`.  It neither
proves that its first three rows lie in `DSat_Q(Syz(P))` nor bounds the `nu_i`.
That is the exact missing algebraic input.

A basic but load-bearing corollary is:

> A nonzero actual-error row of degree `<d` cannot transport directly, because
> every nonzero coordinate divisible by a degree-`d` polynomial has degree at
> least `d`.

## 3. Exact pair law and the mixed-padding statistic

For two equal-weight columns, let the actual error root sets be `E_0,E_1`, each
of size `j`, and the padding root sets be `P_0,P_1`, each of size `d`.  The
within-column sets are disjoint.  Put

```text
c = |E_0 intersect E_1|,
m = |(E_0 union P_0) intersect (E_1 union P_1)| - c.
```

Thus `m` is the number of padded common roots that are not common actual errors.
For split squarefree locators, the unique primitive pair-syzygy degrees are

```text
mu_error = j-c,
mu_padded = (j+d)-(c+m) = mu_error+d-m.        (3.1)
```

The minimal actual-error generator transports directly precisely when

```text
P_0 subset E_1  and  P_1 subset E_0.           (3.2)
```

Indeed, after the actual common gcd is removed, its two coordinates are the
opposite reduced locators.  Condition (3.2) is exactly the root-set form of
`Q_0 | A_0` and `Q_1 | A_1`.

If (3.2) fails, the smallest common scalar multiplier needed to enter the
diagonal-divisibility submodule has root set

```text
(P_0 \ E_1) union (P_1 \ E_0)
```

and degree `2d-m`.  Hence the least diagonally divisible multiple of the
minimal actual pair row has degree

```text
mu_error + 2d-m,
```

which maps to the padded degree in (3.1) after subtracting `d`.  This is an
exact obstruction statistic, not an asymptotic loss.

## 4. Genuine `F_11` Reed--Solomon counterpacket

Take the nine-point subset `D={0,...,8}` of `F_11` and

```text
C = RS[F_11,D,4].
```

Use the degree-`<4` codewords

```text
c_0(X)=0,
c_1(X)=X(X-1)(X-2),
```

and the received word

```text
x       0 1 2 3 4 5  6 7 8
y(x)    0 0 0 0 0 0 10 1 6.
```

The exact agreement and error sets are

```text
A_0={0,1,2,3,4,5},    E_0={6,7,8},
A_1={0,1,2,6,7,8},    E_1={3,4,5}.
```

At threshold `a=5`, the canonical boundary radius is `R=4`, while both
codewords have actual weight `j=3<R`.  This is a literal interior listed pair,
not an abstract support design.

### 4.1 Cross-error padding order

With domain order

```text
O_cross=(0,1,2,3,4,5,6,7,8),
```

the first-five selector gives

```text
T_0={0,1,2,3,4},  P_0={5},  W_0 roots={5,6,7,8},
T_1={0,1,2,6,7},  P_1={8},  W_1 roots={3,4,5,8}.
```

The actual common error core is empty, while the padded common roots are
`{5,8}`.  Both are mixed-status roots: `5` is padding for column 0 and an error
for column 1; `8` has the opposite status.  Condition (3.2) holds.  The minimal
actual pair row transports, and

```text
mu_error=3,     mu_padded=2.
```

### 4.2 Common-agreement padding order

Keep the same field, code, received word, codewords, agreements, and actual
error locators, but use the fixed order

```text
O_common=(0,1,3,4,5,6,7,8,2).
```

Now the first-five selector gives

```text
T_0={0,1,3,4,5},  P_0={2},  W_0 roots={6,7,8,2},
T_1={0,1,6,7,8},  P_1={2},  W_1 roots={3,4,5,2}.
```

Again the actual common error core is empty, but the padded gcd contains the
common discarded agreement `2`.  Condition (3.2) fails: the minimal
actual-error pair generator is not coordinatewise divisible by `X-2`.  Its
least diagonally divisible multiple has degree `4`, while the padded primitive
pair index is `3`.

The two ordered instances therefore have the **same actual-error Forney frame**
and different canonical padding bridges:

```text
                         O_cross       O_common
actual pair index             3              3
minimal row in DSat_Q        yes             no
padded pair index              2              3.
```

This falsifies every bridge theorem whose hypotheses retain only the
actual-error locator row and its Forney indices.  The canonical selector,
root-status masks, and coordinatewise divisibility data are mathematically
load-bearing.

## 5. Deployed numerical route cut

For an M31 packet in error-weight layer `j`, every padding locator has degree

```text
d=R-j=981,129-j.
```

Direct transport of an actual row of degree `mu` requires

```text
mu = lambda+d
```

for some padded row degree `lambda`, hence `mu>=d`.

The existing uniform rank-46 bounds therefore imply:

```text
j <= 960,363  => d >= 20,766 > mu_1,
```

so the first certified actual-error row cannot directly transport; and

```text
j <= 918,833  => d >= 62,296 > mu_r  for r=1,2,3,
```

so none of the first three certified rows can directly transport.

The current source theorem forces marked packets only somewhere in the broad
interior range above `J_0=614,160`; it does not force them into the narrow
near-boundary band `j>=918,834`.  Its sharp arithmetic relaxation is compatible
with one excess object at every weight `721,249,...,981,129`; exactly `197,585`
of those weight positions lie in the three-row blocked band.  As in the source
note, this extremizer is an arithmetic route cut and is not claimed to be
realized by Reed--Solomon codewords.

Thus the existing `62,295<67,447` inequality is not a canonical Popov payment.
Before it can enter a first-match cell, one must either prove a masked
saturation theorem for the relevant source keys or route the blocked interior
layers to a different semantic owner.

## 6. Audit verdict and exact successor theorem

```text
COUNTEREXAMPLE_NEW_FLOOR
```

The counterexample is to the unmasked inference

```text
low actual-error Forney frame
  ==> corresponding low canonical padded/Popov frame.
```

The corrected successor input is:

```text
MASKED_DIAGONAL_SATURATION
```

For every marked rank-46 source key it must retain and certify:

1. the received center, exact codewords, and exact-weight layer;
2. the fixed ordered domain and first-`a` stopping selector;
3. the actual error sets `E_i`, padding sets `P_i`, and locators `Q_i`;
4. either coordinatewise divisibility of named actual-error syzygy rows or a
   direct construction of padded syzygy rows;
5. the diagonal-saturation indices `nu_i` and the shifted padded indices
   `nu_i-(R-j)` with exact constants;
6. the semantic witness-to-owner or witness-to-residual chain; and
7. the signed occupancy credits from equation (5.4) of the rank-46 compiler,
   carried through the terminal without duplication.

Only after that input is supplied may the already separate
`UNPAID_COMMON_CORE_ADD_BACK` and `UNPAID_RANK2_COLOOP` branches be addressed.

## 7. Lean certificate and proof boundary

The stdlib-only module

```text
experimental/lean/m31_q_rooted_shell/
  M31QRootedShell/PaddingBridgeAudit.lean
```

kernel-checks:

- both ordered copies of the nine-point `F_11` domain;
- the polynomial evaluation table for `X(X-1)(X-2)`;
- the received word, exact agreement sets, exact error sets, and interior
  list condition;
- identity of the actual-error frame under the two orderings;
- both canonical selections, padding sets, padded root sets, and common roots;
- direct pair-transport success in `O_cross` and failure in `O_common`;
- the actual and padded pair-index arithmetic;
- the generic degree obstruction `mu<d` to direct diagonal transport;
- the exact M31 blocked-weight cutoffs; and
- the `197,585` arithmetic-extremizer weight count.

The polynomial-module isomorphism in Theorem 2.1 and the split-squarefree pair
law are proved in this note.  The Lean module validates their complete finite
counterpacket and integer consequences; it does not claim a general formalized
polynomial-ring/Forney theory.

Authoritative validation is the fork draft-PR build on Lean `v4.31.0`, stdlib
only.  No local Lean build is part of the packet.

## 8. Nonclaims

- The Mersenne-31 list row remains open.
- No forbidden M31 center is constructed.
- No `U_Q`, `U_list-int`, boundary, whole-ball, or completion atom is banked.
- The sharp occupancy extremizer is not claimed source-realized.
- The audit does not pay common-core add-back or the rank-two coloop branch.
- It does not construct an exhaustive C1--C8 owner atlas or prove row-sharp Q.
- It does not identify the global rank-two Popov basis with any local
  actual-error Forney basis.
- No stable-paper TeX, deployed radius, official score, or prize claim changes.
