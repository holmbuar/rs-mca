import Std

/- Temporary export helper. Removed before handoff. -/
#eval do
  let text ← IO.FS.readFile "../../agents-log.md"
  IO.println "<<<RS_MCA_AGENTS_LOG_BEGIN>>>"
  IO.println text
  IO.println "<<<RS_MCA_AGENTS_LOG_END>>>"
