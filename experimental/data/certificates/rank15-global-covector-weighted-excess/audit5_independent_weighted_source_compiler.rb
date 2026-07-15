#!/usr/bin/env ruby
# frozen_string_literal: true

# Second source/compiler audit for the five-cell impact of the frozen
# global-covector weighted excess theorem.  This verifier is deliberately
# standalone: it does not load, eval, require, or text-transform either the
# claimant impact driver or audit_global_covector_weighted_excess_minima.rb.
#
# It reconstructs the M=213 aggregate marked-coordinate profiles and exact
# residual partition states directly from the pinned source definitions.  It
# also omits the source driver's Cauchy prefilter, so an error in that safe
# relaxation cannot silently delete a row here.

require "digest"
require "set"

M = 213

PINS = {
  "RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS_BOUND.md" =>
    "6f998929209b534d39cb0d31fa6458f5bf63d9326255ec31e7f0f64ae7a5389e",
  "explore_rank15_m213_covector_weight_impact.rb" =>
    "099fab039f0812b9aeb5dce7acdcdc588f43520074ef1ae358a6d6fcfe0e5be2",
  "explore_rank15_m213_exact_localcost_driver.rb" =>
    "8cfcf7475dd153e5e101e0c97467d7d49b0336f902e806ce673dee13f8de533b",
  "verify_rank15_m215_q15_line_residue_exclusion.rb" =>
    "f8cfba142607caccb5eb05ad261919f48697fd8a03b542fd65760075057eda1c",
  "verify_rank15_m216_camacho_sad_line.rb" =>
    "b1161c3563eea5e7dfb4c6522c8139c419ad5ec0a2e1bec5c63bc1e4df64e686"
}.freeze

CELLS = [
  [24, 69, 12_607, 86, 120, 75, 0],
  [24, 68, 16_027, 96, 132, 100, 919],
  [25, 71, 225, 95, 107, 104, 215],
  [25, 70, 350, 106, 119, 130, 350],
  [25, 69, 559, 117, 132, 156, 559]
].freeze

EXPECTED_PROFILE_COUNTS = {
  [24, 69] => 60_358,
  [24, 68] => 63_110,
  [25, 71] => 55_566,
  [25, 70] => 57_799,
  [25, 69] => 60_358
}.freeze

EXPECTED_ROW_SHA256 = {
  [24, 69] => "ff6883869b7126bceea37a3cbd8c3485c9760c9309e6608d924b2c7935c2e80f",
  [24, 68] => "9f9111574caa017e99cad1a7d6064738dd859dcfe778ff9bebf602ef2b0ea16b",
  [25, 71] => "b9073791b5899d8a3c1160dad592b4184519e522ee18d62495e0542140502599",
  [25, 70] => "2de1e48f507995fb5077c5c917f70d9f877e39014bb6464d14def7300b3303b3",
  [25, 69] => "3905a9b69ab4badfc2e22d454faea3509f647900bb5b8789cbc44353d017fbfa"
}.freeze

def check(condition, message)
  raise message unless condition
end

def choose2(number)
  number * (number - 1) / 2
end

def dpw(degree, mdr)
  base = (degree - 1) * (degree - mdr - 1) + mdr * mdr
  correction_argument = 2 * mdr + 1 - degree
  correction = if correction_argument.positive?
                 correction_argument * (correction_argument + 1) / 2
               else
                 0
               end
  base - correction
end

# Exact unbounded knapsack by deficiencies 1,...,13.  The value at
# [total][square_sum] is the least number of nonzero coordinates realizing
# those two moments.  Keeping only that least count is exact because unused
# coordinates are zero and the only later constraint is an upper bound on the
# number of nonzero coordinates.
def minimum_coordinate_counts(maximum_total)
  table = Array.new(maximum_total + 1) { {} }
  table[0][0] = 0
  (1..13).each do |deficiency|
    (deficiency..maximum_total).each do |total|
      table.fetch(total - deficiency).to_a.each do |square_sum, count|
        candidate_square = square_sum + deficiency * deficiency
        candidate_count = count + 1
        incumbent = table.fetch(total)[candidate_square]
        if incumbent.nil? || candidate_count < incumbent
          table.fetch(total)[candidate_square] = candidate_count
        end
      end
    end
  end
  table
end

