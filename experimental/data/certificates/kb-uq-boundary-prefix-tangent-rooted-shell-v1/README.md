# KoalaBear boundary-prefix Q conditional certificate

This directory certifies the exact finite arithmetic and source bindings for
`experimental/notes/frontier-adjacent/kb_uq_boundary_prefix_tangent_rooted_shell_v1.md`.

`round1_row_manifest.json` is the byte-exact canonical row manifest from upstream PR #1049; its Git blob SHA is `15731acc39a4cc38d8175fd09535b149490f8551`, and the verifier recomputes its partition digest.

The mathematical output is conditional on the single pointwise finite residual
hypothesis `KB_TANGENT_ROOTED_Q_SHELL(3,7)`:

```text
p^67471 * max(d_e - 3, 0)
  <= 7 * C(1116048,e) * C(981104,e)
```

on the canonical branch-dependent shell table of the actual post-tangent
`ACTIVE_V4_BOUNDARY_PREFIX_Q` cell.

The resulting uniform integer is

```text
U_Q = 400389155870
remaining reserve after U_paid'=981104 = 274980327721258113
```

The non-column-far branch uses the tangent deletion to remove shells
`0..67472` and has the smaller subcap `400388953453`.  The column-far branch is
binding.

Replay from the repository root:

```text
python3 experimental/scripts/verify_kb_uq_boundary_prefix_tangent_rooted_shell_v1.py --check
python3 -O experimental/scripts/verify_kb_uq_boundary_prefix_tangent_rooted_shell_v1.py --check
python3 experimental/scripts/verify_kb_uq_boundary_prefix_tangent_rooted_shell_v1.py --tamper-selftest
```

`hashes.json` is retained as upstream PR-bundle provenance; it includes
transport-only files not stored in this repository.  The local verifier checks
the retained text, manifest, row manifest, and giant binomial arithmetic by two
independent routes.  Lean validation is stdlib-only and is performed by fork CI;
no local Lean build is authoritative.

This is not an unconditional Q theorem, refund, row refutation, balanced-core
payment, complement payment, or adjacent safe-row certificate.
