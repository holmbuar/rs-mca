# Dual-32 Complete Value Classification Certificate

The repository-facing summary is:

- `experimental/notes/l2/dual32_complete_value_classification.md`.

The frozen proof sources in this directory are:

- `DUAL32_TWENTY_COMPLETE_FIBERS_LACUNARY_REDUCTION.md`;
- `DUAL32_COMPLETE_VALUE_CLASSIFICATION.md`.

The first theorem proves that a deployed 32-valued polynomial phase has at
least twenty complete cyclotomic fibers and a lacunary normal form. The second
uses centered reverse-polynomial contact and differential rigidity to classify
every such phase as

```text
f(X)=aX^65536+b,  a!=0.
```

The two `HOSTILE_AUDIT_*.md` notes check the polynomial reductions
independently. The four
stdlib-only Ruby scripts under `experimental/scripts/` replay the deployed
integer gates and small cyclic regressions. Their combined canonical output is
stored in `verifier_output.txt`.

This packet does not bound the signed aggregate over phases with at least 33
values. It therefore does not prove the deployed Boolean-moment fiber ceiling,
Grand List, or either official prize question.
