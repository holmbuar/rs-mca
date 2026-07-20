import Std

/- Temporary CI-only extraction helper. -/
namespace M31QRootedShell.DumpAgentsLog

#eval do
  let text ← IO.FS.readFile "../../agents-log.md"
  IO.println "BEGIN_AGENTS_LOG_DUMP"
  IO.println text
  IO.println "END_AGENTS_LOG_DUMP"

end M31QRootedShell.DumpAgentsLog
