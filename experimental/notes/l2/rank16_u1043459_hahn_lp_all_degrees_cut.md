# Complete finite Hahn LP cut at `u=1,043,459`

## Verdict

`EXACT ALL-DEGREE ROUTE CUT; STATE NOT PAID.`

At the fixed deployed one-row state `u=1,043,459`, selected agreement supports
have the Johnson-scheme parameters

```text
N=1,053,693,  a=72,588,  h=5,116,  d=a-h=67,472,
allowed distances i=67,472,...,72,588.                  (1)
```

The degree-six primal and its six-point dual reconstructed by
`experimental/scripts/verify_rank16_u1043459_hahn_lp_degree32_cut.rb` remain
exactly optimal after every remaining Hahn degree is admitted.  Since the
Johnson scheme has degrees
`0,...,min(a,N-a)=72,588`, this exhausts the entire finite Delsarte LP:

```text
floor L_Hahn^(all)(1,043,459)
 =600,370,193,369,924,883
 >274,854,110,496,187,592=T,

excess over T=325,516,082,873,737,291.                  (2)
```

Thus no ordinary constant-weight Hahn/Delsarte polynomial, of any degree,
pays the literal target at this state.  A successful continuation must use
structure absent from the distance distribution, such as the fixed syndrome,
the actual polynomial fibers, or a genuinely stronger semidefinite object.

## Source-specific incidence refinement

The exact payment at the child state `u+1=1,043,460` gives the section cap

```text
B=41,358,983,685,320,209.
```

Every candidate at `u=1,043,459` has at least `a=72,588` residual agreements
among `N=1,053,693` coordinates.  Incidence double counting therefore sharpens
the source-specific list ceiling by six:

```text
L <= floor(N B/a)
  =600,370,193,369,924,877,
L-T=325,516,082,873,737,285.                            (3)
```

This refinement is stronger than the bare all-degree LP optimum but remains
above target.  The companion value-fiber countermodel shows that adding the
aggregate agreement/error buckets and pair/cubic moment budgets still does
not close (3).

## Exact prefix

The positive dual measure is supported at

```text
67,472, 67,586, 67,587, 67,700, 67,701, 72,588.         (4)
```

It is tight in degrees `1,...,6`.  An exact three-term Hahn recurrence builds
all six normalized kernels through degree 644.  The verifier cross-checks
that recurrence against the direct terminating hypergeometric sum through
degree 32, then evaluates every reduced cost in degrees `7,...,644` over
Ruby `Rational`.  All are strictly positive.  The unique minimum occurs at
degree 7 and equals

```text
9752283143316102495459108899220020646974327983817317640625151502514401128092695
--------------------------------------------------------------------------------
11523578579538907033081341732618169726529902799883520612323112861257031150780806
```

which is approximately `0.8462894643363746`.

## Exact orthogonality tail

Let `H_j(i)` denote the normalized Johnson zonal function, let

```text
v_i = C(a,i) C(N-a,i),
|X| = C(N,a),
m_j = C(N,j)-C(N,j-1),
```

and let `y_i>0` be the six dual weights supported at the distances in (4).
Johnson orthogonality gives

```text
sum_i v_i H_j(i)^2 = |X|/m_j.                           (5)
```

Weighted Cauchy therefore gives the exact certificate

```text
|sum_i y_i H_j(i)|^2
 <= (sum_i y_i^2/v_i) |X|/m_j.                          (6)
```

At `j=645`, the Cauchy bound on the right side of (6), including the weighted
mass factor `sum_i y_i^2/v_i`, is strictly less than one.  The verifier clears
all denominators and compares the two resulting positive integers.
The positive integer margin has 427,549 bits and SHA-256

```text
89f9c80bd92e06db28d19a9ce398a11ad9abec6d0d428454a4611719c4b8d417.
```

Moreover `m_j` is strictly increasing for every
`j=645,...,72,588`.  This follows from the exact ratio

```text
m_(j+1)/m_j
 = (N-2j-1)(N-j+1) / ((j+1)(N-2j+1)) > 1.              (7)
```

Consequently the Cauchy bound in (6) stays strictly below one throughout the
tail.  Since the dual reduced cost is `1+sum_i y_i H_j(i)`, every degree
`645,...,72,588` has strictly positive reduced cost.  Together with the exact
prefix, this proves full dual feasibility and hence (2).

## Scope ledger

- Field ledger: the list is over `F_p`, while `T` retains the downstream
  challenge denominator `p^6`; after selected supports are formed, this
  certificate is a field-free integer Johnson-scheme calculation.
- Quantifiers: all 5,117 allowed distances were checked by the hash-locked
  degree-six primal certificate; all 72,582 added degrees were checked either
  exactly in the prefix or uniformly by (5)-(6).
- Source dependence: this uses only the already-audited support selection and
  pairwise intersection cap at `u=1,043,459`.
- Source pin: derived at `origin/main`
  `9262f63cf093a7510a2df435f220390f59e2bcd5`, then rebased and replayed at
  `c35a6da31ed0905afcbaaefe4eb0f242572ebb35`.  The consumed source note has
  unchanged blob SHA `90be3164bc9a31d86374d5c0e2d3659968494e47`; no pending PR is consumed.
- Nonclaim: it does not pay the state, improve the official score, analyze a
  Terwilliger SDP, or exploit the fixed received-word syndrome.

## Replay

```text
ruby --disable-gems -w experimental/scripts/verify_rank16_u1043459_hahn_lp_degree32_cut.rb
ruby --disable-gems -w experimental/scripts/verify_rank16_u1043459_hahn_lp_all_degrees.rb
```

Expected verifier SHA-256:

```text
398003ef12e924d0b52bb33542844292d5d2d7f15c22e7ede61330418dde7b17
```

The verifier hash-locks the exact all-distance degree-six primal source at

```text
ed0bda120c8a42eda7aa1c44f9e17101402daf017b12126d69e598fc72d0890f.
```

Canonical outputs are frozen under
`experimental/data/certificates/rank16-u1043459-hahn-all-degrees-cut/`.
