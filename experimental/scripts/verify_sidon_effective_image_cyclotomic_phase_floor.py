#!/usr/bin/env python3
"""Verify the trace-linear cyclotomic phase-floor certificate.

Stdlib only.  The p=3, r=2 row is exhaustively enumerated over all 3^10
trace-linear phase words and all C(12,6) supports.  The p=3, r=5 falsifier is
checked by independent exact combinatorial formulas and integer inequalities.
"""

from __future__ import annotations

import argparse
import copy
import itertools
import json
import math
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[2]
CERT_PATH = (
    ROOT
    / "experimental"
    / "data"
    / "certificates"
    / "sidon-effective-image-cyclotomic-phase-floor"
    / "sidon_effective_image_cyclotomic_phase_floor.json"
)


class CheckCounter:
    def __init__(self) -> None:
        self.count = 0

    def require(self, condition: bool, message: str) -> None:
        self.count += 1
        if not condition:
            raise AssertionError(message)


# Exact arithmetic in Z[zeta_3] with zeta_3^2 + zeta_3 + 1 = 0.
Cyclo3 = tuple[int, int]
ONE: Cyclo3 = (1, 0)
ZERO: Cyclo3 = (0, 0)
ROOTS: tuple[Cyclo3, Cyclo3, Cyclo3] = ((1, 0), (0, 1), (-1, -1))


def cadd(x: Cyclo3, y: Cyclo3) -> Cyclo3:
    return (x[0] + y[0], x[1] + y[1])


def cmul(x: Cyclo3, y: Cyclo3) -> Cyclo3:
    a, b = x
    c, d = y
    # (a+bz)(c+dz) with z^2=-1-z.
    return (a * c - b * d, a * d + b * c - b * d)


def elementary_coefficient_3(phases: Iterable[int], degree: int) -> Cyclo3:
    coeffs = [ZERO] * (degree + 1)
    coeffs[0] = ONE
    seen = 0
    for phase in phases:
        root = ROOTS[phase % 3]
        seen += 1
        for j in range(min(seen, degree), 0, -1):
            coeffs[j] = cadd(coeffs[j], cmul(coeffs[j - 1], root))
    return coeffs[degree]


def phase_word_from_free(free: tuple[int, ...], m: int, p: int) -> tuple[int, ...]:
    """Gauge-fixed phase code for T={0,e_1,...,e_(N-2),u}."""
    last = (-sum(free[: m - 1])) % p
    return (0, *free, last)


def split_balanced(word: tuple[int, ...], p: int, r: int) -> bool:
    n = len(word)
    m = p * r
    if n != 2 * m:
        return False
    # S_* consists of e_1,...,e_(m-1),u; complement contains 0.
    star = (*word[1:m], word[-1])
    complement = (word[0], *word[m:-1])
    target = [r] * p
    return [star.count(a) for a in range(p)] == target and [
        complement.count(a) for a in range(p)
    ] == target


def support_vectors(p: int, r: int) -> list[tuple[int, ...]]:
    n = 2 * p * r
    m = p * r
    d = n - 2
    zero = (0,) * d
    basis = [tuple(1 if i == j else 0 for i in range(d)) for j in range(d)]
    u = tuple((-1 if i < m - 1 else 0) % p for i in range(d))
    return [zero, *basis, u]


def add_vectors_mod(vectors: list[tuple[int, ...]], support: tuple[int, ...], p: int) -> tuple[int, ...]:
    d = len(vectors[0])
    out = [0] * d
    for idx in support:
        vec = vectors[idx]
        for j, value in enumerate(vec):
            out[j] = (out[j] + value) % p
    return tuple(out)


def balanced_word_count(total: int, p: int, each: int) -> int:
    if total != p * each:
        raise ValueError("balanced count mismatch")
    remaining = total
    value = 1
    for _ in range(p - 1):
        value *= math.comb(remaining, each)
        remaining -= each
    return value


