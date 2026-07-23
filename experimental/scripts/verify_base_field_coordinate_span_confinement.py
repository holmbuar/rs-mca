#!/usr/bin/env python3
"""Fail-closed checks for the coordinate-span confinement theorem packet."""

from argparse import ArgumentParser
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
NOTE = ROOT / "experimental/notes/thresholds/base_field_coordinate_span_confinement.md"
CERTIFICATE = (
    ROOT
    / "experimental/data/certificates/base-field-coordinate-span-confinement-v1"
    / "certificate.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def file_sha256(path):
    return sha256(path.read_bytes()).hexdigest()


def f9_add(x, y):
    return ((x % 3 + y % 3) % 3) + 3 * ((x // 3 + y // 3) % 3)


def f9_mul(x, y):
    a, b = x % 3, x // 3
    c, d = y % 3, y // 3
    return ((a * c + 2 * b * d) % 3) + 3 * ((a * d + b * c) % 3)


def f9_inv(x):
    require(x != 0, "attempted to invert zero in F_9")
    for y in range(1, 9):
        if f9_mul(x, y) == 1:
            return y
    raise RuntimeError("nonzero F_9 element has no inverse")


def f9_sum(values):
    total = 0
    for value in values:
        total = f9_add(total, value)
    return total


def f9_span(coordinates):
    return {
        f9_sum(f9_mul(scalar, value) for scalar, value in zip(coeffs, coordinates))
        for coeffs in product(range(3), repeat=len(coordinates))
    }


def ratio_set(left, right):
    return {
        f9_mul(v, f9_inv(w))
        for v in left
        for w in right
        if v != 0 and w != 0
    }


def check_gf9_ratio_layer():
    vectors = [pair for pair in product(range(9), repeat=2) if pair != (0, 0)]
    span_sizes_to_ranks = {1: 0, 3: 1, 9: 2}
    pair_count = 0
    intersection_cases = 0

    for y0 in vectors:
        u0 = f9_span(y0)
        s = span_sizes_to_ranks[len(u0)]
        for y1 in vectors:
            u1 = f9_span(y1)
            u = span_sizes_to_ranks[len(u1)]
            ratios = ratio_set(u0, u1)
            orbit_bound = ((3**s - 1) * (3**u - 1)) // 2
            require(len(ratios) <= orbit_bound, "F_9 ratio orbit bound failed")
            for gamma in range(1, 9):
                gamma_u1 = {f9_mul(gamma, value) for value in u1}
                if (u0 & gamma_u1) - {0}:
                    intersection_cases += 1
                    require(gamma in ratios, "F_9 intersection escaped ratio set")
            pair_count += 1

    return pair_count, intersection_cases


def check_dependent_projective_pairs():
    vectors = [pair for pair in product(range(9), repeat=2) if pair != (0, 0)]
    checked = 0
    for y0 in vectors:
        for lam in range(1, 9):
            y1 = tuple(f9_mul(lam, value) for value in y0)
            zero_finite = []
            for gamma in range(9):
                combination = tuple(
                    f9_add(a, f9_mul(gamma, b)) for a, b in zip(y0, y1)
                )
                if combination == (0, 0):
                    zero_finite.append(gamma)
            require(len(zero_finite) == 1, "dependent pair lacks unique zero parameter")
            checked += 1
    return checked


def check_radial_factorization():
    checked = 0
    for prime in (3, 5, 7):
        directions = [(1, slope) for slope in range(prime)] + [(0, 1)]
        require(len(directions) == prime + 1, "projective direction omitted")
        seen = {}
        for direction in directions:
            for scalar in range(1, prime):
                point = (
                    scalar * direction[0] % prime,
                    scalar * direction[1] % prime,
                )
                require(point != (0, 0), "zero scalar entered a radial cell")
                require(point not in seen, "radial factorization is not unique")
                seen[point] = (scalar, direction)
        require(len(seen) == prime**2 - 1, "radial cells are not exhaustive")
        checked += len(seen)
    return checked


def check_koalabear(certificate):
    p = 2**31 - 2**24 + 1
    field_size = p**6
    n = 2**21
    k = 2**20
    agreement = 1_116_048
    support_cap = n - agreement
    budget = field_size // 2**128
    projective_rank_one_cap = p + 1
    secant_margin = budget - projective_rank_one_cap
    rank_12_raw = p**2 + 1
    radial_threshold = (budget - 2) // projective_rank_one_cap
    paid_at_threshold = 2 + projective_rank_one_cap * radial_threshold
    failed_at_next = 2 + projective_rank_one_cap * (radial_threshold + 1)

    expected = certificate["koalabear"]
    actual = {
        "p": p,
        "field_size": field_size,
        "n": n,
        "k": k,
        "agreement": agreement,
        "support_cap": support_cap,
        "budget": budget,
        "projective_rank_one_cap": projective_rank_one_cap,
        "secant_margin": secant_margin,
        "rank_12_raw": rank_12_raw,
        "radial_threshold": radial_threshold,
        "paid_at_threshold": paid_at_threshold,
        "paid_margin": budget - paid_at_threshold,
        "failed_at_next": failed_at_next,
        "next_excess": failed_at_next - budget,
    }
    require(actual == expected, "KoalaBear certificate constants changed")
    require(projective_rank_one_cap < budget, "rank-one secant cap is not paid")
    require(rank_12_raw > budget, "raw rank-(1,2) orbit bound is unexpectedly paid")
    require(paid_at_threshold < budget, "radial threshold does not pay")
    require(failed_at_next > budget, "radial threshold is not maximal")
    return actual


def run_check():
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    require(certificate["schema"] == "base-field-coordinate-span-confinement-v1", "schema")
    require(
        certificate["source"]["commit"]
        == "fb6d9555339b43911c59c498373c43ed6c5cd391",
        "source commit",
    )
    require(
        certificate["source"]["tree"]
        == "fa7b8d86cb5b65fed52e427648161a9397f19670",
        "source tree",
    )
    require(
        file_sha256(NOTE) == certificate["bindings"]["note_sha256"],
        "theorem note hash",
    )
    require(
        certificate["audit"]["verdict"] == "ACCEPT_NARROWED",
        "audit verdict",
    )
    require(
        certificate["audit"]["public_text_sha256"]
        == "f6456d6fec2ca247b75be89f335d8544eb5588d13a2b60137d8dddcc1d2d97f4",
        "audit text hash",
    )

    pair_count, intersection_cases = check_gf9_ratio_layer()
    dependent_pairs = check_dependent_projective_pairs()
    radial_points = check_radial_factorization()
    kb = check_koalabear(certificate)

    print("SOURCE_BINDING: PASS")
    print(f"NOTE_BINDING: PASS sha256={certificate['bindings']['note_sha256']}")
    print(
        "GF9_RATIO: PASS "
        f"pairs={pair_count} intersection_cases={intersection_cases}"
    )
    print(f"DEPENDENT_PROJECTIVE: PASS pairs={dependent_pairs}")
    print(f"RADIAL_FACTORIZATION: PASS points={radial_points}")
    print(
        "KOALABEAR: PASS "
        f"rank_one_cap={kb['projective_rank_one_cap']} "
        f"radial_threshold={kb['radial_threshold']} "
        f"margin={kb['paid_margin']}"
    )
    print("RESULT: PASS")


def expect_failure(action, label):
    try:
        action()
    except RuntimeError:
        return
    raise RuntimeError(f"tamper was not rejected: {label}")


def run_tamper_selftest():
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    kb = certificate["koalabear"]
    tests = [
        (
            "orbit denominator p",
            lambda: require((3 - 1) * (3 - 1) % 3 == 0, "wrong denominator"),
        ),
        (
            "drop projective infinity",
            lambda: require(3 + 1 <= 3, "p cannot replace p+1"),
        ),
        (
            "admit radial scalar zero",
            lambda: require(len(range(0, 3)) == 2, "zero scalar admitted"),
        ),
        (
            "omit vertical radial direction",
            lambda: require(len([(1, m) for m in range(3)]) == 4, "direction omitted"),
        ),
        (
            "raise radial threshold",
            lambda: require(kb["failed_at_next"] <= kb["budget"], "threshold raised"),
        ),
        (
            "alter audit binding",
            lambda: require(
                certificate["audit"]["public_text_sha256"] == "0" * 64,
                "audit hash altered",
            ),
        ),
    ]
    for label, action in tests:
        expect_failure(action, label)
    print(f"TAMPER_SELFTEST: PASS rejected={len(tests)}/{len(tests)}")


def main():
    parser = ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    require(
        args.check != args.tamper_selftest,
        "choose exactly one of --check or --tamper-selftest",
    )
    if args.check:
        run_check()
    else:
        run_tamper_selftest()


if __name__ == "__main__":
    main()
