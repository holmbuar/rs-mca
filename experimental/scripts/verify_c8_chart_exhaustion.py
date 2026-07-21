#!/usr/bin/env python3
"""Replay the actual finite spine C8 chart-exhaustion certificate.

The verifier is stdlib-only.  It independently recomputes:

* the fixed C1--C7 > shallow > one-pencil > deep classifier;
* first-match deletion from the raw chart slope projections;
* duplicate-free chart and slope ownership across all four buckets;
* the exact #1020 shallow fixture data and shallow direct-RC arithmetic;
* the KoalaBear one-pencil moving-root payment;
* the active KoalaBear/Mersenne cap-two arithmetic; and
* the exact spelling and uniqueness of the unpaid deep residual.

Lean remains the proof-validation authority.  This script is deterministic
certificate replay and mutation-sensitive packaging validation.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any

EXPECTED_SCHEMA = "c8-chart-exhaustion-v1"
EXPECTED_STATUS = "PROVED_FINITE_ROUTE_CUT_PARTIAL_EXHAUSTION"
EXPECTED_BASE_SHA = "4e5f0b77c98f075ea7c8822cd4859847a232bc2a"
EXPECTED_PRIORITY = ["earlier", "shallow", "bounded_pencil", "deep_residual"]
EXPECTED_CHART_ORDER = [
    "earlier-c1",
    "supplied-shallow",
    "moving-pencil-koalabear",
    "deep-higher-dimensional",
]
EXPECTED_DEEP_RESIDUAL = (
    "DEEP_HIGHER_DIMENSIONAL_BALANCED_CORE_AFTER_"
    "C1_C7_SHALLOW_AND_ONE_PENCIL_DELETION"
)
EXPECTED_FLATTENED = [5, 7, 9, 11, 13, 17]
EXPECTED_IMPORT_BLOBS = {
    "experimental/lean/asymptotic_spine/AsymptoticSpine/PrefixAtlas.lean":
        "d14c5fc6d93e0386fc9fb6ebfe0d0c3debc35cb1",
    "experimental/lean/asymptotic_spine/AsymptoticSpine/FirstMatch.lean":
        "44592371660c453c1f8522abb9c0f9364e4dd43d",
    "experimental/lean/asymptotic_spine/AsymptoticSpine/Util.lean":
        "5e09daceb9fa4d3fb72e3c59244ec348b51352c2",
    "experimental/lean/asymptotic_spine/AsymptoticSpine/EffectiveClosure.lean":
        "9fb097e23d00e2f3ee3afeda021b86ba4192d2a4",
    "experimental/lean/asymptotic_spine/AsymptoticSpine/HighKappaCoverage.lean":
        "cdb17177fe7f17a7e8b520d999fa925c5abfaea0",
}
EXPECTED_ROWS = {
    "KoalaBear MCA": (2_097_152, 981_104, 2),
    "Mersenne-31 MCA": (2_097_152, 981_128, 2),
}
EXPECTED_NONCLAIMS = {
    "DEPLOYED_RS_C1_C7_OWNER_FUNCTION",
    "DEPLOYED_RS_SHALLOW_PREFIX_SE2_CERTIFICATE",
    "ACTUAL_RS_COMMON_CORE_SHORTENING_CERTIFICATE",
    "GENERAL_GENUINE_ONE_PENCIL_CLASSIFIER",
    "DEEP_PREFIX_MI_MA_OR_SIDON_PAYMENT",
    "DEEP_HIGHER_DIMENSIONAL_RAY_PAYMENT",
    "ROW_UNIFORM_UNIF",
    "DEPLOYED_ADJACENT_ROW_CLOSURE",
}


class VerificationFailure(AssertionError):
    """Raised when a certificate gate fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationFailure(message)


