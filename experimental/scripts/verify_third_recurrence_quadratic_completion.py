#!/usr/bin/env python3
"""Verify the depth-three quadratic-completion sharpness family."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = (
    ROOT
    / "experimental/data/certificates/third-recurrence-quadratic-completion"
    / "third_recurrence_quadratic_completion.json"
)
BASE_COMMIT = "8b3daf4388cd387dcfece228a95394bd1ce41212"
CLAIM_ID = "third-recurrence-quadratic-completion-v1"


class VerificationError(RuntimeError):
    """An always-active exact check failed."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def payload_digest(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def elementary(support: tuple[int, ...], degree: int, p: int) -> int:
    return sum(
        product_mod(term, p)
        for term in itertools.combinations(support, degree)
    ) % p


def product_mod(values: tuple[int, ...], p: int) -> int:
    result = 1
    for value in values:
        result = result * value % p
    return result


def barycentric_amplitudes(
    support: tuple[int, ...], p: int
) -> tuple[int, ...]:
    amplitudes = []
    for x in support:
        denominator = 1
        for y in support:
            if x != y:
                denominator = denominator * (x - y) % p
        require(denominator != 0, "barycentric denominator vanished")
        amplitudes.append(pow(denominator, -1, p))
    return tuple(amplitudes)


def moment_vector(
    support: tuple[int, ...],
    amplitudes: tuple[int, ...],
    redundancy: int,
    p: int,
) -> tuple[int, ...]:
    return tuple(
        sum(
            amplitude * pow(x, degree, p)
            for x, amplitude in zip(support, amplitudes, strict=True)
        )
        % p
        for degree in range(redundancy)
    )


def locator_coefficients(support: tuple[int, ...], p: int) -> tuple[int, ...]:
    coefficients = [1]
    for root in support:
        updated = [0] * (len(coefficients) + 1)
        for degree, coefficient in enumerate(coefficients):
            updated[degree] = (updated[degree] - root * coefficient) % p
            updated[degree + 1] = (
                updated[degree + 1] + coefficient
            ) % p
        coefficients = updated
    return tuple(coefficients)


def recurrence_value(
    moments: tuple[int, ...],
    locator: tuple[int, ...],
    shift: int,
    p: int,
) -> int:
    return sum(
        coefficient * moments[shift + degree]
        for degree, coefficient in enumerate(locator)
    ) % p


