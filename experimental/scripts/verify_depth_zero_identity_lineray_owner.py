#!/usr/bin/env python3
"""Verify the depth-zero identity owner for complete transverse LineRay pairs."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import math
from pathlib import Path
from typing import Any


BASE_COMMIT = "c35a6da31ed0905afcbaaefe4eb0f242572ebb35"
CLAIM_ID = "depth-zero-identity-lineray-owner-v1"
ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = (
    ROOT
    / "experimental/data/certificates/depth-zero-identity-lineray-owner"
    / "depth_zero_identity_lineray_owner.json"
)


class VerificationError(RuntimeError):
    """Raised when a mathematical or certificate gate fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def payload_digest(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def poly_mul_linear(coeffs: list[int], root: int, p: int) -> list[int]:
    """Multiply a low-to-high coefficient vector by X-root over F_p."""
    out = [0] * (len(coeffs) + 1)
    for i, value in enumerate(coeffs):
        out[i] = (out[i] - root * value) % p
        out[i + 1] = (out[i + 1] + value) % p
    return out


def locator(roots: tuple[int, ...], p: int) -> list[int]:
    coeffs = [1]
    for root in roots:
        coeffs = poly_mul_linear(coeffs, root, p)
    return coeffs


def lagrange_weights(support: tuple[int, ...], p: int) -> dict[int, int]:
    weights: dict[int, int] = {}
    for x in support:
        derivative = 1
        for y in support:
            if x != y:
                derivative = derivative * (x - y) % p
        require(derivative != 0, "distinct roots gave zero locator derivative")
        weights[x] = pow(derivative, -1, p)
    return weights


def finite_fixture(p: int, domain: tuple[int, ...], t: int, k: int) -> dict[str, Any]:
    n = len(domain)
    a = k + 1
    require(n == t + a, "fixture is not on the R=t+1 boundary")
    require(len(set(domain)) == n, "fixture domain is not distinct")
    require(all(0 <= x < p for x in domain), "fixture point is outside F_p")

    domain_set = set(domain)
    domain_sum = sum(domain) % p
    pair_signatures: set[tuple[int, tuple[int, ...]]] = set()
    slopes: set[int] = set()
    slack_slopes: set[int] = set()
    syndrome_checks = 0
    locator_checks = 0

    for support in itertools.combinations(domain, t):
        weights = lagrange_weights(support, p)
        moments = [
            sum(weights[x] * pow(x, degree, p) for x in support) % p
            for degree in range(t + 1)
        ]
        expected = [0] * (t - 1) + [1, sum(support) % p]
        require(moments == expected, f"Lagrange syndrome mismatch: {support}")
        syndrome_checks += 1

        agreement = tuple(x for x in domain if x not in set(support))
        require(len(agreement) == a, "complement agreement has wrong size")
        require(set(agreement) | set(support) == domain_set, "bad complement union")
        require(set(agreement).isdisjoint(support), "bad complement intersection")

        gamma = sum(support) % p
        z = -sum(agreement) % p
        require(gamma == (domain_sum + z) % p, "slack-one affine dictionary failed")

        q_agreement = locator(agreement, p)
        require(len(q_agreement) == a + 1, "locator degree mismatch")
        require(q_agreement[a] == 1, "locator is not monic")
        require(q_agreement[k] == z, "slack-one X^k coefficient mismatch")
        u = [0] * (a + 1)
        u[k] = z
        u[a] = 1
        residual = [(u[i] - q_agreement[i]) % p for i in range(a + 1)]
        require(all(residual[i] == 0 for i in range(k, a + 1)), "residual degree is not <k")
        locator_checks += 1

        signature = (gamma, support)
        require(signature not in pair_signatures, "duplicate canonical pair")
        pair_signatures.add(signature)
        slopes.add(gamma)
        slack_slopes.add(z)

    pair_count = math.comb(n, t)
    identity_scale = math.comb(n, a)
    require(len(pair_signatures) == pair_count, "canonical pair count mismatch")
    require(pair_count == identity_scale, "complement binomial identity failed")
    require({(domain_sum + z) % p for z in slack_slopes} == slopes, "slope images are not translates")

    return {
        "p": p,
        "domain": list(domain),
        "t": t,
        "k": k,
        "n": n,
        "agreement": a,
        "identity_depth": 0,
        "pair_count": pair_count,
        "identity_scale": identity_scale,
        "slope_count": len(slopes),
        "slack_slope_count": len(slack_slopes),
        "syndrome_checks": syndrome_checks,
        "locator_checks": locator_checks,
    }


def build_payload() -> dict[str, Any]:
    arithmetic_rows = 0
    for t in range(1, 33):
        for k in range(1, 33):
            n = t + k + 1
            a = k + 1
            require(n - t == a, "agreement arithmetic failed")
            require(a - k - 1 == 0, "identity depth is not zero")
            require(math.comb(n, t) == math.comb(n, a), "binomial symmetry failed")
            require(n - k == t + 1, "redundancy is not t+1")
            arithmetic_rows += 1

    double_negative_rows = []
    for t in range(2, 41, 2):
        k = t
        n = 2 * t + 1
        d = t + 1
        m = k
        delta = 1
        j = t // 2
        height = max(1, d + j - t)
        xi = d * (m - j) ** 2 + m * height**2 - d * m**2
        separation = min(m, max(delta, d + 2 * j - 2 * t))
        q_den = m * separation - 2 * m * j + j**2
        require(xi < 0, "central Xi route-cut row is not negative")
        require(q_den < 0, "central Q route-cut row is not negative")
        require(math.comb(n, t) == math.comb(n, k + 1), "route-cut scale mismatch")
        double_negative_rows.append(
            {"t": t, "n": n, "j": j, "xi": xi, "q_denominator": q_den}
        )

    fixture_specs = [
        (5, (0, 1, 2, 3, 4), 2, 2),
        (7, (0, 1, 2, 3, 4, 5), 2, 3),
        (7, (0, 1, 2, 3, 4, 5, 6), 3, 3),
        (11, (0, 1, 2, 3, 4, 5, 6, 7), 3, 4),
        (11, (0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 4, 5),
        (13, (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), 5, 6),
    ]
    fixtures = [finite_fixture(*spec) for spec in fixture_specs]

    return {
        "schema_version": 1,
        "claim_id": CLAIM_ID,
        "base_commit": BASE_COMMIT,
        "status": "PROVED_AUDIT_WITH_UNPROVED_LEAN_TARGET",
        "hard_input": "3_residual_ray_compiler_depth_zero_identity_boundary",
        "arithmetic_grid": {
            "t_range": [1, 32],
            "k_range": [1, 32],
            "rows": arithmetic_rows,
        },
        "central_double_negative": {
            "even_t_range": [2, 40],
            "rows": double_negative_rows,
        },
        "finite_prime_fixtures": fixtures,
        "totals": {
            "fixtures": len(fixtures),
            "canonical_pairs": sum(row["pair_count"] for row in fixtures),
            "syndrome_checks": sum(row["syndrome_checks"] for row in fixtures),
            "locator_checks": sum(row["locator_checks"] for row in fixtures),
        },
        "nonclaims": [
            "no_positive_depth_payment",
            "no_atlas_exhaustivity",
            "no_deployed_row_movement",
            "lean_target_unproved",
        ],
    }


def build_certificate() -> dict[str, Any]:
    payload = build_payload()
    return {**payload, "payload_sha256": payload_digest(payload)}


def validate_exact(actual: dict[str, Any], expected: dict[str, Any]) -> None:
    if actual != expected:
        raise VerificationError("certificate differs from exact recomputation")
    digest = actual.get("payload_sha256")
    payload = {key: value for key, value in actual.items() if key != "payload_sha256"}
    require(digest == payload_digest(payload), "certificate payload digest mismatch")


def check_certificate() -> dict[str, Any]:
    require(CERTIFICATE.is_file(), f"missing certificate: {CERTIFICATE}")
    with CERTIFICATE.open("r", encoding="utf-8") as handle:
        actual = json.load(handle)
    expected = build_certificate()
    validate_exact(actual, expected)
    return expected


def tamper_selftest() -> int:
    expected = build_certificate()
    tampers = []

    bad = copy.deepcopy(expected)
    bad["base_commit"] = "0" * 40
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["arithmetic_grid"]["rows"] += 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["finite_prime_fixtures"][0]["pair_count"] -= 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["payload_sha256"] = "f" * 64
    tampers.append(bad)

    rejected = 0
    for tampered in tampers:
        try:
            validate_exact(tampered, expected)
        except VerificationError:
            rejected += 1
    require(rejected == len(tampers), "a pinned tamper was not rejected")
    return rejected


def summary(certificate: dict[str, Any]) -> str:
    totals = certificate["totals"]
    return (
        "DEPTH_ZERO_IDENTITY_LINERAY_OWNER_PASS "
        f"arithmetic={certificate['arithmetic_grid']['rows']} "
        f"double_negative={len(certificate['central_double_negative']['rows'])} "
        f"fixtures={totals['fixtures']} pairs={totals['canonical_pairs']} "
        f"syndrome={totals['syndrome_checks']} locator={totals['locator_checks']}"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true")
    group.add_argument("--tamper-selftest", action="store_true")
    group.add_argument("--print-certificate", action="store_true")
    args = parser.parse_args()

    if args.tamper_selftest:
        rejected = tamper_selftest()
        print(f"DEPTH_ZERO_IDENTITY_LINERAY_OWNER_TAMPER_PASS rejected={rejected}/{rejected}")
        return 0

    if args.print_certificate:
        print(json.dumps(build_certificate(), indent=2, sort_keys=True))
        return 0

    certificate = check_certificate()
    print(summary(certificate))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
