# Primitive top-seam marked-incidence audit v1

Status: `PROVED_LOCAL / COUNTEREXAMPLE_TO_SHORTCUTS / AUDIT / OPEN_GAP`.

## Claim and scope

This note audits the first shift-pair seam

```text
e = w + 1,
A - B = c != 0,
```

using the complete ordered marked object `(G,A,B)`.  Here `A` and `B` are
monic split degree-`e` side locators, `G` is the monic split common-core
locator, the three root sets are pairwise disjoint, and hence `G,A,B` are
pairwise coprime.  The reconstructed supports are

```text
M = roots(G) union roots(A),
E = roots(G) union roots(B).
```

The audit does not replace `(G,A,B)` by `(A,B)`, does not choose a unique mate
for a support, and does not call a support-side packet primitive unless the
actual earlier slope projections have been executed.

The exact verifier and certificate are:

```text
experimental/scripts/verify_primitive_top_seam_marked_incidence_v1.py
experimental/data/certificates/primitive-top-seam-marked-incidence-v1/
```

## Theorem 1: marked top-seam bijection

**Status: PROVED.**

Fix a locator-coefficient prefix target `z`, support size `m`, and `e=w+1`.
If `z` is instead represented by the first `w` power sums, assume
`char(F)>w`.  Ordered distinct support pairs `(M,E)` in the target fibre with

```text
|M \ E| = |E \ M| = e
```

are in bijection with ordered triples `(G,A,B)` satisfying the normal form
above and the target condition on `GA` and `GB`.  The inverse maps are the
displayed support reconstructions.  In particular the common-core mark is not
auxiliary data: it is exactly the intersection locator.

This is the top-seam specialization of the exact second-moment bijection in
`thm:capg-second-moment`.  The verifier independently checks it by enumerating
both full support pairs and side pairs with all common cores.

## Theorem 2: fixed-side common cores are a punctured prefix fiber

**Status: PROVED.**

Assume `char(F)>w`, and let `Phi_w(S)=(p_1(S),...,p_w(S))`.  For fixed target
`z` and fixed side locators `(A,B)`, define

```text
C_z(A,B) = {
  G : G is monic split of degree m-e over D \ (roots(A) union roots(B)),
      Phi_w(roots(G) union roots(A)) = z
}.
```

Because power sums are additive on disjoint unions and `A-B` is constant,

```text
Phi_w(roots(A)) = Phi_w(roots(B)),

G in C_z(A,B)
  iff
Phi_w(roots(G)) = z - Phi_w(roots(A)).
```

Thus the exact common-core multiplicity is

```text
mu_G(z,A,B) = |C_z(A,B)|,
```

a max-fiber problem on the punctured domain.  When `char(F)>w`, Newton
identities give the equivalent affine coefficient slice with the first `w`
high coefficients of `G` fixed.  Consequently common-core determinacy is not a
free consequence of the constant-shift side equation; it is a punctured
prefix-fiber theorem of Q type.

For a fixed target `z`, let `T_z` be a surviving marked set, `P_full,z` its
ordered reconstructed-support-pair image, and `P_side,z` its oriented
side-locator-pair image.  Then

```text
|T_z| = |P_full,z| <= mu_G^max(z) |P_side,z|,
mu_G^max(z) = max_(A,B) mu_G(z,A,B).
```

If targets vary, `z` must remain in the side-projection key; it may not be
forgotten before applying this bound.

When predicates are side-only and the target is forgotten, every side pair
has exactly

```text
binom(n-2e,m-e)
```

marks.  This raw factor cannot be carried through target fixation or
first-match pruning without proving the corresponding fiber statement.

## Counterexample 1: fixed target and fixed sides do not determine G uniquely

**Status: COUNTEREXAMPLE_TO_UNIQUENESS, not a counterexample to an
`exp(o(n))` theorem.**

Over `F_17^*`, take `m=8`, `w=2`, `e=3`, target `z=(16,16)`, and

```text
roots(A) = {1,4,11},
roots(B) = {3,14,16}.
```

Then

```text
A = X^3 + X^2 + 8 X + 7,
B = X^3 + X^2 + 8 X + 8,
A-B = 16.
```

