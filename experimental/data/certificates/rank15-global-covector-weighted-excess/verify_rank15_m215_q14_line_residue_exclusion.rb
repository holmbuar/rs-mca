#!/usr/bin/env ruby
# frozen_string_literal: true

# Complete exact-coordinate and exact-residual census for every stripped
# q=14 endpoint of the post-M216 M=215 plateau.  The finite gates certify that
# one remaining line avoids leaves, all double points, and every possible
# non-simple intersection; the companion note supplies the algebraic residue
# contradiction on that line.

require "digest"

P_FIELD = 2_130_706_433
GLOBAL_N = 2_097_152
GLOBAL_K = 1_048_576
GLOBAL_S = 1_116_047
M215_PLATEAU = (1_042_465..1_043_953)
M215_DIRECT_DEFINITION_SHA256 =
  "b1161c3563eea5e7dfb4c6522c8139c419ad5ec0a2e1bec5c63bc1e4df64e686"

definition_path = File.join(__dir__, "verify_rank15_m216_camacho_sad_line.rb")
raise "M216 exact-profile definition source missing" unless File.file?(definition_path)
raise "M216 exact-profile definition source hash mismatch" unless
  Digest::SHA256.file(definition_path).hexdigest == M215_DIRECT_DEFINITION_SHA256

source = File.read(definition_path).split(/^expected_counts =/, 2).first
source = source.sub("M = 216", "M = 215")
               .sub("LOW_B = 180", "LOW_B = 152")
               .sub("HIGH_B = 193", "HIGH_B = 215")
eval(source, TOPLEVEL_BINDING, definition_path)

ORIGINAL_B_MIN = 164
ORIGINAL_B_MAX = 215
RHO_MAX = 26

def prime?(number)
  return false if number < 2
  return true if number == 2
  return false if number.even?
  divisor = 3
  while divisor * divisor <= number
    return false if (number % divisor).zero?
    divisor += 2
  end
  true
end

check(prime?(P_FIELD), "literal deployed characteristic is not prime")
check(P_FIELD > ORIGINAL_B_MAX, "literal characteristic gate failed")

# Source plateau and the uniform t>=164 gate.
source_gaps = M215_PLATEAU.map do |u|
  n_u = GLOBAL_N - u
  a_u = GLOBAL_S - u
  lambda_u = GLOBAL_K - 1 - u
  M * a_u - 14 * n_u - 163 * lambda_u
end
check(source_gaps.first == 58_582 && source_gaps.last == 2_038,
      "M215 source-gap endpoints mismatch")
check(source_gaps.each_cons(2).all? { |left, right| right == left - 38 },
      "M215 source-gap slope mismatch")
check(source_gaps.all?(&:positive?), "M215 t>=164 source gate failed")

# Profile-free characteristic-valid DPW caps for the original arrangement.
mdr_caps = {}
(ORIGINAL_B_MIN..ORIGINAL_B_MAX).each do |b|
  tau_floor = M * 91 + c2(b) - 196 * (M - b)
  allowed = (0...b).select { |rho| dpw(b, rho) >= tau_floor }
  check(!allowed.empty?, "B=#{b}: empty original mdr range")
  mdr_caps[b] = allowed.max
end
expected_cap_blocks = {
  26 => (164..165), 25 => (166..167), 24 => (168..169),
  23 => (170..171), 22 => (172..174), 21 => (175..177),
  20 => (178..181), 19 => (182..185), 18 => (186..190),
  17 => (191..198), 16 => (199..215)
}
actual_cap_blocks = mdr_caps.group_by { |_b, rho| rho }.to_h do |rho, pairs|
  endpoints = pairs.map(&:first)
  [rho, (endpoints.min..endpoints.max)]
end
check(actual_cap_blocks == expected_cap_blocks, "M215 original mdr-cap blocks mismatch")

# If stripping left B<=151, then h>=164-B and q<=26-h<=B-138.
# Restriction would force n14>=B(14-q)>=B(152-B), incompatible with the
# total deficiency 14*n14<=15(215-B).
deep_gaps = (138..151).to_h do |b|
  [b, 14 * b * (152 - b) - 15 * (M - b)]
end
check(deep_gaps.values.min == 1_154 && deep_gaps.values.all?(&:positive?),
      "M215 deep-deletion gate failed")

# Exact profile table for parts 1,...,13, with minimum nonzero-coordinate
# counts.  A second table with parts 1,...,12 makes the possible number of
# deficiency-13 marked double points exact.
maximum_defect = 15 * (M - LOW_B)
profile_counts = base_square_sum_min_counts(maximum_defect)
without_13 = Array.new(maximum_defect + 1) { {} }
without_13[0][0] = 0
(1..12).each do |part|
  (part..maximum_defect).each do |total|
    without_13[total - part].each do |square_sum, count|
      new_square = square_sum + part * part
      new_count = count + 1
      old_count = without_13[total][new_square]
      without_13[total][new_square] = new_count if old_count.nil? || new_count < old_count
    end
  end
