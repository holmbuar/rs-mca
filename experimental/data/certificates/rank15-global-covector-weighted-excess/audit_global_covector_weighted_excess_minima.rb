#!/usr/bin/env ruby
# frozen_string_literal: true

# Independent exact-state replay for the five cells quoted in
# RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS_BOUND.md.
#
# This verifier intentionally does not load, eval, transform, or invoke either
# explore_rank15_m213_global_covector_bezout_impact.rb or
# explore_rank15_m213_exact_localcost_driver.rb.  It reconstructs the moment
# profiles and the residual multiplicity-partition DP directly.  It also uses
# a point-by-point Cauchy feasibility scan instead of the source driver's
# binary-search implementation.

M = 213

def assert(condition, message)
  raise message unless condition
end

def choose2(value)
  value * (value - 1) / 2
end

def integer_sqrt(value)
  return 0 if value.zero?

  root = 1 << ((value.bit_length + 1) / 2)
  loop do
    next_root = (root + value / root) / 2
    return root if next_root >= root
    root = next_root
  end
end

def dpw_cap(degree, mdr)
  answer = (degree - 1) * (degree - mdr - 1) + mdr * mdr
  correction = 2 * mdr + 1 - degree
  correction.positive? ? answer - correction * (correction + 1) / 2 : answer
end

# table[t][s] is the least number of parts in an unbounded partition of t
# by 1,...,13 having square sum s.
def moment_partition_table(maximum_total)
  table = Array.new(maximum_total + 1) { {} }
  table[0][0] = 0
  (1..13).each do |part|
    (part..maximum_total).each do |total|
      table[total - part].each do |square_sum, count|
        new_square = square_sum + part * part
        new_count = count + 1
        old_count = table[total][new_square]
        table[total][new_square] = new_count if old_count.nil? || new_count < old_count
      end
    end
  end
  table
end

def each_moment_profile(defect, moment_table)
  return enum_for(__method__, defect, moment_table) unless block_given?

  (0..defect / 15).each do |number_15|
    remaining_after_15 = defect - 15 * number_15
    (0..remaining_after_15 / 14).each do |number_14|
      remainder = remaining_after_15 - 14 * number_14
      coordinate_cap = M - number_14 - number_15
      next if coordinate_cap.negative? || remainder > 13 * coordinate_cap

      moment_table.fetch(remainder).each do |residual_square, least_count|
        next if least_count > coordinate_cap

        yield residual_square + 196 * number_14 + 225 * number_15,
              number_14, number_15
      end
    end
  end
end

def balanced_positive_square_sum(number_of_parts, total)
  return nil if number_of_parts <= 0 || total < number_of_parts

  quotient, remainder = total.divmod(number_of_parts)
  (number_of_parts - remainder) * quotient * quotient +
    remainder * (quotient + 1) * (quotient + 1)
end

# Transparent point-by-point version of the necessary residual Cauchy floor.
def residual_tau_floor(pair_budget, point_cap, incidence_cap)
  return nil if pair_budget.negative? || point_cap.negative? || incidence_cap.negative?
  return 0 if pair_budget.zero?
  return nil if point_cap.zero?

  largest_j = nil
  (1..point_cap).each do |points|
    root = integer_sqrt(points * points + 8 * pair_budget * points)
    j_value = (root - points) / 2
    j_value -= 1 while j_value * j_value + points * j_value > 2 * pair_budget * points
    j_value = [j_value, incidence_cap - points].min
    while j_value >= points &&
          balanced_positive_square_sum(points, j_value) > 2 * pair_budget - j_value
      j_value -= 1
    end
    next if j_value < points

    largest_j = j_value if largest_j.nil? || j_value > largest_j
  end
  largest_j ? [pair_budget, 2 * pair_budget - largest_j].max : nil
end

# Exact unbounded partitions by residual multiplicities m>=2.  A state is
# (pair budget, number of points, total incidence).  Keys are packed integers
# to keep this independent replay small enough to run twice in one process.
def residual_partition_states(maximum_pairs, maximum_points, maximum_incidence)
  width = maximum_incidence + 1
  states = Array.new(maximum_pairs + 1) { {} }
  states[0][0] = true

  multiplicity = 2
  loop do
    pair_cost = choose2(multiplicity)
    break if pair_cost > maximum_pairs

    (pair_cost..maximum_pairs).each do |pairs|
      states[pairs - pair_cost].each_key do |packed|
        points, incidence = packed.divmod(width)
        new_points = points + 1
        new_incidence = incidence + multiplicity
        next if new_points > maximum_points || new_incidence > maximum_incidence

        states[pairs][new_points * width + new_incidence] = true
      end
    end
    multiplicity += 1
  end
  [states, width]
