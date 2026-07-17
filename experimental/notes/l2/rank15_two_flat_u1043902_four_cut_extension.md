# Rank-15 exact two-flat four-cut extension through u=1,043,902

## Claim and ownership

Fix

```text
n = 2,097,152,   K = 1,048,576,   m = 1,116,047.
```

Let `F` be any field, let `H subset F` contain `n` distinct points, and let
`U:H -> F`.  Put

```text
L_m(U) = {P in F[X] : deg P < K and |{x in H:P(x)=U(x)}| >= m}.
```

Let

```text
calA = P_0 + span_F{V_1,V_2}
```

be an exact affine two-flat.  Its *actual* universal agreement set is

```text
Z = {x in H : P(x)=U(x) for every P in calA},   |Z|=u.
```

Then

```text
|calA intersect L_m(U)| <= 211
```

for every

```text
1,043,902 <= u <= 1,043,957.                         (T)
```

The 41 states `u=1,043,917..1,043,957` are inherited from integrated PR
`#847` (`168e9ba02`).  The theorem delta in this packet is exactly

```text
D_2(u) <= 211,   u=1,043,902..1,043,916,             (Delta)
```

which is 15 new source-child entries.  The current authority base is
`origin/main@7f278167e1e51f968896229ae438ea5a76398f90`.

The exact next relaxed wall is `u=1,043,901`, where the optimized margin is
`+1,707`.  At that wall any literal 212-point source counterexample must have

```text
d = 4,674,   deg G = 0,   r = 0.                     (W)
```

Neither the positive relaxed margin nor (W) constructs a source
counterexample.

## Literal source reduction

Assume for contradiction that `calA intersect L_m(U)` contains 212 distinct
polynomials, and select exactly 212 of them.  Write their affine parameters
as a set `S subset F^2`.  Set

```text
N = n-u,   a = m-u,   lambda = K-1-u.
```

For `x in H\Z`, the coordinate section

```text
calA_x = {P in calA:P(x)=U(x)}
```

is empty or a proper affine line.  The word *actual* in the definition of
`Z` rules out the whole two-flat.  A nonempty section has universal count at
least `u+1`.  The exact rank-one recurrence is

```text
F_{m,1}(z) = max_{z<=v<=K-1}
  min(
    floor((n-v)/(m-v)),
    floor((n-v)(m-K+1) /
          ((m-v)^2-(n-v)(K-1-v)))
  ),                                                     (1)
```

where the second term is infinity when its denominator is nonpositive.  An
integer scan gives

```text
F_{m,1}(1,043,593) = 15,
```

with maximizers exactly `v=1,045,969..1,048,575`.  Thus every proper
coordinate section contains at most 15 selected points throughout the
source interval `u=1,043,592..1,043,957`.

Let `L_Z` be the monic locator of `Z`.  Factor the two directions as

```text
V_1 = L_Z G A,   V_2 = L_Z G B,   gcd(A,B)=1.
```

Put

```text
d = max(deg A,deg B),
r = |{x in H\Z:G(x)=0}|.
```

The polynomial degree ledger gives

```text
d + deg G <= lambda,   deg G >= r,   d <= lambda-r.    (2)
```

Coordinates where `G` vanishes are inactive: if their common value equalled
`U(x)`, they would belong to `Z`.  At every active coordinate, division by
the nonzero value `L_Z(x)G(x)` gives the literal affine parameter line

```text
ell_x = {(s,t) in F^2 : sA(x)+tB(x)=omega_x}.           (3)
```

For each represented projective normal direction `nu`, let `c_nu` be its
number of active coordinates and let `h_nu` be the largest selected-point
occupancy of a parallel line in that direction.  Coprimality makes the
direction polynomial nonzero and of degree at most `d`, so

```text
c_nu <= d,   sum_nu c_nu <= N-r,   1 <= h_nu <= 15.    (4)
```

Double-counting the required residual agreements yields

```text
212a <= sum_nu c_nu h_nu.                              (5)
```

Replacing `d` by `lambda`, padding the total directional weight to `N`, and
allowing

```text
0 <= c_nu <= lambda,   sum_nu c_nu=N                   (6)
```

only enlarge the right side.  It is enough to exclude (5) in this relaxation.

## Inherited partial-linear-space constraints

Choose one maximum-occupancy line for each represented direction and let
`n_h` count chosen lines containing `h` selected points.  A pair of selected
points lies on at most one chosen line, hence

```text
sum_{h=1}^{15} C(h,2)n_h <= C(212,2)=22,366.            (7)
```

