#!/usr/bin/env python3
"""Exact replay for the rank-16 integer-subcore residual owner.

Python standard library only. This verifier independently reconstructs the
integrated first-match baseline and the pending Q41, X175, and J48 owners,
then checks an append-only exact integer-subcore owner inside three unpaid
e15=31 cells.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
from collections import defaultdict
from dataclasses import dataclass, replace
from functools import cache
from math import comb
from pathlib import Path


P = 2_130_706_433
N = 2_097_152
K = 1_048_576
M = 1_116_047
U = 1_043_459
T = 274_854_110_496_187_592
B = 32_768
PATTERN_REFERENCE_CAP = 121_502_836_610_262

AGREEMENT_OWNER = 57_121_027_290_597_096
Q110_CAP = 904_093_061_906_432
MIXED_OWNER_ZERO = 38_578_286_420_187_472
BASELINE_PAID = 96_603_406_772_691_000
BASELINE_ALLOWANCE = 178_250_703_723_496_592

Q41_CAP = 165_153_328_111_550_464
X175_RAW_CAP = 13_253_558_241_240_832
X175_INCREMENT = 12_796_538_991_542_872
J48_CAP = 294_473_164_820_736
NEW_CHARGE = 178_244_340_267_914_072
NEW_PAID = 274_847_747_040_605_072
NEW_ALLOWANCE = 6_363_455_582_520

CORE25_CAP = 11
CORE26_CAP = 5
CORE27_CAP = 2
F27_CAP = 432_478
F26_CAP = 5_814_732
INTEGER_SUBCORE_CHARGE = 6_363_455_582_517
INTEGER_SUBCORE_PAID = T - 3
INTEGER_SUBCORE_ALLOWANCE = 3

PROFILE_1 = (31, 14, 7, 0, 0, 0)
PROFILE_2 = (31, 15, 6, 2, 1, 0)
PROFILE_3 = (31, 15, 6, 3, 1, 0)
A_PREFIX = 14_553
F_PREFIX = 109_941

BASELINE_CSV = Path(
    "experimental/data/certificates/rank16-global-c0-first-match-ledger/"
    "rank16_global_c0_residual_profiles.csv"
)
BASELINE_ROW_BYTES = 22_590
BASELINE_ROW_SHA256 = (
    "7dfa0fba111addf8ef4568821e2ce451de094c1ccef5de3468e80bd7e0373cfe"
)
BASELINE_CSV_BYTES = 22_614
BASELINE_CSV_SHA256 = (
    "83413c33cbea4f7d3cf7d6aeeb8b7a034317b443e80c1617323a94fdd13220e2"
)


class VerificationError(RuntimeError):
    """Raised when a certificate obligation fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


@dataclass(frozen=True)
class ReplayParameters:
    target_shift: int = 0
    delta_shift: int = 0
    q41_size: int = 41
    x_size: int = 175
    j_size: int = 48
    pattern_threshold_shift: int = 0
    first_match: bool = True
    lexicographic_ties: bool = True


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def enumerate_profiles() -> list[tuple[int, int, int, int, int, int]]:
    profiles: list[tuple[int, int, int, int, int, int]] = []
    for e20 in range(1):
        for e19 in range(2 * e20, 2):
            for e18 in range(2 * e19, 4):
                for e17 in range(2 * e18, 8):
                    for e16 in range(2 * e17, 16):
                        for e15 in range(2 * e16, 33):
                            profiles.append((e15, e16, e17, e18, e19, e20))
    return profiles


