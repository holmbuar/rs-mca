#!/usr/bin/env ruby
# frozen_string_literal: true

# Exact census for the last undeleted q=14 endpoint of the post-M217
# M=216 plateau.  The geometric conclusion is recorded in the companion
# theorem note; this script independently verifies every integer identity
# and every finite-profile gate used there.  Standard library only.

M = 216
Q = 14
LOW_B = 180
HIGH_B = 193
PLANE_POINTS = Q * Q + Q + 1 # 211

def check(condition, message)
  raise message unless condition
end

def c2(n)
  n * (n - 1) / 2
end

def dpw(degree, mdr)
  base = (degree - 1) * (degree - mdr - 1) + mdr * mdr
  alpha = 2 * mdr + 1 - degree
  base - (alpha.positive? ? alpha * (alpha + 1) / 2 : 0)
end

# For each total deficiency and square sum, store the minimum number of
# nonzero parts in a partition by 1,...,13.  This is the exact coordinate-cap
# statistic because zero coordinates pad every realization.  Deficiencies
# 14 and 15 remain explicit below.
def base_square_sum_min_counts(maximum_defect)
  states = Array.new(maximum_defect + 1) { {} }
  states[0][0] = 0
  (1..13).each do |part|
    (part..maximum_defect).each do |total|
      states[total - part].each do |square_sum, count|
        new_square = square_sum + part * part
        new_count = count + 1
        old_count = states[total][new_square]
        states[total][new_square] = new_count if old_count.nil? || new_count < old_count
      end
    end
  end
  states
end

def each_profile(defect, base_min_counts)
  (0..defect / 15).each do |n15|
    (0..(defect - 15 * n15) / 14).each do |n14|
      remainder = defect - 15 * n15 - 14 * n14
      coordinate_cap = M - n14 - n15
      next if coordinate_cap.negative? || remainder > 13 * coordinate_cap

      base_min_counts.fetch(remainder).each do |residual_square, minimum_count|
        next if minimum_count > coordinate_cap
        yield residual_square + 196 * n14 + 225 * n15, n14, n15
      end
    end
  end
end

def exact_residual_partitions(pair_budget, point_cap, incidence_cap)
  return [] if pair_budget.negative? || point_cap.negative? || incidence_cap.negative?
  return [[]] if pair_budget.zero?
  return [] if point_cap.zero?

  answers = []
  visit = lambda do |parts, pairs, incidence, minimum_multiplicity|
    if pairs == pair_budget
      answers << parts
      return
    end
    return if parts.length == point_cap

    (minimum_multiplicity..(incidence_cap - incidence)).each do |multiplicity|
      new_pairs = pairs + c2(multiplicity)
      break if new_pairs > pair_budget
      visit.call(parts + [multiplicity], new_pairs,
                 incidence + multiplicity, multiplicity)
    end
  end
  visit.call([], 0, 0, 2)
  answers
end

check(exact_residual_partitions(0, 1, 1) == [[]],
      "empty residual partition must survive a positive point cap")

expected_counts = {
  193 => 8, 192 => 8, 191 => 9, 190 => 11, 189 => 14, 188 => 16,
  187 => 19, 186 => 22, 185 => 24, 184 => 26, 183 => 27,
  182 => 34, 181 => 43, 180 => 49
}.freeze

base_min_counts = base_square_sum_min_counts(15 * (M - LOW_B))
regression_table = base_square_sum_min_counts(7)
check(regression_table.fetch(7).fetch(27) == 3,
      "minimum-coordinate regression 5+1+1 failed")
outputs = []

HIGH_B.downto(LOW_B) do |b|
  defect = 15 * (M - b)
  exact_rows = []

  each_profile(defect, base_min_counts) do |square_sum, n14, n15|
    marked_pairs = M * 105 - 14 * defect + (square_sum - defect) / 2
    pair_budget = c2(b) - marked_pairs
    next if pair_budget.negative?

    marked_tau = M * 196 - 28 * defect + square_sum - n15
    high_marked_points = M - n14 - n15
    point_cap = PLANE_POINTS - high_marked_points
    next if point_cap.negative?

    exact_residual_partitions(pair_budget, point_cap, n14).each do |partition|
      incidence = partition.sum
      residual_points = partition.length
      j = incidence - residual_points
      residual_tau = 2 * pair_budget - j
      slack = dpw(b, Q) - marked_tau - residual_tau
      next if slack.negative?

      check(slack == j - (5 - n15),
            "B=#{b}: exact DPW-slack identity failed")
      exact_rows << [square_sum, n14, n15, partition, slack]
    end
  end
  exact_rows.uniq!
  check(exact_rows.length == expected_counts.fetch(b),
        "B=#{b}: complete exact-row count changed")

  excess_histogram = Hash.new(0)
  maximum_excess = 0
  maximum_forbidden = 0
  maximum_low_count = 0
  exact_rows.each do |_square_sum, n14, n15, partition, slack|
    incidence = partition.sum
    residual_points = partition.length
    u = n14 - incidence
    chern_excess = u + slack

    check(u >= 0, "B=#{b}: negative restriction deficit")
    check(n14 + n15 <= 8,
          "B=#{b}: low-valency marked-point count exceeds eight")
    check(chern_excess <= 2,
          "B=#{b}: Chern excess exceeds the line-argument threshold")

    intersection_support = M - n14 - n15 + residual_points
    check(PLANE_POINTS - intersection_support == chern_excess,
          "B=#{b}: Chern-excess/support identity failed")

    intersection_incidence = 15 * b - n14 + incidence
    check(intersection_incidence == 15 * b - u,
          "B=#{b}: restriction-deficit incidence identity failed")

    # Every original double point consumes deficiency 13.  Every residual
    # double point consumes two residual incidences.  A double point forbids
    # only its two incident lines; a positive restriction deficit forbids at
    # most one additional line per unit.  This intentionally uses the coarse
    # bounds, not the much smaller exact double-point census.
    marked_double_bound = defect / 13
    residual_double_bound = incidence / 2
    forbidden_line_bound = u + 2 * (marked_double_bound + residual_double_bound)
    check(forbidden_line_bound < b,
          "B=#{b}: coarse bad-line bound no longer leaves a usable line")

    maximum_excess = [maximum_excess, chern_excess].max
    maximum_forbidden = [maximum_forbidden, forbidden_line_bound].max
    maximum_low_count = [maximum_low_count, n14 + n15].max
    excess_histogram[[u, slack]] += 1
  end

  outputs << [b, exact_rows.length, maximum_excess,
              maximum_forbidden, maximum_low_count, excess_histogram.sort]
end

check(outputs.all? { |_b, _rows, excess, _forbidden, _low, _hist| excess <= 2 },
      "uniform Chern-excess gate failed")
check(outputs.all? { |b, _rows, _excess, forbidden, _low, _hist| forbidden < b },
      "uniform good-line gate failed")

puts "RANK15_M216_CAMACHO_SAD_LINE: PASS"
puts "scope=h_zero_q14_B_#{LOW_B}..#{HIGH_B}"
outputs.each do |b, rows, excess, forbidden, low_count, histogram|
  puts "B=#{b} exact_rows=#{rows} max_chern_excess=#{excess} " \
       "max_forbidden_lines=#{forbidden} max_n14_plus_n15=#{low_count} " \
       "excess_histogram=#{histogram.inspect}"
end
puts "arithmetic_conclusion=every_exact_row_has_a_nondeficient_line_avoiding_all_double_points"
puts "geometric_input=camacho_sad_on_that_line_excludes_fifteen_simple_radial_zeros"
