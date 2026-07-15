#!/usr/bin/env ruby
# frozen_string_literal: true

# Exact replay for the value-fiber pair/cubic occupancy countermodel at the
# first state below the accepted Hahn payment.

N_CODE = 2_097_152
K_CODE = 1_048_576
M_AGREE = 1_116_047
U_STATE = 1_043_459
FIELD_SIZE = 2_130_706_433
TARGET = 274_854_110_496_187_592

N_RESIDUAL = N_CODE - U_STATE
WEIGHT = M_AGREE - U_STATE
PAIR_ROOT_CAP = K_CODE - U_STATE - 1

CHILD_ACTIVE_DISTANCES = [67_472, 67_586, 67_587, 67_700, 67_701].freeze
EXPECTED_CHILD_CAP = 41_358_983_685_320_209
ERROR_ACTIVE_DISTANCES = [67_473, 67_587, 67_588, 67_701, 67_702].freeze
EXPECTED_ERROR_FIBER_CAP = 28_334_997_835_769_598
EXPECTED_RELAXED_LIST = 600_370_193_369_924_877

def check(condition, message)
  raise message unless condition
end

def choose(number, order)
  return 0 if order.negative? || order > number

  order = [order, number - order].min
  (1..order).inject(1) do |value, index|
    value * (number - order + index) / index
  end
end

def hahn(length, weight, degree, distance)
  (0..degree).sum do |term|
    Rational(
      (-1)**term * choose(degree, term) *
        choose(length + 1 - degree, term) * choose(distance, term),
      choose(weight, term) * choose(length - weight, term)
    )
  end
end

def solve_linear(matrix, right_hand_side)
  size = right_hand_side.length
  size.times do |column|
    pivot = (column...size).find { |row| !matrix[row][column].zero? }
    raise "singular child Hahn system" unless pivot

    matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
    right_hand_side[column], right_hand_side[pivot] =
      right_hand_side[pivot], right_hand_side[column]
    scale = matrix[column][column]
    (column...size).each { |index| matrix[column][index] /= scale }
    right_hand_side[column] /= scale

    size.times do |row|
      next if row == column

      factor = matrix[row][column]
      next if factor.zero?

      (column...size).each do |index|
        matrix[row][index] -= factor * matrix[column][index]
      end
      right_hand_side[row] -= factor * right_hand_side[column]
    end
  end
  right_hand_side
end

def balanced_moment(total, bucket_count, order)
  base, residue = total.divmod(bucket_count)
  (bucket_count - residue) * choose(base, order) +
    residue * choose(base + 1, order)
end

def certified_hahn_cap(length, weight, intersection_cap, active_distances)
  degrees = (1..5).to_a
  matrix = active_distances.map do |distance|
    degrees.map { |degree| hahn(length, weight, degree, distance) }
  end
  coefficients = solve_linear(matrix, Array.new(5, Rational(-1, 1)))
  check(coefficients.all?(&:positive?), "Hahn coefficient sign")
  polynomial = lambda do |distance|
    1 + degrees.each_with_index.sum do |degree, index|
      coefficients[index] * hahn(length, weight, degree, distance)
    end
  end
  minimum_distance = weight - intersection_cap
  check((minimum_distance..weight).all? do |distance|
          polynomial.call(distance) <= 0
        end, "Hahn sign interval")
  (1 + coefficients.sum).floor
end

check([N_RESIDUAL, WEIGHT, PAIR_ROOT_CAP] == [1_053_693, 72_588, 5_116],
      "new first-wall parameters")

# Reconstruct both pointwise value-fiber ceilings instead of trusting copied
# decimals.  The U-value fiber has threshold m; every other value fiber gains
# one agreement after changing that one received symbol and has threshold m+1.
child_length = N_RESIDUAL - 1
child_intersection_cap = PAIR_ROOT_CAP - 1
child_cap = certified_hahn_cap(
  child_length, WEIGHT - 1, child_intersection_cap,
  CHILD_ACTIVE_DISTANCES
)
check(child_cap == EXPECTED_CHILD_CAP, "child Hahn cap")
error_fiber_cap = certified_hahn_cap(
  child_length, WEIGHT, child_intersection_cap,
  ERROR_ACTIVE_DISTANCES
)
check(error_fiber_cap == EXPECTED_ERROR_FIBER_CAP,
      "modified-word error-fiber Hahn cap")