def dyadic_pattern_counts() -> dict[tuple[int, int, int, int, int, int], int]:
    """Count all leaf subsets by exact complete-node profile."""
    states: dict[tuple[int, tuple[int, ...]], int] = {
        (0, ()): 1,
        (1, ()): 1,
    }
    for height in range(1, 7):
        size = 1 << height
        next_states: defaultdict[tuple[int, tuple[int, ...]], int] = defaultdict(int)
        for (left_weight, left_counts), left_number in states.items():
            for (right_weight, right_counts), right_number in states.items():
                weight = left_weight + right_weight
                counts = tuple(
                    left + right
                    for left, right in zip(left_counts, right_counts)
                ) + (int(weight == size),)
                next_states[(weight, counts)] += left_number * right_number
        states = dict(next_states)

    require(
        sum(number for (weight, _), number in states.items() if weight == 32)
        == comb(64, 32),
        "weight-32 leaf census",
    )

    counts_by_profile: dict[tuple[int, int, int, int, int, int], int] = {}
    for (e15, counts), number in states.items():
        if e15 > 32:
            continue
        e16, e17, e18, e19, e20, _e21 = counts
        profile = (e15, e16, e17, e18, e19, e20)
        if (
            e16 <= 15
            and e17 <= 7
            and e18 <= 3
            and e19 <= 1
            and e20 == 0
        ):
            require(profile not in counts_by_profile, "duplicate dyadic profile")
            counts_by_profile[profile] = number
    return counts_by_profile


@cache
def subtree_states(height: int) -> dict[tuple[int, tuple[int, ...]], int]:
    """Count leaf patterns by their complete-node state at one height."""
    if height == 0:
        return {(0, ()): 1, (1, ()): 1}

    size = 1 << height
    result: defaultdict[tuple[int, tuple[int, ...]], int] = defaultdict(int)
    children = subtree_states(height - 1)
    for (left_weight, left_counts), left_number in children.items():
        for (right_weight, right_counts), right_number in children.items():
            weight = left_weight + right_weight
            counts = tuple(
                left + right for left, right in zip(left_counts, right_counts)
            ) + (int(weight == size),)
            result[(weight, counts)] += left_number * right_number
    return dict(result)


def combine_states(
    left: tuple[int, tuple[int, ...]],
    right: tuple[int, tuple[int, ...]],
    height: int,
) -> tuple[int, tuple[int, ...]]:
    weight = left[0] + right[0]
    counts = tuple(a + b for a, b in zip(left[1], right[1])) + (
        int(weight == 1 << height),
    )
    return weight, counts


def unrank_pattern(
    height: int,
    target: tuple[int, tuple[int, ...]],
    rank: int,
) -> int:
    """Unrank in recursive ordered state-pair, then child-rank order."""
    require(1 <= rank <= subtree_states(height)[target], "pattern rank")
    if height == 0:
        return target[0]

    children = subtree_states(height - 1)
    for left in sorted(children):
        for right in sorted(children):
            if combine_states(left, right, height) != target:
                continue
            block = children[left] * children[right]
            if rank > block:
                rank -= block
                continue
            left_rank, offset = divmod(rank - 1, children[right])
            left_mask = unrank_pattern(height - 1, left, left_rank + 1)
            right_mask = unrank_pattern(height - 1, right, offset + 1)
            return left_mask | (right_mask << (1 << (height - 1)))
    raise VerificationError("unreachable pattern rank")


def unrank_combination(pool: tuple[int, ...], size: int, rank: int) -> tuple[int, ...]:
    """Unrank a fixed-size combination in lexicographic tuple order."""
    require(1 <= rank <= comb(len(pool), size), "combination rank")
    selected: list[int] = []
    start = 0
    for remaining in range(size, 0, -1):
        for index in range(start, len(pool)):
            block = comb(len(pool) - index - 1, remaining - 1)
            if rank > block:
                rank -= block
                continue
            selected.append(pool[index])
            start = index + 1
            break
    return tuple(selected)


def integer_pair_ledger(universe: int, forbidden_r: int) -> dict[str, int]:
    agreement_residual = M - 31 * B
    intersection = K - 1 - 31 * B
    quotient, remainder = divmod(forbidden_r * agreement_residual, universe)
    lower = universe * comb(quotient, 2) + remainder * quotient
    upper = comb(forbidden_r, 2) * intersection
    return {
        "universe": universe,
        "forbidden_r": forbidden_r,
        "quotient": quotient,
        "remainder": remainder,
        "lower": lower,
        "upper": upper,
        "margin": lower - upper,
    }


