#!/usr/bin/env python3
"""Verify the rooted order-two Fourier-band reduction.

The theorem under test is finite and exact.  For a full slice Omega0 of size
M, realized image size L, residual Omega* of mass W, and residual image counts
f, every symmetric dual band A satisfies

    ||P_A f||_2^2 <= SP := sum_s f(s)^2 <= W * max_s f(s).

Consequently, if ||P_A f||_2^2 > C M^2/L for C >= 1, then

    max_s f(s) > C M/L

and the residual contains an actual ordered same-boundary support pair.  For
disjoint symmetric bands, mixed order-two patterns vanish; if the bands
partition the nonzero dual, their energies sum to SP - W^2/|G|.

This script checks the identities by independent exact routes on elementary
2-groups and on rank-one prime-field fixed-weight power-sum profiles.  It is
stdlib-only, deterministic, and writes no files.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations


CHECKS: list[tuple[str, bool]] = []
ABSTRACT_CASES = 0
SOURCE_CASES = 0
EMISSION_CASES = 0


def require(name: str, condition: bool) -> None:
    CHECKS.append((name, bool(condition)))
    if not condition:
        print(f"FAIL: {name}")


def f2_character(character: int, value: int) -> int:
    """Character of (F_2)^r, encoded by bit masks."""
    return -1 if (character & value).bit_count() % 2 else 1


def f2_hat(fibers: Counter[int], character: int) -> int:
    return sum(count * f2_character(character, value) for value, count in fibers.items())


def f2_projection(
    fibers: Counter[int], band: tuple[int, ...], group_order: int
) -> tuple[Fraction, ...]:
    hats = {character: f2_hat(fibers, character) for character in band}
    return tuple(
        Fraction(
            sum(
                hats[character] * f2_character(character, value)
                for character in band
            ),
            group_order,
        )
        for value in range(group_order)
    )


def f2_kernel(band: tuple[int, ...], difference: int) -> int:
    return sum(f2_character(character, difference) for character in band)


def f2_pair_route(
    fibers: Counter[int], band: tuple[int, ...], group_order: int
) -> Fraction:
    numerator = 0
    for left, left_count in fibers.items():
        for right, right_count in fibers.items():
            numerator += (
                left_count
                * right_count
                * f2_kernel(band, left ^ right)
            )
    return Fraction(numerator, group_order)


def f2_analyze(
    label: str,
    full_values: list[int],
    residual_indices: tuple[int, ...],
    bands: tuple[tuple[int, ...], ...],
    group_order: int,
) -> None:
    global ABSTRACT_CASES, EMISSION_CASES
    ABSTRACT_CASES += 1

    require(f"{label}: group order is a power of two", group_order > 1 and group_order.bit_count() == 1)
    nonzero_dual = set(range(1, group_order))
    flat_bands = [character for band in bands for character in band]
    require(f"{label}: bands are nonempty", all(band for band in bands))
    require(f"{label}: bands are disjoint", len(flat_bands) == len(set(flat_bands)))
    require(f"{label}: bands partition the nonzero dual", set(flat_bands) == nonzero_dual)

    full_fibers = Counter(full_values)
    residual_values = [full_values[index] for index in residual_indices]
    fibers = Counter(residual_values)
    M = len(full_values)
    L = len(full_fibers)
    W = len(residual_values)
    SP = sum(count * count for count in fibers.values())
    f_max = max(fibers.values(), default=0)

    require(f"{label}: finite slice inequalities", 1 <= L <= M and 0 <= W <= M)
    require(f"{label}: SP upper by W*fmax", SP <= W * f_max)

    energies: list[Fraction] = []
    projections: list[tuple[Fraction, ...]] = []
    for band_index, band in enumerate(bands):
        projection = f2_projection(fibers, band, group_order)
        projections.append(projection)
        projection_energy = sum(value * value for value in projection)
        parseval_energy = Fraction(
            sum(f2_hat(fibers, character) ** 2 for character in band),
            group_order,
        )
        pair_energy = f2_pair_route(fibers, band, group_order)
        energies.append(projection_energy)

        require(
            f"{label}: band {band_index} projection=parseval",
            projection_energy == parseval_energy,
        )
        require(
            f"{label}: band {band_index} projection=rooted-pair",
            projection_energy == pair_energy,
        )
        require(
            f"{label}: band {band_index} L2 contraction",
            projection_energy <= SP,
        )

        normalized = Fraction(L, M * M) * projection_energy
        if normalized > 1:
            EMISSION_CASES += 1
            pair_count = SP - W
            require(
                f"{label}: band {band_index} violation emits Q failure",
                Fraction(f_max * L, M) > 1,
            )
            require(
                f"{label}: band {band_index} violation emits same-boundary pair",
                pair_count > Fraction(M * M, L) - W >= 0,
            )

    for left in range(len(projections)):
        for right in range(left + 1, len(projections)):
            mixed = sum(
                projections[left][value] * projections[right][value]
                for value in range(group_order)
            )
            require(f"{label}: mixed pattern {left},{right} vanishes", mixed == 0)

    total_nonzero_energy = sum(energies, Fraction(0))
    centered_sp = Fraction(SP) - Fraction(W * W, group_order)
    require(
        f"{label}: band sum equals centered SP",
        total_nonzero_energy == centered_sp,
    )
    require(f"{label}: centered SP is nonnegative", centered_sp >= 0)

    if f_max <= 1:
        require(
            f"{label}: injective residual pays every order-two band",
            all(Fraction(L, M * M) * energy <= 1 for energy in energies),
        )


def support_xor_values(columns: tuple[int, ...], weight: int) -> list[int]:
    values: list[int] = []
    for support in combinations(columns, weight):
        value = 0
        for column in support:
            value ^= column
        values.append(value)
    return values


def run_f2_cases() -> None:
    # A deliberately heavy finite map exercises the strict emission branch.
    skew = [0] * 9 + list(range(1, 8))
    f2_analyze(
        "f2-skew-full-band",
        skew,
        tuple(range(len(skew))),
        (tuple(range(1, 8)),),
        8,
    )
    f2_analyze(
        "f2-skew-split-bands",
        skew,
        tuple(range(len(skew))),
        (
            tuple(character for character in range(1, 8) if character.bit_count() % 2),
            tuple(character for character in range(1, 8) if not character.bit_count() % 2),
        ),
        8,
    )

    for group_order, columns in (
        (4, (1, 2, 3, 1, 2)),
        (8, (1, 2, 3, 4, 5, 6, 7)),
        (16, (1, 2, 3, 4, 5, 6, 7, 8)),
    ):
        bands = (
            tuple(
                character
                for character in range(1, group_order)
                if character.bit_count() % 2
            ),
            tuple(
                character
                for character in range(1, group_order)
                if not character.bit_count() % 2
            ),
        )
        for weight in range(1, min(4, len(columns))):
            full_values = support_xor_values(columns, weight)
            residual_modes = (
                tuple(range(len(full_values))),
                tuple(index for index in range(len(full_values)) if index % 3),
                tuple(index for index in range(len(full_values)) if index % 2 == 0),
            )
            for mode_index, residual in enumerate(residual_modes):
                if not residual:
                    continue
                f2_analyze(
                    f"f2-{group_order}-w{weight}-r{mode_index}",
                    full_values,
                    residual,
                    bands,
                    group_order,
                )


def cyclic_nonzero_kernel(prime: int, difference: int) -> int:
    return prime - 1 if difference % prime == 0 else -1


def cyclic_pair_route(fibers: Counter[int], prime: int) -> Fraction:
    numerator = 0
    for left, left_count in fibers.items():
        for right, right_count in fibers.items():
            numerator += (
                left_count
                * right_count
                * cyclic_nonzero_kernel(prime, right - left)
            )
    return Fraction(numerator, prime)


def source_analyze(
    prime: int, weight: int, residual_mode: int
) -> None:
    global SOURCE_CASES, EMISSION_CASES
    SOURCE_CASES += 1

    active_set = tuple(range(1, prime))
    supports = tuple(combinations(active_set, weight))
    full_values = [sum(support) % prime for support in supports]
    if residual_mode == 0:
        residual_indices = tuple(range(len(supports)))
    elif residual_mode == 1:
        residual_indices = tuple(index for index in range(len(supports)) if index % 3)
    else:
        residual_indices = tuple(
            index
            for index, support in enumerate(supports)
            if sum(support[::2]) % 2 == 0
        )
    if not residual_indices:
        residual_indices = (0,)

    full_fibers = Counter(full_values)
    residual_values = [full_values[index] for index in residual_indices]
    fibers = Counter(residual_values)
    M = len(supports)
    L = len(full_fibers)
    W = len(residual_values)
    SP = sum(count * count for count in fibers.values())
    f_max = max(fibers.values())

    label = f"fp{prime}-m{weight}-r{residual_mode}"
    require(
        f"{label}: nonzero character permutes Fp-star",
        all(
            sorted((character * point) % prime for point in active_set)
            == list(active_set)
            for character in active_set
        ),
    )

    # For T=F_p^*, every nonzero trace character has tau=-1.  Hence the
    # unique nonzero band is the entire nontrivial dual, whose kernel is
    # p-1 at zero and -1 away from zero.
    centered_energy = Fraction(SP) - Fraction(W * W, prime)
    pair_energy = cyclic_pair_route(fibers, prime)
    require(f"{label}: centered projection=rooted-pair", centered_energy == pair_energy)
    require(f"{label}: nonzero-band L2 contraction", centered_energy <= SP)
    require(f"{label}: SP upper by W*fmax", SP <= W * f_max)

    normalized = Fraction(L, M * M) * centered_energy
    if normalized > 1:
        EMISSION_CASES += 1
        require(
            f"{label}: violation emits heavy source fiber",
            Fraction(f_max * L, M) > 1,
        )
        require(
            f"{label}: violation emits source shift pair",
            SP - W > Fraction(M * M, L) - W >= 0,
        )

    if f_max <= 1:
        require(f"{label}: injective source residual is paid", normalized <= 1)


def run_source_cases() -> None:
    for prime in (5, 7, 11, 13):
        for weight in range(1, min(5, prime - 1)):
            for residual_mode in range(3):
                source_analyze(prime, weight, residual_mode)


def main() -> int:
    run_f2_cases()
    run_source_cases()
    require("at least one strict emission case exercised", EMISSION_CASES > 0)

    failed = [name for name, passed in CHECKS if not passed]
    print(f"abstract_cases={ABSTRACT_CASES}")
    print(f"source_cases={SOURCE_CASES}")
    print(f"strict_emission_cases={EMISSION_CASES}")
    if failed:
        print(f"RESULT: FAIL ({len(failed)}/{len(CHECKS)} checks failed)")
        return 1
    print(f"RESULT: PASS ({len(CHECKS)} checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
