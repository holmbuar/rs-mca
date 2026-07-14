# Depth-zero identity owner for all transverse LineRay pairs

## Claim

Let `C=RS_F(U,k)` have `N=|U|`, let `a=k+1`, and put

```text
t=N-a=N-k-1.
```

Fix one received affine line and any finite set `P` of retained
`(slope,codeword)` pairs at agreement at least `a`.  Assume each retained pair
has an actual support on which the line point is explained but the received
pair is not simultaneously explained.  Then every pair can be assigned an
`a`-point noncommon agreement support, and this assignment is injective.
Consequently

```text
|P| <= binom(N,a).                                      (1)
```

This counts every retained codeword at every slope.  No one-witness-per-slope
selector is used.

At `a=k+1`, the identity-prefix depth is

```text
w=a-k-1=0.
```

The depth-zero boundary map has one realized value, so its image-normalized
identity scale is exactly

```text
barN_1=binom(N,a).                                      (2)
```

Thus (1) is an exact, constant-one profile payment for the complete transverse
LineRay pair set at the depth-zero boundary.

## Status

`PROVED / AUDIT` under the displayed Reed--Solomon and noncommon-support
hypotheses.  The accompanying Lean file is an `UNPROVED STATEMENT TARGET`, not
a Lean certificate.

This serves hard input 3, the residual ray compiler, only at the depth-zero
identity boundary.  It does not pay any positive-depth (`w>=1`) residual.

## Existing paper dependency

- `experimental/asymptotic_rs_mca_frontiers.tex`, equation (1.5), defines the
  identity scale `binom(N,a)|B|^{-w}` and therefore gives (2) at `w=0`.
- `experimental/rs_mca_thresholds.tex`, `prop:exact-support-upper`, proves the
  corresponding `binom(N,a)` ceiling after selecting one support for each
  distinct bad slope.  The present statement strengthens precisely this local
  count to the complete `(slope,codeword)` pair set, including same-slope
  multiplicity; it does not strengthen that proposition's global atlas scope.
- The same paper's profile-payment definition requires an actual slope or ray
  projection bound at the profile's natural scale.
- `tex/slackMCA_v4.tex`, `thm:onez` and `thm:exactslack`, supply the adjacent
  one-support and slack-one viewpoints.
- `selector_free_exact_weight_all_pair.md` constructs a genuine exponential
  double-nonpositive family at `R=t+1`.  Section 4 below identifies its exact
  profile owner.

The all-pair exact-weight construction is due to Danny (DannyExperiments).
The LineRay pair-count correction was developed by Latif Kasuli and holmbuar.
This note supplies the depth-zero ownership synthesis and the support-level
injection.

## Proof

### 1. A noncommon `a`-subset exists

Take one retained pair `(gamma,c)`, and let `S` be an agreement support of
size at least `a=k+1` on which the received pair is not simultaneously
explained.

Suppose, for contradiction, that the received pair were simultaneously
explained on every `a`-subset of `S`.  Two adjacent `a`-subsets meet in
`a-1=k` points.  A degree-less-than-`k` polynomial is determined by its values
on `k` distinct evaluation points, so the two explaining polynomials for each
component agree across adjacent subsets.  The graph of `a`-subsets of `S`,
joined when they differ in one point, is connected.  Hence the local
explanations glue to one pair of codewords on all of `S`, contradicting the
choice of `S`.

Therefore some `a`-subset `A(gamma,c) subseteq S` is still noncommon.  Fix one
such subset canonically.

### 2. The support assignment is injective

Suppose two retained pairs `(gamma,c)` and `(delta,d)` receive the same
support `A`.  Both line points agree with their explaining codewords on `A`.

If `gamma!=delta`, subtracting the two explanations and dividing by
`gamma-delta` gives a codeword explaining the line direction on `A`;
substitution back gives a codeword explaining the line anchor on `A`.  The
received pair is then simultaneously explained on `A`, contrary to the
selected noncommon-support property.

If `gamma=delta`, then `c` and `d` agree on the `a=k+1` points of `A`.
Their difference has degree less than `k` and at least `k+1` roots, so
`c=d`.  The retained pairs are equal.

