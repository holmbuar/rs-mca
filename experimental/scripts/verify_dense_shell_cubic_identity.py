#!/usr/bin/env python3
"""Verify source correspondence and the dense-shell integer cubic identity."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
LEAN_PATH = (
    ROOT
    / "experimental/lean/dense_shell_sign_dichotomy/"
    / "DenseShellSignDichotomy.lean"
)


def normalized(text: str) -> str:
    return " ".join(text.split())


def valid_s_expand_declaration(source: str) -> bool:
    """Require the anchored theorem statement and reject proof placeholders."""
    marker = "\ntheorem s_expand "
    try:
        start = source.index(marker) + 1
        end = source.index("\n\n/-- Finite regression", start)
    except ValueError:
        return False
    block = source[start:end]
    statement = normalized(
        """theorem s_expand (x : Int) :
        x * (3 - 4 * x) * (3 - 4 * x) =
        16 * x * x * x - 24 * x * x + 9 * x := by"""
    )
    forbidden = re.search(r"\b(?:sorry|admit|axiom|opaque|sorryAx)\b", block)
    return statement in normalized(block) and forbidden is None


def nat_sub(left: int, right: int) -> int:
    """Natural-number subtraction, used to lock the rejected Nat statement."""
    return max(left - right, 0)


def lhs(x: int) -> int:
    return x * (3 - 4 * x) * (3 - 4 * x)


def rhs(x: int) -> int:
    return 16 * x * x * x - 24 * x * x + 9 * x


def nat_lhs(x: int) -> int:
    factor = nat_sub(3, 4 * x)
    return x * factor * factor


def nat_rhs(x: int) -> int:
    return nat_sub(16 * x * x * x, 24 * x * x) + 9 * x


def verify(check_only: bool) -> tuple[int, int]:
    passed = 0
    total = 0

    def check(condition: bool, label: str) -> None:
        nonlocal passed, total
        total += 1
        if condition:
            passed += 1
        elif not check_only:
            print(f"FAIL: {label}")

    source = (
        ROOT / "experimental/notes/thresholds/dense_shell_sign_dichotomy.md"
    ).read_text()
    lean = LEAN_PATH.read_text()
    readme = (
        ROOT / "experimental/lean/dense_shell_sign_dichotomy/README.md"
    ).read_text()

    check("S(a) = a(3 - 4a)^2" in source, "source D1: definition of S")
    check(
        "full S-preimage product is the cubic identity" in source,
        "source D1: stronger preimage identity is visible",
    )
    check(
        "(e1, e2, e3) = (3/2, 9/16, A/16)" in source,
        "source D1: Vieta data is visible",
    )
    check("theorem s_expand (x : Int)" in lean, "Lean declaration: s_expand")
    check(valid_s_expand_declaration(lean), "Lean declaration: anchored and complete")
    check(
        "x * (3 - 4 * x) * (3 - 4 * x) =" in lean,
        "Lean statement: factored side",
    )
    check(
        "16 * x * x * x - 24 * x * x + 9 * x" in lean,
        "Lean statement: expanded side",
    )
    check("theorem s_expand_census" in lean, "finite regression API retained")
    check(
        "full S-preimage product and Vieta data | none | NOT FORMALIZED IN LEAN"
        in readme,
        "theorem map: stronger D1 statement remains unformalized",
    )
    check(
        "D3/D4, every-depth dense-shell sign dichotomy | none | NOT FORMALIZED IN LEAN"
        in readme,
        "theorem map: sign theorem remains unformalized",
    )
    check(
        "D5, alternating-word closed form | `altSign`, `altN`, `alt_closed`"
        in readme,
        "theorem map: alternating closed form is D5",
    )
    check(
        "D6, certified analytic transfer tail | none | NOT FORMALIZED IN LEAN"
        in readme,
        "theorem map: transfer tail is D6 and remains unformalized",
    )

    for x in range(-512, 513):
        check(lhs(x) == rhs(x), f"integer expansion x={x}")

    for x in (-512, -50, -1, 0, 1, 50, 512):
        check(lhs(x) == rhs(x), f"named boundary x={x}")

    check(nat_lhs(1) == 0, "Nat counterexample: left side at x=1")
    check(nat_rhs(1) == 9, "Nat counterexample: right side at x=1")
    check(nat_lhs(1) != nat_rhs(1), "Nat version is rejected")

    if not check_only:
        print("DENSE-SHELL CUBIC IDENTITY SOURCE VERIFIER")
        print("range: -512 <= x <= 512; exact Python integers")
        print("source: D1 S-expansion; Lean declaration: s_expand")
    return passed, total


def tamper_selftest() -> None:
    lean = LEAN_PATH.read_text()
    caught = 0
    caught += int(
        not valid_s_expand_declaration(
            lean.replace("16 * x * x * x - 24", "15 * x * x * x - 24", 1)
        )
    )
    caught += int(
        not valid_s_expand_declaration(
            lean.replace("\ntheorem s_expand ", "\n-- theorem s_expand ", 1)
        )
    )
    caught += int(
        not valid_s_expand_declaration(
            lean.replace(":= by\n  have h44", ":= by\n  sorry\n  have h44", 1)
        )
    )
    caught += int(
        not valid_s_expand_declaration(
            lean.replace("theorem s_expand (x : Int)", "theorem s_expand (x : Nat)", 1)
        )
    )
    if caught != 4:
        raise AssertionError(f"tamper-selftest caught {caught}/4")
    print("tamper-selftest: caught 4/4")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="print only the result")
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()

    if args.tamper_selftest:
        tamper_selftest()
    passed, total = verify(args.check)
    if passed != total:
        print(f"RESULT: FAIL ({passed}/{total})")
        return 1
    print(f"RESULT: PASS ({passed}/{total})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
