#!/usr/bin/env python3
"""Verify the exact F_11 factored-rank balanced-core audit packet."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path
from typing import Callable, Iterable, Sequence


PRIME = 11
DOMAIN = tuple(range(1, 8))
N = 7
CODE_DIMENSION = 2
SYNDROME_ROWS = 5
AGREEMENT = 4
PREFIX_DEPTH = 1
COMMON_CORE = (1,)

SUPPORTS = (
    (1, 2, 3, 7),
    (1, 2, 4, 6),
    (1, 3, 4, 5),
)
LOCATOR_PINS = (
    (1, 9, 9, 5, 9),
    (1, 9, 1, 7, 4),
    (1, 9, 4, 3, 5),
)
RESIDUAL_SUPPORTS = (
    (2, 3, 7),
    (2, 4, 6),
    (3, 4, 5),
)
RESIDUAL_LOCATOR_PINS = (
    (1, 10, 8, 2),
    (1, 10, 0, 7),
    (1, 10, 3, 6),
)
CORE_FACTOR = (1, 10)

Y0 = (6, 2, 5, 9, 5)
Y1 = (4, 1, 9, 4, 6)
ERROR_WITNESSES = (
    (0, (4, 5, 6), ((4, 10), (5, 3), (6, 4))),
    (1, (3, 5, 7), ((3, 8), (5, 1), (7, 1))),
    (2, (2, 6, 7), ((2, 1), (6, 1), (7, 1))),
)

CERTIFICATE_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "certificates"
    / "balanced-core-factored-rank"
    / "balanced_core_factored_rank.json"
)


class VerificationError(RuntimeError):
    """Raised when an exact audit gate fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def polynomial_multiply(
    left: Sequence[int], right: Sequence[int], prime: int = PRIME
) -> tuple[int, ...]:
    """Multiply descending coefficient vectors over F_prime."""
    require(bool(left) and bool(right), "polynomial factors must be nonempty")
    result = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] = (
                result[left_index + right_index] + left_value * right_value
            ) % prime
    return tuple(result)


def polynomial_evaluate(
    coefficients: Sequence[int], point: int, prime: int = PRIME
) -> int:
    value = 0
    for coefficient in coefficients:
        value = (value * point + coefficient) % prime
    return value


def locator(support: Iterable[int]) -> tuple[int, ...]:
    coefficients = (1,)
    support_tuple = tuple(support)
    require(len(set(support_tuple)) == len(support_tuple), "support repeats a point")
    for point in support_tuple:
        require(point in DOMAIN, f"locator point {point} is outside the domain")
        coefficients = polynomial_multiply(coefficients, (1, -point % PRIME))
    return coefficients