def integer_subcore_values(values: dict[str, object]) -> dict[str, object]:
    pattern_counts = values["pattern_counts"]
    core25 = integer_pair_ledger(8 * B, 12)
    core26 = integer_pair_ledger(7 * B, 6)
    core27 = integer_pair_ledger(6 * B, 3)

    base_incidence = CORE25_CAP * comb(33, 8)
    f27_deficit = (3 * comb(33, 10) + 299) // 300
    f26_deficit = (comb(33, 9) + 24) // 25
    f27_cap = (base_incidence - f27_deficit) // comb(27, 2)
    f26_cap = (base_incidence - f26_deficit) // 26

    cell1 = pattern_counts[PROFILE_1] * f27_cap
    cell2 = pattern_counts[PROFILE_2] * f27_cap
    whole_charge = cell1 + cell2
    profile3_whole = pattern_counts[PROFILE_3] * f26_cap
    pattern_prefix_charge = A_PREFIX * f26_cap
    fixed_f_charge = F_PREFIX * CORE26_CAP
    subcell_charge = pattern_prefix_charge + fixed_f_charge
    total_charge = whole_charge + subcell_charge

    target_state = (PROFILE_3[0], PROFILE_3[1:] + (0,))
    pattern_mask = unrank_pattern(6, target_state, A_PREFIX + 1)
    first_unpaid_a = tuple(i for i in range(64) if pattern_mask >> i & 1)
    complement = tuple(i for i in range(64) if not (pattern_mask >> i & 1))
    first_unpaid_f = unrank_combination(complement, 26, F_PREFIX + 1)

    johnson_rank = {
        (profile, f64): rank
        for rank, (_cap, profile, f64, _vals, _sets) in enumerate(
            values["johnson_rows"], 1
        )
    }

    return {
        "core25": core25,
        "core26": core26,
        "core27": core27,
        "f27_deficit": f27_deficit,
        "f26_deficit": f26_deficit,
        "f27_cap": f27_cap,
        "f26_cap": f26_cap,
        "cell1": cell1,
        "cell2": cell2,
        "whole_charge": whole_charge,
        "profile3_whole": profile3_whole,
        "pattern_prefix_charge": pattern_prefix_charge,
        "fixed_f_charge": fixed_f_charge,
        "subcell_charge": subcell_charge,
        "total_charge": total_charge,
        "paid": values["new_paid"] + total_charge,
        "allowance": T - values["new_paid"] - total_charge,
        "first_unpaid_a": first_unpaid_a,
        "first_unpaid_f": first_unpaid_f,
        "johnson_ranks": {
            "profile1_f27": johnson_rank[(PROFILE_1, 27)],
            "profile2_f27": johnson_rank[(PROFILE_2, 27)],
            "profile3_f26": johnson_rank[(PROFILE_3, 26)],
        },
    }


def canonical_profile_csv(
    profiles: list[tuple[int, int, int, int, int, int]],
) -> bytes:
    rows = ["e15,e16,e17,e18,e19,e20\n"]
    rows.extend(",".join(str(value) for value in profile) + "\n" for profile in profiles)
    return "".join(rows).encode("ascii")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def mixed_shadow(capacity_used: int, shadow_universe: int, paired: int) -> int:
    return paired + capacity_used + (shadow_universe - paired - capacity_used) // 29


def johnson_parameters(e: int, f: int) -> tuple[int, int, int, int, int] | None:
    agreement_residual = M - e * B
    universe = (64 - e - f) * B
    intersection = K - 1 - e * B
    denominator = agreement_residual**2 - universe * intersection
    if denominator <= 0:
        return None
    numerator = universe * (agreement_residual - intersection)
    local_cap = numerator // denominator
    return agreement_residual, universe, intersection, denominator, local_cap


def tie_key(cap: int, profile: tuple[int, ...], extra: tuple[int, ...], lex: bool) -> tuple:
    if lex:
        return (cap, profile, extra)
    return (-cap, tuple(-value for value in profile), tuple(-value for value in extra))


def profile_ledger_bytes(rows: list[dict[str, object]]) -> bytes:
    output = io.StringIO(newline="")
    fields = [
        "e15", "e16", "e17", "e18", "e19", "e20", "pattern_count",
        "q110", "q41_rank", "q41_selected", "x28_nonpaired_sets",
        "x28_cap", "x175_rank", "x175_selected",
    ]
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("ascii")


def johnson_ledger_bytes(rows: list[dict[str, object]]) -> bytes:
    output = io.StringIO(newline="")
    fields = [
        "rank", "e15", "e16", "e17", "e18", "e19", "e20", "f64",
        "agreement_residual", "universe", "intersection", "denominator",
        "local_cap", "pattern_count", "label_sets", "cell_cap", "selected",
    ]
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("ascii")


