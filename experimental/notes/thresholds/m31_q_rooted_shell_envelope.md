# Mersenne-31 row-sharp Q: a rooted shell envelope with exact `3+7` closure

**Status:** `PROVED REDUCTION / EXACT DEPLOYED ARITHMETIC / COUNTEREXAMPLE TO 2+7 / EXHAUSTIVE TOY EVIDENCE / OPEN DEPLOYED INPUT`
**Track:** `prob:row-sharp-q`, binding Mersenne-31 list row.
**Authoritative validation:** stdlib-only Lean package `experimental/lean/m31_q_rooted_shell/`, built only by the fork draft-PR GitHub Action.
**Auxiliary replay:** `experimental/scripts/verify_m31_q_rooted_shell_envelope.py` (exploration and packet regeneration; not proof validation).
**Certificate:** `experimental/data/certificates/m31-q-rooted-shell-envelope/m31_q_rooted_shell_envelope.json`

## 0. Result

Let `F` be any first-match-pruned family inside one depth-`w` locator-prefix
fiber of `m`-subsets of an `n`-point domain. For an anchor `A in F`, write

```text
d(A,B) = m - |A intersect B|,
d_e(A) = #{B in F \ {A} : d(A,B)=e},
H_e    = C(m,e) C(n-m,e),
Q      = p^w.
```

Prefix rigidity gives `d(A,B) >= w+1` for distinct members. Put

```text
u = min(m,n-m),        R = u-w.
```

This packet proves the general rooted-shell summation lemma

```text
Q max(d_e(A)-b,0) <= c H_e     for every A in F and w<e<=u

        ==>   |F| <= 1 + bR + floor(c C(n,m)/Q).                 (RS)
```

Its binding deployed specialization is the integer pair

```text
b=3, c=7.                                                     (3+7)
```

At the Mersenne-31 list row this gives the exact implication

```text
p^w max(d_e(A)-3,0) <= 7 C(m,e)C(n-m,e) for every A,e

        ==> |F| <= 16,696,786
                <= 16,777,215 = B*,
```

leaving an integer reserve of

```text
B* - 16,696,786 = 80,429.
```

The companion Mersenne-31 MCA row gives

```text
|F| <= 15,009,938 <= B*,
reserve = 1,767,277.
```

Thus `(3+7)` is a new, explicit theorem-facing sufficient input for the binding
row-sharp Q atom. It is a **local ambient-shell-normalized degree theorem**,
not another global Fourier `L^1` certificate and not a two-shell assumption.

The packet also shows that the neighboring stronger statement `(2+7)` is
false on a faithful Chebyshev/twin-coset toy after quotient and planted-core
pruning. On the shipped toy,

```text
p=127, n=16, m=8, w=1,
H_7 = C(8,7)^2 = 64,
d_7(A)=6,

p(d_7(A)-2) = 508 > 448 = 7H_7,
p(d_7(A)-3) = 381 <= 448 = 7H_7.
```

All seven exhaustive toy rows satisfy `(3+7)`. Therefore, with coefficient
`7`, the additive intercept `3` is exactly the first integer value that both
survives the faithful counterexample and still closes the deployed binding
budget: intercept `4` is too expensive at M31-list.

This does **not** prove the deployed shell hypothesis. The row-sharp Q atom,
the adjacent safe row, and the full first-match ledger remain open.

### Lean validation boundary

The stdlib-only Lean package kernel-checks the generic rooted-shell compiler,
the deployed list/MCA arithmetic and reserves from the pinned scaled-floor
packet integers, and the complete finite `2+7`/`3+7` control witness. It has no
Mathlib dependency. The gigantic binomial quotient values themselves remain
explicit packet inputs; no green build should be described as proving their
derivation or the open deployed local shell hypothesis.

Agent sessions do not build Lean locally. The authoritative build is the
GitHub Actions run triggered by a draft PR against `holmbuar/rs-mca:main` that
contains this complete research packet.

---

## 1. Board position and exact object

`experimental/grande_finale.tex`, `def:q-row-atom` and
`prop:q-exact-target`, leave the first-match-pruned primitive prefix family

```text
P_Q(z) subseteq Fib_w(z)
```

as the finite max-fiber input. The binding row is

```text
p       = 2^31-1 = 2,147,483,647,
n       = 2^21   = 2,097,152,
K       = 2^20,
a_+     = 1,116,023,
w       = a_+-K = 67,447,
m       = n-a_+ = 981,129,
B*      = 2^24-1 = 16,777,215,
ceil(C(n,m)/p^w) = 1,993,678.
```

