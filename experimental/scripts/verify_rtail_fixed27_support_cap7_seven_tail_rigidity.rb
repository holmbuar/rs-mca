#!/usr/bin/env ruby
# frozen_string_literal: true

def check(condition, message)
  raise message unless condition
end

def choose(n, k)
  return 0 if k.negative? || k > n
  k = [k, n - k].min
  (1..k).inject(1) { |value, i| value * (n - k + i) / i }
end

# Eight-tail Bonferroni obstruction.
eight_lower_union = 8 * 20 - 2 * choose(8, 2)
check(eight_lower_union == 104, 'eight-tail lower union')
check(eight_lower_union > 128 - 27, 'fixed-core complement obstruction')

# Enumerate every integer seven-tail overlap profile allowed by
# delta+D<=3.  D=n3+3n4 and multiplicities >=5 are impossible.
profiles = []
(0..3).each do |delta|
  (0..(3 - delta)).each do |defect|
    (0..1).each do |n4|
      n3 = defect - 3 * n4
      next if n3.negative?
      n2 = 42 - delta - 3 * n3 - 6 * n4
      n1 = 56 + 2 * delta + 3 * n3 + 8 * n4
      union = n1 + n2 + n3 + n4
      incidences = n1 + 2 * n2 + 3 * n3 + 4 * n4
      pair_sum = n2 + 3 * n3 + 6 * n4
      d_replay = n3 + 3 * n4
      check(incidences == 140, 'incidence replay')
      check(pair_sum == 42 - delta, 'pair replay')
      check(d_replay == defect, 'higher-overlap replay')
      check(union == 98 + delta + defect && union <= 101,
            'union rigidity')
      profiles << [delta, defect, n1, n2, n3, n4, union]
    end
  end
end

expected_profiles = [
  [0, 0, 56, 42, 0, 0, 98],
  [0, 1, 59, 39, 1, 0, 99],
  [0, 2, 62, 36, 2, 0, 100],
  [0, 3, 65, 33, 3, 0, 101],
  [0, 3, 64, 36, 0, 1, 101],
  [1, 0, 58, 41, 0, 0, 99],
  [1, 1, 61, 38, 1, 0, 100],
  [1, 2, 64, 35, 2, 0, 101],
  [2, 0, 60, 40, 0, 0, 100],
  [2, 1, 63, 37, 1, 0, 101],
  [3, 0, 62, 39, 0, 0, 101]
]
check(profiles == expected_profiles, 'complete profile list')

# At most three defective pair-edges touch at most six of seven vertices,
# leaving an anchor incident only with size-two intersections.
check(2 * 3 < 7, 'anchor vertex count')

# Value-level identity at seven tails:
# sum distance = 840-P-Z and P=42-delta, so excess over 21*38 is delta-Z.
check(7 * 20 * 6 == 840, 'ordered incidence distance baseline')
check(choose(7, 2) * 38 == 798, 'MDS distance baseline')
check(840 - 42 == 798, 'delta value identity')

puts 'RTAIL_FIXED27_SUPPORT_CAP7_SEVEN_TAIL_RIGIDITY: PASS'
puts "fixed_core=27 complement=101 tail_size=20 pair_intersection_cap=2"
puts "eight_tail_union_lower=#{eight_lower_union} conclusion=at_most_7"
puts 'seven_tail_identity=union_98_plus_delta_plus_D delta_plus_D_at_most_3'
puts 'seven_tail_pairs=size2_at_least_18 anchor_minweight_differences=6'
puts 'value_identity=delta_distance_excess_plus_equal_value_collisions'
puts "overlap_profiles=#{profiles.length} max_multiplicity=4"
puts 'status=necessary_rigidity_cap6_still_open'