The same `(z,A,B)` admits exactly the following three five-point common cores:

```text
{2,5,7,8,12},
{5,9,10,12,15},
{6,8,9,13,15}.
```

The side pair has no common multiplicative pullback scale and no affine map
`x -> ax+b` sends its `A` roots to its `B` roots.  All three cores and all six
reconstructed supports have trivial multiplicative and affine stabilizer.
The three marks lie in the raw fixed-target coefficient slice described by
Theorem 2.  That condition is tautological for this common-core fibre and is
not an affine first-match owner.  The three `G` marks are distinct and their
root intersection is empty, so they also do not establish a planted divisor.
However, the three oriented `M=GA` supports share the fixed side divisor `A`,
and the three `E=GB` supports share `B`; only the aggregate of all six supports
has empty intersection.  The packet therefore leaves the complete C1, C3, and
pre-C8 common-GCD owner tests unknown and does not admit the family to the
primitive residual.

The full exact census is stronger than this example.  Among `132352` nonempty
fixed `(z,A,B)` keys, the common-core multiplicity histogram is

```text
1: 91680 keys
2: 36480 keys
3:  4000 keys
4:   192 keys.
```

Hence multiplicity-one is false after target fixation and the displayed
multiplicative/affine-stabilizer checks.  These checks are not an exhaustive
first-match classification.  The maximum `4` is finite evidence only and does
not decide subexponential determinacy in the deployed regime.

## Audit finding 2: support-side triples do not carry a first-match owner

**Status: PROVED_TYPE_SEPARATION / OWNER CLASSIFICATION OPEN.**

Authoritative first match assigns a bad slope to the first cell whose actual
witness projection contains that slope.  It does not assign an unrooted
support pair or marked triple.

The known `F_17^*` packet makes the projection loss executable.  At `m=4,w=2`,
the support

```text
S0 = {4,6,11,13}
```

is periodic under multiplication by `-1` and has exactly four top-seam mates
at target `(0,2)`.  Periodicity of the support alone does not establish C1
ownership: the received words and explanation data must also descend, and the
present pole line does not supply that classification.  Accordingly the
certificate records only a periodic-support trigger and assigns no actual
first-match owner to any endpoint ray.

Even without an owner assignment, the marked triple has two distinct endpoint
projections and a separate oriented selected-support projection.  A
triple-level owner tag would therefore erase information needed by the rooted
compiler.  The verifier rejects every attempt to admit this packet as primitive
while any earlier slope predicate remains unknown.

The missing typed chain is

```text
(G,A,B)
  -> (gamma,S,h)
  -> (gamma,h)
  -> (gamma,c)
  -> gamma.
```

Without that rooted chain and a witness-exhaustive atlas, the phrase “the set
of marked triples surviving all first-match pruning” does not denote an
executable set in the current artifacts.

## Mandatory F_17 multiple-mate regression

**Status: PROVED_EXACT_FINITE.**

The verifier reproduces the complete seven-support target fibre.  Write the
marked support as

```text
S0 = {4,6,11,13},  Phi_2(S0)=(0,2).
```

It has exactly four top-seam mates

```text
{1,2,4,10},
{3,8,10,13},
{4,7,9,14},
{7,13,15,16},
```

In the orientation `M=S0`, `E=mate`, these have constants

```text
A-B in {5,7,10,12}.
```

All four rooted-star triples satisfy the degree, splitting,
pairwise-disjointness, and pairwise-coprimality checks.  But the star is not the
complete marked object.  Across all seven supports, the exact top-seam graph
has `16` unordered edges and therefore

```text
32 ordered marked triples (G,A,B),
32 ordered reconstructed support pairs P_full,
32 ordered side-locator pairs P_side.
```

The two remaining fibre supports are `{2,3,5,7}` and `{10,12,14,15}`; each is
at distance `e=4` from the marked support above but participates in other
`e=3` pairs.  Omitting them is precisely the selected-support/unique-mate
shortcut forbidden by the counterpacket.

