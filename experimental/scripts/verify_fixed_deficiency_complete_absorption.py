#!/usr/bin/env python3
"""Verify sharp complete-pair absorption at every fixed deficiency."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
from collections import defaultdict
from math import comb
from pathlib import Path
from typing import Any, Iterable

import verify_first_beyond_half_kernel_pencil as first
import verify_fixed_deficiency_kernel_minor_compiler as fixed
import verify_half_distance_generic_rank_deflation as rankdef
import verify_half_distance_hankel_curve_lineray as half


BASE_COMMIT = "c35a6da31ed0905afcbaaefe4eb0f242572ebb35"
CLAIM_ID = "fixed-deficiency-complete-absorption-v1"
ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = (
    ROOT
    / "experimental/data/certificates/fixed-deficiency-complete-absorption"
    / "fixed_deficiency_complete_absorption.json"
)


class VerificationError(RuntimeError):
    """Raised when a theorem gate or certificate check fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def payload_digest(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def selected_pairs(
    selected: dict[int, tuple[first.Atom, ...]],
) -> list[tuple[int, tuple[int, ...]]]:
    return [
        (gamma, atom[0])
        for gamma, atoms in selected.items()
        for atom in atoms
    ]


def determinant_root_capacity(
    determinants: dict[tuple[int, ...], list[int]],
    row_count: int,
    p: int,
) -> int:
    capacity = 0
    for polynomial in determinants.values():
        roots = sum(
            half.poly_eval(polynomial, gamma, p) == 0
            for gamma in range(p)
        )
        require(
            roots <= len(polynomial) - 1 <= row_count,
            "top stacked minor exceeded its root capacity",
        )
        capacity += roots
    return capacity


def complete_absorption_audit(
    p: int,
    domain: tuple[int, ...],
    t: int,
    deficiency: int,
    line_base: tuple[int, ...],
    direction: tuple[int, ...],
    sparse: first.SparseMultimap,
    spans: dict[tuple[int, ...], set[tuple[int, ...]]],
) -> dict[str, int | str | dict[str, int]]:
    redundancy = 2 * t - deficiency
    row_count = t - deficiency
    kernel_dimension = deficiency + 1
    require(
        1 <= deficiency < t
        and len(domain) >= redundancy
        and row_count + kernel_dimension == t + 1,
        "invalid fixed-deficiency slice",
    )
    selected = first.selected_atoms_on_line(
        p, line_base, direction, sparse, spans
    )
    pairs = selected_pairs(selected)
    pair_count = len(pairs)
    complete_bound = comb(len(domain), kernel_dimension)
    weights: dict[str, int] = defaultdict(int)
    for _, support in pairs:
        weights[str(len(support))] += 1
    if not pairs:
        return {
            "pairs": 0,
            "slopes": 0,
            "branch": "empty",
            "incidences": 0,
            "capacity": 0,
            "good_bases": 0,
            "fixed_roots": 0,
            "minimum_chargeable": 0,
            "same_slope_excess": 0,
            "weight_histogram": {},
        }

    pencil = fixed.recurrence_pencil(
        line_base, direction, redundancy, t, p
    )
    pivot = fixed.maximal_pivot(pencil, t, p)
    if pivot == [0]:
        require(
            all(len(support) <= row_count - 1 for _, support in pairs),
            "generic top-rank drop retained too much support",
        )
        core = fixed.audit_half_core(
            p,
            domain,
            row_count - 1,
            line_base,
            direction,
            selected,
        )
        require(core["pairs"] == pair_count, "rank-drop fallback lost a pair")
        require(
            pair_count
            <= len(domain) + row_count - 1
            <= complete_bound,
            "rank-drop fallback exceeded the top binomial",
        )
        return {
            "pairs": pair_count,
            "slopes": len(selected),
            "branch": "generic-rank-deficient",
            "incidences": 0,
            "capacity": 0,
            "good_bases": 0,
            "fixed_roots": 0,
            "minimum_chargeable": 0,
            "same_slope_excess": pair_count - len(selected),
            "weight_histogram": dict(sorted(weights.items())),
        }

    determinants = fixed.stacked_determinants(
        pencil,
        domain,
        t,
        kernel_dimension,
        p,
    )
    good = {
        roots: polynomial
        for roots, polynomial in determinants.items()
        if polynomial != [0]
    }
    fixed_roots = fixed.fixed_kernel_roots(domain, set(good))

    for gamma, support in pairs:
        specialized = fixed.specialized_recurrence(
            line_base,
            direction,
            gamma,
            redundancy,
            t,
            p,
        )
        require(
            rankdef.numeric_rank(specialized, p)
            == min(len(support), row_count),
            "specialized top rank/support identity failed",
        )

    if fixed_roots:
        x = fixed_roots[0]
        for _, support in pairs:
            if x in support:
                require(
                    len(support) <= row_count,
                    "fixed-root branch retained too much support through x",
                )
            else:
                require(
                    len(support) <= row_count - 1,
                    "fixed-root branch retained too much support away from x",
                )
        core = fixed.audit_half_core(
            p,
            domain,
            row_count,
            line_base,
            direction,
            selected,
        )
        require(core["pairs"] == pair_count, "fixed-root fallback lost a pair")
        if row_count == 1 and len(domain) == t + 1:
            require(
                line_base in spans[(x,)] and direction in spans[(x,)],
                "minimal fixed-root edge did not lie in its column span",
            )
            require(
                all(not support for _, support in pairs) and pair_count <= 1,
                "minimal fixed-root edge retained a nonzero transverse error",
            )
        else:
            require(
                pair_count
                <= len(domain) + row_count
                <= complete_bound,
                "fixed-root fallback exceeded the top binomial",
            )
        return {
            "pairs": pair_count,
            "slopes": len(selected),
            "branch": "formal-fixed-root",
            "incidences": 0,
            "capacity": 0,
            "good_bases": len(good),
            "fixed_roots": len(fixed_roots),
            "minimum_chargeable": 0,
            "same_slope_excess": pair_count - len(selected),
            "weight_histogram": dict(sorted(weights.items())),
        }

    require(good, "loopless top evaluation matroid has no basis")
    require(
        len(good) >= len(domain) - kernel_dimension + 1,
        "loopless matroid has too few bases",
    )
    incidence_keys: set[tuple[int, tuple[int, ...]]] = set()
    incidences = 0
    minimum_chargeable: int | None = None
    good_sets = {
        roots: set(roots)
        for roots in good
    }
    for gamma, support in pairs:
        support_set = set(support)
        slack = t - len(support)
        required_rank = max(0, kernel_dimension - slack)
        restriction_rank = max(
            len(roots_set & support_set)
            for roots_set in good_sets.values()
        )
        require(
            restriction_rank >= required_rank,
            "transverse support lost the required top-kernel rank",
        )
        chargeable = [
            roots
            for roots, roots_set in good_sets.items()
            if len(roots_set - support_set) <= slack
        ]
        require(
            len(chargeable) >= row_count,
            "support has too few chargeable top-kernel bases",
        )
        minimum_chargeable = (
            len(chargeable)
            if minimum_chargeable is None
            else min(minimum_chargeable, len(chargeable))
        )
        specialized = fixed.specialized_recurrence(
            line_base,
            direction,
            gamma,
            redundancy,
            t,
            p,
        )
        for roots in chargeable:
            extra = tuple(x for x in roots if x not in support_set)
            padded_locator = half.constant_locator(
                tuple(support) + extra, p
            )
            padded_locator += [0] * (t + 1 - len(padded_locator))
            require(
                all(
                    sum(
                        row[column] * padded_locator[column]
                        for column in range(t + 1)
                    )
                    % p
                    == 0
                    for row in specialized
                ),
                "chargeable padded locator missed the top recurrence",
            )
            require(
                half.poly_eval(determinants[roots], gamma, p) == 0,
                "chargeable basis missed its stacked-minor root",
            )
            key = (gamma, roots)
            require(
                key not in incidence_keys,
                "two same-slope errors reused one top-kernel basis",
            )
            incidence_keys.add(key)
        incidences += len(chargeable)

    capacity = determinant_root_capacity(good, row_count, p)
    require(
        pair_count * row_count <= incidences <= capacity,
        "complete fixed-deficiency incidence count failed",
    )
    require(
        capacity <= complete_bound * row_count,
        "top-kernel root capacity exceeded the binomial budget",
    )
    require(
        pair_count <= complete_bound,
        "fixed-deficiency complete absorption bound failed",
    )
    return {
        "pairs": pair_count,
        "slopes": len(selected),
        "branch": "loopless-full-rank",
        "incidences": incidences,
        "capacity": capacity,
        "good_bases": len(good),
        "fixed_roots": 0,
        "minimum_chargeable": minimum_chargeable or 0,
        "same_slope_excess": pair_count - len(selected),
        "weight_histogram": dict(sorted(weights.items())),
    }


def summarize_grid(
    p: int,
    domain: tuple[int, ...],
    t: int,
    deficiency: int,
    mode: str,
    count: int | None = None,
) -> dict[str, Any]:
    redundancy = 2 * t - deficiency
    kernel_dimension = deficiency + 1
    row_count = t - deficiency
    weights = {x: (2 * x + 1) % p or 1 for x in domain}
    sparse, spans = first.build_sparse_multimap(
        p, domain, t, redundancy, weights
    )
    if mode == "exhaustive":
        lines: Iterable[tuple[tuple[int, ...], tuple[int, ...]]] = (
            first.exhaustive_lines(p, redundancy)
        )
    else:
        require(count is not None, "sample count missing")
        lines = fixed.make_sampled_lines(
            p,
            redundancy,
            sparse,
            t,
            count,
            20260716 + p * 10000 + t * 100 + deficiency,
        )

    line_count = 0
    pair_total = 0
    slope_total = 0
    incidence_total = 0
    capacity_total = 0
    same_slope = 0
    fixed_root_lines = 0
    mixed_weight_lines = 0
    maximum_pairs = 0
    minimum_slack = None
    minimum_chargeable = None
    branches: dict[str, int] = defaultdict(int)
    weight_histogram: dict[str, int] = defaultdict(int)
    for line_base, direction in lines:
        result = complete_absorption_audit(
            p,
            domain,
            t,
            deficiency,
            line_base,
            direction,
            sparse,
            spans,
        )
        line_count += 1
        pair_total += int(result["pairs"])
        slope_total += int(result["slopes"])
        incidence_total += int(result["incidences"])
        capacity_total += int(result["capacity"])
        same_slope += int(result["same_slope_excess"])
        fixed_root_lines += int(result["fixed_roots"]) > 0
        maximum_pairs = max(maximum_pairs, int(result["pairs"]))
        slack = comb(len(domain), kernel_dimension) - int(result["pairs"])
        minimum_slack = slack if minimum_slack is None else min(minimum_slack, slack)
        branches[str(result["branch"])] += 1
        row_weights = result["weight_histogram"]
        require(isinstance(row_weights, dict), "weight histogram changed type")
        mixed_weight_lines += len(row_weights) >= 2
        for weight, amount in row_weights.items():
            weight_histogram[str(weight)] += int(amount)
        charged = int(result["minimum_chargeable"])
        if charged:
            minimum_chargeable = (
                charged
                if minimum_chargeable is None
                else min(minimum_chargeable, charged)
            )
    if mode == "exhaustive":
        expected = p ** (redundancy - 1) * (
            (p**redundancy - 1) // (p - 1)
        )
        require(line_count == expected, "affine line census mismatch")
    return {
        "mode": mode,
        "p": p,
        "domain": list(domain),
        "n": len(domain),
        "t": t,
        "deficiency": deficiency,
        "redundancy": redundancy,
        "row_count": row_count,
        "kernel_dimension": kernel_dimension,
        "lines": line_count,
        "transverse_pairs": pair_total,
        "transverse_slopes": slope_total,
        "same_slope_excess": same_slope,
        "chargeable_incidences": incidence_total,
        "root_capacity": capacity_total,
        "maximum_pairs_on_line": maximum_pairs,
        "complete_binomial_bound": comb(len(domain), kernel_dimension),
        "minimum_bound_slack": minimum_slack,
        "minimum_chargeable_on_loopless_line": minimum_chargeable,
        "fixed_root_lines": fixed_root_lines,
        "mixed_weight_lines": mixed_weight_lines,
        "branch_histogram": dict(sorted(branches.items())),
        "weight_histogram": dict(sorted(weight_histogram.items())),
    }


def canonical_lagrange_fixture(
    deficiency: int,
    *,
    p: int = 7,
    domain: tuple[int, ...] | None = None,
) -> dict[str, Any]:
    if domain is None:
        domain = tuple(range(p))
    t = deficiency + 1
    redundancy = t + 1
    kernel_dimension = deficiency + 1
    line_base = tuple(
        1 if index == t - 1 else 0
        for index in range(redundancy)
    )
    direction = tuple(
        1 if index == t else 0
        for index in range(redundancy)
    )
    require(
        all(
            any(
                (line_base[index] + gamma * direction[index]) % p
                for index in range(redundancy)
            )
            for gamma in range(p)
        ),
        "canonical line acquired a zero-error parameter",
    )
    selected: list[tuple[int, tuple[int, ...]]] = []
    slope_histogram: dict[int, int] = defaultdict(int)
    for support in itertools.combinations(domain, t):
        amplitudes = []
        for x in support:
            denominator = 1
            for y in support:
                if y != x:
                    denominator = denominator * (x - y) % p
            amplitudes.append(pow(denominator, -1, p))
        moments = tuple(
            sum(
                amplitude * pow(x, degree, p)
                for x, amplitude in zip(support, amplitudes, strict=True)
            )
            % p
            for degree in range(redundancy)
        )
        gamma = sum(support) % p
        require(
            moments
            == tuple(
                (line_base[index] + gamma * direction[index]) % p
                for index in range(redundancy)
            ),
            "canonical Lagrange moment identity changed",
        )
        selected.append((gamma, support))
        slope_histogram[gamma] += 1
    row = fixed.audit_exact_selected(
        p,
        domain,
        redundancy,
        t,
        line_base,
        direction,
        selected,
    )
    for size in range(1, t):
        require(
            all(value == 0 for value in line_base[:size])
            and all(value == 0 for value in direction[:size]),
            "canonical line gained an early nonzero moment",
        )
        for support in itertools.combinations(domain, size):
            vandermonde = [
                [pow(x, degree, p) for x in support]
                for degree in range(size)
            ]
            require(
                rankdef.numeric_rank(vandermonde, p) == size,
                "lower-support Vandermonde lost invertibility",
            )
    require(
        row["pairs"] == comb(len(domain), kernel_dimension),
        "canonical fixture missed the complete binomial",
    )
    return {
        "p": p,
        "domain": list(domain),
        "n": len(domain),
        "t": t,
        "deficiency": deficiency,
        "redundancy": redundancy,
        "kernel_dimension": kernel_dimension,
        "complete_pairs": row["pairs"],
        "slopes": row["slopes"],
        "lower_pairs": 0,
        "maximum_pairs_per_slope": max(slope_histogram.values()),
        "complete_binomial_bound": comb(len(domain), kernel_dimension),
        "all_top_supports_realized": True,
    }


def distinct_slope_lagrange_fixture(deficiency: int) -> dict[str, Any]:
    p = 257
    domain = tuple(1 << index for index in range(7))
    t = deficiency + 1
    integer_sums = [
        sum(support)
        for support in itertools.combinations(domain, t)
    ]
    require(
        max(integer_sums) < p,
        "superincreasing fixture wrapped modulo the prime",
    )
    require(
        len(set(integer_sums)) == comb(len(domain), t),
        "superincreasing fixture lost subset-sum injectivity",
    )
    row = canonical_lagrange_fixture(
        deficiency,
        p=p,
        domain=domain,
    )
    require(
        row["slopes"] == row["complete_pairs"],
        "canonical sharp fixture did not separate every slope",
    )
    require(
        row["maximum_pairs_per_slope"] == 1,
        "canonical sharp fixture retained slope multiplicity",
    )
    return row


def branch_fixtures() -> dict[str, Any]:
    fixtures = {}
    for name, t, deficiency, domain, common_support in [
        ("rank_drop", 4, 2, tuple(range(6)), (0,)),
        ("fixed_root", 4, 2, tuple(range(6)), (0, 1)),
        ("minimal_fixed_edge", 3, 2, tuple(range(4)), (0,)),
    ]:
        p = 7 if len(domain) > 4 else 5
        redundancy = 2 * t - deficiency
        weights = {x: 1 for x in domain}
        line_base = (0,) * redundancy
        amplitudes = tuple(range(1, len(common_support) + 1))
        direction = half.syndrome(
            domain,
            common_support,
            amplitudes,
            redundancy,
            p,
            weights,
        )
        sparse, spans = first.build_sparse_multimap(
            p, domain, t, redundancy, weights
        )
        result = complete_absorption_audit(
            p,
            domain,
            t,
            deficiency,
            line_base,
            direction,
            sparse,
            spans,
        )
        expected_branch = (
            "generic-rank-deficient"
            if name == "rank_drop"
            else "formal-fixed-root"
        )
        require(result["branch"] == expected_branch, "branch fixture changed")
        require(result["pairs"] == 1, "branch fixture lost its zero pair")
        fixtures[name] = {
            "p": p,
            "domain": list(domain),
            "n": len(domain),
            "t": t,
            "deficiency": deficiency,
            "redundancy": redundancy,
            "common_support": list(common_support),
            "branch": result["branch"],
            "pairs": result["pairs"],
            "bound": comb(len(domain), deficiency + 1),
        }
    return fixtures


def build_payload() -> dict[str, Any]:
    grids = [
        summarize_grid(3, tuple(range(3)), 2, 1, "exhaustive"),
        summarize_grid(5, (0, 1, 2, 3), 3, 2, "exhaustive"),
        summarize_grid(5, tuple(range(5)), 3, 2, "exhaustive"),
        summarize_grid(7, (0, 1, 2, 3, 4), 3, 1, "sample", 2000),
        summarize_grid(7, (0, 1, 2, 3, 4), 3, 2, "sample", 3000),
        summarize_grid(7, tuple(range(6)), 4, 2, "sample", 3000),
        summarize_grid(5, tuple(range(5)), 4, 3, "sample", 4000),
        summarize_grid(7, tuple(range(7)), 5, 3, "sample", 2500),
        summarize_grid(7, tuple(range(7)), 5, 4, "sample", 2500),
    ]
    sharp = [canonical_lagrange_fixture(d) for d in range(1, 6)]
    distinct_sharp = [
        distinct_slope_lagrange_fixture(d) for d in range(1, 6)
    ]
    require(
        all(row["slopes"] == row["complete_pairs"] for row in distinct_sharp),
        "a distinct-slope canonical fixture lost numerator equality",
    )
    branches = branch_fixtures()
    return {
        "schema_version": 1,
        "claim_id": CLAIM_ID,
        "base_commit": BASE_COMMIT,
        "status": "PROVED_AUDIT_WITH_UNPROVED_LEAN_TARGET",
        "hard_input": "3_fixed_deficiency_complete_pair_absorption",
        "theorem": {
            "range": "N>=R=2t-d and 1<=d<t",
            "row_count": "r=t-d",
            "top_kernel_dimension": "k=d+1",
            "complete_all_pair_bound": "|P|<=binom(N,d+1)",
            "mca_ca_numerator_bound": "B_MCA,B_CA<=binom(N,d+1)",
            "charge": (
                "every retained pair consumes at least r "
                "chargeable top-kernel bases"
            ),
            "sharpness": "canonical Lagrange lines attain equality",
        },
        "grids": grids,
        "canonical_lagrange_sharp_fixtures": sharp,
        "branch_fixtures": branches,
        "totals": {
            "audited_lines": sum(row["lines"] for row in grids),
            "transverse_pairs": sum(
                row["transverse_pairs"] for row in grids
            ),
            "transverse_slopes": sum(
                row["transverse_slopes"] for row in grids
            ),
            "same_slope_excess": sum(
                row["same_slope_excess"] for row in grids
            ),
            "chargeable_incidences": sum(
                row["chargeable_incidences"] for row in grids
            ),
            "root_capacity": sum(row["root_capacity"] for row in grids),
            "fixed_root_lines": sum(
                row["fixed_root_lines"] for row in grids
            ),
            "mixed_weight_lines": sum(
                row["mixed_weight_lines"] for row in grids
            ),
        },
        "nonclaims": [
            "no_uniform_subexponential_bound_when_d_grows_linearly",
            "no_bound_for_d_greater_than_or_equal_to_t",
            "no_atlas_or_deployed_row_movement",
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
        key: value for key, value in actual.items()
        if key != "payload_sha256"
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
    bad["theorem"]["complete_all_pair_bound"] = "|P|<=N"
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["grids"][2]["maximum_pairs_on_line"] -= 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["canonical_lagrange_sharp_fixtures"][4]["complete_pairs"] -= 1
    tampers.append(bad)

    bad = copy.deepcopy(expected)
    bad["branch_fixtures"]["minimal_fixed_edge"]["pairs"] += 1
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
        "FIXED_DEFICIENCY_COMPLETE_ABSORPTION_PASS "
        f"lines={totals['audited_lines']} "
        f"pairs={totals['transverse_pairs']} "
        f"slopes={totals['transverse_slopes']} "
        f"incidences={totals['chargeable_incidences']} "
        f"fixed={totals['fixed_root_lines']} "
        f"mixed={totals['mixed_weight_lines']}"
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
            "FIXED_DEFICIENCY_COMPLETE_ABSORPTION_TAMPER_PASS "
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
