#!/usr/bin/env python3
"""Fail-closed arithmetic replay for the M=212 preserve-all deletion floor."""

from __future__ import annotations

import argparse


N_CODE = 2_097_152
K = 1_048_576
M_AGREE = 1_116_047
M_LIST = 212
U_FIRST = 1_043_592
U_LAST = 1_043_916

EXPECTED_BANDS = (
    (1_043_592, 1_043_627, 123, 168, 118),
    (1_043_628, 1_043_691, 122, 167, 117),
    (1_043_692, 1_043_754, 121, 165, 116),
    (1_043_755, 1_043_815, 120, 164, 115),
    (1_043_816, 1_043_874, 119, 163, 114),
    (1_043_875, 1_043_916, 118, 161, 113),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def ceil_div(a: int, b: int) -> int:
    require(b > 0, "positive denominator")
    return (a + b - 1) // b


def rich_floor(u: int) -> int:
    residual_coordinates = N_CODE - u
    residual_agreements = M_AGREE - u
    direction_degree = K - 1 - u
    deficit_surplus = M_LIST * residual_agreements - 14 * residual_coordinates
    return ceil_div(deficit_surplus, direction_degree)


def preserve_all_floor(t: int) -> int:
    for lines in range(15, M_LIST + 1):
        if 15 * t <= lines * ((lines - 1) // 14):
            return lines
    raise ValueError("no preserve-all line floor")


def omitted_by_42(t: int) -> int:
    preserved = (42 * ((42 - 1) // 14)) // 15
    require(preserved == 5, "B=42 marked-point cap")
    return t - preserved


def bands() -> tuple[tuple[int, int, int, int, int], ...]:
    result: list[list[int]] = []
    previous = None
    for u in range(U_FIRST, U_LAST + 1):
        t = rich_floor(u)
        record = (t, preserve_all_floor(t), omitted_by_42(t))
        if record != previous:
            result.append([u, u, *record])
            previous = record
        else:
            result[-1][1] = u
    return tuple(tuple(row) for row in result)


def verify_constants() -> None:
    require(N_CODE - (K - 1) == 1_048_577, "one-flat numerator")
    require(M_AGREE - (K - 1) == 67_472, "one-flat denominator")
    require(divmod(1_048_577, 67_472) == (15, 36_497), "proper-section cap")
    require(bands() == EXPECTED_BANDS, "exact state bands")

    u = U_LAST
    residual_coordinates = N_CODE - u
    residual_agreements = M_AGREE - u
    direction_degree = K - 1 - u
    surplus = M_LIST * residual_agreements - 14 * residual_coordinates
    require(
        (residual_coordinates, residual_agreements, direction_degree, surplus)
        == (1_053_236, 72_131, 4_659, 546_468),
        "right-edge source ledger",
    )
    require(117 * 4_659 < 546_468 <= 118 * 4_659, "right-edge rich floor")
    require(160 * (159 // 14) < 15 * 118 <= 161 * (160 // 14), "right-edge line floor")


def run() -> None:
    verify_constants()
    print("RANK15_M212_PRESERVE_ALL_DELETION_FLOOR: PASS")
    print("field=2130706433 u=1043592..1043916 M=212")
    print("proper_section_cap=15 numerator=1048577 denominator=67472 remainder=36497")
    for lo, hi, t, line_floor, omitted in EXPECTED_BANDS:
        print(
            f"u={lo}..{hi} rich_direction_floor={t} "
            f"preserve_all_line_floor={line_floor} omitted_by_B42_at_least={omitted}"
        )
    print("B42 per_line_marked15_cap=2 total_marked15_cap=5")
    print("conclusion=preserve_all_source_deletion_to_B42_impossible")
    print("finite_payment=0 official_score=0/2")


def tamper_selftest() -> None:
    rejected = 0
    original = globals()["EXPECTED_BANDS"]
    for index in range(len(original)):
        changed = [list(row) for row in original]
        changed[index][2] += 1
        globals()["EXPECTED_BANDS"] = tuple(tuple(row) for row in changed)
        try:
            verify_constants()
        except ValueError:
            rejected += 1
    globals()["EXPECTED_BANDS"] = original
    require(rejected == len(original), "tamper rejection count")
    print(f"TAMPER: PASS {rejected}/{len(original)} rejected")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    if args.tamper_selftest:
        tamper_selftest()
    else:
        run()


if __name__ == "__main__":
    main()
