# Rank-15 M214 active-deletion certificate

This directory is the replay bundle for
`experimental/notes/l2/rank15_m214_b149_full_active_deletion_nonexistence.md`.

Run:

```text
/Users/danielcabezas/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node \
  verify_m214_b149_full_active_deletion_nonexistence.js
```

The primary verifier source-pins an independently implemented M215 arithmetic
engine, changes only the theorem domain and frozen ledgers, and checks the
complete M214 scan against the adjacent expected output. The M215 files are
included only as frozen verifier dependencies; this packet does not claim to
publish the M215 theorem.

The exact M214 result is:

```text
field characteristic 0 or >214
149 <= marked points <= active lines <= 214
every marked point exactly 15-fold
every active line contains a marked point
=> no such projective line arrangement exists
```

The verifier covers 2,411,034,031 relaxed joint states, the design and
order-13 equality-plane branches, every deletion terminal, the Cauchy moment
ledger, and the final `16=1` residue contradiction.

Nonclaims: this is not a rank-15 recurrence theorem, does not pay rank >=16,
does not close Grand List, and does not move the official score.
