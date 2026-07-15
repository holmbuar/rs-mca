#!/usr/bin/env ruby
# frozen_string_literal: true

# Exhaustive small cyclic audit of the residual-nesting argument.  All
# polynomial coefficients are in increasing degree.

def check(condition, message)
  raise "FAIL: #{message}" unless condition
end

def trim(poly, prime)
  out = poly.map { |value| value % prime }
  out.pop while out.length > 1 && out[-1].zero?
  out
end

def poly_mul(left, right, prime)
  out = Array.new(left.length + right.length - 1, 0)
  left.each_with_index do |x, i|
    right.each_with_index do |y, j|
      out[i + j] = (out[i + j] + x * y) % prime
    end
  end
  trim(out, prime)
end

def poly_divmod(numerator, denominator, prime)
  num = trim(numerator, prime)
  den = trim(denominator, prime)
  raise 'division by zero' if den == [0]

  quotient = Array.new([num.length - den.length + 1, 0].max, 0)
  inverse = den[-1].pow(prime - 2, prime)
  while num != [0] && num.length >= den.length
    shift = num.length - den.length
    coefficient = num[-1] * inverse % prime
    quotient[shift] = coefficient
    den.each_with_index do |value, i|
      num[i + shift] = (num[i + shift] - coefficient * value) % prime
    end
    num = trim(num, prime)
  end
  [trim(quotient, prime), trim(num, prime)]
end

def poly_scale(poly, scalar, prime)
  trim(poly.map { |value| value * scalar % prime }, prime)
end

def poly_gcd(left, right, prime)
  a = trim(left, prime)
  b = trim(right, prime)
  until b == [0]
    _quotient, remainder = poly_divmod(a, b, prime)
    a = b
    b = remainder
  end
  poly_scale(a, a[-1].pow(prime - 2, prime), prime)
end

def poly_eval(poly, x, prime)
  poly.reverse.reduce(0) { |value, coefficient| (value * x + coefficient) % prime }
end

def locator(roots, prime)
  roots.reduce([1]) do |poly, root|
    poly_mul(poly, [-root % prime, 1], prime)
  end
end

def coefficient_at_lag(poly, lag)
  index = poly.length - 1 - lag
  index.negative? ? 0 : poly[index]
end

field_counts = {}
profile_counts = Hash.new(0)
nesting_pairs = 0
boundary_profiles = 0

[7, 11, 13].each do |prime|
  group = (1...prime).to_a
  n = prime - 1
  extremizers = 0

  (1..[4, n - 1].min).each do |degree|
    value_count = (n + degree - 1) / degree
    gap = n - (value_count - 1) * degree
    next unless gap.positive?

    # Monic normalization loses no residual/nesting behavior: affine scaling
    # of f only relabels the values and leaves every normalized residual.
    (prime**degree).times do |code|
      work = code
      polynomial = Array.new(degree) do
        digit = work % prime
        work /= prime
        digit
      end + [1]

      fibers = group.group_by { |x| poly_eval(polynomial, x, prime) }
      next unless fibers.length == value_count

      extremizers += 1
      residuals = {}
      deltas = {}

      fibers.each do |value, roots|
        q_locator = locator(roots, prime)
        shifted = polynomial.dup
        shifted[0] = (shifted[0] - value) % prime
        residual, remainder = poly_divmod(shifted, q_locator, prime)
        check(remainder == [0],
              "fiber locator division p=#{prime},D=#{degree},c=#{value}")

        delta = degree - roots.length
        check(residual.length - 1 == delta,
              "residual degree p=#{prime},D=#{degree},c=#{value}")

        (1...gap).each do |moment|
          power_sum = roots.sum { |x| x.pow(moment, prime) } % prime
          check(power_sum.zero?,
                "moment gap p=#{prime},D=#{degree},c=#{value},j=#{moment}")
        end

        (0...[gap, degree + 1].min).each do |lag|
          expected = lag <= delta ? coefficient_at_lag(residual, lag) : 0
          actual = coefficient_at_lag(polynomial, lag)
          check(actual == expected,
                "leading string p=#{prime},D=#{degree},c=#{value},lag=#{lag}")
        end

        residuals[value] = residual
        deltas[value] = delta
      end

      values = fibers.keys
      values.combination(2) do |left, right|
        check(poly_gcd(residuals.fetch(left), residuals.fetch(right), prime) == [1],
              "residual gcd p=#{prime},D=#{degree},values=#{left}/#{right}")
      end

      values.permutation(2) do |small, large|
        delta_small = deltas.fetch(small)
        delta_large = deltas.fetch(large)
        next unless delta_small <= delta_large && delta_large < gap

        shift = Array.new(delta_large - delta_small, 0) + residuals.fetch(small)
        check(trim(shift, prime) == residuals.fetch(large),
              "nesting p=#{prime},D=#{degree},values=#{small}/#{large}")
        nesting_pairs += 1
      end

      profile = deltas.values.sort
      profile_counts[[prime, degree, value_count, gap, profile]] += 1
      boundary_profiles += 1 if profile.any? { |delta| delta == gap }
    end
  end
  field_counts[prime] = extremizers
end

check(field_counts == { 7 => 42, 11 => 22, 13 => 52 },
      'exhaustive extremizer counts')
check(profile_counts[[7, 4, 2, 2, [0, 2]]] == 21,
      'strict-boundary regression profile')
check(boundary_profiles == 21, 'boundary profile count')
check(nesting_pairs.positive?, 'no nesting pairs audited')

puts 'HOSTILE_AUDIT_DUAL32_TWENTY_COMPLETE_FIBERS_LACUNARY_REDUCTION: PASS'
puts "extremizers=#{field_counts.map { |prime, count| "F#{prime}:#{count}" }.join(',')}"
puts "nesting_pairs_checked=#{nesting_pairs}"
puts "strict_boundary_profile=F7,D4,s2,G2,deltas0/2,count#{boundary_profiles}"
puts 'residual_gcd_failures=0'
puts 'residual_nesting_failures=0'
puts 'RESULT: PASS'
