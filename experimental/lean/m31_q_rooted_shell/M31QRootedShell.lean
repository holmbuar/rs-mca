import M31QRootedShell.Envelope
import M31QRootedShell.Deployed
import M31QRootedShell.ToyCounterexample
import M31QRootedShell.MultiplicativeCounterexample

/-- Temporary CI-only export used to recover the public coordination ledger for
an append-only update through the connector. Removed in the next commit. -/
#eval do
  IO.println "BEGIN_RS_MCA_AGENTS_LOG"
  IO.println (← IO.FS.readFile "../../agents-log.md")
  IO.println "END_RS_MCA_AGENTS_LOG"
