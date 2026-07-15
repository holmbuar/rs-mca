#!/usr/bin/env ruby
# frozen_string_literal: true

# Complete exact-coordinate / exact-residual-state replay for the q=15 branch
# of the post-M216 M=215 layer.  Standard library only.
#
# The residual DP records exact reachability of (pair budget, point count,
# incidence).  For each reachable state it retains componentwise maxima of
# the residual double-point count and residual multiplicity.  Those two
# maxima need not arise in the same partition; combining them can only enlarge
# the forbidden-line bound and is therefore a safe hostile overestimate.

require "digest"

P_FIELD = 2_130_706_433
GLOBAL_N = 2_097_152
GLOBAL_K = 1_048_576
GLOBAL_S = 1_116_047
M = 215
Q = 15
ORIGINAL_B_MIN = 164
ORIGINAL_B_MAX = 215
RHO_MAX = 26
LOW_B = 152
HIGH_B = 215
Q15_LOW_B = 153
Q15_HIGH_B = 174
Q15_ZERO_LENGTH = Q * Q + Q + 1 # c2(T_{P^2}(14)) = 241
M216_DEFINITION_SHA256 =
  "b1161c3563eea5e7dfb4c6522c8139c419ad5ec0a2e1bec5c63bc1e4df64e686"
M215_Q14_VERIFIER_SHA256 =
  "984dfd0c38257899ef89137e979a60fa8ba9e9e98c8e5c9ac022fc8391363028"

definition_path = File.join(__dir__, "verify_rank15_m216_camacho_sad_line.rb")
q14_path = File.join(__dir__, "verify_rank15_m215_q14_line_residue_exclusion.rb")
raise "M216 exact-profile definition source missing" unless File.file?(definition_path)
raise "M216 exact-profile definition source hash mismatch" unless
  Digest::SHA256.file(definition_path).hexdigest == M216_DEFINITION_SHA256
raise "M215 q14 verifier missing" unless File.file?(q14_path)
raise "M215 q14 verifier hash mismatch" unless
  Digest::SHA256.file(q14_path).hexdigest == M215_Q14_VERIFIER_SHA256

def check(condition, message)
  raise message unless condition
end

def c2(number)
  number * (number - 1) / 2
end

def isqrt(number)
  return 0 if number.zero?
  value = 1 << ((number.bit_length + 1) / 2)
  loop do
    next_value = (value + number / value) / 2
    return value if next_value >= value
    value = next_value
  end
end

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

def dpw(degree, mdr)
  base = (degree - 1) * (degree - mdr - 1) + mdr * mdr
  alpha = 2 * mdr + 1 - degree
  base - (alpha.positive? ? alpha * (alpha + 1) / 2 : 0)
end

# For each total deficiency and square sum, store the minimum number of
# nonzero coordinates in an unbounded partition by 1,...,13.  This is exact:
# zero coordinates pad every realization to the available coordinate count.
def base_square_sum_min_counts(maximum_defect, maximum_part = 13)
  states = Array.new(maximum_defect + 1) { {} }
  states[0][0] = 0
  (1..maximum_part).each do |part|
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

def minimum_positive_square_sum(point_count, total)
  return nil if point_count <= 0 || total < point_count
  quotient, residue = total.divmod(point_count)
  (point_count - residue) * quotient * quotient +
    residue * (quotient + 1) * (quotient + 1)
end

# Necessary Cauchy / incidence relaxation.  If R residual points carry pair
# budget P and J=sum(m-1), then J^2<=R(2P-J), I=J+R is bounded by the line
# restriction, and tau_res=2P-J.  Returning a lower bound on tau_res makes
# this a safe superset scan.  The empty partition is feasible whenever P=0.
def residual_tau_floor_slow(pair_budget, point_cap, incidence_cap)
  return nil if pair_budget.negative? || point_cap.negative? || incidence_cap.negative?
  return 0 if pair_budget.zero?
  return nil if point_cap.zero?

  maximum_j = nil
  (1..point_cap).each do |points|
    root = isqrt(points * points + 8 * pair_budget * points)
    candidate = (root - points) / 2
    candidate -= 1 while candidate * candidate + points * candidate >
                         2 * pair_budget * points
    candidate = [candidate, incidence_cap - points].min
    candidate -= 1 while candidate >= points &&
                         minimum_positive_square_sum(points, candidate) >
                           2 * pair_budget - candidate
    next if candidate < points
    maximum_j = candidate if maximum_j.nil? || candidate > maximum_j
  end
  maximum_j ? [pair_budget, 2 * pair_budget - maximum_j].max : nil
end

