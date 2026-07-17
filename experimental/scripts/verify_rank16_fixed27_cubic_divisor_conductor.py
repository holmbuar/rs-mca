#!/usr/bin/env python3
"""Replay the accepted R28 Role 03 cubic divisor/conductor theorem package."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from math import isqrt
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[2]
NOTE_PATH = ROOT / "experimental/notes/l2/rank16_fixed27_cubic_divisor_conductor.md"
MANIFEST_PATH = (
    ROOT
    / "experimental/data/certificates/rank16-fixed27-cubic-divisor-conductor/source_manifest.json"
)
EXPECTED_PATH = Path(__file__).with_suffix(".expected.txt")

BASE_HEAD = "7f278167e1e51f968896229ae438ea5a76398f90"
PR863_HEAD = "55fa998275db505214347db296bdd8e38a3896e6"
NOTE_SHA256 = "f3fdcaa739c6a09ad824a203fcb1c8bdc2f9bded1111bcdc8e458f9089227305"
MANIFEST_SHA256 = "2e66a79dc2856ec8dca52f7a6641ce896085782bc24f166f6a2a3c8c01f7497b"
EXPECTED_SHA256 = "ee774950f25653a898673062c1416ee8e677f33c323e124f3a7c895e9d03de55"

P = 2_130_706_433
N = 2_097_152
M_SOURCE = 1_116_047
K = 1_048_576
SIGMA = M_SOURCE - K
T_SOURCE = N - M_SOURCE
B = 32_768
A_DEG = SIGMA + 1
D = T_SOURCE - 27 * B
R_DEG = D - B
W_DEG = D - A_DEG
CUBIC_DEFICIT = 3 * B - A_DEG
FIRST_LAYER_GAP = B - W_DEG
RESULTANT_M_BOUND = 3 * W_DEG - CUBIC_DEFICIT
RESULTANT_DEG_BOUND = 2 * A_DEG + RESULTANT_M_BOUND

INTEGRATED_SOURCE_PINS = {
    "experimental/notes/l2/rank16_fixed_core_quotient_line_obstruction.md":
        "19325c602ae14082f6ef36db312d815552e0f0eefc0787f3a71fd4254af650f7",
    "experimental/scripts/verify_rank16_fixed_core_quotient_line_obstruction.py":
        "0e7e25a2e696941f42d7eaf24c4b441e769592c3ffff040883bb9b076765d7dd",
    "experimental/scripts/verify_rank16_fixed_core_quotient_line_obstruction.expected.txt":
        "8dbe50b5911bfcdbc10fcc3ee578398d0d068f43f57b672c4e84eb42b64dc109",
    "experimental/notes/l2/rank16_fixed27_block_wedge_stratification.md":
        "b061ede06b138643655cd8c7f9f53e724eb974e9acf924e2e6883f0468cb3c4e",
    "experimental/scripts/verify_rank16_fixed27_block_wedge_stratification.py":
        "345488c3063cfa8c3e9027d83350d26bfc0b40e34abd104f151da0c02318607e",
    "experimental/scripts/verify_rank16_fixed27_block_wedge_stratification.expected.txt":
        "6ba9396b444b490d9d20f1300b92541d04e06ffa718e4bbf35d2e4d114855670",
}

PENDING_SOURCE_PINS = {
    "experimental/notes/l2/rank16_fixed27_residual_specialization_curve.md":
        "dc82be9d643ea9df85f843988acbc38149881297369096e869a6d19082faa195",
    "experimental/data/certificates/rank16-fixed27-residual-specialization-curve/README.md":
        "7c4e5228f44f1a26584515a75a2e8ec14b808406f44d9557d503e6a646ee2c7c",
    "experimental/data/certificates/rank16-fixed27-residual-specialization-curve/SHA256SUMS.txt":
        "08c7481d82a8a9e27d1a7c32931fe1e08271c1d9605549e283f14aa54b1e3eb8",
    "experimental/data/certificates/rank16-fixed27-residual-specialization-curve/verify_rank16_fixed27_residual_specialization_curve.py":
        "5fa2831e3699bdc1a671f23a231e0a865d82157b4c5131d6836aac65dcfab9b7",
    "experimental/data/certificates/rank16-fixed27-residual-specialization-curve/verify_rank16_fixed27_residual_specialization_curve.expected.txt":
        "382da0d934131d8f514b0450f81b9bbee044806ac12f37d8cb2ecc45dfbcb016",
}

CONTRACT: dict[str, Any] = {
    "source": {
        "base_head": BASE_HEAD,
        "pr863_head": PR863_HEAD,
        "fixed_core_size": 27,
        "fixed_generator": True,
        "fixed_syndrome_ray": True,
        "fixed_source_cell": True,
        "actual_labels": 7,
        "e": 3,
        "kappa_B_at_most": 1,
        "all_source_filters_retained": True,
    },
    "claims": {
        "primitive_cubic_reducible": True,
        "remainder": "R=-rem_g(h*((a0(T)-a0(Y))/(T-Y)))",
        "cubic_deficit": CUBIC_DEFICIT,
        "first_layer_deficit_at_most": W_DEG,
        "first_layer_degree_at_least": FIRST_LAYER_GAP,
        "some_conductor_at_most": 16,
        "quadratic_alternative_at_most": 8,
        "squarefree_resultant_g_exponent": 2,
        "resultant_M_degree_at_most": RESULTANT_M_BOUND,
        "resultant_total_degree_at_most": RESULTANT_DEG_BOUND,
    },
    "payments": {
        "finite": 0,
        "asymptotic": 0,
        "parent": 0,
        "official_score": "0/2",
    },
    "nonclaims": {
        "seven_label_closure": False,
        "reverse_source_construction": False,
        "cross_cell_aggregation": False,
        "rank16_closure": False,
    },
}


class CheckError(RuntimeError):
    """A fail-closed replay check failed."""


class ContractError(CheckError):
    """The accepted theorem scope or claim layer changed."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckError(message)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_file_pin(path: Path, expected: str, label: str) -> None:
    require(path.is_file(), f"missing pinned {label}: {path}")
    actual = sha256_file(path)
    require(actual == expected, f"{label} hash mismatch: {actual}")


