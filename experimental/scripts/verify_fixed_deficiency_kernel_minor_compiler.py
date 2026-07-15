#!/usr/bin/env python3
"""Verify fixed-deficiency kernel-minor bounds beyond half distance."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import random
from collections import defaultdict
from math import comb
from pathlib import Path
from typing import Any, Iterable

import verify_first_beyond_half_kernel_pencil as first
import verify_half_distance_generic_rank_deflation as rankdef
import verify_half_distance_hankel_curve_lineray as half


BASE_COMMIT = "c35a6da31ed0905afcbaaefe4eb0f242572ebb35"
CLAIM_ID = "fixed-deficiency-kernel-minor-compiler-v1"
ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = (
    ROOT
    / "experimental/data/certificates/fixed-deficiency-kernel-minor-compiler"
    / "fixed_deficiency_kernel_minor_compiler.json"
)


class VerificationError(RuntimeError):
    """Raised when a theorem gate or pinned certificate fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def payload_digest(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def determinant_numeric(matrix: list[list[int]], p: int) -> int:
    size = len(matrix)
    require(all(len(row) == size for row in matrix), "nonsquare determinant")
    if size == 0:
        return 1
    work = [[value % p for value in row] for row in matrix]
    determinant = 1
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant = -determinant
        pivot_value = work[column][column]
        determinant = determinant * pivot_value % p
        inverse = pow(pivot_value, -1, p)
        for row in range(column + 1, size):
            if work[row][column] == 0:
                continue
            scalar = work[row][column] * inverse % p
            for index in range(column, size):
                work[row][index] = (
                    work[row][index] - scalar * work[column][index]
                ) % p
    return determinant % p


def interpolate(
    points: list[tuple[int, int]], p: int
) -> list[int]:
    result = [0]
    for index, (x_value, y_value) in enumerate(points):
        basis = [1]
        denominator = 1
        for other_index, (other_x, _) in enumerate(points):
            if other_index == index:
                continue
            basis = half.poly_mul(basis, [(-other_x) % p, 1], p)
            denominator = denominator * (x_value - other_x) % p
        result = half.poly_add(
            result,
            half.poly_scale(
                basis, y_value * pow(denominator, -1, p), p
            ),
            p,
        )
    return half.trim(result, p)


def determinant_affine_rows(
    polynomial_rows: list[list[list[int]]],
    constant_rows: list[list[int]],
    degree_bound: int,
    p: int,
) -> list[int]:
    require(degree_bound < p, "interpolation field is too small")
    points = []
    for value in range(degree_bound + 1):
        matrix = [
            [half.poly_eval(entry, value, p) for entry in row]
            for row in polynomial_rows
        ] + [[entry % p for entry in row] for row in constant_rows]
        points.append((value, determinant_numeric(matrix, p)))
    polynomial = interpolate(points, p)
    require(
        len(polynomial) - 1 <= degree_bound,
        "interpolated determinant exceeded its degree bound",
    )
    return polynomial


def recurrence_pencil(
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    redundancy: int,
    support_size: int,
    p: int,
) -> list[list[list[int]]]:
    rows = redundancy - support_size
    require(rows >= 1, "empty recurrence row window")
    return [
        [
            half.trim(
                [line_base[row + column], direction[row + column]], p
            )
            for column in range(support_size + 1)
        ]
        for row in range(rows)
    ]


def maximal_pivot(
    pencil: list[list[list[int]]],
    support_size: int,
    p: int,
) -> list[int]:
    rows = len(pencil)
    for columns in itertools.combinations(range(support_size + 1), rows):
        minor = [
            [row[column] for column in columns]
            for row in pencil
        ]
        determinant = determinant_affine_rows(minor, [], rows, p)
        if determinant != [0]:
            return determinant
    return [0]


def stacked_determinants(
    pencil: list[list[list[int]]],
    domain: tuple[int, ...],
    support_size: int,
    kernel_dimension: int,
    p: int,
) -> dict[tuple[int, ...], list[int]]:
    rows = len(pencil)
    require(
        rows + kernel_dimension == support_size + 1,
        "stacked determinant is not square",
    )
    determinants = {}
    for roots in itertools.combinations(domain, kernel_dimension):
        evaluations = [
            [pow(root, column, p) for column in range(support_size + 1)]
            for root in roots
        ]
        determinants[roots] = determinant_affine_rows(
            pencil, evaluations, rows, p
        )
    return determinants


def specialized_recurrence(
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    gamma: int,
    redundancy: int,
    support_size: int,
    p: int,
) -> list[list[int]]:
    return [
        [
            (
                line_base[row + column]
                + gamma * direction[row + column]
            )
            % p
            for column in range(support_size + 1)
        ]
        for row in range(redundancy - support_size)
    ]


def fixed_kernel_roots(
    domain: tuple[int, ...],
    good_subsets: set[tuple[int, ...]],
) -> tuple[int, ...]:
    return tuple(
        x
        for x in domain
        if not any(x in roots for roots in good_subsets)
    )


def audit_exact_selected(
    p: int,
    domain: tuple[int, ...],
    redundancy: int,
    support_size: int,
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    selected_exact: list[tuple[int, tuple[int, ...]]],
) -> dict[str, int]:
    rows = redundancy - support_size
    kernel_dimension = 2 * support_size - redundancy + 1
    require(
        rows >= 1 and kernel_dimension >= 2,
        "exact stratum is not strictly beyond half distance",
    )
    require(
        rows + kernel_dimension == support_size + 1,
        "row/kernel dimension identity failed",
    )
    if not selected_exact:
        return {
            "pairs": 0,
            "slopes": 0,
            "support_size": support_size,
            "kernel_dimension": kernel_dimension,
            "row_count": rows,
            "families": 0,
            "good_subsets": 0,
            "incidences": 0,
            "capacity": 0,
            "same_slope_excess": 0,
        }

    pencil = recurrence_pencil(
        line_base, direction, redundancy, support_size, p
    )
    pivot = maximal_pivot(pencil, support_size, p)
    require(pivot != [0], "actual exact pair but generic row rank dropped")
    determinants = stacked_determinants(
        pencil, domain, support_size, kernel_dimension, p
    )
    good = {
        roots: polynomial
        for roots, polynomial in determinants.items()
        if polynomial != [0]
    }
    require(good, "exact kernel has no evaluation basis")
    fixed = fixed_kernel_roots(domain, set(good))
    require(
        not fixed,
        "formal common domain root coexists with an exact selected error",
    )

    incidence_keys: set[tuple[int, tuple[int, ...]]] = set()
    incidences = 0
    slopes = {gamma for gamma, _ in selected_exact}
    for gamma, support in selected_exact:
        locator = half.constant_locator(support, p)
        specialized = specialized_recurrence(
            line_base,
            direction,
            gamma,
            redundancy,
            support_size,
            p,
        )
        require(
            rankdef.numeric_rank(specialized, p) == rows,
            "actual exact recurrence lost full row rank",
        )
        require(
            all(
                sum(row[column] * locator[column] for column in range(support_size + 1))
                % p
                == 0
                for row in specialized
            ),
            "actual exact locator missed its recurrence kernel",
        )
        direction_recurrence = [
            sum(
                direction[row + column] * locator[column]
                for column in range(support_size + 1)
            )
            % p
            for row in range(rows)
        ]
        require(
            any(direction_recurrence),
            "selected exact support became common to the line",
        )

        support_subsets = list(
            itertools.combinations(support, kernel_dimension)
        )
        require(
            all(
                half.poly_eval(determinants[roots], gamma, p) == 0
                for roots in support_subsets
            ),
            "actual exact locator missed a stacked-minor root",
        )
        good_inside = [roots for roots in support_subsets if roots in good]
        require(
            len(good_inside) >= rows,
            "support evaluation matroid has too few bases",
        )
        for roots in good_inside:
            key = (gamma, roots)
            require(
                key not in incidence_keys,
                "same-slope exact supports reused one evaluation basis",
            )
            incidence_keys.add(key)
        incidences += len(good_inside)

    capacity = 0
    for polynomial in good.values():
        roots = sum(
            half.poly_eval(polynomial, gamma, p) == 0
            for gamma in range(p)
        )
        require(
            roots <= len(polynomial) - 1 <= rows,
            "stacked minor exceeded its field-root capacity",
        )
        capacity += roots
    require(
        len(selected_exact) * rows <= incidences <= capacity,
        "exact evaluation-basis incidence count failed",
    )
    require(
        capacity <= comb(len(domain), kernel_dimension) * rows,
        "exact stacked-minor capacity exceeded the theorem budget",
    )
    require(
        len(selected_exact) <= comb(len(domain), kernel_dimension),
        "fixed-deficiency exact all-pair bound failed",
    )
    return {
        "pairs": len(selected_exact),
        "slopes": len(slopes),
        "support_size": support_size,
        "kernel_dimension": kernel_dimension,
        "row_count": rows,
        "families": 1,
        "good_subsets": len(good),
        "incidences": incidences,
        "capacity": capacity,
        "same_slope_excess": len(selected_exact) - len(slopes),
    }


def audit_half_core(
    p: int,
    domain: tuple[int, ...],
    budget: int,
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    selected: dict[int, tuple[first.Atom, ...]],
) -> dict[str, int]:
    core = [
        (gamma, atom)
        for gamma, atoms in selected.items()
        for atom in atoms
        if len(atom[0]) <= budget
    ]
    by_gamma: dict[int, list[first.Atom]] = defaultdict(list)
    for gamma, atom in core:
        by_gamma[gamma].append(atom)
    require(
        all(len(atoms) == 1 for atoms in by_gamma.values()),
        "two half-core errors share one syndrome",
    )
    rho, minor = rankdef.generic_hankel_rank(
        line_base, direction, budget, p
    )
    below = []
    exact = []
    for gamma, (support, _) in core:
        specialized = [
            [
                (
                    line_base[row + column]
                    + gamma * direction[row + column]
                )
                % p
                for column in range(budget)
            ]
            for row in range(budget)
        ]
        rank = rankdef.numeric_rank(specialized, p)
        require(rank == len(support), "half-core rank/weight mismatch")
        require(rank <= rho, "half-core specialization exceeded generic rank")
        if len(support) < rho:
            below.append(gamma)
        elif len(support) == rho:
            exact.append((gamma, support))
    require(
        all(half.poly_eval(minor, gamma, p) == 0 for gamma in below),
        "half-core rank drop missed the chosen minor",
    )
    require(
        len(below) <= len(minor) - 1 <= rho,
        "half-core minor root charge failed",
    )
    deflations = 0
    fixed = 0
    if rho > 0 and exact:
        row = rankdef.deflated_exact_weight_audit(
            p, domain, line_base, direction, rho, exact
        )
        deflations = 1
        fixed = int(row["fixed_roots"] > 0)
        require(
            len(exact) <= len(domain) - row["fixed_roots"],
            "half-core exact chart exceeded N-g",
        )
    require(
        len(core) <= len(domain) + rho <= len(domain) + budget,
        "half-core generic-rank bound failed",
    )
    return {
        "pairs": len(core),
        "rho": rho,
        "deflations": deflations,
        "fixed": fixed,
    }


def audit_line(
    p: int,
    domain: tuple[int, ...],
    t: int,
    deficiency: int,
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    sparse: first.SparseMultimap,
    spans: dict[tuple[int, ...], set[tuple[int, ...]]],
) -> dict[str, int]:
    redundancy = 2 * t - deficiency
    require(
        1 <= deficiency < t and redundancy <= len(domain),
        "invalid fixed-deficiency parameters",
    )
    selected = first.selected_atoms_on_line(
        p, line_base, direction, sparse, spans
    )
    half_budget = redundancy // 2
    core = audit_half_core(
        p,
        domain,
        half_budget,
        line_base,
        direction,
        selected,
    )
    high_rows = []
    for support_size in range(half_budget + 1, t + 1):
        exact = [
            (gamma, atom[0])
            for gamma, atoms in selected.items()
            for atom in atoms
            if len(atom[0]) == support_size
        ]
        high_rows.append(
            audit_exact_selected(
                p,
                domain,
                redundancy,
                support_size,
                line_base,
                direction,
                exact,
            )
        )
    pair_count = sum(len(atoms) for atoms in selected.values())
    high_pairs = sum(row["pairs"] for row in high_rows)
    require(
        pair_count == core["pairs"] + high_pairs,
        "half-core/high-stratum partition failed",
    )
    exact_budget = sum(
        comb(len(domain), 2 * support_size - redundancy + 1)
        for support_size in range(half_budget + 1, t + 1)
    )
    total_bound = len(domain) + half_budget + exact_budget
    require(pair_count <= total_bound, "fixed-deficiency total bound failed")
    return {
        "pairs": pair_count,
        "slopes": len(selected),
        "half_core_pairs": core["pairs"],
        "half_core_rho": core["rho"],
        "half_core_deflations": core["deflations"],
        "half_core_fixed": core["fixed"],
        "high_pairs": high_pairs,
        "high_families": sum(row["families"] for row in high_rows),
        "incidences": sum(row["incidences"] for row in high_rows),
        "capacity": sum(row["capacity"] for row in high_rows),
        "same_slope_excess": pair_count - len(selected),
        "bound": total_bound,
    }


def make_sampled_lines(
    p: int,
    dimension: int,
    sparse: first.SparseMultimap,
    t: int,
    count: int,
    seed: int,
) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    top_points = sorted(
        point
        for point, atoms in sparse.items()
        if any(len(atom[0]) == t for atom in atoms)
    )
    require(len(top_points) >= 2, "sample has fewer than two top points")
    rng = random.Random(seed)
    lines: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    while len(lines) < count * 2 // 3:
        first_point = top_points[rng.randrange(len(top_points))]
        second_point = top_points[rng.randrange(len(top_points))]
        if first_point != second_point:
            lines.add(half.canonical_line(first_point, second_point, p))
    directions = half.normalized_directions(p, dimension)
    while len(lines) < count:
        direction = directions[rng.randrange(len(directions))]
        pivot = next(index for index, value in enumerate(direction) if value)
        base = tuple(
            0 if index == pivot else rng.randrange(p)
            for index in range(dimension)
        )
        lines.add((base, direction))
    return sorted(lines)


def summarize_grid(
    p: int,
    domain: tuple[int, ...],
    t: int,
    deficiency: int,
    mode: str,
    count: int | None = None,
) -> dict[str, Any]:
    redundancy = 2 * t - deficiency
    weights = {x: (2 * x + 1) % p or 1 for x in domain}
    sparse, spans = first.build_sparse_multimap(
        p, domain, t, redundancy, weights
    )
    if mode == "exhaustive":
        lines: Iterable[tuple[tuple[int, ...], tuple[int, ...]]] = (
            first.exhaustive_lines(p, redundancy)
        )
    else:
        require(count is not None, "sample count missing")
        lines = make_sampled_lines(
            p,
            redundancy,
            sparse,
            t,
            count,
            20260714 + p * 10000 + t * 100 + deficiency,
        )
    line_count = 0
    pair_total = 0
    slope_total = 0
    core_total = 0
    high_total = 0
    family_total = 0
    incidence_total = 0
    capacity_total = 0
    same_slope = 0
    maximum_pairs = 0
    maximum_high = 0
    minimum_slack = None
    for line_base, direction in lines:
        result = audit_line(
            p,
            domain,
            t,
            deficiency,
            line_base,
            direction,
            sparse,
            spans,
        )
        line_count += 1
        pair_total += result["pairs"]
        slope_total += result["slopes"]
        core_total += result["half_core_pairs"]
        high_total += result["high_pairs"]
        family_total += result["high_families"]
        incidence_total += result["incidences"]
        capacity_total += result["capacity"]
        same_slope += result["same_slope_excess"]
        maximum_pairs = max(maximum_pairs, result["pairs"])
        maximum_high = max(maximum_high, result["high_pairs"])
        slack = result["bound"] - result["pairs"]
        minimum_slack = slack if minimum_slack is None else min(minimum_slack, slack)
    if mode == "exhaustive":
        expected = p ** (redundancy - 1) * (
            (p**redundancy - 1) // (p - 1)
        )
        require(line_count == expected, "exhaustive line census mismatch")
    half_budget = redundancy // 2
    high_bound = sum(
        comb(len(domain), 2 * support_size - redundancy + 1)
        for support_size in range(half_budget + 1, t + 1)
    )
    return {
        "mode": mode,
        "p": p,
        "domain": list(domain),
        "n": len(domain),
        "t": t,
        "deficiency": deficiency,
        "redundancy": redundancy,
        "half_budget": half_budget,
        "lines": line_count,
        "transverse_pairs": pair_total,
        "transverse_slopes": slope_total,
        "half_core_pairs": core_total,
        "high_pairs": high_total,
        "high_families": family_total,
        "good_basis_incidences": incidence_total,
        "root_capacity": capacity_total,
        "same_slope_excess": same_slope,
        "maximum_pairs_on_line": maximum_pairs,
        "maximum_high_pairs_on_line": maximum_high,
        "high_stratum_bound_sum": high_bound,
        "complete_bound": len(domain) + half_budget + high_bound,
        "minimum_complete_bound_slack": minimum_slack,
    }


def canonical_lagrange_fixture(deficiency: int) -> dict[str, Any]:
    p = 7
    domain = tuple(range(p))
    t = deficiency + 1
    redundancy = t + 1
    require(
        redundancy == 2 * t - deficiency,
        "canonical fixture deficiency identity failed",
    )
    line_base = tuple(
        1 if index == t - 1 else 0 for index in range(redundancy)
    )
    direction = tuple(
        1 if index == t else 0 for index in range(redundancy)
    )
    selected: list[tuple[int, tuple[int, ...]]] = []
    slope_histogram: dict[int, int] = defaultdict(int)
    for support in itertools.combinations(domain, t):
        amplitudes = []
        for x in support:
            denominator = 1
            for y in support:
                if y != x:
                    denominator = denominator * (x - y) % p
            amplitudes.append(pow(denominator, -1, p))
        moments = tuple(
            sum(
                amplitude * pow(x, degree, p)
                for x, amplitude in zip(support, amplitudes, strict=True)
            )
            % p
            for degree in range(redundancy)
        )
        gamma = sum(support) % p
        expected = tuple(
            (line_base[index] + gamma * direction[index]) % p
            for index in range(redundancy)
        )
        require(moments == expected, "Lagrange moment fixture changed")
        selected.append((gamma, support))
        slope_histogram[gamma] += 1
    row = audit_exact_selected(
        p,
        domain,
        redundancy,
        t,
        line_base,
        direction,
        selected,
    )
    kernel_dimension = deficiency + 1
    require(
        row["pairs"] == comb(len(domain), kernel_dimension),
        "canonical fixture missed the exact binomial bound",
    )
    return {
        "p": p,
        "domain": list(domain),
        "n": len(domain),
        "t": t,
        "deficiency": deficiency,
        "redundancy": redundancy,
        "kernel_dimension": kernel_dimension,
        "pairs": row["pairs"],
        "slopes": row["slopes"],
        "maximum_pairs_per_slope": max(slope_histogram.values()),
        "exact_bound": comb(len(domain), kernel_dimension),
        "all_supports_realized": True,
    }


def fixed_root_fixture() -> dict[str, Any]:
    p = 7
    domain = (0, 1, 2, 3, 4, 5)
    t = 4
    deficiency = 2
    redundancy = 2 * t - deficiency
    support_size = t
    row_count = redundancy - support_size
    common_support = tuple(range(row_count))
    weights = {x: (3 * x + 1) % p or 1 for x in domain}
    line_base = half.syndrome(
        domain,
        common_support,
        tuple(range(1, row_count + 1)),
        redundancy,
        p,
        weights,
    )
    direction = half.syndrome(
        domain,
        common_support,
        tuple(reversed(range(1, row_count + 1))),
        redundancy,
        p,
        weights,
    )
    pencil = recurrence_pencil(
        line_base, direction, redundancy, support_size, p
    )
    require(
        maximal_pivot(pencil, support_size, p) != [0],
        "fixed-root fixture lost generic row rank",
    )
    kernel_dimension = 2 * support_size - redundancy + 1
    determinants = stacked_determinants(
        pencil, domain, support_size, kernel_dimension, p
    )
    good = {
        roots for roots, polynomial in determinants.items()
        if polynomial != [0]
    }
    fixed = fixed_kernel_roots(domain, good)
    require(
        set(common_support) <= set(fixed),
        "fixed-root fixture lost its common roots",
    )
    sparse, spans = first.build_sparse_multimap(
        p, domain, t, redundancy, weights
    )
    selected = first.selected_atoms_on_line(
        p, line_base, direction, sparse, spans
    )
    exact = [
        atom
        for atoms in selected.values()
        for atom in atoms
        if len(atom[0]) == support_size
    ]
    require(not exact, "fixed-root fixture retained an exact top error")
    return {
        "p": p,
        "domain": list(domain),
        "n": len(domain),
        "t": t,
        "deficiency": deficiency,
        "redundancy": redundancy,
        "support_size": support_size,
        "kernel_dimension": kernel_dimension,
        "common_support": list(common_support),
        "fixed_kernel_roots": list(fixed),
        "transverse_exact_pairs": len(exact),
    }


def build_payload() -> dict[str, Any]:
    grids = [
        summarize_grid(5, (0, 1, 2, 3), 3, 2, "exhaustive"),
        summarize_grid(5, tuple(range(5)), 3, 2, "exhaustive"),
        summarize_grid(7, (0, 1, 2, 3, 4), 3, 2, "sample", 5000),
        summarize_grid(7, tuple(range(6)), 4, 2, "sample", 5000),
        summarize_grid(5, tuple(range(5)), 4, 3, "sample", 7000),
        summarize_grid(7, tuple(range(7)), 5, 3, "sample", 5000),
        summarize_grid(7, tuple(range(7)), 5, 4, "sample", 5000),
    ]
    sharp = [canonical_lagrange_fixture(d) for d in range(1, 6)]
    fixed = fixed_root_fixture()
    return {
        "schema_version": 1,
        "claim_id": CLAIM_ID,
        "base_commit": BASE_COMMIT,
        "status": "PROVED_AUDIT_WITH_UNPROVED_LEAN_TARGET",
        "hard_input": "3_fixed_deficiency_beyond_half_kernel_minors",
        "theorem": {
            "range": "N>=R=2t-d and 1<=d<t",
            "exact_stratum": (
                "kappa=2s-R+1>=2 implies "
                "|P_s|<=binom(N,kappa)"
            ),
            "half_core": (
                "s0=floor(R/2), "
                "|P_{<=s0}|<=N+rho0<=N+s0"
            ),
            "complete": (
                "|P|<=N+s0+sum_{s=s0+1}^t "
                "binom(N,2s-R+1)"
            ),
            "fixed_d_scale": "O_d(N^(d+1))",
            "mca_ca": "same complete numerator bound",
        },
        "grids": grids,
        "canonical_lagrange_sharp_fixtures": sharp,
        "fixed_root_fixture": fixed,
        "totals": {
            "audited_lines": sum(row["lines"] for row in grids),
            "transverse_pairs": sum(
                row["transverse_pairs"] for row in grids
            ),
            "transverse_slopes": sum(
                row["transverse_slopes"] for row in grids
            ),
            "high_pairs": sum(row["high_pairs"] for row in grids),
            "high_families": sum(row["high_families"] for row in grids),
            "good_basis_incidences": sum(
                row["good_basis_incidences"] for row in grids
            ),
            "root_capacity": sum(row["root_capacity"] for row in grids),
            "same_slope_excess": sum(
                row["same_slope_excess"] for row in grids
            ),
        },
        "nonclaims": [
            "no_uniform_subexponential_bound_when_d_grows_linearly",
            "no_bound_for_t_greater_than_or_equal_to_R",
            "no_claim_that_the_complete_sum_is_exact",
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
    bad["theorem"]["fixed_d_scale"] = "O_d(N^d)"
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["grids"][1]["maximum_high_pairs_on_line"] -= 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["canonical_lagrange_sharp_fixtures"][3]["pairs"] -= 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["fixed_root_fixture"]["transverse_exact_pairs"] += 1
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
        "FIXED_DEFICIENCY_KERNEL_MINOR_PASS "
        f"lines={totals['audited_lines']} "
        f"pairs={totals['transverse_pairs']} "
        f"high={totals['high_pairs']} "
        f"families={totals['high_families']} "
        f"incidences={totals['good_basis_incidences']} "
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
            "FIXED_DEFICIENCY_KERNEL_MINOR_TAMPER_PASS "
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
