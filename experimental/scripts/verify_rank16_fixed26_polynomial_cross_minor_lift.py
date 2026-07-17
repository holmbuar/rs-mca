#!/usr/bin/env python3
"""Fail-closed replay for the fixed-26 polynomial cross-minor lift."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from itertools import combinations, permutations
from pathlib import Path
from typing import Any, Callable


class VerificationError(RuntimeError):
    """Raised when a pinned theorem or finite replay check fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError("CHECK FAILED: " + message)


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
CERT_REL = "experimental/data/certificates/rank16-fixed26-polynomial-cross-minor-lift"
CERT_DIR = REPO_ROOT / CERT_REL
MANIFEST_PATH = CERT_DIR / "manifest.json"
EXPECTED_PATH = CERT_DIR / "verify_rank16_fixed26_polynomial_cross_minor_lift.expected.txt"
CHECKSUM_PATH = CERT_DIR / "SHA256SUMS"

NOTE_REL = "experimental/notes/l2/rank16_fixed26_polynomial_cross_minor_lift.md"
SCRIPT_REL = "experimental/scripts/verify_rank16_fixed26_polynomial_cross_minor_lift.py"
MANIFEST_REL = CERT_REL + "/manifest.json"
EXPECTED_REL = CERT_REL + "/verify_rank16_fixed26_polynomial_cross_minor_lift.expected.txt"
ARTIFACTS = (NOTE_REL, SCRIPT_REL, MANIFEST_REL, EXPECTED_REL)

SCHEMA = "rs-mca.rank16-fixed26-polynomial-cross-minor-lift.v1"
BASE = "7f278167e1e51f968896229ae438ea5a76398f90"
DEPENDENCY = "d2b11f1914dea4cb4a7670736cf00d1422c878de"
SOURCE_PINS = {
    "experimental/notes/l2/rank16_fixed26_divided_difference_source_compiler.md":
        "e508b1847228475e5a71ab12df15d69d4091e7558a91f53e68261f06c42205ab",
    "experimental/scripts/verify_rank16_fixed26_divided_difference_source_compiler.py":
        "2dd8cd4d2df24510a4faa57d4ad70feda1b4505814233547f06dea7293afc744",
    (
        "experimental/data/certificates/"
        "rank16-fixed26-divided-difference-source-compiler/manifest.json"
    ): "b8b2791a145af88e7aec2729b3140fe89896fbe0e09236615b0b441fd5c95c55",
    (
        "experimental/data/certificates/"
        "rank16-fixed26-divided-difference-source-compiler/"
        "verify_fixed26_compiler.expected.txt"
    ): "d2f6c375c092e8f0aca993a006ad07082b52a6556e6b904f35703e911daddd43",
}

A = 67_472
R = 63_601
D = 28_897
VERTICES = tuple(range(8))
EDGES = tuple(combinations(VERTICES, 2))


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key: " + key)
        result[key] = value
    return result


def load_manifest() -> dict[str, Any]:
    try:
        value = json.loads(
            MANIFEST_PATH.read_text(encoding="ascii"),
            object_pairs_hook=reject_duplicate_keys,
        )
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise VerificationError("cannot read strict ASCII manifest") from exc
    require(type(value) is dict, "manifest root object")
    return value


def manifest_contract(expected_sha256: str) -> dict[str, Any]:
    return {
        "schema": SCHEMA,
        "base": BASE,
        "dependency_pr_862_head": DEPENDENCY,
        "source_pins": SOURCE_PINS,
        "parameters": {
            "field_prime": 2_130_706_433,
            "domain_order": 2_097_152,
            "fiber_size_B": 32_768,
            "generator_degree_a": A,
            "residual_degree_r": R,
            "adjacent_gcd_degree_d": D,
            "collision_labels": 8,
            "dense_edge_floor": 25,
        },
        "theorem": {
            "four_cycle_nonzero": True,
            "four_cycle_quotient_degree": 59_730,
            "minor_quotient_bounds": {"2": 59_730, "3": 55_859, "4": 51_988},
            "dense_graph_has_K44": True,
            "dichotomy": "zero_source_normalized_minor_or_N5_at_most_51988",
        },
        "scope": {
            "fixed_received_word_ray_core": True,
            "source_normalized_U_entries": True,
            "excludes_seven_star": False,
            "proves_cap_116": False,
            "aggregates_over_cores": False,
            "finite_ledger_payment": False,
            "parent_closure": False,
            "grand_list": False,
            "grand_mca": False,
            "score_movement": False,
        },
        "remaining_wall": {
            "zero_minor": "derive_global_or_rank_two_source_collapse",
            "root_excess_order_3": 55_860,
            "root_excess_order_4": 51_989,
            "global_owner": "marked_incidence_required_by_pr_873",
        },
        "expected_output": {"path": EXPECTED_REL, "sha256": expected_sha256},
        "artifacts": list(ARTIFACTS),
    }


