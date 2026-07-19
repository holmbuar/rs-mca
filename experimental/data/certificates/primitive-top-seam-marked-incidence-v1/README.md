# primitive-top-seam-marked-incidence-v1

Status: `PROVED_LOCAL / AUDIT / OPEN_GAP`.

This packet verifies the complete marked top-seam object `(G,A,B)` with
`A-B=c!=0`, reproduces the `F_17^*` multiple-mate counterpacket, measures the
exact loss from deleting `G`, records a fixed-target multiple-core packet, and
tests the separate support/explanation/ray/slope projections.

For the known `F_17^*` target fibre it records both the four-mate rooted star
and the complete top seam: `32` ordered marked triples, `7` explanation states,
`7` witness rays, and `4` MCA slopes.  The rooted star is retained only as a
multiple-mate/projection regression and is not substituted for the complete
numerator.

Replay:

```text
python3 experimental/scripts/verify_primitive_top_seam_marked_incidence_v1.py --check
python3 experimental/scripts/verify_primitive_top_seam_marked_incidence_v1.py --tamper-selftest
```

The classifier is fail-closed.  Periodic-support and root-set affine-transport
candidates are tested before primitive admission but are not called actual
owners without rooted descent and a slope budget.  The raw common-core prefix
fibre is not mislabeled as an affine owner, arbitrary distinct cores are not
mislabeled as planted, and missing actual-slope context is not admitted to the
primitive residual.

Exact nonclaim: this is not a proof or counterexample for the fully pruned
asymptotic primitive shift-pair ledger and not a deployed adjacent-row
certificate.
