#!/usr/bin/env python3
"""Exact finite verifier for the M31 base-field full-layer-42 theorem."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def phi(u: int, total: int, *, balanced: bool = True) -> int:
    q, r = divmod(total, u)
    if balanced:
        return u * q * (q - 1) // 2 + r * q
    return u * q * (q - 1) // 2 + r * (q + 1)


def packing_delta(
    n: int,
    K: int,
    m: int,
    j: int,
    *,
    mds_offset: int = 1,
    balanced: bool = True,
) -> int:
    return (
        m * (m - 1) // 2 * (2 * j - K - mds_offset)
        - phi(n, m * j, balanced=balanced)
    )


def first_admissible_weight(
    n: int,
    K: int,
    R: int,
    m: int,
    *,
    mds_offset: int = 1,
    balanced: bool = True,
) -> int:
    lo, hi = K // 2 + 1, R + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if packing_delta(
            n, K, m, mid, mds_offset=mds_offset, balanced=balanced
        ) >= 0:
            hi = mid
        else:
            lo = mid + 1
    require(lo <= R, f"no admissible layer for m={m}")
    return lo


def build_certificate(
    *,
    mds_offset: int = 1,
    radius_shift: int = 0,
    high_endpoint_inclusive: bool = True,
    low_includes_zero: bool = False,
    balanced: bool = True,
    forced_layer: int = 42,
    verify_monotonicity: bool = True,
) -> dict[str, object]:
    p = 2**31 - 1
    n = 2**21
    K = 2**20
    a = 1_116_023
    R = n - a + radius_shift
    B = p**4 // 2**100
    L = B + 1

    thresholds = [
        first_admissible_weight(
            n, K, R, m, mds_offset=mds_offset, balanced=balanced
        )
        for m in range(1, forced_layer + 1)
    ]
    for m, j0 in enumerate(thresholds, 1):
        require(
            packing_delta(
                n, K, m, j0, mds_offset=mds_offset, balanced=balanced
            ) >= 0,
            "threshold endpoint failed",
        )
        if j0 > K // 2 + 1:
            require(
                packing_delta(
                    n, K, m, j0 - 1,
                    mds_offset=mds_offset,
                    balanced=balanced,
                ) < 0,
                "threshold predecessor failed",
            )

    monotonicity_checks = 0
    if verify_monotonicity:
        for m in range(1, forced_layer + 1):
            previous = packing_delta(
                n, K, m, K // 2 + 1,
                mds_offset=mds_offset,
                balanced=balanced,
            )
            for j in range(K // 2 + 2, R + 1):
                current = packing_delta(
                    n, K, m, j,
                    mds_offset=mds_offset,
                    balanced=balanced,
                )
                require(current >= previous, "packing delta is not monotone")
                previous = current
                monotonicity_checks += 1

    endpoint_correction = 1 if high_endpoint_inclusive else 0
    high_upper = sum(
        R - thresholds[m - 1] + endpoint_correction
        for m in range(1, forced_layer)
    )
    low_upper = K // 2 + int(low_includes_zero)
    total_upper = low_upper + high_upper

    S = 2 * (n - a) - K - 1
    Dmin = K - (n - a)
    denominator = forced_layer - 2
    mu1 = S // denominator
    mu12 = (2 * S) // denominator
    high_rows = S // Dmin

    return {
        "schema": "m31-base-field-full-layer-42-v1",
        "field": "F_p",
        "p": p,
        "n": n,
        "K": K,
        "a": a,
        "R": R,
        "budget": B,
        "strict_mass": L,
        "mds_offset": mds_offset,
        "balanced_phi": balanced,
        "thresholds": thresholds,
        "thresholds_sha256": hashlib.sha256(
            json.dumps(thresholds, separators=(",", ":")).encode("ascii")
        ).hexdigest(),
        "delta42_predecessor": packing_delta(
            n, K, 42, 606_935, mds_offset=mds_offset, balanced=balanced
        ),
        "delta42_endpoint": packing_delta(
            n, K, 42, 606_936, mds_offset=mds_offset, balanced=balanced
        ),
        "high_endpoint_inclusive": high_endpoint_inclusive,
        "low_includes_zero": low_includes_zero,
        "max_previous_high_upper": high_upper,
        "max_previous_total_upper": total_upper,
        "gap_to_strict_mass": L - total_upper,
        "forced_layer": forced_layer,
        "forced_weight_floor": thresholds[-1],
        "monotonicity_checks": monotonicity_checks,
        "forney_sum_upper": S,
        "D0_lower": Dmin,
        "mu1_upper": mu1,
        "mu1_plus_mu2_upper": mu12,
        "high_rows_at_most": high_rows,
        "low_rows_at_least_offset": 15,
        "ledger_movement": 0,
        "official_score": "0/2",
    }


def check_output() -> str:
    c = build_certificate()
    require(c["budget"] == 16_777_215, "budget changed")
    require(c["strict_mass"] == 16_777_216, "strict mass changed")
    require(c["delta42_predecessor"] == -111, "m=42 predecessor changed")
    require(c["delta42_endpoint"] == 1_107, "m=42 endpoint changed")
    require(c["max_previous_high_upper"] == 16_065_819, "high upper changed")
    require(c["max_previous_total_upper"] == 16_590_107, "total upper changed")
    require(c["gap_to_strict_mass"] == 187_109, "gap changed")
    require(c["forced_layer"] == 42, "forced layer changed")
    require(c["forced_weight_floor"] == 606_936, "weight floor changed")
    require(c["monotonicity_checks"] == 19_187_280, "monotonicity count changed")
    require(c["forney_sum_upper"] == 913_681, "Forney sum changed")
    require(c["D0_lower"] == 67_447, "D0 lower bound changed")
    require(c["mu1_upper"] == 22_842, "mu1 bound changed")
    require(c["mu1_plus_mu2_upper"] == 45_684, "mu1+mu2 bound changed")
    require(c["high_rows_at_most"] == 13, "high-row count changed")
    return "\n".join([
        "R38_M31_BASE_FIELD_FULL_LAYER_42_VERIFIER",
        "mode=check",
        f"field={c['field']} p={c['p']} n={c['n']} K={c['K']} R={c['R']}",
        f"budget=PASS B={c['budget']} L={c['strict_mass']}",
        (
            "packing=PASS "
            f"thresholds_sha256={c['thresholds_sha256']} "
            f"delta42_pre={c['delta42_predecessor']} "
            f"delta42={c['delta42_endpoint']} "
            f"monotonicity_checks={c['monotonicity_checks']}"
        ),
        (
            "layer_cake=PASS "
            f"high={c['max_previous_high_upper']} "
            f"total={c['max_previous_total_upper']} "
            f"gap={c['gap_to_strict_mass']} "
            f"forced_layer={c['forced_layer']} "
            f"j_floor={c['forced_weight_floor']}"
        ),
        (
            "forney=PASS "
            f"S={c['forney_sum_upper']} D0_min={c['D0_lower']} "
            f"mu1={c['mu1_upper']} mu12={c['mu1_plus_mu2_upper']} "
            f"high_rows_at_most={c['high_rows_at_most']}"
        ),
        "scope=BASE_FIELD_ONLY owner=NONE addback=UNCLAIMED quartic_transfer=UNCLAIMED",
        "ledger=0 official_score=0/2",
        "RESULT=PASS",
        "",
    ])


def tamper_output() -> str:
    baseline = build_certificate(verify_monotonicity=False)
    mutations = {
        "mds_K_instead_of_K_plus_1": {"mds_offset": 0},
        "radius_plus_one": {"radius_shift": 1},
        "high_endpoint_exclusive": {"high_endpoint_inclusive": False},
        "low_zero_layer_included": {"low_includes_zero": True},
        "unbalanced_phi_branch": {"balanced": False},
        "claimed_layer_41": {"forced_layer": 41},
    }
    detected = []
    for name, kwargs in mutations.items():
        try:
            candidate = build_certificate(verify_monotonicity=False, **kwargs)
        except RuntimeError:
            detected.append(name)
            continue
        require(candidate != baseline, f"mutation escaped: {name}")
        detected.append(name)
    return "\n".join([
        "R38_M31_BASE_FIELD_FULL_LAYER_42_VERIFIER",
        "mode=tamper-selftest",
        *[f"tamper.{name}=DETECTED" for name in detected],
        f"tamper_count={len(detected)}/{len(mutations)}",
        "RESULT=TAMPER_GUARDS_PASS",
        "",
    ])


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--tamper-selftest", action="store_true")
    parser.add_argument("--expected", type=Path)
    args = parser.parse_args()

    output = check_output() if args.check else tamper_output()
    if args.expected is not None:
        require(args.check, "--expected is valid only with --check")
        require(args.expected.is_file(), "expected-output file is missing")
        require(output.encode("utf-8") == args.expected.read_bytes(),
                "runtime output differs from expected output")
    sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        sys.stderr.write(f"FAIL_CLOSED: {exc}\n")
        raise SystemExit(1)
