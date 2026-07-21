# M31 C9 full-prefix owner-refund floor

**Status:** `AUDIT / CONDITIONAL_ON_NAMED_INPUT`  
**Lane:** hard input 3, row-sharp exact-residual C9 max fiber  
**Outcome:** exact interface cut and deployed falsifier threshold; no RS counterexample is claimed.

## 1. Verdict

The C9 producer field mirrored from upstream PR #1020 is

```text
(fullPrefixFiber leaf syndromeKey).length
  <= compilerLoss * naturalScale.                         (FULL)
```

The v3 finite atom is instead the first-match residual family
`P_Q(z)` in `def:q-row-atom`, and `prob:row-sharp-q` requires its literal
remaining row allocation after earlier cells have been removed.  These are not
interchangeable in a row-sharp ledger without an owner refund.

For the deployed Mersenne-31 list calibration, the already printed `c=2048`
fixed-remainder floor is

```text
O_2048 = ceil(binomial(1023,544) / q_gen^32) = 6,796,405.
```

The row budget and the allowance remaining after that cell are

```text
B*                  = 16,777,215,
R_after_2048        = B* - O_2048 = 9,980,810.
```

If the `c=2048` family is assigned an earlier C1--C8 owner in the same prefix
key and `(FULL)` is instantiated at the remaining allowance `R_after_2048`,
then the exact owner partition forces

```text
|Residual_z| + O_2048 <= R_after_2048,
|Residual_z|          <= 3,184,405.                        (CUT)
```

Thus the exact falsifier for that instantiation is:

```text
|Owned_z|    >= 6,796,405,
|Residual_z| >= 3,184,406.                                (FALSIFIER)
```

Any key satisfying `(FALSIFIER)` makes the #1020 full-prefix field false at the
remaining row allocation.  Conversely, using the whole-row right-hand side
`B*` only gives a local C9 upper bound; appending a separate owner charge gives
the nonclosing upper total

```text
B* + O_2048 = 23,573,620 > B*.
```

This packet therefore does **not** refute row-sharp Q.  It proves that the
full-prefix field has a deployed owner-refund cost of `6,796,405` on this
calibration.  Closing the field requires either the stronger residual cap
`3,184,405`, a theorem showing the earlier floor is not co-located with the C9
key, or a ledger adapter that refunds the earlier-owned part instead of paying
it twice.

The named residual obligation is

```text
M31-C9-POST-C2048-OWNER-REFUND-RESIDUAL-3184405.
```

The named finite search target is

```text
M31-C9-POST-C2048-COLOCATED-RESIDUAL-3184406.
```

## 2. Exact objects and the standalone residual condition

Fix one prefix key `z`.  Let `Omega_{n,a+}` be the complete Boolean fixed-weight
slice.  The full prefix fiber and exact owner-complement residual are:

```text
x in Full_z
  <-> x in Omega_{n,a+} and prefix_w(x) = z,

x in Residual_z
  <-> x in Full_z and earlierOwner(x) = none.
```

The complementary earlier-owned family is

```text
Owned_z = {x in Full_z : earlierOwner(x) != none}.
```

Hence, with no asymptotics and no probability normalization,

```text
Full_z = Residual_z disjoint-union Owned_z,
|Full_z| = |Residual_z| + |Owned_z|.                       (PART)
```

This is the exact content formalized by
`SidonEffectiveImage.mem_residualOf_iff` and
`SidonEffectiveImage.residual_owned_length`.

A genuine `(SE2)` certificate remains separate.  It chooses one noncommon
support for each distinct slope, certifies the chosen list as a sublist of the
residual support projection, and yields

```text
number of distinct slopes
  <= number of selected residual supports
  <= |Residual_z|.
```

No support census is silently identified with the final slope numerator.

## 3. The inequality attacked

The exact #1020 field is retained verbatim at the cardinality level:

```text
|Full_z| <= compilerLoss * naturalScale.                  (C9-FULL)
```

The exact v3 atom is the pruned quantity from `def:q-row-atom`:

```text
R_Q^max = q_gen^w max_z |P_Q(z)| / binomial(n,a+),
max_z |P_Q(z)| <= allocated integer budget.               (Q-RES)
```