def contract_value(contract: dict[str, Any], *path: str) -> Any:
    value: Any = contract
    try:
        for key in path:
            value = value[key]
    except (KeyError, TypeError) as exc:
        raise ContractError("missing contract field: " + ".".join(path)) from exc
    return value


def contract_exact(contract: dict[str, Any], path: tuple[str, ...], expected: Any) -> None:
    actual = contract_value(contract, *path)
    if type(actual) is not type(expected) or actual != expected:
        raise ContractError(
            f"{'.'.join(path)}: expected {expected!r}, got {actual!r}"
        )


def validate_contract(contract: dict[str, Any]) -> None:
    checks = (
        (("source", "base_head"), BASE_HEAD),
        (("source", "pr863_head"), PR863_HEAD),
        (("source", "fixed_core_size"), 27),
        (("source", "fixed_generator"), True),
        (("source", "fixed_syndrome_ray"), True),
        (("source", "fixed_source_cell"), True),
        (("source", "actual_labels"), 7),
        (("source", "e"), 3),
        (("source", "kappa_B_at_most"), 1),
        (("source", "all_source_filters_retained"), True),
        (("claims", "primitive_cubic_reducible"), True),
        (("claims", "remainder"), "R=-rem_g(h*((a0(T)-a0(Y))/(T-Y)))"),
        (("claims", "cubic_deficit"), 30_832),
        (("claims", "first_layer_deficit_at_most"), 28_897),
        (("claims", "first_layer_degree_at_least"), 3_871),
        (("claims", "some_conductor_at_most"), 16),
        (("claims", "quadratic_alternative_at_most"), 8),
        (("claims", "squarefree_resultant_g_exponent"), 2),
        (("claims", "resultant_M_degree_at_most"), 55_859),
        (("claims", "resultant_total_degree_at_most"), 190_803),
        (("payments", "finite"), 0),
        (("payments", "asymptotic"), 0),
        (("payments", "parent"), 0),
        (("payments", "official_score"), "0/2"),
        (("nonclaims", "seven_label_closure"), False),
        (("nonclaims", "reverse_source_construction"), False),
        (("nonclaims", "cross_cell_aggregation"), False),
        (("nonclaims", "rank16_closure"), False),
    )
    for path, expected in checks:
        contract_exact(contract, path, expected)


