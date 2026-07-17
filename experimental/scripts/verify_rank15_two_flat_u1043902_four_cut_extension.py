#!/usr/bin/env python3
"""Replay the rank-15 two-flat four-cut extension at u=1,043,902.

This verifier is standard-library only.  It reconstructs the integrated
PR #847 optimizer, proves four additional point-capacity cuts, reruns the
exact directional optimizer, checks the first open degree-saturated wall,
and replays the rank-15 recurrence consumer.  Every gate uses explicit
exceptions, so ``python -O`` cannot remove a check.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, replace
import hashlib
import json
from pathlib import Path
import string
import sys
from typing import Any, Callable, NoReturn


EXPERIMENTAL = Path(__file__).resolve().parents[1]
PACKET = (
    EXPERIMENTAL
    / "data"
    / "certificates"
    / "rank15-two-flat-u1043902-four-cut-extension"
)
CERTIFICATE_PATH = PACKET / "certificate.json"
EXPECTED_OUTPUT_PATH = PACKET / "verifier_output.txt"
EXPECTED_TAMPER_PATH = PACKET / "tamper_output.txt"
MANIFEST_PATH = PACKET / "SHA256SUMS.txt"

EXPECTED_CERTIFICATE_SHA256 = "5ee565a1ea7065e0317bf70fe511fccee7c8fc2c97be112d7927e93fb068593b"
EXPECTED_OUTPUT_SHA256 = "7c5a12f23f75e2ca27bb175762a70b11465f9074fc25a39981f28fe383b7d627"
EXPECTED_TAMPER_SHA256 = "4b7bbb2c8a095dd35e4343fd072cdde1e1b7886727b65c87e9f2942ee9760ace"
EXPECTED_MANIFEST_FILES = frozenset(
    {
        "README.md",
        "certificate.json",
        "tamper_output.txt",
        "verifier_output.txt",
        "../../../notes/l2/rank15_two_flat_u1043902_four_cut_extension.md",
        "../../../scripts/verify_rank15_two_flat_u1043902_four_cut_extension.py",
    }
)


class VerificationError(RuntimeError):
    """Raised when a theorem, parser, or frozen-artifact gate fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def c2(value: int) -> int:
    return value * (value - 1) // 2


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def reject_json_constant(value: str) -> NoReturn:
    raise VerificationError(f"non-finite JSON constant rejected: {value}")


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key rejected: {key}")
        result[key] = value
    return result


def strict_json_loads(payload: str) -> Any:
    try:
        return json.loads(
            payload,
            object_pairs_hook=unique_object,
            parse_constant=reject_json_constant,
        )
    except VerificationError:
        raise
    except (json.JSONDecodeError, UnicodeError) as exc:
        raise VerificationError(f"invalid JSON rejected: {exc}") from exc


def require_keys(value: Any, expected: set[str], label: str) -> dict[str, Any]:
    require(type(value) is dict, f"{label} must be an object")
    require(set(value) == expected, f"{label} keys changed: {sorted(value)}")
    return value


def require_int(value: Any, label: str) -> int:
    require(type(value) is int, f"{label} must be an integer")
    return value


@dataclass(frozen=True, slots=True)
class Parameters:
    p: int
    n: int
    K: int
    m: int
    list_size: int
    section_cap: int


@dataclass(frozen=True, slots=True)
class Claim:
    u_min: int
    u_max: int
    incremental_min: int
    incremental_max: int
    inherited_min: int
    boundary_u: int
    boundary_margin: int
    source_interval_min: int
    degree_wall_ceiling: int
    degree_wall_margin: int
    final_rank15: int
    target: int
    expected_new_margins: tuple[tuple[int, int], ...]


@dataclass(frozen=True, slots=True)
class OldCut:
    name: str
    target: int
    constant: int
    charges: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class NewCut:
    name: str
    alpha: int
    beta: int
    charges: tuple[int, ...]
    zero_slack_distinguished: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class Certificate:
    schema: str
    base_commit: str
    integrated_pr847_commit: str
    source_final_sha256: str
    source_full_rendered_sha256: str
    parameters: Parameters
    claim: Claim
    pair_budget: int
    mod13_budget: int
    gamma: tuple[int, ...]
    old_cuts: tuple[OldCut, ...]
    new_cuts: tuple[NewCut, ...]


@dataclass(frozen=True, slots=True)
class CutAudit:
    name: str
    cases: int
    minimum_slack: int
    zero_slack_distinguished: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class Pattern:
    residual_h: int
    full_counts: tuple[int, ...]
    full_incidence: int
    capacity: int


@dataclass(frozen=True, slots=True)
class OptimizerCache:
    values: dict[tuple[int, int], tuple[int, tuple[int, ...]]]
    branches: int
    successors_rejected: int
    resources: int