def validate_certificate(cert: dict[str, Any], *, exhaustive: bool) -> int:
    checks = CheckCounter()
    checks.require(cert["schema"] == "rs-mca/sidon-effective-image-cyclotomic-phase-floor/v1", "schema")
    checks.require(cert["status"] == "COUNTEREXAMPLE_NEW_FLOOR", "status")
    checks.require(cert["acceptance_criterion"] == 4, "criterion")
    checks.require(cert["route_cut"] == "PHASE_HISTOGRAM_LOCAL_MI_MA", "route cut")

    reg = cert["finite_enumeration_regression"]
    p = reg["p"]
    r = reg["r"]
    n = 2 * p * r
    m = p * r
    d = n - 2
    checks.require((p, r, n, m, d) == (3, 2, 12, 6, 10), "regression parameters")
    checks.require(reg["N"] == n and reg["m"] == m, "regression N,m")
    checks.require(reg["phase_code_dimension"] == d, "regression phase dimension")
    checks.require(reg["phase_code_size"] == p**d, "regression phase-code size")
    checks.require(reg["source_mass"] == math.comb(n, m), "regression source mass")
    checks.require(reg["realized_image_size"] == math.comb(n, m), "regression image size")
    checks.require(reg["effective_target_size"] == p**d, "regression effective target")

    half = balanced_word_count(m, p, r)
    anchored_complement = math.factorial(m - 1) // (
        math.factorial(r - 1) * math.factorial(r) ** (p - 1)
    )
    checks.require(half == 90, "regression half-balanced formula")
    checks.require(anchored_complement == 30, "regression anchored-complement formula")
    checks.require(reg["half_balanced_count"] == half, "regression half count certificate")
    checks.require(
        reg["anchored_complement_balanced_count"] == anchored_complement,
        "regression complement count certificate",
    )
    checks.require(reg["coherent_block_count"] == half * anchored_complement, "regression block count")
    checks.require(reg["cyclotomic_coefficient"] == math.comb(2 * r, r), "regression coefficient")
    checks.require(
        reg["coherent_block_mass"]
        == reg["coherent_block_count"] * reg["cyclotomic_coefficient"],
        "regression coherent mass",
    )

    if exhaustive:
        block_count = 0
        coherent_sum: Cyclo3 = ZERO
        for free in itertools.product(range(p), repeat=d):
            word = phase_word_from_free(free, m, p)
            if split_balanced(word, p, r):
                block_count += 1
                coefficient = elementary_coefficient_3(word, m)
                checks.require(coefficient == (6, 0), "enumerated block coefficient")
                coherent_sum = cadd(coherent_sum, coefficient)
        checks.require(block_count == reg["coherent_block_count"], "enumerated coherent block count")
        checks.require(coherent_sum == (reg["coherent_block_mass"], 0), "enumerated coherent block sum")

        vectors = support_vectors(p, r)
        fibers: dict[tuple[int, ...], int] = {}
        zero = (0,) * d
        zero_supports: list[tuple[int, ...]] = []
        for support in itertools.combinations(range(n), m):
            target = add_vectors_mod(vectors, support, p)
            fibers[target] = fibers.get(target, 0) + 1
            if target == zero:
                zero_supports.append(support)
        checks.require(len(fibers) == math.comb(n, m), "enumerated injective support image")
        checks.require(max(fibers.values()) == 1, "enumerated singleton fibers")
        checks.require(len(zero_supports) == 1, "enumerated unique zero target")
        expected_star = tuple(range(1, m)) + (n - 1,)
        checks.require(zero_supports[0] == expected_star, "enumerated zero-target support")

    fin = cert["finite_falsifier"]
    p = fin["p"]
    r = fin["r"]
    n = 2 * p * r
    m = p * r
    d = n - 2
    checks.require((p, r, n, m, d) == (3, 5, 30, 15, 28), "falsifier parameters")
    checks.require(fin["N"] == n and fin["m"] == m, "falsifier N,m")
    checks.require(fin["field_extension_degree"] == d, "falsifier field degree")
    checks.require(fin["phase_code_dimension"] == d, "falsifier phase dimension")
    checks.require(fin["phase_code_size"] == p**d, "falsifier phase-code size")
    checks.require(fin["source_mass"] == math.comb(n, m), "falsifier source mass")
    checks.require(fin["realized_image_size"] == math.comb(n, m), "falsifier image size")
    checks.require(fin["effective_target_size"] == p**d, "falsifier effective target")

    half = balanced_word_count(m, p, r)
    anchored_complement = math.factorial(m - 1) // (
        math.factorial(r - 1) * math.factorial(r) ** (p - 1)
    )
    coefficient = math.comb(2 * r, r)
    block = half * anchored_complement
    mass = block * coefficient
    checks.require(half == 756756, "falsifier half-balanced exact")
    checks.require(anchored_complement == 252252, "falsifier anchored complement exact")
    checks.require(block == 190893214512, "falsifier block exact")
    checks.require(coefficient == 252, "falsifier coefficient exact")
    checks.require(mass == 48105090057024, "falsifier coherent mass exact")
    checks.require(fin["half_balanced_count"] == half, "falsifier half certificate")
    checks.require(
        fin["anchored_complement_balanced_count"] == anchored_complement,
        "falsifier complement certificate",
    )
    checks.require(fin["coherent_block_count"] == block, "falsifier block certificate")
    checks.require(fin["cyclotomic_coefficient"] == coefficient, "falsifier coefficient certificate")
    checks.require(fin["coherent_block_mass"] == mass, "falsifier mass certificate")
    checks.require(mass > 2 * p**d, "coherent mass defeats double effective target")
    checks.require(fin["double_effective_target_gap"] == mass - 2 * p**d, "double-target gap")
    checks.require(fin["double_effective_target_gap"] == 2351505147102, "double-target gap exact")

    source = math.comb(n, m)
    required_nontrivial_multiplier = (mass + source - 1) // source
    kappa_floor = required_nontrivial_multiplier + 1
    checks.require(kappa_floor == 310122, "source payment kappa floor exact")
    checks.require(fin["source_payment_kappa_floor"] == kappa_floor, "kappa floor certificate")

    debt = p**d - source - mass
    checks.require(debt == -25228452719583, "signed complement debt exact")
    checks.require(fin["signed_complement_debt"] == debt, "signed debt certificate")
    checks.require(source + mass + debt == p**d, "exact Fourier balance")
    checks.require(fin["unique_zero_target_fiber"] == 1, "finite zero target")

    # Verify the general exact formulas and the elementary lower bounds on a grid.
    for prime in (3, 5, 7):
        for rr in range(1, 7):
            nn = 2 * prime * rr
            mm = prime * rr
            h = balanced_word_count(mm, prime, rr)
            b = h * h // prime
            c = math.comb(2 * rr, rr)
            aeff = prime ** (nn - 2)
            source_mass = math.comb(nn, mm)
            checks.require(h % 1 == 0 and h * h % prime == 0, "integral coherent block")
            checks.require(
                h >= prime**mm // (mm + 1) ** (prime - 1),
                "balanced multinomial lower bound",
            )
            checks.require(c * (2 * rr + 1) >= 2 ** (2 * rr), "central binomial lower bound")
            cleared_fixed_p = (
                b
                * c
                * (mm + 1) ** (2 * (prime - 1))
                * (2 * rr + 1)
            )
            checks.require(
                cleared_fixed_p >= aeff * prime * 2 ** (2 * rr),
                "fixed-p compensated lower bound",
            )
            raw_lhs = b * c * prime * (mm + 1) ** (2 * (prime - 1)) * 2**nn
            raw_rhs = source_mass * prime**nn
            checks.require(raw_lhs >= raw_rhs, "raw phase-block lower bound")

    return checks.count


