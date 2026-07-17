#!/usr/bin/env python3
"""Verify the realized-image Boolean-slice energy and orientation lifts."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import comb, isclose, log, log2


class VerificationError(RuntimeError):
    """Raised when a fail-closed audit gate fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


Syndrome = tuple[int, int]
Selector = dict[Syndrome, int]


def layer_count(n: int, total: int, cap: int) -> int:
    row = [0] * (total + 1)
    row[0] = 1
    for _ in range(n):
        nxt = [0] * (total + 1)
        for s, value in enumerate(row):
            if not value:
                continue
            for digit in range(cap + 1):
                if s + digit <= total:
                    nxt[s + digit] += value
        row = nxt
    return row[total]


def h2(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * log2(p) - (1.0 - p) * log2(1.0 - p)


def entropy(probs: tuple[float, ...]) -> float:
    return -sum(p * log2(p) for p in probs if p)


def g(p: float) -> float:
    return entropy(
        (
            (1.0 - p) ** 2 / 2.0,
            (1.0 - p * p) / 2.0,
            p * (2.0 - p) / 2.0,
            p * p / 2.0,
        )
    )


def masks_of_weight(n: int, m: int) -> list[int]:
    return [x for x in range(1 << n) if x.bit_count() == m]


def syndrome(mask: int, coeffs: tuple[int, ...], modulus: int) -> int:
    return sum(coeffs[i] for i in range(len(coeffs)) if mask >> i & 1) % modulus


def sum_code(a: int, b: int, n: int) -> int:
    code = 0
    scale = 1
    for i in range(n):
        code += (((a >> i) & 1) + ((b >> i) & 1)) * scale
        scale *= 3
    return code


def mask_vector(mask: int, n: int) -> tuple[int, ...]:
    return tuple((mask >> i) & 1 for i in range(n))


def add_vectors(*vectors: tuple[int, ...]) -> tuple[int, ...]:
    require(bool(vectors), "cannot add an empty vector family")
    require(len({len(vector) for vector in vectors}) == 1, "vector lengths differ")
    return tuple(sum(entries) for entries in zip(*vectors, strict=True))


def energy(points: tuple[int, ...], n: int) -> int:
    counts = Counter(sum_code(a, b, n) for a in points for b in points)
    return sum(value * value for value in counts.values())


def subsets(points: list[int], exhaustive: bool) -> list[tuple[int, ...]]:
    if exhaustive:
        return [
            tuple(points[i] for i in range(len(points)) if bits >> i & 1)
            for bits in range(1, 1 << len(points))
        ]
    ans = [(point,) for point in points]
    ans.append(tuple(points))
    if len(points) > 2:
        ans.append(tuple(points[::2]))
        ans.append(tuple(points[1::2]))
    return [item for item in ans if item]


def check_map(n: int, modulus: int, coeffs: tuple[int, ...], exhaustive: bool) -> tuple[int, bool]:
    checked = 0
    tamper_rejected = False
    all_image = set()
    by_weight: dict[int, dict[int, list[int]]] = {}
    for m in range(n + 1):
        fibers: dict[int, list[int]] = defaultdict(list)
        for mask in masks_of_weight(n, m):
            s = syndrome(mask, coeffs, modulus)
            fibers[s].append(mask)
            all_image.add((m, s))
        by_weight[m] = fibers

    l_all = len(all_image)
    for m, fibers in by_weight.items():
        theta = m / n
        l_slice = len(fibers)
        a_count = layer_count(n, 2 * m, 2)
        b_count = layer_count(n, 3 * m, 3)
        a_entropy = 1.0 + h2(theta) / 2.0
        g_entropy = g(theta)
        for points in fibers.values():
            for chosen in subsets(points, exhaustive and len(points) <= 9):
                f = len(chosen)
                e = energy(chosen, n)
                require(
                    f * l_slice <= a_count,
                    "slice coefficient inequality failed",
                )
                require(
                    f * l_slice * f**3 <= b_count * e,
                    "slice energy inequality failed",
                )
                require(
                    f * l_slice <= 2.0 ** (n * a_entropy) + 1e-9,
                    "slice one-copy entropy inequality failed",
                )
                require(
                    f * l_slice * f**3
                    <= 2.0 ** (n * g_entropy) * e + 1e-7,
                    "slice two-copy entropy inequality failed",
                )
                require(
                    f * l_all <= 2.0 ** (n * a_entropy) + 1e-9,
                    "augmented-image one-copy entropy inequality failed",
                )
                require(
                    f * l_all * f**3
                    <= 2.0 ** (n * g_entropy) * e + 1e-7,
                    "augmented-image two-copy entropy inequality failed",
                )
                # The false strengthening fL <= B Delta^2 must not pass all tests.
                if f * l_slice * f**6 > b_count * e * e:
                    tamper_rejected = True
                checked += 6
    return checked, tamper_rejected


def augmented_syndrome(
    mask: int, n: int, coeffs: tuple[int, ...], modulus: int
) -> Syndrome:
    return (mask.bit_count(), syndrome(mask, coeffs, modulus))


def fixed_orbit_fixture() -> tuple[
    int, tuple[Syndrome, ...], tuple[Selector, ...], tuple[int, ...]
]:
    n = 2
    modulus = 2
    coeffs = (0, 0)
    masks = tuple(range(1 << n))
    image = tuple(
        sorted({augmented_syndrome(mask, n, coeffs, modulus) for mask in masks})
    )
    representatives = {
        u: tuple(
            mask
            for mask in masks
            if augmented_syndrome(mask, n, coeffs, modulus) == u
        )
        for u in image
    }
    selectors = tuple(
        dict(zip(image, choices, strict=True))
        for choices in product(*(representatives[u] for u in image))
    )
    fiber = tuple(masks_of_weight(n, 1))
    return n, image, selectors, fiber


def selector_marginal_totals(
    selector: Selector, image: tuple[Syndrome, ...], n: int
) -> tuple[int, ...]:
    return tuple(
        sum((selector[u] >> coordinate) & 1 for u in image)
        for coordinate in range(n)
    )


def require_balanced_deterministic_selector(
    selector: Selector, image: tuple[Syndrome, ...], n: int
) -> None:
    totals = selector_marginal_totals(selector, image, n)
    require(
        all(2 * total == len(image) for total in totals),
        "deterministic selector does not have half marginals",
    )


def fixed_orbit_orientation_regression() -> int:
    n, image, selectors, fiber = fixed_orbit_fixture()
    modulus = 2
    coeffs = (0, 0)
    full_mask = (1 << n) - 1
    total_syndrome = syndrome(full_mask, coeffs, modulus)

    def complement(u: Syndrome) -> Syndrome:
        return (n - u[0], (total_syndrome - u[1]) % modulus)

    checks = 0
    require(image == ((0, 0), (1, 0), (2, 0)), "unexpected augmented image")
    checks += 1
    fixed = tuple(u for u in image if complement(u) == u)
    require(fixed == ((1, 0),), "unexpected complement fixed-point set")
    checks += 1
    require(len(selectors) == 2, "unexpected deterministic selector count")
    checks += 1
    require(
        all(
            augmented_syndrome(selector[u], n, coeffs, modulus) == u
            for selector in selectors
            for u in image
        )
        and all(
            selector[complement(u)] == (full_mask ^ selector[u])
            for selector in selectors
            for u in image
            if complement(u) != u
        ),
        "selector is not source-valid or complement-paired on two-cycles",
    )
    checks += 1

    balanced = sum(
        all(
            2 * total == len(image)
            for total in selector_marginal_totals(selector, image, n)
        )
        for selector in selectors
    )
    require(balanced == 0, "old deterministic-balancing claim was not rejected")
    checks += 1

    one_copy_counts = tuple(
        len(
            {
                add_vectors(mask_vector(x, n), mask_vector(selector[u], n))
                for x in fiber
                for u in image
            }
        )
        for selector in selectors
    )
    require(one_copy_counts == (6, 6), "one-copy orientation map is not injective")
    checks += 1

    mixed_totals = tuple(
        sum(
            (selector[u] >> coordinate) & 1
            for selector in selectors
            for u in image
        )
        for coordinate in range(n)
    )
    require(mixed_totals == (3, 3), "orientation mixture is not marginally fair")
    checks += 1

    one_histogram = Counter(
        add_vectors(mask_vector(x, n), mask_vector(selector[u], n))
        for selector in selectors
        for u in image
        for x in fiber
    )
    one_mass = sum(one_histogram.values())
    require(one_mass == 12, "unexpected one-copy mixture mass")
    checks += 1
    require(len(one_histogram) == 7, "unexpected one-copy mixture support")
    checks += 1
    one_entropy = entropy(tuple(count / one_mass for count in one_histogram.values()))
    require(
        isclose(one_entropy, 2.7516291673878226, abs_tol=1e-15)
        and one_entropy >= log2(6),
        "conditional-injection entropy lower bound failed",
    )
    checks += 1

    pair_histogram = Counter(
        add_vectors(mask_vector(x, n), mask_vector(y, n))
        for x in fiber
        for y in fiber
    )
    pair_mass = sum(pair_histogram.values())
    pair_entropy = entropy(tuple(count / pair_mass for count in pair_histogram.values()))
    e = energy(fiber, n)
    delta = Fraction(e, len(fiber) ** 3)
    require(
        e == 6
        and delta == Fraction(3, 4)
        and isclose(pair_entropy, 1.5, abs_tol=1e-15)
        and pair_entropy >= log2(float(Fraction(len(fiber), 1) / delta)),
        "two-copy Renyi gate failed",
    )
    checks += 1

    two_copy_counts = tuple(
        len(
            {
                add_vectors(pair_sum, mask_vector(selector[u], n))
                for pair_sum in pair_histogram
                for u in image
            }
        )
        for selector in selectors
    )
    require(two_copy_counts == (9, 9), "two-copy orientation map is not injective")
    checks += 1
    return checks


def run_orientation_tamper_selftest() -> int:
    n, image, selectors, _ = fixed_orbit_fixture()
    rejected = 0
    for selector in selectors:
        try:
            require_balanced_deterministic_selector(selector, image, n)
        except VerificationError:
            rejected += 1
        else:
            raise VerificationError("old deterministic-balancing claim was accepted")
    require(rejected == len(selectors), "not every deterministic selector was rejected")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tamper-selftest",
        action="store_true",
        help="reject the old deterministic fixed-orbit balancing claim",
    )
    args = parser.parse_args()
    if args.tamper_selftest:
        rejected = run_orientation_tamper_selftest()
        print(f"PASS: fixed-orbit tamper self-test rejected {rejected}/{rejected}")
        return

    checks = 0
    tamper_rejected = False

    # Exhaust every cyclic syndrome map through N=4.
    for n in range(1, 5):
        for modulus in range(2, 5):
            for coeffs in product(range(modulus), repeat=n):
                count, rejected = check_map(n, modulus, coeffs, True)
                checks += count
                tamper_rejected |= rejected

    # Deterministic N=5 stress maps, including repeated and full-rank-looking rows.
    for modulus in range(2, 8):
        candidates = {
            tuple(0 for _ in range(5)),
            tuple(1 for _ in range(5)),
            tuple(i % modulus for i in range(5)),
            tuple((i * i + 1) % modulus for i in range(5)),
        }
        for coeffs in candidates:
            count, rejected = check_map(5, modulus, coeffs, True)
            checks += count
            tamper_rejected |= rejected

    orientation_checks = fixed_orbit_orientation_regression()
    checks += orientation_checks

    theta0 = 0.173952331409395
    require(
        isclose(h2(theta0), 2.0 / 3.0, rel_tol=0.0, abs_tol=2e-15),
        "binary-entropy root changed",
    )
    g_half = g(0.5)
    gamma0 = g_half - 4.0 / 3.0
    require(
        isclose(g_half, 3.0 - 0.75 * log2(3.0), abs_tol=1e-15),
        "g(1/2) identity changed",
    )
    require(isclose(gamma0, 0.477944791125799, abs_tol=2e-15), "gamma changed")
    require(
        isclose(gamma0 * log(2.0), 0.331286084432160, abs_tol=2e-15),
        "natural-log gamma changed",
    )
    require(
        isclose(log(2.0) / log(4.0 / 3.0), 2.409420839653, abs_tol=5e-13),
        "energy exponent ratio changed",
    )
    require(layer_count(5, 4, 2) == 45, "ternary coefficient changed")
    require(layer_count(5, 6, 3) == 135, "quaternary coefficient changed")
    checks += 7

    require(tamper_rejected, "extra-Delta tamper was not rejected")
    print(f"PASS: {checks:,} theorem checks")
    print(
        "PASS: fixed complement orbit repair "
        "(fixed=1; balanced selectors=0/2; injections=6/6 and 9/9)"
    )
    print("PASS: constants and coefficient recurrences")
    print("PASS: strengthened extra-Delta tamper rejected")


if __name__ == "__main__":
    main()
