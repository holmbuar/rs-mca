# Direct Sidon signed-root and diagonal-pair emissions

## Status

This note packages the narrow source theorem in R28 Role 09. It proves two
support-emission statements and records one exact asymptotic cutoff comparison.
It does not package the worker's stronger pincer, interpolation, or weighted
occupied-emission claims.

The all-characteristic and odd-characteristic statements are deliberately
separate. The signed-root layer is valid for every finite abelian syndrome
group. The root-free ternary layer requires injective doubling on the realized
syndrome set, as it has for vector-space codomains of odd characteristic.

The fail-closed statement pins are:

```text
SIGNED_ROOT_CLAIM: For every finite abelian syndrome group, sum_s f_s/Delta_s <= A_pm(N,m) by canonical signed-root emission.
ODD_DIAGONAL_CLAIM: If doubling is injective on S, in particular for a vector-space codomain of odd characteristic, sum_s f_s/Delta_s <= A_2(N,m) by ternary diagonal-pair emission.
CUTOFF_GAIN_CLAIM: On the literal half-density R=1 family, the exact cutoff improvement is 0.156870036510644 nats = 0.226315623737977 bits.
FINITE_LEDGER_PIN: Pending PR #872 has paid subtotal 274854110496187589 = T-3; this packet adds no finite charge.
NONCLAIM_PIN: This packet does not close hard input 2, any recurrence parent, Grand MCA, Grand List, or the official score.
WOE_SCOPE_PIN: The ternary diagonal-pair WOE is odd-characteristic only; the all-characteristic signed-root WOE analogue is a separate unproved target using A_pm.
```

## Source interface

Let `T` be a set of size `N`, let

```text
Omega_(T,m) = {x in {0,1}^T : |x|=m},
Phi : Z^T -> G
```

be a group homomorphism into a finite abelian group, and put
`S=Phi(Omega_(T,m))`. Let `Omega^o` be an arbitrary first-match residual
subset. For `s in S`, define

```text
F_s = Omega^o intersect Phi^(-1)(s),
f_s = |F_s|,
E_s = |{(a,b,c,d) in F_s^4 : a-b=c-d in Z^T}|,
Delta_s = E_s/f_s^3
```

when `f_s>0`. Empty fibres contribute zero. All additive energy and emitted
vectors live in the torsion-free incidence group `Z^T`; the syndrome map is
applied only after those integer-vector identities are formed.

Define the exact coefficient layers

```text
A_2(N,m)  = [z^(2m)]   (1+z+z^2)^N,
A_pm(N,m) = [z^(N+m)] (1+z+z^2+z^3)^N.
```

## Energy-to-support inequality

For one nonempty fibre `F=F_s`, let

```text
r(u) = |{(a,b) in F^2 : a+b=u}|.
```

Then `sum_u r(u)=f^2` and

```text
sum_u r(u)^2 = E(F).
```

The latter equality follows from the bijection between
`a+b=c+d` and `a-c=d-b`. Cauchy--Schwarz therefore gives

```text
f^4 <= |F+F| E(F),
f/Delta(F) = f^4/E(F) <= |F+F|.                  (1)
```

This is the only energy input in the two emission theorems.

## Canonical signed-root emission

Fix the source order on `T` and choose the lexicographically least
`r_s in F_s` for every nonempty fibre. Put

```text
E_s^pm = F_s + F_s - r_s.
```

Translation preserves cardinality, so (1) gives

```text
f_s/Delta_s <= |E_s^pm|.
```

Every emitted vector `u=a+b-r_s` satisfies

```text
Phi(u)=s+s-s=s,
u_t in {-1,0,1,2},
sum_t u_t=m.
```

The syndrome tag makes the sets `E_s^pm` pairwise disjoint. Adding one to
every coordinate embeds their union in the coefficient layer counted by
`A_pm(N,m)`. Hence, in every characteristic,

```text
sum_s f_s/Delta_s <= sum_s |E_s^pm| <= A_pm(N,m). (S1)
```

The canonical root is an ownership choice, not a balanced selector.

## Odd-characteristic diagonal-pair emission

Assume multiplication by two is injective on `S`. This holds in particular
when the syndrome codomain is a vector space over a field of odd
characteristic. Put

```text
E_s^(2) = F_s + F_s.
```

Every emitted vector has coordinates in `{0,1,2}`, coordinate sum `2m`, and
syndrome tag `2s`. Injective doubling makes these tags distinct, so the
emitted sets are pairwise disjoint. Equation (1) now gives

