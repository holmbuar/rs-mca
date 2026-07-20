# Sparse exact-deep counterexample to universal O5c strict crossing

## Statement

Freeze `epsilon*=2^-128`. For every integer `m>=129`, let

```text
F_m = GF(2^m),        D_m = F_m^*,        Gamma_m = F_m,
n_m = 2^m-1,          k_m = 2^(m-1)-1,    a_m = n_m-1,
B_m^* = floor(epsilon* |Gamma_m|) = 2^(m-128).
```

For `C_m=RS_Fm(D_m,k_m)`, the exact challenge-restricted MCA numerator is

```text
B_Cm,Gamma_m^MCA(a_m) = 2.
```

Hence at `m=129` the actual numerator and target are both two. The literal
universal Role-12 demand that a complete valid lower reserve be strictly
greater than `B_m^*` is false. For every `m>129`, the same numerator is
strictly below the target. This is a sparse occurring-length family
`n_m=2^m-1`, not a claim at every integer length.

## Source chain

The target is fixed before the family, profiles, received line, or remainder
class. The full challenge field is used and no scalar extension, subfield
postselection, or postselected challenge occurs.

At `m=129`, use the concrete presentation

```text
F_2[T]/(T^129+T^5+1).
```

Rabin's criterion proves the polynomial irreducible: the degree-129 Frobenius
condition holds, and the two proper tests corresponding to the prime divisors
`3` and `43` have gcd one. For later `m`, only the abstract finite field
`GF(2^m)` is used; no compatible quotient presentation is claimed.

The source's exact-deep theorem applies because

```text
3(n_m-a_m)=3 <= n_m-k_m=2^(m-1).
```

Together with the universal tangent floor, it gives

```text
B_Cm,Gamma_m^MCA(a_m)=min(|Gamma_m|,n_m-a_m+1)=2.
```

There is also a literal sharp line. Choose `theta` in `F_m\{0,1}` and set

```text
r_0=e_theta,              r_1=e_1+e_theta.
```

Slopes zero and one are explained by the zero codeword on the omitted-point
supports `D_m\{theta}` and `D_m\{1}`. For every other slope the line word has
weight two. Any codeword explaining it on `n_m-1` coordinates would have
weight at most three, contradicting the RS minimum distance
`n_m-k_m+1=2^(m-1)+1`. Thus the bad-slope set is exactly `{0,1}`.

For the adjacent dimension-`k_m+1` code, two distinct listed codewords that
both agree with one received word on at least `a_m` coordinates would agree
with each other on at least `2a_m-n_m>k_m` coordinates. Their difference has
degree at most `k_m`, a contradiction. Every source-valid profile list under
that common-code/common-received-word premise therefore has size at most one.

The collision-aware source formula is

```text
M(L)=ceil(L(q-n)/(q-n+k(L-1))).
```

Only `L=1` is consumed, so `M(1)=1` and the full-field challenge profile floor
is one. No reciprocal `L>1` formula is asserted. The tangent reserve is two,
and the source-valid combination is their maximum, not their sum.

## Admissibility

- `A1`: `D_m=F_m^*` is a multiplicative coset. Every power map indexed by a
  divisor of `n_m` has complete uniform fibers.
- `A2`: the `n_m` omitted-point supports form a deterministic first-match
  atlas. Exact-agreement reduction makes it witness-exhaustive; each support
  contributes at most one distinct slope. Since `log n_m=o(n_m)`, the atlas
  has `e^{o(n_m)}` cells and cost.
- `A3-A6`: no primitive or residual leaf remains after this complete exact
  support atlas. Those obligations are vacuous rather than silently assumed.
- `A7`: the full source profile envelope is retained. It is not replaced by
  the identity term; every applicable profile list is bounded by the adjacent
  list-collapse argument, and in any event no valid floor can exceed the exact
  numerator two.

Support overlap is allowed. The two explicit owner supports overlap in
`n_m-2` points, while their first-match slope sets are disjoint.

## Replay status

The upstream PR supplied a Python verifier/certificate packet that pins the
theorem source, reconstructs the concrete field, checks the endpoint and
`m=129..512`, and rejects twelve semantic mutations.  This curated integration
keeps the mathematical counterexample note but intentionally does not import
the Python replay packet.

## Remaining wall and nonclaims

This counterexample refutes only the literal universal O5c strict-crossing
demand assigned to R32 Role 12. It does not refute the exact-deep theorem; it
uses it. It does not establish Grand MCA, Grand List, a complete general
profile-envelope theorem, an intermediate O7 payment, a closed parent ledger,
or an official score increment. It modifies no deployed row and pays no finite
or asymptotic ledger delta. Official score remains `0/2`.

The remaining theorem-facing task is to replace the false universal strict
crossing with a target-viable formulation that excludes exact-deep rows whose
actual numerator is already at or below the frozen target, then prove the full
profile comparison on the surviving regime.
