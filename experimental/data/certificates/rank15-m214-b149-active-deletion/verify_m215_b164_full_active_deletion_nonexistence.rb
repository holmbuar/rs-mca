#!/usr/bin/env ruby
# frozen_string_literal: true

# Exact, dependency-free verifier for the theorem
#   164 <= b <= d <= 215,
# with d active arrangement lines and b marked 15-fold points.

require 'digest'

def demand(condition, message)
  raise "FAIL: #{message}" unless condition
end

SUPPORT = File.join(__dir__, 'verify_m217_b195_dual_arrangement_nonexistence.rb')
SUPPORT_SHA256 =
  '6260d6f7f44391227c23b5469ce74a2ca1bdd2745a69a94758c8f3fb02b5c3f6'
demand(Digest::SHA256.file(SUPPORT).hexdigest == SUPPORT_SHA256,
       'frozen arithmetic-support hash drift')
EXPECTED_OUTPUT = File.join(
  __dir__, 'verify_m215_b164_full_active_deletion_nonexistence.expected.txt'
)
EXPECTED_OUTPUT_SHA256 =
  '014381b3b29e5edddc9c64423ea8e0f1e43fe5985865f62c7db5eabc134c4594'
demand(Digest::SHA256.file(EXPECTED_OUTPUT).hexdigest == EXPECTED_OUTPUT_SHA256,
       'expected-output hash drift')
definitions = File.read(SUPPORT).split('P_FIELD =', 2).first
demand(definitions.include?('def coarse_branch_margin'),
       'support definition delimiter drift')
eval(definitions, TOPLEVEL_BINDING, SUPPORT)

FIELD_CHARACTERISTIC = 2_130_706_433
MINIMUM_MARKED = 164
MAXIMUM_DEGREE = 215
demand(FIELD_CHARACTERISTIC > MAXIMUM_DEGREE,
       'deployed characteristic gate')

high_rows = []
coarse_rows = []
least_positive_coarse = nil

(MINIMUM_MARKED..MAXIMUM_DEGREE).each do |marked|
  (marked..MAXIMUM_DEGREE).each do |degree|
    forced_tau = choose2(degree) + 91 * marked
    high_start = (degree + 1) / 2
    (high_start...degree).each do |syzygy|
      slack = dpw_high(degree, syzygy) - forced_tau
      high_rows << [marked, degree, syzygy, slack] if slack >= 0
    end

    (0...high_start).each do |syzygy|
      next if dpw_low(degree, syzygy) < forced_tau

      (0..[syzygy + 1, degree - 1].min).each do |bad|
        gap = coarse_branch_margin(marked, degree, syzygy, bad)
        next if gap.nil?

        if gap <= 0
          coarse_rows << [marked, degree, syzygy, bad, gap]
        elsif least_positive_coarse.nil? || gap < least_positive_coarse
          least_positive_coarse = gap
        end
      end
    end
  end
end

demand(high_rows.empty?, "high-DPW survivors #{high_rows.first(5).inspect}")
demand(coarse_rows.length == 29_595,
       "coarse row count #{coarse_rows.length}")
demand(coarse_rows.map { |row| row[3] }.max == 35,
       'maximum coarse bad-line count')
demand(coarse_rows.none? { |row| row[3] > row[2] },
       'coarse survivor violates B<=r')
demand(least_positive_coarse&.positive?,
       'coarse eliminated rows lack strict margin')

structural_rows = []
finite_space_cut = []
coarse_rows.each do |row|
  marked, degree, syzygy, bad = row
  good = degree - bad
  q = syzygy + 1 - bad
  demand(good > 15, "G<=15 in coarse row #{row.inspect}")
  demand(choose2(bad) < 91 * marked,
         "full-pencil pair gate failed #{row.inspect}")
  if q < 2 || good > q * (q - 1) + 1
    finite_space_cut << row
  else
    structural_rows << row
  end
end

