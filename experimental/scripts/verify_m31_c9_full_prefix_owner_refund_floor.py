#!/usr/bin/env python3
"""Replay the exact M31 C9 full-prefix owner-refund floor certificate.

Python is a replay tool only.  The packet's proof validation is the stdlib-only
Lean package experimental/lean/sidon_effective_image.
"""

from __future__ import annotations

import argparse
import copy
import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = (
    ROOT
    / "experimental"
    / "data"
    / "certificates"
    / "m31-c9-full-prefix-owner-refund-floor"
    / "m31_c9_full_prefix_owner_refund_floor.json"
)


def ceil_div(numerator: int, denominator: int) -> int:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    return (numerator + denominator - 1) // denominator


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate(packet: dict[str, Any]) -> None:
    require(packet["schema"] == "m31-c9-full-prefix-owner-refund-floor/v1", "schema")
    require(packet["status"] == "CONDITIONAL_ON_NAMED_INPUT", "status")

    row = packet["row"]
    denominators = packet["denominators"]
    normalization = packet["image_normalization"]
    owner = packet["earlier_owner_floor"]
    ledger = packet["ledger_cut"]
    falsifier = packet["falsifier"]

    q_gen = 2**31 - 1
    q_list = q_gen**4
    require(denominators["q_gen"] == q_gen, "q_gen")
    require(int(denominators["q_list"]) == q_list, "q_list")
    require(denominators["q_line"].startswith("NOT_USED"), "q_line separation")
    require(denominators["q_chal"].startswith("NOT_USED"), "q_chal separation")

    n = 2**21
    k = 2**20
    a_plus = 1_116_023
    w = a_plus - k
    require(row == {
        "name": "Mersenne-31 list",
        "n": n,
        "k": k,
        "a_plus": a_plus,
        "w": w,
    }, "row constants")

    row_budget = q_list // 2**100
    require(row_budget == 16_777_215, "row budget arithmetic")
    require(ledger["row_budget"] == row_budget, "row budget certificate")

    # The million-bit full-slice ceiling is imported from `prop:q-exact-target`.
    # Recomputing binomial(2^21, 1116023) is intentionally not part of this
    # small replay verifier; the exact owner-refund cut below is independently
    # recomputed from its 1023-point quotient row.
    require(normalization["full_slice_average_ceil"] == 1_993_678, "full average source value")

    choose_n = owner["fixed_remainder_choose_n"]
    choose_k = owner["fixed_remainder_choose_k"]
    quotient_depth = owner["quotient_prefix_depth"]
    owner_floor = ceil_div(math.comb(choose_n, choose_k), q_gen**quotient_depth)
    require(owner_floor == 6_796_405, "c=2048 owner floor replay")
    require(owner["value"] == owner_floor, "owner floor certificate")

    residual_allowance = row_budget - owner_floor
    full_prefix_residual_cap = residual_allowance - owner_floor
    full_budget_plus_owner = row_budget + owner_floor
    require(residual_allowance == 9_980_810, "residual allowance")
    require(full_prefix_residual_cap == 3_184_405, "full-prefix residual cap")
    require(full_budget_plus_owner == 23_573_620, "double-charge total")
    require(
        ledger["residual_allowance_after_owner_payment"] == residual_allowance,
        "residual allowance certificate",
    )
    require(
        ledger["full_prefix_residual_cap_if_owner_floor_is_still_inside_the_fiber"]
        == full_prefix_residual_cap,
        "full-prefix residual cap certificate",
    )
    require(ledger["owner_refund_gap"] == owner_floor, "owner refund gap")
    require(
        ledger["full_budget_plus_separate_owner_charge"] == full_budget_plus_owner,
        "double-charge certificate",
    )

    falsifier_residual = full_prefix_residual_cap + 1
    require(falsifier["earlier_owned_prefix_supports_at_least"] == owner_floor, "falsifier owner")
    require(falsifier["residual_prefix_supports_at_least"] == falsifier_residual, "falsifier residual")
    require(owner_floor + falsifier_residual > residual_allowance, "falsifier inequality")


def tamper_selftest(packet: dict[str, Any]) -> None:
    tampered = copy.deepcopy(packet)
    tampered["ledger_cut"]["full_prefix_residual_cap_if_owner_floor_is_still_inside_the_fiber"] += 1
    try:
        validate(tampered)
    except AssertionError:
        return
    raise AssertionError("tamper self-test failed closed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()

    packet = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    validate(packet)
    if args.tamper_selftest:
        tamper_selftest(packet)
    print(
        "PASS: M31 C9 owner-refund floor "
        "B*=16777215, owner=6796405, residual=9980810, full-cap=3184405"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
