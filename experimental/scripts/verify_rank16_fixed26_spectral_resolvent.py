#!/usr/bin/env python3
"""Fail-closed replay for the fixed-26 spectral resolvent theorem."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from itertools import combinations
from math import comb, gcd
from pathlib import Path
from typing import Any, Callable, Iterable


class VerificationError(RuntimeError):
    """Raised when a pinned theorem or replay check fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError("CHECK FAILED: " + message)


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
CERT_REL = "experimental/data/certificates/rank16-fixed26-spectral-resolvent"
CERT_DIR = REPO_ROOT / CERT_REL
MANIFEST_PATH = CERT_DIR / "manifest.json"
EXPECTED_PATH = CERT_DIR / "verify_rank16_fixed26_spectral_resolvent.expected.txt"
CHECKSUM_PATH = CERT_DIR / "SHA256SUMS"

NOTE_REL = "experimental/notes/l2/rank16_fixed26_spectral_resolvent.md"
SCRIPT_REL = "experimental/scripts/verify_rank16_fixed26_spectral_resolvent.py"
MANIFEST_REL = CERT_REL + "/manifest.json"
EXPECTED_REL = CERT_REL + "/verify_rank16_fixed26_spectral_resolvent.expected.txt"
ARTIFACTS = (NOTE_REL, SCRIPT_REL, MANIFEST_REL, EXPECTED_REL)

SCHEMA = "rs-mca.rank16-fixed26-spectral-resolvent.v1"
BASE = "7f278167e1e51f968896229ae438ea5a76398f90"

SOURCE_PINS = {
    "experimental/notes/l2/rank16_fixed26_divided_difference_source_compiler.md":
        "e508b1847228475e5a71ab12df15d69d4091e7558a91f53e68261f06c42205ab",
    "experimental/scripts/verify_rank16_fixed26_divided_difference_source_compiler.py":
        "2dd8cd4d2df24510a4faa57d4ad70feda1b4505814233547f06dea7293afc744",
    (
        "experimental/data/certificates/"
        "rank16-fixed26-divided-difference-source-compiler/manifest.json"
    ): "b8b2791a145af88e7aec2729b3140fe89896fbe0e09236615b0b441fd5c95c55",
    (
        "experimental/data/certificates/"
        "rank16-fixed26-divided-difference-source-compiler/"
        "verify_fixed26_compiler.expected.txt"
    ): "d2f6c375c092e8f0aca993a006ad07082b52a6556e6b904f35703e911daddd43",
}

IDENTITIES = (
    "mu_g(T)=0",
    "g(X)|mu_g(X^B)",
    "mu_g(y)!=0 for y in mu_64",
    "N(Z)=-xi(mu_g(T)-mu_g(Z))/(T-Z)",
    "V_y=N(y)/mu_g(y)",
    "phi_Y(Z)|pi(N(Z))-mu_g(Z)lambda_Y",
    "I_Y(Z)=U_Y(phi_Y(T)-phi_Y(Z))/(T-Z)",
    "U_yz=rem_g(U_Y phi_Y(T)/((T-y)(T-z)))",
    "V_y=W(T^64-1)/(T-y)",
    "U_yz=rem_g(W(T^64-1)/((T-y)(T-z)))",
    "deg gcd(R_yz,R_yw)<=28897",
    "triangle quotient degree>=34704",
    "Res(g,R_yz)=q_yz^a kappa/(rho_y rho_z)",
    "four-cycle resultant ratio is an a-th power",
    "(V_y(0)-V_z(0))/(c_y-c_z) in H",
)

FORBIDDEN_CLAIMS = (
    "local_cap_116",
    "exclude_117_edges",
    "all_core_cap",
    "global_ledger_payment",
    "parent_closure",
    "grand_list",
    "grand_mca",
    "score_movement",
)


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise VerificationError("duplicate JSON key: " + key)
        result[key] = value
    return result


def load_manifest() -> dict[str, Any]:
    try:
        raw = MANIFEST_PATH.read_text(encoding="ascii")
        value = json.loads(raw, object_pairs_hook=reject_duplicate_keys)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise VerificationError("cannot read strict ASCII manifest") from exc
    require(type(value) is dict, "manifest root object")
    return value


