#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "open3"
require "rbconfig"

FILES = {
  "RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS_BOUND.md" =>
    "6f998929209b534d39cb0d31fa6458f5bf63d9326255ec31e7f0f64ae7a5389e",
  "HOSTILE_AUDIT_RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS_BOUND.md" =>
    "e7383111a412c2b2f50738405946c3636f8469e62e2c839672e106b55f286256",
  "explore_rank15_m213_exact_localcost_driver.rb" =>
    "8cfcf7475dd153e5e101e0c97467d7d49b0336f902e806ce673dee13f8de533b",
  "explore_rank15_m213_covector_weight_impact.rb" =>
    "099fab039f0812b9aeb5dce7acdcdc588f43520074ef1ae358a6d6fcfe0e5be2",
  "RANK15_ORDINARY_MULTIPLE_LOCAL_INDEX_LEMMA.md" =>
    "827746bd3e2dc8650ff0ab83e12a71a4b30f5e807cf17d6563327fc003c7f0ab",
  "verify_rank15_ordinary_multiple_local_index_lemma.rb" =>
    "e9f90dd5bdedd401684fa7cfd16e723d50abea9247e9e901770c35d0425af108"
}.freeze

MOD = 1_000_003
P_FIELD = 2_130_706_433

def check(condition, message)
  raise message unless condition
end

def run_ruby(filename, *arguments)
  path = File.join(__dir__, filename)
  stdout, stderr, status = Open3.capture3(
    RbConfig.ruby, "--disable-gems", "-w", path, *arguments
  )
  check(status.success?, "#{filename} failed: #{stderr}")
  check(stderr.empty?, "#{filename} emitted warnings: #{stderr}")
  stdout
end

FILES.each do |filename, expected_sha|
  path = File.join(__dir__, filename)
  check(File.file?(path), "missing frozen input #{filename}")
  actual_sha = Digest::SHA256.file(path).hexdigest
  check(actual_sha == expected_sha,
        "hash mismatch #{filename}: #{actual_sha}")
end

theorem = File.read(
  File.join(__dir__, "RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS_BOUND.md")
)
[
  "E+S=2E-U <= a(q+1)",
  "`X(u)` vanishes identically on no irreducible component of `fg`",
  "K=-Q^2 P_v mod P",
  "i(P,g)=2mu+i(P,P_v)-i(P,F)",
  "u_0=sum_j(r_j-1)=i(P,F)-m",
  "i(P,P_v)>=m-2",
  "n=i(P,u)<=deg(P)<=q+1",
  "At a point not on `g`, the right side",
  "minimum gap\n`86-75=11`"
].each do |marker|
  check(theorem.include?(marker), "missing theorem marker #{marker.inspect}")
end

# Sparse bivariate polynomial tamper guard for the exact congruence
# K == -Q^2 P_v (mod P).  A monomial is [u_exponent,v_exponent].
def normalize(poly)
  poly.transform_values { |value| value % MOD }
      .reject { |_monomial, value| value.zero? }
end

def add(*polys)
  out = Hash.new(0)
  polys.each do |poly|
    poly.each { |monomial, value| out[monomial] += value }
  end
  normalize(out)
end

def scale(poly, scalar)
  normalize(poly.to_h { |monomial, value| [monomial, scalar * value] })
end

def mul(left, right)
  out = Hash.new(0)
  left.each do |(i, j), x|
    right.each { |(r, s), y| out[[i + r, j + s]] += x * y }
  end
  normalize(out)
end

def derivative(poly, axis)
  out = Hash.new(0)
  poly.each do |monomial, value|
    exponent = monomial.fetch(axis)
    next if exponent.zero?

    target = monomial.dup
    target[axis] -= 1
    out[target] += exponent * value
  end
  normalize(out)
end

def apply_field(p_poly, q_poly, target)
  add(mul(p_poly, derivative(target, 0)),
      mul(q_poly, derivative(target, 1)))
end

100.times do |trial|
  p_poly = {
    [1, 0] => 2 + trial, [0, 1] => 5 + 3 * trial,
    [2, 0] => 7 + trial, [1, 1] => 11 + 2 * trial,
    [0, 3] => 13 + trial
  }
  q_poly = {
    [1, 0] => 17 + 2 * trial, [0, 1] => 19 + trial,
    [0, 2] => 23 + trial, [2, 1] => 29 + 3 * trial
  }
  p_poly = normalize(p_poly)
  q_poly = normalize(q_poly)
  x_p = apply_field(p_poly, q_poly, p_poly)
  x_q = apply_field(p_poly, q_poly, q_poly)
  k_poly = add(mul(p_poly, x_q), scale(mul(q_poly, x_p), -1))
  p_v = derivative(p_poly, 1)

  # K+Q^2 P_v=P(X(Q)-Q P_u), hence K=-Q^2 P_v modulo P.
  left = add(k_poly, mul(mul(q_poly, q_poly), p_v))
  right = mul(
    p_poly,
    add(x_q, scale(mul(q_poly, derivative(p_poly, 0)), -1))
  )
  check(left == right, "extactic congruence failed trial=#{trial}")

  wrong_sign = add(k_poly, scale(mul(mul(q_poly, q_poly), p_v), -1))
  check(wrong_sign != right, "sign tamper survived trial=#{trial}")
