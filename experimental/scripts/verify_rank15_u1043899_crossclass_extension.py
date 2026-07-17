#!/usr/bin/env python3
"""Exact verifier for the rank-15 affine-two-flat extension through u=1,043,899.

Standard-library only.  The verifier independently reconstructs:
  * the rank-one proper-section cap 15;
  * the three inherited point-capacity cuts and the four PR-865 cuts;
  * the discrete-convex base directional optimizer;
  * a new cross-occupancy-class pointwise dual cut;
  * every profile in every incidence layer removed by that cut;
  * the exact strengthened f=225 optimizer and its next wall; and
  * the dimension-1 through dimension-15 recurrence consumer.

No source file from a pending PR is imported.
"""

from __future__ import annotations

from math import comb


class VerificationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def c2(x: int) -> int:
    return x * (x - 1) // 2


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


# Literal deployed source parameters.
P = 2_130_706_433
N_TOTAL = 2_097_152
K = 1_048_576
M_AGREE = 1_116_047
LIST = 212
POINT_CAPACITY = LIST - 1
F_FULL = 225
PAIR_BUDGET = c2(LIST)
MOD13_BUDGET = 41_340
TARGET_PARENT = 274_854_110_496_187_592
EXPECTED_PARENT = 283_039_300_733_528_044

GAMMA = (0, 0, 0, 0, 1, 3, 6, 10, 15, 21, 27, 33, 39, 45, 51, 65)

OLD_CUTS = (
    (
        "A",
        15,
        1080,
        (0, 0, 0, 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 65, 79),
    ),
    (
        "B",
        14,
        1170,
        (0, 0, 0, 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 78, 78),
    ),
    (
        "C",
        15,
        870,
        (0, 0, 0, 0, 1, 3, 6, 10, 15, 21, 27, 33, 39, 45, 51, 65),
    ),
)

FOUR_CUTS = (
    (
        "C1",
        840,
        215_775,
        (0, 0, 0, 0, 0, 504, 840, 1080, 1260, 2345, 4347, 5985, 7350, 8505, 8505, 20265),
        (11, 12, 13, 14, 15),
    ),
    (
        "C2",
        1820,
        909_300,
        (0, 0, 0, 0, 0, 5460, 10080, 13380, 15855, 18620, 26628, 33180, 38640, 43260, 47880, 73360),
        (11, 12, 14, 15),
    ),
    (
        "C3",
        385,
        172_200,
        (0, 0, 0, 0, 0, 0, 1435, 2755, 3745, 4515, 5131, 6195, 7105, 7875, 8785, 14175),
        (12, 13, 14, 15),
    ),
    (
        "C4",
        880,
        508_200,
        (0, 0, 0, 0, 0, 0, 4620, 7920, 10395, 12320, 13992, 18360, 22000, 25080, 27720, 40040),
        (10, 11, 12, 14, 15),
    ),
)

# New cross-class local cut.  Classes not listed have coefficient zero.
DUAL_B = 1_000_000_000_009
DUAL_C = {
    10: -35_686_639_872,
    11: -59_318_449_143,
    12: -66_666_666_667,
    13: -66_666_666_667,
    14: -66_666_666_667,
    15: -66_666_666_667,
}
DUAL_L = {
    (10, 11): 4_088_463_951,
    (10, 12): 4_915_294_705,
    (10, 13): 2_733_666_212,
    (10, 14): 1_549_694_453,
    (10, 15): 180_418_024,
    (11, 11): 10_467_842_606,
    (11, 12): 10_549_862_864,
    (11, 13): 6_974_378_531,
    (11, 14): 4_406_162_092,
    (12, 12): 9_468_952_463,
    (12, 13): 6_453_906_223,
    (12, 14): 2_463_237_973,
    (13, 13): 3_794_562_793,
    (13, 14): 1_624_704_129,
    (14, 14): 1_450_158_934,
}
HIGH_CLASSES = tuple(range(10, 16))


