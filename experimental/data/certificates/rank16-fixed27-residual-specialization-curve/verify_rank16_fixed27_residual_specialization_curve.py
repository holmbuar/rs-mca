#!/usr/bin/env python3
"""Independent replay for the fixed-27 residual specialization theorem.

This uses only the Python standard library.  It checks the deployed arithmetic,
source-file pins, exact scalar-normalization and divided-difference identities
on deterministic finite-field fixtures, the root-incidence floors, and the
three-label Vandermonde terminal over a finite quotient-module fixture.
"""

from __future__ import annotations

import argparse
import hashlib
from itertools import product
from pathlib import Path
from typing import Callable


P = 2_130_706_433
N = 2_097_152
K = 1_048_576
M = 1_116_047
B = 32_768
FIXED_CORE = 27
T = N - M
A = M - K + 1
D = T - FIXED_CORE * B
RESIDUAL_DEGREE = D - B
QUOTIENT_DEGREE = D - A

TARGET = 274_854_110_496_187_592
CAP6_TOTAL = 271_769_678_181_377_208
CAP7_TOTAL = 300_964_056_749_491_576

SOURCE_PINS = {
    "experimental/notes/l2/rank16_fixed_core_quotient_line_obstruction.md":
        "19325c602ae14082f6ef36db312d815552e0f0eefc0787f3a71fd4254af650f7",
    "experimental/notes/l2/rank16_fixed27_block_wedge_stratification.md":
        "b061ede06b138643655cd8c7f9f53e724eb974e9acf924e2e6883f0468cb3c4e",
    "experimental/scripts/verify_rank16_fixed27_block_wedge_stratification.py":
        "345488c3063cfa8c3e9027d83350d26bfc0b40e34abd104f151da0c02318607e",
    "experimental/scripts/verify_rank16_fixed27_block_wedge_stratification.expected.txt":
        "6ba9396b444b490d9d20f1300b92541d04e06ffa718e4bbf35d2e4d114855670",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def check_source_pins() -> None:
    root = repo_root()
    for relative, expected in SOURCE_PINS.items():
        path = root / relative
        require(path.is_file(), f"missing pinned source: {relative}")
        require(sha256(path) == expected, f"source pin mismatch: {relative}")


def check_manifest(manifest: dict[str, object]) -> None:
    expected = {
        "p": P,
        "B": B,
        "a": A,
        "D": D,
        "d": RESIDUAL_DEGREE,
        "w": QUOTIENT_DEGREE,
        "normalization": "nonzero_scalar_specialization",
        "kappa_wall": 1,
        "finite_payment": 0,
        "recurrence_payment": 0,
        "score": "0/2",
    }
    require(manifest == expected, "manifest changed or overclaims theorem scope")


def check_deployed_arithmetic() -> None:
    require(P - 1 == 127 * 2**24, "field factorization")
    require(N == 2**21 and N // B == 64, "subgroup or q64 scale")
    require((T, A, D) == (981_105, 67_472, 96_369), "source degrees")
    require(
        (RESIDUAL_DEGREE, QUOTIENT_DEGREE) == (63_601, 28_897),
        "residual degrees",
    )
    require(2 * B < A < D < 3 * B, "block range")
    require(A - 2 * B == 1_936, "quadratic-block cofactor degree")
    require(D - 2 * B == 30_833 < B, "post-division one-block degree")
    require(RESIDUAL_DEGREE - QUOTIENT_DEGREE == 34_704, "degree gap")
    require(TARGET - CAP6_TOTAL == 3_084_432_314_810_384, "cap-six margin")
    require(CAP7_TOTAL - TARGET == 26_109_946_253_303_984, "cap-seven excess")


BiPoly = dict[tuple[int, int], int]


def bi_clean(poly: BiPoly, prime: int) -> BiPoly:
    return {key: value % prime for key, value in poly.items() if value % prime}


def bi_mul(left: BiPoly, right: BiPoly, prime: int) -> BiPoly:
    out: BiPoly = {}
    for (lx, ly), lv in left.items():
        for (rx, ry), rv in right.items():
            key = (lx + rx, ly + ry)
            out[key] = (out.get(key, 0) + lv * rv) % prime
    return bi_clean(out, prime)


def divide_by_xb_minus_y(poly: BiPoly, block: int, prime: int) -> tuple[BiPoly, BiPoly]:
    """Divide a bivariate polynomial by X^block-Y, using X as lead variable."""
    work = bi_clean(dict(poly), prime)
    quotient: BiPoly = {}
    while work and max(x_degree for x_degree, _ in work) >= block:
        lead_x = max(x_degree for x_degree, _ in work)
        lead_y = max(y_degree for x_degree, y_degree in work if x_degree == lead_x)
        coefficient = work.pop((lead_x, lead_y))
        q_key = (lead_x - block, lead_y)
        quotient[q_key] = (quotient.get(q_key, 0) + coefficient) % prime
        shifted = (lead_x - block, lead_y + 1)
        work[shifted] = (work.get(shifted, 0) + coefficient) % prime
        work = bi_clean(work, prime)
    return bi_clean(quotient, prime), bi_clean(work, prime)


def specialize(poly: BiPoly, label: int, prime: int, max_x: int) -> list[int]:
    values = [0] * (max_x + 1)
    for (x_degree, y_degree), coefficient in poly.items():
        values[x_degree] = (
            values[x_degree] + coefficient * pow(label, y_degree, prime)
        ) % prime
    return values


def vector_scale(vector: list[int], scalar: int, prime: int) -> list[int]:
    return [(scalar * value) % prime for value in vector]


def vector_rank(rows: list[list[int]], prime: int) -> int:
    matrix = [row[:] for row in rows]
    rank = 0
    if not matrix:
        return rank
    columns = len(matrix[0])
    for column in range(columns):
        pivot = next(
            (index for index in range(rank, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], -1, prime)
        matrix[rank] = vector_scale(matrix[rank], inverse, prime)
        for index in range(len(matrix)):
            if index == rank or matrix[index][column] == 0:
                continue
            factor = matrix[index][column]
            matrix[index] = [
                (value - factor * pivot_value) % prime
                for value, pivot_value in zip(matrix[index], matrix[rank])
            ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def curve_fixture(e: int) -> None:
    """Check division, scalar normalization, span, and all-nonzero dependence."""
    prime = 101
    block = 5
    residual_degree = 7
    labels = list(range(1, e + 2))

    # The leading coefficient ell(Y)=2+3Y+Y^(e-1) is nonzero at these labels.
    curve: BiPoly = {
        (residual_degree, 0): 2,
        (residual_degree, 1): 3,
        (residual_degree, e - 1): 1,
        (0, 0): 5,
        (0, 1): 7,
        (0, e - 1): 11,
        (2, 0): 13,
        (2, e - 1): 17,
        (5, 1): 19,
    }
    curve = bi_clean(curve, prime)
    numerator = bi_mul({(block, 0): 1, (0, 1): -1}, curve, prime)
    recovered, remainder = divide_by_xb_minus_y(numerator, block, prime)
    require(not remainder and recovered == curve, f"exact Bezout division e={e}")

    monic_residuals: list[list[int]] = []
    dependence_coefficients: list[int] = []
    saw_nonliteral_specialization = False
    for label in labels:
        specialization = specialize(curve, label, prime, residual_degree)
        ell = specialization[-1]
        require(ell != 0, f"leading scalar e={e}, y={label}")
        residual = vector_scale(specialization, pow(ell, -1, prime), prime)
        require(residual[-1] == 1, "monic normalization")
        saw_nonliteral_specialization |= residual != specialization

        a0 = (pow(label, e, prime) + 5) % prime
        require(a0 != 0, "primitive coordinate fixture")
        q = a0 * pow(ell, -1, prime) % prime
        require(q != 0 and a0 * pow(q, -1, prime) % prime == ell, "source scalar")

        denominator = 1
        for other in labels:
            if other != label:
                denominator = denominator * (label - other) % prime
        coefficient = ell * pow(denominator, -1, prime) % prime
        require(coefficient != 0, "all-nonzero divided-difference coefficient")
        dependence_coefficients.append(coefficient)
        monic_residuals.append(residual)

    require(saw_nonliteral_specialization, "fixture must reject literal equality")
    require(vector_rank(monic_residuals, prime) <= e, f"span cap e={e}")
    relation = [0] * (residual_degree + 1)
    for coefficient, residual in zip(dependence_coefficients, monic_residuals):
        relation = [
            (value + coefficient * residual_value) % prime
            for value, residual_value in zip(relation, residual)
        ]
    require(not any(relation), f"divided-difference relation e={e}")


def union_floor(outside_occupancy: int, base_size: int) -> int:
    numerator = 7 * (RESIDUAL_DEGREE - base_size)
    return base_size + (numerator + outside_occupancy - 1) // outside_occupancy


def check_incidence_floors() -> None:
    require(
        min(union_floor(2, base) for base in range(QUOTIENT_DEGREE + 1))
        == 150_361,
        "cubic union floor",
    )
    require(
        min(union_floor(3, base) for base in range(QUOTIENT_DEGREE + 1))
        == 109_873,
        "quartic union floor",
    )
    require(union_floor(2, QUOTIENT_DEGREE) == 150_361, "cubic endpoint")
    require(union_floor(3, QUOTIENT_DEGREE) == 109_873, "quartic endpoint")


def check_vandermonde_quotient_fixture() -> None:
    """Exhaust the three-label terminal over a two-dimensional F_5 module."""
    prime = 5
    labels = (0, 1, 2)
    elements = list(product(range(prime), repeat=2))
    solutions = 0
    for c0, c1, z_value in product(elements, repeat=3):
        valid = True
        for label in labels:
            equation = tuple(
                (c0[index] + label * c1[index] + label * label * z_value[index])
                % prime
                for index in range(2)
            )
            if equation != (0, 0):
                valid = False
                break
        if valid:
            solutions += 1
            require(c0 == c1 == z_value == (0, 0), "nonzero Vandermonde solution")
    determinant = (labels[1] - labels[0]) * (labels[2] - labels[0]) * (
        labels[2] - labels[1]
    ) % prime
    require(determinant != 0 and solutions == 1, "Vandermonde quotient terminal")


def expect_failure(action: Callable[[], None], label: str) -> None:
    try:
        action()
    except ValueError:
        return
    raise ValueError(f"tamper was not rejected: {label}")


def tamper_selftest() -> None:
    manifest: dict[str, object] = {
        "p": P,
        "B": B,
        "a": A,
        "D": D,
        "d": RESIDUAL_DEGREE,
        "w": QUOTIENT_DEGREE,
        "normalization": "nonzero_scalar_specialization",
        "kappa_wall": 1,
        "finite_payment": 0,
        "recurrence_payment": 0,
        "score": "0/2",
    }
    check_manifest(manifest)
    wrong_normalization = dict(manifest)
    wrong_normalization["normalization"] = "literal_equality"
    expect_failure(lambda: check_manifest(wrong_normalization), "normalization")
    wrong_degree = dict(manifest)
    wrong_degree["D"] = D + 1
    expect_failure(lambda: check_manifest(wrong_degree), "degree")
    wrong_payment = dict(manifest)
    wrong_payment["finite_payment"] = 1
    expect_failure(lambda: check_manifest(wrong_payment), "ledger payment")
    wrong_wall = dict(manifest)
    wrong_wall["kappa_wall"] = 2
    expect_failure(lambda: check_manifest(wrong_wall), "remaining wall")


def run_all() -> None:
    check_source_pins()
    check_deployed_arithmetic()
    curve_fixture(3)
    curve_fixture(4)
    check_incidence_floors()
    check_vandermonde_quotient_fixture()
    tamper_selftest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    if args.tamper_selftest:
        tamper_selftest()
        print("TAMPER_SELFTEST: PASS")
        return

    run_all()
    print("RANK16_FIXED27_RESIDUAL_SPECIALIZATION_CURVE: PASS")
    print(f"source_pins={len(SOURCE_PINS)} field=p={P} H_order={N} B={B} q64={N // B}")
    print(f"degrees=a={A} D={D} d={RESIDUAL_DEGREE} w={QUOTIENT_DEGREE} e=3,4")
    print("curve=cubic_degY<=2_span<=3 quartic_degY<=3_span<=4")
    print("normalization=nonzero_scalar_specialization")
    print("dependence=cubic_4_all_nonzero quartic_5_all_nonzero")
    print(
        "base_cap=28897 pairwise_gcd_cap=28897 "
        "union_floors=150361,109873"
    )
    print("quadratic_block=deg_r=1936 labels<=2 kappa_wall<=1")
    print("toy_curve_checks=e3,e4 quotient_vandermonde=PASS")
    print("ledger_payment=0 recurrence_payment=0 score=0/2")
    print("tamper_selftest=PASS")


if __name__ == "__main__":
    main()
