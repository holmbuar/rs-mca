#!/usr/bin/env python3
"""Stdlib-only replay for the M31 common-core add-back packet."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "experimental/data/certificates/m31-common-core-addback/m31_common_core_addback.json"
MODULE = ROOT / "experimental/lean/sidon_effective_image/SidonEffectiveImage/M31CommonCoreAddBack.lean"
ROOT_MODULE = ROOT / "experimental/lean/sidon_effective_image/SidonEffectiveImage.lean"
IMPORTS = ["import AsymptoticSpine.FirstMatch", "import M31QRootedShell.Deployed"]
ROOT_IMPORT = "import SidonEffectiveImage.M31CommonCoreAddBack"


def payload_hash(data: dict[str, Any]) -> str:
    body = copy.deepcopy(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def sweep_hash(n: int, k: int, a: int, radius: int, cap: int) -> str:
    h = hashlib.sha256()
    for c in range(cap + 1):
        nl, rr = n - c, radius - c
        d = nl - k + 1
        h.update(f"{c}:{nl}:{rr}:{nl-k}:{d}:{d-rr}\n".encode())
    return h.hexdigest()


def need(errors: list[str], ok: bool, message: str) -> None:
    if not ok:
        errors.append(message)


def verify(data: dict[str, Any], files: bool = True) -> list[str]:
    e: list[str] = []
    need(e, data.get("payload_sha256") == payload_hash(data), "payload hash")
    need(e, data.get("artifact_kind") == "M31_COMMON_CORE_ADD_BACK", "artifact kind")
    need(e, data.get("schema_version") == 1, "schema version")

    row = {
        "name": "Mersenne-31 list", "object": "LIST", "target_epsilon": "2^-100",
        "p": 2147483647, "n": 2097152, "K": 1048576,
        "agreement": 1116023, "radius": 981129, "w": 67447, "B_star": 16777215,
    }
    frame = {
        "padded_first_cap": 20765, "padded_first_two_cap": 41530,
        "padded_first_three_cap": 62295, "padded_margin_to_w": 5152,
        "marked_source_key_floor": 259881, "signed_occupancy_allowance": 259880,
        "signed_occupancy_baseline": 16517335, "forbidden_list_size": 16777216,
    }
    need(e, data.get("row") == row, "row constants")
    need(e, data.get("padded_frame") == frame, "frame constants")

    n, k, a, radius, w = row["n"], row["K"], row["agreement"], row["radius"], row["w"]
    cap = frame["padded_first_three_cap"]
    need(e, radius == n - a and w == a - k, "row identities")
    need(e, cap < w and w - cap == 5152, "frame margin")

    rows = 0
    min_n, min_r, min_nk, min_gap = n, radius, n - k, None
    dim_ok = agr_ok = radius_ok = excess_ok = True
    for c in range(cap + 1):
        rows += 1
        nl, rr = n - c, radius - c
        dist = nl - k + 1
        min_n, min_r, min_nk = min(min_n, nl), min(min_r, rr), min(min_nk, nl - k)
        gap = dist - rr
        min_gap = gap if min_gap is None else min(min_gap, gap)
        dim_ok &= nl >= k
        agr_ok &= nl >= a
        radius_ok &= rr == nl - a
        excess_ok &= nl - k == w + rr and gap == w + 1
    sweep = {
        "core_degree_min": 0, "core_degree_max": cap, "rows_checked": rows,
        "min_short_length": min_n, "min_short_radius": min_r,
        "min_short_length_minus_K": min_nk,
        "min_short_distance_minus_radius": min_gap,
        "all_dimension_gates": dim_ok, "all_agreement_gates": agr_ok,
        "all_radius_identities": radius_ok, "all_excess_identities": excess_ok,
        "sweep_sha256": sweep_hash(n, k, a, radius, cap),
    }
    need(e, data.get("shortening_sweep") == sweep, "enumeration summary")

    ledger = {
        "baseline_plus_floor": 16777216, "B_star_plus_one": 16777216,
        "allowance_plus_one": 259881, "add_back_factor": 1,
        "source_key_map": "POINTWISE_LENGTH_PRESERVING",
        "selectors": "DEFINITIONALLY_PRESERVED",
        "root_masks": "DEFINITIONALLY_PRESERVED",
        "owners_refunds_signed_credits": "DEFINITIONALLY_PRESERVED",
    }
    need(e, data.get("source_ledger") == ledger, "source ledger")
    need(e, ledger["baseline_plus_floor"] == ledger["B_star_plus_one"], "signed crossing")
    need(e, ledger["allowance_plus_one"] == frame["marked_source_key_floor"], "allowance")

    terminal = {
        "acceptance_criterion": 3,
        "before": "UNPAID_COMMON_CORE_ADD_BACK",
        "after": "PROVED_COMMON_CORE_LOSS_ONE_ADDBACK",
        "remaining": "UNPAID_CANONICAL_LOCATOR_NUMERATOR_ESCAPE_OWNER_REFUND",
        "deployed_atom_moved": False,
    }
    need(e, data.get("terminal") == terminal, "terminal transition")

    blobs = {
        "experimental/lean/asymptotic_spine/AsymptoticSpine/FirstMatch.lean": {
            "fork": "44592371660c453c1f8522abb9c0f9364e4dd43d",
            "upstream": "44592371660c453c1f8522abb9c0f9364e4dd43d",
            "verdict": "BYTE_IDENTICAL",
        },
        "experimental/lean/m31_q_rooted_shell/M31QRootedShell/Deployed.lean": {
            "fork": "7e21ff098567d26aba7330fbb2722d5cb952fb09",
            "upstream": "7e21ff098567d26aba7330fbb2722d5cb952fb09",
            "verdict": "BYTE_IDENTICAL",
        },
    }
    need(e, data.get("import_blob_identity") == blobs, "import blobs")
    source_blobs = {
        "experimental/notes/thresholds/m31_canonical_popov_rank46_compiler.md": "11a1882d88ff8a3f725e61c0ce427cdaaa716fe9",
        "pr1014:experimental/notes/audits/m31_padding_bridge_audit.md": "85ec62a4594e292456e6e7acf26394c73e2af34c",
        "pr1025:experimental/notes/audits/m31_masked_diagonal_saturation.md": "cbb63ec62af7931b3fdb868f8d3745c8822edb09",
        "pr1022:experimental/notes/thresholds/m31_direct_padded_forney_frame_route_cut.md": "4e2652b5486e1f8d06b239142951cc7a6610451c",
    }
    need(e, data.get("source_note_git_blobs") == source_blobs, "source blobs")
    required = {
        "no row-sharp Q", "no list-interior coverage", "no adjacent-row closure",
        "no shortened-component payment or semantic owner/refund",
        "no M31 row upper bound or deployed atom",
    }
    need(e, required <= set(data.get("nonclaims", [])), "nonclaims")

    if files:
        need(e, ROOT_MODULE.read_text().strip() == ROOT_IMPORT, "package root")
        text = MODULE.read_text()
        imports = [x.strip() for x in text.splitlines() if x.strip().startswith("import ")]
        need(e, imports == IMPORTS, "direct imports")
        for token in ("M31C9RowSharp", "HalfSliceFalsifier", "MaskedDiagonalSaturation", "PaddingBridgeAudit"):
            need(e, token not in "\n".join(imports), f"forbidden import {token}")
        for label, pattern in {
            "sorry": r"\bsorry\b", "admit": r"\badmit\b",
            "native_decide": r"\bnative_decide\b", "Mathlib": r"\bMathlib\b",
            "custom axiom": r"(?m)^\s*axiom\s+", "unsafe": r"(?m)^\s*unsafe\s+",
        }.items():
            need(e, re.search(pattern, text) is None, label)
        need(e, text.count("#print axioms") >= 24, "axiom print census")
    return e


def load() -> dict[str, Any]:
    value = json.loads(CERT.read_text())
    if not isinstance(value, dict):
        raise ValueError("certificate root is not an object")
    return value


def check() -> int:
    data = load()
    errors = verify(data)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    s = data["shortening_sweep"]
    print(f"PASS m31_common_core_addback: rows={s['rows_checked']} core_max={s['core_degree_max']} min_length={s['min_short_length']} min_radius={s['min_short_radius']} terminal=PROVED_COMMON_CORE_LOSS_ONE_ADDBACK")
    return 0


def tamper() -> int:
    original = load()
    mutations = [
        lambda d: d["padded_frame"].__setitem__("padded_first_three_cap", 62296),
        lambda d: d["shortening_sweep"].__setitem__("min_short_length", 2034858),
        lambda d: d["shortening_sweep"].__setitem__("min_short_radius", 918835),
        lambda d: d["padded_frame"].__setitem__("marked_source_key_floor", 259880),
        lambda d: d["source_ledger"].__setitem__("add_back_factor", 2),
        lambda d: d["terminal"].__setitem__("after", "UNPAID"),
        lambda d: d["import_blob_identity"][next(iter(d["import_blob_identity"]))].__setitem__("fork", "0" * 40),
        lambda d: d["shortening_sweep"].__setitem__("sweep_sha256", "0" * 64),
    ]
    for i, mutate in enumerate(mutations, 1):
        candidate = copy.deepcopy(original)
        mutate(candidate)
        candidate["payload_sha256"] = payload_hash(candidate)
        if not verify(candidate, files=False):
            print(f"FAIL: mutation {i} accepted", file=sys.stderr)
            return 1
    print(f"PASS tamper-selftest: rejected {len(mutations)}/{len(mutations)} mutations")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    return check() if args.check else tamper()


if __name__ == "__main__":
    raise SystemExit(main())