def matrix_rank(matrix: Sequence[Sequence[int]], prime: int = PRIME) -> int:
    if not matrix:
        return 0
    width = len(matrix[0])
    require(all(len(row) == width for row in matrix), "matrix is ragged")
    rows = [[value % prime for value in row] for row in matrix]
    height = len(rows)
    rank = 0
    for column in range(width):
        pivot = next(
            (row for row in range(rank, height) if rows[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, prime)
        rows[rank] = [(value * inverse) % prime for value in rows[rank]]
        for row in range(height):
            if row == rank or rows[row][column] == 0:
                continue
            scale = rows[row][column]
            rows[row] = [
                (value - scale * pivot_value) % prime
                for value, pivot_value in zip(rows[row], rows[rank], strict=True)
            ]
        rank += 1
        if rank == height:
            break
    return rank


def vandermonde_columns(points: Sequence[int]) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(pow(point, exponent, PRIME) for point in points)
        for exponent in range(SYNDROME_ROWS)
    )


def syndrome(coefficients: Sequence[tuple[int, int]]) -> tuple[int, ...]:
    coefficient_map = dict(coefficients)
    require(
        len(coefficient_map) == len(coefficients),
        "error coefficient list repeats a position",
    )
    return tuple(
        sum(
            coefficient_map.get(point, 0) * pow(point, exponent, PRIME)
            for point in DOMAIN
        )
        % PRIME
        for exponent in range(SYNDROME_ROWS)
    )


def affine_dimension(points: Sequence[Sequence[int]]) -> int:
    require(bool(points), "affine point family is empty")
    width = len(points[0])
    require(all(len(point) == width for point in points), "affine points are ragged")
    base = points[0]
    differences = [
        [(value - base_value) % PRIME for value, base_value in zip(point, base)]
        for point in points[1:]
    ]
    return matrix_rank(differences)


def projective_dimension(vectors: Sequence[Sequence[int]]) -> int:
    rank = matrix_rank(vectors)
    require(rank > 0, "projective coefficient family is zero")
    return rank - 1


def common_intersection(supports: Sequence[Sequence[int]]) -> tuple[int, ...]:
    require(bool(supports), "support family is empty")
    intersection = set(supports[0])
    for support in supports[1:]:
        intersection.intersection_update(support)
    return tuple(sorted(intersection))


def prefix_key(support: Sequence[int]) -> tuple[int, ...]:
    coefficients = locator(support)
    return coefficients[1 : 1 + PREFIX_DEPTH]


def determinant_two(points: Sequence[Sequence[int]]) -> int:
    require(len(points) == 3, "two-dimensional determinant needs three points")
    require(all(len(point) == 2 for point in points), "determinant points are not planar")
    first, second, third = points
    left = ((second[0] - first[0]) * (third[1] - first[1])) % PRIME
    right = ((second[1] - first[1]) * (third[0] - first[0])) % PRIME
    return (left - right) % PRIME


def census() -> dict[str, object]:
    supports_with_core = tuple(
        support
        for support in combinations(DOMAIN, AGREEMENT)
        if set(COMMON_CORE).issubset(support)
    )
    triples = tuple(combinations(supports_with_core, 3))
    exact_core_count = 0
    same_prefix_rows: list[dict[str, object]] = []

    for support_triple in triples:
        if common_intersection(support_triple) != COMMON_CORE:
            continue
        exact_core_count += 1
        keys = tuple(prefix_key(support) for support in support_triple)
        if len(set(keys)) != 1:
            continue
        residual_supports = tuple(
            tuple(point for point in support if point not in COMMON_CORE)
            for support in support_triple
        )
        residual_locators = tuple(locator(support) for support in residual_supports)
        deep_points = tuple(coefficients[2:] for coefficients in residual_locators)
        affine_dim = affine_dimension(deep_points)
        projective_dim = projective_dimension(residual_locators)
        same_prefix_rows.append(
            {
                "supports": [list(support) for support in support_triple],
                "prefix": list(keys[0]),
                "locators": [list(locator(support)) for support in support_triple],
                "residual_supports": [list(support) for support in residual_supports],
                "residual_locators": [list(coefficients) for coefficients in residual_locators],
                "residual_intersection": list(common_intersection(residual_supports)),
                "deep_coefficient_points": [list(point) for point in deep_points],
                "affine_determinant": determinant_two(deep_points),
                "affine_dimension": affine_dim,
                "projective_dimension": projective_dim,
            }
        )

    require(len(supports_with_core) == 20, "support-with-core census changed")
    require(len(triples) == 1140, "support triple census changed")
    require(exact_core_count == 480, "exact-core triple census changed")
    require(len(same_prefix_rows) == 4, "same-prefix exact-core census changed")
    require(
        all(row["projective_dimension"] == 2 for row in same_prefix_rows),
        "a same-prefix triple lost projective dimension two",
    )
    require(
        all(row["affine_dimension"] == 2 for row in same_prefix_rows),
        "a same-prefix triple lost affine dimension two",
    )
    return {
        "supports_containing_core": len(supports_with_core),
        "support_triples": len(triples),
        "exact_core_triples": exact_core_count,
        "same_prefix_exact_core_triples": len(same_prefix_rows),
        "same_prefix_projective_dimensions": [
            int(row["projective_dimension"]) for row in same_prefix_rows
        ],
        "same_prefix_affine_dimensions": [
            int(row["affine_dimension"]) for row in same_prefix_rows
        ],
        "rows": same_prefix_rows,
    }


def build_slope_witnesses() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for support, (gamma, error_support, coefficients) in zip(
        SUPPORTS, ERROR_WITNESSES, strict=True
    ):
        require(
            tuple(point for point in DOMAIN if point not in support) == error_support,
            f"gamma={gamma}: error support is not the support complement",
        )
        require(
            tuple(position for position, _ in coefficients) == error_support,
            f"gamma={gamma}: coefficient positions do not equal the error support",
        )
        require(
            all(value % PRIME != 0 for _, value in coefficients),
            f"gamma={gamma}: error coefficient vanished",
        )
        observed_syndrome = syndrome(coefficients)
        target_syndrome = tuple(
            (left + gamma * right) % PRIME for left, right in zip(Y0, Y1, strict=True)
        )
        require(
            observed_syndrome == target_syndrome,
            f"gamma={gamma}: error coefficients miss the syndrome line",
        )

        h_error = vandermonde_columns(error_support)
        h_rank = matrix_rank(h_error)
        augmented = tuple(
            tuple(row) + (Y0[index], Y1[index])
            for index, row in enumerate(h_error)
        )
        augmented_rank = matrix_rank(augmented)
        require(h_rank == 3, f"gamma={gamma}: H_E rank is not three")
        require(
            augmented_rank == 4,
            f"gamma={gamma}: syndrome line is not transverse to H_E",
        )

        admitted_slopes: list[int] = []
        for candidate in range(PRIME):
            candidate_syndrome = tuple(
                (left + candidate * right) % PRIME
                for left, right in zip(Y0, Y1, strict=True)
            )
            candidate_augmented = tuple(
                tuple(row) + (candidate_syndrome[index],)
                for index, row in enumerate(h_error)
            )
            if matrix_rank(candidate_augmented) == h_rank:
                admitted_slopes.append(candidate)
        require(
            admitted_slopes == [gamma],
            f"gamma={gamma}: transversality did not isolate one slope",
        )
        rows.append(
            {
                "gamma": gamma,
                "support": list(support),
                "error_support": list(error_support),
                "error_coefficients": [
                    {"position": position, "value": value}
                    for position, value in coefficients
                ],
                "syndrome": list(observed_syndrome),
                "line_syndrome": list(target_syndrome),
                "H_E": [list(row) for row in h_error],
                "rank_H_E": h_rank,
                "rank_H_E_y0_y1": augmented_rank,
                "admitted_slopes": admitted_slopes,
            }
        )
    return {
        "column_formula": "H_x=(1,x,x^2,x^3,x^4) over F_11",
        "y0": list(Y0),
        "y1": list(Y1),
        "rows": rows,
    }


def build_certificate() -> dict[str, object]:
    require(N == len(DOMAIN), "domain size does not equal n")
    require(SYNDROME_ROWS == N - CODE_DIMENSION, "R does not equal n-k")
    require(PREFIX_DEPTH == AGREEMENT - CODE_DIMENSION - 1, "w does not equal a-k-1")
    require(all(len(support) == AGREEMENT for support in SUPPORTS), "witness support size changed")

    locators = tuple(locator(support) for support in SUPPORTS)
    require(locators == LOCATOR_PINS, "full locator pins changed")
    require(common_intersection(SUPPORTS) == COMMON_CORE, "full support core changed")
    require(
        all(
            polynomial_evaluate(coefficients, point) == 0
            for support, coefficients in zip(SUPPORTS, locators, strict=True)
            for point in support
        ),
        "a full locator misses a support point",
    )

    residual_supports = tuple(
        tuple(point for point in support if point not in COMMON_CORE)
        for support in SUPPORTS
    )
    require(residual_supports == RESIDUAL_SUPPORTS, "residual support pins changed")
    residual_locators = tuple(locator(support) for support in residual_supports)
    require(
        residual_locators == RESIDUAL_LOCATOR_PINS,
        "residual locator pins changed",
    )
    require(
        all(
            polynomial_multiply(CORE_FACTOR, residual) == full
            for residual, full in zip(residual_locators, locators, strict=True)
        ),
        "the factor X-1 does not reconstruct every full locator",
    )
    require(
        common_intersection(residual_supports) == (),
        "residual supports retain a common point",
    )

    deep_points = tuple(coefficients[2:] for coefficients in residual_locators)
    deep_determinant = determinant_two(deep_points)
    affine_dim = affine_dimension(deep_points)
    projective_dim = projective_dimension(residual_locators)
    require(deep_determinant == 4, "deep-coefficient determinant changed")
    require(affine_dim == 2, "residual affine coefficient dimension changed")
    require(projective_dim == 2, "residual projective coefficient dimension changed")

    active_domain = tuple(sorted(set().union(*(set(support) for support in residual_supports))))
    require(active_domain == tuple(range(2, 8)), "active residual domain changed")
    vandermonde = vandermonde_columns(active_domain)
    vandermonde_rank = matrix_rank(vandermonde)
    require(vandermonde_rank == 5, "active Vandermonde rank changed")
    corrected_kappa = CODE_DIMENSION - len(COMMON_CORE)
    rank_nullity_kappa = len(active_domain) - vandermonde_rank
    require(corrected_kappa == 1, "factored kappa is not one")
    require(
        rank_nullity_kappa == corrected_kappa,
        "active-domain rank nullity disagrees with k-|K|",
    )
    require(corrected_kappa != CODE_DIMENSION, "factoring did not change kappa")

    census_result = census()
    require(
        census_result["rows"][0]["supports"] == [list(support) for support in SUPPORTS],
        "canonical witness is not the first census row",
    )

    return {
        "schema_version": 1,
        "status": {
            "finite_factored_rank_audit": "PROVED",
            "kappa_equals_unfactored_k": "REFUTED_BY_EXACT_WITNESS",
            "general_balanced_core_ray_compiler": "NOT_CERTIFIED",
        },
        "parameters": {
            "field": "F_11",
            "p": PRIME,
            "domain": list(DOMAIN),
            "n": N,
            "k": CODE_DIMENSION,
            "R": SYNDROME_ROWS,
            "a": AGREEMENT,
            "w": PREFIX_DEPTH,
        },
        "factored_witness": {
            "supports": [list(support) for support in SUPPORTS],
            "locators_descending": [list(coefficients) for coefficients in locators],
            "common_core": list(COMMON_CORE),
            "common_factor_descending": list(CORE_FACTOR),
            "residual_supports": [list(support) for support in residual_supports],
            "residual_locators_descending": [
                list(coefficients) for coefficients in residual_locators
            ],
            "residual_intersection": [],
            "deep_coefficient_points": [list(point) for point in deep_points],
            "deep_coefficient_determinant": deep_determinant,
            "affine_coefficient_dimension": affine_dim,
            "projective_coefficient_dimension": projective_dim,
            "active_domain": list(active_domain),
            "vandermonde_matrix": [list(row) for row in vandermonde],
            "vandermonde_rank": vandermonde_rank,
            "kappa": {
                "formula": "k-|K|",
                "common_core_size": len(COMMON_CORE),
                "value": corrected_kappa,
                "rank_nullity_value": rank_nullity_kappa,
                "unfactored_k": CODE_DIMENSION,
                "differs_from_unfactored_k": corrected_kappa != CODE_DIMENSION,
            },
        },
        "slope_witnesses": build_slope_witnesses(),
        "exhaustive_census": census_result,
        "nonclaims": [
            "This finite F_11 witness does not prove a general balanced-core ray compiler.",
            "The 1,140-triple census is restricted to four-supports in D containing the pinned core point 1.",
            "The packet certifies factored coefficient rank and exact syndrome transversality, not a deployed-row target bound.",
        ],
    }


def expect_rejected(label: str, check: Callable[[], None]) -> str:
    try:
        check()
    except VerificationError:
        return label
    raise VerificationError(f"tamper accepted: {label}")


def run_tamper_selftest() -> list[str]:
    certificate = build_certificate()
    rejected: list[str] = []

    mutated_locator = list(LOCATOR_PINS[0])
    mutated_locator[-1] = (mutated_locator[-1] + 1) % PRIME
    rejected.append(
        expect_rejected(
            "locator-coefficient",
            lambda: require(
                locator(SUPPORTS[0]) == tuple(mutated_locator),
                "tampered locator coefficient passed",
            ),
        )
    )
    rejected.append(
        expect_rejected(
            "unfactored-kappa",
            lambda: require(
                CODE_DIMENSION - len(COMMON_CORE) == CODE_DIMENSION,
                "unfactored kappa passed",
            ),
        )
    )
    mutated_y0 = ((Y0[0] + 1) % PRIME,) + Y0[1:]
    gamma, _, coefficients = ERROR_WITNESSES[0]
    rejected.append(
        expect_rejected(
            "syndrome-line",
            lambda: require(
                syndrome(coefficients)
                == tuple(
                    (left + gamma * right) % PRIME
                    for left, right in zip(mutated_y0, Y1, strict=True)
                ),
                "tampered syndrome line passed",
            ),
        )
    )
    rejected.append(
        expect_rejected(
            "exact-core-census",
            lambda: require(
                int(certificate["exhaustive_census"]["exact_core_triples"]) + 1
                == 480,
                "tampered exact-core census passed",
            ),
        )
    )
    rejected.append(
        expect_rejected(
            "projective-dimension",
            lambda: require(
                int(
                    certificate["factored_witness"][
                        "projective_coefficient_dimension"
                    ]
                )
                == 1,
                "tampered projective dimension passed",
            ),
        )
    )
    require(len(rejected) == 5, "not every tamper gate rejected its mutation")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--emit-certificate",
        type=Path,
        metavar="PATH",
        help="write the deterministic JSON certificate to PATH",
    )
    parser.add_argument(
        "--tamper-selftest",
        action="store_true",
        help="run five negative controls and require every mutation to fail",
    )
    args = parser.parse_args()

    if args.tamper_selftest:
        rejected = run_tamper_selftest()
        print(f"PASS: balanced-core tamper self-test rejected {len(rejected)}/{len(rejected)}")
        print("PASS: " + ", ".join(rejected))
        return

    certificate = build_certificate()
    if args.emit_certificate:
        args.emit_certificate.parent.mkdir(parents=True, exist_ok=True)
        args.emit_certificate.write_text(
            json.dumps(certificate, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(f"WROTE: {args.emit_certificate}")
    else:
        require(CERTIFICATE_PATH.is_file(), f"missing certificate: {CERTIFICATE_PATH}")
        recorded = json.loads(CERTIFICATE_PATH.read_text(encoding="utf-8"))
        require(recorded == certificate, "checked-in certificate is stale")

    census_result = certificate["exhaustive_census"]
    print(
        "PASS: balanced-core factored rank over F_11; "
        f"{census_result['support_triples']:,} support triples exhausted"
    )
    print(
        "PASS: exact-core=480, same-prefix=4, "
        "all four affine/projective dimensions are two"
    )
    print("PASS: slopes 0,1,2 are exact and transverse; kappa=1 != k=2")


if __name__ == "__main__":
    main()
