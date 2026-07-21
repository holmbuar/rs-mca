# One loss-one C9 prefix key on the deployed Mersenne-31 Chebyshev row

## Status

```text
Activity: PROVE one scoped instance of hard input 3.

PROVED_SCOPED_ONE_KEY:
  - one exact full-prefix fiber has cardinality one;
  - the owner-complement residual is stated literally as slice membership plus
    `earlierOwner = none`;
  - the bound has compiler loss one and integral natural scale two (the exact ceiling of `70/69`);
  - any genuine SE2 support projection on that residual key receives a direct
    loss-one C9 payment.

CONDITIONAL_ON_NAMED_INPUT:
  M31_C9_GLOBAL_OWNER_COMPLEMENT_AND_KEY_COVERAGE.
```

This is a local deployed-row theorem, not row closure.  It proves the exact
content of one future `C9ResidualMaxFiber.ProfileData.rowSharpMaxFiber` field.
It does not prove that every deployed C9 key is of this type or that the
profile occurs in a row-uniform exhaustive atlas.

## 1. Exact target and statement discipline

The active source nodes are:

- `def:primitive-q` and `lem:logmoment-q` for max-fiber Q;
- `def:q-row-atom` for the finite row-sharp atom;
- `prop:q-exact-target` for the four deployed row constants;
- `eq:image-ambient-scales` for the realized-image normalization;
- `lem:newton-equivalence` for power sums versus locator coefficients;
- `lem:profile-multiplicity` for the separate profile-count obligation;
- `hyp:ray-compiler`, `prop:q-implies-sp`, and `(SE2)` for the separate
  support-to-slope projection.

The imported C9 producer field has the literal form

```text
(fullPrefixFiber leaf syndromeKey).length
  <= compilerLoss * naturalScale.
```

The residual condition is restated standalone, without importing the open
producer module:

```text
x in residual
  <-> x in the complete fixed-weight slice
      and earlierOwner x = none.
```

The theorem below uses exactly that order.  It first proves the full-prefix
fiber bound, then lets arbitrary earlier deletion only reduce the selected
residual fiber, and finally consumes a separately supplied genuine `(SE2)`
certificate.  It does not manufacture a Sidon statement from the direct
payment side.

## 2. Denominator and row ledger

All fields and denominators remain separate.

| object | value or status |
|---|---|
| generated/prefix field `q_gen` | `p = 2^31-1 = 2,147,483,647` |
| deployed M31 list prefix depth | `w = 67,447` |
| deployed complement support size | `m = 981,129` |
| M31 list integer budget `B*` | `2^24-1 = 16,777,215` |
| full-row average ceiling from `prop:q-exact-target` | `1,993,678` |
| full-row allowed Q ratio before other charges | `8.4152...` |
| local source mass | `M_local = C(8,4) = 70` |
| local realized image size | `L_local = 69` |
| local image average | `70/69` |
| selected full fiber | `1` |
| local compiler loss | `1` |
| local integral natural scale | `2 = ceil(70/69)` |
| line field `q_line` | not instantiated by the support theorem |
| challenge denominator `q_chal` | not instantiated |
| list denominator `q_list` | the deployed budget above; not identified with `q_gen` |

The exact image-normalized cleared inequality is

```text
1 * 69 <= 70.
```

Thus the normalized loss is `69/70 < 1`.  The integer field supplied to the
producer is even stronger:

```text
1 <= 1 * 2.
```

No polynomial or subexponential multiplier is used.

## 3. Eight actual deployed-domain points

Let `p=2^31-1`.  In the norm-one group of `F_(p^2)`, the stereographic point

```text
g = (1717986917, 1288490189)
```

has norm one and exact order `2^31`.  For a norm-one element `u`, put
`x(u)=(u+u^(-1))/2`.  Taking exponents

```text
256 + j*2^29,       768 + j*2^29,       j=0,1,2,3,
```

gives the eight `F_p` values

```text
434373082,  614288294, 1713110565, 1533195353,
1984437538, 380812851,  163046109, 1766670796.
```

The identity

```text
T_d(x(u)) = x(u^d)
```

shows that all eight are roots of `T_(2^21)`: multiplying either base exponent
by `2^21` gives an odd multiple of `2^29`, while the `j*2^29` shift disappears
modulo the group order after multiplication by `2^21`.

The first four points form one complete `T_4` fiber and the last four another:

```text
T_4(first block)  = 1,884,637,334,
T_4(second block) =    51,044,589.
```

The Lean module does not rely on the group derivation.  It checks the eight
printed residues directly by the recurrence

```text
T_(2d)(x)=2*T_d(x)^2-1 mod p
```

through depth 21, and checks both exact `T_4` values.

## 4. The complete local slice and the exact owner complement

Let `Omega` be the complete set of four-subsets of these eight points.  Encode a
support by its eight-bit Boolean incidence vector.  The first three power sums
form the prefix key

```text
Phi(S)=(sum x, sum x^2, sum x^3) in F_p^3.
```

There are `70` supports and `69` realized keys.  The only nonsingleton full
fiber is

```text
z_coll=(0,2,0),
```

whose two members are exactly the two complete `T_4` blocks.

The scoped earlier-owner function has the complete constructor grammar C1
through C8.  Its nonempty branch is the exact complete-fiber C1 quotient for
`x -> x^2`.  The eight points form four antipodal pairs, and a weight-four
support is C1-owned exactly when it is the union of two such pairs.  There are
six of these supports:

