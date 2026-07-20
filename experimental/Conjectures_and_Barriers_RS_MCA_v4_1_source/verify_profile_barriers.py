#!/usr/bin/env python3
"""Exact arithmetic for Profile Conjectures and Barriers for RS--MCA.

The binomial coefficients, budgets, lower-route values, extension headrooms,
and affine correction dimensions are computed with integers.  Decimal
logarithms are used only for the printed bit margins and necessary orders for
the ceiling-normalized ambient-moment diagnostic; the precision is far above
what is needed to resolve those ceilings.
"""

from decimal import Decimal, localcontext, ROUND_CEILING
from math import comb


N = 2**21
K = 2**20
P_KB = 2**31 - 2**24 + 1
P_M = 2**31 - 1

# All required agreements lie in this short interval.  Compute one large
# binomial coefficient, then use the exact adjacent recurrence; this avoids
# six independent calls to math.comb at two-million scale.
_MIN_A = 1_116_022
_MAX_A = 1_116_048
BINOM_N = {_MIN_A: comb(N, _MIN_A)}
for _a in range(_MIN_A, _MAX_A):
    _numerator = BINOM_N[_a] * (N - _a)
    assert _numerator % (_a + 1) == 0
    BINOM_N[_a + 1] = _numerator // (_a + 1)


def ceil_div(x: int, y: int) -> int:
    return (x + y - 1) // y


def list_lower(p: int, agreement: int) -> int:
    return ceil_div(BINOM_N[agreement], p ** (agreement - K))


def mca_lower(p: int, q: int, agreement: int) -> int:
    list_size = ceil_div(BINOM_N[agreement], p ** (agreement - K - 1))
    numerator = list_size * (q - N)
    denominator = q - N + K * (list_size - 1)
    return ceil_div(numerator, denominator)


ROWS = (
    {
        "name": "KoalaBear MCA",
        "p": P_KB,
        "q": P_KB**6,
        "target_bits": 128,
        "route_K": K + 1,
        "a0": 1_116_047,
        "a1": 1_116_048,
        "lower": mca_lower,
        "expected_budget": 274_980_728_111_395_087,
        "expected_p0": 138_634_741_058_327_852_652,
        "expected_p1": 57_198_030_366,
        "expected_order": 94_196,
        "expected_headroom": 4_807_520,
        "expected_dimension": 913_633,
    },
    {
        "name": "KoalaBear list",
        "p": P_KB,
        "q": P_KB**6,
        "target_bits": 128,
        "route_K": K,
        "a0": 1_116_046,
        "a1": 1_116_047,
        "lower": list_lower,
        "expected_budget": 274_980_728_111_395_087,
        "expected_p0": 157_702_518_233_425_975_347,
        "expected_p1": 65_065_153_468,
        "expected_order": 94_991,
        "expected_headroom": 4_226_236,
        "expected_dimension": 913_634,
    },
    {
        "name": "Mersenne-31 MCA",
        "p": P_M,
        "q": P_M**4,
        "target_bits": 100,
        "route_K": K + 1,
        "a0": 1_116_023,
        "a1": 1_116_024,
        "lower": mca_lower,
        "expected_budget": 16_777_215,
        "expected_p0": 4_281_388_998_575_706,
        "expected_p1": 1_752_700,
        "expected_order": 641_594,
        "expected_headroom": 9,
        "expected_dimension": 913_681,
    },
    {
        "name": "Mersenne-31 list",
        "p": P_M,
        "q": P_M**4,
        "target_bits": 100,
        "route_K": K,
        "a0": 1_116_022,
        "a1": 1_116_023,
        "lower": list_lower,
        "expected_budget": 16_777_215,
        "expected_p0": 4_870_025_984_688_527,
        "expected_p1": 1_993_678,
        "expected_order": 680_397,
        "expected_headroom": 8,
        "expected_dimension": 913_682,
    },
)


def main() -> None:
    with localcontext() as ctx:
        ctx.prec = 100
        log_two = Decimal(2).ln()

        for row in ROWS:
            p = row["p"]
            q = row["q"]
            a0 = row["a0"]
            a1 = row["a1"]
            budget = q // 2 ** row["target_bits"]

            if row["lower"] is mca_lower:
                p0 = mca_lower(p, q, a0)
                p1 = mca_lower(p, q, a1)
            else:
                p0 = list_lower(p, a0)
                p1 = list_lower(p, a1)

            prefix_depth = a1 - row["route_K"]
            margin = Decimal(budget).ln() / log_two - Decimal(p1).ln() / log_two
            order_real = Decimal(prefix_depth) * (Decimal(p).ln() / log_two) / margin
            necessary_order = int(order_real.to_integral_value(rounding=ROUND_CEILING))
            headroom = (p**prefix_depth * budget) // BINOM_N[a1]
            dimension = N - 2 * a1 + row["route_K"]
            endpoint_numerator = N - a1 + 1

            assert budget == row["expected_budget"]
            assert p0 == row["expected_p0"]
            assert p1 == row["expected_p1"]
            assert p0 > budget > p1
            assert necessary_order == row["expected_order"]
            assert headroom == row["expected_headroom"]
            assert dimension == row["expected_dimension"]

            print(row["name"])
            print(f"  budget             = {budget}")
            print(f"  lower(a0)          = {p0}")
            print(f"  lower(a1)          = {p1}")
            print(f"  prefix depth       = {prefix_depth}")
            print(f"  margin bits        = {margin:.10f}")
            print(f"  necessary order    = {necessary_order}")
            print(f"  extension headroom = {headroom}")
            print(f"  correction dim.    = {dimension}")
            print(f"  real endpoint num. = {endpoint_numerator}")

    print("all profile-barrier arithmetic checks passed")


if __name__ == "__main__":
    main()
