"""Exact finite-field and rational-trigonometric helpers for the M31 Q audit."""
from __future__ import annotations

import hashlib
import itertools
import math
from collections import Counter, defaultdict
from fractions import Fraction
from typing import Iterable


def canonical_hash(items: Iterable[str]) -> str:
    return hashlib.sha256(";".join(items).encode("utf-8")).hexdigest()


def cmul(u: tuple[int, int], v: tuple[int, int], p: int) -> tuple[int, int]:
    a, b = u
    c, d = v
    return ((a * c - b * d) % p, (a * d + b * c) % p)


def cpow(u: tuple[int, int], exponent: int, p: int) -> tuple[int, int]:
    result = (1, 0)
    while exponent:
        if exponent & 1:
            result = cmul(result, u, p)
        u = cmul(u, u, p)
        exponent >>= 1
    return result


def multiplicative_order(u: tuple[int, int], p: int) -> int:
    value = (1, 0)
    for exponent in range(1, p + 2):
        value = cmul(value, u, p)
        if value == (1, 0):
            return exponent
    raise AssertionError("order search exceeded p+1")


def circle_generator(p: int) -> tuple[int, int]:
    assert p % 4 == 3
    elements = [
        (a, b)
        for a in range(p)
        for b in range(p)
        if (a * a + b * b) % p == 1
    ]
    assert len(elements) == p + 1
    for point in elements:
        if multiplicative_order(point, p) == p + 1:
            return point
    raise AssertionError("no norm-one torus generator")


def chebyshev_twin_coset(
    p: int, n: int, offset: int = 1
) -> tuple[list[int], set[tuple[int, int]], tuple[int, int]]:
    generator = circle_generator(p)
    order = p + 1
    assert order % n == 0 and 2 * n < order
    subgroup = [cpow(generator, (order // n) * j, p) for j in range(n)]
    g = cpow(generator, offset, p)
    g_inv = cpow(generator, order - offset, p)
    lifted = {cmul(g, h, p) for h in subgroup} | {
        cmul(g_inv, h, p) for h in subgroup
    }
    by_x: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for point in lifted:
        by_x[point[0]].append(point)
    domain = sorted(by_x)
    assert len(lifted) == 2 * n
    assert len(domain) == n
    assert all(len(preimages) == 2 for preimages in by_x.values())
    return domain, lifted, generator


def t2(x: int, p: int) -> int:
    return (2 * x * x - 1) % p


def direct_prefix_census(
    domain: list[int], p: int, m: int
) -> Counter[tuple[int, int]]:
    fibers: Counter[tuple[int, int]] = Counter()
    squares = {x: x * x % p for x in domain}
    for support in itertools.combinations(domain, m):
        fibers[(sum(support) % p, sum(squares[x] for x in support) % p)] += 1
    return fibers


def dp_prefix_census(
    domain: list[int], p: int, m: int
) -> Counter[tuple[int, int]]:
    dp: list[Counter[tuple[int, int]]] = [Counter() for _ in range(m + 1)]
    dp[0][(0, 0)] = 1
    for index, x in enumerate(domain):
        shift = (x, x * x % p)
        for weight in range(min(m, index + 1), 0, -1):
            for (z1, z2), count in list(dp[weight - 1].items()):
                target = ((z1 + shift[0]) % p, (z2 + shift[1]) % p)
                dp[weight][target] += count
    return dp[m]


def census_hash(fibers: Counter[tuple[int, int]], p: int) -> str:
    return canonical_hash(
        f"{z1},{z2},{fibers.get((z1, z2), 0)}"
        for z1 in range(p)
        for z2 in range(p)
    )


def arctan_inverse_interval(q: int, terms: int) -> tuple[Fraction, Fraction]:
    x = Fraction(1, q)
    partial = Fraction(0)
    for j in range(terms):
        term = x ** (2 * j + 1) / (2 * j + 1)
        partial = partial + term if j % 2 == 0 else partial - term
    next_term = x ** (2 * terms + 1) / (2 * terms + 1)
    if terms % 2 == 0:
        return partial, partial + next_term
    return partial - next_term, partial


def pi_interval(terms_5: int, terms_239: int) -> tuple[Fraction, Fraction]:
    a5_lo, a5_hi = arctan_inverse_interval(5, terms_5)
    a239_lo, a239_hi = arctan_inverse_interval(239, terms_239)
    return 16 * a5_lo - 4 * a239_hi, 16 * a5_hi - 4 * a239_lo


def cosine_interval(
    residue: int,
    p: int,
    pi_lo: Fraction,
    pi_hi: Fraction,
    order: int,
) -> tuple[Fraction, Fraction]:
    r = min(residue % p, (-residue) % p)
    x_lo = Fraction(2 * r, p) * pi_lo
    x_hi = Fraction(2 * r, p) * pi_hi
    lower = Fraction(0)
    upper = Fraction(0)
    for j in range(order + 1):
        factorial = math.factorial(2 * j)
        if j % 2 == 0:
            lower += x_lo ** (2 * j) / factorial
            upper += x_hi ** (2 * j) / factorial
        else:
            lower -= x_hi ** (2 * j) / factorial
            upper -= x_lo ** (2 * j) / factorial
    # Regard the same polynomial as the Taylor polynomial through degree 2*order+1;
    # the odd coefficient is zero, so the Lagrange remainder has this size.
    remainder = x_hi ** (2 * order + 2) / math.factorial(2 * order + 2)
    return lower - remainder, upper + remainder


def floor_scaled(value: Fraction, scale: int) -> int:
    return value.numerator * scale // value.denominator


def ceil_scaled(value: Fraction, scale: int) -> int:
    return -((-value.numerator * scale) // value.denominator)


def cosine_lower_table(
    p: int,
    scale: int,
    terms_5: int,
    terms_239: int,
    order: int,
) -> tuple[list[int], int, Fraction, Fraction]:
    pi_lo, pi_hi = pi_interval(terms_5, terms_239)
    table: list[int] = []
    maximum_scaled_width = 0
    for residue in range(p):
        lower, upper = cosine_interval(residue, p, pi_lo, pi_hi, order)
        lo = floor_scaled(lower, scale)
        hi = ceil_scaled(upper, scale)
        table.append(lo)
        maximum_scaled_width = max(maximum_scaled_width, hi - lo)
    return table, maximum_scaled_width, pi_lo, pi_hi