def replay(params: ReplayParameters = ReplayParameters()) -> dict[str, object]:
    target = T + params.target_shift
    delta = N - 2 * M + K - 1 + params.delta_shift
    shadow_universe = comb(64, 28)
    paired = comb(32, 14)

    profiles = enumerate_profiles()
    pattern_counts = dyadic_pattern_counts()
    require(set(pattern_counts) == set(profiles), "dyadic census/profile mismatch")

    threshold = PATTERN_REFERENCE_CAP + params.pattern_threshold_shift
    q110 = {
        profile
        for profile in profiles
        if profile[0] == 32 and pattern_counts[profile] <= threshold
    }
    baseline_profiles = [profile for profile in profiles if profile not in q110]
    baseline_csv = canonical_profile_csv(baseline_profiles)
    baseline_rows = baseline_csv.split(b"\n", 1)[1]

    q41_candidates = sorted(
        (profile for profile in baseline_profiles if profile[0] == 32),
        key=lambda profile: tie_key(pattern_counts[profile], profile, (), params.lexicographic_ties),
    )
    q41 = q41_candidates[: params.q41_size]
    q41_set = set(q41)
    q41_cap = sum(pattern_counts[profile] for profile in q41)
    q41_next = q41_candidates[params.q41_size]
    q41_next_cap = pattern_counts[q41_next]
    q41_42_cap = q41_cap + q41_next_cap

    residual_profiles = [profile for profile in baseline_profiles if profile not in q41_set]

    x_rows: list[tuple[int, tuple[int, int, int, int, int, int], int]] = []
    for profile in residual_profiles:
        e15, e16, _e17, _e18, _e19, _e20 = profile
        label_sets = comb(64 - e15, 28) - comb(32 - e15 + e16, 14)
        require(label_sets >= 0, "negative nonpaired label-set count")
        cell_cap = pattern_counts[profile] * label_sets
        x_rows.append((cell_cap, profile, label_sets))
    x_rows.sort(key=lambda row: tie_key(row[0], row[1], (), params.lexicographic_ties))
    x_selected = x_rows[: params.x_size]
    x_raw = sum(row[0] for row in x_selected)
    x_next = x_rows[params.x_size]
    mixed_zero = mixed_shadow(0, shadow_universe, paired)
    mixed_x = mixed_shadow(x_raw, shadow_universe, paired)
    mixed_x_next = mixed_shadow(x_raw + x_next[0], shadow_universe, paired)
    x_increment = mixed_x - mixed_zero
    x_next_increment = mixed_x_next - mixed_x

    johnson_rows: list[tuple[int, tuple[int, int, int, int, int, int], int, tuple[int, int, int, int, int], int]] = []
    for profile in residual_profiles:
        e15 = profile[0]
        for f64 in range(0, 28):
            values = johnson_parameters(e15, f64)
            if values is None:
                continue
            label_sets = comb(64 - e15, f64)
            cell_cap = pattern_counts[profile] * label_sets * values[-1]
            johnson_rows.append((cell_cap, profile, f64, values, label_sets))
    johnson_rows.sort(
        key=lambda row: tie_key(row[0], row[1], (row[2],), params.lexicographic_ties)
    )
    j_selected = johnson_rows[: params.j_size]
    j_cap = sum(row[0] for row in j_selected)
    j_next = johnson_rows[params.j_size]

    new_charge = q41_cap + x_increment + j_cap
    new_paid = BASELINE_PAID + new_charge
    new_allowance = target - new_paid

    q41_rank = {profile: rank for rank, profile in enumerate(q41_candidates, 1)}
    x_rank = {profile: rank for rank, (_cap, profile, _sets) in enumerate(x_rows, 1)}
    x_selected_profiles = {profile for _cap, profile, _sets in x_selected}
    profile_rows: list[dict[str, object]] = []
    for profile in profiles:
        q110_value = int(profile in q110)
        if profile in q110:
            q41_rank_value: int | str = ""
            x_sets_value: int | str = ""
            x_cap_value: int | str = ""
            x_rank_value: int | str = ""
        else:
            q41_rank_value = q41_rank.get(profile, "")
            if profile in q41_set:
                x_sets_value = ""
                x_cap_value = ""
                x_rank_value = ""
            else:
                e15, e16 = profile[0], profile[1]
                x_sets_value = comb(64 - e15, 28) - comb(32 - e15 + e16, 14)
                x_cap_value = pattern_counts[profile] * int(x_sets_value)
                x_rank_value = x_rank[profile]
        profile_rows.append(
            {
                "e15": profile[0], "e16": profile[1], "e17": profile[2],
                "e18": profile[3], "e19": profile[4], "e20": profile[5],
                "pattern_count": pattern_counts[profile], "q110": q110_value,
                "q41_rank": q41_rank_value,
                "q41_selected": int(profile in q41_set),
                "x28_nonpaired_sets": x_sets_value, "x28_cap": x_cap_value,
                "x175_rank": x_rank_value,
                "x175_selected": int(profile in x_selected_profiles),
            }
        )

    johnson_ledger_rows: list[dict[str, object]] = []
    for rank, (cell_cap, profile, f64, values, label_sets) in enumerate(johnson_rows, 1):
        agreement_residual, universe, intersection, denominator, local_cap = values
        johnson_ledger_rows.append(
            {
                "rank": rank, "e15": profile[0], "e16": profile[1],
                "e17": profile[2], "e18": profile[3], "e19": profile[4],
                "e20": profile[5], "f64": f64,
                "agreement_residual": agreement_residual, "universe": universe,
                "intersection": intersection, "denominator": denominator,
                "local_cap": local_cap, "pattern_count": pattern_counts[profile],
                "label_sets": label_sets, "cell_cap": cell_cap,
                "selected": int(rank <= params.j_size),
            }
        )

    profile_ledger = profile_ledger_bytes(profile_rows)
    johnson_ledger = johnson_ledger_bytes(johnson_ledger_rows)

    values = {
        "params": params,
        "target": target,
        "delta": delta,
        "shadow_universe": shadow_universe,
        "paired": paired,
        "profiles": profiles,
        "pattern_counts": pattern_counts,
        "q110": q110,
        "baseline_profiles": baseline_profiles,
        "baseline_csv": baseline_csv,
        "baseline_rows": baseline_rows,
        "q41_candidates": q41_candidates,
        "q41": q41,
        "q41_cap": q41_cap,
        "q41_next": q41_next,
        "q41_next_cap": q41_next_cap,
        "q41_42_cap": q41_42_cap,
        "residual_profiles": residual_profiles,
        "x_rows": x_rows,
        "x_selected": x_selected,
        "x_raw": x_raw,
        "x_next": x_next,
        "mixed_zero": mixed_zero,
        "mixed_x": mixed_x,
        "x_increment": x_increment,
        "x_next_increment": x_next_increment,
        "johnson_rows": johnson_rows,
        "j_selected": j_selected,
        "j_cap": j_cap,
        "j_next": j_next,
        "new_charge": new_charge,
        "new_paid": new_paid,
        "new_allowance": new_allowance,
        "profile_ledger": profile_ledger,
        "johnson_ledger": johnson_ledger,
    }
    values["integer_subcore"] = integer_subcore_values(values)
    return values


