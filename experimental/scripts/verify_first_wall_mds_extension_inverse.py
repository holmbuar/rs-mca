#!/usr/bin/env python3
"""Deterministically verify the first-wall MDS extension/inverse packet."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Sequence


SCHEMA = "first_wall_mds_extension_inverse.v1"
BASE_COMMIT = "7f278167e1e51f968896229ae438ea5a76398f90"
SCRIPT_RELATIVE = Path("experimental/scripts/verify_first_wall_mds_extension_inverse.py")
NOTE_RELATIVE = Path("experimental/notes/thresholds/first_wall_mds_extension_inverse.md")
DEFAULT_CERTIFICATE = Path(
    "experimental/data/certificates/first-wall-mds-extension-inverse/"
    "first_wall_mds_extension_inverse.json"
)
PERTURBATION_PRIMES = (5, 7, 11, 13)
EXPECTED_OWNER_LEDGER_SHA256 = {
    "mds_extension": "14d832a5bcad690498063f37791fbabdb05f36e339a8d1296db21b587694eca3",
    "collision_extension": "0841c4e63cb0d53bfc1ba8c52d8def4ad7a1f8fdb7d208243e8dc940e9438803",
}
EXPECTED_GRAPH_DIGESTS = {
    5: {
        "arc_function_sha256": "a9f2a485b423d7e1d036490cf868267f7de93c4327bcf474abee14b830f3ccfe",
        "coefficient_crosswalk_sha256": "0affd7094f45adbdb830eb398cfb0dca7b07747b5fc0b5dcde03940c2e33a5ad",
    },
    7: {
        "arc_function_sha256": "8cfce0a0d41d18b9b7b3c06f0970d14b1d8ea8f83063195e7ef2ae6317257d8b",
        "coefficient_crosswalk_sha256": "79043cea560cb49c77a1eb64b701aa8287648864bd6c4609296a55bcc39cdc22",
    },
}


class VerificationError(RuntimeError):
    """Raised when a mathematical or certificate invariant fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def repository_root() -> Path:
    root = Path(__file__).resolve().parents[2]
    require((root / SCRIPT_RELATIVE).resolve() == Path(__file__).resolve(), "unexpected script path")
    return root


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def object_sha256(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def with_payload_hash(payload: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(payload)
    result["payload_sha256"] = object_sha256(result)
    return result


def refresh_payload_hash(payload: dict[str, Any]) -> None:
    payload.pop("payload_sha256", None)
    payload["payload_sha256"] = object_sha256(payload)


def histogram(values: Iterable[int]) -> dict[str, int]:
    counts = Counter(values)
    return {str(key): counts[key] for key in sorted(counts)}


def inverse_mod(value: int, prime: int) -> int:
    reduced = value % prime
    require(reduced != 0, "attempted to invert zero")
    return pow(reduced, -1, prime)


def rank_mod(rows: Sequence[Sequence[int]], prime: int) -> int:
    if not rows:
        return 0
    width = len(rows[0])
    require(all(len(row) == width for row in rows), "ragged matrix")
    matrix = [[entry % prime for entry in row] for row in rows]
    pivot_row = 0
    for column in range(width):
        pivot = next(
            (row for row in range(pivot_row, len(matrix)) if matrix[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = inverse_mod(matrix[pivot_row][column], prime)
        matrix[pivot_row] = [(scale * entry) % prime for entry in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row:
                continue
            factor = matrix[row][column]
            if factor:
                matrix[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(matrix[row], matrix[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


def solve_square_mod(matrix: Sequence[Sequence[int]], rhs: Sequence[int], prime: int) -> tuple[int, ...]:
    size = len(matrix)
    require(size == len(rhs), "square solve has incompatible right-hand side")
    require(all(len(row) == size for row in matrix), "square solve has nonsquare matrix")
    augmented = [
        [entry % prime for entry in row] + [rhs_value % prime]
        for row, rhs_value in zip(matrix, rhs)
    ]
    for column in range(size):
        pivot = next((row for row in range(column, size) if augmented[row][column]), None)
        require(pivot is not None, "singular interpolation matrix")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = inverse_mod(augmented[column][column], prime)
        augmented[column] = [(scale * entry) % prime for entry in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(augmented[row], augmented[column])
                ]
    return tuple(augmented[row][-1] for row in range(size))


def evaluate_monomial(exponent: int, points: Sequence[int], prime: int) -> tuple[int, ...]:
    return tuple(pow(point, exponent, prime) for point in points)


def linear_combination(
    basis: Sequence[Sequence[int]], coefficients: Sequence[int], prime: int
) -> tuple[int, ...]:
    require(len(basis) == len(coefficients), "linear combination has incompatible dimensions")
    if not basis:
        return tuple()
    length = len(basis[0])
    require(all(len(word) == length for word in basis), "basis has ragged words")
    return tuple(
        sum(coefficient * basis_word[index] for coefficient, basis_word in zip(coefficients, basis))
        % prime
        for index in range(length)
    )


def add_words(left: Sequence[int], right: Sequence[int], prime: int) -> tuple[int, ...]:
    require(len(left) == len(right), "word addition has incompatible lengths")
    return tuple((x + y) % prime for x, y in zip(left, right))


def zero_set(word: Sequence[int]) -> tuple[int, ...]:
    return tuple(index for index, value in enumerate(word) if value == 0)


def minimum_distance(basis: Sequence[Sequence[int]], prime: int) -> int:
    require(bool(basis), "empty code basis")
    length = len(basis[0])
    best = length + 1
    for coefficients in itertools.product(range(prime), repeat=len(basis)):
        if not any(coefficients):
            continue
        word = linear_combination(basis, coefficients, prime)
        best = min(best, sum(value != 0 for value in word))
    require(best <= length, "code contained no nonzero word")
    return best


def enumerate_coset(
    offset: Sequence[int], basis: Sequence[Sequence[int]], prime: int
) -> Iterable[tuple[int, ...]]:
    for coefficients in itertools.product(range(prime), repeat=len(basis)):
        yield add_words(offset, linear_combination(basis, coefficients, prime), prime)


def interpolate_word(
    target: Sequence[int], basis: Sequence[Sequence[int]], indices: Sequence[int], prime: int
) -> tuple[int, ...]:
    require(len(basis) == len(indices), "interpolation needs one point per basis vector")
    matrix = [[basis_column[index] for basis_column in basis] for index in indices]
    coefficients = solve_square_mod(matrix, [target[index] for index in indices], prime)
    return linear_combination(basis, coefficients, prime)


def secant_family(function: Sequence[int], prime: int) -> dict[tuple[int, int], tuple[int, ...]]:
    blocks: dict[tuple[int, int], tuple[int, ...]] = {}
    for slope in range(prime):
        for intercept in range(prime):
            zeros = tuple(
                x for x in range(prime) if (function[x] - slope * x - intercept) % prime == 0
            )
            if len(zeros) >= 2:
                blocks[(slope, intercept)] = zeros
    return blocks


def quadratic_functions(prime: int) -> dict[tuple[int, ...], tuple[int, int, int]]:
    functions: dict[tuple[int, ...], tuple[int, int, int]] = {}
    for leading in range(1, prime):
        for linear in range(prime):
            for constant in range(prime):
                function = tuple(
                    (leading * x * x + linear * x + constant) % prime for x in range(prime)
                )
                require(function not in functions, "two nondegenerate quadratics define the same function")
                functions[function] = (leading, linear, constant)
    return functions


def is_graph_arc(function: Sequence[int], prime: int) -> bool:
    for x, y, z in itertools.combinations(range(prime), 3):
        left = (function[y] - function[x]) * (z - x)
        right = (function[z] - function[x]) * (y - x)
        if (left - right) % prime == 0:
            return False
    return True


def verify_local_gamma(
    prime: int,
    kappa_basis: Sequence[Sequence[int]],
    b0: Sequence[int],
    b1: Sequence[int],
    extension_rows: Sequence[Sequence[int]],
) -> dict[str, Any]:
    kappa = len(kappa_basis)
    length = len(b0)
    image_sizes: list[int] = []
    collision_pair_count = 0
    injective_core_count = 0
    collision_examples: list[dict[str, Any]] = []
    core_count = 0

    for core in itertools.combinations(range(length), kappa):
        core_count += 1
        interpolant0 = interpolate_word(b0, kappa_basis, core, prime)
        interpolant1 = interpolate_word(b1, kappa_basis, core, prime)
        u0 = tuple((value - interpolant) % prime for value, interpolant in zip(b0, interpolant0))
        u1 = tuple((value - interpolant) % prime for value, interpolant in zip(b1, interpolant1))
        require(zero_set(u1) == core, "u1 has zeros beyond its interpolation core")

        outside = tuple(index for index in range(length) if index not in core)
        gamma = {
            index: (-u0[index] * inverse_mod(u1[index], prime)) % prime for index in outside
        }
        fibers: dict[int, list[int]] = defaultdict(list)
        for index, value in gamma.items():
            fibers[value].append(index)
        image_sizes.append(len(fibers))
        if len(fibers) == len(outside):
            injective_core_count += 1

        for value, fiber in sorted(fibers.items()):
            combined = tuple((left + value * right) % prime for left, right in zip(u0, u1))
            expected_zeros = set(core) | set(fiber)
            require(set(zero_set(combined)) == expected_zeros, "Gamma fiber identity failed")

        for left, right in itertools.combinations(outside, 2):
            is_collision = gamma[left] == gamma[right]
            restriction = tuple(sorted(core + (left, right)))
            is_dependent = rank_mod([extension_rows[index] for index in restriction], prime) < kappa + 2
            require(is_collision == is_dependent, "Gamma collision/rank equivalence failed")
            if is_collision:
                collision_pair_count += 1
                if len(collision_examples) < 8:
                    collision_examples.append(
                        {
                            "core": list(core),
                            "points": [left, right],
                            "gamma": gamma[left],
                            "dependent_restriction": list(restriction),
                        }
                    )

    return {
        "core_count": core_count,
        "injective_core_count": injective_core_count,
        "all_injective": injective_core_count == core_count,
        "image_size_histogram": histogram(image_sizes),
        "collision_pair_count": collision_pair_count,
        "collision_examples": collision_examples,
        "fiber_identity_checked": True,
        "rank_collision_equivalence_checked": True,
    }


def verify_general_fixture(name: str, b0_exponent: int, expect_mds_extension: bool) -> dict[str, Any]:
    prime = 11
    points = tuple(range(8))
    length = len(points)
    kappa = 3
    redundancy = length - kappa
    first_wall = redundancy - 1
    extension_dimension = kappa + 1

    kappa_basis = [evaluate_monomial(exponent, points, prime) for exponent in range(kappa)]
    b1 = evaluate_monomial(kappa, points, prime)
    l_basis = kappa_basis + [b1]
    b0 = evaluate_monomial(b0_exponent, points, prime)
    m_basis = l_basis + [b0]

    k_distance = minimum_distance(kappa_basis, prime)
    l_distance = minimum_distance(l_basis, prime)
    m_distance = minimum_distance(m_basis, prime)
    require(k_distance == redundancy + 1, "K is not the expected MDS code")
    require(l_distance == redundancy, "L is not the expected MDS extension")

    l_rows = [[b1[index]] + [basis_word[index] for basis_word in kappa_basis] for index in range(length)]
    require(
        all(
            rank_mod([l_rows[index] for index in restriction], prime) == extension_dimension
            for restriction in itertools.combinations(range(length), extension_dimension)
        ),
        "an extension-dimension restriction of L is singular",
    )

    extension_rows = [
        [b0[index], b1[index]] + [basis_word[index] for basis_word in kappa_basis]
        for index in range(length)
    ]
    dependent_restrictions = [
        restriction
        for restriction in itertools.combinations(range(length), extension_dimension + 1)
        if rank_mod([extension_rows[index] for index in restriction], prime) < extension_dimension + 1
    ]

    owner_map: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for owner in itertools.combinations(range(length), extension_dimension):
        matrix = [[basis_word[index] for basis_word in l_basis] for index in owner]
        coefficients = solve_square_mod(matrix, [(-b0[index]) % prime for index in owner], prime)
        error = add_words(b0, linear_combination(l_basis, coefficients, prime), prime)
        require(all(error[index] == 0 for index in owner), "interpolated error misses its owner")
        owner_map[error].append(owner)

    coset_words = list(enumerate_coset(b0, l_basis, prime))
    coset_distance = min(sum(value != 0 for value in word) for word in coset_words)
    p_full = {word for word in coset_words if len(zero_set(word)) >= extension_dimension}
    require(set(owner_map) == p_full, "interpolated-owner image differs from P_full")

    owner_encoding: list[dict[str, Any]] = []
    for error in sorted(p_full):
        zeros = zero_set(error)
        expected_owners = set(itertools.combinations(zeros, extension_dimension))
        observed_owners = set(owner_map[error])
        require(observed_owners == expected_owners, "owner fiber is not all r-subsets of the zero set")
        owner_encoding.append(
            {
                "error": list(error),
                "owners": [list(owner) for owner in sorted(observed_owners)],
            }
        )

    universe_face_count = math.comb(length, extension_dimension)
    charge = sum(math.comb(len(zero_set(error)), extension_dimension) for error in p_full)
    require(charge == universe_face_count, "owner charge does not equal the face universe")
    pair_count = len(p_full)
    pair_deficit = universe_face_count - pair_count
    collision_excess = sum(
        math.comb(len(zero_set(error)), extension_dimension) - 1 for error in p_full
    )
    require(pair_deficit == collision_excess, "complete-family pair deficit is not collision excess")

    ordered = sorted(p_full, key=lambda error: (-len(zero_set(error)), error))
    retained = set(ordered[::2])
    retained_collision_excess = sum(
        math.comb(len(zero_set(error)), extension_dimension) - 1 for error in retained
    )
    deleted_charge = sum(
        math.comb(len(zero_set(error)), extension_dimension)
        for error in p_full
        if error not in retained
    )
    ledger_left = universe_face_count - len(retained)
    ledger_right = retained_collision_excess + deleted_charge
    require(ledger_left == ledger_right, "retained-subset owner ledger failed")

    local_gamma = verify_local_gamma(prime, kappa_basis, b0, b1, extension_rows)
    condition_values = {
        "pair_count_saturates": pair_count == universe_face_count,
        "all_zero_counts_equal_r": all(
            len(zero_set(error)) == extension_dimension for error in p_full
        ),
        "coset_distance_is_first_wall": coset_distance == first_wall,
        "M_is_mds": m_distance == first_wall,
        "all_extension_restrictions_full_rank": not dependent_restrictions,
        "all_local_gamma_maps_injective": bool(local_gamma["all_injective"]),
    }
    require(len(set(condition_values.values())) == 1, "first-wall equality conditions disagree")
    require(
        next(iter(condition_values.values())) == expect_mds_extension,
        "fixture has the wrong first-wall equality status",
    )

    expected_m_distance = first_wall if expect_mds_extension else first_wall - 1
    expected_coset_distance = first_wall if expect_mds_extension else first_wall - 1
    require(m_distance == expected_m_distance, "unexpected M distance")
    require(coset_distance == expected_coset_distance, "unexpected b0-to-L distance")

    return {
        "name": name,
        "field_order": prime,
        "evaluation_points": list(points),
        "N": length,
        "kappa": kappa,
        "R": redundancy,
        "t": first_wall,
        "r": extension_dimension,
        "b1_exponent": kappa,
        "b0_exponent": b0_exponent,
        "distances": {
            "K": k_distance,
            "L": l_distance,
            "M": m_distance,
            "b0_to_L": coset_distance,
        },
        "p_full": {
            "pair_count": pair_count,
            "universe_face_count": universe_face_count,
            "pair_deficit": pair_deficit,
            "charge": charge,
            "collision_excess": collision_excess,
            "zero_count_histogram": histogram(len(zero_set(error)) for error in p_full),
            "owner_fiber_size_histogram": histogram(len(owners) for owners in owner_map.values()),
            "owner_ledger_sha256": object_sha256(owner_encoding),
        },
        "retained_subset_ledger": {
            "selection": "zero-count-descending,word-lexicographic,even-indices",
            "retained_count": len(retained),
            "left_deficit": ledger_left,
            "retained_collision_excess": retained_collision_excess,
            "deleted_charge": deleted_charge,
            "right_total": ledger_right,
            "identity_holds": True,
        },
        "extension_restrictions": {
            "checked_size": extension_dimension + 1,
            "checked_count": math.comb(length, extension_dimension + 1),
            "dependent_count": len(dependent_restrictions),
            "dependent_sets": [list(restriction) for restriction in dependent_restrictions],
        },
        "local_gamma": local_gamma,
        "equality_conditions": condition_values,
        "equality_case": expect_mds_extension,
    }


def verify_weighted_graph_normalization() -> dict[str, Any]:
    prime = 5
    multiplier = (1, 2, 3, 4, 1)
    coordinate = tuple(range(prime))
    b1 = tuple((weight * x) % prime for weight, x in zip(multiplier, coordinate))
    b0 = tuple((-weight * x * x) % prime for weight, x in zip(multiplier, coordinate))
    normalized_b1 = tuple(
        (value * inverse_mod(weight, prime)) % prime
        for value, weight in zip(b1, multiplier)
    )
    normalized_f = tuple(
        (-value * inverse_mod(weight, prime)) % prime
        for value, weight in zip(b0, multiplier)
    )
    require(normalized_b1 == coordinate, "weighted direction did not normalize to x")
    require(
        normalized_f == tuple((x * x) % prime for x in coordinate),
        "weighted anchor did not normalize to x^2",
    )
    require(is_graph_arc(normalized_f, prime), "normalized weighted graph is not an arc")

    raw_fits = []
    for leading in range(1, prime):
        for linear in range(prime):
            for constant in range(prime):
                if all(
                    (-b0[index] - leading * b1[index] * b1[index]
                     - linear * b1[index] - constant) % prime == 0
                    for index in range(prime)
                ):
                    raw_fits.append((leading, linear, constant))
    require(not raw_fits, "raw weighted coordinates unexpectedly fit a quadratic")

    normalized_blocks = secant_family(normalized_f, prime)
    require(len(normalized_blocks) == math.comb(prime, 2), "weighted arc owner count changed")
    return {
        "field_order": prime,
        "multiplier": list(multiplier),
        "b1": list(b1),
        "b0": list(b0),
        "normalized_b1": list(normalized_b1),
        "normalized_f": list(normalized_f),
        "normalized_coefficients_ABC": [1, 0, 0],
        "normalized_graph_is_arc": True,
        "normalized_pair_count": len(normalized_blocks),
        "raw_nondegenerate_quadratic_fit_count": len(raw_fits),
        "raw_formula_refuted": True,
    }


def verify_graph_exhaustion(prime: int) -> dict[str, Any]:
    require(prime in (5, 7), "graph exhaustion is pinned to q=5,7")
    quadratics = quadratic_functions(prime)
    arcs: list[tuple[int, ...]] = []
    for function in itertools.product(range(prime), repeat=prime):
        if is_graph_arc(function, prime):
            arcs.append(function)

    arc_set = set(arcs)
    quadratic_set = set(quadratics)
    require(len(arcs) == len(arc_set), "arc enumeration contains duplicates")
    require(arc_set == quadratic_set, "normalized graph arcs are not exactly quadratics")
    expected_count = (prime - 1) * prime * prime
    require(len(arcs) == expected_count, "unexpected graph-arc count")

    expected_pairs = math.comb(prime, 2)
    expected_per_slope = (prime - 1) // 2
    for function in sorted(arcs):
        blocks = secant_family(function, prime)
        require(len(blocks) == expected_pairs, "arc has wrong complete-family size")
        require(all(len(block) == 2 for block in blocks.values()), "arc has a non-pair secant")
        charge = sum(math.comb(len(block), 2) for block in blocks.values())
        require(charge == expected_pairs, "arc secant charge is not all point pairs")
        slope_loads = Counter(slope for slope, _intercept in blocks)
        require(len(slope_loads) == prime, "arc omits a slope")
        require(
            all(slope_loads[slope] == expected_per_slope for slope in range(prime)),
            "quadratic arc has nonuniform fixed-slope load",
        )

    sorted_arcs = sorted(arcs)
    coefficient_crosswalk = [
        {"function": list(function), "coefficients_ABC": list(quadratics[function])}
        for function in sorted_arcs
    ]
    return {
        "field_order": prime,
        "function_count_checked": prime**prime,
        "arc_count": len(arcs),
        "nondegenerate_quadratic_count": len(quadratics),
        "arc_equals_nondegenerate_quadratic": True,
        "complete_family_size": expected_pairs,
        "fixed_slope_pair_owners": expected_per_slope,
        "arc_function_sha256": object_sha256([list(function) for function in sorted_arcs]),
        "coefficient_crosswalk_sha256": object_sha256(coefficient_crosswalk),
    }


def verify_graph_local_slopes(function: Sequence[int], prime: int) -> dict[str, Any]:
    injective_cores = 0
    image_sizes: list[int] = []
    collision_pair_count = 0
    for core in range(prime):
        slopes: dict[int, int] = {}
        for point in range(prime):
            if point == core:
                continue
            slopes[point] = (
                (function[point] - function[core]) * inverse_mod(point - core, prime)
            ) % prime
        fibers: dict[int, list[int]] = defaultdict(list)
        for point, slope in slopes.items():
            fibers[slope].append(point)
        image_sizes.append(len(fibers))
        if len(fibers) == prime - 1:
            injective_cores += 1
        collision_pair_count += sum(math.comb(len(fiber), 2) for fiber in fibers.values())
        for slope, fiber in fibers.items():
            intercept = (function[core] - slope * core) % prime
            line_points = tuple(
                point
                for point in range(prime)
                if (function[point] - slope * point - intercept) % prime == 0
            )
            require(set(line_points) == {core, *fiber}, "local graph-slope fiber identity failed")
    return {
        "core_count": prime,
        "injective_core_count": injective_cores,
        "all_injective": injective_cores == prime,
        "image_size_histogram": histogram(image_sizes),
        "collision_pair_count": collision_pair_count,
        "fiber_identity_checked": True,
    }


def verify_one_point_perturbation(prime: int) -> dict[str, Any]:
    require(prime in PERTURBATION_PRIMES, "unpinned perturbation field")
    quadratic = tuple((x * x) % prime for x in range(prime))
    function = tuple(prime - 1 if x == 0 else quadratic[x] for x in range(prime))
    changed_coordinates = [
        index for index, (left, right) in enumerate(zip(function, quadratic)) if left != right
    ]
    require(changed_coordinates == [0], "perturbation is not exactly one edit at zero")
    require(function[0] == prime - 1, "pinned moved value is not -1")
    require(function not in quadratic_functions(prime), "perturbation is still quadratic")
    require(not is_graph_arc(function, prime), "perturbation unexpectedly remains an arc")

    blocks = secant_family(function, prime)
    sizes = [len(block) for block in blocks.values()]
    require(all(size in (2, 3) for size in sizes), "perturbation has a line with four graph points")
    trisecants = [
        (slope, intercept, block)
        for (slope, intercept), block in sorted(blocks.items())
        if len(block) == 3
    ]
    expected_trisecants = (prime - 3) // 2
    require(len(trisecants) == expected_trisecants, "wrong number of perturbation trisecants")
    for _slope, _intercept, block in trisecants:
        require(block[0] == 0, "a perturbation trisecant misses the moved point")
        left, right = block[1], block[2]
        require((left * right) % prime == 1, "trisecant endpoints are not reciprocal")
        require(left not in (1, prime - 1), "a fixed reciprocal point entered a trisecant")
        require(right not in (1, prime - 1), "a fixed reciprocal point entered a trisecant")

    all_point_pairs = math.comb(prime, 2)
    charge = sum(math.comb(size, 2) for size in sizes)
    require(charge == all_point_pairs, "perturbation secants do not own all point pairs")
    pair_count = len(blocks)
    pair_deficit = all_point_pairs - pair_count
    collision_excess = sum(math.comb(size, 2) - 1 for size in sizes)
    require(pair_deficit == prime - 3, "wrong one-point perturbation pair deficit")
    require(pair_deficit == 2 * expected_trisecants, "pair deficit is not twice T")
    require(collision_excess == pair_deficit, "perturbation collision ledger failed")

    slope_loads = Counter(slope for slope, _intercept in blocks)
    local_slopes = verify_graph_local_slopes(function, prime)
    return {
        "field_order": prime,
        "definition": "f(0)=-1; f(x)=x^2 for x!=0",
        "function_values": list(function),
        "changed_coordinates_from_x_squared": changed_coordinates,
        "nonquadratic": True,
        "T_trisecants": len(trisecants),
        "expected_T": expected_trisecants,
        "complete_family_pair_count": pair_count,
        "all_point_pairs": all_point_pairs,
        "pair_deficit": pair_deficit,
        "expected_pair_deficit": prime - 3,
        "zero_count_histogram": histogram(sizes),
        "pair_charge": charge,
        "collision_excess": collision_excess,
        "trisecants": [
            {"slope": slope, "intercept": intercept, "points": list(block)}
            for slope, intercept, block in trisecants
        ],
        "slope_load_histogram": histogram(slope_loads.values()),
        "local_slopes": local_slopes,
    }


def build_certificate() -> dict[str, Any]:
    root = repository_root()
    source_paths = (SCRIPT_RELATIVE, NOTE_RELATIVE)
    for relative in source_paths:
        require((root / relative).is_file(), f"missing source file: {relative}")

    fixtures = [
        verify_general_fixture("mds_extension", b0_exponent=4, expect_mds_extension=True),
        verify_general_fixture("collision_extension", b0_exponent=5, expect_mds_extension=False),
    ]
    weighted_normalization = verify_weighted_graph_normalization()
    graph_exhaustions = [verify_graph_exhaustion(prime) for prime in (5, 7)]
    perturbations = [verify_one_point_perturbation(prime) for prime in PERTURBATION_PRIMES]

    payload = {
        "schema": SCHEMA,
        "status": "verified",
        "base_commit": BASE_COMMIT,
        "sources": {
            str(relative): file_sha256(root / relative) for relative in source_paths
        },
        "general_fixtures": fixtures,
        "weighted_graph_normalization": weighted_normalization,
        "normalized_graph_arc_exhaustion": graph_exhaustions,
        "one_point_perturbations": perturbations,
        "scope": {
            "lean_target_independent": True,
            "python_dependencies": "standard-library-only",
            "proved_by_computation": [
                "finite F_11 interpolation fixtures and owner ledger",
                "local Gamma fiber/rank equivalence",
                "weighted q=5 graph-normalization regression",
                "q=5,7 normalized graph-arc exhaustion",
                "q=5,7,11,13 pinned one-point perturbations",
            ],
            "not_claimed": [
                "general Segre theorem",
                "weighted-GRS interpolation formalization",
                "robust stability without exceptional coordinates",
            ],
        },
    }
    certificate = with_payload_hash(payload)
    validate_certificate(certificate)
    return certificate


def require_mapping(value: Any, message: str) -> dict[str, Any]:
    require(isinstance(value, dict), message)
    return value


def require_list(value: Any, message: str) -> list[Any]:
    require(isinstance(value, list), message)
    return value


def parse_integer_histogram(value: Any, message: str) -> dict[int, int]:
    mapping = require_mapping(value, message)
    parsed: dict[int, int] = {}
    for key, count in mapping.items():
        require(isinstance(key, str) and key.isdigit(), message)
        require(isinstance(count, int) and count >= 0, message)
        parsed[int(key)] = count
    return parsed


def require_sha256(value: Any, message: str) -> str:
    require(isinstance(value, str) and len(value) == 64, message)
    require(all(character in "0123456789abcdef" for character in value), message)
    return value


def validate_general_fixture(fixture: Any, expected_name: str, equality_case: bool) -> None:
    item = require_mapping(fixture, "fixture is not an object")
    require(item.get("name") == expected_name, "unexpected fixture name")
    require(item.get("field_order") == 11, "fixture field is not F_11")
    require(item.get("evaluation_points") == list(range(8)), "fixture has wrong evaluation grid")
    require(
        [item.get(key) for key in ("N", "kappa", "R", "t", "r")] == [8, 3, 5, 4, 4],
        "fixture parameters are not (N,kappa,R,t,r)=(8,3,5,4,4)",
    )
    require(item.get("b1_exponent") == 3, "fixture b1 is not x^3")
    require(item.get("b0_exponent") == (4 if equality_case else 5), "fixture b0 exponent changed")
    require(item.get("equality_case") is equality_case, "fixture equality label changed")

    distances = require_mapping(item.get("distances"), "fixture distances missing")
    require(distances.get("K") == 6 and distances.get("L") == 5, "base MDS distances changed")
    expected_last_distance = 4 if equality_case else 3
    require(
        distances.get("M") == expected_last_distance
        and distances.get("b0_to_L") == expected_last_distance,
        "extension/coset distance changed",
    )

    full = require_mapping(item.get("p_full"), "fixture P_full data missing")
    require(full.get("universe_face_count") == 70, "wrong owner-face universe")
    zero_histogram = parse_integer_histogram(full.get("zero_count_histogram"), "bad zero histogram")
    pair_count = sum(zero_histogram.values())
    charge = sum(count * math.comb(zeros, 4) for zeros, count in zero_histogram.items())
    collision_excess = sum(
        count * (math.comb(zeros, 4) - 1) for zeros, count in zero_histogram.items()
    )
    require(full.get("pair_count") == pair_count, "P_full pair count disagrees with histogram")
    require(full.get("charge") == charge == 70, "P_full charge disagrees with the owner identity")
    require(full.get("pair_deficit") == 70 - pair_count, "P_full deficit is inconsistent")
    require(full.get("collision_excess") == collision_excess, "P_full collision excess is inconsistent")
    require(full.get("pair_deficit") == collision_excess, "complete-family collision ledger changed")
    owner_histogram = parse_integer_histogram(
        full.get("owner_fiber_size_histogram"), "bad owner-fiber histogram"
    )
    expected_owner_histogram: Counter[int] = Counter()
    for zeros, count in zero_histogram.items():
        expected_owner_histogram[math.comb(zeros, 4)] += count
    require(owner_histogram == dict(expected_owner_histogram), "owner fiber sizes do not match zero sets")
    owner_ledger_sha256 = require_sha256(
        full.get("owner_ledger_sha256"), "bad owner-ledger hash"
    )
    require(
        owner_ledger_sha256 == EXPECTED_OWNER_LEDGER_SHA256[expected_name],
        "owner-ledger hash changed",
    )

    ledger = require_mapping(item.get("retained_subset_ledger"), "retained ledger missing")
    retained_count = ledger.get("retained_count")
    require(isinstance(retained_count, int) and 0 <= retained_count <= pair_count, "bad retained count")
    require(ledger.get("left_deficit") == 70 - retained_count, "retained ledger left side changed")
    require(
        ledger.get("right_total")
        == ledger.get("retained_collision_excess") + ledger.get("deleted_charge"),
        "retained ledger right side changed",
    )
    require(ledger.get("left_deficit") == ledger.get("right_total"), "retained ledger identity failed")
    require(ledger.get("identity_holds") is True, "retained ledger lost its success marker")

    restrictions = require_mapping(
        item.get("extension_restrictions"), "extension restriction data missing"
    )
    dependent_sets = require_list(restrictions.get("dependent_sets"), "dependent-set list missing")
    require(restrictions.get("checked_size") == 5, "wrong restriction size")
    require(restrictions.get("checked_count") == 56, "wrong restriction count")
    require(restrictions.get("dependent_count") == len(dependent_sets), "dependent count mismatch")
    require((len(dependent_sets) == 0) is equality_case, "dependent restrictions disagree with equality")
    for dependent in dependent_sets:
        require(
            isinstance(dependent, list)
            and len(dependent) == 5
            and dependent == sorted(set(dependent))
            and all(isinstance(index, int) and 0 <= index < 8 for index in dependent),
            "malformed dependent restriction",
        )
    if not equality_case:
        require(full.get("collision_excess") == 4 * len(dependent_sets), "collision words/dependencies diverged")

    local = require_mapping(item.get("local_gamma"), "local Gamma data missing")
    require(local.get("core_count") == 56, "wrong number of local Gamma cores")
    image_histogram = parse_integer_histogram(
        local.get("image_size_histogram"), "bad Gamma image histogram"
    )
    require(sum(image_histogram.values()) == 56, "Gamma histogram omits cores")
    injective_count = local.get("injective_core_count")
    require(isinstance(injective_count, int) and 0 <= injective_count <= 56, "bad Gamma injective count")
    require(local.get("all_injective") is (injective_count == 56), "Gamma injectivity flag changed")
    require(local.get("all_injective") is equality_case, "Gamma injectivity disagrees with equality")
    require(
        local.get("collision_pair_count") == 10 * len(dependent_sets),
        "Gamma collisions do not crosswalk to dependent five-sets",
    )
    require(local.get("fiber_identity_checked") is True, "Gamma fiber check marker missing")
    require(
        local.get("rank_collision_equivalence_checked") is True,
        "Gamma/rank check marker missing",
    )

    conditions = require_mapping(item.get("equality_conditions"), "equality conditions missing")
    require(len(conditions) == 6, "equality-condition list changed")
    require(all(value is equality_case for value in conditions.values()), "equality conditions diverged")


def validate_weighted_graph_normalization(record: Any) -> None:
    item = require_mapping(record, "weighted graph record is not an object")
    require(item.get("field_order") == 5, "weighted graph field changed")
    require(item.get("multiplier") == [1, 2, 3, 4, 1], "weighted multiplier changed")
    require(item.get("b1") == [0, 2, 1, 2, 4], "weighted b1 changed")
    require(item.get("b0") == [0, 3, 3, 4, 4], "weighted b0 changed")
    require(item.get("normalized_b1") == list(range(5)), "normalized b1 changed")
    require(item.get("normalized_f") == [0, 1, 4, 4, 1], "normalized f changed")
    require(
        item.get("normalized_coefficients_ABC") == [1, 0, 0],
        "normalized quadratic coefficients changed",
    )
    require(item.get("normalized_graph_is_arc") is True, "weighted graph lost arc status")
    require(item.get("normalized_pair_count") == 10, "weighted graph owner count changed")
    require(
        item.get("raw_nondegenerate_quadratic_fit_count") == 0,
        "raw weighted coordinates acquired a quadratic fit",
    )
    require(item.get("raw_formula_refuted") is True, "raw-formula regression marker changed")


def validate_graph_exhaustion(record: Any, expected_prime: int) -> None:
    item = require_mapping(record, "graph exhaustion record is not an object")
    require(item.get("field_order") == expected_prime, "graph exhaustion field changed")
    expected_count = (expected_prime - 1) * expected_prime * expected_prime
    require(item.get("function_count_checked") == expected_prime**expected_prime, "function grid changed")
    require(item.get("arc_count") == expected_count, "graph-arc count changed")
    require(item.get("nondegenerate_quadratic_count") == expected_count, "quadratic count changed")
    require(item.get("arc_equals_nondegenerate_quadratic") is True, "classification marker changed")
    require(item.get("complete_family_size") == math.comb(expected_prime, 2), "arc family size changed")
    require(
        item.get("fixed_slope_pair_owners") == (expected_prime - 1) // 2,
        "fixed-slope multiplicity changed",
    )
    expected_digests = EXPECTED_GRAPH_DIGESTS[expected_prime]
    arc_function_sha256 = require_sha256(
        item.get("arc_function_sha256"), "bad arc-function hash"
    )
    coefficient_crosswalk_sha256 = require_sha256(
        item.get("coefficient_crosswalk_sha256"), "bad coefficient-crosswalk hash"
    )
    require(
        arc_function_sha256 == expected_digests["arc_function_sha256"],
        "arc-function hash changed",
    )
    require(
        coefficient_crosswalk_sha256
        == expected_digests["coefficient_crosswalk_sha256"],
        "coefficient-crosswalk hash changed",
    )


def validate_perturbation(record: Any, expected_prime: int) -> None:
    item = require_mapping(record, "perturbation record is not an object")
    require(item.get("field_order") == expected_prime, "perturbation field changed")
    require(item.get("definition") == "f(0)=-1; f(x)=x^2 for x!=0", "perturbation definition changed")
    expected_function = [expected_prime - 1] + [
        (x * x) % expected_prime for x in range(1, expected_prime)
    ]
    require(item.get("function_values") == expected_function, "perturbation function values changed")
    require(item.get("changed_coordinates_from_x_squared") == [0], "perturbation edit set changed")
    require(item.get("nonquadratic") is True, "perturbation quadraticity marker changed")
    expected_t = (expected_prime - 3) // 2
    require(item.get("T_trisecants") == expected_t, "perturbation T changed")
    require(item.get("expected_T") == expected_t, "perturbation expected T changed")
    trisecants = require_list(item.get("trisecants"), "perturbation trisecants missing")
    require(len(trisecants) == expected_t, "perturbation trisecant list has wrong length")
    for trisecant in trisecants:
        block = require_mapping(trisecant, "malformed trisecant")
        points = block.get("points")
        require(isinstance(points, list) and len(points) == 3 and points[0] == 0, "bad trisecant points")
        require((points[1] * points[2]) % expected_prime == 1, "trisecant is not reciprocal")

    size_histogram = parse_integer_histogram(
        item.get("zero_count_histogram"), "bad perturbation block histogram"
    )
    require(set(size_histogram).issubset({2, 3}), "perturbation has forbidden block size")
    pair_count = sum(size_histogram.values())
    pair_charge = sum(count * math.comb(size, 2) for size, count in size_histogram.items())
    all_pairs = math.comb(expected_prime, 2)
    require(item.get("complete_family_pair_count") == pair_count, "perturbation pair count mismatch")
    require(item.get("all_point_pairs") == all_pairs, "perturbation point-pair count changed")
    require(item.get("pair_charge") == pair_charge == all_pairs, "perturbation pair charge changed")
    require(item.get("pair_deficit") == all_pairs - pair_count, "perturbation deficit inconsistent")
    require(item.get("pair_deficit") == expected_prime - 3, "perturbation deficit formula changed")
    require(item.get("expected_pair_deficit") == expected_prime - 3, "expected deficit changed")
    require(item.get("collision_excess") == expected_prime - 3, "collision excess changed")
    require(item.get("pair_deficit") == 2 * item.get("T_trisecants"), "deficit is not 2T")

    local = require_mapping(item.get("local_slopes"), "perturbation local-slope data missing")
    require(local.get("core_count") == expected_prime, "wrong perturbation core count")
    require(local.get("all_injective") is False, "perturbation incorrectly has injective local slopes")
    require(local.get("fiber_identity_checked") is True, "perturbation fiber marker missing")


def validate_certificate(certificate: Any) -> None:
    payload = require_mapping(certificate, "certificate is not a JSON object")
    require(payload.get("schema") == SCHEMA, "certificate schema changed")
    require(payload.get("status") == "verified", "certificate status changed")
    require(payload.get("base_commit") == BASE_COMMIT, "certificate base commit changed")
    claimed_hash = require_sha256(payload.get("payload_sha256"), "bad payload hash")
    unhashed = copy.deepcopy(payload)
    unhashed.pop("payload_sha256", None)
    require(claimed_hash == object_sha256(unhashed), "payload hash mismatch")

    root = repository_root()
    sources = require_mapping(payload.get("sources"), "certificate sources missing")
    require(set(sources) == {str(SCRIPT_RELATIVE), str(NOTE_RELATIVE)}, "source set changed")
    for relative in (SCRIPT_RELATIVE, NOTE_RELATIVE):
        claimed_source_hash = require_sha256(sources.get(str(relative)), "bad source hash")
        require(claimed_source_hash == file_sha256(root / relative), f"source hash mismatch: {relative}")

    fixtures = require_list(payload.get("general_fixtures"), "general fixtures missing")
    require(len(fixtures) == 2, "general fixture count changed")
    validate_general_fixture(fixtures[0], "mds_extension", True)
    validate_general_fixture(fixtures[1], "collision_extension", False)
    validate_weighted_graph_normalization(payload.get("weighted_graph_normalization"))

    exhaustions = require_list(
        payload.get("normalized_graph_arc_exhaustion"), "graph exhaustions missing"
    )
    require(len(exhaustions) == 2, "graph exhaustion count changed")
    validate_graph_exhaustion(exhaustions[0], 5)
    validate_graph_exhaustion(exhaustions[1], 7)

    perturbations = require_list(payload.get("one_point_perturbations"), "perturbations missing")
    require(len(perturbations) == len(PERTURBATION_PRIMES), "perturbation count changed")
    for record, prime in zip(perturbations, PERTURBATION_PRIMES):
        validate_perturbation(record, prime)

    scope = require_mapping(payload.get("scope"), "scope record missing")
    require(scope.get("lean_target_independent") is True, "Lean independence marker changed")
    require(scope.get("python_dependencies") == "standard-library-only", "dependency scope changed")


def replace_path(root: dict[str, Any], path: Sequence[Any], replacement: Any) -> None:
    cursor: Any = root
    for component in path[:-1]:
        cursor = cursor[component]
    cursor[path[-1]] = replacement


def tamper_selftest() -> int:
    certificate = build_certificate()
    mutations: list[tuple[str, tuple[Any, ...], Any]] = [
        ("schema", ("schema",), "first_wall_mds_extension_inverse.v0"),
        ("base commit", ("base_commit",), "0" * 40),
        ("source hash", ("sources", str(NOTE_RELATIVE)), "0" * 64),
        ("MDS pair count", ("general_fixtures", 0, "p_full", "pair_count"), 69),
        (
            "MDS owner-ledger hash",
            ("general_fixtures", 0, "p_full", "owner_ledger_sha256"),
            "0" * 64,
        ),
        (
            "collision owner-ledger hash",
            ("general_fixtures", 1, "p_full", "owner_ledger_sha256"),
            "0" * 64,
        ),
        (
            "collision ledger",
            ("general_fixtures", 1, "p_full", "collision_excess"),
            -1,
        ),
        (
            "Gamma histogram",
            ("general_fixtures", 0, "local_gamma", "image_size_histogram"),
            {"5": 55},
        ),
        (
            "weighted raw-formula marker",
            ("weighted_graph_normalization", "raw_formula_refuted"),
            False,
        ),
        (
            "dependent count",
            ("general_fixtures", 1, "extension_restrictions", "dependent_count"),
            0,
        ),
        ("q=7 arc count", ("normalized_graph_arc_exhaustion", 1, "arc_count"), 293),
        (
            "q=5 arc-function hash",
            ("normalized_graph_arc_exhaustion", 0, "arc_function_sha256"),
            "0" * 64,
        ),
        (
            "q=5 coefficient-crosswalk hash",
            ("normalized_graph_arc_exhaustion", 0, "coefficient_crosswalk_sha256"),
            "0" * 64,
        ),
        (
            "q=7 arc-function hash",
            ("normalized_graph_arc_exhaustion", 1, "arc_function_sha256"),
            "0" * 64,
        ),
        (
            "q=7 coefficient-crosswalk hash",
            ("normalized_graph_arc_exhaustion", 1, "coefficient_crosswalk_sha256"),
            "0" * 64,
        ),
        (
            "q=5 slope load",
            ("normalized_graph_arc_exhaustion", 0, "fixed_slope_pair_owners"),
            3,
        ),
        ("q=11 perturbation T", ("one_point_perturbations", 2, "T_trisecants"), 3),
        ("q=13 perturbation deficit", ("one_point_perturbations", 3, "pair_deficit"), 9),
    ]
    rejected = 0
    for label, path, replacement in mutations:
        candidate = copy.deepcopy(certificate)
        replace_path(candidate, path, replacement)
        refresh_payload_hash(candidate)
        try:
            validate_certificate(candidate)
        except VerificationError:
            rejected += 1
        else:
            raise VerificationError(f"tamper self-test accepted mutation: {label}")

    bad_hash = copy.deepcopy(certificate)
    bad_hash["payload_sha256"] = "f" * 64
    try:
        validate_certificate(bad_hash)
    except VerificationError:
        rejected += 1
    else:
        raise VerificationError("tamper self-test accepted a bad payload hash")

    require(rejected == len(mutations) + 1, "tamper rejection count changed")
    print(f"tamper-selftest: PASS ({rejected}/{rejected} mutations rejected)")
    print(f"payload_sha256: {certificate['payload_sha256']}")
    return 0


def print_summary(certificate: dict[str, Any]) -> None:
    fixtures = certificate["general_fixtures"]
    print(f"schema: {certificate['schema']}")
    for fixture in fixtures:
        print(
            f"fixture {fixture['name']}: pairs={fixture['p_full']['pair_count']}/70, "
            f"distance={fixture['distances']['b0_to_L']}, "
            f"dependent_5sets={fixture['extension_restrictions']['dependent_count']}, "
            f"Gamma_injective={fixture['local_gamma']['all_injective']}"
        )
    weighted = certificate["weighted_graph_normalization"]
    print(
        "weighted q=5: normalized_arc="
        f"{weighted['normalized_graph_is_arc']}, "
        f"raw_quadratic_fits={weighted['raw_nondegenerate_quadratic_fit_count']}"
    )
    for record in certificate["normalized_graph_arc_exhaustion"]:
        print(
            f"graph q={record['field_order']}: arcs={record['arc_count']}, "
            f"quadratics={record['nondegenerate_quadratic_count']}"
        )
    for record in certificate["one_point_perturbations"]:
        print(
            f"perturbation q={record['field_order']}: T={record['T_trisecants']}, "
            f"deficit={record['pair_deficit']}"
        )
    print(f"payload_sha256: {certificate['payload_sha256']}")


def resolve_certificate_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else repository_root() / path


def run_check(certificate: dict[str, Any], path_value: str) -> None:
    path = resolve_certificate_path(path_value)
    if path.exists():
        try:
            frozen = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise VerificationError(f"cannot read certificate {path}: {error}") from error
        validate_certificate(frozen)
        require(canonical_json(frozen) == canonical_json(certificate), "frozen certificate is stale")
        print(f"certificate check: PASS ({path})")
    else:
        raise VerificationError(f"frozen certificate is missing: {path}")


def write_certificate(certificate: dict[str, Any], path_value: str) -> None:
    path = resolve_certificate_path(path_value)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    frozen = json.loads(path.read_text(encoding="utf-8"))
    validate_certificate(frozen)
    require(canonical_json(frozen) == canonical_json(certificate), "written certificate differs")
    print(f"certificate write: PASS ({path})")


def parse_arguments(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument(
        "--write",
        nargs="?",
        const=str(DEFAULT_CERTIFICATE),
        metavar="PATH",
        help="write a deterministic JSON certificate (default: repository certificate path)",
    )
    modes.add_argument(
        "--check",
        nargs="?",
        const=str(DEFAULT_CERTIFICATE),
        metavar="PATH",
        help="recompute and, when present, compare a deterministic JSON certificate",
    )
    modes.add_argument(
        "--tamper-selftest",
        action="store_true",
        help="confirm that load-bearing certificate mutations are rejected",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    arguments = parse_arguments(sys.argv[1:] if argv is None else argv)
    try:
        if arguments.tamper_selftest:
            return tamper_selftest()
        certificate = build_certificate()
        if arguments.write is not None:
            write_certificate(certificate, arguments.write)
        elif arguments.check is not None:
            run_check(certificate, arguments.check)
        print_summary(certificate)
        print("verification: PASS")
        return 0
    except (VerificationError, OSError, ValueError, TypeError, KeyError) as error:
        print(f"verification: FAIL: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
