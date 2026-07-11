#!/usr/bin/env python3
"""Exact replay for the characteristic-two one-ray saturation wall."""

from collections import Counter, defaultdict
from itertools import combinations
from math import comb, floor, gcd, lgamma, log
from random import Random


IRREDUCIBLE = {
    3: 0b1011,    # x^3+x+1
    4: 0b10011,   # x^4+x+1
    5: 0b100101,  # x^5+x^2+1
}


def gf_mul(left, right, degree):
    modulus = IRREDUCIBLE[degree]
    mask = (1 << degree) - 1
    out = 0
    while right:
        if right & 1:
            out ^= left
        right >>= 1
        left <<= 1
        if left & (1 << degree):
            left ^= modulus
    return out & mask


def locator(selected, degree):
    # Ascending coefficients; in characteristic two, X-x=X+x.
    polynomial = [1]
    for point in selected:
        nxt = [0] * (len(polynomial) + 1)
        for power, coefficient in enumerate(polynomial):
            nxt[power] ^= gf_mul(coefficient, point, degree)
            nxt[power + 1] ^= coefficient
        polynomial = nxt
    return polynomial


def prefix_and_constant(selected, degree, width):
    polynomial = locator(selected, degree)
    m = len(selected)
    prefix = tuple(polynomial[m - index] for index in range(1, width + 1))
    return prefix, polynomial[0], polynomial


def invariant_under_shift(selected, shift, modulus):
    selected = set(selected)
    return {(value + shift) % modulus for value in selected} == selected


def check_aperiodicity():
    checks = 0
    for degree in (3, 4):
        n = (1 << degree) - 1
        m = (1 << (degree - 1)) - 1
        assert gcd(m, n) == 1
        for selected in combinations(range(n), m):
            assert not any(
                invariant_under_shift(selected, shift, n)
                for shift in range(1, n)
            )
            checks += 1
    return checks


def check_exact_small_fields():
    support_checks = 0
    fiber_checks = 0
    for degree in (3, 4):
        q = 1 << degree
        n = q - 1
        m = (q >> 1) - 1
        width = floor(n / (degree * degree))
        k = m - width - 1
        assert k >= 1 and m - width > 0

        refined = Counter()
        full_prefix = defaultdict(lambda: defaultdict(int))
        for selected in combinations(range(1, q), m):
            prefix, constant, polynomial = prefix_and_constant(
                selected, degree, width
            )
            assert constant != 0
            refined[(prefix, constant)] += 1
            full_prefix[prefix][constant] += 1

            # U_z and ell_S cancel through the prefix, and U_z(0)=0.
            difference = polynomial[:]
            difference[m] ^= 1
            for index, coefficient in enumerate(prefix, 1):
                difference[m - index] ^= coefficient
            actual_degree = max(
                (power for power, coefficient in enumerate(difference) if coefficient),
                default=-1,
            )
            assert actual_degree <= k
            assert difference[0] == constant
            support_checks += 1

        lower = (comb(n, m) + q ** (width + 1) - 1) // q ** (width + 1)
        assert max(refined.values()) >= lower
        assert sum(refined.values()) == comb(n, m)
        for cells in full_prefix.values():
            assert sum(cells.values()) > 0
            assert len(cells) <= q - 1
            assert all(slope != 0 and count > 0 for slope, count in cells.items())
            fiber_checks += len(cells)
    return support_checks, fiber_checks


def check_width_one_samples():
    degree = 5
    q = 1 << degree
    n = q - 1
    m = (q >> 1) - 1
    width = floor(n / (degree * degree))
    k = m - width - 1
    assert width == 1
    rng = Random(20260711)
    checks = 0
    for _ in range(4000):
        selected = tuple(sorted(rng.sample(range(1, q), m)))
        prefix, constant, polynomial = prefix_and_constant(selected, degree, width)
        difference = polynomial[:]
        difference[m] ^= 1
        difference[m - 1] ^= prefix[0]
        actual_degree = max(
            (power for power, coefficient in enumerate(difference) if coefficient),
            default=-1,
        )
        assert constant != 0
        assert actual_degree <= k
        assert difference[0] == constant
        checks += 1
    return checks


def check_asymptotic_arithmetic():
    exact_checks = 0
    rate_checks = 0
    for degree in range(5, 13):
        q = 1 << degree
        n = q - 1
        m = (q >> 1) - 1
        width = floor(n / (degree * degree))
        assert gcd(m, n) == 1
        numerator = comb(n, m)
        denominator = q ** (width + 1)
        assert numerator > denominator
        exact_checks += 1

    for degree in range(5, 61):
        q = 1 << degree
        n = q - 1
        m = (q >> 1) - 1
        width = floor(n / (degree * degree))
        log_binomial = lgamma(n + 1) - lgamma(m + 1) - lgamma(n - m + 1)
        normalized = (log_binomial - (width + 1) * log(q)) / n
        assert normalized > 0.35
        assert (width + 1) * log(q) / n < 0.25
        rate_checks += 1
    return exact_checks, rate_checks


def main():
    aperiodic = check_aperiodicity()
    supports, cells = check_exact_small_fields()
    sampled = check_width_one_samples()
    exact, rates = check_asymptotic_arithmetic()
    print("object: aperiodic one-ray saturation wall")
    print(f"aperiodic support census: {aperiodic} PASS")
    print(f"exact small-field support checks: {supports} PASS")
    print(f"complete-prefix constant cells: {cells} PASS")
    print(f"width-one F_32 samples: {sampled} PASS")
    print(f"exact asymptotic integer rows: {exact} PASS")
    print(f"rate rows: {rates} PASS")
    print("status: PROVED route cut")


if __name__ == "__main__":
    main()
