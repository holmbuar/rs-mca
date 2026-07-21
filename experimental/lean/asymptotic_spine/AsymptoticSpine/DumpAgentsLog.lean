import Std

/-! Temporary CI-only exporter used to make a byte-preserving agents-log append.
This file is removed before the packet is declared ready. -/

#eval do
  let text ← IO.FS.readFile "../../agents-log.md"
  IO.println "C8_AGENTS_LOG_BEGIN"
  IO.print text
  IO.println "C8_AGENTS_LOG_END"
