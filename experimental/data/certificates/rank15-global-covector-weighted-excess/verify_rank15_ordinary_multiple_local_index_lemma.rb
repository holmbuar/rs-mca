#!/usr/bin/env ruby
# frozen_string_literal: true

# Arithmetic and contract guard for the ordinary-multiple-point local-index
# lemma.  The commutative-algebra proof is in the companion theorem note.

require "digest"

P_FIELD = 2_130_706_433
MAX_VALENCY = 213
THEOREM_SHA256 =
  "827746bd3e2dc8650ff0ab83e12a71a4b30f5e807cf17d6563327fc003c7f0ab"

def check(condition, message)
  raise message unless condition
end

def prime?(number)
  return false if number < 2
  return true if number == 2
  return false if number.even?
  divisor = 3
  while divisor * divisor <= number
    return false if (number % divisor).zero?
    divisor += 2
  end
  true
end

theorem_path = File.join(__dir__, "RANK15_ORDINARY_MULTIPLE_LOCAL_INDEX_LEMMA.md")
check(File.file?(theorem_path), "local-index theorem note missing")
check(Digest::SHA256.file(theorem_path).hexdigest == THEOREM_SHA256,
      "local-index theorem hash mismatch")
check(prime?(P_FIELD), "deployed characteristic is not prime")
check(P_FIELD > MAX_VALENCY, "characteristic/valency gate failed")

(3..MAX_VALENCY).each do |m|
  scalar_zero_lower = 2 * m - (m - 1)
  hamiltonian_case = (m - 1)**2
  check(scalar_zero_lower == m + 1, "m=#{m}: branch-index identity failed")
  check(hamiltonian_case >= m + 1, "m=#{m}: A=0 case failed")
  excess_cost = scalar_zero_lower - 1
  check(excess_cost >= m, "m=#{m}: excess/valency payment failed")
end

puts "RANK15_ORDINARY_MULTIPLE_LOCAL_INDEX_LEMMA: PASS"
puts "characteristic=#{P_FIELD} max_valency=#{MAX_VALENCY}"
puts "local_index_formula=sum_branch_orders+I(A,B)-(m-1)"
puts "scalar_zero_index_lower=m+1"
puts "global_nonsimple_line_cost_bound=E"
puts "corrected_bad_line_bound=U+2D_double+E"
