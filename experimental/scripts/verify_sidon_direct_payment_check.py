#!/usr/bin/env python3
"""Independent checker for the direct-Sidon C9 correction.

This checker does not import the generator.  It rebuilds the k=5 supports as
20-coordinate tuples, recomputes the source-map fibers, uses a pair-sum energy
histogram, and verifies exact rational normalization and moment data.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import math
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
CERT = REPO_ROOT / (
    "experimental/data/certificates/sidon-direct-payment/sidon_direct_payment.json"
)
C9_ARTIFACT = REPO_ROOT / "experimental/data/c9_literal_interface_counterexample_v1.json"
BASE_SHA = "7f278167e1e51f968896229ae438ea5a76398f90"
FIELD_PRIME = 505_020_040_141
TAU = 0.05


def payload_hash(obj: dict[str, Any]) -> str:
    candidate = copy.deepcopy(obj)
    candidate.pop("payload_sha256", None)
    encoded = json.dumps(
        candidate, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def is_prime_64(n: int) -> bool:
    if n < 2:
        return False
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % prime == 0:
            return n == prime
    odd_part = n - 1
    twos = 0
    while odd_part % 2 == 0:
        twos += 1
        odd_part //= 2
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % n == 0:
            continue
        value = pow(base, odd_part, n)
        if value in (1, n - 1):
            continue
        for _ in range(twos - 1):
            value = pow(value, 2, n)
            if value == n - 1:
                break
        else:
            return False
    return True


def heavy_vector(bits: Sequence[int]) -> tuple[int, ...]:
    vector = [0] * 20
    for block, bit in enumerate(bits):
        offsets = (0, 3) if bit == 0 else (1, 2)
        for offset in offsets:
            vector[4 * block + offset] = 1
    return tuple(vector)


def prefix_vector(word: Sequence[int]) -> tuple[int, ...]:
    vector = [0] * 20
    for block, count in enumerate(word):
        for offset in range(count):
            vector[4 * block + offset] = 1
    return tuple(vector)


def source_map(
    vector: Sequence[int], points: Sequence[int]
) -> tuple[int, int]:
    return (
        sum(vector),
        sum(bit * point for bit, point in zip(vector, points, strict=True))
        % FIELD_PRIME,
    )


def pair_sum_energy(vectors: Sequence[tuple[int, ...]]) -> int:
    if not vectors:
        raise ValueError("energy requires a nonempty fiber")
    histogram: Counter[tuple[int, ...]] = Counter()
    for left, right in itertools.product(vectors, vectors):
        histogram[
            tuple(a + b for a, b in zip(left, right, strict=True))
        ] += 1
    return sum(multiplicity * multiplicity for multiplicity in histogram.values())


def independent_rebuild() -> dict[str, Any]:
    points = [
        501**block + offset
        for block in range(5)
        for offset in range(4)
    ]
    heavy = [
        heavy_vector(bits) for bits in itertools.product((0, 1), repeat=5)
    ]
    balanced = sorted(set(itertools.permutations((0, 1, 2, 3, 4))))
    fillers = [prefix_vector(word) for word in balanced]
    omega = heavy + fillers
    fibers: dict[tuple[int, int], list[tuple[int, ...]]] = defaultdict(list)
    for vector in omega:
        fibers[source_map(vector, points)].append(vector)
    positive = [members for members in fibers.values() if members]
    sizes = sorted(len(members) for members in positive)
    M = sum(sizes)
    L = len(sizes)
    barN = Fraction(M, L)
    q = 3
    sigma = math.log(4.0 / 3.0) / 8.0
    cutoff = math.exp(-sigma * 20)
    total = Fraction(0, 1)
    low_rows: list[dict[str, Any]] = []
    for members in positive:
        size = len(members)
        energy = pair_sum_energy(members)
        delta = Fraction(energy, size**3)
        if float(delta) <= cutoff:
            total += (Fraction(size, 1) / barN) ** q
            low_rows.append(
                {
                    "size": size,
                    "energy": energy,
                    "delta": delta,
                }
            )
    Gsid = total / L
    rate = math.log(float(Gsid)) / (20 * q)

    artifact = json.loads(C9_ARTIFACT.read_text(encoding="utf-8"))
    counts = artifact.get("sample_counts", {})
    artifact_match = (
        artifact.get("status") == "COUNTEREXAMPLE_NEW_FLOOR"
        and artifact.get("scope")
        == "LITERAL_QUANTITATIVE_PRIMITIVE_LEAF_INTERFACE_ONLY"
        and counts.get("domain_size_M") == M
        and counts.get("image_size_L") == L
        and counts.get("barN_numerator") == barN.numerator
        and counts.get("barN_denominator") == barN.denominator
        and artifact.get("energy", {}).get("heavy_energy") == 7776
        and artifact.get("energy", {}).get("heavy_delta_numerator") == 243
        and artifact.get("energy", {}).get("heavy_delta_denominator") == 1024
    )
    checks = {
        "omega_unique": len(set(omega)) == 152,
        "fixed_weight": all(sum(vector) == 10 for vector in omega),
        "field_prime": is_prime_64(FIELD_PRIME),
        "integer_no_wrap": FIELD_PRIME > 2 * sum(points),
        "M": M == 152,
        "L": L == 121,
        "fiber_profile": sizes == [1] * 120 + [32],
        "barN": barN == Fraction(152, 121),
        "energy": len(low_rows) == 1 and low_rows[0]["energy"] == 7776,
        "delta": len(low_rows) == 1
        and low_rows[0]["delta"] == Fraction(243, 1024),
        "sigma_positive": sigma > 0.0,
        "heavy_in_cut": len(low_rows) == 1
        and float(low_rows[0]["delta"]) < cutoff,
        "low_profile": len(low_rows) == 1 and low_rows[0]["size"] == 32,
        "Gsid": Gsid == Fraction(937024, 6859),
        "rate": rate > TAU,
        "artifact": artifact_match,
    }
    if not all(checks.values()):
        failed = sorted(name for name, passed in checks.items() if not passed)
        raise ValueError(f"independent C9 rebuild failed: {failed}")
    return {
        "M": M,
        "L": L,
        "barN": barN,
        "q": q,
        "sigma": sigma,
        "cutoff": cutoff,
        "low": low_rows[0],
        "Gsid": Gsid,
        "rate": rate,
        "checks": checks,
    }


def get_path(obj: dict[str, Any], *parts: str) -> Any:
    current: Any = obj
    for part in parts:
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


def validate_stored(cert: dict[str, Any], rebuilt: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    require(cert.get("schema") == "sidon-direct-payment-v2", "schema")
    require(cert.get("base_sha") == BASE_SHA, "base_sha")
    require(cert.get("payload_sha256") == payload_hash(cert), "self_hash")
    require(cert.get("all_pass") is True, "all_pass")
    require(
        get_path(cert, "proof_status", "literal_quantitative_interface")
        == "COUNTEREXAMPLE_NEW_FLOOR",
        "literal_verdict",
    )
    require(
        get_path(cert, "proof_status", "intended_deployed_smooth_residual")
        == "OPEN GAP",
        "deployed_verdict",
    )
    require(
        get_path(cert, "normalization", "derived_internally") is True
        and get_path(cert, "normalization", "external_barN_accepted") is False,
        "normalization_policy",
    )
    require(get_path(cert, "witness", "M") == rebuilt["M"], "M")
    require(get_path(cert, "witness", "L") == rebuilt["L"], "L")
    require(
        Fraction(
            get_path(cert, "witness", "barN_numerator"),
            get_path(cert, "witness", "barN_denominator"),
        )
        == rebuilt["barN"],
        "barN",
    )
    require(get_path(cert, "witness", "q") == rebuilt["q"], "q")
    require(
        abs(float(get_path(cert, "witness", "sigma")) - rebuilt["sigma"]) < 1e-15,
        "sigma",
    )
    require(
        get_path(cert, "witness", "Gsid_numerator") == rebuilt["Gsid"].numerator
        and get_path(cert, "witness", "Gsid_denominator")
        == rebuilt["Gsid"].denominator,
        "Gsid",
    )
    require(
        abs(float(get_path(cert, "witness", "rate")) - rebuilt["rate"]) < 1e-15
        and get_path(cert, "witness", "finite_gate_fails") is True,
        "rate",
    )
    low = get_path(cert, "witness", "low_energy_fibers")
    require(
        isinstance(low, list)
        and len(low) == 1
        and low[0].get("size") == rebuilt["low"]["size"]
        and low[0].get("energy") == rebuilt["low"]["energy"]
        and Fraction(
            low[0].get("delta_numerator"), low[0].get("delta_denominator")
        )
        == rebuilt["low"]["delta"],
        "low_fiber",
    )
    require(
        get_path(cert, "source_map", "checks", "all_fixed_weight") is True,
        "fixed_weight",
    )
    require(
        get_path(cert, "source_map", "checks", "field_prime_verified") is True,
        "field_prime",
    )
    require(get_path(cert, "c9_artifact", "match") is True, "artifact")
    require(
        get_path(cert, "claim_boundaries", "counterexample_to_intended_smooth_rows")
        is False
        and get_path(cert, "claim_boundaries", "closes_deployed_hard_input_b")
        is False,
        "scope",
    )
    return errors


def run_check() -> int:
    if not CERT.is_file():
        print("RESULT: FAIL missing certificate", file=sys.stderr)
        return 1
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    rebuilt = independent_rebuild()
    errors = validate_stored(cert, rebuilt)
    if errors:
        print("RESULT: FAIL " + ", ".join(errors), file=sys.stderr)
        return 1
    passed = sum(rebuilt["checks"].values())
    total = len(rebuilt["checks"])
    print("RESULT: PASS")
    print(f"independent checks: {passed}/{total}")
    print("route: tuple-support source map + pair-sum energy + exact Fraction moment")
    print(
        "witness: "
        f"M={rebuilt['M']} L={rebuilt['L']} "
        f"barN={rebuilt['barN'].numerator}/{rebuilt['barN'].denominator} "
        f"Gsid={rebuilt['Gsid'].numerator}/{rebuilt['Gsid'].denominator} "
        f"rate={rebuilt['rate']}"
    )
    print(
        "verdicts: literal=COUNTEREXAMPLE_NEW_FLOOR "
        "deployed_smooth=OPEN GAP"
    )
    print("payload_sha256:", cert["payload_sha256"])
    return 0


def run_tamper_selftest() -> int:
    if not CERT.is_file():
        print("RESULT: FAIL missing certificate", file=sys.stderr)
        return 1
    stored = json.loads(CERT.read_text(encoding="utf-8"))
    rebuilt = independent_rebuild()
    mutations: list[tuple[str, Any]] = [
        ("M", lambda d: d["witness"].__setitem__("M", 151)),
        ("L", lambda d: d["witness"].__setitem__("L", 120)),
        ("barN", lambda d: d["witness"].__setitem__("barN_denominator", 120)),
        ("q", lambda d: d["witness"].__setitem__("q", 2)),
        ("sigma", lambda d: d["witness"].__setitem__("sigma", 0.0)),
        ("Gsid", lambda d: d["witness"].__setitem__("Gsid_numerator", 1)),
        ("rate", lambda d: d["witness"].__setitem__("rate", 0.0)),
        (
            "heavy_size",
            lambda d: d["witness"]["low_energy_fibers"][0].__setitem__("size", 31),
        ),
        (
            "energy",
            lambda d: d["witness"]["low_energy_fibers"][0].__setitem__(
                "energy", 7775
            ),
        ),
        (
            "delta",
            lambda d: d["witness"]["low_energy_fibers"][0].__setitem__(
                "delta_numerator", 242
            ),
        ),
        (
            "fixed_weight",
            lambda d: d["source_map"]["checks"].__setitem__(
                "all_fixed_weight", False
            ),
        ),
        (
            "literal_verdict",
            lambda d: d["proof_status"].__setitem__(
                "literal_quantitative_interface", "OPEN GAP"
            ),
        ),
        (
            "deployed_verdict",
            lambda d: d["proof_status"].__setitem__(
                "intended_deployed_smooth_residual", "PROVED"
            ),
        ),
        (
            "scope",
            lambda d: d["claim_boundaries"].__setitem__(
                "counterexample_to_intended_smooth_rows", True
            ),
        ),
        ("artifact", lambda d: d["c9_artifact"].__setitem__("match", False)),
    ]
    undetected: list[str] = []
    for name, mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        candidate["payload_sha256"] = payload_hash(candidate)
        if not validate_stored(candidate, rebuilt):
            undetected.append(name)
    if undetected:
        print(
            "RESULT: FAIL undetected mutations: " + ", ".join(undetected),
            file=sys.stderr,
        )
        return 1
    print(f"tamper self-test: PASS {len(mutations)}/{len(mutations)}")
    print("RESULT: PASS")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args(argv)
    if sum((args.check, args.tamper_selftest)) != 1:
        parser.error("choose exactly one mode")
    if args.check:
        return run_check()
    return run_tamper_selftest()


if __name__ == "__main__":
    raise SystemExit(main())