def require_int(value: Any, context: str, *, positive: bool = False) -> int:
    require(type(value) is int, f"{context} must be an integer")
    if positive:
        require(value > 0, f"{context} must be positive")
    else:
        require(value >= 0, f"{context} must be nonnegative")
    return value


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise VerificationFailure(f"certificate not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise VerificationFailure(f"invalid JSON: {exc}") from exc
    require(isinstance(data, dict), "certificate root must be an object")
    return data


def classify(chart: dict[str, Any]) -> str:
    if chart.get("earlier_owner") is not None:
        return "earlier"
    if chart.get("is_supplied_shallow") is True:
        return "shallow"
    if chart.get("moving_root_certificate") is not None:
        return "bounded_pencil"
    return "deep_residual"


def first_match_leaves(raw_cells: list[list[int]]) -> list[list[int]]:
    paid: list[int] = []
    leaves: list[list[int]] = []
    for cell in raw_cells:
        leaf = [slope for slope in cell if slope not in paid]
        leaves.append(leaf)
        paid.extend(leaf)
    return leaves


def is_subsequence(xs: list[int], ys: list[int]) -> bool:
    cursor = 0
    for value in ys:
        if cursor < len(xs) and xs[cursor] == value:
            cursor += 1
    return cursor == len(xs)


def verify_moving_root_certificate(
    certificate: dict[str, Any], context: str
) -> tuple[list[int], int, int, int]:
    require(isinstance(certificate, dict), f"{context}: certificate must be object")
    slopes = certificate.get("slopes")
    require(isinstance(slopes, list), f"{context}: slopes must be a list")
    require(all(type(x) is int and x >= 0 for x in slopes), f"{context}: invalid slope")
    require(len(slopes) == len(set(slopes)), f"{context}: slope list has duplicates")
    points = require_int(certificate.get("moving_points"), f"{context}.moving_points")
    roots = require_int(
        certificate.get("moving_roots_per_slope"),
        f"{context}.moving_roots_per_slope",
        positive=True,
    )
    cap = require_int(certificate.get("claimed_cap"), f"{context}.claimed_cap")
    require(len(slopes) * roots <= points, f"{context}: incidence inequality fails")
    require(cap * roots <= points, f"{context}: claimed cap is infeasible")
    require(points < (cap + 1) * roots, f"{context}: claimed cap is not exact")
    require(len(slopes) <= cap, f"{context}: actual slope list exceeds claimed cap")
    return slopes, points, roots, cap


def verify(data: dict[str, Any]) -> int:
    checks = 0

    require(data.get("schema") == EXPECTED_SCHEMA, "schema mismatch")
    require(data.get("status") == EXPECTED_STATUS, "status mismatch")
    require(data.get("base_sha") == EXPECTED_BASE_SHA, "base SHA mismatch")
    require(data.get("workboard_item") == "K3", "workboard item mismatch")
    require(data.get("row") == "KoalaBear MCA", "row mismatch")
    require(data.get("object") == "MCA", "object mismatch")
    require(data.get("target_epsilon") == "2^-128", "target mismatch")
    require(data.get("agreement") == 1_116_048, "agreement mismatch")
    require(data.get("B_star") == 274_980_728_111_395_087, "B* mismatch")
    require(data.get("bucket_priority") == EXPECTED_PRIORITY, "bucket priority mismatch")
    require(data.get("deep_residual_name") == EXPECTED_DEEP_RESIDUAL,
            "deep residual spelling mismatch")
    require(data.get("imported_api_blobs") == EXPECTED_IMPORT_BLOBS,
            "imported API blob table mismatch")
    checks += 12

    calibration = data.get("spine_calibration")
    require(isinstance(calibration, dict), "spine_calibration must be an object")
    require(calibration.get("chart_order") == EXPECTED_CHART_ORDER, "chart order mismatch")
    charts = calibration.get("charts")
    require(isinstance(charts, list), "charts must be a list")
    require(len(charts) == 4, "calibration must contain exactly four charts")
    checks += 3

    chart_ids: list[str] = []
    raw_cells: list[list[int]] = []
    expected_leaves: list[list[int]] = []
    observed_buckets: list[str] = []
    bounded_certificate: tuple[list[int], int, int, int] | None = None

    for index, chart in enumerate(charts):
        context = f"chart[{index}]"
        require(isinstance(chart, dict), f"{context}: chart must be object")
        chart_id = chart.get("chart_id")
        require(chart_id == EXPECTED_CHART_ORDER[index], f"{context}: chart ID/order mismatch")
        chart_ids.append(chart_id)

        raw = chart.get("raw_slopes")
        expected = chart.get("expected_post_deletion_slopes")
        require(isinstance(raw, list), f"{context}: raw_slopes must be list")
        require(isinstance(expected, list), f"{context}: expected leaf must be list")
        require(all(type(x) is int and x >= 0 for x in raw), f"{context}: invalid raw slope")
        require(all(type(x) is int and x >= 0 for x in expected),
                f"{context}: invalid expected slope")
        require(len(raw) == len(set(raw)), f"{context}: raw chart contains duplicates")
        require(len(expected) == len(set(expected)), f"{context}: expected leaf contains duplicates")
        raw_cells.append(raw)
        expected_leaves.append(expected)

        owner = chart.get("earlier_owner")
        require(owner is None or owner in {f"C{i}" for i in range(1, 8)},
                f"{context}: invalid earlier owner")
        shallow = chart.get("is_supplied_shallow")
        require(type(shallow) is bool, f"{context}: shallow flag must be bool")
        certificate = chart.get("moving_root_certificate")
        bucket = classify(chart)
        observed_buckets.append(bucket)
        require(chart.get("expected_bucket") == bucket,
                f"{context}: classifier/expected bucket mismatch")

        if certificate is not None:
            require(bounded_certificate is None, "more than one bounded-pencil calibration chart")
            bounded_certificate = verify_moving_root_certificate(certificate, context)
        checks += 8

    require(len(chart_ids) == len(set(chart_ids)), "chart IDs are not duplicate-free")
    require(observed_buckets == EXPECTED_PRIORITY, "calibration does not realize exact bucket order")
    require(sum(chart.get("is_supplied_shallow") is True for chart in charts) == 1,
            "calibration must contain exactly one shallow chart")
    require(sum(bucket == "deep_residual" for bucket in observed_buckets) == 1,
            "calibration must contain exactly one deep residual chart")
    require(bounded_certificate is not None, "bounded-pencil certificate missing")
    checks += 5

    actual_leaves = first_match_leaves(raw_cells)
    require(actual_leaves == expected_leaves, "first-match leaves do not match certificate")
    flattened = [slope for leaf in actual_leaves for slope in leaf]
    require(flattened == EXPECTED_FLATTENED, "flattened post-deletion slopes mismatch")
    require(flattened == calibration.get("expected_flattened_post_deletion_slopes"),
            "certificate flattened slope list mismatch")
    require(len(flattened) == len(set(flattened)), "post-deletion ownership is not duplicate-free")
    raw_union = {slope for cell in raw_cells for slope in cell}
    require(set(flattened) == raw_union, "first-match deletion changed raw slope coverage")
    checks += 5

    shallow = data.get("supplied_shallow_input")
    require(isinstance(shallow, dict), "supplied_shallow_input must be object")
    require(shallow.get("producer_reference") ==
            "upstream PR #1020 C8ShallowClosure.ProfileData fixture",
            "shallow producer reference mismatch")
    full_slice = shallow.get("full_slice")
    supports = shallow.get("supports")
    slopes = shallow.get("slopes")
    support_of = shallow.get("support_of")
    require(full_slice == [0, 1, 2, 3, 4], "affineToyBridge full slice mismatch")
    require(shallow.get("bridge") == "affineToyBridge", "bridge name mismatch")
    require(shallow.get("syndrome_key") == 1, "syndrome key mismatch")
    require(shallow.get("depth_prefix_key") == 11, "translated prefix key mismatch")
    require(supports == [1, 3], "SE2 supports mismatch")
    require(slopes == [7, 9], "SE2 slopes mismatch")
    require(support_of == {"7": 1, "9": 3}, "SE2 support map mismatch")
    chosen = [support_of[str(slope)] for slope in slopes]
    require(is_subsequence(chosen, supports), "SE2 chosen supports are not a sublist")
    require(slopes == actual_leaves[1], "shallow SE2 slopes are not the post-deletion leaf")
    require([x for x in full_slice if x % 2 == 1] == supports,
            "affineToyBridge syndrome fibre mismatch")

    base_size = require_int(shallow.get("base_size"), "shallow.base_size", positive=True)
    prefix_depth = require_int(shallow.get("prefix_depth"), "shallow.prefix_depth")
    image_size = require_int(shallow.get("image_size"), "shallow.image_size")
    effective_size = require_int(shallow.get("effective_size"), "shallow.effective_size")
    average = require_int(shallow.get("average"), "shallow.average")
    compiler_loss = require_int(shallow.get("compiler_loss"), "shallow.compiler_loss")
    natural_scale = require_int(shallow.get("natural_scale"), "shallow.natural_scale")
    require(shallow.get("kernel_dimension_label") == 1_000_000,
            "kernel dimension label mismatch")
    require(compiler_loss == base_size ** prefix_depth, "compiler loss mismatch")
    require(natural_scale == 1 + average, "natural scale mismatch")
    require(len(full_slice) <= image_size * average, "shallow average does not cover mass")
    require(image_size <= effective_size <= compiler_loss,
            "shallow image/effective/loss chain fails")
    require(len(slopes) <= compiler_loss * natural_scale,
            "shallow distinct-slope payment fails")
    checks += 18

    pencil_slopes, points, roots, cap = bounded_certificate
    require(pencil_slopes == actual_leaves[2],
            "one-pencil certificate slopes are not the post-deletion leaf")
    require((points, roots, cap) == EXPECTED_ROWS["KoalaBear MCA"],
            "calibration one-pencil constants are not KoalaBear constants")
    require(actual_leaves[3] == [17], "deep residual assigned slope list mismatch")
    checks += 3

    rows = data.get("active_row_moving_root_caps")
    require(isinstance(rows, list), "active row caps must be a list")
    require(len(rows) == len(EXPECTED_ROWS), "active row cap count mismatch")
    seen_rows: set[str] = set()
    for index, row_record in enumerate(rows):
        context = f"active_row[{index}]"
        require(isinstance(row_record, dict), f"{context}: row must be object")
        row = row_record.get("row")
        require(row in EXPECTED_ROWS, f"{context}: unexpected row")
        require(row not in seen_rows, f"{context}: duplicate row")
        seen_rows.add(row)
        points = require_int(row_record.get("moving_points"), f"{context}.moving_points")
        roots = require_int(row_record.get("moving_roots_per_slope"),
                            f"{context}.moving_roots_per_slope", positive=True)
        cap = require_int(row_record.get("claimed_cap"), f"{context}.claimed_cap")
        require((points, roots, cap) == EXPECTED_ROWS[row], f"{context}: constants mismatch")
        require(cap * roots <= points < (cap + 1) * roots,
                f"{context}: exact cap arithmetic fails")
        checks += 5
    require(seen_rows == set(EXPECTED_ROWS), "not all active rows were checked")
    checks += 1

    nonclaims = data.get("nonclaims")
    require(isinstance(nonclaims, list), "nonclaims must be a list")
    require(len(nonclaims) == len(set(nonclaims)), "nonclaims contain duplicates")
    require(set(nonclaims) == EXPECTED_NONCLAIMS, "nonclaim set mismatch")
    checks += 3

    return checks


def run_tamper_selftest(data: dict[str, Any]) -> int:
    mutations: list[tuple[str, Any]] = []

    def mutate_deep_name(packet: dict[str, Any]) -> None:
        packet["deep_residual_name"] += "_PAID"

    def mutate_first_match(packet: dict[str, Any]) -> None:
        packet["spine_calibration"]["charts"][2]["raw_slopes"] = [7, 11, 13]

    def mutate_shallow(packet: dict[str, Any]) -> None:
        packet["supplied_shallow_input"]["slopes"] = [7, 10]

    def mutate_pencil(packet: dict[str, Any]) -> None:
        packet["spine_calibration"]["charts"][2]["moving_root_certificate"][
            "moving_roots_per_slope"
        ] = 700_000

    def mutate_owner_order(packet: dict[str, Any]) -> None:
        packet["bucket_priority"] = ["shallow", "earlier", "bounded_pencil", "deep_residual"]

    mutations.extend([
        ("deep residual spelling", mutate_deep_name),
        ("first-match overlap", mutate_first_match),
        ("shallow SE2 slope", mutate_shallow),
        ("moving-root exact cap", mutate_pencil),
        ("bucket priority", mutate_owner_order),
    ])

    caught = 0
    for name, mutation in mutations:
        damaged = copy.deepcopy(data)
        mutation(damaged)
        try:
            verify(damaged)
        except VerificationFailure:
            caught += 1
        else:
            raise VerificationFailure(f"tamper selftest did not catch: {name}")
    return caught


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
    parser.add_argument("--check", action="store_true", help="replay all certificate gates")
    parser.add_argument(
        "--tamper-selftest",
        action="store_true",
        help="verify that five load-bearing mutations are rejected",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    try:
        data = load_json(args.certificate)
        checks = verify(data)
        print(f"RESULT: PASS ({checks} checks)")
        print(f"certificate: {args.certificate}")
        print(f"deep residual: {EXPECTED_DEEP_RESIDUAL}")
        if args.tamper_selftest:
            caught = run_tamper_selftest(data)
            print(f"TAMPER SELFTEST: PASS ({caught} mutations rejected)")
    except VerificationFailure as exc:
        print(f"RESULT: FAIL ({exc})")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
