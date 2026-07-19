#!/usr/bin/env python3
"""Exact marked-incidence audit for the primitive top seam ``e = w + 1``.

The executable scope is deliberately fail-closed.  It verifies the marked
normal form and finite projection regressions, but it never promotes a raw
support-side triple to an actual primitive first-match survivor without a
rooted received-line/witness/slope classifier.

Proof status: PROVED_LOCAL / AUDIT / OPEN_GAP.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Sequence


ROOT = Path(__file__).resolve().parents[2]
CERT_REL = Path(
    "experimental/data/certificates/primitive-top-seam-marked-incidence-v1/"
    "primitive_top_seam_marked_incidence_v1.json"
)
P = 17
N = 16
GENERATOR = 3
DOMAIN = tuple(pow(GENERATOR, i, P) for i in range(N))
DOMAIN_SET = frozenset(DOMAIN)
OWNER_STATES = {
    "NOT_APPLICABLE",
    "STRUCTURAL_TRIGGER_ONLY",
    "PAID_OWNER",
    "NAMED_RESIDUAL",
    "UNKNOWN_MISSING_CONTEXT",
}
VERDICT = "OPEN GAP"


class CertificateError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CertificateError(message)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def trim(poly: Sequence[int], p: int = P) -> tuple[int, ...]:
    out = [value % p for value in poly]
    if not out:
        return (0,)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def poly_add(left: Sequence[int], right: Sequence[int], p: int = P) -> tuple[int, ...]:
    width = max(len(left), len(right))
    return trim(
        [
            ((left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)) % p
            for i in range(width)
        ],
        p,
    )


def poly_sub(left: Sequence[int], right: Sequence[int], p: int = P) -> tuple[int, ...]:
    width = max(len(left), len(right))
    return trim(
        [
            ((left[i] if i < len(left) else 0) - (right[i] if i < len(right) else 0)) % p
            for i in range(width)
        ],
        p,
    )


def poly_mul(left: Sequence[int], right: Sequence[int], p: int = P) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return trim(out, p)


def poly_divmod(
    numerator: Sequence[int], denominator: Sequence[int], p: int = P
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    num = list(trim(numerator, p))
    den = trim(denominator, p)
    require(den != (0,), "division by zero polynomial")
    quotient = [0] * max(1, len(num) - len(den) + 1)
    inverse = pow(den[-1], -1, p)
    while len(num) >= len(den) and any(num):
        shift = len(num) - len(den)
        coefficient = num[-1] * inverse % p
        quotient[shift] = coefficient
        for i, value in enumerate(den):
            num[i + shift] = (num[i + shift] - coefficient * value) % p
        while len(num) > 1 and num[-1] == 0:
            num.pop()
    return trim(quotient, p), trim(num, p)


def poly_gcd(left: Sequence[int], right: Sequence[int], p: int = P) -> tuple[int, ...]:
    a, b = trim(left, p), trim(right, p)
    while b != (0,):
        _, remainder = poly_divmod(a, b, p)
        a, b = b, remainder
    inverse = pow(a[-1], -1, p)
    return tuple(value * inverse % p for value in a)


def poly_eval(poly: Sequence[int], x: int, p: int = P) -> int:
    return sum(value * pow(x, degree, p) for degree, value in enumerate(poly)) % p


def degree(poly: Sequence[int], p: int = P) -> int:
    normalized = trim(poly, p)
    return -1 if normalized == (0,) else len(normalized) - 1


def locator(roots: Iterable[int], p: int = P) -> tuple[int, ...]:
    out = (1,)
    for root in sorted(roots):
        out = poly_mul(out, ((-root) % p, 1), p)
    return out


def power_target(roots: Iterable[int], w: int, p: int = P) -> tuple[int, ...]:
    root_tuple = tuple(roots)
    return tuple(sum(pow(root, j, p) for root in root_tuple) % p for j in range(1, w + 1))


def locator_prefix(roots: Iterable[int], w: int, p: int = P) -> tuple[int, ...]:
    roots_tuple = tuple(roots)
    loc = locator(roots_tuple, p)
    m = len(roots_tuple)
    return tuple(loc[m - j] for j in range(1, w + 1))


def divisors(n: int) -> tuple[int, ...]:
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def periodic_scales(roots: Iterable[int]) -> tuple[int, ...]:
    support = frozenset(roots)
    scales = []
    for scale in divisors(N):
        if scale < 2 or len(support) % scale:
            continue
        multiplier = pow(GENERATOR, N // scale, P)
        if frozenset(multiplier * root % P for root in support) == support:
            scales.append(scale)
    return tuple(scales)


def common_pullback_scales(left: Iterable[int], right: Iterable[int]) -> tuple[int, ...]:
    return tuple(sorted(set(periodic_scales(left)) & set(periodic_scales(right))))


def affine_maps(
    source: Iterable[int], target: Iterable[int], *, domain_preserving: bool = False
) -> tuple[tuple[int, int], ...]:
    source_set = frozenset(source)
    target_set = frozenset(target)
    maps = []
    for a in range(1, P):
        for b in range(P):
            if domain_preserving and frozenset((a * x + b) % P for x in DOMAIN_SET) != DOMAIN_SET:
                continue
            if frozenset((a * x + b) % P for x in source_set) == target_set:
                maps.append((a, b))
    return tuple(maps)


def affine_stabilizer(roots: Iterable[int]) -> tuple[tuple[int, int], ...]:
    roots_tuple = tuple(roots)
    return affine_maps(roots_tuple, roots_tuple)


def multiplicative_stabilizer(roots: Iterable[int]) -> tuple[int, ...]:
    support = frozenset(roots)
    return tuple(a for a in range(1, P) if frozenset(a * x % P for x in support) == support)


def source_environment(path: Path, label: str) -> dict[str, Any]:
    text = (ROOT / path).read_text(encoding="utf-8")
    lines = text.splitlines()
    match = re.search(r"\\label\{" + re.escape(label) + r"\}", text)
    require(match is not None, f"missing source label {label}")
    line = text[: match.start()].count("\n") + 1
    start = line
    while start > 1 and "\\begin{" not in lines[start - 1]:
        start -= 1
    begin_match = re.search(r"\\begin\{([^}]+)\}", lines[start - 1])
    require(begin_match is not None, f"missing source environment start {label}")
    environment = begin_match.group(1)
    begin_token = f"\\begin{{{environment}}}"
    end_token = f"\\end{{{environment}}}"
    depth = 0
    end = start
    while end <= len(lines):
        depth += lines[end - 1].count(begin_token)
        depth -= lines[end - 1].count(end_token)
        if depth == 0:
            break
        end += 1
    require(end <= len(lines) and depth == 0, f"unterminated source environment {label}")
    block = "\n".join(lines[start - 1 : end]) + "\n"
    return {
        "path": path.as_posix(),
        "label": label,
        "line_start": start,
        "line_end": end,
        "sha256": hashlib.sha256(block.encode()).hexdigest(),
    }


def source_anchors() -> list[dict[str, Any]]:
    return [
        source_environment(Path("experimental/cap25_cap_v13_raw.tex"), "thm:capg-second-moment"),
        source_environment(Path("experimental/asymptotic_rs_mca_frontiers.tex"), "def:first-match"),
        source_environment(
            Path("experimental/asymptotic_rs_mca_frontiers.tex"),
            "def:primitive-first-match-residual",
        ),
        source_environment(Path("experimental/asymptotic_rs_mca.tex"), "def:closed-ledger"),
        source_environment(Path("experimental/asymptotic_rs_mca.tex"), "def:ray-compiler"),
        source_environment(Path("experimental/grande_finale.tex"), "prop:line-ray-saturation"),
        source_environment(Path("experimental/grande_finale.tex"), "prop:pole-line"),
    ]


def triple_record(core: Iterable[int], side_a: Iterable[int], side_b: Iterable[int]) -> dict[str, Any]:
    core_t = tuple(sorted(core))
    a_t = tuple(sorted(side_a))
    b_t = tuple(sorted(side_b))
    g_poly, a_poly, b_poly = locator(core_t), locator(a_t), locator(b_t)
    diff = poly_sub(a_poly, b_poly)
    support_a = tuple(sorted((*core_t, *a_t)))
    support_b = tuple(sorted((*core_t, *b_t)))
    require(degree(diff) == 0 and diff[0] != 0, "not a top-seam constant shift")
    require(not (set(core_t) & set(a_t) or set(core_t) & set(b_t) or set(a_t) & set(b_t)),
            "triple root sets are not pairwise disjoint")
    require(poly_gcd(g_poly, a_poly) == (1,), "gcd(G,A) is nontrivial")
    require(poly_gcd(g_poly, b_poly) == (1,), "gcd(G,B) is nontrivial")
    require(poly_gcd(a_poly, b_poly) == (1,), "gcd(A,B) is nontrivial")
    return {
        "G_roots": list(core_t),
        "A_roots": list(a_t),
        "B_roots": list(b_t),
        "G_coefficients_ascending": list(g_poly),
        "A_coefficients_ascending": list(a_poly),
        "B_coefficients_ascending": list(b_poly),
        "A_minus_B": diff[0],
        "support_A": list(support_a),
        "support_B": list(support_b),
        "target": list(power_target(support_a, 2)),
        "pairwise_coprime": True,
    }


def known_multiple_mate_packet() -> dict[str, Any]:
    m, w, e = 4, 2, 3
    marked_support = (4, 6, 11, 13)
    expected_mates = (
        (1, 2, 4, 10),
        (3, 8, 10, 13),
        (4, 7, 9, 14),
        (7, 13, 15, 16),
    )
    supports = tuple(itertools.combinations(sorted(DOMAIN_SET), m))
    target = power_target(marked_support, w)
    fiber = tuple(support for support in supports if power_target(support, w) == target)
    seam_mates = tuple(
        support for support in fiber
        if support != marked_support and len(set(support) & set(marked_support)) == m - e
    )
    require(seam_mates == expected_mates, "known F17 multiple-mate packet drift")

    triples = []
    for mate in seam_mates:
        core = tuple(sorted(set(mate) & set(marked_support)))
        side_a = tuple(sorted(set(marked_support) - set(mate)))
        side_b = tuple(sorted(set(mate) - set(marked_support)))
        record = triple_record(core, side_a, side_b)
        record["side_affine_maps_A_to_B"] = [list(item) for item in affine_maps(side_a, side_b)]
        triples.append(record)

    complete_ordered_pairs = tuple(
        (left, right)
        for left in fiber
        for right in fiber
        if left != right and len(set(left) - set(right)) == e
    )
    require(len(complete_ordered_pairs) == 32, "complete F17 top-seam incidence drift")
    complete_triples = []
    for left, right in complete_ordered_pairs:
        core = tuple(sorted(set(left) & set(right)))
        side_a = tuple(sorted(set(left) - set(right)))
        side_b = tuple(sorted(set(right) - set(left)))
        complete_triples.append(triple_record(core, side_a, side_b))
    require(
        len(
            {
                (tuple(row["A_roots"]), tuple(row["B_roots"]))
                for row in complete_triples
            }
        )
        == 32,
        "complete F17 side-locator projection drift",
    )

    prefix = locator_prefix(marked_support, w)
    u_z = [0] * (m + 1)
    u_z[m] = 1
    for j, coefficient in enumerate(prefix, start=1):
        u_z[m - j] = coefficient
    u_z_t = trim(u_z)
    support_states = []
    for support in fiber:
        loc = locator(support)
        slope = (poly_eval(u_z_t, 0) - poly_eval(loc, 0)) % P
        numerator = poly_sub(poly_sub(u_z_t, loc), (slope,))
        require(numerator[0] == 0, "pole-line numerator not divisible by X")
        explanation = trim(numerator[1:])
        require(degree(explanation) < 1, "pole-line explanation exceeds RS dimension one")
        codeword = tuple(poly_eval(explanation, x) for x in DOMAIN)
        support_states.append(
            {
                "support": list(support),
                "slope": slope,
                "explanation_polynomial_ascending": list(explanation),
                "codeword_evaluation_in_domain_order": list(codeword),
                "periodic_scales": list(periodic_scales(support)),
                "support_structural_class": (
                    "periodic_support_trigger_only"
                    if periodic_scales(support)
                    else "not_classified_here"
                ),
                "actual_first_match_owner": None,
            }
        )

    state_by_support = {tuple(row["support"]): row for row in support_states}
    explanation_by_support = {
        support: (
            row["slope"],
            support,
            tuple(row["explanation_polynomial_ascending"]),
        )
        for support, row in state_by_support.items()
    }
    witness_ray_by_support = {
        support: (row["slope"], tuple(row["explanation_polynomial_ascending"]))
        for support, row in state_by_support.items()
    }
    codeword_ray_by_support = {
        support: (row["slope"], tuple(row["codeword_evaluation_in_domain_order"]))
        for support, row in state_by_support.items()
    }
    require(
        len(set(witness_ray_by_support.values()))
        == len(set(codeword_ray_by_support.values())),
        "explanation-to-codeword ray map is not injective in the fixture",
    )

    # Verify the received pole line directly, not only through locator algebra.
    f_values = tuple(poly_eval(u_z_t, x) * pow(x, -1, P) % P for x in DOMAIN)
    g_values = tuple(-pow(x, -1, P) % P for x in DOMAIN)
    require(len(set(g_values)) == len(DOMAIN), "pole direction is not injective")
    exhaustive_scan = []
    for slope in range(P):
        for constant_codeword in range(P):
            agreement = tuple(
                sorted(
                    x
                    for x, f_value, g_value in zip(DOMAIN, f_values, g_values)
                    if (f_value + slope * g_value - constant_codeword) % P == 0
                )
            )
            if len(agreement) >= m:
                exhaustive_scan.append(
                    {
                        "slope": slope,
                        "constant_codeword": constant_codeword,
                        "agreement_support": list(agreement),
                        "agreement_size": len(agreement),
                    }
                )
    scan_keys = {
        (row["slope"], row["constant_codeword"], tuple(row["agreement_support"]))
        for row in exhaustive_scan
    }
    state_keys = {
        (
            row["slope"],
            row["explanation_polynomial_ascending"][0],
            tuple(row["support"]),
        )
        for row in support_states
    }
    require(scan_keys == state_keys and len(exhaustive_scan) == 7,
            "exhaustive pole-line MCA scan drift")
    require(all(row["agreement_size"] == m for row in exhaustive_scan),
            "unexpected pole-line agreement size")

    def incidence_scope(
        name: str,
        oriented_pairs: Sequence[tuple[tuple[int, ...], tuple[int, ...]]],
        endpoint_selector: Any,
    ) -> dict[str, Any]:
        edges = []
        side_projection = set()
        for index, pair in enumerate(oriented_pairs):
            left, right = pair
            side_projection.add(
                (
                    tuple(sorted(set(left) - set(right))),
                    tuple(sorted(set(right) - set(left))),
                )
            )
            for support in endpoint_selector(pair):
                edges.append((index, support))
        selected_supports = tuple(sorted({support for _, support in edges}))
        explanation_states = {
            explanation_by_support[support] for support in selected_supports
        }
        witness_rays = {witness_ray_by_support[support] for support in selected_supports}
        codeword_rays = {codeword_ray_by_support[support] for support in selected_supports}
        require(len(witness_rays) == len(codeword_rays),
                f"{name} explanation/codeword ray multiplicity drift")
        slopes = sorted({ray[0] for ray in witness_rays})
        ray_degrees: Counter[tuple[int, tuple[int, ...]]] = Counter()
        slope_degrees: Counter[int] = Counter()
        triple_degrees: Counter[int] = Counter()
        support_degrees: Counter[tuple[int, ...]] = Counter()
        for index, support in edges:
            ray = witness_ray_by_support[support]
            ray_degrees[ray] += 1
            slope_degrees[ray[0]] += 1
            triple_degrees[index] += 1
            support_degrees[support] += 1
        h_min = min(slope_degrees.values())
        j_max = max(triple_degrees.values())
        require(h_min >= 1, f"{name} is not exhaustive over its declared slope image")
        require(h_min * len(slopes) <= len(edges) <= j_max * len(oriented_pairs),
                f"{name} H/J projection inequality failed")
        return {
            "scope": name,
            "marked_triples_T": len(oriented_pairs),
            "ordered_full_support_pairs_P_full": len(set(oriented_pairs)),
            "ordered_side_locator_pairs_P_side": len(side_projection),
            "explanation_states": len(explanation_states),
            "witness_rays": len(witness_rays),
            "codeword_rays": len(codeword_rays),
            "distinct_slope_image": len(slopes),
            "slopes": slopes,
            "marked_triples_per_witness_ray_histogram": {
                str(key): value
                for key, value in sorted(Counter(ray_degrees.values()).items())
            },
            "witness_rays_per_slope_histogram": {
                str(key): value
                for key, value in sorted(
                    Counter(Counter(ray[0] for ray in witness_rays).values()).items()
                )
            },
            "marked_degree_by_selected_support": {
                ",".join(map(str, support)): value
                for support, value in sorted(support_degrees.items())
            },
            "marked_degree_by_witness_ray": {
                f"gamma={ray[0]};h={list(ray[1])}": value
                for ray, value in sorted(ray_degrees.items())
            },
            "marked_degree_by_slope": {
                str(slope): value for slope, value in sorted(slope_degrees.items())
            },
            "projection_H": h_min,
            "projection_J": j_max,
            "incidence_edges": len(edges),
            "HJ_upper_bound": j_max * len(oriented_pairs) // h_min,
            "HJ_bound_pass": len(slopes) <= j_max * len(oriented_pairs) // h_min,
        }

    rooted_star_pairs = tuple((marked_support, mate) for mate in seam_mates)
    reverse_star_pairs = tuple((mate, marked_support) for mate in seam_mates)
    complete_top_seam_scope = incidence_scope(
        "complete_ordered_top_seam_selected_support_projection",
        complete_ordered_pairs,
        lambda pair: (pair[0],),
    )
    complete_top_seam_endpoint_relation = incidence_scope(
        "complete_ordered_top_seam_both_endpoints",
        complete_ordered_pairs,
        lambda pair: pair,
    )
    endpoint_scope = incidence_scope(
        "rooted_multiple_mate_star_both_endpoints",
        rooted_star_pairs,
        lambda pair: pair,
    )
    selected_S0_scope = incidence_scope(
        "rooted_multiple_mate_star_selected_S0_support",
        rooted_star_pairs,
        lambda pair: (pair[0],),
    )
    reverse_mate_scope = incidence_scope(
        "reverse_rooted_star_selected_mate_supports",
        reverse_star_pairs,
        lambda pair: (pair[0],),
    )
    require(
        (
            complete_top_seam_scope["marked_triples_T"],
            complete_top_seam_scope["ordered_full_support_pairs_P_full"],
            complete_top_seam_scope["ordered_side_locator_pairs_P_side"],
            complete_top_seam_scope["explanation_states"],
            complete_top_seam_scope["witness_rays"],
            complete_top_seam_scope["distinct_slope_image"],
            complete_top_seam_scope["slopes"],
            complete_top_seam_scope["projection_H"],
            complete_top_seam_scope["projection_J"],
            complete_top_seam_scope["incidence_edges"],
        )
        == (32, 32, 32, 7, 7, 4, [2, 5, 8, 11], 4, 1, 32),
        "complete top-seam projection fixture drift",
    )
    require(
        (
            complete_top_seam_endpoint_relation["projection_H"],
            complete_top_seam_endpoint_relation["projection_J"],
            complete_top_seam_endpoint_relation["incidence_edges"],
        )
        == (8, 2, 64),
        "complete two-endpoint relation drift",
    )
    require(
        (
            endpoint_scope["explanation_states"],
            endpoint_scope["witness_rays"],
            endpoint_scope["distinct_slope_image"],
            endpoint_scope["slopes"],
            endpoint_scope["projection_H"],
            endpoint_scope["projection_J"],
        )
        == (5, 5, 3, [2, 5, 8], 2, 2),
        "selected endpoint projection fixture drift",
    )
    require(
        (
            selected_S0_scope["explanation_states"],
            selected_S0_scope["witness_rays"],
            selected_S0_scope["distinct_slope_image"],
            selected_S0_scope["slopes"],
            selected_S0_scope["projection_H"],
            selected_S0_scope["projection_J"],
        )
        == (1, 1, 1, [2], 4, 1),
        "rooted selected-S0 projection fixture drift",
    )
    require(
        (
            reverse_mate_scope["explanation_states"],
            reverse_mate_scope["witness_rays"],
            reverse_mate_scope["distinct_slope_image"],
            reverse_mate_scope["slopes"],
            reverse_mate_scope["projection_H"],
            reverse_mate_scope["projection_J"],
        )
        == (4, 4, 2, [5, 8], 2, 1),
        "reverse mate-selected projection fixture drift",
    )
    full_witness_rays = set(witness_ray_by_support.values())
    full_codeword_rays = set(codeword_ray_by_support.values())
    full_slopes = sorted({ray[0] for ray in full_witness_rays})
    require(len(support_states) == len(full_witness_rays) == len(full_codeword_rays) == 7,
            "complete pole-line state/ray count drift")
    require(full_slopes == [2, 5, 8, 11], "complete pole-line slope set drift")
    rooted_star_uncovered_slopes = sorted(set(full_slopes) - set(endpoint_scope["slopes"]))
    require(rooted_star_uncovered_slopes == [11], "rooted-star coverage guardrail drift")
    return {
        "parameters": {"p": P, "domain": "F_17^*", "m": m, "w": w, "e": e},
        "target_power_sums": list(target),
        "target_locator_prefix": list(prefix),
        "fiber_size": len(fiber),
        "fiber_supports": [list(item) for item in fiber],
        "marked_support_S0": list(marked_support),
        "marked_support_S0_periodic_scales": list(periodic_scales(marked_support)),
        "top_seam_mate_count": len(seam_mates),
        "rooted_multiple_mate_star_triples": triples,
        "complete_ordered_top_seam_triple_count": len(complete_triples),
        "complete_ordered_top_seam_triples": complete_triples,
        "side_affine_trigger_count": sum(bool(row["side_affine_maps_A_to_B"]) for row in triples),
        "pole_line": {
            "code": "RS(F_17,F_17^*,1)",
            "pole": 0,
            "U_z_coefficients_ascending": list(u_z_t),
            "received_line": {
                "f_definition": "f(x)=U_z(x)/x",
                "g_definition": "g(x)=-1/x",
                "domain_order": list(DOMAIN),
                "f_values": list(f_values),
                "g_values": list(g_values),
                "g_pairwise_distinct": True,
                "noncommon_reason": (
                    "g is not a degree-less-than-1 codeword on any support of size at least 2"
                ),
                "exhaustive_slope_codeword_scan": exhaustive_scan,
            },
            "all_support_explanation_states": support_states,
            "complete_pole_line": {
                "support_count": len(support_states),
                "explanation_states": len(support_states),
                "witness_rays": len(full_witness_rays),
                "codeword_rays": len(full_codeword_rays),
                "distinct_MCA_slopes": len(full_slopes),
                "slopes": full_slopes,
                "witness_rays_per_slope_histogram": {
                    str(key): value
                    for key, value in sorted(
                        Counter(Counter(ray[0] for ray in full_witness_rays).values()).items()
                    )
                },
            },
            "complete_top_seam_marked_incidence": complete_top_seam_scope,
            "complete_top_seam_two_endpoint_relation": complete_top_seam_endpoint_relation,
            "rooted_multiple_mate_star_endpoint_incidence": endpoint_scope,
            "rooted_multiple_mate_star_selected_S0_projection": selected_S0_scope,
            "reverse_rooted_star_selected_mate_projection": reverse_mate_scope,
            "complete_MCA_slopes_uncovered_by_rooted_star": rooted_star_uncovered_slopes,
            "rooted_star_complete_slope_set_projection_H": 0,
            "rooted_star_complete_slope_set_HJ_bound_applicable": False,
            "rooted_star_nonpayment_reason": (
                "slope 11 has no incident rooted-star triple, so the four-mate star is not "
                "exhaustive over the complete MCA numerator; the separate complete 32-triple "
                "top-seam incidence does cover it"
            ),
            "first_match_status": (
                "support periodicity is only a structural trigger; no endpoint ray is assigned "
                "an actual first-match owner by this packet"
            ),
        },
    }


def side_pairs(e: int, w: int) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    supports = list(itertools.combinations(sorted(DOMAIN_SET), e))
    buckets: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for support in supports:
        buckets[power_target(support, w)].append(support)
    out = []
    for bucket in buckets.values():
        for left in bucket:
            for right in bucket:
                if left != right and set(left).isdisjoint(right):
                    diff = poly_sub(locator(left), locator(right))
                    require(degree(diff) == e - w - 1, "side-pair degree normal form drift")
                    out.append((left, right))
    return out


def marked_core_census() -> dict[str, Any]:
    m, w, e, g = 8, 2, 3, 5
    pairs = side_pairs(e, w)
    require(len(pairs) == 704, "ordered F17 side-pair count drift")
    require(all(not common_pullback_scales(a, b) for a, b in pairs),
            "unexpected quotient pullback at coprime e=3,n=16")
    raw_core_count = math.comb(N - 2 * e, g)
    key_counts: Counter[tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]] = Counter()
    fixed_candidate_a = (1, 4, 11)
    fixed_candidate_b = (3, 14, 16)
    fixed_target = (16, 16)
    fixed_cores = []
    affine_side_samples = []
    for side_a, side_b in pairs:
        maps = affine_maps(side_a, side_b)
        if maps and len(affine_side_samples) < 2:
            affine_side_samples.append(
                {
                    "A": list(side_a),
                    "B": list(side_b),
                    "root_set_affine_maps": [list(item) for item in maps],
                    "state": "STRUCTURAL_TRIGGER_ONLY",
                    "owner_status": "NOT_ESTABLISHED",
                    "paid_owner_established": False,
                    "primitive_admission": False,
                    "missing_for_owner": (
                        "a declared domain map, rooted witness descent, natural-profile census, "
                        "and exact distinct-slope budget"
                    ),
                }
            )
        complement = sorted(DOMAIN_SET - set(side_a) - set(side_b))
        require(len(complement) == N - 2 * e, "side complement size drift")
        for core in itertools.combinations(complement, g):
            target = tuple(
                (x + y) % P for x, y in zip(power_target(core, w), power_target(side_a, w))
            )
            key_counts[(target, side_a, side_b)] += 1
            if side_a == fixed_candidate_a and side_b == fixed_candidate_b and target == fixed_target:
                fixed_cores.append(core)

    marked_count = len(pairs) * raw_core_count
    require(sum(key_counts.values()) == marked_count, "marked core census total drift")

    # Independent route: enumerate ordered full-support pairs at the fixed target depth.
    support_buckets: dict[tuple[int, ...], list[frozenset[int]]] = defaultdict(list)
    for support in itertools.combinations(sorted(DOMAIN_SET), m):
        support_buckets[power_target(support, w)].append(frozenset(support))
    independent_marked_count = 0
    for bucket in support_buckets.values():
        for left in bucket:
            for right in bucket:
                if left != right and len(left - right) == e:
                    independent_marked_count += 1
    require(independent_marked_count == marked_count, "independent support-pair census mismatch")

    require(
        fixed_cores
        == [
            (2, 5, 7, 8, 12),
            (5, 9, 10, 12, 15),
            (6, 8, 9, 13, 15),
        ],
        "fixed-target common-core packet drift",
    )
    require(not affine_maps(fixed_candidate_a, fixed_candidate_b),
            "fixed candidate unexpectedly has an affine side transport")
    fixed_records = []
    for core in fixed_cores:
        record = triple_record(core, fixed_candidate_a, fixed_candidate_b)
        require(tuple(record["target"]) == fixed_target, "fixed candidate target drift")
        support_a = tuple(record["support_A"])
        support_b = tuple(record["support_B"])
        require(multiplicative_stabilizer(core) == (1,), "core multiplicative stabilizer drift")
        require(multiplicative_stabilizer(support_a) == (1,), "support A quotient gate drift")
        require(multiplicative_stabilizer(support_b) == (1,), "support B quotient gate drift")
        require(affine_stabilizer(core) == ((1, 0),), "core affine stabilizer drift")
        require(affine_stabilizer(support_a) == ((1, 0),), "support A affine stabilizer drift")
        require(affine_stabilizer(support_b) == ((1, 0),), "support B affine stabilizer drift")
        fixed_records.append(record)
    require(
        not set.intersection(*(set(core) for core in fixed_cores)),
        "displayed distinct-core family unexpectedly has a common planted divisor",
    )
    oriented_support_a_intersection = sorted(
        set.intersection(*(set(row["support_A"]) for row in fixed_records))
    )
    oriented_support_b_intersection = sorted(
        set.intersection(*(set(row["support_B"]) for row in fixed_records))
    )
    aggregate_support_intersection = sorted(
        set.intersection(
            *(set(row[key]) for row in fixed_records for key in ("support_A", "support_B"))
        )
    )
    require(oriented_support_a_intersection == list(fixed_candidate_a),
            "oriented support-A common divisor drift")
    require(oriented_support_b_intersection == list(fixed_candidate_b),
            "oriented support-B common divisor drift")
    require(aggregate_support_intersection == [],
            "six-support aggregate common divisor drift")

    histogram = Counter(key_counts.values())
    maximum = max(key_counts.values())
    max_key = min(key for key, value in key_counts.items() if value == maximum)
    max_cores = []
    target_max, side_a_max, side_b_max = max_key
    complement_max = sorted(DOMAIN_SET - set(side_a_max) - set(side_b_max))
    for core in itertools.combinations(complement_max, g):
        target = tuple(
            (x + y) % P for x, y in zip(power_target(core, w), power_target(side_a_max, w))
        )
        if target == target_max:
            max_cores.append(core)
    return {
        "parameters": {"p": P, "n": N, "m": m, "w": w, "e": e, "deg_G": g},
        "ordered_side_pairs": len(pairs),
        "common_pullback_side_pairs": sum(bool(common_pullback_scales(a, b)) for a, b in pairs),
        "raw_cores_per_side_pair": raw_core_count,
        "ordered_marked_triples": marked_count,
        "independent_ordered_support_pair_count": independent_marked_count,
        "mark_erasure_projection": {
            "map": "(G,A,B) -> (A,B), preserving orientation",
            "fibre_size_set_without_target": [raw_core_count],
            "multiplicity_factor": raw_core_count,
            "cardinality_difference": marked_count - len(pairs),
            "identity": f"{len(pairs)}*{raw_core_count}={marked_count}",
        },
        "fixed_target_core_fibres": {
            "nonempty_key_count": len(key_counts),
            "multiplicity_histogram": {str(key): value for key, value in sorted(histogram.items())},
            "maximum_multiplicity": maximum,
            "lexicographically_first_maximum": {
                "target": list(target_max),
                "A": list(side_a_max),
                "B": list(side_b_max),
                "cores": [list(core) for core in max_cores],
            },
        },
        "fixed_no_obvious_symmetry_packet": {
            "target": list(fixed_target),
            "A": list(fixed_candidate_a),
            "B": list(fixed_candidate_b),
            "A_minus_B": poly_sub(locator(fixed_candidate_a), locator(fixed_candidate_b))[0],
            "core_count": len(fixed_cores),
            "records": fixed_records,
            "common_pullback_scales": list(common_pullback_scales(fixed_candidate_a, fixed_candidate_b)),
            "side_affine_maps": [list(item) for item in affine_maps(fixed_candidate_a, fixed_candidate_b)],
            "all_core_and_support_multiplicative_stabilizers_trivial": True,
            "all_core_and_support_affine_stabilizers_trivial": True,
            "raw_Q_prefix_fibre_constraint": {
                "owner_status": "NOT_AN_OWNER",
                "equations": "target(G)=target(z)-target(A) in the first w power sums",
                "coefficient_slice_equivalence_condition": "characteristic(F)>w",
                "meaning": (
                    "this tautological fixed-target slice is the common-core multiplicity "
                    "problem, not an earlier first-match payment"
                ),
            },
            "displayed_core_family_common_root_intersection": [],
            "oriented_support_A_family_common_root_intersection": oriented_support_a_intersection,
            "oriented_support_B_family_common_root_intersection": oriented_support_b_intersection,
            "six_support_aggregate_common_root_intersection": aggregate_support_intersection,
            "planted_owner_status": "UNKNOWN_MISSING_CONTEXT",
            "primitive_admission": False,
            "primitive_admission_blocker": "the rooted first-match owner atlas is unavailable",
        },
        "side_root_affine_transport_gate_regressions": affine_side_samples,
    }


def fail_closed_owner_contract() -> dict[str, Any]:
    order = [
        ("C1", "quotient_pullback_complete_fibre_and_remainder"),
        ("C2", "chebyshev_dihedral"),
        ("C3", "planted_block"),
        ("C4", "tangent_deep_centre"),
        ("C5", "extension_and_field_descent"),
        ("C6", "differential_locator_rank_and_bounded_SPI"),
        ("C7", "saturation_effective_image_collapse"),
        ("pre_C8", "family_level_common_GCD_exclusion"),
        ("C8", "balanced_core_after_common_and_planted_factor_removal_and_split_pencil"),
        ("C9", "fourier_sidon"),
    ]
    fixed_fixture_states = [
        {"cell": "C1_multiplicative_periodicity_subcell", "state": "NOT_APPLICABLE", "reason": "the displayed fixed-target packet has no common side pullback and its displayed supports have trivial multiplicative stabilizer"},
        {"cell": "C1_complete_quotient_remainder", "state": "UNKNOWN_MISSING_CONTEXT", "reason": "not every declared quotient map, canonical remainder, received-line descent, and slope projector is executable from (G,A,B)"},
        {"cell": "C2", "state": "UNKNOWN_MISSING_CONTEXT", "reason": "no typed dihedral witness projector"},
        {"cell": "C3", "state": "UNKNOWN_MISSING_CONTEXT", "reason": "the three distinct G marks have no family-wide common root; no predetermined planted divisor family or payment census is supplied"},
        {"cell": "C4", "state": "UNKNOWN_MISSING_CONTEXT", "reason": "tangent ownership needs the actual received line and witness"},
        {"cell": "C5", "state": "NOT_APPLICABLE", "reason": "base-field toy fixture has no extension-valued parameter"},
        {"cell": "C6", "state": "UNKNOWN_MISSING_CONTEXT", "reason": "no actual owner-typed incidence matrix or bounded-SPI projector"},
        {"cell": "C7", "state": "UNKNOWN_MISSING_CONTEXT", "reason": "support triples do not determine the saturated ray projection"},
        {"cell": "pre_C8_common_GCD", "state": "UNKNOWN_MISSING_CONTEXT", "reason": "the six-support aggregate has empty intersection, but the oriented support-A and support-B subfamilies retain fixed side divisors; the rooted atlas must specify the classified family"},
        {"cell": "C8", "state": "UNKNOWN_MISSING_CONTEXT", "reason": "no residual chart after proved removal of earlier common and planted factors is available"},
        {"cell": "C9", "state": "UNKNOWN_MISSING_CONTEXT", "reason": "Fourier/Sidon is applied only after the earlier actual slope cells"},
    ]
    require(all(row["state"] in OWNER_STATES for row in fixed_fixture_states), "owner-state vocabulary drift")
    periodic_fixture = (4, 6, 11, 13)
    affine_a, affine_b = (1, 2, 4), (12, 14, 15)
    require(periodic_scales(periodic_fixture) == (2,), "periodic gate fixture drift")
    require(affine_maps(affine_a, affine_b) == ((16, 16),), "affine gate fixture drift")
    return {
        "version": "top-seam-fail-closed-v1",
        "authoritative_semantics": "first match partitions actual bad-slope projections, not support-side triples",
        "order_kind": "local refinement of source C1--C9; added pre_C8 is not part of C8",
        "order": [{"cell": cell, "owner_or_exclusion": owner} for cell, owner in order],
        "admission_rule": (
            "primitive only if every earlier actual-slope predicate is executable and false; "
            "STRUCTURAL_TRIGGER_ONLY or UNKNOWN_MISSING_CONTEXT blocks admission"
        ),
        "paid_owner_required_fields": [
            "source_cell",
            "projector_certificate_id",
            "projection_type",
            "exact_slope_budget",
        ],
        "paid_owner_count": 0,
        "fixed_fixture_states": fixed_fixture_states,
        "raw_Q_prefix_fibre_is_not_an_owner": True,
        "preprimitive_gate_regressions": {
            "periodic_support_candidate": {
                "support": list(periodic_fixture),
                "periodic_scales": [2],
                "state": "STRUCTURAL_TRIGGER_ONLY",
                "owner_status": "NOT_ESTABLISHED",
                "paid_owner_established": False,
                "primitive_admission": False,
                "reason": "support periodicity alone does not prove received-line and explanation descent",
            },
            "side_root_affine_transport_candidate": {
                "A": list(affine_a),
                "B": list(affine_b),
                "map_x_to_ax_plus_b": [16, 16],
                "state": "STRUCTURAL_TRIGGER_ONLY",
                "owner_status": "NOT_ESTABLISHED",
                "paid_owner_established": False,
                "primitive_admission": False,
                "reason": "the root-set map is not a declared domain map and has no rooted slope payment",
            },
            "scope": (
                "these are fail-closed gate tests, not proofs that either candidate is a paid owner"
            ),
        },
        "quotient_before_primitive": True,
        "affine_candidate_before_primitive": True,
        "post_first_match_marked_universe_defined": False,
        "actual_surviving_triple_count": None,
        "missing_rooted_chain": "(G,A,B) -> (gamma,S,h) -> (gamma,h) -> (gamma,c) -> gamma",
    }


def projection_interface() -> dict[str, Any]:
    return {
        "sets_kept_separate": [
            "marked_support_incidences_T_z=(G,A,B)",
            "ordered_reconstructed_support_pairs_P_full_z=(GA,GB)",
            "ordered_side_locator_pairs_P_side_z=(A,B)",
            "explanation_states_X=(gamma,S,h)",
            "witness_rays_R=(gamma,h)",
            "codeword_rays_C=(gamma,c)",
            "distinct_MCA_slopes_Z",
        ],
        "marked_full_pair_bijection": "T_z <-> P_full_z, so |T_z|=|P_full_z|",
        "common_core_fibre": "mu_G(z,A,B)=#{G:(G,A,B) in T_z}",
        "mark_erasure_bound": "|T_z| <= max_(A,B) mu_G(z,A,B) * |P_side_z|",
        "aggregated_target_rule": (
            "if targets vary, retain z in the side projection key before applying mu_G"
        ),
        "actual_incidence": "I subseteq Z_T x T_z, where Z_T is exactly the incident slope image",
        "projection_degrees": {
            "H": "min_(gamma in Z_T) deg_I(gamma), with H>=1 by declared exhaustivity",
            "J": "max_(t in T_z) deg_I(t)",
        },
        "slope_bound": (
            "|Z_T| <= floor(J*|T_z|/H) <= "
            "floor(J*mu_G^max*|P_side_z|/H)"
        ),
        "natural_scale_requirement": "J*mu_G^max/H = exp(o(n)) when only a natural-scale side-pair bound is available",
        "full_MCA_guardrail": (
            "if a complete MCA slope has degree zero from the chosen marked family, then H=0 "
            "on the complete slope set and this bound is inapplicable"
        ),
        "nonclaim": (
            "a marked-pair or second-moment estimate without a rooted exhaustive incidence "
            "and explicit H,J is not a slope payment"
        ),
    }


def add_payload_hash(certificate: dict[str, Any]) -> dict[str, Any]:
    out = copy.deepcopy(certificate)
    out.pop("payload_sha256", None)
    out["payload_sha256"] = hashlib.sha256(canonical_json(out).encode()).hexdigest()
    return out


def build_certificate() -> dict[str, Any]:
    certificate = {
        "schema": "primitive_top_seam_marked_incidence.v1",
        "status": "PROVED_LOCAL / AUDIT / OPEN_GAP",
        "verdict": VERDICT,
        "claim_scope": (
            "exact top-seam marked normal form, finite F17 regressions, fail-closed owner typing, "
            "and exact marked-to-slope projection requirements"
        ),
        "source_anchors": source_anchors(),
        "normal_form": {
            "equation": "A-B=c!=0",
            "degrees": "deg(A)=deg(B)=w+1",
            "counted_object": "ordered marked triple (G,A,B)",
            "coprimality": "G,A,B pairwise coprime",
            "support_reconstruction": "M=roots(G) union roots(A), E=roots(G) union roots(B)",
        },
        "known_F17_multiple_mate_regression": known_multiple_mate_packet(),
        "F17_mark_erasure_and_fixed_target_regression": marked_core_census(),
        "first_match_contract": fail_closed_owner_contract(),
        "projection_interface": projection_interface(),
        "target_results": {
            "1_common_core_determinacy": {
                "status": "OPEN",
                "proved_reduction": "for fixed (z,A,B), admissible G form a punctured prefix fibre determined by target(G)=z-target(A)",
                "finite_result": "multiplicity-one is false: the certified fixed (z,A,B) fixture has three G marks",
                "exact_nonclaim": "three does not refute an exp(o(n)) multiplicity theorem after full first-match pruning",
            },
            "2_marked_incidence_payment": {
                "status": "OPEN",
                "finite_result": "the complete F17 target-fibre top seam has 32 ordered marked triples and a functional selected-support projection with H=4,J=1",
                "missing": "an asymptotic natural-profile marked count plus rooted first-match H,J projection bounds",
            },
            "3_earlier_owner_classification": {
                "status": "OPEN",
                "missing": "paid typed projectors for every earlier actual-slope cell; structural triggers are not payments",
            },
            "4_new_obstruction": {
                "status": "NOT_ESTABLISHED",
                "missing": "an actual first-match-surviving rooted marked family with excessive distinct-slope image",
            },
        },
        "exact_nonclaims": [
            "no theorem for Q, C7, C8, or C9",
            "no deployed KoalaBear or Mersenne-31 adjacent payment",
            "no support-side triple is called an actual primitive first-match survivor",
            "no root affine relation is treated as a paid affine-fibre owner",
            "no quotient side-pair trigger is treated as a paid marked-profile owner",
            "no marked-pair or second-moment count is promoted to a distinct-slope payment",
            "the four-mate rooted star is not promoted to the complete MCA numerator",
            "the complete 32-triple raw F17 seam is not called post-first-match primitive",
            "no paper source is modified",
        ],
    }
    return add_payload_hash(certificate)


def validate(certificate: dict[str, Any]) -> None:
    require(certificate.get("schema") == "primitive_top_seam_marked_incidence.v1", "schema drift")
    require(certificate.get("status") == "PROVED_LOCAL / AUDIT / OPEN_GAP", "status drift")
    require(certificate.get("verdict") == VERDICT, "verdict drift")
    expected_hash = certificate.get("payload_sha256")
    unhashed = copy.deepcopy(certificate)
    unhashed.pop("payload_sha256", None)
    require(expected_hash == hashlib.sha256(canonical_json(unhashed).encode()).hexdigest(), "payload hash mismatch")
    require(certificate["source_anchors"] == source_anchors(), "source anchors drift")

    packet = certificate["known_F17_multiple_mate_regression"]
    require(packet["target_power_sums"] == [0, 2], "multiple-mate target drift")
    require(packet["fiber_size"] == 7 and packet["top_seam_mate_count"] == 4, "multiple-mate count drift")
    star_triples = packet["rooted_multiple_mate_star_triples"]
    require(sorted(row["A_minus_B"] for row in star_triples) == [5, 7, 10, 12],
            "constant shifts drift")
    require(all(row["pairwise_coprime"] for row in star_triples),
            "star coprimality regression failed")
    require(packet["complete_ordered_top_seam_triple_count"] == 32,
            "complete top-seam count drift")
    require(len(packet["complete_ordered_top_seam_triples"]) == 32,
            "complete top-seam record count drift")
    require(all(row["pairwise_coprime"] for row in packet["complete_ordered_top_seam_triples"]),
            "complete top-seam coprimality regression failed")
    require(packet["marked_support_S0_periodic_scales"] == [2],
            "marked-support periodicity regression drift")
    pole = packet["pole_line"]
    received_line = pole["received_line"]
    require(len(received_line["exhaustive_slope_codeword_scan"]) == 7,
            "exhaustive MCA scan count drift")
    require(received_line["g_pairwise_distinct"], "pole direction regression drift")
    require(all(row["actual_first_match_owner"] is None
                for row in pole["all_support_explanation_states"]),
            "unsupported pole-line owner assignment")
    complete_line = pole["complete_pole_line"]
    require(
        (complete_line["support_count"], complete_line["explanation_states"],
         complete_line["witness_rays"], complete_line["codeword_rays"],
         complete_line["distinct_MCA_slopes"], complete_line["slopes"])
        == (7, 7, 7, 7, 4, [2, 5, 8, 11]),
        "complete pole-line layer counts drift",
    )
    complete_scope = pole["complete_top_seam_marked_incidence"]
    require(
        (complete_scope["marked_triples_T"],
         complete_scope["ordered_full_support_pairs_P_full"],
         complete_scope["ordered_side_locator_pairs_P_side"],
         complete_scope["explanation_states"], complete_scope["witness_rays"],
         complete_scope["codeword_rays"], complete_scope["distinct_slope_image"],
         complete_scope["slopes"], complete_scope["projection_H"],
         complete_scope["projection_J"], complete_scope["incidence_edges"])
        == (32, 32, 32, 7, 7, 7, 4, [2, 5, 8, 11], 4, 1, 32),
        "complete marked-incidence projection drift",
    )
    require(complete_scope["marked_degree_by_slope"]
            == {"2": 4, "5": 10, "8": 10, "11": 8},
            "complete selected-support slope degrees drift")
    require(sorted(complete_scope["marked_degree_by_selected_support"].values())
            == [4, 4, 4, 5, 5, 5, 5],
            "complete selected-support degrees drift")
    two_endpoint_scope = pole["complete_top_seam_two_endpoint_relation"]
    require((two_endpoint_scope["projection_H"], two_endpoint_scope["projection_J"],
             two_endpoint_scope["incidence_edges"]) == (8, 2, 64),
            "complete two-endpoint relation drift")
    endpoint_scope = pole["rooted_multiple_mate_star_endpoint_incidence"]
    require(
        (endpoint_scope["marked_triples_T"], endpoint_scope["explanation_states"],
         endpoint_scope["witness_rays"], endpoint_scope["distinct_slope_image"],
         endpoint_scope["slopes"], endpoint_scope["projection_H"],
         endpoint_scope["projection_J"], endpoint_scope["incidence_edges"])
        == (4, 5, 5, 3, [2, 5, 8], 2, 2, 8),
        "rooted-star endpoint relation drift",
    )
    selected_S0 = pole["rooted_multiple_mate_star_selected_S0_projection"]
    require(
        (selected_S0["marked_triples_T"], selected_S0["explanation_states"],
         selected_S0["witness_rays"], selected_S0["distinct_slope_image"],
         selected_S0["slopes"], selected_S0["projection_H"], selected_S0["projection_J"])
        == (4, 1, 1, 1, [2], 4, 1),
        "S0-selected many-marks-to-one-ray regression drift",
    )
    reverse_mates = pole["reverse_rooted_star_selected_mate_projection"]
    require(
        (reverse_mates["marked_triples_T"], reverse_mates["witness_rays"],
         reverse_mates["distinct_slope_image"], reverse_mates["slopes"],
         reverse_mates["projection_H"], reverse_mates["projection_J"])
        == (4, 4, 2, [5, 8], 2, 1),
        "many-rays-to-one-slope regression drift",
    )
    require(pole["complete_MCA_slopes_uncovered_by_rooted_star"] == [11],
            "rooted-star missing-slope guardrail drift")
    require(pole["rooted_star_complete_slope_set_projection_H"] == 0
            and not pole["rooted_star_complete_slope_set_HJ_bound_applicable"],
            "rooted-star full-numerator guardrail drift")

    census = certificate["F17_mark_erasure_and_fixed_target_regression"]
    require(census["ordered_side_pairs"] == 704, "side-pair count drift")
    require(census["common_pullback_side_pairs"] == 0, "quotient side-pair drift")
    require(census["raw_cores_per_side_pair"] == 252, "raw core fibre drift")
    require(census["ordered_marked_triples"] == 177_408, "marked count drift")
    require(census["independent_ordered_support_pair_count"] == 177_408, "independent census drift")
    require(census["mark_erasure_projection"]["fibre_size_set_without_target"] == [252], "mark erasure drift")
    fixed = census["fixed_no_obvious_symmetry_packet"]
    require(fixed["target"] == [16, 16] and fixed["core_count"] == 3, "fixed-target core packet drift")
    require(fixed["common_pullback_scales"] == [] and fixed["side_affine_maps"] == [], "obvious owner gate drift")
    require(fixed["raw_Q_prefix_fibre_constraint"]["owner_status"] == "NOT_AN_OWNER",
            "raw Q fibre was mislabeled as an owner")
    require(fixed["raw_Q_prefix_fibre_constraint"]["coefficient_slice_equivalence_condition"]
            == "characteristic(F)>w", "Newton-equivalence condition drift")
    require(fixed["displayed_core_family_common_root_intersection"] == [],
            "planted-family intersection drift")
    require(fixed["oriented_support_A_family_common_root_intersection"] == [1, 4, 11]
            and fixed["oriented_support_B_family_common_root_intersection"] == [3, 14, 16]
            and fixed["six_support_aggregate_common_root_intersection"] == [],
            "oriented common-GCD partition regression drift")
    require(fixed["planted_owner_status"] == "UNKNOWN_MISSING_CONTEXT",
            "unsupported planted owner")
    require(not fixed["primitive_admission"], "fixed packet was incorrectly admitted as primitive")
    require(census["mark_erasure_projection"]["multiplicity_factor"] == 252,
            "mark-erasure multiplicity factor drift")
    require(all(not row["primitive_admission"] and not row["paid_owner_established"]
                for row in census["side_root_affine_transport_gate_regressions"]),
            "affine transport candidate bypassed the primitive gate")

    contract = certificate["first_match_contract"]
    require(contract == fail_closed_owner_contract(), "first-match contract drift")
    require(contract["quotient_before_primitive"] and contract["affine_candidate_before_primitive"],
            "owner precedence drift")
    require(not contract["post_first_match_marked_universe_defined"], "undefined survivor set was promoted")
    require(contract["actual_surviving_triple_count"] is None, "fabricated surviving count")
    require(all(row["state"] in OWNER_STATES for row in contract["fixed_fixture_states"]),
            "invalid owner state")
    require(any(row["state"] == "UNKNOWN_MISSING_CONTEXT" for row in contract["fixed_fixture_states"]),
            "fail-closed unknowns disappeared")
    require(not any(row["state"] == "PAID_OWNER" for row in contract["fixed_fixture_states"]),
            "fabricated paid owner")
    require(not contract["preprimitive_gate_regressions"]["periodic_support_candidate"]["primitive_admission"],
            "periodic candidate bypassed gate")
    require(not contract["preprimitive_gate_regressions"]["side_root_affine_transport_candidate"]["primitive_admission"],
            "affine candidate bypassed gate")
    require(certificate["projection_interface"] == projection_interface(),
            "projection interface drift")

    targets = certificate["target_results"]
    require(targets["1_common_core_determinacy"]["status"] == "OPEN", "target 1 overclaim")
    require(targets["2_marked_incidence_payment"]["status"] == "OPEN", "target 2 overclaim")
    require(targets["3_earlier_owner_classification"]["status"] == "OPEN", "target 3 overclaim")
    require(targets["4_new_obstruction"]["status"] == "NOT_ESTABLISHED", "target 4 overclaim")
    require(len(certificate["exact_nonclaims"]) == 9, "nonclaim ledger drift")


def tamper_selftest(certificate: dict[str, Any]) -> tuple[int, int]:
    mutations = [
        lambda x: x.__setitem__("verdict", "NO ISSUE"),
        lambda x: x["known_F17_multiple_mate_regression"].__setitem__("fiber_size", 6),
        lambda x: x["known_F17_multiple_mate_regression"].__setitem__("top_seam_mate_count", 1),
        lambda x: x["known_F17_multiple_mate_regression"]["rooted_multiple_mate_star_triples"][0].__setitem__("A_minus_B", 0),
        lambda x: x["known_F17_multiple_mate_regression"]["pole_line"]["complete_pole_line"].__setitem__("distinct_MCA_slopes", 5),
        lambda x: x["known_F17_multiple_mate_regression"]["pole_line"]["complete_top_seam_marked_incidence"].__setitem__("marked_triples_T", 4),
        lambda x: x["known_F17_multiple_mate_regression"]["pole_line"].__setitem__("complete_MCA_slopes_uncovered_by_rooted_star", []),
        lambda x: x["F17_mark_erasure_and_fixed_target_regression"].__setitem__("ordered_side_pairs", 705),
        lambda x: x["F17_mark_erasure_and_fixed_target_regression"].__setitem__("raw_cores_per_side_pair", 1),
        lambda x: x["F17_mark_erasure_and_fixed_target_regression"]["fixed_no_obvious_symmetry_packet"]["raw_Q_prefix_fibre_constraint"].__setitem__("owner_status", "PAID_OWNER"),
        lambda x: x["F17_mark_erasure_and_fixed_target_regression"]["fixed_no_obvious_symmetry_packet"].__setitem__("primitive_admission", True),
        lambda x: x["first_match_contract"]["fixed_fixture_states"][1].__setitem__("state", "PAID_OWNER"),
        lambda x: x["first_match_contract"]["fixed_fixture_states"][3].__setitem__("state", "PAID_OWNER"),
        lambda x: x["first_match_contract"]["fixed_fixture_states"][8].__setitem__("state", "NOT_APPLICABLE"),
        lambda x: x["first_match_contract"]["preprimitive_gate_regressions"]["periodic_support_candidate"].__setitem__("primitive_admission", True),
        lambda x: x["first_match_contract"].__setitem__("post_first_match_marked_universe_defined", True),
        lambda x: x["first_match_contract"].__setitem__("actual_surviving_triple_count", 3),
        lambda x: x["target_results"]["1_common_core_determinacy"].__setitem__("status", "PROVED"),
        lambda x: x["target_results"]["4_new_obstruction"].__setitem__("status", "COUNTEREXAMPLE"),
    ]
    caught = 0
    for mutate in mutations:
        candidate = copy.deepcopy(certificate)
        mutate(candidate)
        candidate = add_payload_hash(candidate)
        try:
            validate(candidate)
        except CertificateError:
            caught += 1
    return caught, len(mutations)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="compare exact output with the committed certificate")
    parser.add_argument("--tamper-selftest", action="store_true", help="prove semantic mutations are rejected")
    parser.add_argument("--print", action="store_true", dest="print_certificate", help="print the generated certificate")
    args = parser.parse_args()

    certificate = build_certificate()
    validate(certificate)
    if args.check:
        path = ROOT / CERT_REL
        require(path.exists(), f"missing certificate: {CERT_REL}")
        committed = json.loads(path.read_text(encoding="utf-8"))
        require(committed == certificate, "committed certificate differs from exact regeneration")
        print("certificate: PASS")
    if args.tamper_selftest:
        caught, total = tamper_selftest(certificate)
        require(caught == total, f"tamper self-test caught {caught}/{total}")
        print(f"tamper-selftest: PASS ({caught}/{total})")
    if args.print_certificate or not (args.check or args.tamper_selftest):
        print(json.dumps(certificate, indent=2, sort_keys=True))
    print(VERDICT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
