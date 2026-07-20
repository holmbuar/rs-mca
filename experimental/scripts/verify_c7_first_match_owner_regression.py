#!/usr/bin/env python3
"""Finite replay for the C7 first-match owner regression.

This script checks only the finite owner/payment consequence represented in
AsymptoticSpine.C7OwnerRegression.  The actual affine-Steiner field algebra is
owned by the existing affine_steiner_quotient_owner packet.
"""

from __future__ import annotations

from pathlib import Path


def require(condition: bool, message: str) -> None:
    """Fail closed even when Python is run with optimization enabled."""
    if not condition:
        raise AssertionError(message)


def first_match(cells: list[list[int]]) -> list[list[int]]:
    paid: set[int] = set()
    leaves: list[list[int]] = []
    for cell in cells:
        leaf: list[int] = []
        for slope in cell:
            if slope not in paid and slope not in leaf:
                leaf.append(slope)
        leaves.append(leaf)
        paid.update(leaf)
    return leaves


def main() -> None:
    raw = [[7], [7]]
    leaves = first_match(raw)
    require(leaves == [[7], []], f"unexpected first-match leaves: {leaves!r}")

    raw_assigned = [7] + [7]
    require(
        len(raw_assigned) != len(set(raw_assigned)),
        "raw C1/C7 assignment unexpectedly has no duplicate slope",
    )

    corrected_assigned = [7]
    require(
        len(corrected_assigned) == len(set(corrected_assigned)) == 1,
        "corrected first-match assignment is not one distinct slope",
    )

    c1_ray_budget = 1
    c7_assigned_ray_budget = 0
    line_local_budget = c1_ray_budget + c7_assigned_ray_budget
    require(line_local_budget == 1, "incorrect line-local first-match budget")

    experimental = Path(__file__).resolve().parents[1]
    lean = experimental / "lean/asymptotic_spine/AsymptoticSpine/C7OwnerRegression.lean"
    text = lean.read_text(encoding="utf-8")
    required = (
        "affineSteinerC1C7_firstMatch",
        "affineSteinerRawC7_numericallyPaid",
        "affineSteinerRawC7_breaks_firstMatchOwnership",
        "noClosedLineLedger_with_affineSteinerRawC7",
        "affineSteinerCorrectLine_totals",
        "affineSteinerCorrectLedger_compiles",
    )
    for declaration in required:
        require(declaration in text, f"missing Lean declaration: {declaration}")
    require("sorry" not in text.lower(), "Lean source contains a sorry placeholder")
    require(
        "sum_profile sup_line" not in text,
        "Lean source introduces the forbidden supremum/sum interchange",
    )

    print("RESULT: PASS (C7 raw payment rejected without first-match survival)")


if __name__ == "__main__":
    main()
