# Audit 5: independent weighted-excess source/compiler replay

## Verdict

```text
PASS
```

I independently reconstructed the five-cell `M=213` source census and the
weighted compiler inequality.  The frozen theorem's impact table is exact:
all five raw counts, all five `W` ranges, all five caps, and all five survivor
counts agree.  In particular, the necessary inequality

```text
W=E+S=U+2S <= (3q-B)(q+1)
```

deletes every one of the `12,607` states in `(q,B)=(24,69)`; its least
violation is `86-75=11`.  It does not delete all states in any of the other
four cells.

This is a source/compiler audit.  It neither substitutes for nor weakens the
separate geometric hostile audits of the weighted extactic theorem.

## Frozen inputs

The replay refuses to run unless all of these bytes match:

```text
RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS_BOUND.md
  6f998929209b534d39cb0d31fa6458f5bf63d9326255ec31e7f0f64ae7a5389e

explore_rank15_m213_covector_weight_impact.rb
  099fab039f0812b9aeb5dce7acdcdc588f43520074ef1ae358a6d6fcfe0e5be2

explore_rank15_m213_exact_localcost_driver.rb
  8cfcf7475dd153e5e101e0c97467d7d49b0336f902e806ce673dee13f8de533b

verify_rank15_m215_q15_line_residue_exclusion.rb
  f8cfba142607caccb5eb05ad261919f48697fd8a03b542fd65760075057eda1c

verify_rank15_m216_camacho_sad_line.rb
  b1161c3563eea5e7dfb4c6522c8139c419ad5ec0a2e1bec5c63bc1e4df64e686
```

The claimant driver is byte-hashed only.  The independent verifier does not
load, require, eval, parse, or text-transform it.  It likewise does not load,
require, eval, parse, or text-transform
`audit_global_covector_weighted_excess_minima.rb`.

## Independent reconstruction

Set `M=213`.  For one cell `(q,B)`, let

```text
D=15(M-B).
```

The marked-coordinate aggregate is reconstructed as a deficiency partition
of `D` into `M` entries from `0,...,15`.  Counts of deficiencies `14` and `15`
are retained explicitly as `n14,n15`; deficiencies `1,...,13` are generated
by an exact unbounded moment knapsack.  For each total and square sum the
knapsack stores the least number of nonzero coordinates.  This loses no
profile because all unused coordinates are zeros and the only coordinate
constraint is an upper bound.

Writing `V` for the deficiency square sum, the source quantities are then
reconstructed directly as

```text
marked_pairs = 105M-14D+(V-D)/2,
P            = C(B,2)-marked_pairs,
marked_tau   = 196M-28D+V-n15,
Rcap         = q^2+q+1-(M-n14-n15),
Icap         = B(q-14)+n14.
```

For every aggregate with `P>=0`, the verifier generates every reachable
residual ordinary-multiple-point pair `(R,I)`.  A residual point of
multiplicity `m>=2` contributes

```text
(C(m,2),1,m)
```

to `(P,R,I)`.  The generation is unbounded in the number of points of each
multiplicity and uses a set of exact `(R,I)` keys.  It does not keep only a
componentwise maximum.

For each exact reachable state within `Rcap,Icap`, the verifier computes

```text
J = I-R,
S = dpw(B,q)-marked_tau-[2P-J],
U = Icap-I,
E = U+S.
```

Only `S>=0` rows survive the source DPW gate.  Every surviving row is checked
against the independent support identity

```text
E=Rcap-R,
```

and against both weighted formulas

```text
W=E+S=U+2S.
```

Finally, with `a=3q-B`, a row survives the new theorem precisely when

```text
W<=a(q+1).
```

## Quantifier and deduplication guards

The most dangerous compiler failure modes were tested explicitly.

1. **No source Cauchy prefilter.**  The audit deliberately omits the generic
   driver's residual `tau` relaxation.  It begins with every moment profile
   having `P>=0` and then applies exact residual reachability.  Therefore a
   sign, range, or monotonicity bug in that prefilter cannot remove a row from
   this replay.
