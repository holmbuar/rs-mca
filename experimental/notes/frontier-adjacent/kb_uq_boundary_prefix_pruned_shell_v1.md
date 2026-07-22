---
workboard_item: K2
row: KoalaBear MCA at 2^-128
object: MCA
target_epsilon: 2^-128
agreement: 1116048
B_star: 274980728111395087
direct_statement: "For every admissible received line, KB_V4_PRUNED_Q_ROOTED_SHELL(b,c) implies the branch-sensitive cap on Z_Q; at (b,c)=(0,1), |Z_Q| <= 57198030366. An explicit column-far extension-pole family certifies |Z_Q| >= 57198030366 on one line."
architecture: GRANDE_FINALE_V4_KB_MCA_TANGENT_SOURCE_ADAPTER_V1
partition_digest: 4fade91abc408264989babcff6f8f9bbd80bcec52545a5db15ac376bf17d88fc
atom_or_cell: ACTIVE_V4_BOUNDARY_PREFIX_Q after SOURCE_COORDINATE_TANGENT_IMAGE
quantifier: "uniform over every admissible received line over F_(p^6); the lower floor is existential"
projection_and_unit: distinct bad finite slopes per received line
claimed_bound: "CONDITIONAL U_Q = 57198030366 under KB_V4_PRUNED_Q_ROOTED_SHELL(0,1); PROVED lower floor 57198030366"
status: CONDITIONAL
impact: LOCAL_ONLY
falsifier: "one admissible line violating a pointwise rooted-shell inequality, or one line with |Z_Q| > 57198030366; |Z_Q| > 274980728110413983 would be TANGENT_FIRST_OWNER_ORDER_REFUND"
replay: "python3 experimental/scripts/verify_kb_uq_boundary_prefix_pruned_shell_v1.py --check; python3 experimental/scripts/verify_kb_uq_boundary_prefix_pruned_shell_v1.py --tamper-selftest; source and artifact hashes are pinned in the certificate"
---

# KoalaBear boundary-prefix Q after tangent deletion

## 1. Frozen contract

This packet keeps the round-1 contract unchanged.

| field | frozen value |
|---|---:|
| base prime `p` | `2130706433` |
| line/code field | `F_(p^6)` |
| domain size `n` | `2097152` |
| code dimension `k` | `1048576` |
| agreement `a` | `1116048` |
| mismatch size `j=n-a` | `981104` |
| CAP25 coefficient-prefix dimension `K=k+1` | `1048577` |
| boundary-prefix depth `w=a-K` | `67471` |
| tangent payment `U_paid'` | `981104` |
| row budget `B*` | `274980728111395087` |
| reserve after tangent | `274980728110413983` |

The owner order remains

```text
SOURCE_COORDINATE_TANGENT_IMAGE
  -> ACTIVE_V4_BOUNDARY_PREFIX_Q
  -> ACTIVE_V4_BALANCED_CORE
  -> UNPAID_V4_COMPLEMENT.
```

For one received line `r`, let `Z` be its complete bad-slope set, let `T(r)` be
the round-1 source-coordinate tangent image, and put

```text
Z_Q(r) = (Z \ T(r)) ∩ ACTIVE_V4_BOUNDARY_PREFIX_Q.
```

The unit is one distinct finite slope. No support multiplicity is charged as a
slope, and no maximum is taken separately over alternative translations.

## 2. Verdict

This packet delivers rung **A3**, not A1 or A2.

- A source-bound theorem proves that every non-column-far tangent survivor has
  exchange distance at least `w+2=67473` from a canonical source anchor. Thus
  tangent deletion removes the first boundary-prefix exchange shell in the
  sparse branch.
- One named pointwise hypothesis,
  `KB_V4_PRUNED_Q_ROOTED_SHELL(b,c)`, compiles to an exact uniform cap.
- At `(b,c)=(0,1)` the compiled cap is
  `57198030366`, leaving reserve `274980670912383617`.
- A column-far scalar-extension simple-pole construction certifies the lower
  floor `|Z_Q| >= 57198030366` on one admissible line.
- The rooted-shell hypothesis is not proved here. Therefore this is not an
  unconditional banked `U_Q`, not a refund, and not a row closure.

The exact remaining K2 theorem is the truth or falsity of
`KB_V4_PRUNED_Q_ROOTED_SHELL(0,1)` on the frozen residual.

## 3. Source binding

The packet uses only the following proved source interfaces.

