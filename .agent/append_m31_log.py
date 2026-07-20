from pathlib import Path

path = Path("experimental/agents-log.md")
text = path.read_text(encoding="utf-8")
title = "### 2026-07-20 - Mersenne-31 rooted-shell Q reduction and support-only route counterexamples"

if title not in text:
    entry = """### 2026-07-20 - Mersenne-31 rooted-shell Q reduction and support-only route counterexamples

- **Agent/model:** GPT-5.6 Pro.
- **Files added or changed:** `experimental/notes/thresholds/m31_q_rooted_shell_envelope.md`, `experimental/notes/thresholds/m31_q_three_plus_seven_multiplicative_counterexample.md`, `experimental/data/certificates/m31-q-rooted-shell-envelope/`, `experimental/data/certificates/m31-q-3plus7-multiplicative-counterexample/`, `experimental/scripts/verify_m31_q_rooted_shell_envelope.py`, `experimental/scripts/verify_m31_q_three_plus_seven_multiplicative_counterexample.py`, `experimental/lean/m31_q_rooted_shell/`, and `experimental/agents-log.md`.
- **Status:** PROVED REDUCTION / EXACT ARITHMETIC / COUNTEREXAMPLE / OPEN DEPLOYED INPUT.
- **What is being added:** A rooted-shell summation compiler reduces the binding Mersenne-31 row-sharp Q atom to a local `3+7` shell inequality, with exact deployed list/MCA arithmetic and faithful finite route controls. A second packet gives a Lean-proved multiplicative-subgroup counterexample showing that support-level quotient/dihedral and planted-core pruning alone does not imply `3+7`; semantic slope ownership must enter the next theorem.
- **How it is useful:** The packet gives a precise sufficient closure interface, exact finite reserves, and mandatory regressions against both `2+7` and support-only `3+7` proof routes, while keeping support families distinct from actual first-match slope owners.
- **What to do next:** Prove the deployed semantic alternative `3+7 OR certified earlier slope owner`, preserving the received line, explanation state, first-match projector, natural profile scale, and exact slope budget. Do not claim row-sharp Q or an adjacent safe row from the reduction or finite controls alone.

"""
    anchor = "## Entries\n\n"
    if anchor not in text:
        raise SystemExit("agents-log entry anchor not found")
    path.write_text(text.replace(anchor, anchor + entry, 1), encoding="utf-8")

Path(".agent/append-m31-rooted-shell-log").unlink(missing_ok=True)
Path(__file__).unlink()
try:
    Path(".agent").rmdir()
except OSError:
    pass