end

EXPECTED = {
  [24, 69] => { raw: 12_607, minimum: 86, maximum: 120, cap: 75, survivors: 0 },
  [24, 68] => { raw: 16_027, minimum: 96, maximum: 132, cap: 100, survivors: 919 },
  [25, 71] => { raw: 225, minimum: 95, maximum: 107, cap: 104, survivors: 215 },
  [25, 70] => { raw: 350, minimum: 106, maximum: 119, cap: 130, survivors: 350 },
  [25, 69] => { raw: 559, minimum: 117, maximum: 132, cap: 156, survivors: 559 }
}.freeze

EXPECTED_DP_COUNTS = {
  [24, 68, 69] => 1_814_494,
  [25, 69, 71] => 2_163_789
}.freeze

def replay_range(q_value, low_b, high_b)
  moments = moment_partition_table(15 * (M - low_b))
  profiles = Hash.new { |hash, key| hash[key] = {} }

  high_b.downto(low_b) do |degree|
    defect = 15 * (M - degree)
    each_moment_profile(defect, moments) do |square_sum, number_14, number_15|
      marked_pairs = M * 105 - 14 * defect + (square_sum - defect) / 2
      pair_budget = choose2(degree) - marked_pairs
      next if pair_budget.negative?

      marked_tau = M * 196 - 28 * defect + square_sum - number_15
      point_cap = q_value * q_value + q_value + 1 - (M - number_14 - number_15)
      incidence_cap = degree * (q_value - 14) + number_14
      tau_floor = residual_tau_floor(pair_budget, point_cap, incidence_cap)
      next unless tau_floor && marked_tau + tau_floor <= dpw_cap(degree, q_value)

      row = [square_sum, number_14, number_15, pair_budget, marked_tau,
             point_cap, incidence_cap]
      profiles[degree][row] = true
    end
  end

  rows = profiles.values.flat_map(&:keys)
  maximum_pairs = rows.map { |row| row[3] }.max
  maximum_points = rows.map { |row| row[5] }.max
  maximum_incidence = rows.map { |row| row[6] }.max
  states, width = residual_partition_states(maximum_pairs, maximum_points,
                                             maximum_incidence)
  state_count = states.sum(&:length)
  expected_state_count = EXPECTED_DP_COUNTS.fetch([q_value, low_b, high_b])
  assert(state_count == expected_state_count,
         "q#{q_value}: residual DP count #{state_count} != #{expected_state_count}")

  answers = {}
  high_b.downto(low_b) do |degree|
    impact = { raw: 0, minimum: nil, maximum: nil, survivors: 0 }
    profiles.fetch(degree).each_key do |row|
      _square_sum, _number_14, _number_15, pair_budget, marked_tau,
        point_cap, incidence_cap = row
      states.fetch(pair_budget).each_key do |packed|
        residual_points, incidence = packed.divmod(width)
        next if residual_points > point_cap || incidence > incidence_cap

        j_value = incidence - residual_points
        slack = dpw_cap(degree, q_value) - marked_tau - (2 * pair_budget - j_value)
        next if slack.negative?

        restriction_deficit = incidence_cap - incidence
        weight = restriction_deficit + 2 * slack
        impact[:raw] += 1
        impact[:minimum] = weight if impact[:minimum].nil? || weight < impact[:minimum]
        impact[:maximum] = weight if impact[:maximum].nil? || weight > impact[:maximum]
        cap = (3 * q_value - degree) * (q_value + 1)
        impact[:survivors] += 1 if weight <= cap
      end
    end
    impact[:cap] = (3 * q_value - degree) * (q_value + 1)
    answers[[q_value, degree]] = impact
  end
  answers
end

actual = replay_range(24, 68, 69).merge(replay_range(25, 69, 71))
assert(actual == EXPECTED, "five-cell impact mismatch:\nactual=#{actual.inspect}\nexpected=#{EXPECTED.inspect}")

EXPECTED.each_key do |q_value, degree|
  row = actual.fetch([q_value, degree])
  puts "q=#{q_value} B=#{degree} raw=#{row[:raw]} W=#{row[:minimum]}..#{row[:maximum]} " \
       "cap=#{row[:cap]} survivors=#{row[:survivors]}"
end
puts "GLOBAL_COVECTOR_WEIGHTED_EXCESS_MINIMA_AUDIT: PASS"
