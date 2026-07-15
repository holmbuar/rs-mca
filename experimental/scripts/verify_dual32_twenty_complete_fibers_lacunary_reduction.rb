# frozen_string_literal: true

N = 2_097_152
Q = 65_536
D_MAX = 67_471

def check(condition, message)
  raise message unless condition
end

check(N == 32 * Q, "n/q identity")
check(N - 31 * D_MAX == 5_551, "endpoint gap")

worst_large = -1
worst_small = 33
worst_complete = 33
worst_d = nil

(Q..D_MAX).each do |d|
  s = d - Q
  delta = 32 * s
  gap = N - 31 * d
  check(gap.positive?, "positive locator gap at D=#{d}")
  check(delta < 12 * gap, "twelve-large-residual inequality at D=#{d}")

  large = delta / gap
  small = 32 - large
  complete = small - 1
  check(large <= 11, "large residual count at D=#{d}")
  check(small >= 21, "small residual count at D=#{d}")
  check(complete >= 20, "complete residual count at D=#{d}")

  if large > worst_large
    worst_large = large
    worst_small = small
    worst_complete = complete
    worst_d = d
  end

  check(d - gap == 32 * d - N, "lacunary degree identity at D=#{d}")
end

check(worst_d == 67_469, "first worst residual-count endpoint")
check(worst_large == 11, "worst large count")
check(worst_small == 21, "worst small count")
check(worst_complete == 20, "worst complete count")
check(32 * (D_MAX - Q) == 61_920, "maximum low degree")

puts "DUAL32_TWENTY_COMPLETE_FIBERS_LACUNARY_REDUCTION: PASS"
puts "D_range=#{Q}..#{D_MAX}"
puts "minimum_gap=#{N - 31 * D_MAX}"
puts "maximum_residual_sum=#{32 * (D_MAX - Q)}"
puts "maximum_large_residuals=#{worst_large}"
puts "minimum_small_residuals=#{worst_small}"
puts "minimum_complete_fibers=#{worst_complete}"
puts "maximum_low_degree=#{32 * D_MAX - N}"
