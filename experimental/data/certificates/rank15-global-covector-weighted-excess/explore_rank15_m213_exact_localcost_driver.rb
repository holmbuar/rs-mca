#!/usr/bin/env ruby
# frozen_string_literal: true

# Generic exact-state driver for one M=213 branch under the audited local
# ordinary-multiple-point payment.  Usage: ruby FILE q low_B high_B.

require "digest"

SOURCE_SHA256 =
  "f8cfba142607caccb5eb05ad261919f48697fd8a03b542fd65760075057eda1c"
LOCAL_LEMMA_VERIFIER_SHA256 =
  "e9f90dd5bdedd401684fa7cfd16e723d50abea9247e9e901770c35d0425af108"

q_value, low_b, high_b = ARGV.map(&:to_i)
raise "usage: #{File.basename($PROGRAM_NAME)} q low_B high_B" unless ARGV.length == 3
raise "invalid q/B range" unless q_value >= 14 && low_b.positive? && high_b >= low_b

source_path = File.join(__dir__, "verify_rank15_m215_q15_line_residue_exclusion.rb")
lemma_path = File.join(__dir__, "verify_rank15_ordinary_multiple_local_index_lemma.rb")
raise "generic source hash mismatch" unless File.file?(source_path) &&
  Digest::SHA256.file(source_path).hexdigest == SOURCE_SHA256
raise "local lemma verifier hash mismatch" unless File.file?(lemma_path) &&
  Digest::SHA256.file(lemma_path).hexdigest == LOCAL_LEMMA_VERIFIER_SHA256