def expected_manifest() -> dict[str, Any]:
    return {
        "schema": "rs-mca.r28-role03-cubic-divisor-conductor-source-pins.v1",
        "base": {"ref": "origin/main", "commit": BASE_HEAD},
        "external_return": {
            "path_hint": (
                "/Users/danielcabezas/RS_MCA_HOMERUN_9PRO_20260717_R28/"
                "returns_raw/pro_chrome/role_03/r28_role03_clean_final.md"
            ),
            "sha256": "5b9932f803d2d03a35adde85efb53b4aa8c0eddff55f7db3bf572a9eff2dc75b",
        },
        "packet": {
            "archive": "RS_MCA_R28_ROLE_03_RANK16_FIXED27_CUBIC.zip",
            "sha256": "9be965f8fb41a9bc9ba32b11210d9c6437f01b329a4a6cc2b963a86335f7cfed",
            "source_file_count": 96,
        },
        "missing_worker_attachments": [
            {
                "name": "R28_ROLE03_CUBIC_DIVISOR_CONDUCTOR_REPLAY.py",
                "claimed_sha256": (
                    "ad0ef2f27eb234d19d0c5a7a30fc3745921a48ac99d62201c4a72ce014f55524"
                ),
            },
            {
                "name": "R28_ROLE03_CUBIC_DIVISOR_CONDUCTOR_REPLAY.expected.txt",
                "claimed_sha256": EXPECTED_SHA256,
            },
        ],
        "dependencies": [
            {
                "pr": 826,
                "head": "b6ea362d7aef96bd808fc6799fd45efc4470f476",
                "status": "integrated_at_base",
                "files": {
                    key: INTEGRATED_SOURCE_PINS[key]
                    for key in (
                        "experimental/notes/l2/rank16_fixed_core_quotient_line_obstruction.md",
                        "experimental/scripts/verify_rank16_fixed_core_quotient_line_obstruction.py",
                        "experimental/scripts/verify_rank16_fixed_core_quotient_line_obstruction.expected.txt",
                    )
                },
            },
            {
                "pr": 843,
                "head": "7a8d2ce071af76ec13aab91eff5f3c7182f0d63c",
                "status": "integrated_at_base",
                "packet_note_sha256": (
                    "c5b008082efcad270cecf88688d69499543086ed86d1a29f655a07263f362a6d"
                ),
                "files": {
                    key: INTEGRATED_SOURCE_PINS[key]
                    for key in (
                        "experimental/notes/l2/rank16_fixed27_block_wedge_stratification.md",
                        "experimental/scripts/verify_rank16_fixed27_block_wedge_stratification.py",
                        "experimental/scripts/verify_rank16_fixed27_block_wedge_stratification.expected.txt",
                    )
                },
            },
            {
                "pr": 863,
                "head": PR863_HEAD,
                "status": "pending_conditional_dependency",
                "files": dict(PENDING_SOURCE_PINS),
            },
        ],
        "accepted_claims": [
            "primitive_cubic_reducibility",
            "divided_difference_remainder",
            "nested_divisor_deficit_budget",
            "conductor_at_most_16_with_quadratic_alternative_at_most_8",
            "squarefree_resultant_g_squared_M_degree_at_most_55859",
        ],
        "nonclaims": {
            "seven_label_closure": False,
            "finite_payment": 0,
            "asymptotic_payment": 0,
            "parent_payment": 0,
            "official_score": "0/2",
        },
    }


def validate_manifest(manifest: dict[str, Any]) -> None:
    expected = expected_manifest()
    if manifest != expected:
        raise ContractError("source manifest differs from the accepted pin set")


def verify_statement_and_sources() -> None:
    verify_file_pin(NOTE_PATH, NOTE_SHA256, "theorem statement")
    verify_file_pin(MANIFEST_PATH, MANIFEST_SHA256, "source manifest")
    verify_file_pin(EXPECTED_PATH, EXPECTED_SHA256, "expected transcript")

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    require(isinstance(manifest, dict), "source manifest root must be an object")
    validate_manifest(manifest)

    for relative, expected in INTEGRATED_SOURCE_PINS.items():
        verify_file_pin(ROOT / relative, expected, f"integrated source {relative}")

    pending_paths = [ROOT / relative for relative in PENDING_SOURCE_PINS]
    present_count = sum(path.is_file() for path in pending_paths)
    require(
        present_count in (0, len(pending_paths)),
        "PR #863 dependency is only partially attached",
    )
    if present_count == len(pending_paths):
        for relative, expected in PENDING_SOURCE_PINS.items():
            verify_file_pin(ROOT / relative, expected, f"PR #863 source {relative}")


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    for divisor in range(3, isqrt(number) + 1, 2):
        if number % divisor == 0:
            return False
    return True