demand(finite_space_cut.length == 8_541,
       "finite-space cut #{finite_space_cut.length}")
demand(structural_rows.length == 21_054,
       "structural row count #{structural_rows.length}")
zero_bad_rows, positive_bad_rows = structural_rows.partition do |row|
  row[3].zero?
end
demand(zero_bad_rows.length == 121,
       "B=0 row count #{zero_bad_rows.length}")
demand(positive_bad_rows.length == 20_933,
       "B>0 row count #{positive_bad_rows.length}")

positive_survivors = []
exceptional_integer_states = []
infeasible_rows = []
least_positive_joint = nil
joint_state_count = 0

positive_bad_rows.each do |row|
  marked, degree, syzygy, bad = row
  good = degree - bad
  q = syzygy + 1 - bad
  deletion_mdr = syzygy - bad
  demand(deletion_mdr == q - 1, "deletion mdr identity #{row.inspect}")

  parent_cap = dpw_low(degree, syzygy) - choose2(degree) - 91 * marked
  total_deficiency = 15 * (degree - marked)
  eg_min = [0, total_deficiency - 14 * bad].max
  eg_max = [14 * good, total_deficiency].min
  branch_best = nil
  branch_state = nil

  (eg_min..eg_max).each do |good_deficiency|
    bad_marked_incidence =
      15 * bad - total_deficiency + good_deficiency
    next unless (bad..15 * bad).cover?(bad_marked_incidence)

    c_min_numerator = 14 * bad_marked_incidence - bad * good
    c_min = c_min_numerator.positive? ? (c_min_numerator + 1) / 2 : 0
    c_max = [choose2(bad), 7 * bad_marked_incidence].min
    next if c_min > c_max

    (c_min..c_max).each do |marked_bad_pairs|
      marked_bad_good =
        14 * bad_marked_incidence - 2 * marked_bad_pairs
      next unless (0..bad * good).cover?(marked_bad_good)

      joint_state_count += 1
      residual_bad_good = bad * good - marked_bad_good
      erased_upper = [marked_bad_pairs / 91,
                      bad_marked_incidence / 14,
                      15 * good - good_deficiency].min
      slot_capacity = good * q - (15 * good - good_deficiency) +
                      erased_upper
      next if slot_capacity.negative?

      all_good_residual_degree =
        good * (degree - 211) + 14 * good_deficiency
      good_good_degree =
        [0, all_good_residual_degree - residual_bad_good].max
      lower = partition_charge(good_good_degree, slot_capacity)
      next if lower.nil?

      deletion_marked_excess_lower =
        91 * marked - 13 * bad_marked_incidence + marked_bad_pairs -
        marked_bad_pairs / 105
      deletion_cap = dpw_low(good, deletion_mdr) - choose2(good) -
                     deletion_marked_excess_lower
      effective_cap = [parent_cap, deletion_cap].min
      gap = lower - effective_cap
      state = [good_deficiency, bad_marked_incidence, marked_bad_pairs,
               residual_bad_good, erased_upper, slot_capacity,
               good_good_degree, lower, effective_cap,
               parent_cap, deletion_cap]

      unless q == 15 && good >= 198
        if lower.ceil <= effective_cap
          exceptional_integer_states <<
            [marked, degree, syzygy, bad, q, good, *state]
        end
      end
      if branch_best.nil? || gap < branch_best
        branch_best = gap
        branch_state = state
      end
    end
  end

  if branch_best.nil?
    infeasible_rows << row
  elsif branch_best <= 0
    positive_survivors << [marked, degree, syzygy, bad,
                           q, good, branch_best, branch_state]
  elsif least_positive_joint.nil? || branch_best < least_positive_joint
    least_positive_joint = branch_best
  end
end

demand(infeasible_rows.empty?,
       "joint-C branches without relaxed state #{infeasible_rows.first(5).inspect}")
demand(joint_state_count == 373_774_811,
       "joint-C state count #{joint_state_count}")
