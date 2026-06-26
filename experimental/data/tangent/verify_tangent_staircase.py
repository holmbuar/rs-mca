#!/usr/bin/env python3
"""Verify the arithmetic consequences of the high-agreement tangent staircase.

This script does not formalize the proof.  It checks the exact integer gates for
C = RS[GF(17^32), H, 256] with |H| = 512 under the finite-slope support-wise MCA
normalization.
"""
from fractions import Fraction

p = 17
field_degree = 32
q = p ** field_degree
n = 512
k = 256
eps_bits = 128

# The exact staircase theorem applies when 3a - 2n >= k.
a_min_exact = (2 * n + k + 2) // 3  # ceiling((2n+k)/3)
assert 3 * a_min_exact - 2 * n >= k
assert 3 * (a_min_exact - 1) - 2 * n < k

budget_floor = q // (2 ** eps_bits)
first_safe_agreement = n - budget_floor + 1
last_unsafe_agreement = first_safe_agreement - 1

print("High-agreement tangent staircase arithmetic")
print(f"q_line = 17^32 = {q}")
print(f"n = {n}, k = {k}")
print(f"exact-staircase range starts at a = ceil((2n+k)/3) = {a_min_exact}")
print(f"floor(q_line / 2^128) = {budget_floor}")
print(f"q_line - 6*2^128 = {q - 6 * 2**eps_bits}")
print(f"7*2^128 - q_line = {7 * 2**eps_bits - q}")
print()
for a in [353, 384, 427, 506, 507, 508, 512]:
    tangent = n - a + 1
    exact = a >= a_min_exact
    status = "exact" if exact else "lower-bound"
    eps_cmp = "<= 2^-128" if tangent <= budget_floor else "> 2^-128"
    print(f"a={a:3d}: LD_sw {status} value/floor = {tangent:3d}; tangent density {eps_cmp}")
print()
print(f"last unsafe agreement from exact staircase: a = {last_unsafe_agreement}, LD_sw = {n-last_unsafe_agreement+1}")
print(f"first safe agreement from exact staircase:  a = {first_safe_agreement}, LD_sw = {n-first_safe_agreement+1}")
print(f"largest safe integer distance = {n-first_safe_agreement}")
print(f"first unsafe integer distance = {n-last_unsafe_agreement}")
print(f"safe grid radius = {Fraction(n-first_safe_agreement, n)}")
print(f"unsafe grid radius = {Fraction(n-last_unsafe_agreement, n)}")

assert a_min_exact == 427
assert budget_floor == 6
assert n - 506 + 1 == 7
assert n - 507 + 1 == 6
assert 6 * 2**eps_bits < q < 7 * 2**eps_bits
assert first_safe_agreement == 507
assert last_unsafe_agreement == 506
