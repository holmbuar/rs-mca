#!/usr/bin/env python3
"""Dependency-free checks for the M1 packet-sift popularity digest."""

from __future__ import annotations

from fractions import Fraction


def ceil_fraction(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def comb2(k: int) -> int:
    return k * (k - 1) // 2


def packet_floor(k: int, s: int, overlap_cap: int) -> int:
    return ceil_fraction(Fraction(k * s * s, s + (k - 1) * overlap_cap))


def endpoint_floor(k: int, s: int, h: int, degree_cap: int, overlap_cap: int) -> int:
    denominator = k * s + 2 * k * h * (degree_cap - 1) * s
    denominator += k * (k - 1) * overlap_cap
    return ceil_fraction(Fraction(k * k * s * s, denominator))


def divisor_gate_cap(multiplicity: int, exceptional: int, degrees: list[int]) -> int:
    if multiplicity <= 0:
        raise ValueError("multiplicity must be positive")
    if exceptional < 0 or any(degree < 0 for degree in degrees):
        raise ValueError("negative gate parameter")
    return multiplicity * (exceptional + sum(degrees))


def degeneracy_bound(s: int, h: int, degree_cap: int, overlap_cap: int, pop_cap: int) -> int:
    return h * (2 * degree_cap - 1) * (s * pop_cap // (overlap_cap + 1))


def max_edges_from_degeneracy(k: int, d: int) -> int:
    if d >= k - 1:
        return comb2(k)
    return d * k - comb2(d + 1)


def popularity_floor(k: int, s: int, h: int, degree_cap: int, overlap_cap: int, pop_cap: int) -> int:
    d = degeneracy_bound(s, h, degree_cap, overlap_cap, pop_cap)
    denominator = k * s + 2 * k * h * (degree_cap - 1) * s
    denominator += k * (k - 1) * overlap_cap
    denominator += 2 * (s - overlap_cap) * max_edges_from_degeneracy(k, d)
    return ceil_fraction(Fraction(k * k * s * s, denominator))


def check_packet_and_endpoint_floors() -> None:
    checked = 0
    for k in range(2, 30):
        for s in range(1, 18):
            for overlap_cap in range(0, s + 1):
                floor = packet_floor(k, s, overlap_cap)
                if floor * (s + (k - 1) * overlap_cap) < k * s * s:
                    raise AssertionError(("packet floor", k, s, overlap_cap, floor))
                for h in range(1, 6):
                    for degree_cap in range(1, 8):
                        endpoint = endpoint_floor(k, s, h, degree_cap, overlap_cap)
                        denominator = k * s + 2 * k * h * (degree_cap - 1) * s
                        denominator += k * (k - 1) * overlap_cap
                        if endpoint * denominator < k * k * s * s:
                            raise AssertionError(("endpoint floor", k, s, h, degree_cap, overlap_cap))
                checked += 1
    print(f"packet_endpoint_floor_grid_checked={checked}")


def check_divisor_gate_and_equal_line_caps() -> None:
    for mu in range(1, 64):
        if divisor_gate_cap(mu, 6, [2]) != 8 * mu:
            raise AssertionError(("equal-line cap", mu))
    if divisor_gate_cap(2, 6, [2]) != 16:
        raise AssertionError("injective-z cap")
    for mu in range(1, 8):
        for exceptional in range(0, 8):
            for d0 in range(0, 6):
                for d1 in range(0, 6):
                    cap = divisor_gate_cap(mu, exceptional, [d0, d1])
                    if cap != mu * (exceptional + d0 + d1):
                        raise AssertionError(("divisor cap", mu, exceptional, d0, d1, cap))
    print("divisor_gate_caps_checked=3136")


def check_popularity_floor_monotonicity() -> None:
    checked = 0
    strict = 0
    for k in range(2, 24):
        for s in range(2, 14):
            for h in range(1, 5):
                for degree_cap in range(1, 7):
                    for overlap_cap in range(0, s):
                        strong = popularity_floor(k, s, h, degree_cap, overlap_cap, 16)
                        weak = popularity_floor(k, s, h, degree_cap, overlap_cap, 24)
                        if strong < weak:
                            raise AssertionError(("monotonicity", k, s, h, degree_cap, overlap_cap, strong, weak))
                        if strong > weak:
                            strict += 1
                        checked += 1
    if strict == 0:
        raise AssertionError("popularity floor never improves")
    print(f"popularity_floor_monotonicity_checked={checked}")
    print(f"strict_popularity_improvements={strict}")


def main() -> None:
    check_packet_and_endpoint_floors()
    check_divisor_gate_and_equal_line_caps()
    check_popularity_floor_monotonicity()
    print("m1 packet-sift popularity digest checks passed")


if __name__ == "__main__":
    main()
