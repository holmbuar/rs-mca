#!/usr/bin/env ruby
# frozen_string_literal: true

# Exact completion of the full Johnson-scheme Delsarte dual at u=1,043,459.
# It proves that the degree-six optimum remains optimal through every available
# Hahn degree, not merely through degree 32.

require "digest"

DEGREE32_SOURCE = File.expand_path("verify_rank16_u1043459_hahn_lp_degree32_cut.rb", __dir__)
DEGREE32_SHA = "ed0bda120c8a42eda7aa1c44f9e17101402daf017b12126d69e598fc72d0890f"

N = 1_053_693
A = 72_588
MIN_DISTANCE = 67_472
ACTIVE_DISTANCES = [67_472, 67_586, 67_587, 67_700, 67_701, 72_588].freeze
TARGET = 274_854_110_496_187_592
EXPECTED_FLOOR = 600_370_193_369_924_883
PREFIX_END = 644
TAIL_START = 645
MAX_DEGREE = [A, N - A].min

def check(condition, message)
  raise message unless condition
end

def choose(n, k)
  return 0 if k.negative? || k > n

  k = [k, n - k].min
  (1..k).inject(1) { |value, index| value * (n - k + index) / index }
end

def hahn(degree, distance)
  term = Rational(1, 1)
  sum = term
  (0...degree).each do |t|
    term *= Rational(
      -(degree - t) * (N + 1 - degree - t) * (distance - t),
      (t + 1) * (A - t) * (N - A - t)
    )
    sum += term
  end
  sum
end

# Generate H_0(i),...,H_max(i) in linear time via the standard Hahn
# three-term recurrence in the degree.  This keeps the exact prefix replay
# small enough for routine hostile audit.
def hahn_sequence(distance, maximum_degree)
  values = [Rational(1, 1), hahn(1, distance)]
  (1...maximum_degree).each do |degree|
    aa = Rational(
      (degree - N - 1) * (degree - A) * (N - A - degree),
      (2 * degree - N - 1) * (2 * degree - N)
    )
    cc = Rational(
      degree * (degree - A - 1) * (degree - (N - A) - 1),
      (2 * degree - N - 2) * (2 * degree - N - 1)
    )
    values << ((aa + cc - distance) * values[-1] - cc * values[-2]) / aa
  end
  values
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

      (column...n).each { |j| matrix[row][j] -= factor * matrix[column][j] }
      rhs[row] -= factor * rhs[column]
    end
  end
  rhs
end

check(Digest::SHA256.file(DEGREE32_SOURCE).hexdigest == DEGREE32_SHA,
      "degree-32 source hash mismatch")
check(MAX_DEGREE == 72_588, "maximum Hahn degree changed")

sequences = ACTIVE_DISTANCES.to_h do |distance|
  [distance, hahn_sequence(distance, PREFIX_END)]
end
(0..32).each do |degree|
  ACTIVE_DISTANCES.each do |distance|
    check(sequences.fetch(distance).fetch(degree) == hahn(degree, distance),
          "Hahn recurrence mismatch at degree #{degree}, distance #{distance}")
  end
end

dual_matrix = (1..6).map do |degree|
  ACTIVE_DISTANCES.map { |distance| -sequences.fetch(distance).fetch(degree) }
end
dual_weights = solve_linear(dual_matrix, Array.new(6, Rational(1, 1)))
check(dual_weights.all?(&:positive?), "nonpositive dual weight")
bound = 1 + dual_weights.sum
check(bound.floor == EXPECTED_FLOOR, "LP floor mismatch")
check(bound > TARGET, "full Hahn LP unexpectedly pays")
(1..6).each do |degree|
  lhs = ACTIVE_DISTANCES.each_with_index.sum do |distance, index|
    dual_weights[index] * -sequences.fetch(distance).fetch(degree)
  end
  check(lhs == 1, "dual tightness failure at degree #{degree}")
end

prefix_slacks = {}
(7..PREFIX_END).each do |degree|
  lhs = ACTIVE_DISTANCES.each_with_index.sum do |distance, index|
    dual_weights[index] * -sequences.fetch(distance).fetch(degree)
  end
  prefix_slacks[degree] = 1 - lhs
end
check(prefix_slacks.values.all?(&:positive?), "prefix reduced-cost failure")
prefix_min_degree, prefix_min_slack = prefix_slacks.min_by { |_degree, slack| slack }
check(prefix_min_degree == 7, "prefix minimum degree changed")

# Johnson orthogonality for the normalized kernels is
#   sum_i v_i H_j(i)^2 = |X|/m_j,
# where |X|=C(N,A), v_i=C(A,i)C(N-A,i), and
# m_j=C(N,j)-C(N,j-1).  Weighted Cauchy gives
#   |sum_i y_i H_j(i)|^2
#     <= (sum_i y_i^2/v_i)(sum_i v_i H_j(i)^2)
#     <= (sum_i y_i^2/v_i)|X|/m_j.
# Thus a strict upper bound below one proves positive reduced cost.
valencies = ACTIVE_DISTANCES.to_h do |distance|
  [distance, choose(A, distance) * choose(N - A, distance)]
end
minimum_distance, _minimum_valency = valencies.min_by { |_distance, value| value }
check(minimum_distance == A, "minimum active valency is not the endpoint")

space_size = choose(N, A)
multiplicity = choose(N, TAIL_START) - choose(N, TAIL_START - 1)
weighted_mass = ACTIVE_DISTANCES.each_with_index.sum(Rational(0, 1)) do |distance, index|
  dual_weights[index]**2 / valencies.fetch(distance)
end
tail_left = weighted_mass.numerator * space_size
tail_right = weighted_mass.denominator * multiplicity
check(tail_left < tail_right, "orthogonality tail inequality failed")
tail_margin = tail_right - tail_left

# m_j increases on this whole tail.  Indeed
# m_(j+1)/m_j =
# (N-2j-1)(N-j+1)/[(j+1)(N-2j+1)] > 1.
(TAIL_START...MAX_DEGREE).each do |degree|
  left = (N - 2 * degree - 1) * (N - degree + 1)
  right = (degree + 1) * (N - 2 * degree + 1)
  check(left > right, "multiplicity monotonicity failed at degree #{degree}")
end

puts "RANK16_U1043459_HAHN_LP_ALL_DEGREES: PASS"
puts "active_distances=#{ACTIVE_DISTANCES.join(',')}"
puts "exact_prefix=7..#{PREFIX_END} minimum_degree=#{prefix_min_degree}"
puts "minimum_prefix_slack=#{prefix_min_slack}"
puts "orthogonality_tail=#{TAIL_START}..#{MAX_DEGREE}"
puts "minimum_active_valency_distance=#{minimum_distance}"
puts "tail_integer_margin_bits=#{tail_margin.bit_length}"
puts "tail_integer_margin_sha256=#{Digest::SHA256.hexdigest(tail_margin.to_s)}"
puts "hahn_bound_floor=#{bound.floor} target=#{TARGET} excess=#{bound.floor - TARGET}"
puts "conclusion=degree6_optimum_unchanged_through_all_Hahn_degrees"
