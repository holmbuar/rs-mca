#!/usr/bin/env python3
"""Verify the exact second-recurrence zero-sum LineRay family."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
from collections import defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = (
    ROOT
    / "experimental/data/certificates/second-recurrence-zero-sum-family"
    / "second_recurrence_zero_sum_family.json"
)
BASE_COMMIT = "6b30a5355cfe1bf6d748096af31dc22b8fc03911"
CLAIM_ID = "second-recurrence-zero-sum-family-v1"


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


def barycentric_amplitudes(
    support: tuple[int, ...], p: int
) -> tuple[int, ...]:
    amplitudes = []
    for x in support:
        denominator = 1
        for y in support:
            if y != x:
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


def elementary_two(support: tuple[int, ...], p: int) -> int:
    return sum(x * y for x, y in itertools.combinations(support, 2)) % p


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


def audit_case(p: int, t: int) -> dict[str, Any]:
    require(is_prime(p), "fixture modulus is not prime")
    require(3 <= t <= p - 2, "fixture parameters are inadmissible")
    require(t % p != 0, "translation does not move every sum fiber")
    redundancy = t + 2
    deficiency = t - 2
    domain = tuple(range(p))
    expected_pairs = comb(p, t) // p
    sum_histogram: dict[int, int] = defaultdict(int)
    slope_histogram: dict[int, int] = defaultdict(int)
    selected_pairs = 0
    top_support_checks = 0
    recurrence_checks = 0

    for support in itertools.combinations(domain, t):
        support_sum = sum(support) % p
        sum_histogram[support_sum] += 1
        amplitudes = barycentric_amplitudes(support, p)
        moments = moment_vector(support, amplitudes, redundancy, p)
        require(
            moments[: t - 1] == (0,) * (t - 1),
            "early Lagrange moments changed",
        )
        require(moments[t - 1] == 1, "normalizing moment changed")
        require(moments[t] == support_sum, "first tail moment changed")
        top_support_checks += 1
        if support_sum != 0:
            continue

        gamma = (-elementary_two(support, p)) % p
        target = [0] * redundancy
        target[t - 1] = 1
        target[t + 1] = gamma
        require(moments == tuple(target), "zero-sum support missed the line")

        locator = locator_coefficients(support, p)
        require(
            recurrence_value(tuple(target), locator, 0, p) == 0,
            "first support recurrence failed",
        )
        require(
            recurrence_value(tuple(target), locator, 1, p) == 0,
            "second support recurrence failed",
        )
        shifted_target = target.copy()
        shifted_target[t + 1] = (gamma + 1) % p
        require(
            recurrence_value(tuple(shifted_target), locator, 1, p) == 1,
            "support recurrence became common along the line",
        )
        recurrence_checks += 3
        selected_pairs += 1
        slope_histogram[gamma] += 1

    require(
        set(sum_histogram) == set(domain),
        "not every support-sum fiber was attained",
    )
    require(
        set(sum_histogram.values()) == {expected_pairs},
        "translation failed to equalize support-sum fibers",
    )
    require(selected_pairs == expected_pairs, "zero-sum pair count changed")

    lower_support_checks = 0
    for size in range(1, t):
        for support in itertools.combinations(domain, size):
            determinant = 1
            for left, right in itertools.combinations(support, 2):
                determinant = determinant * (right - left) % p
            require(determinant != 0, "lower-support Vandermonde singular")
            lower_support_checks += 1

    upper_bound = comb(p, deficiency + 1)
    exact_ratio = Fraction(selected_pairs, upper_bound)
    formula_ratio = Fraction(p - t + 1, p * t)
    require(exact_ratio == formula_ratio, "upper-bound ratio changed")

    return {
        "p": p,
        "n": p,
        "t": t,
        "redundancy": redundancy,
        "deficiency": deficiency,
        "pairs": selected_pairs,
        "slopes": len(slope_histogram),
        "same_slope_excess": selected_pairs - len(slope_histogram),
        "maximum_pairs_per_slope": max(slope_histogram.values()),
        "complete_binomial_upper": upper_bound,
        "exact_ratio_to_upper": (
            f"{exact_ratio.numerator}/{exact_ratio.denominator}"
        ),
        "top_support_checks": top_support_checks,
        "lower_support_checks": lower_support_checks,
        "recurrence_checks": recurrence_checks,
        "all_sum_fibers_equal": True,
        "complete_pair_set_exact": True,
    }


def build_payload() -> dict[str, Any]:
    cases = [
        audit_case(5, 3),
        audit_case(7, 3),
        audit_case(7, 4),
        audit_case(7, 5),
        audit_case(11, 3),
        audit_case(11, 4),
        audit_case(11, 5),
        audit_case(11, 6),
        audit_case(13, 7),
    ]
    return {
        "schema_version": 1,
        "claim_id": CLAIM_ID,
        "base_commit": BASE_COMMIT,
        "status": "PROVED_WITH_EXACT_FINITE_REPLAY",
        "theorem": {
            "range": "D=F_q, R=t+2, d=t-2>=1, char(F_q) does not divide t",
            "line": "y_z=e_(t-1)+z e_(t+1)",
            "complete_pair_count": "|P|=binom(q,t)/q",
            "top_bound_ratio": "(q-t+1)/(qt) -> 1/t=1/(d+2)",
            "owner": "zero-sum t-subsets with barycentric amplitudes",
        },
        "cases": cases,
        "totals": {
            "cases": len(cases),
            "pairs": sum(row["pairs"] for row in cases),
            "slopes": sum(row["slopes"] for row in cases),
            "same_slope_excess": sum(
                row["same_slope_excess"] for row in cases
            ),
            "top_support_checks": sum(
                row["top_support_checks"] for row in cases
            ),
            "lower_support_checks": sum(
                row["lower_support_checks"] for row in cases
            ),
            "recurrence_checks": sum(
                row["recurrence_checks"] for row in cases
            ),
        },
        "nonclaims": [
            "no_distinct_slope_lower_bound_of_order_q_to_d_plus_1",
            "no_sharp_constant_for_recurrence_depth_at_least_two",
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
    bad["theorem"]["complete_pair_count"] = "|P|=q"
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["cases"][2]["pairs"] += 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["cases"][5]["all_sum_fibers_equal"] = False
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
        "SECOND_RECURRENCE_ZERO_SUM_FAMILY_PASS "
        f"cases={totals['cases']} "
        f"pairs={totals['pairs']} "
        f"slopes={totals['slopes']} "
        f"same_slope={totals['same_slope_excess']} "
        f"top={totals['top_support_checks']} "
        f"lower={totals['lower_support_checks']} "
        f"recurrences={totals['recurrence_checks']}"
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
            "SECOND_RECURRENCE_ZERO_SUM_FAMILY_TAMPER_PASS "
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