# Reconstruct all distinct aggregate marked profiles for one B.  Parts 14 and
# 15 are explicit because their counts enter the source formulas separately.
# No residual or DPW prefilter is used here.
def aggregate_profiles(q_value, b_value, base_table)
  defect = 15 * (M - b_value)
  profiles = Set.new

  (0..defect / 15).each do |n15|
    remaining_after_15 = defect - 15 * n15
    (0..remaining_after_15 / 14).each do |n14|
      remainder = remaining_after_15 - 14 * n14
      coordinate_cap = M - n14 - n15
      next if coordinate_cap.negative? || remainder > 13 * coordinate_cap

      base_table.fetch(remainder).each do |residual_square, minimum_count|
        next if minimum_count > coordinate_cap

        square_sum = residual_square + 196 * n14 + 225 * n15
        parity_term = square_sum - defect
        check(parity_term.even?, "nonintegral marked-pair formula")
        marked_pairs = M * 105 - 14 * defect + parity_term / 2
        pair_budget = choose2(b_value) - marked_pairs
        next if pair_budget.negative?

        marked_tau = M * 196 - 28 * defect + square_sum - n15
        marked_support = M - n14 - n15
        point_cap = q_value * q_value + q_value + 1 - marked_support
        incidence_cap = b_value * (q_value - 14) + n14
        next if point_cap.negative? || incidence_cap.negative?

        profiles << [square_sum, n14, n15, pair_budget, marked_tau,
                     point_cap, incidence_cap]
      end
    end
  end

  profiles.to_a.sort
end

# Exact reachability of residual ordinary-multiple-point aggregates.  A point
# of multiplicity m contributes (C(m,2),1,m) to (pairs,points,incidence).
# Sets retain every reachable (points,incidence) pair, not a componentwise
# maximum or a representative partition.
def residual_reachability(maximum_pairs, maximum_points, maximum_incidence)
  states = Array.new(maximum_pairs + 1) { Set.new }
  states[0] << [0, 0]

  multiplicity = 2
  loop do
    pair_cost = choose2(multiplicity)
    break if pair_cost > maximum_pairs

    (pair_cost..maximum_pairs).each do |pairs|
      states.fetch(pairs - pair_cost).to_a.each do |points, incidence|
        next_points = points + 1
        next_incidence = incidence + multiplicity
        next if next_points > maximum_points || next_incidence > maximum_incidence

        states.fetch(pairs) << [next_points, next_incidence]
      end
    end
    multiplicity += 1
  end

  states
end

# Independent recursion used only on a small cube to guard the full DP's
# unbounded-copy and order-dedup quantifiers.
def recursive_residual_keys(pair_budget, point_cap, incidence_cap)
  answers = Set.new
  visit = lambda do |pairs, points, incidence, minimum_multiplicity|
    if pairs == pair_budget
      answers << [points, incidence]
      return
    end
    return if points == point_cap

    multiplicity = minimum_multiplicity
    loop do
      new_pairs = pairs + choose2(multiplicity)
      break if new_pairs > pair_budget || incidence + multiplicity > incidence_cap
      visit.call(new_pairs, points + 1, incidence + multiplicity, multiplicity)
      multiplicity += 1
    end
  end
  visit.call(0, 0, 0, 2)
  answers
end

PINS.each do |relative_path, expected_hash|
  path = File.join(__dir__, relative_path)
  check(File.file?(path), "missing pinned source: #{relative_path}")
  actual_hash = Digest::SHA256.file(path).hexdigest
  check(actual_hash == expected_hash,
        "source hash mismatch for #{relative_path}: #{actual_hash}")
end

maximum_defect = CELLS.map { |_q, b, *_rest| 15 * (M - b) }.max
base_table = minimum_coordinate_counts(maximum_defect)

# Small direct moment checks.  They detect changing an unbounded coin loop to
# a 0/1 loop and detect retaining a nonminimal coordinate count.
check(base_table.fetch(7).fetch(27) == 3, "5+1+1 profile regression failed")
check(base_table.fetch(26).fetch(338) == 2, "13+13 profile regression failed")

cell_profiles = {}
CELLS.each do |q_value, b_value, *_rest|
  cell_profiles[[q_value, b_value]] =
    aggregate_profiles(q_value, b_value, base_table)
end

maximum_pairs = cell_profiles.values.flatten(1).map { |row| row.fetch(3) }.max
maximum_points = cell_profiles.values.flatten(1).map { |row| row.fetch(5) }.max
maximum_incidence = cell_profiles.values.flatten(1).map { |row| row.fetch(6) }.max
check([maximum_pairs, maximum_points, maximum_incidence] == [355, 474, 816],
      "aggregate source dimensions changed")
residual_states = residual_reachability(maximum_pairs, maximum_points,
                                        maximum_incidence)
check(residual_states.sum(&:length) == 2_163_789,
      "residual reachable-key count changed")

(0..40).each do |pairs|
  dp_keys = residual_states.fetch(pairs).select do |points, incidence|
    points <= 8 && incidence <= 20
  end.to_set
  recursive_keys = recursive_residual_keys(pairs, 8, 20)
  check(dp_keys == recursive_keys, "residual reachability mismatch at P=#{pairs}")
end