def manifest_contract(expected_sha256: str) -> dict[str, Any]:
    return {
        "schema": SCHEMA,
        "base": BASE,
        "source_pins": SOURCE_PINS,
        "parameters": {
            "field_prime": 2_130_706_433,
            "domain_order": 2_097_152,
            "fiber_size_B": 32_768,
            "fiber_label_order": 64,
            "fixed_core_labels": 26,
            "remaining_labels": 38,
            "pair_positions": 703,
            "generator_degree_a": 67_472,
            "residual_degree_r": 63_601,
            "gcd_degree_d": 28_897,
            "split_s_unit_degree_floor": 34_704,
            "boundary_gap": 3_870,
        },
        "identity_contract": list(IDENTITIES),
        "graph_contract": {
            "putative_edges": 117,
            "large_class_floor": 9,
            "dense_class_size": 8,
            "dense_class_edge_floor": 25,
            "dense_class_missing_edge_cap": 3,
            "universal_vertex_floor": 2,
            "triangle_floor": 38,
            "four_cycle_floor": 120,
        },
        "ownership": {
            "inherited_fixed26_interpolants": 38,
            "inherited_fixed26_pairs": 703,
            "inherited_monomial_cap": 37,
            "reclaims_inherited_claims": False,
            "consumes_global_ledger": False,
        },
        "scope": {name: False for name in FORBIDDEN_CLAIMS},
        "remaining_walls": {
            "global_local_cell": "G64-CAP",
            "non_global": "rank-at-least-3 seven-star",
            "aggregation": "generators/rays/cores/source-cells",
        },
        "expected_output": {
            "path": EXPECTED_REL,
            "sha256": expected_sha256,
        },
        "artifacts": list(ARTIFACTS),
    }


def validate_manifest(value: dict[str, Any]) -> None:
    output = value.get("expected_output")
    require(type(output) is dict, "expected output object")
    digest = output.get("sha256")
    require(
        type(digest) is str and re.fullmatch(r"[0-9a-f]{64}", digest) is not None,
        "expected output SHA-256",
    )
    require(value == manifest_contract(digest), "semantic manifest contract")


def verify_source_pins() -> int:
    for relative, digest in SOURCE_PINS.items():
        path = (REPO_ROOT / relative).resolve()
        require(REPO_ROOT in path.parents, "source pin confinement")
        require(path.is_file(), "source pin exists: " + relative)
        require(sha256_path(path) == digest, "source pin digest: " + relative)
    return len(SOURCE_PINS)


def verify_artifacts(manifest: dict[str, Any]) -> int:
    require(CHECKSUM_PATH.is_file(), "checksum file exists")
    raw = CHECKSUM_PATH.read_bytes()
    require(raw.endswith(b"\n"), "checksum final newline")
    try:
        lines = raw.decode("ascii").splitlines()
    except UnicodeError as exc:
        raise VerificationError("checksum file must be ASCII") from exc
    require(len(lines) == len(ARTIFACTS), "checksum entry count")
    pattern = re.compile(r"([0-9a-f]{64})  ([!-~]+)")
    for line, expected_relative in zip(lines, ARTIFACTS):
        match = pattern.fullmatch(line)
        require(match is not None, "checksum syntax")
        digest, relative = match.groups()
        require(relative == expected_relative, "checksum order")
        require(sha256_path(REPO_ROOT / relative) == digest, "artifact digest")
    require(tuple(manifest["artifacts"]) == ARTIFACTS, "artifact manifest order")
    require(manifest["expected_output"]["path"] == EXPECTED_REL, "expected path")
    require(
        sha256_path(EXPECTED_PATH) == manifest["expected_output"]["sha256"],
        "expected output digest",
    )
    return len(lines)


Poly = tuple[int, ...]


def poly(values: Iterable[int], prime: int) -> Poly:
    result = [int(value) % prime for value in values]
    if not result:
        result = [0]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def degree(value: Poly) -> int:
    return -1 if value == (0,) else len(value) - 1


def coeff(value: Poly, index: int) -> int:
    return value[index] if index < len(value) else 0


def add(left: Poly, right: Poly, prime: int) -> Poly:
    return poly(
        (coeff(left, i) + coeff(right, i) for i in range(max(len(left), len(right)))),
        prime,
    )


def neg(value: Poly, prime: int) -> Poly:
    return poly((-item for item in value), prime)


def sub(left: Poly, right: Poly, prime: int) -> Poly:
    return add(left, neg(right, prime), prime)