`prop:q-exact-target` prints the hypothetical whole-row M31-list target
`B*=16,777,215` and the full-slice average ceiling `1,993,678`.  The final
ledger `eq:mca-final-ledger` and `thm:exact-completion-certificate` explicitly
forbid giving every term the whole row budget: every non-Q first-match payment
reduces the Q allocation.

Combining `(PART)` with `(C9-FULL)` proves the exact owner-refund inequality

```text
|Residual_z| + ownerFloor <= compilerLoss * naturalScale,
```

whenever `ownerFloor <= |Owned_z|`.  This is
`SidonEffectiveImage.residual_plus_ownerFloor_le_budget`.

### Per-claim status

| Claim | Status | Exact content |
|---|---|---|
| Residual is the owner complement | `PROVED` | `x in Residual_z <-> x in Full_z and earlierOwner(x)=none` |
| Owner/residual cardinality partition | `PROVED` | `|Full_z|=|Residual_z|+|Owned_z|` |
| Genuine SE2 projection | `PROVED` as a finite interface | distinct slopes are bounded by selected residual supports |
| Generic owner-refund cut | `PROVED` | full bound plus `ownerFloor <= |Owned_z|` implies `|Residual_z|+ownerFloor <= budget` |
| M31 arithmetic | `PROVED` | `O_2048=6,796,405`, residual allowance `9,980,810`, full-field residual cap `3,184,405` |
| `c=2048` family is assigned by the final explicit C1--C8 `earlierOwner` at the same C9 key | `CONDITIONAL_ON_NAMED_INPUT` | semantic co-location/ownership theorem, not supplied here |
| An actual M31 residual has size at least `3,184,406` at that key | `CONJECTURAL_WITH_FALSIFIER` | exact falsifier is the two cardinality inequalities printed above |
| Row-sharp Q or the deployed safe row | **not claimed** | remains open |

## 4. Deployed M31 normalization, with denominators kept separate

The calibration uses four distinct roles.  None is silently substituted for
another.

```text
q_gen  = 2^31 - 1 = 2,147,483,647
         coefficient field for the prefix map and the denominator q_gen^w;

q_list = q_gen^4
         quartic list field used by the target budget;

q_line = NOT USED in this support max-fiber audit;
q_chal = NOT USED in this support max-fiber audit.
```

The list-row constants are

```text
n       = 2^21       = 2,097,152,
k       = 2^20       = 1,048,576,
a+      = 1,116,023,
w       = a+ - k     = 67,447,
B*      = floor(q_list / 2^100) = 16,777,215.
```

The full-slice average in `prop:q-exact-target` is

```text
barF_full = binomial(n,a+) / q_gen^w,
ceil(barF_full) = 1,993,678.
```

The `c=2048` quotient floor uses a different exponent and a different support
count:

```text
O_2048 = ceil(binomial(1023,544) / q_gen^32)
       = 6,796,405.
```

For any residual Fourier/MI+MA route, let `M_res` be the actual post-C1--C8
residual mass and `L_res` the realized residual prefix image.  The
image-normalized average is

```text
barF_res^img = M_res / L_res.
```

By `lem:image-ambient-moment-conversion`, replacing `L_res` by the ambient
`q_gen^w` costs the exact image-collapse factor.  Such a replacement is valid
only after the full-image certificate discussed in
`rem:flatness-certifies-image`.  This audit uses no MI/MA estimate, but records
the normalization because any successor proof of the named residual must use
it.

## 5. Exact M31 arithmetic

The fixed-remainder source proves

```text
ceil(binomial(1023,544) / q_gen^32) = 6,796,405.
```

The packet then checks:

```text
q_list                         = 21,267,647,892,944,572,736,998,860,269,687,930,881,
floor(q_list / 2^100)          = 16,777,215,
16,777,215 - 6,796,405         = 9,980,810,
9,980,810  - 6,796,405         = 3,184,405,
16,777,215 + 6,796,405         = 23,573,620,
3,184,406 + 6,796,405          = 9,980,811 > 9,980,810.
```