demand(positive_survivors.length == 404,
       "positive-B survivor count #{positive_survivors.length}")
demand(least_positive_joint == Rational(1, 120),
       "least positive joint-C margin #{least_positive_joint}")

qg_distribution = positive_survivors.group_by do |row|
  [row[4], row[5]]
end.transform_values(&:length)
demand(qg_distribution == {
         [15, 207] => 8,
         [15, 208] => 74,
         [15, 209] => 137,
         [15, 210] => 181,
         [16, 214] => 4
       }, "positive survivor q,G distribution #{qg_distribution.inspect}")

positive_design, positive_other = positive_survivors.partition do |row|
  row[4] == 15 && row[5] >= 198
end
demand(positive_design.length == 400,
       "positive design count #{positive_design.length}")
expected_positive_other = [
  [164, 215, 16, 1, 16, 214, Rational(-11, 78)],
  [165, 215, 16, 1, 16, 214, Rational(-4, 39)],
  [166, 215, 16, 1, 16, 214, Rational(-5, 78)],
  [167, 215, 16, 1, 16, 214, Rational(-1, 39)]
]
demand(positive_other.map { |row| row[0, 7] } == expected_positive_other,
       "positive exceptional rows #{positive_other.inspect}")

expected_exceptional_states = [
  [164, 215, 16, 1, 16, 214, 751, 1, 0, 200, 0, 965,
   11_170, Rational(366_355, 78), 4_697, 4_699, 4_697],
  [165, 215, 16, 1, 16, 214, 736, 1, 0, 200, 0, 950,
   10_960, Rational(179_630, 39), 4_606, 4_608, 4_606],
  [166, 215, 16, 1, 16, 214, 721, 1, 0, 200, 0, 935,
   10_750, Rational(352_165, 78), 4_515, 4_517, 4_515],
  [167, 215, 16, 1, 16, 214, 706, 1, 0, 200, 0, 920,
   10_540, Rational(172_535, 39), 4_424, 4_426, 4_424]
]
demand(exceptional_integer_states == expected_exceptional_states,
       "exceptional integer-state ledger #{exceptional_integer_states.inspect}")

zero_design, zero_other = zero_bad_rows.partition do |row|
  _marked, degree, syzygy, bad = row
  syzygy + 1 - bad == 15 && degree - bad >= 198
end
demand(zero_design.length == 106,
       "B=0 design count #{zero_design.length}")

expected_zero_other = [
  [164, 214, 15, 0, Rational(-3, 26)],
  [164, 215, 15, 0, Rational(-31, 78)],
  [165, 214, 15, 0, Rational(-1, 13)],
  [165, 215, 15, 0, Rational(-14, 39)],
  [166, 214, 15, 0, Rational(-1, 26)],
  [166, 215, 15, 0, Rational(-25, 78)],
  [167, 214, 15, 0, Rational(0)],
  [167, 215, 15, 0, Rational(-11, 39)],
  [168, 215, 15, 0, Rational(-19, 78)],
  [169, 215, 15, 0, Rational(-8, 39)],
  [170, 215, 15, 0, Rational(-1, 6)],
  [171, 215, 15, 0, Rational(-5, 39)],
  [172, 215, 15, 0, Rational(-7, 78)],
  [173, 215, 15, 0, Rational(-2, 39)],
  [174, 215, 15, 0, Rational(-1, 78)]
]
demand(zero_other == expected_zero_other,
       "B=0 terminal rows #{zero_other.inspect}")

zero_squeezes = zero_other.map do |marked, degree, syzygy, _bad, gap|
  upper = dpw_low(degree, syzygy) - choose2(degree) - 91 * marked
  lower = upper + gap
  demand(lower.ceil == upper,
         "terminal integral squeeze b=#{marked},d=#{degree}")
  [marked, degree, lower, upper]
end

