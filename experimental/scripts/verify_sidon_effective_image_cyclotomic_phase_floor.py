#!/usr/bin/env python3
"""Verify the trace-linear cyclotomic phase-floor certificate.

Stdlib only. The p=3, r=2 row is exhaustively enumerated over all 3^10
trace-linear phase words and all C(12,6) supports. The p=3, r=5 falsifier is
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


def globally_balanced(word: tuple[int, ...], p: int, r: int) -> bool:
    return [word.count(a) for a in range(p)] == [2 * r] * p


def support_vectors(p: int, r: int) -> list[tuple[int, ...]]:
    n = 2 * p * r
    m = p * r
    d = n - 2
    zero = (0,) * d
    basis = [tuple(1 if i == j else 0 for i in range(d)) for j in range(d)]
    u = tuple((-1 if i < m - 1 else 0) % p for i in range(d))
    return [zero, *basis, u]


def add_vectors_mod(
    vectors: list[tuple[int, ...]], support: tuple[int, ...], p: int
) -> tuple[int, ...]:
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


def multinomial(counts: tuple[int, ...]) -> int:
    total = sum(counts)
    value = math.factorial(total)
    for count in counts:
        value //= math.factorial(count)
    return value


def balanced_histogram_count_p3(r: int) -> int:
    """Exact number of p=3 characters with global histogram (2r,2r,2r)."""
    m = 3 * r
    total = 0
    for a0 in range(2 * r + 1):
        for a1 in range(2 * r + 1):
            a2 = m - a0 - a1
            if not 0 <= a2 <= 2 * r:
                continue
            # The phase sum on S_* must vanish, exactly the trace-code relation.
            if (a1 + 2 * a2) % 3 != 0:
                continue
            b0, b1, b2 = 2 * r - a0, 2 * r - a1, 2 * r - a2
            # The distinguished base coordinate 0 already consumes one zero phase.
            if b0 < 1:
                continue
            star_assignments = multinomial((a0, a1, a2))
            complement_assignments = math.factorial(m - 1) // (
                math.factorial(b0 - 1)
                * math.factorial(b1)
                * math.factorial(b2)
            )
            total += star_assignments * complement_assignments
    return total


def validate_certificate(cert: dict[str, Any], *, exhaustive: bool) -> int:
    checks = CheckCounter()
    checks.require(
        cert["schema"] == "rs-mca/sidon-effective-image-cyclotomic-phase-floor/v2",
        "schema",
    )
    checks.require(cert["status"] == "COUNTEREXAMPLE_NEW_FLOOR", "status")
    checks.require(cert["acceptance_criterion"] == 4, "criterion")
    checks.require(cert["route_cut"] == "PHASE_HISTOGRAM_LOCAL_MI_MA", "route cut")
    checks.require(
        cert["successor_obligation"]
        == "ACTUAL_LEAF_CROSS_HISTOGRAM_CANCELLATION_OR_DIRECT_SIDON",
        "successor",
    )

    reg = cert["finite_enumeration_regression"]
    p = reg["p"]
    r = reg["r"]
    n = 2 * p * r
    m = p * r
    d = n - 2
    checks.require((p, r, n, m, d) == (3, 2, 12, 6, 10), "regression parameters")
    checks.require(reg["N"] == n and reg["m"] == m, "regression N,m")
    checks.require(reg["field_extension_degree"] == d, "regression field degree")
    checks.require(reg["phase_code_dimension"] == d, "regression phase dimension")
    checks.require(reg["phase_code_size"] == p**d, "regression phase-code size")
    checks.require(reg["source_mass"] == math.comb(n, m), "regression source mass")
    checks.require(reg["realized_image_size"] == math.comb(n, m), "regression image size")
    checks.require(reg["effective_target_size"] == p**d, "regression effective target")

    half = balanced_word_count(m, p, r)
    anchored_complement = math.factorial(m - 1) // (
        math.factorial(r - 1) * math.factorial(r) ** (p - 1)
    )
    split_count = half * anchored_complement
    coefficient = math.comb(2 * r, r)
    split_mass = split_count * coefficient
    full_hist_count = balanced_histogram_count_p3(r)
    full_hist_mass = full_hist_count * coefficient
    checks.require(half == 90, "regression half-balanced formula")
    checks.require(anchored_complement == 30, "regression anchored-complement formula")
    checks.require(reg["half_balanced_count"] == half, "regression half count certificate")
    checks.require(
        reg["anchored_complement_balanced_count"] == anchored_complement,
        "regression complement count certificate",
    )
    checks.require(reg["split_balanced_block_count"] == split_count, "regression split count")
    checks.require(reg["cyclotomic_coefficient"] == coefficient, "regression coefficient")
    checks.require(reg["split_balanced_block_mass"] == split_mass, "regression split mass")
    checks.require(full_hist_count == 3900, "regression full histogram formula")
    checks.require(reg["balanced_histogram_count"] == full_hist_count, "regression histogram count")
    checks.require(reg["balanced_histogram_mass"] == full_hist_mass, "regression histogram mass")
    checks.require(
        reg["other_histogram_signed_sum"] == p**d - math.comb(n, m) - full_hist_mass,
        "regression other-histogram balance",
    )

    if exhaustive:
        enumerated_split_count = 0
        enumerated_split_sum: Cyclo3 = ZERO
        enumerated_hist_count = 0
        enumerated_hist_sum: Cyclo3 = ZERO
        total_character_sum: Cyclo3 = ZERO
        for free in itertools.product(range(p), repeat=d):
            word = phase_word_from_free(free, m, p)
            coefficient_exact = elementary_coefficient_3(word, m)
            total_character_sum = cadd(total_character_sum, coefficient_exact)
            if split_balanced(word, p, r):
                enumerated_split_count += 1
                checks.require(coefficient_exact == (6, 0), "enumerated split coefficient")
                enumerated_split_sum = cadd(enumerated_split_sum, coefficient_exact)
            if globally_balanced(word, p, r):
                enumerated_hist_count += 1
                checks.require(coefficient_exact == (6, 0), "enumerated histogram coefficient")
                enumerated_hist_sum = cadd(enumerated_hist_sum, coefficient_exact)
        checks.require(enumerated_split_count == split_count, "enumerated split block count")
        checks.require(enumerated_split_sum == (split_mass, 0), "enumerated split block sum")
        checks.require(enumerated_hist_count == full_hist_count, "enumerated histogram count")
        checks.require(enumerated_hist_sum == (full_hist_mass, 0), "enumerated histogram sum")
        checks.require(total_character_sum == (p**d, 0), "enumerated full Fourier balance")

        vectors = support_vectors(p, r)
        checks.require(len(vectors) == n and len(set(vectors)) == n, "enumerated distinct domain")
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
    split_count = half * anchored_complement
    split_mass = split_count * coefficient
    full_hist_count = balanced_histogram_count_p3(r)
    full_hist_mass = full_hist_count * coefficient
    checks.require(half == 756756, "falsifier half-balanced exact")
    checks.require(anchored_complement == 252252, "falsifier anchored complement exact")
    checks.require(split_count == 190893214512, "falsifier split block exact")
    checks.require(coefficient == 252, "falsifier coefficient exact")
    checks.require(split_mass == 48105090057024, "falsifier split mass exact")
    checks.require(fin["half_balanced_count"] == half, "falsifier half certificate")
    checks.require(
        fin["anchored_complement_balanced_count"] == anchored_complement,
        "falsifier complement certificate",
    )
    checks.require(fin["split_balanced_block_count"] == split_count, "falsifier split count certificate")
    checks.require(fin["cyclotomic_coefficient"] == coefficient, "falsifier coefficient certificate")
    checks.require(fin["split_balanced_block_mass"] == split_mass, "falsifier split mass certificate")
    checks.require(split_mass > 2 * p**d, "split block defeats double effective target")
    checks.require(fin["split_double_effective_target_gap"] == split_mass - 2 * p**d, "split gap")
    checks.require(fin["split_double_effective_target_gap"] == 2351505147102, "split gap exact")

    checks.require(full_hist_count == 616779425262, "falsifier histogram count exact")
    checks.require(full_hist_mass == 155428415166024, "falsifier histogram mass exact")
    checks.require(fin["balanced_histogram_count"] == full_hist_count, "histogram count certificate")
    checks.require(fin["balanced_histogram_mass"] == full_hist_mass, "histogram mass certificate")
    checks.require(full_hist_mass > 6 * p**d, "histogram defeats six effective targets")
    checks.require(
        fin["six_effective_target_gap"] == full_hist_mass - 6 * p**d,
        "six-target gap",
    )
    checks.require(fin["six_effective_target_gap"] == 18167660436258, "six-target gap exact")

    source = math.comb(n, m)
    split_kappa_floor = (split_mass + source - 1) // source + 1
    histogram_kappa_floor = (full_hist_mass + source - 1) // source + 1
    checks.require(split_kappa_floor == 310122, "split payment kappa floor exact")
    checks.require(histogram_kappa_floor == 1002006, "histogram payment kappa floor exact")
    checks.require(fin["split_source_payment_kappa_floor"] == split_kappa_floor, "split kappa certificate")
    checks.require(fin["histogram_source_payment_kappa_floor"] == histogram_kappa_floor, "histogram kappa certificate")

    outside_split = p**d - source - split_mass
    other_histograms = p**d - source - full_hist_mass
    checks.require(outside_split == -25228452719583, "outside-split signed sum exact")
    checks.require(other_histograms == -132551777828583, "other-histogram debt exact")
    checks.require(fin["outside_split_subblock_signed_sum"] == outside_split, "outside-split certificate")
    checks.require(fin["other_histogram_signed_debt"] == other_histograms, "other-histogram certificate")
    checks.require(source + full_hist_mass + other_histograms == p**d, "exact histogram Fourier balance")
    checks.require(fin["unique_zero_target_fiber"] == 1, "finite zero target")

    # Verify the general exact formulas and elementary lower bounds on a grid.
    for prime in (3, 5, 7):
        for rr in range(1, 7):
            nn = 2 * prime * rr
            mm = prime * rr
            h = balanced_word_count(mm, prime, rr)
            split = h * h // prime
            c = math.comb(2 * rr, rr)
            aeff = prime ** (nn - 2)
            source_mass = math.comb(nn, mm)
            checks.require(h * h % prime == 0, "integral split-balanced block")
            checks.require(
                h * (mm + 1) ** (prime - 1) >= prime**mm,
                "balanced multinomial lower bound",
            )
            checks.require(c * (2 * rr + 1) >= 2 ** (2 * rr), "central binomial lower bound")
            cleared_fixed_p = (
                split
                * c
                * (mm + 1) ** (2 * (prime - 1))
                * (2 * rr + 1)
            )
            checks.require(
                cleared_fixed_p >= aeff * prime * 2 ** (2 * rr),
                "fixed-p compensated lower bound",
            )
            raw_lhs = split * c * prime * (mm + 1) ** (2 * (prime - 1)) * 2**nn
            raw_rhs = source_mass * prime**nn
            checks.require(raw_lhs >= raw_rhs, "raw phase-block lower bound")

    return checks.count


def run_mutation_tests(cert: dict[str, Any]) -> int:
    mutations: list[tuple[list[str], int | str]] = [
        (["acceptance_criterion"], 3),
        (["finite_enumeration_regression", "split_balanced_block_count"], 2699),
        (["finite_enumeration_regression", "balanced_histogram_count"], 3899),
        (["finite_falsifier", "split_balanced_block_mass"], 48105090057023),
        (["finite_falsifier", "balanced_histogram_count"], 616779425261),
        (["finite_falsifier", "other_histogram_signed_debt"], -132551777828582),
        (["finite_falsifier", "histogram_source_payment_kappa_floor"], 1002005),
        (["route_cut"], "UNSCOPED_MI_MA"),
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
