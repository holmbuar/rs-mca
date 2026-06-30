# PR triage, 2026-06-30 late batch

**Status:** AUDIT / MANUAL-INTEGRATION.

This records the manual handling of open PRs #150--#158 and draft PR #145.
The goal was to preserve useful local proof material while avoiding stale
roadmap edits, broad conditional imports, and oversized draft scan trees.

## Integrated as standalone notes/scripts

AllenGrahamHart's PRs #150--#156 were imported as experimental notes and
dependency-local verifiers:

```text
#150  M1 root-slice lift
#151  M1 rank-defect packet normal form
#152  M1 t=2 one-exchange residual degree
#153  Step 5 high-agreement envelope map
#154  M1 top-packet lift and compression
#155  M1 two-root line-packet closure
#156  Step 1 sampler reconciliation audit
```

These are local M1/audit contributions.  They do not update the public
leaderboard and do not modify Papers A--D.

PR #158 was imported as an agreement-265 status audit and verifier.  Its
branch-side `towards-prize.md` patch was intentionally skipped because the
current v9 roadmap already moved the threshold program away from the old
agreement-265 upper-bound target.

## Distilled instead of merged wholesale

PR #157 is a large packet-sift popularity-gate package.  Rather than importing
ten notes and ten interdependent verifiers, the reusable core was distilled to

```text
experimental/notes/m1/m1_packet_sift_popularity_digest.md
experimental/scripts/verify_m1_packet_sift_popularity_digest.py
```

The digest preserves the packet-overlap Cauchy floor, endpoint-star sift,
divisor-gate popularity cap, equal-line local cap `U_eq(mu)=8mu`, and
injective finite-slope cap `U=16`.  The missing theorem remains the nonlocal
model-entry/multiplicity statement for actual Hankel packet families.

Draft PR #145 is an oversized a=327 RIM obstruction packet.  The useful
route-cut facts were distilled to

```text
experimental/notes/m1/m1_a327_rim_route_cut_digest.md
experimental/data/m1_a327_rim_route_cut_digest.json
experimental/scripts/verify_m1_a327_rim_route_cut_digest.py
```

The digest records the full-rank local rank gate, 34/34 pivot coverage, and
rank-free audit failures/small RREF-mimic successes.  It is not an `a=327`
witness, not a global upper bound, and not an improvement over the existing
PR #133 interleaved-list record.

## Closure notes

After this manual integration, the source PRs can be closed as integrated or
superseded-by-digest.  Future work should rebase any additional M1 packet
material against the v9 Hankel certificate schema and submit one named residual
bucket or verifier at a time.
