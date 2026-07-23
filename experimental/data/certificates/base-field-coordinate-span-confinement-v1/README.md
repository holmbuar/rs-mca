# Base-field coordinate-span confinement v1

This certificate binds the local RS-MCA syndrome-line theorem in
`experimental/notes/thresholds/base_field_coordinate_span_confinement.md`
to source commit `fb6d9555339b43911c59c498373c43ed6c5cd391`, the repaired
R42 Role 13 artifact, and its independent hostile audit.

The fail-closed verifier checks:

- the source, note, author-repair, and audit bindings;
- exact KoalaBear arithmetic and the maximal conditional radial threshold;
- all base-field coordinate-span ratio sets for nonzero pairs in
  \(\mathbb F_9^2\);
- the unique bad zero combination for every nonzero dependent pair in that
  model;
- exhaustive radial factorization over \(\mathbb F_3,\mathbb F_5,\mathbb
  F_7\);
- six theorem-boundary and provenance tampers.

Run:

```bash
python3 experimental/scripts/verify_base_field_coordinate_span_confinement.py --check
python3 -O experimental/scripts/verify_base_field_coordinate_span_confinement.py --check
python3 experimental/scripts/verify_base_field_coordinate_span_confinement.py --tamper-selftest
python3 -O experimental/scripts/verify_base_field_coordinate_span_confinement.py --tamper-selftest
```

The finite-field checks are falsification guards, not a proof by exhaustion.
The symbolic proof is in the note. The packet proves no KoalaBear row,
uniform radial occupancy bound, ledger payment, endpoint, or score movement.