def rank_one_bound(lower_universal: int) -> tuple[int, int, int, int]:
    best = -1
    first = last = -1
    count = 0
    for v in range(lower_universal, K):
        incidence = (N_TOTAL - v) // (M_AGREE - v)
        denominator = (M_AGREE - v) ** 2 - (N_TOTAL - v) * (K - 1 - v)
        if denominator <= 0:
            johnson = 10**100
        else:
            johnson = (N_TOTAL - v) * (M_AGREE - K + 1) // denominator
        value = min(incidence, johnson)
        if value > best:
            best, first, last, count = value, v, v, 1
        elif value == best:
            last, count = v, count + 1
    return best, first, last, count


def knapsack_max(charges: tuple[int, ...], capacity: int, excluded_h: int | None = None) -> int:
    dp = [0] * (capacity + 1)
    for cap in range(1, capacity + 1):
        best = dp[cap - 1]
        for h in range(2, 16):
            if h == excluded_h:
                continue
            weight = h - 1
            if weight <= cap:
                best = max(best, dp[cap - weight] + charges[h])
        dp[cap] = best
    return dp[capacity]


def verify_old_local_cuts() -> tuple[tuple[str, int, int, tuple[int, ...]], ...]:
    audits = []
    expected = {
        "A": (16, 0, tuple(range(4, 16))),
        "B": (17, 0, tuple(range(0, 12)) + (13,)),
        "C": (16, 0, tuple(range(8, 16))),
    }
    for name, target, constant, charges in OLD_CUTS:
        rows = []
        for j in range(POINT_CAPACITY // (target - 1) + 1):
            remaining = POINT_CAPACITY - (target - 1) * j
            maximum = charges[target] * j + knapsack_max(charges, remaining, target)
            rows.append((j, c2(j) + constant - maximum))
        result = (len(rows), min(slack for _, slack in rows), tuple(j for j, slack in rows if slack == 0))
        require(result == expected[name], f"old local cut {name} changed: {result}")
        audits.append((name, *result))
    return tuple(audits)


def verify_four_local_cuts() -> tuple[tuple[str, int, int, tuple[int, ...]], ...]:
    audits = []
    for name, alpha, beta, charges, expected_zeros in FOUR_CUTS:
        rows = []
        for j in range(16):
            remaining = POINT_CAPACITY - 14 * j
            require(remaining >= 0, f"negative capacity in {name}")
            maximum = charges[15] * j + knapsack_max(charges, remaining, 15)
            rows.append((j, alpha * c2(j) + beta - maximum))
        result = (len(rows), min(slack for _, slack in rows), tuple(j for j, slack in rows if slack == 0))
        require(result == (16, 0, expected_zeros), f"four-cut audit {name} changed: {result}")
        audits.append((name, *result))
    return tuple(audits)


def pair_cost(h: int) -> int:
    return c2(h)


def mod13_cost(h: int) -> int:
    return 0 if h <= 2 else h * (h - 2)


def old_common_cost(h: int) -> int:
    return h * c2(h - 2) if 4 <= h <= 13 else 0


def gamma_cost(h: int) -> int:
    return h * GAMMA[h] if 4 <= h <= 13 else 0


def lower_costs(h: int) -> tuple[int, ...]:
    return (
        pair_cost(h),
        mod13_cost(h),
        old_common_cost(h),
        gamma_cost(h),
        *(h * charges[h] if h <= 13 else 0 for _, _, _, charges, _ in FOUR_CUTS),
    )


RESOURCE_TABLES = tuple(tuple(lower_costs(h)[i] for h in range(16)) for i in range(8))
RESOURCE_INCREMENTS = tuple(
    tuple(table[h + 1] - table[h] for table in RESOURCE_TABLES) for h in range(15)
)


def verify_discrete_convexity() -> None:
    previous = None
    for h in range(1, 13):
        current = RESOURCE_INCREMENTS[h]
        require(all(x >= 0 for x in current), f"negative resource increment at h={h}")
        if previous is not None:
            require(all(x <= y for x, y in zip(previous, current)), f"nonconvex resource at h={h}")
        previous = current


def old_lower_budgets(n15: int, n14: int) -> tuple[int, int]:
    _, _, const_a, q_a = OLD_CUTS[0]
    _, _, const_b, q_b = OLD_CUTS[1]
    _, _, const_c, q_c = OLD_CUTS[2]
    common = min(
        c2(n15) + LIST * const_a - 15 * q_a[15] * n15 - 14 * q_a[14] * n14,
        c2(n14) + LIST * const_b - 15 * q_b[15] * n15 - 14 * q_b[14] * n14,
    )
    gamma = c2(n15) + LIST * const_c - 15 * q_c[15] * n15 - 14 * q_c[14] * n14
    return common, gamma


def branch_max_incidence(hstar: int, full15: int, full14: int) -> int | None:
    residual_cost = tuple(table[hstar] for table in RESOURCE_TABLES)
    n15 = full15 + int(hstar == 15)
    n14 = full14 + int(hstar == 14)
    old1, old2 = old_lower_budgets(n15, n14)
    if old1 < 0 or old2 < 0:
        return None

    fixed_pair = residual_cost[0] + 105 * full15 + 91 * full14
    fixed_mod = residual_cost[1] + 195 * full15 + 168 * full14
    if fixed_pair > PAIR_BUDGET or fixed_mod > MOD13_BUDGET:
        return None

    budgets = [
        PAIR_BUDGET - fixed_pair,
        MOD13_BUDGET - fixed_mod,
        old1 - residual_cost[2],
        old2 - residual_cost[3],
    ]
    for index, (_, alpha, beta, charges, _) in enumerate(FOUR_CUTS, start=4):
        budgets.append(
            alpha * c2(n15)
            + LIST * beta
            - 15 * charges[15] * n15
            - 14 * charges[14] * n14
            - residual_cost[index]
        )
    if any(x < 0 for x in budgets):
        return None

    low = F_FULL - full15 - full14
    if low < 0 or (hstar >= 14 and low):
        return None
    if low == 0:
        return 15 * full15 + 14 * full14

    remaining = [budget - low * table[hstar] for budget, table in zip(budgets, RESOURCE_TABLES)]
    if any(x < 0 for x in remaining):
        return None

    upgrades = 0
    for h in range(hstar, 13):
        step = RESOURCE_INCREMENTS[h]
        number = low
        for i, increment in enumerate(step):
            if increment:
                number = min(number, remaining[i] // increment)
        upgrades += number
        for i, increment in enumerate(step):
            remaining[i] -= number * increment
        if number < low:
            break
    return 15 * full15 + 14 * full14 + low * hstar + upgrades


def base_max_table() -> dict[int, int]:
    table = {}
    for hstar in range(1, 16):
        best = -1
        for full15 in range(F_FULL + 1):
            for full14 in range(F_FULL - full15 + 1):
                value = branch_max_incidence(hstar, full15, full14)
                if value is not None:
                    best = max(best, value)
        require(best >= 0, f"no base profile for hstar={hstar}")
        table[hstar] = best
    return table


EXPECTED_BASE_MAX = {
    1: 3271,
    2: 3271,
    3: 3271,
    4: 3271,
    5: 3271,
    6: 3270,
    7: 3270,
    8: 3269,
    9: 3269,
    10: 3268,
    11: 3267,
    12: 3266,
    13: 3265,
    14: 3254,
    15: 3253,
}


def candidate_pairs(hstar: int, required_incidence: int) -> tuple[tuple[int, int, int], ...]:
    pairs = []
    for full15 in range(F_FULL + 1):
        for full14 in range(F_FULL - full15 + 1):
            maximum = branch_max_incidence(hstar, full15, full14)
            if maximum is not None and maximum >= required_incidence:
                pairs.append((full15, full14, maximum))
    return tuple(pairs)


def base_profile_valid(n: tuple[int, ...] | list[int]) -> bool:
    if sum(pair_cost(h) * n[h] for h in range(16)) > PAIR_BUDGET:
        return False
    if sum(mod13_cost(h) * n[h] for h in range(16)) > MOD13_BUDGET:
        return False
    for _, target, constant, charges in OLD_CUTS:
        if c2(n[target]) + LIST * constant < sum(h * charges[h] * n[h] for h in range(16)):
            return False
    for _, alpha, beta, charges, _ in FOUR_CUTS:
        if alpha * c2(n[15]) + LIST * beta < sum(h * charges[h] * n[h] for h in range(16)):
            return False
    return True


def local_dual_value(r: dict[int, int]) -> int:
    value = DUAL_B + sum(DUAL_C[h] * r[h] for h in HIGH_CLASSES)
    for (h, k), coefficient in DUAL_L.items():
        value += coefficient * (c2(r[h]) if h == k else r[h] * r[k])
    return value


def verify_cross_local_cut() -> tuple[int, int, tuple[int, ...]]:
    r = {h: 0 for h in HIGH_CLASSES}
    types = 0
    minimum = None
    tight = None

    def rec(index: int, capacity: int) -> None:
        nonlocal types, minimum, tight
        if index == len(HIGH_CLASSES):
            types += 1
            value = local_dual_value(r)
            vector = tuple(r[h] for h in HIGH_CLASSES)
            if minimum is None or value < minimum:
                minimum, tight = value, vector
            return
        h = HIGH_CLASSES[index]
        for x in range(capacity // (h - 1) + 1):
            r[h] = x
            rec(index + 1, capacity - (h - 1) * x)
        r[h] = 0

    rec(0, POINT_CAPACITY)
    require((types, minimum, tight) == (139_979, 0, (1, 2, 0, 0, 0, 13)), "cross-local cut changed")
    return types, minimum, tight


def global_dual(n: tuple[int, ...] | list[int]) -> int:
    value = LIST * DUAL_B + sum(DUAL_C[h] * h * n[h] for h in HIGH_CLASSES)
    for (h, k), coefficient in DUAL_L.items():
        value += coefficient * (c2(n[h]) if h == k else n[h] * n[k])
    return value


def scan_level(hstar: int, full_incidence: int) -> tuple[int, int, int, int, tuple[int, ...]]:
    pairs = candidate_pairs(hstar, full_incidence)
    raw = 0
    valid = 0
    maximum_dual = None
    argmax = None

    for full15, full14, _ in pairs:
        low_count = F_FULL - full15 - full14
        low_incidence = full_incidence - 15 * full15 - 14 * full14
        if not hstar * low_count <= low_incidence <= 13 * low_count:
            continue
        deficit = 13 * low_count - low_incidence
        occupancies = list(range(hstar, 13))
        counts = [0] * 16
        counts[15] = full15
        counts[14] = full14

        def rec(index: int, remaining_deficit: int, used: int) -> None:
            nonlocal raw, valid, maximum_dual, argmax
            if index == len(occupancies):
                if remaining_deficit == 0 and used <= low_count:
                    counts[13] = low_count - used
                    total = counts.copy()
                    total[hstar] += 1  # the residual-weight line
                    raw += 1
                    require(sum(total) == F_FULL + 1, "line count mismatch")
                    require(sum(h * total[h] for h in range(16)) - hstar == full_incidence, "incidence mismatch")
                    if base_profile_valid(total):
                        valid += 1
                        value = global_dual(total)
                        if maximum_dual is None or value > maximum_dual:
                            maximum_dual = value
                            argmax = tuple(total)
                    counts[13] = 0
                return

            h = occupancies[index]
            weight = 13 - h
            maximum_x = min(low_count - used, remaining_deficit // weight)
            for x in range(maximum_x + 1):
                next_deficit = remaining_deficit - weight * x
                next_used = used + x
                if next_deficit > (weight - 1) * (low_count - next_used):
                    continue
                counts[h] = x
                rec(index + 1, next_deficit, next_used)
            counts[h] = 0

        rec(0, deficit, 0)

    require(maximum_dual is not None and argmax is not None, f"empty valid layer h={hstar},I={full_incidence}")
    return len(pairs), raw, valid, maximum_dual, argmax


EXPECTED_EXCLUSIONS = {
    (1, 3271): (22, 475_222, 1_794, -391_258_072_517),
    (2, 3271): (22, 409_938, 1_794, -391_258_072_517),
    (3, 3271): (22, 338_424, 1_697, -404_831_192_365),
    (4, 3271): (21, 238_869, 1_401, -433_187_185_481),
    (5, 3271): (7, 83_530, 139, -452_126_071_483),
    (5, 3270): (376, 1_173_441, 39_146, -1_451_438_908),
    (6, 3270): (289, 460_065, 18_335, -115_317_627_970),
    (7, 3270): (43, 88_417, 3_839, -292_322_393_595),
    (9, 3269): (79, 24_479, 7_340, -70_252_622_671),
    (10, 3268): (282, 14_559, 10_054, -69_336_287_784),
    (12, 3266): (274, 274, 274, -196_918_848_509),
    (13, 3265): (7, 7, 7, -743_676_930_267),
    (13, 3264): (19, 12, 12, -559_314_260_159),
    (13, 3263): (38, 19, 19, -366_887_862_827),
}

EXPECTED_AUGMENTED_MAX = {
    1: 3270,
    2: 3270,
    3: 3270,
    4: 3270,
    5: 3269,
    6: 3269,
    7: 3269,
    8: 3269,
    9: 3268,
    10: 3267,
    11: 3267,
    12: 3265,
    13: 3262,
    14: 3254,
    15: 3253,
}

# Total line counts, including the one residual-weight line of class hstar.
WITNESSES = {
    1: ({1: 1, 11: 17, 13: 8, 14: 21, 15: 179}, 2_990_047_298),
    2: ({2: 1, 11: 17, 13: 8, 14: 21, 15: 179}, 2_990_047_298),
    3: ({3: 1, 11: 17, 13: 8, 14: 21, 15: 179}, 2_990_047_298),
    4: ({4: 1, 9: 4, 10: 6, 13: 23, 14: 5, 15: 187}, 46_334_353_108),
    5: ({5: 1, 11: 12, 12: 2, 13: 14, 14: 24, 15: 173}, 21_239_393_791),
    6: ({6: 1, 11: 13, 13: 16, 14: 22, 15: 174}, 7_016_691_767),
    7: ({7: 1, 11: 13, 12: 2, 13: 13, 14: 22, 15: 175}, 28_363_238_775),
    8: ({8: 1, 11: 14, 12: 1, 13: 14, 14: 19, 15: 177}, 191_130_771),
    9: ({9: 1, 11: 11, 13: 22, 14: 19, 15: 173}, 10_533_988_435),
    10: ({10: 1, 11: 10, 12: 2, 13: 20, 14: 22, 15: 171}, 14_883_517_338),
    11: ({11: 15, 12: 2, 13: 14, 14: 18, 15: 177}, 4_485_040_150),
    12: ({12: 27, 13: 14, 14: 4, 15: 181}, 7_531_501_031),
    13: ({13: 28, 14: 59, 15: 139}, 266_244_560_419),
    14: ({14: 122, 15: 104}, 4_836_956_426_006),
    15: ({14: 122, 15: 104}, 4_836_956_426_006),
}


def verify_augmented_optimizer(base: dict[int, int]) -> tuple[dict[tuple[int, int], tuple[int, int, int, int]], dict[int, int]]:
    scans = {}
    for key, expected in EXPECTED_EXCLUSIONS.items():
        pairs, raw, valid, maximum_dual, _ = scan_level(*key)
        result = (pairs, raw, valid, maximum_dual)
        require(result == expected, f"layer scan changed at {key}: {result}")
        require(maximum_dual < 0, f"dual failed to exclude {key}")
        scans[key] = result

    augmented = {}
    for hstar in range(1, 16):
        claimed = EXPECTED_AUGMENTED_MAX[hstar]
        require(claimed <= base[hstar], f"augmented maximum exceeds base at h={hstar}")
        for incidence in range(base[hstar], claimed, -1):
            require((hstar, incidence) in scans, f"missing exclusion layer h={hstar},I={incidence}")

        sparse, expected_dual = WITNESSES[hstar]
        total = [0] * 16
        for h, number in sparse.items():
            total[h] = number
        require(total[hstar] >= 1, f"witness lacks residual line h={hstar}")
        require(sum(total) == F_FULL + 1, f"witness line count changed h={hstar}")
        require(sum(h * total[h] for h in range(16)) - hstar == claimed, f"witness incidence changed h={hstar}")
        require(base_profile_valid(total), f"witness violates inherited cuts h={hstar}")
        require(global_dual(total) == expected_dual >= 0, f"witness dual changed h={hstar}")
        augmented[hstar] = claimed

    require(augmented == EXPECTED_AUGMENTED_MAX, "augmented optimizer table changed")
    return scans, augmented


def state_data(u: int, augmented: dict[int, int]) -> tuple[int, int, int, int, int, int, int]:
    degree = K - 1 - u
    residual_n = N_TOTAL - u
    full, residual_weight = divmod(residual_n, degree)
    require(full == F_FULL and 0 < residual_weight < degree, f"weight decomposition changed at u={u}")
    target = LIST * (M_AGREE - u)
    values = [(degree * augmented[h] + residual_weight * h, h) for h in range(1, 16)]
    capacity, hstar = max(values)
    return degree, residual_n, full, residual_weight, target, capacity, hstar


def target_layers(u: int, base: dict[int, int]) -> tuple[tuple[int, int], ...]:
    degree = K - 1 - u
    residual_n = N_TOTAL - u
    full, residual_weight = divmod(residual_n, degree)
    require(full == F_FULL, "unexpected number of full directions")
    target = LIST * (M_AGREE - u)
    layers = []
    for hstar in range(1, 16):
        required = ceil_div(target - residual_weight * hstar, degree)
        for incidence in range(required, base[hstar] + 1):
            layers.append((hstar, incidence))
    return tuple(layers)


EXPECTED_TARGET_LAYERS = {
    1_043_901: ((4, 3271), (5, 3271), (7, 3270)),
    1_043_900: ((3, 3271), (4, 3271), (5, 3271), (6, 3270), (7, 3270)),
    1_043_899: (
        (1, 3271),
        (2, 3271),
        (3, 3271),
        (4, 3271),
        (5, 3270),
        (5, 3271),
        (6, 3270),
        (7, 3270),
        (9, 3269),
    ),
}

EXPECTED_STATES = {
    1_043_901: (4674, 1_053_251, 225, 1601, 15_294_952, 15_292_114, 8, -2838),
    1_043_900: (4675, 1_053_252, 225, 1377, 15_295_164, 15_293_591, 8, -1573),
    1_043_899: (4676, 1_053_253, 225, 1153, 15_295_376, 15_295_132, 4, -244),
    1_043_898: (4677, 1_053_254, 225, 929, 15_295_588, 15_297_506, 4, 1918),
}


def wall_slacks() -> dict[str, int]:
    sparse = WITNESSES[4][0]
    n = [0] * 16
    for h, number in sparse.items():
        n[h] = number
    slacks = {
        "pair": PAIR_BUDGET - sum(pair_cost(h) * n[h] for h in range(16)),
        "mod13": MOD13_BUDGET - sum(mod13_cost(h) * n[h] for h in range(16)),
    }
    for name, target, constant, charges in OLD_CUTS:
        slacks[name] = c2(n[target]) + LIST * constant - sum(h * charges[h] * n[h] for h in range(16))
    for name, alpha, beta, charges, _ in FOUR_CUTS:
        slacks[name] = alpha * c2(n[15]) + LIST * beta - sum(h * charges[h] * n[h] for h in range(16))
    slacks["cross"] = global_dual(n)
    expected = {
        "pair": 62,
        "mod13": 6,
        "A": 1321,
        "B": 4915,
        "C": 101,
        "C1": 25_830,
        "C2": 94_080,
        "C3": 1_085,
        "C4": 7_920,
        "cross": 46_334_353_108,
    }
    require(slacks == expected, f"wall slacks changed: {slacks}")
    return slacks


def johnson_bound(u: int) -> int | None:
    residual_n = N_TOTAL - u
    residual_a = M_AGREE - u
    denominator = residual_a * residual_a - residual_n * (K - 1 - u)
    if denominator <= 0:
        return None
    return residual_n * (M_AGREE - K + 1) // denominator


def replay_parent() -> tuple[tuple[tuple[int, int, int, int], ...], int, int, int]:
    old_previous = [1] * (K + 2)
    new_previous = [1] * (K + 2)
    rows = []

    for dimension in range(1, 16):
        upper = K - dimension
        old_current = [0] * (K + 2)
        new_current = [0] * (K + 2)
        old_suffix = 0
        new_suffix = 0
        changed_count = 0
        first_changed = -1
        last_changed = -1
        maximum_drop = 0

        for u in range(upper, -1, -1):
            old_candidate = (N_TOTAL - u) * old_previous[u + 1] // (M_AGREE - u)
            new_candidate = (N_TOTAL - u) * new_previous[u + 1] // (M_AGREE - u)
            johnson = johnson_bound(u)
            if johnson is not None:
                old_candidate = min(old_candidate, johnson)
                new_candidate = min(new_candidate, johnson)
            if dimension == 2:
                if 1_043_771 <= u <= 1_043_948:
                    old_candidate = min(old_candidate, 217)
                    new_candidate = min(new_candidate, 217)
                if 1_043_902 <= u <= 1_043_957:
                    old_candidate = min(old_candidate, 211)
                    new_candidate = min(new_candidate, 211)
                if 1_043_899 <= u <= 1_043_901:
                    new_candidate = min(new_candidate, 211)

            old_suffix = max(old_suffix, old_candidate)
            new_suffix = max(new_suffix, new_candidate)
            old_current[u] = old_suffix
            new_current[u] = new_suffix
            if old_suffix != new_suffix:
                changed_count += 1
                first_changed = u if first_changed < 0 else min(first_changed, u)
                last_changed = max(last_changed, u)
                maximum_drop = max(maximum_drop, old_suffix - new_suffix)

        rows.append((dimension, changed_count, first_changed, last_changed, maximum_drop))
        old_previous, new_previous = old_current, new_current

    expected_rows = [(d, 0, -1, -1, 0) for d in range(1, 16)]
    expected_rows[1] = (2, 3, 1_043_899, 1_043_901, 5)
    require(rows == expected_rows, f"recurrence delta changed: {rows}")
    old_final = old_previous[0]
    new_final = new_previous[0]
    require(old_final == new_final == EXPECTED_PARENT, "rank-15 parent changed")
    gap = new_final - TARGET_PARENT
    require(gap == 8_185_190_237_340_452, "parent gap changed")
    return tuple(rows), old_final, new_final, gap


def compact_sparse(sparse: dict[int, int]) -> str:
    return ",".join(f"n{h}={sparse[h]}" for h in sorted(sparse, reverse=True))


def compact_table(table: dict[int, int]) -> str:
    return ",".join(f"h{h}:{table[h]}" for h in range(1, 16))


def main() -> None:
    require((P, N_TOTAL, K, M_AGREE, LIST) == (2_130_706_433, 2_097_152, 1_048_576, 1_116_047, 212), "parameters changed")
    section = rank_one_bound(1_043_900)
    require(section == (15, 1_045_969, 1_048_575, 2607), f"section cap changed: {section}")
    old_audits = verify_old_local_cuts()
    four_audits = verify_four_local_cuts()
    verify_discrete_convexity()
    local_types, local_minimum, local_tight = verify_cross_local_cut()

    base = base_max_table()
    require(base == EXPECTED_BASE_MAX, f"base optimizer changed: {base}")
    scans, augmented = verify_augmented_optimizer(base)

    for u, expected in EXPECTED_STATES.items():
        data = state_data(u, augmented)
        result = (*data, data[5] - data[4])
        require(result == expected, f"state changed at u={u}: {result}")

    for u, expected in EXPECTED_TARGET_LAYERS.items():
        layers = target_layers(u, base)
        require(layers == expected, f"target layer set changed at u={u}: {layers}")
        require(all(layer in scans for layer in layers), f"uncertified target layer at u={u}")

    slacks = wall_slacks()
    replay_rows, old_final, new_final, gap = replay_parent()

    print("RANK15_U1043899_CROSSCLASS_EXTENSION")
    print(f"parameters=p{P},n{N_TOTAL},K{K},m{M_AGREE},M{LIST}")
    print(f"section_cap={section[0]};maximizers={section[1]}..{section[2]};count={section[3]}")
    for name, cases, minimum, zeros in old_audits:
        print(f"old_local_cut={name};cases={cases};minimum_slack={minimum};zero_j={','.join(map(str, zeros))}")
    for name, cases, minimum, zeros in four_audits:
        print(f"four_local_cut={name};cases={cases};minimum_slack={minimum};zero_j={','.join(map(str, zeros))}")
    print("discrete_convex_exchange=PASS;resources=8;occupancies=1..13")
    print(f"cross_local_cut=PASS;types={local_types};minimum_slack={local_minimum};unique_tight={','.join(map(str, local_tight))}")
    print(f"base_full_incidence_max={compact_table(base)}")
    for hstar, incidence in sorted(EXPECTED_EXCLUSIONS):
        pairs, raw, valid, maximum_dual = scans[(hstar, incidence)]
        print(f"EXCLUDED hstar={hstar};incidence={incidence};pairs={pairs};raw={raw};base_valid={valid};max_global_dual={maximum_dual}")
    print(f"augmented_full_incidence_max={compact_table(augmented)}")
    for u in (1_043_901, 1_043_900, 1_043_899, 1_043_898):
        degree, residual_n, full, residual_weight, target, capacity, hstar = state_data(u, augmented)
        print(
            f"STATE u={u};lambda={degree};N={residual_n};decomposition={full}*{degree}+{residual_weight};"
            f"hstar={hstar};capacity={capacity};target={target};margin={capacity-target:+d}"
        )
    for u in (1_043_901, 1_043_900, 1_043_899):
        layers = EXPECTED_TARGET_LAYERS[u]
        print(f"TARGET_LAYERS u={u};count={len(layers)};layers={','.join(f'h{h}:I{inc}' for h,inc in layers)}")
    print(f"exact_new_wall=u1043898;profile={compact_sparse(WITNESSES[4][0])};full_incidence=3270;margin=+1918")
    print("wall_slacks=" + ",".join(f"{name}:{value}" for name, value in slacks.items()))
    print("combined_theorem=D2[1043899..1043957]<=211;new_children=1043899..1043901;inherited=1043902..1043957")
    print(f"parent_replay=D2_changed={replay_rows[1][1]};range={replay_rows[1][2]}..{replay_rows[1][3]};max_drop={replay_rows[1][4]};dimensions3to15_changed=0")
    print(f"rank15_final_old={old_final};rank15_final_new={new_final};target={TARGET_PARENT};gap={gap}")
    print("NONCLAIMS=u<=1043898,source_counterexample,parent_saving,rank16,Grand_List,Grand_MCA,score_movement")
    print("RESULT: PASS")


if __name__ == "__main__":
    main()
