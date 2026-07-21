#!/usr/bin/env python3
"""Verify the F_8 trace--Vandermonde coherent-orbit floor certificate.

The verifier is Python-standard-library only.  Every acceptance gate uses
explicit exceptions rather than ``assert``, so ``python3 -O`` checks the same
conditions as the ordinary interpreter.
"""

from __future__ import annotations

import argparse
import copy
import itertools
import json
from pathlib import Path
from typing import Any, Iterable, Sequence

EXPECTED_SCHEMA = "rs-mca.trace-vandermonde-coherent-orbit-floor.v1"
EXPECTED_BASE_SHA = "4e5f0b77c98f075ea7c8822cd4859847a232bc2a"
EXPECTED_UPSTREAM_SHA = "a3017697ad1594521d2779fe1d83bccd45d4c06e"
EXPECTED_SOURCE_BLOBS = {
    "experimental/grande_finale.tex":
        "8a5d9791900ca9eed773feba146b92ad296704ce",
    "experimental/rs_mca_thresholds.tex":
        "01302a797c502a05ed0b11ba949b8756e0aa2b22",
    "experimental/notes/thresholds/minimal_phase_supplement.md":
        "6b1482b86e5eaad2046a41c5a122b86514a78a10",
}
DEFAULT_CERTIFICATE = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "certificates"
    / "trace-vandermonde-coherent-orbit-floor"
    / "trace_vandermonde_coherent_orbit_floor.json"
)