outputs = []
CELLS.each do |q_value, b_value, expected_raw, expected_min, expected_max,
               expected_cap, expected_survivors|
  rows = []
  raw_iterations = 0

  cell_profiles.fetch([q_value, b_value]).each do |square_sum, n14, n15,
                                                       pair_budget, marked_tau,
                                                       point_cap, incidence_cap|
    residual_states.fetch(pair_budget).each do |residual_points, incidence|
      next if residual_points > point_cap || incidence > incidence_cap

      j_value = incidence - residual_points
      residual_tau = 2 * pair_budget - j_value
      slack = dpw(b_value, q_value) - marked_tau - residual_tau
      next if slack.negative?

      restriction_deficit = incidence_cap - incidence
      excess = restriction_deficit + slack
      support_excess = point_cap - residual_points
      check(excess == support_excess,
            "E identity failed for q=#{q_value}, B=#{b_value}")
      check(restriction_deficit >= 0 && slack >= 0 && excess >= 0,
            "negative U/S/E in q=#{q_value}, B=#{b_value}")

      weight_from_es = excess + slack
      weight_from_us = restriction_deficit + 2 * slack
      check(weight_from_es == weight_from_us,
            "W=E+S=U+2S failed for q=#{q_value}, B=#{b_value}")

      raw_iterations += 1
      rows << [square_sum, n14, n15, pair_budget, residual_points,
               incidence, slack, restriction_deficit, excess, weight_from_es]
    end
  end

  unique_rows = rows.to_set
  check(unique_rows.length == raw_iterations,
        "dedup collision: q=#{q_value}, B=#{b_value}, " \
        "iterations=#{raw_iterations}, unique=#{unique_rows.length}")

  sorted_rows = unique_rows.to_a.sort
  weights = sorted_rows.map(&:last)
  a_value = 3 * q_value - b_value
  cap = a_value * (q_value + 1)
  survivors = weights.count { |weight| weight <= cap }
  digest_input = sorted_rows.map { |row| row.join(",") }.join("\n") + "\n"
  row_sha256 = Digest::SHA256.hexdigest(digest_input)

  check(raw_iterations == expected_raw,
        "raw-count mismatch q=#{q_value}, B=#{b_value}: #{raw_iterations}")
  check(cell_profiles.fetch([q_value, b_value]).length ==
        EXPECTED_PROFILE_COUNTS.fetch([q_value, b_value]),
        "aggregate-profile count mismatch q=#{q_value}, B=#{b_value}")
  check(weights.min == expected_min && weights.max == expected_max,
        "W-range mismatch q=#{q_value}, B=#{b_value}: " \
        "#{weights.min}..#{weights.max}")
  check(cap == expected_cap,
        "cap mismatch q=#{q_value}, B=#{b_value}: #{cap}")
  check(survivors == expected_survivors,
        "survivor mismatch q=#{q_value}, B=#{b_value}: #{survivors}")
  check(row_sha256 == EXPECTED_ROW_SHA256.fetch([q_value, b_value]),
        "full-row digest mismatch q=#{q_value}, B=#{b_value}: #{row_sha256}")

  outputs << [q_value, b_value, a_value, raw_iterations, weights.min,
              weights.max, cap, survivors, row_sha256,
              cell_profiles.fetch([q_value, b_value]).length]
end

puts "AUDIT5_INDEPENDENT_WEIGHTED_SOURCE_COMPILER: PASS"
puts "theorem_sha256=#{PINS.fetch('RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS_BOUND.md')}"
puts "claimant_driver_sha256=#{PINS.fetch('explore_rank15_m213_covector_weight_impact.rb')}"
puts "generic_source_sha256=#{PINS.fetch('explore_rank15_m213_exact_localcost_driver.rb')}"
puts "definition_source_sha256=#{PINS.fetch('verify_rank15_m215_q15_line_residue_exclusion.rb')}"
puts "ancestral_definition_sha256=#{PINS.fetch('verify_rank15_m216_camacho_sad_line.rb')}"
puts "independence=no_import_no_eval_no_transform_no_cauchy_prefilter"
puts "source_scope=M#{M} cells=#{CELLS.map { |q, b, *_rest| "q#{q}B#{b}" }.join(',')}"
puts "aggregate_dimensions=P#{maximum_pairs}_R#{maximum_points}_I#{maximum_incidence}"
puts "residual_reachable_keys=#{residual_states.sum(&:length)}"
outputs.each do |q_value, b_value, a_value, raw, weight_min, weight_max, cap,
                 survivors, row_sha256, profile_count|
  puts "q=#{q_value} B=#{b_value} a=#{a_value} profiles=#{profile_count} " \
       "raw=#{raw} W=#{weight_min}..#{weight_max} cap=#{cap} " \
       "survivors=#{survivors} rows_sha256=#{row_sha256}"
end
puts "quantifier_guard=raw_iterations_equal_unique_full_tuples"
puts "identity_guard=W_equals_E_plus_S_equals_U_plus_2S"
puts "conclusion=q24B69_closed_other_four_cells_not_closed"
