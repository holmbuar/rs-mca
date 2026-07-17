#!/usr/bin/env python3
"""Exact F_169 replay for the strict-deep partial-occupancy counterexample.

This stdlib-only verifier enumerates the complete canonical cell, checks the
fixed-remainder image bound label by label, and records the realized locator-
prefix census.  It also gates the precise correction to the older atlas:
absence of a clean coordinate does not imply that the joint prefix image is
the full Cartesian space B^w.

Both --check and --tamper-selftest are fail-closed under normal Python and
python -O; no verification condition relies on assertions.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import sys


P = 13
ONE = 1

class VerificationError(RuntimeError):
    """Raised when an exact arithmetic or finite-field gate fails."""


def require(condition: bool, message: str) -> None:
    if not bool(condition):
        raise VerificationError(message)




def enc(a: int, b: int) -> int:
    return (a % P) + P * (b % P)


def add(x: int, y: int) -> int:
    return enc(x % P + y % P, x // P + y // P)


def neg(x: int) -> int:
    return enc(-(x % P), -(x // P))


def mul(x: int, y: int) -> int:
    a, b = x % P, x // P
    c, d = y % P, y // P
    return enc(a * c + 2 * b * d, a * d + b * c)


def fpow(x: int, exponent: int) -> int:
    require(exponent >= 0, "field exponent must be nonnegative")
    out = ONE
    while exponent:
        if exponent & 1:
            out = mul(out, x)
        x = mul(x, x)
        exponent >>= 1
    return out


def inv(x: int) -> int:
    require(x != 0, "cannot invert zero")
    return fpow(x, 167)


def div(x: int, y: int) -> int:
    return mul(x, inv(y))


def ceil_div(a: int, b: int) -> int:
    require(a >= 0 and b > 0, "ceil_div expects nonnegative a and positive b")
    return (a + b - 1) // b

def has_clean_slot(c: int, r: int, w: int) -> bool:
    """Whether some quotient coordinate j*c lies above r and within depth w."""
    return any(r < j * c <= w for j in range(1, w // c + 1))


def locator_prefix(support: list[int], depth: int) -> tuple[int, ...]:
    """Return the first ``depth`` coefficients after the monic leading term."""
    require(0 <= depth <= len(support), "locator-prefix depth is out of range")
    coeff = [ONE]
    for root in support:
        new = [0] * (len(coeff) + 1)
        for index, value in enumerate(coeff):
            new[index] = add(new[index], value)
            new[index + 1] = add(new[index + 1], neg(mul(value, root)))
        coeff = new
    require(len(coeff) == len(support) + 1, "locator degree mismatch")
    return tuple(coeff[1 : depth + 1])


def validate_generator(theta: int) -> None:
    require(fpow(theta, 168) == ONE, "theta does not lie in F_169^x")
    require(all(fpow(theta, 168 // prime) != ONE for prime in (2, 3, 7)),
            "theta is not primitive of order 168")
    require(fpow(theta, 7) == enc(0, 1), "theta^7 mismatch")
    require(fpow(theta, 24) == enc(4, 1), "theta^24 mismatch")
    require(fpow(theta, 56) == enc(3, 0), "theta^56 mismatch")
    require(fpow(theta, 84) == enc(-1, 0), "theta^84 mismatch")


def validate_mask_count(mask_count: int) -> None:
    require(mask_count == 16, "four partial fibers require exactly 2^4 root masks")


def validate_prefix_denominator(denominator: int) -> None:
    require(denominator == 13, "fixed-label image uses |B_phi|=13, not |B|=169")


def validate_strict_deep(w: int, r: int) -> None:
    require(w < r, "counterexample must be strictly deep (w<r)")


def validate_exact_census(realized_image: int, max_fiber: int) -> None:
    require(realized_image == 86_320, "realized prefix-image size mismatch")
    require(max_fiber == 20, "maximum prefix-fiber size mismatch")


def field_and_fibers() -> tuple[list[tuple[int, int]], int]:
    require(pow(2, 6, 13) == 12, "T^2-2 must be irreducible over F_13")

    theta = enc(2, 1)
    validate_generator(theta)

    hgen = fpow(theta, 7)
    subgroup = [fpow(hgen, index) for index in range(24)]
    domain = [mul(theta, value) for value in subgroup]
    require(len(set(subgroup)) == 24, "order-24 subgroup census failed")
    require(len(set(domain)) == 24, "domain coset census failed")

    by_square: dict[int, list[int]] = {}
    for point in domain:
        by_square.setdefault(fpow(point, 2), []).append(point)
    require(len(by_square) == 12, "square fold must have N=12 fibers")
    require(all(len(points) == 2 for points in by_square.values()),
            "square fold must be two-to-one")

    eta = fpow(theta, 2)
    descended = {div(value, eta) for value in by_square}
    require(descended == set(range(1, 13)),
            "quotient points do not descend to F_13^x")

    fibers = [tuple(sorted(by_square[value])) for value in sorted(by_square)]
    return fibers, theta


def enumerate_cell() -> tuple[Counter[tuple[int, ...]], int, int]:
    fibers, _ = field_and_fibers()
    counts: Counter[tuple[int, ...]] = Counter()
    indices = tuple(range(12))
    labels = 0
    max_fixed_label_image = 0
    mask_count = 16
    validate_mask_count(mask_count)

    for partial in combinations(indices, 4):
        partial_set = set(partial)
        remaining = tuple(index for index in indices if index not in partial_set)
        for mask in range(mask_count):
            partial_points = [
                fibers[fiber_index][(mask >> bit) & 1]
                for bit, fiber_index in enumerate(partial)
            ]
            fixed_label_image: set[tuple[int, ...]] = set()
            for complete in combinations(remaining, 4):
                support = partial_points + [
                    point for fiber_index in complete for point in fibers[fiber_index]
                ]
                require(len(support) == 12, "support size must be a=12")
                prefix = locator_prefix(support, 3)
                counts[prefix] += 1
                fixed_label_image.add(prefix)

            # Arbitrary-remainder QR5: each fixed label has image <=|B_phi|^1.
            require(len(fixed_label_image) <= 13,
                    "fixed-label prefix image exceeds |B_phi|=13")
            max_fixed_label_image = max(max_fixed_label_image, len(fixed_label_image))
            labels += 1

    require(labels == comb(12, 4) * 2**4 == 7_920,
            "remainder-label census mismatch")
    return counts, labels, max_fixed_label_image


def collision_floor(list_size: int) -> tuple[int, int]:
    require(list_size >= 1, "collision list size must be positive")
    q, n, k, challenge = 169, 24, 8, 168
    multiplicity = ceil_div(list_size * (q - n), q - n + k * (list_size - 1))
    return multiplicity, ceil_div(challenge * multiplicity, q)


def verify() -> None:
    counts, labels, max_fixed_label_image = enumerate_cell()

    n, a, k, w, c, m, p, r = 24, 12, 8, 3, 2, 4, 4, 4
    validate_strict_deep(w, r)
    depth = min(m, w // c)
    validate_prefix_denominator(13)
    omega = labels * comb(12 - p, m)
    image_bound = labels * 13**depth
    guaranteed_list = ceil_div(comb(12 - p, m), 13**depth)
    identity_list = ceil_div(comb(n, a), 169**w)
    full_cartesian = 169**w

    require((n, a, k, w, c, m, p, r) == (24, 12, 8, 3, 2, 4, 4, 4),
            "strict-deep parameter tuple mismatch")
    require(labels == 7_920, "J must equal 7920")
    require(omega == 554_400, "profile size must equal 554400")
    require(image_bound == 102_960, "analytic image bound must equal 102960")
    require(guaranteed_list == 6, "guaranteed profile list must equal 6")
    require(identity_list == 1, "identity pigeonhole floor must equal 1")
    require(guaranteed_list > identity_list,
            "strict-deep profile list must beat the identity floor")

    require(sum(counts.values()) == omega, "enumerated support count mismatch")
    realized_image = len(counts)
    max_fiber = max(counts.values())
    validate_exact_census(realized_image, max_fiber)
    require(Fraction(omega, realized_image) == Fraction(6_930, 1_079),
            "average prefix-fiber size mismatch")
    require(realized_image <= image_bound, "realized image exceeds analytic bound")
    require(Fraction(omega, realized_image) >= Fraction(comb(8, 4), 13),
            "realized average violates fixed-label guarantee")
    require(max_fiber >= guaranteed_list, "maximum fiber is below guaranteed list")
    require(max_fixed_label_image == 13, "fixed-label image maximum must attain 13")
    require(max_fiber < comb(8, 4),
            "max fiber 20 < 70 must refute any binom(8,4) fixed-prefix "
            "factorization in the r>=c cell")

    no_clean_coordinate = not has_clean_slot(c, r, w)
    require(no_clean_coordinate,
            "strict-deep witness unexpectedly has a clean coordinate")
    require(full_cartesian == 4_826_809,
            "full Cartesian prefix-space size mismatch")
    require(image_bound < full_cartesian and realized_image < full_cartesian,
            "no-clean coordinate must not be upgraded to Cartesian image fill")

    require(collision_floor(6) == (5, 5), "collision floor at L=6 mismatch")
    require(collision_floor(20) == (10, 10), "collision floor at L=20 mismatch")
    require(min(168, n - a + 1) == 13, "tangent floor mismatch")

    print("field=F_13[T]/(T^2-2) theta=2+T domain=theta<theta^7>")
    print("params=(n,a,k,w,c,m,p,r)=(24,12,8,3,2,4,4,4) strict_deep=True")
    print(f"labels={labels} supports={omega} analytic_image_bound={image_bound}")
    print(
        f"realized_image={realized_image} max_fiber={max_fiber} "
        f"average={Fraction(omega, realized_image)} "
        f"max_fixed_label_image={max_fixed_label_image}"
    )
    print(
        f"no_clean_coordinate={no_clean_coordinate} full_cartesian={full_cartesian} "
        "cartesian_fill_implication=False fixed_prefix_factorization=False"
    )
    print(
        f"guaranteed_list={guaranteed_list} identity_floor={identity_list} "
        "pole_floor_L6=5 pole_floor_L20=10 tangent_floor=13"
    )
    print("RESULT: PASS")


def expect_rejected(name: str, action) -> bool:
    try:
        action()
    except VerificationError:
        print("ok    tamper rejected:", name)
        return True
    print("FAIL  tamper accepted:", name)
    return False


def tamper_selftest() -> None:
    trials = [
        expect_rejected("nonprimitive generator theta=1+T",
                        lambda: validate_generator(enc(1, 1))),
        expect_rejected("15 masks instead of 16",
                        lambda: validate_mask_count(15)),
        expect_rejected("full-field denominator 169 instead of 13",
                        lambda: validate_prefix_denominator(169)),
        expect_rejected("boundary w=r=4 instead of strict w<r",
                        lambda: validate_strict_deep(4, 4)),
        expect_rejected("realized image 86321 instead of 86320",
                        lambda: validate_exact_census(86_321, 20)),
        expect_rejected("maximum fiber 19 instead of 20",
                        lambda: validate_exact_census(86_320, 19)),
    ]
    passed = sum(1 for trial in trials if trial)
    require(passed == len(trials),
            "one or more tamper corruptions escaped detection")
    print(f"RESULT: PASS tamper-selftest {passed}/{len(trials)}")


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "--check"
    try:
        if mode == "--check":
            verify()
            return 0
        if mode == "--tamper-selftest":
            tamper_selftest()
            return 0
        print("usage: verify_deep_remainder_partial_occupancy_counterexample.py "
              "[--check | --tamper-selftest]")
        return 2
    except (VerificationError, ValueError, ZeroDivisionError) as exc:
        print("RESULT: FAIL:", exc, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