```text
earlierOwner(S) = some C1,  if S is a union of two antipodal pairs;
earlierOwner(S) = none,     otherwise.
```

The two complete `T_4` blocks in the doubled key are among those six C1-owned
supports.  The residual is defined by filtering the full slice with that
function.  Lean proves the literal equivalence

```text
S in residual
  <-> S in Omega and earlierOwner(S)=none.
```

It also proves:

```text
|C1-owned supports| = 6,
|residual| = 64,
Phi is injective on residual,
residual fiber over (0,2,0) is empty.
```

This is an exact local owner-complement specification.  It is not advertised as
an exhaustive C1--C8 classifier for all supports of the deployed row.

## 5. The selected row-sharp key

Choose the quotient-free support with mask `51`, namely indices

```text
{0,1,4,5}.
```

It contains no complete antipodal pair, hence is outside the displayed C1
quotient owner.  Its exact prefix key is

```text
z_*=(1,266,428,118, 2, 458,186,840).
```

The complete, pre-deletion fiber is already

```text
fullPrefixFiber(z_*) = [{0,1,4,5}].
```

Therefore the post-deletion fiber is the same singleton, and

```text
fullPrefixFiber(z_*).length <= 1 * 2.
```

This theorem is definitionally the field needed by the future producer.  Once
the producer is integrated, its adapter line is:

```text
rowSharpMaxFiber :=
  SidonEffectiveImage.M31C9RowSharp.fullPrefixFiber_rowSharp
```

The exact owner and residual fields are likewise generic in the future owner
type and instantiate without a translation layer:

```text
earlierOwner  := SidonEffectiveImage.M31C9RowSharp.earlierOwner .c1
residual_exact := SidonEffectiveImage.M31C9RowSharp.residual_exact .c1
```

No theorem from the open producer PR is imported here.

## 6. Embedding into the exact deployed row

Use the complement-side parametrization from the current M31 Q packet:

```text
n       = 2,097,152,
m       =   981,129,
w       =    67,447.
```

Fix `m-4=981,125` complement points outside the displayed eight-point active
set and choose four active points.  The availability inequality is literal:

```text
981,125 <= 2,097,144 = n-8.
```

If `P` is the fixed outside locator and `A` the monic active degree-four
locator, the global locator is `P*A`.  Its first coefficients satisfy the
unitriangular identities

```text
q1 = p1+a1,
q2 = p2+p1*a1+a2,
q3 = p3+p2*a1+p1*a2+a3.
```

Thus, after `P` is fixed, the first three global coefficients recover the first
three active coefficients successively.  Since `w>=3`, equality of the full
depth-`w` prefix inside this fixed profile implies equality of the active first
three coefficients.  Newton's triangular identities are invertible because
`p>3`, so they are equivalent to the three power sums used above.

Consequently the selected key supplies a singleton full prefix fiber inside
this exact deployed profile.  This is the finite profile-local meaning of the
Lean field.  The theorem does not sum over the possible fixed outside locators.

## 7. Genuine slope projection is retained

The Lean theorem does not define a fake slope.  Instead it accepts an arbitrary
integrated

```text
SE2Certificate Support Nat
```

whose support list is a sublist of the selected residual prefix fiber.  It then
proves the exact chain

```text
selected slopes
  <= selected supports                    by SE2
  <= residual prefix fiber
  <= full prefix fiber
  <= 1 * 2.
```

The resulting `ProfilePayment.ofDirect .c9` is therefore a direct payment.  Its
Sidon and residual stages are identities, exactly as required by the producer
boundary.  An actual received-line construction of the SE2 certificate remains
an explicit semantic input and is not inferred from support data.

## 8. Exact deployed comparison

The exact support fiber is one, the integral profile charge is two, and the literal M31 list budget comparison is

```text
2 <= 16,777,215.
```

This proves one row-sharp key with zero slack.  It does not allocate the other
row cells or claim that the full budget remains available after them.

## 9. Ledger impact and named residual

### What is proved

- one actual M31 Chebyshev-domain fixed-weight profile;
- exact complete-slice enumeration;
- exact C1 antipodal-quotient owner complement;
- exact singleton full prefix key;
- exact image-normalized loss below one;
- the loss-one future producer field with exact integral scale two;
- the exact SE2-to-direct-payment compiler on that key;
- exact compatibility with the deployed M31 integer budget.

### What remains

```text
CONDITIONAL_ON_NAMED_INPUT:
M31_C9_GLOBAL_OWNER_COMPLEMENT_AND_KEY_COVERAGE
```

This means:

1. construct the actual fixed-before-line C1--C8 owner function on the deployed
   row;
2. prove which realized profiles and keys survive it;
3. cover every surviving key by loss-one row-sharp certificates, or produce an
   exact counterexample;
4. prove a genuine SE2 support projection for each paid slope cell;
5. pay profile multiplicity, residual add-back, and the line-local UNIF sum.

## 10. Explicit nonclaims

- No theorem for every M31 prefix key.
- No global fixed-before-line C1--C8 atlas.
- No claim that only C1 is nonempty on the complete deployed row.
- No profile-count or fixed-outside-locator census.
- No general residual-to-full add-back.
- No image-normalized Sidon or MI+MA theorem.
- No synthetic conversion from support fibers to slopes.
- No list-interior, balanced-core, extension, or quotient payment.
- No adjacent-row completion certificate, stable-paper promotion, official
  score, or prize claim.
