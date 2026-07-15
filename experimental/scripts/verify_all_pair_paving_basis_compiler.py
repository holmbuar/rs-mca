#!/usr/bin/env python3
"""Replay exact finite formulas for the all-pair paving-basis compiler.

This standard-library script is deliberately non-load-bearing.  It checks
integer/binomial identities, finite monotonicity grids, pinned calibrations,
and common formula mutations.  It does not verify the weighted-RS source
hypotheses, the matroid proof, or the one-owner argument.

No ``assert`` statements are used, so ``python -O`` performs the same checks.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable
from fractions import Fraction
from itertools import combinations
from math import comb


class VerificationError(RuntimeError):
    """Raised when an always-active exact check fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def ceil_div(numerator: int, denominator: int) -> int:
    require(numerator >= 0, "ceil_div received a negative numerator")
    require(denominator > 0, "ceil_div received a nonpositive denominator")
    return (numerator + denominator - 1) // denominator


def paving_term(length: int, kappa: int, weight: int) -> int:
    return comb(length - weight - 1, kappa)


def direction_numerator(
    length: int,
    kappa: int,
    distance: int,
    weight: int,
) -> int:
    return max(distance - weight, 0) * comb(length - weight, kappa)


def direction_term(
    length: int,
    kappa: int,
    distance: int,
    weight: int,
) -> int:
    return ceil_div(
        direction_numerator(length, kappa, distance, weight),
        kappa + 1,
    )


def paving_charge(
    length: int,
    kappa: int,
    distance: int,
    weight: int,
) -> int:
    return max(
        paving_term(length, kappa, weight),
        direction_term(length, kappa, distance, weight),
    )


def compiler_bound(
    length: int,
    kappa: int,
    distance: int,
    radius: int,
) -> int:
    charge = paving_charge(length, kappa, distance, radius)
    require(charge > 0, "uniform paving charge vanished")
    return comb(length, kappa + 1) // charge


def check_pinned_calibration() -> dict[str, int]:
    length = 90
    redundancy = 86
    kappa = 4
    radius = 31
    distance = 50

    require(length == redundancy + kappa, "calibration N != R+kappa")
    require(0 <= radius < redundancy, "calibration radius is inadmissible")
    require(1 <= distance <= redundancy, "calibration distance is inadmissible")

    ambient = comb(length, kappa + 1)
    paving = paving_term(length, kappa, radius)
    direction_binomial = comb(length - radius, kappa)
    direction = direction_term(length, kappa, distance, radius)
    charge = paving_charge(length, kappa, distance, radius)
    bound = compiler_bound(length, kappa, distance, radius)

    require(ambient == 43_949_268, "ambient basis census changed")
    require(paving == 424_270, "paving charge changed")
    require(direction_binomial == 455_126, "direction binomial changed")
    require(direction == 1_729_479, "direction ceiling changed")
    require(charge == direction, "wrong active calibration charge")
    require(bound == 25, "calibration compiler bound changed")

    return {
        "ambient": ambient,
        "paving": paving,
        "direction_binomial": direction_binomial,
        "direction": direction,
        "charge": charge,
        "bound": bound,
    }


