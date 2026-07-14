#!/usr/bin/env python3
"""Verify complete-pair absorption into the R=2t-1 pair-minor capacity."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
from collections import defaultdict
from math import comb
from pathlib import Path
from typing import Any, Iterable

import verify_first_beyond_half_kernel_pencil as first
import verify_half_distance_generic_rank_deflation as rankdef
import verify_half_distance_hankel_curve_lineray as half


BASE_COMMIT = "c35a6da31ed0905afcbaaefe4eb0f242572ebb35"
CLAIM_ID = "first-beyond-half-complete-absorption-v1"
ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = (
    ROOT
    / "experimental/data/certificates/first-beyond-half-complete-absorption"
    / "first_beyond_half_complete_absorption.json"
)


class VerificationError(RuntimeError):
    """Raised when a theorem gate or certificate check fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def payload_digest(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def specialized_top_recurrence(
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    gamma: int,
    t: int,
    p: int,
) -> list[list[int]]:
    return [
        [
            (
                line_base[row + column]
                + gamma * direction[row + column]
            )
            % p
            for column in range(t + 1)
        ]
        for row in range(t - 1)
    ]


def root_capacity(
    determinants: dict[tuple[int, int], list[int]], p: int
) -> int:
    capacity = 0
    for polynomial in determinants.values():
        if polynomial == [0]:
            continue
        roots = sum(
            half.poly_eval(polynomial, gamma, p) == 0
            for gamma in range(p)
        )
        require(
            roots <= len(polynomial) - 1,
            "pair determinant exceeded its field-root capacity",
        )
        capacity += roots
    return capacity


def complete_absorption_audit(
    p: int,
    domain: tuple[int, ...],
    t: int,
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    sparse: first.SparseMultimap,
    spans: dict[tuple[int, ...], set[tuple[int, ...]]],
) -> dict[str, int | str]:
    require(t >= 2 and len(domain) >= 2 * t - 1, "invalid slice")
    selected = first.selected_atoms_on_line(
        p, line_base, direction, sparse, spans
    )
    pairs = [
        (gamma, atom[0])
        for gamma, atoms in selected.items()
        for atom in atoms
    ]
    pair_count = len(pairs)
    pair_bound = comb(len(domain), 2)
    row_count = t - 1
    pencil = first.recurrence_pencil(
        line_base, direction, t, p
    )
    pivot = first.maximal_pivot(pencil, t, p)

    if pivot == [0]:
        require(
            all(len(support) <= t - 2 for _, support in pairs),
            "generic top-rank drop retained weight t-1 or t",
        )
        if t == 2:
            require(pair_count <= 1, "rank-zero t=2 line retained two pairs")
        else:
            require(
                pair_count <= len(domain) + t - 2 <= pair_bound,
                "rank-drop half-core fallback exceeded pair capacity",
            )
        return {
            "pairs": pair_count,
            "slopes": len(selected),
            "branch": "generic-rank-deficient",
            "incidences": 0,
            "capacity": 0,
            "good_pairs": 0,
            "fixed_roots": 0,
            "same_slope_excess": pair_count - len(selected),
        }

    determinants = first.pair_determinants(
        pencil, domain, t, p
    )
    good = {
        roots: polynomial
        for roots, polynomial in determinants.items()
        if polynomial != [0]
    }
    fixed = first.fixed_kernel_roots(domain, determinants)

    for gamma, support in pairs:
        specialized = specialized_top_recurrence(
            line_base, direction, gamma, t, p
        )
        expected_rank = min(len(support), row_count)
        require(
            rankdef.numeric_rank(specialized, p) == expected_rank,
            "specialized top recurrence rank/weight mismatch",
        )

    if fixed:
        x = fixed[0]
        for _, support in pairs:
            if x in support:
                require(
                    len(support) <= row_count,
                    "fixed-root branch retained too much support through x",
                )
            else:
                require(
                    len(support) <= row_count - 1,
                    "fixed-root branch retained too much support away from x",
                )
        if t == 2 and len(domain) == 3:
            require(
                pair_count <= 1,
                "minimal fixed-root edge retained a noncommon singleton",
            )
        else:
            require(
                pair_count <= len(domain) + t - 1 <= pair_bound,
                "fixed-root half-core fallback exceeded pair capacity",
            )
        return {
            "pairs": pair_count,
            "slopes": len(selected),
            "branch": "formal-fixed-root",
            "incidences": 0,
            "capacity": root_capacity(good, p),
            "good_pairs": len(good),
            "fixed_roots": len(fixed),
            "same_slope_excess": pair_count - len(selected),
        }

    require(good, "full-rank loopless pencil has no good pair")
    incidence_keys: set[tuple[int, tuple[int, int]]] = set()
    incidences = 0
    for gamma, support in pairs:
        support_set = set(support)
        slack = t - len(support)
        chargeable = [
            roots
            for roots in good
            if len(set(roots) - support_set) <= slack
        ]
        require(
            len(chargeable) >= row_count,
            "retained support has too few chargeable good pairs",
        )
        specialized = specialized_top_recurrence(
            line_base, direction, gamma, t, p
        )
        for roots in chargeable:
            extra = tuple(x for x in roots if x not in support_set)
            padded_locator = half.constant_locator(
                tuple(support) + extra, p
            )
            padded_locator += [0] * (t + 1 - len(padded_locator))
            require(
                all(
                    sum(
                        row[column] * padded_locator[column]
                        for column in range(t + 1)
                    )
                    % p
                    == 0
                    for row in specialized
                ),
                "chargeable padded locator missed the top recurrence",
            )
            require(
                half.poly_eval(determinants[roots], gamma, p) == 0,
                "chargeable good pair missed its determinant root",
            )
            key = (gamma, roots)
            require(
                key not in incidence_keys,
                "two same-slope errors reused one chargeable pair",
            )
            incidence_keys.add(key)
        incidences += len(chargeable)

    capacity = root_capacity(good, p)
    require(
        pair_count * row_count <= incidences <= capacity,
        "complete-pair determinant double count failed",
    )
    require(
        capacity <= pair_bound * row_count,
        "complete-pair determinant capacity exceeded binomial budget",
    )
    require(pair_count <= pair_bound, "complete absorption bound failed")
    return {
        "pairs": pair_count,
        "slopes": len(selected),
        "branch": "loopless-full-rank",
        "incidences": incidences,
        "capacity": capacity,
        "good_pairs": len(good),
        "fixed_roots": 0,
        "same_slope_excess": pair_count - len(selected),
    }


def summarize_lines(
    p: int,
    domain: tuple[int, ...],
    t: int,
    weights: dict[int, int],
    lines: Iterable[tuple[tuple[int, ...], tuple[int, ...]]],
    mode: str,
) -> dict[str, Any]:
    redundancy = 2 * t - 1
    sparse, spans = first.build_sparse_multimap(
        p, domain, t, redundancy, weights
    )
    line_count = 0
    pair_total = 0
    slope_total = 0
    incidence_total = 0
    capacity_total = 0
    same_slope = 0
    maximum_pairs = 0
    minimum_slack = None
    branch_histogram: dict[str, int] = defaultdict(int)
    fixed_root_lines = 0
    for line_base, direction in lines:
        result = complete_absorption_audit(
            p,
            domain,
            t,
            line_base,
            direction,
            sparse,
            spans,
        )
        line_count += 1
        pair_total += int(result["pairs"])
        slope_total += int(result["slopes"])
        incidence_total += int(result["incidences"])
        capacity_total += int(result["capacity"])
        same_slope += int(result["same_slope_excess"])
        maximum_pairs = max(maximum_pairs, int(result["pairs"]))
        slack = comb(len(domain), 2) - int(result["pairs"])
        minimum_slack = slack if minimum_slack is None else min(minimum_slack, slack)
        branch_histogram[str(result["branch"])] += 1
        fixed_root_lines += int(result["fixed_roots"]) > 0
    return {
        "mode": mode,
        "p": p,
        "domain": list(domain),
        "n": len(domain),
        "t": t,
        "redundancy": redundancy,
        "lines": line_count,
        "transverse_pairs": pair_total,
        "transverse_slopes": slope_total,
        "same_slope_excess": same_slope,
        "good_pair_incidences": incidence_total,
        "root_capacity": capacity_total,
        "maximum_pairs_on_line": maximum_pairs,
        "complete_pair_bound": comb(len(domain), 2),
        "minimum_bound_slack": minimum_slack,
        "fixed_root_lines": fixed_root_lines,
        "branch_histogram": dict(sorted(branch_histogram.items())),
    }


def sharp_fixtures() -> dict[str, Any]:
    unique = first.sharp_top_fixture()
    repeated = first.same_slope_sharp_fixture()
    require(
        unique["top_pairs"] == comb(unique["n"], 2),
        "unique-slope fixture lost equality",
    )
    require(
        repeated["top_pairs"] == comb(repeated["n"], 2),
        "same-slope fixture lost equality",
    )
    return {
        "unique_slope": unique,
        "same_slope": repeated,
    }


def fixed_root_edge_fixture() -> dict[str, Any]:
    p = 3
    domain = tuple(range(p))
    t = 2
    weights = {x: 1 for x in domain}
    # The theorem assumes a nonzero direction, so use a line through zero
    # whose generic moment row is the evaluation vector at x=0.
    line_base = (0, 0, 0)
    direction = (1, 0, 0)
    sparse, spans = first.build_sparse_multimap(
        p, domain, t, 2 * t - 1, weights
    )
    result = complete_absorption_audit(
        p,
        domain,
        t,
        line_base,
        direction,
        sparse,
        spans,
    )
    require(result["branch"] == "formal-fixed-root", "edge branch changed")
    require(result["pairs"] == 1, "fixed-root edge lost its zero pair")
    return {
        "p": p,
        "domain": list(domain),
        "n": len(domain),
        "t": t,
        "line_base": list(line_base),
        "direction": list(direction),
        "branch": result["branch"],
        "pairs": result["pairs"],
        "bound": comb(len(domain), 2),
    }


def build_payload() -> dict[str, Any]:
    exhaustive_specs = [
        (3, tuple(range(3)), 2),
        (5, (0, 1, 2), 2),
        (5, tuple(range(5)), 2),
        (7, (0, 1, 2, 3, 4), 2),
        (7, tuple(range(7)), 2),
        (11, (0, 1, 2, 3, 4), 2),
        (13, (0, 1, 2, 3, 4), 2),
        (17, (0, 1, 2, 3, 4), 2),
    ]
    exhaustive = []
    for p, domain, t in exhaustive_specs:
        weights = {x: 1 for x in domain}
        row = summarize_lines(
            p,
            domain,
            t,
            weights,
            first.exhaustive_lines(p, 2 * t - 1),
            "exhaustive",
        )
        expected = p ** (2 * t - 2) * (
            (p ** (2 * t - 1) - 1) // (p - 1)
        )
        require(row["lines"] == expected, "affine line census mismatch")
        exhaustive.append(row)

    sampled_specs = [
        (7, tuple(range(7)), 3, 8000),
        (11, (0, 1, 2, 3, 4), 3, 4000),
        (13, (0, 1, 2, 3, 4), 3, 4000),
    ]
    sampled = []
    for p, domain, t, count in sampled_specs:
        weights = {x: (3 * x + 2) % p or 1 for x in domain}
        sparse, _ = first.build_sparse_multimap(
            p, domain, t, 2 * t - 1, weights
        )
        lines = first.sampled_lines(
            p,
            domain,
            t,
            weights,
            count,
            20260715 + 1000 * p + len(domain),
        )
        require(len(lines) == count and sparse, "sample construction failed")
        sampled.append(
            summarize_lines(
                p, domain, t, weights, lines, "deterministic-sample"
            )
        )

    fixtures = sharp_fixtures()
    fixed_edge = fixed_root_edge_fixture()
    rows = exhaustive + sampled
    return {
        "schema_version": 1,
        "claim_id": CLAIM_ID,
        "base_commit": BASE_COMMIT,
        "status": "PROVED_AUDIT_WITH_UNPROVED_LEAN_TARGET",
        "hard_input": "3_first_beyond_half_complete_pair_absorption",
        "theorem": {
            "range": "N>=R=2t-1 and t>=2",
            "complete_all_pair_bound": "|P|<=binom(N,2)",
            "mca_ca_numerator_bound": "B_MCA,B_CA<=binom(N,2)",
            "rank_deficient_branch": "falls_to_weight_at_most_t-2",
            "fixed_root_branch": "falls_to_weight_at_most_t-1",
            "loopless_branch": (
                "every retained pair consumes at least t-1 good pair roots"
            ),
        },
        "exhaustive_grids": exhaustive,
        "sampled_weight_three_grids": sampled,
        "sharp_fixtures": fixtures,
        "fixed_root_edge_fixture": fixed_edge,
        "totals": {
            "audited_lines": sum(row["lines"] for row in rows),
            "transverse_pairs": sum(
                row["transverse_pairs"] for row in rows
            ),
            "transverse_slopes": sum(
                row["transverse_slopes"] for row in rows
            ),
            "same_slope_excess": sum(
                row["same_slope_excess"] for row in rows
            ),
            "good_pair_incidences": sum(
                row["good_pair_incidences"] for row in rows
            ),
            "root_capacity": sum(row["root_capacity"] for row in rows),
            "fixed_root_lines": sum(
                row["fixed_root_lines"] for row in rows
            ),
        },
        "nonclaims": [
            "no_complete_single_binomial_absorption_claim_for_d_at_least_2",
            "no_bound_for_R_less_than_2t_minus_1_in_this_packet",
            "no_atlas_or_deployed_row_movement",
            "lean_target_unproved",
        ],
    }


def build_certificate() -> dict[str, Any]:
    payload = build_payload()
    return {**payload, "payload_sha256": payload_digest(payload)}


def validate_exact(actual: dict[str, Any], expected: dict[str, Any]) -> None:
    if actual != expected:
        raise VerificationError("certificate differs from exact recomputation")
    digest = actual.get("payload_sha256")
    payload = {
        key: value for key, value in actual.items() if key != "payload_sha256"
    }
    require(digest == payload_digest(payload), "certificate digest mismatch")


def check_certificate() -> dict[str, Any]:
    require(CERTIFICATE.is_file(), f"missing certificate: {CERTIFICATE}")
    with CERTIFICATE.open("r", encoding="utf-8") as handle:
        actual = json.load(handle)
    expected = build_certificate()
    validate_exact(actual, expected)
    return expected


def tamper_selftest() -> int:
    expected = build_certificate()
    tampers = []

    bad = copy.deepcopy(expected)
    bad["base_commit"] = "0" * 40
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["theorem"]["complete_all_pair_bound"] = "|P|<=N"
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["exhaustive_grids"][4]["maximum_pairs_on_line"] -= 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["sharp_fixtures"]["same_slope"]["top_pairs"] -= 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["fixed_root_edge_fixture"]["pairs"] += 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["payload_sha256"] = "f" * 64
    tampers.append(bad)

    rejected = 0
    for tampered in tampers:
        try:
            validate_exact(tampered, expected)
        except VerificationError:
            rejected += 1
    require(rejected == len(tampers), "a pinned tamper was not rejected")
    return rejected


def summary(certificate: dict[str, Any]) -> str:
    totals = certificate["totals"]
    return (
        "FIRST_BEYOND_HALF_COMPLETE_ABSORPTION_PASS "
        f"lines={totals['audited_lines']} "
        f"pairs={totals['transverse_pairs']} "
        f"slopes={totals['transverse_slopes']} "
        f"incidences={totals['good_pair_incidences']} "
        f"fixed={totals['fixed_root_lines']} "
        f"same_slope={totals['same_slope_excess']}"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true")
    group.add_argument("--tamper-selftest", action="store_true")
    group.add_argument("--print-certificate", action="store_true")
    args = parser.parse_args()

    if args.tamper_selftest:
        rejected = tamper_selftest()
        print(
            "FIRST_BEYOND_HALF_COMPLETE_ABSORPTION_TAMPER_PASS "
            f"rejected={rejected}/{rejected}"
        )
        return 0
    if args.print_certificate:
        print(json.dumps(build_certificate(), indent=2, sort_keys=True))
        return 0
    certificate = check_certificate()
    print(summary(certificate))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