source = File.read(source_path).split(/^check\(P_FIELD/, 2).first
source = source.sub("M = 215", "M = 213")
               .sub("Q = 15", "Q = #{q_value}")
               .sub("LOW_B = 152", "LOW_B = #{low_b}")
               .sub("HIGH_B = 215", "HIGH_B = #{high_b}")
eval(source, TOPLEVEL_BINDING, source_path)

profiles = base_square_sum_min_counts(15 * (M - LOW_B))
without_13 = base_square_sum_min_counts(15 * (M - LOW_B), 12)
relaxed = Hash.new { |hash, key| hash[key] = [] }
HIGH_B.downto(LOW_B) do |b|
  defect = 15 * (M - b)
  each_profile(defect, profiles) do |square_sum, n14, n15|
    marked_pairs = M * 105 - 14 * defect + (square_sum - defect) / 2
    pair_budget = c2(b) - marked_pairs
    next if pair_budget.negative?
    marked_tau = M * 196 - 28 * defect + square_sum - n15
    point_cap = Q * Q + Q + 1 - (M - n14 - n15)
    incidence_cap = b * (Q - 14) + n14
    floor = residual_tau_floor(pair_budget, point_cap, incidence_cap)
    next unless floor && marked_tau + floor <= dpw(b, Q)
    relaxed[b] << [square_sum, n14, n15, pair_budget, marked_tau,
                   point_cap, incidence_cap]
  end
  relaxed[b].uniq!
end

all_rows = relaxed.values.flatten(1)
raise "empty branch" if all_rows.empty?
maximum_pairs = all_rows.map { |row| row[3] }.max
maximum_points = all_rows.map { |row| row[5] }.max
maximum_incidence = all_rows.map { |row| row[6] }.max
states = residual_state_table(maximum_pairs, maximum_points, maximum_incidence)

outputs = []
# If a connected component of the double-point graph contains only saturated
# lines and no non-simple higher point, the line-residue equations on a tree
# component read L_G x = Q x.  For a tree on n<Q vertices all real Laplacian
# eigenvalues lie in [0,n], hence 0<det(QI-L_G)<Q^n.  The following is the
# largest uniform n for which Q^n<P_FIELD, so reduction modulo P_FIELD cannot
# create a spurious zero determinant.
small_tree_limit = 0
while small_tree_limit + 1 < Q && Q**(small_tree_limit + 1) < P_FIELD
  small_tree_limit += 1
end
check(small_tree_limit.positive?, "small-tree determinant gate vanished")
HIGH_B.downto(LOW_B) do |b|
  defect = 15 * (M - b)
  exact_count = 0
  excess_max = 0
  double_maximum = 0
  bad_max = 0
  failures = []
  graph_unresolved = []
  relaxed.fetch(b).each do |square_sum, n14, n15, pair_budget, marked_tau,
                              point_cap, incidence_cap|
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
      n13_values << n13 if minimum_count && minimum_count + n13 <= coordinate_cap
    end
    check(!n13_values.empty?, "B=#{b}: profile lost in n13 audit")

    states.fetch(pair_budget).each do |(residual_points, incidence),
                                        (residual_doubles, _residual_m_max)|
      next if residual_points > point_cap || incidence > incidence_cap
      j_value = incidence - residual_points
      slack = dpw(b, Q) - marked_tau - (2 * pair_budget - j_value)
      next if slack.negative?
      expected_slack = j_value + (14 - Q) * b + Q * Q + Q + 1 - M + n15
      check(slack == expected_slack, "B=#{b}: q#{Q} slack identity failed")
      restriction_deficit = incidence_cap - incidence
      excess = restriction_deficit + slack
      check(excess == point_cap - residual_points,
            "B=#{b}: q#{Q} excess identity failed")
      doubles = n13_values.max + residual_doubles
      bad = restriction_deficit + 2 * doubles + excess
      exact_count += 1
      excess_max = [excess_max, excess].max
      double_maximum = [double_maximum, doubles].max
      bad_max = [bad_max, bad].max
      failures << [square_sum, n14, n15, pair_budget, residual_points,
                   incidence, slack, restriction_deficit, excess, doubles,
                   bad] if bad >= b
      # A graph with b vertices and doubles edges has at least b-doubles tree
      # components.  At most restriction_deficit+excess components can meet
      # an exceptional line: restriction_deficit bounds unsaturated lines and
      # the local-index lemma bounds the total line valency through non-simple
      # higher points by excess.  Thus the displayed number of clean tree
      # components is forced.  If there are too many to all have more than
      # small_tree_limit vertices, one forbidden small clean tree exists.
      forced_clean_trees =
        [b - doubles - restriction_deficit - excess, 0].max
      graph_closed = forced_clean_trees * small_tree_limit > b
      unless bad < b || graph_closed
        graph_unresolved << [square_sum, n14, n15, pair_budget,
                             residual_points, incidence, slack,
                             restriction_deficit, excess, doubles, bad,
                             forced_clean_trees]
      end
    end
  end
  outputs << [b, relaxed.fetch(b).length, exact_count, excess_max,
              double_maximum, bad_max, failures, graph_unresolved]
end

puts "M213_Q#{Q}_EXACT_LOCALCOST: COMPLETE"
puts "source_sha256=#{SOURCE_SHA256}"
puts "local_lemma_verifier_sha256=#{LOCAL_LEMMA_VERIFIER_SHA256}"
puts "range=B#{LOW_B}..#{HIGH_B}"
puts "dimensions=P#{maximum_pairs}_R#{maximum_points}_I#{maximum_incidence}"
puts "residual_dp_states=#{states.sum(&:length)}"
puts "small_clean_tree_limit=#{small_tree_limit} determinant_bound=#{Q**small_tree_limit}<p"
outputs.each do |b, profiles_count, exact_count, excess_max, doubles_max, bad_max, failures,
                 graph_unresolved|
  puts "B=#{b} profiles=#{profiles_count} exact_states=#{exact_count} " \
       "Emax=#{excess_max} Dmax=#{doubles_max} badmax=#{bad_max} " \
       "line_failures=#{failures.length} graph_unresolved=#{graph_unresolved.length}"
  failures.first(10).each { |row| puts "FAIL B=#{b} row=#{row.inspect}" }
  graph_unresolved.first(10).each do |row|
    puts "GRAPH_UNRESOLVED B=#{b} row=#{row.inspect}"
  end
end
puts "total_exact_states=#{outputs.sum { |row| row[2] }}"
puts "uniform_good_line=#{outputs.all? { |row| row[6].empty? }}"
puts "uniform_line_or_small_tree=#{outputs.all? { |row| row[7].empty? }}"
puts "nonclaim=branch_diagnostic_until_all_q_ranges_are_composed"