The complement size `m=n-a_+` is used here because the Johnson exchange
shells are symmetric under `m <-> n-m`; `C(n,m)=C(n,a_+)` and the prefix depth
is unchanged.

The support-side pruning matters. The signed-`e_m` masked-residual audit
correctly separates the actual first-match residual coefficient

```text
E_Q(t) = sum_{M in P_Q} psi(t . Phi_w(M))
```

from the raw unpruned elementary-symmetric coefficient. This packet therefore
quantifies directly over the actual residual family `F=P_Q(z)`. It does not
replace first-match support deletion by a frequency restriction.

For each anchor `A in F`, the shell degree `d_e(A)` is the exact rooted count
of residual supports at exchange distance `e`. It retains the anchor and the
prefix target. It is not an unrooted pair total, a support census before
first match, an explanation-state count, or an MCA slope count.

---

## 2. General rooted-shell envelope

### Theorem

Let `Omega` be the set of all `m`-subsets of an `n`-set, and let
`F subseteq Omega`. Assume every two distinct members of `F` have exchange
distance greater than `w`. Set

```text
Q = p^w,
u = min(m,n-m),
R = u-w,
H_e = C(m,e)C(n-m,e).
```

Fix nonnegative integers `b,c`. If

```text
Q max(d_e(A)-b,0) <= c H_e                         (E_b,c)
```

for every `A in F` and every `w<e<=u`, then

```text
|F| <= 1 + bR + floor(c C(n,m)/Q).                 (RS)
```

### Proof

Fix `A in F`. Prefix rigidity removes all distances `1,...,w`, so

```text
|F|-1 = sum_{e=w+1}^u d_e(A).
```

For every term,

```text
d_e(A) <= b + max(d_e(A)-b,0)
       <= b + c H_e/Q.
```

Summing over the `R=u-w` admissible shells gives

```text
|F|-1 <= bR + (c/Q) sum_{e=w+1}^u H_e.
```

The Johnson shell identity around one anchor is

```text
sum_{e=0}^u H_e = C(n,m),
```

so the displayed tail is at most `C(n,m)`. Since `|F|` and `bR` are
integers,

```text
|F| <= 1+bR+floor(c C(n,m)/Q).
```

This proves `(RS)`.

### Contrapositive / falsifier

If a prefix fiber has size strictly larger than the right side of `(RS)`, then
**every anchor** `A` has at least one admissible shell satisfying

```text
Q max(d_e(A)-b,0) > c H_e.                         (V_b,c)
```

For the binding packet, a counterexample to the proposed route is therefore a
first-match residual fiber above budget together with the forced rooted
`(3+7)` shell violation from each anchor. This is substantially more typed
than the bare statement “a large fiber contains many equal-distance pairs.”

---

## 3. Exact deployed specialization

### 3.1 Mersenne-31 list — binding row

Use

```text
n=2,097,152, m=981,129, w=67,447, Q=p^w.
R=m-w=913,682.
```

The auxiliary replay recomputes the `2,090,878`-bit binomial `C(n,m)` and obtains

```text
floor(C(n,m)/Q) = 1,993,677,
ceil (C(n,m)/Q) = 1,993,678.
```

For `(b,c)=(3,7)`, exact integer division gives

```text
1 + 3R + floor(7 C(n,m)/Q)
  = 1 + 2,741,046 + 13,955,739
  = 16,696,786.
```

Hence `(3+7)` fits under `B*=16,777,215` by `80,429`.

The exact real coefficient that would consume the whole budget after an
additive intercept `b` is

```text
kappa_b = (B*-1-bR) Q / C(n,m).
```

The calibrated values are

| `b` | `kappa_b` | Does integer coefficient `7` fit? |
|---:|---:|:---:|
| 0 | 8.415211213 | yes |
| 1 | 7.956921355 | yes |
| 2 | 7.498631498 | yes, but false on the faithful toy below |
| **3** | **7.040341641** | **yes** |
| 4 | 6.582051783 | no |
| 18 | 0.165993780 | no |

Thus `3` is the unique integer intercept immediately between the faithful
`2+7` failure and the deployed `4+7` budget failure.

### 3.2 Mersenne-31 MCA companion

For the MCA complement size `m=981,128`, the same prefix depth gives

