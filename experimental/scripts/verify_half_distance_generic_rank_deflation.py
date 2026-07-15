#!/usr/bin/env python3
"""Verify generic-rank compression and fixed-root deflation at half distance."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import random
from collections import defaultdict
from pathlib import Path
from typing import Any

import verify_half_distance_hankel_curve_lineray as base


BASE_COMMIT = "c35a6da31ed0905afcbaaefe4eb0f242572ebb35"
CLAIM_ID = "half-distance-generic-rank-deflation-v1"
ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = (
    ROOT
    / "experimental/data/certificates/half-distance-generic-rank-deflation"
    / "half_distance_generic_rank_deflation.json"
)


class VerificationError(RuntimeError):
    """Raised when a stronger theorem or certificate gate fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def payload_digest(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def numeric_rank(matrix: list[list[int]], p: int) -> int:
    if not matrix:
        return 0
    work = [[value % p for value in row] for row in matrix]
    rows = len(work)
    columns = len(work[0])
    rank = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, rows) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, p)
        work[rank] = [value * inverse % p for value in work[rank]]
        for row in range(rows):
            if row == rank or work[row][column] == 0:
                continue
            scalar = work[row][column]
            work[row] = [
                (value - scalar * pivot_value) % p
                for value, pivot_value in zip(
                    work[row], work[rank], strict=True
                )
            ]
        rank += 1
        if rank == rows:
            break
    return rank


def generic_hankel_rank(
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    t: int,
    p: int,
) -> tuple[int, list[int]]:
    matrix = [
        [
            base.trim(
                [line_base[row + column], direction[row + column]], p
            )
            for column in range(t)
        ]
        for row in range(t)
    ]
    for size in range(t, 0, -1):
        for row_set in itertools.combinations(range(t), size):
            for column_set in itertools.combinations(range(t), size):
                minor = [
                    [matrix[row][column] for column in column_set]
                    for row in row_set
                ]
                determinant = base.determinant_poly(minor, p)
                if determinant != [0]:
                    require(
                        len(determinant) - 1 <= size,
                        "generic-rank minor degree exceeded its size",
                    )
                    return size, determinant
    return 0, [1]


def selected_transverse_pairs(
    p: int,
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    sparse: dict[
        tuple[int, ...], tuple[tuple[int, ...], tuple[int, ...]]
    ],
    spans: dict[tuple[int, ...], set[tuple[int, ...]]],
) -> dict[int, list[tuple[int, tuple[int, ...]]]]:
    selected: dict[int, list[tuple[int, tuple[int, ...]]]] = defaultdict(list)
    for gamma in range(p):
        point = tuple(
            (line_base[index] + gamma * direction[index]) % p
            for index in range(len(line_base))
        )
        atom = sparse.get(point)
        if atom is None:
            continue
        support, _ = atom
        if direction not in spans[support]:
            selected[len(support)].append((gamma, support))
    return selected


def fixed_roots_of_locator(
    locator: list[list[int]], domain: tuple[int, ...], p: int
) -> tuple[int, ...]:
    return tuple(
        x
        for x in domain
        if base.locator_value_polynomial(locator, x, p) == [0]
    )


