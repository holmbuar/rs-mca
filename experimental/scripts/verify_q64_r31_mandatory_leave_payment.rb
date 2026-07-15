#!/usr/bin/env ruby
# frozen_string_literal: true

def check(condition, message)
  raise message unless condition
end

def choose(n, k)
  return 0 if k.negative? || k > n
  k = [k, n - k].min
  (1..k).inject(1) { |a, i| a * (n - k + i) / i }
end

def ceil_div(a, b)
  (a + b - 1) / b
end

n = 2**21
k = 2**20
q = 64
fiber = n / q
check(fiber == 32_768, "q64 fiber")
check(k == 32 * fiber, "distance boundary")

c29 = choose(64, 29)
c30 = choose(64, 30)
leave = ceil_div(c29, 30)
old_r31 = c30 / 31
new_r31 = (c30 - leave) / 31
saving = old_r31 - new_r31

check(c29 == 1_388_818_294_740_297_792, "C(64,29)")
check(c30 == 1_620_288_010_530_347_424, "C(64,30)")
check(leave == 46_293_943_158_009_927, "mandatory leave")
check(old_r31 == 52_267_355_178_398_304, "old r31")
check(new_r31 == 50_774_002_173_301_209, "new r31")
check(saving == 1_493_353_005_097_095, "r31 saving")
check(30 * leave >= c29, "leave flag coverage")
check(30 * (leave - 1) < c29, "leave ceiling sharpness")
check(31 * new_r31 <= c30 - leave, "new shadow capacity")
check(31 * (new_r31 + 1) > c30 - leave, "new cap floor")

# Rebuild the prior q64 caps, then replace only r=31.
caps = (0..31).map do |r|
  distance = 33 - r
  if distance > r
    1
  else
    radius = (distance - 1) / 2
    ball = (0..radius).sum { |i| choose(r, i) * choose(q - r, i) }
    sphere_cap = choose(q, r) / ball
    shadow_size = 2 * r - 32
    shadow_cap = choose(q, shadow_size) / choose(r, shadow_size)
    [sphere_cap, shadow_cap].min
  end
end

old_low = caps.sum
check(old_low == 54_024_655_287_584_031, "old q64 cumulative")
check(caps[31] == old_r31, "old r31 vector entry")
caps[31] = new_r31
new_low = caps.sum
check(new_low == 52_531_302_282_486_936, "new q64 cumulative")
check(old_low - new_low == saving, "cumulative saving")

# Small exact analogues: if v-(k-2) is odd, every (k-2)-set has an
# uncovered (k-1)-extension in every packing of k-blocks.  Exhaustively
# enumerate all block subfamilies for the bounded instances and verify the
# derived leave/cap inequalities directly.
small_families = 0
(4..7).each do |v|
  (3..[v, 4].min).each do |block_size|
    next unless (v - (block_size - 2)).odd?
    blocks = (0...v).to_a.combination(block_size).to_a
    next if blocks.length > 20
    shadows = (0...v).to_a.combination(block_size - 1).to_a
    lower = (0...v).to_a.combination(block_size - 2).to_a
    (0...(1 << blocks.length)).each do |mask|
      family = blocks.each_index.select { |i| ((mask >> i) & 1) == 1 }
      covered = {}
      valid = true
      family.each do |i|
        blocks[i].combination(block_size - 1) do |shadow|
          key = shadow.freeze
          if covered.key?(key)
            valid = false
            break
          end
          covered[key] = true
        end
        break unless valid
      end
      next unless valid

      uncovered = shadows.count { |shadow| !covered.key?(shadow) }
      lower.each do |base|
        extensions = shadows.count do |shadow|
          (base - shadow).empty?
        end
        uncovered_extensions = shadows.count do |shadow|
          (base - shadow).empty? && !covered.key?(shadow)
        end
        check(extensions == v - (block_size - 2), "small extension count")
        check(uncovered_extensions >= 1, "small mandatory leave")
      end
      check((block_size - 1) * uncovered >= lower.length,
            "small leave double count")
      check(block_size * family.length <= shadows.length - uncovered,
            "small shadow ledger")
      small_families += 1
    end
  end
end
check(small_families > 0, "small census empty")

target = 274_854_110_496_187_592
other_payments = [
  59_604_759_736_923_812,
  155_264_635_132_828_620,
  5_078_015_114_505_213
]
paid = new_low + other_payments.sum
allowance = target - paid
check(paid == 272_478_712_266_744_581, "new paid subtotal")
check(allowance == 2_375_398_229_443_011, "new residual allowance")

denominator = choose(47, 27)
universe = choose(128, 27)
cap6 = 6 * universe / denominator
cap7 = 7 * universe / denominator
margin6 = allowance - cap6
check(cap6 == 2_309_103_404_380_482, "common27 cap6 compiler")
check(cap7 == 2_693_953_971_777_229, "common27 cap7 compiler")
check(margin6 == 66_294_825_062_529, "conditional margin")
check(cap6 < allowance && cap7 > allowance, "closing threshold")

puts "Q64_R31_MANDATORY_LEAVE_PAYMENT: PASS"
puts "C64_29=#{c29} C64_30=#{c30} mandatory_leave=#{leave}"
puts "old_r31=#{old_r31} new_r31=#{new_r31} saving=#{saving}"
puts "old_q64_cumulative=#{old_low} new_q64_cumulative=#{new_low}"
puts "paid_subtotal=#{paid} residual_allowance=#{allowance}"
puts "common27_cap6=#{cap6} margin=#{margin6} common27_cap7=#{cap7}"
puts "small_exact_families=#{small_families}"
puts "status=PASS"