def check_monotonicity_grid() -> tuple[int, int]:
    transition_checks = 0
    ratio_checks = 0

    for redundancy in range(2, 25):
        for kappa in range(1, 9):
            length = redundancy + kappa
            for distance in range(1, redundancy + 1):
                for radius in range(redundancy):
                    charges = [
                        paving_charge(length, kappa, distance, weight)
                        for weight in range(radius + 1)
                    ]
                    paving_values = [
                        paving_term(length, kappa, weight)
                        for weight in range(radius + 1)
                    ]
                    direction_values = [
                        direction_term(length, kappa, distance, weight)
                        for weight in range(radius + 1)
                    ]
                    for index in range(radius):
                        require(
                            paving_values[index] >= paving_values[index + 1],
                            "paving term increased with weight",
                        )
                        require(
                            direction_values[index] >= direction_values[index + 1],
                            "direction term increased with weight",
                        )
                        require(
                            charges[index] >= charges[index + 1],
                            "combined charge increased with weight",
                        )
                        transition_checks += 1

                    for weight in range(min(radius, distance - 2) + 1):
                        current = direction_numerator(
                            length, kappa, distance, weight
                        )
                        following = direction_numerator(
                            length, kappa, distance, weight + 1
                        )
                        require(following > 0, "ratio denominator vanished")
                        direct_ratio = Fraction(current, following)
                        factored_ratio = Fraction(
                            distance - weight,
                            distance - weight - 1,
                        ) * Fraction(
                            length - weight,
                            length - weight - kappa,
                        )
                        require(
                            direct_ratio == factored_ratio,
                            "factored monotonicity ratio changed",
                        )
                        require(
                            direct_ratio > 1,
                            "direction monotonicity ratio is not greater than one",
                        )
                        ratio_checks += 1

    require(transition_checks > 0, "monotonicity grid was empty")
    require(ratio_checks > 0, "ratio grid was empty")
    return transition_checks, ratio_checks


def check_deep_hole_identity() -> int:
    checks = 0
    for redundancy in range(1, 33):
        for kappa in range(1, 11):
            length = redundancy + kappa
            for weight in range(redundancy):
                numerator = (redundancy - weight) * comb(
                    length - weight, kappa
                )
                total_local_subsets = comb(length - weight, kappa + 1)
                require(
                    numerator == (kappa + 1) * total_local_subsets,
                    "deep-hole binomial identity failed",
                )
                require(
                    ceil_div(numerator, kappa + 1) == total_local_subsets,
                    "deep-hole ceiling did not equal the full local census",
                )
                checks += 1
    return checks


def check_one_circuit_formula() -> int:
    checks = 0
    for redundancy in range(2, 97):
        length = redundancy + 1
        ambient = comb(length, 2)
        for radius in range(redundancy):
            expected = (redundancy * (redundancy + 1)) // (
                2 * (redundancy - radius)
            )
            actual = ambient // comb(length - radius - 1, 1)
            require(actual == expected, "one-circuit formula mismatch")
            if radius <= redundancy - 2:
                require(actual < ambient, "one-circuit strengthening is not strict")
            else:
                require(actual == ambient, "sharp one-circuit boundary changed")
            checks += 1
    return checks


def check_sharp_family() -> tuple[int, int, int, int]:
    formula_checks = 0
    for radius in range(2, 21):
        redundancy = radius + 1
        for kappa in range(1, 13):
            length = radius + kappa + 1
            pair_count = comb(length, radius)
            ambient = comb(length, kappa + 1)
            deep_charge = comb(length - radius, kappa + 1)
            require(pair_count == ambient, "sharp-family pair/ambient identity failed")
            require(deep_charge == 1, "sharp-family deep charge is not one")
            require(
                ambient // deep_charge == pair_count,
                "sharp-family compiler is not attained",
            )
            require(
                compiler_bound(length, kappa, redundancy, radius) == pair_count,
                "sharp-family uniform compiler changed",
            )
            formula_checks += 1

    slopes: dict[int, int] = {}
    for left, right in combinations(range(5), 2):
        slope = (left + right) % 5
        slopes[slope] = slopes.get(slope, 0) + 1
    pair_count = sum(slopes.values())
    require(pair_count == 10, "F_5 sharp pair count changed")
    require(len(slopes) == 5, "F_5 slope projection changed")
    require(set(slopes.values()) == {2}, "F_5 slope multiplicity changed")
    return formula_checks, pair_count, len(slopes), max(slopes.values())


def expect_rejected(label: str, check: Callable[[], None]) -> str:
    try:
        check()
    except VerificationError:
        return label
    raise VerificationError(f"mutation was not rejected: {label}")