def run_mutation_tests(cert: dict[str, Any]) -> int:
    mutations: list[tuple[list[str], int | str]] = [
        (["acceptance_criterion"], 3),
        (["finite_enumeration_regression", "coherent_block_count"], 2699),
        (["finite_falsifier", "coherent_block_mass"], 48105090057023),
        (["finite_falsifier", "signed_complement_debt"], -25228452719582),
        (["finite_falsifier", "source_payment_kappa_floor"], 310121),
    ]
    passed = 0
    for path, value in mutations:
        changed = copy.deepcopy(cert)
        cursor: dict[str, Any] = changed
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = value
        try:
            validate_certificate(changed, exhaustive=False)
        except AssertionError:
            passed += 1
        else:
            raise AssertionError(f"mutation was not rejected: {'.'.join(path)}")
    return passed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="run the full certificate replay")
    parser.add_argument("--no-enumeration", action="store_true", help="skip the 3^10 and C(12,6) censuses")
    args = parser.parse_args()
    if not args.check:
        parser.error("pass --check")

    cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
    checks = validate_certificate(cert, exhaustive=not args.no_enumeration)
    mutations = run_mutation_tests(cert)
    mode = "formula-only" if args.no_enumeration else "full-enumeration"
    print(f"RESULT: PASS ({checks} exact checks, {mutations} rejected mutations, mode={mode})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