```text
R=913,681,
floor(C(n,m)/Q)=1,752,699,
ceil (C(n,m)/Q)=1,752,700,
```

and

```text
1+3R+floor(7C(n,m)/Q)=15,009,938,
B*-bound=1,767,277.
```

No MCA slope projection is claimed: this is the companion prefix-fiber atom
calibration only.

---

## 4. Why a bare same-shell star is not the right target

A family of size `B*+1` has `B*` neighbors from every anchor. Since there are
`R=913,682` admissible shells, pigeonholing alone gives only

```text
max_e d_e(A) >= ceil(B*/R) = 19.
```

That absolute star is far below the ambient random shell scale. The exact
Johnson shell sizes are unimodal because

```text
H_{e+1}/H_e = ((m-e)(n-m-e))/(e+1)^2.
```

The peak is therefore

```text
e_peak = floor((m(n-m)-1)/(n+2))+1 = 522,119.
```

At that shell the auxiliary replay obtains

```text
floor(H_peak/Q)=2,206,
ceil (H_peak/Q)=2,207.
```

So a 19-neighbor shell is more than two orders of magnitude below even the
ambient average peak. It is not a heavy-shell certificate. The normalized
`(3+7)` ceiling at the peak is instead

```text
d_peak(A) <= 3 + floor(7H_peak/Q) = 15,445.
```

This explains the normalization in `(E_b,c)`: the theorem asks for a constant
factor over each shell's own ambient mass, with a small additive allowance for
very thin shells. It does not ask for an absolute uniform degree bound.

---

## 5. Faithful Chebyshev counterexample to `2+7`

The auxiliary replay builds `F_{127^2}=F_127(i)`, its cyclic norm-one group of
order `128`, a subgroup `H` of order `16`, and the x-coordinate image of

```text
g^3 H union g^-3 H.
```

The x-projection is checked to be exactly two-to-one and its image is the
negation-stable, nonmultiplicative Chebyshev/twin-coset domain

```text
D = [5,39,89,42,22,125,9,53,122,88,38,85,105,2,118,74].
```

Enumerate every 8-subset, key it by its first elementary symmetric coefficient,
remove complete `T_2` fibers, and then remove a prefix key if all remaining
supports share a planted point. In the residual prefix key

```text
z=[22]
```

there are 88 supports. The anchor

```text
indices = [0,1,3,4,7,8,13,14],
values  = [5,39,42,22,53,122,2,118]
```

has six residual neighbors at exchange distance seven. The six neighbor index
sets, and their canonical SHA-256 digest, are frozen in the JSON certificate:

```text
c674ee4d16ded9401adea1c9141b6ebf22fd6cb06a39a0c9dfb676811f41b962.
```

Since `H_7=C(8,7)^2=64`,

```text
127(6-2)=508 > 7*64=448,
127(6-3)=381 <=448.
```

Therefore every `b<=2` version with coefficient `7` is false, while the
`b=3` inequality survives this witness. The object is a genuine fixed-prefix,
post-quotient, no-common-planted-core shell. It is not a target-erasure graph,
a sparse-average artifact, or a raw quotient cell.

This remains a toy counterexample to a proposed proof route, not a deployed
counterexample and not a new obstruction floor.

---

## 6. Exhaustive toy census

The auxiliary replay enumerates all supports, all residual prefix fibers, all
anchors, and all rooted shell degrees on six faithful Chebyshev rows and one
multiplicative control. No sampling is used.

The table records the largest coefficient required in

```text
p^w max(d_e(A)-b,0) <= coefficient * H_e.
```

| row | max residual fiber | required at `b=2` | required at `b=3` |
|---|---:|---:|---:|
| Chebyshev `p=127,n=16,m=8,w=1,offset=1` | 120 | 3.968750 | 2.753827 |
| Chebyshev `p=127,n=16,m=9,w=1,offset=1` | 112 | 3.527778 | 2.687831 |
| Chebyshev `p=127,n=16,m=8,w=1,offset=2` | 135 | 5.953125 | 3.968750 |
| Chebyshev `p=127,n=16,m=9,w=1,offset=2` | 119 | 3.527778 | 3.359788 |
| Chebyshev `p=127,n=16,m=8,w=1,offset=3` | 125 | **7.937500** | **5.953125** |
| Chebyshev `p=127,n=16,m=9,w=1,offset=3` | 117 | 3.527778 | 3.359788 |
| multiplicative `p=101,n=20,m=12,w=2` | 40 | 4.830019 | 3.532814 |

