#!/usr/bin/env python3
"""Exact checks for the growing-characteristic R=2 cycle bound."""

from __future__ import annotations

import argparse
import copy
import json
import math
from fractions import Fraction
from pathlib import Path


CERTIFICATE = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "certificates"
    / "r2-growing-characteristic-cycle-flatness"
    / "r2_growing_characteristic_cycle_flatness.json"
)


def rising_binom(parameter: Fraction, order: int) -> Fraction:
    """Return binom(parameter + order - 1, order) exactly."""
    assert parameter > 0
    assert order >= 0
    value = Fraction(1, 1)
    for index in range(order):
        value *= parameter + index
        value /= index + 1
    return value


def ceil_fraction(value: Fraction) -> int:
    return (value.numerator + value.denominator - 1) // value.denominator


def cycle_coefficient(n: int, p: int, r: int, lam: Fraction) -> Fraction:
    """Coefficient in (1-v)^(-lam)(1-v^p)^(-(n-lam)/p)."""
    beta = (Fraction(n, 1) - lam) / p
    total = Fraction(0, 1)
    for ell in range(r // p + 1):
        total += rising_binom(beta, ell) * rising_binom(
            lam, r - p * ell
        )
    return total


def hockey_factor(beta: Fraction, level: int) -> Fraction:
    """Return binom(beta+level, level) as a rising binomial."""
    return rising_binom(beta + 1, level)


def load_certificate() -> dict:
    with CERTIFICATE.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_certificate(data: dict) -> int:
    assert data["schema"] == "rs-mca.r2-growing-characteristic-flatness.v1"
    assert data["status"] == "PROVED"
    assert data["hard_input"] == 2
    assert data["source"]["commit"] == (
        "6588d8d6c393df81642dafafc82c70f565d009cf"
    )
    assert data["source"]["integrated_by"] == (
        "7d66bfa9b2f3c3cf557f1a4e898fe6cbc26a4ce3"
    )
    assert data["parameters"]["weil_constant"] == "C_W=3*C_0"
    assert data["finite_bound"]["cycle_penalty"] == (
        "binom((N-Lambda)/p+floor(r/p),floor(r/p))"
    )
    assert data["asymptotic_gate"]["characteristic_penalty"] == (
        "3*log(2)/(2*p)"
    )
    assert data["strict_family"]["field"] == "F_(p^4)"
    assert data["strict_family"]["subgroup_order"] == "d*(p^2+1)"
    assert data["strict_family"]["requirement"] == "d>2*C_W and p=1 mod d"
    assert "circle twin-cosets" in data["nonclaims"]
    assert "deployed finite leaves" in data["nonclaims"]
    return 14


def check_hockey_grid() -> int:
    checks = 0
    for p in (3, 5, 7, 11, 13):
        for n in range(4, min(6 * p + 8, 72)):
            candidates = {
                Fraction(1, 1),
                Fraction(n, 9),
                Fraction(n, 3),
                Fraction(n - 1, 2),
            }
            for lam in sorted(candidates):
                if not (1 <= lam < n):
                    continue
                beta = (Fraction(n, 1) - lam) / p
                for r in range(n // 2 + 1):
                    level = r // p

                    lhs = sum(
                        (rising_binom(beta, ell) for ell in range(level + 1)),
                        Fraction(0, 1),
                    )
                    rhs = hockey_factor(beta, level)
                    assert lhs == rhs, ("hockey", n, p, r, lam, lhs, rhs)
                    checks += 1

                    exact = cycle_coefficient(n, p, r, lam)
                    base = rising_binom(lam, r)
                    upper = base * rhs
                    assert exact <= upper, (
                        "coefficient",
                        n,
                        p,
                        r,
                        lam,
                        exact,
                        upper,
                    )
                    checks += 1

                    binary = Fraction(2 ** (ceil_fraction(beta) + level), 1)
                    assert rhs <= binary, (
                        "binary",
                        n,
                        p,
                        r,
                        lam,
                        rhs,
                        binary,
                    )
                    checks += 1

                    exponent = ceil_fraction(beta) + level
                    exponent_upper = 1 + Fraction(3 * n, 2 * p)
                    assert exponent <= exponent_upper, (
                        "exponent",
                        n,
                        p,
                        r,
                        lam,
                        exponent,
                        exponent_upper,
                    )
                    checks += 1

                    for q in (n + 1, (n + 1) ** 2):
                        multiplier = q * q - 1
                        exact_error = Fraction(multiplier, math.comb(n, r)) * exact
                        certified_error = (
                            Fraction(multiplier, math.comb(n, r)) * upper
                        )
                        assert exact_error <= certified_error
                        checks += 1
    return checks


def entropy(x: float) -> float:
    if x == 0.0 or x == 1.0:
        return 0.0
    return -x * math.log(x) - (1.0 - x) * math.log(1.0 - x)


def entropy_gap(x: float, lam: float) -> float:
    return entropy(x) - (x + lam) * entropy(x / (x + lam))


def check_entropy(data: dict) -> int:
    checks = 0
    for sample in data["entropy_samples"]:
        alpha = sample["alpha"]
        lam = sample["lambda"]
        assert 0.0 < alpha < 0.5
        assert 0.0 < lam < 0.5

        endpoint_minimum = min(
            entropy_gap(alpha, lam), entropy_gap(0.5, lam)
        )
        assert endpoint_minimum > 0.0
        checks += 1

        sampled = []
        for index in range(1001):
            x = alpha + (0.5 - alpha) * index / 1000.0
            value = entropy_gap(x, lam)
            assert value > 0.0
            sampled.append(value)
            checks += 1

        # The gap is concave, so its minimum on the interval is at an endpoint.
        assert min(sampled) + 1e-12 >= endpoint_minimum
        checks += 1
    return checks


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def check_strict_family(data: dict) -> int:
    checks = 0
    previous_by_d: dict[int, Fraction] = {}
    for row in data["strict_family"]["arithmetic_rows"]:
        d = row["d"]
        p = row["p"]
        assert is_prime(p)
        assert p % d == 1
        checks += 2

        q = p**4
        n = d * (p * p + 1)
        assert (q - 1) % n == 0
        assert n > p * p - 1
        checks += 2

        n_over_p = Fraction(n, p)
        if d in previous_by_d:
            assert n_over_p > previous_by_d[d]
            checks += 1
        previous_by_d[d] = n_over_p

        shallow_ratio = Fraction(2 * p * p, n)
        assert shallow_ratio > 0
        assert shallow_ratio < Fraction(2, d)
        checks += 2
    return checks


def run_check(data: dict) -> int:
    checks = 0
    checks += validate_certificate(data)
    checks += check_hockey_grid()
    checks += check_entropy(data)
    checks += check_strict_family(data)
    print("object: R=2 growing-characteristic cycle flatness")
    print(f"exact checks: {checks} PASS")
    print("theorem: quantitative cycle gate and p->infinity corollary")
    print("status: PROVED conditional on integrated weighted-Weil input")
    print(f"RESULT: PASS ({checks}/{checks})")
    return checks


def run_tamper_selftest(data: dict) -> None:
    tampered = copy.deepcopy(data)
    tampered["hard_input"] = 3
    try:
        validate_certificate(tampered)
    except AssertionError:
        print("tamper self-test: altered hard-input binding detected PASS")
    else:
        raise AssertionError("tamper self-test failed to detect altered binding")
    print("RESULT: PASS (tamper detected)")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()

    data = load_certificate()
    if args.check or not args.tamper_selftest:
        run_check(data)
    if args.tamper_selftest:
        run_tamper_selftest(data)


if __name__ == "__main__":
    main()
