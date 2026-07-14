#!/usr/bin/env python3
"""Verify the canonical-Lagrange rational-curve LineRay compiler."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
from pathlib import Path
from typing import Any, Iterable


BASE_COMMIT = "c35a6da31ed0905afcbaaefe4eb0f242572ebb35"
CLAIM_ID = "canonical-lagrange-curve-compiler-v1"
ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = (
    ROOT
    / "experimental/data/certificates/canonical-lagrange-curve-compiler"
    / "canonical_lagrange_curve_compiler.json"
)


class VerificationError(RuntimeError):
    """Raised when a theorem or certificate gate fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def payload_digest(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def trim(poly: list[int], p: int) -> list[int]:
    out = [value % p for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_add(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] = (out[index] + value) % p
    for index, value in enumerate(right):
        out[index] = (out[index] + value) % p
    return trim(out, p)


def poly_scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return trim([(scalar * value) % p for value in poly], p)


def poly_mul(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] = (out[i + j] + left_value * right_value) % p
    return trim(out, p)


def poly_eval(poly: list[int], value: int, p: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % p
    return result


def poly_degree(poly: list[int], p: int) -> int:
    return len(trim(poly, p)) - 1


def complete_to_elementary(
    complete: list[list[int]], p: int
) -> list[list[int]]:
    """Division-free E(-u)H(u)=1 recurrence."""
    elementary: list[list[int]] = [[1]]
    for degree in range(1, len(complete)):
        current = [0]
        for index in range(1, degree + 1):
            term = poly_mul(elementary[degree - index], complete[index], p)
            sign = 1 if index % 2 == 1 else -1
            current = poly_add(current, poly_scale(term, sign, p), p)
        elementary.append(current)
    return elementary


def locator_from_affine_complete(
    constants: tuple[int, ...], directions: tuple[int, ...], p: int
) -> tuple[list[list[int]], list[list[int]], list[list[int]]]:
    require(len(constants) == len(directions), "affine moment length mismatch")
    t = len(constants)
    complete = [[1]] + [
        trim([constants[index], directions[index]], p) for index in range(t)
    ]
    elementary = complete_to_elementary(complete, p)
    locator = [[0] for _ in range(t + 1)]
    locator[t] = [1]
    for degree in range(1, t + 1):
        locator[t - degree] = poly_scale(
            elementary[degree], -1 if degree % 2 else 1, p
        )
        require(
            poly_degree(elementary[degree], p) <= degree,
            "full locator coefficient exceeded its triangular degree",
        )
    return complete, elementary, locator


def locator_at_parameter(
    locator: list[list[int]], gamma: int, p: int
) -> list[int]:
    return [poly_eval(coefficient, gamma, p) for coefficient in locator]


def locator_value_polynomial(
    locator: list[list[int]], x: int, p: int
) -> list[int]:
    out = [0]
    power = 1
    for coefficient in locator:
        out = poly_add(out, poly_scale(coefficient, power, p), p)
        power = power * x % p
    return trim(out, p)


def divide_locator_by_root(
    locator: list[list[int]], root: int, p: int
) -> list[list[int]]:
    degree = len(locator) - 1
    require(degree >= 1, "cannot divide a constant locator")
    quotient = [[0] for _ in range(degree)]
    quotient[degree - 1] = locator[degree]
    for index in range(degree - 1, 0, -1):
        quotient[index - 1] = poly_add(
            locator[index], poly_scale(quotient[index], root, p), p
        )
    remainder = poly_add(
        locator[0], poly_scale(quotient[0], root, p), p
    )
    require(remainder == [0], "claimed fixed root left a remainder")
    return quotient


def elementary_from_locator(
    locator: list[list[int]], p: int
) -> list[list[int]]:
    degree = len(locator) - 1
    require(locator[-1] == [1], "locator is not monic")
    elementary = [[1]]
    for index in range(1, degree + 1):
        coefficient = locator[degree - index]
        elementary.append(
            poly_scale(coefficient, -1 if index % 2 else 1, p)
        )
    return elementary


def elementary_to_complete(
    elementary: list[list[int]], count: int, p: int
) -> list[list[int]]:
    complete: list[list[int]] = [[1]]
    degree = len(elementary) - 1
    for index in range(1, count + 1):
        current = [0]
        for j in range(1, min(index, degree) + 1):
            term = poly_mul(elementary[j], complete[index - j], p)
            sign = 1 if j % 2 == 1 else -1
            current = poly_add(current, poly_scale(term, sign, p), p)
        complete.append(current)
    return complete


def constant_locator(roots: Iterable[int], p: int) -> list[int]:
    locator = [1]
    for root in roots:
        out = [0] * (len(locator) + 1)
        for index, value in enumerate(locator):
            out[index] = (out[index] - root * value) % p
            out[index + 1] = (out[index + 1] + value) % p
        locator = out
    return locator


def constant_elementary(roots: tuple[int, ...], p: int) -> list[int]:
    locator = constant_locator(roots, p)
    degree = len(roots)
    return [
        ((-1 if index % 2 else 1) * locator[degree - index]) % p
        for index in range(degree + 1)
    ]


def lagrange_weights(support: tuple[int, ...], p: int) -> dict[int, int]:
    weights: dict[int, int] = {}
    for x in support:
        derivative = 1
        for y in support:
            if x != y:
                derivative = derivative * (x - y) % p
        require(derivative != 0, "distinct roots gave zero derivative")
        weights[x] = pow(derivative, -1, p)
    return weights


def moments(
    support: tuple[int, ...], weights: dict[int, int], count: int, p: int
) -> tuple[int, ...]:
    return tuple(
        sum(weights[x] * pow(x, degree, p) for x in support) % p
        for degree in range(count)
    )


def audit_affine_family(
    p: int,
    t: int,
    domain: tuple[int, ...],
    constants: tuple[int, ...],
    directions: tuple[int, ...],
) -> dict[str, int]:
    require(t >= 1, "t must be positive")
    require(len(domain) >= 2 * t, "domain is shorter than the 2t chart")
    require(any(directions), "this routine audits a nonconstant line")
    complete, _, locator = locator_from_affine_complete(
        constants, directions, p
    )

    fixed_roots = tuple(
        x for x in domain if locator_value_polynomial(locator, x, p) == [0]
    )
    residual = locator
    for root in fixed_roots:
        residual = divide_locator_by_root(residual, root, p)
    g = len(fixed_roots)
    moving_degree = t - g
    require(moving_degree > 0, "nonconstant line has constant locator")
    require(len(residual) == moving_degree + 1, "residual degree mismatch")

    residual_elementary = elementary_from_locator(residual, p)
    residual_complete = elementary_to_complete(
        residual_elementary, moving_degree, p
    )
    fixed_elementary = constant_elementary(fixed_roots, p)

    for degree in range(1, moving_degree + 1):
        expected = [0]
        for j in range(0, min(g, degree) + 1):
            term = poly_scale(
                complete[degree - j],
                ((-1 if j % 2 else 1) * fixed_elementary[j]) % p,
                p,
            )
            expected = poly_add(expected, term, p)
        require(
            residual_complete[degree] == expected,
            "fixed-factor complete-homogeneous division failed",
        )
        require(
            poly_degree(residual_complete[degree], p) <= 1,
            "residual complete moment is not affine",
        )
        require(
            poly_degree(residual_elementary[degree], p) <= degree,
            "residual locator coefficient exceeds moving degree",
        )

    selected: list[tuple[int, tuple[int, ...]]] = []
    for gamma in range(p):
        specialized = locator_at_parameter(locator, gamma, p)
        roots = tuple(x for x in domain if poly_eval(specialized, x, p) == 0)
        if len(roots) == t:
            require(
                constant_locator(roots, p) == specialized,
                "t roots did not reconstruct the specialized locator",
            )
            selected.append((gamma, roots))

    root_cap_sum = 0
    moving_incidences = 0
    fixed_set = set(fixed_roots)
    for x in domain:
        if x in fixed_set:
            continue
        value_poly = locator_value_polynomial(residual, x, p)
        require(value_poly != [0], "nonfixed residual evaluation vanished")
        degree = poly_degree(value_poly, p)
        require(degree <= moving_degree, "root divisor degree exceeded h")
        hits = sum(
            poly_eval(value_poly, gamma, p) == 0 for gamma in range(p)
        )
        require(hits <= degree, "polynomial has more roots than its degree")
        root_cap_sum += moving_degree
        moving_incidences += sum(x in roots for _, roots in selected)

    require(
        moving_incidences == len(selected) * moving_degree,
        "selected locator has the wrong moving-root count",
    )
    require(
        moving_incidences <= root_cap_sum,
        "moving-root double count exceeded capacity",
    )
    require(
        len(selected) <= len(domain) - g,
        "canonical-Lagrange N-g bound failed",
    )

    for gamma, support in selected:
        weights = lagrange_weights(support, p)
        row = moments(support, weights, 2 * t, p)
        expected = (0,) * (t - 1) + (1,) + tuple(
            (constants[index] + gamma * directions[index]) % p
            for index in range(t)
        )
        require(row == expected, "selected locator failed the moment line")

    return {
        "selected": len(selected),
        "fixed_roots": g,
        "moving_degree": moving_degree,
        "root_capacity": root_cap_sum,
        "moving_incidences": moving_incidences,
        "parameter_checks": p,
        "coordinate_checks": len(domain) - g,
    }


def exhaustive_affine_grid(p: int, t: int) -> dict[str, Any]:
    domain = tuple(range(p))
    require(len(domain) >= 2 * t, "exhaustive grid has too few points")
    families = 0
    selected_total = 0
    parameter_checks = 0
    coordinate_checks = 0
    fixed_root_families = 0
    maximum_fixed_roots = 0
    maximum_selected = 0
    minimum_margin = len(domain)

    for values in itertools.product(range(p), repeat=2 * t):
        constants = tuple(values[:t])
        directions = tuple(values[t:])
        if not any(directions):
            continue
        result = audit_affine_family(
            p, t, domain, constants, directions
        )
        families += 1
        selected_total += result["selected"]
        parameter_checks += result["parameter_checks"]
        coordinate_checks += result["coordinate_checks"]
        maximum_selected = max(maximum_selected, result["selected"])
        maximum_fixed_roots = max(
            maximum_fixed_roots, result["fixed_roots"]
        )
        if result["fixed_roots"]:
            fixed_root_families += 1
        minimum_margin = min(
            minimum_margin,
            len(domain) - result["fixed_roots"] - result["selected"],
        )

    expected_families = p ** (2 * t) - p**t
    require(families == expected_families, "affine family census mismatch")
    require(minimum_margin >= 0, "negative theorem margin")
    return {
        "p": p,
        "t": t,
        "domain_size": len(domain),
        "families": families,
        "parameter_checks": parameter_checks,
        "coordinate_checks": coordinate_checks,
        "selected_total": selected_total,
        "maximum_selected": maximum_selected,
        "fixed_root_families": fixed_root_families,
        "maximum_fixed_roots": maximum_fixed_roots,
        "minimum_bound_margin": minimum_margin,
    }


def cyclotomic_fixture(p: int, t: int) -> dict[str, Any]:
    domain = tuple(range(1, p))
    require((p - 1) % (t + 1) == 0, "missing cyclotomic subgroup")
    require(len(domain) >= 2 * t, "cyclotomic domain is too short")
    constants = (0,) * t
    directions = (1,) + (0,) * (t - 1)
    result = audit_affine_family(
        p, t, domain, constants, directions
    )
    require(result["fixed_roots"] == 0, "cyclotomic curve gained a fixed root")
    require(
        result["selected"] == len(domain),
        "cyclotomic curve did not attain N",
    )
    require(
        result["moving_incidences"] == len(domain) * t,
        "cyclotomic incidence count is not sharp",
    )
    return {
        "p": p,
        "t": t,
        "domain_size": len(domain),
        "selected": result["selected"],
        "fixed_roots": result["fixed_roots"],
        "moving_degree": result["moving_degree"],
        "root_capacity": result["root_capacity"],
        "moving_incidences": result["moving_incidences"],
        "bound_attained": result["selected"] == len(domain),
    }


def fixed_root_fixture() -> dict[str, Any]:
    p = 7
    t = 3
    domain = tuple(range(p))
    # Q_z=X(X^2-X+1-A-z), with A=0.  Thus zero is a formal fixed root,
    # while h_1=1, h_2=z, h_3=2z-1 are affine.
    constants = (1, 0, -1 % p)
    directions = (0, 1, 2)
    result = audit_affine_family(
        p, t, domain, constants, directions
    )
    require(result["fixed_roots"] == 1, "fixed-root fixture lost its root")
    require(result["moving_degree"] == 2, "fixed-root residual degree changed")
    require(result["selected"] > 0, "fixed-root fixture became vacuous")
    return {
        "p": p,
        "t": t,
        "domain_size": len(domain),
        "constants": list(constants),
        "directions": list(directions),
        **result,
        "bound": len(domain) - result["fixed_roots"],
    }


def constant_locator_fixture() -> dict[str, Any]:
    p = 7
    t = 2
    domain = tuple(range(p))
    support = (0, 1)
    weights = lagrange_weights(support, p)
    base = moments(support, weights, 2 * t + 1, p)
    pairs = []
    expected_prefix = (0,) * (t - 1) + (1,)
    for gamma in range(p):
        target = base[: 2 * t] + ((base[2 * t] + gamma) % p,)
        for candidate in itertools.combinations(domain, t):
            candidate_weights = lagrange_weights(candidate, p)
            row = moments(candidate, candidate_weights, 2 * t + 1, p)
            if row[:t] == expected_prefix and row == target:
                pairs.append((gamma, candidate))
    require(pairs == [(0, support)], "constant-locator branch is not singleton")
    return {
        "p": p,
        "t": t,
        "domain_size": len(domain),
        "redundancy": 2 * t + 1,
        "formal_fixed_roots": t,
        "pair_count": len(pairs),
        "bound": len(domain) - t,
        "support_checks": p * 21,
    }


def build_payload() -> dict[str, Any]:
    exhaustive_specs = [(2, 1), (3, 1), (5, 2), (7, 2), (7, 3)]
    exhaustive = [
        exhaustive_affine_grid(p, t) for p, t in exhaustive_specs
    ]
    cyclotomic_specs = [(7, 2), (13, 2), (13, 3), (17, 3), (31, 4)]
    cyclotomic = [
        cyclotomic_fixture(p, t) for p, t in cyclotomic_specs
    ]
    fixed = fixed_root_fixture()
    constant = constant_locator_fixture()
    return {
        "schema_version": 1,
        "claim_id": CLAIM_ID,
        "base_commit": BASE_COMMIT,
        "status": "PROVED_AUDIT_WITH_UNPROVED_LEAN_TARGET",
        "hard_input": "3_canonical_lagrange_rational_curve_compiler",
        "theorem": {
            "dimension_range": "N>=R>=2t",
            "all_pair_bound": "|P|=|Z|<=N-g<=N",
            "residual_curve_degree": "delta<=t-g",
            "assumptions_not_used": ["transversality", "selector", "field_size"],
        },
        "exhaustive_affine_grids": exhaustive,
        "fixed_root_fixture": fixed,
        "constant_locator_fixture": constant,
        "cyclotomic_sharpness_fixtures": cyclotomic,
        "totals": {
            "exhaustive_families": sum(row["families"] for row in exhaustive),
            "parameter_checks": sum(
                row["parameter_checks"] for row in exhaustive
            ),
            "coordinate_checks": sum(
                row["coordinate_checks"] for row in exhaustive
            ),
            "selected_locators": sum(
                row["selected_total"] for row in exhaustive
            ),
            "fixed_root_families": sum(
                row["fixed_root_families"] for row in exhaustive
            ),
            "sharp_fixtures": sum(row["bound_attained"] for row in cyclotomic),
            "sharp_pairs": sum(row["selected"] for row in cyclotomic),
        },
        "nonclaims": [
            "no_arbitrary_syndrome_line_bound",
            "no_first_match_atlas_exhaustivity",
            "no_primitive_profile_survival",
            "no_deployed_threshold_movement",
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
    require(digest == payload_digest(payload), "certificate digest mismatch")


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
    bad["theorem"]["all_pair_bound"] = "|P|<=N+1"
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["fixed_root_fixture"]["fixed_roots"] = 0
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["cyclotomic_sharpness_fixtures"][0]["selected"] -= 1
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
        "CANONICAL_LAGRANGE_CURVE_COMPILER_PASS "
        f"families={totals['exhaustive_families']} "
        f"parameters={totals['parameter_checks']} "
        f"coordinates={totals['coordinate_checks']} "
        f"selected={totals['selected_locators']} "
        f"fixed={totals['fixed_root_families']} "
        f"sharp={totals['sharp_fixtures']}"
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
            "CANONICAL_LAGRANGE_CURVE_COMPILER_TAMPER_PASS "
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
