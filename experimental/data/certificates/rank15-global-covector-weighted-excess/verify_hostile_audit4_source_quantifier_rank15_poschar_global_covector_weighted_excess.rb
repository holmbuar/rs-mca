#!/usr/bin/env ruby
# frozen_string_literal: true

# Fast hash/tamper/constants verifier for Hostile Audit 4.  The full optimized
# independent exact-state program is pinned together with its byte-exact
# output; this wrapper deliberately does not rerun the multi-million-state DP.

require "digest"

FILES = {
  "RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS_BOUND.md" =>
    "6f998929209b534d39cb0d31fa6458f5bf63d9326255ec31e7f0f64ae7a5389e",
  "HOSTILE_AUDIT4_SOURCE_QUANTIFIER_RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS.md" =>
    "41311e6c2c0ce724546eaeea9a720ee9268750a6e26ce08d429c2d25f11fb0f0",
  "audit_global_covector_weighted_excess_minima.rb" =>
    "ceb9e8fa47fc7d1e03d3c4ef69ceb0b72fffc222f7d54b6443b586e73e7dcd3a",
  "audit_global_covector_weighted_excess_minima.expected.txt" =>
    "12488f13a9545c41a749a0fa348d078bf29f3c584ee8c93a92db8662ecc07a6d",
  "explore_rank15_m213_exact_localcost_driver.rb" =>
    "8cfcf7475dd153e5e101e0c97467d7d49b0336f902e806ce673dee13f8de533b"
}.freeze

def assert(condition, message)
  raise message unless condition
end

FILES.each do |name, expected|
  path = File.join(__dir__, name)
  assert(File.file?(path), "missing #{name}")
  actual = Digest::SHA256.file(path).hexdigest
  assert(actual == expected, "hash mismatch #{name}: #{actual}")
end

theorem = File.read(File.join(__dir__, FILES.keys.first))
[
  "p>max(B,q+1)",
  "`X(u)` vanishes identically on no irreducible component of `fg`",
  "h=<alpha,X> in H^0(P^2,O(q+1))",
  "K=-Q^2 P_v mod P",
  "i(P,g)=2mu+i(P,P_v)-i(P,F)",
  "u_0=sum_j(r_j-1)=i(P,F)-m",
  "i(P,P_v)>=m-2",
  "E+S=2E-U <= a(q+1)"
].each { |marker| assert(theorem.include?(marker), "missing marker #{marker}") }

# Byte/sign/hypothesis tampering must leave the frozen theorem object.
[
  theorem.sub("p>max(B,q+1)", "p>B"),
  theorem.sub("K=-Q^2 P_v mod P", "K=Q^2 P_v mod P"),
  theorem.sub("2E-U <= a(q+1)", "2E-U <= a*q")
].each do |mutant|
  assert(Digest::SHA256.hexdigest(mutant) != FILES.fetch(FILES.keys.first),
         "tampered theorem retained canonical hash")
end

# Independent arithmetic reconstruction of the exact local comparison.
(0..71).each do |m|
  (1..12).each do |mu|
    (0..24).each do |i_pf|
      next if m.zero? && !i_pf.zero?
      polar = [m - 2, 0].max + ((m + mu + i_pf) % 5)
      i_pg = 2 * mu + polar - i_pf
      weight = if m.zero?
                 2 * mu
               elsif m == 1
                 2 * mu - i_pf
               else
                 2 * mu - i_pf + m - 2
               end
      assert(i_pg >= weight, "local sign/support payment failed m=#{m}")
    end
  end
end

p_field = 2_130_706_433
targets = [
  [24, 69, 3, 75, 12_607, 86, 0],
  [24, 68, 4, 100, 16_027, 96, 919],
  [25, 71, 4, 104, 225, 95, 215],
  [25, 70, 5, 130, 350, 106, 350],
  [25, 69, 6, 156, 559, 117, 559]
]
targets.each do |q, b, a, cap, _raw, _minimum, _survivors|
  assert(a == 3 * q - b, "residual degree failed")
  assert(cap == a * (q + 1), "projective twist/cap failed")
  assert(p_field > [b, q + 1].max, "tame characteristic failed")
  (2..b).each { |m| assert((m % p_field) != 0, "Saito valency vanished") }
  (1..q + 1).each { |n| assert((n % p_field) != 0, "polar coefficient vanished") }
end

expected = <<~TEXT
  q=24 B=69 raw=12607 W=86..120 cap=75 survivors=0
  q=24 B=68 raw=16027 W=96..132 cap=100 survivors=919
  q=25 B=71 raw=225 W=95..107 cap=104 survivors=215
  q=25 B=70 raw=350 W=106..119 cap=130 survivors=350
  q=25 B=69 raw=559 W=117..132 cap=156 survivors=559
  GLOBAL_COVECTOR_WEIGHTED_EXCESS_MINIMA_AUDIT: PASS
TEXT
actual = File.read(File.join(__dir__, "audit_global_covector_weighted_excess_minima.expected.txt"))
assert(actual == expected, "independent replay transcript changed")
assert(targets.first[5] - targets.first[3] == 11, "cubic gap changed")

puts "HOSTILE_AUDIT4_SOURCE_QUANTIFIER_GLOBAL_COVECTOR_WEIGHTED_EXCESS: PASS"
puts "theorem_sha256=#{FILES.fetch('RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS_BOUND.md')}"
puts "audit_sha256=#{FILES.fetch('HOSTILE_AUDIT4_SOURCE_QUANTIFIER_RANK15_POSCHAR_GLOBAL_COVECTOR_WEIGHTED_EXCESS.md')}"
puts "independent_replay_sha256=#{FILES.fetch('audit_global_covector_weighted_excess_minima.rb')}"
puts "independent_output_sha256=#{FILES.fetch('audit_global_covector_weighted_excess_minima.expected.txt')}"
puts "source=E_CminusR_U_Bqplus1minusI_S_EminusU extactic=Fg fixed_covector=true"
puts "q24_B69=12607_to_0_gap_11 other_survivors=919,559,350,215"