end

expected_counts_high_to_low = [
  0, 0, 0, 0,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 7,
  9, 11, 14, 17, 19, 21, 22, 23, 29, 34, 35, 36, 37,
  41, 42, 46, 47, 50, 52, 58, 72, 85, 94, 100, 101, 102,
  103, 107, 114, 124, 136, 151, 162, 172, 179, 199, 235, 267
].freeze
check(expected_counts_high_to_low.length == HIGH_B - LOW_B + 1,
      "M215 expected-count vector length mismatch")

outputs = []
HIGH_B.downto(LOW_B) do |b|
  defect = 15 * (M - b)
  rows = []

  each_profile(defect, profile_counts) do |square_sum, n14, n15|
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
      check(slack == j - (M - PLANE_POINTS - n15),
            "B=#{b}: M215 DPW-slack identity failed")

      u = n14 - incidence
      excess = u + slack
      check(u >= 0, "B=#{b}: negative restriction deficit")
      check(PLANE_POINTS - (M - n14 - n15 + residual_points) == excess,
            "B=#{b}: Chern-excess/support identity failed")

      residual_total = defect - 14 * n14 - 15 * n15
      residual_square = square_sum - 196 * n14 - 225 * n15
      coordinate_cap = M - n14 - n15
      n13_values = []
      n13_max = [residual_total / 13, residual_square / 169].min
      (0..n13_max).each do |n13|
        total = residual_total - 13 * n13
        target_square = residual_square - 169 * n13
        next if target_square.negative?
        minimum_count = without_13.fetch(total)[target_square]
        if minimum_count && minimum_count + n13 <= coordinate_cap
          n13_values << n13
        end
      end
      check(!n13_values.empty?, "B=#{b}: exact profile lost in n13 audit")

      double_max = n13_values.max + partition.count(2)
      # Every non-simple intersection of multiplicity >=3 costs at least
      # three units beyond its support point.  Each lies on at most 15 lines:
      # marked valency is <=15, while residual multiplicity is <=n14<=10.
      non_simple_count = excess / 3
      bad_line_bound = u + 2 * double_max + 15 * non_simple_count
      check(bad_line_bound < b, "B=#{b}: no residue-test line remains")

      rows << [square_sum, n14, n15, partition, slack, u, excess,
               n13_values, double_max, bad_line_bound]
    end
  end
  rows.uniq!

  expected_count = expected_counts_high_to_low.fetch(HIGH_B - b)
  check(rows.length == expected_count, "B=#{b}: complete M215 row count changed")
  outputs << [
    b, rows.length,
    rows.map { |row| row[6] }.max || 0,
    rows.map { |row| row[8] }.max || 0,
    rows.map { |row| row[9] }.max || 0,
    rows.map { |row| row[1] + row[2] }.max || 0
  ]
end

check(outputs.sum { |row| row[1] } == 3_225, "M215 total exact-row count mismatch")
check(outputs.map { |row| row[2] }.max == 5, "M215 maximum Chern excess mismatch")
check(outputs.map { |row| row[3] }.max == 7, "M215 maximum double count mismatch")
check(outputs.map { |row| row[4] }.max == 24, "M215 maximum bad-line bound mismatch")
check(outputs.map { |row| row[5] }.max == 10, "M215 maximum low-point count mismatch")

puts "RANK15_M215_Q14_LINE_RESIDUE_EXCLUSION: PASS"
puts "definition_source_sha256=#{M215_DIRECT_DEFINITION_SHA256}"
puts "source_plateau=#{M215_PLATEAU.begin}..#{M215_PLATEAU.end} states=#{M215_PLATEAU.size} q=15"
puts "source_t_gate=164..215 gaps=#{source_gaps.last}..#{source_gaps.first}"
puts "original_mdr_cap_blocks=#{actual_cap_blocks.sort.to_h.inspect}"
puts "deep_deletion_excluded=B138..151 min_gap=#{deep_gaps.values.min}"
puts "q14_endpoint_range=B#{LOW_B}..#{HIGH_B}"
puts "exact_row_counts=#{expected_counts_high_to_low.join(',')} total=3225"
puts "max_chern_excess=5 max_double_points=7 max_bad_lines=24<B_min=#{LOW_B}"
puts "line_residue_gap_mod_p=#{(15 - 1) % P_FIELD}"
puts "conclusion=all_stripped_q14_endpoints_excluded"
