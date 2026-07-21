#!/usr/bin/env python3
"""Replay the exact finite C8 chart-exhaustion certificate.

This script is stdlib-only.  It verifies the shipped JSON packet's classifier
priority, duplicate-free calibration IDs, exact four-bucket exhaustion,
moving-root incidence arithmetic, active-row cap-two calculations, and exact
name of the sole unpaid deep residual.

Lean remains the proof-validation authority.  This script is a deterministic
certificate replay and mutation-sensitive packaging check.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

EXPECTED_SCHEMA = "c8-chart-exhaustion-v1"
EXPECTED_STATUS = "PROVED_FINITE_ROUTE_CUT_PARTIAL_EXHAUSTION"
EXPECTED_PRIORITY = [
    "earlier",
    "shallow",
    "bounded_pencil",
    "deep_residual",
]
EXPECTED_DEEP_RESIDUAL = (
    "DEEP_HIGHER_DIMENSIONAL_BALANCED_CORE_AFTER_"
    "C1_C7_SHALLOW_AND_ONE_PENCIL_DELETION"
)
EXPECTED_BASE_SHA = "4e5f0b77c98f075ea7c8822cd4859847a232bc2a"
EXPECTED_ROWS = {
    "Mersenne-31 MCA": (2_097_152, 981_128, 2),
    "KoalaBear MCA": (2_097_152, 981_104, 2),
}
EXPECTED_NONCLAIMS = {
    "ACTUAL_RS_C1_C7_OWNER_FUNCTION",
    "ACTUAL_RS_SHALLOW_PREFIX_SE2_CERTIFICATE",
    "ACTUAL_RS_COMMON_CORE_SHORTENING_CERTIFICATE",
    "GENERAL_GENUINE_ONE_PENCIL_CLASSIFIER",
    "DEEP_PREFIX_MI_MA_OR_SIDON_PAYMENT",
    "DEEP_HIGHER_DIMENSIONAL_RAY_PAYMENT",
    "ROW_UNIFORM_UNIF",
    "DEPLOYED_ADJACENT_ROW_CLOSURE",
}


def fail(message: str) -> None:
    raise AssertionError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise AssertionError(f"certificate not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise AssertionError(f"invalid JSON: {exc}") from exc
    require(isinstance(data, dict), "certificate root must be an object")
    return data


def classify(chart: dict[str, Any], supplied_shallow: str) -> str:
    owner = chart.get("earlier_owner")
    chart_id = chart.get("chart_id")
    certificate = chart.get("moving_root_certificate")

    if owner is not None:
        return "earlier"
    if chart_id == supplied_shallow:
        return "shallow"
    if certificate is not None:
        return "bounded_pencil"
    return "deep_residual"


def verify_moving_root_certificate(
    certificate: dict[str, Any], context: str
) -> tuple[int, int, int]:
    require(isinstance(certificate, dict), f"{context}: certificate must be object")
    points = certificate.get("moving_points")
    roots = certificate.get("moving_roots_per_slope")
    slopes = certificate.get("slope_count")
    for name, value in (
        ("moving_points", points),
        ("moving_roots_per_slope", roots),
        ("slope_count", slopes),
    ):
        require(type(value) is int, f"{context}: {name} must be an integer")
        require(value >= 0, f"{context}: {name} must be nonnegative")
    require(roots > 0, f"{context}: moving roots per slope must be positive")
    require(
        slopes * roots <= points,
        f"{context}: incidence inequality slope_count*roots <= points fails",
    )
    return points, roots, slopes


def verify(data: dict[str, Any]) -> int:
    checks = 0

    require(data.get("schema") == EXPECTED_SCHEMA, "schema mismatch")
    checks += 1
    require(data.get("status") == EXPECTED_STATUS, "status mismatch")
    checks += 1
    require(data.get("base_sha") == EXPECTED_BASE_SHA, "base SHA mismatch")
    checks += 1
    require(data.get("bucket_priority") == EXPECTED_PRIORITY, "bucket priority mismatch")
    checks += 1
    require(
        data.get("deep_residual_name") == EXPECTED_DEEP_RESIDUAL,
        "deep residual spelling mismatch",
    )
    checks += 1

    supplied_shallow = data.get("supplied_shallow_chart")
    require(isinstance(supplied_shallow, str) and supplied_shallow, "invalid shallow chart ID")
    checks += 1

    charts = data.get("charts")
    require(isinstance(charts, list), "charts must be a list")
    require(len(charts) == 4, "calibration must contain exactly four charts")
    checks += 2

    chart_ids: list[str] = []
    observed_buckets: list[str] = []
    shallow_flags = 0
    deep_ids: list[str] = []

    for index, raw_chart in enumerate(charts):
        context = f"chart[{index}]"
        require(isinstance(raw_chart, dict), f"{context}: chart must be an object")
        chart_id = raw_chart.get("chart_id")
        require(isinstance(chart_id, str) and chart_id, f"{context}: invalid chart_id")
        chart_ids.append(chart_id)

        owner = raw_chart.get("earlier_owner")
        require(
            owner is None or owner in {"C1", "C2", "C3", "C4", "C5", "C6", "C7"},
            f"{context}: invalid earlier owner",
        )
        checks += 1

        is_supplied = raw_chart.get("is_supplied_shallow")
        require(type(is_supplied) is bool, f"{context}: shallow flag must be bool")
        require(
            is_supplied == (chart_id == supplied_shallow),
            f"{context}: shallow flag disagrees with supplied chart ID",
        )
        shallow_flags += int(is_supplied)
        checks += 2

        certificate = raw_chart.get("moving_root_certificate")
        if certificate is not None:
            verify_moving_root_certificate(certificate, context)
            checks += 4

        bucket = classify(raw_chart, supplied_shallow)
        observed_buckets.append(bucket)
        require(
            raw_chart.get("expected_bucket") == bucket,
            f"{context}: expected bucket does not match fixed-priority classifier",
        )
        checks += 1
        if bucket == "deep_residual":
            deep_ids.append(chart_id)

    require(len(set(chart_ids)) == len(chart_ids), "chart IDs are not duplicate-free")
    checks += 1
    require(shallow_flags == 1, "calibration must contain exactly one supplied shallow key")
    checks += 1
    require(
        sorted(observed_buckets) == sorted(EXPECTED_PRIORITY),
        "calibration must realize every bucket exactly once",
    )
    checks += 1
    require(
        deep_ids == ["deep-higher-dimensional"],
        "the calibration must have exactly the named deep chart ID",
    )
    checks += 1

    rows = data.get("active_row_moving_root_caps")
    require(isinstance(rows, list), "active row caps must be a list")
    require(len(rows) == len(EXPECTED_ROWS), "active row cap count mismatch")
    checks += 2
    seen_rows: set[str] = set()
    for index, raw_row in enumerate(rows):
        context = f"active_row[{index}]"
        require(isinstance(raw_row, dict), f"{context}: row must be an object")
        row = raw_row.get("row")
        require(row in EXPECTED_ROWS, f"{context}: unexpected row")
        require(row not in seen_rows, f"{context}: duplicate row")
        seen_rows.add(row)
        points = raw_row.get("moving_points")
        roots = raw_row.get("moving_roots_per_slope")
        cap = raw_row.get("claimed_cap")
        require(
            (points, roots, cap) == EXPECTED_ROWS[row],
            f"{context}: active-row constants mismatch",
        )
        require(roots > 0, f"{context}: roots must be positive")
        require(cap * roots <= points, f"{context}: claimed cap is not feasible")
        require(
            points < (cap + 1) * roots,
            f"{context}: claimed cap is not exact from incidence arithmetic",
        )
        checks += 6

    require(seen_rows == set(EXPECTED_ROWS), "not all active rows were checked")
    checks += 1

    nonclaims = data.get("nonclaims")
    require(isinstance(nonclaims, list), "nonclaims must be a list")
    require(len(nonclaims) == len(set(nonclaims)), "nonclaims contain duplicates")
    require(set(nonclaims) == EXPECTED_NONCLAIMS, "nonclaim set mismatch")
    checks += 3

    return checks


def default_certificate_path() -> Path:
    return (
        Path(__file__).resolve().parents[1]
        / "data"
        / "certificates"
        / "c8-chart-exhaustion"
        / "c8_chart_exhaustion.json"
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--certificate",
        type=Path,
        default=default_certificate_path(),
        help="path to the C8 chart-exhaustion JSON certificate",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="accepted for consistency with repository verifier conventions",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    try:
        checks = verify(load_json(args.certificate))
    except AssertionError as exc:
        print(f"RESULT: FAIL ({exc})")
        return 1
    print(f"RESULT: PASS ({checks} checks)")
    print(f"certificate: {args.certificate}")
    print(f"deep residual: {EXPECTED_DEEP_RESIDUAL}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
