#!/usr/bin/env python3
"""Replay the M31 C9 sixteen-root residual max-fiber certificate.

Stdlib only.  This is an independent enumeration/replay layer; Lean CI is the
proof-validation layer.  The `--emit-lean-table` mode generates the complete
key-sorted literal table consumed by `M31C9ScaleStep.lean`.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import json
from pathlib import Path
import sys
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CERT = (
    ROOT
    / "experimental/data/certificates/m31-c9-scale16-residual-max-fiber"
    / "m31_c9_scale16_residual_max_fiber.json"
)


def canonical_json(data: Any) -> str:
    return json.dumps(data, indent=2, sort_keys=True) + "\n"


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return sha1(header + data).hexdigest()


def fp2_mul(a: tuple[int, int], b: tuple[int, int], p: int) -> tuple[int, int]:
    return ((a[0] * b[0] - a[1] * b[1]) % p,
            (a[0] * b[1] + a[1] * b[0]) % p)


def fp2_pow(a: tuple[int, int], exponent: int, p: int) -> tuple[int, int]:
    result = (1, 0)
    base = a
    e = exponent
    while e:
        if e & 1:
            result = fp2_mul(result, base, p)
        base = fp2_mul(base, base, p)
        e >>= 1
    return result


def chebyshev_pow_two(x: int, depth: int, p: int) -> int:
    value = x % p
    for _ in range(depth):
        value = (2 * value * value - 1) % p
    return value


def prefix_key(mask: int, domain: list[int], p: int) -> tuple[int, int, int]:
    return tuple(
        sum(pow(domain[i], exponent, p)
            for i in range(len(domain)) if (mask >> i) & 1) % p
        for exponent in (1, 2, 3)
    )


def is_c1_owned(mask: int, antipodal_pairs: list[tuple[int, int]]) -> bool:
    return all(((mask >> a) & 1) == ((mask >> b) & 1)
               for a, b in antipodal_pairs)


def first_repeated(
    masks: Iterable[int],
    keys: dict[int, tuple[int, int, int]],
) -> tuple[tuple[int, int, int], int, int] | None:
    seen: dict[tuple[int, int, int], int] = {}
    for mask in masks:
        key = keys[mask]
        previous = seen.get(key)
        if previous is not None:
            return key, previous, mask
        seen[key] = mask
    return None


def support_indices(mask: int, n: int) -> list[int]:
    return [i for i in range(n) if (mask >> i) & 1]


def derived_roots(data: dict[str, Any]) -> tuple[list[int], list[int]]:
    domain_data = data["domain"]
    p = domain_data["field_prime"]
    generator = (domain_data["generator"]["re"], domain_data["generator"]["im"])
    bases = domain_data["base_exponents"]
    shift = domain_data["translate_step"]
    exponents = [base + j * shift for base in bases for j in range(4)]
    roots = [fp2_pow(generator, exponent, p)[0] for exponent in exponents]
    return exponents, roots


def literal_table_rows(data: dict[str, Any]) -> list[tuple[int, int, int, int]]:
    p = data["domain"]["field_prime"]
    _, roots = derived_roots(data)
    n = data["slice"]["ambient_dimension"]
    weight = data["slice"]["weight"]
    masks = [mask for mask in range(1 << n) if mask.bit_count() == weight]
    rows = [
        (mask, *prefix_key(mask, roots, p))
        for mask in masks
    ]
    rows.sort(key=lambda row: (row[1], row[2], row[3], row[0]))
    return rows


def emit_lean_table(data: dict[str, Any]) -> str:
    rows = literal_table_rows(data)
    lines = []
    for index, (mask, p1, p2, p3) in enumerate(rows):
        comma = "," if index + 1 < len(rows) else ""
        lines.append(f"  ⟨{mask}, {p1}, {p2}, {p3}⟩{comma}")
    return "\n".join(lines) + "\n"


def compute(data: dict[str, Any]) -> dict[str, Any]:
    domain_data = data["domain"]
    p = domain_data["field_prime"]
    generator = (domain_data["generator"]["re"], domain_data["generator"]["im"])
    exponents, roots = derived_roots(data)

    if fp2_mul(generator, (generator[0], (-generator[1]) % p), p) != (1, 0):
        raise AssertionError("generator norm-one check failed")
    if fp2_pow(generator, 2**30, p) != (p - 1, 0):
        raise AssertionError("generator half-order check failed")
    if fp2_pow(generator, 2**31, p) != (1, 0):
        raise AssertionError("generator full-order check failed")

    n = data["slice"]["ambient_dimension"]
    weight = data["slice"]["weight"]
    antipodal_pairs = [tuple(pair) for pair in domain_data["antipodal_pairs"]]
    full_masks = [mask for mask in range(1 << n) if mask.bit_count() == weight]
    keys = {mask: prefix_key(mask, roots, p) for mask in full_masks}
    full_fibers: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    for mask in full_masks:
        full_fibers[keys[mask]].append(mask)

    c1_masks = [mask for mask in full_masks if is_c1_owned(mask, antipodal_pairs)]
    residual_masks = [
        mask for mask in full_masks
        if not is_c1_owned(mask, antipodal_pairs)
    ]
    residual_fibers: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    for mask in residual_masks:
        residual_fibers[keys[mask]].append(mask)

    block_masks = domain_data["t4_block_masks"]
    block_swap_keys: dict[tuple[int, int, int], tuple[int, int, int]] = {}
    for left_index in range(len(block_masks)):
        for right_index in range(left_index + 1, len(block_masks)):
            left_block = block_masks[left_index]
            right_block = block_masks[right_index]
            forbidden = left_block | right_block
            for remainder in range(1 << n):
                if remainder.bit_count() != 4 or (remainder & forbidden):
                    continue
                left = left_block | remainder
                right = right_block | remainder
                if is_c1_owned(left, antipodal_pairs):
                    continue
                if is_c1_owned(right, antipodal_pairs):
                    continue
                left_key = keys[left]
                right_key = keys[right]
                if left_key != right_key:
                    raise AssertionError(
                        "claimed T4 block swap changed the prefix key"
                    )
                if left_key in block_swap_keys:
                    raise AssertionError("duplicate block-swap key")
                block_swap_keys[left_key] = (left, right, remainder)

    doubled_residual = {
        key: fiber for key, fiber in residual_fibers.items() if len(fiber) == 2
    }
    first = first_repeated(residual_masks, keys)
    if first is None:
        raise AssertionError("no residual collision found")

    full_hist = Counter(len(fiber) for fiber in full_fibers.values())
    residual_hist = Counter(len(fiber) for fiber in residual_fibers.values())
    max_full = max(full_hist)
    max_residual = max(residual_hist)
    residual_mass = len(residual_masks)
    residual_image = len(residual_fibers)
    exact_image_loss = (
        max_residual * residual_image + residual_mass - 1
    ) // residual_mass

    result = {
        "exponents": exponents,
        "roots": roots,
        "roots_nodup": len(set(roots)) == len(roots),
        "all_t_2_21_roots": all(
            chebyshev_pow_two(root, 21, p) == 0 for root in roots
        ),
        "t4_values": [
            chebyshev_pow_two(roots[4 * block], 2, p) for block in range(4)
        ],
        "t4_prefix_keys": [
            list(prefix_key(mask, roots, p)) for mask in block_masks
        ],
        "full_support_count": len(full_masks),
        "full_image_count": len(full_fibers),
        "full_histogram": {str(k): v for k, v in sorted(full_hist.items())},
        "full_max_fiber": max_full,
        "full_six_key": list(next(
            key for key, fiber in full_fibers.items() if len(fiber) == 6
        )),
        "full_six_masks": next(
            fiber for fiber in full_fibers.values() if len(fiber) == 6
        ),
        "c1_owned_support_count": len(c1_masks),
        "residual_support_count": len(residual_masks),
        "residual_image_count": len(residual_fibers),
        "residual_histogram": {
            str(k): v for k, v in sorted(residual_hist.items())
        },
        "residual_max_fiber": max_residual,
        "residual_exact_image_loss": exact_image_loss,
        "residual_loss_one_fails": (
            residual_mass < max_residual * residual_image
        ),
        "residual_loss_two_holds": (
            max_residual * residual_image <= 2 * residual_mass
        ),
        "first_repeated_key": list(first[0]),
        "first_repeated_masks": [first[1], first[2]],
        "first_repeated_supports": [
            support_indices(first[1], n), support_indices(first[2], n)
        ],
        "first_repeated_remainder": first[1] & first[2],
        "doubled_residual_key_count": len(doubled_residual),
        "block_swap_key_count": len(block_swap_keys),
        "all_doubled_keys_are_block_swaps": (
            set(doubled_residual) == set(block_swap_keys)
        ),
        "all_block_swap_fibers_exact": all(
            residual_fibers[key] == [left, right]
            for key, (left, right, _) in block_swap_keys.items()
        ),
    }
    return result


def verify_files(data: dict[str, Any]) -> None:
    for entry in data["imported_api_blobs"]:
        path = ROOT / entry["path"]
        blob = git_blob_sha(path.read_bytes())
        if blob != entry["fork_main_blob"]:
            raise AssertionError(
                f"blob mismatch for {entry['path']}: {blob} != "
                f"{entry['fork_main_blob']}"
            )
        if entry["fork_main_blob"] != entry["upstream_main_blob"]:
            raise AssertionError(f"fork/upstream blob mismatch: {entry['path']}")

    lean_path = ROOT / data["files"]["lean_module"]["path"]
    actual_sha = sha256(lean_path.read_bytes()).hexdigest()
    expected_sha = data["files"]["lean_module"]["sha256"]
    if actual_sha != expected_sha:
        raise AssertionError(
            f"Lean module sha256 mismatch: {actual_sha} != {expected_sha}"
        )

    source = lean_path.read_text(encoding="utf-8")
    forbidden = [
        "native_decide",
        "M31C9RowSharp",
        "HalfSliceFalsifier",
        "sorry",
        "admit",
        "axiom ",
        "eraseDups",
        ".contains",
        "def unsortedTable",
    ]
    for token in forbidden:
        if token in source:
            raise AssertionError(f"forbidden Lean token/import present: {token}")
    required = [
        "set_option maxRecDepth 1000000",
        "def sortedTable : List TableRow := [",
        "theorem sorted_table_key_recomputation",
        "theorem sorted_table_mask_column_complete",
        "theorem scale_step_summary_exact",
        "#print axioms scale_step_summary_exact",
    ]
    for token in required:
        if token not in source:
            raise AssertionError(f"required Lean marker absent: {token}")


def check(certificate_path: Path) -> None:
    raw = certificate_path.read_text(encoding="utf-8")
    data = json.loads(raw)
    if raw != canonical_json(data):
        raise AssertionError("certificate JSON is not canonical")

    verify_files(data)
    result = compute(data)
    expected = data["computed"]
    if result != expected:
        raise AssertionError(
            "enumeration mismatch\nexpected="
            + canonical_json(expected)
            + "actual="
            + canonical_json(result)
        )

    rows = literal_table_rows(data)
    if len(rows) != result["full_support_count"]:
        raise AssertionError("literal table row count mismatch")
    if rows != sorted(rows, key=lambda row: (row[1], row[2], row[3], row[0])):
        raise AssertionError("literal table generator is not key sorted")

    if data["acceptance_gate"]["primary"] != 4:
        raise AssertionError("primary acceptance gate must be criterion 4")
    if data["acceptance_gate"]["additional"] != 2:
        raise AssertionError("additional acceptance gate must be criterion 2")
    if not result["all_doubled_keys_are_block_swaps"]:
        raise AssertionError("block-swap obstruction classification failed")
    if result["residual_max_fiber"] != 2:
        raise AssertionError("scaled residual maximum is not exactly two")

    print(
        "PASS m31-c9-scale16-residual-max-fiber "
        f"full={result['full_support_count']} "
        f"residual={result['residual_support_count']} "
        f"image={result['residual_image_count']} "
        f"max={result['residual_max_fiber']} "
        f"doubled={result['doubled_residual_key_count']}"
    )


def tamper_selftest(certificate_path: Path) -> None:
    data = json.loads(certificate_path.read_text(encoding="utf-8"))
    data["computed"]["residual_max_fiber"] = 1
    try:
        actual = compute(data)
        if actual == data["computed"]:
            raise AssertionError("tamper self-test failed to detect mutation")
    except AssertionError:
        raise
    print("PASS tamper-selftest: residual max mutation rejected")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERT)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--tamper-selftest", action="store_true")
    mode.add_argument("--emit-lean-table", action="store_true")
    args = parser.parse_args()

    try:
        if args.emit_lean_table:
            data = json.loads(args.certificate.read_text(encoding="utf-8"))
            sys.stdout.write(emit_lean_table(data))
        elif args.check:
            check(args.certificate)
        else:
            tamper_selftest(args.certificate)
    except (AssertionError, KeyError, OSError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
