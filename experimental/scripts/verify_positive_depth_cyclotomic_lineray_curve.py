#!/usr/bin/env python3
"""Verify the positive-depth cyclotomic LineRay curve and sharp RC payment."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


BASE_COMMIT = "c35a6da31ed0905afcbaaefe4eb0f242572ebb35"
CLAIM_ID = "positive-depth-cyclotomic-lineray-curve-v1"
ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = (
    ROOT
    / "experimental/data/certificates/positive-depth-cyclotomic-lineray-curve"
    / "positive_depth_cyclotomic_lineray_curve.json"
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


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def poly_mul_linear(coeffs: list[int], root: int, p: int) -> list[int]:
    """Multiply low-to-high coefficients by X-root over F_p."""
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


def moments(
    support: tuple[int, ...], weights: dict[int, int], p: int, count: int
) -> tuple[int, ...]:
    return tuple(
        sum(weights[x] * pow(x, degree, p) for x in support) % p
        for degree in range(count)
    )


def word_weight(word: tuple[int, ...]) -> int:
    return sum(value != 0 for value in word)


def exhaustive_t_supports(
    p: int, domain: tuple[int, ...], t: int
) -> dict[str, int]:
    expected_prefix = (0,) * (t - 1) + (1,)
    matches = []
    examined = 0
    for support in itertools.combinations(domain, t):
        weights = lagrange_weights(support, p)
        row = moments(support, weights, p, 2 * t)
        examined += 1
        if row[:t] == expected_prefix and row[t + 1 :] == (0,) * (t - 1):
            matches.append((support, row[t]))

    require(len(matches) == len(domain), "exhaustive complete-family count failed")
    require(
        len({support for support, _ in matches}) == len(domain),
        "support collision",
    )
    require(
        {gamma for _, gamma in matches} == set(domain),
        "slope image is not F_p^*",
    )
    return {"supports_examined": examined, "matches": len(matches)}


def finite_fixture(p: int, t: int, exhaustive: bool) -> dict[str, Any]:
    require(is_prime(p), "fixture modulus is not prime")
    require(t >= 2, "fixture depth is not positive")
    require((p - 1) % (t + 1) == 0, "missing (t+1)-st roots of unity")

    domain = tuple(range(1, p))
    domain_set = set(domain)
    n = len(domain)
    require(n >= 2 * t + 2, "kernel dimension is below two")
    kappa = n - 2 * t
    agreement = n - t
    depth = t - 1
    d = t + 1
    outside_length = n - d
    punctured_distance = t

    mu = tuple(x for x in domain if pow(x, t + 1, p) == 1)
    require(len(mu) == t + 1, "root subgroup has wrong size")
    mu_set = set(mu)

    lift_weights = lagrange_weights(mu, p)
    lift_moments = moments(mu, lift_weights, p, 2 * t)
    expected_lift = (0,) * t + (1,) + (0,) * (t - 1)
    require(lift_moments == expected_lift, "minimum-lift syndrome mismatch")

    family: dict[int, tuple[tuple[int, ...], dict[int, int]]] = {}
    prefixes: dict[tuple[int, ...], list[int]] = defaultdict(list)
    root_degrees = {x: 0 for x in domain}
    pair_signatures: set[tuple[int, tuple[int, ...]]] = set()
    stratum_counts: dict[int, int] = defaultdict(int)
    realized_clusters: dict[tuple[int, ...], list[int]] = defaultdict(list)
    syndrome_checks = 0
    profile_checks = 0

    for gamma in domain:
        support = tuple(
            sorted({(-gamma * z) % p for z in mu if z != 1})
        )
        require(len(support) == t, "cyclotomic support has wrong size")
        require(set(support) <= domain_set, "support left F_p^*")

        weights = lagrange_weights(support, p)
        row = moments(support, weights, p, 2 * t)
        expected = (0,) * (t - 1) + (1, gamma) + (0,) * (t - 1)
        require(row == expected, "cyclotomic LineRay syndrome mismatch")
        syndrome_checks += 1

        coefficients = locator(support, p)
        expected_coefficients = [
            pow(-gamma, t - degree, p) for degree in range(t + 1)
        ]
        require(
            coefficients == expected_coefficients,
            "locator formula mismatch",
        )

        support_set = set(support)
        agreement_support = tuple(x for x in domain if x not in support_set)
        require(len(agreement_support) == agreement, "agreement size mismatch")
        agreement_locator = locator(agreement_support, p)
        prefix = tuple(
            agreement_locator[agreement - index] for index in range(1, t)
        )
        require(
            prefix == (gamma,) + (0,) * (t - 2),
            "complement prefix mismatch",
        )
        prefixes[prefix].append(gamma)
        profile_checks += 1

        signature = (gamma, support)
        require(signature not in pair_signatures, "duplicate pair signature")
        pair_signatures.add(signature)
        family[gamma] = (support, weights)

        for x in support:
            root_degrees[x] += 1

        j = len(support_set - mu_set)
        stratum_counts[j] += 1

        base_word = []
        for x in domain:
            value = (
                weights.get(x, 0) - gamma * lift_weights.get(x, 0)
            ) % p
            base_word.append(0 if x in mu_set else value)
        realized_clusters[tuple(base_word)].append(gamma)

    require(
        len(family) == n,
        "family does not have one pair per nonzero slope",
    )
    require(len(pair_signatures) == n, "pair count mismatch")
    require(len(prefixes) == n, "realized prefix image mismatch")
    require(
        all(len(fiber) == 1 for fiber in prefixes.values()),
        "prefix is not flat",
    )
    require(
        all(degree == t for degree in root_degrees.values()),
        "curve root degree mismatch",
    )
    require(
        sum(root_degrees.values()) == n * t,
        "root incidence total mismatch",
    )

    cluster_sizes = sorted(
        (len(cluster) for cluster in realized_clusters.values()),
        reverse=True,
    )
    require(
        cluster_sizes == [t + 1] + [1] * (n - t - 1),
        "realized puncture cluster distribution mismatch",
    )
    require(len(realized_clusters) == n - t, "realized word count mismatch")

    weighted_budget = 0
    for word, cluster in realized_clusters.items():
        height = max(1, d + word_weight(word) - t)
        cap = d // height
        require(len(cluster) <= cap, "cluster exceeds exact weighted cap")
        weighted_budget += cap
    require(weighted_budget == n, "weighted puncture budget is not sharp")

    require(
        dict(stratum_counts) == {0: t + 1, t: n - t - 1},
        "exact strata changed",
    )

    exact_separation = min(
        outside_length,
        max(punctured_distance, d + 2 * t - 2 * t),
    )
    q_denominator = (
        outside_length * exact_separation
        - 2 * outside_length * t
        + t * t
    )
    xi = (
        d * (outside_length - t) ** 2
        + outside_length * d**2
        - d * outside_length**2
    )
    require(exact_separation == d, "exact separation is not d")
    require(
        q_denominator == t * t - (t - 1) * outside_length,
        "Q formula failed",
    )
    require(xi == d * q_denominator, "Xi/Q factorization failed")

    high_denominator = (n - t) ** 2 - n * (n - d)
    low_denominator = (
        (outside_length - t) ** 2
        - outside_length * (outside_length - punctured_distance)
    )

    exhaustive_result = (
        exhaustive_t_supports(p, domain, t)
        if exhaustive
        else {"supports_examined": 0, "matches": 0}
    )

    return {
        "p": p,
        "t": t,
        "n": n,
        "redundancy": 2 * t,
        "kernel_dimension": kappa,
        "agreement": agreement,
        "identity_depth": depth,
        "root_subgroup": list(mu),
        "pair_count": n,
        "slope_count": n,
        "profile_mass": n,
        "profile_image": n,
        "profile_max_fiber": 1,
        "profile_scale": 1,
        "ray_to_profile_ratio": n,
        "minimum_lift_weight": d,
        "realized_words": len(realized_clusters),
        "cluster_sizes": cluster_sizes,
        "weighted_puncture_budget": weighted_budget,
        "strata": {"j0": t + 1, "jt": n - t - 1},
        "curve_degree": t,
        "moving_roots": t,
        "curve_bound": n,
        "root_incidences": n * t,
        "high_denominator": high_denominator,
        "low_denominator": low_denominator,
        "exact_q_denominator_jt": q_denominator,
        "exact_xi_jt": xi,
        "exact_jt_double_negative": q_denominator < 0 and xi < 0,
        "syndrome_checks": syndrome_checks,
        "profile_checks": profile_checks,
        "exhaustive": exhaustive_result,
    }


def arithmetic_grid() -> dict[str, Any]:
    rows = 0
    double_negative = 0
    minimum_q = None
    maximum_q = None
    for t in range(2, 33):
        for multiplier in range(3, 21):
            n = multiplier * (t + 1)
            kappa = n - 2 * t
            agreement = n - t
            depth = agreement - kappa - 1
            d = t + 1
            outside_length = n - d
            q_denominator = t * t - (t - 1) * outside_length
            xi = d * q_denominator

            require(kappa >= 2, "grid kernel dimension fell below two")
            require(depth == t - 1, "grid identity depth mismatch")
            require(
                outside_length >= d,
                "grid puncture blocks are malformed",
            )
            require(
                q_denominator < 0 and xi < 0,
                "grid residual is not double-negative",
            )
            require(n % (t + 1) == 0, "grid cyclotomic divisibility failed")

            rows += 1
            double_negative += 1
            minimum_q = (
                q_denominator
                if minimum_q is None
                else min(minimum_q, q_denominator)
            )
            maximum_q = (
                q_denominator
                if maximum_q is None
                else max(maximum_q, q_denominator)
            )

    return {
        "t_range": [2, 32],
        "multiplier_range": [3, 20],
        "rows": rows,
        "double_negative_rows": double_negative,
        "minimum_q_denominator": minimum_q,
        "maximum_q_denominator": maximum_q,
    }


def build_payload() -> dict[str, Any]:
    fixture_specs = [
        (7, 2, True),
        (13, 2, True),
        (13, 3, True),
        (17, 3, True),
        (31, 5, False),
        (41, 4, False),
        (43, 6, False),
    ]
    fixtures = [finite_fixture(*spec) for spec in fixture_specs]
    exhaustive_rows = [
        row for row in fixtures if row["exhaustive"]["supports_examined"]
    ]

    return {
        "schema_version": 1,
        "claim_id": CLAIM_ID,
        "base_commit": BASE_COMMIT,
        "status": "PROVED_COUNTEREXAMPLE_AUDIT_WITH_UNPROVED_LEAN_TARGET",
        "hard_input": "3_positive_depth_rational_normal_curve_ray_compiler",
        "symbolic_grid": arithmetic_grid(),
        "finite_prime_fixtures": fixtures,
        "totals": {
            "fixtures": len(fixtures),
            "constructed_pairs": sum(
                row["pair_count"] for row in fixtures
            ),
            "syndrome_checks": sum(
                row["syndrome_checks"] for row in fixtures
            ),
            "profile_checks": sum(
                row["profile_checks"] for row in fixtures
            ),
            "exhaustive_supports": sum(
                row["exhaustive"]["supports_examined"]
                for row in exhaustive_rows
            ),
            "exhaustive_matches": sum(
                row["exhaustive"]["matches"] for row in exhaustive_rows
            ),
            "double_negative_fixtures": sum(
                row["exact_jt_double_negative"] for row in fixtures
            ),
        },
        "nonclaims": [
            "no_primitive_first_match_survival",
            "no_atlas_exhaustivity",
            "no_higher_dimensional_balanced_core_payment",
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
    payload = {
        key: value for key, value in actual.items() if key != "payload_sha256"
    }
    require(
        digest == payload_digest(payload),
        "certificate payload digest mismatch",
    )


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
    bad["symbolic_grid"]["rows"] += 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["finite_prime_fixtures"][1]["profile_scale"] += 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["finite_prime_fixtures"][2]["cluster_sizes"][0] -= 1
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
        "POSITIVE_DEPTH_CYCLOTOMIC_LINERAY_CURVE_PASS "
        f"grid={certificate['symbolic_grid']['rows']} "
        f"fixtures={totals['fixtures']} "
        f"pairs={totals['constructed_pairs']} "
        f"syndrome={totals['syndrome_checks']} "
        f"profile={totals['profile_checks']} "
        f"exhaustive={totals['exhaustive_supports']} "
        f"double_negative={totals['double_negative_fixtures']}"
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
        print(
            "POSITIVE_DEPTH_CYCLOTOMIC_LINERAY_CURVE_TAMPER_PASS "
            f"rejected={rejected}/{rejected}"
        )
        return 0

    if args.print_certificate:
        print(json.dumps(build_certificate(), indent=2, sort_keys=True))
        return 0

    certificate = check_certificate()
    print(summary(certificate))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
