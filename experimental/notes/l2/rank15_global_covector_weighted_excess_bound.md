# Rank-15 global-covector weighted excess bound

## Claim

Let `k` be algebraically closed of characteristic zero or characteristic
`p > max(B,q+1)`. Let a reduced arrangement of `B` projective lines be
preserved by a nonzero field

```text
X in H^0(P^2,T_{P^2}(q-1))
```

with isolated zero scheme. Suppose the nonzero line-extactic divisor factors
as

```text
Xi = lambda f g,    deg(f)=B,    deg(g)=a=3q-B,
```

where `f` is the reduced arrangement equation. If

```text
E=(q^2+q+1)-R,    S=E-U,
```

with `R` the number of distinct arrangement intersections and `U` the total
arrangement-line restriction deficit, then

```text
E+S=2E-U <= a(q+1).                                      (1)
```

No reducedness hypothesis is imposed on `g`.

## Status

**PROVED**, with a frozen proof object and three independent hostile audit
layers. The exact frozen theorem is

```text
experimental/data/certificates/rank15-global-covector-weighted-excess/
  RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS_BOUND.md
```

at SHA-256
`6f998929209b534d39cb0d31fa6458f5bf63d9326255ec31e7f0f64ae7a5389e`.

## Proof spine

1. Choose a generic affine covector `du` so that `h=X(u)` has degree `q+1`
   and shares no component with `fg`. Hence `(g,h)` is a complete
   intersection of total length `a(q+1)`.
2. At a field zero, write `X=P partial_u+Q partial_v`. The local extactic
   equation satisfies

   ```text
   K=P X(Q)-Q X(P)=F g,    K=-Q^2 P_v mod P,
   ```

   and therefore

   ```text
   i(P,g)=2mu+i(P,P_v)-i(P,F).
   ```
3. The local contribution `w` to `E+S=2E-U` is bounded by `i(P,g)`. At an
   ordinary `m`-fold arrangement point, the only extra input is
   `i(P,P_v)>=m-2`. A Saito-basis calculation gives
   `i(P,u)>=m-1`, and the tame Artin quotient gives
   `i(P,P_v)>=i(P,u)-1`.
4. Summing the local inequalities over field zeros and applying the complete
   intersection length proves (1).

The tame Artin-length argument is characteristic-safe under the printed
hypothesis; it does not invoke a characteristic-zero Milnor or Teissier
formula.

## Exact rank-15 impact

For the source-locked `M=213` cells, with deployed characteristic
`p=2130706433`, the independent compiler reconstructs the complete table:

| `(q,B,a)` | raw states | `E+S` range | cap `a(q+1)` | survivors |
|---|---:|---:|---:|---:|
| `(24,69,3)` | 12,607 | `86..120` | 75 | 0 |
| `(24,68,4)` | 16,027 | `96..132` | 100 | 919 |
| `(25,71,4)` | 225 | `95..107` | 104 | 215 |
| `(25,70,5)` | 350 | `106..119` | 130 | 350 |
| `(25,69,6)` | 559 | `117..132` | 156 | 559 |

Thus the residual cubic cell `(q,B,a)=(24,69,3)` closes with exact margin
`86-75=11`. Under this bound alone, the five-cell boundary falls from 29,768
states to 2,043 exact necessary states. Later independent refinements may
further reduce those four surviving cells.

## Verifier

Run from the certificate directory:

```bash
ruby --disable-gems -w verify_rank15_poschar_global_covector_weighted_excess_bound.rb
ruby --disable-gems -w verify_hostile_audit_rank15_poschar_global_covector_weighted_excess_bound.rb
ruby --disable-gems -w verify_hostile_audit4_source_quantifier_rank15_poschar_global_covector_weighted_excess.rb
ruby --disable-gems -w audit5_independent_weighted_source_compiler.rb
```

The last audit independently reconstructs all aggregate profiles and residual
partition states. It does not import, evaluate, or transform either claimant
driver, and it omits the claimant's Cauchy prefilter. Its exact row digests and
canonical output are frozen in the certificate directory.

## Consumers

This theorem pays the residual-cubic cell in the rank-15 `M=213` Grand List
boundary ledger. It supplies a characteristic-safe structural inequality that
can also be tested against later residual-degree cells without changing its
statement.

## Risk-limits

- Under this bound alone, the four degree-four, degree-five, and degree-six
  cells retain `919+215+350+559=2043` necessary states.
- This note proves no rank-16 payment and does not consume any unpublished
  recurrence.
- It does not close Grand List, change either official question, or change the
  official score from `0/2`.
- It does not edit or promote any stable paper theorem.