def check_mutations(verbose: bool) -> tuple[str, ...]:
    calibration = check_pinned_calibration()

    def paving_off_by_one() -> None:
        mutated = comb(90 - 31, 4)
        require(mutated == calibration["paving"], "paving off-by-one accepted")

    def direction_floor_for_ceiling() -> None:
        mutated = (50 - 31) * comb(90 - 31, 4) // 5
        require(mutated == calibration["direction"], "direction floor accepted")

    def reversed_monotonicity_sign() -> None:
        ratio = Fraction(50 - 31, 50 - 31 - 1) * Fraction(
            90 - 31, 90 - 31 - 4
        )
        require(ratio < 1, "reversed monotonicity sign accepted")

    def wrong_deep_hole_order() -> None:
        mutated = comb(5 - 2, 2)
        require(mutated == 1, "deep-hole kappa-order denominator accepted")

    def slope_projection_as_pair_count() -> None:
        require(5 == 10, "slope projection accepted as the pair count")

    def inverted_one_circuit_fraction() -> None:
        redundancy = 6
        radius = 2
        mutated = 2 * (redundancy - radius) // (
            redundancy * (redundancy + 1)
        )
        correct = comb(redundancy + 1, 2) // (redundancy - radius)
        require(mutated == correct, "inverted one-circuit fraction accepted")

    mutations = (
        ("paving_N_minus_t_off_by_one", paving_off_by_one),
        ("direction_floor_for_ceiling", direction_floor_for_ceiling),
        ("monotonicity_ratio_less_than_one", reversed_monotonicity_sign),
        ("deep_hole_choose_kappa", wrong_deep_hole_order),
        ("slope_projection_as_pair_count", slope_projection_as_pair_count),
        ("one_circuit_fraction_inverted", inverted_one_circuit_fraction),
    )
    rejected = tuple(expect_rejected(label, check) for label, check in mutations)
    require(len(rejected) == len(mutations), "mutation rejection count changed")
    if verbose:
        for label in rejected:
            print(f"mutation.{label}=REJECTED")
    return rejected


def run_check() -> None:
    calibration = check_pinned_calibration()
    transitions, ratios = check_monotonicity_grid()
    deep_checks = check_deep_hole_identity()
    circuit_checks = check_one_circuit_formula()
    sharp_checks, sharp_pairs, sharp_slopes, sharp_multiplicity = check_sharp_family()
    rejected = check_mutations(verbose=False)

    require(transitions == 340_400, "finite charge-transition coverage changed")
    require(ratios == 239_200, "finite ratio coverage changed")
    require(deep_checks == 5_280, "deep-hole identity coverage changed")
    require(circuit_checks == 4_655, "one-circuit coverage changed")
    require(sharp_checks == 228, "sharp-family coverage changed")

    print("ALL_PAIR_PAVING_BASIS_FORMULA_AUDIT")
    print("scope=exact_integer_formulas_and_pinned_mutations_only")
    print("proof_status=NOT_A_PROOF")
    print("calibration=N90_R86_kappa4_t31_d50")
    print(f"ambient_basis_census={calibration['ambient']}")
    print(f"paving_charge={calibration['paving']}")
    print(f"direction_binomial={calibration['direction_binomial']}")
    print(f"direction_charge={calibration['direction']}")
    print(f"uniform_charge={calibration['charge']}")
    print(f"all_pair_bound={calibration['bound']}")
    print("monotonicity_ratio_relation=>1")
    print(f"finite_grid_charge_transitions={transitions}")
    print(f"finite_grid_ratio_checks={ratios}")
    print(f"deep_hole_identity_checks={deep_checks}")
    print(f"one_circuit_formula_checks={circuit_checks}")
    print(f"sharp_family_formula_checks={sharp_checks}")
    print(
        "sharp_F5_pair_projection="
        f"pairs:{sharp_pairs},slopes:{sharp_slopes},max_multiplicity:{sharp_multiplicity}"
    )
    print(f"mutation_classes={len(rejected)}")
    print(f"mutation_rejections={len(rejected)}")
    print("RESULT=PASS")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--tamper-selftest", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.check:
        run_check()
        return

    print("ALL_PAIR_PAVING_BASIS_MUTATION_SELFTEST")
    print("scope=pinned_formula_mutations_only")
    rejected = check_mutations(verbose=True)
    print(f"mutation_rejections={len(rejected)}")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