For a selected point `p`, let `r_h(p)` count selected `h`-point lines through
`p`.  Distinct such lines use disjoint sets of other selected points, so

```text
sum_{h=2}^{15}(h-1)r_h(p) <= 211.                       (8)
```

The exact mod-13 consequence of (8), and the three finite point-capacity
cuts already integrated through #847, give the global resources

```text
195n_15 + 168n_14 + sum_{h=3}^{13}h(h-2)n_h <= 41,340, (9)

C(n_15,2)+228,960 >=
  1185n_15+910n_14+sum_{h=4}^{13}hC(h-2,2)n_h,          (10)

C(n_14,2)+248,040 >=
  1170n_15+1092n_14+sum_{h=4}^{13}hC(h-2,2)n_h,         (11)

C(n_15,2)+184,440 >=
  975n_15+714n_14+sum_{h=4}^{13}h gamma_h n_h,          (12)
```

where

```text
(gamma_4,...,gamma_15)=(1,3,6,10,15,21,27,33,39,45,51,65).
```

The new verifier independently reconstructs these inherited cuts and the
old `+878` optimizer wall; it does not trust a stored #847 result.

## Four new point-capacity cuts

For a selected point, write `r_h=r_h(p)`.  The four new inequalities are

```text
alpha_i C(r_15,2) + beta_i >= sum_{h=2}^{15} q_{i,h}r_h. (13)
```

All omitted `q` coefficients are zero:

```text
C1: alpha=840, beta=215775
    q5=504, q6=840, q7=1080, q8=1260, q9=2345,
    q10=4347, q11=5985, q12=7350, q13=8505,
    q14=8505, q15=20265.

C2: alpha=1820, beta=909300
    q5=5460, q6=10080, q7=13380, q8=15855, q9=18620,
    q10=26628, q11=33180, q12=38640, q13=43260,
    q14=47880, q15=73360.

C3: alpha=385, beta=172200
    q6=1435, q7=2755, q8=3745, q9=4515, q10=5131,
    q11=6195, q12=7105, q13=7875, q14=8785, q15=14175.

C4: alpha=880, beta=508200
    q6=4620, q7=7920, q8=10395, q9=12320, q10=13992,
    q11=18360, q12=22000, q13=25080, q14=27720,
    q15=40040.
```

These are finite theorems, not fitted assumptions.  Fix `j=r_15`; the
remaining point capacity is `211-14j`.  For each cut let

```text
T_i(0)=0,
T_i(c)=max(T_i(c-1),
           max_{2<=h<=14, h-1<=c}(T_i(c-h+1)+q_{i,h})). (14)
```

The recurrence enumerates every multiset of non-15 lines through the point.
For every `j=0..15`, the verifier checks

```text
q_{i,15}j + T_i(211-14j) <= alpha_i C(j,2)+beta_i.      (15)
```

All four minimum slacks are zero.  Their exact zero-slack `j` sets are

```text
C1: 11,12,13,14,15
C2: 11,12,14,15
C3: 12,13,14,15
C4: 10,11,12,14,15.
```

Two lines of the 15-point class meet in at most one selected point, so

```text
sum_p C(r_15(p),2) <= C(n_15,2).
```

Summing (13) over all 212 points therefore gives the four valid global cuts

```text
alpha_i C(n_15,2)+212 beta_i
  >= sum_{h=2}^{15} h q_{i,h}n_h.                       (16)
```

The constants `212 beta_i` are respectively

```text
45,744,300; 192,771,600; 36,506,400; 107,738,400.
```

## Exact directional optimizer

Write

```text
N=f lambda+s,   0<s<lambda.
```

For fixed line occupancies, (6) assigns weight `lambda` to the `f` largest
occupancies and weight `s` to one residual occupancy `h_*`.  For each
`h_*=1..15`, the optimizer enumerates the full-weight counts `n_15,n_14`.
All remaining full-weight occupancies lie in `[h_*,13]`.

The eight lower-occupancy resources are (7), (9), the resources in
(10)--(12), and C1--C4.  For each resource `Phi`, its forward differences

```text
Phi(h+1)-Phi(h),   1<=h<13,
```

are nonnegative and nondecreasing.  If two lower occupancies differ by at
least two, moving one unit from the larger to the smaller preserves total
occupancy and weakly decreases every resource.  Repeating this exchange
proves that the balanced multiset simultaneously minimizes all eight
resources at fixed occupancy sum.  Therefore complete balanced layers,
followed by one partial layer, give the exact optimum.  The verifier checks
both feasibility and rejection of the one-unit balanced successor.

