"""Certificate producer and validator for the M31 fold-primitive STAR route cut."""
from __future__ import annotations

import json
import math
from collections import Counter, defaultdict
from fractions import Fraction

from m31_fold_primitive_star_core import (
    canonical_hash,
    census_hash,
    chebyshev_twin_coset,
    cosine_lower_table,
    direct_prefix_census,
    dp_prefix_census,
    t2,
)

P, N, M, W = 127, 32, 5, 2
COS_SCALE = 10**24
PI_TERMS_5, PI_TERMS_239 = 50, 15
ALIGN_RADIUS, COSINE_ORDER = 4, 35
DEPLOYED_BSTAR, DEPLOYED_AVG_CEIL = 16_777_215, 1_993_678
K = Fraction(DEPLOYED_BSTAR, DEPLOYED_AVG_CEIL)
K_MINUS_ONE = K - 1
SOURCE_HEAD = "70954978f82e146d445731f81f6b96c19859479f"


def phase_distribution(
    fibers: Counter[tuple[int, int]], u: int, p: int
) -> list[int]:
    distribution = [0] * p
    for (z1, z2), count in fibers.items():
        distribution[(z1 + u * z2) % p] += count
    return distribution


def polygon_l1_lower(
    fibers: Counter[tuple[int, int]],
    p: int,
    cosine_lower: list[int],
) -> tuple[int, str, str]:
    """Rigorous L1 lower bound on all directions with first coordinate nonzero."""
    total_lower = 0
    alignments: list[str] = []
    orbit_lowers: list[str] = []
    for u in range(p):
        distribution = phase_distribution(fibers, u, p)
        peak = max(distribution)
        peak_mode = min(s for s, count in enumerate(distribution) if count == peak)
        orbit_lower = 0
        for scalar in range(1, p):
            center = scalar * peak_mode % p
            candidates = []
            for delta in range(-ALIGN_RADIUS, ALIGN_RADIUS + 1):
                alignment = (center + delta) % p
                lower = sum(
                    distribution[s]
                    * cosine_lower[(scalar * s - alignment) % p]
                    for s in range(p)
                )
                candidates.append((lower, -alignment, alignment))
            best_lower, _, best_alignment = max(candidates)
            certified = max(0, best_lower)
            total_lower += certified
            orbit_lower += certified
            alignments.append(str(best_alignment))
        orbit_lowers.append(str(orbit_lower))
    return (
        total_lower,
        canonical_hash(alignments),
        canonical_hash(orbit_lowers),
    )


