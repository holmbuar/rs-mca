#!/usr/bin/env ruby
# frozen_string_literal: true

# Output-only exact diagnostic for the universal weighted covector bound
# E+S=U+2S <= a(q+1), a=3q-B.  This instruments, but does not modify, the
# source-locked M=213 exact-state enumeration.
#
# Usage: ruby FILE q low_B high_B

require "digest"

BASE_SHA256 =
  "8cfcf7475dd153e5e101e0c97467d7d49b0336f902e806ce673dee13f8de533b"

q_text, low_text, high_text = ARGV
raise "usage: #{File.basename($PROGRAM_NAME)} q low_B high_B" unless ARGV.length == 3
q_value = Integer(q_text, 10)
low_b = Integer(low_text, 10)
high_b = Integer(high_text, 10)
raise "requires a positive residual degree" unless low_b <= high_b && high_b < 3 * q_value

source_path = File.join(__dir__, "explore_rank15_m213_exact_localcost_driver.rb")
raise "source hash mismatch" unless File.file?(source_path) &&
  Digest::SHA256.file(source_path).hexdigest == BASE_SHA256

source = File.read(source_path)
source.sub!("q_value, low_b, high_b = ARGV.map(&:to_i)",
            "q_value, low_b, high_b = [#{q_value}, #{low_b}, #{high_b}]")
source.sub!("raise \"usage: #{'#{File.basename($PROGRAM_NAME)}'} q low_B high_B\" unless ARGV.length == 3",
            "# wrapper supplies the frozen q/B range")

initialization = <<~'RUBY'.chomp
  covector_weight = Hash.new do |hash, key|
    hash[key] = { raw: 0, survivors: 0, minimum: nil, maximum: nil }
  end
  outputs = []
RUBY
raise "initialization changed" unless source.sub!("outputs = []", initialization)

needle = "      check(excess == point_cap - residual_points,\n" \
         "            \"B=#{'#{b}'}: q#{'#{Q}'} excess identity failed\")"
replacement = needle + <<~'RUBY'

      weight = restriction_deficit + 2 * slack
      impact = covector_weight[b]
      impact[:raw] += 1
      impact[:minimum] = weight if impact[:minimum].nil? || weight < impact[:minimum]
      impact[:maximum] = weight if impact[:maximum].nil? || weight > impact[:maximum]
      impact[:survivors] += 1 if weight <= (3 * Q - b) * (Q + 1)
RUBY
raise "covector insertion changed" unless source.sub!(needle, replacement)

output_needle = "puts \"total_exact_states=#{'#{outputs.sum { |row| row[2] }}'}\""
output_replacement = <<~'RUBY'.chomp
  covector_weight.sort.each do |b, impact|
    a = 3 * Q - b
    puts "COVECTOR_WEIGHT B=#{b} a=#{a} cap=#{a * (Q + 1)} " \
         "raw=#{impact[:raw]} min=#{impact[:minimum]} max=#{impact[:maximum]} " \
         "survivors=#{impact[:survivors]}"
  end
  puts "total_exact_states=#{outputs.sum { |row| row[2] }}"
RUBY
raise "output insertion changed" unless source.sub!(output_needle, output_replacement)
source.sub!("nonclaim=branch_diagnostic_until_all_q_ranges_are_composed",
            "nonclaim=global_covector_weight_impact_diagnostic")

eval(source, TOPLEVEL_BINDING, source_path)
