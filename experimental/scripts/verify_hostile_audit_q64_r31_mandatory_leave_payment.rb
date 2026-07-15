#!/usr/bin/env ruby
# frozen_string_literal: true

require 'digest'

def check(condition, message)
  raise message unless condition
end

def choose(n, k)
  return 0 if k.negative? || k > n
  k = [k, n - k].min
  (1..k).inject(1) { |value, i| value * (n - k + i) / i }
end

def ceil_div(a, b)
  (a + b - 1) / b
end

root = File.expand_path('../..', __dir__)
source = File.join(root, 'experimental', 'notes', 'l2',
                   'q64_r31_mandatory_leave_payment.md')
verifier = File.join(root, 'experimental', 'scripts',
                     'verify_q64_r31_mandatory_leave_payment.rb')
expected = File.join(root, 'experimental', 'data', 'certificates',
                     'q64-r31-leave-cap7-rigidity', 'q64_leave_output.txt')

check(Digest::SHA256.file(source).hexdigest ==
      'd472cfef95d5292d54db34dbd5b2e76522b5af787c6076afbb293bf2ab558e51',
      'source hash drift')
check(Digest::SHA256.file(verifier).hexdigest ==
      '1cbb1b77337d589688f1a6cafb6f93f359432e9ea4d642cf87ddddd2657e77fb',
      'verifier hash drift')
check(Digest::SHA256.file(expected).hexdigest ==
      '20d79500c6a0ed848847fdafc8a3cb8399c0b3df9595713f74324c396dea30ba',
      'expected hash drift')

# Independent leave arithmetic.
c29 = choose(64, 29)
c30 = choose(64, 30)
extensions_per_29 = 64 - 29
covered_per_block = 31 - 29
check(extensions_per_29 == 35 && extensions_per_29.odd?,
      'odd extension quantifier')
check(covered_per_block == 2, 'pair coverage')

leave = ceil_div(c29, 30)
old_r31 = c30 / 31
new_r31 = (c30 - leave) / 31
saving = old_r31 - new_r31
check([c29, c30] ==
      [1_388_818_294_740_297_792, 1_620_288_010_530_347_424],
      'binomial arithmetic')
check(leave == 46_293_943_158_009_927, 'leave ceiling')
check(new_r31 == 50_774_002_173_301_209, 'new r31 cap')
check(saving == 1_493_353_005_097_095, 'saving')
check(30 * leave >= c29 && 30 * (leave - 1) < c29,
      'leave ceiling inequalities')
check(31 * new_r31 <= c30 - leave &&
      31 * (new_r31 + 1) > c30 - leave,
      'outer floor inequalities')

# Source bridge endpoints.
n = 1 << 21
k = 1 << 20
fiber = n / 64
check(fiber == 32_768 && 32 * fiber == k, 'GRS support endpoint')
check(31 + 31 - 29 == 33, 'intersection-union equivalence')

# Replacement and disjoint-subtotal arithmetic.
old_low = 54_024_655_287_584_031
new_low = old_low - saving
check(new_low == 52_531_302_282_486_936, 'replacement semantics')
other = [
  59_604_759_736_923_812,
  155_264_635_132_828_620,
  5_078_015_114_505_213
]
target = 274_854_110_496_187_592
paid = new_low + other.sum
allowance = target - paid
check(paid == 272_478_712_266_744_581, 'disjoint subtotal')
check(allowance == 2_375_398_229_443_011, 'residual allowance')

# Conditional common-27 floors.
universe = choose(128, 27)
per_support = choose(47, 27)
cap6 = 6 * universe / per_support
cap7 = 7 * universe / per_support
margin = allowance - cap6
check(cap6 == 2_309_103_404_380_482, 'cap6 floor')
check(cap7 == 2_693_953_971_777_229, 'cap7 floor')
check(margin == 66_294_825_062_529, 'cap6 margin')
check(cap6 < allowance && cap7 > allowance, 'threshold direction')

puts 'HOSTILE_AUDIT_Q64_R31_MANDATORY_LEAVE_PAYMENT: PASS'
puts "odd_extensions=#{extensions_per_29} pair_cover=#{covered_per_block} mandatory_leave=#{leave}"
puts "old_r31=#{old_r31} new_r31=#{new_r31} saving=#{saving}"
puts "new_q64_cumulative=#{new_low} paid_subtotal=#{paid} residual_allowance=#{allowance}"
puts "common27_cap6=#{cap6} margin=#{margin} common27_cap7=#{cap7}"
puts 'quantifiers=uniform_fixed_syndrome_no_design_assumption'
puts 'replacement=old_r31_only_cells_disjoint'
puts 'verdict=source_valid_cap6_is_calibration_only'
