#!/usr/bin/env ruby
# frozen_string_literal: true

# Exact arithmetic replay for the fixed-pair active-pencil grid/tail cut.
# Standard library only; all inequalities are integral.

def check(condition, message)
  raise "CHECK FAILED: #{message}" unless condition
end

def c2(x)
  x < 2 ? 0 : x * (x - 1) / 2
end

# Minimum sum binom(d_i,2) over at most r nonnegative degrees of total e.
def balanced_pair_sum(e, r)
  q, rem = e.divmod(r)
  r * c2(q) + rem * q
end

# Minimum sum binom(q_x,2) for total incidence i on u coordinates.
def integral_collision_floor(i, u)
  q, rem = i.divmod(u)
  u * c2(q) + rem * q
end

# Exact maximum total number of upgrades h_i-1 for f full direction bins,
# where 1<=h_i<=q and sum binom(h_i,2)<=budget.
def full_direction_upgrades(q, f, budget)
  return 0 if f.zero?
  return -1 if budget.negative?

  layer = (0..(q - 1)).select { |ell| f * ell * (ell + 1) / 2 <= budget }.max
  return f * (q - 1) if layer == q - 1

  spent = f * layer * (layer + 1) / 2
  f * layer + [f, (budget - spent) / (layer + 1)].min
end

# Direction-pair capacity.  Coordinate weights in one primitive direction
# total at most d.  Selecting a maximum-occupancy line in every occupied
# direction charges binom(h,2) disjoint neighbor pairs.  Weight transfer
# leaves floor(u/d) full directions and at most one partial direction.
def direction_pair_capacity(d, u, pair_budget, q)
  full, rem = u.divmod(d)
  if rem.zero?
    return u + d * full_direction_upgrades(q, full, pair_budget)
  end

  best = -1
  (1..q).each do |partial_h|
    partial_cost = c2(partial_h)
    next if partial_cost > pair_budget

    upgrades = full_direction_upgrades(q, full, pair_budget - partial_cost)
    value = u + rem * (partial_h - 1) + d * upgrades
    best = value if value > best
  end
  best
end

# Brute-force regression for the closed form on small full-bin instances.
(2..6).each do |q|
  (1..5).each do |full|
    max_budget = full * c2(q)
    (0..max_budget).each do |budget|
      dp = Array.new(budget + 1, -1)
      dp[0] = 0
      full.times do
        nxt = Array.new(budget + 1, -1)
        dp.each_with_index do |value, used|
          next if value.negative?
          (1..q).each do |h|
            cost = c2(h)
            next if used + cost > budget
            candidate = value + h - 1
            nxt[used + cost] = candidate if candidate > nxt[used + cost]
          end
        end
        dp = nxt
      end
      brute = dp.max
      closed = full_direction_upgrades(q, full, budget)
      check(closed == brute, "upgrade DP #{[q, full, budget, closed, brute]}")
    end
  end
end

N = 1_053_693
A = 72_588
H = 5_116
TAIL_UNIVERSE = N - (2 * A - H)
check(TAIL_UNIVERSE == 913_633, "tail universe")

def row_bound(c)
  d = H - c
  (A - c) / d - 1
end

def shared_pair_floor(e, rows)
  2 * balanced_pair_sum(e, rows)
end

def graph_ceiling(rows)
  rows * [rows, 14].min
end

def second_moment_feasible?(c, e)
  d = H - c
  tail = 62_356 + c
  rows = row_bound(c)
  pair_budget = c2(e) - shared_pair_floor(e, rows)
  integral_collision_floor(e * tail, TAIL_UNIVERSE) <= d * pair_budget
end

def direction_pair_feasible?(c, e)
  d = H - c
  tail = 62_356 + c
  rows = row_bound(c)
  pair_budget = c2(e) - shared_pair_floor(e, rows)
  e * tail <= direction_pair_capacity(d, TAIL_UNIVERSE, pair_budget, rows)
end

def maximum_feasible(c, method)
  rows = row_bound(c)
  predicate = method == :second ? method(:second_moment_feasible?) : method(:direction_pair_feasible?)
  graph_ceiling(rows).downto(0).find { |e| predicate.call(c, e) }
end