def v2(number: int) -> int:
    require(number > 0, "v2 requires a positive integer")
    exponent = 0
    while number % 2 == 0:
        exponent += 1
        number //= 2
    return exponent


def verify_constants() -> None:
    require(is_prime(P), "deployed field modulus is not prime")
    require(P == 127 * (1 << 24) + 1, "field factorization drift")
    require(N == 1 << 21, "deployed n drift")
    require(B == 1 << 15, "deployed block size drift")
    require((P - 1) % B == 0, "mu_B is not contained in F_p")
    require(T_SOURCE == 981_105, "t arithmetic drift")
    require(SIGMA == 67_471, "sigma arithmetic drift")
    require(A_DEG == 67_472, "generator degree drift")
    require(D == 96_369, "D arithmetic drift")
    require(R_DEG == 63_601, "residual degree drift")
    require(W_DEG == 28_897, "source tail degree drift")
    require(CUBIC_DEFICIT == 30_832, "cubic deficit drift")
    require(FIRST_LAYER_GAP == 3_871, "first-layer gap drift")
    require(A_DEG - R_DEG == 3_871, "a-d gap drift")
    require(R_DEG - W_DEG == A_DEG - B == 34_704, "d-w identity drift")
    require(A_DEG - 2 * B == 1_936, "a-2B identity drift")
    require(v2(CUBIC_DEFICIT) == 4, "cubic deficit 2-adic valuation drift")


Sparse = dict[tuple[int, int, int, int, int], int]


def sparse_atom(index: int) -> Sparse:
    exponent = [0, 0, 0, 0, 0]
    exponent[index] = 1
    return {tuple(exponent): 1}


def sparse_add(left: Sparse, right: Sparse) -> Sparse:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, 0) + coefficient
        if result[monomial] == 0:
            del result[monomial]
    return result


def sparse_scale(poly: Sparse, scalar: int) -> Sparse:
    return {
        monomial: scalar * coefficient
        for monomial, coefficient in poly.items()
        if scalar * coefficient
    }


def sparse_sub(left: Sparse, right: Sparse) -> Sparse:
    return sparse_add(left, sparse_scale(right, -1))


def sparse_mul(left: Sparse, right: Sparse) -> Sparse:
    result: Sparse = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(
                left_monomial[index] + right_monomial[index]
                for index in range(5)
            )
            result[monomial] = (
                result.get(monomial, 0) + left_coefficient * right_coefficient
            )
            if result[monomial] == 0:
                del result[monomial]
    return result


def sparse_pow(poly: Sparse, exponent: int) -> Sparse:
    result: Sparse = {(0, 0, 0, 0, 0): 1}
    factor = poly
    power = exponent
    while power:
        if power & 1:
            result = sparse_mul(result, factor)
        factor = sparse_mul(factor, factor)
        power >>= 1
    return result


def verify_divided_difference_symbolically() -> None:
    t_var = sparse_atom(0)
    y_var = sparse_atom(1)
    c2_var = sparse_atom(2)
    c1_var = sparse_atom(3)
    c0_var = sparse_atom(4)

    def cubic(variable: Sparse) -> Sparse:
        return sparse_add(
            sparse_add(
                sparse_pow(variable, 3),
                sparse_mul(c2_var, sparse_pow(variable, 2)),
            ),
            sparse_add(sparse_mul(c1_var, variable), c0_var),
        )

    quotient = sparse_add(
        sparse_pow(y_var, 2),
        sparse_add(
            sparse_mul(sparse_add(t_var, c2_var), y_var),
            sparse_add(
                sparse_pow(t_var, 2),
                sparse_add(sparse_mul(c2_var, t_var), c1_var),
            ),
        ),
    )
    left = sparse_sub(cubic(t_var), cubic(y_var))
    right = sparse_mul(sparse_sub(t_var, y_var), quotient)
    require(left == right, "monic cubic divided-difference identity failed")


