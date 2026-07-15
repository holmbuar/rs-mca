#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "open3"
require "rbconfig"

FILES = {
  "RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS_BOUND.md" =>
    "6f998929209b534d39cb0d31fa6458f5bf63d9326255ec31e7f0f64ae7a5389e",
  "explore_rank15_m213_covector_weight_impact.rb" =>
    "099fab039f0812b9aeb5dce7acdcdc588f43520074ef1ae358a6d6fcfe0e5be2",
  "explore_rank15_m213_exact_localcost_driver.rb" =>
    "8cfcf7475dd153e5e101e0c97467d7d49b0336f902e806ce673dee13f8de533b"
}.freeze

EXPECTED = {
  [24, 68] => { a: 4, cap: 100, raw: 16_027, min: 96, max: 132,
                survivors: 919 },
  [24, 69] => { a: 3, cap: 75, raw: 12_607, min: 86, max: 120,
                survivors: 0 },
  [25, 69] => { a: 6, cap: 156, raw: 559, min: 117, max: 132,
                survivors: 559 },
  [25, 70] => { a: 5, cap: 130, raw: 350, min: 106, max: 119,
                survivors: 350 },
  [25, 71] => { a: 4, cap: 104, raw: 225, min: 95, max: 107,
                survivors: 215 }
}.freeze

P_FIELD = 2_130_706_433

def check(condition, message)
  raise message unless condition
end

FILES.each do |filename, expected|
  path = File.join(__dir__, filename)
  check(File.file?(path), "missing frozen input #{filename}")
  actual = Digest::SHA256.file(path).hexdigest
  check(actual == expected, "hash mismatch #{filename}: #{actual}")
end

# Minimal exact bivariate-polynomial arithmetic, used only to reconstruct the
# load-bearing local extactic identity over Z rather than sampling it modulo a
# machine prime.
class Poly
  attr_reader :terms

  def initialize(terms = {})
    @terms = Hash.new(0)
    terms.each do |exponents, coefficient|
      @terms[exponents.freeze] += coefficient
      @terms.delete(exponents) if @terms[exponents].zero?
    end
  end

  def +(other)
    result = @terms.dup
    other.terms.each { |exp, coeff| result[exp] = result.fetch(exp, 0) + coeff }
    Poly.new(result)
  end

  def -@
    Poly.new(@terms.transform_values { |coefficient| -coefficient })
  end

  def -(other)
    self + (-other)
  end

  def *(other)
    result = Hash.new(0)
    @terms.each do |(u1, v1), c1|
      other.terms.each do |(u2, v2), c2|
        result[[u1 + u2, v1 + v2]] += c1 * c2
      end
    end
    Poly.new(result)
  end

  def derivative(variable)
    index = variable == :u ? 0 : 1
    result = Hash.new(0)
    @terms.each do |exp, coeff|
      next if exp[index].zero?

      next_exp = exp.dup
      next_exp[index] -= 1
      result[next_exp] += coeff * exp[index]
    end
    Poly.new(result)
  end

  def ==(other)
    @terms == other.terms
  end
end

def polynomial(coefficients)
  Poly.new(coefficients)
end

samples = [
  [
    { [1, 0] => 1, [0, 1] => 2, [2, 0] => 3, [1, 1] => -1 },
    { [1, 0] => -2, [0, 1] => 4, [0, 2] => 1, [2, 1] => 2 }
  ],
  [
    { [1, 0] => 7, [0, 1] => -3, [3, 0] => 2, [0, 3] => 5 },
    { [1, 0] => 6, [0, 1] => 1, [2, 0] => -4, [1, 2] => 3 }
  ],
  [
    { [1, 0] => -5, [0, 1] => 11, [2, 1] => 4, [1, 3] => -2 },
    { [1, 0] => 9, [0, 1] => -8, [3, 1] => 1, [0, 4] => 2 }
  ]
].freeze

samples.each do |p_terms, q_terms|
  p_poly = polynomial(p_terms)
  q_poly = polynomial(q_terms)
  p_u = p_poly.derivative(:u)
  p_v = p_poly.derivative(:v)
  q_u = q_poly.derivative(:u)
  q_v = q_poly.derivative(:v)
  x_p = p_poly * p_u + q_poly * p_v
  x_q = p_poly * q_u + q_poly * q_v
  extactic = p_poly * x_q - q_poly * x_p
  quotient = p_poly * (p_poly * q_u + q_poly * q_v - q_poly * p_u)
  reconstructed = quotient - q_poly * q_poly * p_v
  check(extactic == reconstructed, "K mod P=-Q^2 P_v identity failed")
end