Two rooted-star side pairs admit a root-set affine transport.  The marked
support also has periodicity scale `2`.  Neither fact is promoted to a paid
owner: the affine maps are not declared domain maps with rooted slope payment,
and support periodicity alone does not prove quotient descent of the received
line and explanation.  Both candidates are gated before primitive admission,
and the complete owner tests remain fail-closed.

## Mandatory common-core mark-erasure regression

**Status: PROVED_EXACT_FINITE.**

For `F_17^*`, `m=8`, `w=2`, `e=3`, there are

```text
704 ordered side pairs,
252 = binom(10,5) common-core marks per side pair,
177408 = 704*252 ordered marked triples.
```

An independent full-support enumeration also returns `177408`.  Therefore the
orientation-preserving projection

```text
(G,A,B) -> (A,B)
```

loses the exact factor `252` before target fixation.  The fixed-target census
above records the separate losses after retaining `z`.  Ordered marked counts
are never compared with unordered side-pair counts.

## Projection to the MCA numerator

**Status: PROVED_COMBINATORIAL_INTERFACE; application remains open.**

Keep the following objects separate:

```text
T_z       marked support incidences (G,A,B),
P_full,z  ordered reconstructed support pairs (GA,GB),
P_side,z  ordered side-locator pairs (A,B),
X         explanation states (gamma,S,h),
R         witness rays (gamma,h),
C         codeword rays (gamma,c),
Z         distinct MCA slopes gamma.
```

The top-seam bijection gives `|T_z|=|P_full,z|`; only the projection to
`P_side,z` incurs `mu_G`.  For an actual rooted incidence
`I subset Z_T x T_z`, where `Z_T` is exactly its incident slope image, put

```text
H = min_(gamma in Z_T) deg_I(gamma) >= 1,
J = max_(t in T_z) deg_I(t).
```

Exact double counting gives

```text
H |Z_T| <= |I| <= J |T_z|,

|Z_T| <= floor(J |T_z| / H)
      <= floor(J mu_G^max |P_side,z| / H).
```

Thus a natural-scale side-pair estimate reaches the MCA numerator only after
proving

```text
J mu_G^max / H = exp(o(n))
```

or an explicit finite analogue.  A second moment, one selected pair per slope,
or a marked-pair count alone does not supply this statement.  If a complete MCA
slope has degree zero from the selected marked family, then `H=0` on the full
slope set and the inequality is inapplicable.

The verifier directly constructs the pole line

```text
f(x)=U_z(x)/x,  g(x)=-1/x,
```

and exhaustively scans all `17^2` slope/constant-codeword choices.  It finds
exactly seven agreement states and the complete layers

```text
7 explanation states,
7 witness rays,
7 codeword rays,
4 distinct MCA slopes {2,5,8,11}.
```

For the complete `32`-triple ordered top seam, use the functional projection
that sends `(G,A,B)` to its selected support `M=roots(GA)`.  The exact marked
degrees by slope are

```text
gamma  2   5   8  11
degree 4  10  10   8
```

The seven selected-support/ray degrees are three `4`s and four `5`s, so
`H=4`, `J=1`, `|I|=32`, and

```text
4 = |Z| <= J|T|/H = 8.
```

The symmetric two-endpoint relation is also printed separately; it has
`H=8`, `J=2`, and `64` edges.  It is not substituted for the functional
selected-support compiler.

The four-mate rooted star is oriented with `M=S0` and `E=mate`, so its printed
constants use `A=Q_(S0\mate)` and `B=Q_(mate\S0)`.  It supplies two additional
regression scopes:

- with `S0` selected, four marked incidences project to one explanation state,
  one witness ray, and slope `2` (`H=4,J=1`);
- with the four mates selected in the reverse orientations, four incidences
  project to four rays and then two slopes `{5,8}` (`H=2,J=1`).

Thus several marked incidences really do project to one ray, and several rays
really do project to one slope.  The both-endpoint star sees only slopes
`{2,5,8}` and misses slope `11`; its `H` on the complete slope set is zero.
Only the separate complete `32`-triple raw seam covers all four slopes, and
that finite raw coverage is not a first-match-pruned asymptotic payment.

## Fail-closed owner contract

**Status: AUDIT / EXECUTABLE_SCHEMA.**

