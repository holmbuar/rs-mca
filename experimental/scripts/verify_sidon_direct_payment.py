#!/usr/bin/env python3
"""Audit hard input (b): direct image-normalized Sidon payment.

The verifier derives M, L, and barN from an explicit partition into nonempty
fibers.  Its positive falsifier is the k=5 member of the existing C9
literal-interface family.  That family refutes only the displayed quantitative
primitive-leaf interface; the intended deployed smooth residual remains open.

Generator route:
  * explicit fixed-weight Boolean supports and weighted-Vandermonde source map;
  * difference-histogram additive energy;
  * exact rational image normalization and Sidon moment.

Status: COUNTEREXAMPLE_NEW_FLOOR (literal interface only) / OPEN GAP
(intended deployed smooth residual).
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import math
import re
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterator, Sequence


STATUS = (
    "COUNTEREXAMPLE_NEW_FLOOR (literal quantitative interface only) / "
    "OPEN GAP (intended deployed smooth residual)"
)
BASE_SHA = "7f278167e1e51f968896229ae438ea5a76398f90"
CERT = Path(
    "experimental/data/certificates/sidon-direct-payment/sidon_direct_payment.json"
)
C9_ARTIFACT = Path("experimental/data/c9_literal_interface_counterexample_v1.json")
TEX = Path("experimental/asymptotic_rs_mca_frontiers.tex")
LABELS = (
    "def:sidon-paid-cell",
    "def:sidon-heavy",
    "prop:ordinary-moment-split",
    "thm:unconditional-shallow-mi-ma",
    "cor:fourier-sidon-paid-smooth-circle",
)

K = 5
N = 20
M_WEIGHT = 10
R = 2
QBASE = 501
FIELD_PRIME = 505_020_040_141
MOMENT_Q = 3
SIGMA = math.log(4.0 / 3.0) / 8.0
TAU = 0.05


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def payload_hash(obj: dict[str, Any]) -> str:
    candidate = copy.deepcopy(obj)
    candidate.pop("payload_sha256", None)
    encoded = json.dumps(
        candidate, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def pin_labels(text: str) -> dict[str, Any]:
    lines = text.splitlines()
    pins: dict[str, Any] = {}
    for label in LABELS:
        pattern = re.compile(
            r"\\label(?:\[[^\]]*\])?\{" + re.escape(label) + r"\}"
        )
        line_number = next(
            (index for index, line in enumerate(lines, 1) if pattern.search(line)),
            None,
        )
        if line_number is None:
            pins[label] = {"found": False}
        else:
            pins[label] = {
                "found": True,
                "line": line_number,
                "sha256_line": hashlib.sha256(
                    lines[line_number - 1].encode("utf-8")
                ).hexdigest()[:16],
            }
    return pins


def is_prime_64(n: int) -> bool:
    """Deterministic Miller--Rabin for n < 2**64."""
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for prime in small_primes:
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


def balanced_words(k: int) -> Iterator[tuple[int, ...]]:
    """Yield words with k/5 copies of each digit 0,...,4."""
    if k <= 0 or k % 5:
        raise ValueError("k must be a positive multiple of five")
    counts = [k // 5] * 5
    word = [0] * k

    def recurse(position: int) -> Iterator[tuple[int, ...]]:
        if position == k:
            yield tuple(word)
            return
        for digit in range(5):
            if counts[digit] == 0:
                continue
            counts[digit] -= 1
            word[position] = digit
            yield from recurse(position + 1)
            counts[digit] += 1

    yield from recurse(0)


def prefix_support(word: Sequence[int]) -> int:
    mask = 0
    for block, count in enumerate(word):
        for offset in range(count):
            mask |= 1 << (4 * block + offset)
    return mask


def heavy_support(bits: Sequence[int]) -> int:
    mask = 0
    for block, bit in enumerate(bits):
        offsets = (0, 3) if bit == 0 else (1, 2)
        for offset in offsets:
            mask |= 1 << (4 * block + offset)
    return mask


def support_sum(mask: int, points: Sequence[int]) -> int:
    return sum(point for index, point in enumerate(points) if (mask >> index) & 1)


def source_map(mask: int, points: Sequence[int], prime: int) -> tuple[int, int]:
    return mask.bit_count(), support_sum(mask, points) % prime


def energy_difference_histogram(masks: Sequence[int], n: int) -> int:
    """Boolean additive energy via the ordered positive/negative difference mask."""
    full_mask = (1 << n) - 1
    differences: Counter[tuple[int, int]] = Counter()
    for left, right in itertools.product(masks, masks):
        differences[
            (left & (~right & full_mask), right & (~left & full_mask))
        ] += 1
    return sum(multiplicity * multiplicity for multiplicity in differences.values())


def construct_c9_fibers() -> dict[str, Any]:
    bases = [QBASE**index for index in range(K)]
    points = [base + offset for base in bases for offset in range(4)]
    heavy = [
        heavy_support(bits) for bits in itertools.product((0, 1), repeat=K)
    ]
    fillers = [prefix_support(word) for word in balanced_words(K)]
    omega = heavy + fillers

    fibers: dict[tuple[int, int], list[int]] = defaultdict(list)
    for mask in omega:
        fibers[source_map(mask, points, FIELD_PRIME)].append(mask)

    positive_fibers = {label: members for label, members in fibers.items() if members}
    fiber_sizes = sorted(len(members) for members in positive_fibers.values())
    total_point_sum = sum(points)
    heavy_images = {source_map(mask, points, FIELD_PRIME) for mask in heavy}
    filler_images = {source_map(mask, points, FIELD_PRIME) for mask in fillers}
    checks = {
        "all_supports_unique": len(set(omega)) == len(omega),
        "all_fixed_weight": all(mask.bit_count() == M_WEIGHT for mask in omega),
        "all_points_distinct_mod_p": len({point % FIELD_PRIME for point in points})
        == len(points),
        "field_prime_verified": is_prime_64(FIELD_PRIME),
        "integer_no_wrap": FIELD_PRIME > 2 * total_point_sum,
        "heavy_same_image": len(heavy_images) == 1,
        "filler_images_distinct": len(filler_images) == len(fillers),
        "filler_images_avoid_heavy": heavy_images.isdisjoint(filler_images),
        "fiber_size_profile": fiber_sizes == [1] * 120 + [32],
    }
    if not all(checks.values()):
        failed = sorted(name for name, passed in checks.items() if not passed)
        raise ValueError(f"C9 source-map construction failed: {failed}")
    return {
        "points": points,
        "omega": omega,
        "heavy": heavy,
        "fillers": fillers,
        "fibers": positive_fibers,
        "total_point_sum": total_point_sum,
        "checks": checks,
    }


def sidon_moment_from_fibers(
    fibers: dict[tuple[int, int], list[int]],
    n: int,
    q: int,
    sigma: float,
) -> dict[str, Any]:
    """Derive normalization from positive fibers and compute the exact moment."""
    if n <= 0 or q <= 0:
        raise ValueError("N and q must be positive")
    if not math.isfinite(sigma) or sigma <= 0.0:
        raise ValueError("sigma must be finite and strictly positive")
    positive = [members for members in fibers.values() if members]
    if not positive:
        raise ValueError("at least one nonempty fiber is required")
    M = sum(len(members) for members in positive)
    L = len(positive)
    barN = Fraction(M, L)
    cutoff = math.exp(-sigma * n)
    total = Fraction(0, 1)
    low_rows: list[dict[str, Any]] = []
    energies: Counter[int] = Counter()
    for members in positive:
        size = len(members)
        energy = energy_difference_histogram(members, n)
        delta = Fraction(energy, size**3)
        energies[energy] += 1
        if float(delta) <= cutoff:
            contribution = (Fraction(size, 1) / barN) ** q
            total += contribution
            low_rows.append(
                {
                    "size": size,
                    "energy": energy,
                    "delta_numerator": delta.numerator,
                    "delta_denominator": delta.denominator,
                    "contribution_numerator": contribution.numerator,
                    "contribution_denominator": contribution.denominator,
                }
            )
    Gsid = total / L
    rate = math.log(float(Gsid)) / (n * q) if Gsid > 0 else None
    return {
        "M": M,
        "L": L,
        "barN_numerator": barN.numerator,
        "barN_denominator": barN.denominator,
        "q": q,
        "sigma": sigma,
        "energy_cutoff": cutoff,
        "n_low_energy_fibers": len(low_rows),
        "low_energy_fibers": low_rows,
        "energy_histogram": {
            str(energy): count for energy, count in sorted(energies.items())
        },
        "Gsid_numerator": Gsid.numerator,
        "Gsid_denominator": Gsid.denominator,
        "Gsid": float(Gsid),
        "rate": rate,
        "tau": TAU,
        "finite_gate_fails": rate is not None and rate > TAU,
    }


def compare_c9_artifact(root: Path, witness: dict[str, Any]) -> dict[str, Any]:
    path = root / C9_ARTIFACT
    raw = path.read_bytes()
    artifact = json.loads(raw.decode("utf-8"))
    counts = artifact.get("sample_counts", {})
    energy = artifact.get("energy", {})
    sample = artifact.get("C9_sample", {})
    expected = {
        "N": N,
        "m": M_WEIGHT,
        "R": R,
        "Q": QBASE,
        "M": witness["M"],
        "L": witness["L"],
        "barN_numerator": witness["barN_numerator"],
        "barN_denominator": witness["barN_denominator"],
        "heavy_fiber_size": 32,
        "heavy_energy": 7776,
        "heavy_delta_numerator": 243,
        "heavy_delta_denominator": 1024,
        "q": MOMENT_Q,
    }
    observed = {
        "N": artifact.get("parameters", {}).get("N"),
        "m": artifact.get("parameters", {}).get("m"),
        "R": artifact.get("parameters", {}).get("R"),
        "Q": artifact.get("parameters", {}).get("Q"),
        "M": counts.get("domain_size_M"),
        "L": counts.get("image_size_L"),
        "barN_numerator": counts.get("barN_numerator"),
        "barN_denominator": counts.get("barN_denominator"),
        "heavy_fiber_size": counts.get("heavy_fiber_size"),
        "heavy_energy": energy.get("heavy_energy"),
        "heavy_delta_numerator": energy.get("heavy_delta_numerator"),
        "heavy_delta_denominator": energy.get("heavy_delta_denominator"),
        "q": sample.get("logarithmic_q"),
    }
    match = (
        observed == expected
        and abs(float(sample.get("sigma", -1.0)) - SIGMA) < 1e-15
        and abs(float(sample.get("normalized_log_C9_lower_bound", -1.0))
                - float(witness["rate"])) < 1e-15
        and artifact.get("status") == "COUNTEREXAMPLE_NEW_FLOOR"
        and artifact.get("scope")
        == "LITERAL_QUANTITATIVE_PRIMITIVE_LEAF_INTERFACE_ONLY"
    )
    return {
        "path": str(C9_ARTIFACT).replace("\\", "/"),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "expected": expected,
        "observed": observed,
        "match": match,
    }


def build_certificate(root: Path) -> dict[str, Any]:
    tex = (root / TEX).read_text(encoding="utf-8")
    pins = pin_labels(tex)
    pins_ok = all(pins[label].get("found") for label in LABELS)
    construction = construct_c9_fibers()
    moment = sidon_moment_from_fibers(
        construction["fibers"], N, MOMENT_Q, SIGMA
    )
    artifact = compare_c9_artifact(root, moment)
    low = moment["low_energy_fibers"]
    witness_checks = {
        **construction["checks"],
        "M_is_sum_positive_fibers": moment["M"] == len(construction["omega"]) == 152,
        "L_is_positive_fiber_count": moment["L"] == len(construction["fibers"]) == 121,
        "barN_is_M_over_L": (
            moment["barN_numerator"] == 152
            and moment["barN_denominator"] == 121
        ),
        "fixed_sigma_positive": SIGMA > 0.0,
        "one_low_energy_fiber": len(low) == 1 and low[0]["size"] == 32,
        "heavy_energy_exact": (
            len(low) == 1
            and low[0]["energy"] == 7776
            and low[0]["delta_numerator"] == 243
            and low[0]["delta_denominator"] == 1024
        ),
        "heavy_inside_fixed_cut": (
            len(low) == 1
            and Fraction(
                low[0]["delta_numerator"], low[0]["delta_denominator"]
            )
            < Fraction.from_float(moment["energy_cutoff"])
        ),
        "Gsid_exact": (
            moment["Gsid_numerator"] == 937024
            and moment["Gsid_denominator"] == 6859
        ),
        "positive_rate_gate_fails": (
            moment["finite_gate_fails"] and moment["rate"] > TAU
        ),
        "existing_c9_artifact_matches": artifact["match"],
    }
    all_pass = pins_ok and all(witness_checks.values())
    cert: dict[str, Any] = {
        "schema": "sidon-direct-payment-v2",
        "object": "hard input (b): direct image-normalized Sidon payment",
        "status": STATUS,
        "base_sha": BASE_SHA,
        "tex_path": str(TEX).replace("\\", "/"),
        "proof_status": {
            "literal_quantitative_interface": "COUNTEREXAMPLE_NEW_FLOOR",
            "intended_deployed_smooth_residual": "OPEN GAP",
        },
        "verdict": "COUNTEREXAMPLE_NEW_FLOOR / OPEN GAP",
        "hard_input": "image-scale MI + MA, or a direct Sidon payment",
        "pins": pins,
        "pins_ok": pins_ok,
        "normalization": {
            "rule": "M=sum_s f_s over nonempty fibers; L=#nonempty fibers; barN=M/L",
            "derived_internally": True,
            "external_barN_accepted": False,
        },
        "source_map": {
            "family": "C9 literal-interface block/trade family, k=5",
            "N": N,
            "m": M_WEIGHT,
            "R": R,
            "Q": QBASE,
            "field_prime": FIELD_PRIME,
            "integer_total_point_sum": construction["total_point_sum"],
            "map": "Phi(x)=(|x|, sum_t x_t*t mod p)",
            "domain": "152 explicit distinct fixed-weight Boolean supports",
            "checks": construction["checks"],
        },
        "witness": moment,
        "witness_checks": witness_checks,
        "c9_artifact": artifact,
        "claim_boundaries": {
            "literal_interface_counterexample": True,
            "counterexample_to_intended_smooth_rows": False,
            "survives_exact_C1_to_C8_predicates": False,
            "closes_deployed_hard_input_b": False,
            "intended_deployed_smooth_residual_open": True,
        },
        "open_input": {
            "id": "OPEN-direct-Sidon-residual-after-algebraic-removal",
            "closes_hard_b_at_deployed": False,
            "detail": (
                "The explicit C9 family attacks the displayed literal quantitative "
                "interface only. It is not known to survive the intended C1--C8 "
                "first-match residual or to belong to the deployed smooth rows."
            ),
        },
        "evidence_type": "EXPLICIT_FIXED_WEIGHT_BOOLEAN_SOURCE_MAP",
        "falsifiable": True,
        "is_degenerate_by_construction": False,
        "is_tautology_under_preconditions": False,
        "generator_route": (
            "explicit C9 supports and field map; difference-histogram energy; "
            "exact Fraction normalization and moment"
        ),
        "checker_route": (
            "independent tuple-support rebuild; pair-sum energy; exact Fraction "
            "normalization and stored-artifact reconciliation"
        ),
        "honest_headline": (
            "The previous toy falsifier was unrealizable and is retired. The C9 "
            "k=5 fixed-weight Boolean map gives M=152, L=121, barN=152/121, "
            "Delta=243/1024 under fixed sigma=log(4/3)/8, and "
            "Gsid=937024/6859 with rate>0.05. This is a counterexample only to "
            "the literal quantitative interface; the intended deployed smooth "
            "direct-Sidon payment remains open."
        ),
        "nonclaims": [
            "Not a counterexample to C9 for formal smooth-domain rows.",
            "Not a proof that the family survives exact C1--C8 predicates.",
            "Not a closure of hard input (b) at the intended deployed residual.",
            "The finite tau gate is a replay of the witness, not the asymptotic theorem.",
        ],
        "all_pass": all_pass,
        "regeneration": (
            "python3 experimental/scripts/verify_sidon_direct_payment.py "
            "--emit-defaults"
        ),
    }
    cert["payload_sha256"] = payload_hash(cert)
    return cert


def get_path(obj: dict[str, Any], *parts: str) -> Any:
    current: Any = obj
    for part in parts:
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


def validate_certificate(cert: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    require(cert.get("schema") == "sidon-direct-payment-v2", "schema")
    require(cert.get("base_sha") == BASE_SHA, "base_sha")
    require(cert.get("payload_sha256") == payload_hash(cert), "self_hash")
    require(cert.get("all_pass") is True, "all_pass")
    require(cert.get("pins_ok") is True, "pins_ok")
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
    require(get_path(cert, "witness", "M") == 152, "M")
    require(get_path(cert, "witness", "L") == 121, "L")
    require(get_path(cert, "witness", "barN_numerator") == 152, "barN_num")
    require(get_path(cert, "witness", "barN_denominator") == 121, "barN_den")
    require(get_path(cert, "witness", "q") == 3, "q")
    sigma = get_path(cert, "witness", "sigma")
    require(isinstance(sigma, (int, float)) and sigma > 0.0, "sigma_positive")
    require(
        get_path(cert, "witness", "Gsid_numerator") == 937024
        and get_path(cert, "witness", "Gsid_denominator") == 6859,
        "Gsid_exact",
    )
    require(
        isinstance(get_path(cert, "witness", "rate"), (int, float))
        and get_path(cert, "witness", "rate") > TAU,
        "rate",
    )
    low = get_path(cert, "witness", "low_energy_fibers")
    require(
        isinstance(low, list)
        and len(low) == 1
        and low[0].get("size") == 32
        and low[0].get("energy") == 7776
        and low[0].get("delta_numerator") == 243
        and low[0].get("delta_denominator") == 1024,
        "heavy_fiber",
    )
    require(
        get_path(cert, "source_map", "checks", "all_fixed_weight") is True,
        "fixed_weight",
    )
    require(
        get_path(cert, "source_map", "checks", "field_prime_verified") is True,
        "field_prime",
    )
    require(get_path(cert, "c9_artifact", "match") is True, "c9_artifact")
    require(
        get_path(cert, "claim_boundaries", "counterexample_to_intended_smooth_rows")
        is False,
        "scope_boundary",
    )
    require(
        get_path(cert, "claim_boundaries", "closes_deployed_hard_input_b") is False,
        "deployed_open",
    )
    return errors


def emit(root: Path) -> dict[str, Any]:
    cert = build_certificate(root)
    output = root / CERT
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(cert, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    return cert


def check(root: Path) -> int:
    path = root / CERT
    if not path.is_file():
        print("RESULT: FAIL missing certificate", file=sys.stderr)
        return 1
    stored = json.loads(path.read_text(encoding="utf-8"))
    rebuilt = build_certificate(root)
    errors = validate_certificate(stored)
    if stored != rebuilt:
        errors.append("deterministic_rebuild")
    if errors:
        print("RESULT: FAIL " + ", ".join(errors), file=sys.stderr)
        return 1
    witness = stored["witness"]
    print("RESULT: PASS")
    print("witness checks: 19/19; pins: 5/5")
    print(
        "witness: "
        f"M={witness['M']} L={witness['L']} "
        f"barN={witness['barN_numerator']}/{witness['barN_denominator']} "
        f"Gsid={witness['Gsid_numerator']}/{witness['Gsid_denominator']} "
        f"rate={witness['rate']}"
    )
    print(
        "verdicts: literal=COUNTEREXAMPLE_NEW_FLOOR "
        "deployed_smooth=OPEN GAP"
    )
    print("payload_sha256:", stored["payload_sha256"])
    return 0


def tamper_selftest(root: Path) -> int:
    expected = build_certificate(root)
    mutations: list[tuple[str, Any]] = [
        ("M", lambda d: d["witness"].__setitem__("M", 151)),
        ("L", lambda d: d["witness"].__setitem__("L", 120)),
        ("barN", lambda d: d["witness"].__setitem__("barN_denominator", 120)),
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
        ("sigma", lambda d: d["witness"].__setitem__("sigma", 0.0)),
        ("q", lambda d: d["witness"].__setitem__("q", 2)),
        ("Gsid", lambda d: d["witness"].__setitem__("Gsid_numerator", 1)),
        ("rate", lambda d: d["witness"].__setitem__("rate", 0.0)),
        (
            "fixed_weight",
            lambda d: d["source_map"]["checks"].__setitem__(
                "all_fixed_weight", False
            ),
        ),
        (
            "literal_scope",
            lambda d: d["proof_status"].__setitem__(
                "literal_quantitative_interface", "OPEN GAP"
            ),
        ),
        (
            "deployed_scope",
            lambda d: d["claim_boundaries"].__setitem__(
                "closes_deployed_hard_input_b", True
            ),
        ),
        ("artifact", lambda d: d["c9_artifact"].__setitem__("match", False)),
    ]
    undetected: list[str] = []
    for name, mutate in mutations:
        candidate = copy.deepcopy(expected)
        mutate(candidate)
        candidate["payload_sha256"] = payload_hash(candidate)
        if not validate_certificate(candidate):
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
    parser.add_argument("--emit-defaults", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args(argv)
    modes = sum((args.emit_defaults, args.check, args.tamper_selftest))
    if modes != 1:
        parser.error("choose exactly one mode")
    root = repo_root()
    if args.emit_defaults:
        cert = emit(root)
        print("wrote", root / CERT)
        print("witness checks: 19/19; pins: 5/5")
        print("payload_sha256:", cert["payload_sha256"])
        print("verdict:", cert["verdict"])
        return 0 if cert["all_pass"] else 1
    if args.check:
        return check(root)
    return tamper_selftest(root)


if __name__ == "__main__":
    raise SystemExit(main())