# Terminal arithmetic for every equality branch.  The d=214 threshold 163
# also covers the 214-line deletion of the four B=1 exceptional rows.
terminal_families = [
  [215, 164, 416, 1_066, [4_717, 15_384, 17_689, 14_161], 2_988],
  [214, 163, 432, 1_134, [7_074, 17_525, 22_201, 18_225], 5_350]
]
terminal_ledgers = terminal_families.map do |degree, marked_minimum,
                                               epsilon_base,
                                               epsilon_square_base,
                                               expected_moment_minima,
                                               expected_double_minimum|
  tau = dpw_low(degree, 15)
  sum_mu_minus_one = degree * (degree - 1) - tau
  demand(sum_mu_minus_one == 16 * degree - 241,
         "sum(mu-1), d=#{degree}")
  moment_minima = (1..4).map do |defect|
    point_count = 241 - defect
    epsilon_sum = epsilon_base - 15 * defect
    epsilon_squares = epsilon_square_base - 225 * defect
    gaps = (marked_minimum..point_count).map do |marked|
      (epsilon_sum - marked)**2 -
        (point_count - marked) * (epsilon_squares - marked)
    end
    demand(gaps.min.positive?, "Cauchy D=#{defect},d=#{degree}")
    gaps.min
  end
  demand(moment_minima == expected_moment_minima,
         "moment minima d=#{degree}: #{moment_minima.inspect}")
  demand(epsilon_square_base - 225 * 5 < marked_minimum,
         "D>=5 exclusion d=#{degree}")

  double_minimum = (marked_minimum..240).map do |marked|
    remaining_sum = epsilon_base - 14 - marked
    remaining_squares = epsilon_square_base - 196 - marked
    remaining_sum**2 - (240 - marked) * remaining_squares
  end.min
  demand(double_minimum == expected_double_minimum,
         "double-point minimum d=#{degree}: #{double_minimum}")
  [degree, tau, sum_mu_minus_one, moment_minima, double_minimum]
end

demand(15 % FIELD_CHARACTERISTIC != 0,
       'invariant-line residue contradiction vanished')

survivor_ledger = positive_survivors.map do |row|
  gap = row[6]
  [*row[0, 6], gap.numerator, gap.denominator].join(',')
end.sort.join("\n")
survivor_digest = Digest::SHA256.hexdigest(survivor_ledger)
expected_survivor_digest =
  'd4f0798b89f133791e2e79d90851eb51937cbee4bb816ee5634c64d7f0f67dc6'
demand(survivor_digest == expected_survivor_digest,
       "positive-B survivor ledger digest #{survivor_digest}")

canonical_lines = [
  'M215_B164_FULL_ACTIVE_DELETION_NONEXISTENCE: PASS',
  'field_characteristic=2130706433>215 range=164<=b<=d<=215',
  'high_DPW_survivors=0',
  "coarse_rows=#{coarse_rows.length} max_B=35",
  "finite_space_cut=#{finite_space_cut.length} structural_rows=#{structural_rows.length}",
  "B0_rows=#{zero_bad_rows.length} Bpositive_rows=#{positive_bad_rows.length}",
  "joint_C_states=#{joint_state_count} joint_C_survivors=#{positive_survivors.length}",
  "joint_C_min_positive_gap=#{least_positive_joint} qG=#{qg_distribution.inspect}",
  "joint_C_survivor_sha256=#{survivor_digest}",
  "positive_design=#{positive_design.length} exceptional=#{positive_other.length}",
  "B0_design=#{zero_design.length} B0_terminal=#{zero_other.length}",
  "terminal_squeezes=#{zero_squeezes.inspect}",
  "terminal_ledgers=#{terminal_ledgers.inspect}",
  'terminal_residue_contradiction=16=1 impossible in char0 or char>215',
  'RESULT: PASS'
]
canonical_output = canonical_lines.join("\n") + "\n"
demand(File.binread(EXPECTED_OUTPUT) == canonical_output,
       'canonical stdout differs byte-for-byte from expected artifact')
print canonical_output