# Equivalent logarithmic implementation.  For fixed J, the largest allowed
# number of residual points minimizes the integer-balanced square sum.  Thus
# J is feasible exactly when
#
#   min_square(min(J,R_cap,I_cap-J),J) <= 2P-J.
#
# On 1<=J<=P the left obstruction is monotone, so binary search returns the
# same maximum J as the transparent point-by-point implementation above.
def residual_tau_floor(pair_budget, point_cap, incidence_cap)
  return nil if pair_budget.negative? || point_cap.negative? || incidence_cap.negative?
  return 0 if pair_budget.zero?
  return nil if point_cap.zero? || incidence_cap < 2

  feasible = lambda do |j_value|
    points = [j_value, point_cap, incidence_cap - j_value].min
    next false if points <= 0
    minimum_positive_square_sum(points, j_value) <= 2 * pair_budget - j_value
  end
  low = 1
  high = [pair_budget, incidence_cap - 1].min
  return nil if high < low || !feasible.call(low)
  while low < high
    middle = (low + high + 1) / 2
    if feasible.call(middle)
      low = middle
    else
      high = middle - 1
    end
  end
  [pair_budget, 2 * pair_budget - low].max
end

# Exact unbounded residual reachability.  A point of multiplicity m contributes
# (C(m,2),1,m) to (P,R,I).  The ascending P loop permits every count of each
# multiplicity and prevents order copies.  Values are [max #m=2, max m].
def residual_state_table(maximum_pairs, maximum_points, maximum_incidence)
  states = Array.new(maximum_pairs + 1) { {} }
  states[0][[0, 0]] = [0, 0]
  multiplicity = 2
  loop do
    pair_cost = c2(multiplicity)
    break if pair_cost > maximum_pairs

    (pair_cost..maximum_pairs).each do |pairs|
      states[pairs - pair_cost].to_a.each do |(points, incidence), (doubles, max_m)|
        new_points = points + 1
        new_incidence = incidence + multiplicity
        next if new_points > maximum_points || new_incidence > maximum_incidence

        key = [new_points, new_incidence]
        value = [doubles + (multiplicity == 2 ? 1 : 0), [max_m, multiplicity].max]
        old = states[pairs][key]
        states[pairs][key] = if old
                               [[old[0], value[0]].max, [old[1], value[1]].max]
                             else
                               value
                             end
      end
    end
    multiplicity += 1
  end
  states
end

# Small independent recursive regression for exact residual reachability.
def brute_residual_states(pair_budget, point_cap, incidence_cap)
  answers = {}
  visit = lambda do |pairs, points, incidence, minimum_m|
    if pairs == pair_budget
      answers[[points, incidence]] = true
      return
    end
    return if points == point_cap

    multiplicity = minimum_m
    loop do
      new_pairs = pairs + c2(multiplicity)
      break if new_pairs > pair_budget || incidence + multiplicity > incidence_cap
      visit.call(new_pairs, points + 1, incidence + multiplicity, multiplicity)
      multiplicity += 1
    end
  end
  visit.call(0, 0, 0, 2)
  answers.keys.sort
end

check(P_FIELD == 2**31 - 2**24 + 1, "field formula mismatch")
check(prime?(P_FIELD), "literal deployed characteristic is not prime")
check(P_FIELD > ORIGINAL_B_MAX, "literal characteristic gate failed")
check(Q15_ZERO_LENGTH == 241, "q15 Chern length mismatch")
check(residual_tau_floor(0, 7, 0) == 0,
      "empty residual partition must survive a positive point cap")
(0..40).each do |pairs|
  (0..12).each do |point_cap|
    (0..30).each do |incidence_cap|
      slow = residual_tau_floor_slow(pairs, point_cap, incidence_cap)
      fast = residual_tau_floor(pairs, point_cap, incidence_cap)
      check(fast == slow,
            "residual relaxation regression P=#{pairs},R=#{point_cap},I=#{incidence_cap}")
    end
  end
end

# Source plateau and t>=164 gate, replayed here rather than trusted from the
# q=14 branch.
plateau = (1_042_465..1_043_953)
source_gaps = plateau.map do |u|
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

# Exact deficiency profiles and a safe all-q relaxation.  The original mdr
# caps imply q<=26-max(164-B,0).  This scan must leave only q=14 or q=15.
maximum_defect = 15 * (M - LOW_B)
profiles = base_square_sum_min_counts(maximum_defect)
regression = base_square_sum_min_counts(7)
check(regression.fetch(7).fetch(27) == 3,
      "minimum-coordinate regression 5+1+1 failed")