@dataclass(frozen=True, slots=True)
class Replay:
    margins: dict[int, int]
    patterns: dict[int, Pattern]
    first_closed: int
    closed_count: int


def parse_int_list(value: Any, length: int, label: str) -> tuple[int, ...]:
    require(type(value) is list and len(value) == length, f"{label} length changed")
    return tuple(require_int(item, f"{label}[{index}]") for index, item in enumerate(value))


def parse_certificate_data(raw: Any) -> Certificate:
    root = require_keys(
        raw,
        {
            "schema",
            "authority",
            "parameters",
            "claim",
            "budgets",
            "gamma",
            "old_cuts",
            "new_cuts",
        },
        "certificate",
    )
    require(root["schema"] == "rank15-two-flat-u1043902-four-cut-extension-v1", "schema changed")

    authority = require_keys(
        root["authority"],
        {
            "base_commit",
            "integrated_pr847_commit",
            "source_final_sha256",
            "source_full_rendered_sha256",
        },
        "authority",
    )
    for key in authority:
        require(type(authority[key]) is str, f"authority.{key} must be text")
    require(
        authority["base_commit"] == "7f278167e1e51f968896229ae438ea5a76398f90",
        "authority base changed",
    )
    require(
        authority["integrated_pr847_commit"] == "168e9ba02",
        "integrated PR847 commit changed",
    )
    require(
        authority["source_final_sha256"]
        == "3370f0937ecbfd4f43f6f3e9c5d13b547ad980da918afc7765aa8223819ee31c",
        "source final-response pin changed",
    )
    require(
        authority["source_full_rendered_sha256"]
        == "5565ae711d64cc5934d83932ce66de7f5fe23a1f00566807e187fe97d3b1055a",
        "source full-rendered pin changed",
    )

    parameter_raw = require_keys(
        root["parameters"],
        {"p", "n", "K", "m", "list_size", "section_cap"},
        "parameters",
    )
    parameters = Parameters(
        *(require_int(parameter_raw[key], f"parameters.{key}") for key in ("p", "n", "K", "m", "list_size", "section_cap"))
    )
    require(
        parameters == Parameters(2_130_706_433, 2_097_152, 1_048_576, 1_116_047, 212, 15),
        "fixed parameter interface changed",
    )

    claim_raw = require_keys(
        root["claim"],
        {
            "u_min",
            "u_max",
            "incremental_min",
            "incremental_max",
            "inherited_min",
            "boundary_u",
            "boundary_margin",
            "source_interval_min",
            "degree_wall_ceiling",
            "degree_wall_margin",
            "final_rank15",
            "target",
            "expected_new_margins",
        },
        "claim",
    )
    margin_rows = claim_raw["expected_new_margins"]
    require(type(margin_rows) is list, "expected_new_margins must be a list")
    expected_margins: list[tuple[int, int]] = []
    for index, row in enumerate(margin_rows):
        require(type(row) is list and len(row) == 2, f"margin row {index} malformed")
        expected_margins.append(
            (require_int(row[0], f"margin[{index}].u"), require_int(row[1], f"margin[{index}].value"))
        )
    claim = Claim(
        u_min=require_int(claim_raw["u_min"], "claim.u_min"),
        u_max=require_int(claim_raw["u_max"], "claim.u_max"),
        incremental_min=require_int(claim_raw["incremental_min"], "claim.incremental_min"),
        incremental_max=require_int(claim_raw["incremental_max"], "claim.incremental_max"),
        inherited_min=require_int(claim_raw["inherited_min"], "claim.inherited_min"),
        boundary_u=require_int(claim_raw["boundary_u"], "claim.boundary_u"),
        boundary_margin=require_int(claim_raw["boundary_margin"], "claim.boundary_margin"),
        source_interval_min=require_int(claim_raw["source_interval_min"], "claim.source_interval_min"),
        degree_wall_ceiling=require_int(claim_raw["degree_wall_ceiling"], "claim.degree_wall_ceiling"),
        degree_wall_margin=require_int(claim_raw["degree_wall_margin"], "claim.degree_wall_margin"),
        final_rank15=require_int(claim_raw["final_rank15"], "claim.final_rank15"),
        target=require_int(claim_raw["target"], "claim.target"),
        expected_new_margins=tuple(expected_margins),
    )
    require(
        (
            claim.u_min,
            claim.u_max,
            claim.incremental_min,
            claim.incremental_max,
            claim.inherited_min,
            claim.boundary_u,
            claim.boundary_margin,
            claim.source_interval_min,
            claim.degree_wall_ceiling,
            claim.degree_wall_margin,
            claim.final_rank15,
            claim.target,
        )
        == (
            1_043_902,
            1_043_957,
            1_043_902,
            1_043_916,
            1_043_917,
            1_043_901,
            1_707,
            1_043_592,
            4_673,
            -439,
            283_039_300_733_528_044,
            274_854_110_496_187_592,
        ),
        "claim anchors changed",
    )
    require(
        tuple(u for u, _ in claim.expected_new_margins)
        == tuple(range(claim.incremental_min, claim.incremental_max + 1)),
        "incremental margin states changed",
    )

    budget_raw = require_keys(root["budgets"], {"pair", "mod13"}, "budgets")
    pair_budget = require_int(budget_raw["pair"], "budgets.pair")
    mod13_budget = require_int(budget_raw["mod13"], "budgets.mod13")
    require(pair_budget == c2(parameters.list_size), "pair budget changed")
    require(mod13_budget == 41_340, "mod13 budget changed")
    gamma = parse_int_list(root["gamma"], 16, "gamma")
    require(gamma == (0, 0, 0, 0, 1, 3, 6, 10, 15, 21, 27, 33, 39, 45, 51, 65), "gamma changed")

    old_raw = root["old_cuts"]
    require(type(old_raw) is list and len(old_raw) == 3, "old_cuts count changed")
    old_cuts: list[OldCut] = []
    for index, item in enumerate(old_raw):
        row = require_keys(item, {"name", "target", "constant", "charges"}, f"old_cuts[{index}]")
        require(type(row["name"]) is str, "old-cut name must be text")
        old_cuts.append(
            OldCut(
                row["name"],
                require_int(row["target"], f"old_cuts[{index}].target"),
                require_int(row["constant"], f"old_cuts[{index}].constant"),
                parse_int_list(row["charges"], 16, f"old_cuts[{index}].charges"),
            )
        )
    require(tuple((cut.name, cut.target) for cut in old_cuts) == (("cut_a", 15), ("cut_b", 14), ("cut_c", 15)), "old-cut identities changed")

    new_raw = root["new_cuts"]
    require(type(new_raw) is list and len(new_raw) == 4, "new_cuts count changed")
    new_cuts: list[NewCut] = []
    for index, item in enumerate(new_raw):
        row = require_keys(
            item,
            {"name", "alpha", "beta", "charges", "zero_slack_distinguished"},
            f"new_cuts[{index}]",
        )
        require(type(row["name"]) is str, "new-cut name must be text")
        zero = row["zero_slack_distinguished"]
        require(type(zero) is list, "zero-slack set must be a list")
        new_cuts.append(
            NewCut(
                row["name"],
                require_int(row["alpha"], f"new_cuts[{index}].alpha"),
                require_int(row["beta"], f"new_cuts[{index}].beta"),
                parse_int_list(row["charges"], 16, f"new_cuts[{index}].charges"),
                tuple(require_int(value, f"new_cuts[{index}].zero") for value in zero),
            )
        )
    require(tuple(cut.name for cut in new_cuts) == ("C1", "C2", "C3", "C4"), "new-cut identities changed")

    return Certificate(
        root["schema"],
        authority["base_commit"],
        authority["integrated_pr847_commit"],
        authority["source_final_sha256"],
        authority["source_full_rendered_sha256"],
        parameters,
        claim,
        pair_budget,
        mod13_budget,
        gamma,
        tuple(old_cuts),
        tuple(new_cuts),
    )


