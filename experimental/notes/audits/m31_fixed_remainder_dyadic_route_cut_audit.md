```yaml
workboard_item: M1
row: Mersenne-31 list at 2^-100
object: LIST
target_epsilon: 2^-100
agreement: 1116023
B_star: 16777215
direct_statement: "For every fixed-remainder dyadic Chebyshev complete-fiber family on the deployed domain, the post-C1 residual is empty at scales 2^1 through 2^17, while every remaining fixed-R prefix fiber has size at most 35."
architecture: GRANDE_FINALE_V3_EXACT_COMPLETION
partition_digest: null
atom_or_cell: C1_QUOTIENT_REMAINDER / M31_FIXED_REMAINDER_DYADIC_FOLD
quantifier: "for every 1<=s<=21 and every admissible fixed remainder R"
projection_and_unit: support fibers; no codeword projection claimed
claimed_bound: "0 after C1 for s<=17; at most 35 even pre-deletion for s>=18"
status: PROVED
impact: ROUTE_CUT
falsifier: "a fixed-R support at one enumerated dyadic scale that survives C1 and has more than the certified cap"
replay: "python3 experimental/scripts/verify_m31_fixed_remainder_dyadic_route_cut.py --check"
```

# Audit: M31 fixed-remainder dyadic fold route cut

## 1. Packet verdict and acceptance gate

```text
Activity: PROVE one named Lane-F route cut.
Acceptance path: named route-cut fallback.
Criterion 4 deployed witness: not found.
Route cut:
  M31_FIXED_REMAINDER_DYADIC_FOLD_ROUTE_CUT.
Residual named by the packet:
  M31_VARIABLE_REMAINDER_ORIENTATION_RESIDUAL.
Ledger movement: zero.
```

This packet is not an interface or adapter. It proves an exact family theorem at
the deployed row constants: all 21 dyadic Chebyshev fixed-remainder scales are
either assigned to the earlier C1 quotient/remainder owner or have exact
pre-deletion family cap at most `35`.

The row remains open because the family is not witness-exhaustive and no
support-to-codeword realization is claimed.

## 2. Base, branch, and overlap audit

| item | exact value |
|---|---|
| fork repository | `holmbuar/rs-mca` |
| pinned fork main | `4e5f0b77c98f075ea7c8822cd4859847a232bc2a` |
| pinned upstream main | `a3017697ad1594521d2779fe1d83bccd45d4c06e` |
| freshness | fork contains upstream main and is behind by zero commits |
| lane branch | `gptpro/m31-rowsharp-falsifier` |
| active row | Mersenne-31 list, target `2^-100`, agreement `1116023` |
| object/unit | support-fiber route cut; no codeword atom banked |

The latest upstream and fork draft PR descriptions were read before work began.
The open one-key M31 C9 packet and the open effective-dual-mass packet both use
other modules in the same future package. This branch imports neither module
and defines no declaration with their names. The root
`SidonEffectiveImage.lean` imports only
`SidonEffectiveImage.M31DyadicBlockRouteCut`; ship-side root composition remains
separate.

No file under `.github/` is modified. The full `experimental/agents-log.md` is
not read or changed.

## 3. Imported integrated API blob identity

Only one integrated package is imported. Its transitive integrated dependency
is also pinned.

| imported module | role | fork-main blob | upstream-main blob | result |
|---|---|---|---|---|
| `M31QRootedShell.Envelope` | transitive dependency of `Deployed` | `2bd4a5b051f482bfe222917e10d302b997a9c6ed` | `2bd4a5b051f482bfe222917e10d302b997a9c6ed` | byte-identical |
| `M31QRootedShell.Deployed` | `p`, `B*`, `w`, and list complement size | `7e21ff098567d26aba7330fbb2722d5cb952fb09` | `7e21ff098567d26aba7330fbb2722d5cb952fb09` | byte-identical |

No `AsymptoticSpine.*` module is imported. No open-PR module is imported.

## 4. Source authority and label map

| packet statement | proof authority |
|---|---|
| M31 list constants `p,n,k,a,M,w,B*` and average ceiling | `agents.md` M1; live four-row completion packet; `tex/cs25_cap_v13_2.tex` |
| `T_(2^s)` as a complete-fiber folding on the deployed Chebyshev root domain | `experimental/grande_finale.tex`, `def:structured-folding`, together with Chebyshev composition and the deployed norm-one parametrization |
| fixed-remainder family `S=phi^{-1}(E) disjoint_union R` | `def:quotient-remainder-profile` |
| `r<=w`: prefix fixes `R` and leaves exactly one quotient-prefix fiber | `thm:exact-quotient-remainder-normal-form`, QR2 |
| `w<r<c`: quotient set is prefix-invisible and the exact count is QR4 | `thm:exact-quotient-remainder-normal-form`, QR3--QR4 |
| boundary excluding arbitrary large remainders from the route cut | `prop:complete-support-factorization` |
| why C1 classification is not a primitive Q payment | `eq:profile-envelope`, `def:admissible-sequence`, and the ordered first-match contract |
| global scalar symmetry `lambda D=D` implies `lambda=+-1` | monic Chebyshev coefficient comparison in the threshold note |

The source theorem carries the explicit first-match hypothesis that declared
quotient/remainder profiles are assigned to C1. The Lean table does not infer
that architecture choice from arithmetic.

## 5. Exact deployed arithmetic

The verifier recomputes

```text
p = 2147483647
n = 2097152
k = 1048576
a = 1116023
M = 981129
w = 67447
B* = 16777215
floor(choose(n,M)/p^w) = 1993677
ceil (choose(n,M)/p^w) = 1993678
floor(B* / (choose(n,M)/p^w)) = 8
```