def quadratic_character(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    residue = pow(value, (p - 1) // 2, p)
    require(residue in (1, p - 1), "Euler criterion failed")
    return 1 if residue == 1 else -1


def audit_character_sum(p: int, free_size: int) -> dict[str, int]:
    prefix_checks = 0
    degenerate_prefixes = 0
    leading = -3 % p
    leading_character = quadratic_character(leading, p)
    for prefix in itertools.product(range(p), repeat=free_size - 1):
        prefix_sum = sum(prefix) % p
        prefix_e2 = elementary(tuple(prefix), 2, p)
        linear = -2 * prefix_sum % p
        constant = (4 * prefix_e2 - 3 * prefix_sum * prefix_sum) % p
        discriminant = (
            linear * linear - 4 * leading * constant
        ) % p
        require(
            discriminant
            == 16 * (3 * prefix_e2 - 2 * prefix_sum * prefix_sum) % p,
            "one-variable discriminant identity changed",
        )
        actual_sum = sum(
            quadratic_character(
                leading * x * x + linear * x + constant, p
            )
            for x in range(p)
        )
        if discriminant == 0:
            degenerate_prefixes += 1
            expected_sum = (p - 1) * leading_character
        else:
            expected_sum = -leading_character
        require(actual_sum == expected_sum, "quadratic character sum changed")
        prefix_checks += 1
    require(
        degenerate_prefixes <= 2 * p ** (free_size - 2),
        "Schwartz-Zippel degeneracy budget changed",
    )
    return {
        "character_prefix_checks": prefix_checks,
        "degenerate_prefixes": degenerate_prefixes,
    }


def audit_case(p: int, t: int) -> dict[str, Any]:
    require(is_prime(p) and p > 3, "fixture field is inadmissible")
    require(4 <= t <= p, "fixture support size is inadmissible")
    redundancy = t + 3
    deficiency = t - 3
    free_size = t - 2
    domain = tuple(range(p))
    selected_supports: set[tuple[int, ...]] = set()
    slope_histogram: dict[int, int] = defaultdict(int)
    top_support_checks = 0
    recurrence_checks = 0

    for support in itertools.combinations(domain, t):
        e1 = elementary(support, 1, p)
        e2 = elementary(support, 2, p)
        e3 = elementary(support, 3, p)
        amplitudes = barycentric_amplitudes(support, p)
        moments = moment_vector(support, amplitudes, redundancy, p)
        require(moments[: t - 1] == (0,) * (t - 1), "early moments changed")
        require(moments[t - 1] == 1, "normalizing moment changed")
        require(moments[t] == e1, "first tail moment changed")
        require(moments[t + 1] == (e1 * e1 - e2) % p, "h2 changed")
        require(
            moments[t + 2]
            == (e1 * e1 * e1 - 2 * e1 * e2 + e3) % p,
            "h3 changed",
        )
        top_support_checks += 1
        if e1 != 0 or e2 != 0:
            continue

        gamma = e3
        target = [0] * redundancy
        target[t - 1] = 1
        target[t + 2] = gamma
        require(moments == tuple(target), "selected support missed the line")
        locator = locator_coefficients(support, p)
        for shift in range(3):
            require(
                recurrence_value(tuple(target), locator, shift, p) == 0,
                "support recurrence failed",
            )
            recurrence_checks += 1
        shifted_target = target.copy()
        shifted_target[t + 2] = (gamma + 1) % p
        require(
            recurrence_value(tuple(shifted_target), locator, 2, p) == 1,
            "third recurrence became common along the line",
        )
        recurrence_checks += 1
        selected_supports.add(support)
        slope_histogram[gamma] += 1

    lower_support_checks = 0
    for size in range(1, t):
        for support in itertools.combinations(domain, size):
            determinant = 1
            for left, right in itertools.combinations(support, 2):
                determinant = determinant * (right - left) % p
            require(determinant != 0, "lower-support Vandermonde singular")
            lower_support_checks += 1

    completion_multiplicity: Counter[tuple[int, ...]] = Counter()
    split_quadratics = 0
    collision_completions = 0
    zero_discriminants = 0
    character_sum = 0
    for free_support in itertools.combinations(domain, free_size):
        support_sum = elementary(free_support, 1, p)
        support_e2 = elementary(free_support, 2, p)
        discriminant = (
            4 * support_e2 - 3 * support_sum * support_sum
        ) % p
        character = quadratic_character(discriminant, p)
        character_sum += character
        roots = tuple(
            x
            for x in domain
            if (
                x * x
                + support_sum * x
                + support_sum * support_sum
                - support_e2
            )
            % p
            == 0
        )
        if character == 0:
            zero_discriminants += 1
            require(len(roots) == 1, "double-root quadratic changed")
            continue
        require(
            len(roots) == (2 if character == 1 else 0),
            "quadratic splitting criterion changed",
        )
        if character == -1:
            continue
        split_quadratics += 1
        if not set(roots).isdisjoint(free_support):
            collision_completions += 1
            continue
        completed = tuple(sorted((*free_support, *roots)))
        require(len(completed) == t, "completion lost distinctness")
        require(elementary(completed, 1, p) == 0, "completion e1 changed")
        require(elementary(completed, 2, p) == 0, "completion e2 changed")
        completion_multiplicity[completed] += 1

    partition_multiplicity = comb(t, 2)
    require(
        set(completion_multiplicity) == selected_supports,
        "quadratic completion missed a selected support",
    )
    require(
        set(completion_multiplicity.values()) <= {partition_multiplicity},
        "quadratic completion multiplicity changed",
    )
    require(
        sum(completion_multiplicity.values())
        == len(selected_supports) * partition_multiplicity,
        "partition double count changed",
    )

    character_audit = audit_character_sum(p, free_size)
    upper_bound = comb(p, deficiency + 1)
    exact_ratio = Fraction(len(selected_supports), upper_bound)
    return {
        "p": p,
        "n": p,
        "t": t,
        "redundancy": redundancy,
        "deficiency": deficiency,
        "free_size": free_size,
        "pairs": len(selected_supports),
        "slopes": len(slope_histogram),
        "same_slope_excess": len(selected_supports) - len(slope_histogram),
        "maximum_pairs_per_slope": max(slope_histogram.values(), default=0),
        "complete_binomial_upper": upper_bound,
        "exact_ratio_to_upper": (
            f"{exact_ratio.numerator}/{exact_ratio.denominator}"
        ),
        "split_quadratics": split_quadratics,
        "collision_completions": collision_completions,
        "zero_discriminants": zero_discriminants,
        "subset_character_sum": character_sum,
        "partition_multiplicity": partition_multiplicity,
        "top_support_checks": top_support_checks,
        "lower_support_checks": lower_support_checks,
        "recurrence_checks": recurrence_checks,
        **character_audit,
    }


def build_payload() -> dict[str, Any]:
    parameters = [
        (5, 4),
        (7, 4),
        (7, 5),
        (11, 4),
        (11, 5),
        (11, 6),
        (13, 4),
        (13, 5),
        (13, 6),
        (13, 7),
        (17, 4),
        (17, 5),
        (17, 6),
    ]
    cases = [audit_case(p, t) for p, t in parameters]
    return {
        "schema_version": 1,
        "claim_id": CLAIM_ID,
        "base_commit": BASE_COMMIT,
        "status": "PROVED_WITH_EXACT_FINITE_REPLAY",
        "theorem": {
            "range": "D=F_q, R=t+3, d=t-3>=1, char(F_q) not in {2,3}",
            "line": "y_z=e_(t-1)+z e_(t+2)",
            "complete_pair_set": "e1(S)=e2(S)=0 and z=e3(S)",
            "asymptotic_pair_count": "|P|=q^(d+1)/t!+O_d(q^d)",
            "ratio_to_top_bound": "1/(t(t-1))+O_d(1/q)",
            "quadratic_completion": "X^2+s1(A)X+s1(A)^2-e2(A)",
        },
        "cases": cases,
        "totals": {
            "cases": len(cases),
            "pairs": sum(row["pairs"] for row in cases),
            "slopes": sum(row["slopes"] for row in cases),
            "top_support_checks": sum(
                row["top_support_checks"] for row in cases
            ),
            "lower_support_checks": sum(
                row["lower_support_checks"] for row in cases
            ),
            "recurrence_checks": sum(
                row["recurrence_checks"] for row in cases
            ),
            "character_prefix_checks": sum(
                row["character_prefix_checks"] for row in cases
            ),
        },
        "nonclaims": [
            "no_exact_finite_formula_for_the_pair_count",
            "no_distinct_slope_lower_bound_of_order_q_to_d_plus_1",
            "no_arbitrary_recurrence_depth_theorem",
            "no_target_or_deployed_row_movement",
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
        key: value
        for key, value in actual.items()
        if key != "payload_sha256"
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
    bad["theorem"]["asymptotic_pair_count"] = "|P|=q"
    tampers.append(bad)
    bad = copy.deepcopy(expected)
    bad["cases"][4]["pairs"] += 1
    tampers.append(bad)
    bad = copy.deepcopy(expected)
    bad["cases"][7]["partition_multiplicity"] += 1
    tampers.append(bad)
    bad = copy.deepcopy(expected)
    bad["base_commit"] = "0" * 40
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
        "THIRD_RECURRENCE_QUADRATIC_COMPLETION_PASS "
        f"cases={totals['cases']} "
        f"pairs={totals['pairs']} "
        f"slopes={totals['slopes']} "
        f"top={totals['top_support_checks']} "
        f"lower={totals['lower_support_checks']} "
        f"recurrences={totals['recurrence_checks']} "
        f"characters={totals['character_prefix_checks']}"
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
            "THIRD_RECURRENCE_QUADRATIC_COMPLETION_TAMPER_PASS "
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
