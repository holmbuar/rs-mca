# Rank-15 `M=212` preserve-all deletion-floor certificate

This packet supports
`experimental/notes/l2/rank15_m212_preserve_all_deletion_floor.md`.

Run:

```text
python3 experimental/scripts/verify_rank15_m212_preserve_all_deletion_floor.py
python3 -O experimental/scripts/verify_rank15_m212_preserve_all_deletion_floor.py
python3 experimental/scripts/verify_rank15_m212_preserve_all_deletion_floor.py --tamper-selftest
```

The normal and optimized runs must byte-match
`verify_rank15_m212_preserve_all_deletion_floor.expected.txt`.

The script replays only exact integer arithmetic.  The source theorem and its
proof are in the note.  The packet makes zero child, recurrence-parent, Grand
List, Grand MCA, or official-score payment.
