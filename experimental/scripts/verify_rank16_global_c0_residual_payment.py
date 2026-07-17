#!/usr/bin/env python3
"""Exact replay for the rank-16 global c=0 residual payment.

Python standard library only.  This verifier independently reconstructs the
integrated first-match baseline and the deterministic Q41, X175, and J48
owners.  It writes reviewable profile and Johnson-cell ledgers on request.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
from collections import defaultdict
from dataclasses import dataclass, replace
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

    return {
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


def render(values: dict[str, object]) -> list[str]:
    x_next = values["x_next"]
    j_next = values["j_next"]
    quotient, remainder = divmod(int(values["new_allowance"]), 1_641)
    return [
        "RANK16_GLOBAL_C0_RESIDUAL_PAYMENT: PASS",
        f"baseline_profiles={len(values['baseline_profiles'])} row_stream_bytes={len(values['baseline_rows'])} row_stream_sha256={digest(values['baseline_rows'])}",
        f"baseline_csv_bytes={len(values['baseline_csv'])} baseline_csv_sha256={digest(values['baseline_csv'])}",
        f"Q41=count:{len(values['q41'])} cap:{values['q41_cap']} next:{values['q41_next']} next_cap:{values['q41_next_cap']}",
        f"X175=count:{len(values['x_selected'])} raw:{values['x_raw']} joint_M_X:{values['mixed_x']} increment:{values['x_increment']}",
        f"X176_frontier={x_next[1]} raw_cap:{x_next[0]} increment:{values['x_next_increment']}",
        f"J48=count:{len(values['j_selected'])} split_f27:{sum(1 for row in values['j_selected'] if row[2] == 27)} split_f26:{sum(1 for row in values['j_selected'] if row[2] == 26)} cap:{values['j_cap']}",
        f"J49_frontier={j_next[1]},f64={j_next[2]} local_cap:{j_next[3][-1]} total_cap:{j_next[0]}",
        f"new_charge={values['new_charge']} paid_subtotal={values['new_paid']} residual={values['new_allowance']}",
        f"truncated_profiles={len(values['residual_profiles'])} uniform_cap={quotient} remainder={remainder} forced_at_T_plus_1={quotient + 1}",
        f"profile_owner_ledger_bytes={len(values['profile_ledger'])} sha256={digest(values['profile_ledger'])}",
        f"johnson_cell_ledger_bytes={len(values['johnson_ledger'])} sha256={digest(values['johnson_ledger'])}",
        "owner_order=D->Q110->M->Q41->X175->J48",
        "scope=deployed base-field row; one arbitrary normalized received word; no generator/ray multiplication",
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
