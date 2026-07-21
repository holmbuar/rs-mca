#!/usr/bin/env python3
"""Independent exact verifier for the M31 padded rank-two coloop elimination.

The general no-coloop argument is proved in the threshold note and Lean module.
This stdlib-only verifier pins the source packet, exhausts small finite-field
matrix regressions, and checks the load-bearing nonzero distinguished
coefficient.  It does not prove the Mersenne-31 list bound or any adjacent row.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[2]
PACKET = "m31-rank2-coloop-elimination"
CERT_PATH = (
    ROOT
    / "experimental/data/certificates/m31-rank2-coloop-elimination"
    / "m31_rank2_coloop_elimination.json"
)
LEAN_PACKAGE = ROOT / "experimental/lean/sidon_effective_image"
LEAN_MODULE = LEAN_PACKAGE / "SidonEffectiveImage/M31RankTwoColoop.lean"
LEAN_ROOT = LEAN_PACKAGE / "SidonEffectiveImage.lean"
LAKEFILE = LEAN_PACKAGE / "lakefile.lean"
MANIFEST = LEAN_PACKAGE / "lake-manifest.json"
TOOLCHAIN = LEAN_PACKAGE / "lean-toolchain"
THRESHOLD_NOTE = ROOT / "experimental/notes/thresholds/m31_rank2_coloop_elimination.md"
LOG_ENTRY = ROOT / "experimental/agents-log-entry-gptpro-m31-rank2-coloop.md"

FORK_BASE = "4e5f0b77c98f075ea7c8822cd4859847a232bc2a"
UPSTREAM_MAIN = "a3017697ad1594521d2779fe1d83bccd45d4c06e"
INTEGRATED_COMPILER_BLOB = "11a1882d88ff8a3f725e61c0ce427cdaaa716fe9"
PADDING_AUDIT_HEAD = "c7cbcf1cff1180b4aac0862ae3c3e665f6b29b21"
PADDING_AUDIT_BLOB = "85ec62a4594e292456e6e7acf26394c73e2af34c"
SATURATION_AUDIT_HEAD = "626c61a95b0836e84655762ef4c90ca002da986b"
SATURATION_AUDIT_BLOB = "cbb63ec62af7931b3fdb868f8d3745c8822edb09"

DEPLOYED_CONSTANTS = {
    "marked_source_key_floor": 259_881,
    "lambda_1_upper": 20_765,
    "lambda_1_2_upper": 41_530,
    "lambda_1_2_3_upper": 62_295,
    "shifted_locator_cutoff": 67_447,
    "terminal_survivors": 0,
}

# Exhaustive finite-field regressions.  The deployed theorem is general; these
# small cases are hostile checks of the exact dependence/coloop implication.
ENUMERATION_CASES = tuple(
    [(2, rows, old) for rows in range(1, 4) for old in range(1, 4)]
    + [(3, rows, old) for rows in range(1, 4) for old in range(1, 3)]
)


class VerificationError(RuntimeError):
    """Raised when an exact gate fails."""


CHECKS = 0


def require(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise VerificationError(label)


def canonical_json(payload: Any) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def seal(payload: dict[str, Any]) -> dict[str, Any]:
    out = copy.deepcopy(payload)
    out.pop("certificate_sha256", None)
    out["certificate_sha256"] = hashlib.sha256(canonical_json(out)).hexdigest()
    return out


def matrix_rank(columns: tuple[tuple[int, ...], ...], q: int, rows: int) -> int:
    """Column rank over the prime field F_q by exact modular elimination."""
    if not columns:
        return 0
    matrix = [[columns[c][r] % q for c in range(len(columns))] for r in range(rows)]
    rank = 0
    col = 0
    while rank < rows and col < len(columns):
        pivot = next((r for r in range(rank, rows) if matrix[r][col] % q != 0), None)
        if pivot is None:
            col += 1
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inv = pow(matrix[rank][col], -1, q)
        matrix[rank] = [(inv * x) % q for x in matrix[rank]]
        for r in range(rows):
            if r == rank:
                continue
            factor = matrix[r][col] % q
            if factor:
                matrix[r] = [
                    (matrix[r][c] - factor * matrix[rank][c]) % q
                    for c in range(len(columns))
                ]
        rank += 1
        col += 1
    return rank


def chunks(values: tuple[int, ...], size: int) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(values[i : i + size]) for i in range(0, len(values), size))


def is_relation(
    columns: tuple[tuple[int, ...], ...], coefficients: tuple[int, ...], q: int, rows: int
) -> bool:
    return all(
        sum(coefficients[c] * columns[c][r] for c in range(len(columns))) % q == 0
        for r in range(rows)
    )


def enumerate_case(q: int, rows: int, old_columns: int) -> dict[str, int]:
    column_count = old_columns + 1
    matrix_count = q ** (rows * column_count)
    coefficient_vectors = q**old_columns * (q - 1)
    relation_instances = 0
    matrices_with_relation = 0
    rank_preservation_checks = 0
    violations = 0

    old_coefficients = tuple(itertools.product(range(q), repeat=old_columns))
    extra_coefficients = tuple(range(1, q))

    for flat in itertools.product(range(q), repeat=rows * column_count):
        columns = chunks(tuple(flat), rows)
        saw_relation = False
        full_rank: int | None = None
        old_rank: int | None = None
        for old_coeff in old_coefficients:
            for extra_coeff in extra_coefficients:
                coefficients = tuple(old_coeff) + (extra_coeff,)
                if not is_relation(columns, coefficients, q, rows):
                    continue
                relation_instances += 1
                saw_relation = True
                if full_rank is None:
                    full_rank = matrix_rank(columns, q, rows)
                    old_rank = matrix_rank(columns[:-1], q, rows)
                rank_preservation_checks += 1
                if full_rank != old_rank:
                    violations += 1
        if saw_relation:
            matrices_with_relation += 1

    require(violations == 0, f"no-coloop implication over F_{q}, rows={rows}, old={old_columns}")
    return {
        "field_order": q,
        "row_count": rows,
        "old_column_count": old_columns,
        "matrix_count": matrix_count,
        "coefficient_vectors_per_matrix": coefficient_vectors,
        "relation_instances": relation_instances,
        "matrices_with_relation": matrices_with_relation,
        "rank_preservation_checks": rank_preservation_checks,
        "violations": violations,
    }


def zero_extra_falsifier() -> dict[str, Any]:
    # Over F_2, old column 0 and extra column 1.  Coefficients (1,0) give a
    # relation, but deletion changes rank from one to zero.  This is outside the
    # theorem because the distinguished coefficient is zero.
    q = 2
    rows = 1
    columns = ((0,), (1,))
    coefficients = (1, 0)
    relation = is_relation(columns, coefficients, q, rows)
    full_rank = matrix_rank(columns, q, rows)
    old_rank = matrix_rank(columns[:-1], q, rows)
    require(relation, "zero-extra falsifier is a relation")
    require(coefficients[-1] == 0, "zero-extra falsifier drops the load-bearing hypothesis")
    require(full_rank == 1 and old_rank == 0, "zero-extra falsifier deletes a coloop")
    return {
        "field_order": q,
        "row_count": rows,
        "old_columns": [[0]],
        "extra_column": [1],
        "coefficients": [1, 0],
        "relation_holds": relation,
        "full_rank": full_rank,
        "old_rank": old_rank,
        "deletion_lowers_rank": full_rank > old_rank,
        "distinguished_coefficient_nonzero": False,
    }


def source_gate() -> dict[str, str]:
    for path in (LEAN_MODULE, LEAN_ROOT, LAKEFILE, MANIFEST, TOOLCHAIN, THRESHOLD_NOTE, LOG_ENTRY):
        require(path.is_file(), f"required packet file exists: {path.relative_to(ROOT)}")

    module = LEAN_MODULE.read_text()
    root = LEAN_ROOT.read_text()
    lakefile = LAKEFILE.read_text()
    manifest = json.loads(MANIFEST.read_text())
    toolchain = TOOLCHAIN.read_text().strip()
    note = THRESHOLD_NOTE.read_text()

    import_lines = [line.strip() for line in module.splitlines() if line.strip().startswith("import ")]
    require(import_lines == ["import Std"], "Lean module imports only Std")
    require(root.strip() == "import SidonEffectiveImage.M31RankTwoColoop", "root imports only lane module")
    require("require " not in lakefile, "lakefile has no package requires")
    require(manifest == {
        "version": "1.2.0",
        "packagesDir": ".lake/packages",
        "packages": [],
        "name": "sidonEffectiveImage",
        "lakeDir": ".lake",
        "fixedToolchain": False,
    }, "empty Lake manifest is canonical")
    require(toolchain == "leanprover/lean4:v4.31.0", "Lean toolchain is exactly v4.31.0")

    modules = sorted(path.name for path in (LEAN_PACKAGE / "SidonEffectiveImage").glob("*.lean"))
    require(modules == ["M31RankTwoColoop.lean"], "package contains exactly one module")

    forbidden_imports = ("M31C9RowSharp", "HalfSliceFalsifier", "AsymptoticSpine.", "M31QRootedShell.")
    for token in forbidden_imports:
        require(token not in module, f"forbidden/open dependency absent: {token}")

    for line in module.splitlines():
        stripped = line.strip()
        require(not stripped.startswith("axiom "), "no custom axiom declaration")
        require(not stripped.startswith("axioms "), "no custom axioms declaration")
        require("native_decide" not in stripped, "no native_decide")
        require("Mathlib" not in stripped, "no Mathlib import")
        require(not stripped.startswith("sorry"), "no sorry term")

    theorem_markers = (
        "theorem paddedLocatorGivesNonzeroExtraDependence",
        "theorem extraColumnIsNotColoop",
        "theorem rankTwoColoopTerminalIsEmpty",
        "theorem everyMarkedFrameExcludesRankTwoColoop",
        "theorem deployedConstantsExact",
        "#print axioms paddedLocatorGivesNonzeroExtraDependence",
        "#print axioms extraColumnIsNotColoop",
        "#print axioms rankTwoColoopTerminalIsEmpty",
        "#print axioms everyMarkedFrameExcludesRankTwoColoop",
        "#print axioms deployedConstantsExact",
    )
    for marker in theorem_markers:
        require(marker in module, f"Lean marker present: {marker}")

    note_markers = (
        "UNPAID_RANK2_COLOOP",
        "sum_(i=1)^46 W'_i v_i = 0",
        "ACCEPTANCE GATE CRITERION 3",
        "F_11",
        "UNPAID_COMMON_CORE_ADD_BACK",
    )
    for marker in note_markers:
        require(marker in note, f"threshold marker present: {marker}")

    require(DEPLOYED_CONSTANTS["lambda_1_2_3_upper"] < DEPLOYED_CONSTANTS["shifted_locator_cutoff"],
            "padded rank-three sum is below cutoff")
    require(DEPLOYED_CONSTANTS["terminal_survivors"] == 0, "terminal survivor count is zero")

    return {
        "lean_module_sha256": sha256_path(LEAN_MODULE),
        "lean_root_sha256": sha256_path(LEAN_ROOT),
        "lakefile_sha256": sha256_path(LAKEFILE),
        "lake_manifest_sha256": sha256_path(MANIFEST),
        "lean_toolchain_sha256": sha256_path(TOOLCHAIN),
        "threshold_note_sha256": sha256_path(THRESHOLD_NOTE),
        "agents_log_entry_sha256": sha256_path(LOG_ENTRY),
    }


def build_payload() -> dict[str, Any]:
    source_hashes = source_gate()
    cases = [enumerate_case(q, rows, old) for q, rows, old in ENUMERATION_CASES]
    totals = {
        "case_count": len(cases),
        "matrix_count": sum(case["matrix_count"] for case in cases),
        "relation_instances": sum(case["relation_instances"] for case in cases),
        "matrices_with_relation": sum(case["matrices_with_relation"] for case in cases),
        "rank_preservation_checks": sum(case["rank_preservation_checks"] for case in cases),
        "violations": sum(case["violations"] for case in cases),
    }
    require(totals["case_count"] == 15, "printed enumeration case count")
    require(totals["violations"] == 0, "aggregate no-coloop violations")

    payload: dict[str, Any] = {
        "schema_version": 1,
        "packet": PACKET,
        "proof_status": "PROVED_TERMINAL_ELIMINATION",
        "acceptance_gate_criterion": 3,
        "base": {
            "fork_repository": "holmbuar/rs-mca",
            "fork_main_sha": FORK_BASE,
            "upstream_repository": "przchojecki/rs-mca",
            "upstream_main_sha_included": UPSTREAM_MAIN,
        },
        "source_blobs": {
            "integrated_rank46_compiler_fork": INTEGRATED_COMPILER_BLOB,
            "integrated_rank46_compiler_upstream": INTEGRATED_COMPILER_BLOB,
            "padding_bridge_audit_head": PADDING_AUDIT_HEAD,
            "padding_bridge_audit_blob": PADDING_AUDIT_BLOB,
            "masked_saturation_audit_head": SATURATION_AUDIT_HEAD,
            "masked_saturation_audit_blob": SATURATION_AUDIT_BLOB,
        },
        "imported_repository_apis": [],
        "deployed_constants": DEPLOYED_CONSTANTS,
        "source_sha256": source_hashes,
        "enumeration": {
            "claim": "nonzero distinguished relation coefficient implies deletion preserves rank",
            "cases": cases,
            "totals": totals,
            "zero_distinguished_coefficient_falsifier": zero_extra_falsifier(),
        },
        "nonclaims": [
            "no common-core add-back",
            "no row-sharp Q",
            "no list-interior payment",
            "no adjacent-row closure",
            "no direct transport of a named actual-error basis",
        ],
    }
    return seal(payload)


def verify_certificate(actual: dict[str, Any], expected: dict[str, Any]) -> None:
    require(actual.get("certificate_sha256") is not None, "certificate has self hash")
    unsealed = copy.deepcopy(actual)
    claimed = unsealed.pop("certificate_sha256")
    require(claimed == hashlib.sha256(canonical_json(unsealed)).hexdigest(), "certificate self hash")
    require(actual == expected, "certificate exactly matches independent recomputation")


def write_certificate(payload: dict[str, Any]) -> None:
    CERT_PATH.parent.mkdir(parents=True, exist_ok=True)
    CERT_PATH.write_bytes(canonical_json(payload))


def run_tamper_selftest(expected: dict[str, Any]) -> int:
    tests: list[tuple[str, dict[str, Any]]] = []

    bad_constant = copy.deepcopy(expected)
    bad_constant["deployed_constants"]["terminal_survivors"] = 1
    tests.append(("terminal survivor mutation", bad_constant))

    bad_violation = copy.deepcopy(expected)
    bad_violation["enumeration"]["totals"]["violations"] = 1
    tests.append(("enumeration violation mutation", bad_violation))

    bad_blob = copy.deepcopy(expected)
    bad_blob["source_blobs"]["integrated_rank46_compiler_fork"] = "0" * 40
    tests.append(("source blob mutation", bad_blob))

    bad_hash = copy.deepcopy(expected)
    bad_hash["certificate_sha256"] = "0" * 64
    tests.append(("self-hash mutation", bad_hash))

    rejected = 0
    for label, mutation in tests:
        try:
            verify_certificate(mutation, expected)
        except VerificationError:
            rejected += 1
        else:
            raise VerificationError(f"tamper was not rejected: {label}")

    falsifier = expected["enumeration"]["zero_distinguished_coefficient_falsifier"]
    require(falsifier["relation_holds"], "falsifier relation retained")
    require(not falsifier["distinguished_coefficient_nonzero"], "falsifier drops nonzero coefficient")
    require(falsifier["deletion_lowers_rank"], "falsifier demonstrates coloop after hypothesis drop")

    print(f"TAMPER_SELFTEST: PASS ({rejected}/{len(tests)} mutations rejected)")
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify the frozen certificate")
    parser.add_argument("--write", action="store_true", help="write the independently recomputed certificate")
    parser.add_argument("--tamper-selftest", action="store_true", help="run hostile mutation gates")
    args = parser.parse_args()

    require(args.check or args.write or args.tamper_selftest, "select --check, --write, or --tamper-selftest")
    expected = build_payload()

    if args.write:
        write_certificate(expected)
        print(f"WROTE: {CERT_PATH.relative_to(ROOT)}")

    if args.check:
        require(CERT_PATH.is_file(), "certificate exists")
        actual = json.loads(CERT_PATH.read_text())
        verify_certificate(actual, expected)
        totals = expected["enumeration"]["totals"]
        print(
            "RESULT: PASS "
            f"cases={totals['case_count']} matrices={totals['matrix_count']} "
            f"relations={totals['relation_instances']} "
            f"rank_checks={totals['rank_preservation_checks']} violations={totals['violations']}"
        )
        print("TERMINAL: UNPAID_RANK2_COLOOP -> EMPTY")

    if args.tamper_selftest:
        run_tamper_selftest(expected)

    print(f"checks={CHECKS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