2. **Unbounded-copy semantics.**  A separate non-DP recursion agrees with the
   residual reachability table for every `P=0,...,40` after restriction to
   `R<=8,I<=20`.  This catches accidental 0/1 use of a multiplicity and
   accidental ordering multiplicities as distinct partitions.
3. **Marked-coordinate semantics.**  The regressions `5+1+1` and `13+13`
   check both unbounded use of a deficiency and minimum-coordinate retention.
4. **No silent row collapse.**  Each row is represented by the full tuple
   `(V,n14,n15,P,R,I,S,U,E,W)`.  For every cell, the number of loop iterations
   equals the cardinality of the full-tuple set.  Hence the displayed raw
   counts contain neither order copies nor a hidden post hoc dedup collision.
5. **Exact fixed range.**  The verifier scans exactly
   `q24/B69`, `q24/B68`, `q25/B71`, `q25/B70`, and `q25/B69`, with `M=213` in
   every source formula.  It does not widen a successful cell claim to other
   `q,B` values.

The prefilter-free aggregate dimensions are

```text
Pmax=355, Rcap_max=474, Icap_max=816,
2,163,789 residual reachable keys.
```

The large aggregate-profile counts printed by the verifier are expected:
they are counts before the omitted safe Cauchy prefilter.  The final exact
row counts agree with the source-locked claims.

## Exact results

| `(q,B,a)` | prefilter-free profiles | raw rows | `W` range | cap | survivors |
|---|---:|---:|---:|---:|---:|
| `(24,69,3)` | 60,358 | 12,607 | `86..120` | 75 | 0 |
| `(24,68,4)` | 63,110 | 16,027 | `96..132` | 100 | 919 |
| `(25,71,4)` | 55,566 | 225 | `95..107` | 104 | 215 |
| `(25,70,5)` | 57,799 | 350 | `106..119` | 130 | 350 |
| `(25,69,6)` | 60,358 | 559 | `117..132` | 156 | 559 |

Canonical sorted full-row digests are:

```text
q24/B69  ff6883869b7126bceea37a3cbd8c3485c9760c9309e6608d924b2c7935c2e80f
q24/B68  9f9111574caa017e99cad1a7d6064738dd859dcfe778ff9bebf602ef2b0ea16b
q25/B71  b9073791b5899d8a3c1160dad592b4184519e522ee18d62495e0542140502599
q25/B70  2de1e48f507995fb5077c5c917f70d9f877e39014bb6464d14def7300b3303b3
q25/B69  3905a9b69ab4badfc2e22d454faea3509f647900bb5b8789cbc44353d017fbfa
```

## Replay artifacts

```text
audit5_independent_weighted_source_compiler.rb
  bd3dfd13aacda58d78de44398826e6db6cf2000d538406b5c5e5745470bc1f89

audit5_independent_weighted_source_compiler.expected.txt
  9444c6c213908f178473dd19f7420b0b8a2e43fa6552134c1454f3d895e2244a
```

Replay with:

```bash
ruby audit5_independent_weighted_source_compiler.rb \
  > /tmp/audit5_independent_weighted_source_compiler.actual.txt
cmp -s /tmp/audit5_independent_weighted_source_compiler.actual.txt \
  audit5_independent_weighted_source_compiler.expected.txt
```

The default replay performs all source-hash checks, all exact-state checks,
all full-row digest checks, and all claimed-impact checks before printing
`PASS`.

## Exact claim layer

The source/compiler verdict is:

```text
(q,B,a)=(24,69,3): 12,607 -> 0, exact closure.
(q,B,a)=(24,68,4): 16,027 -> 919, not closed.
(q,B,a)=(25,71,4): 225 -> 215, not closed.
(q,B,a)=(25,70,5): 350 -> 350, no deletion.
(q,B,a)=(25,69,6): 559 -> 559, no deletion.
```

No range widening and no full-`M=213` closure is claimed.
