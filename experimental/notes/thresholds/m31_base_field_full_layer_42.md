# M31 base-field full-layer multiplicity 42

## Status

**PROVED LOCAL / CONDITIONAL / BASE FIELD ONLY / INDEPENDENT HOSTILE AUDIT
`ACCEPT_NARROWED` / ZERO PAYMENT / OFFICIAL SCORE `0/2`.**

This note strengthens one finite counting step in the Mersenne-31 list
stress test.  It does not prove the deployed quartic-field list bound.

At the current source base
`main@32a41660e3088eeeb15a16645330856794302ff0`, the only change after the
audited Grande Finale v4 snapshot
`a3017697ad1594521d2779fe1d83bccd45d4c06e` is the unrelated promotion of
Paving v9.2 to the repository root and its documentation.  The mathematical
input used below is the full-packet exact-support theorem in open PR #1023 at
head `895d15ee9a67fee0fff9c3098306d5f93ca3bcbd`.

The nonduplicate delta relative to PR #1023 is the exact layer-cake
strengthening

```text
M >= 42,
j_* >= 606936,
max-41 total upper = 16590107,
gap to the strict contradiction mass = 187109.
```

The resulting base-field Forney averages are

```text
mu_1 <= 22842,
mu_1 + mu_2 <= 45684 < 67447,
at least M - 15 locator rows have degree below D_0.
```

The Padé coupling, common-core construction, source-row annihilation,
collision dictionary, and rank-two saturation used by the larger repaired
packet overlap PRs #1023, #1028, #1029, #1031, and #1037 and are not
republished here.

## Theorem

Let

```text
p = 2^31 - 1,
n = 2^21,
K = 2^20,
a = 1116023,
R = n - a = 981129,
B* = floor(p^4 / 2^100) = 16777215,
L = B* + 1 = 16777216.
```

Work over `F = F_p`.  Let `D` be the archived `n`-point evaluation domain,
let `C = RS_F(D,K)`, and let `y` not lie in `C`.  For `|E| <= R`, write
`z_y(E) = 1` when there is a codeword whose exact error support relative to
`y` is `E`, and put

```text
M_j = sum_{|E|=j} z_y(E).
```

Assume the strict integer hypothesis

```text
sum_{|E|<=R} z_y(E) > B*.
```

Let `j_*` be the least maximizer of `M_j` over `K/2 < j <= R`, using the
lexicographic incidence-vector ordering inherited from PR #1023 only to name
the members of the full layer.  Put `M = M_{j_*}`.  Then

```text
M >= 42,
j_* >= 606936.
```

If `mu_1 <= ... <= mu_(M-1)` are the locator-syzygy minimal indices from PR
#1023 and `D_0 = K-j_*`, then

```text
mu_1 <= 22842,
mu_1 + mu_2 <= 45684 < D_0,
#{r : mu_r < D_0} >= M-15.
```

No selector `J(y)` or normalized coefficient relation is claimed in this
note.  In particular, no permutation-independent choice or residual
field-unit normalization is needed for the theorem stated here.

## Proof

Take `m` distinct exact supports `E_1,...,E_m` in one weight-`j` layer.
Let their common core have size `c`, put `V_i = E_i \ C`, and let `t_x` be
the number of variable supports containing coordinate `x`.

Two distinct explanations differ by a nonzero Reed--Solomon codeword.  Since
`n=2K`, the minimum distance is `K+1`, so

```text
|E_i union E_k| >= K+1,
|V_i intersect V_k| <= 2j-c-K-1.
```

For integers `u,T >= 0`, define

```text
Phi(u,T) = min sum_x binom(s_x,2),  subject to sum_x s_x=T.
```

Convexity makes the minimizing occupancies differ by at most one.  If
`T = q u + r`, `0 <= r < u`, then

```text
Phi(u,T) = u*binom(q,2) + r*q.
```

Summing pairwise intersections and then restoring the `c` common
coordinates gives the core-free necessary condition

```text
Phi(n,mj) <= binom(m,2) * (2j-K-1).                 (1)
```

Put

```text
Delta_m(j) = binom(m,2)*(2j-K-1) - Phi(n,mj).
```