def validate_manifest(value: dict[str, Any]) -> None:
    output = value.get("expected_output")
    require(type(output) is dict, "expected output object")
    digest = output.get("sha256")
    require(
        type(digest) is str and re.fullmatch(r"[0-9a-f]{64}", digest) is not None,
        "expected output SHA-256",
    )
    require(value == manifest_contract(digest), "semantic manifest contract")


def verify_source_pins() -> int:
    for relative, digest in SOURCE_PINS.items():
        path = (REPO_ROOT / relative).resolve()
        require(REPO_ROOT in path.parents, "source pin confinement")
        require(path.is_file(), "source pin exists: " + relative)
        require(sha256_path(path) == digest, "source pin digest: " + relative)
    return len(SOURCE_PINS)


def verify_artifacts(manifest: dict[str, Any]) -> int:
    require(CHECKSUM_PATH.is_file(), "checksum file exists")
    raw = CHECKSUM_PATH.read_bytes()
    require(raw.endswith(b"\n"), "checksum final newline")
    lines = raw.decode("ascii").splitlines()
    require(len(lines) == len(ARTIFACTS), "checksum entry count")
    pattern = re.compile(r"([0-9a-f]{64})  ([!-~]+)")
    for line, expected_relative in zip(lines, ARTIFACTS):
        match = pattern.fullmatch(line)
        require(match is not None, "checksum syntax")
        digest, relative = match.groups()
        require(relative == expected_relative, "checksum order")
        require(sha256_path(REPO_ROOT / relative) == digest, "artifact digest")
    require(tuple(manifest["artifacts"]) == ARTIFACTS, "artifact manifest order")
    require(manifest["expected_output"]["path"] == EXPECTED_REL, "expected path")
    require(
        sha256_path(EXPECTED_PATH) == manifest["expected_output"]["sha256"],
        "expected output digest",
    )
    return len(lines)


def quotient_bound(order: int) -> int:
    return order * R - (order - 1) * A


def crossing_edges(left: frozenset[int]) -> frozenset[tuple[int, int]]:
    return frozenset(
        tuple(sorted((u, v)))
        for u in left
        for v in VERTICES
        if v not in left
    )


def has_k44(graph: frozenset[tuple[int, int]]) -> bool:
    return any(
        crossing_edges(frozenset(left)) <= graph
        for left in combinations(VERTICES, 4)
    )


def set_partitions(items: tuple[int, ...]):
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for partition in set_partitions(rest):
        yield ((first,),) + partition
        for i in range(len(partition)):
            block = partition[i]
            yield partition[:i] + ((first,) + block,) + partition[i + 1 :]


def determinant_has_nonzero_term(partition, left: tuple[int, ...]) -> bool:
    block_of = {}
    for block_id, block in enumerate(partition):
        for vertex in block:
            block_of[vertex] = block_id
    right = tuple(v for v in VERTICES if v not in left)
    return any(
        all(block_of[a] != block_of[b] for a, b in zip(left, perm))
        for perm in permutations(right)
    )