# Exact row/direction thresholds.
check(row_bound(0) == 13, "c=0 row bound")
check(row_bound(296) == 13, "c=296 row bound")
check(row_bound(297) == 14, "c=297 row jump")
check(row_bound(617) == 14, "c=617 row bound")
check(row_bound(618) == 15, "c=618 row jump")
check(row_bound(832) == 15, "c=832 row bound")

second = (0..832).map { |c| maximum_feasible(c, :second) }
direction = (0..832).map { |c| maximum_feasible(c, :direction) }

check(second[0] == 169, "second c=0")
check(second[297] == 196, "second c=297")
check(second[557] == 156, "second c=557")
check(second[558] == 155, "second c=558")
check(second[832] == 101, "second c=832")
check(second[558..832].max == 155, "second uniform high-core cap")

check(direction[0] == 169, "direction c=0")
check(direction[297] == 196, "direction c=297")
check(direction[553] == 156, "direction c=553")
check(direction[554] == 155, "direction c=554")
check(direction[557] == 153, "direction c=557")
check(direction[558] == 152, "direction c=558")
check(direction[618] == 148, "direction c=618")
check(direction[832] == 101, "direction c=832")
check(direction[554..832].max == 155, "direction uniform high-core cap")
check(direction[0..553].max == 196, "unpaid low-core maximum")

def boundary_row(c, e)
  d = H - c
  tail = 62_356 + c
  rows = row_bound(c)
  shared = shared_pair_floor(e, rows)
  budget = c2(e) - shared
  collision_floor = integral_collision_floor(e * tail, TAIL_UNIVERSE)
  collision_cap = d * budget
  incidence_need = e * tail
  incidence_cap = direction_pair_capacity(d, TAIL_UNIVERSE, budget, rows)
  [d, tail, rows, shared, budget, collision_floor, collision_cap,
   incidence_need, incidence_cap]
end

c553 = boundary_row(553, 156)
c554 = boundary_row(554, 156)
c557 = boundary_row(557, 156)
c558 = boundary_row(558, 156)
check(c553[-1] - c553[-2] == 778, "c553 direction margin")
check(c554[-1] - c554[-2] == -728, "c554 direction margin")
check(c557[6] - c557[5] == 2_389, "c557 second margin")
check(c558[6] - c558[5] == -9_677, "c558 second margin")

# Explicit graph-degree witnesses for the relaxed e=156 boundary rows.
# c=0: K_13,13 minus one perfect matching is 12-regular.
check(13 * 12 == 156, "c0 graph witness")
check(2 * 13 * c2(12) == shared_pair_floor(156, 13), "c0 shared pairs")
# R=14: shifts 0..10 give an 11-regular circulant; add two absent
# edges in distinct rows and columns to obtain two degrees 12 and twelve 11
# on both sides.
check(2 * c2(12) + 12 * c2(11) == balanced_pair_sum(156, 14),
      "R14 graph witness")

puts "RANK16_FIXED_PAIR_ACTIVE_PENCIL_GRID_TAIL_CUT: PASS"
puts "tail_universe=#{TAIL_UNIVERSE} cores=0..832"
puts "row_bound_jumps=c0:13,c297:14,c618:15"
puts "second_moment=c0:#{second[0]},c297:#{second[297]},c557:#{second[557]},c558:#{second[558]},c832:#{second[832]}"
puts "second_moment_uniform_c558_832=#{second[558..832].max}"
puts "direction_pair=c0:#{direction[0]},c297:#{direction[297]},c553:#{direction[553]},c554:#{direction[554]},c557:#{direction[557]},c558:#{direction[558]},c618:#{direction[618]},c832:#{direction[832]}"
puts "direction_pair_uniform_c554_832=#{direction[554..832].max}"
puts "unpaid_c0_553_max=#{direction[0..553].max}"
puts "c553_e156_direction_need_cap_margin=#{c553[-2]},#{c553[-1]},#{c553[-1] - c553[-2]}"
puts "c554_e156_direction_need_cap_margin=#{c554[-2]},#{c554[-1]},#{c554[-1] - c554[-2]}"
puts "c557_e156_second_floor_cap_margin=#{c557[5]},#{c557[6]},#{c557[6] - c557[5]}"
puts "c558_e156_second_floor_cap_margin=#{c558[5]},#{c558[6]},#{c558[6] - c558[5]}"