def verify(values: dict[str, object], repository_root: Path) -> None:
    params = values["params"]
    require(isinstance(params, ReplayParameters), "parameter record")
    require(params.first_match, "first-match owner order disabled")
    require(params.lexicographic_ties, "lexicographic tie-breaking disabled")
    require(is_prime(P) and P - 1 == 1016 * N, "deployed field/subgroup")
    require(values["target"] == T, "target")
    require(values["delta"] == 913_633, "canonical complement intersection")
    require(27 * B <= int(values["delta"]) < 28 * B, "28-shadow uniqueness")
    require(values["shadow_universe"] == 1_118_770_292_985_239_888, "shadow universe")
    require(values["paired"] == 471_435_600, "paired shadows")
    require(values["mixed_zero"] == MIXED_OWNER_ZERO, "integrated mixed owner")

    profiles = values["profiles"]
    require(isinstance(profiles, list) and len(profiles) == 1_792, "profile census")
    require(len(values["pattern_counts"]) == 1_792, "pattern census")
    require(len(values["q110"]) == 110, "Q110 profile count")
    require(
        sum(values["pattern_counts"][profile] for profile in values["q110"]) == Q110_CAP,
        "Q110 exact cap",
    )
    require(len(values["baseline_profiles"]) == 1_682, "#838 residual profiles")
    require(len(values["baseline_rows"]) == BASELINE_ROW_BYTES, "#838 row-stream bytes")
    require(digest(values["baseline_rows"]) == BASELINE_ROW_SHA256, "#838 row-stream digest")
    require(len(values["baseline_csv"]) == BASELINE_CSV_BYTES, "#838 complete CSV bytes")
    require(digest(values["baseline_csv"]) == BASELINE_CSV_SHA256, "#838 complete CSV digest")
    integrated = (repository_root / BASELINE_CSV).read_bytes()
    require(integrated == values["baseline_csv"], "integrated #838 CSV byte mismatch")

    require(len(values["q41_candidates"]) == 56, "Q41 candidate count")
    require(len(values["q41"]) == 41, "Q41 selected count")
    require(values["q41_cap"] == Q41_CAP, "Q41 cap")
    require(values["q41_next"] == (32, 10, 0, 0, 0, 0), "Q41 frontier profile")
    require(values["q41_next_cap"] == 21_719_537_074_307_072, "Q41 frontier cap")
    require(values["q41_42_cap"] == 186_872_865_185_857_536, "Q41 42-profile cap")
    require(len(values["residual_profiles"]) == 1_641, "post-Q41 profile count")

    require(len(values["x_selected"]) == 175, "X175 selected count")
    require(values["x_raw"] == X175_RAW_CAP, "X175 raw cap")
    require(values["mixed_x"] == 51_374_825_411_730_344, "M union X175 cap")
    require(values["x_increment"] == X175_INCREMENT, "X175 incremental charge")
    x_next = values["x_next"]
    require(x_next[1] == (31, 13, 6, 2, 1, 0), "X175 frontier profile")
    require(x_next[0] == 423_894_739_968_000, "X175 frontier raw cap")
    require(values["x_next_increment"] == 409_277_679_969_103, "X175 frontier increment")
    require(
        Q41_CAP + X175_INCREMENT <= BASELINE_ALLOWANCE
        < Q41_CAP + X175_INCREMENT + int(values["x_next_increment"]),
        "X175 maximal prefix",
    )

    require(len(values["johnson_rows"]) == 1_696, "positive Johnson-cell pool")
    require(len(values["j_selected"]) == 48, "J48 selected count")
    require(sum(1 for row in values["j_selected"] if row[2] == 27) == 38, "J48 f=27 split")
    require(sum(1 for row in values["j_selected"] if row[2] == 26) == 10, "J48 f=26 split")
    require(values["j_cap"] == J48_CAP, "J48 cap")
    j_next = values["j_next"]
    require(j_next[1] == (30, 15, 5, 2, 1, 0) and j_next[2] == 27, "J48 frontier cell")
    require(j_next[3][-1] == 5, "J48 frontier local cap")
    require(j_next[0] == 19_087_738_306_560, "J48 frontier total cap")

    expected_j = {
        (28, 27): (198_543, 294_912, 131_071, 764_912_097, 26),
        (29, 27): (165_775, 262_144, 98_303, 1_711_808_993, 10),
        (30, 27): (133_007, 229_376, 65_535, 2_658_705_889, 5),
        (31, 27): (100_239, 196_608, 32_767, 3_605_602_785, 3),
        (30, 26): (133_007, 262_144, 65_535, 511_255_009, 34),
        (31, 26): (100_239, 229_376, 32_767, 2_531_893_729, 6),
    }
    for key, expected in expected_j.items():
        require(johnson_parameters(*key) == expected, f"Johnson constants {key}")

    require(values["new_charge"] == NEW_CHARGE, "new owner charge")
    require(values["new_paid"] == NEW_PAID, "new paid subtotal")
    require(values["new_allowance"] == NEW_ALLOWANCE, "new residual allowance")
    quotient, remainder = divmod(int(values["new_allowance"]), 1_641)
    require((quotient, remainder) == (3_877_791_336, 144), "truncated-profile division")
    require(
        int(values["new_allowance"]) < int(j_next[0]),
        "next Johnson cell should not fit",
    )

    require(len(set(values["q110"]).intersection(values["q41"])) == 0, "Q110/Q41 overlap")
    x_profiles = {row[1] for row in values["x_selected"]}
    require(not x_profiles.intersection(values["q41"]), "Q41/X175 overlap")
    require(len(x_profiles) == len(values["x_selected"]), "X175 duplicate profile cell")
    require(all(row[2] <= 27 for row in values["j_selected"]), "J48 lower-f scope")

    subcore = values["integer_subcore"]
    expected_core_rows = (
        (subcore["core25"], 262_144, 12, 4, 154_292, 2_190_032, 2_162_622, 27_410),
        (subcore["core26"], 229_376, 6, 2, 142_682, 514_740, 491_505, 23_235),
        (subcore["core27"], 196_608, 3, 1, 104_109, 104_109, 98_301, 5_808),
    )
    for row, universe, forbidden_r, quotient, remainder, lower, upper, margin in expected_core_rows:
        require(
            row == {
                "universe": universe,
                "forbidden_r": forbidden_r,
                "quotient": quotient,
                "remainder": remainder,
                "lower": lower,
                "upper": upper,
                "margin": margin,
            },
            f"integer core row {universe}",
        )
        require(margin > 0, f"strict integer contradiction {universe}")

    require(subcore["f27_deficit"] == 925_611, "f27 modular deficit")
    require(subcore["f26_deficit"] == 1_542_684, "f26 modular deficit")
    require(subcore["f27_cap"] == F27_CAP, "fixed-A f27 cap")
    require(subcore["f26_cap"] == F26_CAP, "fixed-A f26 cap")
    require(values["pattern_counts"][PROFILE_1] == 6_684_672, "profile 1 patterns")
    require(values["pattern_counts"][PROFILE_2] == 7_833_600, "profile 2 patterns")
    require(values["pattern_counts"][PROFILE_3] == 783_360, "profile 3 patterns")
    require(subcore["cell1"] == 2_890_973_577_216, "profile 1 charge")
    require(subcore["cell2"] == 3_387_859_660_800, "profile 2 charge")
    require(subcore["whole_charge"] == 6_278_833_238_016, "whole-cell charge")
    require(subcore["profile3_whole"] == 4_555_028_459_520, "frontier whole cap")
    require(subcore["pattern_prefix_charge"] == 84_621_794_796, "A prefix charge")
    require(subcore["fixed_f_charge"] == 549_705, "fixed-F prefix charge")
    require(subcore["subcell_charge"] == 84_622_344_501, "subcell charge")
    require(subcore["total_charge"] == INTEGER_SUBCORE_CHARGE, "total new charge")
    require(subcore["paid"] == INTEGER_SUBCORE_PAID, "expanded paid subtotal")
    require(subcore["allowance"] == INTEGER_SUBCORE_ALLOWANCE, "remaining allowance")
    require(
        subcore["johnson_ranks"]
        == {"profile1_f27": 51, "profile2_f27": 53, "profile3_f26": 50},
        "post-J48 cell ranks",
    )
    require(all(profile[0] == 31 and profile[1] <= 15 for profile in (PROFILE_1, PROFILE_2, PROFILE_3)), "outside D")
    require(not {PROFILE_1, PROFILE_2, PROFILE_3}.intersection(values["q41"]), "outside Q41")
    require(
        subcore["first_unpaid_a"]
        == (6, 7, 22, 23, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 62),
        "first unpaid agreement pattern",
    )
    require(
        subcore["first_unpaid_f"]
        == (0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 16, 17, 19, 20, 24, 26, 28, 29, 30, 58, 59, 60, 61, 63),
        "first unpaid complement bucket",
    )