def deflated_exact_weight_audit(
    p: int,
    domain: tuple[int, ...],
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    support_size: int,
    selected: list[tuple[int, tuple[int, ...]]],
) -> dict[str, int]:
    require(support_size >= 1 and selected, "empty deflation stratum")
    full_locator = base.cofactor_locator(
        line_base, direction, support_size, p
    )
    full_degree = max(len(coefficient) - 1 for coefficient in full_locator)
    require(full_degree <= support_size, "full cofactor degree exceeded s")
    fixed_roots = fixed_roots_of_locator(full_locator, domain, p)
    g = len(fixed_roots)
    require(g <= support_size, "formal fixed roots exceed locator degree")
    fixed_set = set(fixed_roots)
    moving = support_size - g

    if moving == 0:
        require(len(selected) <= 1, "fixed locator repeated transversely")
        return {
            "support_size": support_size,
            "fixed_roots": g,
            "moving_roots": 0,
            "full_degree": full_degree,
            "deflated_degree": 0,
            "selected": len(selected),
            "incidences": 0,
            "capacity": 1,
        }

    fixed_locator = base.constant_locator(fixed_roots, p)
    transformed_base = []
    transformed_direction = []
    for row in range(2 * moving):
        transformed_base.append(
            sum(
                fixed_locator[index] * line_base[row + index]
                for index in range(g + 1)
            )
            % p
        )
        transformed_direction.append(
            sum(
                fixed_locator[index] * direction[row + index]
                for index in range(g + 1)
            )
            % p
        )

    residual_locator = base.cofactor_locator(
        tuple(transformed_base),
        tuple(transformed_direction),
        moving,
        p,
    )
    residual_degree = max(
        len(coefficient) - 1 for coefficient in residual_locator
    )
    require(
        residual_degree <= moving,
        "deflated locator degree exceeds its moving-root count",
    )
    require(
        not fixed_roots_of_locator(
            residual_locator,
            tuple(x for x in domain if x not in fixed_set),
            p,
        ),
        "deflated curve retained a new formal domain root",
    )

    for gamma, support in selected:
        residual_support = tuple(x for x in support if x not in fixed_set)
        require(
            len(residual_support) == moving,
            "actual support lost the wrong number of fixed roots",
        )
        specialized = [
            base.poly_eval(coefficient, gamma, p)
            for coefficient in residual_locator
        ]
        require(any(specialized), "actual residual landed at rank drop")
        require(specialized[-1] != 0, "residual locator lost monicity")
        inverse = pow(specialized[-1], -1, p)
        monic = [value * inverse % p for value in specialized]
        require(
            monic == base.constant_locator(residual_support, p),
            "transformed moments did not recover the residual support",
        )

    incidences = len(selected) * moving
    capacity = 0
    measured = 0
    for x in domain:
        if x in fixed_set:
            continue
        value_poly = base.locator_value_polynomial(residual_locator, x, p)
        require(value_poly != [0], "nonfixed residual evaluation vanished")
        roots = sum(
            base.poly_eval(value_poly, gamma, p) == 0 for gamma in range(p)
        )
        require(
            roots <= len(value_poly) - 1,
            "deflated evaluation has too many roots",
        )
        capacity += residual_degree
        measured += sum(x in support for _, support in selected)
    require(measured == incidences, "deflated incidence recount failed")
    require(incidences <= capacity, "deflated root capacity failed")
    require(
        len(selected) <= len(domain) - g,
        "exact-weight deflated bound N-g failed",
    )
    return {
        "support_size": support_size,
        "fixed_roots": g,
        "moving_roots": moving,
        "full_degree": full_degree,
        "deflated_degree": residual_degree,
        "selected": len(selected),
        "incidences": incidences,
        "capacity": capacity,
    }


def strong_line_audit(
    p: int,
    domain: tuple[int, ...],
    t: int,
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    sparse: dict[
        tuple[int, ...], tuple[tuple[int, ...], tuple[int, ...]]
    ],
    spans: dict[tuple[int, ...], set[tuple[int, ...]]],
) -> dict[str, Any]:
    # Retain every gate of the predecessor packet.
    base.audit_line(
        p, domain, t, line_base, direction, sparse, spans
    )
    selected = selected_transverse_pairs(
        p, line_base, direction, sparse, spans
    )
    rho, rank_minor = generic_hankel_rank(
        line_base, direction, t, p
    )

    all_parameters = []
    deflation_rows = []
    for support_size, pairs in selected.items():
        all_parameters.extend(gamma for gamma, _ in pairs)
        for gamma, support in pairs:
            specialized = [
                [
                    (
                        line_base[row + column]
                        + gamma * direction[row + column]
                    )
                    % p
                    for column in range(t)
                ]
                for row in range(t)
            ]
            require(
                numeric_rank(specialized, p) == support_size,
                "actual error Hankel rank does not equal its weight",
            )
            require(
                support_size <= rho,
                "specialized Hankel rank exceeded generic rank",
            )
        if support_size > 0:
            deflation_rows.append(
                deflated_exact_weight_audit(
                    p,
                    domain,
                    line_base,
                    direction,
                    support_size,
                    pairs,
                )
            )

    require(
        len(all_parameters) == len(set(all_parameters)),
        "same-slope multiplicity survived the base verifier",
    )
    pair_count = len(all_parameters)
    if rho == 0:
        require(
            set(selected) <= {0} and pair_count <= 1,
            "generic rank zero retained a positive-weight error",
        )
        lower_parameters = []
        top_count = pair_count
    else:
        lower_parameters = [
            gamma
            for support_size, pairs in selected.items()
            if support_size < rho
            for gamma, _ in pairs
        ]
        require(
            all(base.poly_eval(rank_minor, gamma, p) == 0 for gamma in lower_parameters),
            "lower-weight parameter missed the generic-rank minor",
        )
        require(
            len(lower_parameters) <= len(rank_minor) - 1 <= rho,
            "generic-rank lower-stratum charge failed",
        )
        top_count = len(selected.get(rho, []))
        require(top_count <= len(domain), "generic-rank top curve exceeds N")

    require(
        pair_count <= len(domain) + rho,
        "strong half-distance bound N+rho failed",
    )
    require(
        pair_count <= len(domain) + t,
        "uniform half-distance bound N+t failed",
    )
    return {
        "pair_count": pair_count,
        "generic_rank": rho,
        "minor_degree": len(rank_minor) - 1,
        "lower_weight_parameters": len(lower_parameters),
        "top_weight_parameters": top_count,
        "deflation_rows": deflation_rows,
    }