1. Round 1 defines the canonical sparse translation and tangent image. In the
   non-column-far branch it fixes one common explaining triple, translates by
   its two codewords, and obtains source support `Sigma` of size at most
   `j=981104`. Its tangent image is

   ```text
   T(r) = {-e0(x)/e1(x) : x in Sigma, e1(x) != 0}.
   ```

   In the column-far branch it sets `T(r)=empty`.

2. `experimental/rs_mca_thresholds.tex`, `thm:exact-sparsification` and `(SP3)`,
   with the integrated theorem
   `RsMcaThresholds.ExactSparsification.mcaBad_sub_mem_iff`, preserve the exact
   bad-slope predicate under that one fixed translation.

3. `GrandeFinale.RSExactSupportUpper.mcaBad_has_exact_support` supplies an exact
   `a`-element support while preserving support-wise MCA nontriviality.

4. `GrandeFinale.SyndromeLine.badSlopesOnSupport_card_le_one` proves that one
   fixed noncommon support carries at most one finite slope. This is the
   support-to-slope injectivity used below.

5. `GrandeFinale.PrefixPigeonhole.exists_large_coefficientFiber` and
   `prefixPolynomial_list_floor`, together with
   `GrandeFinale.ExactPrefixList`, give the exact base-field prefix fiber/list
   dictionary with denominator `p^w`.

6. `GrandeFinale.PrefixRigidityPacking.coefficientFiber_johnsonDistance` gives
   one-sided Johnson distance at least `w+1` between distinct supports in one
   depth-`w` coefficient fiber.

7. Grande Finale v4 `prob:large-owner` identifies the full-owner simple-pole
   boundary atom as the challenge-slope image

   ```text
   {U_z(alpha)-Lambda_M(alpha) : M in Fib_w(z)}.
   ```

8. `GrandeFinale.ScalarExtensionListLine.mappedPolynomialList_card` and
   `extensionAgreementSet_map_eq_base` preserve a selected base prefix
   subfamily and all of its agreement supports after scalar extension.

9. `GrandeFinale.SeparatingPole.exists_separating_pole` gives an off-domain
   pole whose evaluation is injective on any supplied finite polynomial
   family under the exact unordered-pair budget, and
   `GrandeFinale.CollisionAwarePole.eval_slope_mcaBad` turns every selected
   polynomial into a bad slope of the resulting simple-pole line.

No legacy-M1 charge is transported.

## 4. Proven pruning theorem

### Theorem 4.1 — tangent survivors are nonzero on the source support

Work in the non-column-far branch after the canonical sparse translation. Write

```text
e_gamma = e0 + gamma e1,
Sigma = supp(e0) union supp(e1).
```

If `gamma` is not in `T(r)`, then

```text
e_gamma(x) != 0 for every x in Sigma.
```

Indeed, if `e1(x) != 0` and `e_gamma(x)=0`, then
`gamma=-e0(x)/e1(x)` belongs to `T(r)`. If `e1(x)=0`, membership in `Sigma`
forces `e0(x) != 0`, so again `e_gamma(x) != 0`.

This is the first place where `Z \ T(r)`, rather than `Z`, is used.

### Theorem 4.2 — exact-support source intersection

Let `gamma in Z \ T(r)`. Select an exact `a`-support `S_gamma` and a degree-`<k`
explanation polynomial `h_gamma` using
`RSExactSupportUpper.mcaBad_has_exact_support`.
Then

```text
|S_gamma ∩ Sigma| >= a-k+1 = 67473 = w+2.
```

Proof.

- `S_gamma ∩ Sigma` is nonempty. Otherwise both translated received words are
  zero on `S_gamma`, so the pair is simultaneously explained there by the zero
  codewords, contradicting the selected support's MCA nontriviality.
- On `S_gamma ∩ Sigma`, the explanation equals `e_gamma`, which is nonzero by
  Theorem 4.1. Hence `h_gamma` is not the zero polynomial.
- On `S_gamma \ Sigma`, the translated line word is zero, so `h_gamma` vanishes.
  A nonzero polynomial of degree `<k` has at most `k-1` roots. Therefore

  ```text
  |S_gamma \ Sigma| <= k-1,
  |S_gamma ∩ Sigma| >= a-(k-1)=67473.
  ```

Every displayed inequality is source-bound: exact support comes from the
integrated exact-support theorem, translation invariance from exact
sparsification, and the last inequality from the Reed--Solomon root bound.

### Corollary 4.3 — the first sparse exchange shell is deleted