Thus `(gamma,c) -> A(gamma,c)` is injective into the `a`-subsets of `U`,
proving (1).  The argument retains same-slope multiplicity: it proves that
distinct codewords at one slope must use distinct selected supports.

### 3. Exact profile payment

The identity-prefix map at agreement `a` has depth `w=a-k-1`.  When
`a=k+1`, `w=0`, its codomain and realized image are both the singleton empty
prefix.  Its full slice is the set of all `a`-subsets.  Therefore

```text
L_1=1,
barN_1=|Omega_1^0|/L_1=binom(N,a).
```

Combining this identity with (1) gives the required constant-one payment.
Because the pair count dominates the distinct-slope projection, the same
statement also pays the MCA slope numerator on this cell.

## The exact-weight route cut is sharp but already owned

Take the canonical construction from
`selector_free_exact_weight_all_pair.md`:

```text
N=t+k+1,       R=t+1,
h_x=(1,x,...,x^t)^T,
y_0=e_(t-1),   y_1=e_t.
```

For each `t`-set `T subset U`, put

```text
Q_T(X)=product_(x in T)(X-x),
c_T(x)=1/Q_T'(x) on T, and 0 off T.
```

Lagrange coefficient extraction gives

```text
H(c_T)=e_(t-1)+(sum_(x in T)x)e_t.                      (3)
```

The agreement support is `A=U\T`, of size `k+1`.  Distinct `T` give
distinct pairs, so

```text
|P|=binom(N,t)=binom(N,k+1)=barN_1.                     (4)
```

It attains the all-pair bound exactly.

The slope dictionary also identifies the known slack-one line.  Put
`sigma_U=sum_(x in U)x` and `z_A=-sum_(x in A)x`.  Then

```text
gamma_T=sum_(x in T)x=sigma_U+z_A.                      (5)
```

Hence the canonical slope set is an affine translate of the slack-one
restricted-sum image `-(k+1)^wedge U`.  Even if every restricted sum is
distinct and the slope count is exponential, (4) shows that it is exactly at
the depth-zero identity scale.  It is not a counterexample to profile-scale
RC.

This classification supersedes only the interpretation of that canonical
family as an unowned chart-only obstruction.  Its negative conclusion remains
correct: no field-independent polynomial bound is possible there.

## Reproducibility

Run

```bash
python3 experimental/scripts/verify_depth_zero_identity_lineray_owner.py --check
python3 -O experimental/scripts/verify_depth_zero_identity_lineray_owner.py --check
python3 experimental/scripts/verify_depth_zero_identity_lineray_owner.py --tamper-selftest
python3 -m json.tool experimental/data/certificates/depth-zero-identity-lineray-owner/depth_zero_identity_lineray_owner.json
```

The verifier checks the parameter identities on a deterministic grid and,
over exact prime-field fixtures, exhausts every canonical support, recomputes
the Lagrange weights and syndrome identity (3), checks the complement/slack
dictionary (5), and compares pair, support, identity-scale, and slope counts.

The Lean statement target is

```text
experimental/lean/grande_finale/GrandeFinale/DepthZeroIdentityLineRayOwner.lean
```

It records the noncommon-support selector, its injection, the binomial cap,
and the depth-zero profile arithmetic.  It does not claim a Lean proof.

## Ledger impact and nonclaims

The result closes the `R=t+1`, `a=k+1`, `w=0` endpoint of the realized
weighted-puncture residual at its exact natural scale, and explains why the
integrated canonical exponential family is sharp rather than obstructive.

It does **not**:

- pay a positive-depth identity profile;
- prove prefix max-fiber flatness, MI/MA, Sidon payment, or a full profile
  envelope comparison;
- pay a double-nonpositive exact-weight stratum at `w>=1`;
- prove atlas exhaustivity or that every chart is assigned to the identity
  profile first;
- replace the need for an actual noncommon support on each retained pair;
- move a deployed finite row or alter stable paper TeX/PDF; or
- claim Lean certification.