class VerificationError(RuntimeError):
    """Raised when one exact certificate gate fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def bit(a: int, k: int) -> int:
    return (a >> k) & 1


def gf8_add(a: int, b: int) -> int:
    require(0 <= a < 8 and 0 <= b < 8, "F_8 addition input out of range")
    return a ^ b


def gf8_mul(a: int, b: int) -> int:
    """Multiply in F_2[x]/(x^3+x+1), encoded in three low bits."""
    require(0 <= a < 8 and 0 <= b < 8, "F_8 multiplication input out of range")
    a0, a1, a2 = (bit(a, i) for i in range(3))
    b0, b1, b2 = (bit(b, i) for i in range(3))
    c0 = a0 * b0
    c1 = a0 * b1 + a1 * b0
    c2 = a0 * b2 + a1 * b1 + a2 * b0
    c3 = a1 * b2 + a2 * b1
    c4 = a2 * b2
    # x^3 = x+1 and x^4 = x^2+x modulo x^3+x+1.
    r0 = (c0 + c3) & 1
    r1 = (c1 + c3 + c4) & 1
    r2 = (c2 + c4) & 1
    return r0 + 2 * r1 + 4 * r2


def gf8_pow(a: int, exponent: int) -> int:
    require(0 <= a < 8 and exponent >= 0, "invalid F_8 power input")
    result = 1
    base = a
    e = exponent
    while e:
        if e & 1:
            result = gf8_mul(result, base)
        base = gf8_mul(base, base)
        e >>= 1
    return result


def gf8_trace(a: int) -> int:
    value = gf8_add(gf8_add(a, gf8_pow(a, 2)), gf8_pow(a, 4))
    require(value in (0, 1), "absolute trace did not land in F_2")
    return value


Vector = tuple[int, int, int]


def vec_add(left: Vector, right: Vector) -> Vector:
    return tuple(gf8_add(x, y) for x, y in zip(left, right, strict=True))  # type: ignore[return-value]


def vec_sum(vectors: Iterable[Vector]) -> Vector:
    total: Vector = (0, 0, 0)
    for vector in vectors:
        total = vec_add(total, vector)
    return total


def column(t: int) -> Vector:
    return (t, gf8_pow(t, 2), gf8_pow(t, 3))


def dot(coeff: Vector, vector: Vector) -> int:
    value = 0
    for a, b in zip(coeff, vector, strict=True):
        value = gf8_add(value, gf8_mul(a, b))
    return value


def phase_pattern(coeff: Vector, domain: Sequence[int]) -> tuple[int, ...]:
    return tuple(gf8_trace(dot(coeff, column(t))) for t in domain)


def incidence_pattern(support: Sequence[int], domain: Sequence[int]) -> tuple[int, ...]:
    support_set = set(support)
    return tuple(1 if t in support_set else 0 for t in domain)


def fixed_weight_coefficient(
    pattern: Sequence[int], supports: Sequence[tuple[int, ...]], domain: Sequence[int]
) -> int:
    position = {t: i for i, t in enumerate(domain)}
    total = 0
    for support in supports:
        parity = sum(pattern[position[t]] for t in support) & 1
        total += 1 if parity == 0 else -1
    return total


def canonical_records(records: Any) -> list[dict[str, Any]]:
    require(isinstance(records, list), "records must be a list")
    require(all(isinstance(record, dict) for record in records), "record is not an object")
    return records


def verify(data: dict[str, Any]) -> dict[str, int]:
    require(data.get("schema") == EXPECTED_SCHEMA, "schema mismatch")
    require(data.get("status") == "COUNTEREXAMPLE_NEW_FLOOR", "status mismatch")
    require(data.get("acceptance_criterion") == 4, "acceptance criterion is not 4")
    require(
        data.get("named_floor") == "RS_TRACE_VANDERMONDE_COHERENT_ORBIT_FLOOR",
        "named floor mismatch",
    )
    require(
        data.get("named_successor_residual")
        == "POST_C1_C8_RS_ORBIT_DECORRELATION_OR_DIRECT_SIDON",
        "named successor residual mismatch",
    )

    repository = data.get("repository")
    require(isinstance(repository, dict), "repository ledger missing")
    require(repository.get("base_sha") == EXPECTED_BASE_SHA, "stale fork base SHA")
    require(
        repository.get("upstream_main_sha") == EXPECTED_UPSTREAM_SHA,
        "stale upstream-main SHA",
    )
    require(data.get("source_blobs") == EXPECTED_SOURCE_BLOBS, "source blob ledger mismatch")

    finite = data.get("finite_falsifier")
    require(isinstance(finite, dict), "finite falsifier object missing")
    field = finite.get("field")
    params = finite.get("rs_parameters")
    require(isinstance(field, dict) and isinstance(params, dict), "field/RS ledger missing")

    require(field.get("name") == "F_8", "wrong finite field")
    require(field.get("characteristic") == 2, "wrong characteristic")
    require(field.get("extension_degree") == 3, "wrong extension degree")
    require(field.get("modulus_polynomial") == "x^3+x+1", "wrong modulus polynomial")
    require(field.get("modulus_bits") == 0b1011, "wrong modulus bits")
    require(field.get("primitive_element") == 2, "wrong primitive element")
    primitive_cycle = [gf8_pow(2, exponent) for exponent in range(7)]
    require(field.get("primitive_power_cycle") == primitive_cycle, "primitive cycle mismatch")
    require(len(set(primitive_cycle)) == 7 and gf8_pow(2, 7) == 1, "2 is not order seven")

    domain = params.get("domain")
    require(domain == list(range(1, 8)), "domain is not F_8^times in canonical order")
    require(params.get("q") == 8, "wrong q")
    require(params.get("N") == 7, "wrong N")
    require(params.get("R") == 3, "wrong R")
    require(params.get("m") == 2, "wrong m")
    require(params.get("parity_exponents") == [1, 2, 3], "wrong parity exponents")

    expected_columns = [{"t": t, "coords": list(column(t))} for t in domain]
    require(params.get("parity_columns") == expected_columns, "Vandermonde columns mismatch")

    supports = list(itertools.combinations(domain, 2))
    require(len(supports) == 21, "support count mismatch")
    syndromes = [vec_sum(column(t) for t in support) for support in supports]
    support_records = [
        {"support": list(support), "syndrome": list(syndrome)}
        for support, syndrome in zip(supports, syndromes, strict=True)
    ]
    require(finite.get("supports") == support_records, "support/syndrome enumeration mismatch")
    require(len(set(syndromes)) == 21, "weight-two RS syndrome map is not injective")

    source_mass = len(supports)
    realized_image_size = len(set(syndromes))
    multiplicities = {syndrome: syndromes.count(syndrome) for syndrome in set(syndromes)}
    max_fiber = max(multiplicities.values(), default=0)
    require(finite.get("source_mass_M") == source_mass == 21, "source mass mismatch")
    require(
        finite.get("realized_image_size_L") == realized_image_size == 21,
        "realized image mismatch",
    )
    require(finite.get("max_fiber") == max_fiber == 1, "max-fiber mismatch")

    anchor = column(domain[0])
    difference_generators = [vec_add(column(t), anchor) for t in domain[1:]]
    require(
        finite.get("difference_generators") == [list(v) for v in difference_generators],
        "difference-generator list mismatch",
    )
    difference_span = {
        vec_sum(difference_generators[index] for index in range(6) if mask & (1 << index))
        for mask in range(1 << 6)
    }
    require(len(difference_span) == 64, "effective difference span is not full")
    require(finite.get("difference_span_size") == 64, "difference-span size mismatch")
    require(finite.get("effective_target_size_A_eff") == 64, "A_eff mismatch")

    all_coefficients = list(itertools.product(range(8), repeat=3))
    trace_patterns = {phase_pattern(coeff, domain) for coeff in all_coefficients}
    require(len(trace_patterns) == 64, "trace-phase image does not have 64 patterns")
    require(all(sum(pattern) % 2 == 0 for pattern in trace_patterns), "odd trace phase found")
    weight_census = {
        str(weight): sum(1 for pattern in trace_patterns if sum(pattern) == weight)
        for weight in (0, 2, 4, 6)
    }
    require(
        weight_census == {"0": 1, "2": 21, "4": 35, "6": 7},
        "trace-phase weight census mismatch",
    )
    require(finite.get("trace_phase_image_size") == 64, "trace-phase image size mismatch")
    require(finite.get("trace_phase_weight_census") == weight_census, "weight census ledger mismatch")

    orbit = finite.get("coherent_orbit")
    require(isinstance(orbit, dict), "coherent orbit missing")
    orbit_supports = list(itertools.combinations(domain, 4))
    records = canonical_records(orbit.get("records"))
    require(orbit.get("character_weight") == 4, "wrong orbit character weight")
    require(orbit.get("orbit_size") == len(orbit_supports) == 35, "orbit size mismatch")
    require(len(records) == 35, "orbit record count mismatch")

    coefficients: list[int] = []
    seen_witnesses: set[Vector] = set()
    for index, (expected_support, record) in enumerate(
        zip(orbit_supports, records, strict=True)
    ):
        require(
            record.get("character_support") == list(expected_support),
            f"orbit support mismatch at record {index}",
        )
        raw_witness = record.get("coefficient_vector")
        require(
            isinstance(raw_witness, list)
            and len(raw_witness) == 3
            and all(isinstance(value, int) and 0 <= value < 8 for value in raw_witness),
            f"invalid coefficient vector at record {index}",
        )
        witness: Vector = tuple(raw_witness)  # type: ignore[assignment]
        require(witness not in seen_witnesses, f"duplicate witness at record {index}")
        seen_witnesses.add(witness)
        pattern = phase_pattern(witness, domain)
        expected_pattern = incidence_pattern(expected_support, domain)
        require(pattern == expected_pattern, f"trace-phase realization failed at record {index}")
        require(record.get("trace_pattern") == list(pattern), f"stored trace pattern mismatch at {index}")
        coefficient = fixed_weight_coefficient(pattern, supports, domain)
        require(coefficient == -3, f"orbit coefficient is not -3 at record {index}")
        require(
            record.get("fixed_weight_coefficient") == coefficient,
            f"stored coefficient mismatch at record {index}",
        )
        anchor_bit = pattern[0]
        anchored_pattern = tuple((value + anchor_bit) & 1 for value in pattern)
        require(
            record.get("anchored_trace_pattern_at_t1") == list(anchored_pattern),
            f"stored anchored trace pattern mismatch at record {index}",
        )
        anchored_coefficient = fixed_weight_coefficient(
            anchored_pattern, supports, domain
        )
        require(
            anchored_coefficient == coefficient == -3,
            f"anchor translation changed the weight-two coefficient at record {index}",
        )
        require(
            record.get("anchored_fixed_weight_coefficient") == anchored_coefficient,
            f"stored anchored coefficient mismatch at record {index}",
        )
        coefficients.append(anchored_coefficient)

    coherent_sum = sum(coefficients)
    coherent_magnitude = abs(coherent_sum)
    require(orbit.get("common_coefficient") == -3, "common coefficient ledger mismatch")
    require(orbit.get("coherent_signed_sum") == coherent_sum == -105, "coherent sum mismatch")
    require(
        orbit.get("coherent_magnitude_H") == coherent_magnitude == 105,
        "coherent magnitude mismatch",
    )
    require(
        orbit.get("source_normalized_numerator") == 105
        and orbit.get("source_normalized_denominator") == 21
        and orbit.get("source_normalized_value_integer") == 5,
        "source-normalized aggregate mismatch",
    )
    require(105 == 5 * 21, "source normalization did not clear exactly")
    require(
        orbit.get("image_compensated_numerator") == 105
        and orbit.get("image_compensated_denominator") == 64,
        "image-compensated aggregate mismatch",
    )
    cleared = orbit.get("cleared_image_compensated_strict_inequality")
    require(isinstance(cleared, dict), "cleared inequality object missing")
    left = 64 * source_mass
    right = realized_image_size * coherent_magnitude
    require(cleared.get("left_A_eff_times_M") == left == 1344, "left cleared value mismatch")
    require(cleared.get("right_L_times_H") == right == 2205, "right cleared value mismatch")
    require(left < right, "image-compensated coherent aggregate is not greater than one")

    # The finite row is the r=2 specialization of the printed family formulas.
    r = 2
    require(
        len(orbit_supports) == __import__("math").comb(4 * r - 1, 2 * r),
        "general orbit-size formula fails at r=2",
    )
    require(
        abs(coefficients[0]) == __import__("math").comb(2 * r - 1, r // 2),
        "general coefficient formula fails at r=2",
    )
    require(
        coherent_magnitude
        == __import__("math").comb(4 * r - 1, 2 * r)
        * __import__("math").comb(2 * r - 1, r // 2),
        "general coherent-magnitude formula fails at r=2",
    )
    require(
        coherent_magnitude * ((4 * r + 1) * (r + 1))
        >= (2 ** (r + 1)) * 64,
        "printed general lower bound fails at r=2",
    )

    return {
        "field_elements_checked": 64,
        "supports_checked": len(supports),
        "difference_subsets_checked": 64,
        "trace_coefficients_checked": len(all_coefficients),
        "orbit_records_checked": len(records),
        "exact_gates": 26 + len(records) * 11,
    }


def load_certificate(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    require(isinstance(value, dict), "certificate root is not an object")
    return value


def tamper_selftest(original: dict[str, Any]) -> int:
    mutations: list[tuple[str, Any]] = []

    value = copy.deepcopy(original)
    value["finite_falsifier"]["source_mass_M"] = 22
    mutations.append(("source mass", value))

    value = copy.deepcopy(original)
    value["finite_falsifier"]["supports"][0]["syndrome"][0] ^= 1
    mutations.append(("syndrome", value))

    value = copy.deepcopy(original)
    value["finite_falsifier"]["coherent_orbit"]["records"][0]["coefficient_vector"][2] ^= 1
    mutations.append(("phase witness", value))

    value = copy.deepcopy(original)
    value["finite_falsifier"]["coherent_orbit"]["coherent_signed_sum"] = -104
    mutations.append(("coherent sum", value))

    value = copy.deepcopy(original)
    value["repository"]["base_sha"] = "0" * 40
    mutations.append(("base SHA", value))

    value = copy.deepcopy(original)
    value["source_blobs"]["experimental/grande_finale.tex"] = "f" * 40
    mutations.append(("source blob", value))

    rejected = 0
    for name, mutation in mutations:
        try:
            verify(mutation)
        except VerificationError:
            rejected += 1
        else:
            raise VerificationError(f"tamper mutation was accepted: {name}")
    require(rejected == len(mutations), "not every tamper mutation was rejected")
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "certificate",
        nargs="?",
        type=Path,
        default=DEFAULT_CERTIFICATE,
        help="path to the canonical certificate JSON",
    )
    parser.add_argument("--check", action="store_true", help="verify the certificate")
    parser.add_argument(
        "--tamper-selftest",
        action="store_true",
        help="verify that six independent corruptions are rejected",
    )
    args = parser.parse_args()

    if not args.check and not args.tamper_selftest:
        parser.error("choose --check and/or --tamper-selftest")

    data = load_certificate(args.certificate)
    if args.check:
        counts = verify(data)
        print(
            "PASS trace-Vandermonde coherent-orbit floor: "
            f"{counts['supports_checked']} supports, "
            f"{counts['trace_coefficients_checked']} trace coefficients, "
            f"{counts['orbit_records_checked']} coherent characters, "
            f"{counts['exact_gates']} exact gates"
        )
    if args.tamper_selftest:
        rejected = tamper_selftest(data)
        print(f"PASS tamper self-test: {rejected}/6 mutations rejected")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except VerificationError as exc:
        print(f"FAIL: {exc}")
        raise SystemExit(1)