```text
sum_s f_s/Delta_s <= sum_s |E_s^(2)| <= A_2(N,m). (S2)
```

This ternary statement is not asserted in characteristic two. For example,
with `N=4`, `m=2`, syndrome weights `(0,0,1,1)` modulo two, the fibres

```text
{1100,0011} and {1010,0101}
```

have different syndromes but both diagonal-pair emissions contain `1111`.
The signed-root theorem remains valid because its tag is `s`, not `2s`.

## Exact cutoff comparison

Consider the literal odd-prime source family

```text
T=F_p, N=p, m=(p-1)/2, R=1,
Phi(x)=sum_(t in F_p) x_t t.
```

Translation by `c` changes the syndrome by `mc`; because `m` is nonzero
modulo `p`, the realized image has exactly `L=p` syndromes. Thus `log L=o(N)`.
At half density, the diagonal-pair coefficient has exponential rate `ln 3`
while `M=binom(N,m)` has rate `ln 2`. The new diagonal-pair cutoff is

```text
kappa_pair = ln(3)-ln(2) = ln(3/2)
           = 0.405465108108164 nats
           = 0.584962500721156 bits.
```

The repaired fixed-orbit cutoff at PR #860 head
`fb54c47553d3948f3dc6e64b0a292747459fc482` is

```text
kappa_860 = 2 ln(2) - (3/4) ln(3)
          = 0.562335144618808 nats
          = 0.811278124459133 bits.
```

Therefore the exact strict cutoff improvement is

```text
kappa_860-kappa_pair = 3 ln(2) - (7/4) ln(3)
                     = 0.156870036510644 nats
                     = 0.226315623737977 bits.
```

This is a fixed-width improvement of one asymptotic alternative on a literal
source family. It is not payment for every fixed positive Sidon exponent.

## Novelty relative to PR #870

Pending PR #870 retires an inconsistent direct-Sidon toy falsifier and
reconstructs the quantitative interface of one fixed-weight Boolean source.
It does not prove either emission inequality in this note. Conversely, the
present packet does not revive that falsifier or contradict PR #870: it proves
the all-characteristic signed-root identity and the odd-characteristic
diagonal-pair identity for source-realized fibres, then records the resulting
cutoff comparison. The two claims are therefore complementary and no finite
ledger charge is imported from either one.

## Current ledger and nonimpact

The worker return predated pending PR #872 and therefore repeated the stale
rank-16 allowance from PR #861. The current pending finite ledger is PR #872
at head `37e08b4feb60714a6c9955ae408edf1742f0fc2b`:

```text
target T:                  274854110496187592
pending paid subtotal:    274854110496187589 = T-3
formal residual allowance:                    3
```

PR #872 explicitly does not prove that at most three candidates remain
outside its expanded owner. This packet supplies no finite owner and makes no
change to that ledger, any recurrence parent, or the official score.

## Exact remaining wall

For odd-characteristic primitive leaves, a future weighted occupied-emission
estimate may use `c_s=|F_s+F_s|` and the ternary coefficient `A_2`. That WOE
statement is unproved here.

In all characteristics, the separate analogue must instead use
`c_s^pm=|F_s+F_s-r_s|` and `A_pm`. It must not be described as a ternary
diagonal-pair emission. This signed-root WOE analogue is also unproved here.

Neither support bound controls the representation weights strongly enough to
pay every fixed `sigma>0`. Hard input 2 still requires the weighted estimate
using actual shared-prefix locator equations or a new first-match algebraic
owner.

## Reproduction and provenance

Run from the repository root:

```bash
python3 experimental/scripts/verify_direct_sidon_pair_emission.py
python3 -O experimental/scripts/verify_direct_sidon_pair_emission.py
python3 experimental/scripts/verify_direct_sidon_pair_emission.py --tamper-selftest
python3 -m py_compile experimental/scripts/verify_direct_sidon_pair_emission.py
```

The verifier is standard-library only. It exhausts arbitrary residual subsets
for every scalar cyclic syndrome map through `N=4` over moduli `2`, `3`, and
`5`; checks the characteristic-two collision fixture; reconstructs the exact
coefficient layers and literal `R=1` rows; and verifies source, authority, and
statement pins. The semantic self-test mutates every load-bearing distinction
recorded above.

Authority pins are frozen in
`experimental/data/certificates/direct-sidon-pair-emission/source_pins.json`.
The external Role 09 return is provenance, not an independently available
publication artifact; its frozen SHA-256 is
`7afc4c422cfd1bd5f5a66354ae24d5899184b866137f80a65795b24b6c42a86c`.