The exact certificate is
`experimental/data/certificates/m31-c9-full-prefix-owner-refund-floor/m31_c9_full_prefix_owner_refund_floor.json`.
The stdlib replay is
`experimental/scripts/verify_m31_c9_full_prefix_owner_refund_floor.py`.
Lean kernel-checks the downstream row-budget and owner-refund arithmetic from
the integrated floor value in
`experimental/lean/sidon_effective_image/SidonEffectiveImage.lean`.

## 6. Why this is not an RS counterexample

The floor `O_2048` is an exact support-family lower floor at the planted
`c=2048` condition.  This packet does not construct the final integrated
`earlierOwner` function on the deployed M31 support catalogue, and it does not
prove that a residual family of size `3,184,406` co-locates with that floor.
Therefore:

- `M31-C9-POST-C2048-COLOCATED-RESIDUAL-3184406` is a falsifier specification,
  not an exhibited support JSON;
- the theorem `m31_full_bound_fails_of_falsifier` is an implication from the two
  exact cardinality hypotheses, not a theorem that those hypotheses hold for
  the deployed row;
- `def:q-row-atom`, `prop:q-exact-target`, and `prob:row-sharp-q` remain open at
  the M31 list row.

This distinction is load-bearing.  The packet audits the producer/ledger
interface; it does not manufacture a synthetic Sidon claim or promote a
conditional co-location into a counterexample.

## 7. Successor routes

Exactly one of the following is needed for this C9 interface at the calibrated
key:

1. **Strong full-prefix route:** prove `|Full_z| <= 9,980,810`; the known owner
   floor then automatically forces `|Residual_z| <= 3,184,405`.
2. **Direct residual plus refund route:** prove the v3 residual inequality at
   its literal allocation and change the adapter so earlier-owned supports are
   not recharged through the C9 full-prefix budget.
3. **Disjointness route:** prove the `c=2048` floor cannot be co-located with the
   C9 residual key selected by the producer.
4. **Refutation route:** exhibit the two-line owner-complement residual and a
   genuine `(SE2)` support projection with the cardinalities in `(FALSIFIER)`.

A Sidon/Fourier or effective MI+MA proof is useful only if it proves one of these
literal cardinality statements at the image-normalized scale.

## 8. Source-label map

| Packet object | Proof authority |
|---|---|
| image-normalized primitive Q | `experimental/grande_finale.tex`, `def:primitive-q` |
| logarithmic moment/max-fiber interface | `experimental/grande_finale.tex`, `lem:logmoment-q` |
| ambient/image conversion | `experimental/grande_finale.tex`, `lem:image-ambient-moment-conversion` |
| full-image guard | `experimental/grande_finale.tex`, `rem:flatness-certifies-image` |
| exact finite residual Q atom | `experimental/grande_finale.tex`, `def:q-row-atom` |
| four deployed full-budget targets | `experimental/grande_finale.tex`, `prop:q-exact-target` |
| residual mass in moment proofs | `experimental/grande_finale.tex`, `prop:q-moment-order-floor` |
| summed first-match ledger | `experimental/grande_finale.tex`, `eq:mca-final-ledger` |
| no cell independently consumes the row budget | `experimental/grande_finale.tex`, `thm:exact-completion-certificate` |
| remaining row-sharp pruned target | `experimental/grande_finale.tex`, `prob:row-sharp-q` |
| normalized MCA/challenge denominator convention | `experimental/rs_mca_thresholds.tex`, `eq:intro-normalized-mca` |
| exact integer target convention | `experimental/rs_mca_thresholds.tex`, `eq:intro-asymptotic-threshold` |
| M31 `c=2048` floor | `experimental/notes/thresholds/20260709_m31_chebyshev_fixed_remainder_floor/cap25_v13_m31_chebyshev_fixed_remainder_floor.md` |

## 9. Nonclaims

This note does not prove:

- the #1020 full-prefix field for the deployed M31 row;
- a counterexample to that field on an actual RS support catalogue;
- the final semantic C1--C8 owner/co-location theorem;
- row-sharp Q, `U(1116023) <= B*`, or any deployed adjacent certificate;
- a Sidon, Fourier, MI, MA, RC, add-back, `UNIF`, or target-comparison theorem;
- any identification of `q_gen`, `q_line`, `q_chal`, and `q_list`.
