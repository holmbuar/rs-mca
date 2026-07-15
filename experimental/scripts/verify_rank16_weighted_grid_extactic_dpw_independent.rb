#!/usr/bin/env ruby
# frozen_string_literal: true

# Independent standard-library replay of the finite DPW/extactic profile scan.
P_FIELD = 2_130_706_433
N = 1_053_693
A = 72_588
H = 5_116
U = 913_633
V = 156


def fail_check(msg)
  raise "CHECK FAILED: #{msg}"
end

def c2(x)
  x < 2 ? 0 : x * (x - 1) / 2
end

def rmax(c)
  (A - c) / (H - c) - 1
end

def dpw(deg, rho)
  ans = (deg - 1) * (deg - rho - 1) + rho * rho
  alpha = 2 * rho + 1 - deg
  ans -= c2(alpha + 1) if alpha.positive?
  ans
end

def convex_extra(inc)
  q, rem = inc.divmod(V)
  (V - rem) * c2(q + 1) + rem * c2(q + 2)
end

def inverse_extra(budget, e)
  return -1 if budget.negative?

  lo = 0
  hi = V * e
  while lo < hi
    mid = (lo + hi + 1) / 2
    if convex_extra(mid) <= budget
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end

def one_color(e, r, t)
  deg = e + r + t + 1
  fixed = c2(deg) + c2(r) + c2(t)
  ordinary_line_cap = [r, t].min * e
  best = 0
  best_info = nil
  (0...deg).each do |rho|
    bound = inverse_extra(dpw(deg, rho) - fixed, e)
    next if bound.negative?

    bound = [bound, ordinary_line_cap].min
    branch = :dpw
    if 3 * rho < deg
      next if rho < r + t - 1

      pencil = e + 155 + ([r, t].min - 1) * (rho - r - t + 1)
      bound = [bound, pencil].min
      branch = :pencil
    end
    if bound > best
      best = bound
      best_info = [e, rho, branch, deg]
    end
  end
  [best, best_info]
end

def all_grid_pairs(limit)
  out = []
  (1..limit).each do |r|
    (1..limit).each do |t|
      next if r * t < V
      next if 14 * r < V || 14 * t < V

      out << [r, t]
    end
  end
  out
end

max_e = (U + (H - 553) - 1) / (H - 553)
cache = {}
all_grid_pairs(14).each do |r, t|
  running = 0
  info = nil
  (0..max_e).each do |e|
    value, local_info = one_color(e, r, t)
    if value > running
      running = value
      info = local_info
    end
    cache[[e, r, t]] = [running, info]
  end
end

minimum = nil
c553 = nil
(0..553).each do |c|
  d = H - c
  b = 62_356 + c
  emax = (U + d - 1) / d
  best = -1
  profile = nil
  all_grid_pairs(rmax(c)).each do |r, t|
    cap, info = cache[[emax, r, t]]
    if cap > best
      best = cap
      profile = [r, t, info]
    end
  end
  need = V * b
  total = d * best
  margin = need - total
  fail_check("c=#{c} margin") unless margin.positive?
  row = [c, d, b, rmax(c), emax, best, profile, need, total, margin]
  minimum = row if minimum.nil? || margin < minimum[-1]
  c553 = row if c == 553
end

fail_check('global minimum') unless minimum == [
  12, 5104, 62_368, 13, 180, 1816,
  [13, 13, [180, 69, :dpw, 207]],
  9_729_408, 9_268_864, 460_544
]
fail_check('c553') unless c553 == [
  553, 4563, 62_909, 14, 201, 2029,
  [14, 14, [201, 77, :dpw, 230]],
  9_813_804, 9_258_327, 555_477
]
fail_check('c12 convex boundary') unless convex_extra(1816) == 11_496 && convex_extra(1817) == 11_508
fail_check('c553 convex boundary') unless convex_extra(2029) == 14_210 && convex_extra(2030) == 14_224

puts 'RANK16_WEIGHTED_GRID_EXTACTIC_DPW_INDEPENDENT: PASS'
puts "field_p=#{P_FIELD} max_color_lines=#{max_e}"
puts "uniform_min=#{minimum.inspect}"
puts "c553=#{c553.inspect}"
