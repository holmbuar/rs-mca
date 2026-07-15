#!/usr/bin/env ruby
# frozen_string_literal: true

# Exact Johnson-scheme/Hahn Delsarte LP certificate at one fixed deployed
# Grand List state.

N_CODE = 2_097_152
K_CODE = 1_048_576
M_AGREE = 1_116_047
U_STATE = 1_043_460
TARGET = 274_854_110_496_187_592

N_RESIDUAL = N_CODE - U_STATE
WEIGHT = M_AGREE - U_STATE
INTERSECTION_CAP = K_CODE - U_STATE - 1
MIN_DISTANCE = WEIGHT - INTERSECTION_CAP

ACTIVE_DISTANCES = [67_472, 67_586, 67_587, 67_700, 67_701].freeze
EXPECTED_FLOOR = 41_358_983_685_320_209

def check(condition, message)
  raise message unless condition
end

def choose(n, k)
  return 0 if k.negative? || k > n

  k = [k, n - k].min
  (1..k).inject(1) { |value, index| value * (n - k + index) / index }
end

# Normalized Hahn zonal function of Johnson eigenspace j.  This is the
# normalization H_j(0)=1; the kernel H_j(dist(A,B)) is positive semidefinite
# on the a-subsets of an N-set.
def hahn(j, distance)
  (0..j).sum do |t|
    Rational(
      (-1)**t * choose(j, t) * choose(N_RESIDUAL + 1 - j, t) *
        choose(distance, t),
      choose(WEIGHT, t) * choose(N_RESIDUAL - WEIGHT, t)
    )
  end
end

def solve_linear(matrix, rhs)
  n = rhs.length
  n.times do |column|
    pivot = (column...n).find { |row| !matrix[row][column].zero? }
    raise "singular active-constraint matrix" unless pivot

    matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
    rhs[column], rhs[pivot] = rhs[pivot], rhs[column]
    scale = matrix[column][column]
    (column...n).each { |j| matrix[column][j] /= scale }
    rhs[column] /= scale

    n.times do |row|
      next if row == column

      factor = matrix[row][column]
      next if factor.zero?

      (column...n).each do |j|
        matrix[row][j] -= factor * matrix[column][j]
      end
      rhs[row] -= factor * rhs[column]
    end
  end
  rhs
end

check([N_RESIDUAL, WEIGHT, INTERSECTION_CAP, MIN_DISTANCE] ==
      [1_053_692, 72_587, 5_115, 67_472],
      "fixed-state parameters")
check(M_AGREE > K_CODE - 1, "selected-support injectivity gate")
check((1..5).all? { |j| hahn(j, 0) == 1 }, "Hahn normalization")
check(ACTIVE_DISTANCES.first == MIN_DISTANCE,
      "first active distance is not the minimum")

degrees = (1..5).to_a
matrix = ACTIVE_DISTANCES.map do |distance|
  degrees.map { |degree| hahn(degree, distance) }
end
coefficients = solve_linear(matrix, Array.new(5, Rational(-1, 1)))
check(coefficients.all?(&:positive?), "nonpositive Hahn LP coefficient")

lp_value = lambda do |distance|
  1 + degrees.each_with_index.sum do |degree, index|
    coefficients[index] * hahn(degree, distance)
  end
end

zeros = []
positive_distances = []
(MIN_DISTANCE..WEIGHT).each do |distance|
  value = lp_value.call(distance)
  zeros << distance if value.zero?
  positive_distances << distance if value.positive?
end
check(zeros == ACTIVE_DISTANCES, "Hahn LP zero set mismatch")
check(positive_distances.empty?, "Hahn LP sign failure on allowed distance")

finite_differences = (0..5).map { |distance| lp_value.call(distance) }
5.times do
  finite_differences = finite_differences.each_cons(2).map do |left, right|
    right - left
  end
end
check(finite_differences.length == 1 && finite_differences.first.negative?,
      "Hahn LP leading coefficient is not negative")

# With constant coefficient one and H_j(0)=1, Delsarte gives
# |C|<=F(0)=1+sum_j f_j.
bound = 1 + coefficients.sum
check(bound.floor == EXPECTED_FLOOR, "Hahn LP floor mismatch")
check(bound < TARGET, "Hahn LP does not pay literal target")
check(EXPECTED_FLOOR < TARGET, "integer target comparison")

# The roots after the minimum distance occur in adjacent integer pairs.  This
# is the discrete Johnson-scheme improvement: no allowed integer distance lies
# in either positive real interval between those adjacent roots.
check(ACTIVE_DISTANCES[2] == ACTIVE_DISTANCES[1] + 1,
      "first adjacent-root pair")
check(ACTIVE_DISTANCES[4] == ACTIVE_DISTANCES[3] + 1,
      "second adjacent-root pair")

puts "RANK16_U1043460_HAHN_LP_PAYMENT: PASS"
puts "parameters=N#{N_RESIDUAL}_a#{WEIGHT}_h#{INTERSECTION_CAP}_d#{MIN_DISTANCE}"
puts "active_distances=#{ACTIVE_DISTANCES.join(',')}"
puts "coefficient_signs=#{coefficients.map { |value| value.positive? ? '+' : '-' }.join}"
puts "hahn_bound_floor=#{bound.floor} target=#{TARGET} margin=#{TARGET - bound.floor}"
puts "all_integer_distances_checked=#{WEIGHT - MIN_DISTANCE + 1}"
puts "line15_twoflat213_inputs_used=false"
puts "nonclaim=states_below_1043460_not_paid"