def exhaustive_strong_grid(
    p: int, domain: tuple[int, ...], t: int
) -> dict[str, Any]:
    redundancy = 2 * t
    column_weights = {x: 1 for x in domain}
    sparse, spans = base.build_sparse_syndromes(
        p, domain, t, redundancy, column_weights
    )
    directions = base.normalized_directions(p, redundancy)
    rank_histogram: dict[int, int] = defaultdict(int)
    line_count = 0
    pair_total = 0
    lower_total = 0
    maximum_pairs = 0
    maximum_excess_over_n = 0
    deflation_families = 0
    fixed_root_families = 0
    maximum_full_degree = 0
    maximum_deflated_degree = 0

    for direction in directions:
        pivot = next(index for index, value in enumerate(direction) if value)
        free_indices = [index for index in range(redundancy) if index != pivot]
        for values in itertools.product(range(p), repeat=redundancy - 1):
            line_base_list = [0] * redundancy
            for index, value in zip(free_indices, values, strict=True):
                line_base_list[index] = value
            result = strong_line_audit(
                p,
                domain,
                t,
                tuple(line_base_list),
                direction,
                sparse,
                spans,
            )
            line_count += 1
            rank_histogram[result["generic_rank"]] += 1
            pair_total += result["pair_count"]
            lower_total += result["lower_weight_parameters"]
            maximum_pairs = max(maximum_pairs, result["pair_count"])
            maximum_excess_over_n = max(
                maximum_excess_over_n,
                result["pair_count"] - len(domain),
            )
            for row in result["deflation_rows"]:
                deflation_families += 1
                fixed_root_families += row["fixed_roots"] > 0
                maximum_full_degree = max(
                    maximum_full_degree, row["full_degree"]
                )
                maximum_deflated_degree = max(
                    maximum_deflated_degree, row["deflated_degree"]
                )

    expected = p ** (redundancy - 1) * (
        (p**redundancy - 1) // (p - 1)
    )
    require(line_count == expected, "strong affine line census mismatch")
    return {
        "p": p,
        "domain": list(domain),
        "n": len(domain),
        "t": t,
        "redundancy": redundancy,
        "affine_lines": line_count,
        "generic_rank_histogram": {
            str(rank): count for rank, count in sorted(rank_histogram.items())
        },
        "transverse_pair_incidences": pair_total,
        "lower_weight_parameters": lower_total,
        "maximum_pairs_on_line": maximum_pairs,
        "maximum_excess_over_n": maximum_excess_over_n,
        "strong_bound": len(domain) + t,
        "deflation_families": deflation_families,
        "fixed_root_families": fixed_root_families,
        "maximum_full_degree": maximum_full_degree,
        "maximum_deflated_degree": maximum_deflated_degree,
    }


def sampled_strong_grid(redundancy: int) -> dict[str, Any]:
    p = 7
    domain = tuple(range(p))
    t = 3
    column_weights = {x: (x + 1) % p or 1 for x in domain}
    sparse, spans = base.build_sparse_syndromes(
        p, domain, t, redundancy, column_weights
    )
    points = sorted(sparse)
    rng = random.Random(20260714 + 100 * redundancy)
    lines: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    while len(lines) < 5000:
        first = points[rng.randrange(len(points))]
        second = points[rng.randrange(len(points))]
        if first != second:
            lines.add(base.canonical_line(first, second, p))
    directions = base.normalized_directions(p, redundancy)
    while len(lines) < 8000:
        direction = directions[rng.randrange(len(directions))]
        pivot = next(index for index, value in enumerate(direction) if value)
        line_base = tuple(
            0 if index == pivot else rng.randrange(p)
            for index in range(redundancy)
        )
        lines.add((line_base, direction))

    rank_histogram: dict[int, int] = defaultdict(int)
    pair_total = 0
    lower_total = 0
    maximum_pairs = 0
    deflation_families = 0
    fixed_root_families = 0
    for line_base, direction in sorted(lines):
        result = strong_line_audit(
            p, domain, t, line_base, direction, sparse, spans
        )
        rank_histogram[result["generic_rank"]] += 1
        pair_total += result["pair_count"]
        lower_total += result["lower_weight_parameters"]
        maximum_pairs = max(maximum_pairs, result["pair_count"])
        for row in result["deflation_rows"]:
            deflation_families += 1
            fixed_root_families += row["fixed_roots"] > 0

    return {
        "p": p,
        "n": len(domain),
        "t": t,
        "redundancy": redundancy,
        "sampled_lines": len(lines),
        "generic_rank_histogram": {
            str(rank): count for rank, count in sorted(rank_histogram.items())
        },
        "transverse_pair_incidences": pair_total,
        "lower_weight_parameters": lower_total,
        "maximum_pairs_on_line": maximum_pairs,
        "strong_bound": len(domain) + t,
        "deflation_families": deflation_families,
        "fixed_root_families": fixed_root_families,
    }


