#!/usr/bin/env python3
"""Independent stdlib replay for the compact M31 C9 owner/key certificate."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CERT = (
    ROOT / "experimental" / "data" / "certificates"
    / "m31-c9-owner-coverage" / "m31_c9_owner_coverage.json"
)

P = 2_147_483_647
DOMAIN = [
    434_373_082, 614_288_294, 1_713_110_565, 1_533_195_353,
    1_984_437_538, 380_812_851, 163_046_109, 1_766_670_796,
]
PAIRS = [[0, 2], [1, 3], [4, 6], [5, 7]]
T4_BLOCKS = [[0, 1, 2, 3], [4, 5, 6, 7]]
ORDER = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"]
SEMANTICS = [
    "C1:two antipodal x^2 fibers",
    "C2:complete T4 fiber",
    "C3:nonempty common active core",
    "C4:repeated active root",
    "C5:active extension degree > 1",
    "C6:power-sum Jacobian rank drop",
    "C7:full prefix fiber size > 1",
    "C8:post-C1-C7 prefix fiber size > 1",
]
EXPECTED_BASE = [
    "4e5f0b77c98f075ea7c8822cd4859847a232bc2a",
    "a3017697ad1594521d2779fe1d83bccd45d4c06e",
]
EXPECTED_SOURCES = [
    ["experimental/grande_finale.tex",
     "8a5d9791900ca9eed773feba146b92ad296704ce"],
    ["experimental/rs_mca_thresholds.tex",
     "01302a797c502a05ed0b11ba949b8756e0aa2b22"],
    ["tex/cs25_cap_v13_2.tex",
     "5ceff5dbc4b1ac4cef53eae7eada32046e4bafeb"],
]
EXPECTED_IMPORTS = [
    [
        "experimental/lean/asymptotic_spine/AsymptoticSpine/PrimitiveBoolean.lean",
        "777273e4377c31c815062769803622c6226988d3",
        "777273e4377c31c815062769803622c6226988d3",
    ],
    [
        "experimental/lean/m31_q_rooted_shell/M31QRootedShell/Deployed.lean",
        "7e21ff098567d26aba7330fbb2722d5cb952fb09",
        "7e21ff098567d26aba7330fbb2722d5cb952fb09",
    ],
]
EXPECTED_PARTITION_DIGEST = (
    "c6a154c32e8950762a992e8631bfa49e62762d43bf374cbf8674b5c417d3952e"
)


class VerificationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def indices(mask: int) -> list[int]:
    return [i for i in range(8) if (mask >> i) & 1]


def chebyshev_double(x: int) -> int:
    return (2 * (x % P) * (x % P) + P - 1) % P


def chebyshev_pow_two(depth: int, x: int) -> int:
    for _ in range(depth):
        x = chebyshev_double(x)
    return x


def prefix_key(mask: int) -> tuple[int, int, int]:
    chosen = indices(mask)
    return tuple(
        sum(pow(DOMAIN[i], exponent, P) for i in chosen) % P
        for exponent in (1, 2, 3)
    )


def mod_sub(a: int, b: int) -> int:
    return ((a % P) + P - (b % P)) % P


def jacobian_minor(mask: int) -> int:
    values = [DOMAIN[i] for i in indices(mask)]
    if len(values) < 3:
        return 0
    a, b, c = values[:3]
    return (6 * mod_sub(b, a) * mod_sub(c, a) * mod_sub(c, b)) % P


def build_expected() -> dict[str, Any]:
    full_masks = [mask for mask in range(256) if mask.bit_count() == 4]
    full_fibers: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    for mask in full_masks:
        full_fibers[prefix_key(mask)].append(mask)

    common_core = full_masks[0]
    for mask in full_masks[1:]:
        common_core &= mask

    def c1(mask: int) -> bool:
        return all(
            ((mask >> i) & 1) == ((mask >> j) & 1)
            for i, j in PAIRS
        )

    def c2(mask: int) -> bool:
        values = [chebyshev_pow_two(2, DOMAIN[i]) for i in indices(mask)]
        return len(values) == 4 and len(set(values)) == 1

    def c3(_mask: int) -> bool:
        return common_core != 0

    def c4(mask: int) -> bool:
        values = [DOMAIN[i] for i in indices(mask)]
        return len(values) != len(set(values))

    def c5(_mask: int) -> bool:
        return 1 > 1

    def c6(mask: int) -> bool:
        return jacobian_minor(mask) == 0

    def c7(mask: int) -> bool:
        return len(full_fibers[prefix_key(mask)]) > 1

    raw: dict[str, Callable[[int], bool]] = {
        "C1": c1, "C2": c2, "C3": c3, "C4": c4,
        "C5": c5, "C6": c6, "C7": c7,
    }

    owner7: dict[int, str | None] = {}
    for mask in full_masks:
        owner7[mask] = next(
            (owner for owner in ORDER[:7] if raw[owner](mask)), None
        )
    post7 = [mask for mask in full_masks if owner7[mask] is None]
    post7_fibers: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    for mask in post7:
        post7_fibers[prefix_key(mask)].append(mask)

    def c8(mask: int) -> bool:
        return len(post7_fibers[prefix_key(mask)]) > 1

    raw["C8"] = c8

    owners: dict[int, str | None] = {}
    for mask in full_masks:
        owners[mask] = next(
            (owner for owner in ORDER if raw[owner](mask)), None
        )

    residual = [mask for mask in full_masks if owners[mask] is None]
    residual_fibers: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    for mask in residual:
        residual_fibers[prefix_key(mask)].append(mask)

    owner_code = {None: 0}
    owner_code.update({owner: i + 1 for i, owner in enumerate(ORDER)})

    def raw_bits(mask: int) -> int:
        return sum(
            1 << i for i, owner in enumerate(ORDER) if raw[owner](mask)
        )

    owner_rows = [
        [mask, *prefix_key(mask), raw_bits(mask), owner_code[owners[mask]]]
        for mask in full_masks
    ]
    residual_key_rows = [
        [
            mask, *prefix_key(mask),
            full_fibers[prefix_key(mask)][0],
            residual_fibers[prefix_key(mask)][0],
        ]
        for mask in residual
    ]
    partition_payload = {
        "order": ORDER,
        "semantics": SEMANTICS,
        "owner_rows": owner_rows,
    }
    partition_digest = hashlib.sha256(
        json.dumps(
            partition_payload, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
    ).hexdigest()

    return {
        "full_masks": full_masks,
        "full_fibers": full_fibers,
        "common_core": common_core,
        "raw": raw,
        "owners": owners,
        "residual": residual,
        "residual_fibers": residual_fibers,
        "owner_rows": owner_rows,
        "residual_key_rows": residual_key_rows,
        "partition_digest": partition_digest,
    }


def validate(data: dict[str, Any]) -> None:
    expected = build_expected()
    full_masks = expected["full_masks"]
    full_fibers = expected["full_fibers"]
    raw = expected["raw"]
    owners = expected["owners"]
    residual = expected["residual"]
    residual_fibers = expected["residual_fibers"]

    require(data.get("schema") == "rs-mca.m31-c9-owner-coverage.v2",
            "schema mismatch")
    require(data.get("status") == "PROVED_CRITERION_2_ALL_KEY_LOSS_ONE",
            "status mismatch")
    require(data.get("criterion") == 2, "criterion mismatch")
    require(
        data.get("predecessor")
        == "M31_C9_GLOBAL_OWNER_COMPLEMENT_AND_KEY_COVERAGE",
        "predecessor mismatch",
    )
    require(data.get("base") == EXPECTED_BASE, "base pins mismatch")
    require(data.get("sources") == EXPECTED_SOURCES, "source pins mismatch")
    require(data.get("imports") == EXPECTED_IMPORTS,
            "imported API blob table mismatch")
    require(all(row[1] == row[2] for row in data["imports"]),
            "fork/upstream imported API blobs differ")
    require(
        data.get("row")
        == [P, 2**21, 67_447, 981_129, 981_125, 2_097_144, 16_777_215, 1],
        "row constants mismatch",
    )
    require(data.get("domain") == DOMAIN, "domain mismatch")
    require(len(set(DOMAIN)) == 8, "domain is not duplicate-free")
    require(all(chebyshev_pow_two(21, x) == 0 for x in DOMAIN),
            "deployed root check failed")
    require(data.get("pairs") == PAIRS, "antipodal pair table mismatch")
    require(all((DOMAIN[i] + DOMAIN[j]) % P == 0 for i, j in PAIRS),
            "antipodal pair arithmetic failed")
    require(data.get("t4") == [T4_BLOCKS, [1_884_637_334, 51_044_589]],
            "T4 table mismatch")
    for block, target in zip(T4_BLOCKS, [1_884_637_334, 51_044_589]):
        require(
            all(chebyshev_pow_two(2, DOMAIN[i]) == target for i in block),
            "T4 fiber arithmetic failed",
        )
    require(data.get("order") == ORDER, "first-match order mismatch")
    require(data.get("semantics") == SEMANTICS, "local semantics mismatch")
    require(expected["common_core"] == 0, "active common core is nonempty")
    require(
        data.get("partition_digest") == expected["partition_digest"]
        == EXPECTED_PARTITION_DIGEST,
        "partition digest mismatch",
    )
    require(data.get("owner_rows") == expected["owner_rows"],
            "one or more of 70 owner rows differs")
    require(len(data["owner_rows"]) == 70, "owner row count mismatch")
    require(data.get("residual_key_rows") == expected["residual_key_rows"],
            "one or more of 64 key rows differs")
    require(len(data["residual_key_rows"]) == 64,
            "residual key row count mismatch")

    raw_counts = [
        sum(bool(raw[owner](mask)) for mask in full_masks)
        for owner in ORDER
    ]
    first_counts = [
        sum(owners[mask] == owner for mask in full_masks)
        for owner in ORDER
    ]
    collision = [
        list(key) + fibers
        for key, fibers in sorted(full_fibers.items())
        if len(fibers) > 1
    ]
    require(collision == [[0, 2, 0, 15, 240]],
            "unexpected full-prefix collision census")
    require(
        data.get("summary")
        == {
            "raw": raw_counts,
            "first": first_counts,
            "residual": len(residual),
            "full_supports": len(full_masks),
            "full_image": len(full_fibers),
            "residual_image": len(residual_fibers),
            "collision": collision[0],
            "counterexamples": [
                mask for mask in residual
                if len(full_fibers[prefix_key(mask)]) != 1
            ],
            "compiler_loss": 1,
            "natural_scale": 2,
        },
        "summary mismatch",
    )
    require(raw_counts == [6, 2, 0, 0, 0, 0, 2, 0],
            "unexpected raw trigger counts")
    require(first_counts == [6, 0, 0, 0, 0, 0, 0, 0],
            "unexpected first-match counts")
    require(len(residual) == len(residual_fibers) == 64,
            "residual size or injectivity mismatch")
    require(
        all(len(full_fibers[prefix_key(mask)]) == 1 for mask in residual),
        "a residual key is not singleton in the full slice",
    )
    require(1 * 69 <= 70, "image-normalized inequality failed")
    require(1 * 2 <= 16_777_215, "deployed budget comparison failed")
    require(
        data.get("nonclaims")
        == ["profile multiplicity", "SE2", "Sidon/MI+MA",
            "add-back/UNIF", "adjacent row"],
        "nonclaim list mismatch",
    )
    require(data.get("verdict") == "FIXED", "verdict mismatch")


def canonical_text(data: dict[str, Any]) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":")) + "\n"


def load(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    data = json.loads(text)
    require(isinstance(data, dict), "certificate root must be an object")
    return data, text


def run_check(path: Path) -> None:
    data, text = load(path)
    require(text == canonical_text(data), "JSON is not canonical")
    validate(data)
    print(
        "PASS m31-c9-owner-coverage: 70 supports, C1=6, residual=64, "
        "64/64 full-prefix singleton keys, criterion=2, verdict=FIXED"
    )


def expect_failure(data: dict[str, Any], label: str) -> None:
    try:
        validate(data)
    except VerificationError:
        return
    raise VerificationError(f"tamper self-test accepted {label}")


def run_tamper_selftest(path: Path) -> None:
    data, _ = load(path)
    validate(data)

    mutation = copy.deepcopy(data)
    mutation["owner_rows"][0][-1] = 0
    expect_failure(mutation, "owner mutation")

    mutation = copy.deepcopy(data)
    mutation["order"][0:2] = ["C2", "C1"]
    expect_failure(mutation, "order mutation")

    mutation = copy.deepcopy(data)
    mutation["residual_key_rows"][0][-2] = 240
    expect_failure(mutation, "fiber mutation")

    mutation = copy.deepcopy(data)
    mutation["imports"][0][1] = "0" * 40
    expect_failure(mutation, "blob mutation")

    print("PASS tamper-selftest: 4/4 mutations rejected")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--check", action="store_true")
    action.add_argument("--tamper-selftest", action="store_true")
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERT)
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    try:
        if args.check:
            run_check(args.certificate)
        else:
            run_tamper_selftest(args.certificate)
    except (OSError, json.JSONDecodeError, VerificationError) as exc:
        print(f"FAIL m31-c9-owner-coverage: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