def replay_finite_ledger() -> tuple[int, tuple[tuple[int, int], ...], int, int]:
    require(A - R == 3_871, "source boundary gap")
    require(R - 2 * D == 5_807, "strict four-cycle nonvanishing gap")
    require(
        [quotient_bound(s) for s in (2, 3, 4)] == [59_730, 55_859, 51_988],
        "minor quotient bounds",
    )

    checked_dense_graphs = 0
    for missing_count in range(4):
        for missing in combinations(EDGES, missing_count):
            graph = frozenset(set(EDGES) - set(missing))
            require(has_k44(graph), "25-edge graph without K4,4")
            checked_dense_graphs += 1
    require(checked_dense_graphs == 3_683, "dense graph count")

    bad_24 = None
    for missing in combinations(EDGES, 4):
        graph = frozenset(set(EDGES) - set(missing))
        if not has_k44(graph):
            bad_24 = missing
            break
    require(bad_24 is not None, "24-edge sharpness mutation")

    partitions = tuple(set_partitions(VERTICES))
    require(len(partitions) == 4_140, "Bell(8) partition count")
    large_block_partitions = tuple(p for p in partitions if max(map(len, p)) >= 5)
    checked_partition_splits = 0
    for partition in large_block_partitions:
        for left in combinations(VERTICES, 4):
            require(
                not determinant_has_nonzero_term(partition, left),
                "large block admits nonzero determinant term",
            )
            checked_partition_splits += 1
    require(checked_partition_splits == 24_150, "partition-split count")
    return checked_dense_graphs, bad_24, len(partitions), checked_partition_splits


def semantic_tamper_selftests(manifest: dict[str, Any]) -> int:
    def claim_cap(value: dict[str, Any]) -> None:
        value["scope"]["proves_cap_116"] = True

    def claim_aggregation(value: dict[str, Any]) -> None:
        value["scope"]["aggregates_over_cores"] = True

    def monic_entries(value: dict[str, Any]) -> None:
        value["scope"]["source_normalized_U_entries"] = False

    def weaken_four_cycle(value: dict[str, Any]) -> None:
        value["theorem"]["four_cycle_nonzero"] = False

    def alter_bound(value: dict[str, Any]) -> None:
        value["theorem"]["minor_quotient_bounds"]["4"] = 51_987

    def alter_dependency(value: dict[str, Any]) -> None:
        value["dependency_pr_862_head"] = BASE

    mutators: tuple[tuple[str, Callable[[dict[str, Any]], None]], ...] = (
        ("cap", claim_cap),
        ("aggregation", claim_aggregation),
        ("normalization", monic_entries),
        ("four-cycle", weaken_four_cycle),
        ("minor bound", alter_bound),
        ("dependency", alter_dependency),
    )
    rejected = 0
    for name, mutate in mutators:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate_manifest(candidate)
        except VerificationError:
            rejected += 1
        else:
            raise VerificationError("semantic tamper accepted: " + name)
    require(rejected == len(mutators), "all semantic tampers rejected")
    return rejected


def render_output(
    source_count: int,
    artifact_count: int,
    tamper_count: int,
    replay: tuple[int, tuple[tuple[int, int], ...], int, int],
) -> bytes:
    dense, bad_24, partitions, partition_splits = replay
    lines = (
        "RANK16_FIXED26_POLYNOMIAL_CROSS_MINOR_LIFT: PASS",
        "schema=" + SCHEMA,
        "base=" + BASE,
        "dependency_pr_862_head=" + DEPENDENCY,
        "source_pins=PASS,count=" + str(source_count),
        "four_cycle_gap=5807",
        "minor_quotient_bounds=2:59730,3:55859,4:51988",
        "dense_graphs_checked=" + str(dense),
        "first_24_edge_counterexample_missing=" + str(bad_24),
        "set_partitions_checked=" + str(partitions),
        "large_block_partition_splits_checked=" + str(partition_splits),
        "semantic_tamper_selftests=PASS,count=" + str(tamper_count),
        "artifact_checksums=PASS,count=" + str(artifact_count),
        "finite_ledger_delta=0 official_score=0/2",
        "RESULT=PASS",
    )
    return ("\n".join(lines) + "\n").encode("ascii")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--tamper-self-test", action="store_true")
    group.add_argument("--check-checksums", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        manifest = load_manifest()
        validate_manifest(manifest)
        if args.tamper_self_test:
            count = semantic_tamper_selftests(manifest)
            print(f"SEMANTIC_TAMPER_SELFTEST: PASS count={count}")
            return 0
        if args.check_checksums:
            count = verify_artifacts(manifest)
            print(f"ARTIFACT_CHECKSUMS: PASS count={count}")
            return 0
        source_count = verify_source_pins()
        replay = replay_finite_ledger()
        tamper_count = semantic_tamper_selftests(manifest)
        artifact_count = verify_artifacts(manifest)
        output = render_output(source_count, artifact_count, tamper_count, replay)
        require(output == EXPECTED_PATH.read_bytes(), "frozen expected output byte match")
        sys.stdout.buffer.write(output)
        return 0
    except (VerificationError, OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
