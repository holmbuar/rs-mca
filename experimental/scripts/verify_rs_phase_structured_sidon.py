#!/usr/bin/env python3
"""Exact stdlib verifier for the RS phase-structured Sidon packet.

The verifier recomputes the actual Mersenne-31 Chebyshev-domain leaf, the
explicit C1 owner complement, the realized second-power-sum image, quadratic
locator phases, the 32-pair cancellation certificate, and all printed integer
aggregates.  It also runs three mutation tests proving the gates are live.

No floating point and no third-party packages are used.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CERT = (
    ROOT
    / "experimental/data/certificates/rs-phase-structured-sidon/"
      "rs_phase_structured_sidon.json"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def mask_weight(mask: int) -> int:
    return sum((mask >> i) & 1 for i in range(8))


def chebyshev_double(x: int, p: int) -> int:
    return (2 * (x % p) * (x % p) - 1) % p


def chebyshev_pow_two(exponent: int, x: int, p: int) -> int:
    for _ in range(exponent):
        x = chebyshev_double(x, p)
    return x % p


def selected_product(mask: int, domain: list[int], p: int) -> int:
    value = 1
    for i, x in enumerate(domain):
        if (mask >> i) & 1:
            value = (value * x) % p
    return value


def sum_power(mask: int, exponent: int, domain: list[int], p: int) -> int:
    return sum(
        pow(x, exponent, p)
        for i, x in enumerate(domain)
        if (mask >> i) & 1
    ) % p


def quadratic_phase(mask: int, domain: list[int], p: int) -> int:
    value = pow(selected_product(mask, domain, p), (p - 1) // 2, p)
    require(value in (1, p - 1), f"zero/nonquadratic Euler output for mask {mask}")
    return 1 if value == 1 else -1


def realized_data(
    domain: list[int], p: int, owned_masks: list[int]
) -> dict[str, Any]:
    full = [m for m in range(256) if mask_weight(m) == 4]
    residual = [m for m in full if m not in set(owned_masks)]

    image: list[int] = []
    for mask in residual:
        key = sum_power(mask, 2, domain, p)
        if key not in image:
            image.append(key)

    fibers = {
        key: [m for m in residual if sum_power(m, 2, domain, p) == key]
        for key in image
    }
    coefficients = {
        key: sum(quadratic_phase(m, domain, p) for m in fibers[key])
        for key in image
    }

    return {
        "full": full,
        "residual": residual,
        "image": image,
        "fibers": fibers,
        "coefficients": coefficients,
    }


def complete_pair_owners() -> list[int]:
    pair_masks = [5, 10, 80, 160]
    return sorted(a | b for a, b in itertools.combinations(pair_masks, 2))


def verify_certificate(cert: dict[str, Any], *, mutation_tests: bool = True) -> None:
    require(cert["schema"] == "rs-phase-structured-sidon-v1", "schema")
    require(cert["status"] == "PROVED_SCOPED_PHASE_PAYMENT", "status")
    require(cert["acceptance_gate_criterion"] == 2, "acceptance criterion")

    base = cert["base"]
    require(
        base["fork_main_sha"] == "4e5f0b77c98f075ea7c8822cd4859847a232bc2a",
        "fork base pin",
    )
    require(
        base["upstream_main_sha"] == "a3017697ad1594521d2779fe1d83bccd45d4c06e",
        "upstream base pin",
    )

    field = cert["field"]
    p = int(field["prime"])
    domain = list(map(int, field["domain"]))
    require(p == 2**31 - 1, "M31 prime")
    require(len(domain) == 8 and len(set(domain)) == 8, "domain cardinality/nodup")
    require(
        all(chebyshev_pow_two(field["chebyshev_power"], x, p) == 0 for x in domain),
        "all domain points are T_(2^21) roots",
    )
    for i, j in field["antipodal_index_pairs"]:
        require((domain[i] + domain[j]) % p == 0, f"antipodal pair {(i, j)}")

    owner = cert["owner"]
    owned_masks = list(map(int, owner["owned_masks"]))
    require(sorted(owned_masks) == complete_pair_owners(), "exact C1 complete-fiber masks")

    data = realized_data(domain, p, owned_masks)
    expected = cert["expected"]
    require(len(data["full"]) == expected["full_slice_card"] == 70, "full slice")
    require(len(owned_masks) == expected["c1_owned_card"] == 6, "owner size")
    require(len(data["residual"]) == expected["residual_slice_card"] == 64, "residual")

    image = data["image"]
    fibers = data["fibers"]
    coefficients = data["coefficients"]
    require(image == expected["realized_image_keys"], "realized image order/content")
    require(len(image) == expected["realized_image_card"] == 9, "A_eff=L=9")
    require([len(fibers[k]) for k in image] == expected["fiber_sizes"], "fiber sizes")
    require([coefficients[k] for k in image] == expected["phase_coefficients"], "coefficients")

    pairs = [tuple(map(int, pair)) for pair in cert["phase"]["cancellation_pairs"]]
    require(len(pairs) == 32, "pair count")
    flattened = [m for pair in pairs for m in pair]
    require(len(flattened) == len(set(flattened)) == 64, "pairing is fixed-point-free")
    require(set(flattened) == set(data["residual"]), "pairing exhausts owner complement")
    for a, b in pairs:
        require(sum_power(a, 2, domain, p) == sum_power(b, 2, domain, p), f"p2 pair {a,b}")
        require(
            quadratic_phase(a, domain, p) + quadratic_phase(b, domain, p) == 0,
            f"phase flip {a,b}",
        )

    phase_l1 = sum(abs(coefficients[k]) for k in image)
    phase_moment = sum(coefficients[k] ** 2 for k in image)
    unsigned_moment = sum(len(fibers[k]) ** 2 for k in image)
    max_fiber = max(len(fibers[k]) for k in image)
    natural_scale = (len(data["residual"]) + len(image) - 1) // len(image)

    require(phase_l1 == expected["phase_aware_l1"] == 0, "phase L1")
    require(phase_moment == expected["phase_collision_moment"] == 0, "phase moment")
    require(unsigned_moment == expected["unsigned_collision_moment"] == 576, "unsigned moment")
    require(max_fiber == expected["max_unsigned_fiber"] == 16, "max fiber")
    require(natural_scale == expected["natural_scale"] == 8, "natural scale")
    require(expected["phase_multiplier"] == 1, "phase multiplier")

    row = cert["row"]
    require(row["length"] == 2**21, "deployed length")
    require(row["agreement"] == 1116023, "deployed agreement")
    require(row["complement_weight"] == row["length"] - row["agreement"], "complement")
    require(row["fixed_outside_weight"] == row["complement_weight"] - 4, "outside weight")
    require(row["outside_available"] == row["length"] - 8, "outside available")
    require(row["fixed_outside_weight"] <= row["outside_available"], "outside embedding")
    require(natural_scale <= row["B_star"], "local scale fits deployed budget")

    if mutation_tests:
        # Restoring one C1-owned complete fiber destroys exact cancellation.
        mutated_owner = owned_masks[1:]
        mutated = realized_data(domain, p, mutated_owner)
        mutated_l1 = sum(abs(v) for v in mutated["coefficients"].values())
        require(mutated_l1 > 0, "mutation: missing owner must break cancellation")

        # Deleting one genuine residual support also destroys exact cancellation.
        mutated_owner = owned_masks + [data["residual"][0]]
        mutated = realized_data(domain, p, mutated_owner)
        mutated_l1 = sum(abs(v) for v in mutated["coefficients"].values())
        require(mutated_l1 > 0, "mutation: broken residual pair must break cancellation")

        # Perturbing one domain point must break the deployed-root provenance gate.
        bad_domain = domain.copy()
        bad_domain[0] = (bad_domain[0] + 1) % p
        require(
            chebyshev_pow_two(field["chebyshev_power"], bad_domain[0], p) != 0,
            "mutation: perturbed domain must fail root gate",
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERT)
    parser.add_argument("--no-mutations", action="store_true")
    args = parser.parse_args()

    cert = json.loads(args.certificate.read_text(encoding="utf-8"))
    verify_certificate(cert, mutation_tests=not args.no_mutations)
    print("PASS: exact RS owner-complement phase cancellation")
    print("VERDICT: PROVED_SCOPED_PHASE_PAYMENT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