Poly = list[int]


def poly_trim(poly: Poly, prime: int) -> Poly:
    result = [coefficient % prime for coefficient in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result or [0]


def poly_zero(poly: Poly, prime: int) -> bool:
    return poly_trim(poly, prime) == [0]


def poly_degree(poly: Poly, prime: int) -> int:
    normalized = poly_trim(poly, prime)
    return -1 if normalized == [0] else len(normalized) - 1


def poly_add(left: Poly, right: Poly, prime: int) -> Poly:
    size = max(len(left), len(right))
    result = [0] * size
    for index in range(size):
        result[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    return poly_trim(result, prime)


def poly_sub(left: Poly, right: Poly, prime: int) -> Poly:
    size = max(len(left), len(right))
    result = [0] * size
    for index in range(size):
        result[index] = (
            (left[index] if index < len(left) else 0)
            - (right[index] if index < len(right) else 0)
        ) % prime
    return poly_trim(result, prime)


def poly_scale(poly: Poly, scalar: int, prime: int) -> Poly:
    return poly_trim([scalar * coefficient for coefficient in poly], prime)


def poly_mul(left: Poly, right: Poly, prime: int) -> Poly:
    if poly_zero(left, prime) or poly_zero(right, prime):
        return [0]
    result = [0] * (len(left) + len(right) - 1)
    for i, left_coefficient in enumerate(left):
        for j, right_coefficient in enumerate(right):
            result[i + j] = (
                result[i + j] + left_coefficient * right_coefficient
            ) % prime
    return poly_trim(result, prime)


def poly_divmod(numerator: Poly, denominator: Poly, prime: int) -> tuple[Poly, Poly]:
    denominator = poly_trim(denominator, prime)
    require(not poly_zero(denominator, prime), "polynomial division by zero")
    remainder = poly_trim(numerator, prime)
    quotient = [0] * max(
        1, poly_degree(remainder, prime) - poly_degree(denominator, prime) + 1
    )
    denominator_degree = poly_degree(denominator, prime)
    inverse_lead = pow(denominator[-1], -1, prime)
    while (
        not poly_zero(remainder, prime)
        and poly_degree(remainder, prime) >= denominator_degree
    ):
        shift = poly_degree(remainder, prime) - denominator_degree
        coefficient = remainder[-1] * inverse_lead % prime
        quotient[shift] = (quotient[shift] + coefficient) % prime
        subtraction = [0] * shift + poly_scale(denominator, coefficient, prime)
        remainder = poly_sub(remainder, subtraction, prime)
    return poly_trim(quotient, prime), poly_trim(remainder, prime)


def poly_mod(numerator: Poly, denominator: Poly, prime: int) -> Poly:
    return poly_divmod(numerator, denominator, prime)[1]


def poly_gcd(left: Poly, right: Poly, prime: int) -> Poly:
    left = poly_trim(left, prime)
    right = poly_trim(right, prime)
    while not poly_zero(right, prime):
        left, right = right, poly_mod(left, right, prime)
    require(not poly_zero(left, prime), "undefined gcd(0,0)")
    return poly_scale(left, pow(left[-1], -1, prime), prime)


def poly_eval(poly: Poly, value: int, prime: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % prime
    return result


def compose_x_power(poly: Poly, power: int, prime: int) -> Poly:
    result = [0] * ((len(poly) - 1) * power + 1)
    for index, coefficient in enumerate(poly):
        result[index * power] = coefficient % prime
    return poly_trim(result, prime)


def verify_divided_difference_fixture() -> None:
    prime = 101
    roots = (1, 2, 3)
    a0 = [1]
    for root in roots:
        a0 = poly_mul(a0, [-root, 1], prime)
    require(a0 == [95, 11, 95, 1], "toy cubic coefficients drift")

    block = 2
    t_poly = [0, 0, 1]
    g = compose_x_power(a0, block, prime)
    h = [0, 1]
    c2 = a0[2]
    c1 = a0[1]
    q_coefficients = (
        poly_add(
            poly_add(poly_mul(t_poly, t_poly, prime), poly_scale(t_poly, c2, prime), prime),
            [c1],
            prime,
        ),
        poly_add(t_poly, [c2], prime),
        [1],
    )
    remainder_coefficients = tuple(
        poly_scale(poly_mod(poly_mul(h, coefficient, prime), g, prime), -1, prime)
        for coefficient in q_coefficients
    )

    require(remainder_coefficients[2] == poly_scale(h, -1, prime),
            "toy Y^2 coefficient lost the minus sign")
    for q_coefficient, r_coefficient in zip(q_coefficients, remainder_coefficients):
        congruence = poly_add(r_coefficient, poly_mul(h, q_coefficient, prime), prime)
        require(poly_zero(poly_mod(congruence, g, prime), prime),
                "toy remainder congruence failed")
        require(poly_degree(r_coefficient, prime) < poly_degree(g, prime),
                "toy remainder is not canonical")
    require(poly_gcd(h, g, prime) == [1], "toy h and g must be coprime")


def verify_irreducible_degree_obstruction() -> None:
    require(3 * B == 98_304, "cubic composition degree drift")
    require(A_DEG % 3 == 2, "deployed generator unexpectedly has degree divisible by 3")
    sample_factor_degrees = tuple(range(3, 3 * B + 1, 3))
    require(all(degree % 3 == 0 for degree in sample_factor_degrees),
            "irreducible cubic tower-law degree class failed")
    require(not any(degree == A_DEG for degree in sample_factor_degrees),
            "irreducible cubic obstruction failed")


def zero_root_layers(multiplicity: int, valuation: int) -> tuple[list[int], list[int]]:
    degrees = [
        min(B, max(valuation - layer * B, 0))
        for layer in range(multiplicity)
    ]
    deficits = [B - degree for degree in degrees]
    return degrees, deficits


def verify_divisor_deficit_layers() -> None:
    require(CUBIC_DEFICIT == 3 * B - A_DEG, "total divisor deficit failed")
    require(FIRST_LAYER_GAP == B - W_DEG, "first-layer lower bound failed")
    for multiplicity in (1, 2, 3):
        for valuation in range(multiplicity * B + 1):
            degrees, deficits = zero_root_layers(multiplicity, valuation)
            require(all(0 <= degree <= B for degree in degrees),
                    "zero-root layer degree escaped [0,B]")
            require(deficits == sorted(deficits),
                    "zero-root deficits are not nested")
            require(sum(degrees) == valuation,
                    "zero-root layers do not recover the valuation")
            require(sum(deficits) == multiplicity * B - valuation,
                    "zero-root deficit identity failed")

    compatible_patterns = (
        (10_000, 10_000, 10_832),
        (5_000, 10_000, 15_832),
        (1_000, 10_000, 19_832),
    )
    for deficits in compatible_patterns:
        require(sum(deficits) == CUBIC_DEFICIT, "sample layer budget drift")
        require(all(0 <= deficit <= B for deficit in deficits),
                "sample layer deficit escaped [0,B]")
    require(W_DEG <= B, "first-layer deficit bound exceeds one block")


def verify_conductor_cases() -> int:
    powers = tuple(1 << exponent for exponent in range(16))
    require(powers[-1] == B, "power-of-two conductor list drift")
    compatible_with_total = tuple(
        conductor for conductor in powers if CUBIC_DEFICIT % conductor == 0
    )
    require(max(compatible_with_total) == 16,
            "repeated-root conductor bound failed")

    s2_min = (CUBIC_DEFICIT - W_DEG + 1) // 2
    s2_max = CUBIC_DEFICIT // 2
    require((s2_min, s2_max) == (968, 15_416),
            "linear-quadratic deficit range drift")

    checked = 0
    for s2 in range(s2_min, s2_max + 1):
        s0 = CUBIC_DEFICIT - 2 * s2
        require(0 <= s0 <= W_DEG, "linear deficit escaped its source bound")
        for delta0 in powers:
            if s0 % delta0:
                continue
            for delta2 in powers:
                if s2 % delta2:
                    continue
                checked += 1
                require(delta0 <= 16 or delta2 <= 8,
                        "quadratic conductor alternative failed")

    require(checked == 110_196, "compatible conductor case count drift")
    require(15_416 == 8 * 1_927, "whole-linear quadratic endpoint drift")
    return checked


def lagrange_interpolate_values(
    roots: tuple[int, ...], values: tuple[Poly, ...], prime: int
) -> list[Poly]:
    coefficients: list[Poly] = [[0] for _ in roots]
    for index, root in enumerate(roots):
        basis: Poly = [1]
        for other_index, other_root in enumerate(roots):
            if other_index != index:
                basis = poly_mul(basis, [-other_root, 1], prime)
        denominator = poly_eval(basis, root, prime)
        scale = pow(denominator, -1, prime)
        for y_degree, scalar in enumerate(basis):
            term = poly_scale(values[index], scalar * scale, prime)
            coefficients[y_degree] = poly_add(coefficients[y_degree], term, prime)
    return coefficients


def evaluate_poly_y(coefficients: list[Poly], value: int, prime: int) -> Poly:
    result: Poly = [0]
    power = 1
    for coefficient in coefficients:
        result = poly_add(result, poly_scale(coefficient, power, prime), prime)
        power = power * value % prime
    return result


def verify_squarefree_resultant() -> None:
    require(RESULTANT_M_BOUND == 55_859, "resultant multiplier degree drift")
    require(RESULTANT_DEG_BOUND == 190_803, "resultant total degree drift")
    require(RESULTANT_DEG_BOUND == 3 * R_DEG, "resultant 3d identity failed")

    layer_inclusion_counts = [0, 0, 0]
    for omitted in range(3):
        for layer in range(3):
            if layer != omitted:
                layer_inclusion_counts[layer] += 1
    require(layer_inclusion_counts == [2, 2, 2],
            "squarefree resultant does not contribute g^2")

    prime = 101
    roots = (1, 2, 3)
    layers = ([97, 1], [96, 1], [95, 1])
    g: Poly = [1]
    for layer in layers:
        g = poly_mul(g, layer, prime)
    multipliers = ([7, 1], [2], [1, 0, 1])

    values: list[Poly] = []
    for layer, multiplier in zip(layers, multipliers):
        complement, remainder = poly_divmod(g, layer, prime)
        require(poly_zero(remainder, prime), "toy first layer does not divide g")
        values.append(poly_mul(complement, multiplier, prime))

    curve = lagrange_interpolate_values(roots, tuple(values), prime)
    require(len(curve) <= 3, "toy specialization curve has Y-degree above two")
    for root, value in zip(roots, values):
        require(evaluate_poly_y(curve, root, prime) == value,
                "toy specialization interpolation failed")

    resultant: Poly = [1]
    for value in values:
        resultant = poly_mul(resultant, value, prime)
    multiplier_product: Poly = [1]
    for multiplier in multipliers:
        multiplier_product = poly_mul(multiplier_product, multiplier, prime)
    expected = poly_mul(poly_mul(g, g, prime), multiplier_product, prime)
    require(resultant == expected, "toy squarefree resultant factorization failed")


def set_path(path: tuple[str, ...], value: Any) -> Callable[[dict[str, Any]], None]:
    def mutate(contract: dict[str, Any]) -> None:
        target: Any = contract
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
    return mutate


def compare_expected(rendered: str, expected: str) -> None:
    require(rendered == expected, "rendered transcript differs from expected output")


def semantic_tamper_selftests() -> int:
    cases: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
        ("base-head", set_path(("source", "base_head"), "0" * 40)),
        ("pr863-head", set_path(("source", "pr863_head"), "f" * 40)),
        ("core-size", set_path(("source", "fixed_core_size"), 26)),
        ("fixed-generator", set_path(("source", "fixed_generator"), False)),
        ("fixed-ray", set_path(("source", "fixed_syndrome_ray"), False)),
        ("fixed-cell", set_path(("source", "fixed_source_cell"), False)),
        ("label-count", set_path(("source", "actual_labels"), 6)),
        ("cubic-branch", set_path(("source", "e"), 4)),
        ("kappa", set_path(("source", "kappa_B_at_most"), 2)),
        ("source-filters", set_path(("source", "all_source_filters_retained"), False)),
        ("cubic-reducibility", set_path(("claims", "primitive_cubic_reducible"), False)),
        ("remainder-sign", set_path(
            ("claims", "remainder"), "R=+rem_g(h*((a0(T)-a0(Y))/(T-Y)))")),
        ("deficit", set_path(("claims", "cubic_deficit"), 30_831)),
        ("first-deficit", set_path(("claims", "first_layer_deficit_at_most"), 28_898)),
        ("first-degree", set_path(("claims", "first_layer_degree_at_least"), 3_870)),
        ("conductor", set_path(("claims", "some_conductor_at_most"), 32)),
        ("quadratic-conductor", set_path(("claims", "quadratic_alternative_at_most"), 16)),
        ("resultant-exponent", set_path(("claims", "squarefree_resultant_g_exponent"), 1)),
        ("resultant-M-degree", set_path(("claims", "resultant_M_degree_at_most"), 55_860)),
        ("resultant-total-degree", set_path(("claims", "resultant_total_degree_at_most"), 190_804)),
        ("finite-payment", set_path(("payments", "finite"), 1)),
        ("asymptotic-payment", set_path(("payments", "asymptotic"), 1)),
        ("parent-payment", set_path(("payments", "parent"), 1)),
        ("official-score", set_path(("payments", "official_score"), "1/2")),
        ("seven-label-closure", set_path(("nonclaims", "seven_label_closure"), True)),
        ("reverse-source", set_path(("nonclaims", "reverse_source_construction"), True)),
        ("aggregation", set_path(("nonclaims", "cross_cell_aggregation"), True)),
        ("rank16-closure", set_path(("nonclaims", "rank16_closure"), True)),
    )

    for name, mutate in cases:
        candidate = copy.deepcopy(CONTRACT)
        mutate(candidate)
        try:
            validate_contract(candidate)
        except ContractError:
            pass
        else:
            raise CheckError(f"semantic tamper escaped rejection: {name}")

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    manifest["dependencies"][2]["head"] = "0" * 40
    try:
        validate_manifest(manifest)
    except ContractError:
        pass
    else:
        raise CheckError("manifest tamper escaped rejection")

    first_source = next(iter(INTEGRATED_SOURCE_PINS))
    try:
        verify_file_pin(ROOT / first_source, "0" * 64, "tampered source pin")
    except CheckError:
        pass
    else:
        raise CheckError("source-pin tamper escaped rejection")

    try:
        verify_file_pin(NOTE_PATH, "0" * 64, "tampered theorem statement")
    except CheckError:
        pass
    else:
        raise CheckError("statement-pin tamper escaped rejection")

    try:
        compare_expected("expected\n", "tampered\n")
    except CheckError:
        pass
    else:
        raise CheckError("expected-output tamper escaped rejection")

    return len(cases) + 4


def render_transcript(conductor_cases: int) -> str:
    lines = (
        "R28_ROLE03_CUBIC_DIVISOR_CONDUCTOR: PASS",
        "field=p=2130706433 B=32768 a=67472 D=96369 d=63601 w=28897",
        "cubic_complement=30832 v2=4 gap=3871",
        "irreducible_cubic=EXCLUDED deg_g_mod_3=2",
        "remainder=quadratic_divided_difference_coefficients",
        "specialization=first_layer_deficit<=28897 first_layer_degree>=3871",
        "squarefree_resultant=g^2*M deg_M<=55859 total_deg<=190803=3d",
        "linear_times_quadratic=S2_range_968_15416",
        "conductor=some_block<=16 quadratic_alternative<=8",
        f"linear_quadratic_conductor_cases_checked={conductor_cases}",
        "finite_payment=0 asymptotic_payment=0 score=0/2",
        "tamper_selftest=PASS",
    )
    return "\n".join(lines) + "\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tamper-selftest",
        action="store_true",
        help="run only the fail-closed statement/source/semantic mutation suite",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.tamper_selftest:
        verify_statement_and_sources()
        count = semantic_tamper_selftests()
        print(f"SEMANTIC_TAMPER_SELFTEST: PASS count={count}")
        return 0

    validate_contract(CONTRACT)
    verify_statement_and_sources()
    verify_constants()
    verify_divided_difference_symbolically()
    verify_divided_difference_fixture()
    verify_irreducible_degree_obstruction()
    verify_divisor_deficit_layers()
    conductor_cases = verify_conductor_cases()
    verify_squarefree_resultant()
    semantic_tamper_selftests()

    rendered = render_transcript(conductor_cases)
    expected = EXPECTED_PATH.read_text(encoding="utf-8")
    compare_expected(rendered, expected)
    sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (CheckError, json.JSONDecodeError) as exc:
        print(f"REPLAY_FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