# The strongest bound from agreement incidence plus the pointwise child cap.
relaxed_list = N_RESIDUAL * child_cap / WEIGHT
check(relaxed_list == EXPECTED_RELAXED_LIST, "incidence/child relaxed list")
check(relaxed_list > TARGET, "countermodel is not above target")

agreement_total = relaxed_list * WEIGHT
agreement_base, agreement_residue = agreement_total.divmod(N_RESIDUAL)
check(agreement_base == child_cap - 1, "balanced agreement base")
check(agreement_residue == 1_043_532, "balanced agreement residue")
check(agreement_base + 1 == child_cap, "pointwise child cap saturation")

pair_count = 0
triple_count = 0
maximum_error_bucket = 0
[
  [N_RESIDUAL - agreement_residue, agreement_base],
  [agreement_residue, agreement_base + 1]
].each do |coordinate_count, agreement_bucket|
  error_total = relaxed_list - agreement_bucket
  error_base, error_residue = error_total.divmod(FIELD_SIZE - 1)
  maximum_error_bucket = [maximum_error_bucket,
                          error_base + (error_residue.positive? ? 1 : 0)].max
  pair_at_coordinate = choose(agreement_bucket, 2) +
    balanced_moment(error_total, FIELD_SIZE - 1, 2)
  triple_at_coordinate = choose(agreement_bucket, 3) +
    balanced_moment(error_total, FIELD_SIZE - 1, 3)
  pair_count += coordinate_count * pair_at_coordinate
  triple_count += coordinate_count * triple_at_coordinate
end
check(maximum_error_bucket == 262_359_564, "maximum error-value bucket")
check(maximum_error_bucket < error_fiber_cap, "error-value fiber cap")

pair_cap = PAIR_ROOT_CAP * choose(relaxed_list, 2)
strong_triple_cap = (PAIR_ROOT_CAP - 1) * choose(relaxed_list, 3)
pair_slack = pair_cap - pair_count
triple_slack = strong_triple_cap - triple_count

check(pair_count ==
      901_205_540_550_566_667_931_568_949_443_065_569_399,
      "pair count")
check(pair_slack ==
      20_811_155_574_084_179_721_487_399_799_490_395_217,
      "pair slack")
check(triple_count ==
      12_424_314_017_670_523_947_730_899_534_775_908_638_224_058_405_553_538_731,
      "triple count")
check(triple_slack ==
      172_056_733_353_953_458_998_899_367_231_177_382_803_429_011_586_301_107_519,
      "strong triple slack")
check(pair_slack.positive? && triple_slack.positive?,
      "strict value-fiber moment feasibility")

puts "RANK16_U1043459_VALUE_FIBER_MOMENT_ROUTE_CUT: PASS"
puts "parameters=N#{N_RESIDUAL}_a#{WEIGHT}_h#{PAIR_ROOT_CAP}_p#{FIELD_SIZE}"
puts "child_hahn_cap=#{child_cap}"
puts "modified_word_error_fiber_hahn_cap=#{error_fiber_cap} max_model_bucket=#{maximum_error_bucket}"
puts "relaxed_list=#{relaxed_list} target=#{TARGET} ratio=#{relaxed_list.to_f / TARGET}"
puts "agreement_profile=#{N_RESIDUAL - agreement_residue}x#{agreement_base},#{agreement_residue}x#{agreement_base + 1}"
puts "pair_slack=#{pair_slack}"
puts "strong_zero_collinearity_triple_slack=#{triple_slack}"
puts "nonclaim=occupancy_model_not_an_RS_list_no_state_paid"
