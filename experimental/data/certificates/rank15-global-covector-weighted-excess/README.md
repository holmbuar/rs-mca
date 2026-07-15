# Rank-15 global-covector weighted excess certificate

This directory preserves the frozen theorem, proof dependency, three hostile
audit layers, exact source drivers, and canonical compiler outputs for

```text
E+S <= (3q-B)(q+1).
```

The accepted source impact is narrow: the `(q,B)=(24,69)` cubic cell has
12,607 source states, minimum weight 86, and cap 75, so it has no survivors.
The other four cells retain 2,043 exact necessary states in total.

Run all four gates from this directory:

```bash
ruby --disable-gems -w verify_rank15_poschar_global_covector_weighted_excess_bound.rb
ruby --disable-gems -w verify_hostile_audit_rank15_poschar_global_covector_weighted_excess_bound.rb
ruby --disable-gems -w verify_hostile_audit4_source_quantifier_rank15_poschar_global_covector_weighted_excess.rb
ruby --disable-gems -w audit5_independent_weighted_source_compiler.rb
```

The fourth command is the slow independent compiler replay. It reconstructs
2,163,789 residual reachable keys and compares complete row digests for every
one of the five cells.

The frozen theorem calls itself a "theorem candidate" because acceptance is
deliberately external to that immutable object. The hostile audit files and
the repository-facing note record the accepted status.

No file in this directory claims a recurrence payment, rank-16 payment, Grand
List closure, or official-score change.