def cyclotomic_strong_fixture() -> dict[str, Any]:
    p = 13
    t = 3
    domain = tuple(range(1, p))
    line_base = (0, 0, 1, 0, 0, 0)
    direction = (0, 0, 0, 1, 0, 0)
    mu = tuple(x for x in domain if pow(x, t + 1, p) == 1)
    selected = []
    for gamma in domain:
        support = tuple(
            sorted({(-gamma * root) % p for root in mu if root != 1})
        )
        selected.append((gamma, support))
    row = deflated_exact_weight_audit(
        p, domain, line_base, direction, t, selected
    )
    rho, minor = generic_hankel_rank(line_base, direction, t, p)
    require(rho == t, "cyclotomic generic Hankel rank changed")
    require(row["selected"] == len(domain), "cyclotomic N scale changed")
    return {
        "p": p,
        "n": len(domain),
        "t": t,
        "generic_rank": rho,
        "rank_minor_degree": len(minor) - 1,
        "pairs": row["selected"],
        "fixed_roots": row["fixed_roots"],
        "moving_roots": row["moving_roots"],
        "deflated_degree": row["deflated_degree"],
        "strong_bound": len(domain) + rho,
        "N_scale_attained": row["selected"] == len(domain),
    }


def build_payload() -> dict[str, Any]:
    exhaustive_specs = [
        (2, tuple(range(2)), 1),
        (3, tuple(range(3)), 1),
        (5, tuple(range(5)), 2),
        (7, (0, 1, 2, 3, 4), 2),
        (7, tuple(range(7)), 2),
    ]
    exhaustive = [
        exhaustive_strong_grid(p, domain, t)
        for p, domain, t in exhaustive_specs
    ]
    sampled = [sampled_strong_grid(6), sampled_strong_grid(7)]
    cyclotomic = cyclotomic_strong_fixture()
    return {
        "schema_version": 1,
        "claim_id": CLAIM_ID,
        "base_commit": BASE_COMMIT,
        "status": "PROVED_AUDIT_WITH_UNPROVED_LEAN_TARGET",
        "hard_input": "3_half_distance_generic_rank_deflation",
        "theorem": {
            "dimension_range": "N>=R>=2t",
            "line_bound": "|P|<=N+rho<=N+t",
            "generic_rank": "rho=rank_F(z) leading_t_by_t_Hankel",
            "lower_weight_charge": "at_most_rho_roots_of_one_minor",
            "top_weight_charge": "|P_rho|<=N-g<=N",
            "deflated_degree": "delta<=rho-g",
        },
        "exhaustive_strong_grids": exhaustive,
        "sampled_weight_three_grids": sampled,
        "cyclotomic_strong_fixture": cyclotomic,
        "totals": {
            "exhaustive_affine_lines": sum(
                row["affine_lines"] for row in exhaustive
            ),
            "exhaustive_pair_incidences": sum(
                row["transverse_pair_incidences"] for row in exhaustive
            ),
            "exhaustive_lower_weight_parameters": sum(
                row["lower_weight_parameters"] for row in exhaustive
            ),
            "sampled_lines": sum(row["sampled_lines"] for row in sampled),
            "sampled_pair_incidences": sum(
                row["transverse_pair_incidences"] for row in sampled
            ),
            "deflation_families": sum(
                row["deflation_families"] for row in exhaustive + sampled
            )
            + 1,
            "fixed_root_families": sum(
                row["fixed_root_families"] for row in exhaustive + sampled
            ),
        },
        "nonclaims": [
            "no_bound_beyond_half_distance_R<2t",
            "no_exact_endpoint_numerator",
            "no_improvement_over_strict_half_distance_BCHKS",
            "no_deployed_row_movement",
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
    bad["theorem"]["line_bound"] = "|P|<=N"
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["exhaustive_strong_grids"][2]["generic_rank_histogram"]["2"] += 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["exhaustive_strong_grids"][4]["maximum_pairs_on_line"] += 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["cyclotomic_strong_fixture"]["pairs"] -= 1
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
        "HALF_DISTANCE_GENERIC_RANK_DEFLATION_PASS "
        f"lines={totals['exhaustive_affine_lines']} "
        f"pairs={totals['exhaustive_pair_incidences']} "
        f"lower={totals['exhaustive_lower_weight_parameters']} "
        f"sampled={totals['sampled_lines']} "
        f"deflations={totals['deflation_families']} "
        f"fixed={totals['fixed_root_families']}"
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
            "HALF_DISTANCE_GENERIC_RANK_DEFLATION_TAMPER_PASS "
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