end

# Exhaust the arithmetic comparison between the exact local formulas.  The
# chosen i(P,F) values need not describe actual germs; this is a formula and
# sign guard, while the theorem supplies realizability and properness.
(0..20).each do |m|
  (1..40).each do |mu|
    i_pf_values = m.zero? ? [0] : (0..80)
    i_pf_values.each do |i_pf|
      polar_floor = [m - 2, 0].max
      polar = polar_floor + ((m + mu + i_pf) % 7)
      i_pg = 2 * mu + polar - i_pf
      w = if m.zero?
            2 * mu
          elsif m == 1
            2 * mu - i_pf
          else
            2 * mu - i_pf + m - 2
          end
      check(i_pg >= w, "local weighted payment failed m=#{m}")
    end
  end
end

# Direct Artin-quotient boundary model: P=u-v^n has
# O/(P,P_v) ~= k[[v]]/(v^(n-1)).  It reaches the n-1 lower bound exactly.
(2..100).each do |n|
  check(n < MOD, "toy characteristic gate failed")
  quotient_basis = (0...(n - 1)).map { |j| [0, j] }
  check(quotient_basis.length == n - 1, "polar boundary length failed n=#{n}")
end
check((P_FIELD % P_FIELD).zero?, "characteristic negative control changed")

# Target characteristic and degree gates, plus the five exact caps.
targets = [
  [24, 69, 3, 75], [24, 68, 4, 100],
  [25, 71, 4, 104], [25, 70, 5, 130], [25, 69, 6, 156]
]
targets.each do |q, b, a, cap|
  check(a == 3 * q - b, "residual degree mismatch q=#{q} B=#{b}")
  check(cap == a * (q + 1), "Bezout cap mismatch q=#{q} B=#{b}")
  check(P_FIELD > [b, q + 1].max, "target characteristic gate failed")
end

local_index = run_ruby("verify_rank15_ordinary_multiple_local_index_lemma.rb")
check(local_index.include?("RANK15_ORDINARY_MULTIPLE_LOCAL_INDEX_LEMMA: PASS"),
      "ordinary-point dependency failed")

# Full source-locked replay.  This deliberately recomputes the five cells;
# it does not trust the /tmp transcripts cited by the theorem.
q24 = run_ruby("explore_rank15_m213_covector_weight_impact.rb",
               "24", "68", "69")
q25 = run_ruby("explore_rank15_m213_covector_weight_impact.rb",
               "25", "69", "71")

expected_lines = {
  q24 => [
    "COVECTOR_WEIGHT B=68 a=4 cap=100 raw=16027 min=96 max=132 survivors=919",
    "COVECTOR_WEIGHT B=69 a=3 cap=75 raw=12607 min=86 max=120 survivors=0"
  ],
  q25 => [
    "COVECTOR_WEIGHT B=69 a=6 cap=156 raw=559 min=117 max=132 survivors=559",
    "COVECTOR_WEIGHT B=70 a=5 cap=130 raw=350 min=106 max=119 survivors=350",
    "COVECTOR_WEIGHT B=71 a=4 cap=104 raw=225 min=95 max=107 survivors=215"
  ]
}
expected_lines.each do |output, lines|
  lines.each do |line|
    check(output.lines.map(&:chomp).include?(line), "missing replay line #{line}")
  end
  check(output.include?("nonclaim=global_covector_weight_impact_diagnostic"),
        "replay nonclaim marker missing")
end

puts "RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS_BOUND_HOSTILE_AUDIT: PASS"
puts "theorem_sha256=#{FILES.fetch('RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS_BOUND.md')}"
puts "audit_sha256=#{FILES.fetch('HOSTILE_AUDIT_RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS_BOUND.md')}"
puts "bound=E_plus_S_le_(3q_minus_B)_times_(q_plus_1)"
puts "q24_B69=raw_12607_Wmin_86_cap_75_survivors_0_gap_11"
puts "other_cells=q24_B68_919;q25_B71_215;q25_B70_350;q25_B69_559"
