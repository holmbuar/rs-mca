# M31 rooted-shell lane: a multiplicative-subgroup counterexample to support-only `3+7`

**Status:** `COUNTEREXAMPLE_TO_SUPPORT_ONLY_3PLUS7 / LEAN-PROVED EXPLICIT PACKET / AUXILIARY EXHAUSTIVE CENSUS / OPEN DEPLOYED EXACT RESIDUAL`

**Track:** `prob:row-sharp-q`, exact-residual C9 rooted-shell lane.

**Source interface:** `experimental/notes/thresholds/m31_q_rooted_shell_envelope.md`.

**Lean validation:** `experimental/lean/m31_q_rooted_shell/M31QRootedShell/MultiplicativeCounterexample.lean` in the existing stdlib-only package.

**Auxiliary replay:** `experimental/scripts/verify_m31_q_three_plus_seven_multiplicative_counterexample.py`.

**Certificate:** `experimental/data/certificates/m31-q-3plus7-multiplicative-counterexample/m31_q_three_plus_seven_multiplicative_counterexample.json`.

## 1. Result

The local rooted-shell inequality

```text
p^w max(d_e(A)-3,0) <= 7 C(m,e) C(n-m,e)                 (3+7)
```

is **false** if the phrase “first-match pruned” is replaced only by the
following support-level filters:

1. delete every support invariant under a nonidentity multiplicative quotient
   symmetry or scale-inversion symmetry of the domain; and
2. delete a prefix target when all remaining supports share a planted point.

The counterexample is a genuine multiplicative-subgroup control:

```text
field       F_241,
domain      H=<235> subset F_241^*,  |H|=20,
support     m=10,
prefix      w=2,
target      z=(e_1,e_2)=(92,135).
```

The exact target fibre has `17` ten-subsets. Two are fixed by the reflection
`i -> 17-i mod 20` and are deleted. The remaining family `F_z` has `15`
supports, every one with trivial stabilizer under the full order-`40`
dihedral action

```text
i -> i+s,       i -> s-i                 (mod 20).
```

Its total common core is empty. In particular, every retained support is
outside every complete multiplicative-quotient fibre and every support-level
dihedral fibre, and the retained target is outside the literal planted-core
proxy.

For the anchor

```text
A={2,5,6,10,11,13,14,17,18,19},
```

the other `14` supports have exchange-distance distribution

```text
distance 5 : 1
distance 6 : 10
distance 7 : 3.
```

No distance-six neighbor lies in the dihedral orbit of `A`, and the anchor plus
all ten distance-six neighbors have empty common core. At `e=6`,

```text
H_6 = C(10,6)^2 = 44,100,
Q   = 241^2      = 58,081,
d_6(A)=10.
```

Therefore

```text
Q(d_6(A)-3) = 406,567
             > 308,700 = 7 H_6,
```

with exact margin

```text
406,567 - 308,700 = 97,867.                              (1)
```

The neighboring intercept `4` also fails:

```text
Q(d_6(A)-4)=348,486 > 308,700,
```

while intercept `5` is the first of these three to hold:

```text
Q(d_6(A)-5)=290,405 <= 308,700.
```

Equivalently, with intercept `3`, the least integer shell coefficient for this
packet is `10`, not `7`.

## 2. Exact mathematical object

Index the subgroup by

```text
x_i = 235^i in F_241,       0 <= i < 20.
```

The domain values in index order are

```text
[1,235,36,25,91,177,143,106,87,201,
 240,6,205,216,150,64,98,135,154,40].
```

For a ten-subset `S`, use the first two elementary symmetric coordinates

```text
Phi_2(S)=(e_1(S),e_2(S)) in F_241^2.
```

The field is the prefix field and the shell denominator is literally

```text
Q=|F_241|^2=241^2.
```

There is no extension field, line-field substitution, or list denominator in
this packet.

The support-level dihedral proxy is executable. Rotation by `s` is
multiplication by `235^s`; reflection about `s` is multiplication by `235^s`
followed by inversion. A support is retained exactly when no nonidentity
rotation and no reflection fixes it. This is stronger than deleting only
periodic supports.

The raw target fibre is

```text
 0  {0,1,2,3,4,6,7,9,15,18}
 1  {0,1,2,4,6,7,12,15,17,19}
 2  {0,1,2,5,7,10,12,15,16,17}       deleted: reflection 17
 3  {0,1,3,4,6,8,13,15,18,19}
 4  {0,1,3,5,8,10,13,15,16,18}
 5  {0,1,3,6,7,8,12,14,15,19}
 6  {0,1,4,5,9,10,14,15,16,19}
 7  {0,1,4,7,8,9,11,17,18,19}
 8  {0,2,3,4,5,6,12,13,15,16}
 9  {0,2,4,5,7,9,11,12,16,17}
10  {0,3,4,5,8,9,11,13,16,18}
11  {0,3,5,7,8,9,11,12,14,16}
12  {0,4,5,8,11,12,13,16,17,19}
13  {1,2,3,7,8,12,13,16,17,18}
14  {1,2,4,7,9,12,14,16,17,19}
15  {1,3,4,8,9,13,14,16,18,19}       deleted: reflection 17
16  {2,5,6,10,11,13,14,17,18,19}     anchor A.
```

After deleting rows `2` and `15`, the remaining fifteen supports have empty
intersection. The explicit Lean module checks all support shapes, the common
prefix, the subgroup generator, every dihedral stabilizer, the exact residual
filter, the empty common cores, the rooted shell degree, and (1).

## 3. Why this is a real route cut

The reduction in `m31_q_rooted_shell_envelope.md` remains correct:

