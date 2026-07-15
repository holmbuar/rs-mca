#!/usr/bin/env python3
"""Exact standard-library replay for the Role-07 dyadic full-fiber route cut."""

from math import comb, isqrt

p = 2_130_706_433
n = 2_097_152
K = 1_048_576
sigma = 67_471
m = K + sigma
t = n - m

if p < 2 or any(p % d == 0 for d in range(2, isqrt(p) + 1)):
    raise RuntimeError("p is not prime")
if p - 1 != 1_016 * n:
    raise RuntimeError("deployed subgroup divisibility mismatch")

B_star = p**6 // 2**128
challenge_remainder = p**6 - B_star * 2**128
if challenge_remainder != 301_186_360_634_199_111_531_904_678_745_128_042_497:
    raise RuntimeError("p^6 denominator remainder mismatch")
if not 0 <= challenge_remainder < 2**128:
    raise RuntimeError("invalid p^6 Euclidean remainder")

T = ((B_star + 1) * (p - n + m) - 1) // p
target_safe_gap = (B_star + 1) * (p - n + m) - p * T
target_next_gap = p * (T + 1) - (B_star + 1) * (p - n + m)

if target_safe_gap != 79_209_528 or target_next_gap != 2_051_496_905:
    raise RuntimeError("closed target seam mismatch")
if p * T // (p - t) != B_star or p * (T + 1) // (p - t) != B_star + 1:
    raise RuntimeError("target floor transition mismatch")


def subset_cap(N: int, e: int, h: int) -> int:
    """(h+1)-subset packing for e-subsets with pairwise intersection <= h."""
    return comb(N, h + 1) // comb(e, h + 1)


def johnson_cap(N: int, e: int, h: int) -> tuple[int, int]:
    """Disjoint-radius Johnson-ball packing in J(N,e)."""
    minimum_distance = e - h
    radius = (minimum_distance - 1) // 2
    ball = sum(comb(e, i) * comb(N - e, i) for i in range(radius + 1))
    return comb(N, e) // ball, ball


# First disjoint category: e_15 >= 33.
N15 = n // 2**15
h15 = (K - 1) // 2**15
if (N15, h15, m // 2**15) != (64, 31, 34):
    raise RuntimeError("unexpected level-15 parameters")

cap_15_33 = subset_cap(N15, 33, h15)
cap_15_34, ball_15_34 = johnson_cap(N15, 34, h15)
if cap_15_33 != 55_534_064_877_048_198:
    raise RuntimeError("level-15 e=33 cap mismatch")
if ball_15_34 != 1_021 or cap_15_34 != 1_586_961_812_468_508:
    raise RuntimeError("level-15 e=34 cap mismatch")

# Second disjoint category: e_15 <= 32 and e_16 >= 16.
N16 = n // 2**16
h16 = (K - 1) // 2**16
if (N16, h16, m // 2**16) != (32, 15, 17):
    raise RuntimeError("unexpected level-16 parameters")

cap_16_16 = subset_cap(N16, 16, h16)
if cap_16_16 != 601_080_390:
    raise RuntimeError("level-16 e=16 cap mismatch")

U_dyadic = cap_15_33 + cap_15_34 + cap_16_16
T_minus_U = T - U_dyadic
residual_if_violator = T + 1 - U_dyadic

if U_dyadic != 57_121_027_290_597_096:
    raise RuntimeError("optimized aggregate mismatch")
if T_minus_U != 217_733_083_205_590_496:
    raise RuntimeError("optimized slack mismatch")
if residual_if_violator != 217_733_083_205_590_497:
    raise RuntimeError("optimized residual mismatch")

profile_max = (32, 15, 7, 3, 1, 0)

tuples: list[tuple[int, int, int, int, int, int]] = []
for e20 in range(profile_max[5] + 1):
    for e19 in range(profile_max[4] + 1):
        if e19 < 2 * e20:
            continue
        for e18 in range(profile_max[3] + 1):
            if e18 < 2 * e19:
                continue
            for e17 in range(profile_max[2] + 1):
                if e17 < 2 * e18:
                    continue
                for e16 in range(profile_max[1] + 1):
                    if e16 < 2 * e17:
                        continue
                    for e15 in range(profile_max[0] + 1):
                        if e15 < 2 * e16:
                            continue
                        tuples.append((e15, e16, e17, e18, e19, e20))

if len(tuples) != 1_792:
    raise RuntimeError("tuple count mismatch")

fixed_tuple_sublist = (
    residual_if_violator + len(tuples) - 1
) // len(tuples)
if fixed_tuple_sublist != 121_502_836_610_263:
    raise RuntimeError("fixed-tuple pigeonhole mismatch")

per_tuple_sufficient_cap = fixed_tuple_sublist - 1
aggregate_under_sufficient_cap = (
    len(tuples) * per_tuple_sufficient_cap
)

if aggregate_under_sufficient_cap != 217_733_083_205_589_504:
    raise RuntimeError("per-tuple aggregate mismatch")
if T_minus_U - aggregate_under_sufficient_cap != 992:
    raise RuntimeError("per-tuple closing margin mismatch")

print(f"p={p}")
print(f"n={n},K={K},sigma={sigma},m={m},t={t}")
print(f"B_star={B_star}")
print(f"challenge_remainder={challenge_remainder}")
print(f"T={T}")
print(f"target_safe_gap={target_safe_gap}")
print(f"target_next_gap={target_next_gap}")
print("disjoint_category,cap")
print(f"e32768=33,{cap_15_33}")
print(f"e32768=34,{cap_15_34}")
print(f"e32768<=32_and_e65536=16,{cap_16_16}")
print(f"U_dyadic={U_dyadic}")
print(f"T_minus_U={T_minus_U}")
print(f"residual_if_L_ge_T_plus_1={residual_if_violator}")
print(
    "residual_profile="
    "e32768<=32,e65536<=15,e131072<=7,"
    "e262144<=3,e524288<=1,e1048576=0"
)
print(f"admissible_residual_full_fiber_tuples={len(tuples)}")
print(f"fixed_tuple_sublist_if_L_ge_T_plus_1={fixed_tuple_sublist}")
print(f"uniform_per_tuple_cap_sufficient={per_tuple_sufficient_cap}")
print(
    "closing_margin_after_addback="
    f"{T_minus_U - aggregate_under_sufficient_cap}"
)
print("VERIFIED")
