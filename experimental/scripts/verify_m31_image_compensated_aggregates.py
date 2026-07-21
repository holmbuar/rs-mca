#!/usr/bin/env python3
"""Independent stdlib replay for the M31 image-compensated aggregate packet."""

from __future__ import annotations

import argparse
import copy
import itertools
import json
from collections import Counter
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[2]
DEFAULT_CERT = (
    REPO_ROOT
    / "experimental/data/certificates/"
    / "sidon-effective-image-image-compensated-aggregates/"
    / "m31_image_compensated_aggregates.json"
)


class CheckError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckError(message)


def load_certificate(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    require(isinstance(data, dict), "certificate root must be an object")
    return data


def support_masks(n: int, weight: int) -> list[int]:
    return [sum(1 << i for i in choice) for choice in itertools.combinations(range(n), weight)]


def prefix_key(mask: int, domain: list[int], prime: int, depth: int) -> tuple[int, ...]:
    selected = [domain[i] for i in range(len(domain)) if (mask >> i) & 1]
    return tuple(sum(pow(x, e, prime) for x in selected) % prime for e in range(1, depth + 1))


def chebyshev_pow_two(x: int, exponent: int, prime: int) -> int:
    value = x % prime
    for _ in range(exponent):
        value = (2 * value * value - 1) % prime
    return value


def matrix_mul(a: list[list[int]], b: list[list[int]], prime: int) -> list[list[int]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(3)) % prime for j in range(3)]
        for i in range(3)
    ]


def moment_column(x: int, prime: int) -> list[int]:
    return [x % prime, pow(x, 2, prime), pow(x, 3, prime)]


def matrix_from_domain(domain: list[int], prime: int) -> list[list[int]]:
    base = moment_column(domain[0], prime)
    columns: list[list[int]] = []
    for x in domain[1:4]:
        col = moment_column(x, prime)
        columns.append([(col[i] - base[i]) % prime for i in range(3)])
    return [[columns[j][i] for j in range(3)] for i in range(3)]