For `c=2^s`, `1<=s<=21`, it recomputes all exact values

```text
N_s = n/c
q_s = M div c
r_s = M mod c.
```

The split is exact:

```text
s=1..17:
  r_s <= w and q_s > 0;
  route = C1 quotient/remainder;
  post-C1 cap recorded by this family = 0.

s=18..21:
  w < r_s < c;
  fixed-R cap <= choose(N_s-1,q_s) = 35,3,1,1.
```

The maximum surviving/pre-deletion cap in the named family is therefore `35`,
which is below both one full-slice average ceiling and the official budget.

## 6. Exact PROVED declaration table

All declarations are in
`SidonEffectiveImage.M31DyadicBlockRouteCut`.

| Lean declaration | exact proved statement | source correspondence |
|---|---|---|
| `deployed_dimensions` | imported M31 prime, budget, prefix depth, list complement size, domain size, and average ceiling equal the printed integers | deployed row ledger |
| `all_scale_rows_checked` | every one of the 21 frozen rows satisfies its exact division, remainder, route, and late-cap checks | full dyadic census |
| `postC1_caps_exact` | exact 21-entry cap vector: seventeen zeros followed by `35,3,1,1` | C1/late split |
| `late_rows_exact` | the only late rows are exponents `18,19,20,21` with all printed integers | QR4 range |
| `late_caps_exact` | late cap list is exactly `[35,3,1,1]` | `choose(N-1,q)` |
| `postC1_cap_max` | maximum named-family cap is exactly `35` | finite maximum |
| `postC1_cap_below_average` | `35 < 1993678` | margin comparison |
| `postC1_cap_below_budget` | `35 < 16777215` | official budget comparison |
| `deployed_margin_bracket` | `8*1993678 <= B* < 9*1993678` | integer form of the `8.4152...` calibration |
| `antipodal_and_t4_are_c1_scales` | the `c=2` and `c=4` rows occur in the census and satisfy the visible-remainder C1 predicate | antipodal and `T_4` mechanisms |
| `named_route_cut_arithmetic` | conjunction of the all-row check, exact max `35`, and both margin comparisons | source theorem arithmetic payload |

The module contains no theorem asserting a received-word list count, actual
`U_Q`, profile exhaustion, or row closure.

## 7. Statement correspondence audit

### 7.1 What Lean proves

Lean proves the frozen finite arithmetic and executable row classification
predicate. The source note proves that:

1. each `T_(2^s)` restriction is a complete-fiber folding;
2. QR2 maps the first seventeen rows to declared C1 quotient/remainder
   profiles;
3. QR4 gives the exact late fixed-remainder count;
4. the global scalar-domain automorphism class reduces to `+-1`.

The compiled theorem `named_route_cut_arithmetic` matches exactly the integer
premise consumed by that source proof.

### 7.2 What Lean deliberately does not prove

Lean does not formalize Chebyshev polynomials, the norm-one parameterization,
the full first-match owner function, or codeword realization. Those are not
hidden axioms: they are source-level statements or explicit nonclaims. No Lean
declaration upgrades them to a row theorem.

## 8. Explicit nonclaims

- No deployed M31 list-row counterexample is constructed.
- No exact `U_Q`, `U_list_int`, or `U_new` is supplied.
- No arbitrary varying-remainder partial-occupancy family is bounded.
- No antipodal-transversal orientation fiber is bounded.
- No isolated multiplicative coset in a proper subset of the domain is
  classified.
- No support fiber is automatically converted into codewords.
- No received-word maximum, list-interior projection, add-back, owner census,
  or line/word-uniform sum is proved.
- No deployed ledger term moves.
- No adjacent row is closed.
- No result from an open PR is imported or assumed.

## 9. Certificate and replay

Certificate:

```text
experimental/data/certificates/m31-fixed-remainder-dyadic-route-cut/
  m31_fixed_remainder_dyadic_route_cut.json
```

Verifier:

```text
experimental/scripts/verify_m31_fixed_remainder_dyadic_route_cut.py
```

Replay:

```text
python3 experimental/scripts/verify_m31_fixed_remainder_dyadic_route_cut.py --check
python3 -O experimental/scripts/verify_m31_fixed_remainder_dyadic_route_cut.py --check
python3 experimental/scripts/verify_m31_fixed_remainder_dyadic_route_cut.py --tamper-selftest
```

The checker is Python standard-library only. It recomputes the exact large
binomial quotient and rejects six rehashed semantic mutations.

## 10. Lean and CI census

```text
Lean version: 4.31.0
Mathlib imports: 0
native_decide: 0
sorry: 0
admit: 0
custom axioms: 0
unsafe declarations: 0
```

Imported API comparison is recorded in Section 3.

```text
Fork draft PR: AWAITING_CREATION
Candidate head: AWAITING_CREATION
Authoritative Lean run: AWAITING_FORK_CI
Axiom output: AWAITING_FORK_CI
Final validation state: AWAITING_FORK_CI
```

The audit will be updated with the authoritative fork run after the complete
candidate packet is pushed. No local Lean build is used.

## 11. Remaining exact obligation

The named successor is:

```text
M31_VARIABLE_REMAINDER_ORIENTATION_RESIDUAL
```

It asks for a direct fixed-residual maximum, a statement-changing
counterexample, or another genuine route cut for families in which the
remainder varies, the support is an antipodal transversal, or the multiplicative
structure is local rather than a global scalar action.

# OPEN GAP