Each owner test has one of the states

```text
NOT_APPLICABLE
STRUCTURAL_TRIGGER_ONLY
PAID_OWNER
NAMED_RESIDUAL
UNKNOWN_MISSING_CONTEXT.
```

The certificate uses a local refinement of the source C1--C9 order:
quotient-pullback; Chebyshev/dihedral; planted; tangent; extension/descent;
differential-locator, rank, and bounded-SPI; saturation; a separate
family-level common-GCD exclusion; balanced core and split pencil only after
common/planted factors are removed; then Fourier/Sidon.  The added common-GCD
test is explicitly `pre_C8`, not bundled into the balanced-core cell.

A triple is admitted as primitive only when every earlier actual-slope
predicate is executable and false.  `STRUCTURAL_TRIGGER_ONLY` and
`UNKNOWN_MISSING_CONTEXT` both block admission.  In particular:

- a periodic support is only a C1 candidate until the support, received words,
  explanation, natural-profile census, and slope projection descend;
- a root-set affine transport is only a candidate until it is a declared
  domain map with rooted witness descent and an exact slope budget;
- the raw fixed-target coefficient slice for `G` is the Q-type multiplicity
  problem, not an earlier affine owner;
- several arbitrary `G` marks are not planted unless a predetermined common
  divisor family and its payment census are supplied.

The periodic and affine-candidate regressions are executed before primitive
admission and are both blocked.  This is a gate test, not a claim that either
candidate is an actual paid owner.  Any `PAID_OWNER` row must carry a source
cell, projector certificate ID, projection type, and exact slope budget.  The
current expected state vector contains no paid owner; the tamper self-test
rejects fabricated C1 and C3 payments even after the payload hash is recomputed.

The marked common core `G=gcd(GA,GB)` is also distinct from a common-GCD owner,
which requires one divisor fixed across every support locator in a classified
family.  In the fixed three-core packet, the six-support aggregate has empty
intersection but its two oriented endpoint subfamilies retain fixed divisors
`A` and `B`; without the rooted atlas, `pre_C8_common_GCD` must remain unknown.

## Status of the four requested targets

1. **Common-core determinacy: OPEN.**  The exact reduction to a punctured
   prefix fiber is proved; uniqueness is refuted; an `exp(o(n))` maximum after
   the actual slope-level deletions is not proved or refuted.
2. **Marked-incidence payment: OPEN.**  The complete finite `F_17` raw seam has
   `32` ordered triples and a functional `H=4,J=1` projection, and the `m=8`
   census counts `177408` raw triples.  Neither supplies the asymptotic
   natural-profile bound after actual first-match pruning.
3. **Earlier-owner classification: OPEN.**  Quotient and affine candidates are
   gate-tested before primitive, but the complete rooted owner projectors and
   paid budgets are absent; no candidate is mislabeled as an owner.
4. **New obstruction: NOT ESTABLISHED.**  The finite packets refute shortcuts,
   not the fully pruned asymptotic ledger; no new floor is claimed.

## Exact nonclaims

This packet does not:

- prove Q, C7, C8, or C9;
- prove a KoalaBear or Mersenne-31 adjacent safe row;
- construct the complete witness-exhaustive first-match atlas;
- call a raw side pair, marked triple, or structural trigger primitive;
- treat a pair-level quotient or affine relation as a paid marked-profile
  owner;
- turn a marked-pair or second-moment estimate into a slope payment without
  `H,J`;
- promote the four-mate rooted star to the complete MCA numerator;
- call the complete `32`-triple raw `F_17` seam post-first-match primitive;
- modify a paper source.

## Reproduction

```text
python3 experimental/scripts/verify_primitive_top_seam_marked_incidence_v1.py --check
python3 experimental/scripts/verify_primitive_top_seam_marked_incidence_v1.py --tamper-selftest
```

The verifier uses two independent exact enumerations for the `177408` marked
count, an exhaustive `17^2` pole-line scan, and a complete ordered enumeration
of the `32`-triple target-fibre seam.  Its tamper self-test rejects `19/19`
semantic mutations, including fabricated paid-owner states.

OPEN GAP