def validate(data: dict[str, Any]) -> dict[str, int]:
    expected_top = {
        "schema_version",
        "packet",
        "acceptance_gate",
        "provenance",
        "imported_api_parity",
        "leaf",
        "span_certificate",
        "character_partition",
        "compensated_bounds",
    }
    require(set(data) == expected_top, "unexpected top-level certificate keys")
    require(data["schema_version"] == 1, "unsupported schema version")
    require(data["packet"] == "m31-image-compensated-aggregates-v1", "wrong packet id")
    require(data["acceptance_gate"] == 2, "packet must name acceptance criterion 2")

    provenance = data["provenance"]
    require(
        provenance["fork_base_sha"] == "4e5f0b77c98f075ea7c8822cd4859847a232bc2a",
        "fork base SHA drift",
    )
    require(
        provenance["upstream_main_sha"] == "a3017697ad1594521d2779fe1d83bccd45d4c06e",
        "upstream main SHA drift",
    )
    require(
        provenance["grande_finale_v4_blob"] == "8a5d9791900ca9eed773feba146b92ad296704ce",
        "Grande Finale v4 blob drift",
    )

    parity = data["imported_api_parity"]
    require(len(parity) == 2, "expected exactly two directly imported integrated APIs")
    expected_parity = {
        "experimental/lean/asymptotic_spine/AsymptoticSpine/PrimitiveBoolean.lean":
            "777273e4377c31c815062769803622c6226988d3",
        "experimental/lean/m31_q_rooted_shell/M31QRootedShell/Deployed.lean":
            "7e21ff098567d26aba7330fbb2722d5cb952fb09",
    }
    for row in parity:
        path = row["path"]
        require(path in expected_parity, f"unexpected imported API path: {path}")
        expected_sha = expected_parity[path]
        require(row["fork_blob"] == expected_sha, f"fork blob drift for {path}")
        require(row["upstream_blob"] == expected_sha, f"upstream blob drift for {path}")
        require(row["byte_identical"] is True, f"parity flag false for {path}")

    leaf = data["leaf"]
    prime = leaf["prime"]
    domain = leaf["domain"]
    n = leaf["active_dimension"]
    weight = leaf["weight"]
    depth = leaf["prefix_depth"]
    owner_masks = leaf["c1_owner_masks"]
    require(prime == 2_147_483_647, "wrong M31 prime")
    require(n == 8 and weight == 4 and depth == 3, "wrong local slice dimensions")
    require(len(domain) == n and len(set(domain)) == n, "domain must have eight distinct points")
    require(all(0 <= x < prime for x in domain), "domain residue outside field")
    require(
        all(chebyshev_pow_two(x, 21, prime) == 0 for x in domain),
        "a displayed point is not a T_(2^21) root",
    )
    require(
        [chebyshev_pow_two(x, 2, prime) for x in domain[:4]] == [1_884_637_334] * 4,
        "first T4 fiber drift",
    )
    require(
        [chebyshev_pow_two(x, 2, prime) for x in domain[4:]] == [51_044_589] * 4,
        "second T4 fiber drift",
    )
    require(
        [
            (domain[0] + domain[2]) % prime,
            (domain[1] + domain[3]) % prime,
            (domain[4] + domain[6]) % prime,
            (domain[5] + domain[7]) % prime,
        ]
        == [0, 0, 0, 0],
        "antipodal pairing drift",
    )

    masks = support_masks(n, weight)
    keys = [prefix_key(mask, domain, prime, depth) for mask in masks]
    full_counts = Counter(keys)
    residual_masks = [mask for mask in masks if mask not in set(owner_masks)]
    residual_keys = [prefix_key(mask, domain, prime, depth) for mask in residual_masks]
    residual_counts = Counter(residual_keys)

    require(len(masks) == leaf["expected_full_mass"] == 70, "full support census mismatch")
    require(len(full_counts) == leaf["expected_full_image"] == 69, "full image census mismatch")
    require(len(owner_masks) == len(set(owner_masks)) == leaf["expected_c1_owned"] == 6,
            "C1 owner census mismatch")
    require(all(mask in masks for mask in owner_masks), "C1 owner mask outside full slice")
    require(len(residual_masks) == leaf["expected_residual_mass"] == 64,
            "residual support census mismatch")
    require(len(residual_counts) == leaf["expected_residual_image"] == 64,
            "residual image census mismatch")
    require(max(residual_counts.values(), default=0) == 1, "residual prefix map is not injective")
    doubled = sorted((list(key), count) for key, count in full_counts.items() if count > 1)
    require(
        len(doubled) == 1
        and doubled[0][0] == leaf["collision_key"]
        and doubled[0][1] == 2,
        "full-slice collision census drift",
    )
    require(leaf["selected_support_mask"] in residual_masks, "selected support did not survive C1")
    require(
        list(prefix_key(leaf["selected_support_mask"], domain, prime, depth))
        == leaf["selected_key"],
        "selected key drift",
    )

    span = data["span_certificate"]
    computed_basis = matrix_from_domain(domain, prime)
    require(computed_basis == span["basis_matrix"], "basis matrix drift")
    inverse = span["inverse_matrix"]
    identity = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    require(matrix_mul(computed_basis, inverse, prime) == identity, "basis * inverse != I")
    require(matrix_mul(inverse, computed_basis, prime) == identity, "inverse * basis != I")
    require(span["effective_dimension"] == 3, "effective dimension drift")

    part = data["character_partition"]
    p2 = prime**2
    p3 = prime**3
    minor_count = p2 - 1
    major_count = p3 - p2
    require(part["minor_rule"] == "a1=0 and character!=0", "minor rule drift")
    require(part["major_rule"] == "a1!=0", "major rule drift")
    require(part["minor_count"] == minor_count, "minor count mismatch")
    require(part["major_count"] == major_count, "major count mismatch")
    require(part["effective_size"] == p3, "effective group size mismatch")
    require(1 + minor_count + major_count == p3, "partition does not cover nontrivial dual")
    require(part["minor_witness"] == [0, 1, 0], "minor witness drift")
    require(part["major_witness"] == [1, 0, 0], "major witness drift")
    require(part["lift"] == "identity", "certified lift must be identity")

    bounds = data["compensated_bounds"]
    source_mass = leaf["expected_full_mass"]
    image_size = leaf["expected_full_image"]
    require(bounds["source_mass"] == source_mass, "source mass normalization drift")
    require(bounds["realized_image_size"] == image_size, "realized image normalization drift")
    require(bounds["effective_size"] == p3, "bound effective size drift")
    require(bounds["minor_loss"] == 1, "minor loss drift")
    require(bounds["major_loss"] == 69, "major loss drift")
    require(bounds["full_loss"] == 69, "full loss drift")
    require(image_size * minor_count <= bounds["minor_loss"] * p3,
            "cleared compensated minor inequality failed")
    require(image_size * major_count <= bounds["major_loss"] * p3,
            "cleared compensated major inequality failed")
    require(
        image_size * (1 + minor_count + major_count)
        <= bounds["full_loss"] * p3,
        "cleared full multiplier inequality failed",
    )
    require(
        bounds["cleared_minor_slack"]
        == bounds["minor_loss"] * p3 - image_size * minor_count,
        "minor slack drift",
    )
    require(
        bounds["cleared_major_slack"]
        == bounds["major_loss"] * p3 - image_size * major_count,
        "major slack drift",
    )

    return {
        "full_supports": len(masks),
        "full_image": len(full_counts),
        "residual_supports": len(residual_masks),
        "residual_image": len(residual_counts),
        "effective_size": p3,
        "minor_count": minor_count,
        "major_count": major_count,
    }


def tamper_selftest(data: dict[str, Any]) -> int:
    mutators = [
        lambda d: d.__setitem__("acceptance_gate", 4),
        lambda d: d["provenance"].__setitem__("fork_base_sha", "0" * 40),
        lambda d: d["imported_api_parity"][0].__setitem__("byte_identical", False),
        lambda d: d["leaf"]["domain"].__setitem__(0, d["leaf"]["domain"][0] + 1),
        lambda d: d["leaf"]["c1_owner_masks"].__setitem__(0, 51),
        lambda d: d["leaf"].__setitem__("expected_residual_image", 63),
        lambda d: d["span_certificate"]["inverse_matrix"][0].__setitem__(0, 0),
        lambda d: d["character_partition"].__setitem__("minor_count", 0),
        lambda d: d["compensated_bounds"].__setitem__("minor_loss", 0),
        lambda d: d["compensated_bounds"].__setitem__("cleared_major_slack", 0),
    ]
    rejected = 0
    for mutate in mutators:
        candidate = copy.deepcopy(data)
        mutate(candidate)
        try:
            validate(candidate)
        except CheckError:
            rejected += 1
        else:
            raise CheckError("tamper self-test accepted a mutated certificate")
    require(rejected == len(mutators), "not all mutations were rejected")
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERT)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    if not args.check and not args.tamper_selftest:
        parser.error("select --check and/or --tamper-selftest")

    data = load_certificate(args.certificate)
    if args.check:
        result = validate(data)
        print("PASS m31 image-compensated aggregate certificate")
        for key, value in result.items():
            print(f"{key}={value}")
    if args.tamper_selftest:
        rejected = tamper_selftest(data)
        print(f"PASS tamper self-test: {rejected}/{rejected} mutations rejected")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except CheckError as exc:
        print(f"FAIL: {exc}")
        raise SystemExit(1)
