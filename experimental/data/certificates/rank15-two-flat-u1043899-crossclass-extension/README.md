# Rank-15 two-flat u=1,043,899 cross-class certificate

This packet verifies the field-uniform theorem

```text
D_2(u) <= 211 for u=1,043,899..1,043,957.
```

The exact new ownership is `u=1,043,899..1,043,901`. PR #865 already owns
`u=1,043,902..1,043,916`, and #847 owns `u=1,043,917..1,043,957`.

Run from the repository root:

```bash
python3 experimental/scripts/verify_rank15_u1043899_crossclass_extension.py
python3 -O experimental/scripts/verify_rank15_u1043899_crossclass_extension.py
python3 -m py_compile experimental/scripts/verify_rank15_u1043899_crossclass_extension.py
```

Both verifier modes must byte-match
`verify_rank15_u1043899_crossclass_extension.expected.txt`.

The verifier is standard-library only. It reconstructs the source reduction,
the inherited point-capacity cuts, the 139,979-type local cross-class cut,
the exact profile scans, the `u=1,043,898` wall, and dimensions 1 through 15
of the recurrence consumer without importing a pending-PR module.

Exact remaining wall:

```text
u=1,043,898: strengthened-relaxation surplus +1,918.
```

The new child entries save no rank-15 parent. No rank-16, Grand List, Grand
MCA, counterexample, or official-score claim is made.