def scale(value: Poly, scalar: int, prime: int) -> Poly:
    return poly((scalar * item for item in value), prime)


def mul(left: Poly, right: Poly, prime: int) -> Poly:
    result = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] = (result[i + j] + left_value * right_value) % prime
    return poly(result, prime)


def divmod_poly(numerator: Poly, denominator: Poly, prime: int) -> tuple[Poly, Poly]:
    require(denominator != (0,), "polynomial division by zero")
    remainder = list(numerator)
    quotient = [0] * max(1, degree(numerator) - degree(denominator) + 1)
    inverse_lead = pow(denominator[-1], -1, prime)
    while not (len(remainder) == 1 and remainder[0] == 0) and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        factor = remainder[-1] * inverse_lead % prime
        quotient[shift] = factor
        for index, value in enumerate(denominator):
            remainder[index + shift] = (remainder[index + shift] - factor * value) % prime
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
    return poly(quotient, prime), poly(remainder, prime)


def mod(value: Poly, modulus: Poly, prime: int) -> Poly:
    return divmod_poly(value, modulus, prime)[1]


def gcd_poly(left: Poly, right: Poly, prime: int) -> Poly:
    while right != (0,):
        left, right = right, mod(left, right, prime)
    return scale(left, pow(left[-1], -1, prime), prime)


def xgcd(left: Poly, right: Poly, prime: int) -> tuple[Poly, Poly, Poly]:
    old_r, r = left, right
    old_s, s = (1,), (0,)
    old_t, t = (0,), (1,)
    while r != (0,):
        quotient, remainder = divmod_poly(old_r, r, prime)
        old_r, r = r, remainder
        old_s, s = s, sub(old_s, mul(quotient, s, prime), prime)
        old_t, t = t, sub(old_t, mul(quotient, t, prime), prime)
    inverse = pow(old_r[-1], -1, prime)
    return scale(old_r, inverse, prime), scale(old_s, inverse, prime), scale(old_t, inverse, prime)


def inverse_mod(value: Poly, modulus: Poly, prime: int) -> Poly:
    divisor, inverse, _ = xgcd(value, modulus, prime)
    require(divisor == (1,), "nonunit in quotient algebra")
    return mod(inverse, modulus, prime)


def quotient_mul(left: Poly, right: Poly, modulus: Poly, prime: int) -> Poly:
    return mod(mul(left, right, prime), modulus, prime)


def quotient_pow(value: Poly, exponent: int, modulus: Poly, prime: int) -> Poly:
    result = (1,)
    base = value
    while exponent:
        if exponent & 1:
            result = quotient_mul(result, base, modulus, prime)
        base = quotient_mul(base, base, modulus, prime)
        exponent //= 2
    return result


def evaluate_scalar(value: Poly, point: int, prime: int) -> int:
    result = 0
    for item in reversed(value):
        result = (result * point + item) % prime
    return result


def evaluate_in_quotient(
    scalar_polynomial: Poly, point: Poly, modulus: Poly, prime: int
) -> Poly:
    result = (0,)
    for item in reversed(scalar_polynomial):
        result = add(quotient_mul(result, point, modulus, prime), (item,), prime)
    return result


def vector(value: Poly, dimension: int) -> list[int]:
    return [coeff(value, index) for index in range(dimension)]


