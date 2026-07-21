#!/usr/bin/env python3
"""Verify the exact M31 fixed-remainder dyadic route-cut certificate."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
from typing import Any

SCHEMA = "rs-mca-m31-fixed-remainder-dyadic-route-cut-v1"
CERT_REL = Path(
    "experimental/data/certificates/"
    "m31-fixed-remainder-dyadic-route-cut/"
    "m31_fixed_remainder_dyadic_route_cut.json"
)

EXPECTED_SOURCE_BLOBS = {
    "agents.md": "6cb0090bf92b356033050b4be2a27f14484bff53",
    "experimental/grande_finale.tex": "8a5d9791900ca9eed773feba146b92ad296704ce",
    "tex/cs25_cap_v13_2.tex": "5ceff5dbc4b1ac4cef53eae7eada32046e4bafeb",
    "experimental/notes/frontier-adjacent/four_row_exact_completion_compiler_v1.md":
        "375f99c02d59cefb6842b91115f07b88e2e258cc",
    "experimental/data/certificates/four-row-exact-completion-compiler-v1/"
    "four_row_exact_completion_compiler_v1.json":
        "357cf4865a04f3db78eda39c983a2d1ef79451e1",
    "experimental/lean/m31_q_rooted_shell/M31QRootedShell/Envelope.lean":
        "2bd4a5b051f482bfe222917e10d302b997a9c6ed",
    "experimental/lean/m31_q_rooted_shell/M31QRootedShell/Deployed.lean":
        "7e21ff098567d26aba7330fbb2722d5cb952fb09",
}

EXPECTED_IMPORTED_APIS = {
    "experimental/lean/m31_q_rooted_shell/M31QRootedShell/Envelope.lean":
        "2bd4a5b051f482bfe222917e10d302b997a9c6ed",
    "experimental/lean/m31_q_rooted_shell/M31QRootedShell/Deployed.lean":
        "7e21ff098567d26aba7330fbb2722d5cb952fb09",
}


def canonical_payload(data: dict[str, Any]) -> bytes:
    payload = copy.deepcopy(data)
    payload.pop("payload_sha256", None)
    return json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def payload_sha256(data: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_payload(data)).hexdigest()


def is_prime_32(n: int) -> bool:
    """Deterministic Miller--Rabin for the 32-bit input used here."""
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for q in small:
        if n == q:
            return True
        if n % q == 0:
            return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in (2, 3, 5, 7, 11):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def expected_rows(n: int, m: int, w: int) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for exponent in range(1, 22):
        c = 1 << exponent
        quotient_fibers = n // c
        complete_fibers, remainder = divmod(m, c)
        visible = remainder <= w and complete_fibers > 0
        if visible:
            cap = 0
            route = "C1_QUOTIENT_REMAINDER"
        else:
            # The late rows all have a nonempty fixed remainder, so at least
            # one quotient value is unavailable to the complete-fiber set E.
            if remainder <= 0:
                raise ValueError("late route unexpectedly has empty remainder")
            cap = math.comb(quotient_fibers - 1, complete_fibers)
            route = "SMALL_FIXED_REMAINDER"
        rows.append(
            {
                "exponent": exponent,
                "fiberSize": c,
                "quotientFibers": quotient_fibers,
                "completeFibers": complete_fibers,
                "remainder": remainder,
                "visible": visible,
                "cap": cap,
                "route": route,
            }
        )
    return rows


def validate(data: dict[str, Any], *, recompute_average: bool = True) -> list[str]:
    errors: list[str] = []

    def check(condition: bool, label: str) -> None:
        if not condition:
            errors.append(label)

    check(data.get("schema") == SCHEMA, "schema")
    check(
        data.get("payload_sha256") == payload_sha256(data),
        "payload_sha256",
    )

    base = data.get("base", {})
    check(
        base.get("fork_main_sha")
        == "4e5f0b77c98f075ea7c8822cd4859847a232bc2a",
        "fork_main_sha",
    )
    check(
        base.get("upstream_main_sha")
        == "a3017697ad1594521d2779fe1d83bccd45d4c06e",
        "upstream_main_sha",
    )
    check(base.get("fork_contains_upstream_main") is True, "fork_contains_upstream")
    check(
        base.get("branch") == "gptpro/m31-rowsharp-falsifier",
        "branch",
    )

    gate = data.get("acceptance_gate", {})
    check(gate.get("criterion_4_witness_found") is False, "criterion4_false")
    check(gate.get("fallback_gate") == "NAMED_ROUTE_CUT", "named_route_cut_gate")
    check(
        gate.get("route_cut_name")
        == "M31_FIXED_REMAINDER_DYADIC_FOLD_ROUTE_CUT",
        "route_cut_name",
    )
    check(gate.get("ledger_movement") == 0, "ledger_movement_zero")

    deployed = data.get("deployed_row", {})
    p = 2**31 - 1
    n = 2**21
    k = 2**20
    agreement = 1_116_023
    m = n - agreement
    w = agreement - k
    b_star = 2**24 - 1

    exact_constants = {
        "row_id": "m31_list",
        "p": p,
        "n": n,
        "k": k,
        "agreement": agreement,
        "support_complement_m": m,
        "prefix_depth_w": w,
        "budget_B_star": b_star,
    }
    for key, expected in exact_constants.items():
        check(deployed.get(key) == expected, f"deployed:{key}")

    check(is_prime_32(p), "p_is_prime")
    check(p**4 // 2**100 == b_star, "budget_formula")

    if recompute_average:
        numerator = math.comb(n, m)
        denominator = p**w
        average_floor, remainder = divmod(numerator, denominator)
        average_ceiling = average_floor + int(remainder != 0)
        multiplier_floor = b_star * denominator // numerator
        check(
            deployed.get("full_slice_average_floor") == average_floor,
            "average_floor",
        )
        check(
            deployed.get("full_slice_average_ceiling") == average_ceiling,
            "average_ceiling",
        )
        check(
            deployed.get("full_budget_multiplier_floor") == multiplier_floor,
            "multiplier_floor",
        )
        check(
            deployed.get("binomial_bit_length") == numerator.bit_length(),
            "binomial_bit_length",
        )
        check(
            deployed.get("prefix_denominator_bit_length")
            == denominator.bit_length(),
            "denominator_bit_length",
        )
        check(multiplier_floor == 8, "binding_multiplier_is_eight")
        check(8 * average_ceiling <= b_star < 9 * average_ceiling,
              "ceiling_margin_bracket")

    rows = data.get("dyadic_rows")
    expected = expected_rows(n, m, w)
    check(rows == expected, "dyadic_rows_exact")

    terminal = data.get("terminal", {})
    late_caps = [row["cap"] for row in expected if not row["visible"]]
    check(
        terminal.get("c1_owned_scale_exponents") == list(range(1, 18)),
        "c1_exponents",
    )
    check(
        terminal.get("late_scale_exponents") == [18, 19, 20, 21],
        "late_exponents",
    )
    check(terminal.get("late_fixed_R_caps") == [35, 3, 1, 1], "late_caps")
    check(max(late_caps) == 35, "late_cap_recomputed")
    check(terminal.get("max_late_fixed_R_cap") == 35, "late_cap_recorded")
    check(35 < deployed.get("full_slice_average_ceiling", 0), "cap_below_average")
    check(35 < b_star, "cap_below_budget")
    check(
        terminal.get("post_C1_margin_breach_in_named_family") is False,
        "no_named_family_breach",
    )
    check(
        expected[0]["route"] == "C1_QUOTIENT_REMAINDER"
        and expected[0]["fiberSize"] == 2,
        "antipodal_scale_routed",
    )
    check(
        expected[1]["route"] == "C1_QUOTIENT_REMAINDER"
        and expected[1]["fiberSize"] == 4,
        "T4_scale_routed",
    )

    scalar = data.get("global_scalar_symmetry", {})
    lead = pow(2, n - 1, p)
    next_coeff = (-n * pow(2, n - 3, p)) % p
    monic_next = next_coeff * pow(lead, -1, p) % p
    check(scalar.get("standard_leading_coefficient_mod_p") == lead, "cheb_lead")
    check(scalar.get("standard_next_coefficient_mod_p") == next_coeff,
          "cheb_next")
    check(scalar.get("monic_next_coefficient_mod_p") == monic_next,
          "cheb_monic_next")
    check(next_coeff != 0 and monic_next != 0, "cheb_next_nonzero")
    check(lead == 2, "cheb_lead_exact")
    check(next_coeff == p - 2**20, "cheb_next_exact")

    check(
        data.get("source_bindings_git_blob_sha") == EXPECTED_SOURCE_BLOBS,
        "source_bindings",
    )
    imported_rows = data.get("imported_api_blob_identity", [])
    imported = {
        row.get("path"): row
        for row in imported_rows
        if isinstance(row, dict) and isinstance(row.get("path"), str)
    }
    check(set(imported) == set(EXPECTED_IMPORTED_APIS), "imported_api_paths")
    for path, blob in EXPECTED_IMPORTED_APIS.items():
        row = imported.get(path, {})
        check(row.get("fork_main_blob") == blob, f"fork_blob:{path}")
        check(row.get("upstream_main_blob") == blob, f"upstream_blob:{path}")
        check(row.get("byte_identical") is True, f"blob_identity:{path}")

    nonclaims = data.get("nonclaims", [])
    required_nonclaim_fragments = (
        "does not construct a deployed M31 list-row counterexample",
        "does not prove the full M31 row-sharp Q target",
        "isolated multiplicative cosets",
        "does not move a deployed row ledger term",
        "does not close an adjacent row",
    )
    for fragment in required_nonclaim_fragments:
        check(any(fragment in item for item in nonclaims), f"nonclaim:{fragment}")

    return errors


def tamper_selftest(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []

    mutations: list[tuple[str, Any]] = []

    x = copy.deepcopy(data)
    x["dyadic_rows"][17]["cap"] = 36
    mutations.append(("late cap 35 -> 36", x))

    x = copy.deepcopy(data)
    x["dyadic_rows"][1]["route"] = "SMALL_FIXED_REMAINDER"
    mutations.append(("T4 route removed", x))

    x = copy.deepcopy(data)
    x["deployed_row"]["prefix_depth_w"] += 1
    mutations.append(("prefix depth drift", x))

    x = copy.deepcopy(data)
    x["acceptance_gate"]["criterion_4_witness_found"] = True
    mutations.append(("false criterion-4 promotion", x))

    x = copy.deepcopy(data)
    x["imported_api_blob_identity"][0]["upstream_main_blob"] = "0" * 40
    mutations.append(("API blob mismatch", x))

    x = copy.deepcopy(data)
    x["terminal"]["post_C1_margin_breach_in_named_family"] = True
    mutations.append(("false margin breach", x))

    for name, mutated in mutations:
        mutated["payload_sha256"] = payload_sha256(mutated)
        if not validate(mutated, recompute_average=False):
            failures.append(name)

    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--tamper-selftest", action="store_true")
    parser.add_argument("--certificate", type=Path)
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[2]
    cert_path = args.certificate or repo_root / CERT_REL
    data = json.loads(cert_path.read_text(encoding="utf-8"))

    if args.tamper_selftest:
        failures = tamper_selftest(data)
        if failures:
            print("TAMPER SELFTEST FAIL:", ", ".join(failures))
            return 1
        print("TAMPER SELFTEST PASS (6/6)")
        return 0

    errors = validate(data, recompute_average=True)
    if errors:
        print("RESULT: FAIL")
        for error in errors:
            print(f" - {error}")
        return 1

    print("RESULT: PASS")
    print("terminal: M31_FIXED_REMAINDER_DYADIC_FOLD_ROUTE_CUT")
    print("dyadic scales checked: 21")
    print("post-C1 fixed-remainder cap on unrouted scales: 35")
    print("criterion-4 deployed witness: NOT FOUND")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