q15_relaxed = Hash.new { |hash, key| hash[key] = [] }
all_relaxed_q = {}
HIGH_B.downto(LOW_B) do |b|
  defect = 15 * (M - b)
  q_max = RHO_MAX - [ORIGINAL_B_MIN - b, 0].max
  q_values = {}

  each_profile(defect, profiles) do |square_sum, n14, n15|
    marked_pairs = M * 105 - 14 * defect + (square_sum - defect) / 2
    pair_budget = c2(b) - marked_pairs
    next if pair_budget.negative?

    marked_tau = M * 196 - 28 * defect + square_sum - n15
    high_marked_points = M - n14 - n15
    (0..q_max).each do |q|
      point_cap = q * q + q + 1 - high_marked_points
      incidence_cap = b * (q - 14) + n14
      tau_floor = residual_tau_floor(pair_budget, point_cap, incidence_cap)
      next unless tau_floor
      next if marked_tau + tau_floor > dpw(b, q)

      q_values[q] = true
      next unless q == Q
      q15_relaxed[b] << [square_sum, n14, n15, pair_budget, marked_tau,
                         point_cap, incidence_cap]
    end
  end
  q15_relaxed[b].uniq!
  all_relaxed_q[b] = q_values.keys.sort
  check((all_relaxed_q[b] - [14, 15]).empty?,
        "B=#{b}: relaxed q values #{all_relaxed_q[b].inspect}")
end

expected_relaxed_counts = {
  174 => 4, 173 => 17, 172 => 31, 171 => 31, 170 => 32, 169 => 34,
  168 => 37, 167 => 42, 166 => 53, 165 => 71, 164 => 92, 163 => 116,
  162 => 143, 161 => 173, 160 => 219, 159 => 285, 158 => 358,
  157 => 429, 156 => 486, 155 => 510, 154 => 520, 153 => 540
}.freeze
actual_relaxed_counts = (Q15_LOW_B..Q15_HIGH_B).to_h do |b|
  [b, q15_relaxed.fetch(b).length]
end
check(actual_relaxed_counts == expected_relaxed_counts,
      "M215 q15 relaxed-profile counts changed")
check((LOW_B..HIGH_B).all? do |b|
        expected_relaxed_counts.key?(b) || q15_relaxed.fetch(b).empty?
      end, "q15 survivor outside B153..174")
check(all_relaxed_q.values.flatten.uniq.sort == [14, 15],
      "all-q relaxation did not reduce to q=14,15")

maximum_pairs = q15_relaxed.values.flatten(1).map { |row| row[3] }.max
maximum_points = q15_relaxed.values.flatten(1).map { |row| row[5] }.max
maximum_incidence = q15_relaxed.values.flatten(1).map { |row| row[6] }.max
check([maximum_pairs, maximum_points, maximum_incidence] == [523, 29, 174],
      "residual DP dimensions changed")

residual_states = residual_state_table(maximum_pairs, maximum_points,
                                       maximum_incidence)
check(residual_states.sum(&:length) == 510_102,
      "complete residual-state table size changed")
(0..24).each do |pairs|
  exact_keys = residual_states.fetch(pairs).keys.select do |points, incidence|
    points <= 8 && incidence <= 20
  end.sort
  brute_keys = brute_residual_states(pairs, 8, 20)
  check(exact_keys == brute_keys, "P=#{pairs}: residual-state DP regression failed")
end

# Exact profile audit without part 13, used to maximize the number of marked
# double points (deficiency 13) in each moment profile.
without_13 = base_square_sum_min_counts(maximum_defect, 12)

expected_exact_state_counts = {
  174 => 4, 173 => 19, 172 => 57, 171 => 57, 170 => 62, 169 => 70,
  168 => 83, 167 => 104, 166 => 139, 165 => 193, 164 => 268,
  163 => 384, 162 => 552, 161 => 788, 160 => 1_142, 159 => 1_667,
  158 => 2_442, 157 => 3_282, 156 => 3_622, 155 => 3_755,
  154 => 3_958, 153 => 4_282
}.freeze
expected_excess_max = {
  174 => 0, 173 => 1, 172 => 1, 171 => 1, 170 => 2, 169 => 2,
  168 => 2, 167 => 2, 166 => 2, 165 => 3, 164 => 3, 163 => 4,
  162 => 4, 161 => 5, 160 => 5, 159 => 6, 158 => 6, 157 => 7,
  156 => 7, 155 => 7, 154 => 7, 153 => 7
}.freeze
expected_bad_line_max = {
  174 => 0, 173 => 2, 172 => 4, 171 => 4, 170 => 4, 169 => 6,
  168 => 6, 167 => 6, 166 => 8, 165 => 18, 164 => 18, 163 => 20,
  162 => 22, 161 => 22, 160 => 25, 159 => 36, 158 => 38, 157 => 38,
  156 => 38, 155 => 38, 154 => 40, 153 => 40
}.freeze