For `j<n/2`, `Delta_m(j)` is nondecreasing.  Increasing `j` adds `m`
balanced incidence units, each costing at most `m-1`, while the first term
increases by exactly `m(m-1)`.

For `1 <= m <= 42`, let `t_m` be the first integer `j>K/2` with
`Delta_m(j) >= 0`.  Exact integer evaluation gives

```text
m= 1.. 7: 524289 524289 524289 524289 559242 567980 569228
m= 8..14: 576718 582543 584208 585570 589825 591506 591698
m=15..21: 594194 595783 596250 597107 598581 599187 599187
m=22..28: 600549 601223 601390 602007 602708 602983 603130
m=29..35: 603836 604181 604239 604720 605108 605245 605429
m=36..42: 605845 606039 606049 606443 606677 606747 606936
```

At the last boundary,

```text
Delta_42(606935) = -111,
Delta_42(606936) = 1107.
```

For `j <= K/2`, a layer has at most one exact support; otherwise two
explanations would differ in a nonzero codeword supported on at most `K`
coordinates.  The zero layer is absent because `y` is not a codeword.  Thus
the low layers contribute at most `K/2 = 524288`.

If every high layer had multiplicity at most 41, the layer-cake identity and
(1) would give

```text
sum_{K/2<j<=R} M_j
  <= sum_{m=1}^{41} (R-t_m+1)
  = 16065819.
```

Including low layers gives

```text
sum_{|E|<=R} z_y(E) <= 16590107 < 16777216 = L,
```

contradicting the strict hypothesis.  Hence some high layer has at least 42
members.  The maximizing layer has `M>=42`, and applying (1) to any 42 of
its members gives `j_*>=606936`.

PR #1023 supplies

```text
sum_{r=1}^{M-2} mu_r <= 2R-K-1 = 913681.
```

Since `M-2>=40`, averaging the smallest ordered entries gives

```text
mu_1 <= floor(913681/40) = 22842,
mu_1+mu_2 <= floor(2*913681/40) = 45684.
```

Also `D_0 >= K-R = 67447`.  At most
`floor(913681/67447)=13` of the first `M-2` indices can reach `D_0`, and
PR #1023 contributes at most one exceptional largest index.  Therefore at
least `M-15` indices are strictly below `D_0`.

## Replay

```text
python3 experimental/scripts/verify_m31_base_field_full_layer_42.py --check \
  --expected experimental/data/certificates/m31-base-field-full-layer-42/expected.txt
python3 -O experimental/scripts/verify_m31_base_field_full_layer_42.py --check \
  --expected experimental/data/certificates/m31-base-field-full-layer-42/expected.txt
python3 experimental/scripts/verify_m31_base_field_full_layer_42.py --tamper-selftest
python3 -O experimental/scripts/verify_m31_base_field_full_layer_42.py --tamper-selftest
```

The verifier uses exact integers only.  Its tamper suite changes actual
arithmetic inputs and branches: the MDS `K+1` threshold, the strict-mass
budget, the high-layer endpoint, the low-layer count, the radius, the
balanced-incidence formula, and the claimed multiplicity.

## Audit and nonclaims

The independent hostile-proof audit returned `ACCEPT_NARROWED`.

- audit conversation: `6a5fdcf5-8450-83ec-8f4f-6b218b211537`;
- audit packet SHA-256:
  `9cc8da64c349c547259b63d126a0fa129dfc276fdb9936fcd6355259418d82d3`;
- frozen audit public text SHA-256:
  `e2afcb299230c39dc98b6b1f8aeaad734584fc8a9a3805bfea0930680ac9abc9`;
- repaired claimant bundle SHA-256:
  `968c6c2139e4eab203c039e5ce03bbc99111ded81282fa4b94c60f164b62a815`.

This theorem does not claim that the strict hypothesis is satisfiable.  It
does not prove an XOR-zero quartet, a collision-bearing circuit, a
first-match owner, a common-core add-back, a quartic-field transfer, a
whole-ball upper bound, the adjacent endpoint, ledger movement, payment, or
an official theorem.  The archived Grande Finale v3 `135168/33792/879753`
signature is omitted because it is not part of the current v4 theorem.