def render(values: dict[str, object]) -> list[str]:
    subcore = values["integer_subcore"]
    c25 = subcore["core25"]
    c26 = subcore["core26"]
    c27 = subcore["core27"]
    return [
        "RANK16_INTEGER_SUBCORE_OWNER: PASS",
        f"replay_861=paid:{values['new_paid']} residual:{values['new_allowance']} profiles:{len(values['residual_profiles'])}",
        f"core25=g:25 cap:{CORE25_CAP} N:{c25['universe']} forbidden_r:{c25['forbidden_r']} q:{c25['quotient']} rem:{c25['remainder']} pair_lower:{c25['lower']} pair_upper:{c25['upper']} margin:{c25['margin']}",
        f"core26=g:26 cap:{CORE26_CAP} N:{c26['universe']} forbidden_r:{c26['forbidden_r']} q:{c26['quotient']} rem:{c26['remainder']} pair_lower:{c26['lower']} pair_upper:{c26['upper']} margin:{c26['margin']}",
        f"core27=g:27 cap:{CORE27_CAP} N:{c27['universe']} forbidden_r:{c27['forbidden_r']} q:{c27['quotient']} rem:{c27['remainder']} pair_lower:{c27['lower']} pair_upper:{c27['upper']} margin:{c27['margin']}",
        f"incidence_dual=f27_deficit:{subcore['f27_deficit']} per_A_f27:{subcore['f27_cap']} f26_deficit:{subcore['f26_deficit']} per_A_f26:{subcore['f26_cap']}",
        f"IS2_1=profile:{PROFILE_1} f64:27 patterns:{values['pattern_counts'][PROFILE_1]} per_A:{subcore['f27_cap']} cap:{subcore['cell1']}",
        f"IS2_2=profile:{PROFILE_2} f64:27 patterns:{values['pattern_counts'][PROFILE_2]} per_A:{subcore['f27_cap']} cap:{subcore['cell2']}",
        f"IS3_frontier=profile:{PROFILE_3} f64:26 patterns:{values['pattern_counts'][PROFILE_3]} per_A:{subcore['f26_cap']} cap:{subcore['profile3_whole']}",
        f"new_charge={subcore['whole_charge']} paid_subtotal:{values['new_paid'] + subcore['whole_charge']} residual:{T - values['new_paid'] - subcore['whole_charge']}",
        f"subcell_prefix=A:{A_PREFIX} F:{F_PREFIX} charge:{subcore['subcell_charge']} total_new_charge:{subcore['total_charge']} paid_subtotal:{subcore['paid']} residual:{subcore['allowance']}",
        f"first_unpaid_bucket=profile:{PROFILE_3} f64:26 A_rank:{A_PREFIX + 1} A:{subcore['first_unpaid_a']} F_rank:{F_PREFIX + 1} F:{subcore['first_unpaid_f']}",
        "owner_order=D->Q110->M->Q41->X175->J48->IS2->A14553->F109941",
        "scope=deployed base field; one arbitrary normalized received word",
        "RESULT=PASS",
    ]