outputs = []
Q15_HIGH_B.downto(Q15_LOW_B) do |b|
  defect = 15 * (M - b)
  exact_rows = []

  q15_relaxed.fetch(b).each do |square_sum, n14, n15, pair_budget, marked_tau,
                                  point_cap, incidence_cap|
    residual_total = defect - 14 * n14 - 15 * n15
    residual_square = square_sum - 196 * n14 - 225 * n15
    coordinate_cap = M - n14 - n15
    feasible_n13 = []
    n13_max = [residual_total / 13, residual_square / 169].min
    (0..n13_max).each do |n13|
      total = residual_total - 13 * n13
      target_square = residual_square - 169 * n13
      next if target_square.negative?
      minimum_count = without_13.fetch(total)[target_square]
      if minimum_count && minimum_count + n13 <= coordinate_cap
        feasible_n13 << n13
      end
    end
    check(!feasible_n13.empty?, "B=#{b}: exact profile lost in n13 audit")
    marked_double_max = feasible_n13.max

    residual_states.fetch(pair_budget).each do |(residual_points, incidence),
                                                (residual_double_max, residual_m_max)|
      next if residual_points > point_cap || incidence > incidence_cap

      residual_j = incidence - residual_points
      residual_tau = 2 * pair_budget - residual_j
      slack = dpw(b, Q) - marked_tau - residual_tau
      next if slack.negative?

      check(slack == residual_j - (b - 26 - n15),
            "B=#{b}: q15 DPW-slack identity failed")
      restriction_deficit = incidence_cap - incidence
      excess = restriction_deficit + slack
      check(excess == point_cap - residual_points,
            "B=#{b}: q15 Chern-excess/support identity failed")

      double_max = marked_double_max + residual_double_max
      nonsimple_max = excess / 3
      point_valency_max = [15, residual_m_max].max
      bad_line_bound = restriction_deficit + 2 * double_max +
                       nonsimple_max * point_valency_max
      check(bad_line_bound < b,
            "B=#{b}: no q15 residue-test line remains")

      exact_rows << [square_sum, n14, n15, pair_budget, residual_points,
                     incidence, slack, restriction_deficit, excess,
                     marked_double_max, residual_double_max, residual_m_max,
                     bad_line_bound]
    end
  end
  exact_rows.uniq!

  exact_count = exact_rows.length
  excess_max = exact_rows.map { |row| row[8] }.max || 0
  bad_line_max = exact_rows.map { |row| row[12] }.max || 0
  check(exact_count == expected_exact_state_counts.fetch(b),
        "B=#{b}: complete exact-state count changed")
  check(excess_max == expected_excess_max.fetch(b),
        "B=#{b}: maximum Chern excess changed")
  check(bad_line_max == expected_bad_line_max.fetch(b),
        "B=#{b}: maximum bad-line bound changed")
  outputs << [b, q15_relaxed.fetch(b).length, exact_count,
              excess_max, bad_line_max]
end

check(outputs.sum { |row| row[2] } == 26_930,
      "M215 q15 total exact-state count mismatch")
check(outputs.map { |row| row[3] }.max == 7,
      "M215 q15 maximum Chern excess mismatch")
check(outputs.map { |row| row[4] }.max == 40,
      "M215 q15 maximum bad-line bound mismatch")
check(outputs.all? { |b, _profiles, _states, _excess, bad| bad < b },
      "uniform q15 good-line gate failed")

puts "RANK15_M215_Q15_LINE_RESIDUE_EXCLUSION: PASS"
puts "definition_source_sha256=#{M216_DEFINITION_SHA256}"
puts "q14_verifier_sha256=#{M215_Q14_VERIFIER_SHA256}"
puts "source_plateau=#{plateau.begin}..#{plateau.end} states=#{plateau.size} q=15"
puts "source_t_gate=164..215 gaps=#{source_gaps.last}..#{source_gaps.first}"
puts "all_q_relaxed_subset=#{all_relaxed_q.values.flatten.uniq.sort.join(',')}"
puts "q15_endpoint_range=B#{Q15_LOW_B}..#{Q15_HIGH_B}"
puts "residual_dp_dimensions=P#{maximum_pairs}_R#{maximum_points}_I#{maximum_incidence}"
puts "residual_dp_states=#{residual_states.sum(&:length)}"
outputs.each do |b, profile_count, state_count, excess_max, bad_line_max|
  puts "B=#{b} relaxed_profiles=#{profile_count} exact_states=#{state_count} " \
       "max_chern_excess=#{excess_max} max_bad_lines=#{bad_line_max}"
end
puts "total_exact_states=#{outputs.sum { |row| row[2] }}"
puts "max_chern_excess=7 max_bad_lines=40<B_min=#{Q15_LOW_B}"
puts "line_residue_gap_mod_p=#{(16 - 1) % P_FIELD}"
puts "conclusion=all_stripped_q15_endpoints_excluded"
puts "composition=all_q_subset_14_15_plus_hash_locked_q14_exclusion_closes_M215"
