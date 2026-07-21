import Std

#eval do
  let contents ← IO.FS.readFile "../../agents-log.md"
  IO.println "AGENTS_LOG_BEGIN"
  IO.println contents
  IO.println "AGENTS_LOG_END"
