#!/usr/bin/env python3
"""Fail-closed arithmetic replay for the conditional D=73 exclusion."""

from __future__ import annotations

import argparse
import hashlib
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / (
    "experimental/data/certificates/"
    "rank15-m212-q14-b42-d69-d72-arrangement-exclusion/"
    "verify_rank15_m212_q14_b42_d69_d73_arrangement_profiles.expected.txt"
)
SOURCE_SHA256 = "facf1236a5517763ee4e8531515cae071f597d1d4a9432473f4621ffa9f4e9e2"
OPEN_D73 = (
    "D=73 n3=122 n4=1 n5=1 n6=1 n7=11 n11=1 n15=1 "
    "route=OPEN_D73"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def balanced_pair_min(total: int, cells: int) -> int:
    q, r = divmod(total, cells)
    return (cells - r) * comb(q, 2) + r * comb(q + 1, 2)


def verify_record(record: dict[str, int]) -> None:
    expected = {
        "points": 27,
        "anchor": 10,
        "selected": 8,
        "secant": 6,
        "six_secants": 11,
    }
    require(record == expected, "deployed D73 witness record")

    complement = record["points"] - record["anchor"]
    incidence = record["selected"] * (record["secant"] - 1)
    lower = balanced_pair_min(incidence, complement)
    upper = comb(record["selected"], 2)
    require((complement, incidence, lower, upper) == (17, 40, 29, 28), "29>28 ledger")
    require(lower > upper, "anchor-trace contradiction")

    all_incidence = record["six_secants"] * (record["secant"] - 1)
    all_lower = balanced_pair_min(all_incidence, complement)
    all_upper = comb(record["six_secants"], 2)
    require((all_incidence, all_lower, all_upper) == (55, 63, 55), "63>55 audit")


def verify_source() -> None:
    data = SOURCE.read_bytes()
    require(hashlib.sha256(data).hexdigest() == SOURCE_SHA256, "integrated source pin")
    lines = data.decode("ascii").splitlines()
    require(lines.count(OPEN_D73) == 1, "unique OPEN_D73 record")


def verify_spectrum() -> None:
    spectrum = {10: 1, 6: 11, 5: 1, 4: 1, 3: 1, 2: 122, 1: 73}
    require(sum(spectrum.values()) == 210, "occupied-line count")
    require(sum(k * n for k, n in spectrum.items()) == 405, "incidence count")
    require(sum(comb(k, 2) * n for k, n in spectrum.items()) == 351, "pair count")


def run() -> None:
    verify_source()
    verify_spectrum()
    verify_record({"points": 27, "anchor": 10, "selected": 8, "secant": 6, "six_secants": 11})
    print("RANK15_D73_ANCHOR_TRACE: PASS")
    print("source_open_profile=D73")
    print("spectrum=blocks:210 incidences:405 pairs:351")
    print("anchor=10 selected=8 complement=17 incidence=40 lower_pairs=29 upper_pairs=28")
    print("all_six_secants=11 incidence=55 lower_pairs=63 upper_pairs=55")
    print("conditional_excluded_D=73 next_conditional_D=74")
    print("finite_payment=0 official_score=0/2")


def tamper_selftest() -> None:
    base = {"points": 27, "anchor": 10, "selected": 8, "secant": 6, "six_secants": 11}
    rejected = 0
    for key in base:
        changed = dict(base)
        changed[key] += 1
        try:
            verify_record(changed)
        except ValueError:
            rejected += 1
    require(rejected == len(base), "tamper rejection count")
    print(f"TAMPER: PASS {rejected}/{len(base)} rejected")


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