def load_certificate() -> tuple[Certificate, dict[str, Any], str]:
    payload = CERTIFICATE_PATH.read_bytes()
    digest = sha256_bytes(payload)
    require(digest == EXPECTED_CERTIFICATE_SHA256, "certificate SHA-256 mismatch")
    try:
        text = payload.decode("ascii")
    except UnicodeDecodeError as exc:
        raise VerificationError("certificate is not ASCII") from exc
    raw = strict_json_loads(text)
    return parse_certificate_data(raw), raw, digest


def verify_manifest() -> int:
    lines = MANIFEST_PATH.read_text(encoding="ascii").splitlines()
    entries: dict[str, str] = {}
    hexdigits = set(string.hexdigits.lower())
    for index, line in enumerate(lines, start=1):
        require(len(line) >= 67 and line[64:66] == "  ", f"manifest line {index} malformed")
        digest = line[:64]
        name = line[66:]
        require(len(digest) == 64 and digest == digest.lower() and set(digest) <= hexdigits, f"manifest digest {index} malformed")
        require(name in EXPECTED_MANIFEST_FILES, f"unexpected manifest path: {name}")
        require(name not in entries, f"duplicate manifest entry: {name}")
        entries[name] = digest
    require(set(entries) == EXPECTED_MANIFEST_FILES, "manifest file set changed")
    for name, expected in entries.items():
        require(sha256_bytes((PACKET / name).resolve().read_bytes()) == expected, f"manifest checksum mismatch: {name}")
    return len(entries)


