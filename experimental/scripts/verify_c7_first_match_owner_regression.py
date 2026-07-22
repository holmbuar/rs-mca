#!/usr/bin/env python3
"""Support verifier for the conditional C7 adapter and atlas-order regressions.

This script replays finite fixtures and checks the source/module boundary.  It is
fail-closed under ``python -O``.  Lean compilation, not this script, is the
proof-validation authority.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Mapping


ROOT = Path(__file__).resolve().parents[2]
LEAN_DIR = ROOT / "experimental/lean/asymptotic_spine/AsymptoticSpine"
ROOT_MODULE = ROOT / "experimental/lean/asymptotic_spine/AsymptoticSpine.lean"
AUDIT_DIR = ROOT / "experimental/notes/audits"


MODULE_DECLARATIONS: dict[str, tuple[str, ...]] = {
    "C7BasePoleLedgerBridge.lean": (
        "basePoleC7Profile",
        "basePoleC7Profiles_flatten_assignedSlopes",
        "basePoleC7Line_budgetTotal",
        "basePoleC7Line_naturalTotal",
        "basePoleC7Line_budgetTotal_eq_directBudget",
        "basePoleC7Line_naturalTotal_eq_directBudget",
        "basePoleC7Line_budgetTotal_le_qMinusOne",
        "basePoleC7Line_naturalTotal_le_qMinusOne",
        "basePoleC7Ledger_compiles",
    ),
    "C7BasePoleWitnessLedgerBridge.lean": (
        "c7Line_flatten_assignedSlopes",
        "c7Line_budgetTotal_eq_directBudget",
        "c7Line_naturalTotal_eq_directBudget",
        "c7Line_budgetTotal_le_qMinusOne",
        "c7Line_naturalTotal_le_qMinusOne",
        "c7Ledger_compiles",
        "rootedFixture_compiles",
    ),
    "C7BasePoleLineExtension.lean": (
        "def liftLoss",
        "basePoleC7ProfilesAtLoss_flatten_assignedSlopes",
        "basePoleC7ProfilesAtLoss_budgetTotal",
        "basePoleC7ProfilesAtLoss_naturalTotal",
        "lineAssignedSlopes_nodup",
        "earlier_append_assignedSlopes_nodup",
        "extendLine_flatten_assignedSlopes",
        "extendLine_budgetTotal",
        "extendLine_naturalTotal",
        "extendLine_budgetTotal_le_prior_add_qMinusOne",
        "extendLine_naturalTotal_le_prior_add_qMinusOne",
        "extensionFixture_assignedSlopes",
        "extensionFixture_totals",
        "extensionFixture_loss3_totals",
    ),
    "SemanticAtlasOwnership.lean": (
        "inductive C3ProvenanceLabel",
        "structure LabeledC3Payment",
        "structure WitnessLocalRefinement",
        "structure LabeledC3ThenLater",
        "LabeledC3ThenLater.bad_le_loss_mul_naturalTotal",
        "LabeledC3ThenLater.ledger_compiles",
    ),
    "C7OwnerRegression.lean": (
        "affineSteinerC1C7_firstMatch",
        "affineSteinerRawC7_numericallyPaid",
        "affineSteinerRawC7_breaks_firstMatchOwnership",
        "noClosedLineLedger_with_affineSteinerRawC7",
        "affineSteinerCorrectLine_totals",
        "affineSteinerCorrectLedger_compiles",
    ),
    "C7SingletonPlantedAbsorption.lean": (
        "singletonPlantedRawSlopeCells_eq",
        "singletonPlanted_absorbs_rawC7",
        "singletonPlantedC3Line_totals",
        "singletonPlantedRawC7_breaks_firstMatchOwnership",
        "noClosedLineLedger_with_singletonPlanted_then_rawC7",
        "singletonPlantedC3Ledger_compiles",
    ),
}

ROOT_IMPORTS = tuple(
    f"import AsymptoticSpine.{name.removesuffix('.lean')}"
    for name in MODULE_DECLARATIONS
)

AUDIT_MARKERS: dict[str, tuple[str, ...]] = {
    "c7_base_pole_closed_ledger_producer.md": (
        "deferred third unit",
        "Exact PROVED statements",
        "ProfilePayment.liftLoss",
        "sorry / sorryAx placeholders: 0",
        "CONDITIONAL RS INSTANTIATION",
    ),
    "c7_first_match_owner_regression.md": (
        "COUNTEREXAMPLE TO ATLAS-INDEPENDENT C7 OWNERSHIP",
        "basePoleC7DirectBudget",
        "LabeledC3Payment",
        "fail-closed support verifier",
    ),
    "c7_singleton_planted_absorption.md": (
        "archived/asymptotic_rs_mca_frontiers.tex",
        "ACTIVE-ATLAS NONCANONICITY",
        "POLICY DECISION REQUIRED",
        "Nonclaims",
    ),
}


class VerificationError(RuntimeError):
    """Raised for any failed packet invariant."""


def require(condition: bool, message: str) -> None:
    """Fail closed even when Python optimization removes ``assert`` statements."""
    if not condition:
        raise VerificationError(message)


def first_match(cells: list[list[int]]) -> list[list[int]]:
    """Ordered duplicate-free first-match leaves for finite numeric cells."""
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


def read_text(path: Path, overrides: Mapping[Path, str]) -> str:
    if path in overrides:
        return overrides[path]
    require(path.is_file(), f"missing packet file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def verify(overrides: Mapping[Path, str] | None = None) -> dict[str, int]:
    overrides = {} if overrides is None else overrides

    # Exact finite atlas-order regressions.
    require(
        first_match([[7], [7]]) == [[7], []],
        "affine-Steiner first-match regression changed",
    )
    singleton_cells = [[10, 13], [10, 11], [11, 12], [12, 13]]
    require(
        first_match(singleton_cells + [[10, 11, 12, 13]])
        == [[10, 13], [11], [12], [], []],
        "singleton-planted first-match regression changed",
    )

    earlier = [100, 102]
    raw = [100, 101, 102, 103]
    assigned = [slope for slope in raw if slope not in earlier]
    require(assigned == [101, 103], "rooted deletion fixture changed")
    require(len(assigned) == 2, "direct budget is not the survivor count")
    require(2 + len(assigned) == 4, "loss-one telescope changed")
    require(6 + len(assigned) == 8, "larger-loss ray telescope changed")
    require(2 + len(assigned) == 4, "larger-loss natural telescope changed")

    declaration_count = 0
    all_lean_texts: list[str] = []
    module_texts: dict[str, str] = {}
    for filename, declarations in MODULE_DECLARATIONS.items():
        path = LEAN_DIR / filename
        text = read_text(path, overrides)
        module_texts[filename] = text
        all_lean_texts.append(text)
        for declaration in declarations:
            require(
                declaration in text,
                f"missing Lean declaration marker {declaration!r} in {filename}",
            )
            declaration_count += 1
        require(
            re.search(r"(?m)^\s*import\s+AsymptoticSpine\.", text) is not None,
            f"{filename} has no package import",
        )
        require(
            re.search(r"(?m)^\s*import\s+Mathlib(?:\.|\s|$)", text) is None,
            f"Mathlib import found in {filename}",
        )

    combined_lean = "\n".join(all_lean_texts)
    require(
        re.search(r"\bsorryAx\b|\bsorry\b|\badmit\b", combined_lean) is None,
        "Lean source contains a proof placeholder",
    )
    require(
        re.search(r"(?m)^\s*axiom\s+", combined_lean) is None,
        "Lean source introduces a custom axiom declaration",
    )
    require(
        re.search(r"(?m)^\s*unsafe\s+", combined_lean) is None,
        "Lean source introduces an unsafe declaration",
    )

    # The critical split: integrated narrow producers remain ledger-free.
    narrow_producer = read_text(LEAN_DIR / "C7BasePoleProducer.lean", overrides)
    narrow_witness = read_text(
        LEAN_DIR / "C7BasePoleWitnessProducer.lean", overrides
    )
    for filename, text in (
        ("C7BasePoleProducer.lean", narrow_producer),
        ("C7BasePoleWitnessProducer.lean", narrow_witness),
    ):
        require(
            "UniformClosedLedger" not in text,
            f"integrated narrow file was widened: {filename}",
        )
        require(
            "ProfilePayment" not in text and "ClosedLineLedger" not in text,
            f"ledger layer leaked into integrated narrow file: {filename}",
        )

    ledger_bridge = module_texts["C7BasePoleLedgerBridge.lean"]
    witness_bridge = module_texts["C7BasePoleWitnessLedgerBridge.lean"]
    line_extension = module_texts["C7BasePoleLineExtension.lean"]
    labeled_interface = module_texts["SemanticAtlasOwnership.lean"]
    require(
        "import AsymptoticSpine.C7BasePoleProducer" in ledger_bridge
        and "import AsymptoticSpine.UniformClosedLedger" in ledger_bridge,
        "raw-list bridge does not import both narrow producer and ledger",
    )
    require(
        "import AsymptoticSpine.C7BasePoleWitnessProducer" in witness_bridge
        and "import AsymptoticSpine.C7BasePoleLedgerBridge" in witness_bridge,
        "conditional witness bridge does not layer on both interfaces",
    )
    require(
        "ClosedLineLedger compilerLoss profileCap" in line_extension
        and "profile.liftLoss hLoss" in line_extension,
        "line extension is not generic in compilerLoss",
    )
    require(
        "extensionFixture_loss3_totals" in line_extension,
        "larger-loss unit-budget regression is missing",
    )
    require(
        "CertifiedC3Profile" not in labeled_interface
        and "CertifiedC3ThenLater" not in labeled_interface,
        "semantic certification overclaim returned",
    )
    require(
        "labels prove no semantic classification" in labeled_interface,
        "numeric-only provenance boundary is not explicit",
    )

    root_text = read_text(ROOT_MODULE, overrides)
    require(
        "import AsymptoticSpine.UniformClosedLedger" in root_text,
        "package root does not import UniformClosedLedger",
    )
    for import_line in ROOT_IMPORTS:
        require(import_line in root_text, f"missing package-root import: {import_line}")

    for filename, markers in AUDIT_MARKERS.items():
        text = read_text(AUDIT_DIR / filename, overrides)
        for marker in markers:
            require(marker in text, f"missing audit marker {marker!r} in {filename}")

    return {
        "modules": len(MODULE_DECLARATIONS),
        "declarations": declaration_count,
        "sorry": 0,
        "custom_axiom": 0,
        "unsafe": 0,
        "finite_regressions": 4,
    }


def tamper_selftest() -> None:
    victim = LEAN_DIR / "C7BasePoleLineExtension.lean"
    original = victim.read_text(encoding="utf-8")
    tampered = original.replace(
        "theorem extensionFixture_loss3_totals",
        "theorem removed_extensionFixture_loss3_totals",
        1,
    )
    require(tampered != original, "tamper self-test could not alter victim")
    try:
        verify({victim: tampered})
    except VerificationError:
        return
    raise VerificationError("tamper self-test was not detected")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check", action="store_true", help="run the packet checks (default)"
    )
    parser.add_argument(
        "--tamper-selftest",
        action="store_true",
        help="also prove that an in-memory declaration deletion is rejected",
    )
    args = parser.parse_args()

    summary = verify()
    print(
        "RESULT: PASS "
        f"(modules={summary['modules']}, declarations={summary['declarations']}, "
        f"finite_regressions={summary['finite_regressions']}, "
        f"sorry={summary['sorry']}, custom_axiom={summary['custom_axiom']}, "
        f"unsafe={summary['unsafe']})"
    )
    if args.tamper_selftest:
        tamper_selftest()
        print("tamper-selftest: PASS (1/1)")


if __name__ == "__main__":
    main()