def tamper_selftest(repository_root: Path) -> None:
    base = ReplayParameters()
    mutations = (
        replace(base, target_shift=1),
        replace(base, delta_shift=1),
        replace(base, q41_size=42),
        replace(base, x_size=176),
        replace(base, j_size=49),
        replace(base, pattern_threshold_shift=1_000_000_000_000_000),
        replace(base, first_match=False),
        replace(base, lexicographic_ties=False),
    )
    caught = 0
    for mutation in mutations:
        try:
            mutated = replay(mutation)
            verify(mutated, repository_root)
        except (VerificationError, IndexError):
            caught += 1
    require(caught == len(mutations), "tamper self-test")
    print(f"TAMPER_SELFTEST: PASS ({caught}/{len(mutations)} rejected)")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-profile-ledger", type=Path)
    parser.add_argument("--write-johnson-ledger", type=Path)
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()

    repository_root = Path(__file__).resolve().parents[2]
    if args.tamper_selftest:
        tamper_selftest(repository_root)
        return

    values = replay()
    verify(values, repository_root)
    if args.write_profile_ledger:
        args.write_profile_ledger.parent.mkdir(parents=True, exist_ok=True)
        args.write_profile_ledger.write_bytes(values["profile_ledger"])
    if args.write_johnson_ledger:
        args.write_johnson_ledger.parent.mkdir(parents=True, exist_ok=True)
        args.write_johnson_ledger.write_bytes(values["johnson_ledger"])
    print("\n".join(render(values)))


if __name__ == "__main__":
    main()