def rank_one_bound(parameters: Parameters, lower_universal: int) -> tuple[int, int, int, int]:
    best = -1
    first = last = -1
    count = 0
    for u in range(lower_universal, parameters.K):
        numerator = (parameters.n - u) * (parameters.m - parameters.K + 1)
        denominator = (parameters.m - u) ** 2 - (parameters.n - u) * (parameters.K - 1 - u)
        incidence = (parameters.n - u) // (parameters.m - u)
        johnson = numerator // denominator if denominator > 0 else 10**100
        value = min(incidence, johnson)
        if value > best:
            best, first, last, count = value, u, u, 1
        elif value == best:
            last, count = u, count + 1
    require(best >= 0, "empty rank-one scan")
    return best, first, last, count


def verify_section_cap(certificate: Certificate) -> tuple[int, int, int, int]:
    result = rank_one_bound(certificate.parameters, certificate.claim.source_interval_min + 1)
    require(result == (15, 1_045_969, 1_048_575, 2_607), "proper-section cap scan changed")
    for u in range(certificate.claim.source_interval_min, certificate.claim.u_max + 1):
        require(rank_one_bound(certificate.parameters, u + 1)[0] <= 15, f"section cap failed at u={u}")
    return result


def verify_old_cut(cut: OldCut, list_size: int) -> CutAudit:
    target_weight = cut.target - 1
    slacks: list[tuple[int, int]] = []
    for distinguished in range((list_size - 1) // target_weight + 1):
        remaining = list_size - 1 - target_weight * distinguished
        dp = [0] * (remaining + 1)
        for capacity in range(1, remaining + 1):
            best = dp[capacity - 1]
            for h in range(2, 16):
                if h != cut.target and h - 1 <= capacity:
                    best = max(best, dp[capacity - h + 1] + cut.charges[h])
            dp[capacity] = best
        maximum = cut.charges[cut.target] * distinguished + dp[remaining]
        slacks.append((distinguished, c2(distinguished) + cut.constant - maximum))
    require(min(slack for _, slack in slacks) >= 0, f"old cut {cut.name} failed")
    zeros = tuple(j for j, slack in slacks if slack == 0)
    return CutAudit(cut.name, len(slacks), min(slack for _, slack in slacks), zeros)


def verify_new_cut(cut: NewCut, list_size: int) -> CutAudit:
    slacks: list[tuple[int, int]] = []
    for distinguished in range(16):
        remaining = list_size - 1 - 14 * distinguished
        require(remaining >= 0, f"{cut.name}: negative point capacity")
        dp = [0] * (remaining + 1)
        for capacity in range(1, remaining + 1):
            best = dp[capacity - 1]
            for h in range(2, 15):
                if h - 1 <= capacity:
                    best = max(best, dp[capacity - h + 1] + cut.charges[h])
            dp[capacity] = best
        maximum = cut.charges[15] * distinguished + dp[remaining]
        allowance = cut.alpha * c2(distinguished) + cut.beta
        slacks.append((distinguished, allowance - maximum))
    require(min(slack for _, slack in slacks) >= 0, f"new cut {cut.name} failed")
    zeros = tuple(j for j, slack in slacks if slack == 0)
    require(zeros == cut.zero_slack_distinguished, f"{cut.name} zero-slack set changed")
    return CutAudit(cut.name, len(slacks), min(slack for _, slack in slacks), zeros)


def pair_cost(h: int) -> int:
    return c2(h)


def mod13_cost(h: int) -> int:
    return 0 if h <= 2 else h * (h - 2)


def old_cut1_cost(h: int) -> int:
    return h * c2(h - 2) if 4 <= h <= 13 else 0


def old_cut2_cost(h: int, gamma: tuple[int, ...]) -> int:
    return h * gamma[h] if 4 <= h <= 13 else 0


def lower_resource_costs(certificate: Certificate, h: int, include_new: bool) -> tuple[int, ...]:
    costs = [pair_cost(h), mod13_cost(h), old_cut1_cost(h), old_cut2_cost(h, certificate.gamma)]
    if include_new:
        costs.extend(h * cut.charges[h] if h <= 13 else 0 for cut in certificate.new_cuts)
    return tuple(costs)


def verify_discrete_convexity(certificate: Certificate, include_new: bool) -> tuple[tuple[int, ...], ...]:
    increments: list[tuple[int, ...]] = []
    previous = tuple(-1 for _ in lower_resource_costs(certificate, 1, include_new))
    for h in range(1, 13):
        left = lower_resource_costs(certificate, h, include_new)
        right = lower_resource_costs(certificate, h + 1, include_new)
        current = tuple(b - a for a, b in zip(left, right))
        require(all(value >= 0 for value in current), f"negative resource increment at h={h}")
        require(all(a <= b for a, b in zip(previous, current)), f"nonconvex resource at h={h}")
        increments.append(current)
        previous = current
    return tuple(increments)


def old_lower_budgets(certificate: Certificate, n15: int, n14: int) -> tuple[int, int]:
    cut_a, cut_b, cut_c = certificate.old_cuts
    m = certificate.parameters.list_size
    cut1 = min(
        c2(n15) + m * cut_a.constant - 15 * cut_a.charges[15] * n15 - 14 * cut_a.charges[14] * n14,
        c2(n14) + m * cut_b.constant - 15 * cut_b.charges[15] * n15 - 14 * cut_b.charges[14] * n14,
    )
    cut2 = c2(n15) + m * cut_c.constant - 15 * cut_c.charges[15] * n15 - 14 * cut_c.charges[14] * n14
    return cut1, cut2


def optimize_full_directions(
    f: int,
    residual_h: int,
    certificate: Certificate,
    include_new: bool,
) -> tuple[int, tuple[int, ...], int, int]:
    resources = len(lower_resource_costs(certificate, 1, include_new))
    tables = tuple(
        tuple(lower_resource_costs(certificate, h, include_new)[index] for h in range(16))
        for index in range(resources)
    )
    increments = tuple(
        tuple(table[h + 1] - table[h] for table in tables)
        for h in range(13)
    )
    residual_cost = tuple(table[residual_h] for table in tables)
    residual_15 = int(residual_h == 15)
    residual_14 = int(residual_h == 14)
    best = -1
    best_counts: tuple[int, ...] | None = None
    branches = 0
    successors = 0

    for full_15 in range(f + 1):
        for full_14 in range(f - full_15 + 1):
            branches += 1
            n15 = full_15 + residual_15
            n14 = full_14 + residual_14
            old1, old2 = old_lower_budgets(certificate, n15, n14)
            if old1 < 0 or old2 < 0:
                continue
            fixed_pair = residual_cost[0] + 105 * full_15 + 91 * full_14
            fixed_mod13 = residual_cost[1] + 195 * full_15 + 168 * full_14
            if fixed_pair > certificate.pair_budget or fixed_mod13 > certificate.mod13_budget:
                continue
            budgets = [
                certificate.pair_budget - fixed_pair,
                certificate.mod13_budget - fixed_mod13,
                old1 - residual_cost[2],
                old2 - residual_cost[3],
            ]
            if include_new:
                for index, cut in enumerate(certificate.new_cuts, start=4):
                    budget = (
                        cut.alpha * c2(n15)
                        + certificate.parameters.list_size * cut.beta
                        - 15 * cut.charges[15] * n15
                        - 14 * cut.charges[14] * n14
                        - residual_cost[index]
                    )
                    budgets.append(budget)
            if any(value < 0 for value in budgets):
                continue

            low = f - full_15 - full_14
            if residual_h >= 14 and low:
                continue
            counts = [0] * 16
            counts[15] = full_15
            counts[14] = full_14
            if low == 0:
                low_incidence = 0
            else:
                remaining = [budget - low * table[residual_h] for budget, table in zip(budgets, tables)]
                if any(value < 0 for value in remaining):
                    continue
                upgrades = 0
                for h in range(residual_h, 13):
                    step = increments[h]
                    number = low
                    for index, increment in enumerate(step):
                        if increment:
                            number = min(number, remaining[index] // increment)
                    upgrades += number
                    for index, increment in enumerate(step):
                        remaining[index] -= number * increment
                    if number < low:
                        break
                layers, partial = divmod(upgrades, low)
                low_h = residual_h + layers
                high_h = low_h + 1
                require(low_h <= 13 and (partial == 0 or high_h <= 13), "balanced occupancy overflow")
                counts[low_h] += low - partial
                if partial:
                    counts[high_h] += partial
                low_incidence = low * residual_h + upgrades
                balanced = tuple(sum(counts[h] * table[h] for h in range(1, 14)) for table in tables)
                require(all(cost <= budget for cost, budget in zip(balanced, budgets)), "balanced result infeasible")
                if upgrades < low * (13 - residual_h):
                    next_layers, next_partial = divmod(upgrades + 1, low)
                    next_low = residual_h + next_layers
                    next_counts = [0] * 16
                    next_counts[next_low] = low - next_partial
                    if next_partial:
                        next_counts[next_low + 1] = next_partial
                    successor = tuple(sum(next_counts[h] * table[h] for h in range(1, 14)) for table in tables)
                    require(any(cost > budget for cost, budget in zip(successor, budgets)), "one-unit successor feasible")
                    successors += 1

            incidence = 15 * full_15 + 14 * full_14 + low_incidence
            if incidence > best:
                best = incidence
                best_counts = tuple(counts)

    require(best >= 0 and best_counts is not None, f"no pattern at f={f},h={residual_h}")
    require(sum(best_counts) == f, "full-direction count changed")
    require(sum(h * best_counts[h] for h in range(16)) == best, "pattern incidence mismatch")
    return best, best_counts, branches, successors


def build_optimizer_cache(certificate: Certificate, include_new: bool) -> OptimizerCache:
    verify_discrete_convexity(certificate, include_new)
    values: dict[tuple[int, int], tuple[int, tuple[int, ...]]] = {}
    branches = successors = 0
    for f in range(211, 229):
        for residual_h in range(1, 16):
            best, counts, checked, rejected = optimize_full_directions(f, residual_h, certificate, include_new)
            values[(f, residual_h)] = (best, counts)
            branches += checked
            successors += rejected
    require(len(values) == 270, "optimizer cache size changed")
    return OptimizerCache(values, branches, successors, 8 if include_new else 4)


def state_pattern(u: int, degree: int, residual_n: int, certificate: Certificate, cache: OptimizerCache) -> Pattern:
    f, residual_weight = divmod(residual_n, degree)
    require(0 < residual_weight < degree, f"non-strict residual weight at u={u}")
    best: Pattern | None = None
    for residual_h in range(1, 16):
        full_incidence, counts = cache.values[(f, residual_h)]
        capacity = degree * full_incidence + residual_weight * residual_h
        candidate = Pattern(residual_h, counts, full_incidence, capacity)
        if best is None or candidate.capacity > best.capacity:
            best = candidate
    require(best is not None, f"no state pattern at u={u}")
    return best


def replay_margins(certificate: Certificate, cache: OptimizerCache) -> Replay:
    p = certificate.parameters
    margins: dict[int, int] = {}
    patterns: dict[int, Pattern] = {}
    for u in range(certificate.claim.source_interval_min, certificate.claim.u_max + 1):
        pattern = state_pattern(u, p.K - 1 - u, p.n - u, certificate, cache)
        patterns[u] = pattern
        margins[u] = pattern.capacity - p.list_size * (p.m - u)
    negative = [u for u in sorted(margins) if margins[u] < 0]
    require(negative, "optimizer closes no states")
    return Replay(margins, patterns, negative[0], sum(margins[u] < 0 for u in range(certificate.claim.u_min, certificate.claim.u_max + 1)))


def compact_counts(counts: tuple[int, ...]) -> str:
    return ",".join(f"n{h}={counts[h]}" for h in range(15, 0, -1) if counts[h])


def verify_optimizer(certificate: Certificate) -> tuple[OptimizerCache, OptimizerCache, Replay, Replay, Pattern]:
    old_cache = build_optimizer_cache(certificate, False)
    new_cache = build_optimizer_cache(certificate, True)
    require(new_cache.branches == 6_597_135, "new optimizer branch count changed")
    require(new_cache.successors_rejected == 215_009, "new optimizer successor count changed")
    old_replay = replay_margins(certificate, old_cache)
    new_replay = replay_margins(certificate, new_cache)

    target_u = 1_043_916
    require(old_replay.margins[target_u] == 878, "integrated PR847 wall did not reconstruct")
    require(new_replay.margins[target_u] == -17_758, "literal target margin changed")
    require(new_replay.first_closed == certificate.claim.u_min, "first closed state changed")
    require(new_replay.closed_count == 56, "combined closed count changed")
    require(new_replay.margins[certificate.claim.boundary_u] == certificate.claim.boundary_margin, "boundary margin changed")
    require(
        tuple((u, new_replay.margins[u]) for u in range(certificate.claim.incremental_min, certificate.claim.incremental_max + 1))
        == certificate.claim.expected_new_margins,
        "incremental margin table changed",
    )
    require(all(new_replay.margins[u] < 0 for u in range(certificate.claim.inherited_min, certificate.claim.u_max + 1)), "inherited suffix reopened")

    degree_pattern = state_pattern(
        certificate.claim.boundary_u,
        certificate.claim.degree_wall_ceiling,
        certificate.parameters.n - certificate.claim.boundary_u,
        certificate,
        new_cache,
    )
    degree_margin = degree_pattern.capacity - certificate.parameters.list_size * (certificate.parameters.m - certificate.claim.boundary_u)
    require(degree_margin == certificate.claim.degree_wall_margin, "degree-wall margin changed")
    return old_cache, new_cache, old_replay, new_replay, degree_pattern


def johnson_bound(parameters: Parameters, u: int) -> int | None:
    residual_n = parameters.n - u
    residual_a = parameters.m - u
    denominator = residual_a * residual_a - residual_n * (parameters.K - 1 - u)
    if denominator <= 0:
        return None
    return residual_n * (parameters.m - parameters.K + 1) // denominator


def replay_parent_recurrence(certificate: Certificate) -> tuple[int, int, int, int]:
    p = certificate.parameters
    old_previous = [1] * (p.K + 2)
    new_previous = [1] * (p.K + 2)
    d2_changed = 0
    d2_max_drop = 0
    higher_changed = 0

    for dimension in range(1, 16):
        upper = p.K - dimension
        old_current = [0] * (p.K + 2)
        new_current = [0] * (p.K + 2)
        old_suffix = new_suffix = 0
        for u in range(upper, -1, -1):
            old_candidate = (p.n - u) * old_previous[u + 1] // (p.m - u)
            new_candidate = (p.n - u) * new_previous[u + 1] // (p.m - u)
            johnson = johnson_bound(p, u)
            if johnson is not None:
                old_candidate = min(old_candidate, johnson)
                new_candidate = min(new_candidate, johnson)
            if dimension == 2:
                if 1_043_771 <= u <= 1_043_948:
                    old_candidate = min(old_candidate, 217)
                    new_candidate = min(new_candidate, 217)
                if 1_043_917 <= u <= 1_043_957:
                    old_candidate = min(old_candidate, 211)
                    new_candidate = min(new_candidate, 211)
                if certificate.claim.incremental_min <= u <= certificate.claim.incremental_max:
                    new_candidate = min(new_candidate, 211)
            old_suffix = max(old_suffix, old_candidate)
            new_suffix = max(new_suffix, new_candidate)
            old_current[u] = old_suffix
            new_current[u] = new_suffix
        changed = [u for u in range(upper + 1) if old_current[u] != new_current[u]]
        if dimension == 2:
            d2_changed = len(changed)
            d2_max_drop = max((old_current[u] - new_current[u] for u in changed), default=0)
            require(changed == list(range(certificate.claim.incremental_min, certificate.claim.incremental_max + 1)), "D2 ownership changed")
        elif dimension >= 3:
            higher_changed += len(changed)
        old_previous, new_previous = old_current, new_current

    require(d2_changed == 15 and d2_max_drop == 5, "D2 delta changed")
    require(higher_changed == 0, "higher-rank parent changed")
    require(old_previous[0] == new_previous[0] == certificate.claim.final_rank15, "rank-15 recurrence value changed")
    gap = certificate.claim.final_rank15 - certificate.claim.target
    require(gap == 8_185_190_237_340_452, "target gap changed")
    return d2_changed, d2_max_drop, higher_changed, gap


def render_main(certificate: Certificate, certificate_sha256: str) -> str:
    section = verify_section_cap(certificate)
    old_audits = tuple(verify_old_cut(cut, certificate.parameters.list_size) for cut in certificate.old_cuts)
    new_audits = tuple(verify_new_cut(cut, certificate.parameters.list_size) for cut in certificate.new_cuts)
    old_cache, new_cache, old_replay, new_replay, degree_pattern = verify_optimizer(certificate)
    d2_changed, d2_max_drop, higher_changed, gap = replay_parent_recurrence(certificate)
    target_old = old_replay.patterns[1_043_916]
    target_new = new_replay.patterns[1_043_916]
    first_new = new_replay.patterns[certificate.claim.u_min]

    lines = [
        "RANK15_TWO_FLAT_U1043902_FOUR_CUT_EXTENSION",
        f"authority_base={certificate.base_commit};integrated_pr847={certificate.integrated_pr847_commit}",
        f"source_pins=final:{certificate.source_final_sha256};full:{certificate.source_full_rendered_sha256}",
        f"certificate_sha256={certificate_sha256}",
        f"parameters=p{certificate.parameters.p},n{certificate.parameters.n},K{certificate.parameters.K},m{certificate.parameters.m},M{certificate.parameters.list_size}",
        f"section_cap=15;maximizers={section[1]}..{section[2]};count={section[3]}",
    ]
    for audit in old_audits:
        lines.append(f"inherited_local_cut={audit.name};cases={audit.cases};minimum_slack={audit.minimum_slack}")
    for audit in new_audits:
        zeros = ",".join(str(value) for value in audit.zero_slack_distinguished)
        lines.append(f"new_local_cut={audit.name};cases={audit.cases};minimum_slack={audit.minimum_slack};zero_slack_j={zeros}")
    lines.extend(
        [
            "discrete_convex_exchange=PASS;old_resources=4;new_resources=8;occupancies=1..13",
            f"optimizer_cache={len(new_cache.values)};branches={new_cache.branches};successors_rejected={new_cache.successors_rejected}",
            f"pr847_reconstruction=u1043916;capacity={target_old.capacity};margin={old_replay.margins[1043916]:+d};hstar={target_old.residual_h};profile={compact_counts(target_old.full_counts)}",
            f"literal_target=u1043916;capacity={target_new.capacity};margin={new_replay.margins[1043916]:+d};hstar={target_new.residual_h};profile={compact_counts(target_new.full_counts)}",
            f"first_closed=u{certificate.claim.u_min};capacity={first_new.capacity};margin={new_replay.margins[certificate.claim.u_min]:+d};hstar={first_new.residual_h};profile={compact_counts(first_new.full_counts)}",
            f"exact_new_wall=u{certificate.claim.boundary_u};margin={new_replay.margins[certificate.claim.boundary_u]:+d}",
        ]
    )
    lines.extend(f"NEW_MARGIN u={u} margin={new_replay.margins[u]:+d}" for u in range(certificate.claim.incremental_min, certificate.claim.incremental_max + 1))
    lines.extend(
        [
            f"combined_theorem=D2[{certificate.claim.u_min}..{certificate.claim.u_max}]<=211;closed_count={new_replay.closed_count}",
            f"incremental_ownership={certificate.claim.incremental_min}..{certificate.claim.incremental_max};states=15;inherited={certificate.claim.inherited_min}..{certificate.claim.u_max}",
            f"degree_le_{certificate.claim.degree_wall_ceiling}=EXCLUDED;capacity={degree_pattern.capacity};margin={certificate.claim.degree_wall_margin:+d}",
            "degree_wall_consequence=d=4674,degG=0,r=0",
            f"parent_replay=D2_changed={d2_changed};max_drop={d2_max_drop};dimensions3to15_changed={higher_changed}",
            f"rank15_final={certificate.claim.final_rank15};target={certificate.claim.target};gap={gap}",
            "NONCLAIMS=u<=1043901,parent_saving,source_transport,rank16,Grand_List,Grand_MCA,score_movement",
            "RESULT: PASS",
        ]
    )
    return "\n".join(lines) + "\n"


def expect_rejected(label: str, action: Callable[[], Any]) -> str:
    try:
        action()
    except VerificationError as exc:
        return f"TAMPER {label}: REJECTED ({exc})"
    raise VerificationError(f"tamper accepted: {label}")


def replace_new_charge(cut: NewCut, h: int, delta: int) -> NewCut:
    charges = list(cut.charges)
    charges[h] += delta
    return replace(cut, charges=tuple(charges))


def render_tamper(certificate: Certificate, raw: dict[str, Any]) -> str:
    _, new_cache, _, replay, _ = verify_optimizer(certificate)
    lines = ["RANK15_TWO_FLAT_U1043902_TAMPER_SELFTEST"]
    lines.append(expect_rejected("extend_to_u1043901", lambda: require(replay.margins[1_043_901] < 0, "boundary remains open")))
    for index, h in ((0, 15), (1, 15), (2, 15), (3, 15)):
        mutated = replace_new_charge(certificate.new_cuts[index], h, 1)
        lines.append(expect_rejected(f"{mutated.name}_q{h}_plus_1", lambda mutated=mutated: verify_new_cut(mutated, certificate.parameters.list_size)))
    lines.append(
        expect_rejected(
            "degree_ceiling_4674",
            lambda: require(
                state_pattern(1_043_901, 4_674, certificate.parameters.n - 1_043_901, certificate, new_cache).capacity
                - certificate.parameters.list_size * (certificate.parameters.m - 1_043_901)
                < 0,
                "full degree is not excluded",
            ),
        )
    )
    lines.append(expect_rejected("parser_duplicate_key", lambda: strict_json_loads('{"schema":"a","schema":"b"}')))
    unknown = deepcopy(raw)
    unknown["unexpected"] = 1
    lines.append(expect_rejected("parser_unknown_field", lambda: parse_certificate_data(unknown)))
    floating = deepcopy(raw)
    floating["parameters"]["n"] = 2_097_152.0
    lines.append(expect_rejected("parser_float_integer", lambda: parse_certificate_data(floating)))
    lines.append("TAMPER_RESULT: PASS")
    return "\n".join(lines) + "\n"


def emit_frozen(rendered: str, path: Path, expected_sha256: str) -> None:
    payload = rendered.encode("ascii")
    frozen = path.read_bytes()
    require(sha256_bytes(frozen) == expected_sha256, f"frozen output hash changed: {path.name}")
    require(payload == frozen, f"replayed output differs from {path.name}")
    sys.stdout.buffer.write(payload)


def main(argv: list[str]) -> int:
    try:
        certificate, raw, digest = load_certificate()
        verify_manifest()
        if not argv:
            emit_frozen(render_main(certificate, digest), EXPECTED_OUTPUT_PATH, EXPECTED_OUTPUT_SHA256)
        elif argv == ["--tamper-selftest"]:
            emit_frozen(render_tamper(certificate, raw), EXPECTED_TAMPER_PATH, EXPECTED_TAMPER_SHA256)
        else:
            raise VerificationError(f"unsupported arguments: {argv}")
    except (OSError, VerificationError) as exc:
        print(f"VERIFY_ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