```text
(3+7) on the actual first-match residual
    ==> the binding M31 list prefix fibre is below B*.
```

What fails is the tempting stronger claim that `(3+7)` follows from prefix
rigidity plus obvious support-level quotient/dihedral and planted-core removal.
The present packet satisfies those hypotheses and violates `(3+7)`.

This matters because the deployed list row permits intercept `3` with only
`80,429` units of reserve, while intercept `4` is already too expensive. A
proof cannot repair the route merely by increasing the additive intercept on
all residual shells. It must use information absent from the support-only
packet, for example:

- an actual slope-level C1--C8 first-match owner;
- received-line or explanation descent, rather than support symmetry;
- a rooted phase/cancellation estimate using the semantic deletion mask; or
- a different local inequality whose exceptional charge is paid by named
  owners.

The counterexample is also not a disguised orbit coincidence within the fixed
target: every retained support has trivial dihedral stabilizer, and no
shell-six neighbor is a dihedral image of the anchor. The twenty global
violations obtained by multiplying the packet are expected covariance across
**different** prefix targets, not a quotient inside the fixed target.

## 4. Exhaustive auxiliary census

The standard-library Python replay enumerates all

```text
C(20,10)=184,756
```

supports. It obtains

```text
raw prefix keys                    53,381
dihedral-generic supports         179,600
dihedral-symmetric supports         5,156
generic prefix keys                52,790
planted-core keys removed          45,060
residual prefix keys                7,730
maximum residual fibre                 15
violating anchor/shell cells            20.
```

All twenty violations are one multiplicative orbit of the canonical packet.
No other violation occurs in this exact finite universe. This exhaustive census
is useful replay and falsifier evidence; it is not the Lean proof validator.
The counterexample itself needs only the explicit retained family checked in
Lean.

## 5. Lean correspondence

The source-facing declarations are in
`M31QRootedShell/MultiplicativeCounterexample.lean`:

```text
domain_is_order_twenty_control
raw_catalog_has_common_prefix
residual_is_exact_dihedral_filter
residual_supports_are_dihedral_generic
residual_common_core_empty
anchor_neighbors_not_dihedrally_related
anchor_distance_histogram
rootedDegree_six
three_plus_seven_fails
four_plus_seven_fails
five_plus_seven_holds
localEnvelope_three_seven_fails.
```

The last declaration instantiates the existing generic `LocalEnvelope`
interface, so the route failure is connected directly to the compiler used by
the rooted-shell packet rather than being recorded as unrelated arithmetic.

The Lean module does not enumerate every ten-subset. Its proof claim is the
explicit counterexample family. The Python certificate separately confirms
that the displayed raw catalogue is the complete target fibre and that the
same phenomenon forms exactly one twenty-cell orbit in the full census.

## 6. Proof status and nonclaims

### Proved in Lean after green CI

- `235` has exact order `20` modulo `241`, and the displayed domain is its
  multiplicative subgroup;
- all seventeen displayed supports are duplicate-free ten-subsets with prefix
  `(92,135)`;
- the dihedral filter removes exactly the two displayed reflection-fixed
  supports and retains fifteen supports;
- every retained support has trivial dihedral stabilizer;
- the retained family and the violating rooted star have empty common core;
- no violating neighbor lies in the dihedral orbit of the anchor;
- the anchor has distance histogram `1,10,3` on shells `5,6,7`;
- `(3+7)` and `(4+7)` fail, while `(5+7)` holds;
- the existing `LocalEnvelope` predicate is false at `(Q,b,c)=(241^2,3,7)`.

### Auxiliary exact replay

- completeness of the seventeen-member raw target fibre;
- completeness of the fifteen-member support-level residual;
- the all-support census and exact twenty-cell multiplicative orbit;
- certificate and digest regeneration with hostile tamper rejection.

### Not claimed

This packet does **not** claim that the fifteen supports survive the actual
slope-level C1--C8 first-match atlas. Support symmetry is only a structural
trigger in the project grammar; a paid owner also requires received-line and
explanation descent plus a distinct-slope budget. Accordingly the packet does
not refute:

- the deployed Mersenne-31 exact residual;
- row-sharp Q;
- a semantic violation-to-owner version of `(3+7)`;
- an adjacent safe list or MCA row;
- the complete first-match or exact completion ledger.

Its exact verdict is

```text
COUNTEREXAMPLE_TO_SUPPORT_ONLY_3PLUS7.
```

## 7. Next mathematical target

The next theorem must include semantic ownership in its statement. A viable
form is

```text
p^w max(d_e(A)-3,0) <= 7 H_e
    OR
one of the excess neighbors has a certified earlier slope owner,
```

where “owner” carries the received line, explanation state, first-match
projector, natural profile scale, and exact slope budget. The present orbit is a
mandatory regression: any proposed owner theorem should classify it, while any
support-only proof must reject it.

## 8. Replay

```text
python3 experimental/scripts/verify_m31_q_three_plus_seven_multiplicative_counterexample.py --write
python3 experimental/scripts/verify_m31_q_three_plus_seven_multiplicative_counterexample.py --check
python3 experimental/scripts/verify_m31_q_three_plus_seven_multiplicative_counterexample.py --tamper-selftest
python3 -O experimental/scripts/verify_m31_q_three_plus_seven_multiplicative_counterexample.py --check --tamper-selftest
```

Expected summary:

```text
RESULT: PASS
target= [92, 135] raw= 17 residual= 15
shell= 6 degree= 10 b3_lhs= 406567 rhs= 308700 margin= 97867
global_violations= 20 single_orbit= True
tamper-selftest: PASS (12/12)
```
