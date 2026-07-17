# Rank-15 two-flat u=1,043,902 four-cut certificate

This packet verifies the field-uniform, fixed-parameter theorem

```text
D_2(u) <= 211 for u=1,043,902..1,043,957.
```

Integrated PR #847 already owns `u=1,043,917..1,043,957`; the new ownership
is exactly the 15 states `u=1,043,902..1,043,916`.

Run from the repository root with a Python 3 runtime:

```bash
python3 experimental/scripts/verify_rank15_two_flat_u1043902_four_cut_extension.py
python3 -O experimental/scripts/verify_rank15_two_flat_u1043902_four_cut_extension.py
python3 experimental/scripts/verify_rank15_two_flat_u1043902_four_cut_extension.py --tamper-selftest
python3 -m py_compile experimental/scripts/verify_rank15_two_flat_u1043902_four_cut_extension.py
```

Verify packet hashes from this directory:

```bash
shasum -a 256 -c SHA256SUMS.txt
```

The verifier is standard-library only.  It reconstructs the inherited #847
optimizer, proves the four new point-capacity cuts by exact knapsack DP,
runs the 6,597,135-branch strengthened optimizer, checks the `u=1,043,901`
degree wall, and replays the parent recurrence as a fresh independent
implementation.

Exact remaining wall:

```text
u=1,043,901: relaxed margin +1,707;
any literal source counterexample requires d=4,674, deg G=0, r=0.
```

The 15 child improvements are swallowed by the existing recurrence suffix:
dimensions 3 through 15 are unchanged, the rank-15 value remains
`283,039,300,733,528,044`, and the target gap remains
`8,185,190,237,340,452`.  No rank-16, Grand List, Grand MCA, or official-score
claim is made.
