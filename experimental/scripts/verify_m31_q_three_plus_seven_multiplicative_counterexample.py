#!/usr/bin/env python3
"""Exact replay for the multiplicative-subgroup counterexample to support-only 3+7.

Python is auxiliary replay only.  The corresponding stdlib-only Lean module is
`M31QRootedShell/MultiplicativeCounterexample.lean` and is the proof validator
for the explicit counterexample packet.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from collections import Counter, defaultdict
from itertools import combinations
from math import comb
from pathlib import Path
from typing import Any, Iterable

P = 241
N = 20
M = 10
W = 2
GENERATOR = 235
TARGET = (92, 135)
ANCHOR = (2, 5, 6, 10, 11, 13, 14, 17, 18, 19)
SHELL = 6
B = 3
C = 7
CERT_PATH = Path(
    "experimental/data/certificates/"
    "m31-q-3plus7-multiplicative-counterexample/"
    "m31_q_three_plus_seven_multiplicative_counterexample.json"
)


def stable_digest(value: Any) -> str:
    data = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def payload_digest(cert: dict[str, Any]) -> str:
    payload = {k: v for k, v in cert.items() if k != "payload_sha256"}
    return stable_digest(payload)


def mask_of(support: Iterable[int]) -> int:
    mask = 0
    for i in support:
        mask |= 1 << i
    return mask


def support_of(mask: int) -> tuple[int, ...]:
    return tuple(i for i in range(N) if (mask >> i) & 1)


def rotate_mask(mask: int, shift: int) -> int:
    shift %= N
    all_bits = (1 << N) - 1
    if shift == 0:
        return mask & all_bits
    return ((mask << shift) | (mask >> (N - shift))) & all_bits


def reflect_mask(mask: int, axis: int) -> int:
    out = 0
    for i in range(N):
        if (mask >> i) & 1:
            out |= 1 << ((axis - i) % N)
    return out


def dihedral_stabilizer(mask: int) -> list[tuple[str, int]]:
    stabilizer: list[tuple[str, int]] = []
    for shift in range(N):
        if rotate_mask(mask, shift) == mask:
            stabilizer.append(("rotation", shift))
    for axis in range(N):
        if reflect_mask(mask, axis) == mask:
            stabilizer.append(("reflection", axis))
    return stabilizer


def dihedral_generic(mask: int) -> bool:
    return dihedral_stabilizer(mask) == [("rotation", 0)]


def same_dihedral_orbit(left: int, right: int) -> bool:
    return any(rotate_mask(left, s) == right for s in range(N)) or any(
        reflect_mask(left, s) == right for s in range(N)
    )


def domain() -> tuple[int, ...]:
    values = tuple(pow(GENERATOR, i, P) for i in range(N))
    assert pow(GENERATOR, N, P) == 1
    assert all(pow(GENERATOR, i, P) != 1 for i in range(1, N))
    assert len(set(values)) == N
    return values


def elementary_prefix(mask: int, values: tuple[int, ...]) -> tuple[int, int]:
    selected = [values[i] for i in range(N) if (mask >> i) & 1]
    e1 = sum(selected) % P
    e2 = 0
    for i, x in enumerate(selected):
        for y in selected[i + 1 :]:
            e2 = (e2 + x * y) % P
    return e1, e2


def exchange_distance(left: int, right: int) -> int:
    return M - (left & right).bit_count()


def common_core(family: list[int]) -> tuple[int, ...]:
    inter = (1 << N) - 1
    for support in family:
        inter &= support
    return support_of(inter)


def enumerate_packet() -> dict[str, Any]:
    values = domain()
    all_supports = [mask_of(s) for s in combinations(range(N), M)]
    by_prefix: dict[tuple[int, int], list[int]] = defaultdict(list)
    for support in all_supports:
        by_prefix[elementary_prefix(support, values)].append(support)

    raw_target = sorted(by_prefix[TARGET], key=support_of)
    deleted_target = [s for s in raw_target if not dihedral_generic(s)]
    residual_target = [s for s in raw_target if dihedral_generic(s)]

    residual_by_prefix: dict[tuple[int, int], list[int]] = {}
    generic_support_count = 0
    symmetric_support_count = 0
    generic_key_count = 0
    planted_key_count = 0
    for prefix, raw_family in by_prefix.items():
        generic_family = [s for s in raw_family if dihedral_generic(s)]
        symmetric_support_count += len(raw_family) - len(generic_family)
        generic_support_count += len(generic_family)
        if not generic_family:
            continue
        generic_key_count += 1
        if common_core(generic_family):
            planted_key_count += 1
            continue
        residual_by_prefix[prefix] = sorted(generic_family, key=support_of)

    anchor_mask = mask_of(ANCHOR)
    assert anchor_mask in residual_target
    distances = Counter(
        exchange_distance(anchor_mask, support)
        for support in residual_target
        if support != anchor_mask
    )
    shell_neighbors = [
        support
        for support in residual_target
        if support != anchor_mask
        and exchange_distance(anchor_mask, support) == SHELL
    ]

    ambient_shell = comb(M, SHELL) * comb(N - M, SHELL)
    q = P**W
    degree = len(shell_neighbors)
    lhs_b3 = q * max(degree - 3, 0)
    lhs_b4 = q * max(degree - 4, 0)
    lhs_b5 = q * max(degree - 5, 0)
    rhs = C * ambient_shell

    failures: list[dict[str, Any]] = []
    for prefix, family in residual_by_prefix.items():
        for anchor in family:
            histogram = Counter(
                exchange_distance(anchor, support)
                for support in family
                if support != anchor
            )
            for shell, rooted_degree in histogram.items():
                if shell <= W or rooted_degree <= B:
                    continue
                h_shell = comb(M, shell) * comb(N - M, shell)
                local_lhs = q * (rooted_degree - B)
                local_rhs = C * h_shell
                if local_lhs > local_rhs:
                    failures.append(
                        {
                            "target": list(prefix),
                            "anchor": list(support_of(anchor)),
                            "shell": shell,
                            "rooted_degree": rooted_degree,
                            "residual_fiber_size": len(family),
                            "ambient_shell": h_shell,
                            "lhs": local_lhs,
                            "rhs": local_rhs,
                            "margin": local_lhs - local_rhs,
                        }
                    )

    failures.sort(key=lambda row: (row["target"], row["anchor"]))
    canonical_failure = {
        "target": list(TARGET),
        "anchor": list(ANCHOR),
        "shell": SHELL,
        "rooted_degree": degree,
        "residual_fiber_size": len(residual_target),
        "ambient_shell": ambient_shell,
        "lhs": lhs_b3,
        "rhs": rhs,
        "margin": lhs_b3 - rhs,
    }
    assert canonical_failure in failures

    failure_keys = {
        (tuple(row["target"]), tuple(row["anchor"])) for row in failures
    }
    orbit = []
    for shift in range(N):
        rotated_anchor = support_of(rotate_mask(anchor_mask, shift))
        scale = pow(GENERATOR, shift, P)
        rotated_target = (
            TARGET[0] * scale % P,
            TARGET[1] * scale * scale % P,
        )
        orbit.append(
            {
                "shift": shift,
                "target": list(rotated_target),
                "anchor": list(rotated_anchor),
                "is_failure": (rotated_target, rotated_anchor) in failure_keys,
            }
        )

    cert: dict[str, Any] = {
        "schema": "m31-q-3plus7-multiplicative-counterexample-v1",
        "status": {
            "explicit_counterexample": "LEAN_PROVED",
            "exhaustive_census": "AUXILIARY_EXACT_REPLAY",
            "deployed_m31_exact_residual": "OPEN",
            "verdict": "COUNTEREXAMPLE_TO_SUPPORT_ONLY_3PLUS7",
        },
        "parameters": {
            "field": "F_241",
            "p": P,
            "n": N,
            "m": M,
            "w": W,
            "q": q,
            "generator": GENERATOR,
            "generator_order": N,
            "domain": list(values),
            "target": list(TARGET),
            "b": B,
            "c": C,
        },
        "pruning": {
            "rotation_action": "i -> i+s mod 20 (multiplicative scaling)",
            "reflection_action": "i -> s-i mod 20 (scale followed by inversion)",
            "support_rule": "delete every support with nontrivial dihedral stabilizer",
            "target_rule": "delete a remaining prefix target when all supports share a point",
        },
        "canonical_target": {
            "raw_fiber_size": len(raw_target),
            "raw_fiber": [list(support_of(s)) for s in raw_target],
            "deleted_dihedral_size": len(deleted_target),
            "deleted_dihedral": [
                {
                    "support": list(support_of(s)),
                    "stabilizer": [list(item) for item in dihedral_stabilizer(s)],
                }
                for s in deleted_target
            ],
            "residual_fiber_size": len(residual_target),
            "residual_fiber": [list(support_of(s)) for s in residual_target],
            "residual_common_core": list(common_core(residual_target)),
            "all_residual_stabilizers_trivial": all(
                dihedral_generic(s) for s in residual_target
            ),
            "anchor": list(ANCHOR),
            "anchor_distance_histogram": {
                str(k): v for k, v in sorted(distances.items())
            },
            "shell_neighbors": [list(support_of(s)) for s in shell_neighbors],
            "star_common_core": list(common_core([anchor_mask, *shell_neighbors])),
            "anchor_neighbor_dihedral_relations": sum(
                same_dihedral_orbit(anchor_mask, s) for s in shell_neighbors
            ),
        },
        "inequality": {
            "shell": SHELL,
            "choose_m_e": comb(M, SHELL),
            "choose_n_minus_m_e": comb(N - M, SHELL),
            "ambient_shell": ambient_shell,
            "rooted_degree": degree,
            "rhs_7H": rhs,
            "b3_lhs": lhs_b3,
            "b3_margin": lhs_b3 - rhs,
            "b3_verdict": "FAIL",
            "b4_lhs": lhs_b4,
            "b4_margin": lhs_b4 - rhs,
            "b4_verdict": "FAIL",
            "b5_lhs": lhs_b5,
            "b5_reserve": rhs - lhs_b5,
            "b5_verdict": "HOLD",
            "least_integer_coefficient_at_b3": (lhs_b3 + ambient_shell - 1)
            // ambient_shell,
        },
        "global_census": {
            "total_supports": len(all_supports),
            "raw_prefix_keys": len(by_prefix),
            "dihedral_generic_supports": generic_support_count,
            "dihedral_symmetric_supports": symmetric_support_count,
            "generic_prefix_keys": generic_key_count,
            "planted_keys_removed": planted_key_count,
            "residual_prefix_keys": len(residual_by_prefix),
            "max_residual_fiber": max(map(len, residual_by_prefix.values())),
            "violating_anchor_shells": len(failures),
            "violations": failures,
            "single_multiplicative_orbit": len(failures) == N
            and all(row["is_failure"] for row in orbit),
            "orbit": orbit,
        },
        "digests": {
            "raw_fiber_sha256": stable_digest(
                [list(support_of(s)) for s in raw_target]
            ),
            "residual_fiber_sha256": stable_digest(
                [list(support_of(s)) for s in residual_target]
            ),
            "shell_neighbors_sha256": stable_digest(
                [list(support_of(s)) for s in shell_neighbors]
            ),
            "violations_sha256": stable_digest(failures),
        },
        "nonclaims": [
            "No actual C1-C8 slope-level first-match projector is executed.",
            "The packet does not refute the deployed Mersenne-31 exact residual.",
            "The packet does not prove or refute row-sharp Q.",
            "The exhaustive Python census is replay evidence, not Lean validation.",
        ],
    }
    cert["payload_sha256"] = payload_digest(cert)
    return cert


def validate(cert: dict[str, Any], expected: dict[str, Any] | None = None) -> None:
    if expected is None:
        expected = enumerate_packet()
    if cert != expected:
        raise AssertionError("certificate differs from exact recomputation")
    if cert["payload_sha256"] != payload_digest(cert):
        raise AssertionError("payload digest mismatch")


def write_certificate(path: Path) -> dict[str, Any]:
    cert = enumerate_packet()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    return cert


def check_certificate(path: Path) -> dict[str, Any]:
    cert = json.loads(path.read_text())
    validate(cert)
    return cert


def tamper_selftest() -> None:
    base = enumerate_packet()
    mutations = [
        ("p", lambda x: x["parameters"].__setitem__("p", 239)),
        ("domain", lambda x: x["parameters"]["domain"].__setitem__(1, 234)),
        ("target", lambda x: x["parameters"]["target"].__setitem__(0, 93)),
        (
            "raw support",
            lambda x: x["canonical_target"]["raw_fiber"][0].__setitem__(0, 19),
        ),
        (
            "residual support",
            lambda x: x["canonical_target"]["residual_fiber"][0].__setitem__(0, 19),
        ),
        (
            "stabilizer",
            lambda x: x["canonical_target"]["deleted_dihedral"][0].__setitem__(
                "stabilizer", []
            ),
        ),
        ("degree", lambda x: x["inequality"].__setitem__("rooted_degree", 9)),
        ("margin", lambda x: x["inequality"].__setitem__("b3_margin", 97866)),
        (
            "global failure count",
            lambda x: x["global_census"].__setitem__("violating_anchor_shells", 19),
        ),
        (
            "orbit",
            lambda x: x["global_census"]["orbit"][0].__setitem__(
                "is_failure", False
            ),
        ),
        ("digest", lambda x: x["digests"].__setitem__("raw_fiber_sha256", "0" * 64)),
        ("payload", lambda x: x.__setitem__("payload_sha256", "0" * 64)),
    ]
    caught = 0
    for name, mutate in mutations:
        sample = copy.deepcopy(base)
        mutate(sample)
        try:
            validate(sample, expected=base)
        except AssertionError:
            caught += 1
        else:
            raise AssertionError(f"tamper mutation was not rejected: {name}")
    print(f"tamper-selftest: PASS ({caught}/{len(mutations)})")


def print_summary(cert: dict[str, Any]) -> None:
    target = cert["canonical_target"]
    inequality = cert["inequality"]
    census = cert["global_census"]
    print("RESULT: PASS")
    print(
        "target=",
        cert["parameters"]["target"],
        "raw=",
        target["raw_fiber_size"],
        "residual=",
        target["residual_fiber_size"],
    )
    print(
        "shell=",
        inequality["shell"],
        "degree=",
        inequality["rooted_degree"],
        "b3_lhs=",
        inequality["b3_lhs"],
        "rhs=",
        inequality["rhs_7H"],
        "margin=",
        inequality["b3_margin"],
    )
    print(
        "global_violations=",
        census["violating_anchor_shells"],
        "single_orbit=",
        census["single_multiplicative_orbit"],
    )
    print("payload_sha256=", cert["payload_sha256"])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--tamper-selftest", action="store_true")
    parser.add_argument("--certificate", type=Path, default=CERT_PATH)
    args = parser.parse_args()

    if args.write:
        cert = write_certificate(args.certificate)
    elif args.check or args.certificate.exists():
        cert = check_certificate(args.certificate)
    else:
        cert = enumerate_packet()

    print_summary(cert)
    if args.tamper_selftest:
        tamper_selftest()


if __name__ == "__main__":
    main()