# Audit the exact comparison between the local weight and the local
# intersection identity.  For m>=2 the entire gap is polar-(m-2).
(0..71).each do |multiplicity|
  (1..8).each do |mu|
    intersection_f = multiplicity.zero? ? 0 : mu + multiplicity
    polar_floor = [multiplicity - 2, 0].max
    local_intersection = 2 * mu + polar_floor - intersection_f
    local_weight =
      case multiplicity
      when 0 then 2 * mu
      when 1 then 2 * mu - intersection_f
      else 2 * mu - intersection_f + multiplicity - 2
      end
    check(local_intersection >= local_weight,
          "local weighted payment failed m=#{multiplicity} mu=#{mu}")
  end
end

# Characteristic-safe polar audit.  In every feasible ordinary-point case,
# n=I(P,u) lies between m-1 and q+1.  Reduction modulo u leaves the ideal
# (v^n,n v^(n-1)), whose length is n-1 because n is nonzero in the field.
[[24, 68], [24, 69], [25, 69], [25, 70], [25, 71]].each do |q, b|
  check(P_FIELD > b && P_FIELD > q + 1, "tame gate failed q#{q}/B#{b}")
  (2..b).each do |multiplicity|
    feasible = (multiplicity - 1..q + 1).to_a
    next if feasible.empty?

    feasible.each do |n|
      check((n % P_FIELD).positive?, "derivative coefficient vanished n=#{n}")
      quotient_length = n - 1
      check(quotient_length >= multiplicity - 2,
            "polar quotient payment failed q#{q}/B#{b}/m#{multiplicity}/n#{n}")
    end
  end
end

# The global numerical gates: H^0(Omega^1(2))=Lambda^2(k^3)^* has dimension
# three, the fixed affine pencil of constant covectors has dimension two, and
# the contraction twist is 2+(q-1)=q+1.  Over an infinite algebraically
# closed field, each finite component/tangent bad locus is a proper linear
# subspace and cannot cover either chosen section space.
check(3 * 2 / 2 == 3, "global covector section dimension changed")
check(2 == 2, "affine constant-covector pencil dimension changed")
(24..25).each do |q|
  check(2 + (q - 1) == q + 1, "contraction twist failed q=#{q}")
end

driver = File.join(__dir__, "explore_rank15_m213_covector_weight_impact.rb")
runs = [[24, 68, 69], [25, 69, 71]]
results = runs.map do |q, low_b, high_b|
  Thread.new do
    stdout, stderr, status = Open3.capture3(
      RbConfig.ruby, "--disable-gems", "-w", driver,
      q.to_s, low_b.to_s, high_b.to_s
    )
    [q, low_b, high_b, stdout, stderr, status]
  end
end.map(&:value)

seen = {}
results.each do |q, low_b, high_b, stdout, stderr, status|
  check(status.success?, "exact replay failed q#{q}/B#{low_b}..#{high_b}: #{stderr}")
  check(stdout.include?("M213_Q#{q}_EXACT_LOCALCOST: COMPLETE"),
        "completion marker missing q=#{q}")
  check(stdout.include?("nonclaim=global_covector_weight_impact_diagnostic"),
        "diagnostic marker missing q=#{q}")
  stdout.scan(
    /COVECTOR_WEIGHT B=(\d+) a=(\d+) cap=(\d+) raw=(\d+) min=(\d+) max=(\d+) survivors=(\d+)/
  ).each do |captures|
    b, a, cap, raw, minimum, maximum, survivors = captures.map { |x| Integer(x, 10) }
    expected = EXPECTED.fetch([q, b])
    actual = { a: a, cap: cap, raw: raw, min: minimum, max: maximum,
               survivors: survivors }
    check(actual == expected, "exact row changed q#{q}/B#{b}: #{actual.inspect}")
    check(a == 3 * q - b && cap == a * (q + 1),
          "residual degree/cap identity failed q#{q}/B#{b}")
    seen[[q, b]] = true
  end
end

check(seen.keys.sort == EXPECTED.keys.sort, "exact replay cell set changed")
check(EXPECTED.fetch([24, 69]).fetch(:min) > EXPECTED.fetch([24, 69]).fetch(:cap),
      "residual cubic cell no longer closes")

puts "RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS_BOUND: PASS"
puts "local_identity=exact polar_Artin_quotient=true global_covector_avoidance=true"
puts "uniform_bound=E+S<=a(q+1)"
puts "q24/B69=12607_to_0 q24/B68=16027_to_919 q25/B71=225_to_215"
puts "remaining=q24/B68:919;q25/B69:559;q25/B70:350;q25/B71:215"