The replay has exactly

```text
270 cached (f,h_*) states,
6,597,135 enumerated (n_15,n_14) branches,
215,009 rejected one-unit successors.
```

At `u=1,043,916`, the inherited four-resource optimizer is reconstructed as

```text
h_*=6; n_15=181, n_13=27, n_12=18;
capacity=15,292,650; margin=+878.
```

With C1--C4, the optimum becomes

```text
h_*=6; n_15=163, n_14=14, n_13=49;
capacity=15,274,014; margin=-17,758.
```

Scanning the complete interval `u=1,043,592..1,043,957` gives first negative
margin at `u=1,043,902`.  The 15 new margins are

```text
u=1043902    -232       u=1043910  -10606
u=1043903   -2171       u=1043911  -11647
u=1043904   -4110       u=1043912  -12688
u=1043905   -5401       u=1043913  -13729
u=1043906   -6442       u=1043914  -14770
u=1043907   -7483       u=1043915  -16042
u=1043908   -8524       u=1043916  -17758
u=1043909   -9565
```

Every margin is `capacity-212(m-u)`.  This proves (Delta), and together with
integrated #847 proves (T).

## Exact remaining wall

At `u=1,043,901`, the full-degree relaxation has

```text
lambda=4,674,   N=1,053,251=225(4,674)+1,601,
margin=+1,707.                                           (17)
```

This is open.  If instead the literal source degree satisfies `d<=4,673`,
pad the active-coordinate total to `N` and optimize with per-direction
ceiling `4,673`:

```text
N=225(4,673)+1,826,
capacity=15,294,513,
capacity-212(m-u)=-439.                                  (18)
```

Thus a source counterexample must have `d=4,674=lambda`.  Equation (2) then
forces `deg G=0`, hence `r=0`, proving (W).  The remaining object is a
full-degree, gcd-free rational-fiber realizability problem; this packet does
not solve it.

## Recurrence consumer

The verifier replays the literal affine-section recurrence from dimensions
1 through 15, with the integrated `D_2<=217` plateau, the inherited #847
suffix, and then the 15 new entries.  Relative to #847:

```text
dimension 2 changed states: 15 (exactly 1,043,902..1,043,916),
maximum pointwise drop: 5,
dimensions 3..15 changed states: 0.
```

The final rank-15 value remains

```text
283,039,300,733,528,044.
```

Against target `274,854,110,496,187,592`, the exact remaining gap is

```text
8,185,190,237,340,452.
```

Thus this is a real 15-child source payment but no parent payment.

## Verifier

The preserved standard-library verifier is

```text
experimental/scripts/verify_rank15_two_flat_u1043902_four_cut_extension.py
```

It independently checks the rank-one scan, all inherited point cuts, C1--C4,
discrete convexity, the old and new exact optimizers, all claimed margins,
the degree wall, and the rank-15 recurrence.  The certificate packet under

```text
experimental/data/certificates/
  rank15-two-flat-u1043902-four-cut-extension/
```

contains frozen output, semantic tamper tests, and SHA-256 pins.  This is a
fresh independent implementation of the theorem-relevant calculation.

## Provenance

```text
authority base:
  origin/main@7f278167e1e51f968896229ae438ea5a76398f90

integrated dependency:
  PR #847 through commit 168e9ba02

external theorem worker:
  ChatGPT Pro, R27 Role 01
  conversation 6a5927a2-1670-83ec-897d-9f760c0ce5df
  final response SHA-256
  3370f0937ecbfd4f43f6f3e9c5d13b547ad980da918afc7765aa8223819ee31c
  full rendered SHA-256
  5565ae711d64cc5934d83932ce66de7f5fe23a1f00566807e187fe97d3b1055a

native hostile audit:
  ACCEPT_MATH / REPAIR_PACKET, confidence 0.98
  gpt-5.6-sol ultra
  agent 019f6cb5-cd35-7cc0-b29f-99cbfc3f556d
```

## Nonclaims

This packet does not prove or claim:

- `D_2(u)<=211` for any `u<=1,043,901`;
- realizability or nonexistence of the relaxed `+1,707` profile;
- that C1--C4 are facet-defining, unique, or classification-complete;
- any source-to-arrangement transport, including the conditional geometry
  associated with former PR #848;
- any rank-15 parent saving or a closure of the rank-15 recurrence gap;
- any rank-16 result or all-rank theorem;
- Grand List, Grand MCA, or official-score movement.

The official score remains `0/2`.