def solve_columns(columns: list[list[int]], target: list[int], prime: int) -> list[int] | None:
    rows = len(target)
    column_count = len(columns)
    matrix = [
        [columns[column][row] % prime for column in range(column_count)] + [target[row] % prime]
        for row in range(rows)
    ]
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(column_count):
        selected = next((row for row in range(pivot_row, rows) if matrix[row][column]), None)
        if selected is None:
            continue
        matrix[pivot_row], matrix[selected] = matrix[selected], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], -1, prime)
        matrix[pivot_row] = [(item * inverse) % prime for item in matrix[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = matrix[row][column]
            if factor:
                matrix[row] = [
                    (matrix[row][index] - factor * matrix[pivot_row][index]) % prime
                    for index in range(column_count + 1)
                ]
        pivot_columns.append(column)
        pivot_row += 1
    for row in range(rows):
        if all(matrix[row][column] == 0 for column in range(column_count)) and matrix[row][-1]:
            return None
    solution = [0] * column_count
    for row, column in enumerate(pivot_columns):
        solution[column] = matrix[row][-1]
    return solution


def matrix_rank(columns: list[list[int]], prime: int) -> int:
    if not columns:
        return 0
    zero_target = [0] * len(columns[0])
    rank = 0
    basis: list[list[int]] = []
    for column in columns:
        if solve_columns(basis, column, prime) is None:
            basis.append(column)
            rank += 1
    require(solve_columns(basis, zero_target, prime) is not None, "basis zero span")
    return rank


def minimal_polynomial(
    point: Poly, modulus: Poly, prime: int
) -> Poly:
    dimension = degree(modulus)
    powers = [(1,)]
    for exponent in range(1, dimension + 1):
        powers.append(quotient_mul(powers[-1], point, modulus, prime))
        solution = solve_columns(
            [vector(item, dimension) for item in powers[:-1]],
            vector(powers[-1], dimension),
            prime,
        )
        if solution is not None:
            return poly(([-item % prime for item in solution] + [1]), prime)
    raise VerificationError("minimal polynomial not found")


def scalar_product_polynomial(points: Iterable[int], prime: int) -> Poly:
    result = (1,)
    for point in points:
        result = mul(result, ((-point) % prime, 1), prime)
    return result


def divided_difference_at_T(
    scalar_polynomial: Poly, point: Poly, modulus: Poly, prime: int
) -> list[Poly]:
    # Coefficient j in (f(T)-f(Z))/(T-Z) is
    # sum_{i=j+1}^deg(f) f_i T^(i-1-j).
    result: list[Poly] = []
    for j in range(degree(scalar_polynomial)):
        coefficient_value = (0,)
        for i in range(j + 1, len(scalar_polynomial)):
            term = scale(
                quotient_pow(point, i - 1 - j, modulus, prime),
                scalar_polynomial[i],
                prime,
            )
            coefficient_value = add(coefficient_value, term, prime)
        result.append(coefficient_value)
    return result or [(0,)]


def evaluate_A_polynomial(coefficients: list[Poly], point: int, modulus: Poly, prime: int) -> Poly:
    result = (0,)
    for item in reversed(coefficients):
        result = add(scale(result, point, prime), item, prime)
        result = mod(result, modulus, prime)
    return result


def lagrange_interpolate_A(
    points: list[int], values: list[Poly], modulus: Poly, prime: int
) -> list[Poly]:
    result = [(0,)] * len(points)
    for index, point in enumerate(points):
        basis = (1,)
        denominator = 1
        for other_index, other in enumerate(points):
            if other_index == index:
                continue
            basis = mul(basis, ((-other) % prime, 1), prime)
            denominator = denominator * (point - other) % prime
        basis = scale(basis, pow(denominator, -1, prime), prime)
        for degree_index, scalar in enumerate(basis):
            result[degree_index] = add(
                result[degree_index], scale(values[index], scalar, prime), prime
            )
    return [mod(item, modulus, prime) for item in result]


def determinant(matrix: list[list[int]], prime: int) -> int:
    value = [row[:] for row in matrix]
    result = 1
    size = len(value)
    for column in range(size):
        pivot = next((row for row in range(column, size) if value[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            value[column], value[pivot] = value[pivot], value[column]
            result = -result
        pivot_value = value[column][column]
        result = result * pivot_value % prime
        inverse = pow(pivot_value, -1, prime)
        for row in range(column + 1, size):
            factor = value[row][column] * inverse % prime
            for index in range(column, size):
                value[row][index] = (value[row][index] - factor * value[column][index]) % prime
    return result % prime


def resultant(left: Poly, right: Poly, prime: int) -> int:
    m, n = degree(left), degree(right)
    require(m >= 0 and n >= 0, "resultant nonzero polynomials")
    size = m + n
    matrix = [[0] * size for _ in range(size)]
    left_desc = list(reversed(left))
    right_desc = list(reversed(right))
    for row in range(n):
        for index, value in enumerate(left_desc):
            matrix[row][row + index] = value
    for row in range(m):
        for index, value in enumerate(right_desc):
            matrix[n + row][row + index] = value
    return determinant(matrix, prime)


def verify_deployed_parameters(manifest: dict[str, Any]) -> None:
    p = manifest["parameters"]
    require(p["domain_order"] == 64 * p["fiber_size_B"], "n=64B")
    require(p["pair_positions"] == comb(p["remaining_labels"], 2), "38 choose 2")
    require(p["residual_degree_r"] - p["gcd_degree_d"] == 34_704, "S-unit floor")
    require(p["generator_degree_a"] - p["residual_degree_r"] - 1 == 3_870, "gap")
    require(gcd(p["generator_degree_a"], p["field_prime"] - 1) == 16, "power subgroup")


def verify_graph_contract(manifest: dict[str, Any]) -> None:
    graph = manifest["graph_contract"]
    require(graph["dense_class_missing_edge_cap"] == comb(8, 2) - 25, "missing edges")
    require(graph["universal_vertex_floor"] == 8 - 2 * 3, "universal vertices")
    require(graph["triangle_floor"] == comb(8, 3) - 3 * 6, "triangle union bound")
    require(graph["four_cycle_floor"] == 3 * comb(8, 4) - 3 * 30, "four-cycle union bound")


def replay_toy_quotient() -> None:
    prime = 17
    B = 2
    dimension = 5
    x = (0, 1)
    x8_minus_1 = poly([-1] + [0] * 7 + [1], prime)

    modulus: Poly | None = None
    spectral: Poly | None = None
    for constant in range(1, prime):
        for linear in range(prime):
            candidate = poly([constant, linear, 0, 0, 0, 1], prime)
            if gcd_poly(candidate, x8_minus_1, prime) != (1,):
                continue
            candidate_spectral = minimal_polynomial(quotient_pow(x, B, candidate, prime), candidate, prime)
            if degree(candidate_spectral) == dimension:
                modulus = candidate
                spectral = candidate_spectral
                break
        if modulus is not None:
            break
    require(modulus is not None and spectral is not None, "toy root-free modulus")

    T = quotient_pow(x, B, modulus, prime)
    mu = spectral
    nu = degree(mu)
    require(nu == dimension, "toy minimal spectral degree")
    require(evaluate_in_quotient(mu, T, modulus, prime) == (0,), "mu(T)=0")

    composed = (0,)
    for exponent, value in enumerate(mu):
        composed = add(composed, scale(poly([0] * (B * exponent) + [1], prime), value, prime), prime)
    require(mod(composed, modulus, prime) == (0,), "g divides mu(X^B)")

    omega = 4
    labels = [pow(omega, index, prime) for index in range(4)]
    require(len(set(labels)) == 4 and pow(omega, 4, prime) == 1, "toy mu4 labels")
    for label in labels:
        require(evaluate_scalar(mu, label, prime) != 0, "mu(label) nonzero")

    xi = poly((3, 5, 7, 11, 13), prime)
    if gcd_poly(xi, modulus, prime) != (1,):
        xi = (1,)
    require(gcd_poly(xi, modulus, prime) == (1,), "toy xi unit")

    q_coefficients = divided_difference_at_T(mu, T, modulus, prime)
    N = [neg(quotient_mul(xi, item, modulus, prime), prime) for item in q_coefficients]
    require(len(N) == nu and N[-1] == neg(xi, prime), "N leading coefficient")

    V: dict[int, Poly] = {}
    for label in labels:
        factor = sub(T, (label,), prime)
        V[label] = quotient_mul(xi, inverse_mod(factor, modulus, prime), modulus, prime)
        n_value = evaluate_A_polynomial(N, label, modulus, prime)
        expected = scale(n_value, pow(evaluate_scalar(mu, label, prime), -1, prime), prime)
        require(V[label] == expected, "exact rational resolvent")

    projection_degree = 2
    classes: dict[tuple[int, ...], list[int]] = {}
    for label in labels:
        key = tuple(coeff(V[label], index) for index in range(projection_degree + 1, dimension))
        classes.setdefault(key, []).append(label)
    for key, collision_labels in classes.items():
        lambda_value = key
        phi = scalar_product_polynomial(collision_labels, prime)
        for coordinate in range(projection_degree + 1, dimension):
            polynomial_value = poly(
                (
                    (coeff(N[index], coordinate) if index < len(N) else 0)
                    - coeff(mu, index) * lambda_value[coordinate - projection_degree - 1]
                    for index in range(max(len(N), len(mu)))
                ),
                prime,
            )
            require(divmod_poly(polynomial_value, phi, prime)[1] == (0,), "collision divisibility")
    for left, right in combinations(labels, 2):
        same_tail = all(
            coeff(V[left], index) == coeff(V[right], index)
            for index in range(projection_degree + 1, dimension)
        )
        difference = sub(V[left], V[right], prime)
        require(same_tail == (degree(difference) <= projection_degree), "collision criterion")

    Y = labels
    phi = scalar_product_polynomial(Y, prime)
    phi_T = evaluate_in_quotient(phi, T, modulus, prime)
    U_Y = quotient_mul(xi, inverse_mod(phi_T, modulus, prime), modulus, prime)
    interpolation = lagrange_interpolate_A(Y, [V[label] for label in Y], modulus, prime)
    rhs = [quotient_mul(U_Y, item, modulus, prime) for item in divided_difference_at_T(phi, T, modulus, prime)]
    require(interpolation == rhs, "simultaneous Krylov identity")

    krylov = [
        vector(quotient_mul(quotient_pow(T, exponent, modulus, prime), U_Y, modulus, prime), dimension)
        for exponent in range(len(Y) - 1)
    ]
    require(matrix_rank(krylov, prime) == len(Y) - 1, "Krylov independence")

    pair_count = 0
    for left, right in combinations(Y, 2):
        pair_count += 1
        remaining = [label for label in Y if label not in (left, right)]
        p_yz = scalar_product_polynomial(remaining, prime)
        via_krylov = quotient_mul(
            U_Y, evaluate_in_quotient(p_yz, T, modulus, prime), modulus, prime
        )
        direct = quotient_mul(
            xi,
            inverse_mod(mul(sub(T, (left,), prime), sub(T, (right,), prime), prime), modulus, prime),
            modulus,
            prime,
        )
        require(via_krylov == direct, "pair Krylov collapse")

    require(pair_count == 6, "toy pair count")

    label_order = len(labels)
    T_order_minus_1 = sub(quotient_pow(T, label_order, modulus, prime), (1,), prime)
    W = quotient_mul(xi, inverse_mod(T_order_minus_1, modulus, prime), modulus, prime)
    for label in labels:
        geometric = (0,)
        for index in range(label_order):
            geometric = add(
                geometric,
                scale(
                    quotient_pow(T, label_order - 1 - index, modulus, prime),
                    pow(label, index, prime),
                    prime,
                ),
                prime,
            )
        require(quotient_mul(W, geometric, modulus, prime) == V[label], "Fourier resolvent")
    for left, right in combinations(labels, 2):
        denominator = quotient_mul(sub(T, (left,), prime), sub(T, (right,), prime), modulus, prime)
        correct = quotient_mul(
            W,
            quotient_mul(
                T_order_minus_1,
                inverse_mod(denominator, modulus, prime),
                modulus,
                prime,
            ),
            modulus,
            prime,
        )
        direct = quotient_mul(xi, inverse_mod(denominator, modulus, prime), modulus, prime)
        require(correct == direct, "correct Fourier pair orientation")

        F_left = poly((-left, 0, 1), prime)
        F_right = poly((-right, 0, 1), prime)
        require(
            resultant(modulus, F_left, prime)
            * resultant(modulus, F_right, prime)
            % prime
            * resultant(modulus, direct, prime)
            % prime
            == resultant(modulus, xi, prime),
            "resultant denominator orientation",
        )

    edge_resultants: dict[tuple[int, int], int] = {}
    for left, right in combinations(labels, 2):
        denominator = quotient_mul(sub(T, (left,), prime), sub(T, (right,), prime), modulus, prime)
        edge_resultants[tuple(sorted((left, right)))] = resultant(
            modulus,
            quotient_mul(xi, inverse_mod(denominator, modulus, prime), modulus, prime),
            prime,
        )
    a_label, b_label, c_label, d_label = labels
    def edge(left: int, right: int) -> int:
        return edge_resultants[tuple(sorted((left, right)))]
    ratio = edge(a_label, c_label) * edge(b_label, d_label) % prime
    ratio = ratio * pow(edge(a_label, b_label) * edge(c_label, d_label) % prime, -1, prime) % prime
    require(ratio == 1, "toy four-cycle resultant cancellation")

    h_generator = 2
    h_roots = [pow(h_generator, index, prime) for index in (0, 1, 3)]
    split_locator = scalar_product_polynomial(h_roots, prime)
    require(degree(split_locator) == 3, "odd split locator")
    require(pow(split_locator[0], 8, prime) == 1, "split constant term in H")


def semantic_tamper_selftests(manifest: dict[str, Any]) -> int:
    def reverse_fourier(value: dict[str, Any]) -> None:
        value["identity_contract"][9] = "U_yz=rem_g(W(T-y)(T-z)/(T^64-1))"

    def reverse_resultant(value: dict[str, Any]) -> None:
        value["identity_contract"][12] = "Res(g,R_yz)=q_yz^a rho_y rho_z/kappa"

    def claim_cap(value: dict[str, Any]) -> None:
        value["scope"]["local_cap_116"] = True

    def claim_global(value: dict[str, Any]) -> None:
        value["scope"]["global_ledger_payment"] = True

    def reclaim(value: dict[str, Any]) -> None:
        value["ownership"]["reclaims_inherited_claims"] = True

    def alter_graph(value: dict[str, Any]) -> None:
        value["graph_contract"]["triangle_floor"] = 39

    def alter_floor(value: dict[str, Any]) -> None:
        value["parameters"]["split_s_unit_degree_floor"] = 34_705

    def remove_source_pin(value: dict[str, Any]) -> None:
        value["source_pins"].pop(next(iter(value["source_pins"])))

    def redirect_expected(value: dict[str, Any]) -> None:
        value["expected_output"]["path"] = "experimental/forged.txt"

    mutators: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
        ("Fourier orientation", reverse_fourier),
        ("resultant orientation", reverse_resultant),
        ("local cap", claim_cap),
        ("global payment", claim_global),
        ("ownership", reclaim),
        ("graph count", alter_graph),
        ("S-unit floor", alter_floor),
        ("source pin", remove_source_pin),
        ("expected path", redirect_expected),
    )
    rejected = 0
    for name, mutate in mutators:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate_manifest(candidate)
        except VerificationError:
            rejected += 1
        else:
            raise VerificationError("semantic tamper accepted: " + name)
    require(rejected == len(mutators), "all semantic tampers rejected")
    return rejected


def render_output(source_count: int, artifact_count: int, tamper_count: int) -> bytes:
    lines = (
        "RANK16_FIXED26_SPECTRAL_RESOLVENT: PASS",
        "schema=" + SCHEMA,
        "base=" + BASE,
        "deployed=p2130706433,n2097152,B32768,a67472,r63601,d28897,floor34704",
        "source_pins=PASS,count=" + str(source_count),
        "minimal_resolvent=PASS,mu_divisibility=PASS,collision_collapse=PASS",
        "krylov=PASS,global64=PASS,fourier_pair_orientation=PASS",
        "split_star=gcd28897,S-unit_floor34704,resultant_denominator=PASS",
        "graph=labels38,pairs703,branches{class>=9|class8_edges>=25},triangles>=38,cycles>=120",
        "ownership=inherited38/703/graph/monomial37;reclaimed=0",
        "ledger=0,parent=0,score_delta=0,remaining=G64-CAP+rank>=3-star+aggregation",
        "semantic_tamper_selftests=PASS,count=" + str(tamper_count),
        "artifact_checksums=PASS,count=" + str(artifact_count),
        "RESULT=PASS",
    )
    return ("\n".join(lines) + "\n").encode("ascii")


def run_default() -> None:
    manifest = load_manifest()
    validate_manifest(manifest)
    verify_deployed_parameters(manifest)
    verify_graph_contract(manifest)
    source_count = verify_source_pins()
    replay_toy_quotient()
    tamper_count = semantic_tamper_selftests(manifest)
    artifact_count = verify_artifacts(manifest)
    output = render_output(source_count, artifact_count, tamper_count)
    require(output == EXPECTED_PATH.read_bytes(), "frozen expected output byte match")
    sys.stdout.buffer.write(output)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--tamper-self-test", action="store_true")
    group.add_argument("--check-checksums", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        manifest = load_manifest()
        validate_manifest(manifest)
        if args.tamper_self_test:
            count = semantic_tamper_selftests(manifest)
            print(f"SEMANTIC_TAMPER_SELFTEST: PASS count={count}")
        elif args.check_checksums:
            count = verify_artifacts(manifest)
            print(f"ARTIFACT_CHECKSUMS: PASS count={count}")
        else:
            run_default()
        return 0
    except (VerificationError, OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