Pad `Sigma` canonically to a `j`-set `A_Sigma`, and let
`S_Sigma=D\A_Sigma`, an `a`-set. Complementation preserves one-sided Johnson
exchange distance, and

```text
d_J(S_Sigma,S_gamma)
  = |S_Sigma \ S_gamma|
  = |A_Sigma ∩ S_gamma|
  >= |Sigma ∩ S_gamma|
  >= w+2.
```

Thus every sparse-branch slope in `Z_Q` lies in a shell

```text
e in {w+2,...,j} = {67473,...,981104}
```

around the canonical source anchor. The ordinary boundary-prefix minimum shell
is `w+1=67472`; tangent deletion removes that shell in this branch.

By `SyndromeLine.badSlopesOnSupport_card_le_one`, choosing one exact support
canonically for each distinct slope gives an injection from `Z_Q` into the
selected support family.

The conclusion is false as stated for `Z` in place of `Z\T(r)`: at a tangent
slope the nonvanishing argument on `Sigma` fails, and the `w+1` shell is no
longer deleted.

## 5. The one residual hypothesis

For `0 <= e <= j`, define the full Johnson shell capacity around one `a`-set by

```text
H_e = binom(a,e) binom(j,e).
```

Let `Q0=p^w`. For nonnegative integers `b,c`, the named residual hypothesis

```text
KB_V4_PRUNED_Q_ROOTED_SHELL(b,c)
```

means the following pointwise statement for **every** admissible received line.
The exact-support selector is the canonical selector described above, and shell
counts count distinct slopes through that injective selector.

### Column-far clause

Here round 1 has `T(r)=empty`. If `Z_Q` is nonempty, choose its canonical first
slope and its selected support `S_0`. Boundary-prefix membership and
`PrefixRigidityPacking.coefficientFiber_johnsonDistance` place every other
selected support in a shell `e>=w+1`. Let `d_e(S_0)` be the number of the other
Q slopes in shell `e`. For every `e=w+1,...,j`, require

```text
Q0 * max(d_e(S_0)-b,0) <= c * H_e.                 (CF_e)
```

### Non-column-far sparse clause

Use the source anchor `S_Sigma` from Corollary 4.3. Let `d_e(S_Sigma)` be the
number of Q slopes whose selected support lies in shell `e`. The proved pruning
theorem gives `d_e=0` for `e<=w+1`. For every `e=w+2,...,j`, require

```text
Q0 * max(d_e(S_Sigma)-b,0) <= c * H_e.             (SP_e)
```

These two clauses are one branch-sensitive finite hypothesis. They are not two
independent residual assumptions: the round-1 column-far dichotomy decides
which clause applies to a line.

At `(b,c)=(0,1)` the hypothesis says exactly that every active shell contains at
most its full-shell capacity divided by the base prefix codomain size, in
cross-multiplied integer form.

## 6. Exact compiler

Put

```text
T_CF = sum_{e=w+1}^j H_e,
T_SP = sum_{e=w+2}^j H_e,
R_CF = j-w   = 913633,
R_SP = j-w-1 = 913632.
```

Summing `(CF_e)` and using
`d <= b+max(d-b,0)` gives

```text
|Z_Q| <= U_CF(b,c)
      := 1 + b R_CF + floor(c T_CF/Q0).
```

The leading `1` is the canonical column-far anchor. Summing `(SP_e)` gives

```text
|Z_Q| <= U_SP(b,c)
      := b R_SP + floor(c T_SP/Q0).
```

There is no sparse leading anchor because every sparse survivor is counted in a
positive-distance source shell. Therefore the uniform conditional cap is

```text
U_Q(b,c) := max(U_CF(b,c), U_SP(b,c)).
```

For all nonnegative `b,c`, `U_CF` is the dominating branch for this row.

The stdlib-only Lean module in this packet checks the pointwise-to-summed
rooted-shell compiler, both the anchored and anchor-free variants, the
`67473=w+2` source-intersection arithmetic, and all printed deployed constants.
The large binomial quotient is independently replayed by the integer verifier.

## 7. Exact arithmetic and viable window

Vandermonde gives

```text
sum_{e=0}^j H_e = binom(n,a) = binom(n,j).
```

Two independent exact computations certify

```text
floor(binom(n,j)/p^w) = 57198030365,
ceil (binom(n,j)/p^w) = 57198030366,
floor(T_CF/p^w)       = 57198030365,
floor(T_SP/p^w)       = 57198030365.
```

