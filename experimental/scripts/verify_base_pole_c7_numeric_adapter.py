#!/usr/bin/env python3
"""Finite regressions for the conditional base-pole C7 numeric adapter.

This script checks only list deletion, duplicate control, local unit payments,
and exact line-local telescopes.  It does not model finite-field algebra,
Reed--Solomon witnesses, semantic ownership, line completeness, or UNIF.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence


def require(condition: bool, message: str) -> None:
    """Fail identically under normal and optimized Python."""
    if not condition:
        raise RuntimeError(message)


def is_nodup(values: Sequence[int]) -> bool:
    return len(values) == len(set(values))


def survivors(earlier: Sequence[int], raw: Sequence[int]) -> list[int]:
    """Delete every raw slope already assigned to an earlier profile."""
    earlier_set = set(earlier)
    return [slope for slope in raw if slope not in earlier_set]


@dataclass(frozen=True)
class NumericProfile:
    assigned_slopes: tuple[int, ...]
    natural_scale: int
    residual_budget: int
    sidon_budget: int
    ray_budget: int
    compiler_loss: int


def unit_profile(slope: int, compiler_loss: int) -> NumericProfile:
    """Lift the loss-one singleton profile without changing local budgets."""
    require(compiler_loss >= 1, "compiler loss must dominate the unit source")
    return NumericProfile(
        assigned_slopes=(slope,),
        natural_scale=1,
        residual_budget=1,
        sidon_budget=1,
        ray_budget=1,
        compiler_loss=compiler_loss,
    )


def assigned_image(profiles: Iterable[NumericProfile]) -> list[int]:
    return [slope for profile in profiles for slope in profile.assigned_slopes]


def budget_total(profiles: Iterable[NumericProfile]) -> int:
    return sum(profile.ray_budget for profile in profiles)


def natural_total(profiles: Iterable[NumericProfile]) -> int:
    return sum(profile.natural_scale for profile in profiles)


def extend(
    prior: Sequence[NumericProfile], raw: Sequence[int], compiler_loss: int
) -> list[NumericProfile]:
    earlier = assigned_image(prior)
    added = [unit_profile(slope, compiler_loss) for slope in survivors(earlier, raw)]
    return [*prior, *added]


def run() -> None:
    raw = [100, 101, 102, 103]
    require(is_nodup(raw), "fixture raw slope image must be duplicate-free")
    require(survivors([100, 102], raw) == [101, 103], "deletion fixture failed")

    # Affine-Steiner double-charge regression: the numerical singleton payment
    # is valid in isolation, but the untrimmed append repeats an earlier slope.
    require(survivors([7], [7]) == [], "earlier owner must erase shared slope")
    require(not is_nodup([7, 7]), "untrimmed double charge must be detected")
    require(is_nodup([7] + survivors([7], [7])), "trimmed append must be nodup")

    # Atlas-order noncanonicity: a broad earlier singleton-root image can erase
    # the later residual; an empty earlier image leaves it intact.
    singleton_raw = [10, 11, 12, 13]
    require(
        survivors([10, 13, 11, 12], singleton_raw) == [],
        "broad singleton-root atlas should erase the finite later residual",
    )
    require(
        survivors([], singleton_raw) == singleton_raw,
        "empty earlier image should preserve the raw residual",
    )

    # Generic compiler-loss lift: local budgets stay at one rather than being
    # inflated to the allowed global loss.
    lifted = unit_profile(9, compiler_loss=4)
    require(lifted.natural_scale == 1, "loss lift changed natural scale")
    require(lifted.residual_budget == 1, "loss lift changed residual budget")
    require(lifted.sidon_budget == 1, "loss lift changed Sidon budget")
    require(lifted.ray_budget == 1, "loss lift changed ray budget")

    prior = [
        NumericProfile(
            assigned_slopes=(100, 102),
            natural_scale=2,
            residual_budget=2,
            sidon_budget=2,
            ray_budget=2,
            compiler_loss=3,
        )
    ]
    combined = extend(prior, raw, compiler_loss=3)
    survivor_count = len(survivors(assigned_image(prior), raw))

    require(
        assigned_image(combined) == [100, 102, 101, 103],
        "extension assigned-image telescope failed",
    )
    require(is_nodup(assigned_image(combined)), "extension lost nodup ownership")
    require(
        budget_total(combined) == budget_total(prior) + survivor_count,
        "direct-budget telescope failed",
    )
    require(
        natural_total(combined) == natural_total(prior) + survivor_count,
        "natural-scale telescope failed",
    )

    q_minus_one = 4
    require(len(raw) <= q_minus_one, "source q-1 census fixture failed")
    require(survivor_count <= q_minus_one, "survivor census exceeded q-1")
    require(
        budget_total(combined) <= budget_total(prior) + q_minus_one,
        "combined budget exceeded prior plus q-1",
    )
    require(
        natural_total(combined) <= natural_total(prior) + q_minus_one,
        "combined natural total exceeded prior plus q-1",
    )

    print("base-pole C7 numeric adapter regressions: PASS")
    print(f"raw slopes: {raw}")
    print(f"survivors after [100, 102]: {survivors([100, 102], raw)}")
    print(f"combined assigned image: {assigned_image(combined)}")
    print(f"combined budget/natural totals: {budget_total(combined)}/{natural_total(combined)}")


if __name__ == "__main__":
    run()
