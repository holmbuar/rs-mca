#!/usr/bin/env python3
"""Verify the compact a=327 RIM route-cut digest."""

from __future__ import annotations

import json
from pathlib import Path


DATA_PATH = Path("experimental/data/m1_a327_rim_route_cut_digest.json")

REQUIRED_NONCLAIMS = {
    "MCA N_bad",
    "protocol soundness",
    "ordinary list decoding beyond the stated interleaved-list predicate",
    "a=327 interleaved-list certificate",
    "global Lambda_mu(C,327) <= 6",
    "global RIM full-rank theorem",
    "deterministic combinatorial pivot schedule",
    "exact Lambda_mu",
    "exact delta*_C",
    "improvement over PR #133",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(DATA_PATH.read_text())

    require(data["source_pr"] == 145, "wrong source PR")
    require(data["track"] == "INTERLEAVED_LIST", "wrong track")
    require(data["denominator"] == "17^32", "wrong denominator")
    require(data["agreement_target"] == 327, "wrong agreement target")
    require(data["baseline"]["current_pr_133_agreement"] == 326, "wrong baseline agreement")
    require(data["baseline"]["current_pr_133_lambda_lower"] == 7, "wrong baseline lower bound")

    rank_gate = data["rank_gate"]
    require(rank_gate["support_count"] == 7, "wrong support count")
    require(rank_gate["support_size"] == 327, "wrong support size")
    require(rank_gate["max_pair_intersection"] == 254, "wrong max pair intersection")
    require(rank_gate["matrix_shape"] == [2882, 382], "wrong rank-gate shape")
    require(rank_gate["rank"] == 382, "wrong rank")
    require(rank_gate["nullity"] == 0, "wrong nullity")

    pivot = data["pivot_coverage"]
    require(pivot["source_matrices"] == 34, "wrong source-matrix count")
    require(pivot["pivot_certified"] == 34, "wrong pivot-certified count")
    require(sum(pivot["pattern_classes"].values()) == 34, "pivot classes do not sum")

    rank_free = data["rank_free_audits"]
    require(rank_free["support_overlap"]["successes"] == 0, "support-overlap rank-free success changed")
    require(rank_free["generic_pairwise"]["successes"] == 0, "generic rank-free success changed")
    require(rank_free["quotient_residual"]["successes"] == 2, "quotient residual success count changed")
    require(rank_free["quotient_residual"]["deterministic_rule_successes"] == 0, "deterministic success claimed")

    claim = data["repo_claim"]
    require(claim["improves_pr_133"] is False, "unexpected PR #133 improvement claim")
    require(claim["mca_counted"] is False, "unexpected MCA claim")
    require(claim["global_upper_bound"] is False, "unexpected global upper-bound claim")
    require(REQUIRED_NONCLAIMS.issubset(set(claim["not_claimed"])), "missing non-claims")

    print("m1 a=327 RIM route-cut digest checks passed")


if __name__ == "__main__":
    main()