The last two equalities are checked without materializing the enormous omitted
tails. Two independent routes compute `binom(n,j)`, the boundary shell terms,
and the exact remainder modulo `p^w`; monotonicity gives
`sum_{e=0}^w H_e <= (w+1)H_w` and
`sum_{e=0}^{w+1} H_e <= (w+2)H_(w+1)`, and both upper bounds lie strictly below
the relevant remainders. The same guarded subtraction certifies every printed
window endpoint.

Consequently

```text
U_CF(0,1) = 57198030366,
U_SP(0,1) = 57198030365,
U_Q (0,1) = 57198030366.
```

The remaining reserve would be

```text
274980728110413983 - 57198030366
  = 274980670912383617.
```

This leaves room for the balanced-core and complement cells, but it is
conditional room only.

### Complete arithmetic window

Let

```text
L = 57198030366,
R = R_CF,
T = T_CF,
Reserve = 274980728110413983.
```

A nonnegative integer pair `(b,c)` is arithmetically viable exactly when

```text
L <= 1+bR+floor(cT/Q0) <= Reserve.
```

For fixed `b`, put `Y=Reserve-1-bR`. If `Y<0` there is no viable `c`; otherwise

```text
c_min(b) = ceil(max(0,L-1-bR) Q0 / T),
c_max(b) = floor(((Y+1)Q0-1)/T).
```

The viable integers are precisely `c_min(b) <= c <= c_max(b)`.
Equivalently, for fixed `c`, with `f_c=floor(cT/Q0)`,

```text
b_min(c) = ceil(max(0,L-1-f_c)/R),
b_max(c) = floor((Reserve-1-f_c)/R),
```

provided the upper numerator is nonnegative.

Exact boundary slices are

```text
b=0:        1 <= c <= 4807520,
c=0:        62606 <= b <= 300975039332,
c=4807520:  0 <= b <= 58194.
```

The last admitted point on the full-budget multiplier slice has

```text
U_Q(58194,4807520) = 274980728109989882
```

and margin `424101`. The next point has

```text
U_Q(58195,4807520) = 274980728110903515,
```

which exceeds the reserve by `489532`.

Thus `(0,1)` is the smallest normalized viable pair and the only displayed pair
whose conditional cap equals the certified lower floor.

## 8. Certified lower floor

The lower construction uses the actual base-prefix/extension-line dictionary,
not a field-size count.

1. `PrefixPigeonhole.exists_large_coefficientFiber` gives a base-field depth-`w`
   coefficient fiber of cardinality at least

   ```text
   L = ceil(binom(n,a)/p^w) = 57198030366.
   ```

   Select exactly `L` supports from that fiber and their distinct listed
   polynomials. This exact-size selection is essential: the heavy fiber may be
   larger, so a separation check using only its lower bound cannot be applied
   to the complete fiber.

2. Map the selected polynomials to `F_(p^6)`.
   `ScalarExtensionListLine.mappedPolynomialList_card` and
   `extensionAgreementSet_map_eq_base` preserve their exact cardinality and
   agreement supports. The generic separating-pole budget is

   ```text
   n + k*binom(L,2)
     = 1715268316138129359421571072
     < p^6,
   ```

   with margin

   ```text
   93571093019388561295270373779934612037648035832681988097.
   ```

3. `SeparatingPole.exists_separating_pole` therefore selects an off-domain
   extension pole at which the `L` mapped polynomial values are pairwise
   distinct. For each selected polynomial,
   `CollisionAwarePole.eval_slope_mcaBad` supplies a bad slope of the same
   simple-pole received line. Hence that line has at least `L` distinct bad
   slopes; no completeness claim for the selected subfamily is used.

4. The pole direction cannot be explained by a degree-`<k` polynomial on
   `k+1` points: multiplying by `X-alpha` would produce a nonzero polynomial of
   degree at most `k` with at least `k+1` roots and value `1` at `alpha`.
   Therefore the pair is column-far, so round 1 gives `T(r)=empty`.

5. Each selected slope comes from the full-owner boundary-prefix fiber singled
   out in Grande Finale v4 `prob:large-owner`. Since `T(r)=empty` and Q is the
   next frozen owner, all selected slopes belong to `Z_Q`, and

   ```text
   |Z_Q(r)| >= 57198030366.
   ```

This is a lower floor, not an exact unconditional value. The complete heavy
fiber may be larger. In particular, the construction does not prove the
rooted-shell hypothesis; a larger attained fiber would falsify `(0,1)`.

The floor is far below the reserve, so it is not a refund and not a row
refutation.

## 9. Rung ladder record

Every rung was attacked from at least two distinct angles.

