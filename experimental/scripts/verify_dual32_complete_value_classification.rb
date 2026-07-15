# frozen_string_literal: true

P_FIELD = 2_130_706_433
N = 2_097_152
Q = 65_536
D_MAX = 67_471

def check(condition, message)
  raise message unless condition
end

check(N == 32 * Q, "n/q identity")
check(P_FIELD > 32 * D_MAX, "characteristic gate")
check(N > 2 * D_MAX, "2D contact precedes z^n")

minimum_gap = nil
minimum_degree_margin = nil
minimum_cyclotomic_margin = nil

(Q..D_MAX).each do |d|
  delta = 32 * d - N
  gap = N - 31 * d
  expected_gap = Q - 31 * (d - Q)
  check(delta == 32 * (d - Q), "Delta identity D=#{d}")
  check(gap == expected_gap, "G identity D=#{d}")
  check(gap.positive?, "positive gap D=#{d}")
  check(delta < d, "Delta<D D=#{d}")
  check(32 * gap > delta, "32G>Delta D=#{d}")
  check(d + delta - 1 < 2 * d - 1, "differential degree D=#{d}")

  minimum_gap = gap if minimum_gap.nil? || gap < minimum_gap
  margin = 32 * gap - delta
  minimum_degree_margin = margin if minimum_degree_margin.nil? || margin < minimum_degree_margin

  if N.gcd(d) == Q
    cyclotomic_margin = (d - Q).abs
    minimum_cyclotomic_margin = cyclotomic_margin if minimum_cyclotomic_margin.nil? || cyclotomic_margin < minimum_cyclotomic_margin
    check(d == Q, "unique power-map exponent D=#{d}")
  end
end

check(minimum_gap == 5_551, "minimum gap")
check(minimum_degree_margin == 115_712, "minimum 32G-Delta margin")
check(minimum_cyclotomic_margin == 0, "quotient exponent present")

puts "DUAL32_COMPLETE_VALUE_CLASSIFICATION: PASS"
puts "D_range=#{Q}..#{D_MAX}"
puts "minimum_gap=#{minimum_gap}"
puts "minimum_32G_minus_Delta=#{minimum_degree_margin}"
puts "contact_order_min=#{2 * Q}"
puts "n_gt_2D_margin=#{N - 2 * D_MAX}"
puts "unique_exponent=#{Q}"