Every `b=3` coefficient is strictly below `7`. The worst faithful value is the
counterexample row, where it is exactly `381/64=5.953125`.

These rows support the scale and falsify the adjacent stronger conjecture.
They are not evidence sufficient to promote `(3+7)` at deployment.

---

## 7. Relation to existing shell and Fourier lanes

### Multi-anchor shell SOS

`cap25_v13_m31_multi_anchor_shell_sos.md` proves the complete rooted shell-pair
PSD matrix and several global tail inequalities, then leaves aggregation to a
max-fiber bound open. This packet uses the same rooted degrees `d_e(A)` but
adds a different terminal interface:

```text
pointwise ambient-shell excess <= 3 + 7 H_e/p^w.
```

The SOS identities may be one route to prove or refute that interface; they are
not reproved here.

### Two-shell Delsarte / nullity / SDP lane

The two-shell Delsarte packets retain millions of LP-consistent distance pairs,
and the modular nullity floor is pair-uniform on the unrestricted class. The
present reduction does not assume two shells and does not claim an LP
improvement. It identifies a pointwise local distribution target that would
pay arbitrary shell support in one summation.

### Signed-`e_m` and masked residual lane

A raw Fourier `L^1` inequality is only a sufficient certificate and can be
strictly stronger than the max-fiber target. The present theorem is entirely
support-side and applies to the literal first-match-pruned family. A future
Fourier argument is useful only if it proves `(3+7)` for that masked family or
routes any violation to a named earlier owner.

### Binding-row calibration

The exact small-row calibration measured primitive max/mean at most `1.221` on
heavy rows, far below the deployed ratio `8.4152`. The current packet neither
uses nor extrapolates that fit. Its deployed implication is exact, and its toy
role is limited to route falsification and regression.

---

## 8. Next mathematical target

The PR-worthy theorem target exposed by this packet is:

> **M31 rooted shell envelope.** For every actual first-match-pruned primitive
> Mersenne-31 list prefix family `P_Q(z)`, every anchor `A`, and every
> `w<e<=m`, prove
>
> ```text
> p^w max(d_e(A)-3,0) <= 7 C(m,e)C(n-m,e),
> ```
>
> or show that a violation routes to a named paid cell.

Useful attacks should preserve the anchor and prefix target. Candidate tools
include:

1. the existing shell-pair PSD matrix with a pointwise localization or a
   many-anchor averaging argument;
2. a masked character-phase inequality for the rooted distance enumerator;
3. a Johnson-scheme SDP with the prefix-nullity module retained, rather than an
   unlabelled Delsarte distribution;
4. an inverse theorem: a shell above `3+7H_e/Q` forces a common core, quotient
   fold, extension descent, rank drop, or balanced-core owner.

The exact falsifier is equally clear: construct one legal first-match residual
fiber and one anchor/shell violating `(3+7)`. Such a result would invalidate
this closure route without needing to decide the full Q atom.

---

## 9. Validation and nonclaims

The authoritative validation is the PR-triggered GitHub Actions build of
`experimental/lean/m31_q_rooted_shell/`. Agent sessions must not build Lean
locally. The draft fork PR must include the complete research packet, not a
Lean-only patch.

The auxiliary Python replay may be run by humans for packet regeneration and
hostile data checks:

```text
python3 experimental/scripts/verify_m31_q_rooted_shell_envelope.py
python3 experimental/scripts/verify_m31_q_rooted_shell_envelope.py --tamper-selftest
```

That script recomputes the giant binomial, both adjacent rows, the peak-shell
normalization, all seven exhaustive toy rows, the frozen counterexample digest,
and corruption rejections. Those computed checks are supporting evidence;
they are not a substitute for the Lean build or a proof of the open deployed
local shell premise.

**Nonclaims.** This packet does not prove:

- the deployed `(3+7)` hypothesis;
- `max_z |P_Q(z)|<=B*`;
- the Mersenne-31 adjacent safe list or MCA row;
- an MCA distinct-slope bound;
- exhaustive first-match coverage or the summed completion ledger;
- a Fourier participation-ratio theorem;
- a two-shell realizability/SDP theorem;
- a new unsafe construction or obstruction floor.

The result is a proved reduction with exact row closure arithmetic, a sharp
neighboring-route counterexample, and a reproducible finite regression suite.