### A1 — exact unconditional pruned row-sharp Q

**Angle 1: sparse source polynomial.** Theorem 4.2 proves the exact deletion of
the first sparse exchange shell. It stops at the occupancy of the remaining
`913632` shells; root counting alone does not control their joint slope image.

**Angle 2: exact moments/packing.** Prefix rigidity, Johnson packing, the exact
second moment, and the pruned-Q toy calibration were tested. Packing lacks the
`p^-w` factor, and pruning can leave the maximizing fiber unchanged. None gives
a reserve-sized uniform maximum.

### A2 — any unconditional nonvacuous cap

**Angle 1: inject into surviving support shells.** The source anchor and fixed-
support slope uniqueness give an honest pruning-dependent injection, but the
raw surviving-shell capacity already exceeds the reserve; no unconditional
cap results.

**Angle 2: singleton/top-seam Route-D.** The candidate `t(p-1)` image-cell cap
fits numerically, but its weighted primitive SP/Padé, planted-core,
strict-distance, and charged-row-scope payments remain open. It is not a proved
one-hypothesis cap and cannot be banked as A2.

### A3 — one finite residual hypothesis

**Angle 1: rooted-shell aggregation.** The branch-sensitive pointwise condition
above compiles exactly and uses tangent deletion in the sparse branch. This is
the delivered rung.

**Angle 2: direct max-fiber/MI--MA.** A direct hypothesis of the form
`max fiber <= 57198030366` merely restates K2 and does not spend tangent
pruning. It was rejected in favor of the pointwise shell condition.

### B — refund or blowup

**Angle 1: extension-pole boundary family.** It gives the certified floor
`57198030366`, far below reserve.

**Angle 2: quotient and top-seam support packets.** Existing large support
families do not supply one admissible received line with Q membership,
tangent survival, and distinct-slope projection above reserve. No refund or row
refutation follows.

## 10. Mandatory adversarial epilogue

The strongest attack found was against the lower-floor separation step. The
heavy-fiber theorem gives only `|Fib_w(z)|>=L`; checking the separating-pole
budget at `L` does not justify applying a complete-fiber theorem when the actual
fiber may be larger. The construction now selects an exact `L`-subfamily first,
maps that subfamily to `F_(p^6)`, applies the generic separating-pole theorem,
and invokes the pointwise simple-pole bad-slope theorem. No completeness or
exact-total claim remains.

A second attack found a branch mistake in the first draft. The simple-pole lower
family is column-far, so its compiler has a leading anchor `+1`. Applying the
sparse anchor-free formula to that line would incorrectly claim that `(0,1)` is
refuted by one slope. Separating the branches fixes the error: `(0,1)` compiles
to the floor `57198030366` in the column-far branch and to `57198030365` in the
sparse branch.

Further attacks were checked as follows.

- **Zero denominator coordinate.** If `e1(x)=0` on `Sigma`, then `e0(x)!=0`;
  tangent survival still implies `e_gamma(x)!=0`.
- **Zero explanation polynomial.** Exact-support MCA nontriviality forces the
  support to meet `Sigma`; there the line value is nonzero, so `h_gamma` is not
  zero.
- **Support selector collision.** One fixed noncommon support carries at most
  one finite slope, so the selected-support map is injective.
- **Padding artifact.** Padding `Sigma` to a `j`-set only enlarges
  `A_Sigma ∩ S_gamma`; it cannot weaken the `67473` lower bound.
- **Deletion-free substitution.** Replacing `Z\T(r)` by `Z` destroys Theorem
  4.1 and reopens the `w+1` sparse shell. The proof is not deletion-free.
- **Lower-floor exactness and separation.** The source theorem gives a complete
  fiber of size at least `L`, not exactly `L`. The construction therefore
  selects an exact `L`-subfamily before applying the generic separating-pole
  theorem; the report makes no exact-total or complete-image claim.
- **Known support counterpackets.** Mersenne-31 T64 and small top-seam examples
  are support-profile obstructions without a KoalaBear received-line,
  tangent-survival, and final-slope certificate. They do not presently refute
  the named hypothesis.

No stronger self-refutation survived these checks. The pointwise shell
hypothesis remains genuinely open.

## 11. Nonclaims

This packet does not prove an unconditional `U_Q`, an A2 cap, a refund, a
balanced-core payment, a complement payment, `U_total<=B*`, or the first safe
agreement. It does not transport `422354730332`, union alternative
translations, count supports as slopes, or replace a uniform line maximum by
an average.

# OPEN GAP