def compute_certificate() -> dict:
    domain, lifted, generator = chebyshev_twin_coset(P, N)
    direct = direct_prefix_census(domain, P, M)
    dynamic = dp_prefix_census(domain, P, M)
    assert direct == dynamic

    total_supports = math.comb(N, M)
    histogram = Counter(direct.values())
    maximum_fiber = max(direct.values())

    t2_fibers: dict[int, list[int]] = defaultdict(list)
    for x in domain:
        t2_fibers[t2(x, P)].append(x)
    fold_iff_t1_zero = all(
        all(
            (
                all(
                    len({(t1 * x + t2c * x * x) % P for x in fiber}) == 1
                    for fiber in t2_fibers.values()
                )
                == (t1 == 0)
            )
            for t2c in range(P)
        )
        for t1 in range(P)
    )

    cos_lower, cos_width, pi_lo, pi_hi = cosine_lower_table(
        P, COS_SCALE, PI_TERMS_5, PI_TERMS_239, COSINE_ORDER
    )
    lower_num, alignment_hash, orbit_hash = polygon_l1_lower(
        direct, P, cos_lower
    )

    target_num = K_MINUS_ONE.numerator * total_supports
    target_den = K_MINUS_ONE.denominator
    cross_margin = lower_num * target_den - target_num * COS_SCALE
    atom_lhs = maximum_fiber * P**W * K.denominator
    atom_rhs = total_supports * K.numerator
    domain_set = set(domain)

    return {
        "schema": "m31-chebyshev-fold-primitive-star-counterexample-v1",
        "status": (
            "COUNTEREXAMPLE_TO_UNIFORM_CHEBYSHEV_FOLD_PRIMITIVE_STAR / "
            "AUDIT / OPEN_DEPLOYED_Q"
        ),
        "source_head": SOURCE_HEAD,
        "proof_protocol": {
            "cos_scale": COS_SCALE,
            "pi_terms_arctan_1_over_5": PI_TERMS_5,
            "pi_terms_arctan_1_over_239": PI_TERMS_239,
            "cosine_taylor_order": COSINE_ORDER,
            "alignment_radius": ALIGN_RADIUS,
            "prefix_census_methods": [
                "direct_combinations",
                "weight_indexed_dynamic_program",
            ],
        },
        "toy": {
            "p": P,
            "n": N,
            "m": M,
            "w": W,
            "total_supports": total_supports,
            "domain": domain,
            "domain_sha256": canonical_hash(str(x) for x in domain),
            "lifted_size": len(lifted),
            "circle_generator": list(generator),
            "t2_image_size": len(t2_fibers),
            "t2_fiber_sizes": sorted(len(v) for v in t2_fibers.values()),
            "fold_iff_t1_zero": fold_iff_t1_zero,
            "not_product_closed": any(
                x * y % P not in domain_set for x in domain for y in domain
            ),
        },
        "prefix_census": {
            "image_size": len(direct),
            "ambient_size": P**W,
            "full_image": len(direct) == P**W,
            "max_fiber": maximum_fiber,
            "average": {
                "num": total_supports,
                "den": P**W,
                "decimal": float(Fraction(total_supports, P**W)),
            },
            "histogram": {
                str(size): histogram[size] for size in sorted(histogram)
            },
            "histogram_sha256": canonical_hash(
                f"{size},{histogram[size]}" for size in sorted(histogram)
            ),
            "census_sha256": census_hash(direct, P),
        },
        "deployed_calibration": {
            "B_star": DEPLOYED_BSTAR,
            "avg_ceil": DEPLOYED_AVG_CEIL,
            "K": {
                "num": K.numerator,
                "den": K.denominator,
                "decimal": float(K),
            },
            "K_minus_one": {
                "num": K_MINUS_ONE.numerator,
                "den": K_MINUS_ONE.denominator,
                "decimal": float(K_MINUS_ONE),
            },
            "toy_atom_ratio": {
                "num": Fraction(maximum_fiber * P**W, total_supports).numerator,
                "den": Fraction(maximum_fiber * P**W, total_supports).denominator,
                "decimal": float(
                    Fraction(maximum_fiber * P**W, total_supports)
                ),
            },
            "atom_cross_lhs": atom_lhs,
            "atom_cross_rhs": atom_rhs,
            "atom_passes": atom_lhs <= atom_rhs,
        },
        "fold_primitive_star_counterexample": {
            "fold_primitive_direction_count": P * (P - 1),
            "fold_direction_count": P - 1,
            "cos_scale": COS_SCALE,
            "pi_interval_width": {
                "num": (pi_hi - pi_lo).numerator,
                "den": (pi_hi - pi_lo).denominator,
            },
            "maximum_cos_interval_scaled_width": cos_width,
            "certified_fold_primitive_l1_lower": {
                "num": lower_num,
                "den": COS_SCALE,
            },
            "certified_normalized_l1_lower": {
                "num": lower_num,
                "den": COS_SCALE * total_supports,
                "decimal": float(
                    Fraction(lower_num, COS_SCALE * total_supports)
                ),
            },
            "star_target": {"num": target_num, "den": target_den},
            "exact_cross_margin": cross_margin,
            "star_fails": cross_margin > 0,
            "alignment_sha256": alignment_hash,
            "orbit_lower_sha256": orbit_hash,
        },
        "nonclaims": [
            "Does not refute row-sharp Q at the deployed Mersenne-31 row.",
            (
                "Does not refute a signed-e_m theorem with a quantitative "
                "large-average, deployed-scale, or row-specific hypothesis."
            ),
            (
                "Does not prove this toy slice survives every earlier semantic "
                "first-match owner; primitive here means only non-T_2-fold."
            ),
            "Does not provide a complete first-match atlas or finite adjacent-row certificate.",
            "Does not treat three-or-more-shell residuals or balanced-core ray compilation.",
        ],
    }


def validation_results(cert: dict, fresh: dict) -> list[tuple[str, bool]]:
    keys = [
        ("schema", "schema"),
        ("status", "status"),
        ("source head", "source_head"),
        ("proof protocol", "proof_protocol"),
        ("faithful domain", "toy"),
        ("prefix census", "prefix_census"),
        ("deployed calibration", "deployed_calibration"),
        ("fold-primitive STAR certificate", "fold_primitive_star_counterexample"),
        ("nonclaims", "nonclaims"),
    ]
    return [(name, cert.get(key) == fresh[key]) for name, key in keys]


def mutate(cert: dict, path: tuple[str, ...], value) -> dict:
    clone = json.loads(json.dumps(cert))
    node = clone
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    return clone


def tamper_cases(cert: dict) -> list[dict]:
    return [
        mutate(cert, ("status",), "PROVED"),
        mutate(cert, ("proof_protocol", "alignment_radius"), 0),
        mutate(
            cert,
            ("prefix_census", "max_fiber"),
            cert["prefix_census"]["max_fiber"] + 1,
        ),
        mutate(cert, ("prefix_census", "census_sha256"), "0" * 64),
        mutate(cert, ("toy", "fold_iff_t1_zero"), False),
        mutate(cert, ("deployed_calibration", "atom_passes"), False),
        mutate(
            cert,
            (
                "fold_primitive_star_counterexample",
                "certified_fold_primitive_l1_lower",
                "num",
            ),
            0,
        ),
        mutate(
            cert,
            ("fold_primitive_star_counterexample", "alignment_sha256"),
            "f" * 64,
        ),
        mutate(
            cert,
            ("fold_primitive_star_counterexample", "star_fails"),
            False,
        ),
    ]
