#!/usr/bin/env ruby
# frozen_string_literal: true

# Exact primal/dual certificate for the full-distance Johnson/Hahn Delsarte LP
# at u=1,043,459, truncated only in Hahn degree at 32.

N_CODE = 2_097_152
K_CODE = 1_048_576
M_AGREE = 1_116_047
U_STATE = 1_043_459
TARGET = 274_854_110_496_187_592
MAX_DEGREE = 32

N_RESIDUAL = N_CODE - U_STATE
WEIGHT = M_AGREE - U_STATE
INTERSECTION_CAP = K_CODE - U_STATE - 1
MIN_DISTANCE = WEIGHT - INTERSECTION_CAP

ACTIVE_DISTANCES = [67_472, 67_586, 67_587, 67_700, 67_701, 72_588].freeze
DEGREE5_FARKAS_DISTANCES = [67_472, 67_582, 67_595, 67_690, 67_700, 67_709].freeze
PREVIOUS_ACTIVE_DISTANCES = [67_472, 67_586, 67_587, 67_700, 67_701].freeze
EXPECTED_FLOOR = 600_370_193_369_924_883

def check(condition, message)
  raise message unless condition
end

def choose(n, k)
  return 0 if k.negative? || k > n

  k = [k, n - k].min
  (1..k).inject(1) { |value, index| value * (n - k + index) / index }
end

# Normalized Johnson zonal function, H_j(0)=1.
def hahn(degree, distance)
  (0..degree).sum(Rational(0, 1)) do |t|
    Rational(
      (-1)**t * choose(degree, t) *
        choose(N_RESIDUAL + 1 - degree, t) * choose(distance, t),
      choose(WEIGHT, t) * choose(N_RESIDUAL - WEIGHT, t)
    )
  end
end

def solve_linear(matrix, rhs)
  n = rhs.length
  n.times do |column|
    pivot = (column...n).find { |row| !matrix[row][column].zero? }
    raise "singular matrix" unless pivot

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
      [1_053_693, 72_588, 5_116, 67_472], "state parameters")
check((1..MAX_DEGREE).all? { |degree| hahn(degree, 0) == 1 },
      "Hahn normalization")

# Degree 5 is not merely nonpaying: its full-distance primal is infeasible.
# A positive Farkas ray supported on six allowed distances annihilates all
# five primal columns A(i,j)=-H_j(i).
farkas_anchor = DEGREE5_FARKAS_DISTANCES.first
farkas_other = DEGREE5_FARKAS_DISTANCES.drop(1)
farkas_matrix = (1..5).map do |degree|
  farkas_other.map { |distance| -hahn(degree, distance) }
end
farkas_rhs = (1..5).map { |degree| hahn(degree, farkas_anchor) }
farkas_other_weights = solve_linear(farkas_matrix, farkas_rhs)
farkas_weights = [Rational(1, 1)] + farkas_other_weights
check(farkas_weights.all?(&:positive?), "degree-5 Farkas ray is not positive")
(1..5).each do |degree|
  annihilation = DEGREE5_FARKAS_DISTANCES.each_with_index.sum do |distance, index|
    farkas_weights[index] * -hahn(degree, distance)
  end
  check(annihilation.zero?, "degree-5 Farkas annihilation failure")
end
check(farkas_weights.sum.positive?, "zero Farkas ray")

# Exact degree-6 primal.  Every one of the 5,117 integer distance constraints
# is checked, so this is not an adjacent-root ansatz.
degrees = (1..6).to_a
primal_matrix = ACTIVE_DISTANCES.map do |distance|
  degrees.map { |degree| hahn(degree, distance) }
end
coefficients = solve_linear(primal_matrix, Array.new(6, Rational(-1, 1)))
check(coefficients.all?(&:positive?), "nonpositive primal coefficient")

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
check(zeros == ACTIVE_DISTANCES, "degree-6 zero set mismatch")
check(positive_distances.empty?, "degree-6 sign failure")

# Exact dual measure.  It is tight in degrees 1..6 and strictly feasible in
# every added degree 7..32, proving the degree-6 polynomial remains globally
# optimal in each of those full-distance truncations.
dual_matrix = degrees.map do |degree|
  ACTIVE_DISTANCES.map { |distance| -hahn(degree, distance) }
end
dual_weights = solve_linear(dual_matrix, Array.new(6, Rational(1, 1)))
check(dual_weights.all?(&:positive?), "nonpositive dual weight")

degrees.each do |degree|
  lhs = ACTIVE_DISTANCES.each_with_index.sum do |distance, index|
    dual_weights[index] * -hahn(degree, distance)
  end
  check(lhs == 1, "dual tightness failure")
end

dual_slacks = (7..MAX_DEGREE).to_h do |degree|
  lhs = ACTIVE_DISTANCES.each_with_index.sum do |distance, index|
    dual_weights[index] * -hahn(degree, distance)
  end
  [degree, 1 - lhs]
end
check(dual_slacks.values.all?(&:positive?), "dual feasibility failure")
minimum_slack_degree, minimum_slack = dual_slacks.min_by { |_degree, slack| slack }
check(minimum_slack_degree == 7 && minimum_slack > Rational(4, 5),
      "reduced-cost barrier mismatch")

bound = 1 + coefficients.sum
check(coefficients.sum == dual_weights.sum, "primal/dual objective mismatch")
check(bound.floor == EXPECTED_FLOOR, "LP floor mismatch")
check(bound > TARGET, "degree-32 truncation unexpectedly pays")

# The literal u=1,043,460 degree-5 support does not extend even one state.
# Re-solving on the same five roots at the new parameters flips every
# nonconstant coefficient negative and also violates the far endpoint.
previous_matrix = PREVIOUS_ACTIVE_DISTANCES.map do |distance|
  (1..5).map { |degree| hahn(degree, distance) }
end
previous_coefficients = solve_linear(
  previous_matrix, Array.new(5, Rational(-1, 1))
)
previous_at_endpoint = 1 + (1..5).each_with_index.sum do |degree, index|
  previous_coefficients[index] * hahn(degree, WEIGHT)
end
check(previous_coefficients.all?(&:negative?),
      "previous support did not flip coefficient signs")
check(previous_at_endpoint.positive?,
      "previous support unexpectedly satisfies new endpoint")

puts "RANK16_U1043459_HAHN_LP_DEGREE32_CUT: PASS"
puts "parameters=N#{N_RESIDUAL}_a#{WEIGHT}_h#{INTERSECTION_CAP}_d#{MIN_DISTANCE}"
puts "all_integer_distances_checked=#{WEIGHT - MIN_DISTANCE + 1}"
puts "degree5_status=exactly_infeasible farkas_support=#{DEGREE5_FARKAS_DISTANCES.join(',')}"
puts "optimal_active_distances=#{ACTIVE_DISTANCES.join(',')}"
puts "optimal_primal_degrees=#{degrees.join(',')}"
puts "exact_optimal_through_degree=#{MAX_DEGREE}"
puts "hahn_bound_floor=#{bound.floor} target=#{TARGET} excess=#{bound.floor - TARGET}"
puts "degree7_through_32_dual_slacks=all_strictly_positive"
puts "minimum_added_degree_slack=degree#{minimum_slack_degree},greater_than_4/5"
puts "u1043460_degree5_parametric_extension=false"
puts "nonclaim=degrees_above_32_not_excluded"
