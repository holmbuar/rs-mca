#!/usr/bin/env python3
"""Verify the half-distance Hankel/cofactor LineRay compiler."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import random
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


BASE_COMMIT = "c35a6da31ed0905afcbaaefe4eb0f242572ebb35"
CLAIM_ID = "half-distance-hankel-curve-lineray-v1"
ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = (
    ROOT
    / "experimental/data/certificates/half-distance-hankel-curve-lineray"
    / "half_distance_hankel_curve_lineray.json"
)


class VerificationError(RuntimeError):
    """Raised when a mathematical or certificate gate fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def payload_digest(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def trim(poly: list[int], p: int) -> list[int]:
    out = [value % p for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_add(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] = (out[index] + value) % p
    for index, value in enumerate(right):
        out[index] = (out[index] + value) % p
    return trim(out, p)


def poly_scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return trim([(scalar * value) % p for value in poly], p)


def poly_mul(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] = (out[i + j] + left_value * right_value) % p
    return trim(out, p)


def poly_eval(poly: list[int], value: int, p: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % p
    return result


def poly_divmod(
    numerator: list[int], denominator: list[int], p: int
) -> tuple[list[int], list[int]]:
    numerator = trim(numerator, p)
    denominator = trim(denominator, p)
    require(denominator != [0], "division by zero polynomial")
    if len(numerator) < len(denominator):
        return [0], numerator
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    inverse = pow(denominator[-1], -1, p)
    remainder = numerator[:]
    while remainder != [0] and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        coefficient = remainder[-1] * inverse % p
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            remainder[index + shift] = (
                remainder[index + shift] - coefficient * value
            ) % p
        remainder = trim(remainder, p)
    return trim(quotient, p), remainder


def poly_gcd(left: list[int], right: list[int], p: int) -> list[int]:
    left = trim(left, p)
    right = trim(right, p)
    while right != [0]:
        _, remainder = poly_divmod(left, right, p)
        left, right = right, remainder
    if left == [0]:
        return [0]
    return poly_scale(left, pow(left[-1], -1, p), p)


def polynomial_vector_gcd(polys: list[list[int]], p: int) -> list[int]:
    nonzero = [trim(poly, p) for poly in polys if trim(poly, p) != [0]]
    require(nonzero, "zero cofactor vector over F[z]")
    result = nonzero[0]
    for poly in nonzero[1:]:
        result = poly_gcd(result, poly, p)
    return result


def determinant_poly(matrix: list[list[list[int]]], p: int) -> list[int]:
    size = len(matrix)
    if size == 0:
        return [1]
    require(all(len(row) == size for row in matrix), "nonsquare determinant")
    result = [0]
    for permutation in itertools.permutations(range(size)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(size)
            for j in range(i + 1, size)
        )
        term = [1]
        for row, column in enumerate(permutation):
            term = poly_mul(term, matrix[row][column], p)
        result = poly_add(
            result,
            poly_scale(term, -1 if inversions % 2 else 1, p),
            p,
        )
    return result


def constant_locator(roots: Iterable[int], p: int) -> list[int]:
    locator = [1]
    for root in roots:
        out = [0] * (len(locator) + 1)
        for index, value in enumerate(locator):
            out[index] = (out[index] - root * value) % p
            out[index + 1] = (out[index + 1] + value) % p
        locator = out
    return locator


def locator_value_polynomial(
    coefficient_polys: list[list[int]], x: int, p: int
) -> list[int]:
    result = [0]
    power = 1
    for coefficient in coefficient_polys:
        result = poly_add(result, poly_scale(coefficient, power, p), p)
        power = power * x % p
    return trim(result, p)


def cofactor_locator(
    base: tuple[int, ...],
    direction: tuple[int, ...],
    support_size: int,
    p: int,
) -> list[list[int]]:
    matrix = [
        [
            trim([base[row + column], direction[row + column]], p)
            for column in range(support_size + 1)
        ]
        for row in range(support_size)
    ]
    cofactors = []
    for deleted in range(support_size + 1):
        minor = [
            [entry for column, entry in enumerate(row) if column != deleted]
            for row in matrix
        ]
        determinant = determinant_poly(minor, p)
        cofactors.append(
            poly_scale(determinant, -1 if deleted % 2 else 1, p)
        )
    divisor = polynomial_vector_gcd(cofactors, p)
    primitive = []
    for coefficient in cofactors:
        if coefficient == [0]:
            primitive.append([0])
            continue
        quotient, remainder = poly_divmod(coefficient, divisor, p)
        require(remainder == [0], "cofactor content did not divide")
        primitive.append(quotient)
    return primitive


def syndrome(
    domain: tuple[int, ...],
    support: tuple[int, ...],
    amplitudes: tuple[int, ...],
    redundancy: int,
    p: int,
    column_weights: dict[int, int],
) -> tuple[int, ...]:
    amplitude_by_x = dict(zip(support, amplitudes, strict=True))
    return tuple(
        sum(
            amplitude_by_x.get(x, 0)
            * column_weights[x]
            * pow(x, degree, p)
            for x in domain
        )
        % p
        for degree in range(redundancy)
    )


def lagrange_weights(support: tuple[int, ...], p: int) -> dict[int, int]:
    weights: dict[int, int] = {}
    for x in support:
        derivative = 1
        for y in support:
            if x != y:
                derivative = derivative * (x - y) % p
        require(derivative != 0, "distinct roots gave zero derivative")
        weights[x] = pow(derivative, -1, p)
    return weights


def build_sparse_syndromes(
    p: int,
    domain: tuple[int, ...],
    t: int,
    redundancy: int,
    column_weights: dict[int, int],
) -> tuple[
    dict[tuple[int, ...], tuple[tuple[int, ...], tuple[int, ...]]],
    dict[tuple[int, ...], set[tuple[int, ...]]],
]:
    require(len(domain) >= redundancy >= 2 * t, "invalid half-distance row")
    sparse: dict[
        tuple[int, ...], tuple[tuple[int, ...], tuple[int, ...]]
    ] = {}
    spans: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
    for size in range(t + 1):
        for support in itertools.combinations(domain, size):
            spans[support] = {
                syndrome(
                    domain,
                    support,
                    tuple(coefficients),
                    redundancy,
                    p,
                    column_weights,
                )
                for coefficients in itertools.product(range(p), repeat=size)
            }
            amplitude_rows = (
                [()]
                if size == 0
                else itertools.product(range(1, p), repeat=size)
            )
            for amplitudes_raw in amplitude_rows:
                amplitudes = tuple(amplitudes_raw)
                value = syndrome(
                    domain,
                    support,
                    amplitudes,
                    redundancy,
                    p,
                    column_weights,
                )
                atom = (support, amplitudes)
                require(
                    value not in sparse or sparse[value] == atom,
                    "two weight-at-most-t errors share a syndrome",
                )
                sparse[value] = atom
    return sparse, spans


def normalized_directions(p: int, dimension: int) -> list[tuple[int, ...]]:
    directions = []
    for vector in itertools.product(range(p), repeat=dimension):
        if not any(vector):
            continue
        pivot = next(index for index, value in enumerate(vector) if value)
        if vector[pivot] == 1:
            directions.append(tuple(vector))
    expected = (p**dimension - 1) // (p - 1)
    require(len(directions) == expected, "projective direction census failed")
    return directions


def canonical_line(
    first: tuple[int, ...], second: tuple[int, ...], p: int
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    raw_direction = tuple((b - a) % p for a, b in zip(first, second))
    require(any(raw_direction), "two points do not determine a line")
    pivot = next(
        index for index, value in enumerate(raw_direction) if value
    )
    inverse = pow(raw_direction[pivot], -1, p)
    direction = tuple(value * inverse % p for value in raw_direction)
    scalar = first[pivot]
    base = tuple(
        (value - scalar * direction[index]) % p
        for index, value in enumerate(first)
    )
    require(base[pivot] == 0 and direction[pivot] == 1, "line normalization")
    return base, direction


def audit_cofactor_family(
    p: int,
    domain: tuple[int, ...],
    base: tuple[int, ...],
    direction: tuple[int, ...],
    support_size: int,
    selected: list[tuple[int, tuple[int, ...]]],
) -> dict[str, int]:
    require(selected, "empty cofactor family")
    cofactors = cofactor_locator(base, direction, support_size, p)
    degree = max(len(coefficient) - 1 for coefficient in cofactors)
    require(degree <= support_size, "cofactor curve degree exceeded s")

    fixed_roots = tuple(
        x
        for x in domain
        if locator_value_polynomial(cofactors, x, p) == [0]
    )
    g = len(fixed_roots)
    require(g <= support_size, "too many formal common roots")
    fixed_set = set(fixed_roots)
    seen_supports: set[tuple[int, ...]] = set()
    seen_parameters: set[int] = set()

    for gamma, support in selected:
        specialized = [poly_eval(coefficient, gamma, p) for coefficient in cofactors]
        require(any(specialized), "actual error landed at cofactor rank drop")
        require(
            specialized[-1] != 0,
            "exact support produced a lower-degree cofactor locator",
        )
        inverse = pow(specialized[-1], -1, p)
        monic = [value * inverse % p for value in specialized]
        require(
            monic == constant_locator(support, p),
            "cofactor locator did not recover the actual support",
        )
        require(g == len(fixed_set.intersection(support)), "formal root missing")
        require(support not in seen_supports, "transverse support repeated")
        require(gamma not in seen_parameters, "parameter repeated")
        seen_supports.add(support)
        seen_parameters.add(gamma)

    if g == support_size:
        require(len(selected) <= 1, "constant locator violates transversality")
        capacity = 1
        incidences = 0
    else:
        moving = support_size - g
        incidences = len(selected) * moving
        capacity = 0
        measured = 0
        for x in domain:
            if x in fixed_set:
                continue
            value_poly = locator_value_polynomial(cofactors, x, p)
            require(value_poly != [0], "nonfixed evaluation vanished formally")
            root_count = sum(
                poly_eval(value_poly, gamma, p) == 0 for gamma in range(p)
            )
            require(
                root_count <= len(value_poly) - 1,
                "evaluation polynomial has too many field roots",
            )
            capacity += degree
            measured += sum(x in support for _, support in selected)
        require(measured == incidences, "moving incidence recount failed")
        require(incidences <= capacity, "cofactor moving-root capacity failed")
        require(
            len(selected) * moving <= (len(domain) - g) * degree,
            "sharp cofactor curve inequality failed",
        )

    require(
        len(selected) <= len(domain) * support_size,
        "coarse Ns exact-weight bound failed",
    )
    return {
        "degree": degree,
        "fixed_roots": g,
        "selected": len(selected),
        "incidences": incidences,
        "capacity": capacity,
    }


def audit_line(
    p: int,
    domain: tuple[int, ...],
    t: int,
    base: tuple[int, ...],
    direction: tuple[int, ...],
    sparse: dict[
        tuple[int, ...], tuple[tuple[int, ...], tuple[int, ...]]
    ],
    spans: dict[tuple[int, ...], set[tuple[int, ...]]],
) -> dict[str, Any]:
    selected_by_weight: dict[int, list[tuple[int, tuple[int, ...]]]] = (
        defaultdict(list)
    )
    for gamma in range(p):
        point = tuple(
            (base[index] + gamma * direction[index]) % p
            for index in range(len(base))
        )
        atom = sparse.get(point)
        if atom is None:
            continue
        support, _ = atom
        if direction in spans[support]:
            continue
        selected_by_weight[len(support)].append((gamma, support))

    require(
        len(selected_by_weight.get(0, [])) <= 1,
        "zero error occurs at two parameters",
    )
    cofactor_rows = []
    for support_size, selected in selected_by_weight.items():
        if support_size == 0:
            continue
        cofactor_rows.append(
            audit_cofactor_family(
                p,
                domain,
                base,
                direction,
                support_size,
                selected,
            )
        )

    pair_count = sum(len(selected) for selected in selected_by_weight.values())
    bound = 1 + len(domain) * t * (t + 1) // 2
    require(pair_count <= bound, "all-weight half-distance bound failed")
    return {
        "pair_count": pair_count,
        "by_weight": {
            str(weight): len(selected)
            for weight, selected in sorted(selected_by_weight.items())
        },
        "cofactor_rows": cofactor_rows,
    }


def exhaustive_line_grid(
    p: int, domain: tuple[int, ...], t: int
) -> dict[str, Any]:
    redundancy = 2 * t
    column_weights = {x: 1 for x in domain}
    sparse, spans = build_sparse_syndromes(
        p, domain, t, redundancy, column_weights
    )
    directions = normalized_directions(p, redundancy)

    line_count = 0
    lines_with_pairs = 0
    pair_total = 0
    maximum_pairs = 0
    maximum_by_weight: dict[str, int] = defaultdict(int)
    cofactor_families = 0
    fixed_root_families = 0
    maximum_curve_degree = 0

    for direction in directions:
        pivot = next(index for index, value in enumerate(direction) if value)
        free_indices = [index for index in range(redundancy) if index != pivot]
        for values in itertools.product(range(p), repeat=redundancy - 1):
            base_list = [0] * redundancy
            for index, value in zip(free_indices, values, strict=True):
                base_list[index] = value
            result = audit_line(
                p,
                domain,
                t,
                tuple(base_list),
                direction,
                sparse,
                spans,
            )
            line_count += 1
            count = result["pair_count"]
            pair_total += count
            maximum_pairs = max(maximum_pairs, count)
            if count:
                lines_with_pairs += 1
            for weight, value in result["by_weight"].items():
                maximum_by_weight[weight] = max(maximum_by_weight[weight], value)
            for row in result["cofactor_rows"]:
                cofactor_families += 1
                fixed_root_families += row["fixed_roots"] > 0
                maximum_curve_degree = max(maximum_curve_degree, row["degree"])

    expected_lines = p ** (redundancy - 1) * (
        (p**redundancy - 1) // (p - 1)
    )
    require(line_count == expected_lines, "affine line census mismatch")
    return {
        "p": p,
        "domain": list(domain),
        "n": len(domain),
        "t": t,
        "redundancy": redundancy,
        "sparse_syndromes": len(sparse),
        "affine_lines": line_count,
        "lines_with_transverse_pairs": lines_with_pairs,
        "transverse_pair_incidences": pair_total,
        "maximum_pairs_on_line": maximum_pairs,
        "maximum_by_exact_weight": dict(sorted(maximum_by_weight.items())),
        "theorem_bound": 1 + len(domain) * t * (t + 1) // 2,
        "cofactor_families": cofactor_families,
        "fixed_root_families": fixed_root_families,
        "maximum_curve_degree": maximum_curve_degree,
    }


def sampled_weight_three_grid(redundancy: int) -> dict[str, Any]:
    p = 7
    domain = tuple(range(p))
    t = 3
    column_weights = {x: (x + 1) % p or 1 for x in domain}
    sparse, spans = build_sparse_syndromes(
        p, domain, t, redundancy, column_weights
    )
    points = sorted(sparse)
    rng = random.Random(20260714 + redundancy)
    lines: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()

    while len(lines) < 5000:
        first = points[rng.randrange(len(points))]
        second = points[rng.randrange(len(points))]
        if first != second:
            lines.add(canonical_line(first, second, p))
    directions = normalized_directions(p, redundancy)
    while len(lines) < 8000:
        direction = directions[rng.randrange(len(directions))]
        pivot = next(index for index, value in enumerate(direction) if value)
        base = tuple(
            0 if index == pivot else rng.randrange(p)
            for index in range(redundancy)
        )
        lines.add((base, direction))

    pair_total = 0
    maximum_pairs = 0
    cofactor_families = 0
    fixed_root_families = 0
    maximum_curve_degree = 0
    maximum_by_weight: dict[str, int] = defaultdict(int)
    for base, direction in sorted(lines):
        result = audit_line(
            p, domain, t, base, direction, sparse, spans
        )
        pair_total += result["pair_count"]
        maximum_pairs = max(maximum_pairs, result["pair_count"])
        for weight, value in result["by_weight"].items():
            maximum_by_weight[weight] = max(maximum_by_weight[weight], value)
        for row in result["cofactor_rows"]:
            cofactor_families += 1
            fixed_root_families += row["fixed_roots"] > 0
            maximum_curve_degree = max(maximum_curve_degree, row["degree"])

    return {
        "p": p,
        "domain": list(domain),
        "n": len(domain),
        "t": t,
        "redundancy": redundancy,
        "column_weights": [column_weights[x] for x in domain],
        "sparse_syndromes": len(sparse),
        "sampled_lines": len(lines),
        "transverse_pair_incidences": pair_total,
        "maximum_pairs_on_line": maximum_pairs,
        "maximum_by_exact_weight": dict(sorted(maximum_by_weight.items())),
        "theorem_bound": 1 + len(domain) * t * (t + 1) // 2,
        "cofactor_families": cofactor_families,
        "fixed_root_families": fixed_root_families,
        "maximum_curve_degree": maximum_curve_degree,
    }


def cyclotomic_endpoint_fixture() -> dict[str, Any]:
    p = 13
    t = 3
    redundancy = 2 * t
    domain = tuple(range(1, p))
    base = (0, 0, 1, 0, 0, 0)
    direction = (0, 0, 0, 1, 0, 0)
    mu = tuple(x for x in domain if pow(x, t + 1, p) == 1)
    require(len(mu) == t + 1, "cyclotomic subgroup size mismatch")
    selected = []
    for gamma in domain:
        support = tuple(
            sorted({(-gamma * root) % p for root in mu if root != 1})
        )
        weights = lagrange_weights(support, p)
        row = tuple(
            sum(weights[x] * pow(x, degree, p) for x in support) % p
            for degree in range(redundancy)
        )
        target = tuple(
            (base[index] + gamma * direction[index]) % p
            for index in range(redundancy)
        )
        require(row == target, "cyclotomic endpoint syndrome mismatch")
        selected.append((gamma, support))
    curve = audit_cofactor_family(
        p, domain, base, direction, t, selected
    )
    require(curve["selected"] == len(domain), "endpoint N lower bound failed")
    return {
        "p": p,
        "n": len(domain),
        "t": t,
        "redundancy": redundancy,
        "pairs": curve["selected"],
        "curve_degree": curve["degree"],
        "fixed_roots": curve["fixed_roots"],
        "moving_incidences": curve["incidences"],
        "root_capacity": curve["capacity"],
        "universal_N_lower_bound_attained": curve["selected"] == len(domain),
    }


def tangent_rejection_fixture() -> dict[str, Any]:
    p = 7
    domain = tuple(range(p))
    t = 2
    redundancy = 2 * t
    column_weights = {x: 1 for x in domain}
    sparse, spans = build_sparse_syndromes(
        p, domain, t, redundancy, column_weights
    )
    support = (1, 2)
    base = syndrome(domain, support, (1, 1), redundancy, p, column_weights)
    direction = syndrome(
        domain, support, (1, 2), redundancy, p, column_weights
    )
    result = audit_line(
        p, domain, t, base, direction, sparse, spans
    )
    close_parameters = 0
    common_support_parameters = 0
    transverse_supports = []
    for gamma in range(p):
        point = tuple(
            (base[index] + gamma * direction[index]) % p
            for index in range(redundancy)
        )
        close_parameters += point in sparse
        atom = sparse.get(point)
        require(atom is not None, "tangent point left the sparse shell")
        actual_support, _ = atom
        if direction in spans[actual_support]:
            common_support_parameters += 1
        else:
            transverse_supports.append(actual_support)
    require(close_parameters == p, "tangent line is not entirely sparse")
    require(
        common_support_parameters == p - 2,
        "full-support tangent parameters were not rejected",
    )
    require(
        transverse_supports == [(1,), (2,)],
        "amplitude-cancellation tangent ratios changed",
    )
    require(
        result["pair_count"] == 2,
        "lower-weight tangent ratios were not retained",
    )
    return {
        "p": p,
        "n": len(domain),
        "t": t,
        "redundancy": redundancy,
        "close_parameters": close_parameters,
        "common_support_parameters_rejected": common_support_parameters,
        "transverse_pairs": result["pair_count"],
        "transverse_supports": [list(row) for row in transverse_supports],
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
        exhaustive_line_grid(p, domain, t)
        for p, domain, t in exhaustive_specs
    ]
    sampled = [
        sampled_weight_three_grid(6),
        sampled_weight_three_grid(7),
    ]
    cyclotomic = cyclotomic_endpoint_fixture()
    tangent = tangent_rejection_fixture()
    return {
        "schema_version": 1,
        "claim_id": CLAIM_ID,
        "base_commit": BASE_COMMIT,
        "status": "PROVED_AUDIT_WITH_UNPROVED_LEAN_TARGET",
        "hard_input": "3_half_distance_transverse_hankel_curve_compiler",
        "theorem": {
            "dimension_range": "N>=R>=2t",
            "all_pair_bound": "1+N*t*(t+1)/2",
            "exact_weight_bound": "|P_s|<=N*s",
            "rank_drop": "impossible_for_actual_exact_weight_s_error",
            "assumptions": ["transverse_support", "weighted_GRS_moment_columns"],
            "field_dependence": "none",
        },
        "exhaustive_line_grids": exhaustive,
        "sampled_weight_three_grids": sampled,
        "cyclotomic_endpoint_fixture": cyclotomic,
        "tangent_rejection_fixture": tangent,
        "totals": {
            "exhaustive_affine_lines": sum(
                row["affine_lines"] for row in exhaustive
            ),
            "exhaustive_pair_incidences": sum(
                row["transverse_pair_incidences"] for row in exhaustive
            ),
            "sampled_lines": sum(row["sampled_lines"] for row in sampled),
            "sampled_pair_incidences": sum(
                row["transverse_pair_incidences"] for row in sampled
            ),
            "cofactor_families": sum(
                row["cofactor_families"] for row in exhaustive + sampled
            )
            + 1,
            "fixed_root_families": sum(
                row["fixed_root_families"] for row in exhaustive + sampled
            ),
            "sharp_endpoint_pairs": cyclotomic["pairs"],
        },
        "prior_work_boundary": [
            "BCHKS_stronger_in_strict_range_2t<R_under_its_hypotheses",
            "repository_SPI_deficiency_one_is_domain_specific",
            "new_claim_is_self_contained_polynomial_endpoint_and_all_weights",
        ],
        "nonclaims": [
            "no_bound_beyond_half_distance_R<2t",
            "no_exact_t_plus_one_endpoint_staircase",
            "no_atlas_or_profile_envelope",
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
    bad["theorem"]["all_pair_bound"] = "N"
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["exhaustive_line_grids"][2]["maximum_pairs_on_line"] += 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["cyclotomic_endpoint_fixture"]["pairs"] -= 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["tangent_rejection_fixture"]["transverse_pairs"] = 1
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
        "HALF_DISTANCE_HANKEL_CURVE_LINERAY_PASS "
        f"lines={totals['exhaustive_affine_lines']} "
        f"pairs={totals['exhaustive_pair_incidences']} "
        f"sampled={totals['sampled_lines']} "
        f"cofactors={totals['cofactor_families']} "
        f"fixed={totals['fixed_root_families']} "
        f"sharp={totals['sharp_endpoint_pairs']}"
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
            "HALF_DISTANCE_HANKEL_CURVE_LINERAY_TAMPER_PASS "
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
