#!/usr/bin/env python3
"""Verify the R=2t-1 two-dimensional locator-kernel LineRay compiler."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import random
from collections import defaultdict
from math import comb
from pathlib import Path
from typing import Any, Iterable

import verify_half_distance_generic_rank_deflation as rankdef
import verify_half_distance_hankel_curve_lineray as half


BASE_COMMIT = "c35a6da31ed0905afcbaaefe4eb0f242572ebb35"
CLAIM_ID = "first-beyond-half-kernel-pencil-v1"
ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = (
    ROOT
    / "experimental/data/certificates/first-beyond-half-kernel-pencil"
    / "first_beyond_half_kernel_pencil.json"
)


class VerificationError(RuntimeError):
    """Raised when a theorem gate or pinned certificate fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def payload_digest(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


Atom = tuple[tuple[int, ...], tuple[int, ...]]
SparseMultimap = dict[tuple[int, ...], tuple[Atom, ...]]


def build_sparse_multimap(
    p: int,
    domain: tuple[int, ...],
    t: int,
    redundancy: int,
    column_weights: dict[int, int],
) -> tuple[SparseMultimap, dict[tuple[int, ...], set[tuple[int, ...]]]]:
    sparse_lists: dict[tuple[int, ...], list[Atom]] = defaultdict(list)
    spans: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
    for size in range(t + 1):
        for support in itertools.combinations(domain, size):
            spans[support] = {
                half.syndrome(
                    domain,
                    support,
                    tuple(coefficients),
                    redundancy,
                    p,
                    column_weights,
                )
                for coefficients in itertools.product(range(p), repeat=size)
            }
            amplitude_rows: Iterable[tuple[int, ...]]
            if size == 0:
                amplitude_rows = [()]
            else:
                amplitude_rows = itertools.product(range(1, p), repeat=size)
            for amplitudes_raw in amplitude_rows:
                amplitudes = tuple(amplitudes_raw)
                value = half.syndrome(
                    domain,
                    support,
                    amplitudes,
                    redundancy,
                    p,
                    column_weights,
                )
                atom = (support, amplitudes)
                require(
                    atom not in sparse_lists[value],
                    "duplicate sparse atom generated",
                )
                sparse_lists[value].append(atom)
    sparse = {
        point: tuple(sorted(atoms)) for point, atoms in sparse_lists.items()
    }
    return sparse, spans


def selected_atoms_on_line(
    p: int,
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    sparse: SparseMultimap,
    spans: dict[tuple[int, ...], set[tuple[int, ...]]],
) -> dict[int, tuple[Atom, ...]]:
    selected: dict[int, tuple[Atom, ...]] = {}
    for gamma in range(p):
        point = tuple(
            (line_base[index] + gamma * direction[index]) % p
            for index in range(len(line_base))
        )
        atoms = tuple(
            atom
            for atom in sparse.get(point, ())
            if direction not in spans[atom[0]]
        )
        if atoms:
            selected[gamma] = atoms
    return selected


def recurrence_pencil(
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    t: int,
    p: int,
) -> list[list[list[int]]]:
    return [
        [
            half.trim(
                [line_base[row + column], direction[row + column]], p
            )
            for column in range(t + 1)
        ]
        for row in range(t - 1)
    ]


def maximal_pivot(
    pencil: list[list[list[int]]], t: int, p: int
) -> list[int]:
    for columns in itertools.combinations(range(t + 1), t - 1):
        minor = [
            [row[column] for column in columns]
            for row in pencil
        ]
        determinant = half.determinant_poly(minor, p)
        if determinant != [0]:
            require(
                len(determinant) - 1 <= t - 1,
                "maximal pivot degree exceeded t-1",
            )
            return determinant
    return [0]


def pair_determinants(
    pencil: list[list[list[int]]],
    domain: tuple[int, ...],
    t: int,
    p: int,
) -> dict[tuple[int, int], list[int]]:
    determinants: dict[tuple[int, int], list[int]] = {}
    for first, second in itertools.combinations(domain, 2):
        evaluation_rows = [
            [[pow(root, column, p)] for column in range(t + 1)]
            for root in (first, second)
        ]
        determinant = half.determinant_poly(
            pencil + evaluation_rows, p
        )
        require(
            len(determinant) - 1 <= t - 1,
            "stacked pair determinant degree exceeded t-1",
        )
        determinants[(first, second)] = determinant
    return determinants


def fixed_kernel_roots(
    domain: tuple[int, ...],
    determinants: dict[tuple[int, int], list[int]],
) -> tuple[int, ...]:
    return tuple(
        x
        for x in domain
        if all(
            determinants[tuple(sorted((x, y)))] == [0]
            for y in domain
            if y != x
        )
    )


def specialized_recurrence(
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    gamma: int,
    t: int,
    p: int,
) -> list[list[int]]:
    return [
        [
            (
                line_base[row + column]
                + gamma * direction[row + column]
            )
            % p
            for column in range(t + 1)
        ]
        for row in range(t - 1)
    ]


def audit_lower_strata(
    p: int,
    domain: tuple[int, ...],
    t: int,
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    selected: dict[int, tuple[Atom, ...]],
) -> dict[str, int]:
    lower = [
        (gamma, atom)
        for gamma, atoms in selected.items()
        for atom in atoms
        if len(atom[0]) < t
    ]
    by_gamma: dict[int, list[Atom]] = defaultdict(list)
    for gamma, atom in lower:
        by_gamma[gamma].append(atom)
    require(
        all(len(atoms) == 1 for atoms in by_gamma.values()),
        "two lower-weight errors share one syndrome",
    )

    u = t - 1
    if u == 0:
        require(len(lower) <= 1, "t=1 retained two zero errors")
        return {
            "pairs": len(lower),
            "generic_rank": 0,
            "lower_minor_roots": len(lower),
            "top_lower_pairs": 0,
            "deflation_families": 0,
            "fixed_root_families": 0,
        }

    rho, minor = rankdef.generic_hankel_rank(
        line_base, direction, u, p
    )
    below = []
    exact = []
    for gamma, (support, _) in lower:
        specialized = [
            [
                (
                    line_base[row + column]
                    + gamma * direction[row + column]
                )
                % p
                for column in range(u)
            ]
            for row in range(u)
        ]
        rank = rankdef.numeric_rank(specialized, p)
        require(rank == len(support), "lower Hankel rank/weight mismatch")
        require(rank <= rho, "lower specialization exceeded generic rank")
        if len(support) < rho:
            below.append(gamma)
        elif len(support) == rho:
            exact.append((gamma, support))

    require(
        all(half.poly_eval(minor, gamma, p) == 0 for gamma in below),
        "lower rank-drop parameter missed the chosen minor",
    )
    require(
        len(below) <= len(minor) - 1 <= rho,
        "lower rank-drop charge failed",
    )

    deflations = 0
    fixed = 0
    top_cap = 0
    if rho > 0 and exact:
        row = rankdef.deflated_exact_weight_audit(
            p,
            domain,
            line_base,
            direction,
            rho,
            exact,
        )
        deflations = 1
        fixed = int(row["fixed_roots"] > 0)
        top_cap = len(domain) - row["fixed_roots"]
        require(len(exact) <= top_cap, "lower top chart exceeded N-g")

    require(
        len(lower) <= len(domain) + rho,
        "banked lower-weight N+rho bound failed",
    )
    return {
        "pairs": len(lower),
        "generic_rank": rho,
        "lower_minor_roots": len(below),
        "top_lower_pairs": len(exact),
        "deflation_families": deflations,
        "fixed_root_families": fixed,
    }


def audit_top_stratum(
    p: int,
    domain: tuple[int, ...],
    t: int,
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    selected: dict[int, tuple[Atom, ...]],
) -> dict[str, int]:
    top = [
        (gamma, atom)
        for gamma, atoms in selected.items()
        for atom in atoms
        if len(atom[0]) == t
    ]
    if not top:
        return {
            "pairs": 0,
            "slopes": 0,
            "same_slope_excess": 0,
            "pencil_families": 0,
            "good_pair_incidences": 0,
            "root_capacity": 0,
            "good_domain_pairs": 0,
            "fixed_kernel_roots": 0,
        }
    require(t >= 2, "a transverse t=1 top atom survived")

    pencil = recurrence_pencil(line_base, direction, t, p)
    pivot = maximal_pivot(pencil, t, p)
    require(pivot != [0], "actual top pair but generic rank below t-1")
    determinants = pair_determinants(pencil, domain, t, p)
    fixed = fixed_kernel_roots(domain, determinants)
    require(
        not fixed,
        "formal common kernel root coexists with an actual top error",
    )
    good = {
        pair: polynomial
        for pair, polynomial in determinants.items()
        if polynomial != [0]
    }
    require(good, "top pencil has no nonzero pair determinant")

    incidence_keys: set[tuple[int, tuple[int, int]]] = set()
    incidences = 0
    top_slopes = {gamma for gamma, _ in top}
    supports_by_gamma: dict[int, list[tuple[int, ...]]] = defaultdict(list)
    for gamma, (support, _) in top:
        supports_by_gamma[gamma].append(support)
        locator = half.constant_locator(support, p)
        specialized = specialized_recurrence(
            line_base, direction, gamma, t, p
        )
        require(
            rankdef.numeric_rank(specialized, p) == t - 1,
            "actual top recurrence rank is not t-1",
        )
        require(
            all(
                sum(row[column] * locator[column] for column in range(t + 1))
                % p
                == 0
                for row in specialized
            ),
            "actual top locator missed the recurrence kernel",
        )
        direction_recurrence = [
            sum(
                direction[row + column] * locator[column]
                for column in range(t + 1)
            )
            % p
            for row in range(t - 1)
        ]
        require(
            any(direction_recurrence),
            "retained top support became common to the syndrome line",
        )

        support_pairs = list(itertools.combinations(support, 2))
        require(
            all(
                half.poly_eval(determinants[pair], gamma, p) == 0
                for pair in support_pairs
            ),
            "actual top locator missed a stacked determinant root",
        )
        good_inside = [pair for pair in support_pairs if pair in good]
        require(
            len(good_inside) >= t - 1,
            "top support has too few independent evaluation pairs",
        )
        for pair in good_inside:
            key = (gamma, pair)
            require(
                key not in incidence_keys,
                "same-slope top supports reused one root pair",
            )
            incidence_keys.add(key)
        incidences += len(good_inside)

    for supports in supports_by_gamma.values():
        for first, second in itertools.combinations(supports, 2):
            require(
                set(first).isdisjoint(second),
                "same-syndrome top supports are not disjoint",
            )

    capacity = 0
    for polynomial in good.values():
        roots = sum(
            half.poly_eval(polynomial, gamma, p) == 0
            for gamma in range(p)
        )
        require(
            roots <= len(polynomial) - 1,
            "stacked determinant has too many field roots",
        )
        capacity += roots
    require(
        len(top) * (t - 1) <= incidences <= capacity,
        "top good-pair incidence double count failed",
    )
    require(
        capacity <= comb(len(domain), 2) * (t - 1),
        "top determinant root capacity exceeded the theorem budget",
    )
    require(
        len(top) <= comb(len(domain), 2),
        "top all-pair binomial bound failed",
    )
    return {
        "pairs": len(top),
        "slopes": len(top_slopes),
        "same_slope_excess": len(top) - len(top_slopes),
        "pencil_families": 1,
        "good_pair_incidences": incidences,
        "root_capacity": capacity,
        "good_domain_pairs": len(good),
        "fixed_kernel_roots": 0,
    }


def audit_line(
    p: int,
    domain: tuple[int, ...],
    t: int,
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    sparse: SparseMultimap,
    spans: dict[tuple[int, ...], set[tuple[int, ...]]],
) -> dict[str, int]:
    selected = selected_atoms_on_line(
        p, line_base, direction, sparse, spans
    )
    lower = audit_lower_strata(
        p, domain, t, line_base, direction, selected
    )
    top = audit_top_stratum(
        p, domain, t, line_base, direction, selected
    )
    selected_pairs = sum(len(atoms) for atoms in selected.values())
    selected_slopes = len(selected)
    require(
        selected_pairs == lower["pairs"] + top["pairs"],
        "lower/top pair partition mismatch",
    )
    require(
        selected_pairs <= comb(len(domain), 2) + len(domain) + t - 1,
        "first-beyond-half all-pair bound failed",
    )
    return {
        "pairs": selected_pairs,
        "slopes": selected_slopes,
        "lower_pairs": lower["pairs"],
        "top_pairs": top["pairs"],
        "top_slopes": top["slopes"],
        "same_slope_top_excess": top["same_slope_excess"],
        "lower_generic_rank": lower["generic_rank"],
        "lower_minor_roots": lower["lower_minor_roots"],
        "lower_deflation_families": lower["deflation_families"],
        "lower_fixed_root_families": lower["fixed_root_families"],
        "top_pencil_families": top["pencil_families"],
        "good_pair_incidences": top["good_pair_incidences"],
        "root_capacity": top["root_capacity"],
    }


def summarize_lines(
    p: int,
    domain: tuple[int, ...],
    t: int,
    column_weights: dict[int, int],
    lines: Iterable[tuple[tuple[int, ...], tuple[int, ...]]],
    mode: str,
) -> dict[str, Any]:
    redundancy = 2 * t - 1
    sparse, spans = build_sparse_multimap(
        p, domain, t, redundancy, column_weights
    )
    line_count = 0
    pair_total = 0
    slope_total = 0
    lower_total = 0
    top_total = 0
    top_slope_total = 0
    same_slope_excess = 0
    maximum_pairs = 0
    maximum_slopes = 0
    maximum_top_pairs = 0
    maximum_same_slope_multiplicity = 0
    pencil_families = 0
    good_incidences = 0
    root_capacity = 0
    deflations = 0
    lower_fixed = 0
    rank_histogram: dict[int, int] = defaultdict(int)

    for line_base, direction in lines:
        result = audit_line(
            p,
            domain,
            t,
            line_base,
            direction,
            sparse,
            spans,
        )
        line_count += 1
        pair_total += result["pairs"]
        slope_total += result["slopes"]
        lower_total += result["lower_pairs"]
        top_total += result["top_pairs"]
        top_slope_total += result["top_slopes"]
        same_slope_excess += result["same_slope_top_excess"]
        maximum_pairs = max(maximum_pairs, result["pairs"])
        maximum_slopes = max(maximum_slopes, result["slopes"])
        maximum_top_pairs = max(maximum_top_pairs, result["top_pairs"])
        pencil_families += result["top_pencil_families"]
        good_incidences += result["good_pair_incidences"]
        root_capacity += result["root_capacity"]
        deflations += result["lower_deflation_families"]
        lower_fixed += result["lower_fixed_root_families"]
        rank_histogram[result["lower_generic_rank"]] += 1
        selected = selected_atoms_on_line(
            p, line_base, direction, sparse, spans
        )
        maximum_same_slope_multiplicity = max(
            maximum_same_slope_multiplicity,
            max((len(atoms) for atoms in selected.values()), default=0),
        )

    return {
        "mode": mode,
        "p": p,
        "domain": list(domain),
        "n": len(domain),
        "t": t,
        "redundancy": redundancy,
        "lines": line_count,
        "transverse_pairs": pair_total,
        "transverse_slopes": slope_total,
        "lower_pairs": lower_total,
        "top_pairs": top_total,
        "top_slopes": top_slope_total,
        "same_slope_top_excess": same_slope_excess,
        "maximum_pairs_on_line": maximum_pairs,
        "maximum_slopes_on_line": maximum_slopes,
        "maximum_top_pairs_on_line": maximum_top_pairs,
        "maximum_same_slope_multiplicity": maximum_same_slope_multiplicity,
        "top_pair_bound": comb(len(domain), 2),
        "all_pair_bound": comb(len(domain), 2) + len(domain) + t - 1,
        "top_pencil_families": pencil_families,
        "good_pair_incidences": good_incidences,
        "root_capacity": root_capacity,
        "lower_deflation_families": deflations,
        "lower_fixed_root_families": lower_fixed,
        "lower_generic_rank_histogram": {
            str(rank): count
            for rank, count in sorted(rank_histogram.items())
        },
    }


def exhaustive_lines(
    p: int, dimension: int
) -> Iterable[tuple[tuple[int, ...], tuple[int, ...]]]:
    for direction in half.normalized_directions(p, dimension):
        pivot = next(index for index, value in enumerate(direction) if value)
        free = [index for index in range(dimension) if index != pivot]
        for values in itertools.product(range(p), repeat=dimension - 1):
            base_list = [0] * dimension
            for index, value in zip(free, values, strict=True):
                base_list[index] = value
            yield tuple(base_list), direction


def sampled_lines(
    p: int,
    domain: tuple[int, ...],
    t: int,
    column_weights: dict[int, int],
    count: int,
    seed: int,
) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    redundancy = 2 * t - 1
    sparse, _ = build_sparse_multimap(
        p, domain, t, redundancy, column_weights
    )
    top_points = sorted(
        point
        for point, atoms in sparse.items()
        if any(len(atom[0]) == t for atom in atoms)
    )
    require(len(top_points) >= 2, "not enough top syndromes to sample")
    rng = random.Random(seed)
    lines: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    pair_target = count * 3 // 5
    while len(lines) < pair_target:
        first = top_points[rng.randrange(len(top_points))]
        second = top_points[rng.randrange(len(top_points))]
        if first != second:
            lines.add(half.canonical_line(first, second, p))
    directions = half.normalized_directions(p, redundancy)
    while len(lines) < count:
        direction = directions[rng.randrange(len(directions))]
        pivot = next(index for index, value in enumerate(direction) if value)
        base = tuple(
            0 if index == pivot else rng.randrange(p)
            for index in range(redundancy)
        )
        lines.add((base, direction))
    return sorted(lines)


def sharp_top_fixture() -> dict[str, Any]:
    p = 11
    domain = (0, 1, 2, 3, 4)
    t = 2
    line_base = (1, 0, 7)
    direction = (5, 1, 9)
    weights = {x: 1 for x in domain}
    sparse, spans = build_sparse_multimap(
        p, domain, t, 2 * t - 1, weights
    )
    result = audit_line(
        p,
        domain,
        t,
        line_base,
        direction,
        sparse,
        spans,
    )
    selected = selected_atoms_on_line(
        p, line_base, direction, sparse, spans
    )
    supports = sorted(
        atom[0]
        for atoms in selected.values()
        for atom in atoms
        if len(atom[0]) == t
    )
    require(
        result["top_pairs"] == comb(len(domain), 2),
        "sharp fixture no longer attains every domain pair",
    )
    require(
        supports == list(itertools.combinations(domain, 2)),
        "sharp fixture support census changed",
    )
    require(result["lower_pairs"] == 0, "sharp fixture gained lower pairs")
    return {
        "p": p,
        "domain": list(domain),
        "n": len(domain),
        "t": t,
        "line_base": list(line_base),
        "direction": list(direction),
        "top_pairs": result["top_pairs"],
        "top_slopes": result["top_slopes"],
        "lower_pairs": result["lower_pairs"],
        "top_pair_bound": comb(len(domain), 2),
        "all_domain_pairs_realized": True,
    }


def same_slope_sharp_fixture() -> dict[str, Any]:
    p = 7
    domain = tuple(range(p))
    t = 2
    line_base = (0, 1, 0)
    direction = (0, 0, 1)
    weights = {x: 1 for x in domain}
    sparse, spans = build_sparse_multimap(
        p, domain, t, 2 * t - 1, weights
    )
    result = audit_line(
        p,
        domain,
        t,
        line_base,
        direction,
        sparse,
        spans,
    )
    selected = selected_atoms_on_line(
        p, line_base, direction, sparse, spans
    )
    top_by_slope = {
        gamma: sorted(
            atom[0] for atom in atoms if len(atom[0]) == t
        )
        for gamma, atoms in selected.items()
    }
    top_by_slope = {
        gamma: supports
        for gamma, supports in top_by_slope.items()
        if supports
    }
    flattened = sorted(
        support
        for supports in top_by_slope.values()
        for support in supports
    )
    require(
        result["top_pairs"] == comb(len(domain), 2),
        "same-slope fixture lost the top all-pair equality",
    )
    require(
        flattened == list(itertools.combinations(domain, 2)),
        "same-slope fixture no longer realizes every domain pair",
    )
    require(
        len(top_by_slope) == p
        and all(len(supports) == 3 for supports in top_by_slope.values()),
        "same-slope fixture lost its seven near-perfect matchings",
    )
    require(result["lower_pairs"] == 0, "same-slope fixture gained lower pairs")
    return {
        "p": p,
        "domain": list(domain),
        "n": len(domain),
        "t": t,
        "line_base": list(line_base),
        "direction": list(direction),
        "top_pairs": result["top_pairs"],
        "top_slopes": result["top_slopes"],
        "pairs_per_slope": sorted(
            len(supports) for supports in top_by_slope.values()
        ),
        "lower_pairs": result["lower_pairs"],
        "top_pair_bound": comb(len(domain), 2),
        "all_domain_pairs_realized": True,
        "near_perfect_matching_factorization": True,
    }


def fixed_kernel_fixture() -> dict[str, Any]:
    p = 7
    domain = tuple(range(p))
    t = 3
    weights = {x: (2 * x + 1) % p or 1 for x in domain}
    support = (0, 1)
    line_base = half.syndrome(
        domain, support, (1, 2), 2 * t - 1, p, weights
    )
    direction = half.syndrome(
        domain, support, (2, 1), 2 * t - 1, p, weights
    )
    require(any(direction), "fixed-kernel fixture direction vanished")
    sparse, spans = build_sparse_multimap(
        p, domain, t, 2 * t - 1, weights
    )
    selected = selected_atoms_on_line(
        p, line_base, direction, sparse, spans
    )
    pencil = recurrence_pencil(line_base, direction, t, p)
    pivot = maximal_pivot(pencil, t, p)
    require(pivot != [0], "fixed-kernel fixture lost generic full row rank")
    determinants = pair_determinants(pencil, domain, t, p)
    fixed = fixed_kernel_roots(domain, determinants)
    top = [
        atom
        for atoms in selected.values()
        for atom in atoms
        if len(atom[0]) == t
    ]
    require(set(support) <= set(fixed), "common support roots not detected")
    require(not top, "formal fixed kernel retained an exact top error")
    return {
        "p": p,
        "domain": list(domain),
        "n": len(domain),
        "t": t,
        "common_support": list(support),
        "fixed_kernel_roots": list(fixed),
        "transverse_top_pairs": len(top),
        "generic_pivot_degree": len(pivot) - 1,
    }


def build_payload() -> dict[str, Any]:
    exhaustive_specs = [
        (3, tuple(range(3)), 2),
        (5, (0, 1, 2), 2),
        (5, tuple(range(5)), 2),
        (7, (0, 1, 2, 3, 4), 2),
        (7, tuple(range(7)), 2),
        (11, (0, 1, 2, 3, 4), 2),
        (13, (0, 1, 2, 3, 4), 2),
        (17, (0, 1, 2, 3, 4), 2),
    ]
    exhaustive = []
    for p, domain, t in exhaustive_specs:
        weights = {x: 1 for x in domain}
        dimension = 2 * t - 1
        row = summarize_lines(
            p,
            domain,
            t,
            weights,
            exhaustive_lines(p, dimension),
            "exhaustive",
        )
        expected = p ** (dimension - 1) * (
            (p**dimension - 1) // (p - 1)
        )
        require(row["lines"] == expected, "affine line census mismatch")
        exhaustive.append(row)

    sampled_specs = [
        (7, tuple(range(7)), 3, 8000),
        (11, (0, 1, 2, 3, 4), 3, 10000),
        (13, (0, 1, 2, 3, 4), 3, 10000),
    ]
    sampled = []
    for p, domain, t, count in sampled_specs:
        weights = {x: (3 * x + 2) % p or 1 for x in domain}
        lines = sampled_lines(
            p,
            domain,
            t,
            weights,
            count,
            20260714 + 1000 * p + len(domain),
        )
        sampled.append(
            summarize_lines(
                p, domain, t, weights, lines, "deterministic-sample"
            )
        )

    sharp = sharp_top_fixture()
    same_slope_sharp = same_slope_sharp_fixture()
    fixed = fixed_kernel_fixture()
    all_rows = exhaustive + sampled
    return {
        "schema_version": 1,
        "claim_id": CLAIM_ID,
        "base_commit": BASE_COMMIT,
        "status": "PROVED_AUDIT_WITH_UNPROVED_LEAN_TARGET",
        "hard_input": "3_first_beyond_half_distance_R_equals_2t_minus_1",
        "theorem": {
            "dimension_range": "N>=R=2t-1",
            "top_all_pair_bound": "|P_t|<=binom(N,2)",
            "lower_all_pair_bound": "|P_<t|<=N+rho<=N+t-1",
            "complete_all_pair_bound": (
                "|P|<=binom(N,2)+N+rho"
                "<=binom(N+1,2)+t-1"
            ),
            "mca_ca_numerator_bound": "same_as_complete_all_pair_bound",
        },
        "exhaustive_grids": exhaustive,
        "sampled_weight_three_grids": sampled,
        "sharp_top_fixture": sharp,
        "same_slope_sharp_fixture": same_slope_sharp,
        "fixed_kernel_fixture": fixed,
        "totals": {
            "audited_lines": sum(row["lines"] for row in all_rows),
            "transverse_pairs": sum(
                row["transverse_pairs"] for row in all_rows
            ),
            "transverse_slopes": sum(
                row["transverse_slopes"] for row in all_rows
            ),
            "top_pairs": sum(row["top_pairs"] for row in all_rows),
            "lower_pairs": sum(row["lower_pairs"] for row in all_rows),
            "top_pencil_families": sum(
                row["top_pencil_families"] for row in all_rows
            ),
            "good_pair_incidences": sum(
                row["good_pair_incidences"] for row in all_rows
            ),
            "root_capacity": sum(
                row["root_capacity"] for row in all_rows
            ),
            "lower_deflation_families": sum(
                row["lower_deflation_families"] for row in all_rows
            ),
            "same_slope_top_excess": sum(
                row["same_slope_top_excess"] for row in all_rows
            ),
        },
        "nonclaims": [
            "no_bound_for_R_less_than_2t_minus_1",
            "no_claim_that_the_complete_bound_is_exact",
            "no_atlas_or_deployed_row_movement",
            "no_priority_claim_over_existing_half_distance_literature",
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
    bad["theorem"]["top_all_pair_bound"] = "|P_t|<=N"
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["exhaustive_grids"][5]["maximum_top_pairs_on_line"] -= 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["sharp_top_fixture"]["top_pairs"] -= 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["same_slope_sharp_fixture"]["top_slopes"] += 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["fixed_kernel_fixture"]["transverse_top_pairs"] += 1
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
        "FIRST_BEYOND_HALF_KERNEL_PENCIL_PASS "
        f"lines={totals['audited_lines']} "
        f"pairs={totals['transverse_pairs']} "
        f"top={totals['top_pairs']} "
        f"pencils={totals['top_pencil_families']} "
        f"incidences={totals['good_pair_incidences']} "
        f"same_slope={totals['same_slope_top_excess']}"
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
            "FIRST_BEYOND_HALF_KERNEL_PENCIL_TAMPER_PASS "
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
