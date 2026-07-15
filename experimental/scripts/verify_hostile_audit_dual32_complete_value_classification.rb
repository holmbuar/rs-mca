#!/usr/bin/env ruby
# frozen_string_literal: true

def check(condition, message)
  raise "FAIL: #{message}" unless condition
end

P_DEPLOYED = 2_130_706_433
N_DEPLOYED = 2_097_152
Q_DEPLOYED = 65_536
D_MAX = 67_471

minimum_contact_margin = nil
minimum_differential_margin = nil
minimum_final_margin = nil

(Q_DEPLOYED..D_MAX).each do |degree|
  delta = 32 * degree - N_DEPLOYED
  gap = N_DEPLOYED - 31 * degree

  check(N_DEPLOYED + delta == 32 * degree,
        "reverse weight identity D=#{degree}")
  check(N_DEPLOYED > 2 * degree,
        "contact precedes z^n D=#{degree}")
  check(delta < degree, "differential degree gate D=#{degree}")
  check(degree - delta == gap, "reverse support gap D=#{degree}")
  check(32 * gap > delta, "final degree contradiction D=#{degree}")
  check(P_DEPLOYED > 32 * degree, "characteristic gate D=#{degree}")

  contact_margin = N_DEPLOYED - 2 * degree
  differential_margin = (2 * degree - 1) - (degree + delta - 1)
  final_margin = 32 * gap - delta
  minimum_contact_margin = contact_margin if minimum_contact_margin.nil? ||
                                               contact_margin < minimum_contact_margin
  minimum_differential_margin = differential_margin if minimum_differential_margin.nil? ||
                                                       differential_margin < minimum_differential_margin
  minimum_final_margin = final_margin if minimum_final_margin.nil? ||
                                         final_margin < minimum_final_margin
end

check(minimum_contact_margin == 1_962_210, 'minimum n-2D margin')
check(minimum_differential_margin == 5_551, 'minimum D-Delta margin')
check(minimum_final_margin == 115_712, 'minimum 32G-Delta margin')

# Centering sign in a generic degree-m value polynomial: translating the
# phase by u requires P_c(Y)=P(Y-u), whose next coefficient is p1-mu.
prime_center = 101
m_center = 5
nodes = [3, 7, 12, 24, 51]

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

def poly_eval(poly, x, prime)
  poly.reverse.reduce(0) { |value, coefficient| (value * x + coefficient) % prime }
end

def value_locator(nodes, prime)
  nodes.reduce([1]) do |poly, node|
    poly_mul(poly, [-node % prime, 1], prime)
  end
end

p_value = value_locator(nodes, prime_center)
p1 = p_value[-2]
u = p1 * m_center.pow(prime_center - 2, prime_center) % prime_center
centered_nodes = nodes.map { |node| (node + u) % prime_center }
p_centered = value_locator(centered_nodes, prime_center)
check(p_centered[-2].zero?, 'centered Y^(m-1) coefficient')
(0...prime_center).each do |y|
  check(poly_eval(p_centered, (y + u) % prime_center, prime_center) ==
        poly_eval(p_value, y, prime_center), 'P_c(f+u)=P(f) sign')
end

def prime_factors(number)
  factors = []
  divisor = 2
  value = number
  while divisor * divisor <= value
    if (value % divisor).zero?
      factors << divisor
      value /= divisor while (value % divisor).zero?
    end
    divisor += 1
  end
  factors << value if value > 1
  factors
end

def primitive_root(prime)
  factors = prime_factors(prime - 1)
  (2...prime).find do |candidate|
    factors.all? { |factor| candidate.pow((prime - 1) / factor, prime) != 1 }
  end
end

def cyclic_group(prime, order)
  check(((prime - 1) % order).zero?, "group order #{order} not in F_#{prime}")
  generator = primitive_root(prime).pow((prime - 1) / order, prime)
  roots = (0...order).map { |index| generator.pow(index, prime) }
  check(roots.uniq.length == order, "cyclic group order #{order}")
  roots
end

# Exhaust every monic lacunary polynomial X^D+A in the listed rows.
cases = [
  [41, 8, 4, 2],
  [41, 8, 3, 3],
  [41, 10, 3, 4],
  [41, 20, 3, 7]
]
case_counts = {}

cases.each do |prime, n, value_count, degree|
  delta = value_count * degree - n
  gap = n - (value_count - 1) * degree
  check(delta >= 0 && delta < degree, 'small Delta range')
  check(prime > value_count * degree, 'small characteristic gate')
  check(n > 2 * degree, 'small contact gate')
  check(value_count * gap > delta, 'small final degree gate')

  group = cyclic_group(prime, n)
  hits = 0
  (prime**(delta + 1)).times do |code|
    work = code
    low = Array.new(delta + 1) do
      digit = work % prime
      work /= prime
      digit
    end
    polynomial = low + Array.new(degree - delta - 1, 0) + [1]
    values = group.map { |x| poly_eval(polynomial, x, prime) }.uniq
    next unless values.length == value_count

    hits += 1
    p1_small = -values.sum % prime
    shift = p1_small * value_count.pow(prime - 2, prime) % prime
    centered = polynomial.dup
    centered[0] = (centered[0] + shift) % prime
    check(centered[1...degree].all?(&:zero?),
          "nonmonomial small survivor p=#{prime},n=#{n},m=#{value_count},D=#{degree}")
    check(n / n.gcd(degree) == value_count,
          'small centered monomial image size')
  end
  case_counts[[prime, n, value_count, degree]] = hits
end

check(case_counts == {
        [41, 8, 4, 2] => 41,
        [41, 8, 3, 3] => 0,
        [41, 10, 3, 4] => 0,
        [41, 20, 3, 7] => 0
      }, 'small cyclic census')

# Guardrail outside the hypotheses: X^4+X^2 is two-valued on F_7^*, but
# n>2D and char>mD both fail, so it is not a counterexample to the theorem.
bad_prime = 7
bad_poly = [0, 0, 1, 0, 1]
bad_values = (1...bad_prime).map { |x| poly_eval(bad_poly, x, bad_prime) }.uniq.sort
check(bad_values == [2, 6], 'small excluded counterexample values')
check(!(bad_prime > 2 * 4), 'excluded characteristic gate')
check(!(6 > 2 * 4), 'excluded contact gate')

puts 'HOSTILE_AUDIT_DUAL32_COMPLETE_VALUE_CLASSIFICATION: PASS'
puts "source_sha256=5264d6d7a067513b7aa6124ac0a4e6915c9dd28a552194c8b8987ea920d3fd13"
puts "minimum_n_minus_2D=#{minimum_contact_margin}"
puts "minimum_D_minus_Delta=#{minimum_differential_margin}"
puts "minimum_32G_minus_Delta=#{minimum_final_margin}"
puts 'centering=f->f+p1/32,P(Y)->P(Y-p1/32)'
puts "small_census=#{case_counts.map { |key, count| "#{key.join('/')}:#{count}" }.join(',')}"
puts 'excluded_guardrail=F7:X4+X2,two_values,fails_char_and_contact'
puts 'RESULT: PASS'
